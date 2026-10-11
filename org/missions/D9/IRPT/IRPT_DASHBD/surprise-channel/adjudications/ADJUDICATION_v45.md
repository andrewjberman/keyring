# IRPT_DASHBD: CVO adjudication, rounds 71 and 72

<sweep_watermark>2026-10-11T17:57Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:57:20Z. Input: msg 5485 (IRPT_DASHBD rounds 71 and 72 drained; DSGN_IRPTV1 round 23, two of three cells drained, portal DEV ca23f110). No judgment criterion. No served write.
3 rows dismissed below. 1 row is ready to graduate and is HELD in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_REMEDIATION_ROUNDS_71_72_HELD_20261011.md` until TO-DB-b-139 is terminal.

```json
[
  {
    "id": "IRPT_DASHBD-C-S56",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T17:57:20Z",
    "one_line": "Rounds 71 and 72: dismissed, D2-W110-S1 (an order's bounds and its own item 2 could not both hold as worded; a wording note), D2-W109-S1 (the reader census missed an eleventh reader and three line numbers; the issuer read the eleventh and it passes no manifest on), and this seat's read row D2-S17. Held to graduate: D2-W111-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W110-S1",
      "IRPT_DASHBD-D2-W109-S1",
      "IRPT_DASHBD-D2-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Rounds 71 and 72 read MAY-CLOSE (the issuer's check).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W110-S1, D2-W109-S1, D2-S17",
        "msg 5485 (IRPT_DASHBD rounds 71 and 72 drained; DSGN_IRPTV1 round 23, two of three cells drained, portal DEV ca23f110)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An order-text note, a census gap the issuer closed by reading, and a read row."
  }
]
```
