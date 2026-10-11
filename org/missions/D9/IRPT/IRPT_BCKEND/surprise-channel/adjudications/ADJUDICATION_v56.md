# IRPT_BCKEND: CVO adjudication, rounds 119 to 121 (workstream ~P)

<sweep_watermark>2026-10-11T09:39Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:39:12Z. Input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_119_121_P_DRAIN_END_20261011.md @a3cb79cdb6 (msg 4591)`. No judgment criterion.
**Read** (row D2-S75): the vendor performance release is APPLIED, UNEXERCISED; the live bytes and the two grants match the packet.
5 rows dismissed below. 4 rows are held to graduate in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S332",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:39:12Z",
    "one_line": "Rounds 119-121 (~P) rows dismissed: D2-W282-S1 with its resolving row D2-S73 (the adapter role lacked the secret read; both single-secret grants are read live by this seat), D2-W283-S1 with its resolving row D2-S74 (the deferred Lambda plan line; ruled a targeted apply, the applier's 2/0/0 then 0/1/0, not re-read here), and this seat's read row D2-S75. Four rows are held to graduate: D2-W282-S2, D2-W282-S3, D2-S71, D2-S72.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W282-S1",
      "IRPT_BCKEND-D2-S73",
      "IRPT_BCKEND-D2-W283-S1",
      "IRPT_BCKEND-D2-S74",
      "IRPT_BCKEND-D2-S75"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rounds 119, 120 and 121 are terminal. Two IRPT_BCKEND orders (IB-pr-404, IB-pr-413) are pending on the 2026-10-12 fire, so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W282-S1, D2-S73, D2-W283-S1, D2-S74, D2-S75",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_119_121_P_DRAIN_END_20261011.md @a3cb79cdb6 (msg 4591)",
        "this seat's live reads 2026-10-11T09:39:12Z: irpt-performance-adapter CodeSha256 OF+8j4uc...859RU=, LastModified 2026-10-11T09:19:10Z, equal to the build the packet names; irpt-performance-adapter-role holds 9 inline policies; each of its two session policies is 1 Allow statement with the single action secretsmanager:GetSecretValue on 1 resource"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A missing grant read live as present, a plan artifact ruled and applied, their resolving rows, and a read row."
  }
]
```
