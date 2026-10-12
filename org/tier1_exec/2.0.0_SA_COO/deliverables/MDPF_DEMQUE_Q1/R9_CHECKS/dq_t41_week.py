"""MDPF_DEMQUE round 9, DQ-t-41 criterion AC2 (REAL served store, S3 read only, nothing written): `extend_frontier.py --plan-week --from
2026-10-12 --days 7 --assume-landed IRPT_BCKEND-AS-TRADED-CLOSES-878` prints ONE JSON line {"days": [{"date", "daily", "rolling", "requests"}...],
"max_requests", "max_lag_trading_days", "rolling_names", "assumed_landed"} for the next 7 trading days with the 782 new IRPT names treated as
landed (planning only; the line says so). Required: 7 days; every day `requests` <= 400; `daily` >= 141 each day; rolling_names == 782 (the 878 minus
the 96 already stored); every rolling name appears in at least one day's slice within any 5 consecutive trading days (max_lag_trading_days <= 5);
max_requests >= 250 (the load is real). TIER-REAL-OK; else TIER-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "extend_frontier.py")


def _bad(why):
    print("TIER-REAL-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--plan-week", "--from", "2026-10-12", "--days", "7", "--assume-landed",
                        "IRPT_BCKEND-AS-TRADED-CLOSES-878"], capture_output=True, text=True, timeout=115, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(lines[-1])
    days = d.get("days") or []
    print("days=%d max_requests=%s max_lag=%s rolling_names=%s assumed=%s" % (
        len(days), d.get("max_requests"), d.get("max_lag_trading_days"), d.get("rolling_names"), d.get("assumed_landed")))
    for x in days:
        print("  %s daily=%s rolling=%s requests=%s" % (x.get("date"), x.get("daily"), x.get("rolling"), x.get("requests")))
    arms = {
        "seven_days": len(days) == 7,
        "under_cap": bool(days) and all(isinstance(x.get("requests"), int) and x["requests"] <= 400 for x in days),
        "daily_floor": bool(days) and all(isinstance(x.get("daily"), int) and x["daily"] >= 141 for x in days),
        "rolling_782": d.get("rolling_names") == 782,
        "lag_within_5": isinstance(d.get("max_lag_trading_days"), int) and d["max_lag_trading_days"] <= 5,
        "load_real": isinstance(d.get("max_requests"), int) and d["max_requests"] >= 250,
        "says_assumed": bool(d.get("assumed_landed")),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("TIER-REAL-OK 7 trading days, max %d requests a day, every rolling name within %d trading days" % (d["max_requests"], d["max_lag_trading_days"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
