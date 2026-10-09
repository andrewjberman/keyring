"""MDPF_STRATID workstream 2, W2-2 criterion AC1: one shared matcher (sleeve name -> strategy member) reads the ETF list and the
SMA name rules as data; today's behaviour is kept; a new ticker or rule row is found with no code edit. W22-OK when every named
test PASSED; else W22-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ["test_today_rules_unchanged", "test_two_hits_raise", "test_new_ticker_in_list_found_without_code_edit",
         "test_full_name_matches", "test_data_rule_row_found_without_code_edit", "test_null_member_rule_is_flagged_not_counted",
         "test_rebalancer_schemas_delegates_to_the_matcher"]

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/silver/tests/test_opal_strategy_matcher.py", "W22-OK", "W22-BAD", TESTS))
