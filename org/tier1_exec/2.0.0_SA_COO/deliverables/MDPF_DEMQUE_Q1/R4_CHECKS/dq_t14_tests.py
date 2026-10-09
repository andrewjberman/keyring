"""MDPF_DEMQUE round 4, DQ-t-14 (site-Z demand-ledger uploader; site Z ruling 32309, CTO msg 1536 item 6) criterion AC1: by named tests in
data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py (fixture jsonl files, S3 stubbed; runnable on any box). UPL-OK when every named
test PASSED; else UPL-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_reads_record_lines_and_converts_rows_to_cells_per_mode', 'test_unknown_mode_is_written_with_claim_absent_not_defaulted',
         'test_target_is_the_builder_address_for_the_utc_day', 'test_dry_run_writes_nothing', 'test_rerun_of_a_day_is_idempotent']

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_bbg_ledger_upload.py", "UPL-OK", "UPL-BAD", TESTS))
