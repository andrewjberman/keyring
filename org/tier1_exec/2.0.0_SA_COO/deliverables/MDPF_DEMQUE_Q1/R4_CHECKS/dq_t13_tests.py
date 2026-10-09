"""MDPF_DEMQUE round 4, DQ-t-13 (FWD-9 within-tier ranking, CTO msg 1519 item 3) criterion AC1: by named tests in data/mdpf/scripts/demque/test_demque_rank.py (no network, no Bloomberg, no
S3 write). RANK-OK when every named test PASSED; else RANK-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_living_client_outranks_match_open_outranks_gone', 'test_within_priority_score_is_held_days_times_accounts_times_largest_purchase', 'test_gone_client_unmatchable_fund_is_not_pursued', 'test_draw_order_is_tier_then_rank', 'test_each_item_carries_its_rank_and_reason']

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_rank.py", "RANK-OK", "RANK-BAD", TESTS))
