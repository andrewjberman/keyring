"""MDPF_STRATID workstream 2, ST-w-6 criterion AC1: rebalancer_schemas reads the strategy config from S3 on first use when no
caller set one, once per process, and fails closed (raises) when it is unreadable; an explicit set_strategy_config or cfg= still
wins. W26-OK when every named test PASSED; else W26-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ["test_default_reads_s3_config_on_first_use", "test_s3_config_loaded_once_per_process", "test_unreadable_config_raises",
         "test_set_strategy_config_overrides_the_s3_default", "test_cfg_argument_still_wins"]

if __name__ == "__main__":
    sys.exit(run("data/assets/scripts/silver/tests/test_opal_strategy_wiring.py", "W26-OK", "W26-BAD", TESTS))
