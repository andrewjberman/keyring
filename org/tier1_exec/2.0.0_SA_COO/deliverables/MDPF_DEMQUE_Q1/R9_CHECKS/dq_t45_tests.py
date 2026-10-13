"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_yahoo_need_class.py, no network). YCLASS-OK when every named test PASSED; else YCLASS-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_yahoo_request_without_a_declared_need_class_or_window_start_is_refused_at_validate', 'test_a_yahoo_window_before_2012_or_a_security_start_before_the_declared_window_start_is_refused_never_trimmed', 'test_the_standing_extension_request_declares_client_and_a_window_start_on_or_after_the_floor']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_yahoo_need_class.py', 'YCLASS-OK', 'YCLASS-BAD', TESTS))
