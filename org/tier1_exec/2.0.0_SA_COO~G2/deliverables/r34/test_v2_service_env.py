"""Offline test of v2_service_env_r34d.sh (issuer 2.0.0_SA_COO~G2): stub systemctl and systemd-run on PATH, a fake root holding the intake/yfinance_check.py under test,
a fake yfinance whose history() RAISES the real yfinance exception classes, and run the script. Prints one RESULT line:
V2S-SCRIPT-TEST-OK <n> cases or V2S-SCRIPT-TEST-FAIL <why>. No network, no AWS, no host.

usage: python test_v2_service_env.py        (run from the repository root; needs bash)
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip())
HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "v2_service_env_r34d.sh"
CHECKER = REPO / "infra/aws/lambda/investor-reporting/intake/yfinance_check.py"
EXC = REPO / "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/yfinance_exceptions_1_2_0.py"
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


FAKE_YF = '''
import importlib.util
__version__ = "1.2.0-fake"
spec = importlib.util.spec_from_file_location("yf_exc", EXC_PATH)
exc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exc)


class _Cfg:
    pass


config = _Cfg()
config.debug = _Cfg()
config.debug.hide_exceptions = True


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
        if not config.debug.hide_exceptions:
            raise exc.YFPricesMissingError(self.symbol, "(1mo)")
        return _Frame([])
'''


def make_stubs(bindir, root):
    interp = sys.executable.replace("\\", "/")
    (bindir / "systemctl").write_text(
        '#!/bin/bash\n'
        'case "$*" in\n'
        '  *is-active*) echo active;;\n'
        '  *"-p MainPID"*) echo 4242;;\n'
        '  *"-p User"*) echo tester;;\n'
        '  *"-p WorkingDirectory"*) echo %s;;\n'
        '  *"-p Environment"*) echo "PYTHONPATH=%s PYTHONUNBUFFERED=1";;\n'
        '  *"-p ExecStart"*) echo "{ path=%s ; argv[]=%s %s/ycharts/generate/resident_main.py --factory x ; ignore_errors=no }";;\n'
        'esac\n' % (root, root, interp, interp, root), encoding="ascii")
    # the stub systemd-run keeps what the script hands a transient unit: the working directory and the environment
    (bindir / "systemd-run").write_text(
        '#!/bin/bash\n'
        'WD=; ENVS=\n'
        'while [ $# -gt 0 ]; do\n'
        '  case "$1" in\n'
        '    -p) shift; case "$1" in WorkingDirectory=*) WD="${1#WorkingDirectory=}";; esac;;\n'
        '    --setenv=*) ENVS="$ENVS ${1#--setenv=}";;\n'
        '    --uid=*|--quiet|--wait|--pipe|--collect) ;;\n'
        '    *) break;;\n'
        '  esac\n'
        '  shift\n'
        'done\n'
        'cd "$WD" || exit 99\n'
        'exec env $ENVS "$@"\n', encoding="ascii")
    for f in bindir.iterdir():
        f.chmod(0o755)


def run(tmp, checker_text, want_root=None):
    root = tmp / "root"
    bindir = tmp / "bin"
    for d in (root, bindir):
        if d.exists():
            shutil.rmtree(d)
    (root / "intake").mkdir(parents=True)
    bindir.mkdir()
    (root / "intake" / "yfinance_check.py").write_text(checker_text, encoding="utf-8")
    (root / "yfinance.py").write_text("EXC_PATH = %r\n%s" % (EXC.as_posix(), FAKE_YF), encoding="utf-8")
    make_stubs(bindir, root.as_posix())
    env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"], MSYS_NO_PATHCONV="1",
               V2S_WANT_ROOT=want_root if want_root is not None else root.as_posix(), V2S_PYFILE=(tmp / "v2s.py").as_posix())
    proc = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
    return proc.returncode, proc.stdout + proc.stderr


tmp = Path(tempfile.mkdtemp(prefix="v2s_test_"))
try:
    check("bash -n", subprocess.run(["bash", "-n", str(SCRIPT)]).returncode == 0)
    check("script is ASCII", all(b < 128 for b in SCRIPT.read_bytes()))
    fixed = CHECKER.read_text(encoding="utf-8")
    check("the checker under test carries the fix", "def _is_ticker_missing(exc):" in fixed)
    rc, out = run(tmp, fixed)
    check("the fixed checker: SPY KEPT, ZQXWVK NOT_KEPT, V2S OK, rc 0", rc == 0 and "V2S OK SPY KEPT and ZQXWVK NOT_KEPT" in out, "rc=%d %s" % (rc, out[-400:]))
    check("the process had the unit's working directory and environment", "cwd=" in out and "uid=" in out and "1.2.0-fake" in out, out[-300:])
    check("the run printed the result line with both states", '"state": "KEPT"' in out and '"state": "NOT_KEPT"' in out, out[-300:])
    unfixed = fixed.replace("def _is_ticker_missing(exc):", "def _is_ticker_missing_disabled(exc):").replace(
        "if _is_ticker_missing(exc):", "if False:")
    rc, out = run(tmp, unfixed)
    check("the pre-fix checker reads CHECK_FAILED for ZQXWVK: V2S FAIL, rc 1", rc == 1 and "V2S FAIL" in out and "CHECK_FAILED" in out, "rc=%d %s" % (rc, out[-300:]))
    rc, out = run(tmp, fixed, want_root="/opt/irpt-resident/0485393f3a-r34d")
    check("the root guard refuses a root that is not the wanted r34d root (rc 62)", rc == 62 and "V2S FAIL" in out, "rc=%d %s" % (rc, out[-300:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("V2S-SCRIPT-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("V2S-SCRIPT-TEST-OK %d cases" % len(cases))
