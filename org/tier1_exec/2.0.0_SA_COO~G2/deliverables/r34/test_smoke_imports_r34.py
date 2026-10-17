"""Offline test of smoke_imports_r34.py (issuer 2.0.0_SA_COO~G2): a synthetic package-layout tree; the real reachability walk; a fresh `python -I` interpreter per case.
Prints SMOKE-TEST-OK <n> cases or SMOKE-TEST-FAIL. No network, no AWS.

usage: python test_smoke_imports_r34.py        (from anywhere inside the repository)
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SMOKE = HERE / "smoke_imports_r34.py"
REACH = HERE.parent / "r32" / "r32_reachability.py"
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


MAIN = '''
from pathlib import Path
import sys
_root = Path(__file__).resolve().parents[2]
for _relative in (%s):
    _path = _root / _relative
    if _path.is_dir():
        sys.path.insert(0, str(_path))
'''


def make_tree(root, with_lib=True, helper_extra=""):
    entries = ['"intake"', '"ops"', '"reports"'] + (['"lib"'] if with_lib else []) + ['"ycharts/session"']
    files = {
        "ycharts/generate/resident_main.py": MAIN % (", ".join(entries) + ","),
        "reports/resident_installed.py": "import helper_mod\n",
        "ycharts/research/opal_producer.py": "",
        "ycharts/research/opal_packager.py": "",
        "intake/helper_mod.py": "%s\n\ndef lazy():\n    import cal_mod\n    return cal_mod.X\n" % helper_extra,
        "lib/cal_mod.py": "X = 1\n",
        "ops/unused.py": "Y = 2\n",
        "ycharts/session/lease_mod.py": "Z = 3\n",
    }
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def run(root):
    proc = subprocess.run([sys.executable, "-I", str(SMOKE), str(root), str(REACH)], capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


tmp = Path(tempfile.mkdtemp(prefix="smoke_test_"))
try:
    check("bash-free: the tool and the walk exist", SMOKE.is_file() and REACH.is_file())
    check("the tool is ASCII", all(b < 128 for b in SMOKE.read_bytes()))
    tree = tmp / "good"
    make_tree(tree)
    rc, out = run(tree)
    check("lib on the tuple: every LIVE module imports, rc 0", rc == 0 and "fail=0" in out and "SMOKE live=" in out, "rc=%d %s" % (rc, out[-400:]))
    tree = tmp / "nolib"
    make_tree(tree, with_lib=False)
    rc, out = run(tree)
    check("lib off the tuple: the lazily imported lib module is a FAILURE naming it, rc 1", rc == 1 and "SMOKE FAIL lib/cal_mod.py: ModuleNotFoundError cal_mod" in out, "rc=%d %s" % (rc, out[-400:]))
    tree = tmp / "thirdparty"
    make_tree(tree, helper_extra="import a_library_nobody_has_zzz")
    rc, out = run(tree)
    check("a third-party library absent here is a NOTE, not a failure", rc == 0 and "SMOKE NOTE intake/helper_mod.py: a_library_nobody_has_zzz" in out, "rc=%d %s" % (rc, out[-400:]))
    tree = tmp / "raises"
    make_tree(tree, helper_extra="raise ValueError('boom at import')")
    rc, out = run(tree)
    check("a LIVE module that raises another exception on import is a FAILURE", rc == 1 and "ValueError" in out and "boom at import" in out, "rc=%d %s" % (rc, out[-400:]))
    check("the tool wrote nothing into the good tree (no __pycache__)", not list((tmp / "good").rglob("__pycache__")), str(list((tmp / "good").rglob("__pycache__"))[:3]))
    tree = tmp / "notuple"
    make_tree(tree)
    (tree / "ycharts/generate/resident_main.py").write_text("x = 1\n", encoding="utf-8")
    rc, out = run(tree)
    check("a built tree whose resident_main has no path tuple is refused", rc != 0 and "SMOKE-BAD" in out, "rc=%d %s" % (rc, out[-300:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("SMOKE-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("SMOKE-TEST-OK %d cases" % len(cases))
