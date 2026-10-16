"""MDPF_DEMQUE round 9, DQ-t-72 criterion AC2 (local, no network, no S3, a temp state file): a Yahoo symbol that returned EMPTY within the last 7 days is not requested again and costs no budget.
Builds a Pacer on a temp state with: A = FAILED_EMPTY attempted now, B = FAILED_EMPTY attempted 8 days ago, C = OK, then yahoo_pull.run over [A, B, C, D] with a stub fetch that counts calls.
COOL-OK when: the stub is called for exactly B and D (A is cooling, C is done), the pacer count rose by exactly 2, yahoo_pull.EMPTY_COOLDOWN_DAYS == 7.
Else COOL-BAD <why>."""
from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone

HERE = os.path.join("data", "mdpf", "scripts", "demque")
sys.path.insert(0, HERE)
sys.path.insert(0, os.getcwd())


def main() -> int:
    import pandas as pd
    import yahoo_pull as yp

    if getattr(yp, "EMPTY_COOLDOWN_DAYS", None) != 7:
        print("COOL-BAD yahoo_pull.EMPTY_COOLDOWN_DAYS is %r, not 7" % (getattr(yp, "EMPTY_COOLDOWN_DAYS", None),))
        return 1
    now = datetime.now(timezone.utc)
    stamp = lambda dt: dt.strftime("%Y-%m-%dT%H:%M:%SZ")  # noqa: E731
    state = {"day": now.date().isoformat(), "count": 10, "pushback": False, "factor": 1.0, "last_request_ts": None,
             "symbols": {
                 "AAA": {"last_attempt": stamp(now - timedelta(hours=1)), "outcome": "FAILED_EMPTY", "http_status": None, "rows": 0},
                 "BBB": {"last_attempt": stamp(now - timedelta(days=8)), "outcome": "FAILED_EMPTY", "http_status": None, "rows": 0},
                 "CCC": {"last_attempt": stamp(now - timedelta(days=1)), "outcome": "OK", "http_status": 200, "rows": 5}}}
    path = os.path.join(tempfile.mkdtemp(prefix="dq_t72_"), "pacer.json")
    json.dump(state, open(path, "w", encoding="utf-8"))
    pacer = yp.Pacer(path, min_gap=0.0, max_gap=0.0, sleep=lambda s: None, today=now.date().isoformat())
    called = []

    def fetch(sym):
        called.append(sym)
        return pd.DataFrame()

    yp.run(["AAA", "BBB", "CCC", "DDD"], pacer, fetch)
    if sorted(called) != ["BBB", "DDD"]:
        print("COOL-BAD the stub fetch was called for %s, expected ['BBB', 'DDD']" % sorted(called))
        return 1
    if pacer.state["count"] != 12:
        print("COOL-BAD the pacer count is %r, expected 12 (10 plus the two requests made)" % pacer.state["count"])
        return 1
    print("COOL-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
