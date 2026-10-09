"""MDPF_DEMQUE round 4, DQ-t-10 (C-RESERVE, CTO msg 1524) criterion AC1: by named tests in data/mdpf/scripts/demque/test_demque_reserve.py (no network, no Bloomberg, no
S3 write). RESERVE-OK when every named test PASSED; else RESERVE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_reserve_is_names_times_fields_times_rows_per_producer_run', 'test_margin_is_stated_and_applied', 'test_reserve_written_with_claim_held_and_basis', 'test_quote_finish_date_carries_held_when_reserve_is_held']

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_reserve.py", "RESERVE-OK", "RESERVE-BAD", TESTS))
