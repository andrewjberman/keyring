"""MDPF_DEMQUE DQ-t-77 criterion AC1 (named tests in test_demque_sweep.py, no network). SWEEP-OK when every named test PASSED; else SWEEP-BAD.
Run from the worktree root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_sweep_draws_on_a_trading_day_up_to_the_daily_total_left",
    "test_the_sweep_ignores_surface_lines_and_the_untagged_ceiling",
    "test_the_sweep_counts_production_and_the_morning_fire_once_each",
    "test_an_unreadable_production_ledger_gives_the_sweep_no_room",
    "test_the_sweep_runs_once_a_day_and_never_draws_a_held_request",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_sweep.py", "SWEEP-OK", "SWEEP-BAD", TESTS))
