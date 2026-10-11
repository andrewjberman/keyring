# DSGN_IRPTV1: CVO adjudication, round 16

<sweep_watermark>2026-10-11T10:08Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T10:08:26Z. Input: msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json). 3 rows dismissed below.
14 rows graduate OPEN in `remediations/REMEDIATION_v8.md`.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S74",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:08:26Z",
    "one_line": "Round 16: dismissed, D2-W52-S1 (a second arm of one test failed behind the first and was repaired in the same order), D2-W52-S4 (two temporary mutants touched a file outside the grant and were reverted; none committed, the worker's statement) and this seat's read row D2-S12. Fourteen rows graduate with the slug.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W52-S1",
      "DSGN_IRPTV1-D2-W52-S4",
      "DSGN_IRPTV1-D2-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No DSGN_IRPTV1 order is open. S7 and W21-S2 stay ARMED from earlier files.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W52-S1, D2-W52-S4, D2-S12",
        "msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A repair made in its order, a reverted test aid, and a read row."
  }
]
```
