# Deploy Completion Record
**Date opened:** 2026-10-14T19:01:59.399608+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / L2 = the first scheduled etf-positioning-producer run, cron(0 13 * * ? *) = 2026-10-15 13:00Z, read and graded by the issuer 2.0.0_SA_COO~H1 per TO-SH-t27 step 6; this seat owes nothing further (held since 2026-10-14T19:14:08.159150+00:00)
**Deploy:** MDPF_SECHIST closed-market frontier: etf-positioning-producer re-deploy at pin 87a0dcf14d (same 14 members, no IAM change)
**Authored by:** 0.7.0_AE_CloudOps~SH1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts etfs-positioning/etf-positioning-producer.zip + terraform infra/aws/terraform/etfs-positioning | new VersionId + content-sha256 head-object match + 14-member comparison (2 differ) + import smoke line + plan JSON code-change-only zero IAM + safe-apply + 0-diff re-plan | VERIFIED head-object on s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip: ContentLength=680674 AND Metadata.content-sha256=M6X6eJ3QCDXopGif5PvlrlqBS/ynXHOpuxWDUIGFbAQ= matched the locally computed values; new VersionId ButacRtDI8gfK1Ilv0GNZCcgkJZ6HpHq, prior oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T. Built at pin 11dc6a2161 (COO ruling b after the 87a0dcf14d STOP, msg 5752): 14 members, member comparison 12 identical, exactly etf_positioning_gold.py and etf_positioning_publisher.py differ plus in-zip BUILD_MANIFEST (evidence/frontier_member_comparison_20261014.txt). PRE-APPLY IMPORT SMOKE PASSED: printed 'frontier_returns s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json'; negative control on the live package gives AttributeError (evidence/frontier_import_smoke_20261014.txt). safe-apply of the SAVED plan: Apply complete, 0 added, 1 changed, 0 destroyed; plan JSON graded: 9 resource_changes, 8 no-op, Lambda 46 attributes with exactly s3_object_version, source_code_hash, last_modified differing, ZERO IAM change (evidence/frontier_plan_20261014.txt). LIVE AFTER APPLY: CodeSha256=M6X6eJ3QCDXopGif5PvlrlqBS/ynXHOpuxWDUIGFbAQ= (equals the built+verified artifact), LastModified 2026-10-14T19:13:06Z, Active/Successful, handler/layers/env unchanged, role policy 9 statements sha256 96a9dedf...194a unchanged. 0-DIFF RE-PLAN: terraform plan -detailed-exitcode exit 0. NOT PROVEN BY THIS SEAT: the gold parquet write of the new column and the publisher stage (L2). | CLOSED 20261014T191407Z |
| L2 | verify | first scheduled run cron(0 13 * * ? *) 2026-10-15 13:00Z (ISSUER 2.0.0_SA_COO~H1) | run read against the dry run |  | OPEN |

## Log

- 20261014T190159Z OPENED by 0.7.0_AE_CloudOps~SH1 with 2 leg(s)
- 20261014T191407Z LEG L1 closed: VERIFIED head-object on s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip: ContentLe
- 20261014T191408Z HELD-SOVEREIGN-GATED gate=external/L2 = the first scheduled etf-positioning-producer run, cron(0 13 * * ? *) = 2026

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
