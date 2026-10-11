"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_extend_guard.py, no network). GUARD-OK when every named test PASSED; else GUARD-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_plan_refuses_a_frontier_before_the_latest_valid_to_in_the_store', 'test_apply_writes_nothing_and_resets_nothing_when_the_plan_would_shorten_a_file', 'test_a_frontier_on_or_after_the_latest_valid_to_still_plans']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_extend_guard.py', 'GUARD-OK', 'GUARD-BAD', TESTS))
