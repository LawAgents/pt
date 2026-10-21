"""Validator tests: test.validation_blocking, test.unique_ids, test.gaps_warning, test.parts, test.act_type."""
import json
import shutil
import unittest

from helpers import REPO, TmpCase, common

import convert
import validate

TYPES = common.load_act_types(REPO / "config" / "act-types.txt")
GOOD_BODY = "# Lei n.º 1/2000\n\n## Artigo 1.º (Objeto)\n\nTexto um.\n\n## Artigo 2.º (Âmbito)\n\nTexto dois.\n"


def codes(issues):
    return sorted({i["code"] for i in issues})


class Blocking(TmpCase):
    def check(self, meta=None, body=GOOD_BODY, counts=None, extra=None, types=TYPES):
        root = self.tmp / "tree"
        self.write_file(root, "leis/2000/lei-1-2000.md", meta or {}, body)
        for rel, m, b in extra or []:
            self.write_file(root, rel, m, b)
        return validate.validate(root, types, counts)

    def test_control_file_is_accepted(self):
        errors, warnings = self.check(counts={"1": 2})
        self.assertEqual((errors, warnings), ([], []))

    def test_seven_broken_files_are_all_rejected(self):
        broken = {
            "incomplete metadata": dict(meta={"date": None}, expect="incomplete_metadata"),
            "missing official link": dict(meta={"source": None}, expect="missing_source"),
            "missing dre_id": dict(meta={"dre_id": None}, expect="missing_dre_id"),
            "empty article": dict(body="# T\n\n## Artigo 1.º\n\n## Artigo 2.º\n\nTexto.\n", expect="empty_article"),
            "type outside the list": dict(meta={"type": "Tipo Inventado"}, expect="unknown_type"),
            "article count differs from the DRE": dict(counts={"1": 3}, expect="article_count_mismatch"),
            "duplicate id": dict(extra=[("leis/2000/outro/lei-1-2000.md", {"dre_id": "2"}, GOOD_BODY)], expect="duplicate_id"),
        }
        self.assertEqual(len(broken), 7)
        for name, case in broken.items():
            with self.subTest(name):
                expect = case.pop("expect")
                shutil.rmtree(self.tmp / "tree", ignore_errors=True)
                errors, _ = self.check(**case)
                self.assertIn(expect, codes(errors))

    def test_amendment_notes_do_not_make_an_empty_article_non_empty(self):
        errors, _ = self.check(body="# T\n\n## Artigo 1.º\n\n- *Alterado pela Lei n.º 5/2001*\n")
        self.assertIn("empty_article", codes(errors))

    def test_revoked_article_is_not_empty(self):
        errors, _ = self.check(body="# T\n\n## Artigo 1.º\n\n*(Revogado)* — *Revogado pelo Artigo 3.º*\n")
        self.assertEqual(errors, [])

    def test_file_name_must_match_id_and_id_must_be_well_formed(self):
        root = self.tmp / "tree"
        self.write_file(root, "leis/2000/other-name.md", {}, GOOD_BODY)
        self.write_file(root, "leis/2000/Bad_Id.md", {"id": "Bad_Id", "dre_id": "2"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertEqual(codes(errors), ["bad_id"])
        self.assertEqual(len(errors), 2)

    def test_json_output_and_exit_code(self):
        root = self.tmp / "tree"
        self.write_file(root, "leis/2000/lei-1-2000.md", {"source": None}, GOOD_BODY)
        out = self.tmp / "errors.json"
        rc = validate.main(["--root", str(root), "--act-types", str(REPO / "config" / "act-types.txt"), "--json", str(out)])
        self.assertEqual(rc, 1)
        data = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(data["errors"][0]["code"], "missing_source")
        self.assertEqual(set(data["errors"][0]), {"code", "file", "dre_id", "message"})
        self.assertEqual(data["warnings"], [])

    def test_clean_tree_exit_code_0(self):
        root = self.tmp / "tree"
        self.write_file(root, "leis/2000/lei-1-2000.md", {}, GOOD_BODY)
        self.assertEqual(validate.main(["--root", str(root), "--act-types", str(REPO / "config" / "act-types.txt")]), 0)


class UniqueIds(TmpCase):
    def test_ids_generated_for_the_fixtures_validate_and_follow_the_format(self):
        from helpers import FIX
        out = self.tmp / "out"
        convert.convert_all(FIX / "raw", out, log=lambda m: None)
        counts = validate.expected_counts_from_raw(FIX / "raw")
        errors, warnings = validate.validate(out, TYPES, counts)
        self.assertEqual(errors, [])
        ids = [m["id"] for m in common.main_files(out)]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("decreto-legislativo-regional-7-1999-a", ids)   # regional suffix

    def test_duplicate_dre_id_between_different_diplomas_is_rejected(self):
        root = self.tmp / "tree"
        self.write_file(root, "leis/2000/lei-1-2000.md", {}, GOOD_BODY)
        self.write_file(root, "leis/2000/lei-2-2000.md", {"id": "lei-2-2000"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertEqual(codes(errors), ["duplicate_dre_id"])

    def test_issuer_and_numberless_ids_are_valid(self):
        root = self.tmp / "tree"
        self.write_file(root, "avisos/2019/aviso-12-2019-banco-de-portugal.md",
                        {"id": "aviso-12-2019-banco-de-portugal", "type": "Aviso", "dre_id": "5"}, GOOD_BODY)
        self.write_file(root, "outros/edital/2021/edital-2021-dre-123456.md",
                        {"id": "edital-2021-dre-123456", "type": "Edital", "dre_id": "123456"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertEqual(errors, [])


class Gaps(TmpCase):
    def test_gap_in_numbering_is_a_warning_and_does_not_block(self):
        root = self.tmp / "tree"
        body = "# T\n\n## Artigo 1.º\n\nA.\n\n## Artigo 2.º\n\nB.\n\n## Artigo 5.º\n\nC.\n\n## Artigo 5.º-A\n\nD.\n"
        self.write_file(root, "leis/2000/lei-1-2000.md", {}, body)
        errors, warnings = validate.validate(root, TYPES)
        self.assertEqual(errors, [])
        self.assertEqual(codes(warnings), ["numbering_gap"])
        self.assertIn("2->5", warnings[0]["message"])

    def test_letter_suffixes_and_revoked_articles_are_not_gaps(self):
        self.assertEqual(validate.number_gaps(["1.º", "1.º-A", "2.º", "3.º-B", "3.º"]), [])
        self.assertEqual(validate.number_gaps(["1.º", "2.º", "1.º"]), [])  # a restart (annex) is not a gap


class PartsTest(TmpCase):
    def make(self, overview_rows=("a", "b", "c"), part_ids=("a", "b", "c"), part_of="codigo-1-2000"):
        root = self.tmp / "tree"
        rows = "\n".join(f"| Parte {p} | codigos/codigo/{part_of}-{p}.md | 1.º | 2.º |" for p in overview_rows)
        self.write_file(root, f"codigos/codigo/{part_of}.md", {"id": part_of, "dre_id": "7"},
                        f"# Código\n\n| parte | caminho | primeiro artigo | último artigo |\n|---|---|---|---|\n{rows}\n")
        for p in part_ids:
            self.write_file(root, f"codigos/codigo/{part_of}-{p}.md",
                            {"id": f"{part_of}-{p}", "dre_id": "7", "part_of": part_of, "part": f"Parte {p}"}, GOOD_BODY)
        return root

    def test_three_parts_sharing_a_dre_id_are_accepted_and_the_overview_is_complete(self):
        errors, _ = validate.validate(self.make(), TYPES, {"7": 6})
        self.assertEqual(errors, [])

    def test_overview_missing_a_part_is_rejected(self):
        errors, _ = validate.validate(self.make(overview_rows=("a", "b")), TYPES)
        self.assertIn("overview_incomplete", codes(errors))

    def test_two_parts_with_the_same_title_and_dre_id_are_duplicates(self):
        root = self.make()
        self.write_file(root, "codigos/codigo/codigo-1-2000-d.md",
                        {"id": "codigo-1-2000-d", "dre_id": "7", "part_of": "codigo-1-2000", "part": "Parte a"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertIn("duplicate_dre_id", codes(errors))

    def test_part_without_existing_overview_or_with_wrong_id_is_rejected(self):
        root = self.make()
        self.write_file(root, "codigos/codigo/x.md", {"id": "x", "dre_id": "7", "part_of": "nao-existe", "part": "Parte x"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertEqual(codes(errors), ["bad_part"])

    def test_part_fields_must_come_in_pairs(self):
        root = self.tmp / "tree"
        self.write_file(root, "leis/2000/lei-1-2000.md", {"part": "Livro I"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertIn("bad_part", codes(errors))

    def test_converted_code_passes_with_its_dre_count(self):
        from helpers import FIX
        out = self.tmp / "out"
        convert.convert_all(FIX / "raw", out, log=lambda m: None, max_bytes=12_000)
        errors, _ = validate.validate(out, TYPES, validate.expected_counts_from_raw(FIX / "raw"))
        self.assertEqual(errors, [])


class ActTypes(TmpCase):
    def test_new_type_blocks_until_it_is_added_to_the_list(self):
        root = self.tmp / "tree"
        self.write_file(root, "outros/novo/2000/lei-1-2000.md", {"type": "Tipo Novo"}, GOOD_BODY)
        errors, _ = validate.validate(root, TYPES)
        self.assertEqual(codes(errors), ["unknown_type"])
        listing = self.tmp / "act-types.txt"
        listing.write_text("\n".join(TYPES + ["Tipo Novo"]) + "\n", encoding="utf-8")
        errors, _ = validate.validate(root, common.load_act_types(listing))
        self.assertEqual(errors, [])

    def test_gen_act_types_writes_the_types_of_in_force_diplomas(self):
        import gen_act_types
        from helpers import FIX
        out = self.tmp / "types.txt"
        self.assertEqual(gen_act_types.main(["--raw", str(FIX / "raw"), "--out", str(out)]), 0)
        self.assertEqual(out.read_text(encoding="utf-8").splitlines(), ["Decreto Legislativo Regional", "Decreto-Lei", "Lei"])


if __name__ == "__main__":
    unittest.main()
