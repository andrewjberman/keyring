"""MDPF_DEMQUE round 1, DQ-t-4 (FWD-1 hop 5) criterion AC1: the lander into Cottonwood's Yahoo tier, by named tests in
`test_demque_land.py` (run from data/mdpf/scripts/demque; S3 is stubbed). LAND-OK when every named test PASSED; else
LAND-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run  # noqa: E402

TESTS = [
    "test_only_locked_rows_inside_their_range_land",
    "test_close_written_is_the_as_traded_close",
    "test_existing_tickers_rows_are_never_rewritten",
    "test_lookup_entry_maps_cot_asset_name_to_symbol",
    "test_unmatched_security_is_listed_not_landed",
    "test_default_run_writes_nothing",
]

if __name__ == "__main__":
    sys.exit(run("test_demque_land.py", "LAND-OK", "LAND-BAD", TESTS))
