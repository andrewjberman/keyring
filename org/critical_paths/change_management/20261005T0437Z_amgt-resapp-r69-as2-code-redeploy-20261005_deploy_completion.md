# Deploy Completion Record
**Date opened:** 2026-10-05T04:37:47.678973+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 69 AMGT-as-2: ONE code-only redeploy of opal-amgt-scoped-api at build commit 863c62a855, carrying as-1 (the /ledger filings reason printed once, plus the driver-chart and forecast articles). memory_size stays 1769. No IAM, no new S3 read path. Base 6wwEU3Sw+zFE66qfpFMXKL07e5QobD35LsRm2GsOZws= / VersionId 3eIFUS9kZLTBHPeHXkhsf_4OF8rE41Fc (round 68 ar-3 build); rollback is that VersionId through one code-only safe-apply
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 5.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 read back by the uploader and independently by head-object; CONTENT-DIFF against the DEPLOYED build exactly files 356 IDENTICAL 355 CHANGED 1 ADDED 0 REMOVED 0, the one being lib/research/api/scoped_amgt.py; size printed and under 262144000 B; plus MY OWN read-path scan over the diff per CTO round-67 ruling 4 (the halves declare NONE; measured 0 added S3-read lines over a 29-line diff with a positive control firing on 19 existing S3 lines, so no simulate arm is owed and no grant rides this act) |  | OPEN |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply at pin 863c62a855 | new CodeSha256 off 6wwEU3Sw + MemorySize still 1769, proven from a FULL show -json plan: exactly 1 non-no-op (the lambda, update), 0 destroy/create/replace, 0 non-no-op IAM, 0 non-no-op route/gateway; then a full 0-diff replan and the deployed sha re-read live |  | OPEN |
| L3 | verify | AC1 r69 c29 (95 names, 0 non-200, C1 and C2 PASS), AC2 r68 c27+c28, AC3 r67 c23+c24+c25+c26, all on deployed; plus the reported set r64 c9/c10 (30-day)/c11-c14, r65 c17, r66 c18/c19/c22, and r64 c15 cold on the day route | each verdict line with exit=0; rollback to VersionId 3eIFUS9kZLTBHPeHXkhsf_4OF8rE41Fc if c29 is not YES, any other check moves, c15 exceeds 5 s, a covered key returns non-200, or the ZZZZ_US_Equity control answers anything but 404 |  | OPEN |

## Log

- 20261005T043747Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
