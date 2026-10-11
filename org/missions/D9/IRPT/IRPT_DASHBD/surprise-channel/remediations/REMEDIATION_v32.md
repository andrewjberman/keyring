# IRPT_DASHBD: remediations, round 75 (workstream B)

<sweep_watermark>2026-10-11T20:02Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:02:47Z. Input: msg 5720 (IRPT_DASHBD round 75 fully drained @fc42bbcab0; orders DB-b-141 and DB-b-142).
Graduated, round label v76: 1 row, OPEN, INERT.

**For the CTO's analysis:**
1. **The duplication reaches a quoted figure, not a served one.** One tracked reader of the ledger copy, a project script, serves nothing.
   Two untracked scripts also sum without the id, so '59 of 90 tie' may include repetition: not established (row D2-W114-S1).
2. **Row D2-W113-S2 stays OPEN:** the search covered 71,502 files of this repository; portal, opal_ai and mcportal were not searched, and
   the readers of the ORIGINAL store were not listed. Whether that census is this project's cell is the issuer's ask to you.
3. **Row D2-W113-S3 stays OPEN on one thing:** the method's rule is read (this seat confirmed it in the code: an administrative expense
   stays inside the return), but the shared code table's class for that one row was not read by anyone.
4. The tie-out reads 185 classed, 51 contested, 8 unclassed; not closed.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W114-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-141: the tracked tree holds one reader of the silver_legacy transactions copy (a project script, not keyed on the transaction id, nothing served); the readers whose figures the records quote live outside the tree, and one record figure rests on an unkeyed sum.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W114-S1",
   "msg 5720 (IRPT_DASHBD round 75 fully drained @fc42bbcab0; orders DB-b-141 and DB-b-142)"
  ],
  "remedy": "The record figure that rests on an unkeyed sum (59 of 90 in UNCLASSED_90.json) is re-derived with each transaction id counted once, or withdrawn; the two untracked scripts are tracked or their figures are not quoted.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v76",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v76"
  },
  "closed": false
 }
]
```
