"""MDPF_DEMQUE round 9, DQ-t-73 criterion AC1 (named tests in test_demque_budget.py, no network). BUDGT-OK when every named test PASSED; else BUDGT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_budget_block_sums_to_the_daily_total_and_every_figure_carries_its_claim",
    "test_the_history_ceiling_and_a_quote_are_unchanged_by_the_budget_block",
    "test_a_ceiling_or_reserve_write_keeps_the_budget_block",
    "test_surface_of_maps_each_page_family_and_refuses_to_guess",
    "test_apply_tags_a_bloomberg_request_by_text_insertion_and_leaves_every_other_byte",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_budget.py", "BUDGT-OK", "BUDGT-BAD", TESTS))
