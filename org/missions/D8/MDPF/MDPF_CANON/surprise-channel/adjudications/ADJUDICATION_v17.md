# MDPF_CANON -- round 9 L9 CORRECTION: CN-p-2 AC4 re-graded NOT MET (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T15:59:17Z. Self-correction, prompted by row MDPF_CANON-D1-S29 (2.0.0_SA_COO~D1 @5437fda3de). One row; no rows swept, so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S90",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T15:59:17Z",
    "one_line": "CORRECTION: JUDGMENT MDPF_CANON.TO-CN-p-2 AC4 is NOT MET, superseding the MET in D1-C-S89 (ADJUDICATION_v16). Variant 2 draws both the carried Models band and the five-model stack on the 9 carried dates after 2026-05-15, so the stack overdraws the served Total by about $1.32B on each.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D1 via row MDPF_CANON-D1-S29 (the round-11 cell on portal/src/lib/trendGrouping.ts buildGlobalTrendRows Variant 2); this row adds no second owner",
    "spec_asserts": "PRD v2.22 override (d) and MDPF_CANON.TO-CN-p-2 AC4: Variant 2 draws one Models band before per-model detail begins (2026-05-15) and the model stack after it, and the groups partition the served Total.",
    "world_is": "THIS SEAT RE-RAN round9/checks/measure_real_variants.ts (UNROLLED=1) over the three gold objects it fetched itself (s3://opal-data-assets/portal/gold/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries/2026-10-14.json, LastModified 2026-10-15 09:31 local), importing portal trendGrouping.ts whose blob a3d11cfe61 equals origin/PROD 33ad65eef3, c3b21a40e2 and the worktree. Counts over the output: Variant 2 rows at or after 2026-05-15 with modelsBand > 0 = 9 of 497, all 9 in carried_dates (9): 2026-05-30, 05-31, 06-06, 06-07, 06-13, 06-14, 06-19, 06-20, 06-21. Rows whose drawn groups sum above the served Total by more than 0.1%: Variant 2 = 9 of 497 (the same 9), Variant 1 = 0 of 497. Row 2026-05-30: total 1,766,813,072.41; five model lines 1,447,899,773.04; modelsBand 1,349,270,858.88; clientSupervised 266,863,283.74; etfStrategies 25,033,596.36; drawn sum about 3.089B. WHY v16 MISSED IT: v16 tested the band on the 383 pre-detail rows and single-firm cells only, and compared each group between the variants; it never summed the drawn groups against the Total, which is the partition clause of the criterion. Every v16 count stands; its verdict does not. A non-internal Global session sees the spikes on PROD today; the fix is client-facing and its PROD push waits on Andrew.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO: DATA_DIR=<own fetch> UNROLLED=1 OUT=m.json bun run round9/checks/measure_real_variants.ts -> rows 497 frontier 2026-10-14; python over m.json: v2 post-begins band>0 = 9 (9 carried); stack>total v2 9 of 497, v1 0 of 497",
        "portal: git rev-parse {HEAD,origin/PROD,c3b21a40e2}:src/lib/trendGrouping.ts and git hash-object src/lib/trendGrouping.ts all a3d11cfe61",
        "org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md MDPF_CANON-D1-S29",
        "adjudications/ADJUDICATION_v16.md MDPF_CANON-D1-C-S89"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Round 9's MAY-CLOSE slug rested on this criterion; that verdict is withdrawn for CN-p-2 AC4 and re-stated to 1.0.0_SA_CTO~DELL1. D1-S29 is confirmed in the world by an independent re-run; its disposition stays with the round-10 L9."
  }
]
```

-- 3.0.0_SA_CVO
