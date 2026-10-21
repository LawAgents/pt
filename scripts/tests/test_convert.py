"""Converter tests: smoke comparison with LawCodex, headings, revoked articles, ids, parts, originals."""
import unittest

from helpers import DLR_15_96, DLR_7_99, FIX, LEI_24_96, PUBLICIDADE, common, load_raw_record

import convert
from convert import Item


def conv(db_id, act_id, codes=("34537375",), max_bytes=convert.DEFAULT_MAX_PART_BYTES):
    return convert.convert_record(load_raw_record(db_id), act_id, set(codes), max_bytes)


def articles_of(act):
    out = []
    for rel, text in act.files:
        meta, body = common.parse_frontmatter(text)
        out += [(h, b) for h, b in common.split_articles(body)]
    return out


class Smoke(unittest.TestCase):
    def test_lei_24_96_has_the_same_article_text_as_lawcodex_in_the_new_schema(self):
        act = conv(LEI_24_96, "lei-24-1996")
        self.assertEqual(len(act.files), 1)
        rel, text = act.files[0]
        self.assertEqual(rel, "leis/1996/lei-24-1996.md")
        lc_meta, lc_body = common.parse_frontmatter((FIX / "lawcodex" / "lei-24-96.md").read_text(encoding="utf-8"))
        ours = common.split_articles(common.parse_frontmatter(text)[1])
        theirs = common.split_articles(lc_body)
        self.assertEqual(len(ours), len(theirs))
        self.assertEqual(len(ours), convert.dre_article_count(load_raw_record(LEI_24_96)))
        for (h1, b1), (h2, b2) in zip(ours, theirs):
            self.assertEqual(h1, h2)
            self.assertEqual(b1, b2, h1)
        # the whole body (preamble, chapters, amendment notes) is the same too, apart from the H1 title line
        ours_body = common.parse_frontmatter(text)[1].split("\n", 2)[2]
        their_body = lc_body.split("\n", 2)[2]
        self.assertEqual(ours_body.strip(), their_body.strip())

    def test_front_matter_follows_the_schema(self):
        meta, body = common.parse_frontmatter(conv(LEI_24_96, "lei-24-1996").files[0][1])
        self.assertEqual(meta["id"], "lei-24-1996")
        self.assertEqual(meta["dre_id"], "406882")
        self.assertEqual(meta["title"], "Lei n.º 24/96, de 31 de julho")
        self.assertEqual((meta["type"], meta["number"], meta["year"], meta["date"]), ("Lei", "24/96", 1996, "1996-07-31"))
        self.assertEqual((meta["status"], meta["text_version"], meta["last_amended"]), ("em vigor", "consolidado", "2023-07-04"))
        self.assertTrue(meta["source"].startswith("https://diariodarepublica.pt/dr/legislacao-consolidada/lei/"))
        self.assertIn("/eli/", meta["eli"])
        self.assertTrue(meta["original_pdf"].endswith(".pdf"))
        self.assertRegex(meta["retrieved"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertEqual(meta["legal_notice"], common.LEGAL_NOTICE)
        self.assertNotIn("part_of", meta)
        self.assertNotIn("part", meta)
        self.assertTrue(body.strip().startswith("# Lei n.º 24/96, de 31 de julho"))

    def test_front_matter_lines_are_flat_json_quoted_strings(self):
        text = conv(LEI_24_96, "lei-24-1996").files[0][1]
        head = text.split("\n---\n")[0].splitlines()[1:]
        for ln in head:
            k, v = ln.split(": ", 1)
            if k in ("year",):
                self.assertTrue(v.isdigit())
            elif k in ("date", "last_amended", "retrieved"):
                self.assertRegex(v, r"^\d{4}-\d{2}-\d{2}$")
            else:
                self.assertTrue(v.startswith('"') and v.endswith('"'), ln)

    def test_revoked_article_keeps_its_heading_and_the_official_mark(self):
        text = conv(LEI_24_96, "lei-24-1996").files[0][1]
        revoked = [(h, b) for h, b in common.split_articles(text) if b.startswith("*(Revogado)*")]
        self.assertEqual(len(revoked), 3)
        h, b = revoked[0]
        self.assertTrue(h.startswith("Artigo "))
        self.assertIn("Revogado pelo/a Artigo", b)
        self.assertNotIn("O fornecedor de bens deve entregar", b)  # no text of the old version

    def test_article_headings_have_the_schema_shape(self):
        for db, act_id in ((LEI_24_96, "lei-24-1996"), (DLR_7_99, "decreto-legislativo-regional-7-1999-a")):
            for rel, text in conv(db, act_id).files:
                for line in text.splitlines():
                    if line.startswith("#") and "Artigo" in line.split(" ", 2)[1:2] + [""]:
                        self.assertRegex(line, r"^#{1,6} Artigo \S+")

    def test_article_count_matches_the_dre_data(self):
        for db, act_id in ((LEI_24_96, "lei-24-1996"), (PUBLICIDADE, "decreto-lei-330-1990"), (DLR_7_99, "x-7-1999-a")):
            rec = load_raw_record(db)
            self.assertEqual(len(articles_of(conv(db, act_id))), convert.dre_article_count(rec))


class Parts(unittest.TestCase):
    def test_code_with_approval_decree_is_split_so_article_numbers_stay_unique(self):
        act = conv(PUBLICIDADE, "decreto-lei-330-1990")
        paths = [rel for rel, _ in act.files]
        self.assertEqual(paths[0], "codigos/codigo-da-publicidade/decreto-lei-330-1990.md")  # overview first
        self.assertEqual(act.parts, ["decreto-lei-330-1990-diploma-de-aprovacao", "decreto-lei-330-1990-anexo-codigo-da-publicidade"])
        metas = {common.parse_frontmatter(t)[0]["id"]: common.parse_frontmatter(t)[0] for _, t in act.files}
        for pid in act.parts:
            self.assertEqual(metas[pid]["part_of"], "decreto-lei-330-1990")
            self.assertEqual(metas[pid]["dre_id"], "565417")
        self.assertEqual(metas[act.parts[0]]["part"], "Diploma de aprovação")
        for rel, text in act.files[1:]:
            nums = [common.article_number(h) for h, _ in common.split_articles(text)]
            self.assertEqual(len(nums), len(set(nums)), rel)
        overview = common.parse_frontmatter(act.files[0][1])
        self.assertNotIn("part_of", overview[0])
        self.assertIn("| Diploma de aprovação | codigos/codigo-da-publicidade/decreto-lei-330-1990-diploma-de-aprovacao.md | 1.º | 3.º |", overview[1])
        self.assertEqual(common.split_articles(overview[1]), [])  # the overview holds no articles

    def test_oversized_code_is_split_by_its_structure(self):
        act = conv(PUBLICIDADE, "decreto-lei-330-1990", max_bytes=12_000)
        self.assertGreater(len(act.parts), 2)
        titles = [common.parse_frontmatter(t)[0]["part"] for _, t in act.files[1:]]
        self.assertEqual(titles[0], "Diploma de aprovação")
        self.assertTrue(any(t.startswith("Capítulo") for t in titles))
        for _, t in act.files[1:]:
            self.assertLessEqual(len(t.encode()), 12_000 * 1.6)  # packing is by whole units, never mid-article
        total = sum(len(common.split_articles(t)) for _, t in act.files[1:])
        self.assertEqual(total, convert.dre_article_count(load_raw_record(PUBLICIDADE)))

    def test_pack_never_repeats_an_article_number_in_one_part(self):
        def art(n):
            return Item(1, 11, f"Artigo {n}.º", f"Artigo {n}.º", f"## Artigo {n}.º\n\ntext")
        items = [art(1), art(2), Item(1, 14, "Anexo", "Anexo", "## Anexo"), Item(2, 11, "Artigo 1.º", "Artigo 1.º", "### Artigo 1.º\n\nx")]
        parts = convert.split_parts(items, 10_000)
        self.assertEqual(len(parts), 2)
        self.assertEqual(parts[0][0], "Diploma de aprovação")

    def test_small_diploma_stays_in_one_file(self):
        act = conv(LEI_24_96, "lei-24-1996")
        self.assertEqual((len(act.files), act.parts), (1, []))

    def test_part_titles_are_unique(self):
        act = conv(PUBLICIDADE, "decreto-lei-330-1990", max_bytes=3_000)
        ids = [common.parse_frontmatter(t)[0]["id"] for _, t in act.files]
        self.assertEqual(len(ids), len(set(ids)))


class Originals(unittest.TestCase):
    def test_original_text_gets_article_headings_from_the_dre_markup(self):
        act = conv(DLR_15_96, "decreto-legislativo-regional-15-1996-a")
        meta, body = common.parse_frontmatter(act.files[0][1])
        self.assertEqual(meta["text_version"], "original sem alterações")
        self.assertNotIn("last_amended", meta)
        arts = common.split_articles(body)
        self.assertGreaterEqual(len(arts), 5)
        self.assertEqual(arts[0][0], "Artigo 1.º (Objecto)")
        self.assertIn("estabelece os princípios", arts[0][1])
        self.assertTrue(all(b.strip() for _, b in arts))

    def test_original_has_no_dre_article_count(self):
        self.assertIsNone(convert.dre_article_count(load_raw_record(DLR_15_96)))


class Ids(unittest.TestCase):
    def src(self, **kw):
        s = {"dbId": 1, "tipo": "Lei", "numero": "24/96", "ano": "1996", "emissor": "Assembleia da República"}
        s.update(kw)
        return s

    def test_formats(self):
        b = convert.base_id
        self.assertEqual(b(self.src()), "lei-24-1996")
        self.assertEqual(b(self.src(tipo="Decreto-Lei", numero="84/2021", ano="2021")), "decreto-lei-84-2021")
        self.assertEqual(b(self.src(tipo="Decreto Legislativo Regional", numero="5/2020/A", ano="2020")), "decreto-legislativo-regional-5-2020-a")
        self.assertEqual(b(self.src(tipo="Decreto Legislativo Regional", numero="15/96/M", ano="1996")), "decreto-legislativo-regional-15-1996-m")
        self.assertEqual(b(self.src(tipo="Portaria", numero="268-A/2012", ano="2012")), "portaria-268-a-2012")
        self.assertEqual(b(self.src(tipo="Edital", numero="", ano="2021", dbId=123456)), "edital-2021-dre-123456")
        self.assertEqual(b(self.src(tipo="Decreto do Presidente da República", numero="1/2020", ano="2020")), "decreto-presidente-republica-1-2020")

    def test_repeated_numbering_gets_the_issuer_then_the_dre_id(self):
        a = self.src(dbId=1, tipo="Aviso", numero="12/2019", ano="2019", emissor="Banco de Portugal")
        b = self.src(dbId=2, tipo="Aviso", numero="12/2019", ano="2019", emissor="Ministério das Finanças")
        c = self.src(dbId=3, tipo="Aviso", numero="12/2019", ano="2019", emissor="Banco de Portugal")
        ids = convert.assign_ids([a, b, c])
        self.assertEqual(ids[2], "aviso-12-2019-ministerio-financas")
        self.assertEqual(ids[1], "aviso-12-2019-dre-1")  # same issuer twice: DRE id as last resort
        self.assertEqual(ids[3], "aviso-12-2019-dre-3")
        self.assertEqual(len(set(ids.values())), 3)

    def test_ids_already_in_the_repo_never_change(self):
        a = self.src(dbId=1, tipo="Aviso", numero="12/2019", ano="2019", emissor="Banco de Portugal")
        b = self.src(dbId=2, tipo="Aviso", numero="12/2019", ano="2019", emissor="Ministério das Finanças")
        ids = convert.assign_ids([a, b], {1: "aviso-12-2019"})
        self.assertEqual(ids[1], "aviso-12-2019")
        self.assertNotEqual(ids[2], "aviso-12-2019")
        self.assertEqual(len(set(ids.values())), 2)

    def test_no_duplicates_in_a_large_synthetic_set(self):
        entries = [self.src(dbId=i, numero=f"{i % 50}/2020", ano="2020", emissor=f"E{i % 3}") for i in range(500)]
        ids = convert.assign_ids(entries)
        self.assertEqual(len(set(ids.values())), 500)


class Layout(unittest.TestCase):
    def test_paths(self):
        self.assertEqual(conv(DLR_7_99, "decreto-legislativo-regional-7-1999-a").files[0][0],
                         "decretos-legislativos-regionais/1999/decreto-legislativo-regional-7-1999-a.md")
        self.assertEqual(convert.type_dir("Aviso do Banco de Portugal"), "outros/aviso-banco-portugal")
        self.assertEqual(convert.index_group("outros/edital/2021/x.md"), "outros/edital")
        self.assertEqual(convert.index_group("leis/1996/x.md"), "leis")

    def test_convert_all_writes_only_in_force_diplomas(self):
        import tempfile, shutil
        out = tempfile.mkdtemp()
        try:
            acts, errors = convert.convert_all(FIX / "raw", out, log=lambda m: None)
            self.assertEqual(errors, [])
            self.assertEqual(sorted(a.dre_id for a in acts), [145612, 406882, 407287, 565417])  # 142345 is revoked
        finally:
            shutil.rmtree(out, ignore_errors=True)

    def test_a_record_without_text_is_a_conversion_error_not_a_crash(self):
        rec = load_raw_record(LEI_24_96)
        rec["data"]["LegConsBase"]["List"] = []
        rec["original"] = None
        with self.assertRaises(ValueError):
            convert.convert_record(rec, "lei-24-1996", set())


if __name__ == "__main__":
    unittest.main()


def synthetic_code(livros, text="Lorem ipsum dolor sit amet. " * 60):
    """A raw record shaped like a big code: approval decree (articles 1-2) + Anexo with Livros > Titulos > Artigos."""
    def frag(nivel, tipo, tituo, epi="", texto=""):
        return {"IsHidden": False, "Nivel": nivel,
                "ConsolidacaoFragmento": {"AssociacaoDescription": ""},
                "FragmentoVersao": {"TipoFragmentoId": tipo, "VersaoEstadoId": 6, "Tituo": tituo, "Identificacao": "",
                                    "Epigrafe": epi, "Texto": texto},
                "AlteracoesList": {"List": []}}
    frags = [frag(0, 15, "Diploma", texto="Preâmbulo."), frag(1, 11, "Artigo 1.º", "Aprovação", "Aprovado."),
             frag(1, 11, "Artigo 2.º", "Vigência", "Vigora."), frag(1, 14, "Anexo", "Código Grande")]
    n = 0
    for li, titulos in enumerate(livros, 1):
        frags.append(frag(2, 2, f"Livro {li}", f"Parte {li}"))
        for ti, arts in enumerate(titulos, 1):
            frags.append(frag(3, 3, f"Título {ti}", "Matéria"))
            for _ in range(arts):
                n += 1
                frags.append(frag(4, 11, f"Artigo {n}.º", "Epígrafe", text))
    rec = load_raw_record(PUBLICIDADE)
    rec["data"]["LegConsBase"]["List"] = frags
    rec["search"]["dbId"] = 777
    return rec, n


class BigCode(unittest.TestCase):
    def test_a_big_code_is_split_into_parts_under_90_kb_with_a_structure_outline(self):
        import time
        rec, n = synthetic_code([[40, 40, 30], [90, 80, 60], [30, 20], [40, 40], [20]])
        t0 = time.time()
        act = convert.convert_record(rec, "decreto-lei-1-2000", {"34537375"})
        self.assertLess(time.time() - t0, 5)
        sizes = [len(t.encode()) for _, t in act.files[1:]]
        self.assertGreater(sum(sizes), 600_000)
        self.assertGreater(len(act.parts), 3)
        # a part is closed before it passes the limit; an indivisible unit (a Titulo) may overshoot by its own size
        self.assertTrue(all(s <= 90 * 1024 for s in sizes), sizes)
        total = 0
        for rel, text in act.files[1:]:
            arts = common.split_articles(text)
            nums = [common.article_number(h) for h, _ in arts]
            self.assertEqual(len(nums), len(set(nums)), rel)
            total += len(arts)
        self.assertEqual(total, n + 2)
        first = common.parse_frontmatter(act.files[1][1])[0]
        self.assertEqual(first["part"], "Diploma de aprovação")
        parts = [common.parse_frontmatter(t)[0]["part"] for _, t in act.files[2:]]
        self.assertTrue(parts[0].startswith("Livro 1"), parts)
        self.assertTrue(any(x.startswith("Livro 2, Título 2") for x in parts), parts)
        self.assertEqual(len(parts), len(set(parts)))
        overview = act.files[0][1]
        self.assertLess(len(overview.encode()), 60_000)
        for pid in act.parts:
            self.assertIn(pid, overview)
        # outline: structural headings only, in order, each followed by the part file where it lives
        outline = overview.split("## Estrutura")[1].strip().splitlines()
        self.assertNotIn("Artigo", " ".join(outline))
        self.assertTrue(outline[0].startswith("- Anexo"))
        self.assertTrue(all(l.rstrip().endswith(".md)") for l in outline))
        self.assertIn("  - Livro 1 — Parte 1 (decreto-lei-1-2000-livro-1", outline[1])
        by_file = {common.parse_frontmatter(t)[0]["id"] + ".md": t for _, t in act.files[1:]}
        for line in outline:
            label, fname = line.strip()[2:].rsplit(" (", 1)
            self.assertIn("# " + label.split(" — ")[0], by_file[fname.rstrip(")")])

    def test_single_article_larger_than_the_cap_stays_whole(self):
        rec, _ = synthetic_code([[3]], text="Palavra. " * 20_000)  # each article about 180 KB
        act = convert.convert_record(rec, "decreto-lei-1-2000", {"34537375"})
        arts = [h for _, t in act.files[1:] for h, _ in common.split_articles(t)]
        self.assertEqual(len(arts), 5)
        self.assertGreater(len(act.parts), 3)    # one article per part: never cut inside an article


class HeadingLabels(unittest.TestCase):
    def frag(self, **kw):
        f = {"TipoFragmentoId": 11, "Tituo": "", "Identificacao": "", "Epigrafe": ""}
        f.update(kw)
        return f

    def test_labels(self):
        h = convert.heading_label
        self.assertEqual(h(self.frag(Tituo="ARTIGO ÚNICO")), "Artigo ÚNICO")
        self.assertEqual(h(self.frag(Identificacao="12.º")), "Artigo 12.º")           # bare number
        self.assertEqual(h(self.frag(Tituo="Artigo 9.º-B", Epigrafe="Entrega")), "Artigo 9.º-B — Entrega")
        self.assertEqual(h(self.frag(Tituo="Artigo 483.º", Epigrafe="(Princípio geral)")), "Artigo 483.º (Princípio geral)")
        self.assertEqual(h(self.frag(TipoFragmentoId=1, Tituo="Capítulo I", Epigrafe="Geral")), "Capítulo I — Geral")

    def test_article_fragments_without_an_artigo_heading_are_not_counted_but_reported(self):
        rec = load_raw_record(LEI_24_96)
        n = convert.dre_article_count(rec)
        for x in rec["data"]["LegConsBase"]["List"]:
            if x["FragmentoVersao"].get("TipoFragmentoId") == 11:
                x["FragmentoVersao"]["Tituo"] = "Base I"
                break
        self.assertEqual(convert.dre_article_count(rec), n - 1)
        self.assertEqual(convert.dre_other_article_headings(rec), 1)


class PartNames(unittest.TestCase):
    def test_a_pipe_in_an_annex_title_does_not_break_the_overview_table(self):
        rec, _ = synthetic_code([[2]])
        for x in rec["data"]["LegConsBase"]["List"]:
            if x["FragmentoVersao"]["Tituo"] == "Anexo":
                x["FragmentoVersao"]["Epigrafe"] = "Plano 21|23"
        act = convert.convert_record(rec, "decreto-lei-1-2000", {"34537375"})
        rows = [l for l in act.files[0][1].splitlines() if l.startswith("| Anexo")]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].count("|"), 5)


def _frag(nivel, tipo, tituo, epi="", texto=""):
    return {"IsHidden": False, "Nivel": nivel, "ConsolidacaoFragmento": {"AssociacaoDescription": ""},
            "FragmentoVersao": {"TipoFragmentoId": tipo, "VersaoEstadoId": 6, "Tituo": tituo, "Identificacao": "",
                                "Epigrafe": epi, "Texto": texto},
            "AlteracoesList": {"List": []}}


def constitution_like(text="Lorem ipsum dolor sit amet. " * 60):
    """Like the real Constitution: no approving decree; the first level-1 block has the 'annex' fragment type."""
    frags = [_frag(0, 15, "Diploma", texto="Preâmbulo."), _frag(1, 14, "Princípios fundamentais")]
    n = 0
    for _ in range(20):
        n += 1
        frags.append(_frag(2, 11, f"Artigo {n}.º", "Princípio", text))
    for pi, ntit in enumerate((3, 2), 1):
        frags.append(_frag(1, 4, f"Parte {'I' * pi}", "Matéria"))
        for ti in range(1, ntit + 1):
            frags.append(_frag(2, 13, f"Título {'I' * ti}", "Assunto"))
            for _ in range(25):
                n += 1
                frags.append(_frag(3, 11, f"Artigo {n}.º", "Epígrafe", text))
    frags.append(_frag(1, 7, "Assinatura", texto="Assinado."))
    rec = load_raw_record(PUBLICIDADE)
    rec["data"]["LegConsBase"]["List"] = frags
    rec["search"].update(dbId=778, tipo="Decreto de Aprovação da Constituição", numero="")
    return rec, n


class ApprovalPart(unittest.TestCase):
    def meta_of(self, act):
        return [common.parse_frontmatter(t) for _, t in act.files]

    def test_constitution_like_diploma_has_no_approval_part_and_names_come_from_headings(self):
        rec, n = constitution_like()
        act = convert.convert_record(rec, "decreto-aprovacao-constituicao-1976-dre-778", set())
        parts = [m["part"] for m, _ in self.meta_of(act)[1:]]
        self.assertGreater(len(parts), 3)
        self.assertFalse(any("aprovação" in p for p in parts), parts)
        self.assertTrue(parts[0].startswith("Princípios fundamentais"), parts)
        for (m, body), p in zip(self.meta_of(act)[1:], parts):
            # every part is named after a structural heading it really contains (or its articles)
            heads = [l.lstrip("# ").split(" — ")[0] for l in body.splitlines() if l.startswith("## ") or l.startswith("### ")]
            first_word = p.split(",")[0].split(" a ")[0]
            self.assertTrue(first_word.startswith("Artigo") or any(first_word.startswith(h) or h.startswith(first_word) for h in heads)
                            or any(first_word in l for l in body.splitlines()[:40]), (p, heads[:3]))
        self.assertEqual(sum(len(common.split_articles(b)) for _, b in self.meta_of(act)[1:]), n)

    def test_approval_part_holds_only_the_decrees_own_articles(self):
        rec, n = synthetic_code([[40, 40], [30]])
        act = convert.convert_record(rec, "decreto-lei-1-2000", {"34537375"})
        metas = self.meta_of(act)[1:]
        approval = [(m, b) for m, b in metas if "aprovação" in m["part"]]
        self.assertEqual(len(approval), 1)
        self.assertEqual([common.article_number(h) for h, _ in common.split_articles(approval[0][1])], ["1.º", "2.º"])
        self.assertEqual(metas[0][0]["part"], "Diploma de aprovação")
        for m, b in metas[1:]:
            self.assertNotIn("aprovação", m["part"])

    def test_overview_ranges_match_the_part_files_and_the_validator_catches_a_mismatch(self):
        import tempfile, shutil, validate
        rec, _ = constitution_like()
        act = convert.convert_record(rec, "decreto-aprovacao-constituicao-1976-dre-778", set())
        out = tempfile.mkdtemp()
        try:
            for rel, text in act.files:
                p = common.Path(out) / rel if hasattr(common, "Path") else __import__("pathlib").Path(out) / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text, encoding="utf-8")
            types = common.load_act_types(__import__("pathlib").Path(__file__).resolve().parents[2] / "config" / "act-types.txt")
            errors, _ = validate.validate(out, types)
            self.assertEqual([e for e in errors if e["code"].startswith(("overview", "approval"))], [])
            ov = __import__("pathlib").Path(out) / act.files[0][0]
            ov.write_text(ov.read_text(encoding="utf-8").replace("| 1.º |", "| 2.º |", 1), encoding="utf-8")
            errors, _ = validate.validate(out, types)
            self.assertIn("overview_range_mismatch", {e["code"] for e in errors})
        finally:
            shutil.rmtree(out, ignore_errors=True)


class LongPartNames(unittest.TestCase):
    def unit(self, prefix, tituo, level=5):
        it = Item(level, 8, f"{tituo} — Epígrafe", tituo, f"{'#' * (level + 1)} {tituo}")
        return convert.Unit([it], False, level, prefix)

    def test_range_drops_the_segments_shared_with_the_first_end(self):
        a = self.unit("Livro I, Título II, Capítulo I", "Secção VI")
        b = self.unit("Livro I, Título II, Capítulo I", "Secção IX")
        self.assertEqual(convert.part_title([a, b], False), "Livro I, Título II, Capítulo I, Secção VI a Secção IX")
        c = self.unit("Livro I, Título II, Capítulo II, Secção IX", "Subsecção V")
        self.assertEqual(convert.part_title([a, c], False), "Livro I, Título II, Capítulo I, Secção VI a Capítulo II, Secção IX, Subsecção V")

    def test_long_names_are_cut_at_a_segment_boundary_with_an_ellipsis(self):
        long = ", ".join(f"Segmento número {n}" for n in range(1, 12))
        out = convert.fit(long)
        self.assertLessEqual(len(out), 91)
        self.assertTrue(out.endswith("…"))
        self.assertIn(out[:-1], long)
        self.assertTrue(long[len(out) - 1:].startswith(", "))        # the cut falls right before a ', '
        self.assertEqual(convert.fit("Livro I, Título II"), "Livro I, Título II")

    def test_file_names_do_not_get_the_ellipsis_and_stay_unique(self):
        rec, _ = synthetic_code([[40, 40, 30]] * 3, text="Palavra. " * 400)
        for x in rec["data"]["LegConsBase"]["List"]:
            if x["FragmentoVersao"]["Tituo"].startswith("Título"):
                x["FragmentoVersao"]["Tituo"] += " com um nome extraordinariamente comprido para forçar o corte do título da parte"
        act = convert.convert_record(rec, "decreto-lei-1-2000", {"34537375"}, max_bytes=20_000)
        ids, parts = [], []
        for rel, text in act.files[1:]:
            m = common.parse_frontmatter(text)[0]
            ids.append(m["id"]); parts.append(m["part"])
            self.assertTrue(rel.endswith(".md") and "…" not in rel and "…" not in m["id"])
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(len(p) <= 100 for p in parts), max(parts, key=len))
        self.assertTrue(any(p.endswith("…") for p in parts))
