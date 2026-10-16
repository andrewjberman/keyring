set -u
# Ledger irpt-resident-r34g-20261016, leg V2 (READ ONLY on the host; TWO Yahoo calls, plus ONE per symbol that reads CHECK_FAILED): run the door's real checker INSIDE THE RESIDENT SERVICE'S OWN ENVIRONMENT.
# Not a shell run: the user, the working directory and every Environment= entry are READ from the unit (systemctl show) and handed to a transient unit
# (systemd-run) that runs the same interpreter over the same root, so the process has the service's identity, cwd and import path, not the operator's.
# The code under test is the root's own intake/yfinance_check.py, loaded by path (the file the door imports), with the DEFAULT history port (the real yfinance call).
# Expected: SPY KEPT (HISTORY_ROWS), ZQXWVK NOT_KEPT (NO_ROWS) and four no-Yahoo controls (see below). Prints V2S OK only when all hold. Writes nothing on the host except the transient unit's own journal lines.
# On any CHECK_FAILED the script asks the default port once more for that symbol and prints the exception's module, name, MRO, HTTP status, the response URL without its query, and the first
# 200 characters of its message (a crumb= token redacted): the CTO's rule (msg 9354) that a failed V2 names the class it met.
# Written for IRPT_ANLREQ round 43 (issuer 2.0.0_SA_COO~G2). NOT RUN: a CloudOps applier runs it under a signed never-widen pair, as root (systemd-run needs it).
U=irpt-analysis-resident.service
echo "V2S unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
EXEC=$(systemctl show -p ExecStart --value $U)
WANT_ROOT=${V2S_WANT_ROOT:-/opt/irpt-resident/0485393f3a-r34g}
ROOT=$WD
echo "V2S user=$USR workdir=$WD interpreter=$PY"
echo "V2S environment entries: $(echo "$ENVS" | wc -w)"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "V2S FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
if [ "$ROOT" != "$WANT_ROOT" ]; then echo "V2S FAIL the working directory (the running root) is $ROOT, want $WANT_ROOT"; exit 62; fi
if ! echo "$EXEC" | grep -q "$ROOT/ycharts/generate/resident_main.py"; then echo "V2S FAIL ExecStart does not run resident_main.py from $ROOT"; exit 63; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${V2S_PYFILE:-/tmp/v2s_r34g.py}
cat > "$PYF" <<'PYEOF'
import importlib.util
import json
import os
import re
import sys

root = os.getcwd()
path = root + "/intake/yfinance_check.py"
spec = importlib.util.spec_from_file_location("yfinance_check", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
import yfinance  # noqa: E402  (the service's own import path)
print("V2S process: uid=%d cwd=%s file=%s yfinance=%s from=%s" % (getattr(os, "getuid", lambda: -1)(), root, path, yfinance.__version__, os.path.dirname(yfinance.__file__)))
text = open(path, encoding="utf-8").read()
fixed = "def _symbol_404(exc, symbol):" in text and "def _is_ticker_missing(exc, symbol=None):" in text
print("V2S the shipped checker carries the symbol-404 fix: %s" % ("yes" if fixed else "NO"))
out = mod.YfinanceChecker().check(["SPY", "ZQXWVK"])
print("V2S RESULT " + json.dumps(out, sort_keys=True))


def clean(value):
    return re.sub(r"crumb=[^&\s'\"]*", "crumb=REDACTED", str(value))


for symbol in sorted(out):
    if out[symbol].get("state") != "CHECK_FAILED":
        continue
    try:
        mod.default_history(symbol)
        print("V2S CLASS %s no exception on the second ask" % symbol)
    except BaseException as exc:  # a diagnostic prints whatever is raised
        kind = type(exc)
        response = getattr(exc, "response", None)
        url = getattr(response, "url", None)
        base = str(url).split("?", 1)[0] if url is not None else None
        print("V2S CLASS %s module=%s name=%s status=%s url=%s" % (symbol, kind.__module__, kind.__name__, getattr(response, "status_code", None), base))
        print("V2S CLASS %s MRO %s" % (symbol, ",".join("%s.%s" % (c.__module__, c.__name__) for c in kind.__mro__)))
        print("V2S CLASS %s MESSAGE[:200] %r" % (symbol, clean(exc)[:200]))
        print("V2S CLASS %s checker _is_ticker_missing=%s _failure_reason=%s" % (symbol, mod._is_ticker_missing(exc, symbol), mod._failure_reason(exc)))
spy, bad = out.get("SPY", {}), out.get("ZQXWVK", {})
ok = fixed and spy.get("state") == "KEPT" and spy.get("reason") == "HISTORY_ROWS" and bad.get("state") == "NOT_KEPT" and bad.get("reason") == "NO_ROWS"


# The in-service CONTROLS (no Yahoo call): the real default_history code path, with yfinance's Ticker.history replaced by a function that raises the host's REAL
# curl_cffi HTTPError, built the way curl_cffi's Response.raise_for_status builds it (HTTPError("HTTP Error N: ", 0, response)). One control must read NOT_KEPT
# (a 404 on its own symbol's quoteSummary URL) and three must STAY CHECK_FAILED (a 429 on that URL, a 404 on another symbol's URL, a 404 on the chart endpoint).
class _Resp:
    def __init__(self, status, url):
        self.status_code, self.url, self.reason = status, url, ""


def controls():
    import curl_cffi.requests.exceptions as ce
    base = "https://query2.finance.yahoo.com/v10/finance/"
    cases = [("404 on its own quoteSummary URL", 404, base + "quoteSummary/CTLSYM", "NOT_KEPT", "NO_ROWS"),
             ("429 on its own quoteSummary URL", 429, base + "quoteSummary/CTLSYM", "CHECK_FAILED", "PUSHBACK"),
             ("404 on another symbol's quoteSummary URL", 404, base + "quoteSummary/OTHERSYM", "CHECK_FAILED", "EXCEPTION"),
             ("404 on the chart endpoint", 404, base + "chart/CTLSYM", "CHECK_FAILED", "EXCEPTION")]
    original = yfinance.Ticker.history
    passed = 0
    try:
        for label, status, url, state, reason in cases:
            def raiser(self, *args, **kwargs):
                raise ce.HTTPError("HTTP Error %s: " % status, 0, _Resp(status, url))
            yfinance.Ticker.history = raiser
            got = mod.YfinanceChecker(sleep=lambda s: None).check(["CTLSYM"])["CTLSYM"]
            good = got.get("state") == state and got.get("reason") == reason
            passed += good
            print("V2S CONTROL %s: %s %s (want %s %s) %s" % (label, got.get("state"), got.get("reason"), state, reason, "ok" if good else "WRONG"))
    finally:
        yfinance.Ticker.history = original
    return passed, len(cases)


try:
    cpass, ctotal = controls()
except BaseException as exc:  # a control that cannot run is a failed control
    print("V2S CONTROLS could not run: %s.%s" % (type(exc).__module__, type(exc).__name__))
    cpass, ctotal = 0, 4
print("V2S CONTROLS %s %d of %d" % ("OK" if cpass == ctotal else "FAIL", cpass, ctotal))
ok = ok and cpass == ctotal


# r34g: the resolve hop's WAF back-off, read INSIDE the service's environment with no vendor call: the shipped resident_worker is imported on the
# service's own flat import path and its schedule is asked the three questions the order's checks ask (the WAF code at receives 1, 2, 3; a
# non-WAF code; the constants), so the root that runs is the root that carries the change.
def backoff():
    for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
        sys.path.insert(0, root + "/" + sub)
    import resident_worker as rwk
    waf = [rwk._resolve_retry_visibility("PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE", n) for n in (1, 2, 3)]
    flat = rwk._resolve_retry_visibility("PROVIDER_READ_UNAVAILABLE:STATUS_503", 2)
    good = (waf == [150, 300, 450] and flat == 60 and tuple(rwk.RESOLVE_WAF_BACKOFF_S) == (150, 300, 450) and rwk.RESOLVE_MAX_RECEIVES < 5
            and os.path.abspath(rwk.__file__).startswith(os.path.abspath(root)))
    print("V2S BACKOFF waf=%s flat=%s schedule=%s max_receives=%s file=%s %s" % (waf, flat, tuple(rwk.RESOLVE_WAF_BACKOFF_S), rwk.RESOLVE_MAX_RECEIVES,
                                                                              rwk.__file__, "ok" if good else "WRONG"))
    return good


# r34g: the upload door asks yfinance FIRST, read INSIDE the service's environment with no vendor call: the shipped security_resolution is imported on the
# service's flat import path and run with fake ports (a checker that keeps AAA and not BBB, a provider that finds nothing): the checker is asked ONCE about both,
# the provider ONLY about BBB, AAA reads KEPT and BBB NOT_FOUND. And the shipped bindings carry opal_pricing ON.
def door():
    sys.path.insert(0, root + "/intake")
    import security_resolution as sr
    calls = {"checker": [], "provider": []}

    class Checker:
        def check(self, symbols):
            calls["checker"].append(list(symbols))
            return {"AAA": {"state": "KEPT", "rows": 5, "last_close": 10.5}, "BBB": {"state": "NOT_KEPT"}}

    def provider(symbols):
        calls["provider"].append(list(symbols))
        return {"http_status": 200, "complete": True, "final_url_path": "/securities/securities_info", "account_id": "acct", "source_revision": "rev",
                "requested": list(symbols), "observed_at": "2026-10-16T15:00:00Z", "json": []}
    resolver = sr.SecurityResolver(provider_check=provider, identity=lambda symbol, kind: None, cache=None, clock=lambda: 1000.0,
                                   account_id="acct", source_revision="rev", checker=Checker())
    rows = {r["symbol"]: r for r in resolver.check(["AAA", "BBB"])["results"]}
    good = (calls["checker"] == [["AAA", "BBB"]] and calls["provider"] == [["BBB"]] and rows["AAA"]["state"] == "KEPT"
            and rows["AAA"]["price_source"] == "yfinance" and rows["BBB"]["state"] == "NOT_FOUND"
            and os.path.abspath(sr.__file__).startswith(os.path.abspath(root)))
    print("V2S DOOR checker_calls=%s provider_calls=%s AAA=%s BBB=%s file=%s %s" % (calls["checker"], calls["provider"], rows["AAA"]["state"], rows["BBB"]["state"],
                                                                                    sr.__file__, "ok" if good else "WRONG"))
    return good


def pricing():
    import json
    binding = json.load(open(root + "/reports/resident_bindings.json", encoding="utf-8"))["opal_pricing"]
    good = binding == {"enabled": True, "tiers": ["estate", "yfinance"]}
    print("V2S PRICING binding=%s %s" % (json.dumps(binding, sort_keys=True), "ok" if good else "WRONG"))
    return good


for label, fn in (("DOOR", door), ("PRICING", pricing)):
    try:
        good = fn()
    except BaseException as exc:  # a check that cannot run is a failed check
        print("V2S %s could not run: %s.%s %r" % (label, type(exc).__module__, type(exc).__name__, clean(exc)[:160]))
        good = False
    print("V2S %s %s" % (label, "OK" if good else "FAIL"))
    ok = ok and good


try:
    back_ok = backoff()
except BaseException as exc:  # a check that cannot run is a failed check
    print("V2S BACKOFF could not run: %s.%s %r" % (type(exc).__module__, type(exc).__name__, clean(exc)[:160]))
    back_ok = False
print("V2S BACKOFF %s" % ("OK" if back_ok else "FAIL"))
ok = ok and back_ok
print("V2S " + ("OK SPY KEPT and ZQXWVK NOT_KEPT" if ok else "FAIL want SPY KEPT HISTORY_ROWS, ZQXWVK NOT_KEPT NO_ROWS, all four controls, the back-off, the yfinance-first door and pricing ON"))
sys.exit(0 if ok else 1)
PYEOF
chmod 644 "$PYF"
echo "V2S script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" $SETENV "$PY" "$PYF"
RC=$?
echo "V2S transient unit rc=$RC"
rm -f "$PYF"
exit $RC
