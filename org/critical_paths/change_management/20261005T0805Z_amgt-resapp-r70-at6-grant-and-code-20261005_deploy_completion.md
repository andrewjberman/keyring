# Deploy Completion Record
**Date opened:** 2026-10-05T08:05:18.653729+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 70 AMGT-at-6: TWO legs under ONE entry -- (1) grant leg, add exactly one prefix issuer-site/harvest/silver/filing_source/ to local.scoped_amgt_pool_prefixes and ONE targeted safe-apply on aws_iam_role_policy.scoped_amgt_api_grants, then AC4 YES with issuer-site/harvest/bronze/ still implicitDeny; (2) code leg, ONE artifact at build commit e041c86791 carrying at-1..at-4 then ONE code-only safe-apply, memory_size stays 1769. Base CodeSha256 OcKZF34X9liuVKg9ZnpaqBcbSxwcDl6JlW+PlxWyF4k= / VersionId WlTp7CvQs4zkxFnYmwhDPB8cITLFF.Ve (round 69 as-2); rollback per leg -- the grant leg a targeted safe-apply with the entry removed, the code leg that VersionId through one code-only safe-apply
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 5.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_iam_role_policy.scoped_amgt_api_grants -- add exactly one prefix issuer-site/harvest/silver/filing_source/ | the targeted plan is ONE in-place update of the grants policy and nothing else, proven from a FULL show -json (0 destroy/create/replace, 0 other non-no-op resources); the added strings are exactly opal-data-harvest/issuer-site/harvest/silver/filing_source/* in the GetObject Resource list and issuer-site/harvest/silver/filing_source/* in the ListBucket s3:prefix condition; BEFORE/AFTER simulate pair on the new prefix (implicitDeny -> allowed on both limbs) AND issuer-site/harvest/bronze/ still implicitDeny after, each call one --resource-arns with an isolated control |  | OPEN |
| L2 | verify | AC4 r70_grant_at6.sh on the APPLIED plane, before the code leg | both controls allowed and C1 GetObject + C2 ListBucket allowed on issuer-site/harvest/silver/filing_source/; R70 AT6 GRANT: YES; exit=0. The BEFORE run of the same script is the negative arm and must have read NO |  | OPEN |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 read back by the uploader and independently by head-object; CONTENT-DIFF against the DEPLOYED build exactly files 363 IDENTICAL 354 CHANGED 2 ADDED 7 REMOVED 0, the CHANGED being lib/research/api/scoped_amgt.py and lib/research/harvest/store.py and the ADDED being the seven AMENDMENT 1 names; size printed and under 262144000 B; plus a simulate arm reading allowed for every new S3 read path the halves list, taken BEFORE the code leg is called LANDED |  | OPEN |
| L4 | activation | opal-amgt-scoped-api code-only safe-apply at pin e041c86791 | new CodeSha256 off OcKZF34X + MemorySize still 1769, proven from a FULL show -json plan: exactly 1 non-no-op (the lambda, update), 0 destroy/create/replace, 0 non-no-op IAM (the grant leg is already applied and must show no-op here), 0 non-no-op route/gateway; then a full 0-diff replan and the deployed sha re-read live |  | OPEN |
| L5 | verify | AC1 r70 c30+c31, AC2 r70 c32+c33, AC3 r69 c29 + r68 c27/c28 + r67 c23-c26, all on deployed; plus the reported set r64 c9/c10/c11/c12/c13/c14, r65 c17, r66 c18/c19/c22, r64 c15 amended taken FIRST after the apply, and /peers timed per segment on 3 names | each verdict line with exit=0; rollback to VersionId WlTp7CvQs4zkxFnYmwhDPB8cITLFF.Ve if c30-c33 are not YES, any other check moves, c15 exceeds 5 s, a covered key returns non-200, or ZZZZ_US_Equity answers anything but 404. A /peers latency over 5 s is a STOP reported with its segment times, not a rollback |  | OPEN |

## Log

- 20261005T080518Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
