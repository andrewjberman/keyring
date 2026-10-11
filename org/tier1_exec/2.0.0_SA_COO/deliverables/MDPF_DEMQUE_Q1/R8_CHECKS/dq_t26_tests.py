"""MDPF_DEMQUE round 8, DQ-t-26 (CTO round-7 analysis R2, quote half) criterion AC1: named tests in test_demque_refreeze.py (no network). RF-OK when every named test PASSED; else RF-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")

TESTS = ['test_quote_counts_only_scheduled_non_trading_days', 'test_refreeze_writes_beside_and_keeps_the_superseded_quote', 'test_quote_vs_actual_grades_the_refrozen_quote_and_prints_both']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_refreeze.py', 'RF-OK', 'RF-BAD', TESTS))
