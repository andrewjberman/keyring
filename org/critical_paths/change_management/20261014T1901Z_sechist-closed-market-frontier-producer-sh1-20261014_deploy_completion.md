# Deploy Completion Record
**Date opened:** 2026-10-14T19:01:59.399608+00:00
**Status:** OPEN
**Deploy:** MDPF_SECHIST closed-market frontier: etf-positioning-producer re-deploy at pin 87a0dcf14d (same 14 members, no IAM change)
**Authored by:** 0.7.0_AE_CloudOps~SH1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts etfs-positioning/etf-positioning-producer.zip + terraform infra/aws/terraform/etfs-positioning | new VersionId + content-sha256 head-object match + 14-member comparison (2 differ) + import smoke line + plan JSON code-change-only zero IAM + safe-apply + 0-diff re-plan |  | OPEN |
| L2 | verify | first scheduled run cron(0 13 * * ? *) 2026-10-15 13:00Z (ISSUER 2.0.0_SA_COO~H1) | run read against the dry run |  | OPEN |

## Log

- 20261014T190159Z OPENED by 0.7.0_AE_CloudOps~SH1 with 2 leg(s)

## ROLLBACK -- read LIVE 2026-10-14 before any change (TO-SH-t27 step 2); this is the rollback

Rollback is CODE only. NO IAM change in this act, so no policy leg.

| what | value | instrument |
|---|---|---|
| Lambda `CodeSha256` (prior) | `YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=` | `lambda get-function-configuration` |
| Lambda `LastModified` (prior) | 2026-10-09T20:08:21.000+0000 | same |
| handler / runtime / layers | `etf_positioning_gold.lambda_handler` / python3.11 / pandas-pyarrow-requests-layer:1 + opal-trading-calendar-layer:1 | same |
| env (prior) | OPAL_ETFS_PUBLISH_GRANT=1, ETFS_BUCKET=opal-data-etfs | same |
| artifact object (prior) | `s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip` | `s3api head-object` |
| artifact `VersionId` (prior) | `oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T` (LastModified 2026-10-09T20:01:56Z) | same |
| artifact `content-sha256` metadata (prior) | `YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=` | same |
| inline role policy (prior) | `s3-rw-etfs-gold-platinum` on `etf-positioning-producer-role`, 9 statements | `iam get-role-policy --query PolicyDocument` |
| prior `PolicyDocument` sha256 | `96a9dedfed250542b92620a964b95e59fc4e275b3b14f9183dbc81a72919194a` | sort-keys dump of the live inner document |

Procedure: copy the prior version back to the current version of the key with `content-sha256` metadata set to the prior value, then `safe-apply`; the module reads the object at plan time.
