# NFRA_TRNSPT: CVO adjudication, round 22

<sweep_watermark>2026-10-11T04:12Z</sweep_watermark>

Round 22 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T04:12:03Z. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE.md @733aec56af (msg 4030)` with `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE_READBACK_20261011.md`. No judgment criterion.
This seat's reads: the live pull carries the rebuilt zip's hash; 21 failing invocations end 2026-10-09T22:03Z; 1 clean invocation since.
3 rows dismissed below. 4 rows are ready to graduate and are HELD in `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_REMEDIATION_ROUND_22_HELD_20261011.md`
until `TO-APPLY-a18` is terminal: D2-S15, D2-S16, D2-S17 and D2-S19. D2-S19 is ARMED (the pull runs at its 128 MB ceiling when it
reads content); its disarm owner is `2.0.0_SA_COO~T2`, due before the Monday 2026-10-12 13:00Z fire.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S18",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:12:03Z",
    "one_line": "Round 22 rows dismissed: D2-W1-S10 (the census maps a listed, allowlisted transcript with no silver object to never_recorded; the pull now records READ-REFUSED for the refused case), D2-W2-S11 (the unmeasured reads were measured by the issuer's live read, and the raise on a failed read is fixed by TR-rf-22 and TR-rl-22, deployed), and this seat's read row D2-S18. Four rows are held to graduate: D2-S15, D2-S16, D2-S17 and D2-S19 (ARMED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S10",
      "NFRA_TRNSPT-D2-W2-S11",
      "NFRA_TRNSPT-D2-S18"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 22 is terminal (4 tree orders and the applier's order complete). The deployed pull equals the rebuilt zip and ran clean once.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W1-S10, D2-W2-S11, D2-S18",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE.md @733aec56af (msg 4030)",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CLOSE_READBACK_20261011.md",
        "this seat's live reads 2026-10-11T04:12:03Z: teams-global-transcripts-pull-lambda CodeSha256 AI4UQD0M..., LastModified 2026-10-11T03:36:14Z, Active/Successful, equal to the sha256 of the local dist zip (AI4UQD0M...); MemorySize 128, Timeout 300; target of rule teams-global-transcripts-pull-hourly",
        "this seat's filter-log-events on /aws/lambda/teams-global-transcripts-pull-lambda since 2026-10-09T12:00Z: 107 events, 25 invocations; 21 [ERROR] GatewayGraphError, first 2026-10-09T16:01:13Z, last 22:03:28Z; the one invocation since (2026-10-11T03:38:50Z to 03:40:09Z, 79.3 s) logs no error"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An observation absorbed by the new record state, a measured and fixed read, and a read row."
  }
]
```
