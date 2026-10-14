"""MDPF_DEMQUE round 9, DQ-t-63 criterion AC1 (named tests in test_demque_etfs_rivals_intake.py, stub frames, no network). INTAKE-OK when every named test PASSED; else INTAKE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_three_stages_are_disjoint_and_newest_first_and_their_union_is_the_365_day_set",
    "test_a_unit_is_one_security_on_one_trading_day_and_dates_entries_validate_under_bbg_quote",
    "test_the_dividend_request_is_one_reference_cell_per_security_and_excludes_a_null_key",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_etfs_rivals_intake.py", "INTAKE-OK", "INTAKE-BAD", TESTS))
