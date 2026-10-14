"""MDPF_DEMQUE round 9, DQ-t-61 criterion AC1 (named tests in test_demque_b1_names_mode.py, stub frames, no network). NAMES-OK when every named test PASSED; else NAMES-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_named_cusip_list_builds_the_option_c_request_over_those_names_only",
    "test_the_named_request_carries_its_own_request_id_and_the_default_b1_request_id_is_unchanged",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_b1_names_mode.py", "NAMES-OK", "NAMES-BAD", TESTS))
