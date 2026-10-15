# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PM, the ratio-absent split securities named in the served manifest)

<sweep_watermark>2026-10-15T19:51Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:51Z, on msg 8586 (the shared packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md` @f7b4555d40; v129 to v134 grade its six lane rounds). One order, IB-pr-592 (risk LOCAL), complete, merged @f005060a06 (`holdings_performance.py` and a new test `test_split_ratio_absent_named.py`). Re-run here at HEAD: IB225-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PM"`: MAY-CLOSE. Nothing deployed: `irpt-holdings-performance-lambda` still reads CodeSha256 `o9UugRAV...` (LastModified 2026-10-15T06:06:08Z), the same as in v120.

This meets the CTO half's condition 3 of the 49 Financial split pair: the per-day served manifest names each ratio-absent split security by security and day. Held: `D2-W432-S1` (ARMED, `~P2`). The worker's Read of the order returned the RECORD FACE. This is the same dispatch defect as W430-S2 and W431-S1, and W433-S4 and W434-S2 in these rounds, recurring across workers.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S37",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:51:00Z",
  "one_line": "~PM r1. The performance producer's per-day served manifest now names the ratio-absent split securities by security and day (the 49F split pair's CTO condition 3). IB225-1-AC1..AC3 PASS re-run; repository only (live performance Lambda still o9UugRAV, 06:06Z). Dismissed (3): D2-W432-S2, -S3, -S4 (readings). Held: D2-W432-S1 (the RECORD FACE reached the worker, a recurring dispatch defect).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W432-S2",
   "IRPT_BCKEND-D2-W432-S3",
   "IRPT_BCKEND-D2-W432-S4"
  ],
  "spec_asserts": "The CTO half of the 49 Financial split pair, condition 3: the ratio-absent securities are named in the served manifest.",
  "world_is": "Built and tested in the repository; the live producer is unchanged.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:3xZ of the invocations in IB-pr-592: IB225-1-AC1..3 PASS, exit 0; round-close-check ~PM round 1 MAY-CLOSE",
    "git diff --name-only f005060a06^1 f005060a06: holdings_performance.py, tests/test_split_ratio_absent_named.py",
    "aws lambda get-function-configuration irpt-holdings-performance-lambda 2026-10-15T19:4xZ: 2026-10-15T06:06:08Z, o9UugRAV...",
    "investigation rows D2-W432-S1..S4",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md @f7b4555d40 (msg 8586)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings. The recurring RECORD FACE dispatch defect stays held with ~P2."
 }
]
```
