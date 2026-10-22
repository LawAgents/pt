"""config/extras.txt: curated diplomas the DRE does not consolidate (parse, resolve, precedence, text version)."""
import contextlib
import copy
import io
import json
import unittest
from pathlib import Path

from helpers import DLR_15_96, FakeClock, FakeServer, LEI_24_96, REPO, TmpCase, common, load_raw_record

import convert
import fetch
import run_update
import validate

EXTRA_DB = 3_000_001
ACT_TYPES = common.load_act_types(REPO / "config" / "act-types.txt")


def hit(db, tipo="Decreto-Lei", numero="84/2021", ano="2021", **kw):
    return dict({"dbId": db, "tipo": tipo, "numero": numero, "ano": ano}, **kw)


class StubDre:
    """search() returns the same hits for every query (the filters are not simulated)."""

    def __init__(self, hits):
        self.hits = hits

    def search(self, filters, start=0, size=100, text="*", sort=None):
        page = self.hits[start:start + size]
        return {"hits": {"total": {"value": len(self.hits)}, "hits": [{"_source": h} for h in page]}}


class ExtrasServer(FakeServer):
    """Fake DRE with one extra diploma (a copy of an original-only record) that the public-consolidation list hides."""

    def __init__(self, clock):
        super().__init__(clock)
        r = copy.deepcopy(self.records[DLR_15_96])
        r["search"].update(dbId=EXTRA_DB, tipo="Decreto-Lei", numero="84/2021", ano="2021", dataPublicacao="2021-10-18",
                           DiplomaFragmentadoId=None, vigencia=None)
        r["original"]["Id"] = EXTRA_DB
        self.records[EXTRA_DB] = r

    def action(self, action, v):
        if action == "DataActionGetPesquisas":
            public = any(f["Area"] == "consolidacaoVisibility" for f in v["ListaFiltros"]["List"])
            entries = [e for e in self.list_entries() if not (public and e["dbId"] == EXTRA_DB)]
            s, n = v["StartIndex"], v["MaxRecordsPerPage"]
            hits = [{"_source": e} for e in entries[s:s + n]]
            return {"Resultado": json.dumps({"hits": {"total": {"value": len(entries)}, "hits": hits}})}
        return super().action(action, v)


class Parsing(TmpCase):
    def test_comments_and_blank_lines_are_ignored(self):
        p = self.tmp / "extras.txt"
        p.write_text("# comment\n\nDecreto-Lei | 84/2021 | nota\n  \nLei | 74-A/2017\n", encoding="utf-8")
        self.assertEqual(fetch.parse_extras(p), [(3, "Decreto-Lei", "84", "2021", "nota"), (5, "Lei", "74-A", "2017", "")])

    def test_a_bad_line_fails_with_its_line_number(self):
        for bad in ("Lei | sem-ano | x", "Lei", "| 1/2000 | x", "Lei | 1/00 | x"):
            with self.subTest(bad=bad):
                p = self.tmp / "extras.txt"
                p.write_text("# c\nLei | 1/2000 | ok\n" + bad + "\n", encoding="utf-8")
                with self.assertRaisesRegex(fetch.ExtrasError, r"extras\.txt:3:"):
                    fetch.parse_extras(p)

    def test_the_seed_file_parses(self):
        rows = fetch.parse_extras(REPO / "config" / "extras.txt")
        self.assertEqual([(r[1], r[2], r[3]) for r in rows], [
            ("Decreto-Lei", "84", "2021"), ("Lei", "60", "2013"), ("Lei", "83", "2021"), ("Lei", "23", "2018"),
            ("Lei", "58", "2019"), ("Decreto-Lei", "62", "2013"), ("Decreto-Lei", "69", "2015")])


class Resolving(TmpCase):
    def resolve(self, hits, listed=()):
        p = self.tmp / "extras.txt"
        p.write_text("# c\nDecreto-Lei | 84/2021 | nota\n", encoding="utf-8")
        return fetch.resolve_extras(StubDre(hits), p, set(listed))

    def test_exactly_one_match_is_flagged_as_extra(self):
        out = self.resolve([hit(1), hit(2, numero="85/2021"), hit(3, tipo="Lei"), hit(4, ano="2020")])
        self.assertEqual([(s["dbId"], s["extra"]) for s in out], [(1, True)])

    def test_unresolved_fails_with_the_line_number(self):
        with self.assertRaisesRegex(fetch.ExtrasError, r"extras\.txt:2: .*matches 0 DRE records"):
            self.resolve([hit(2, numero="85/2021")])

    def test_ambiguous_fails_with_the_line_number(self):
        with self.assertRaisesRegex(fetch.ExtrasError, r"extras\.txt:2: .*matches 2 DRE records"):
            self.resolve([hit(1), hit(2)])

    def test_not_in_force_fails(self):
        for kw in ({"vigencia": "NAO_VIGENTE"}, {"vigencia": "CADUCADO"}, {"consolidacaoEstado": "REVOKED"},
                   {"vigencia": "OUTRO"}):
            with self.subTest(kw=kw):
                with self.assertRaisesRegex(fetch.ExtrasError, r"extras\.txt:2: .*not in force"):
                    self.resolve([hit(1, **kw)])

    def test_a_consolidated_diploma_in_the_normal_list_wins(self):
        self.assertEqual(self.resolve([hit(1)], listed={1}), [])

    def test_search_pages_are_followed(self):
        hits = [hit(10 + i, numero=f"{1000 + i}/2021") for i in range(600)] + [hit(1)]
        self.assertEqual([s["dbId"] for s in self.resolve(hits)], [1])


class EndToEnd(TmpCase):
    def setUp(self):
        super().setUp()
        self.server = ExtrasServer(FakeClock())
        self.extras = self.tmp / "extras.txt"

    def fetch(self, lines):
        self.extras.write_text(lines, encoding="utf-8")
        raw = fetch.Raw(self.tmp / "raw")
        rc = fetch.run_fetch(self.server.dre(), raw, "initial", log=lambda m: None, extras=self.extras)
        return rc, raw

    def test_extra_is_fetched_with_its_original_text_and_converted(self):
        rc, raw = self.fetch("Decreto-Lei | 84/2021 | nota\n")
        self.assertEqual(rc, 0)
        rec = raw.read(EXTRA_DB)
        self.assertTrue(rec["search"]["extra"])
        self.assertTrue(rec["original"])
        act = convert.convert_record(rec, "decreto-lei-84-2021", set())
        meta, body = common.parse_frontmatter(act.files[0][1])
        self.assertEqual(meta["text_version"], "original sem consolidação")
        self.assertNotIn("last_amended", meta)
        self.assertEqual(meta["legal_notice"], common.LEGAL_NOTICE)
        lines = [ln for ln in body.splitlines() if ln.strip()]
        self.assertTrue(lines[0].startswith("# "))
        self.assertEqual(lines[1], "Texto original, sem consolidação: pode ter sido alterado depois.")

    def test_existing_originals_keep_their_text_version_and_get_no_notice(self):
        act = convert.convert_record(load_raw_record(DLR_15_96), "x-1-2000", set())
        meta, body = common.parse_frontmatter(act.files[0][1])
        self.assertEqual(meta["text_version"], "original sem alterações")
        self.assertNotIn(common.EXTRA_NOTICE, body)

    def test_a_consolidated_diploma_is_not_added_twice(self):
        rc, raw = self.fetch("Lei | 24/1996 | already consolidated\n")
        self.assertEqual(rc, 0)
        lst = raw.read_json("list.json")
        self.assertEqual([s["dbId"] for s in lst].count(LEI_24_96), 1)
        self.assertFalse(any(s.get("extra") for s in lst))
        self.assertIsNone(raw.read(EXTRA_DB))

    def test_unresolved_line_writes_nothing(self):
        with self.assertRaisesRegex(fetch.ExtrasError, r"extras\.txt:1:"):
            self.fetch("Lei | 999/2021 | nope\n")
        self.assertFalse((self.tmp / "raw" / "list.json").exists())

    def test_a_revoked_original_fails_loudly(self):
        self.server.records[EXTRA_DB]["original"]["Vigencia"] = "NAO_VIGENTE"
        with self.assertRaisesRegex(fetch.ExtrasError, "not in force"):
            self.fetch("Decreto-Lei | 84/2021 | nota\n")

    def test_run_update_adds_the_extra_and_fails_on_a_bad_line_without_touching_the_repo(self):
        repo, cfg = self.tmp / "repo", self.config_dir()
        repo.mkdir()

        def go(extras_text):
            (cfg / "extras.txt").write_text(extras_text, encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                return run_update.run("initial", self.tmp / "raw", repo, config=cfg, count_check=False,
                                      dre=self.server.dre(), clock=FakeClock())

        self.assertEqual(go("Decreto-Lei | 84/2021 | nota\n"), 0)
        f = repo / "decretos-lei/2021/decreto-lei-84-2021.md"
        self.assertIn(common.EXTRA_NOTICE, f.read_text(encoding="utf-8"))
        before = f.read_bytes()
        self.assertEqual(go("Decreto-Lei | 84/2021 | nota\nLei | 5/1999 | missing\n"), 1)
        err = json.loads((self.tmp / "raw" / "errors.json").read_text(encoding="utf-8"))
        self.assertEqual(err["stage"], "extras")
        self.assertIn("extras.txt:2:", err["errors"][0]["message"])
        self.assertEqual(f.read_bytes(), before)


class ValidatingTextVersion(TmpCase):
    BODY = "# Decreto-Lei n.º 84/2021\n\n" + common.EXTRA_NOTICE + "\n\n## Artigo 1.º\n\nTexto.\n"

    def check(self, body=BODY, **meta):
        meta = dict({"text_version": common.TEXT_EXTRA, "last_amended": None}, **meta)
        self.write_file(self.tmp, "leis/2000/lei-1-2000.md", meta, body)
        return validate.validate(self.tmp, ACT_TYPES)

    def test_new_value_is_accepted(self):
        self.assertEqual(self.check(), ([], []))

    def test_missing_notice_is_rejected(self):
        errors, _ = self.check(body=self.BODY.replace(common.EXTRA_NOTICE + "\n\n", ""))
        self.assertEqual([e["code"] for e in errors], ["bad_text_version"])

    def test_last_amended_is_rejected(self):
        errors, _ = self.check(last_amended="2021-01-01")
        self.assertEqual([e["code"] for e in errors], ["bad_text_version"])

    def test_unknown_value_is_still_rejected(self):
        errors, _ = self.check(text_version="inventado")
        self.assertEqual([e["code"] for e in errors], ["incomplete_metadata"])


if __name__ == "__main__":
    unittest.main()


class DroppedExtras(TmpCase):
    def test_dropped_extra_is_not_reported_as_left_force(self):
        class Raw:
            def read_json(self, name, default=None):
                return []  # nothing selected any more

        for did, tv in (("1", "consolidado"), ("2", common.TEXT_EXTRA)):
            d = self.tmp / "leis" / "2000"
            d.mkdir(parents=True, exist_ok=True)
            (d / f"lei-{did}-2000.md").write_text(
                f'---\nid: "lei-{did}-2000"\ndre_id: "{did}"\ntext_version: "{tv}"\n---\n\n# x\n', encoding="utf-8")
        self.assertEqual(fetch.left_force_ids(Raw(), self.tmp), ["1"])
