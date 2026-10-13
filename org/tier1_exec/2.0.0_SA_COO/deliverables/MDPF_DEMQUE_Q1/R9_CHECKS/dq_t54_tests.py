"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_carry_over.py, no network). CARRY-OK when every named test PASSED; else CARRY-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_non_trading_day_room_is_the_measured_ceiling_plus_the_trading_day_cells_production_left_unused",
    "test_a_trading_day_production_overspent_carries_nothing_and_never_a_negative",
    "test_an_absent_or_unreadable_budget_ledger_carries_zero_and_the_receipt_says_so",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_carry_over.py", "CARRY-OK", "CARRY-BAD", TESTS))
