"""test.fetch_rate and test.import_batches (TESTS.xml) against a simulated DRE server."""
import unittest

from helpers import DLR_15_96, FakeClock, FakeServer, LEI_24_96, REVOKED_808, TmpCase, common

import fetch


def gaps(server):
    t = [e[0] for e in server.log]
    return [b - a for a, b in zip(t, t[1:])]


class FetchRate(TmpCase):
    def run_fetch(self, server, mode="initial", **kw):
        return fetch.run_fetch(server.dre(), fetch.Raw(self.tmp / "raw"), mode, log=lambda m: None, **kw)

    def test_at_most_one_request_per_second_and_user_agent_on_every_request(self):
        clock = FakeClock()
        server = FakeServer(clock, latency=0.0)  # even with instant answers the client must wait
        self.assertEqual(self.run_fetch(server), 0)
        self.assertGreater(len(server.log), 10)
        self.assertGreaterEqual(min(gaps(server)), 0.55 - 1e-6)  # any two requests, including moduleinfo and the JS files
        self.assertGreaterEqual(min(gaps(server)), 0.5)  # the rule: at most 2 requests per second
        self.assertEqual({e[2] for e in server.log}, {common.USER_AGENT})
        self.assertIn("LawAgents-pt/", common.USER_AGENT)
        self.assertIn("https://github.com/LawAgents/pt", common.USER_AGENT)

    def test_stops_after_three_consecutive_errors(self):
        clock = FakeClock()
        server = FakeServer(clock)
        server.fault = lambda n, url: 500 if n >= 3 else None
        self.assertEqual(self.run_fetch(server), 1)
        failing = [e for e in server.log][2:]
        self.assertEqual(len(failing), 3)          # exactly 3 failed requests, then nothing more
        self.assertFalse((self.tmp / "raw" / "list.json").exists())  # no partial list

    def test_an_isolated_error_is_retried_and_resets_the_counter(self):
        clock = FakeClock()
        server = FakeServer(clock)
        server.fault = lambda n, url: 500 if n in (3, 5) else None
        self.assertEqual(self.run_fetch(server), 0)

    def test_network_errors_count_too(self):
        clock = FakeClock()
        server = FakeServer(clock)
        server.fault = lambda n, url: "oserror" if n >= 2 else None
        self.assertEqual(self.run_fetch(server), 1)
        self.assertEqual(len(server.log), 4)

    def test_stops_immediately_on_429_and_503(self):
        for status in (429, 503):
            with self.subTest(status=status):
                clock = FakeClock()
                server = FakeServer(clock)
                server.fault = lambda n, url, s=status: s if n == 2 else None
                self.assertEqual(self.run_fetch(server), 1)
                self.assertEqual(len(server.log), 2)  # the request that got the status was the last one

    def test_unknown_answer_shape_is_a_site_change(self):
        clock = FakeClock()
        server = FakeServer(clock)
        server.fault = lambda n, url: "garbage" if n == 1 else None
        self.assertEqual(self.run_fetch(server), 1)


class ImportBatches(TmpCase):
    def test_budget_exit_2_then_resume_without_repeating_work(self):
        clock = FakeClock()
        server = FakeServer(clock)
        server.add_clones(12)
        raw = fetch.Raw(self.tmp / "raw")
        dre = server.dre()
        total_in_force = sum(1 for s in server.list_entries() if fetch.selected(s))
        rc = fetch.run_fetch(dre, raw, "initial", budget_seconds=12, clock=clock, log=lambda m: None, with_eli=True)
        self.assertEqual(rc, 2)
        first = len(server.requests_to("DataActionGetData"))
        self.assertTrue(0 < first < total_in_force)
        # a fresh process (new client, same raw dir) resumes
        dre2 = server.dre()
        rc = fetch.run_fetch(dre2, raw, "initial", budget_seconds=10_000, clock=clock, log=lambda m: None, with_eli=True)
        self.assertEqual(rc, 0)
        self.assertEqual(len(server.requests_to("DataActionGetData")), total_in_force)  # every diploma fetched exactly once in total
        self.assertEqual(len(server.requests_to("DataActionGetPesquisas")),  # the list was not fetched again
                         -(-len(server.list_entries()) // 100))
        self.assertGreaterEqual(min(gaps(server)), 0.55 - 1e-6)
        for s in server.list_entries():
            if fetch.selected(s):
                self.assertTrue(raw.read(s["dbId"])["data"]["LegConsBase"]["List"] or raw.read(s["dbId"]).get("original"))

    def test_completed_initial_run_repeated_fetches_nothing(self):
        clock = FakeClock()
        server = FakeServer(clock)
        raw = fetch.Raw(self.tmp / "raw")
        self.assertEqual(fetch.run_fetch(server.dre(), raw, "initial", log=lambda m: None), 0)
        before = len(server.requests_to("DataActionGetData"))
        self.assertEqual(fetch.run_fetch(server.dre(), raw, "initial", log=lambda m: None), 0)
        self.assertEqual(len(server.requests_to("DataActionGetData")), before)

    def test_weekly_refetches_text_but_reuses_metadata_when_unchanged(self):
        clock = FakeClock()
        server = FakeServer(clock)
        raw = fetch.Raw(self.tmp / "raw")
        self.assertEqual(fetch.run_fetch(server.dre(), raw, "initial", log=lambda m: None, with_eli=True), 0)
        frag_before = len(server.requests_to("DataActionGetDiplomaFragByIdAndApplicationSetting"))
        self.assertEqual(fetch.run_fetch(server.dre(), raw, "weekly", log=lambda m: None, with_eli=True), 0)
        self.assertEqual(len(server.requests_to("DataActionGetDiplomaFragByIdAndApplicationSetting")), frag_before)
        # a changed text is detected and stored
        server.records[LEI_24_96]["data"]["DataUltimaConsolidada"] = "2030-01-01"
        self.assertEqual(fetch.run_fetch(server.dre(), raw, "weekly", log=lambda m: None, with_eli=True), 0)
        self.assertEqual(raw.read(LEI_24_96)["data"]["DataUltimaConsolidada"], "2030-01-01")
        self.assertGreater(len(server.requests_to("DataActionGetDiplomaFragByIdAndApplicationSetting")), frag_before)

    def test_eli_is_off_by_default_so_no_metadata_request(self):
        clock = FakeClock()
        server = FakeServer(clock)
        raw = fetch.Raw(self.tmp / "raw")
        self.assertEqual(fetch.run_fetch(server.dre(), raw, "initial", log=lambda m: None), 0)
        self.assertEqual(len(server.requests_to("DataActionGetDiplomaFragByIdAndApplicationSetting")), 0)
        self.assertTrue(raw.read(LEI_24_96)["url"].startswith("https://diariodarepublica.pt/dr/legislacao-consolidada/lei/"))

    def test_selection_rule_excludes_revoked(self):
        server = FakeServer(FakeClock())
        sel = {s["dbId"] for s in server.list_entries() if fetch.selected(s)}
        self.assertNotIn(REVOKED_808, sel)
        self.assertIn(DLR_15_96, sel)

    def test_raw_files_are_written_atomically(self):
        raw = fetch.Raw(self.tmp / "raw")
        raw.write(5, {"x": 1})
        self.assertEqual(raw.read(5), {"x": 1})
        self.assertEqual([p.name for p in (self.tmp / "raw" / "json").iterdir()], ["5.json.gz"])  # no .tmp left


if __name__ == "__main__":
    unittest.main()
