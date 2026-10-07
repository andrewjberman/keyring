"""MDPF_SECHIST round 1, criterion SH1-t1-AC2: the history plan, run read-only against the REAL S3 plane.

Imports the pull module WITHOUT running main() (main() pulls Bloomberg and writes S3), and calls its
read-only entry `plan_only()`, which derives the universe from silver/holdings and the coverage from
the stored history, and returns the plan. It must write nothing and need no blpapi.

The seam: CSCO and BX (in the Opal ETF universe since about 2026-09-18, no backfill) are the live
negative case, so a correct plan names both, each starting at least 365 days before the as-of.
Last line: SEAM-OK ... or SEAM-BAD <reason>.
"""
from __future__ import annotations

import datetime as dt
import importlib.util
import os
import sys

MOD = os.path.join("integrations", "bloomberg", "pipeline", "etf_daily_pull.py")
MUST = ["CSCO", "BX"]


def main() -> int:
    spec = importlib.util.spec_from_file_location("etf_daily_pull", MOD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn = getattr(mod, "plan_only", None)
    if fn is None:
        print("SEAM-BAD no plan_only() in " + MOD)
        return 1
    plan = fn()
    asof = dt.date.fromisoformat(str(plan["asof"])[:10])
    windows = plan["backfill"]
    print("asof=" + asof.isoformat() + " universe=" + str(plan["universe_count"])
          + " needing=" + str(plan["needing_count"]) + " planned=" + str(len(windows))
          + " capped=" + str(len(plan.get("capped", []))))
    bad = []
    for t in MUST:
        w = windows.get(t)
        if w is None:
            bad.append(t + ":absent")
            continue
        start = dt.date.fromisoformat(str(w["start"])[:10])
        if (asof - start).days < 365:
            bad.append(t + ":start=" + start.isoformat())
    for t, w in windows.items():
        start = dt.date.fromisoformat(str(w["start"])[:10])
        if (asof - start).days > 400:
            bad.append(t + ":over-deep=" + start.isoformat())
    if plan.get("written"):
        bad.append("wrote=" + str(plan["written"]))
    if bad:
        print("SEAM-BAD " + " ".join(bad))
        return 1
    print("SEAM-OK planned=" + str(len(windows)) + " " + " ".join(
        t + "@" + str(windows[t]["start"]) for t in MUST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
