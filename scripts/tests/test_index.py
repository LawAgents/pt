"""Index tests: test.index_layers and test.index_contract (SCHEMA table.index_files, article_heading, code_layout)."""
import re
import shutil
import unittest

from helpers import FIX, TmpCase, common

import build_index
import convert
import validate


class IndexCase(TmpCase):
    def build(self, **kw):
        out = self.tmp / "tree"
        convert.convert_all(FIX / "raw", out, log=lambda m: None)
        self.cfg = self.config_dir()
        return out

    def run_index(self, out, **kw):
        kw.setdefault("check_count", False)
        return build_index.build_all(out, self.cfg, FIX / "raw", **kw)


class IndexLayers(IndexCase):
    def test_generator_fails_when_an_id_of_the_common_names_list_is_missing(self):
        out = self.build()
        self.run_index(out)  # all ids exist: fine
        shutil.rmtree(out / "leis")  # lei-24-1996 disappears from the tree
        with self.assertRaises(build_index.IndexError_) as cm:
            self.run_index(out)
        self.assertIn("lei-24-1996", str(cm.exception))
        self.assertEqual(build_index.main(["--root", str(out), "--config", str(self.cfg), "--raw", str(FIX / "raw"),
                                           "--no-count-check"]), 1)

    def test_a_theme_id_that_does_not_exist_fails_too(self):
        out = self.build()
        (self.cfg / "temas.txt").write_text("nao-existe-1-2000 | Tema\n", encoding="utf-8")
        with self.assertRaises(build_index.IndexError_):
            self.run_index(out)

    def test_missing_common_names_file_fails(self):
        out = self.build()
        (self.cfg / "nomes-comuns.txt").unlink()
        with self.assertRaises(build_index.IndexError_):
            self.run_index(out)

    def test_common_names_must_have_30_to_50_entries(self):
        out = self.build()
        with self.assertRaises(build_index.IndexError_) as cm:
            build_index.build_all(out, self.cfg, FIX / "raw")  # the fixture has 2 entries
        self.assertIn("30 to 50", str(cm.exception))

    def test_short_list_names_come_first_and_type_index_has_the_rest(self):
        out = self.build()
        self.run_index(out)
        short = (out / "nomes-comuns.md").read_text(encoding="utf-8")
        self.assertIn("Lei de Defesa do Consumidor", short)
        self.assertNotIn("decreto-legislativo-regional-7-1999-a", short)  # only in the type index
        self.assertIn("decreto-legislativo-regional-7-1999-a",
                      (out / "indice-decretos-legislativos-regionais.md").read_text(encoding="utf-8"))


class IndexContract(IndexCase):
    def test_files_names_columns_and_sizes_follow_the_schema(self):
        out = self.build()
        written = self.run_index(out)
        self.assertEqual(sorted(p.name for p in out.iterdir() if p.is_file()), written)
        self.assertIn("nomes-comuns.md", written)
        self.assertIn("indice.md", written)
        self.assertIn("indice-temas.md", written)
        self.assertIn("revogados.md", written)
        self.assertLessEqual((out / "nomes-comuns.md").stat().st_size, 10 * 1024)
        self.assertIn("| nome comum | siglas | id | caminho |", (out / "nomes-comuns.md").read_text(encoding="utf-8"))
        self.assertIn("| id | título | caminho | nome comum | siglas | sumário |",
                      (out / "indice-leis.md").read_text(encoding="utf-8"))
        self.assertIn("| id | título | data da revogação | ligação oficial |", (out / "revogados.md").read_text(encoding="utf-8"))
        for n in written:
            if n.startswith("indice-") and n != "indice-temas.md":
                self.assertRegex(n, r"^indice-[a-z0-9-]+\.md$")
                self.assertLessEqual((out / n).stat().st_size, 40 * 1024)

    def test_manifest_lists_every_index_file_with_counts(self):
        out = self.build()
        written = self.run_index(out)
        manifest = (out / "indice.md").read_text(encoding="utf-8")
        self.assertIn("| ficheiro | tipo | ano inicial | ano final | n.º de diplomas |", manifest)
        for n in written:
            if n.startswith("indice-"):
                self.assertIn(f"| {n} |", manifest)
        rows = [ln for ln in manifest.splitlines() if ln.startswith("| indice-") and "temas" not in ln]
        self.assertEqual(sum(int(r.strip("| ").split("|")[-1]) for r in rows), len(common.main_files(out)))

    def test_every_index_row_points_to_a_real_file_with_the_same_id(self):
        out = self.build()
        self.run_index(out)
        n_rows = 0
        for p in out.glob("indice-*.md"):
            if p.name == "indice-temas.md":
                continue
            for ln in p.read_text(encoding="utf-8").splitlines():
                if ln.startswith("| ") and not ln.startswith("| id ") and not ln.startswith("|---"):
                    cells = [c.strip() for c in ln.strip("|").split(" | ")]
                    meta = common.parse_frontmatter((out / cells[2]).read_text(encoding="utf-8"))[0]
                    self.assertEqual(meta["id"], cells[0])
                    n_rows += 1
        self.assertEqual(n_rows, len(common.main_files(out)))

    def test_articles_and_code_layout_follow_the_schema(self):
        out = self.build()
        self.run_index(out)
        for rel in (p.relative_to(out).as_posix() for p in common.iter_owned_files(out)):
            meta, body = common.parse_frontmatter((out / rel).read_text(encoding="utf-8"))
            for line in body.splitlines():
                if re.match(r"^#{1,6} Artigo", line):
                    self.assertRegex(line, r"^#{1,6} Artigo \S+")
            if rel.startswith("codigos/"):
                parts = rel.split("/")
                self.assertEqual(len(parts), 3)          # codigos/{name}/{file}.md
                self.assertEqual(parts[2], meta["id"] + ".md")
        code = common.parse_frontmatter((out / "codigos/codigo-da-publicidade/decreto-lei-330-1990.md").read_text(encoding="utf-8"))
        self.assertEqual(code[0]["id"], "decreto-lei-330-1990")      # main file id = id of the approving act
        self.assertNotIn("part_of", code[0])
        self.assertTrue((out / "codigos/codigo-da-publicidade/decreto-lei-330-1990-diploma-de-aprovacao.md").exists())

    def test_themes_file_format_and_codes_section(self):
        out = self.build()
        self.run_index(out)
        text = (out / "indice-temas.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^## Consumo$")
        self.assertRegex(text, r"(?m)^- lei-24-1996 \| Lei n\.º 24/96$")
        self.assertRegex(text, r"(?m)^## Códigos$")           # from the DRE page Legislacao por codigo
        sec = text.split("## Códigos")[1].split("\n## ")[0]
        self.assertIn("- decreto-lei-330-1990 | Código da Publicidade", sec)
        self.assertNotIn("(Decreto-Lei", text)                 # short titles

    def test_code_acronyms_from_the_dre_page_become_aliases(self):
        out = self.build()
        raw = self.tmp / "raw"
        shutil.copytree(FIX / "raw", raw)
        import json
        cod = json.loads((raw / "codigos.json").read_text(encoding="utf-8"))
        for c in cod:
            if c["Designacao"] == "Código da Publicidade":
                c["Designacao"] = "Código da Publicidade - CPUB"
        (raw / "codigos.json").write_text(json.dumps(cod, ensure_ascii=False), encoding="utf-8")
        self.cfg = self.config_dir()
        (self.cfg / "nomes-comuns.txt").write_text("lei-24-1996 | Lei de Defesa do Consumidor | LDC\n", encoding="utf-8")
        build_index.build_all(out, self.cfg, raw, check_count=False)
        self.assertIn("| decreto-lei-330-1990 |", (out / "indice-codigos.md").read_text(encoding="utf-8"))
        self.assertRegex((out / "indice-codigos.md").read_text(encoding="utf-8"), r"\| Código da Publicidade \| CPUB \|")

    def test_large_group_is_sharded_by_years_without_splitting_a_year(self):
        out = self.tmp / "tree"
        n = 0
        for year in range(2000, 2010):
            for i in range(70):
                n += 1
                self.write_file(out, f"leis/{year}/lei-{n}-{year}.md",
                                {"id": f"lei-{n}-{year}", "dre_id": str(n), "year": year, "summary": "x" * 150,
                                 "title": f"Lei n.º {n}/{year}, de 1 de janeiro"}, "# T\n\n## Artigo 1.º\n\nA.\n")
        self.cfg = self.config_dir()
        (self.cfg / "nomes-comuns.txt").write_text("lei-1-2000 | Lei Um | L1\n", encoding="utf-8")
        (self.cfg / "temas.txt").write_text("", encoding="utf-8")
        names = build_index.build_all(out, self.cfg, None, check_count=False)
        shards = sorted(x for x in names if x.startswith("indice-leis"))
        self.assertGreater(len(shards), 1)
        seen_years = []
        for s in shards:
            self.assertRegex(s, r"^indice-leis-\d{4}-\d{4}\.md$")
            self.assertLessEqual((out / s).stat().st_size, 40 * 1024)
            years = {int(y) for y in re.findall(r"leis/(\d{4})/", (out / s).read_text(encoding="utf-8"))}
            self.assertTrue(years.isdisjoint(seen_years))
            seen_years += sorted(years)
        self.assertEqual(sorted(seen_years), list(range(2000, 2010)))
        self.assertEqual(validate.validate(out, ["Lei"])[0], [])

    def test_a_single_year_larger_than_the_limit_is_cut_by_id_order_into_lettered_files(self):
        out = self.tmp / "tree"
        for i in range(400):
            self.write_file(out, f"leis/2000/lei-{i:03d}-2000.md",
                            {"id": f"lei-{i:03d}-2000", "dre_id": str(i), "year": 2000, "summary": "x" * 150},
                            "# T\n\n## Artigo 1.º\n\nA.\n")
        self.write_file(out, "leis/2001/lei-001-2001.md", {"id": "lei-001-2001", "dre_id": "9001", "year": 2001},
                        "# T\n\n## Artigo 1.º\n\nA.\n")
        self.cfg = self.config_dir()
        (self.cfg / "nomes-comuns.txt").write_text("lei-001-2000 | Lei Um | L1\n", encoding="utf-8")
        (self.cfg / "temas.txt").write_text("", encoding="utf-8")
        names = build_index.build_all(out, self.cfg, None, check_count=False)
        shards = sorted(n for n in names if n.startswith("indice-leis"))
        self.assertEqual(shards[:2], ["indice-leis-2000-a.md", "indice-leis-2000-b.md"])
        ids = []
        for s in shards:
            self.assertLessEqual((out / s).stat().st_size, 40 * 1024)
            ids += re.findall(r"(?m)^\| (lei-\d+-\d+) ", (out / s).read_text(encoding="utf-8"))
        self.assertEqual(len(ids), 401)                       # nothing lost
        self.assertEqual(ids[:400], sorted(ids[:400]))        # id order inside the year
        manifest = (out / "indice.md").read_text(encoding="utf-8")
        self.assertIn("| indice-leis-2000-a.md | Lei | 2000 | 2000 |", manifest)
        self.assertIn("| indice-leis-2000-b.md | Lei | 2000 | 2000 |", manifest)
        self.assertEqual(validate.validate(out, ["Lei"])[0], [])



class Revoked(IndexCase):
    def test_revoked_list_merges_old_and_new_rows_and_drops_diplomas_in_force_again(self):
        out = self.build()
        repo = self.tmp / "repo"
        repo.mkdir()
        (repo / "revogados.md").write_text(
            "# Diplomas revogados\n\n| id | título | data da revogação | ligação oficial |\n|---|---|---|---|\n"
            "| lei-9-1990 | Lei n.º 9/90 | 2001-02-03 | https://example.org/a |\n"
            "| lei-24-1996 | Lei n.º 24/96 | 2001-02-03 | https://example.org/b |\n", encoding="utf-8")
        new = [{"id": "lei-5-1980", "title": "Lei n.º 5/80", "date": "2026-01-02", "source": "https://example.org/c"}]
        self.run_index(out, repo_dir=repo, revoked_new=new)
        rows = build_index.parse_revoked(out / "revogados.md")
        self.assertEqual([r["id"] for r in rows], ["lei-5-1980", "lei-9-1990"])   # lei-24-1996 is in force again
        self.assertEqual(rows[0]["date"], "2026-01-02")


if __name__ == "__main__":
    unittest.main()


class ShardColumns(IndexCase):
    def test_shards_have_source_last_amended_and_text_version_and_list_only_overviews(self):
        out = self.build()
        self.run_index(out)
        head = "| id | título | caminho | nome comum | siglas | sumário | source | last_amended | text_version |"
        lei = (out / "indice-leis.md").read_text(encoding="utf-8").splitlines()
        self.assertIn(head, lei)
        row = [c.strip() for c in next(l for l in lei if l.startswith("| lei-24-1996")).strip("|").split(" | ")]
        self.assertEqual(row[6:], ["https://diariodarepublica.pt/dr/legislacao-consolidada/lei/1996-34491075", "2023-07-04", "consolidado"])
        dlr = (out / "indice-decretos-legislativos-regionais.md").read_text(encoding="utf-8")
        orig = next(l for l in dlr.splitlines() if l.startswith("| decreto-legislativo-regional-15-1996-a"))
        self.assertTrue(orig.rstrip().endswith("|  | original sem alterações |"))      # no last_amended for originals
        cod = (out / "indice-codigos.md").read_text(encoding="utf-8")
        self.assertEqual(cod.count("| decreto-lei-330-1990"), 1)                # parts are not listed
        self.assertNotIn("diploma-de-aprovacao", cod)
        self.assertLessEqual((out / "indice-leis.md").stat().st_size, 40 * 1024)
