"""MDPF_DEMQUE round 2, DQ-t-8 (row D1-W4-S1; FWD-1 hop 6) criterion AC1: Cottonwood's price build survives the absent Tier-2
objects, by named tests in data/cot/scripts/gold/test_s00_missing_tier2.py (S3 stubbed). S00-OK when every named test PASSED;
else S00-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_dir import run  # noqa: E402

TESTS = [
    "test_missing_historical_prices_skips_tier2_and_writes",
    "test_missing_ticker_lookup_skips_tier2_and_writes",
    "test_present_tier2_is_still_joined",
]

if __name__ == "__main__":
    sys.exit(run(os.path.join("data", "cot", "scripts", "gold"), "test_s00_missing_tier2.py", "S00-OK", "S00-BAD", TESTS))
