#!/usr/bin/env python3
"""A2 BACKFILL_CAP 50 to 62: the pull's existing offline history-plan tests still pass (a bound check; it PASSES at the base).

Run from the worktree root. Runs integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py under pytest with a 100 s bound.
Prints A2-TESTS-OK passed=<n> when rc 0 and no failures or errors; otherwise A2-TESTS-BAD <tail>. Plain ASCII.
"""
import re
import subprocess
import sys

TEST = "integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py"


def main():
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", TEST],
                           capture_output=True, text=True, timeout=100)
    except subprocess.TimeoutExpired:
        print("A2-TESTS-BAD timeout 100s")
        return 1
    tail = (r.stdout.strip().splitlines() or [""])[-1]
    m = re.search(r"(\d+) passed", tail)
    if r.returncode == 0 and m and "failed" not in tail and "error" not in tail:
        print("A2-TESTS-OK passed=%s" % m.group(1))
        return 0
    print("A2-TESTS-BAD rc=%d tail=%s" % (r.returncode, tail))
    return 1


if __name__ == "__main__":
    sys.exit(main())
