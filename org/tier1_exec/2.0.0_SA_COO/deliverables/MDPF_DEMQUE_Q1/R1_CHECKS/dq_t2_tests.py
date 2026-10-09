"""MDPF_DEMQUE round 1, DQ-t-2 (FWD-1 hop 3, FWD-7) criterion AC1: the Yahoo pull and the shared pacer, by named tests
in `test_demque_yahoo.py` (run from data/mdpf/scripts/demque; the fetch is stubbed, no vendor call). YAHOO-OK when every
named test PASSED; else YAHOO-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run  # noqa: E402

TESTS = [
    "test_as_traded_close_undoes_later_splits",
    "test_empty_answer_is_failure_never_prices",
    "test_refusal_stops_the_day_and_checkpoints",
    "test_resume_skips_symbols_already_done",
    "test_daily_cap_stops_drawing",
    "test_gap_doubles_after_a_pushback_day",
]

if __name__ == "__main__":
    sys.exit(run("test_demque_yahoo.py", "YAHOO-OK", "YAHOO-BAD", TESTS))
