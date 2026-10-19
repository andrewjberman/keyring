"""MDPF_DEMQUE DQ-t-78 criterion AC2 (site Z; date-gated to the first scheduled sweep after the GO): read the newest sweep receipt.
FIRE-OK when the newest receipt.<day>.sweep.json in the standing drawer's output folder carries pass "sweep", drew more than 0 cells, drew no more
than its daily_total_left at the start, and carries no stop naming a vendor limit, refusal or PRODUCTION_SPEND_UNREAD. Else FIRE-BAD <why>.
At the base (no sweep has run): FIRE-BAD no sweep receipt. Run from the repository root at site Z.
"""
from __future__ import annotations

import glob
import json
import os
import sys

OUT = os.path.join("org", "tier2_senior", "0.7.0_AE_CloudOps", "deliverables", "MDPF_DEMQUE_ZQ_STANDING")


def bad(why: str) -> int:
    print("FIRE-BAD " + why)
    return 1


def main() -> int:
    paths = sorted(glob.glob(os.path.join(OUT, "receipt.*.sweep.json")))
    if not paths:
        return bad("no sweep receipt in %s" % OUT)
    r = json.load(open(paths[-1], encoding="utf-8"))
    cells, left = r.get("cells_drawn"), r.get("daily_total_left")
    stop = str(r.get("stop_reason") or "")
    print("newest %s: cells_drawn=%r daily_total_left=%r stop=%r" % (os.path.basename(paths[-1]), cells, left, stop))
    if r.get("pass") != "sweep":
        return bad("receipt does not carry pass sweep")
    if type(cells) is not int or cells <= 0:
        return bad("the sweep drew no cells")
    if type(left) is not int or cells > left:
        return bad("cells_drawn %r exceeds daily_total_left %r" % (cells, left))
    if any(w in stop.lower() for w in ("limit", "refus", "entitle", "production_spend_unread")):
        return bad("stop %r" % stop)
    print("FIRE-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
