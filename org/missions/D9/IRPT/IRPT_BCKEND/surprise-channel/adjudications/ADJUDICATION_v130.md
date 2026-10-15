# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PN, the Scope feed's daily factor)

<sweep_watermark>2026-10-15T19:51Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:51Z, on msg 8586 (shared packet @f7b4555d40). One order, IB-pr-594 (risk LOCAL), complete, merged @2f24af25ae (`pull_inflection_scope_account_returns.py`, its test, and a new `test_scope_feed_daily_factor.py`). Re-run here at HEAD: IB227-1-AC1..AC3 PASS (exit 0). `round-close-check --round 2 --workstream "~PN"`: MAY-CLOSE.

Nothing deployed: `s3://opal-data-inf/code/manual_api/pull_inflection_scope_account_returns.py` reads 404, and the runner's `code/gold/orion-gold-dispatch.sh` is unchanged (2026-08-30T14:03:13Z). The feed stores the daily factor only, admits `SERIES_ENDED_AT_SOURCE`, chains calendar days, and starts a scheduled window the day after the newest landed day. The worker's rows are readings of order-text limits (the calendar rule applies to the scheduled window only; the cap reads as up to 11 inclusive days; a Monday run pulls the Friday).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S38",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:51:00Z",
  "one_line": "~PN r2. The Scope feed stores the daily factor only, admits SERIES_ENDED_AT_SOURCE, chains calendar days, and schedules from the day after the newest landed day. IB227-1-AC1..AC3 PASS re-run; repository only (feed script 404 on the runner's code paths; catalog unchanged since 2026-08-30). Dismissed (5): D2-W433-S1..S5 (order-text readings, a shadowing note, the RECORD FACE note, all INERT).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W433-S1",
   "IRPT_BCKEND-D2-W433-S2",
   "IRPT_BCKEND-D2-W433-S3",
   "IRPT_BCKEND-D2-W433-S4",
   "IRPT_BCKEND-D2-W433-S5"
  ],
  "spec_asserts": "Signed pair (b) ADDENDUM 2 condition 1: the daily factor only, no return_value, no summary.",
  "world_is": "Built and tested in the repository; nothing on the runner.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:3xZ of the invocations in IB-pr-594: IB227-1-AC1..3 PASS, exit 0; round-close-check ~PN round 2 MAY-CLOSE",
    "aws s3api head-object opal-data-inf code/manual_api/pull_inflection_scope_account_returns.py: 404; code/gold/orion-gold-dispatch.sh: 2026-08-30T14:03:13Z",
    "investigation rows D2-W433-S1..S5",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PM1_PN2_PN3_PJ4_PJ5_PO8_DRAIN_END_20261015.md @f7b4555d40 (msg 8586)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Order-text readings and inert notes."
 }
]
```
