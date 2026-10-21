"""Several requests in flight never start closer than min_interval (rule.fetch_rate, test.fetch_rate)."""
import sys
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import dre_client  # noqa: E402


class StartRate(unittest.TestCase):
    def test_starts_are_spaced_while_requests_overlap(self):
        starts, lock = [], threading.Lock()

        def transport(url, data, headers, timeout=None):
            with lock:
                starts.append(time.monotonic())
            time.sleep(0.3)  # slow server: responses overlap
            return 200, b"{}"

        dre = dre_client.DRE(transport=transport, min_interval=0.1)
        t0 = time.monotonic()
        with ThreadPoolExecutor(4) as pool:
            list(pool.map(lambda i: dre._request(f"http://x/{i}"), range(12)))
        elapsed = time.monotonic() - t0
        gaps = [b - a for a, b in zip(sorted(starts), sorted(starts)[1:])]
        self.assertGreaterEqual(min(gaps), 0.1 - 0.01)   # never faster than the interval
        self.assertLess(elapsed, 2.8)               # but overlapping beats strict one-at-a-time
        self.assertEqual(dre.requests, 12)

    def test_error_stops_every_thread(self):
        def transport(url, data, headers, timeout=None):
            return 429, b""

        dre = dre_client.DRE(transport=transport, min_interval=0.01)
        with self.assertRaises(dre_client.FetchAborted):
            dre._request("http://x/1")
        with self.assertRaises(dre_client.FetchAborted):
            dre._request("http://x/2")   # already aborted: no further request is made
        self.assertEqual(dre.requests, 1)


if __name__ == "__main__":
    unittest.main()
