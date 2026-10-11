# Deploy Completion Record
**Date opened:** 2026-10-09T19:49:46.445628+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T022430Z -- gate: external / L3 = the first scheduled etf-positioning-producer run, cron(0 13 * * ? *) = 2026-10-10 13:00Z, read and graded by the issuer 2.0.0_SA_COO~H1 per TO step 6; this seat owes nothing further (held since 2026-10-09T20:22:48.874043+00:00)
**Deploy:** MDPF_SECHIST gold deploy: etf-positioning-producer at pin 09b6a7d580 (14 members) plus ONE IAM statement (history_gaps PutObject)
**Authored by:** 0.7.0_AE_CloudOps~SH1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts etfs-positioning/etf-positioning-producer.zip | new VersionId + content-sha256 metadata + 14-member BUILD_MANIFEST + import smoke output line | VERIFIED head-object on s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip: ContentLength=676850 AND Metadata.content-sha256=YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM= both matched the locally computed values (rc=0 from the cp was not accepted as evidence; this is the build-and-upload.sh:634 silent-no-op gate). New VersionId oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T, prior 7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii. 14 members from pin 09b6a7d580, zip sha256 60461dcc865dd8a429dcd9e08c9e5a9eff117d372c07c32a1b6d7246f08a5613, in-zip BUILD_MANIFEST copied to evidence/gold_build_manifest_20261009.json. PRE-APPLY IMPORT SMOKE PASSED: record_address('2026-10-12') printed s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json with only the package and published layer v1 on the path, module origins confirming package-not-repo resolution; negative control at 3 members re-run here gave ModuleNotFoundError, so the gate discriminates. Evidence evidence/gold_import_smoke_20261009.txt. Builder edit committed d49af8a50b. | CLOSED 20261009T202208Z |
| L2 | verify | terraform infra/aws/terraform/etfs-positioning: code change + ONE added IAM statement | safe-apply output, plan summary showing the code change and exactly one added statement, 0-diff re-plan, new CodeSha256 | safe-apply of the SAVED plan (so what was graded is what landed): Apply complete, 0 added, 2 changed, 0 destroyed. Seat gates APPLY-WHO verdict=ADMITTED, CROSSBOX-DEPLOY verdict=CLEAR; comp-tagauthz PASSED (0 candidates overwrite an access-granting tag); tombstone-gate CLEAN; naming gate WARN-only on 6 pre-existing names, 0 REFUSED, no new resource. No HALTGT pass is cited -- the checkpoint cannot halt a ~lane seat. AC2 GRADED FROM THE PLAN JSON, not the collapsed text: IAM 8 -> 9 statements with exactly 1 ADDED (Stage1WriteHistoryGaps, s3:PutObject on arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*), 0 removed, 8 of 8 prior statements carried byte-identical; the Lambda's 46 attributes compared and exactly 3 differ (s3_object_version, source_code_hash, last_modified) with no env/memory/timeout/layer/role/handler/schedule change; 9 resource_changes, 7 no-op. STOP condition not met. LIVE AFTER APPLY: CodeSha256=YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM= (equals the built+verified artifact), LastModified 2026-10-09T20:08:21Z, get-role-policy returns 9 statements with the new Sid and exact ARN, IAM denominator unchanged at 1 inline + 1 attached. 0-DIFF RE-PLAN: terraform plan -detailed-exitcode exit 0. Evidence evidence/gold_plan_20261009.txt; commit d49af8a50b. NOT PROVEN BY THIS SEAT: the grant is APPLIED, not EXERCISED -- iam:SimulatePrincipalPolicy is denied to cloudops-dell1-agent-user (row MDPF_SECHIST-D1-S3 @d875f1c0be, positive control run beside it); the exercise is L3. | CLOSED 20261009T202227Z |
| L3 | verify | first scheduled gold run 2026-10-10 13:00Z (ISSUER 2.0.0_SA_COO~H1, not this seat) | gap record at record_address(as_of), no WRITE FAILED and no ImportError, served page diffed against the prior day | GOLD-L3-OK as_of=2026-10-09 read by 2.0.0_SA_COO~H1 2026-10-11T02:2xZ against the scheduled run 2026-10-10 13:00Z: served positioning_data.json LastModified 2026-10-10T13:01:40Z; gap record exists at s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-09/gap_record.json and the log line 'WROTE gap record' names it (R1 PutObject grant EXERCISED); 36 log lines 12:55-13:40Z, 0 ImportError/WRITE FAILED/Traceback; diff vs prior: weight>1 0, industry_group changed 0, 188 of 188 keys common, 2 prior keys (IDVZ KCDMY, UNVGY) absent because bronze characteristics for 2026-10-09 never carried them. Record org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/L3_GOLD/L3_READ_20261010_RESULT.md | CLOSED 20261011T022420Z |

## Log

- 20261009T194946Z OPENED by 0.7.0_AE_CloudOps~SH1 with 3 leg(s)
- 20261009T202208Z LEG L1 closed: VERIFIED head-object on s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip: ContentLe
- 20261009T202227Z LEG L2 closed: safe-apply of the SAVED plan (so what was graded is what landed): Apply complete, 0 added, 2 changed, 0 destroyed. Seat 
- 20261009T202248Z HELD-SOVEREIGN-GATED gate=external/L3 = the first scheduled etf-positioning-producer run, cron(0 13 * * ? *) = 2026
- 20261011T022420Z LEG L3 closed: GOLD-L3-OK as_of=2026-10-09 read by 2.0.0_SA_COO~H1 2026-10-11T02:2xZ against the scheduled run 2026-10-10 13:00Z: serve
- 20261011T022430Z CLOSED -- all 3 legs proven

## ROLLBACK -- read LIVE before any change (TO step 1); this is the rollback

Rollback is CODE plus POLICY only. NO S3 delete of `history_gaps/` objects:
CTO half condition 1 supersedes the COO half's delete line -- the pre-pin code has no
reader of that prefix, so after a rollback those objects are inert and are left.

| what | value | instrument |
|---|---|---|
| Lambda `CodeSha256` (prior) | `qQk9ohLihOInJnvj/NncAms1IuoEIkkjRwpb8EIFouQ=` | `lambda get-function-configuration` |
| Lambda `LastModified` (prior) | 2026-08-28T18:49:14.000+0000 | same |
| artifact object (prior) | `s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip` | `s3api head-object` |
| artifact `VersionId` (prior) | `7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii` | same -- the bucket is versioned; this is the handle that restores the bytes |
| artifact bytes / ETag (prior) | 162733 B / `26c1fab1c30ab90038a8ec1796e47561` | same |
| artifact `content-sha256` metadata (prior) | `qQk9ohLihOInJnvj/NncAms1IuoEIkkjRwpb8EIFouQ=` | same -- equals the live `CodeSha256`, so code and artifact agree at open |
| inline role policy (prior) | `s3-rw-etfs-gold-platinum` on `etf-positioning-producer-role`, 8 statements | `iam get-role-policy` |
| prior `PolicyDocument` sha256 | `7b6c32036b616dae23914a0392392ebac8b9fb6ba0295356d2a58490afe9909c` | normalized sort-keys dump of the live document |
| prior statement Sids (8) | Stage1ReadInputs, Stage1ListBackfill, Stage1WriteGold, Stage2ReadGold, Stage2ServePlatinum, ListEtfsBucket, ListPlatinumEtfs, Stage2ReadEtfClassifications | same |
| IAM denominator at open | 1 inline policy, 1 attached managed (AWSLambdaBasicExecutionRole) | `list-role-policies` + `list-attached-role-policies` |

Rollback procedure, both legs, runnable in one hour:
1. CODE: restore the prior artifact bytes to the current version of the key (copy from
   `VersionId=7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii` with `content-sha256` metadata set to the
   prior value), then `safe-apply` -- the module reads `data.aws_s3_object` at plan time, so
   the prior `CodeSha256` returns without `update-function-code`.
2. POLICY: revert the one added statement in `producer-lambda.tf` and `safe-apply`.
