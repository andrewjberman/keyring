"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_window_exception.py, no network). EXC-OK when every named test PASSED; else EXC-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_model_block_with_the_named_research_app_exception_is_admitted_from_2016_and_no_earlier', 'test_the_exception_is_refused_on_another_channel_another_class_or_an_unnamed_reason', 'test_the_rule_still_refuses_an_undeclared_exception_and_a_start_before_2012']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_window_exception.py', 'EXC-OK', 'EXC-BAD', TESTS))
