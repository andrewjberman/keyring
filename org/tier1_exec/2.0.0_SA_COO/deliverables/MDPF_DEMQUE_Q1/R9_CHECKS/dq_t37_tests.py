"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_extend_future.py, no network). FUT-OK when every named test PASSED; else FUT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_plan_refuses_a_today_after_the_local_date', 'test_apply_refuses_a_future_today_and_writes_nothing', 'test_today_equal_to_the_local_date_still_plans']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_extend_future.py', 'FUT-OK', 'FUT-BAD', TESTS))
