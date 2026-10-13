"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_active_windows.py, no network). WIN-OK when every named test PASSED; else WIN-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_active_set_is_refused_when_its_sha256_differs_and_is_never_printed_by_account",
    "test_a_security_window_is_the_union_of_its_active_accounts_held_dates_floored_at_2012_and_open_when_any_account_still_holds_it",
    "test_the_b1_request_is_clipped_to_the_active_window_leaves_a_name_outside_the_set_unclipped_and_holds_back_a_p2_name",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_active_windows.py", "WIN-OK", "WIN-BAD", TESTS))
