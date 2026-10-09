"""MDPF_DEMQUE round 4, DQ-t-12 (FWD-5 unresolved list, CTO msg 1519 item 4) criterion AC1: by named tests in data/mdpf/scripts/demque/test_demque_unresolved.py (no network, no Bloomberg, no
S3 write). UNRES-OK when every named test PASSED; else UNRES-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_row_per_cusip_and_open_period_with_reason', 'test_failed_pull_and_rejected_lock_both_feed_the_list', 'test_partial_lock_leaves_only_the_uncovered_period_open', 'test_seed_file_loads_the_five_no_data_cusips', 'test_resolved_security_leaves_the_list']

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_unresolved.py", "UNRES-OK", "UNRES-BAD", TESTS))
