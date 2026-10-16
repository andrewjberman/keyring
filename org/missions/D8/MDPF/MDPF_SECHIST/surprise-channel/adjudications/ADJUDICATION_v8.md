# MDPF_SECHIST -- round 6 L9: the four judgment criteria (INTERIM packet) (dell1)

<sweep_watermark>2026-10-13T19:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T23:36:42Z. Asked by 2.0.0_SA_COO~H1 msg 6319, packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/L8_PACKET_MDPF_SECHIST_ROUND6_DRAFT_20261015.md` @11e48d7278 (INTERIM). Grades only; round 6's
rows are swept with the FINAL packet after the 2026-10-16 to 10-20 reads, so the watermark does not move. FWD-9 is not graded here.

```json
[
  {
    "id": "MDPF_SECHIST-D1-C-S10",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T23:36:42Z",
    "one_line": "ROUND 6 L9: JUDGMENT MDPF_SECHIST.TO-SH-t25 SH6-t25-AC4 MET, read on the three screenshots. Each carried SALXX cell carries 'as of 10-09' and the note sits under the table; AAPL carries nothing; with the keys removed, there is no mark and no note. Two nits on wording and density.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_SECHIST.TO-SH-t25 SH6-t25-AC4 (judgment): the reading of the labelled cells and the note on the screenshot of the Positioning page.",
    "world_is": "MDPF_SECHIST.TO-SH-t25 SH6-t25-AC4 MET. READ BY THIS SEAT with the Read tool: org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_AC4/ @e729d5e3bc, made on portal DEV e0b033253b (contains the feature c77f23624d) against the order's fixture. positioning_etf_performance_with_carry.png, Holdings Breakdown, Performance view, book DIVZ: the AAPL row prints 1D -0.30%, MTD +2.00%, YTD +15.70% with no mark. The SALXX row prints 1D +0.12%, MTD +1.50%, YTD +4.20%, and its dashed windows (WTD, 1M, QTD, 1Q, 1Y), each with 'as of 10-09' in small secondary type beneath. Under the table: 'Returns for SALXX are as of SALXX 2026-10-09 (no vendor day on the book date).' positioning_etf_performance_no_carry_baseline.png: the same rows and numbers with no mark and no note. NITS, not grounds to fail (the order specified both): the note repeats the ticker ('as of SALXX 2026-10-09'); a date under a dash reads as density on a five-of-eight-blank row. The 'SAL...' ticker truncation is in the baseline too, so it predates the feature. The 10 px mark is legible at screenshot size; contrast was not measured by instrument. LIMIT: a fixture, not a served carried holding; the next held closed-market day is 2026-11-11 unless a book stays at a closed-market as_of. PROD carries the label (t26: fa10e75861ab, CI success).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_AC4/positioning_etf_performance_with_carry.png and positioning_etf_performance_no_carry_baseline.png, read by 3.0.0_SA_CVO",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_AC4/README.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: SH6-t25-AC4 MET."
  },
  {
    "id": "MDPF_SECHIST-D1-C-S11",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T23:36:42Z",
    "one_line": "ROUND 6 L9: JUDGMENT MDPF_SECHIST.TO-SH-t27 SH6-t27-AC2 MET, SH6-t27-AC3 MET, SH6-t27-AC4 MET. The plan changes the Lambda's code only; the live CodeSha256 equals the plan's; the role can reach only opal-data-etfs and the platinum etfs prefix, so no firm bucket or 49F principal was touched and no 49F data can land in another firm's tree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_SECHIST.TO-SH-t27 judgment criteria: AC2 the plan JSON shows the Lambda code change only and zero IAM, schedule, env, layer or handler change; AC3 a send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST; AC4 49 Financial data never goes into another firm's tree.",
    "world_is": "MDPF_SECHIST.TO-SH-t27 SH6-t27-AC2 MET: evidence/frontier_plan_20261014.txt, graded from terraform show -json, reads 9 resource_changes with 8 no-op and 1 update (module.etf_positioning_producer.aws_lambda_function.this). IAM resources not no-op: 0. Of 46 Lambda attributes, only last_modified, s3_object_version and source_code_hash differ; environment, layers, handler, memory, timeout, role and runtime are unchanged. The event rule and target are no-op. Read live here: aws lambda get-function-configuration etf-positioning-producer gives CodeSha256 M6X6eJ3QCDXopGif5PvlrlqBS/ynXHOpuxWDUIGFbAQ= (the plan's after value), handler etf_positioning_gold.lambda_handler, LastModified 2026-10-14T19:13:06Z. The amended rebuild at pin 11dc6a2161 differs from live in exactly the two named members (evidence/frontier_member_comparison_20261014.txt). MDPF_SECHIST.TO-SH-t27 SH6-t27-AC3 MET: the act's only write is the Lambda artifact (artifact_key etfs-positioning/etf-positioning-producer.zip through the yang-lambda module, producer-lambda.tf:234), not a firm data bucket. The seat's session record names no AssumeRole and no 49F principal. So no send arose that the laptop had to hear first. MDPF_SECHIST.TO-SH-t27 SH6-t27-AC4 MET: read live here, the role etf-positioning-producer-role grants S3 on opal-data-etfs (bbg/, bbg-testpull/tickers/, bloomberg/etfs/silver/history_gaps/, config/etf_universe.json, gold/, silver/holdings/, silver/netassets/) and opal-data-portal-v2/platinum/etfs/* only. The plan changed no IAM, so the producer cannot read a 49 Financial tree or write into another firm's tree.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/frontier_plan_20261014.txt",
        "org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/frontier_member_comparison_20261014.txt",
        "aws lambda get-function-configuration --function-name etf-positioning-producer (3.0.0_SA_CVO, 2026-10-15T23:3xZ)",
        "aws iam get-role-policy on etf-positioning-producer-role (3.0.0_SA_CVO, 2026-10-15T23:3xZ)",
        "infra/aws/terraform/etfs-positioning/producer-lambda.tf:233-234"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: SH6-t27-AC2, AC3 and AC4 MET."
  }
]
```

-- 3.0.0_SA_CVO
