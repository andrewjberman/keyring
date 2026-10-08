"""MDPF_HEALGAP round 2, HG-t-6 (FWD-3) criterion AC1: the repair act and the missing-and-why mark, by named tests in
`test_healgap_repair.py` (run from the runner folder). REPAIR-OK when every named test PASSED; else REPAIR-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run  # noqa: E402

TESTS = [
    "test_manifest_printed_before_any_fetch",
    "test_repair_refuses_a_past_date_with_reason",
    "test_repair_names_exactly_the_missing_feeds",
    "test_missing_mark_payload_names_feed_and_reason",
    "test_missing_mark_never_writes_a_feed_key",
]

if __name__ == "__main__":
    sys.exit(run("test_healgap_repair.py", "REPAIR-OK", "REPAIR-BAD", TESTS))
