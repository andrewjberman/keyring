"""MDPF_DEMQUE round 9, DQ-t-73 criterion AC2 (read-only, no network): the real bbg_allowance.json carries the 2.5M-cell daily budget.
BUDGT-OK when: budgets.daily_total is 2,500,000; surfaces A..E are 350,000 / 1,500,000 / 400,000 / 100,000 / 150,000 and sum to the total;
budgets.e_request_cap is 5,000; every figure carries a claim of held or inferred; unit_weight is inferred; release_rule sends A, C, D and E to B with A
first claim; ramp_steps lists the seven steps; and NOTHING served moved: history.ceiling is 5858 measured, bql.ceiling 2920000 measured.
Else BUDGT-BAD <why>. Run from the worktree root."""
from __future__ import annotations

import json
import os
import sys

PATH = os.path.join("data", "mdpf", "scripts", "demque", "bbg_allowance.json")
WANT = {"A": 350000, "B": 1500000, "C": 400000, "D": 100000, "E": 150000}
STEPS = [11716, 23432, 29290, 100000, 300000, 1000000, 2500000]


def bad(why: str) -> int:
    print("BUDGT-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(PATH):
        return bad("no file " + PATH)
    a = json.load(open(PATH, encoding="utf-8"))
    b = a.get("budgets")
    if not isinstance(b, dict):
        return bad("no budgets block in bbg_allowance.json")
    if (b.get("daily_total") or {}).get("value") != 2500000:
        return bad("budgets.daily_total.value is %r, not 2500000" % ((b.get("daily_total") or {}).get("value"),))
    s = b.get("surfaces") or {}
    got = {k: (s.get(k) or {}).get("value") for k in WANT}
    if got != WANT:
        return bad("surface budgets are %r, not %r" % (got, WANT))
    if sum(got.values()) != 2500000:
        return bad("surface budgets sum to %d, not 2500000" % sum(got.values()))
    if (b.get("e_request_cap") or {}).get("value") != 5000:
        return bad("budgets.e_request_cap.value is %r, not 5000" % ((b.get("e_request_cap") or {}).get("value"),))
    figs = [b["daily_total"], b["e_request_cap"]] + [s[k] for k in WANT]
    for f in figs:
        if f.get("claim") not in ("held", "inferred") or not f.get("basis"):
            return bad("a budget figure lacks a claim of held or inferred, or its basis: %r" % (f,))
    if (b.get("unit_weight") or {}).get("claim") != "inferred":
        return bad("budgets.unit_weight.claim is not inferred")
    r = b.get("release_rule") or {}
    if sorted(r.get("from") or []) != ["A", "C", "D", "E"] or r.get("to") != "B" or r.get("a_first_claim") is not True:
        return bad("release_rule is %r" % (r,))
    if (b.get("ramp_steps") or {}).get("values") != STEPS:
        return bad("ramp_steps.values is %r" % ((b.get("ramp_steps") or {}).get("values"),))
    h = (a.get("history") or {}).get("ceiling") or {}
    if h.get("value") != 5858 or h.get("claim") != "measured":
        return bad("history.ceiling moved: %r" % (h,))
    q = (a.get("bql") or {}).get("ceiling") or {}
    if q.get("value") != 2920000 or q.get("claim") != "measured":
        return bad("bql.ceiling moved: %r" % (q,))
    print("BUDGT-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
