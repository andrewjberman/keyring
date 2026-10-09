"""MDPF_DEMQUE round 6, DQ-t-19 (FWD-4 exercised; CTO round-5 analysis item 1) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_quote_vs_actual.py (temporary files only). QVA-OK when every named test PASSED; else QVA-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_on_time_when_drawn_on_or_before_finish_day', 'test_late_when_drawn_after_finish_day', 'test_open_when_no_actual_yet']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_quote_vs_actual.py', 'QVA-OK', 'QVA-BAD', TESTS))
