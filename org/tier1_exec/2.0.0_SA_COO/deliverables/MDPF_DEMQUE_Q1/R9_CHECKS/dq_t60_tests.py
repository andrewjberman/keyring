"""MDPF_DEMQUE round 9, DQ-t-60 criterion AC1 (named tests in test_demque_active_windows.py, no network). V2-OK when every named test PASSED; else V2-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_pinned_active_set_is_the_v2_file_and_a_v1_hash_is_refused",
    "test_the_four_bonds_v1_held_back_window_in_when_the_v2_set_names_them",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_active_windows.py", "V2-OK", "V2-BAD", TESTS))
