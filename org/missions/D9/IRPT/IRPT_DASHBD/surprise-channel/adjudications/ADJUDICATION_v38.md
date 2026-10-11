# IRPT_DASHBD: CVO adjudication, round 65 (workstream B)

<sweep_watermark>2026-10-11T09:10Z</sweep_watermark>

Round 65 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:10:50Z. Input: msg 4541 (round 65 drained @1d9c2fb822); record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~96/REPORTING_READ_PER_FIRM.json`. No judgment criterion.
3 rows dismissed below. D2-W96-S2 and D2-W96-S3 are held to graduate in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_REMEDIATION_ROUNDS_55_56_HELD_20261010.md`.
The row to read: D2-W96-S2 -- the reporting publisher refuses a null income value, and the minted Cottonwood table has none.

```json
[
  {
    "id": "IRPT_DASHBD-C-S49",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:10:50Z",
    "one_line": "Round 65 rows dismissed: D2-W96-S1 (ARMED: a 49 Financial hop3 file would have met DB-b-86's un-block condition; disarmed by AMENDMENT 4 @4b9db08e1a, which asks a record naming the Cottonwood table, read by this seat), D2-W96-S4 (the order named a path one folder off), and this seat's read row D2-S10. D2-W96-S2 and D2-W96-S3 are held to graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W96-S1",
      "IRPT_DASHBD-D2-W96-S4",
      "IRPT_DASHBD-D2-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 65 is terminal. TO-DB-b-86 stays ACTIVE and blocked, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W96-S1, D2-W96-S4, D2-S10",
        "msg 4541 (round 65 drained @1d9c2fb822)",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~96/REPORTING_READ_PER_FIRM.json",
        "this seat's read of TO-DB-b-86 AMENDMENT 4 (lines 103-115, @4b9db08e1a): condition 3 now asks a hop3 output whose record states it read irpt/cottonwood/gold/account_return_daily/ for Cottonwood masters; a 49 Financial file does not un-block the order"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hazard disarmed by an amendment this seat read, an order-text slip, and a read row."
  }
]
```
