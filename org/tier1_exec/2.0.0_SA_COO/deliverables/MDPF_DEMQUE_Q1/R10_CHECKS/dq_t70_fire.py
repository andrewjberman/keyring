"""MDPF_DEMQUE DQ-t-70 criterion AC2 (site Z; date-gated to the 2026-10-24 fire of the standing drawer task, 14:00Z): read the real actuals ledger.
Amended 2026-10-18 ~14:2xZ by the issuer: DATE-GATE MOVED from the 2026-10-17 fire to the 2026-10-24 fire (14:00Z). The 10-17 fire read FIRE-BAD (stopped on an empty window; Z-S6) and the 10-18 fire drew 0 history cells (the history probe of /cusip/662858FV6 returned 0 rows, so every history request was refused; Z-S8): the property this arm grades, a surface-budget fire drawing past the history ceiling, was stopped upstream both times. Both FIRE-BAD reads stay recorded on the order. Earlier amendment 2026-10-17 ~04:4xZ by the issuer: every ETFS_RIVALS-C1 request carries a draw_hold (CTO msg 7279), so surface C has no open request; the fire is graded on
the surfaces that do draw. FIRE-OK when, over the rows dated 2026-10-17 on channel history: (1) the rows of surface-tagged jobs (a row's own "surface" member,
else the surface of the request file of the job) sum to MORE than 5858; (2) each surface's cells are at most its budget in bbg_allowance.json budgets.surfaces;
(3) all rows of the day (every job, history and reference) sum to at most budgets.daily_total; (4) no row of the day carries a stop_reason naming a vendor limit
(the words limit or warning, any case). Else FIRE-BAD <why>. At the base (no fire yet): FIRE-BAD no surface-tagged cells drawn on 2026-10-24.
Run from the repository root.
"""
from __future__ import annotations

import json
import os
import sys

MISSION = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE")
LEDGER = os.path.join(MISSION, "ledger", "BBG_ACTUALS.jsonl")
ALLOW = os.path.join("data", "mdpf", "scripts", "demque", "bbg_allowance.json")
DAY = "2026-10-24"


def surface_of(row: dict):
    if row.get("surface"):
        return row["surface"]
    path = os.path.join(MISSION, "requests", "%s.json" % row.get("job"))
    try:
        return json.load(open(path, encoding="utf-8")).get("surface")
    except (OSError, ValueError):
        return None


def main() -> int:
    rows = [json.loads(ln) for ln in open(LEDGER, encoding="utf-8", errors="replace").read().splitlines() if ln.strip()]
    day = [r for r in rows if r.get("date") == DAY]
    budgets = json.load(open(ALLOW, encoding="utf-8"))["budgets"]
    per = {}
    for r in day:
        s = surface_of(r) if r.get("channel") == "history" else None
        if s in budgets["surfaces"]:
            per[s] = per.get(s, 0) + int(r.get("cells_drawn") or 0)
    tagged = sum(per.values())
    total = sum(int(r.get("cells_drawn") or 0) for r in day)
    if tagged <= 0:
        print("FIRE-BAD no surface-tagged cells drawn on %s (%d rows that day, %d cells in all)" % (DAY, len(day), total))
        return 1
    print("surface cells on %s: %s; all jobs %d cells in %d rows" % (DAY, json.dumps(per, sort_keys=True), total, len(day)))
    if tagged <= 5858:
        print("FIRE-BAD surface-tagged cells %d are not past the 5858 history ceiling" % tagged)
        return 1
    over = {s: n for s, n in per.items() if n > budgets["surfaces"][s]["value"]}
    if over:
        print("FIRE-BAD over budget: %s" % json.dumps(over, sort_keys=True))
        return 1
    if total > budgets["daily_total"]["value"]:
        print("FIRE-BAD the day's cells %d exceed the %d daily total" % (total, budgets["daily_total"]["value"]))
        return 1
    hit = [r.get("job") for r in day if any(w in str(r.get("stop_reason") or "").lower() for w in ("limit", "warning"))]
    if hit:
        print("FIRE-BAD a vendor limit stop on %s" % ",".join(sorted(set(map(str, hit)))))
        return 1
    print("FIRE-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
