"""MDPF_DEMQUE round 9, DQ-t-64 criterion AC1 (named tests in test_demque_inactive_set.py, stub frames, no network). INACTIVE-OK when every named test PASSED; else INACTIVE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_inactive_set_is_the_held_cusips_not_in_the_active_set_and_a_blank_cusip_is_never_held",
    "test_the_census_adds_up_classes_symbols_and_stored_against_the_inactive_total",
    "test_nights_at_cap_is_the_ceiling_of_symbols_over_the_request_cap",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_inactive_set.py", "INACTIVE-OK", "INACTIVE-BAD", TESTS))
