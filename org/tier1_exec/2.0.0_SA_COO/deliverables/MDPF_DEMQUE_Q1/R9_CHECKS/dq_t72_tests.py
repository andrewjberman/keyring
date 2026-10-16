"""MDPF_DEMQUE round 9, DQ-t-72 criterion AC1 (named tests in test_demque_empty_cooldown.py, no network). COOLT-OK when every named test PASSED; else COOLT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_symbol_that_returned_empty_within_the_cooldown_is_not_requested_again_and_uses_no_budget",
    "test_a_symbol_that_returned_empty_before_the_cooldown_is_requested_again",
    "test_an_ok_symbol_and_a_new_symbol_behave_as_before_and_a_pushback_still_stops_the_run",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_empty_cooldown.py", "COOLT-OK", "COOLT-BAD", TESTS))
