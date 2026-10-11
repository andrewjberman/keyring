# NFRA_OPLGTW -- surprise channel, ADJUDICATION v24 (site Z) -- ROUND 33 L8 + L9

**Lane:** the CVO. **By:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~14:0xZ, on `2.0.0_SA_COO~O` msg 33281 (packet
`deliverables/2.0.0_SA_COO~O/ROUND33_TERMINAL_20261011.md @8e37955c18`; 10 of 10 orders complete, proofs VALID).

**Judgment:** ONE of the three is graded here (C-S63). The other two are NOT graded, because the act each one reads has
not happened: dell2's per-meeting re-probe of the transcript allowlist has no row in NFRA_TRNSPT's channel, and
s3://opal-data-assets/smartx/49financial/ does not exist (the bucket answers; sibling smartx/ prefixes list). This file
deliberately carries no row naming either criterion, so round-close-check cannot read them as graded. Both are carried in
the slug. **L8:** C-S64 dismisses 19 rows and C-S65 graduates 10 (29 of 29 undispositioned rows).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S63",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T14:00Z",
    "one_line": "L9 grade, TO-OG-bh-1 AC3 (judgment, EXACT SAME): PASS -- for 2026-10-07 and 2025-04-15, 08403355's bronze key grammar, silver tables' columns and types, and completion-record shape equal 08335338's; the only differences are source files Schwab does not publish for 08403355 (slm, fam), named as such in its own closure.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-bh-1 AC3: EXACT SAME -- 08403355's bronze key grammar, silver datasets and columns, and completion-record shape equal 08335338's for the same date.",
    "world_is": "This seat read s3://opal-data-assets/schwab/{08335338,08403355}/ for two dates. BRONZE: every type both masters carry follows one grammar, schwab/<M>/bronze/<type>/<YYYYMMDD>/<M>.CRS<YYYYMMDD>.<TYPE>.zip. 08335338 alone carries slm (and fam on 2025-04-15) as CS<mmddyy> files. 08403355 has NO slm/ or fam/ prefix anywhere in its bronze history, so they are unpublished for that master, not lost by the backfill. SILVER: on 2026-10-07, 14 tables are shared and 0 differ in column names or Arrow types (pyarrow schema of each data.parquet); 08335338 adds only fact_slm. On 2025-04-15, the same 14 are shared with 0 differing, and 08335338 adds fact_fam and fact_slm. COMPLETION RECORD (meta/complete/date=2026-10-07.json): the same schema opal.silver.complete/v1, the same 10 top-level keys, the same closure schema opal.silver.closure/v1 and structure. Both read status=qualified, day_disposition=DATA, missing=0, failed=0. 08403355's closure names slm and fact_slm non_applicable, reason NOT_PUBLISHED_FOR_MASTER. On 2025-04-15, 08335338 has no completion record (its records start 2025-09-08) and 08403355 has one. CARRIED, not grounds: (1) the two records' declared_source pins differ (schwab_schemas.SPECS @1f03a3f209 vs @47c3c75f11), and the columns agree anyway; (2) 'disagreement.declared_not_written' lists all but this run's one written table on BOTH masters, so it is a per-run field, not a defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "boto3 list_objects_v2 + pyarrow.parquet.read_schema over both masters, dates 20261007 and 20250415 (scratch script bh1_same.py, read 2026-10-11 ~13:3xZ)",
        "aws s3api list-objects-v2 --prefix schwab/<M>/bronze/ --delimiter /: 08335338 has 18 types including slm and fam; 08403355 has 16, with no slm or fam",
        "s3 cp meta/complete/date=2026-10-07.json for both masters: closure counts, non_applicable reasons, schema versions",
        "deliverables/2.0.0_SA_COO~O/ROUND33_TERMINAL_20261011.md @8e37955c18"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-OG-bh-1 AC3 PASS."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S64",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T14:00Z",
    "one_line": "Round 33 L8: 19 rows DISMISSED -- the BLOCKING/ARMED ones each resolved by a committed amendment, re-cut or completed order (W46-S3, W50-S2, W51-S1, Z-S78, Z-S81), and fourteen worker or issuer notes with no standing defect.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned BLOCKING or ARMED row of the round.",
    "world_is": "W46-S3 (bh-1 stopped on six era-C RPS dates) is resolved by AMENDMENT 1 (W46-S4) and OG-pn-1: the converter grades a table by its own D-tag, and the six dates re-ran 6 of 6 qualified; W50-S1 is the cause. W50-S2 (AC1's expect regex): OG-pn-1 is complete with a VALID proof (round-close-check proof_ok=10 of 10). W51-S1 (release branch name taken): the re-cut used rel-nfra-oplgtw-r16c. Z-S78 is resolved by Z-S80 (ap-5 AMENDMENT 1, OPAL_BUILD_COMMIT b3e481b261). Z-S81 is resolved by Z-S83 (policy planned from a box/sitez-HEAD worktree); this seat's RE-PIN 1 measured the policy blob 49c420ac equal at a88661b145, 6aadf7db37 and HEAD. Z-S82: the four host orphans are read back unchanged (Z-S83); the standing pruning gap is NFRA_MCPINDEX-Z-S94, already graduated to 2.0.0_SA_COO~O. Z-S79 is corrected @68c493e37c. W45-S1, W45-S3, W46-S1, W46-S2, W47-S1, W48-S2, W48-S3 (resolved by A1 @9ba3e56d87; its standing remainder is Z-S85), W49-S6, W51-S2 and W51-S4 are worker notes on premises, procedure or confirmed design, with no standing defect.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W45-S1",
      "NFRA_OPLGTW-Z-W45-S3",
      "NFRA_OPLGTW-Z-W46-S1",
      "NFRA_OPLGTW-Z-W46-S2",
      "NFRA_OPLGTW-Z-W46-S3",
      "NFRA_OPLGTW-Z-W46-S4",
      "NFRA_OPLGTW-Z-W47-S1",
      "NFRA_OPLGTW-Z-W48-S2",
      "NFRA_OPLGTW-Z-W48-S3",
      "NFRA_OPLGTW-Z-W49-S6",
      "NFRA_OPLGTW-Z-W50-S1",
      "NFRA_OPLGTW-Z-W50-S2",
      "NFRA_OPLGTW-Z-W51-S1",
      "NFRA_OPLGTW-Z-W51-S2",
      "NFRA_OPLGTW-Z-W51-S4",
      "NFRA_OPLGTW-Z-S78",
      "NFRA_OPLGTW-Z-S79",
      "NFRA_OPLGTW-Z-S81",
      "NFRA_OPLGTW-Z-S82"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/ROUND33_TERMINAL_20261011.md @8e37955c18",
        "investigation rows Z-W45-S1, Z-W45-S3, Z-W46-S1, Z-W46-S2, Z-W46-S3, Z-W46-S4, Z-W47-S1, Z-W48-S2, Z-W48-S3, Z-W49-S6, Z-W50-S1, Z-W50-S2, Z-W51-S1, Z-W51-S2, Z-W51-S4, Z-S78, Z-S79, Z-S81, Z-S82",
        "issuer rows Z-S80, Z-S83 (DISMISSED_WITH_REASON)",
        "git log 68c493e37c",
        "half RE-PIN 1 @b8b7ab0f11"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by committed amendments, re-cuts or completed orders, or notes with no standing defect."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S65",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-11T14:00Z",
    "one_line": "Round 33 L8: 10 rows GRADUATE to REMEDIATION_v16 -- Z-S85 (ARMED: trunk's deploy script writes the transcript allowlist EMPTY; 0 refs at HEAD vs 5 at the live release), an unknown DLQ consumer (Z-S77), the BD tool open to unprofiled principals (W45-S2, a CTO call), the stale EC2 manifest (Z-S84), and six check or test gaps.",
    "class": "OBSERVATION",
    "spec_asserts": "A standing defect leaves the round as an owned remediation row.",
    "world_is": "Z-S85, re-read here: git show HEAD:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh has 0 'meeting_allowlist' references, and 6aadf7db37 has 5. A trunk-cut release revokes the 4-meeting allowlist silently. Z-S77, re-read here: CloudTrail shows no PurgeQueue and no management event on opal-assets-silver-dlq 15:00-17:00Z 2026-10-09. MessageRetentionPeriod is 1209600 s (14 days, so not expiry), and there is NO Lambda event-source mapping on the queue. The six messages were received and deleted by a data-plane actor nobody has named. The queue holds ApproximateNumberOfMessages=12 now. W45-S2: blackdiamond_list_fees passes an unprofiled principal to its own gate, where every Schwab family tool is denied. The worker kept it deliberately; whether to deny it is a policy call. Z-S84: EC2_MANIFEST file_checksums are stale on 8 of 10 entries. W45-S4 and W47-S2: pre-existing gateway test failures (portal_grant asker_sender_domain and three suites). W49-S2: the registry has no table row for fee_statement or market_update, while address() accepts any snake_case table. W51-S3: naming-gate errors on DIRECTIVES.yaml in a sparse worktree. W51-S5: rl16's mechanical AC1 read the Phase A record, not the live re-cut; the substance holds by this seat's patch-id re-pin and the served-release read. W51-S6: the bad-quarter refusal was exercised through the module entry, not the MCP wrapper.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W45-S2",
      "NFRA_OPLGTW-Z-W45-S4",
      "NFRA_OPLGTW-Z-W47-S2",
      "NFRA_OPLGTW-Z-W49-S2",
      "NFRA_OPLGTW-Z-W51-S3",
      "NFRA_OPLGTW-Z-W51-S5",
      "NFRA_OPLGTW-Z-W51-S6",
      "NFRA_OPLGTW-Z-S77",
      "NFRA_OPLGTW-Z-S84",
      "NFRA_OPLGTW-Z-S85"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show HEAD and 6aadf7db37 :infra/aws/ec2/opal-gateway/deploy-to-ec2.sh | grep -c meeting_allowlist -> 0 and 5",
        "cloudtrail lookup-events PurgeQueue and ResourceName=opal-assets-silver-dlq, 2026-10-09 15:00-17:00Z: 0 events; sqs get-queue-attributes: retention 1209600, ApproximateNumberOfMessages 12; lambda list-event-source-mappings on the queue ARN: none",
        "investigation rows Z-W45-S2, Z-W45-S4, Z-W47-S2, Z-W49-S2, Z-W51-S3, Z-W51-S5, Z-W51-S6, Z-S77, Z-S84, Z-S85",
        "deliverables/2.0.0_SA_COO~O/ROUND33_TERMINAL_20261011.md @8e37955c18"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
