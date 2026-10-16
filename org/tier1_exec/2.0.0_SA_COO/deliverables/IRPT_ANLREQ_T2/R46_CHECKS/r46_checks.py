"""IRPT_ANLREQ round 46, workstream TX -- the issuer's mechanical check for cross-firm TEST files (2.0.0_SA_COO~T2).

  red <min_failed> <test_file> [<test_file> ...]
        acceptance tests written AHEAD of a fix: names as below; at least <min_failed> FAIL now and none errors out
        (prints R46-RED-OK red=<n> or R46-RED-FAIL <reason>).
  tests <min_passed> <test_file> [<test_file> ...]
        every file exists; every test function in each is named `test_cross_firm_*`; pytest over all of them passes with no
        failure or error and at least <min_passed> tests passed; at least <min_passed> test functions are defined.
  --self-test
        a green pair, then four mutants (a failing test, a mis-named test, too few tests, an absent file); each mutant must fail.

Prints R46-TESTS-OK passed=<n> or R46-TESTS-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ANSI = re.compile(r"\x1b\[[0-9;]*m")
DEF = re.compile(r"^\s*(?:async\s+)?def\s+(test_\w+)\s*\(", re.M)
PREFIX = "test_cross_firm_"   # --prefix=<p> as the first argument after the mode overrides it (FWD-4 cells name tests test_hop_failure_*)


def check(min_passed, files, cwd=None):
    names = []
    for f in files:
        p = Path(f)
        if not p.is_file():
            return False, "absent: %s" % Path(f).as_posix()
        found = DEF.findall(p.read_text(encoding="utf-8"))
        bad = [n for n in found if not n.startswith(PREFIX)]
        if bad:
            return False, "%s: test(s) not named test_cross_firm_*: %s" % (p.name, ", ".join(bad[:3]))
        names += found
    if len(names) < min_passed:
        return False, "only %d test functions defined, need %d" % (len(names), min_passed)
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"] + [str(f) for f in files],
                       capture_output=True, text=True, timeout=600, cwd=cwd)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""]
    tail = ANSI.sub("", lines[-1])
    m = re.search(r"(\d+) passed", tail)
    passed = int(m.group(1)) if m else 0
    if r.returncode != 0 or re.search(r"\d+ failed", tail) or "error" in tail.lower():
        return False, tail
    if passed < min_passed:
        return False, "%d passed, need %d: %s" % (passed, min_passed, tail)
    return True, "passed=%d" % passed


def check_red(min_failed, files, cwd=None):
    """Acceptance tests written ahead of a fix: they must be RED now -- at least min_failed fail, none errors out."""
    for f in files:
        p = Path(f)
        if not p.is_file():
            return False, "absent: %s" % p.as_posix()
        bad = [n for n in DEF.findall(p.read_text(encoding="utf-8")) if not n.startswith(PREFIX)]
        if bad:
            return False, "%s: test(s) not named test_cross_firm_*: %s" % (p.name, ", ".join(bad[:3]))
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"] + [str(f) for f in files],
                       capture_output=True, text=True, timeout=600, cwd=cwd)
    tail = ANSI.sub("", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    m = re.search(r"(\d+) failed", tail)
    failed = int(m.group(1)) if m else 0
    if re.search(r"\d+ error", tail):
        return False, "collection or setup error, not a red test: " + tail
    if failed < min_failed:
        return False, "%d failed, need at least %d red: %s" % (failed, min_failed, tail)
    return True, "red=%d" % failed


def self_test():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        good = d / "test_cross_firm_a.py"
        good.write_text("def test_cross_firm_one():\n    assert 1 == 1\n\ndef test_cross_firm_two():\n    assert 2 == 2\n", encoding="utf-8")
        bad_fail = d / "test_cross_firm_b.py"
        bad_fail.write_text("def test_cross_firm_x():\n    assert 1 == 2\n", encoding="utf-8")
        bad_name = d / "test_cross_firm_c.py"
        bad_name.write_text("def test_cross_firm_ok():\n    assert True\n\ndef test_other_thing():\n    assert True\n", encoding="utf-8")
        cases = [("green", 2, [good], True), ("failing test", 1, [bad_fail], False), ("mis-named test", 1, [bad_name], False),
                 ("too few tests", 3, [good], False), ("absent file", 1, [d / "nope.py"], False)]
        for name, n, files, want in cases:
            ok, why = check(n, files)
            if ok != want:
                print("R46-SELFTEST-FAIL %s: got ok=%s (%s)" % (name, ok, why))
                return 1
        broken = d / "test_cross_firm_d.py"
        broken.write_text("def test_cross_firm_y(:\n", encoding="utf-8")
        red_cases = [("red: failing test is red", 1, [bad_fail], True), ("red: passing test is not red", 1, [good], False),
                     ("red: syntax error is not red", 1, [broken], False), ("red: absent file", 1, [d / "nope.py"], False)]
        for name, n, files, want in red_cases:
            ok, why = check_red(n, files)
            if ok != want:
                print("R46-SELFTEST-FAIL %s: got ok=%s (%s)" % (name, ok, why))
                return 1
    print("R46-SELFTEST-OK green plus four mutants refused, red mode plus three mutants refused")
    return 0


if __name__ == "__main__":
    for _a in [a for a in sys.argv[1:] if a.startswith("--prefix=")]:
        PREFIX = _a.split("=", 1)[1]
        sys.argv.remove(_a)
    if len(sys.argv) >= 2 and sys.argv[1] == "--self-test":
        sys.exit(self_test())
    if len(sys.argv) >= 4 and sys.argv[1] == "red" and sys.argv[2].isdigit():
        ok, why = check_red(int(sys.argv[2]), sys.argv[3:])
        print("R46-RED-%s %s" % ("OK" if ok else "FAIL", why))
        sys.exit(0 if ok else 1)
    if len(sys.argv) < 4 or sys.argv[1] != "tests" or not sys.argv[2].isdigit():
        print("usage: r46_checks.py tests|red <min> <test_file> [...] | --self-test")
        sys.exit(2)
    ok, why = check(int(sys.argv[2]), sys.argv[3:])
    print("R46-TESTS-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
