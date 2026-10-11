"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_standing_drawer_close.py, no network). CL-OK when every named test PASSED; else CL-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_request_whose_securities_all_reached_their_end_is_closed_and_skipped', 'test_the_completing_fire_records_complete_not_drawn', 'test_no_zero_cell_drawn_line_after_completion']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_standing_drawer_close.py', 'CL-OK', 'CL-BAD', TESTS))
