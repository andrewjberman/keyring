"""MDPF_STRATID ST-w-8 criterion AC1: every scope carries unidentified_strategies so the L-1 key-set identity holds (amendment A11).
W28-OK when every named test PASSED; else W28-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ["test_every_scope_carries_unidentified_strategies", "test_keyset_identity_passes_with_cottonwood_block",
         "test_padding_moves_no_figure"]

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/stratid/test_stratid_unidentified_keyset.py", "W28-OK", "W28-BAD", TESTS))
