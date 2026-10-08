"""MDPF_SECHIST round 2, criterion SH2-t4-AC1: the ETF daily pull's run record prints the backfill draw beside the remainder.

Runs the pull's history-plan test file under pytest and requires each named test PASSED by name, so an empty or renamed
file cannot pass. Offline: the tests use fakes, never S3 or Bloomberg.
Last line: BUDGET-TESTS-OK or BUDGET-TESTS-BAD <reason>.
"""
from __future__ import annotations

import subprocess
import sys

TEST_FILE = "integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py"
REQUIRED = [
    "test_backfill_budget_refusal_and_record",
    "test_run_record_prints_draw_and_remainder",
]


def main() -> int:
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", TEST_FILE],
                       capture_output=True, text=True, timeout=110, check=False)
    out = r.stdout + r.stderr
    print(out[-3000:])
    missing = [t for t in REQUIRED if not any(t in ln and "PASSED" in ln for ln in out.splitlines())]
    if r.returncode != 0:
        print("BUDGET-TESTS-BAD rc=" + str(r.returncode))
        return 1
    if missing:
        print("BUDGET-TESTS-BAD not-passed=" + ",".join(missing))
        return 1
    print("BUDGET-TESTS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
