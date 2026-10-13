"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_priority_gate.py, no network). GATE-OK when every named test PASSED; else GATE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_p3_name_is_never_pursued_and_a_p2_name_waits_on_its_match_while_p1_is_unchanged', 'test_the_standing_extension_tiers_leave_out_p2_and_p3_names_and_count_them', 'test_the_daily_draw_skips_an_excluded_request_security_and_counts_the_skip']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_priority_gate.py', 'GATE-OK', 'GATE-BAD', TESTS))
