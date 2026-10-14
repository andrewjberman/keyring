"""MDPF_DEMQUE round 9, DQ-t-58 criterion AC3 (the REAL store, S3 and the client transactions READ ONLY, no Yahoo, no write).

`incremental_equal.py --relock-census` (no limit; about 60 seconds for 483 names) runs `daily_draw.combined_relock` on the stored data alone (no appended rows) for EVERY CUSIP in the store and prints ONE JSON line
{"names", "no_trade_rows", "not_applicable", "applicable", "locked", "held_by_combined": [{"symbol","state","trades_inside","trades_before_window"}], "price_mismatch_holds"}.
AMENDED 2026-10-14 (issuer, after tonight's run grew the store from 326 to 483 names): "applicable" = NO trade row is dated before the stored price date range's first day AND at least one trade row is dated inside [first day, last day]. A name with ANY trade before its stored window is "not_applicable":
the stored rows cannot reproduce the observations the original lock used (the issuer's probe: FUEPX, FWMMX, ORCL read PRICE_MISMATCH on the stored rows while their stored locks read 7 of 7, 13 of 13 and 30 of 33 observations passed). Names with trade rows all dated after the stored last day count under no_trade_rows.
Required: names >= 300; no_trade_rows + not_applicable + applicable == names; locked + len(held_by_combined) == applicable; price_mismatch_holds == 0; every held name has trades_inside >= 1 and trades_before_window == 0; not_applicable >= 1.
CENSUS-OK; else CENSUS-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "incremental_equal.py")


def _bad(why):
    print("CENSUS-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--relock-census"], capture_output=True, text=True, timeout=115, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip()))
    d = json.loads(ls[-1])
    held = d.get("held_by_combined") or []
    print("names=%s no_trade_rows=%s not_applicable=%s applicable=%s locked=%s held=%d price_mismatch_holds=%s" % (
        d.get("names"), d.get("no_trade_rows"), d.get("not_applicable"), d.get("applicable"), d.get("locked"), len(held), d.get("price_mismatch_holds")))
    ints = all(isinstance(d.get(k), int) for k in ("names", "no_trade_rows", "not_applicable", "applicable", "locked", "price_mismatch_holds"))
    if not (ints and d["names"] >= 300 and d["no_trade_rows"] + d["not_applicable"] + d["applicable"] == d["names"] and d["locked"] + len(held) == d["applicable"]):
        return _bad("the denominators do not add up")
    if d["price_mismatch_holds"] != 0 or any("PRICE_MISMATCH" in str(h.get("state")) for h in held):
        return _bad("a stored LOCKED name is held for a price mismatch: %s" % held)
    if not all(isinstance(h.get("trades_inside"), int) and h["trades_inside"] >= 1 and h.get("trades_before_window") == 0 for h in held):
        return _bad("a held name has no trade inside the stored window, or has a trade before it: %s" % held)
    if d["not_applicable"] < 1:
        return _bad("no name has trades that predate its window; the census is not exercising the case")
    print("CENSUS-OK %d names: %d applicable (%d locked, %d held), %d trades predate the window and are not held, %d without trade rows; 0 price-mismatch holds" % (
        d["names"], d["applicable"], d["locked"], len(held), d["not_applicable"], d["no_trade_rows"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
