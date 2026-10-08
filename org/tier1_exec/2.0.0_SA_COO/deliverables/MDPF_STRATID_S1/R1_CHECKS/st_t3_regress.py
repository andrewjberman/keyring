"""MDPF_STRATID round 1, ST-t-3 criterion AC3: the TaxSMA served-fold tests still pass. T3-REGRESS-OK when every named test PASSED; else T3-REGRESS-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = []

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/taxsma/test_taxsma_served_fold.py", "T3-REGRESS-OK", "T3-REGRESS-BAD", TESTS))
