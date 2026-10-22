"""Shared constants and helpers for the leis-pt pipeline (standard library only)."""
import json
import re
from pathlib import Path

VERSION = "0.1.0"
REPO_URL = "https://github.com/LawAgents/pt"
USER_AGENT = f"LawAgents-pt/{VERSION} (+{REPO_URL})"
SITE = "https://diariodarepublica.pt"

# Fixed notice, CONTENT.xml#str.legal_notice (pt-PT, on purpose: it is data shown to users).
LEGAL_NOTICE = ("Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. "
                "Não substitui aconselhamento jurídico.")

STATUS_IN_FORCE = "em vigor"
TEXT_CONSOLIDATED = "consolidado"
TEXT_ORIGINAL = "original sem alterações"
# Curated diploma (config/extras.txt) that the DRE never consolidated: original text, may have been amended since.
TEXT_EXTRA = "original sem consolidação"
TEXT_VERSIONS = (TEXT_CONSOLIDATED, TEXT_ORIGINAL, TEXT_EXTRA)
# Body line right after the title of a TEXT_EXTRA file (pt-PT on purpose: it is data shown to users).
EXTRA_NOTICE = "Texto original, sem consolidação: pode ter sido alterado depois."

# Front matter fields in file order (SCHEMA.xml#table.diploma_file).
FIELDS = ["id", "dre_id", "title", "type", "number", "year", "date", "issuer", "status", "text_version",
          "last_amended", "source", "eli", "original_pdf", "retrieved", "summary", "legal_notice",
          "part_of", "part"]
REQUIRED = ["id", "dre_id", "title", "type", "year", "date", "status", "text_version", "source",
            "retrieved", "legal_notice"]
DATE_FIELDS = {"date", "last_amended", "retrieved"}
INT_FIELDS = {"year"}
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REVOKED_MARK = "*(Revogado)*"


def format_frontmatter(meta):
    """Flat `key: value` lines; strings JSON-quoted (valid YAML), dates bare ISO, year an integer."""
    lines = ["---"]
    for k in FIELDS:
        v = meta.get(k)
        if v is None or v == "":
            continue
        if k in INT_FIELDS:
            lines.append(f"{k}: {int(v)}")
        elif k in DATE_FIELDS:
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {json.dumps(str(v), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def parse_frontmatter(text):
    """Return (dict, body). Raises ValueError when there is no well-formed front matter."""
    if not text.startswith("---\n"):
        raise ValueError("missing front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        if text.endswith("\n---"):
            end = len(text) - 4
        else:
            raise ValueError("unterminated front matter")
    meta = {}
    for ln in text[4:end].split("\n"):
        if not ln.strip():
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", ln)
        if not m:
            raise ValueError(f"bad front matter line: {ln!r}")
        k, v = m.group(1), m.group(2).strip()
        if v.startswith('"'):
            v = json.loads(v)
        elif re.fullmatch(r"-?\d+", v):
            v = int(v)
        meta[k] = v
    return meta, text[end + 5:]


def read_frontmatter(path):
    """Front matter of a file reading only its head (the files can be large)."""
    with open(path, "r", encoding="utf-8") as fh:
        head = fh.read(8192)
    return parse_frontmatter(head if "\n---\n" in head else Path(path).read_text(encoding="utf-8"))[0]


def split_articles(body):
    """List of (heading_text, body_text) for every article heading in a markdown body.

    An article ends at the next heading of any level (SCHEMA constraint.article_heading)."""
    heads = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"^#{1,6}[ \t].*$", body, re.M)]
    out = []
    for i, (s, e, line) in enumerate(heads):
        text = line.lstrip("#").strip()
        if not re.match(r"^Artigo\s", text):
            continue
        nxt = heads[i + 1][0] if i + 1 < len(heads) else len(body)
        out.append((text, body[e:nxt].strip()))
    return out


def article_number(heading_text):
    """'Artigo 483.º-A (Epígrafe)' -> '483.º-A'. None when the heading is not an article heading."""
    m = re.match(r"^Artigo\s+(\S+)", heading_text)
    if not m:
        return None
    return m.group(1).rstrip("—-–:")


def atomic_write(path, data, binary=False):
    """Write via tmp + rename so a reader never sees a partial file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    if binary:
        tmp.write_bytes(data)
    else:
        tmp.write_text(data, encoding="utf-8", newline="\n")
    tmp.replace(path)


def load_act_types(path):
    """Closed act-type list (one per line; blank lines and '#' comments ignored)."""
    types = []
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            types.append(ln)
    return types


# ---- repo layout ----------------------------------------------------------------------------------------

TYPE_DIRS = {
    "Lei": "leis",
    "Lei Orgânica": "leis-organicas",
    "Lei Constitucional": "leis-constitucionais",
    "Decreto-Lei": "decretos-lei",
    "Decreto Legislativo Regional": "decretos-legislativos-regionais",
    "Decreto Regulamentar": "decretos-regulamentares",
    "Decreto Regulamentar Regional": "decretos-regulamentares-regionais",
    "Decreto": "decretos",
    "Decreto do Presidente da República": "decretos-presidente-republica",
    "Portaria": "portarias",
    "Resolução do Conselho de Ministros": "resolucoes-conselho-ministros",
    "Resolução da Assembleia da República": "resolucoes-assembleia-republica",
    "Despacho Normativo": "despachos-normativos",
    "Despacho": "despachos",
    "Aviso": "avisos",
    "Declaração": "declaracoes",
}
# Top-level folders written by the pipeline; everything else in the repo is never touched.
OWNED_DIRS = sorted(set(TYPE_DIRS.values()) | {"codigos", "constituicao", "outros"})
ROOT_INDEX = re.compile(r"^(nomes-comuns|indice(-.*)?|revogados)\.md$")


def iter_owned_files(root):
    """Every markdown file of the pipeline-owned folders under root, sorted."""
    root = Path(root)
    for d in OWNED_DIRS:
        if (root / d).is_dir():
            yield from sorted((root / d).rglob("*.md"))


def main_files(root):
    """Front matter dicts (plus 'path') of the main/overview files, i.e. those that are not a part of another file."""
    out = []
    for p in iter_owned_files(root):
        try:
            meta = read_frontmatter(p)
        except (ValueError, OSError):
            continue
        if not meta.get("part_of"):
            meta["path"] = Path(p).relative_to(root).as_posix()
            out.append(meta)
    return out
