"""Offline test of probe_exc_class_r34d.sh (issuer 2.0.0_SA_COO~G2): stub systemctl and systemd-run on PATH, a fake probe root holding the repository's intake/yfinance_check.py,
a fake yfinance whose history() raises a class the checker does not treat as ticker-missing (an HTTP-error-shaped class with a crumb in its message) for ZQXWVK and returns rows for SPY.
Prints one RESULT line: PROBE-SCRIPT-TEST-OK <n> cases or PROBE-SCRIPT-TEST-FAIL <why>. No network, no AWS, no host.

usage: python test_probe_exc_class.py        (run from the repository root; needs bash)
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip())
HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "probe_exc_class_r34d.sh"
CHECKER = REPO / "infra/aws/lambda/investor-reporting/intake/yfinance_check.py"
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


FAKE_YF = '''
__version__ = "1.2.0-fake"


class _Cfg:
    pass


config = _Cfg()
config.debug = _Cfg()
config.debug.hide_exceptions = True
shared = _Cfg()
shared._ERRORS = {}


class HTTPError(Exception):
    pass


class _Frame:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)


class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol

    def history(self, period, auto_adjust):
        if self.symbol == "SPY":
            return _Frame([(d, 100.0 + d) for d in range(1, 23)])
        shared._ERRORS[self.symbol] = "HTTP Error 404: Quote not found crumb=SECRETVALUE"
        raise HTTPError("HTTP Error 404 for https://query1.finance.yahoo.com/v8/finance/chart/ZQXWVK?range=1mo&crumb=SECRETVALUE&x=1")
'''


def run(tmp, user="tester", checker_text=None, want_fix=True):
    root = tmp / "root"
    bindir = tmp / "bin"
    for d in (root, bindir):
        if d.exists():
            shutil.rmtree(d)
    (root / "intake").mkdir(parents=True)
    bindir.mkdir()
    text = checker_text if checker_text is not None else CHECKER.read_text(encoding="utf-8")
    (root / "intake" / "yfinance_check.py").write_text(text, encoding="utf-8")
    (root / "yfinance.py").write_text(FAKE_YF, encoding="utf-8")
    interp = sys.executable.replace("\\", "/")
    (bindir / "systemctl").write_text(
        '#!/bin/bash\ncase "$*" in\n'
        '  *is-active*) echo active;;\n'
        '  *"-p MainPID"*) echo 4242;;\n'
        '  *"-p User"*) echo %s;;\n'
        '  *"-p WorkingDirectory"*) echo /opt/irpt-resident/0485393f3a-r34c;;\n'
        '  *"-p Environment"*) echo "PYTHONPATH=/opt/irpt-resident/0485393f3a-r34c PYTHONUNBUFFERED=1";;\n'
        '  *"-p ExecStart"*) echo "{ path=%s ; argv[]=%s /opt/irpt-resident/0485393f3a-r34c/ycharts/generate/resident_main.py ; ignore_errors=no }";;\n'
        'esac\n' % (user, interp, interp), encoding="ascii")
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
    env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"], MSYS_NO_PATHCONV="1",
               PROBE_ROOT_OVERRIDE=root.as_posix(), PROBE_PYFILE=(tmp / "probe.py").as_posix())
    proc = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
    return proc.returncode, proc.stdout + proc.stderr


tmp = Path(tempfile.mkdtemp(prefix="probe_test_"))
try:
    check("bash -n", subprocess.run(["bash", "-n", str(SCRIPT)]).returncode == 0)
    check("script is ASCII", all(b < 128 for b in SCRIPT.read_bytes()))
    rc, out = run(tmp)
    check("rc 0 and the probe finishes", rc == 0 and "PROBE DONE" in out, "rc=%d %s" % (rc, out[-300:]))
    check("ZQXWVK: module, name and the whole MRO are printed", "name=HTTPError" in out and "MRO yfinance.HTTPError,builtins.Exception" in out, out[-500:])
    check("the message is printed and the crumb is redacted", "crumb=REDACTED" in out and "SECRETVALUE" not in out, out[-500:])
    check("the checker's own answer is printed (not ticker-missing, EXCEPTION)", "_is_ticker_missing=False _failure_reason=EXCEPTION" in out, out[-500:])
    check("the stack frames are printed without locals", "FRAMES" in out and "in history" in out, out[-500:])
    check("SPY is the control: no exception", "PROBE SPY NO EXCEPTION rows=22" in out, out[-500:])
    check("the process used the probe root as its working directory", "cwd=%s" % (tmp / "root").as_posix() in out.replace("\\", "/"), out[:400])
    rc, out = run(tmp, checker_text="# the r33 checker without the fix\n")
    check("a probe root without the r34d checker is refused (rc 62)", rc == 62 and "PROBE FAIL" in out, "rc=%d %s" % (rc, out[-200:]))
    rc, out = run(tmp, user="")
    check("an empty unit user is refused (rc 61)", rc == 61, "rc=%d %s" % (rc, out[-200:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("PROBE-SCRIPT-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("PROBE-SCRIPT-TEST-OK %d cases" % len(cases))
