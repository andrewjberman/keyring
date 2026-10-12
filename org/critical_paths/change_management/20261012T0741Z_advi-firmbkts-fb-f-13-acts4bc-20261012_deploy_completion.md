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
| L1 | verify | step 0 and 1 reads: act 3 EQUAL, pair bytes and SIGNED, authority at both functions' ARNs, both functions' current version/CodeSha256/LastModified/env keys, artifact prior S3 VersionIds | the entry carries the read lines | act 3 compare EQUAL (FB-f-10 b913cc0f1f); pair COO dd143981f4 + CTO 6f5335f5c0 SIGNED 0 uncommitted; authority allowed at both functions' ARNs (UpdateFunctionCode, UpdateFunctionConfiguration, PublishVersion, GetFunctionConfiguration, InvokeFunction), control shared-advisor-router explicitDeny; before: exec-summary CodeSha256 71vki1gz..., partners CodeSha256 jbQNErp0..., env keys recorded, artifact bucket versioning Enabled, prior S3 VersionIds MaOXo36rclBdPR9bnKawP8UXnUdXLYhS and PrImfkXLOP1weeBmlOJRYwkCghMq0PhI | CLOSED 20261012T074459Z |
| L2 | s3-prefix | act 4b build: build-and-upload.sh exec-summary exec-summary-generator, artifact sha256 recorded in ACT4BC_EXPECT.json, r4_execeq.py --zip reads EXEC READS: legacy and canonical EQUAL | the artifact sha256 and the r4_execeq line | build-and-upload.sh exec-summary exec-summary-generator: write VERIFIED size 20195, artifact sha256 fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4= (S3 VersionId pOUiPH87zO8.FnEzSXQ7cW57HflaOdh9), recorded in ACT4BC_EXPECT.json; r4_execeq.py: EXEC READS: legacy and canonical EQUAL: advisors 194/194, leaderboards 2/2, artifacts 4/4 | CLOSED 20261012T074500Z |
| L3 | activation | act 4b: scoped plan of the exec-summary root (-var platinum_mode=canonical -target aws_lambda_function.exec_summary_generator) one function's code and ONE env key; .tools/safe-apply.sh on the saved plan | plan summary line, apply result, CodeSha256 equals the artifact, BD_PLATINUM_MODE=canonical, five base keys unchanged | scoped plan Plan: 0 to add, 1 to change, 0 to destroy (one function: s3_object_version, source_code_hash, last_modified, and ONE env key BD_PLATINUM_MODE=canonical added, five base keys unchanged); --dry-seat-gates CLEAR; safe-apply 07:43:38Z-07:44:15Z Apply complete! Resources: 0 added, 1 changed, 0 destroyed; read back CodeSha256 equals the artifact, BD_PLATINUM_MODE=canonical, six env keys, State Active; function NOT invoked | CLOSED 20261012T074500Z |
| L4 | s3-prefix | act 4c build: build-and-upload.sh partners-api opal-partners-data, artifact sha256 recorded; the partners API cache TTL READ and NAMED | artifact sha256 and the TTL |  | OPEN |
| L5 | verify | act 4c BEFORE sample: PARTNERS_BEFORE.json one record per invokable event (status and body sha256 only), the denominator of status-200 printed | record count and the denominator |  | OPEN |
| L6 | activation | act 4c: scoped plan of the partners-api root (-var platinum_mode=canonical -target module.opal_partners_data) one function's code and ONE env key; safe-apply on the saved plan | plan summary line, apply result, CodeSha256 equals the artifact, BD_PLATINUM_MODE=canonical |  | OPEN |
| L7 | verify | AC1 and AC2 deployed hash and mode, the AFTER sample PARTNERS_AFTER.json, AC3 r4_sample_eq.py SAMPLE EQUAL N of N | the three outputs quoted |  | OPEN |
| L8 | git | proof instance written and TO-FB-f-13 status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T074122Z OPENED by 0.7.0_AE_CloudOps~FB1 with 8 leg(s)
- 20261012T074459Z LEG L1 closed: act 3 compare EQUAL (FB-f-10 b913cc0f1f); pair COO dd143981f4 + CTO 6f5335f5c0 SIGNED 0 uncommitted; authority allowed a
- 20261012T074500Z LEG L2 closed: build-and-upload.sh exec-summary exec-summary-generator: write VERIFIED size 20195, artifact sha256 fdPwodukz88dtRfm0bGw
- 20261012T074500Z LEG L3 closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (one function: s3_object_version, source_code_hash, last_modified,

## ACT 4B -- exec-summary-generator (0.7.0_AE_CloudOps~FB1, 2026-10-12T07:44:59Z; GO AMENDMENT 3 @d2715c3e9e)

- **Pair:** act 4b/4c COO half (amended, `dd143981f4`) and CTO half (`6f5335f5c0`), SIGNED at the current bytes, 0 uncommitted. Order of the window:
  act 3 compare EQUAL (`FB-f-10` @b913cc0f1f), acts 3c (`FB-f-17`) and 3b (`FB-f-14`) applied, `FB-f-18` applied: all read at HEAD.
- **Authority at the functions' own ARNs (simulated on this identity, one resource per call, plain and `:*`):** UpdateFunctionCode,
  UpdateFunctionConfiguration, PublishVersion, GetFunctionConfiguration, InvokeFunction `allowed` for `exec-summary-generator` and
  `opal-partners-data`; control `shared-advisor-router` UpdateFunctionCode `explicitDeny`. Neither function is on the protected list.
- **Before (read 07:3xZ):** `exec-summary-generator`: CodeSha256 `71vki1gzHKsOG+/zApgt2qYjsa7Qv0qlQ3w3ExGkhjI=`, LastModified 2026-04-27T13:14:20Z,
  python3.12, layer `anthropic-sdk-deps:1`, env keys ANTHROPIC_SECRET_NAME, DATA_BUCKET, LOG_LEVEL, MAX_ADVISORS_HARD_CAP, MODEL, no numbered
  published version. Prior artifact: S3 `exec-summary/exec-summary-generator.zip` VersionId `MaOXo36rclBdPR9bnKawP8UXnUdXLYhS` (17,676 bytes).
- **Build:** `build-and-upload.sh exec-summary exec-summary-generator`: import-closure OK (10 packaged .py files), write VERIFIED
  (size 20,195, sha256 metadata match), **artifact sha256 `fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4=`**, new S3 VersionId
  `pOUiPH87zO8.FnEzSXQ7cW57HflaOdh9`; recorded in `ACT4BC_EXPECT.json`.
- **The read BEFORE the value:** `EXEC READS: legacy and canonical EQUAL: advisors 194/194, leaderboards 2/2, artifacts 4/4`.
- **Plan (scoped, saved):** `-var platinum_mode=canonical -target=aws_lambda_function.exec_summary_generator`:
  `Plan: 0 to add, 1 to change, 0 to destroy`; attributes that differ: `s3_object_version`, `source_code_hash`, `last_modified` (known after
  apply) and the environment, where exactly ONE key is added, `BD_PLATINUM_MODE=canonical`; the five base keys unchanged; layers and
  architecture unchanged. `evidence/act4bc/4b_plan_check.txt`.
- **Seat gates:** `--dry-seat-gates` first: CLEAR (open_call, overlap, upset, open_deploy all clear).
- **Apply:** 07:43:38Z to 07:44:15Z, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
- **Read back (07:44Z):** CodeSha256 `fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4=` EQUAL to the artifact; env keys now the five base keys plus
  `BD_PLATINUM_MODE`; `BD_PLATINUM_MODE=canonical`; State Active, LastUpdateStatus Successful; layer `anthropic-sdk-deps:1` unchanged.
- **Not done, as ordered:** the function was NOT invoked (its handler runs every advisor and uploads); its put is read at its next scheduled
  run, 04:30Z on 2026-10-13 (runbook step 9).
- **Rollback (4b), unused:** re-put S3 object `exec-summary/exec-summary-generator.zip` VersionId `MaOXo36rclBdPR9bnKawP8UXnUdXLYhS` as the
  key's latest version (`aws s3api copy-object --copy-source ...?versionId=`), then a plan WITHOUT `-var platinum_mode` and `safe-apply` of it.
