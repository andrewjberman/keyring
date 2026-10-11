# IRPT_BCKEND: CVO adjudication, round 122 (workstream ~P, the rollback)

<sweep_watermark>2026-10-11T10:35Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T10:35:01Z. Input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_122_P_DRAIN_END_AND_CORRECTION_20261011.md (msg 4726)`. No judgment criterion.
**Read** (row D2-S77): the rollback is complete, read live. This seat's rounds 119-121 compile (row D2-S75) did not read the
release against the ENDPOINT; corrected here. 2 rows dismissed below. Rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S333",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:35:01Z",
    "one_line": "Round 122 (~P): dismissed, D2-W282-S2 (a repeat of a vendor request is refused: with the release rolled back that is the designed state, read live as rolled back) and this seat's read row D2-S77. Held to graduate: D2-S78, D2-S76, D2-W282-S3, D2-S71, D2-S72.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W282-S2",
      "IRPT_BCKEND-D2-S77"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 122 is terminal. IB-pr-404 and IB-pr-413 are pending on the 2026-10-12 fire, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W282-S2, D2-S77",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_122_P_DRAIN_END_AND_CORRECTION_20261011.md (msg 4726)",
        "this seat's live reads 2026-10-11T10:35:01Z: irpt-performance-adapter CodeSha256 9kYLdR64...W31A=, LastModified 2026-10-11T10:03:25Z (it read OF+8j4uc... at 09:41Z); irpt-performance-adapter-role holds 7 inline policies and neither session policy (it held 9 at 09:41Z)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A designed state restored, and a read row."
  }
]
```
