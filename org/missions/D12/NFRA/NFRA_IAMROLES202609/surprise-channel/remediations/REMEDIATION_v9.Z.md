# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v9 (site Z) -- THE ROUND-9 SLUG, AND THE PROJECT CLOSE

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-13 ~07:1xZ. **Reader:** `1.0.0_SA_CTO~Z`, who answers with the CLOSE (msg 33510).

**Round 9:** 6 of 6 orders complete. round-close-check reads MAY-CLOSE (orders 6, judgment 6, graded 6, ungraded 0, self_graded 0). L9 at `adjudications/ADJUDICATION_v1.md`:
- C-S45 to C-S49: z-1 PASS, z-3 PASS, z-4 FAIL narrow, z-5 PASS, z-6 PASS bounded.
- C-S50: z-2 PASS, bounded. No live path remains to the canonical build (303 roles swept). Both post-delete bd
  chains were read at 29 of 29. The staged builder copies still read the name (Z-S44).
- L8: C-S51 dismisses 3 rows; C-S52 graduates 6.

**PROJECT CLOSE -- FWD-4's 16 rows as they end:** 8 DECLARED in Terraform (rows 1, 2, 3, 6, 9, 11, 13, 14; rounds 6-7 adopted
7 of them, and row 13 was already declared), 5 EXEMPT with named owners (rows 4, 8, 10, 12, 15), 2 DEFER, each with a reopen condition
(rows 5, 16), and 1 RETIRED (row 7, lambda-test-role, deleted 2026-10-11). That is 16 of 16 owned and 0 unowned. Rounds 7-9 also
removed live grants on dead or claimable names: x-2, x-5 (12 ARNs on the portal role), z-1, z-2, z-3. The rows below carry what
outlives the project. Every owner is a seat that survives the close; none is the ended issuer.

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S47",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the opal-* bucket name list is a declared floor (dell2's trail never read, dell1 a partial 2000-event sample), not a census, and the opal* grant is a bucket-CREATION grant that no list of names can replace without breaking its holder",
    "evidence": [
      "ADJUDICATION_v1 Z-C-S47 (TO-IAM-z-4 AC4 FAIL, narrow)"
    ],
    "remedy": "Read the full CloudTrail on every box to turn the floor into a census, then replace opal* with a constrained creation grant (a name-prefix condition plus a tag-on-create condition).",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S44",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the canonical Schwab runner executes S3-staged copies (s3://opal-data-bd/code/canonical/schwab/build_canonical_daily.py and code/canonical-schwab-runner/s8_gate.py, both 2026-06-29) that still read the deleted, claimable opal-data-schwab; a repo fix does not move them",
    "evidence": [
      "ADJUDICATION_v1 Z-C-S50: staged copy md5 883960c6097d vs HEAD d441869da69c, 2 Bucket=SRC_BUCKET reads; s8_gate.py SRC_BUCKET='opal-data-schwab'; no canonical output since 2026-07-24"
    ],
    "remedy": "Restage both copies from HEAD (s8_gate.py also needs its own re-point off opal-data-schwab) under a never-widen pair, or delete the staged copies and retire the runner; either way, never run the staged copy as it stands.",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S46",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "both ends of the smartx chain (EC2 smartx-exporter production.env/run-all-portfolios.sh and Lambda opal-smartx-ingestion-pipeline) are configured to opal-data-smartx-v2, which reads NoSuchBucket; z-1 removed the write grants, so a claimant receives nothing, but the chain cannot run",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S46 (34 + 19 references); ADJUDICATION_v1 Z-C-S45 (z-1 PASS)"
    ],
    "remedy": "The smartx pipeline's owner decides: re-point to a live bucket, or retire the chain and its two components.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S51",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "two production consumers hold 44 live, non-comment S3 references to opal-data-smartx-v2 (EC2 smartx-exporter 30, Lambda opal-smartx-ingestion-pipeline 14)",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S51 (z-1's reference census)"
    ],
    "remedy": "Rides Z-S46's decision.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S47",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "aws logs filter-log-events with --query 'length(events)' applies the query per page and prints one count per page, so a first-line read under-reports a positive and a zero proves only the first page",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S47: 10 matching events printed '2' five times; no matches printed '0' six times"
    ],
    "remedy": "Add it to the /cloud-ops instrument traps beside the list-* rule: auto-paginate, then count client-side.",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S49",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FredIngestionLambdaRole's inline SecretsManagerAccess grants GetSecretValue on arn:aws:secretsmanager:us-east-2:313476888478:secret:FredApiKey-yWbGDi, which returns ResourceNotFoundException, a dead SECRET outside the project's S3-name instrument",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S49"
    ],
    "remedy": "Remove the dead secret statement under a never-widen pair (the live fred-ingestion-secrets-read covers the function), and widen the dead-reference sweep to secrets, tables and keys.",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v9"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S50",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "yield_curve_fred.json writes data_as_of as the run date (2026-10-11) while every tenor's newest observation is 2026-10-08, so a consumer believes the curve is fresher than it is",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S50; ADJUDICATION_v1 Z-C-S49 (z-6 PASS, bounded)"
    ],
    "remedy": "Write data_as_of as the newest observation date across tenors, and keep generated_at for the run time.",
    "owner": "0.7.0_AE_CloudOps~Z",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps~Z",
      "round": "v9"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
