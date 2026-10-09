"""NFRA_TRNSPT round 15 -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  j15   TR15-j15-AC1  the classification-join test file passes and holds, by name: categories derive from the canonical table by
                      security id, coverage (classified share of total weight) is printed, and every unclassified holding is named,
                      never guessed

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("data/transcripts/scripts/tests/test_commentary_classification.py")
NAMES = ["test_categories_from_canonical_join", "test_unclassified_named_never_guessed", "test_coverage_reported"]


def j15():
    if not TEST.exists():
        return False, "absent: %s" % TEST.as_posix()
    text = TEST.read_text(encoding="utf-8")
    missing = [n for n in NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(NAMES)), tail


CHECKS = {"j15": ("R15-J15", j15)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r15_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
