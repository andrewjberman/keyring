# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v6 (site Z) -- THE ROUND-6 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~04:4xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 6 is terminal: 4 of 4 orders complete with VALID proofs (`ledger/COMPLETION_REPORT.round6.json` @dfe1a35d13).

**L9:** AC4 x4 PASS, at `ADJUDICATION_v1.md` C-S28 (w-1), C-S29 (w-2), C-S30 (w-3) and C-S31 (w-4). The custody grades rest on
CloudTrail, not on the post-apply reads: the five adopted roles carry exactly one IAM write each since 10-09, a TagRole, and
the account-wide TagRole count is the same five. FWD-4 is in code for 6 of 16 rows, and every row is owned.

**L8:** C-S32 dismisses 12 rows. **Z-S37 is OVERTAKEN:** it recorded the R20 ask withdrawn at 02:55Z, but Andrew said yes at
~03:2xZ and the R20 entries landed @bd2cacee69. C-S33 graduates the 5 rows below.

**For the analysis:**
1. The two remaining ADOPT rows (6 lambda-ec2-runtime-monitor-role, 14 sentiment_query_api-role) are outside round 6's
   families.
2. GOVERNANCE_DISPOSITION.md's tokens for the five adopted rows still read ADOPT: the world moved and the record did not.
3. Z-S34's R20 bridge has a date on it (2026-12-31).

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-S21",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "infra/aws/terraform/smartx-pipeline carries three pre-existing Lambda drifts (assets_daily_pull, jwt_refresher, rest_pull s3_object_version / source_code_hash) and three outputs going null; any UNSCOPED apply of the module deploys them",
    "evidence": [
      "Z-S21; PLAN_SURVEY_family_b.md section 5 (baseline plan 0/3/0 without the adoption)"
    ],
    "remedy": "The smartx pipeline's owner reconciles the drift (deploy deliberately or revert the source) under its own pair; until then every apply of the module is -target scoped.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S23",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal-smartx-lambda-role's inline grants name an S3 bucket and secrets that do not exist live, on a role no Lambda assumes",
    "evidence": [
      "Z-S23; Z-S24 (the issuer's reading: nothing runs on it)"
    ],
    "remedy": "Decide in the next disposition pass: narrow the dead grants, or record the role under DEFER with a reopen condition like rows 5 and 16.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S32",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "codebuild-semantic-clustering-role's inline grant names a bucket that returns NoSuchBucket",
    "evidence": [
      "Z-S32 (1.0.0_SA_CTO~Z, signing the w-3 CTO half @8453026444)"
    ],
    "remedy": "Same pass as Z-S23: narrow the dead grant, or record why it stays.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S25",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "naming-gate.py judge() decides NEW from the file's pre-image, so a pre-existing live resource adopted under its live name reads NEW and OUT-OF-PATTERN",
    "evidence": [
      "Z-S25; crossbox XB-20261010T225240Z-dcb5 (LGIC_ENFORCE PRD v1.4 FWD-8 at dell1)"
    ],
    "remedy": "LGIC_ENFORCE FWD-8 served: an adopted live name reads EXISTING on both naming limbs. The placement override stays until then.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S34",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bd-merge-daily-lambda-role and bd-pipeline-task-role are in code on R20 entries NFRA-IAMROLES-R20-01/02 that Andrew granted 'for now', cutoff 2026-12-31",
    "evidence": [
      "@bd2cacee69; ANDREW_DIRECT_20261011_032xZ item 4"
    ],
    "remedy": "Before 2026-12-31: either FWD-8 serves (the names read EXISTING and the R20 entries retire), or the exception is re-decided by Andrew.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v6"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
