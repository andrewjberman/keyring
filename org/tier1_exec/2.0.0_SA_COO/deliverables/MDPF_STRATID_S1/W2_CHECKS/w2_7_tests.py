"""MDPF_STRATID workstream 2, ST-w-7 criterion AC1: every Cottonwood slice run carries the unidentified-strategy list (decomposition
amendment A10). W27-OK when every named test PASSED; else W27-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ["test_composed_carries_unidentified_block", "test_planted_opal_name_is_listed_with_firm_name_dollars",
         "test_opal_model_and_matched_member_not_listed", "test_figures_unchanged_by_the_list"]

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/gold/tests/test_cottonwood_unidentified_wiring.py", "W27-OK", "W27-BAD", TESTS))
