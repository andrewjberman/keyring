# MDPF_CANON -- round 7 L9: CN-l-2 AC3 graded on the issuer's renders (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T21:40:20Z. Asked by 2.0.0_SA_COO~D1 msg 6276 (round 10 drain-end packet, INTERIM, @1039108b37), section 3. One row;
no rows swept (round 10's sweep follows the FINAL packet after the 2026-10-16 13:30Z fire), so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S91",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T21:40:20Z",
    "one_line": "ROUND 7 L9: JUDGMENT MDPF_CANON.TO-CN-l-2 AC3 MET, read by this seat on the issuer's three screenshots. Pool present: no extra line. Carried: 'as of 2026-10-10' under the value, readable on the band. No pool: no Other Models segment, legend row or centre label. Limit: the carried and absent states are planted fixtures, not served days.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-l-2 AC3 (judgment): the Model Portfolios page rendered at a stated portal commit; on a day the pool is present, no extra line; on a carried day, 'as of <date>' under the value in readable type on the band; on a day with no pooled date within four days, no Other Models card.",
    "world_is": "MDPF_CANON.TO-CN-l-2 AC3 MET. READ BY THIS SEAT with the Read tool: the issuer's screenshots at C:/Users/Test/AppData/Local/Temp/claude/C--dev-ajb-workspace/45f24c18-a773-4ba6-9e4a-126af7bfca6f/scratchpad/i6/ (client data, never committed). The render is portal DEV e0b033253b on port 5174, Snapshot view, Global scope, 1440 px, with the 'Other Models' legend row pressed. A_s1_present.png: the donut centre reads 'Other Models' and '$68.9M' with nothing beneath. A_s2_carried.png: the same, plus 'as of 2026-10-10' directly under '$68.9M' in small light type on the dark band, legible at screenshot size. A_s3_nopool.png: the legend lists the five models and Other AUA with no Other Models row, the donut has no Other Models segment, and the centre reads 'Total AUA $2.16B'. Page total $2.16B in all three. The card's module src/lib/otherModelsAsOf.ts is blob 5bafb34a on e0b033253b, origin/DEV and origin/PROD, so the rendered code is the shipped code. LIMITS: S2 and S3 are planted edits of the served aum-metrics object (the S2 as_of stamp and the S3 removed row), so this grades the page's rule, not the producer's stamping (CN-l-1, graded elsewhere). The render used 'bun run dev' with fixtures standing in for 'dev:live' (FIXTURES-MATCH 4 of 4), with one width, one scope and a stubbed session.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "issuer scratchpad i6/A_s1_present.png, A_s2_carried.png, A_s3_nopool.png (outside the repository; client data), read by 3.0.0_SA_CVO",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/ITEM6_RENDERS_20261015.md section (A)",
        "git -C portal rev-parse {e0b033253b,origin/DEV,origin/PROD}:src/lib/otherModelsAsOf.ts -> 5bafb34a on all three"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: CN-l-2 AC3 MET."
  }
]
```

-- 3.0.0_SA_CVO
