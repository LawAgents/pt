"""Generate COBERTURA.md and estatisticas.html from the front matter of the generated files.

Usage: python -I scripts/estatisticas.py --repo DIR --name "Legislação portuguesa" [--excluded excluded.json]

Only the front matter of each file is read (first 4 KB), so the numbers are exactly what is published.
estatisticas.html is one file: no server, no external script, no external font, dark mode included.
"""
import argparse
import collections
import html
import json
import os
import re
from datetime import date
from pathlib import Path

SKIP_DIRS = {".git", ".github", "docs", "config", "scripts", "__pycache__"}
STOP = set("""a as o os um uma uns umas de do da dos das em no na nos nas por para com sem sob sobre entre ate ao aos aa as e ou que se
 seu sua seus suas este esta estes estas esse essa isso mais menos ser sao foi pelo pela pelos pelas n art artigo artigos presente
 alteracao altera alterado alterada alterados revoga republica portuguesa lei decreto portaria regulamento diretiva europeu europeia
 parlamento conselho uniao ue ce cee euratom janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro
 dezembro dia dias ano anos 1 2 3 4 5 6 7 8 9 0 relativo relativa relativos relativas respeitante nos termos aprova estabelece
 define efeitos relevante texto comissao directiva eee anexo respeito refere respeita certas certos determinadas determinados procede cria
 protegidas restritivas""".split())


def fold(w):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", w) if unicodedata.category(c) != "Mn")


def front(path):
    with open(path, encoding="utf-8") as f:
        t = f.read(4000)
    if not t.startswith("---"):
        return None
    end = t.find("\n---", 3)
    meta = {}
    for ln in t[3:end if end > 0 else len(t)].splitlines():
        m = re.match(r'([a-z_]+): "?(.*?)"?$', ln)
        if m:
            meta[m.group(1)] = m.group(2)
    return meta


def scan(repo):
    acts, files, size = [], 0, 0
    for top in sorted(os.listdir(repo)):
        base = os.path.join(repo, top)
        if top in SKIP_DIRS or not os.path.isdir(base):
            continue
        for root, _, names in os.walk(base):
            for n in names:
                if not n.endswith(".md"):
                    continue
                p = os.path.join(root, n)
                files += 1
                size += os.path.getsize(p)
                meta = front(p)
                if meta and meta.get("id") and not meta.get("part_of"):
                    meta["_top"] = top
                    acts.append(meta)
    return acts, files, size


def words(acts, n=30):
    c = collections.Counter()
    for a in acts:
        text = a.get("summary") or a.get("title") or ""
        for w in re.findall(r"[^\W\d_]{4,}", text.lower()):
            if fold(w) not in STOP:
                c[w] += 1
    return c.most_common(n)


def table(rows, head):
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join(["---"] + ["---:"] * (len(head) - 1)) + " |"]
    out += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return "\n".join(out)


def fmt(n):
    return f"{n:,}".replace(",", ".")


def bars(items, total=None, unit=""):
    top = max((v for _, v in items), default=1) or 1
    rows = []
    for k, v in items:
        rows.append(f'<div class="row"><span class="k">{html.escape(str(k))}</span>'
                    f'<span class="bar"><i style="width:{100 * v / top:.1f}%"></i></span><span class="v">{fmt(v)}{unit}</span></div>')
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--excluded", help="excluded.json of the raw cache (acts left out and why)")
    a = ap.parse_args()
    repo = Path(a.repo)
    acts, files, size = scan(repo)
    today = date.today().isoformat()
    by_type = collections.Counter(x.get("type", "?") for x in acts)
    by_ver = collections.Counter(x.get("text_version", "?") for x in acts)
    by_dec = collections.Counter((x.get("year") or "0000")[:3] + "0" for x in acts)
    by_year = collections.Counter(x.get("year", "?") for x in acts)
    by_issuer = collections.Counter(x["issuer"] for x in acts if x.get("issuer"))
    by_top = collections.Counter(x["_top"] for x in acts)
    revoked = 0
    rv = repo / "revogados.md"
    if rv.exists():
        revoked = sum(1 for ln in rv.read_text(encoding="utf-8").splitlines() if ln.startswith("- "))

    md = [f"# Cobertura: {a.name}", "",
          f"Números medidos nos cabeçalhos dos ficheiros publicados em {today}. Gerado por `scripts/estatisticas.py`.", "",
          f"- Atos em vigor: **{fmt(len(acts))}**, em {fmt(files)} ficheiros ({size / 1e6:.0f} MB sem compressão).",
          f"- Atos revogados listados em `revogados.md`: {fmt(revoked)}.", "",
          "## Por tipo de ato", "", table([(k, fmt(v)) for k, v in by_type.most_common()], ["Tipo", "Atos"]), "",
          "## Por versão do texto", "", table([(k, fmt(v)) for k, v in by_ver.most_common()], ["Texto", "Atos"]), "",
          "## Por década do ato", "", table([(k, fmt(v)) for k, v in sorted(by_dec.items())], ["Década", "Atos"]), ""]
    if by_issuer:
        md += ["## Por entidade emissora (as 20 maiores)", "",
               table([(k, fmt(v)) for k, v in by_issuer.most_common(20)], ["Entidade", "Atos"]), ""]
    md += ["## Por pasta", "", table([(k, fmt(v)) for k, v in by_top.most_common()], ["Pasta", "Atos"]), ""]
    if a.excluded:
        ex = json.loads(Path(a.excluded).read_text(encoding="utf-8"))
        why = collections.Counter(e.get("reason", "?") for e in ex)
        md += ["## O que ficou de fora e porquê", "",
               f"{fmt(len(ex))} atos foram avaliados e não entraram:", "",
               table([(k, fmt(v)) for k, v in why.most_common()], ["Motivo", "Atos"]), ""]
    md += ["Para ver em gráficos, abre `estatisticas.html` no navegador.", ""]
    (repo / "COBERTURA.md").write_text("\n".join(md), encoding="utf-8")

    decs = sorted(by_dec.items())
    page = f"""<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Estatísticas: {html.escape(a.name)}</title>
<style>
:root{{--bg:#fff;--fg:#1a1a1a;--mut:#666;--bar:#2a5db0;--trk:#e8ecf3}}
@media (prefers-color-scheme:dark){{:root{{--bg:#14161a;--fg:#e8e8e8;--mut:#9aa0aa;--bar:#6b9be8;--trk:#252a33}}}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif}}
main{{max-width:880px;margin:0 auto;padding:24px 16px}}
h1{{font-size:1.6rem;margin:0 0 4px}}h2{{font-size:1.1rem;margin:32px 0 8px}}p{{color:var(--mut);margin:4px 0}}
.kpis{{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}}.kpi{{background:var(--trk);border-radius:8px;padding:10px 16px}}
.kpi b{{display:block;font-size:1.5rem}}
.row{{display:grid;grid-template-columns:minmax(120px,38%) 1fr 70px;gap:8px;align-items:center;margin:3px 0}}
.k{{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.bar{{background:var(--trk);height:14px;border-radius:7px;overflow:hidden}}
.bar i{{display:block;height:100%;background:var(--bar)}}.v{{text-align:right;color:var(--mut);font-variant-numeric:tabular-nums}}
.cols{{display:flex;align-items:flex-end;gap:6px;height:180px;margin-top:8px}}.col{{flex:1;text-align:center;font-size:12px}}
.col i{{display:block;background:var(--bar);border-radius:4px 4px 0 0}}.col span{{display:block;color:var(--mut)}}
@media (max-width:520px){{.row{{grid-template-columns:1fr 1fr 60px}}}}
</style></head><body><main>
<h1>{html.escape(a.name)}</h1>
<p>Números medidos nos cabeçalhos dos ficheiros publicados em {today}. Texto sem valor legal: confirma sempre na fonte oficial.</p>
<div class="kpis"><div class="kpi"><b>{fmt(len(acts))}</b>atos em vigor</div><div class="kpi"><b>{fmt(files)}</b>ficheiros</div>
<div class="kpi"><b>{size / 1e6:.0f} MB</b>de texto</div><div class="kpi"><b>{len(by_type)}</b>tipos de ato</div></div>
<h2>Por tipo de ato</h2>
{bars(by_type.most_common(15))}
<h2>Por década do ato</h2>
<div class="cols">{''.join(f'<div class="col"><span>{fmt(v)}</span><i style="height:{150 * v / max(by_dec.values()):.0f}px"></i>{k}</div>' for k, v in decs)}</div>
<h2>Por versão do texto</h2>
{bars(by_ver.most_common())}
{('<h2>Por entidade emissora</h2>' + bars(by_issuer.most_common(15))) if by_issuer else ''}
<h2>Palavras mais frequentes nos sumários e títulos</h2>
{bars(words(acts))}
<h2>Anos com mais atos</h2>
{bars(by_year.most_common(12))}
</main></body></html>
"""
    (repo / "estatisticas.html").write_text(page, encoding="utf-8")
    print(f"{len(acts)} acts, {files} files -> COBERTURA.md, estatisticas.html")


if __name__ == "__main__":
    main()
