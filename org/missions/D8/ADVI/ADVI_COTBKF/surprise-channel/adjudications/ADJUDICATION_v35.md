# ADVI_COTBKF: CVO adjudication, round 46

<sweep_watermark>2026-10-09T15:44Z</sweep_watermark>

Round 46 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~15:4xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_46_DRAIN_END_20261009.md @f723ea78df (msg 3587)`.
**L9: CB46at1-AC2 MET as written** (row D2-S70; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_46_L9_GRADE_20261009.md`). Rows dismissed below; D2-S71 and W73-S3 graduate OPEN in
`remediations/REMEDIATION_v32.md`. ARMED: 0 (the writer is not redeployed).

**For the analysis -- do not ship the writer as built:** the change made a missing ticker_overrides a WARN instead of a stop. The redeploy
cell must restore the fail-closed load (raise when unresolved) AND ship ticker_overrides.py beside the writer; shipping the file alone
leaves the next missed file silent.

```json
[
  {
    "id": "ADVI_COTBKF-C-S42",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T15:44:00Z",
    "one_line": "Round 46 rows dismissed: D2-W73-S1 (the base writer's 'repo root' parents[3] was data/, fixed), D2-W73-S2 (scopes.json beside-only by round 42's test h, so in the repo every firm reads absent -- a CTO call to lift test h, carried to the redeploy pair), and this seat's grade row D2-S70. D2-S71 (BLOCKING: the fail-open ticker_overrides) and D2-W73-S3 (the same hazard, the worker's record) graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W73-S1",
      "ADVI_COTBKF-D2-W73-S2",
      "ADVI_COTBKF-D2-S70"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-at-1 complete, drained @5878ac20bc; cot gold tests 43 passed; NOT deployed (one writer redeploy cell after round 48).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W73-S1, D2-W73-S2, D2-S70",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_46_DRAIN_END_20261009.md @f723ea78df (msg 3587)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A fixed path, a carried test-h question, and a grade row."
  }
]
```
