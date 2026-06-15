# 0.4.0_DS_ClientPlatform — work_1507Z (ADVI_COTETL P3: COT gold chain SSM doc + EventBridge)

**archetype:** IMPLEMENT

## Summary

Built COT v1 gold chain infrastructure: SSM document `opal-cot-gold-run` + EventBridge rules for silver/gold daily triggers. Validated TF (7-add plan, 0 changes, 0 destroy). RAVC2'd AE to commit + apply + extend Lambda for silver/gold dispatch modes.

Also: MDPF_CADENCE gate re-verified (COO DRIVE); pipeline-complete.json stale Jun 8, 0 Lambda invocations Jun 9 → DEFER correct, no escalation. RAVC2'd COO.

## Key technical outcomes

### Gold chain design
- **Script source**: `s3://opal-data-bd/code/gold/` (sync including lib/ + _lib/) → `/tmp/cot-gold/`
- **Env vars**: BD_S3_BUCKET=opal-data-cot, FIRM_ID=cottonwood, FIRM_NAME='Cottonwood Capital Advisors', SCHWAB_S3_BUCKET=opal-data-bd
- **Schwab degradation verified**: A_03 RPS injection catches missing mapping → BD-only positions; C_01 Schwab load catches exception → `schwab_flows_by_date={}` → BD-only NNA
- **§6.1 skips**: B_01/B_01b/B_02/B_03 (lots chain), C_07 (advisor attribution), C_08 (advisor fee), D_00c (leaderboards), D_01 (partner analytics)

### COT v1 gold chain (18 scripts)
| Phase | Scripts | Flags |
|---|---|---|
| Dimensions | A_00 A_01 A_02 A_03 A_04 | A_01/A_02 optional |
| Canonical | B_00 C_00 C_01 C_02 C_04 | B_00: --force-recent-days 14; C_04 optional |
| Downstream | C_03 C_05 C_06 D_00 D_00b D_02 D_03 D_04 | C_05/D_02/D_03/D_04 optional; C_06: workers 2/4 |

### TF resources (7-add plan)
- `aws_ssm_document.cot_gold_run` (opal-cot-gold-run): 18000s timeout, StartAt param for resume
- `aws_cloudwatch_event_rule.cot_silver_daily` (cot-silver-daily-trigger, 03:30 UTC, DISABLED)
- `aws_cloudwatch_event_target.cot_silver_daily_target`
- `aws_lambda_permission.eventbridge_cot_silver_daily`
- `aws_cloudwatch_event_rule.cot_gold_daily` (cot-gold-daily-trigger, 04:30 UTC, DISABLED)
- `aws_cloudwatch_event_target.cot_gold_daily_target`
- `aws_lambda_permission.eventbridge_cot_gold_daily`

### Blocker: owned-paths gate
DS cannot commit infra/aws/terraform/ (CLOUD_OPS_OR_ETL lane, AE-owned). RAVC2'd 0.6.2_AE with full diff + action items: commit TF, safe-apply, extend Lambda mode=silver-run/gold-run, ENABLE after v1 validation.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| terraform validate | cot-pipeline/ | PASS (fixed ${4:-required} → $${4:-required} TF escape) |
| terraform plan | cot-pipeline/ | 7 to add, 0 to change, 0 to destroy |

## Files Modified (pending AE commit)

| File | Change |
|---|---|
| infra/aws/terraform/cot-pipeline/ssm.tf | +opal-cot-gold-run SSM doc (18-script COT gold chain) |
| infra/aws/terraform/cot-pipeline/eventbridge.tf | +cot-silver-daily-trigger + cot-gold-daily-trigger (both DISABLED) |

## RAVC2 Sent

- AE (0.6.2_AE_PartnerETL): commit+apply TF + Lambda extension for silver-run/gold-run modes
- COO (2.0.0_SA_COO): MDPF_CADENCE DEFER (INF pipeline-complete.json Jun 8, 0 invocations Jun 9)

## Next Steps

- Tonight ~02:00Z: verify cot-bd-session-daily fires, session refreshed in SM
- Tonight ~02:30Z: verify cot-bronze-daily-trigger fires; RAVC2 AE post-run (row counts)
- Tonight ~03:00-03:30Z: manual trigger opal-cot-silver-run (or AE ENABLES cot-silver-daily after apply)
- Tonight ~23:00Z: GLDINC P0 first incremental + P1 first shadow scorecard — RAVC2 COO+AE

**Remaining gaps after this cycle:**
- Realized (qt3) + unrealized (qt4) bronze templates — BLOCKED until 02:00Z session refresh; then call DimensionsFacts qt3/qt4 + upload templates
- Silver SSM doc update for realized/unrealized tables (post-templates)
- AE: Lambda extension + TF apply + EventBridge ENABLE

work-cycle:0012
