#!/usr/bin/env python3
"""Download the consolidated legislation of the Diario da Republica into a raw cache outside the repo.

  python scripts/fetch.py --mode initial|weekly --raw DIR [--budget-seconds N]

Raw cache layout (DIR):
  list.json            search list of the current cycle (every diploma with a public consolidation, plus the
                       curated config/extras.txt diplomas, flagged "extra": true)
  codigos.json         the "Legislacao por codigo" page (main codes, with acronyms)
  json/<dbId>.json.gz  one record per diploma: {"search", "frag", "url", "data", "original", "fetched"}
  cycle.json           progress of the current cycle, so an interrupted run resumes without repeating work

Modes
  initial  list + every in-force diploma that has no up-to-date record in the cache.
  weekly   a new cycle: list + one consolidated-text request per in-force diploma (the search list carries no
           last-consolidation date, so amendments can only be seen in the text itself); the extra requests
           (metadata, original text) are made only for new or changed diplomas.
Exit codes: 0 done, 1 aborted (3 consecutive errors, HTTP 429/503 or the site changed), 2 time budget reached.
"""
import argparse
import gzip
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import atomic_write  # noqa: E402
from dre_client import DRE, FetchAborted, SITE  # noqa: E402

FILTERS = [("docType_facet.keyword", "LEGISLACAO"), ("consolidacaoVisibility", "PUBLIC")]
# List fields that, when they change, make an already cached diploma stale.
SIGNAL_KEYS = ("consolidacaoEstado", "vigencia", "DiplomaFragmentadoId", "title", "numero", "ano")
STOP_WORDS = {"de", "do", "da", "dos", "das"}
SAVE_EVERY = 25


def tipo_slug(tipo):
    """DRE URL slug of an act type: 'Decreto do Presidente da República' -> 'decreto-presidente-republica'."""
    s = unicodedata.normalize("NFKD", tipo).encode("ascii", "ignore").decode().lower()
    return "-".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in STOP_WORDS)


def selected(src):
    """In force: public consolidation, not revoked / expired / not in force / lapsed."""
    if src.get("consolidacaoEstado") in ("REVOKED", "EXPIRED"):
        return False
    return src.get("vigencia") not in ("NAO_VIGENTE", "CADUCADO")


class ExtrasError(Exception):
    """config/extras.txt cannot be used (bad line, unresolved, ambiguous, not in force). Nothing is guessed."""


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---- raw cache -------------------------------------------------------------------------------

class Raw:
    def __init__(self, path):
        self.dir = Path(path)
        (self.dir / "json").mkdir(parents=True, exist_ok=True)

    def rec_path(self, db_id):
        return self.dir / "json" / f"{db_id}.json.gz"

    def read(self, db_id):
        p = self.rec_path(db_id)
        if not p.exists():
            return None
        try:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return None  # damaged file: treated as missing and fetched again

    def write(self, db_id, rec):
        data = gzip.compress(json.dumps(rec, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 6, mtime=0)
        atomic_write(self.rec_path(db_id), data, binary=True)

    def read_json(self, name, default=None):
        p = self.dir / name
        if not p.exists():
            return default
        return json.loads(p.read_text(encoding="utf-8"))

    def write_json(self, name, obj):
        atomic_write(self.dir / name, json.dumps(obj, ensure_ascii=False, separators=(",", ":")))


# ---- curated extras (diplomas the DRE does not consolidate) -----------------------------------------

EXTRA_LINE = re.compile(r"^(\d+(?:-[A-Za-z])?)/(\d{4})$")


def parse_extras(path):
    """[(line number, tipo, numero, ano, nota)] from lines `tipo | numero/ano | nota`; blanks and '#' lines ignored."""
    rows = []
    for n, ln in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        cells = [c.strip() for c in ln.split("|")]
        m = EXTRA_LINE.match(cells[1]) if len(cells) >= 2 else None
        if not cells[0] or not m:
            raise ExtrasError(f"{path}:{n}: expected `tipo | numero/ano | nota`, got {ln!r}")
        rows.append((n, cells[0], m.group(1), m.group(2), cells[2] if len(cells) > 2 else ""))
    return rows


def resolve_extras(dre, path, listed_ids, log=lambda m: None):
    """DRE search records (flagged extra=True) for the lines of `path` that are not already in the normal list.
    Raises ExtrasError, with the line number, for a line that matches no record, more than one, or a diploma that is
    not in force."""
    out = []
    for n, tipo, num, ano, _ in parse_extras(path):
        hits, start = [], 0
        while True:  # filters by type and year; the exact number is matched here, so no text search is trusted
            r = dre.search([("docType_facet.keyword", "LEGISLACAO"), ("tipo_facet.keyword", tipo), ("ano", ano)], start, 500)
            page = [h["_source"] for h in r["hits"]["hits"]]
            hits += page
            start += 500
            if not page or start >= r["hits"]["total"]["value"]:
                break
        found = {h["dbId"]: h for h in hits if h.get("tipo") == tipo and str(h.get("ano")) == ano
                 and (h.get("numero") or "").split("/")[0].strip() == num}
        if len(found) != 1:
            raise ExtrasError(f"{path}:{n}: {tipo} {num}/{ano} matches {len(found)} DRE records (need exactly 1)")
        src = next(iter(found.values()))
        if src["dbId"] in listed_ids:
            log(f"extras line {n}: {tipo} {num}/{ano} is consolidated, the consolidated text wins")
            continue
        if not selected(src) or src.get("vigencia") not in (None, "", "VIGENTE"):
            raise ExtrasError(f"{path}:{n}: {tipo} {num}/{ano} is not in force at the DRE "
                              f"(vigencia {src.get('vigencia')!r}, state {src.get('consolidacaoEstado')!r})")
        out.append(dict(src, extra=True))
    return out


# ---- DRE calls ---------------------------------------------------------------------------------

def fetch_list(dre, size=100, log=print):
    out, start = [], 0
    while True:
        r = dre.search(FILTERS, start, size)
        hits, total = r["hits"]["hits"], r["hits"]["total"]["value"]
        out += [h["_source"] for h in hits]
        log(f"list: {len(out)}/{total}")
        if not hits or len(out) >= total:
            break
        start += size
    seen, uniq = set(), []
    for s in out:
        if s["dbId"] not in seen:
            seen.add(s["dbId"])
            uniq.append(s)
    if len(uniq) != total:
        log(f"WARNING: {len(uniq)} unique diplomas for a total of {total}")
    return uniq


def original_keys(src):
    """Candidate DRE detail-page keys of an act's original text, most likely first."""
    num, ano, dbid = (src.get("numero") or "").strip(), str(src.get("ano") or ""), src["dbId"]
    norm = lambda s: re.sub(r"[^0-9A-Za-z]+", "-", s).strip("-").lower()  # noqa: E731
    keys = []
    if num:
        n = norm(num)
        keys.append(f"{n}-{dbid}")
        m = re.match(r"^(.*)/(\d{2})$", num)
        if m and ano.endswith(m.group(2)):
            keys.append(f"{norm(m.group(1))}-{ano}-{dbid}")
        elif "/" not in num and ano:
            keys.append(f"{n}-{ano}-{dbid}")
        m = re.match(r"^(.+?/\d{4})/.+$", num)
        if m:
            keys.append(f"{norm(m.group(1))}-{dbid}")
        m = re.match(r"^(.+?)/(\d{2})/.+$", num)
        if m and ano.endswith(m.group(2)):
            keys.append(f"{norm(m.group(1))}-{ano}-{dbid}")
    keys.append(f"{ano}-{dbid}")
    return list(dict.fromkeys(keys))


def fetch_original(dre, src):
    tipo = tipo_slug(src.get("tipo") or "")
    for k in original_keys(src):
        r = dre.original_detail(tipo, k)
        dc = r.get("DetalheConteudo") or {}
        if r.get("IsVisible") and str(dc.get("Id")) == str(src["dbId"]):
            dc["url"] = f"{SITE}/dr/detalhe/{tipo}/{k}"
            return dc
    return None


def fetch_diploma(dre, src, cached=None, with_eli=False):
    """Raw record of one diploma. Metadata and original text are reused from `cached` when the text did not change.
    with_eli=False skips the metadata request (one request fewer per diploma) and with it the ELI link."""
    data = dre.consolidated(src["dbId"])
    if cached and cached.get("data") == data:
        rec = dict(cached)
        rec["search"] = src
        return rec, False
    rec = {"search": src, "frag": None, "data": data}
    frag_id = src.get("DiplomaFragmentadoId")
    if frag_id:
        key = f"{src['ano']}-{frag_id}"
        url = f"{SITE}/dr/legislacao-consolidada/{tipo_slug(src['tipo'])}/{key}"
        if with_eli:
            fi = dre.frag_detail(tipo_slug(src["tipo"]), key, frag_id)
            if not fi.get("IsSitemapErro"):
                rec["frag"] = fi["ConsolidadaConteudoDetalhe"]
                rec["url"] = url
        else:
            rec["url"] = url
    if not data["LegConsBase"]["List"]:
        rec["original"] = fetch_original(dre, src)
        if src.get("extra"):
            vig = (rec["original"] or {}).get("Vigencia")
            if not rec["original"] or vig not in (None, "", "VIGENTE"):
                raise ExtrasError(f"extras: dbId {src['dbId']} has no original text or is not in force (Vigencia {vig!r})")
    rec["fetched"] = now_iso()
    return rec, True


def usable(rec):
    return bool(rec) and (rec["data"]["LegConsBase"]["List"] or rec.get("original"))


def up_to_date(rec, src):
    return usable(rec) and all(rec["search"].get(k) == src.get(k) for k in SIGNAL_KEYS)


# ---- diplomas that left force ----------------------------------------------------------------------

def revocation_date(data):
    """When a diploma stopped being in force. The search list has no such date, so it is read from the root fragment of
    the diploma's own text: 'em vigor a partir de YYYY-MM-DD' in the revocation note, else the date of the revoking act.
    Returns (iso date or '', source label)."""
    for x in data.get("LegConsBase", {}).get("List", []):
        if int(x.get("Nivel") or 0) == 0 and x["FragmentoVersao"].get("VersaoEstadoId") == 4:
            c = x["ConsolidacaoFragmento"]
            m = re.search(r"em vigor a partir de (\d{4}-\d{2}-\d{2})", c.get("AssociacaoDescription") or "")
            if m:
                return m.group(1), "note"
            if re.match(r"\d{4}-\d{2}-\d{2}", c.get("DataVersao") or "") and not (c["DataVersao"]).startswith("1900"):
                return c["DataVersao"][:10], "version"
    return "", ""


def fetch_revocations(dre, raw, left, today, log=lambda m: None):
    """For diplomas that left force (repo files whose dre_id is no longer in force) write raw/revoked/<dbId>.json with
    the revocation date. `left`: iterable of dre ids. Falls back to the detection date when the DRE gives none."""
    out = raw.dir / "revoked"
    for dbid in sorted(left, key=int):
        p = out / f"{dbid}.json"
        if p.exists():
            continue
        date, how = revocation_date(dre.consolidated(dbid))
        atomic_write(p, json.dumps({"dbId": str(dbid), "date": date or today, "date_source": how or "detected"}))
        log(f"revoked {dbid}: {date or today} ({how or 'detected'})")


# ---- driver ------------------------------------------------------------------------------------

def run_fetch(dre, raw, mode, budget_seconds=None, clock=time.monotonic, log=lambda m: print(m, file=sys.stderr),
              with_eli=False, workers=1, extras=None):
    """Run (or resume) a fetch cycle. Returns the exit code 0, 1 or 2. `extras`: path of config/extras.txt; its
    diplomas are added to the cycle's list (ExtrasError is raised before anything is written)."""
    t0 = clock()
    try:
        state = raw.read_json("cycle.json")
        if state and not state.get("complete") and state.get("mode") == mode and (raw.dir / "list.json").exists():
            log(f"resuming cycle started {state['started']} ({len(state['done'])} diplomas done)")
            lst = raw.read_json("list.json")
        else:
            lst = fetch_list(dre, log=log)
            if extras and Path(extras).exists():
                lst += resolve_extras(dre, extras, {s["dbId"] for s in lst}, log)
            codes = dre.codigos()
            raw.write_json("list.json", lst)
            raw.write_json("codigos.json", codes)
            state = {"mode": mode, "started": now_iso(), "complete": False, "done": []}
            raw.write_json("cycle.json", state)
        done = set(state["done"])
        todo = [s for s in lst if selected(s) and s["dbId"] not in done]
        if mode == "initial":
            todo = [s for s in todo if not up_to_date(raw.read(s["dbId"]), s)]
        log(f"{len(todo)} diplomas to fetch")
        n_new = n_same = 0
        def work(src):
            cached = raw.read(src["dbId"]) if mode == "weekly" else None
            return src, fetch_diploma(dre, src, cached if usable(cached) else None, with_eli)

        # Batches keep the budget check and the progress saves; inside a batch up to `workers` diplomas are in flight
        # (the client still starts at most one request per interval in total).
        batch = workers
        pool = ThreadPoolExecutor(max_workers=workers)
        try:
            for b0 in range(0, len(todo), batch):
                if budget_seconds is not None and clock() - t0 >= budget_seconds:
                    state["done"] = sorted(done)
                    raw.write_json("cycle.json", state)
                    log(f"time budget reached after {b0} diplomas; run again to resume")
                    return 2
                for src, (rec, changed) in pool.map(work, todo[b0:b0 + batch]):
                    raw.write(src["dbId"], rec)
                    done.add(src["dbId"])
                    n_new += changed
                    n_same += not changed
                if (b0 // batch + 1) % max(1, SAVE_EVERY // batch) == 0:
                    state["done"] = sorted(done)
                    raw.write_json("cycle.json", state)
                    log(f"{min(b0 + batch, len(todo))}/{len(todo)}")
        finally:
            pool.shutdown(wait=True, cancel_futures=True)
        state["done"] = sorted(done)
        state["complete"] = True
        raw.write_json("cycle.json", state)
        log(f"fetch done: {n_new} new or changed, {n_same} unchanged, {dre.requests} requests this run")
        return 0
    except FetchAborted as e:
        log(f"FETCH ABORTED: {e}")
        return 1


def left_force_ids(raw, repo):
    """dre ids of main files in the repo whose diploma is no longer in force according to the raw list."""
    from common import TEXT_EXTRA, main_files
    sel = {str(s["dbId"]) for s in raw.read_json("list.json", []) if selected(s)}
    # an extras diploma dropped from config/extras.txt just leaves the repo: it was never shown to be revoked
    kept = {str(m["dre_id"]) for m in main_files(repo) if m.get("dre_id") and m.get("text_version") != TEXT_EXTRA}
    return sorted(kept - sel, key=int)


def run_revocations(dre, raw, repo, log=lambda m: print(m, file=sys.stderr)):
    try:
        fetch_revocations(dre, raw, left_force_ids(raw, repo), datetime.now(timezone.utc).strftime("%Y-%m-%d"), log)
        return 0
    except FetchAborted as e:
        log(f"FETCH ABORTED: {e}")
        return 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--mode", choices=["initial", "weekly"], required=True)
    ap.add_argument("--raw", required=True, help="raw cache directory (outside the repo)")
    ap.add_argument("--budget-seconds", type=float, default=None,
                    help="stop gracefully after this many seconds (exit code 2); a later run resumes")
    ap.add_argument("--workers", type=int, default=8,
                    help="diplomas in flight at once; the total start rate stays at most 2 requests per second")
    ap.add_argument("--eli", action="store_true",
                    help="also ask for the per-diploma metadata (ELI link): one more request per diploma")
    ap.add_argument("--extras", default=None, help="curated list of diplomas the DRE does not consolidate (config/extras.txt)")
    ap.add_argument("--repo", default=None,
                    help="current repo: diplomas in it that are no longer in force get their revocation date fetched")
    a = ap.parse_args(argv)
    dre, raw = DRE(), Raw(a.raw)
    rc = run_fetch(dre, raw, a.mode, a.budget_seconds, with_eli=a.eli, workers=a.workers, extras=a.extras)
    if rc == 0 and a.repo:
        rc = run_revocations(dre, raw, a.repo)
    return rc


if __name__ == "__main__":
    sys.exit(main())
