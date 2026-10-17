"""MDPF_DEMQUE DQ-t-69 criterion AC1 (named tests in test_demque_surface_room.py, no network). SURF-OK when every named test PASSED; else SURF-BAD.
Run from the worktree root.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_surface_c_request_quotes_the_surface_budget_less_what_surface_c_drew_today",
    "test_an_untagged_request_still_quotes_the_history_ceiling",
    "test_the_drawer_draws_a_surface_c_request_past_the_history_ceiling_on_a_non_trading_day",
    "test_surface_cells_never_exceed_the_daily_total_and_each_surface_has_its_own_room",
    "test_a_trading_day_still_draws_nothing_for_a_surface_tagged_request",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_surface_room.py", "SURF-OK", "SURF-BAD", TESTS))
