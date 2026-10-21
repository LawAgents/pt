"""Throttled client for the internal JSON services of the Diario da Republica Eletronico.

The site is an OutSystems app: data comes from "screen service" endpoints
(POST /dr/screenservices/dr/<Module>/<Screen>/<Action>) that need the current module version token
(from /dr/moduleservices/moduleinfo) and the action's apiVersion (read from the screen's JS).

Rules (RULES.xml#rule.fetch_rate): one global throttle for ANY request (>= MIN_INTERVAL seconds between
two request STARTS; several requests may be in flight), the project User-Agent on every request, and an immediate stop after
3 consecutive errors or on HTTP 429/503.
"""
import http.client
import json
import threading
import re
import sys
import time
import urllib.error
import urllib.request

from common import USER_AGENT

BASE = "https://diariodarepublica.pt/dr/"
SITE = "https://diariodarepublica.pt"
ANON_CSRF = "T6C+9iB49TLra4jEsMeSckDMNhQ="  # public anonymous CSRF token of OutSystems
MIN_INTERVAL = 0.55  # 2 request starts per second at most (owner decision dec.37)
MAX_CONSECUTIVE_ERRORS = 3
SLOW_DOWN = (429, 503)


class FetchAborted(Exception):
    """Too many errors or the server asked to slow down: stop everything, publish nothing."""


class ServiceChanged(FetchAborted):
    """The JSON services answered in a shape we do not know: the site changed."""


def urllib_transport(url, data, headers, timeout=None):
    """Default transport: returns (status, body). Network failures raise OSError.
    The text of a big code can take minutes to build on the server, hence the long timeout for POSTs."""
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout or (600 if data else 120)) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() or b""
    except urllib.error.URLError as e:
        raise OSError(str(e.reason)) from e
    except http.client.HTTPException as e:
        raise OSError(f"{type(e).__name__}: {e}") from e


class DRE:
    def __init__(self, transport=urllib_transport, clock=time.monotonic, sleep=time.sleep,
                 min_interval=MIN_INTERVAL, user_agent=USER_AGENT, log=None):
        self._transport = transport
        self._clock = clock
        self._sleep = sleep
        self.min_interval = min_interval
        self.user_agent = user_agent
        self._log = log or (lambda msg: print(msg, file=sys.stderr))
        # A new client waits one interval before its first request, so two runs started back to back also keep the rate.
        self._next_start = clock() + min_interval
        self._lock = threading.Lock()
        self.aborted = False
        self.errors_in_row = 0
        self.requests = 0
        self._api = {}
        self.version = None
        self.urls = {}

    # ---- low level -------------------------------------------------------------------------

    def _request(self, url, data=None, headers=None):
        """One throttled HTTP request with error accounting; returns the body bytes."""
        h = {"User-Agent": self.user_agent}
        h.update(headers or {})
        while True:
            # Slots are reserved by START time, so requests may overlap but never start more often than once per
            # min_interval seconds in total, whatever the number of threads.
            with self._lock:
                if self.aborted:
                    raise FetchAborted("aborted by another request")
                now = self._clock()
                start = max(now, self._next_start)
                self._next_start = start + self.min_interval
                self.requests += 1
            if start > now:
                self._sleep(start - now)
            try:
                status, body = self._transport(url, data, h)
                err = None if status == 200 else f"HTTP {status}"
            except OSError as e:
                status, body, err = None, b"", f"network error: {e}"
            with self._lock:
                if err is None:
                    self.errors_in_row = 0
                    return body
                self.errors_in_row += 1
                errors_in_row = self.errors_in_row
            self._log(f"request failed ({err}) for {url}")
            if status in SLOW_DOWN:
                self.aborted = True
                raise FetchAborted(f"{err} for {url}: the server asked to slow down")
            if errors_in_row >= MAX_CONSECUTIVE_ERRORS:
                self.aborted = True
                raise FetchAborted(f"{errors_in_row} consecutive errors, last: {err} for {url}")

    def _get_json(self, url):
        body = self._request(url)
        try:
            return json.loads(body)
        except ValueError as e:
            raise ServiceChanged(f"not JSON: {url}") from e

    # ---- OutSystems screen services ---------------------------------------------------------

    def refresh(self):
        try:
            mi = self._get_json(BASE + "moduleservices/moduleinfo")["manifest"]
            self.version, self.urls = mi["versionToken"], mi["urlVersions"]
        except (KeyError, TypeError) as e:
            raise ServiceChanged("moduleinfo has an unknown shape") from e
        self._api = {}

    def api_version(self, module, screen, action):
        key = (module, screen, action)
        if key not in self._api:
            path = f"/dr/scripts/dr.{module}.{screen}.mvc.js"
            js = self._request(SITE + path + self.urls.get(path, "")).decode("utf-8", "replace")
            m = re.search(r'callDataAction\("%s", "[^"]*", "[^"]*", "([^"]*)"' % re.escape(action), js)
            if not m:
                raise ServiceChanged(f"apiVersion of {action} not found in {path}")
            self._api[key] = m.group(1)
        return self._api[key]

    def data_action(self, module, screen, action, variables):
        """Call a screen DataAction and return its `data` dict."""
        if self.version is None:
            self.refresh()
        url = f"{BASE}screenservices/dr/{module}/{screen}/{action}"
        for _ in range(3):
            body = {
                "versionInfo": {"moduleVersion": self.version,
                                "apiVersion": self.api_version(module, screen, action)},
                "viewName": f"{module}.{screen}",
                "screenData": {"variables": variables},
                "clientVariables": {},
            }
            raw = self._request(url, json.dumps(body).encode(),
                                {"X-CSRFToken": ANON_CSRF, "Accept": "application/json",
                                 "Content-Type": "application/json; charset=UTF-8"})
            try:
                j = json.loads(raw)
            except ValueError as e:
                raise ServiceChanged(f"{action}: answer is not JSON") from e
            vi = j.get("versionInfo") or {}
            if vi.get("hasModuleVersionChanged") or vi.get("hasApiVersionChanged"):
                self._log("DRE redeployed; refreshing version tokens")
                self.refresh()
                continue
            if "exception" in j or "data" not in j:
                # The service answered but failed: counts as an error like a bad HTTP status.
                self.errors_in_row += 1
                if self.errors_in_row >= MAX_CONSECUTIVE_ERRORS:
                    raise FetchAborted(f"{action}: {str(j.get('exception'))[:200]}")
                self._log(f"{action}: service error {str(j.get('exception'))[:200]}")
                continue
            return j["data"]
        raise ServiceChanged(f"{action}: no usable answer after retries")

    # ---- high level helpers (same services the site uses) -----------------------------------

    def search(self, filters, start=0, size=100, text="*", sort=None):
        v = {
            "FiltrosDePesquisa": {"texto": text, "tipoConteudo": {"List": []}},
            "ListaFiltros": {"List": [{"Area": a, "Value": val} for a, val in filters]},
            "PesquisaSimplesFiltro": text,
            "Pesquisa": {"List": [text]},
            "IsPesquisaSimples": True,
            "StartIndex": start,
            "MaxRecordsPerPage": size,
            "TipoOrdenacaoId": 9,
            "Ordenacoes": {"List": [{"Field": f, "Order": o} for f, o in (sort or [("dbId", "asc")])]},
        }
        d = self.data_action("Pesquisas", "PesquisaResultado", "DataActionGetPesquisas", v)
        try:
            return json.loads(d["Resultado"])
        except (KeyError, ValueError) as e:
            raise ServiceChanged("search answer has an unknown shape") from e

    def codigos(self):
        d = self.data_action("MenusParaPesquisa", "LegislacaoPorCodigo", "DataActionGetCodigos", {})
        return [x["DiplomaFrag"] for x in d["CodigosList"]["List"]]

    def consolidated(self, diploma_legis_id):
        v = {"DiplomaLegisId": str(diploma_legis_id), "DiplomaFragId": "0",
             "GetDiplomaFragByIdAndApplicationSetting": {}}
        return self.data_action("LegislacaoConsolidada", "LegCons_Detalhe", "DataActionGetData", v)

    def frag_detail(self, tipo_slug, key, frag_id):
        v = {"Tipo": tipo_slug, "Key": key, "DiplomaFragId": str(frag_id)}
        return self.data_action("LegislacaoConsolidada", "LegCons_Detalhe",
                                "DataActionGetDiplomaFragByIdAndApplicationSetting", v)

    def original_detail(self, tipo_slug, key):
        return self.data_action("Legislacao_Conteudos", "Conteudo_Detalhe",
                                "DataActionGetAllConteudoDetalheData", {"Tipo": tipo_slug, "Key": key})
