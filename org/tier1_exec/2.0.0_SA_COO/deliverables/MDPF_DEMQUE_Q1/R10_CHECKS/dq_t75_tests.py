"""MDPF_DEMQUE DQ-t-75 criterion AC1 (named tests in test_demque_empty_window.py, no network). EMPTY-OK when every named test PASSED; else EMPTY-BAD.
Run from the worktree root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_an_empty_window_is_skipped_and_the_run_continues_to_the_next_security",
    "test_a_cooled_window_is_not_asked_again_for_seven_days_and_is_asked_once_after",
    "test_more_than_five_empty_windows_in_one_fire_stop_the_run",
    "test_an_incomplete_row_or_a_refusal_still_stops_the_run",
    "test_the_receipt_lists_empty_windows_and_a_second_empty_makes_a_standing_gap",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_empty_window.py", "EMPTY-OK", "EMPTY-BAD", TESTS))
