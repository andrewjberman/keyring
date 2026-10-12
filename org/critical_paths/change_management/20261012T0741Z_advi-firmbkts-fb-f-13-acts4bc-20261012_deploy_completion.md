# Deploy Completion Record
**Date opened:** 2026-10-12T07:41:22.850287+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-13 (acts 4b then 4c, GO AMENDMENT 3 @d2715c3e9e): one code version and ONE environment value BD_PLATINUM_MODE=canonical each for exec-summary-generator (root infra/aws/terraform/exec-summary) and opal-partners-data (root infra/aws/terraform/partners-api); prior: exec-summary-generator CodeSha256 71vki1gzHKsOG+/zApgt2qYjsa7Qv0qlQ3w3ExGkhjI= (S3 exec-summary/exec-summary-generator.zip VersionId MaOXo36rclBdPR9bnKawP8UXnUdXLYhS, LastModified 2026-04-27T13:14:20Z, env keys ANTHROPIC_SECRET_NAME DATA_BUCKET LOG_LEVEL MAX_ADVISORS_HARD_CAP MODEL), opal-partners-data CodeSha256 jbQNErp0T8bOz6OJ7dttxQaaO0Hggkqp4runyM3wyrE= (S3 partners-api/opal-partners-data.zip VersionId PrImfkXLOP1weeBmlOJRYwkCghMq0PhI, LastModified 2026-06-03T17:08:36Z, env key USERS_TABLE); neither function has a numbered published version, so the rollback is the prior S3 object version re-put as the key's latest and a plan WITHOUT -var platinum_mode; pair COO half @dd143981f4 (amended) + CTO half @6f5335f5c0; the exec-summary function is NOT invoked (its 04:30Z run is the next day's read)
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 and 1 reads: act 3 EQUAL, pair bytes and SIGNED, authority at both functions' ARNs, both functions' current version/CodeSha256/LastModified/env keys, artifact prior S3 VersionIds | the entry carries the read lines |  | OPEN |
| L2 | s3-prefix | act 4b build: build-and-upload.sh exec-summary exec-summary-generator, artifact sha256 recorded in ACT4BC_EXPECT.json, r4_execeq.py --zip reads EXEC READS: legacy and canonical EQUAL | the artifact sha256 and the r4_execeq line |  | OPEN |
| L3 | activation | act 4b: scoped plan of the exec-summary root (-var platinum_mode=canonical -target aws_lambda_function.exec_summary_generator) one function's code and ONE env key; .tools/safe-apply.sh on the saved plan | plan summary line, apply result, CodeSha256 equals the artifact, BD_PLATINUM_MODE=canonical, five base keys unchanged |  | OPEN |
| L4 | s3-prefix | act 4c build: build-and-upload.sh partners-api opal-partners-data, artifact sha256 recorded; the partners API cache TTL READ and NAMED | artifact sha256 and the TTL |  | OPEN |
| L5 | verify | act 4c BEFORE sample: PARTNERS_BEFORE.json one record per invokable event (status and body sha256 only), the denominator of status-200 printed | record count and the denominator |  | OPEN |
| L6 | activation | act 4c: scoped plan of the partners-api root (-var platinum_mode=canonical -target module.opal_partners_data) one function's code and ONE env key; safe-apply on the saved plan | plan summary line, apply result, CodeSha256 equals the artifact, BD_PLATINUM_MODE=canonical |  | OPEN |
| L7 | verify | AC1 and AC2 deployed hash and mode, the AFTER sample PARTNERS_AFTER.json, AC3 r4_sample_eq.py SAMPLE EQUAL N of N | the three outputs quoted |  | OPEN |
| L8 | git | proof instance written and TO-FB-f-13 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T074122Z OPENED by 0.7.0_AE_CloudOps~FB1 with 8 leg(s)
