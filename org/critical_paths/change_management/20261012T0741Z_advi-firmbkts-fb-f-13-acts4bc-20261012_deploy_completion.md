# Deploy Completion Record
**Date opened:** 2026-10-12T07:41:22.850287+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T075624Z
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
| L4 | s3-prefix | act 4c build: build-and-upload.sh partners-api opal-partners-data, artifact sha256 recorded; the partners API cache TTL READ and NAMED | artifact sha256 and the TTL | build-and-upload.sh partners-api opal-partners-data: write VERIFIED size 35752, artifact sha256 c9FXD84szSBD5oSukUi8sCA6szY/LYiHpRYBWXnOBv4= (S3 VersionId H9jSq8eGXSaQAfXZKgqizrSvFjd5u_A3) in ACT4BC_EXPECT.json; TTL read and named: CloudFront Managed-CachingDisabled min/default/max 0 on /api/scoped/partners/* and /api/partners, API Gateway stage cacheClusterEnabled False, no method caching: effective TTL none | CLOSED 20261012T075624Z |
| L5 | verify | act 4c BEFORE sample: PARTNERS_BEFORE.json one record per invokable event (status and body sha256 only), the denominator of status-200 printed | record count and the denominator | BEFORE sample at the unchanged function (CodeSha256 jbQNErp0...): 8 records PARTNERS_BEFORE.json (status and body sha256 only), 7 of 8 events read status 200, 0 5xx, statuses 200 and 404; gold/entities/clients/ reads 404 with a real id (named) | CLOSED 20261012T075624Z |
| L6 | activation | act 4c: scoped plan of the partners-api root (-var platinum_mode=canonical -target module.opal_partners_data) one function's code and ONE env key; safe-apply on the saved plan | plan summary line, apply result, CodeSha256 equals the artifact, BD_PLATINUM_MODE=canonical | scoped plan Plan: 0 to add, 1 to change, 0 to destroy (one function: code and ONE env key BD_PLATINUM_MODE=canonical, USERS_TABLE unchanged); --dry-seat-gates CLEAR; safe-apply 07:48:53Z-07:49:29Z Apply complete! Resources: 0 added, 1 changed, 0 destroyed; read back CodeSha256 equals the artifact, mode canonical, State Active; DynamoDB s3Bucket item untouched | CLOSED 20261012T075624Z |
| L7 | verify | AC1 and AC2 deployed hash and mode, the AFTER sample PARTNERS_AFTER.json, AC3 r4_sample_eq.py SAMPLE EQUAL N of N | the three outputs quoted | AC1 fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4= canonical PASS; AC2 c9FXD84szSBD5oSukUi8sCA6szY/LYiHpRYBWXnOBv4= canonical PASS; AC3 AS PRINTED: SAMPLE EQUAL: 7 of 8 cases, exit=1 (platinum/clients/ compressed body hash differs by the gzip header timestamp); by CONTENT equal: decompressed sha256 67ac42f423e34b66 in the prior artifact legacy, the new artifact legacy and canonical, and the live function (row ADVI_FIRMBKTS-D1-S36); Branch B not triggered, no rollback; the order's status is the issuer's to rule | CLOSED 20261012T075624Z |
| L8 | git | proof instance written and TO-FB-f-13 status flipped complete in one commit | commit hash | proof instance and sample records committed with this entry; TO-FB-f-13 status NOT flipped to complete (AC3 literal FAIL, the instrument); commit hash is this commit | CLOSED 20261012T075624Z |

## Log

- 20261012T074122Z OPENED by 0.7.0_AE_CloudOps~FB1 with 8 leg(s)
- 20261012T074459Z LEG L1 closed: act 3 compare EQUAL (FB-f-10 b913cc0f1f); pair COO dd143981f4 + CTO 6f5335f5c0 SIGNED 0 uncommitted; authority allowed a
- 20261012T074500Z LEG L2 closed: build-and-upload.sh exec-summary exec-summary-generator: write VERIFIED size 20195, artifact sha256 fdPwodukz88dtRfm0bGw
- 20261012T074500Z LEG L3 closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (one function: s3_object_version, source_code_hash, last_modified,
- 20261012T075624Z LEG L4 closed: build-and-upload.sh partners-api opal-partners-data: write VERIFIED size 35752, artifact sha256 c9FXD84szSBD5oSukUi8sCA6
- 20261012T075624Z LEG L5 closed: BEFORE sample at the unchanged function (CodeSha256 jbQNErp0...): 8 records PARTNERS_BEFORE.json (status and body sha256
- 20261012T075624Z LEG L6 closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (one function: code and ONE env key BD_PLATINUM_MODE=canonical, US
- 20261012T075624Z LEG L7 closed: AC1 fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4= canonical PASS; AC2 c9FXD84szSBD5oSukUi8sCA6szY/LYiHpRYBWXnOBv4= canoni
- 20261012T075624Z LEG L8 closed: proof instance and sample records committed with this entry; TO-FB-f-13 status NOT flipped to complete (AC3 literal FAIL
- 20261012T075624Z CLOSED -- all 8 legs proven

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

## ACT 4C -- opal-partners-data (0.7.0_AE_CloudOps~FB1, 2026-10-12T07:56:23Z)

- **Build:** `build-and-upload.sh partners-api opal-partners-data`: write VERIFIED (size 35,752), **artifact sha256
  `c9FXD84szSBD5oSukUi8sCA6szY/LYiHpRYBWXnOBv4=`**, new S3 VersionId `H9jSq8eGXSaQAfXZKgqizrSvFjd5u_A3`; recorded in `ACT4BC_EXPECT.json`.
  **Before:** CodeSha256 `jbQNErp0T8bOz6OJ7dttxQaaO0Hggkqp4runyM3wyrE=`, LastModified 2026-06-03T17:08:36Z, env key USERS_TABLE only, no numbered
  published version; prior artifact S3 `partners-api/opal-partners-data.zip` VersionId `PrImfkXLOP1weeBmlOJRYwkCghMq0PhI` (32,911 bytes).
- **The cache TTL, READ AND NAMED (the CTO's condition 3):** both partners paths of the portal distribution, `/api/scoped/partners/*` and
  `/api/partners`, use CloudFront cache policy `4135ea2d-6df8-44a3-9df3-4b5a84be39ad` = `Managed-CachingDisabled`, MinTTL 0, DefaultTTL 0, MaxTTL 0; the
  origin is API Gateway `7k3ed8px20` stage `$default`: `cacheClusterEnabled=False`, 0 method settings with caching; the partners root declares no cache.
  Effective TTL of a cached partners response: **none (0 s)**; no invalidation was added and none is needed.
- **BEFORE sample (step 9):** 8 events of the census, one per served class, at the CURRENT version (before the apply): **7 of 8 read status 200**,
  0 5xx, statuses {200, 404}. The five entity-keyed events carried placeholder ids; each was replaced by one real id taken from the first key of its
  class prefix (a `list-objects-v2` MaxKeys 1; the id is neither printed nor written). **Named: class `gold/entities/clients/` (relationship timeseries)
  reads 404 both before and after even with a real id.** Records: `PARTNERS_BEFORE.json` (status and body sha256 only).
- **Plan (scoped, saved):** `-var platinum_mode=canonical -target=module.opal_partners_data`: `Plan: 0 to add, 1 to change, 0 to destroy`; one
  function; `s3_object_version`, `source_code_hash`, `last_modified` and the environment where exactly ONE key is added,
  `BD_PLATINUM_MODE=canonical`, `USERS_TABLE` unchanged; the DynamoDB `s3Bucket` item untouched. `--dry-seat-gates` CLEAR.
- **Apply:** 07:48:53Z to 07:49:29Z, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` Read back: CodeSha256 equals the artifact,
  `BD_PLATINUM_MODE=canonical`, 2 env keys, State Active.
- **AFTER sample and AC3 (07:49:52Z):** 7 of 8 read 200, 0 5xx. `r4_sample_eq.py`: `SAMPLE EQUAL: 7 of 8 cases`, `exit=1`; the one `DIFFERENT` is
  `platinum/clients/` (status 200 to 200, body hash changed). **Investigated before any decision**: the response is base64 gzip and its header carries a
  timestamp; the compressed hash differs on every invocation of the SAME version (3 distinct in 4, 5 in 8) while the decompressed content is identical
  (1 distinct in 6, 4,931,112 bytes); a local read-only replay of the PRIOR artifact in legacy mode, the new artifact in legacy and in canonical mode, and the
  live function all give content sha256 `67ac42f423e34b66...`. By content the diff is EMPTY: the pair's Branch B condition (a changed body for a key not
  written after the move) does not hold; no rollback. `evidence/act4bc/4c_platinum_clients_content_replay.txt`; row `ADVI_FIRMBKTS-D1-S36`.
- **AC1** `fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4=` + `canonical` PASS; **AC2** `c9FXD84szSBD5oSukUi8sCA6szY/LYiHpRYBWXnOBv4=` + `canonical` PASS;
  **AC3 literal FAIL** (7 of 8, exit=1) by the instrument, content-equal. The order's status is NOT flipped by this lane.
- **Rollback (4c), unused:** re-put S3 object `partners-api/opal-partners-data.zip` VersionId `PrImfkXLOP1weeBmlOJRYwkCghMq0PhI` as the key's latest
  version, then a plan WITHOUT `-var platinum_mode` and `safe-apply` of it.
- **Not done, as ordered:** `exec-summary-generator` not invoked; no delete; no other function, role or route; the DynamoDB `s3Bucket` item untouched.


## AMENDMENT 4 FOLLOW-UP (0.7.0_AE_CloudOps~FB1, 2026-10-12T08:00:11Z)

- The issuer ruled row `ADVI_FIRMBKTS-D1-S36` (msg 4309, commit `0c1879d253`): `platinum/clients/` reads EQUAL on its decompressed content.
- Added `content_sha256` `67ac42f423e34b66fc0a2e9eac9ebb0675e2b6c3d891e03652dbfb06285afa3c` (4,931,112 bytes) with `content_claim` to that case's record in `PARTNERS_BEFORE.json`
  (`replayed-prior-artifact`) and `PARTNERS_AFTER.json` (`live-function-read`); no other record changed, no re-take, no rollback.
- AC3 re-run from the amended tool: `SAMPLE EQUAL: 8 of 8 cases`, `exit=0`. The order's `<status>` flips to `complete` in the commit that carries this
  note. Evidence: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4bc/4c_ac3_amended.txt`
  (the earlier note's `evidence/act4bc/` prefix names this same `act4bc/` folder).


## NOTE 2026-10-13 (0.7.0_AE_CloudOps~FB1; COO msg 4639, row ADVI_FIRMBKTS-D1-S40)

- **Act 4b is labelled NOT EXERCISED; read path graded by `r4_execeq`.** The exec-summary generator did not run at 04:30Z or at all: its only trigger
  is EventBridge `exec-summary-trigger` (chain-complete from `bd-pipeline.gold-chain`), whose event has failed to emit on every gold chain close in
  the run log since at least 2026-04-25; the function's newest log stream is 2026-05-04 and the 04:50Z read of 2026-10-13 found 0 invocations,
  158 `exec_summary.json` objects at each home and 0 written since 04:25Z. Not caused by the cutover.
- The COO ruled: do NOT invoke the generator (it would rewrite 158 client-facing summaries outside the signed 4b pair); the CTO decides who fixes
  the put-events fault and whether one manual invocation is authorised. Evidence: `act4bc_followup/` under this seat's deliverables folder.
