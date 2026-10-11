# IRPT_ANLREQ: CVO adjudication, rounds 5 to 7 (workstream Y)

<sweep_watermark>2026-10-11T14:21Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T14:21:25Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND7_Y_L8_COMPILE_20261011.md @24ffff9b45 (msg 5106)`. No judgment criterion.
**Read** (row D2-S50): nothing from rounds 3 to 7 is live; the ordering hazard is confirmed in source and filed ARMED (row D2-S51).
4 rows dismissed below. Row D2-S48 of REMEDIATION_v4 closes in place. 3 rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_REMEDIATION_ROUNDS_5_7_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S8",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T14:21:25Z",
    "one_line": "Rounds 5 to 7 (Y) rows dismissed: D2-S49 (the CTO's answer to row D2-S48: 4 history-route requests in the window, one script, no browser; D2-S48 closes in place), D2-W51-S8 (two clauses of an order could not both hold; one shared helper, accepted by the CTO), D2-W52-S6 (a new public reason needed one line in another lane's file; ruled by CTO msg 5045 with that lane's yes), and this seat's read row D2-S50. Held: D2-W52-S5, D2-W52-S7 (ARMED), D2-S51 (ARMED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S49",
      "IRPT_ANLREQ-D2-W51-S8",
      "IRPT_ANLREQ-D2-W52-S6",
      "IRPT_ANLREQ-D2-S50"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 7 reads MAY-CLOSE. One IRPT_ANLREQ order is pending in workstream G (to-check), so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S49, D2-W51-S8, D2-W52-S6, D2-S50",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND7_Y_L8_COMPILE_20261011.md @24ffff9b45 (msg 5106)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An owner's answer, an order-text conflict resolved, a ruled grant, and a read row."
  }
]
```
