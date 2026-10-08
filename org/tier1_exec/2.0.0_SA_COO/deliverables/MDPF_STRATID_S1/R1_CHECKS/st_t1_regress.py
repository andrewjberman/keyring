"""MDPF_STRATID round 1, ST-t-1 criterion AC2: the existing Cottonwood SMA/custom slice tests still pass. T1-REGRESS-OK when every named test PASSED; else T1-REGRESS-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = []

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py", "T1-REGRESS-OK", "T1-REGRESS-BAD", TESTS))
