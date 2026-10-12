"""MDPF_DEMQUE round 9, DQ-t-42 criterion AC2 (REAL served store, S3 read only, nothing written): `extend_frontier.py --lag-report` prints ONE JSON
line {"freshness_basis", "frontier", "indexed", "tiers": {"daily": T, "rolling": T}, "rolling_not_landed"} with T = {"declared_cycle_trading_days",
"names", "within", "over", "max_lag", "over_names": [{"cusip","symbol","valid_to","as_of","lag"}]}. Required: freshness_basis ==
trading-day-frontier; declared cycles daily 1, rolling 5; daily.names + rolling.names == indexed; within + over == names in each tier; len(over_names)
== over; every over name's lag > its tier's declared cycle; indexed >= 141. LAG-REAL-OK; else LAG-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "extend_frontier.py")


def _bad(why):
    print("LAG-REAL-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--lag-report"], capture_output=True, text=True, timeout=115, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(lines[-1])
    t = d.get("tiers") or {}
    daily, rolling = t.get("daily") or {}, t.get("rolling") or {}
    print("basis=%s frontier=%s indexed=%s rolling_not_landed=%s" % (d.get("freshness_basis"), d.get("frontier"), d.get("indexed"), d.get("rolling_not_landed")))
    for k, v in (("daily", daily), ("rolling", rolling)):
        print("  %s: declared=%s names=%s within=%s over=%s max_lag=%s" % (k, v.get("declared_cycle_trading_days"), v.get("names"), v.get("within"),
                                                                       v.get("over"), v.get("max_lag")))
    ints = all(isinstance(x.get(k), int) for x in (daily, rolling) for k in ("names", "within", "over"))
    arms = {
        "basis": d.get("freshness_basis") == "trading-day-frontier",
        "cycles": daily.get("declared_cycle_trading_days") == 1 and rolling.get("declared_cycle_trading_days") == 5,
        "ints": ints,
        "indexed_floor": isinstance(d.get("indexed"), int) and d["indexed"] >= 141,
        "partition": ints and daily["names"] + rolling["names"] == d.get("indexed"),
        "within_over": ints and all(x["within"] + x["over"] == x["names"] for x in (daily, rolling)),
        "over_listed": ints and all(len(x.get("over_names") or []) == x["over"] for x in (daily, rolling)),
        "over_really_over": ints and all(isinstance(n.get("lag"), int) and n["lag"] > x["declared_cycle_trading_days"]
                                         for x in (daily, rolling) for n in (x.get("over_names") or [])),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("LAG-REAL-OK %d names, %d over their tier's declared cycle" % (d["indexed"], daily["over"] + rolling["over"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
