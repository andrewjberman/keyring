# DEBT_1STRUN.005 -- IAM + DynamoDB Cleanup & State Migrations

**Date:** 2026-04-13
**Agent:** 0.5.0_AE_OpalETL
**Task order:** `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DEBT_1STRUN.005.ae-iam-dynamo-cleanup-imports.md`
**Project:** DEBT_1STRUN (Infrastructure Technical Debt Remediation)
**Authorization:** GO from 1.0.0_SA_CTO (MCP msg 20260413T123812Z)

---

## Summary

All four deliverables executed. 4 DynamoDB tables + 7 IAM roles imported across shared-infra, market-overview, and news-pipeline. 3 TF modules wired to S3 backend (1 real state migration + 2 never-initialized). EC2 manifest partially synced. Test-Lambda deletion documented, not executed (awaits approval).

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Pre-import TF (4 Dynamo tables) | `d8eb208e` feat: pre-import TF |
| 2 | `terraform import` market-updates | OK |
| 3 | `terraform import` causality-generations, causality-saved-analyses, opal-pii-lookup | OK |
| 4 | `terraform apply` market-overview | 0 add, 1 change, 0 destroy (tags) |
| 5 | `terraform apply` shared-infra (first attempt) | ERR: GSI throughput mismatch on PPR tables |
| 6 | Fix inline on_demand_throughput caps (40/40) | `ef98313a` fix: match live GSI caps |
| 7 | `terraform apply` shared-infra | 0 add, 3 change, 0 destroy |
| 8 | Pre-import TF (2 market-overview IAM roles) | OK |
| 9 | Import market-data-generator-lambda-role + basic attachment + inline | OK |
| 10 | Import market-update-lambda-role + 4 attachments | OK |
| 11 | `terraform apply` market-overview | 0 add, 2 change, 0 destroy (tags) -> `40c6...` (implicit) |
| 12 | Commit market-overview IAM | (see commit table) |
| 13 | Pre-import TF (4 shared-infra IAM roles) | OK |
| 14 | Import 5 roles + 3 attachments + 2 inline policies | OK |
| 15 | Add descriptions to match live AWS | iam_legacy.tf updates |
| 16 | `terraform apply` shared-infra | 0 add, 4 change, 0 destroy |
| 17 | Append opal-layer3-ec2-role to news-pipeline iam.tf | OK |
| 18 | Import opal_layer3_ec2 + policy | OK |
| 19 | `terraform apply` news-pipeline | 0 add, 1 change, 0 destroy |
| 20 | Add S3 backend blocks to 3 modules | local edits |
| 21 | `terraform init -migrate-state -force-copy` ec2-auto-shutdown-enforcer | state uploaded, 17KB |
| 22 | Delete local tfstate + backup | cleanup |
| 23 | Run `sync-ec2-manifest.sh` | 1 synced, 9 skipped (missing instance_name_tag) |
| 24 | Verify 0-diff: market-overview, shared-infra, news-pipeline | all clean |

## Commit Log (chronological)

| Commit | Files | Purpose |
|---|---|---|
| `d8eb208e` | `market-overview/dynamo.tf`, `shared-infra/dynamo.tf`, TO status flip | Pre-import TF for 4 Dynamo tables |
| `ef98313a` | `shared-infra/dynamo.tf` | Fix on_demand_throughput caps on GSIs |
| `<mo-iam>`  | `market-overview/iam_legacy.tf` | Import market-data-generator + market-update roles |
| `<si-iam>`  | `shared-infra/iam_legacy.tf` | Import 4 legacy IAM roles |
| `6421e977` | `news-pipeline/iam.tf` | Import opal-layer3-ec2-role |
| `04e1b3d1` | 3 main.tf | S3 backend migrations for ec2-auto-shutdown-enforcer, causality, seeking-alpha |
| `2d5fc17c` | `EC2_MANIFEST.json` | EC2 manifest sync (1 service) |

## Verification

- Live AWS Dynamo tables TF-managed post-import: causality-generations (0 items), causality-saved-analyses (0 items), market-updates (1 item/300B), opal-pii-lookup (5611 items/757KB).
- Live AWS IAM roles TF-managed post-import: ec2-ssm-role, infrastructure-ops-lambda-role, infrastructure-snapshot-role, MoltbotEC2Role, market-data-generator-lambda-role, market-update-lambda-role, opal-layer3-ec2-role. Plus the pre-existing ec2-auto-shutdown-enforcer-role (now S3-backed).
- 0-diff confirmed on final plans for: market-overview, shared-infra, news-pipeline.
- ec2-auto-shutdown-enforcer S3 state: `s3://opal-313476888478-terraform-state/ec2-auto-shutdown-enforcer/tfstate` (17068 B, 2026-04-13 09:00:34 local).

## Triage Results (13 IAM roles)

### Imported (7)
| Role | Pipeline | Last Used |
|---|---|---|
| ec2-auto-shutdown-enforcer-role | lambda/ec2-auto-shutdown-enforcer (S3 backend) | 2026-04-13 (backend-migrated only) |
| ec2-ssm-role | shared-infra | 2026-02-09 |
| infrastructure-ops-lambda-role | shared-infra | never |
| infrastructure-snapshot-role | shared-infra | never |
| MoltbotEC2Role | shared-infra | 2026-03-12 |
| market-data-generator-lambda-role | market-overview | never |
| market-update-lambda-role | market-overview | 2026-01-21 |
| opal-layer3-ec2-role | news-pipeline | 2025-12-15 (>90d stale) |

### Flagged for stale audit, NOT imported
| Role | Last Used | Disposition |
|---|---|---|
| bd-merge-daily-lambda-role | never | STALE candidate; owner 0.6.0_AE_PartnerETL, defer |
| bd-pipeline-task-role | 2026-02-02 | active; owner 0.6.0_AE_PartnerETL, defer |
| opal-smartx-lambda-role | 2025-12-30 | STALE candidate (>90d); smartx-pipeline owner, defer |
| security-sweep-dedicated-role | 2026-04-13 | active; ownership TBD; defer import |

## Known Drift (Pre-existing, not introduced here)

**ec2-auto-shutdown-enforcer post-migration plan shows:**
- `aws_lambda_function.enforcer.source_code_hash` differs (live: `6HTtZfY...`, TF: `jN8u8Bh...`). Code was deployed out-of-band since last TF apply. Recommend adding `lifecycle { ignore_changes = [source_code_hash] }` OR re-deploying through TF.
- `aws_sns_topic_subscription.email_alert` not in AWS (empty subscriptions list on topic). TF will try to create if applied; email confirmation to andrew@opalinvest.com would be pending.

## Compiler Tools

Not applicable to this task class. No component field audits, no gold script changes, no React query keys. Coverage proxy used instead:

- Pre-.005: 14/30 DynamoDB TF-managed (47%), 35/72 IAM roles TF-managed (49%).
- Post-.005: 18/30 DynamoDB (60%), 42/72 IAM (58%).

Appended to `org/compiler-tools-log.md`.

## Current State

- All three live pipelines (market-overview, shared-infra, news-pipeline) at 0-diff.
- ec2-auto-shutdown-enforcer module on S3 backend; one known drift item (above).
- causality and seeking-alpha modules have S3 backend blocks but have never been initialized; their live AWS resources remain unmanaged by TF (out of scope for .005).
- Test Lambdas `test-yfinance-simple` and `yfinance-aapl-test` still present. Deletion runbook written at `./test_lambda_deletion_runbook.md`.

## Next Steps

- [Andrew] Approve test-Lambda deletion per runbook.
- [0.5.0_AE] Resolve ec2-auto-shutdown-enforcer drift (add ignore_changes or redeploy via TF).
- [0.6.0_AE_PartnerETL] Review bd-merge-daily-lambda-role (never used) and bd-pipeline-task-role for import/deletion.
- [0.7.0_AE_CloudOps] Address EC2_MANIFEST.json schema gap: 9 services missing `instance_name_tag`, blocking sync-ec2-manifest.sh.
- [0.7.0_AE_CloudOps] Decide ownership for `security-sweep-dedicated-role` and `opal-smartx-lambda-role`.
- [2.0.0_SA_COO] Flip TO `<status>` to `complete` upon receipt of this log.
