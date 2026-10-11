# IRPT_ANLREQ: CVO adjudication, round 3 (workstream Y)

<sweep_watermark>2026-10-11T09:35Z</sweep_watermark>

Round 3 L8 compile and L9 read by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:35:56Z. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_20261011.md @b8ed5db8be (msg 4564), corrected by msg 4571 (row D2-S36 @12dc42e1c6)`. No judgment criterion.
**Read** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_3_Y_L9_READ_20261011.md`): the issuer's correction holds -- a build from the source map carries no retained_ref; nothing built this round is live.
11 rows dismissed below. 8 rows are held to graduate in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_REMEDIATION_ROUND_3_HELD_20261011.md` until the project's orders read terminal.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S4",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:35:56Z",
    "one_line": "Round 3 (Y) rows dismissed: D2-S31 with D2-W54-S1 (the generate suite's 34 failures were a live table read, not test order; the suite reads 497 passed in two full runs at the drain), D2-W54-S2 and D2-W52-S1 (helpers and fixtures outside an order's grant, repaired at the drain; ops tests read 306 passed), D2-W52-S2 (retained_ref is optional in the schema because the stored report cannot carry it; a recorded choice), D2-W51-S1, S2, S3 and S5 (order-text and mount-point notes of the firm-choice cell, closed by its amendments), D2-W51-S4 (a state no caller can reach was not captured), and this seat's read row D2-S37. Eight rows are held to graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S31",
      "IRPT_ANLREQ-D2-W54-S1",
      "IRPT_ANLREQ-D2-W54-S2",
      "IRPT_ANLREQ-D2-W52-S1",
      "IRPT_ANLREQ-D2-W52-S2",
      "IRPT_ANLREQ-D2-W51-S1",
      "IRPT_ANLREQ-D2-W51-S2",
      "IRPT_ANLREQ-D2-W51-S3",
      "IRPT_ANLREQ-D2-W51-S4",
      "IRPT_ANLREQ-D2-W51-S5",
      "IRPT_ANLREQ-D2-S37"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The drain reads are the issuer's; this seat did not re-run the suites. to-check reads TO-AR-y-33 ACTIVE, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S31, D2-W54-S1, D2-W54-S2, D2-W52-S1, D2-W52-S2, D2-W51-S1, D2-W51-S2, D2-W51-S3, D2-W51-S4, D2-W51-S5, D2-S37",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_20261011.md @b8ed5db8be (msg 4564), corrected by msg 4571 (row D2-S36 @12dc42e1c6)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_3_Y_L9_READ_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A cause found and a suite re-read at the drain, a repaired helper or fixture, a recorded choice, an order-text note, and a read row."
  }
]
```
