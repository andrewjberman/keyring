"""IRPT_ANLREQ round 43, workstream T -- the issuer's mechanical check (2.0.0_SA_COO~T2).

  cn1  R43-CN1  CTO condition 4 (msg 8577): feeding the drafter's figure projection a dollar amount, a name and an account id drops all
                three; tickers must be in the estate's classification table and model names must be among the request's own
                comparison keys (three named tests pass, in the existing figures test file)

Prints R43-<TOKEN>-OK or R43-<TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TEST_FILE = Path("data/transcripts/scripts/tests/test_commentary_figures.py")
NAMES = ["test_condition_dollar_name_and_account_id_are_all_dropped",
         "test_tickers_must_be_in_the_estate_table",
         "test_model_names_must_be_among_the_requests_comparison_keys"]
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def check():
    if not TEST_FILE.exists():
        return False, "absent: %s" % TEST_FILE.as_posix()
    text = TEST_FILE.read_text(encoding="utf-8")
    missing = [n for n in NAMES if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(TEST_FILE), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=300)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""]
    tail = ANSI.sub("", lines[-1])
    m = re.search(r"(\d+) passed", tail)
    passed = int(m.group(1)) if m else 0
    return (r.returncode == 0 and passed >= 4 + len(NAMES) and "failed" not in tail), tail


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] != "cn1":
        print("usage: r43_checks.py cn1")
        sys.exit(2)
    ok, why = check()
    print("R43-CN1-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
