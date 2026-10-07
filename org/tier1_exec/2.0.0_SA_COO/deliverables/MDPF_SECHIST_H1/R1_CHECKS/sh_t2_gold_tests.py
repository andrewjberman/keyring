"""MDPF_SECHIST round 1, criterion SH1-t2-AC1: Positioning gold reads a year of backfill rows carried
in one daily history_topup partition, and computes every window from them.

Runs the cell's own test file under pytest (from the gold folder, where its sibling tests import
`etf_positioning_gold` bare) and requires each named test PASSED by name.
Last line: GOLD-TESTS-OK or GOLD-TESTS-BAD <reason>.
"""
from __future__ import annotations

import os
import subprocess
import sys

GOLD = os.path.join("data", "etfs", "scripts", "gold")
TEST_FILE = "test_etf_positioning_backfill_rows.py"
REQUIRED = [
    "test_backfill_rows_in_topup_fill_all_windows",
    "test_single_row_only_1d_control",
]


def main() -> int:
    r = subprocess.run([sys.executable, "-m", "pytest", "-v", "-p", "no:cacheprovider", TEST_FILE],
                       capture_output=True, text=True, timeout=110, check=False, cwd=GOLD)
    out = r.stdout + r.stderr
    print(out[-3000:])
    missing = [t for t in REQUIRED if not any(t in ln and "PASSED" in ln for ln in out.splitlines())]
    if r.returncode != 0:
        print("GOLD-TESTS-BAD rc=" + str(r.returncode))
        return 1
    if missing:
        print("GOLD-TESTS-BAD not-passed=" + ",".join(missing))
        return 1
    print("GOLD-TESTS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
