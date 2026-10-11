# IRPT_BCKEND: CVO adjudication, round 118 (workstream ~P)

<sweep_watermark>2026-10-11T04:42Z</sweep_watermark>

Round 118 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T04:42:13Z. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_118_P_DRAIN_END_20261011.md @6eaa44414b (msg 4085)`. No judgment criterion.
This seat's reads: the adapter and the narrative are live on the map's digests; each log shows the TypeError before the apply and a typed
refusal after. 5 rows dismissed below. The held rows in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md` are updated: D2-S60 narrows to irpt-status, and D2-W278-S5's live
mismatch is closed. The slug still waits: 2 IRPT_BCKEND orders read pending. ARMED: 1 (D2-S60).

```json
[
  {
    "id": "IRPT_BCKEND-C-S331",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:42:13Z",
    "one_line": "Round 118 rows dismissed: D2-S65 (the resolving record for D2-S64, dismissed at round 117), D2-S66 (the resolving record for D2-W278-S2, dismissed at round 117), D2-S68 with its resolving record D2-S69 (IB118-1-AC1 compared a field the apply rewrites; re-cut by AMENDMENT 1 @8d0d9976ed; the live digests equal the map), and this seat's read row D2-S70. D2-S60 stays ARMED for irpt-status alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-S65",
      "IRPT_BCKEND-D2-S66",
      "IRPT_BCKEND-D2-S68",
      "IRPT_BCKEND-D2-S69",
      "IRPT_BCKEND-D2-S70"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 118 is terminal (1 of 1 complete, 0 judgment). Two IRPT_BCKEND orders read pending, so the slug still waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S65, D2-S66, D2-S68, D2-S69, D2-S70",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_118_P_DRAIN_END_20261011.md @6eaa44414b (msg 4085)",
        "this seat's live reads 2026-10-11T04:42:13Z: irpt-performance-adapter CodeSha256 9kYLdR64... LastModified 2026-10-11T03:59:40Z; irpt-narrative x0SqAx2U... 04:08:06Z; both equal their source-map artifact_sha256; irpt-status t6OJTCcm... 2026-10-09T18:02:51Z, unchanged, and not equal to its map entry (E7VKvhg3...)",
        "this seat's filter-log-events: irpt-performance-adapter -- 6 TypeError lines from 2026-10-09T15:41Z, the last at 2026-10-11T03:57Z; after the 03:59:40Z apply, 1 invocation (04:00:42Z), performance-report NOT_AUTHORIZED (AuthzError NO_PRINCIPAL), 0 TypeError. irpt-narrative -- 1 invocation before the apply (04:04:32Z) with 1 TypeError; 1 after (04:08:22Z), narrative-packet NOT_AUTHORIZED, 0 TypeError"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolving records for rows already dismissed, a repaired issuer check, and a read row."
  }
]
```
