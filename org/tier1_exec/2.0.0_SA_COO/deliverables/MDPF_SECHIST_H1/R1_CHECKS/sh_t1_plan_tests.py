"""MDPF_SECHIST round 1, criterion SH1-t1-AC1: the history-plan tests of the ETF daily pull pass.

Runs the cell's own test file under pytest and requires each named test to be PASSED by name, so an
empty or renamed file cannot pass. Offline: the tests use fakes, never S3 or Bloomberg.
Last line: PLAN-TESTS-OK or PLAN-TESTS-BAD <reason>.
"""
from __future__ import annotations

import subprocess
import sys

TEST_FILE = "integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py"
REQUIRED = [
    "test_plan_new_security_gets_one_year",
    "test_plan_covered_security_not_requested",
    "test_plan_cap_bounds_count",
    "test_backfill_failure_keeps_production_rc",
]


def main() -> int:
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", TEST_FILE],
                       capture_output=True, text=True, timeout=110, check=False)
    out = r.stdout + r.stderr
    print(out[-3000:])
    missing = [t for t in REQUIRED if not any(t in ln and "PASSED" in ln for ln in out.splitlines())]
    if r.returncode != 0:
        print("PLAN-TESTS-BAD rc=" + str(r.returncode))
        return 1
    if missing:
        print("PLAN-TESTS-BAD not-passed=" + ",".join(missing))
        return 1
    print("PLAN-TESTS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
