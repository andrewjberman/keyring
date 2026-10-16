"""Offline test of v2_service_env_r34h.sh (issuer 2.0.0_SA_COO~G2): stub systemctl and systemd-run on PATH, a fake root holding the intake/yfinance_check.py under test, a fake
yfinance whose Ticker.history() raises the REAL curl_cffi 0.13.0 HTTPError (404 on the quoteSummary URL of the symbol, as the service's probe read) for an unknown symbol and returns
rows for SPY, and run the script. Prints one RESULT line: V2S-R34H-TEST-OK <n> cases or V2S-R34H-TEST-FAIL <why>. No network, no AWS, no host.

usage: python test_v2_service_env_r34h.py        (run from the repository root; needs bash)
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip())
HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "v2_service_env_r34h.sh"
CHECKER = REPO / "infra/aws/lambda/investor-reporting/intake/yfinance_check.py"
CURL_FIX = REPO / "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/curl_cffi_0_13_0"
WORKER = REPO / "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py"
DOOR = REPO / "infra/aws/lambda/investor-reporting/intake/security_resolution.py"
LEASE = REPO / "infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py"
TRANSPORT = REPO / "infra/aws/lambda/investor-reporting/ycharts/research/price_transport_ycharts.py"
INSTALLED = REPO / "infra/aws/lambda/investor-reporting/reports/resident_installed.py"
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


FAKE_YF = '''
__version__ = "1.2.0-fake"
from curl_cffi.requests.exceptions import HTTPError


class _Cfg:
    pass


config = _Cfg()
config.debug = _Cfg()
config.debug.hide_exceptions = True
shared = _Cfg()
shared._ERRORS = {}


class _Response:
    def __init__(self, status, url):
        self.status_code, self.url, self.reason = status, url, ""


class _Frame:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    @property
    def columns(self):
        return ["Close"]

    @property
    def index(self):
        return ["2026-09-%02d 00:00:00-04:00" % d for d, _ in self.rows]

    def __getitem__(self, name):
        return [c for _, c in self.rows]


class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol

    def history(self, period, auto_adjust):
        if self.symbol == "SPY":
            return _Frame([(d, 100.0 + d) for d in range(1, 23)])
        url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/%s?modules=x&crumb=SECRETVALUE" % self.symbol
        raise HTTPError("HTTP Error 404: ", 0, _Response(404, url))
'''


def make_stubs(bindir, root):
    interp = sys.executable.replace("\\", "/")
    (bindir / "systemctl").write_text(
        '#!/bin/bash\ncase "$*" in\n'
        '  *is-active*) echo active;;\n'
        '  *"-p MainPID"*) echo 4242;;\n'
        '  *"-p User"*) echo tester;;\n'
        '  *"-p WorkingDirectory"*) echo %s;;\n'
        '  *"-p Environment"*) echo "PYTHONPATH=%s PYTHONUNBUFFERED=1";;\n'
        '  *"-p ExecStart"*) echo "{ path=%s ; argv[]=%s %s/ycharts/generate/resident_main.py --factory x ; ignore_errors=no }";;\n'
        'esac\n' % (root, root, interp, interp, root), encoding="ascii")
    (bindir / "systemd-run").write_text(
        '#!/bin/bash\nWD=; ENVS=\n'
        'while [ $# -gt 0 ]; do\n  case "$1" in\n'
        '    -p) shift; case "$1" in WorkingDirectory=*) WD="${1#WorkingDirectory=}";; esac;;\n'
        '    --setenv=*) ENVS="$ENVS ${1#--setenv=}";;\n'
        '    --uid=*|--quiet|--wait|--pipe|--collect) ;;\n'
        '    *) break;;\n  esac\n  shift\ndone\n'
        'cd "$WD" || exit 99\nexec env $ENVS "$@"\n', encoding="ascii")
    for f in bindir.iterdir():
        f.chmod(0o755)


def worker_stub(mutate=None):
    """A stand-in resident_worker holding the REAL back-off block of the repository's resident_worker.py (the constants and the function),
    cut from `RESOLVE_RETRY_VISIBILITY_S = 60` up to the next comment block; the rest of that module needs the whole package."""
    text = WORKER.read_text(encoding="utf-8")
    start = text.index("RESOLVE_RETRY_VISIBILITY_S = 60")
    end = text.index("# CTO rulings batch 262", start)
    block = text[start:end]
    if mutate:
        block = block.replace(*mutate)
    window = next(ln for ln in text.split("\n") if ln.startswith("RESOLVE_WINDOW_CLASS = "))
    return block + "\nRESOLVE_MAX_RECEIVES = 4\n" + window + "\n"


def run(tmp, checker_text, want_root=None, worker_mutate=None, door_mutate=None, pricing_on=True, lease_mutate=None, budget=True):
    root = tmp / "root"
    bindir = tmp / "bin"
    for d in (root, bindir):
        if d.exists():
            shutil.rmtree(d)
    (root / "intake").mkdir(parents=True)
    bindir.mkdir()
    (root / "intake" / "yfinance_check.py").write_text(checker_text, encoding="utf-8")
    for src in CURL_FIX.rglob("*.pyfix"):  # the real curl_cffi classes, materialised as .py inside the fake root (the fixture's README)
        dst = root / src.relative_to(CURL_FIX).with_suffix(".py")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    (root / "yfinance.py").write_text(FAKE_YF, encoding="utf-8")
    (root / "ycharts" / "generate").mkdir(parents=True)
    (root / "ycharts" / "generate" / "resident_worker.py").write_text(worker_stub(worker_mutate), encoding="utf-8")
    door_text = DOOR.read_text(encoding="utf-8")
    if door_mutate:
        assert door_text.count(door_mutate[0]) == 1, door_mutate[0]
        door_text = door_text.replace(*door_mutate)
    (root / "intake" / "security_resolution.py").write_text(door_text, encoding="utf-8")
    (root / "reports").mkdir()
    bindings = '{"opal_pricing": {"enabled": %s, "tiers": ["estate", "yfinance", "ycharts"]}%s}' % (
        "true" if pricing_on else "false", ', "ycharts_window_budget": {"calls": 6, "window_s": 390}' if budget else "")
    (root / "reports" / "resident_bindings.json").write_text(bindings, encoding="utf-8")
    (root / "reports" / "resident_installed.py").write_text(INSTALLED.read_text(encoding="utf-8"), encoding="utf-8")
    (root / "ycharts" / "session").mkdir(parents=True)
    lease_text = LEASE.read_text(encoding="utf-8")
    if lease_mutate:
        assert lease_text.count(lease_mutate[0]) == 1, lease_mutate[0]
        lease_text = lease_text.replace(*lease_mutate)
    (root / "ycharts" / "session" / "operation_lease.py").write_text(lease_text, encoding="utf-8")
    (root / "ycharts" / "research").mkdir(parents=True)
    (root / "ycharts" / "research" / "price_transport_ycharts.py").write_text(TRANSPORT.read_text(encoding="utf-8"), encoding="utf-8")
    make_stubs(bindir, root.as_posix())
    env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"], MSYS_NO_PATHCONV="1",
               V2S_WANT_ROOT=want_root if want_root is not None else root.as_posix(), V2S_PYFILE=(tmp / "v2s.py").as_posix())
    proc = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
    return proc.returncode, proc.stdout + proc.stderr


tmp = Path(tempfile.mkdtemp(prefix="v2s_r34h_test_"))
try:
    check("bash -n", subprocess.run(["bash", "-n", str(SCRIPT)]).returncode == 0)
    check("script is ASCII", all(b < 128 for b in SCRIPT.read_bytes()))
    fixed = CHECKER.read_text(encoding="utf-8")
    check("the checker under test carries the symbol-404 fix", "def _symbol_404(exc, symbol):" in fixed and "def _is_ticker_missing(exc, symbol=None):" in fixed)
    rc, out = run(tmp, fixed)
    out_fixed = out
    check("the fixed checker: SPY KEPT, ZQXWVK NOT_KEPT, V2S OK, rc 0", rc == 0 and "V2S OK SPY KEPT and ZQXWVK NOT_KEPT" in out, "rc=%d %s" % (rc, out[-500:]))
    check("no class line is printed when nothing failed", "V2S CLASS" not in out, out[-400:])
    check("the in-service back-off check passes: 150, 300, 450 for a WAF code, 60 for another cause", "V2S BACKOFF OK" in out and "waf=[150, 300, 450] flat=60" in out, out[-900:])
    check("the shipped worker is the real back-off block (the stand-in is cut from the repository file)", "def _resolve_retry_visibility(code, receives):" in worker_stub() and "RESOLVE_WAF_BACKOFF_S = (150, 300, 450)" in worker_stub())
    check("the four in-service controls pass: one NOT_KEPT, three stay CHECK_FAILED", "V2S CONTROLS OK 4 of 4" in out and out.count("V2S CONTROL ") >= 4 and "WRONG" not in out, out[-900:])
    check("the 429 control reads PUSHBACK and the other-symbol and chart controls read EXCEPTION",
          "429 on its own quoteSummary URL: CHECK_FAILED PUSHBACK" in out and "404 on another symbol's quoteSummary URL: CHECK_FAILED EXCEPTION" in out
          and "404 on the chart endpoint: CHECK_FAILED EXCEPTION" in out, out[-900:])
    unfixed = fixed.replace("return symbol is not None and _symbol_404(exc, symbol)", "return False")
    check("the unfixed variant differs from the fixed text", unfixed != fixed)
    rc, out = run(tmp, unfixed)
    check("the checker without the 404 rule reads CHECK_FAILED: V2S FAIL, rc 1", rc == 1 and "V2S FAIL" in out and "CHECK_FAILED" in out, "rc=%d %s" % (rc, out[-500:]))
    check("a failed V2 names the class, module, status and the URL without its query",
          "V2S CLASS ZQXWVK module=curl_cffi.requests.exceptions name=HTTPError status=404 url=https://query2.finance.yahoo.com/v10/finance/quoteSummary/ZQXWVK" in out
          and "crumb" not in out.split("V2S CLASS", 1)[1].split("MRO", 1)[0], out[-700:])
    check("the MRO and the checker's own answer are printed", "MRO curl_cffi.requests.exceptions.HTTPError,curl_cffi.requests.exceptions.RequestException" in out
          and "_is_ticker_missing=False _failure_reason=EXCEPTION" in out, out[-700:])
    check("the secret in the URL query never reaches the output", "SECRETVALUE" not in out, out[-300:])
    broad = fixed.replace("return symbol is not None and _symbol_404(exc, symbol)", "return True")
    rc, out = run(tmp, broad)
    check("an over-broad checker (every exception reads as missing) fails the controls: V2S FAIL, rc 1", rc == 1 and "V2S CONTROLS FAIL" in out and "WRONG" in out and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-900:]))
    rc, out = run(tmp, fixed, worker_mutate=("RESOLVE_WAF_BACKOFF_S = (150, 300, 450)", "RESOLVE_WAF_BACKOFF_S = (60, 60, 60)"))
    check("a worker whose schedule is the old flat 60 fails the back-off check: V2S BACKOFF FAIL, V2S FAIL, rc 1", rc == 1 and "V2S BACKOFF FAIL" in out and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-700:]))
    rc, out = run(tmp, fixed, worker_mutate=("code.endswith(RESOLVE_WAF_CLASS)", "True"))
    check("a worker that gives every cause the schedule fails (the non-WAF code reads 150, not 60)", rc == 1 and "V2S BACKOFF FAIL" in out, "rc=%d %s" % (rc, out[-700:]))
    check("the in-service door check passes: one checker call, the provider asked only about the symbol not kept", "V2S DOOR OK" in out_fixed and "provider_calls=[['BBB']]" in out_fixed, out_fixed[-900:])
    check("the in-service pricing check passes: opal_pricing ON with the same tiers", "V2S PRICING OK" in out_fixed, out_fixed[-900:])
    rc, out = run(tmp, fixed, door_mutate=("                        if symbol in pending:\n                            pending.remove(symbol)\n", "                        pass\n"))
    check("a door that still sends a KEPT symbol to the provider fails: V2S DOOR FAIL, V2S FAIL, rc 1", rc == 1 and "V2S DOOR FAIL" in out and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-700:]))
    rc, out = run(tmp, fixed, pricing_on=False)
    check("a bindings file with pricing OFF fails: V2S PRICING FAIL, V2S FAIL, rc 1", rc == 1 and "V2S PRICING FAIL" in out and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-700:]))
    check("the in-service budget check passes: the 3rd call over a (2, 100 s) budget is refused OPERATION_WINDOW_BUDGET with retry_after 94", "V2S BUDGET passed=2 third=OPERATION_WINDOW_BUDGET retry_after=94" in out_fixed and "V2S BUDGET OK" in out_fixed, out_fixed[-1200:])
    check("the in-service tier check passes: the transport encodes the runner's query, closes its facade, and the tier list names ycharts", "V2S TIER OK" in out_fixed, out_fixed[-1200:])
    check("the pricing check now reads the three tiers and the 6 by 390 budget binding", 'budget={"calls": 6, "window_s": 390}' in out_fixed and "V2S PRICING OK" in out_fixed, out_fixed[-1200:])
    rc, out = run(tmp, fixed, budget=False)
    check("a bindings file with no budget fails: V2S PRICING FAIL, V2S FAIL, rc 1", rc == 1 and "V2S PRICING FAIL" in out and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-700:]))
    rc, out = run(tmp, fixed, lease_mutate=("if count >= calls:", "if count >= calls + 1000:"))
    check("a lease that ignores its budget fails: V2S BUDGET FAIL, V2S FAIL, rc 1", rc == 1 and "V2S BUDGET FAIL" in out and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-700:]))
    rc, out = run(tmp, fixed, want_root="/opt/irpt-resident/0485393f3a-r34h")
    check("the root guard refuses a root that is not the wanted r34h root (rc 62)", rc == 62 and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-300:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("V2S-R34H-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("V2S-R34H-TEST-OK %d cases" % len(cases))
