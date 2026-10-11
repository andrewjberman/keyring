# IRPT_BCKEND: CVO adjudication, rounds 133 and 134 (workstream ~P)

<sweep_watermark>2026-10-11T15:36Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T15:36:53Z. Input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_133_134_P_DRAIN_END_20261011.md @b23f6ec18f (msg 5234)`. No judgment criterion. Both orders read-only.
3 rows dismissed below. 4 rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S337",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:36:53Z",
    "one_line": "Rounds 133 and 134 (~P) rows dismissed: D2-W294-S2 (the worker read one library version and the issuer another; this box's default python reads the issuer's, 1.2.0, and the packet states no effect on the result), D2-W294-S3 (the majority-mark rule hides 497 prior-day rows; the worker added the row-level counts and the packet carries them), and this seat's read row D2-S90. Held: D2-W293-S1, D2-W293-S2, D2-W293-S3, D2-W294-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W294-S2",
      "IRPT_BCKEND-D2-W294-S3",
      "IRPT_BCKEND-D2-S90"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Four IRPT_BCKEND orders are pending (IB-pr-404, IB-pr-413, IB-pr-437, IB-pr-438), so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W294-S2, D2-W294-S3, D2-S90",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_133_134_P_DRAIN_END_20261011.md @b23f6ec18f (msg 5234)",
        "this seat's read 2026-10-11T15:36:53Z: the box's default python (3.14.7, the one `python` resolves to) imports yfinance 1.2.0, which agrees with the issuer's read and not the worker's 1.7.0; a second interpreter on the box was not searched for"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A version question read on the box, a disclosure carried in the packet, and a read row."
  }
]
```
