"""MDPF_STRATID round 1, ST-t-1 criterion AC1: the Cottonwood slice measures each Opal SMA sleeve's model overlap per date. T1-OK when every named test PASSED; else T1-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ['test_overlap_zero_when_no_sleeve_account_has_a_model', 'test_overlap_counts_dollars_of_sleeve_accounts_with_a_model', 'test_overlap_none_when_assignments_absent_for_date', 'test_overlap_field_aligned_to_dates']

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/gold/tests/test_cottonwood_sma_overlap.py", "T1-OK", "T1-BAD", TESTS))
