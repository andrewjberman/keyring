"""MDPF_DEMQUE DQ-t-70 criterion AC2 (site Z; date-gated to the 2026-10-17 fire of the standing drawer task, 14:00Z): read the real actuals ledger.
FIRE-OK when, over the rows dated 2026-10-17 on channel history: (1) the rows of surface C (a row's own "surface" member, else the surface of the
request file of the job) sum to MORE than 5858 and at most 400000; (2) all rows of the day (every job, history and reference) sum to at most 2500000;
(3) no row of the day carries a stop_reason naming a vendor limit (the words limit or warning, any case). Else FIRE-BAD <why>.
At the base (no fire yet): FIRE-BAD no surface-C cells drawn on 2026-10-17. Run from the repository root.
"""
from __future__ import annotations

import json
import os
import sys

MISSION = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE")
LEDGER = os.path.join(MISSION, "ledger", "BBG_ACTUALS.jsonl")
DAY = "2026-10-17"


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
    c_cells = sum(int(r.get("cells_drawn") or 0) for r in day if r.get("channel") == "history" and surface_of(r) == "C")
    total = sum(int(r.get("cells_drawn") or 0) for r in day)
    if c_cells <= 0:
        print("FIRE-BAD no surface-C cells drawn on %s (%d rows that day, %d cells in all)" % (DAY, len(day), total))
        return 1
    print("surface C drew %d cells on %s; all jobs %d cells in %d rows" % (c_cells, DAY, total, len(day)))
    if c_cells <= 5858:
        print("FIRE-BAD surface C drew %d, not past the 5858 history ceiling" % c_cells)
        return 1
    if c_cells > 400000:
        print("FIRE-BAD surface C drew %d, over its 400000 budget" % c_cells)
        return 1
    if total > 2500000:
        print("FIRE-BAD the day's cells %d exceed the 2500000 daily total" % total)
        return 1
    hit = [r.get("job") for r in day if any(w in str(r.get("stop_reason") or "").lower() for w in ("limit", "warning"))]
    if hit:
        print("FIRE-BAD a vendor limit stop on %s" % ",".join(sorted(set(map(str, hit)))))
        return 1
    print("FIRE-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
