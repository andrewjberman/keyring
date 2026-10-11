# IRPT_BCKEND: CVO adjudication, rounds 135 and 136 (workstream ~P)

<sweep_watermark>2026-10-11T16:04Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T16:04:13Z. Input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_135_136_P_DRAIN_END_20261011.md @dc47506c21 (msg 5271)`. No judgment criterion. Nothing applied or served.
**PRD ADDENDUM v0.37: the ratified-text half is REFUSED** (row D2-S92; `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.37_RATIFIED_TEXT_REVIEW_20261011.md @5810d49063`).
3 rows dismissed below. 2 rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S338",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T16:04:13Z",
    "one_line": "Rounds 135 and 136 (~P) rows dismissed: D2-W295-S1 (typing the members by type alone left two portal tests red; the members took v1 references and the tests pass on the regenerated output, by the worker's seam probe), D2-W295-S3 (a criterion failed in the worker's worktree on a fixture count, on the unchanged schema as well; graded at the drain's checkout by amendment), and this seat's read row D2-S91. Held: D2-W295-S2, D2-S92.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W295-S1",
      "IRPT_BCKEND-D2-W295-S3",
      "IRPT_BCKEND-D2-S91"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "IB-pr-404 and IB-pr-413 are pending on the 2026-10-12 fire, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W295-S1, D2-W295-S3, D2-S91",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_135_136_P_DRAIN_END_20261011.md @dc47506c21 (msg 5271)",
        "this seat's reads 2026-10-11T16:04:13Z of docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json at HEAD: data.anyOf holds 2 forms, each additionalProperties false; the vendor form's six members are v1 $refs; the Opal form requires provider, request_ref, sections and computation_validation, and each of those four carries a plain const or type plus allOf of one {if: {}, then: {$ref into the v2 report schema}}; an empty `if` is always true, so a Draft-07 validator enforces the v2 shape; retained_ref is a v1 $ref in both forms"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A repair made in its order, a check artifact, and a read row."
  }
]
```
