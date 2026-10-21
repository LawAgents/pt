#!/usr/bin/env python3
"""Write the closed list of act types (config/act-types.txt) from the raw cache.

  python scripts/gen_act_types.py --raw DIR [--out config/act-types.txt]

The list is the set of act types the DRE returned for the in-force diplomas of the list (RULES.xml#rule.act_type_closed).
Run it once after the initial import; afterwards a new type blocks the update until someone adds it on purpose.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import atomic_write  # noqa: E402
from fetch import selected  # noqa: E402

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "config" / "act-types.txt"


def act_types(lst):
    return sorted({(s.get("tipo") or "").strip() for s in lst if selected(s)} - {""})


def main(argv=None):
    ap = argparse.ArgumentParser(description="Write the closed list of act types from the raw cache.")
    ap.add_argument("--raw", required=True, help="raw cache directory (needs list.json)")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="output file, one type per line")
    a = ap.parse_args(argv)
    lst = json.loads((Path(a.raw) / "list.json").read_text(encoding="utf-8"))
    types = act_types(lst)
    atomic_write(a.out, "\n".join(types) + "\n")
    print(f"{len(types)} act types written to {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
