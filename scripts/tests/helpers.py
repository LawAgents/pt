"""Shared test helpers: fixture loading, a fake clock and a simulated DRE server."""
import copy
import gzip
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
REPO = SCRIPTS.parent
FIX = HERE / "fixtures"
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402
import dre_client  # noqa: E402

LEI_24_96, PUBLICIDADE, DLR_7_99, DLR_15_96, REVOKED_808 = 406882, 565417, 145612, 407287, 142345


def load_raw_record(db_id):
    with gzip.open(FIX / "raw" / "json" / f"{db_id}.json.gz", "rt", encoding="utf-8") as fh:
        return json.load(fh)


class TmpCase(unittest.TestCase):
    """Test case with a temporary directory removed afterwards."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="leis-pt-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def config_dir(self):
        """Temp config: the real closed act-type list plus the fixture common names and themes."""
        cfg = self.tmp / "config"
        cfg.mkdir(exist_ok=True)
        shutil.copy(REPO / "config" / "act-types.txt", cfg / "act-types.txt")
        for n in ("nomes-comuns.txt", "temas.txt"):
            shutil.copy(FIX / "config" / n, cfg / n)
        return cfg

    def write_file(self, root, rel, meta, body):
        """Write a diploma file with a valid default front matter overridden by `meta`."""
        m = {"id": "lei-1-2000", "dre_id": "1", "title": "Lei n.º 1/2000, de 1 de janeiro", "type": "Lei",
             "number": "1/2000", "year": 2000, "date": "2000-01-01", "status": common.STATUS_IN_FORCE,
             "text_version": common.TEXT_CONSOLIDATED, "last_amended": "2001-01-01",
             "source": "https://diariodarepublica.pt/dr/x", "retrieved": "2026-10-21",
             "legal_notice": common.LEGAL_NOTICE}
        m.update(meta)
        text = common.format_frontmatter({k: v for k, v in m.items() if v is not None}) + "\n\n" + body
        p = Path(root) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
        return p


class FakeClock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self):
        return self.now

    def sleep(self, s):
        self.now += s


class FakeServer:
    """Simulated DRE: serves the fixture records (and clones) through the same URLs the client uses."""

    def __init__(self, clock, records=None, latency=0.2):
        self.clock = clock
        self.latency = latency
        self.records = {}      # dbId -> raw record
        for r in (records or [load_raw_record(i) for i in (LEI_24_96, PUBLICIDADE, DLR_7_99, DLR_15_96, REVOKED_808)]):
            self.records[r["search"]["dbId"]] = copy.deepcopy(r)
        self.log = []          # (time, url, user_agent)
        self.fault = None      # callable(n, url) -> None | int HTTP status | "garbage" | "oserror"
        self.n = 0

    def add_clones(self, count, base=LEI_24_96, start=2_000_000):
        for i in range(count):
            r = copy.deepcopy(self.records[base])
            db = start + i
            r["search"].update(dbId=db, numero=f"{i + 1}/2024", ano="2024", title=f"Lei n.º {i + 1}/2024  - Diário da República n.º 1/2024",
                               dataPublicacao="2024-03-01", DiplomaFragmentadoId=str(9_000_000 + i))
            self.records[db] = r

    def list_entries(self):
        return [copy.deepcopy(r["search"]) for _, r in sorted(self.records.items())]

    def requests_to(self, action):
        return [e for e in self.log if e[1].endswith(action)]

    # -- the transport used by DRE(transport=server.transport)
    def transport(self, url, data, headers):
        self.n += 1
        self.log.append((self.clock(), url, headers.get("User-Agent")))
        self.clock.now += self.latency
        if self.fault:
            f = self.fault(self.n, url)
            if f == "oserror":
                raise OSError("simulated network failure")
            if f == "garbage":
                return 200, b"<html>the site changed</html>"
            if isinstance(f, int):
                return f, b""
        if url.endswith("moduleservices/moduleinfo"):
            urls = {f"/dr/scripts/dr.{m}.{s}.mvc.js": "?v1" for m, s in (
                ("Pesquisas", "PesquisaResultado"), ("MenusParaPesquisa", "LegislacaoPorCodigo"),
                ("LegislacaoConsolidada", "LegCons_Detalhe"), ("Legislacao_Conteudos", "Conteudo_Detalhe"))}
            return 200, json.dumps({"manifest": {"versionToken": "tok", "urlVersions": urls}}).encode()
        m = re.search(r"/dr/scripts/dr\.\w+\.\w+\.mvc\.js", url)
        if m:
            js = "".join(f'controller.callDataAction("{a}", "id", "path", "api-{a}", function ()' for a in (
                "DataActionGetPesquisas", "DataActionGetCodigos", "DataActionGetData",
                "DataActionGetDiplomaFragByIdAndApplicationSetting", "DataActionGetAllConteudoDetalheData"))
            return 200, js.encode()
        m = re.search(r"screenservices/dr/(\w+)/(\w+)/(\w+)$", url)
        assert m, url
        action = m.group(3)
        v = json.loads(data)["screenData"]["variables"]
        return 200, json.dumps({"versionInfo": {}, "data": self.action(action, v)}).encode()

    def action(self, action, v):
        if action == "DataActionGetPesquisas":
            entries = self.list_entries()
            s, n = v["StartIndex"], v["MaxRecordsPerPage"]
            res = {"hits": {"total": {"value": len(entries)}, "hits": [{"_source": e} for e in entries[s:s + n]]}}
            return {"Resultado": json.dumps(res)}
        if action == "DataActionGetCodigos":
            return {"CodigosList": {"List": [{"DiplomaFrag": {"Designacao": "Código da Publicidade",
                                                              "LinkSiteMap": "/dr/legislacao-consolidada/decreto-lei/1990-34537375"}}]}}
        if action == "DataActionGetData":
            return self.records[int(v["DiplomaLegisId"])]["data"]
        if action == "DataActionGetDiplomaFragByIdAndApplicationSetting":
            r = next(r for r in self.records.values() if str(r["search"].get("DiplomaFragmentadoId")) == v["DiplomaFragId"])
            return {"IsSitemapErro": r["frag"] is None, "ConsolidadaConteudoDetalhe": r["frag"]}
        if action == "DataActionGetAllConteudoDetalheData":
            key = v["Key"]
            db = int(key.rsplit("-", 1)[1])
            r = self.records.get(db)
            orig = (r or {}).get("original")
            return {"IsVisible": bool(orig), "DetalheConteudo": orig or {}}
        raise AssertionError(action)

    def dre(self, **kw):
        return dre_client.DRE(transport=self.transport, clock=self.clock, sleep=self.clock.sleep,
                              log=lambda m: None, **kw)
