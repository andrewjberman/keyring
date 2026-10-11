# IRPT_BCKEND: CVO adjudication, rounds 123 to 128 (workstream ~P)

<sweep_watermark>2026-10-11T13:11Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T13:11:57Z. Input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_123_128_P_DRAIN_END_20261011.md @f8b92be3b4 (msg 4965)`. No judgment criterion.
**PRD ADDENDUM v0.34: the ratified-text half is REFUSED** (row D2-S82; `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.34_RATIFIED_TEXT_REVIEW_20261011.md @3f67123932`).
9 rows dismissed below. 6 rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S335",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T13:11:57Z",
    "one_line": "Rounds 123 to 128 (~P) rows dismissed: D2-W285-S1 (a check's bar set at 0 where live reads 4; ruled by AMENDMENT 1 of IB-pr-426), D2-W287-S1, D2-W287-S2 and D2-W289-S1 (four closed response schemas omitted the envelope member; 21 of 21 declare it now, read by this seat), D2-W289-S2, S3 and S4 (the naming gate and the handler against a fixture's firm id; ruled by AMENDMENTS 1 to 3 of IB-pr-430), D2-W288-S1 (two ungradeable kinds added by the worker; adopted by ADDENDUM v0.34), and this seat's read row D2-S81. Held: D2-W284-S1, D2-W286-S1, D2-W285-S2, D2-W285-S3, D2-S82, D2-S83.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W285-S1",
      "IRPT_BCKEND-D2-W287-S1",
      "IRPT_BCKEND-D2-W287-S2",
      "IRPT_BCKEND-D2-W289-S1",
      "IRPT_BCKEND-D2-W289-S2",
      "IRPT_BCKEND-D2-W289-S3",
      "IRPT_BCKEND-D2-W289-S4",
      "IRPT_BCKEND-D2-W288-S1",
      "IRPT_BCKEND-D2-S81"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Six rounds terminal. IB-pr-404, IB-pr-413, IB-pr-431 and IB-pr-432 are open, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W285-S1, D2-W287-S1, D2-W287-S2, D2-W289-S1, D2-W289-S2, D2-W289-S3, D2-W289-S4, D2-W288-S1, D2-S81",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_123_128_P_DRAIN_END_20261011.md @f8b92be3b4 (msg 4965)",
        "this seat's reads 2026-10-11T13:11:57Z: all 21 files under docs/contracts/investor-reporting/v1/responses/ name unprojected_grant; prd-signoff status IRPT_BCKEND read 'ratified-text SIGNED 3.0.0_SA_CVO current' at v0.34 before this seat's review, on a signature file whose prd_version is v0.33 @13ee60595d; after the stamp it reads REFUSED, PRD WITHHELD (stamp @f2fa66e7aa)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Stops ruled by amendment, a contract gap closed and read, a recorded adoption, and a read row."
  }
]
```
