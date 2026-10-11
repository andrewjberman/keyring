"""MDPF_DEMQUE round 8, DQ-t-28 (D1-S8) criterion AC1: named tests in test_demque_redraw_stale.py (stub S3 and stub pacer, no network). RDS-OK when every named test PASSED; else RDS-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")

TESTS = ['test_lists_only_files_with_the_original_three_columns', 'test_resets_exactly_those_symbols_in_the_pacer_and_enqueues_one_request', 'test_second_run_with_no_stale_files_enqueues_nothing']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_redraw_stale.py', 'RDS-OK', 'RDS-BAD', TESTS))
