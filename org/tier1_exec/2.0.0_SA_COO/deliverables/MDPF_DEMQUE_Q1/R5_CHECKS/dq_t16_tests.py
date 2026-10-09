"""MDPF_DEMQUE round 5, DQ-t-16 (ADDENDUM v0.4 standing request + state; CTO round-4 analysis item 2) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_standing.py (stub S3 only). STAND-OK when every named test PASSED; else STAND-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_standing_request_quotes_its_per_run_cap', 'test_state_written_once_to_builder_address_with_state_as_of_reason', 'test_paused_reads_paused_and_unknown_state_refused']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_standing.py', 'STAND-OK', 'STAND-BAD', TESTS))
