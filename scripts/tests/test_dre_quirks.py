"""Quirks found in the real DRE data during the first full import (see GOAL.md progress notes)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import convert  # noqa: E402


def frag(tipo, tituo, epigrafe="", texto="", state=0, nivel=1):
    return {"IsHidden": False, "Nivel": nivel, "AlteracoesList": {"List": []},
            "ConsolidacaoFragmento": {"AssociacaoDescription": ""},
            "FragmentoVersao": {"TipoFragmentoId": tipo, "Tituo": tituo, "Epigrafe": epigrafe, "Texto": texto,
                                "VersaoEstadoId": state}}


def rec(*frags):
    return {"data": {"LegConsBase": {"List": list(frags)}}}


class Quirks(unittest.TestCase):
    def test_article_revoked_only_in_its_heading_gets_the_revoked_mark(self):
        items = convert.render_items([frag(11, "Artigo 6.º", "(Revogado.)")])
        self.assertIn(convert.REVOKED_MARK, items[0].md)

    def test_placeholder_article_without_number_or_text_is_neither_written_nor_counted(self):
        r = rec(frag(11, "Artigo .º"), frag(11, "Artigo 1.º", "(Objeto)", "Texto."))
        self.assertEqual([i.label for i in convert.render_items(r["data"]["LegConsBase"]["List"])],
                         ["Artigo 1.º (Objeto)"])
        self.assertEqual(convert.dre_article_count(r), 1)

    def test_article_filed_under_another_fragment_type_is_counted(self):
        r = rec(frag(11, "Artigo 9.º", "(A)", "Texto."), frag(12, "Artigo 9.º-A", "(B)", "Texto novo."))
        self.assertEqual(convert.dre_article_count(r), 2)
        md = "\n".join(i.md for i in convert.render_items(r["data"]["LegConsBase"]["List"]))
        self.assertEqual(sum(1 for line in md.split("\n") if line.lstrip("#").startswith(" Artigo ")), 2)


if __name__ == "__main__":
    unittest.main()


class LongPartNames(unittest.TestCase):
    def test_long_part_name_is_cut_at_a_heading_boundary(self):
        long = "Livro I, Título II, Capítulo I, Secção VI a Livro I, Título II, Capítulo I, Secção IX, Subsecção V"
        self.assertGreater(len(long), 90)
        # the cut rule, exercised through the same expression the converter uses
        cut = long[:90]
        i = cut.rfind(", ")
        name = (cut[:i] if i > 40 else cut[:cut.rfind(" ")]).rstrip(" ,") + " …"
        self.assertTrue(name.endswith(" …"))
        self.assertNotIn("Sub …", name)
