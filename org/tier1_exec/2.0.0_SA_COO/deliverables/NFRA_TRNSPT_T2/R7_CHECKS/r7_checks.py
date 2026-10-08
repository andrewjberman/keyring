"""NFRA_TRNSPT round 7 -- the issuer's mechanical checks (2.0.0_SA_COO~T2), one subcommand per criterion.

  g7-class   TR7-g7-AC1  the encrypted-class test file passes and holds, by name: the author+client encrypted-only email lands
                         with class ENCRYPTED_UNVERIFIED and is held out in silver; the author email failing the client test does
                         not land
  g7-gold    TR7-g7-AC2  the same file holds and passes the test that no gold row ever carries the class
  h7-match   TR7-h7-AC1  the completeness test file passes and holds the one-day-shift match test and the two-day negative test

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")


def _pytest(path, k=None):
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    cmd = [sys.executable, "-m", "pytest", str(path), "-q", "-p", "no:cacheprovider"]
    if k:
        cmd += ["-k", k]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=110)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    tail = re.sub(r"\x1b\[[0-9;]*m", "", lines[-1] if lines else "")
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    if r.returncode != 0 or passed == 0:
        return False, "rc=%d %s" % (r.returncode, tail)
    return True, "passed=%d" % passed


def _needs(path, names):
    if not path.exists():
        return "absent: %s" % path.as_posix()
    text = path.read_text(encoding="utf-8")
    missing = [n for n in names if "def %s(" % n not in text]
    return ("missing %s" % ", ".join(missing)) if missing else None


def g7_class():
    path = TESTS / "test_encrypted_class.py"
    names = ["test_encrypted_author_client_lands_class_held_out", "test_encrypted_author_nonclient_not_landed"]
    why = _needs(path, names)
    if why:
        return False, why
    return _pytest(path, " or ".join(names))


def g7_gold():
    path = TESTS / "test_encrypted_class.py"
    why = _needs(path, ["test_no_gold_row_carries_class"])
    if why:
        return False, why
    return _pytest(path, "test_no_gold_row_carries_class")


def h7_match():
    path = TESTS / "test_completeness.py"
    why = _needs(path, ["test_one_day_shift_matched", "test_two_day_offset_not_matched"])
    if why:
        return False, why
    return _pytest(path)


CHECKS = {"g7-class": ("R7-G7-CLASS", g7_class), "g7-gold": ("R7-G7-GOLD", g7_gold), "h7-match": ("R7-H7-MATCH", h7_match)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r7_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
