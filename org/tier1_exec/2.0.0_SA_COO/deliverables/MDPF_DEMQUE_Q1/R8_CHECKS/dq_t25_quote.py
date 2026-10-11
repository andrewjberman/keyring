"""MDPF_DEMQUE round 8, DQ-t-25 criterion AC2: the tier rule on REAL requests, files and the trading calendar only (no network).
(a) the 15,720-cell tier-4 TR request with BOTH history claims `measured` quoted on Fri 2026-10-09 still finishes 2026-10-17 over
non-trading days with allowance_today 0; (b) the tier-1 SHT8 history request quoted on Mon 2026-10-12 reads allowance_today > 0 and
finishes 2026-10-12; (c) the tier-4 request with the history ceiling claim `held` quotes finish_date null with a gap naming the
ceiling "not measured", and the same tier-4 request on trading Monday 2026-10-12 (both claims measured) reads allowance_today 0.
TQQ-OK; else TQQ-BAD <which arm>.
"""
from __future__ import annotations

import copy
import json
import os
import sys

HOME = os.path.join("data", "mdpf", "scripts", "demque")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")
sys.path.insert(0, ".")
sys.path.insert(0, HOME)


def _load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    try:
        import bbg_quote
    except Exception as e:  # a missing module reads BAD, never an error
        print("TQQ-BAD import bbg_quote: %s" % e)
        return 1
    base = _load(os.path.join(HOME, "bbg_allowance.json"))
    both = copy.deepcopy(base)
    both["history"]["reserve"]["claim"] = "measured"
    held = copy.deepcopy(both)
    held["history"]["ceiling"]["claim"] = "held"
    tr = _load(os.path.join(REQ, "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json"))
    sh = _load(os.path.join(REQ, "MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009.json"))
    try:
        a = bbg_quote.quote(tr, both, 0, "2026-10-09")
        b = bbg_quote.quote(sh, base, 0, "2026-10-12")
        c1 = bbg_quote.quote(tr, held, 0, "2026-10-09")
        c2 = bbg_quote.quote(tr, both, 0, "2026-10-12")
    except Exception as e:
        print("TQQ-BAD quote raised %s: %s" % (type(e).__name__, e))
        return 1
    print("a: tier=%s finish=%s today=%s" % (tr.get("tier"), a.get("finish_date"), a.get("allowance_today")))
    print("b: tier=%s finish=%s today=%s" % (sh.get("tier"), b.get("finish_date"), b.get("allowance_today")))
    print("c1: finish=%s gap=%s" % (c1.get("finish_date"), c1.get("allowance_gap")))
    print("c2: finish=%s today=%s" % (c2.get("finish_date"), c2.get("allowance_today")))
    arms = {
        "a": a.get("finish_date") == "2026-10-17" and a.get("allowance_today") == 0,
        "b": isinstance(b.get("allowance_today"), int) and b["allowance_today"] > 0 and b.get("finish_date") == "2026-10-12",
        "c1": c1.get("finish_date") is None and "not measured" in str(c1.get("allowance_gap")),
        "c2": c2.get("allowance_today") == 0,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        print("TQQ-BAD arms=%s" % ",".join(bad))
        return 1
    print("TQQ-OK tier-4 walks non-trading days (claims measured), tier-1 reads reserve on Monday, not-measured ceiling is null with reason")
    return 0


if __name__ == "__main__":
    sys.exit(main())
