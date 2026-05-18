# 0.5.0_AE_OpalETL Session Log -- 2026-05-18 (TRSB_LEDGER.006 DynamoDB durability)

**Agent:** 0.5.0_AE_OpalETL
**Date:** 2026-05-18
**Branch:** CLOUD
**TO:** TRSB_LEDGER.006.ae-dynamodb-durability (2.0.0_SA_COO~B)
**Headline:** Added point-in-time recovery + deletion protection to the trade system-of-record DynamoDB tables. Deployed `trade-pipeline-v1.9.0`, 0-diff verified, PITR ENABLED on both tables confirmed via the AWS API.

---

## TRSB_LEDGER.006 -- DynamoDB durability (PRD hole B8)

Pillar C / P1. `aws_dynamodb_table.trade_submissions` and `trade_users` had neither PITR nor deletion protection -- table-stakes for a record-keeping system Andrew called "crucial."

### Cross-domain coordination

`infra/aws/terraform/trade-pipeline/dynamodb.tf` is shared with TRSB_LEDGER.005 (AE 0.7.0, by-approver GSI repoint). MCP'd 0.7.0 pre-edit: they confirmed NOT editing dynamodb.tf (on TRSB_LEDGER.000, TO-5 several sequential TOs away), no uncommitted changes, no objection to TO-6-first. Landed TO-6 first per COO~B's cross_domain recommendation; 0.7.0 will rebase the TO-5 GSI stanza on top. Pinged 0.7.0 on landing.

### Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Phase 1 -- read dynamodb.tf | Confirmed neither table declared `point_in_time_recovery` or `deletion_protection_enabled` |
| 2 | Edit dynamodb.tf | +12 lines: `point_in_time_recovery { enabled = true }` + `deletion_protection_enabled = true` on both tables |
| 3 | Commit source (Rule 2, commit before apply) | `05f91fef0` feat(trade-pipeline): DynamoDB durability |
| 4 | terraform plan | `0 to add, 2 to change, 0 to destroy` -- durability attrs only, no GSI/key-schema delta |
| 5 | terraform apply | `0 added, 2 changed, 0 destroyed` |
| 6 | 0-diff plan | `No changes. Your infrastructure matches the configuration.` |
| 7 | Tag | `trade-pipeline-v1.9.0` -> `05f91fef0` (annotated) |
| 8 | Push --follow-tags | (see push) |

### Verification (AWS API)

| Table | PITR (describe-continuous-backups) | deletion_protection (describe-table) |
|-------|-----|-----|
| trade-users | ENABLED | True |
| opal-trade-submissions | ENABLED | True |

### Note -- attribute-already-present (TO Phase-1 `<if_mismatch>`)

`trade-users` PITR was ALREADY ENABLED in AWS pre-deploy (verified `describe-continuous-backups` before the apply -- trade-users ENABLED, opal-trade-submissions DISABLED). So the `point_in_time_recovery` block I added to `trade_users` in the .tf converged the configuration-as-code to the existing AWS state -- a no-op for that one attribute. The terraform plan therefore showed **3 effective changes**, not 4:
  1. trade_submissions PITR false -> true
  2. trade_submissions deletion_protection false -> true
  3. trade_users deletion_protection false -> true
  (trade_users PITR: already enabled in AWS -> .tf declaration is a no-op convergence)
AC1 (both tables DECLARE all 4 attributes in the .tf) is fully satisfied -- durability is now codified for both tables. AC2's intent (plan isolated to durability attrs, no GSI/key-schema/other-resource delta) is satisfied -- the "4 vs 3" is purely the pre-existing trade-users PITR state, not a collision or an unexpected delta.

### Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| trade-pipeline | `trade-pipeline-v1.9.0` | `05f91fef0` |

### Notes / decisions

- `record-terraform-deploy.sh` NOT run: the TO Phase-3 step list explicitly omits it (`commit -> plan -> apply -> 0-diff -> tag -> push`); this is a non-Lambda table-config change with no source-map impact, and trade-pipeline's CHANGELOG cadence has not used record-deploy historically (last entry v1.3.0).
- `pipeline_inventory.xml` NOT updated -- trade-pipeline is not an OpalETL-owned pipeline; this was a cross-lane TO.
- `MSYS_NO_PATHCONV=1` (required for `terraform.exe -chdir=`) mangles the `aws` CLI path -- ran the AWS verification calls in a separate shell without it.

## Compiler Tools

| Tool / mandate run | Result |
|--------------------|--------|
| Direct read `dynamodb.tf` (Phase-1 mandate) | Neither table declared PITR / deletion_protection -- TO scope confirmed. comp-* N/A (trade pipeline uninstrumented, PRD section 5). |
| `terraform.exe plan` (Phase-2 mandate) | `0 add, 2 change, 0 destroy` -- durability attrs only; no GSI delta. STOP-condition not triggered. |
| `aws dynamodb describe-continuous-backups` (Phase-3 mandate) | PointInTimeRecoveryStatus ENABLED for both tables post-apply. |

## Current State

- TRSB_LEDGER.006 COMPLETE -- `trade-pipeline-v1.9.0` deployed, 0-diff, PITR + deletion protection live on both trade tables.
- Pipeline tags: trade-pipeline-v1.9.0 (new) / smartx-v2.2.0 / yang-v2.4.0 / news-v2.9.6 / market-overview-v1.9.0.

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 validation AC1-5.
- `[0.7.0_AE_CloudOps]` TO-6 landed -- clear to rebase the TRSB_LEDGER.005 by-approver GSI change on the durability-attrs version of dynamodb.tf.
