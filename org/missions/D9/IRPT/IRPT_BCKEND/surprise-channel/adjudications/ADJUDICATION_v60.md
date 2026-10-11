# IRPT_BCKEND: CVO adjudication, rounds 127 (amended), 129, 130 and 132 (workstream ~P)

<sweep_watermark>2026-10-11T14:58Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T14:58:13Z. Input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_127B_129_130_132_P_DRAIN_END_20261011.md @0135c6f2c8 (msg 5175)`. No judgment criterion. Nothing applied or served.
4 rows dismissed below. 6 rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S336",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T14:58:13Z",
    "one_line": "Rounds 127 (amended), 129, 130, 132 (~P) rows dismissed: D2-W290-S1 (the contract test's registry loaded only v1 schemas; ruled by AMENDMENT 1, a bounded edit with a control), D2-W290-S2 (ARMED: one existing test turned red on the new two-form shape; repaired by the issuer before the merge, and the repair read by this seat adds an assertion and removes none), D2-S87 (two false positives in the issuer's own check; amended), and this seat's read row D2-S89. Held: D2-W288-S2, D2-S85, D2-S86, D2-S88, D2-W292-S1, D2-S84.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W290-S1",
      "IRPT_BCKEND-D2-W290-S2",
      "IRPT_BCKEND-D2-S87",
      "IRPT_BCKEND-D2-S89"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Orders IB-pr-404, IB-pr-413, IB-pr-435 and IB-pr-436 are open, so the slug waits. Other recent rows not in this packet: D2-W293-S1, D2-W293-S2, D2-W293-S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W290-S1, D2-W290-S2, D2-S87, D2-S89",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_127B_129_130_132_P_DRAIN_END_20261011.md @0135c6f2c8 (msg 5175)",
        "this seat's reads 2026-10-11T14:58:13Z: docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json data.anyOf holds 2 forms, each additionalProperties false; the vendor form requires extraction_validation and has no provider member, the Opal form requires provider and computation_validation, so no document fits both; commit 168a3a1400 changes ops/tests/test_owned_report.py by 5 added and 1 removed lines: the test selects the form that requires extraction_validation and adds an assertion that it is closed; no assertion is removed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A ruled bounded edit, a hazard disarmed by a repair this seat read, a check amended, and a read row."
  }
]
```
