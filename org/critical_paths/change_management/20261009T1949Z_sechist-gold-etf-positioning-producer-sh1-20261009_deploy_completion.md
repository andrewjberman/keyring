# Deploy Completion Record
**Date opened:** 2026-10-09T19:49:46.445628+00:00
**Status:** OPEN
**Deploy:** MDPF_SECHIST gold deploy: etf-positioning-producer at pin 09b6a7d580 (14 members) plus ONE IAM statement (history_gaps PutObject)
**Authored by:** 0.7.0_AE_CloudOps~SH1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts etfs-positioning/etf-positioning-producer.zip | new VersionId + content-sha256 metadata + 14-member BUILD_MANIFEST + import smoke output line |  | OPEN |
| L2 | verify | terraform infra/aws/terraform/etfs-positioning: code change + ONE added IAM statement | safe-apply output, plan summary showing the code change and exactly one added statement, 0-diff re-plan, new CodeSha256 |  | OPEN |
| L3 | verify | first scheduled gold run 2026-10-10 13:00Z (ISSUER 2.0.0_SA_COO~H1, not this seat) | gap record at record_address(as_of), no WRITE FAILED and no ImportError, served page diffed against the prior day |  | OPEN |

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

## Log

- 20261009T194946Z OPENED by 0.7.0_AE_CloudOps~SH1 with 3 leg(s)
