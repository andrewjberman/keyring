"""MDPF_STRATID workstream 2, ST-w-4 criterion AC1: the unidentified list excludes an Opal Model unless it also matches a sleeve
rule (amendment A1), and the six ST-w-3 tests still pass. W24-OK when every named test PASSED; else W24-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ["test_opal_named_unmatched_sleeve_is_listed", "test_ticker_named_unmatched_is_listed", "test_matched_sleeve_is_not_listed",
         "test_null_member_rule_is_listed_with_reason", "test_non_opal_name_is_not_listed", "test_row_carries_firm_name_dollars_reason",
         "test_opal_model_is_not_listed", "test_opal_model_matching_a_sleeve_rule_is_listed"]

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/silver/tests/test_opal_unidentified.py", "W24-OK", "W24-BAD", TESTS))
