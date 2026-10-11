# DSGN_IRPTV1: CVO adjudication, round 14

<sweep_watermark>2026-10-11T09:19Z</sweep_watermark>

Round 14 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:19:12Z. Input: msg 4551 (round 14 fully drained @b97b6ac14a).
**L9, the re-derived totals** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md` addendum, row D2-S10): two of four tests stay as strict; two are weaker and need the excused set
pinned by name. 2 rows dismissed below. 10 rows are ready to graduate and are HELD in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUNDS_14_15_HELD_20261011.md` until TO-IV-e-94 (batched repairs) is terminal.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S73",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:19:12Z",
    "one_line": "Round 14: dismissed, D2-W49-S2 (the DOM is registered per test file, not by a preload, because the preload was measured to turn six other ids red; a recorded choice) and this seat's read row D2-S10. Ten rows are held to graduate: D2-S7 and D2-W50-S1 (held at rounds 14-15), and D2-W49-S1, S3, S4, S5, S6, S7, S8 and S9.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W49-S2",
      "DSGN_IRPTV1-D2-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 14 is terminal (4 of 4 orders complete). S7 and W21-S2 stay ARMED: 2 of the 10 retirements are not ruled.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W49-S2, D2-S10",
        "msg 4551 (round 14 fully drained @b97b6ac14a)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A recorded, measured choice, and a read row."
  }
]
```
