"""NFRA_TRNSPT round 9 -- the issuer's mechanical checks (2.0.0_SA_COO~T2), one subcommand per criterion.

  w9-write   TR9-w9-AC1  the research-store test file passes and holds, by name: the 29 keys written to a fake s3 equal
                         lib/opal_naming address() output and carry a held_out column; the stored-bytes verifier finds 0 wipeable
                         tokens in non-held-out rows; and read_meeting reads a research_meeting parquet (start_utc None)

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST = Path("data/transcripts/scripts/tests/test_research_store.py")
NAMES = ["test_keys_equal_builder_and_held_out_column", "test_stored_bytes_rewipe_clean", "test_read_meeting_reads_research_parquet"]


def w9_write():
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
    return (r.returncode == 0 and passed >= 3), tail


CHECKS = {"w9-write": ("R9-W9-WRITE", w9_write)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r9_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
