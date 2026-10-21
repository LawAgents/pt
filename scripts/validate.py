#!/usr/bin/env python3
"""Validate a tree of generated diploma files (RULES.xml rule.blocking_validation / rule.numbering_gaps_warning).

  python scripts/validate.py --root DIR --act-types config/act-types.txt [--raw DIR] [--json OUT]

Blocking errors (exit code 1): incomplete metadata, missing official link (source), missing dre_id, empty article,
type outside the closed list, article count different from the one in the DRE data, duplicate id, plus structural
errors in parts. Gaps in article numbering are warnings only. The JSON output is
{"errors": [{"code", "file", "dre_id", "message"}], "warnings": [...]}.
"""
import argparse
import gzip
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (DATE_FIELDS, ISO_DATE, REQUIRED, STATUS_IN_FORCE, TEXT_CONSOLIDATED, TEXT_ORIGINAL,  # noqa: E402
                    article_number, iter_owned_files, load_act_types, parse_frontmatter, split_articles)

ROW_RE = re.compile(r"^\|([^|\n]*)\|\s*([^|\n]+?\.md)\s*\|([^|\n]*)\|([^|\n]*)\|\s*$", re.M)
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NOTE_LINE = re.compile(r"^\s*-\s+\*.*\*\s*$")


def _issue(code, file, dre_id, message):
    return {"code": code, "file": file, "dre_id": dre_id, "message": message}


def number_gaps(numbers):
    """Pairs (previous, next) where the integer part of consecutive article numbers jumps by more than 1."""
    gaps, prev = [], None
    for n in numbers:
        m = re.match(r"(\d+)", n or "")
        if not m:
            continue
        cur = int(m.group(1))
        if prev is not None and cur > prev + 1:
            gaps.append((prev, cur))
        prev = cur
    return gaps


def article_empty(body):
    return not [ln for ln in body.splitlines() if ln.strip() and not NOTE_LINE.match(ln)]


def validate(root, act_types, expected_counts=None, other_headings=None):
    """Returns (errors, warnings). expected_counts: {dre_id: article count from the DRE data}."""
    errors, warnings = [], []
    root = Path(root)
    types = set(act_types)
    files = []  # (rel, meta, article numbers, headings of empty articles, overview body, has body text)
    for p in iter_owned_files(root):
        rel = p.relative_to(root).as_posix()
        try:
            meta, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        except (ValueError, OSError) as e:
            errors.append(_issue("bad_frontmatter", rel, None, str(e)))
            continue
        arts = split_articles(body)
        core = [ln for ln in body.splitlines() if ln.strip() and not ln.startswith("# ")]
        # keep summaries only (the corpus is hundreds of MB): the body is needed later just for overview tables
        files.append((rel, meta, [article_number(h) for h, _ in arts], [h for h, b in arts if article_empty(b)],
                      body if "| parte | caminho |" in body else "", bool(core)))

    ids, by_dre = {}, {}
    for rel, meta, nums, empties, _, has_text in files:
        did = str(meta.get("dre_id") or "") or None
        # --- metadata
        missing = [k for k in REQUIRED if meta.get(k) in (None, "")]
        if "dre_id" in missing:
            errors.append(_issue("missing_dre_id", rel, did, "dre_id is missing"))
        if "source" in missing:
            errors.append(_issue("missing_source", rel, did, "official link (source) is missing"))
        rest = [k for k in missing if k not in ("dre_id", "source")]
        if rest:
            errors.append(_issue("incomplete_metadata", rel, did, "missing fields: " + ", ".join(rest)))
        for k in DATE_FIELDS:
            if meta.get(k) and not ISO_DATE.match(str(meta[k])):
                errors.append(_issue("incomplete_metadata", rel, did, f"{k} is not an ISO date: {meta[k]!r}"))
        if meta.get("status") and meta["status"] != STATUS_IN_FORCE:
            errors.append(_issue("incomplete_metadata", rel, did, f"status not allowed: {meta['status']!r}"))
        if meta.get("text_version") and meta["text_version"] not in (TEXT_CONSOLIDATED, TEXT_ORIGINAL):
            errors.append(_issue("incomplete_metadata", rel, did, f"text_version not allowed: {meta['text_version']!r}"))
        if bool(meta.get("part_of")) != bool(meta.get("part")):
            errors.append(_issue("bad_part", rel, did, "part_of and part must both be filled or both empty"))
        if meta.get("source") and not re.match(r"^https?://", str(meta["source"])):
            errors.append(_issue("missing_source", rel, did, f"source is not a link: {meta['source']!r}"))
        # --- type
        if meta.get("type") and meta["type"] not in types:
            errors.append(_issue("unknown_type", rel, did, f"act type not in the closed list: {meta['type']!r}"))
        # --- id
        fid = meta.get("id")
        if fid:
            if not ID_RE.match(str(fid)):
                errors.append(_issue("bad_id", rel, did, f"id has an invalid format: {fid!r}"))
            if Path(rel).stem != fid:
                errors.append(_issue("bad_id", rel, did, f"file name does not match id {fid!r}"))
            if fid in ids:
                errors.append(_issue("duplicate_id", rel, did, f"id {fid!r} is also used by {ids[fid]}"))
            else:
                ids[fid] = rel
        if did:
            by_dre.setdefault(did, []).append((rel, meta))
        # --- articles
        for head in empties:
            errors.append(_issue("empty_article", rel, did, f"empty article: {head[:80]}"))
        dup = sorted(n for n, c in Counter(nums).items() if c > 1)
        if dup:
            warnings.append(_issue("duplicate_article_numbers", rel, did, "article numbers repeated: " + ", ".join(dup[:10])))
        gaps = number_gaps(nums)
        if gaps:
            warnings.append(_issue("numbering_gap", rel, did,
                                   "gaps in article numbering: " + ", ".join(f"{a}->{b}" for a, b in gaps[:10])))
        if not nums and not has_text:
            warnings.append(_issue("no_text", rel, did, "the file has no body text"))

    # --- dre_id uniqueness: the pair (dre_id, part) is the key; an overview has an empty part
    for did, group in by_dre.items():
        seen = {}
        for rel, meta in group:
            key = meta.get("part") or ""
            if key in seen:
                errors.append(_issue("duplicate_dre_id", rel, did,
                                     f"dre_id {did} (part {key!r}) is also used by {seen[key]}"))
            else:
                seen[key] = rel

    # --- parts: each part belongs to an existing overview and the overview lists exactly its parts
    nums_by_rel = {rel: nums for rel, _, nums, *_ in files}
    by_rel = {rel: (meta, ovb) for rel, meta, _, _, ovb, _ in files}
    parts_of = {}
    for rel, meta, *_ in files:
        po = meta.get("part_of")
        if not po:
            continue
        parts_of.setdefault(po, []).append(meta["id"])
        if po not in ids:
            errors.append(_issue("bad_part", rel, str(meta.get("dre_id")), f"overview {po!r} does not exist"))
        if not str(meta.get("id", "")).startswith(po + "-"):
            errors.append(_issue("bad_part", rel, str(meta.get("dre_id")),
                                 "part id must be the code id followed by the part name"))
    for po, pids in parts_of.items():
        if po not in ids:
            continue
        ov_meta, ov_body = by_rel[ids[po]]
        listed = [Path(m.group(1)).stem for m in re.finditer(r"^\|[^|\n]*\|\s*([^|\n]+?\.md)\s*\|", ov_body, re.M)]
        if sorted(listed) != sorted(pids):
            errors.append(_issue("overview_incomplete", ids[po], str(ov_meta.get("dre_id")),
                                 "overview does not list exactly its parts: expected " + ", ".join(sorted(pids))))
        # the ranges of the table must be the first and last article of each part file; the approval part comes first
        seen_other = False
        for row in ROW_RE.finditer(ov_body):
            title, path, a0, a1 = (c.strip() for c in row.groups())
            if path in nums_by_rel:
                got = nums_by_rel[path]
                if (a0, a1) != ((got[0], got[-1]) if got else ("", "")):
                    errors.append(_issue("overview_range_mismatch", ids[po], str(ov_meta.get("dre_id")),
                                         f"{path}: table says {a0!r} to {a1!r}, the file has {got[:1]} to {got[-1:]}"))
            if title.startswith("Diploma de aprovação") and seen_other:
                errors.append(_issue("approval_part_not_first", ids[po], str(ov_meta.get("dre_id")),
                                     "the approval part must come before every other part"))
            seen_other = seen_other or not title.startswith("Diploma de aprovação")

    # --- article count against the DRE data (sum over the parts of an act; originals have no DRE count)
    if expected_counts:
        got = {}
        for rel, meta, nums, *_ in files:
            got[str(meta.get("dre_id"))] = got.get(str(meta.get("dre_id")), 0) + len(nums)
        for did, group in by_dre.items():
            want = expected_counts.get(did)
            if want is not None and got[did] != want:
                errors.append(_issue("article_count_mismatch", group[0][0], did,
                                     f"file has {got[did]} articles, the DRE data has {want}"))
    for did, n in sorted((other_headings or {}).items()):
        if n and did in by_dre:
            warnings.append(_issue("non_article_headings", by_dre[did][0][0], did,
                                   f"{n} article fragments have a heading that does not start with 'Artigo' (not counted)"))
    return errors, warnings


def expected_counts_from_raw(raw_dir, with_notes=False):
    """{dre_id: article count in the DRE JSON} for every cached diploma (None for original texts).
    with_notes also returns {dre_id: number of article fragments with a non-'Artigo' heading}."""
    from convert import dre_article_count, dre_other_article_headings
    counts, notes = {}, {}
    for p in sorted((Path(raw_dir) / "json").glob("*.json.gz")):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            rec = json.load(fh)
        did = p.name.split(".")[0]
        counts[did] = dre_article_count(rec)
        notes[did] = dre_other_article_headings(rec)
    return (counts, notes) if with_notes else counts


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate generated diploma files (blocking errors, numbering warnings).")
    ap.add_argument("--root", required=True, help="tree to validate (staging directory or repo)")
    ap.add_argument("--act-types", required=True, help="closed list of act types (config/act-types.txt)")
    ap.add_argument("--raw", default=None, help="raw cache: enables the article count check against the DRE data")
    ap.add_argument("--json", default=None, help="write the error and warning lists here")
    a = ap.parse_args(argv)
    counts, notes = expected_counts_from_raw(a.raw, True) if a.raw else (None, None)
    errors, warnings = validate(a.root, load_act_types(a.act_types), counts, notes)
    if a.json:
        Path(a.json).write_text(json.dumps({"errors": errors, "warnings": warnings}, ensure_ascii=False, indent=1),
                                encoding="utf-8")
    for e in errors:
        print(f"ERROR   {e['code']}: {e['file']}: {e['message']}", file=sys.stderr)
    for w in warnings:
        print(f"warning {w['code']}: {w['file']}: {w['message']}", file=sys.stderr)
    print(f"{len(errors)} errors, {len(warnings)} warnings", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
