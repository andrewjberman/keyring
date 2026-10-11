# DSGN_IRPTV1: CVO adjudication, rounds 14 and 15

<sweep_watermark>2026-10-11T08:32Z</sweep_watermark>

L8 compile and L9 read by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T08:32:48Z. Inputs: msg 4490 (round 15 drained @6d3bb93153; round 14 table @a5590e4734).
**L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md`, row D2-S8): FWD-1 is NOT MET on the rendered walk; hop 7's PARTIAL stands; the 43 failing ids are tabled and 2
retirements are not yet ruled. 2 rows dismissed below. 2 rows are held to graduate in `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUNDS_14_15_HELD_20261011.md` until round 14's orders are terminal.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S72",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:32:48Z",
    "one_line": "Rounds 14-15: dismissed, D2-W51-S1 (the order's premise was wrong: the page does bind the reporting reads to the picked client's firm; the refusal is the function's one-firm map, measured live by this seat, and the CTO ruled it IRPT_DASHBD's unbuilt FWD-11) and this seat's read row D2-S8. Held to graduate: D2-S7 (the walk breaks at Performance) and D2-W50-S1 (three failing ids outside the repair cell).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W51-S1",
      "DSGN_IRPTV1-D2-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 15 is terminal; round 14 is open (three orders ACTIVE), so the slug waits. S7 and W21-S2 stay ARMED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W51-S1, D2-S8",
        "msg 4490 (round 15 drained @6d3bb93153; round 14 table @a5590e4734)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/FIRM_BINDING_PLACED.json",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md",
        "this seat's live read 2026-10-11T08:32:48Z: get-function-configuration irpt-49f-reporting-read-lambda, IRPT_DIRECTORY_BUCKET_MAP holds 1 key, 49financial -- the record's inferred live state, now measured"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A premise corrected by its own worker and ruled by the CTO, and a read row."
  }
]
```
