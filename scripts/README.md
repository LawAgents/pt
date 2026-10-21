# Pipeline scripts

Python 3.12+, standard library only. Every script has `--help`. Tests: `python -m unittest discover -s scripts/tests`.

| Script | What it does |
|---|---|
| `run_update.py --mode initial\|weekly --raw DIR --repo DIR --budget-seconds N` | fetch, convert, validate, index and size check in a staging dir (`DIR/stage`), then replaces the repo files. Optional `--config DIR` (default `REPO/config`), `--eli`, `--max-part-kb`. |
| `fetch.py --mode ... --raw DIR [--budget-seconds N] [--repo DIR] [--eli]` | downloads the DRE JSON into the raw cache (outside the repo). With `--repo` it also fetches the revocation date of diplomas that left force. |
| `convert.py --raw DIR --out DIR [--repo DIR] [--max-part-kb 70]` | raw JSON to markdown (ids, front matter, parts). `--repo` keeps ids already in the repo. |
| `validate.py --root DIR --act-types FILE [--raw DIR] [--json OUT]` | blocking errors and warnings as JSON; exit 1 on any blocking error. |
| `build_index.py --root DIR --config DIR [--raw DIR] [--repo DIR]` | `nomes-comuns.md`, `indice.md`, `indice-<type folder>[-<from>-<to>].md` (each at most 40 KB; a year is never split unless it alone passes 40 KB, then `-<year>-a`, `-<year>-b`...), `indice-temas.md`, `revogados.md`. |
| `check_size.py --repo DIR [--tree DIR]` | prints git objects and tracked tree size; exit 1 above 1 GiB. |
| `gen_act_types.py --raw DIR [--out config/act-types.txt]` | writes the closed list of act types from the raw list. |

## `run_update.py` exit codes

- `0` ready to commit. Prints `CHANGED=true|false` (also appended to `$GITHUB_OUTPUT` when set).
- `2` time budget reached while fetching. The repo is untouched; run the same command again and it resumes.
- `1` failure. The repo is untouched, the error list is in `RAW/errors.json` (`{mode, stage, errors, warnings}`), a summary goes to stderr.
  Stages: `fetch`, `validate` (conversion errors too), `index`, `size`, `internal`.

Any blocking error fails the whole update (nothing is written to the repo). `RAW` must survive between runs
(resume after exit 2, and weekly runs only re-download the extra requests for diplomas whose text changed).

## Fetching

- One global throttle: at least 0.55 s between the start of any two requests (including `moduleinfo` and the JS files), single thread.
- `User-Agent: LawAgents-pt/<version> (+https://github.com/LawAgents/pt)` on every request.
- Stops at once after 3 consecutive errors or on HTTP 429/503 (exit 1). Cache files are written with tmp + rename.
- `initial`: list + every in-force diploma without an up-to-date cache record. `weekly`: a new cycle that re-reads the text of
  every in-force diploma (the search list has no last-consolidation date) and asks for metadata/original text only when the
  text changed.
- Requests: list about 60 pages, about 6 setup requests; per diploma 1 (text) + 1 (metadata, ELI) + 1 to 2 for acts with no
  consolidated text. Roughly 10,400 requests for `initial` (about 3.0 h at 1.05 s, 4 to 5 h with server time),
  about 5,500 by default (ELI off), about 10,400 with `--eli`; about 5,000 for `weekly` (1.5 to 2 h).

## Config (`config/`)

- `act-types.txt`: closed list of act types, one per line (seeded from the LawCodex README, replaced by `gen_act_types.py`).
- `nomes-comuns.txt`: `id | common name | acronym1, acronym2`, 30 to 50 entries, written by hand. Missing file, missing id or a
  wrong number of entries fails the update.
- `temas.txt` (optional): `id | theme`. The theme index also gets a "Códigos" section from the DRE page "Legislação por código".

## Layout written to the repo

`{type folder}/{year}/{id}.md`, codes in `codigos/{code}/{id}.md`, the Constitution in `constituicao/`. A diploma whose article
numbers would repeat in one file (approving decree + annex) or that is above 70 KB is split (with a `## Estrutura` outline in the overview): overview `{id}.md` with a table of
parts, plus one file per part `{id}-{part}.md` (`part_of` and `part` filled, same `dre_id`).
Only these folders and the root index files are ever written or deleted.
