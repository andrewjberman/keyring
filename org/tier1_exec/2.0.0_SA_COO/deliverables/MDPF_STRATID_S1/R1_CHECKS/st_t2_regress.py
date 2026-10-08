"""MDPF_STRATID round 1, ST-t-2 criterion AC2: the TaxSMA Cottonwood-into-Global fold tests (registry basis readers) still pass. T2-REGRESS-OK when every named test PASSED; else T2-REGRESS-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = []

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/taxsma/test_taxsma_cot_global_fold.py", "T2-REGRESS-OK", "T2-REGRESS-BAD", TESTS))
