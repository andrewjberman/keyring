"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_extend_frontier.py, no network). XF-OK when every named test PASSED; else XF-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_plan_window_ends_at_the_expected_last_trading_day_and_lists_every_locked_symbol', 'test_apply_resets_exactly_the_plan_symbols_and_replaces_the_standing_request_file', 'test_run_daily_draw_runs_the_extension_before_the_draw']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_extend_frontier.py', 'XF-OK', 'XF-BAD', TESTS))
