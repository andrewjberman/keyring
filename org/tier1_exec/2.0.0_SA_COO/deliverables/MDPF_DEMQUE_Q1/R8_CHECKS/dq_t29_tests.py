"""MDPF_DEMQUE round 8, DQ-t-29 (rows D1-S6 and D1-S7, batched repair) criterion AC1: named tests in two files, no network.
test_demque_bbg_ledger_upload.py: the existing `test_reads_record_lines_and_converts_rows_to_cells_per_mode` PASSES again and
`test_name_to_literal_assignment_is_resolved_before_literal_eval` is new. test_demque_land.py: `test_consumer_keys_resolve_through_the_registry_legacy_rows`
is new and the file imports (no SystemExit at collection). FIX-OK when every named test PASSED in both files; else FIX-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
UPLOAD = ["test_reads_record_lines_and_converts_rows_to_cells_per_mode", "test_name_to_literal_assignment_is_resolved_before_literal_eval"]
LAND = ["test_consumer_keys_resolve_through_the_registry_legacy_rows"]

if __name__ == "__main__":
    a = run(HOME, "test_demque_bbg_ledger_upload.py", "UPLOAD-OK", "FIX-BAD", UPLOAD)
    b = run(HOME, "test_demque_land.py", "LAND-OK", "FIX-BAD", LAND)
    if a == 0 and b == 0:
        print("FIX-OK")
        sys.exit(0)
    sys.exit(1)
