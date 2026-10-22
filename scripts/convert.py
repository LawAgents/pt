#!/usr/bin/env python3
"""Convert the raw DRE JSON cache (fetch.py) into markdown files in the repo layout.

  python scripts/convert.py --raw DIR --out DIR [--repo DIR] [--max-part-kb 250]

Layout (SCHEMA.xml constraints article_heading, code_layout, part_id_format):
  leis/1996/lei-24-1996.md                    one file per diploma, `{type folder}/{year}/{id}.md`
  codigos/codigo-civil/{id}.md                codes: own folder, main file id = id of the approving act
  <dir>/{id}/{id}.md + {id}-{part}.md         a diploma split into parts: overview + one file per part
  constituicao/{id}.md                        the Constitution
Article numbers must be unique inside a file, so an approving decree and its annex (which repeat "Artigo 1.º")
go to different parts ("diploma-de-aprovacao" and the annex), and files above --max-part-kb are split by their
top-level structure (Livro, Parte, Titulo...).
"""
import argparse
import gzip
import html
import json
import re
import sys
import unicodedata
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (LEGAL_NOTICE, REVOKED_MARK, SITE, STATUS_IN_FORCE, TEXT_CONSOLIDATED, TEXT_EXTRA, TEXT_ORIGINAL,  # noqa: E402
                    EXTRA_NOTICE, TYPE_DIRS, article_number, atomic_write, format_frontmatter, main_files)
from fetch import tipo_slug, selected  # noqa: E402

CONSTITUTION_TYPE = "Decreto de Aprovação da Constituição"
CODE_TYPES = {"Lei", "Decreto-Lei", "Decreto Legislativo Regional", "Lei Orgânica"}
REVOKED_STATE = 4     # FragmentoVersao.VersaoEstadoId of a revoked fragment
ROOT_TYPE = 15        # the act itself (preamble)
ARTICLE_TYPE = 11
ANNEX_TYPE = 14
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
          "outubro", "novembro", "dezembro"]
DEFAULT_MAX_PART_BYTES = 70 * 1024  # readers (Read/WebFetch) cut files at about 100 KB


# ---- small text helpers ---------------------------------------------------------------------------

def slug(s, maxlen=90):
    s = re.sub(r"[ºª°]", "", s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].rstrip("-")


def plain(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


TAG_RE = re.compile(r"</?(?:br|a|u|span|div|p|b|i|strong|em|sup|sub|font|img|table|thead|tbody|tfoot|tr|td|th|col|"
                    r"colgroup|caption)\b[^>]*>", re.I)
TABLE_RE = re.compile(r"<table\b.*?</table>", re.I | re.S)


def table_to_md(t):
    """Simple HTML table -> markdown table; tables with spans or nesting stay as one-line HTML."""
    if re.search(r"(rowspan|colspan)\s*=\s*\"?\s*[2-9]", t, re.I) or re.search(r"<table\b[^>]*>.*<table", t[6:], re.I | re.S):
        return "\n\n" + re.sub(r"\s*\n\s*", " ", t) + "\n\n"
    rows = []
    for tr in re.findall(r"<tr\b.*?</tr>", t, re.I | re.S):
        cells = re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", tr, re.I | re.S)
        rows.append([inline(c).replace("\n", "<br>").replace("|", "\\|").strip() for c in cells])
    if not rows:
        return ""
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n\n" + "\n".join(out) + "\n\n"


def _link(m):
    href = re.search(r'href\s*=\s*"([^"]*)"', m.group(1))
    text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
    if href and href.group(1).strip():
        h = href.group(1).strip()
        if h.startswith("/"):
            h = SITE + h
        if h.startswith("http"):
            return f"[{text}]({h.replace(' ', '%20').replace(')', '%29')})"
    return text


def _img(m):
    src = m.group(1).strip()
    if src.startswith("data:"):
        return "\n*[imagem embutida não reproduzida — ver o PDF original]*\n"
    if src.startswith("/"):
        src = SITE + src
    return f"\n![]({src.replace(' ', '%20')})\n"


def inline(s):
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<a\b([^>]*)>(.*?)</a>", _link, s, flags=re.I | re.S)
    s = re.sub(r"<img\b[^>]*src\s*=\s*[\"']([^\"']+)[\"'][^>]*>", _img, s, flags=re.I)
    s = TAG_RE.sub("", s)
    if re.search(r"&(?:[a-z]+|#\d+|#x[0-9a-f]+);", s, re.I):
        s = html.unescape(s)
    return s


def escape_line(line):
    """A body line must never look like a heading or other block markup."""
    if re.match(r"^\s*(#|>|\+\s|\*|=+\s*$|-{3,}\s*$|_{3,}\s*$)", line):
        return "\\" + line.lstrip()
    return line


def body_text(t):
    if not t:
        return ""
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    parts, pos = [], 0
    for m in TABLE_RE.finditer(t):
        parts.append(("t", t[pos:m.start()]))
        parts.append(("table", m.group(0)))
        pos = m.end()
    parts.append(("t", t[pos:]))
    out = []
    for kind, chunk in parts:
        if kind == "table":
            out.append(table_to_md(chunk).strip("\n"))
            continue
        lines = [escape_line(re.sub(r"[ \t ]+", " ", ln).strip()) for ln in inline(chunk).split("\n")]
        lines = [ln for ln in lines if ln]
        if lines:
            out.append("\n\n".join(lines))
    return "\n\n".join(o for o in out if o)


def note_text(s):
    """DRE amendment note: '... [L]<a ...>Lei n.º X ...</a>[/L], em vigor ...'."""
    s = inline(s.replace("[L]", "").replace("[/L]", ""))
    return re.sub(r"\s+", " ", s).strip()


# ---- fragments -> items ---------------------------------------------------------------------------

class Item:
    """One rendered DRE fragment: a heading (optional) plus body, with its structure level."""
    __slots__ = ("level", "tipo", "label", "tituo", "md", "art", "size")

    def __init__(self, level, tipo, label, tituo, md):
        self.level, self.tipo, self.label, self.tituo, self.md = level, tipo, label, tituo, md
        self.art = article_number(label) if label.startswith("Artigo ") else None
        self.size = len(md.encode("utf-8")) + 2


def heading_label(f):
    t = (f.get("Tituo") or "").strip() or (f.get("Identificacao") or "").strip()
    e = (f.get("Epigrafe") or "").strip()
    if f.get("TipoFragmentoId") == ARTICLE_TYPE and t:
        if re.match(r"^\d+[.ºª°]*(-[A-Za-z]+)?$", t):
            t = "Artigo " + t  # DRE sometimes keeps only the bare number
        else:
            t = re.sub(r"^ARTIGO(?=\s|$)", "Artigo", t)
    if t and e:
        label = f"{t} {e}" if e.startswith("(") else f"{t} — {e}"
    else:
        label = t or e
    return re.sub(r"\s+", " ", label.replace("\n", " ")).strip()


def is_placeholder(f):
    """An 'Artigo .º' fragment with no number and no text (the DRE keeps one after an amendment): it holds no law, so it
    is neither written nor counted."""
    return bool(re.match(r"^Artigo\s*\.", heading_label(f))) and not body_text(f.get("Texto"))


def render_items(frags):
    items = []
    for x in frags:
        if x.get("IsHidden"):
            continue
        f, c = x["FragmentoVersao"], x["ConsolidacaoFragmento"]
        level = int(x.get("Nivel") or 0)
        if f.get("TipoFragmentoId") == ROOT_TYPE and level == 0:
            items.append(Item(0, ROOT_TYPE, "", "", body_text(f.get("Texto"))))
            continue
        if is_placeholder(f):
            continue
        label = heading_label(f)
        tituo = re.sub(r"\s+", " ", (f.get("Tituo") or f.get("Identificacao") or "").replace("\n", " ")).strip()
        h = level + 1
        blocks = []
        if label:
            if h <= 6:
                blocks.append("#" * h + " " + label)
            elif f.get("TipoFragmentoId") == ARTICLE_TYPE:
                blocks.append("###### " + label)
            else:
                blocks.append(f"**{label}**")
        if f.get("VersaoEstadoId") == REVOKED_STATE:
            desc = note_text(c.get("AssociacaoDescription") or "")
            blocks.append(REVOKED_MARK + (f" — *{desc}*" if desc else ""))
        else:
            txt = body_text(f.get("Texto"))
            if txt:
                blocks.append(txt)
            elif label.startswith("Artigo ") and re.search(r"\(\s*Revogad[oa]\.?\s*\)", label, re.I):
                blocks.append(REVOKED_MARK)  # the DRE marks the article as revoked in its heading only
            alts = [note_text(a) for a in (x.get("AlteracoesList") or {}).get("List", []) if a]
            if alts:
                blocks.append("\n".join(f"- *{a}*" for a in alts))
        items.append(Item(level, f.get("TipoFragmentoId"), label, tituo, "\n\n".join(blocks)))
    return items


def render_original_items(dc):
    """Original (as published) text of an act the DRE never consolidated: no structure in the data, so only
    lines that are exactly 'Artigo N.º' (as the DRE styles them) become article headings."""
    t = dc.get("TextoFormatado") or ""
    if not t.strip():
        txt = body_text(dc.get("Texto") or "")
        return [Item(0, ROOT_TYPE, "", "", txt)] if txt else []
    paras = re.findall(r"<p\b([^>]*)>(.*?)</p\s*>", t, flags=re.I | re.S)
    if not paras:
        return [Item(0, ROOT_TYPE, "", "", body_text(t))]
    items, i = [], 0
    pending = []
    while i < len(paras):
        attrs, inner = paras[i]
        text = plain(inner)
        if "center" in attrs and re.fullmatch(r"Artigo\s+\S+", text):
            if pending:
                items.append(Item(0, ROOT_TYPE, "", "", body_text("<br>".join(pending))))
                pending = []
            label = text
            if i + 1 < len(paras) and "bold-center-14px" in paras[i + 1][0] and plain(paras[i + 1][1]):
                e = plain(paras[i + 1][1])
                label = f"{text} ({e})" if not e.startswith("(") else f"{text} {e}"
                i += 1
            items.append(Item(1, ARTICLE_TYPE, label, text, f"## {label}"))
        else:
            pending.append(inner)
        i += 1
    if pending:
        items.append(Item(0 if not items else 1, ROOT_TYPE, "", "", body_text("<br>".join(pending))))
    # text after an article heading belongs to that article
    return items


def _article_fragments(rec):
    return [x for x in rec["data"]["LegConsBase"]["List"]
            if not x.get("IsHidden") and x["FragmentoVersao"].get("TipoFragmentoId") == ARTICLE_TYPE]


def dre_article_count(rec):
    """Number of articles the DRE data says the diploma has: article fragments whose heading is an 'Artigo ...'
    (None for original texts: no count in the data)."""
    if not rec["data"]["LegConsBase"]["List"]:
        return None
    # by heading, whatever the fragment type: the DRE sometimes files an inserted article (e.g. 'Artigo 9.º-A') under
    # another type; placeholders ('Artigo .º' with no text) are not articles
    return sum(1 for x in rec["data"]["LegConsBase"]["List"]
               if not x.get("IsHidden") and x["FragmentoVersao"].get("TipoFragmentoId") != ROOT_TYPE
               and heading_label(x["FragmentoVersao"]).startswith("Artigo ")
               and not is_placeholder(x["FragmentoVersao"]))


def dre_other_article_headings(rec):
    """Article fragments whose heading does not start with 'Artigo' (for example 'Base I'): kept as headings of their
    own but not counted as articles; the validator reports them as a warning."""
    if not rec["data"]["LegConsBase"]["List"]:
        return 0
    return sum(1 for x in _article_fragments(rec) if not heading_label(x["FragmentoVersao"]).startswith("Artigo "))


# ---- splitting into parts ---------------------------------------------------------------------------

def split_units(items, level):
    """Cut `items` into units that start at a heading of exactly `level`; lower-level lead items join the first."""
    units, cur, lead = [], None, []
    for it in items:
        if it.level == level:
            cur = [it]
            units.append(cur)
        elif cur is None:
            lead.append(it)
        else:
            cur.append(it)
    if lead:
        if units:
            units[0] = lead + units[0]
        else:
            units = [lead]
    return units


class Unit:
    """A run of consecutive items cut at one heading level: the atom that parts are packed from."""
    __slots__ = ("items", "annex", "level", "prefix", "size", "nums", "approval")

    def __init__(self, items, annex, level, prefix="", approval=False):
        self.items, self.annex, self.level, self.prefix = items, annex, level, prefix
        self.approval = approval  # belongs to the approving decree itself (comes before the first annex)
        self.size = sum(i.size for i in items)
        self.nums = [i.art for i in items if i.art]

    def head(self):
        """The heading this unit was cut at (lead items of a parent may come before it)."""
        for i in self.items:
            if i.level == self.level and i.label:
                return i
        return next((i for i in self.items if i.label), None)

    def name(self):
        h = self.head()
        if h is None:
            return ""
        if h.art is not None:
            return f"Artigo {h.art}"
        n = h.tituo or h.label
        return h.label if h.tipo == ANNEX_TYPE and h.label != n else n

    def end_label(self):
        return f"{self.prefix}, {self.name()}" if self.prefix and self.name() else (self.name() or self.prefix)


def pack(items, max_bytes):
    """Greedy packing of top-level units into parts: a part is closed when the next unit would make it exceed
    `max_bytes` or repeat an article number already in the part. Oversized units are opened up level by level
    (Livro > Titulo > Capitulo...). Returns a list of parts, each a list of Unit."""
    base = min((i.level for i in items if i.level > 0), default=1)
    queue = deque(Unit(u, any(i.tipo == ANNEX_TYPE and i.level == 1 for i in u[:2]), base) for u in split_units(items, base))
    first_annex = next((k for k, u in enumerate(queue) if u.annex), None)
    for k, u in enumerate(queue):
        u.approval = first_annex is not None and k < first_annex
    single_annex = sum(1 for u in queue if u.annex) <= 1  # a lone annex is the code itself: no need to name it in every part
    parts, cur, nums, size = [], [], set(), 0
    while queue:
        u = queue.popleft()
        if u.size > max_bytes:
            sub, lv = None, None
            for lv in sorted({i.level for i in u.items[1:] if i.level > u.level}):  # next level that really splits
                sub = split_units(u.items, lv)
                if len(sub) > 1:
                    break
            if sub and len(sub) > 1:
                parent = u.head()
                own = "" if parent is None or (single_annex and parent.tipo == ANNEX_TYPE) else (parent.tituo or parent.label)
                prefix = ", ".join(x for x in (u.prefix, own) if x)
                queue.extendleft(Unit(s, u.annex, lv, prefix, u.approval) for s in reversed(sub))
                continue
        clash = bool(set(u.nums) & nums) or len(set(u.nums)) != len(u.nums)
        if cur and (clash or size + u.size > max_bytes or cur[-1].approval != u.approval):
            parts.append(cur)
            cur, nums, size = [], set(), 0
        cur.append(u)
        nums |= set(u.nums)
        size += u.size
    parts.append(cur)
    return parts


def part_title(units, doc_has_annex):
    """Display title of a part from its units."""
    if all(u.approval for u in units):
        return "Diploma de aprovação"
    first, last = units[0], units[-1]
    if all(u.items and u.head() is not None and u.head().art is not None for u in units):
        arts = [u.head().art for u in units]
        pre = first.prefix + ", " if first.prefix else ""
        return fit(f"{pre}Artigo {arts[0]}" if len(arts) == 1 else f"{pre}Artigos {arts[0]} a {arts[-1]}")
    if len(units) == 1 or first.end_label() == last.end_label():
        name = first.end_label()
    else:
        # "X a Y": drop from Y the leading segments it shares with X (Livro I, Título II, Secção VI a Secção IX)
        c1 = [s for s in first.prefix.split(", ") if s] + [first.name()]
        c2 = [s for s in last.prefix.split(", ") if s] + [last.name()]
        common = 0
        while common < len(c1) - 1 and common < len(c2) - 1 and c1[common] == c2[common]:
            common += 1
        name = f"{', '.join(c1)} a {', '.join(c2[common:])}"
    return fit(name or "Texto")


def fit(name, limit=90):
    """Cut a long part title at a ', ' boundary (never mid-word) and mark the cut with an ellipsis."""
    name = name.strip()
    if len(name) <= limit:
        return name
    cut = name.rfind(", ", 0, limit - 1)
    if cut > 0:
        return name[:cut] + "…"
    cut = name.rfind(" ", 0, limit - 1)
    return name[:cut if cut > 0 else limit - 1] + "…"


def split_parts(items, max_bytes):
    """Returns [(title, items)]; one element means the diploma stays in one file."""
    packed = pack(items, max_bytes)
    if len(packed) == 1:
        return [("", [i for u in packed[0] for i in u.items])]
    has_annex = any(u.annex for p in packed for u in p)
    out, seen = [], {}
    for p in packed:
        t = part_title(p, has_annex).replace("|", "/")  # a pipe would break the overview table
        s = slug(t, 60) or "parte"
        seen[s] = seen.get(s, 0) + 1
        if seen[s] > 1:
            t = f"{t} ({seen[s]})"
        out.append((t, [i for u in p for i in u.items]))
    return out


def assemble(items):
    return "\n\n".join(i.md for i in items if i.md)


def outline(parts, max_depth=4):
    """Non-article headings of the whole diploma, in order, as a nested bullet list with the part file of each.
    parts: [(file name, items)]. Depth counts from the shallowest structural heading."""
    heads = [(i, name) for name, its in parts for i in its if i.label and i.art is None and i.level > 0]
    if not heads:
        return []
    base = min(i.level for i, _ in heads)
    return [f"{'  ' * (i.level - base)}- {i.label} ({name})" for i, name in heads if i.level - base < max_depth]


def article_range(items):
    arts = [i.art for i in items if i.art]
    if not arts:
        return "—"
    return arts[0] if len(arts) == 1 else f"{arts[0]} a {arts[-1]}"


# ---- ids and layout ---------------------------------------------------------------------------------

def base_id(src):
    """type-number-year[-region]; acts without a number: type-year-dre-<dbId> (RULES.xml#rule.id_format)."""
    typ, year, db = tipo_slug(src.get("tipo") or "") or "ato", str(src.get("ano") or (src.get("dataPublicacao") or "0000")[:4]), src["dbId"]
    num = (src.get("numero") or "").strip()
    if not slug(num):
        return f"{typ}-{year}-dre-{db}"
    toks = [t for t in num.split("/") if t.strip()]
    main, rest = toks[0], toks[1:]
    if rest and re.fullmatch(r"\d{2}|\d{4}", rest[0]):
        rest = rest[1:]
    region = ""
    if rest and rest[-1].strip().upper() in ("A", "M"):
        region = "-" + rest.pop().strip().lower()
    n = slug("-".join([main] + rest))
    return f"{typ}-{n}-{year}{region}"


def issuer_suffix(src):
    s = slug(src.get("emissor") or "", 200)
    words = [w for w in s.split("-") if w not in ("de", "do", "da", "dos", "das", "e")]
    out = ""
    for w in words:
        if len(out) + len(w) + 1 > 40:
            break
        out = f"{out}-{w}" if out else w
    return out


def assign_ids(entries, existing=None):
    """entries: list of search records. existing: {dbId: id} already in the repo (kept, ids never change).
    Colliding new ids get the issuer, then the DRE id as last resort. Returns {dbId: id}."""
    existing = dict(existing or {})
    ids = {}
    for e in entries:
        if e["dbId"] in existing:
            ids[e["dbId"]] = existing[e["dbId"]]
    taken = set(ids.values())
    todo = sorted((e for e in entries if e["dbId"] not in ids), key=lambda e: e["dbId"])
    groups = {}
    for e in todo:
        groups.setdefault(base_id(e), []).append(e)
    for b, grp in sorted(groups.items()):
        if len(grp) == 1 and b not in taken:
            ids[grp[0]["dbId"]] = b
            taken.add(b)
            continue
        for e in grp:
            sfx = issuer_suffix(e)
            cand = f"{b}-{sfx}" if sfx else None
            if not cand or cand in taken or sum(1 for g in grp if issuer_suffix(g) == sfx) > 1:
                cand = f"{b}-dre-{e['dbId']}"
            ids[e["dbId"]] = cand
            taken.add(cand)
    return ids


def short_title(src):
    t = re.split(r"\s+-\s+Di[áa]rio d", src.get("title") or "")[0]
    return re.sub(r"\s+", " ", t).strip()


def long_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return d, MONTHS[m - 1], y


def legible_title(src):
    base = short_title(src) or (src.get("tipo") or "").strip()
    iso = (src.get("dataPublicacao") or "")[:10]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", iso):
        return base
    d, mon, y = long_date(iso)
    if (src.get("numero") or "").strip():
        return f"{base}, de {d} de {mon}"
    return f"{base}, de {d} de {mon} de {y}"


def type_dir(tipo):
    return TYPE_DIRS.get(tipo) or f"outros/{tipo_slug(tipo) or 'sem-tipo'}"


def index_group(rel):
    """Index group of a repo path: first folder, or outros/<type>."""
    p = rel.split("/")
    return "/".join(p[:2]) if p[0] == "outros" else p[0]


class Act:
    def __init__(self, dre_id, act_id, files, parts, kind):
        self.dre_id, self.id, self.files, self.parts, self.kind = dre_id, act_id, files, parts, kind


def classify(rec, code_frag_ids):
    src = rec["search"]
    tipo = src.get("tipo") or ""
    frag = (rec.get("frag") or {}).get("DiplomaFrag") or {}
    desig = (frag.get("Designacao") or src.get("designacao") or "").strip()
    if tipo == CONSTITUTION_TYPE:
        return "constitution", desig
    is_code = str(src.get("DiplomaFragmentadoId") or "") in code_frag_ids or (
        tipo in CODE_TYPES and re.match(r"^C[óo]digos? ", desig))
    return ("code" if is_code else "act"), desig


def code_frag_ids_from(codigos):
    out = set()
    for c in codigos or []:
        m = re.search(r"-(\d+)$", c.get("LinkSiteMap") or "")
        if m:
            out.add(m.group(1))
    return out


def convert_record(rec, act_id, code_frag_ids, max_bytes=DEFAULT_MAX_PART_BYTES, code_dirs=None):
    """One raw record -> Act with its files [(relpath, text)]. Raises on unusable data."""
    src, data = rec["search"], rec["data"]
    orig = rec.get("original")
    frags = data["LegConsBase"]["List"]
    if not frags and not orig:
        raise ValueError("no text in the DRE data (neither consolidated nor original)")
    kind, desig = classify(rec, code_frag_ids)
    items = render_items(frags) if frags else render_original_items(orig)
    frag_meta = (rec.get("frag") or {}).get("DiplomaFrag") or {}
    eli = frag_meta.get("ELI") or ""
    if not re.search(r"/eli/.+", eli):
        eli = ""
    last = (data.get("DataUltimaConsolidada") or "")[:10]
    if not frags or last.startswith("1900") or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", last):
        last = ""
    title = legible_title(src)
    if kind == "code":
        name = re.sub(r"\s+-\s+[A-Z]{2,6}$", "", desig)
        title = f"{name} ({title})" if name else title
    elif kind == "constitution":
        title = "Constituição da República Portuguesa"
    year = int(src.get("ano") or (src.get("dataPublicacao") or "0")[:4])
    source = rec.get("url") or (orig or {}).get("url") or f"{SITE}/dr/detalhe/{tipo_slug(src.get('tipo') or '')}/{year}-{src['dbId']}"
    meta = {
        "id": act_id, "dre_id": str(src["dbId"]), "title": title, "type": src.get("tipo") or "",
        "number": (src.get("numero") or "").strip(), "year": year,
        "date": (src.get("dataPublicacao") or "")[:10], "issuer": (src.get("emissor") or "").strip(),
        "status": STATUS_IN_FORCE, "text_version": TEXT_CONSOLIDATED if frags else (TEXT_EXTRA if src.get("extra") else TEXT_ORIGINAL),
        "last_amended": last, "source": source, "eli": eli,
        "original_pdf": data.get("URLPDF") or (orig or {}).get("URL_PDF") or "",
        "retrieved": (rec.get("fetched") or "")[:10], "summary": plain(src.get("sumario")),
        "legal_notice": LEGAL_NOTICE,
    }
    parts = split_parts(items, max_bytes) if frags else [("", items)]
    if kind == "code":
        cname = slug(re.sub(r"\s+-\s+[A-Z]{2,6}$", "", desig)) or act_id
        base_dir = f"codigos/{cname}"
        if code_dirs is not None:
            if code_dirs.get(base_dir, src["dbId"]) != src["dbId"]:
                base_dir = f"{base_dir}-{src['dbId']}"
            code_dirs[base_dir] = src["dbId"]
        single, multi = base_dir, base_dir
    elif kind == "constitution":
        single, multi = "constituicao", f"constituicao/{act_id}"
    else:
        d = f"{type_dir(src.get('tipo') or '')}/{year}"
        single, multi = d, f"{d}/{act_id}"
    files = []
    if len(parts) == 1:
        body = assemble(parts[0][1])
        if meta["text_version"] == TEXT_EXTRA:
            body = EXTRA_NOTICE + ("\n\n" + body if body else "")
        meta["part_of"] = meta["part"] = ""
        files.append((f"{single}/{act_id}.md", format_frontmatter(meta) + f"\n\n# {title}\n\n" + (body + "\n" if body else "")))
        return Act(src["dbId"], act_id, files, [], kind)
    used, rows = set(), []
    for t, its in parts:
        pid = f"{act_id}-{slug(t, 60) or 'parte'}"
        while pid in used:
            pid += "-2"
        used.add(pid)
        pmeta = dict(meta, id=pid, title=f"{title} — {t}", part_of=act_id, part=t)
        body = assemble(its)
        files.append((f"{multi}/{pid}.md", format_frontmatter(pmeta) + f"\n\n# {pmeta['title']}\n\n" + (body + "\n" if body else "")))
        arts = [i.art for i in its if i.art]
        rows.append((t, f"{multi}/{pid}.md", arts[0] if arts else "", arts[-1] if arts else ""))
    ov = [f"# {title}", "",
          "Este diploma está dividido em partes. Cada parte é um ficheiro; os números de artigo são únicos dentro de cada ficheiro.",
          "", "| parte | caminho | primeiro artigo | último artigo |", "|---|---|---|---|"]
    ov += [f"| {t} | {path} | {a0} | {a1} |" for t, path, a0, a1 in rows]
    for depth in (4, 3, 2, 1):  # the overview must stay small: fewer levels when the outline is long
        out = outline([(Path(r[1]).name, its) for r, (_, its) in zip(rows, parts)], depth)
        if sum(len(x) + 1 for x in out) <= 45_000:
            break
    if out:
        ov += ["", "## Estrutura", ""] + out
    meta["part_of"] = meta["part"] = ""
    files.insert(0, (f"{multi}/{act_id}.md", format_frontmatter(meta) + "\n\n" + "\n".join(ov) + "\n"))
    return Act(src["dbId"], act_id, files, [Path(r[1]).stem for r in rows], kind)


# ---- driver ---------------------------------------------------------------------------------------------

def existing_ids(repo):
    """{dbId: id} of the diplomas already in the repo (main or overview files only)."""
    if not repo:
        return {}
    return {int(m["dre_id"]): m["id"] for m in main_files(repo) if m.get("dre_id")}


def convert_all(raw_dir, out_dir, repo=None, max_bytes=DEFAULT_MAX_PART_BYTES, log=lambda m: print(m, file=sys.stderr)):
    """Convert every in-force diploma of the raw cache. Returns (acts, errors). Writes nothing outside out_dir."""
    raw = Path(raw_dir)
    lst = json.loads((raw / "list.json").read_text(encoding="utf-8"))
    codigos = json.loads((raw / "codigos.json").read_text(encoding="utf-8")) if (raw / "codigos.json").exists() else []
    code_ids = code_frag_ids_from(codigos)
    sel = [s for s in lst if selected(s)]
    ids = assign_ids(sel, existing_ids(repo))
    acts, errors, code_dirs = [], [], {}
    for s in sorted(sel, key=lambda s: s["dbId"]):
        p = raw / "json" / f"{s['dbId']}.json.gz"
        try:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                rec = json.load(fh)
            act = convert_record(rec, ids[s["dbId"]], code_ids, max_bytes, code_dirs)
        except FileNotFoundError:
            errors.append({"dre_id": str(s["dbId"]), "error": "convert: no raw record (fetch incomplete)"})
            continue
        except Exception as e:  # noqa: BLE001  one bad diploma must not hide the others
            errors.append({"dre_id": str(s["dbId"]), "error": f"convert: {type(e).__name__}: {e}"})
            continue
        for rel, text in act.files:
            atomic_write(Path(out_dir) / rel, text)
        act.files = [(rel, "") for rel, _ in act.files]  # keep the paths only: the texts are on disk now
        acts.append(act)
    log(f"converted {len(acts)} diplomas, {len(errors)} errors")
    return acts, errors


def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert the raw DRE cache into markdown files.")
    ap.add_argument("--raw", required=True, help="raw cache directory written by fetch.py")
    ap.add_argument("--out", required=True, help="output directory (use an empty staging directory)")
    ap.add_argument("--repo", default=None, help="existing repo: ids already assigned there are kept")
    ap.add_argument("--max-part-kb", type=int, default=DEFAULT_MAX_PART_BYTES // 1024, help="split files above this size")
    a = ap.parse_args(argv)
    _, errors = convert_all(a.raw, a.out, a.repo, a.max_part_kb * 1024)
    for e in errors:
        print(f"ERROR {e['dre_id']}: {e['error']}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
