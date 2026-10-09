"""MDPF_DEMQUE round 5, DQ-t-15 (FWD-4 per-kind ceilings; CTO round-4 analysis item 1) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_ceiling.py (no network, no Bloomberg, no S3). CEIL-OK when every named test PASSED; else CEIL-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_ceiling_is_largest_ledger_day_per_channel_never_lowered', 'test_ceiling_carries_claim_held_and_basis', 'test_model_block_finish_is_later_of_its_component_channels']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_ceiling.py', 'CEIL-OK', 'CEIL-BAD', TESTS))
