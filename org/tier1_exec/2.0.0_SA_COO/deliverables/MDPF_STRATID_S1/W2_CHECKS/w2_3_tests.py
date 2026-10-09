"""MDPF_STRATID workstream 2, W2-3 criterion AC1: the unidentified-strategy list (C-UNIDENTIFIED): a sleeve that looks like an
Opal strategy but matched no member, or matched a rule with no member, is listed with firm, name and dollars; a matched sleeve
is not listed. W23-OK when every named test PASSED; else W23-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ["test_opal_named_unmatched_sleeve_is_listed", "test_ticker_named_unmatched_is_listed", "test_matched_sleeve_is_not_listed",
         "test_null_member_rule_is_listed_with_reason", "test_non_opal_name_is_not_listed", "test_row_carries_firm_name_dollars_reason"]

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/silver/tests/test_opal_unidentified.py", "W23-OK", "W23-BAD", TESTS))
