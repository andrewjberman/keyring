# DSGN_IRPTV1: CVO adjudication, round 11

<sweep_watermark>2026-10-11T06:41Z</sweep_watermark>

Round 11 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:41:10Z. Inputs: msgs 4273 and 4276 (round 11 fully drained @8f6e2524d5).
**L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_11_L9_GRADE_20261011.md`, row D2-S4): IV83-AC2 MET; IV85-AC2 MET; the press test ACCEPTED with a condition; of the 43 suite rulings, 29
REGRESSION accepted and 14 KNOWN-LEGACY not accepted as labelled.
6 rows dismissed below. 6 rows are held to graduate in `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUND_11_HELD_20261011.md` until TO-IV-e-87 is terminal.
Closed in place: S60 (the press test is on DEV as 6f70e36b), and the three determinism rows W23-S1, W29-S10 and W34-S1 (three runs, the
same 43 failing ids). S7 and W21-S2 stay ARMED: the 43 are not yet ruled.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S70",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T06:41:10Z",
    "one_line": "Round 11 rows dismissed: D2-W44-S1 (the portal repo carries no git identity, so safe-commit fails there; the order's stated fallback was used), D2-W46-S2 (the Export finding's record; graded MET, and row W35-S2 stays open with the CTO's contract call), D2-W46-S3 (the order named a page file that does not exist; nothing was wired, so nothing was made outside the grant), D2-W46-S4 (the render script needed two further stubs to reach the review table; they are listed in the record), D2-S2 (a wrong word in a code comment; the page is right), and this seat's grade row D2-S4. Six rows are held to graduate: D2-W43-S1, D2-W43-S2, D2-W43-S3, D2-W46-S1, D2-W46-S5 and D2-S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W44-S1",
      "DSGN_IRPTV1-D2-W46-S2",
      "DSGN_IRPTV1-D2-W46-S3",
      "DSGN_IRPTV1-D2-W46-S4",
      "DSGN_IRPTV1-D2-S2",
      "DSGN_IRPTV1-D2-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 11's five orders are terminal. TO-IV-e-87 is ACTIVE, so the slug waits. Closed in place on the round's records: S60 (REMEDIATION_v6), and the determinism rows W23-S1, W29-S10 and W34-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W44-S1, D2-W46-S2, D2-W46-S3, D2-W46-S4, D2-S2, D2-S4",
        "msgs 4273 and 4276 (round 11 fully drained @8f6e2524d5)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_11_L9_GRADE_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An environment note, a graded record, an order-text error with no act, a script note, a comment word, and a grade row."
  }
]
```
