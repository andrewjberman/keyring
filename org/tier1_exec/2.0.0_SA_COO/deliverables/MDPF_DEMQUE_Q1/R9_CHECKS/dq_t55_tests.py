"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_surface_e_cap.py, no network). CAP-OK when every named test PASSED; else CAP-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_cap_is_ten_percent_of_the_days_history_allowance_and_a_request_above_it_is_refused_naming_the_cap",
    "test_a_request_at_or_below_the_cap_is_accepted_and_the_remaining_reserve_is_printed",
    "test_a_refused_request_is_never_split_and_writes_nothing",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_surface_e_cap.py", "CAP-OK", "CAP-BAD", TESTS))
