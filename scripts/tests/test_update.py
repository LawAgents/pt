"""test.update_failure: a failed update leaves the repo untouched; plus end-to-end behaviour of run_update."""
import contextlib
import io
import json
import os
import subprocess
import unittest
from unittest import mock

from helpers import DLR_7_99, FakeClock, FakeServer, LEI_24_96, REVOKED_808, TmpCase, common, load_raw_record

import check_size
import convert
import run_update


def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


class UpdateCase(TmpCase):
    def setUp(self):
        super().setUp()
        self.raw, self.repo = self.tmp / "raw", self.tmp / "repo"
        self.repo.mkdir()
        self.cfg = self.config_dir()
        self.clock = FakeClock()
        self.server = FakeServer(self.clock)

    def run_update(self, mode="initial", **kw):
        out = io.StringIO()
        kw.setdefault("dre", self.server.dre())
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = run_update.run(mode, self.raw, self.repo, config=self.cfg, count_check=False, clock=self.clock, **kw)
        return rc, out.getvalue()

    def errors(self):
        return json.loads((self.raw / "errors.json").read_text(encoding="utf-8"))


class Success(UpdateCase):
    def test_initial_then_weekly_without_changes(self):
        github_output = self.tmp / "gh_output"
        with mock.patch.dict(os.environ, {"GITHUB_OUTPUT": str(github_output)}):
            rc, out = self.run_update("initial")
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=true", out.splitlines())
        self.assertEqual(github_output.read_text(encoding="utf-8").strip(), "CHANGED=true")
        self.assertTrue((self.repo / "leis/1996/lei-24-1996.md").exists())
        self.assertTrue((self.repo / "codigos/codigo-da-publicidade/decreto-lei-330-1990.md").exists())
        self.assertTrue((self.repo / "indice.md").exists())
        self.assertFalse((self.repo / "leis/1996/lei-24-1996.md.tmp").exists())
        self.assertFalse((self.raw / "errors.json").exists())
        before = snapshot(self.repo)
        rc, out = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=false", out.splitlines())
        self.assertEqual(snapshot(self.repo), before)

    def test_weekly_changes_only_the_changed_diploma(self):
        self.run_update("initial")
        before = snapshot(self.repo)
        rec = self.server.records[DLR_7_99]
        rec["data"]["DataUltimaConsolidada"] = "2030-05-05"
        rc, out = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual((rc, "CHANGED=true" in out), (0, True))
        after = snapshot(self.repo)
        changed = sorted(k for k in after if before.get(k) != after[k])
        self.assertEqual(changed, ["decretos-legislativos-regionais/1999/decreto-legislativo-regional-7-1999-a.md",
                                   "indice-decretos-legislativos-regionais.md"])  # the shard shows last_amended
        self.assertIn(b"last_amended: 2030-05-05", after[changed[0]])
        self.assertIn(b"2030-05-05", after[changed[1]])

    def test_diploma_that_left_force_is_removed_and_listed_as_revoked(self):
        self.run_update("initial")
        path = self.repo / "leis/1996/lei-24-1996.md"
        self.assertTrue(path.exists())
        # the hand-written lists must not name a diploma that is gone (rule.common_names_list)
        (self.cfg / "nomes-comuns.txt").write_text("decreto-lei-330-1990 | Código da Publicidade | CPub\n", encoding="utf-8")
        (self.cfg / "temas.txt").write_text("decreto-lei-330-1990 | Publicidade\n", encoding="utf-8")
        rec = self.server.records[LEI_24_96]
        rec["search"].update(consolidacaoEstado="REVOKED", vigencia="NAO_VIGENTE")
        rec["data"] = load_raw_record(REVOKED_808)["data"]   # the real data of a revoked diploma (note: em vigor a partir de 2020-01-29)
        rc, out = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 0)
        self.assertFalse(path.exists())
        self.assertFalse(path.parent.exists())          # empty folder pruned
        text = (self.repo / "revogados.md").read_text(encoding="utf-8")
        self.assertIn("| lei-24-1996 | Lei n.º 24/96, de 31 de julho | 2020-01-29 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/", text)
        self.assertNotIn("lei-24-1996", (self.repo / "indice-leis.md").read_text(encoding="utf-8") if (self.repo / "indice-leis.md").exists() else "")

    def test_other_files_of_the_repo_are_never_touched(self):
        for rel in ("README.md", "scripts/x.py", "config/y.txt", "spec/z.xml", "plugin/a.md", "leis/README.md"):
            (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / rel).write_text("keep", encoding="utf-8")
        self.run_update("initial")
        for rel in ("README.md", "scripts/x.py", "config/y.txt", "spec/z.xml", "plugin/a.md", "leis/README.md"):
            self.assertEqual((self.repo / rel).read_text(encoding="utf-8"), "keep")


class UpdateFailure(UpdateCase):
    def setUp(self):
        super().setUp()
        self.run_update("initial")
        self.before = snapshot(self.repo)

    def assertUntouched(self):
        self.assertEqual(snapshot(self.repo), self.before)

    def test_validation_error_blocks_everything(self):
        self.server.records[DLR_7_99]["search"]["tipo"] = "Tipo Inventado"
        rc, out = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        self.assertNotIn("CHANGED", out)
        err = self.errors()
        self.assertEqual(err["stage"], "validate")
        self.assertIn("unknown_type", {e["code"] for e in err["errors"]})
        self.assertUntouched()

    def test_article_count_different_from_the_dre_blocks(self):
        real = convert.dre_article_count
        # the DRE data says one more article than the markdown shows (as if the converter had lost one)
        with mock.patch.object(convert, "dre_article_count", lambda rec: (real(rec) or 0) + 1 if rec["search"]["dbId"] == LEI_24_96 else real(rec)):
            rc, _ = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        self.assertEqual({e["code"] for e in self.errors()["errors"]}, {"article_count_mismatch"})
        self.assertUntouched()

    def test_dre_services_change_blocks(self):
        self.server.fault = lambda n, url: "garbage" if n > 3 else None
        rc, _ = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        self.assertEqual(self.errors()["stage"], "fetch")
        self.assertUntouched()

    def test_server_asking_to_slow_down_blocks(self):
        self.server.fault = lambda n, url: 503
        rc, _ = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        self.assertUntouched()

    def test_index_failure_blocks(self):
        (self.cfg / "nomes-comuns.txt").write_text("nao-existe-1-2000 | Nome | N\n", encoding="utf-8")
        rc, _ = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        err = self.errors()
        self.assertEqual((err["stage"], err["errors"][0]["code"]), ("index", "index_error"))
        self.assertUntouched()

    def test_repo_over_the_size_limit_blocks(self):
        rc, _ = self.run_update("weekly", dre=self.server.dre(), size_limit=1000)
        self.assertEqual(rc, 1)
        self.assertEqual(self.errors()["errors"][0]["code"], "repo_too_big")
        self.assertUntouched()

    def test_unexpected_exception_is_a_failure_not_a_half_written_repo(self):
        with mock.patch.object(convert, "convert_all", side_effect=RuntimeError("boom")):
            rc, _ = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        self.assertEqual(self.errors()["errors"][0]["code"], "internal_error")
        self.assertUntouched()

    def test_copy_failure_during_the_swap_is_rolled_back(self):
        self.server.records[DLR_7_99]["data"]["DataUltimaConsolidada"] = "2031-01-01"
        self.server.records[LEI_24_96]["data"]["DataUltimaConsolidada"] = "2031-01-01"
        real = common.atomic_write
        calls = []

        def flaky(path, data, binary=False):
            calls.append(path)
            if len(calls) == 2 and "stage" not in str(path):
                raise OSError("disk full")
            return real(path, data, binary)

        with mock.patch.object(run_update, "atomic_write", flaky):
            rc, _ = self.run_update("weekly", dre=self.server.dre())
        self.assertEqual(rc, 1)
        self.assertUntouched()


class Budget(UpdateCase):
    def test_budget_reached_exit_2_leaves_the_repo_untouched_and_the_next_run_finishes(self):
        self.server.add_clones(10)
        rc, out = self.run_update("initial", budget_seconds=9)
        self.assertEqual(rc, 2)
        self.assertEqual(snapshot(self.repo), {})
        self.assertNotIn("CHANGED", out)
        self.assertFalse((self.raw / "errors.json").exists())
        rc, out = self.run_update("initial", dre=self.server.dre(), budget_seconds=100000)
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=true", out)
        self.assertEqual(len(self.server.requests_to("DataActionGetData")), 14)   # each in-force diploma exactly once


class CheckSize(TmpCase):
    def git(self, *args):
        subprocess.run(["git", "-C", str(self.tmp), *args], check=True, capture_output=True)

    def test_prints_both_numbers_and_fails_over_the_limit(self):
        self.git("init", "-q")
        (self.tmp / "a.bin").write_bytes(b"x" * 5000)
        self.git("add", "a.bin")
        self.git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "x")
        ok, objs, work = check_size.check(self.tmp)
        self.assertTrue(ok)
        self.assertEqual(work, 5000)
        self.assertGreaterEqual(objs, 0)
        self.assertFalse(check_size.check(self.tmp, limit=4000)[0])           # tracked tree too big
        self.assertFalse(check_size.check(self.tmp, limit=objs - 1)[0])       # git objects too big
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = check_size.main(["--repo", str(self.tmp), "--limit-bytes", "4000"])
        self.assertEqual(rc, 1)
        self.assertIn("git objects:", buf.getvalue())
        self.assertIn("working tree: 5000 bytes", buf.getvalue())
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(check_size.main(["--repo", str(self.tmp)]), 0)

    def test_untracked_files_do_not_count_but_a_given_tree_does(self):
        self.git("init", "-q")
        (self.tmp / "big.bin").write_bytes(b"x" * 9000)    # untracked
        self.assertEqual(check_size.check(self.tmp)[2], 0)
        self.assertEqual(check_size.check(self.tmp, tree=self.tmp)[2], 9000)


if __name__ == "__main__":
    unittest.main()


class Cli(UpdateCase):
    def test_main_wires_the_arguments_and_enforces_the_30_to_50_names_rule(self):
        with mock.patch.object(run_update, "DRE", lambda: self.server.dre()), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = run_update.main(["--mode", "initial", "--raw", str(self.raw), "--repo", str(self.repo),
                                  "--config", str(self.cfg), "--budget-seconds", "100000"])
        self.assertEqual(rc, 1)                              # the fixture list has 2 entries, the rule asks for 30 to 50
        err = self.errors()
        self.assertEqual(err["stage"], "index")
        self.assertIn("30 to 50", err["errors"][0]["message"])
        self.assertEqual(snapshot(self.repo), {})
