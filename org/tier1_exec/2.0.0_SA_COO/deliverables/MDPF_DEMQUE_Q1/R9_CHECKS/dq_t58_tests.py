"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_incremental_wiring.py, no network, a local store directory). WIRE-OK when every named test PASSED; else WIRE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_stored_name_takes_the_five_day_window_and_appends_only_new_rows_with_tr_columns_and_an_extended_lock",
    "test_a_gained_split_or_a_restated_overlap_bar_is_held_restatement_and_the_name_keeps_its_files",
    "test_a_gap_beyond_five_days_pulls_from_the_stored_max_and_appends_only",
    "test_the_receipt_lists_names_appended_without_a_relock_and_a_failed_lock_check_makes_the_name_held",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_incremental_wiring.py", "WIRE-OK", "WIRE-BAD", TESTS))
