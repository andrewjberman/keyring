"""Offline test of ycharts_price_probe2.sh (issuer 2.0.0_SA_COO~G2): stub systemctl, systemd-run and journalctl on PATH, a fake root that carries the REAL price_adapter_ycharts, price_transport_ycharts and
tr_level (copied from the repository) beside a fake boto3 and a fake ResidentSession whose facades answer by a plan (c clean series, e empty series, x 202 WAF challenge, r raised exception), and run the script.
Prints one RESULT line: YCP2-PROBE-TEST-OK <n> cases or YCP2-PROBE-TEST-FAIL <why>. No network, no AWS, no host.

usage: python test_ycharts_price_probe.py        (needs bash)
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "ycharts_price_probe2.sh"
REPO = HERE
while not (REPO / "infra").is_dir():
    REPO = REPO.parent
LAMBDA = REPO / "infra" / "aws" / "lambda" / "investor-reporting" / "ycharts" / "research"
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


SESSION = '''
import json
import os


def _plan_char():
    counter = os.environ["FAKE_COUNTER"]
    with open(counter, encoding="ascii") as fh:
        n = len(fh.read().split("\\n")) - 1
    plan = os.environ.get("FAKE_PLAN", "")
    return plan[n - 1] if n <= len(plan) else "c"


class Facade:
    def __init__(self, mode):
        self.mode = mode

    def request(self, path):
        with open(os.environ["FAKE_COUNTER"], "a", encoding="ascii") as fh:
            fh.write(self.mode + " " + path + "\\n")
        ch = _plan_char()
        if "securities_info" in path:
            sym = path.split("=")[-1]
            rows = [] if ch == "n" else [{"id": "M:" + sym, "security_id": "M:" + sym, "display_security_id": sym, "securitylist_security_id": "M1", "security_name": "SECRETVALUE name"}]
            return {"status": 200, "waf_action": None, "content_type": "application/json"}, json.dumps(rows).encode("ascii")
        if ch == "h":
            return {"status": 400, "waf_action": None, "content_type": "text/plain"}, b"bad crumb=SECRETVALUE"
        if ch == "r":
            raise OSError("connection reset crumb=SECRETVALUE")
        if ch == "x":
            body = b"<html>awswaf challenge crumb=SECRETVALUE</html>"
            return {"status": 202, "waf_action": "challenge", "content_type": "text/html"}, body
        raw = [] if ch == "e" else [[1700000000000 + 86400000 * i, 100.0 + i] for i in range(5)]
        body = json.dumps({"chart_data": [[{"raw_data": raw, "extra_field": "SECRETVALUE"}]]}).encode("ascii")
        return {"status": 200, "waf_action": None, "content_type": "application/json"}, body

    def close(self):
        with open(os.environ["FAKE_COUNTER"] + ".closed", "a", encoding="ascii") as fh:
            fh.write("closed\\n")


class ResidentSession:
    def __init__(self, **kw):
        with open(os.environ["FAKE_COUNTER"] + ".init", "w", encoding="ascii") as fh:
            fh.write(repr(kw.get("window_budget")))

    def acquire(self, *, request_budget=60, ttl=120):
        return Facade("session")

    def acquire_sessionless(self, *, request_budget=60, ttl=120):
        return Facade("sessionless")
'''

BOTO3 = '''
def client(name, region_name=None):
    return name
'''


def make_stubs(bindir, root, user, handled):
    interp = sys.executable.replace("\\", "/")
    (bindir / "systemctl").write_text(
        '#!/bin/bash\ncase "$*" in\n'
        '  *is-active*) echo active;;\n'
        '  *"-p MainPID"*) echo 4242;;\n'
        '  *"-p ActiveEnterTimestamp"*) echo "Fri 2026-10-16 13:28:25 UTC";;\n'
        '  *"-p User"*) echo %s;;\n'
        '  *"-p WorkingDirectory"*) echo %s;;\n'
        '  *"-p Environment"*) echo "PYTHONUNBUFFERED=1";;\n'
        '  *"-p ExecStart"*) echo "{ path=%s ; argv[]=%s %s/x.py ; ignore_errors=no }";;\n'
        'esac\n' % (user, root, interp, interp, root), encoding="ascii")
    (bindir / "journalctl").write_text(
        '#!/bin/bash\necho "Oct 16 14:00:00 h python3.12[1]: IRPT_RESIDENT_POLL handled=%d"\n' % handled, encoding="ascii")
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


def run(tmp, plan="", user="tester", handled=0, budget=True):
    root, bindir = tmp / "root", tmp / "bin"
    for d in (root, bindir):
        if d.exists():
            shutil.rmtree(d)
    for sub in ("reports", "ycharts/research", "ycharts/session", "lib"):
        (root / sub).mkdir(parents=True)
    bindir.mkdir()
    for name in ("price_adapter_ycharts.py", "price_transport_ycharts.py", "tr_level.py"):
        shutil.copy(LAMBDA / name, root / "ycharts" / "research" / name)
    (root / "ycharts" / "session" / "resident_session.py").write_text(SESSION, encoding="utf-8")
    (root / "lib" / "boto3.py").write_text(BOTO3, encoding="utf-8")
    bindings = {"region": "us-east-1", "jobs_table": "jobs", "enrolled_user_id": 7, "opal_pricing": {"enabled": True, "tiers": ["estate", "yfinance", "ycharts"]}}
    if budget:
        bindings["ycharts_window_budget"] = {"calls": 6, "window_s": 390}
    (root / "reports" / "resident_bindings.json").write_text(json.dumps(bindings), encoding="utf-8")
    make_stubs(bindir, root.as_posix(), user, handled)
    counter = tmp / "calls.txt"
    for p in (counter, Path(str(counter) + ".closed"), Path(str(counter) + ".init")):
        if p.exists():
            p.unlink()
    counter.write_text("", encoding="ascii")
    env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"], MSYS_NO_PATHCONV="1", FAKE_PLAN=plan, FAKE_COUNTER=counter.as_posix(),
               YCP2_PYFILE=(tmp / "ycp2.py").as_posix())
    proc = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
    calls = [ln for ln in counter.read_text(encoding="ascii").split("\n") if ln]
    closed = len(Path(str(counter) + ".closed").read_text(encoding="ascii").split()) if Path(str(counter) + ".closed").exists() else 0
    init = Path(str(counter) + ".init").read_text(encoding="ascii") if Path(str(counter) + ".init").exists() else ""
    return proc.returncode, proc.stdout + proc.stderr, calls, closed, init


tmp = Path(tempfile.mkdtemp(prefix="ycp2_test_"))
RECIPE = "securities=id:SPY,include:true,,&calcs=id:level,include:true,,&zoom=max&maxPoints=100000&partner=basic_2000"
try:
    check("bash -n", subprocess.run(["bash", "-n", str(SCRIPT)]).returncode == 0)
    check("script is ASCII", all(b < 128 for b in SCRIPT.read_bytes()))
    rc, out, calls, closed, init = run(tmp, "")
    check("all clean: three calls, rc 0, plain recipe form OK, second symbol OK, signed out ANSWERS", rc == 0 and len(calls) == 3 and "YCP2 RESULT form=RECIPE_PLAIN plain=OK typed=SKIP shape=ADAPTER_PARSES second_symbol=OK signed_out=ANSWERS calls=3" in out, "rc=%d calls=%s %s" % (rc, calls, out[-700:]))
    check("the modes and symbols are session SPY, session AAPL, sessionless SPY", [c.split(" ")[0] for c in calls] == ["session", "session", "sessionless"] and "id:AAPL," in calls[1], str(calls))
    check("every fund_data request is the CRO's captured recipe form: id, include, calcs level, zoom max, maxPoints, partner (no bare id:TICKER,include:true,& form)",
          RECIPE in calls[0] and RECIPE in calls[2] and all("/charts/fund_data.json?" in c for c in calls) and not any("securities=id:SPY,include:true,&zoom" in c for c in calls), str(calls))
    check("the root's window budget reaches the session as (6, 390)", init == "(6, 390)", init)
    check("every facade is closed (3)", closed == 3, str(closed))
    check("the adapter parsed rows from each served answer", out.count("rows=5") == 3 and "first=('" in out, out[:1600])
    check("no body value or secret is printed (key names are the shape and may print)", "SECRETVALUE" not in out, out[-400:])
    rc, out, calls, closed, init = run(tmp, "h")
    check("plain refused 400: lookup, then the typed id in the recipe form, signed in and out: four calls, RECIPE_TYPED", len(calls) == 4 and "securities_info?securities=SPY" in calls[1] and "securities=id:M:SPY,include:true,,&calcs=id:level" in calls[2]
          and "form=RECIPE_TYPED plain=REFUSED:PriceTransportRefused:PRICE_HTTP_400 typed=OK shape=ADAPTER_PARSES second_symbol=SKIP signed_out=ANSWERS calls=4" in out, "calls=%s %s" % (calls, out[-800:]))
    check("the lookup's id fields print (public ids) and its other values do not", 'id_fields={"display_security_id": "SPY", "id": "M:SPY", "security_id": "M:SPY", "securitylist_security_id": "M1"}' in out and "SECRETVALUE" not in out, out[:1800])
    rc, out, calls, closed, init = run(tmp, "hch")
    check("plain refused and typed refused: three calls, form NONE, typed REFUSED", len(calls) == 3 and "form=NONE" in out and "typed=REFUSED:PriceTransportRefused:PRICE_HTTP_400" in out, "calls=%s %s" % (calls, out[-600:]))
    rc, out, calls, closed, init = run(tmp, "hn")
    check("plain refused and the lookup has no row: two calls, typed NO_TYPED_ID", len(calls) == 2 and "typed=NO_TYPED_ID" in out, "calls=%s %s" % (calls, out[-500:]))
    rc, out, calls, closed, init = run(tmp, "e")
    check("an empty series on the plain form goes to the lookup branch, plain EMPTY", "plain=EMPTY" in out and len(calls) == 4, "calls=%s %s" % (calls, out[-500:]))
    rc, out, calls, closed, init = run(tmp, "cch")
    check("signed out refused 400: signed_out REFUSED:400, the signed-in answers stand", "signed_out=REFUSED:400" in out and "plain=OK" in out and "SECRETVALUE" not in out, out[-600:])
    rc, out, calls, closed, init = run(tmp, "crc")
    check("a raised exception on call 2 is named, the secret is redacted, the run goes on", "verdict=EXCEPTION module=builtins name=OSError" in out and len(calls) == 3 and "second_symbol=FAIL" in out and "SECRETVALUE" not in out, out[-700:])
    rc, out, calls, closed, init = run(tmp, "", budget=False)
    check("a bindings file with no budget passes None (the probe never invents a budget)", init == "None" and rc == 0, init)
    rc, out, calls, closed, init = run(tmp, "", handled=2)
    check("a busy resident refuses the whole read (rc 70, no call)", rc == 70 and not calls and "YCP2 FAIL the resident is busy" in out, "rc=%d %s" % (rc, out[-300:]))
    rc, out, calls, closed, init = run(tmp, "", user="")
    check("an empty unit user is refused (rc 61)", rc == 61 and not calls, "rc=%d %s" % (rc, out[-200:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("YCP2-PROBE-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("YCP2-PROBE-TEST-OK %d cases" % len(cases))
