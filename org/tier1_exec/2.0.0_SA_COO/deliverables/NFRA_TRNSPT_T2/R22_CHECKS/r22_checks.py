"""NFRA_TRNSPT round 22 -- the issuer's mechanical check (2.0.0_SA_COO~T2).

  c22   TR22-c22-AC1  teams/census.py: the fetchable-on-cutoff set with its denominator, each entry landed or missing with a completeness cause;
                      a --live CLI that only reads; counts only

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("data/transcripts/scripts/tests/test_census.py")
NAMES = ["test_cutoff_denominator_counts_only_on_or_before", "test_missing_entries_carry_a_completeness_cause",
         "test_live_reads_only_and_prints_no_text"]


def c22():
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


if __name__ == "__main__":
    if sys.argv[1:] != ["c22"]:
        print("usage: r22_checks.py c22")
        sys.exit(2)
    ok, why = c22()
    print("R22-C22-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
