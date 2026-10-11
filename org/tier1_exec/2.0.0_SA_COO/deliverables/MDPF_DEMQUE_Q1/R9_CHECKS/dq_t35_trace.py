"""MDPF_DEMQUE round 9, DQ-t-35 criterion AC1: the structure of the valuation trace file
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~27/VALUATION_TRACE.json (a read-only artifact; the worker writes it).
Required: `denominator` {"fthsx_accounts": 4, "pforx_accounts": 11, "total": 15}; `positions` a list of exactly 15 rows, each with account,
cusip, symbol, price_file (an S3 key under price_history, or null), value_artifact (a key or path, or null), route (a portal route, or
null), firm (or null) and `read_by_a_page` (bool); a row with read_by_a_page false must carry `evidence` (a non-empty string naming what
was read); `candidates` for each of the three CUSIPs 14064D865, 693390882, 77958B402, each candidate with resolver, ticker and
agreement_pct (a number), or an entry {"cusip", "candidates": [], "reason": "..."}. TRACE-OK; else TRACE-BAD <why>.
"""
from __future__ import annotations

import json
import os
import sys

PATH = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "0.9.0_WK_MDPF_DEMQUE~27", "VALUATION_TRACE.json")
CUSIPS = ("14064D865", "693390882", "77958B402")


def _bad(why):
    print("TRACE-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(PATH):
        return _bad("no file " + PATH)
    try:
        d = json.load(open(PATH, encoding="utf-8"))
    except ValueError as e:
        return _bad("not JSON: %s" % e)
    den = d.get("denominator") or {}
    if (den.get("fthsx_accounts"), den.get("pforx_accounts"), den.get("total")) != (4, 11, 15):
        return _bad("denominator %r is not 4 / 11 / 15" % den)
    pos = d.get("positions")
    if not isinstance(pos, list) or len(pos) != 15:
        return _bad("positions has %s rows, not 15" % (len(pos) if isinstance(pos, list) else None))
    for i, r in enumerate(pos):
        miss = [k for k in ("account", "cusip", "symbol", "price_file", "value_artifact", "route", "firm", "read_by_a_page") if k not in r]
        if miss:
            return _bad("row %d lacks %s" % (i, miss))
        if not isinstance(r["read_by_a_page"], bool):
            return _bad("row %d read_by_a_page is not a bool" % i)
        if r["read_by_a_page"] and not (r["route"] and r["firm"] and r["value_artifact"]):
            return _bad("row %d is read by a page but names no route, firm and artifact" % i)
        if not r["read_by_a_page"] and not str(r.get("evidence") or "").strip():
            return _bad("row %d is not read by a page and carries no evidence" % i)
    cand = {c.get("cusip"): c for c in d.get("candidates", []) if isinstance(c, dict)}
    for cu in CUSIPS:
        c = cand.get(cu)
        if c is None:
            return _bad("no candidates entry for " + cu)
        lst = c.get("candidates")
        if not isinstance(lst, list):
            return _bad("%s candidates is not a list" % cu)
        if not lst and not str(c.get("reason") or "").strip():
            return _bad("%s has no candidate and no reason" % cu)
        for x in lst:
            if not (x.get("resolver") and x.get("ticker") and isinstance(x.get("agreement_pct"), (int, float))):
                return _bad("%s candidate %r lacks resolver, ticker or a numeric agreement_pct" % (cu, x))
    read = sum(1 for r in pos if r["read_by_a_page"])
    print("TRACE-OK 15 positions (4 FTHSX, 11 PFORX), %d read by a page, candidates for 3 CUSIPs" % read)
    return 0


if __name__ == "__main__":
    sys.exit(main())
