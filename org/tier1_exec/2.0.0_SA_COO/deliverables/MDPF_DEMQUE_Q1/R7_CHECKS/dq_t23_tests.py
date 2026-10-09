"""MDPF_DEMQUE round 7, DQ-t-23 (quote_vs_actual --all over every quote shape; CTO round-6 analysis R2) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_qva_all.py (temporary files). QALLT-OK when every named test PASSED; else QALLT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_quote_without_finish_date_reads_unquoted_not_raises', 'test_all_reads_every_quote_file']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_qva_all.py', 'QALLT-OK', 'QALLT-BAD', TESTS))
