# 0.6.0_AE Log: ADVI_GLDRST.022 Phase 1 -- bd-canonical-prices-daily EventBridge rule
**Date:** 2026-04-10
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** bd-v2.22.0
**Related:** docs/briefs/ae-brief-v2-prestep-integration.md (Phase 1 of 5)
**Predecessor:** ADVI_GLDRST.022 DS integration shipped earlier today (commit 8c801923 on CLOUD; v2 + ticker_overrides.py in s3://opal-data-bd/code/gold/)

## Context

DS completed ADVI_GLDRST.022 integration: `build_canonical_prices_v2.py` is now registered as `S_00` in `gold_dispatch.sh` CATALOG and runs as a silver-prep pre-step before the freshness gate on every `--chain full` / `--chain rebuild` invocation. Code + S3 artifacts are in place. AE owns the downstream infra work.

Phase 1 of the AE brief: add a new daily EventBridge cron rule that fires `bd-gold-trigger` every day (including weekends and US market holidays), so v2 can T3-interpolate or T4-carry-forward the weekend/holiday gap dates into `silver/prices/canonical_prices.parquet`. Pre-Phase 1 coverage was Mon-Fri only via `bd-allocation-pipeline-trigger` + `bd-gold-nightly-fallback`, leaving weekends/holidays with no canonical_prices refresh.

## Work Done

### Terraform -- new resources

Added to `infra/aws/terraform/bd-pipeline/eventbridge.tf` section 7:

- `aws_cloudwatch_event_rule.bd_canonical_prices_daily` -- `cron(0 22 * * ? *)`, ENABLED, every day
- `aws_cloudwatch_event_target.bd_canonical_prices_daily_target` -- targets `module.gold_trigger.function_arn`, input `{"mode":"incremental"}`
- `aws_lambda_permission.eventbridge_canonical_prices_daily` -- `statement_id = "allow-canonical-prices-daily-trigger"`

Cron pattern rationale: `cron(0 22 * * ? *)` not `cron(0 22 ? * * *)` -- EventBridge requires exactly one of day-of-month or day-of-week to be `?`. Matches the pattern already used by `historical-prices-daily`.

Mode rationale: `incremental` delegates to `gold_dispatch.sh --chain full --incremental` on the runner. On weekdays that runs silver-prep (S_00) first, then the freshness gate passes (new allocations landed), then the full A/B/C/D chain executes. On weekends/holidays silver-prep runs, the gate trips, A/B/C/D skips, and the instance shuts down via watchdog -- canonical_prices is still updated for that weekend/holiday date.

### Drift handling

Initial `terraform plan` showed 3 adds (my changes) plus 2 unexpected drift items:

| Resource | Live state | TF-defined | Decision |
|---|---|---|---|
| bd-gold-layer-monthly-trigger | DISABLED | ENABLED | Keep live (DISABLED) -- codified into tf |
| bd-gold-nightly-fallback | cron(0 23 ? * MON-SAT *) | cron(0 23 ? * MON-FRI *) | Keep live (MON-SAT) -- codified into tf |

Flagged both to Andrew, who confirmed both live-state changes are intentional. Chose the targeted-apply path to ship Phase 1 cleanly without sweeping the drift:

1. Applied the 3 new resources via `terraform apply -target=...` (3 added, 0 changed, 0 destroyed)
2. Edited `eventbridge.tf` to match live state: `bd_gold_monthly.state = "DISABLED"` and `bd_gold_nightly_fallback.schedule_expression = "cron(0 23 ? * MON-SAT *)"` + updated description
3. Follow-up `terraform apply` picked up only a description text change on `bd_gold_nightly_fallback` (0 added, 1 changed)
4. Final `terraform plan` returned `No changes. Your infrastructure matches the configuration.`

`-target` is flagged as non-routine by Terraform, but this was the right call here: the drift was load-bearing intent from someone else and bundling it into the Phase 1 apply would have silently reverted their changes.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read AE brief + DS session log | Phase 1 scope confirmed |
| 2 | comp-blast bd-gold-trigger | No down connections (known compiler gap: lambda->EC2 edges not indexed) |
| 3 | Read eventbridge.tf | Confirmed section 6 (historical-prices-daily) as append point |
| 4 | Edit eventbridge.tf -- add section 7 (canonical_prices_daily) | 3 new resources |
| 5 | terraform plan | 3 add + 2 drift changes -- flagged to Andrew |
| 6 | Andrew confirmed drift is intentional | Targeted apply approved |
| 7 | terraform apply -target=... (3 resources) | 3 added, 0 changed, 0 destroyed |
| 8 | Verify rule in live AWS | `bd-canonical-prices-daily` ENABLED, cron(0 22 * * ? *), target=bd-gold-trigger, input={"mode":"incremental"} |
| 9 | Verify Lambda policy | `allow-canonical-prices-daily-trigger` statement present |
| 10 | Edit eventbridge.tf -- codify live state (monthly DISABLED, nightly MON-SAT) | Matches live |
| 11 | terraform apply (full, no -target) | 0 added, 1 changed, 0 destroyed (nightly description text) |
| 12 | terraform plan | No changes. Infrastructure matches configuration. |
| 13 | Update pipeline_inventory.xml (current_tag, add 2 rules, DISABLED monthly) | Core doc in sync |
| 14 | git commit (infra + core doc) | (filled by commit) |
| 15 | record-terraform-deploy.sh + tag + push | bd-v2.22.0 |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| BD | bd-v2.22.0 | (filled by commit) |

## Verification

```
$ aws events describe-rule --name bd-canonical-prices-daily --query '[Name,State,ScheduleExpression]' --output text
bd-canonical-prices-daily   ENABLED   cron(0 22 * * ? *)

$ aws events list-targets-by-rule --rule bd-canonical-prices-daily --query 'Targets[0].[Id,Arn,Input]' --output text
1   arn:aws:lambda:us-east-1:313476888478:function:bd-gold-trigger   {"mode":"incremental"}

$ aws lambda get-policy --function-name bd-gold-trigger (Sids)
allow-monthly-trigger
S3PricesTrigger
allow-nightly-fallback-trigger
allow-canonical-prices-daily-trigger

$ terraform plan (final)
No changes. Your infrastructure matches the configuration.
```

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before writing) | comp-blast | `comp-blast bd-gold-trigger` | "No downstream consumers" -- known compiler gap: graph doesn't index lambda->EC2 invocation edges or EventBridge->lambda reverse targets. Graph built 659 nodes / 285 edges in 1.4s. |
| 1 (before writing) | comp-trace | `comp-trace bd-gold-trigger --direction down` | "No down connections found" -- same graph gap |
| 2 (before commit) | terraform validate (implicit via plan) | `terraform plan` | Plan succeeded, resources resolvable, no syntax errors |
| 2 (before commit) | terraform plan (post-edit) | `terraform plan` | 0-diff confirmed |
| 3 (after commit) | aws events describe-rule + list-targets-by-rule + get-policy | see Verification | Rule + target + lambda permission live |

**Compiler gaps logged** (also flagged by DS earlier today in `advi_gldrst_022_v2_prestep_gold_runner_integration.md`):

1. Graph builder does not follow Lambda-to-Lambda `lam.invoke(FunctionName=...)` edges
2. Graph builder does not follow Lambda-to-EC2 SSM send_command / start_instances edges
3. Graph builder does not index EventBridge->Lambda target edges (reverse direction)

Combined, these gaps meant neither comp-blast nor comp-trace could surface anything meaningful for this change. Verification fell back to direct AWS CLI describe-rule / get-policy and terraform plan 0-diff. Appending to `org/compiler-tools-log.md`.

## Current State

| Component | State |
|---|---|
| `bd-canonical-prices-daily` EventBridge rule | ENABLED, cron(0 22 * * ? *), target=bd-gold-trigger, input={"mode":"incremental"} |
| `bd-gold-nightly-fallback` rule | ENABLED, cron(0 23 ? * MON-SAT *) (live + tf in sync) |
| `bd-gold-layer-monthly-trigger` rule | DISABLED (live + tf in sync) |
| `bd-price-update` Lambda Job 1 | STILL ENABLED -- Phase 3 parallel-run diff must complete before Phase 4 disables it |
| pipeline_inventory.xml | updated to bd-v2.22.0, new rules documented |
| Production gold runner (i-01003b035d2988dfb) | Not yet booted by new rule -- first fire at 22:00 UTC today (6 PM EDT) |

## Next Steps

- **[0.6.0_AE_PartnerETL]** Tonight at 22:00 UTC (6 PM EDT, ~3h from now): monitor the first fire of `bd-canonical-prices-daily`. Watch `bd-gold-trigger` CloudWatch logs and the runner's systemd logs at `s3://opal-data-bd/logs/gold-layer/`. Today is Friday, so `bd-allocation-pipeline-trigger` also fires at 22:00 UTC -- the pending-marker mechanism should absorb the double-fire into a single runner boot.
- **[0.6.0_AE_PartnerETL]** Phase 2 (IAM sanity check): run the `aws s3 ls` / `aws s3 cp` tests from the brief against the runner's instance profile to verify read on `silver/transactions/`, `silver/historical_prices.parquet`, `silver/prices/canonical_prices.parquet` and write on `silver/prices/`. Run before the first fire if possible; if not, check after tonight's run.
- **[0.6.0_AE_PartnerETL]** Phase 3 (parallel-run diff protocol): starting Monday (2026-04-13), snapshot `silver/prices/canonical_prices.parquet` after `bd-price-update` Job 1 completes and again after v2's silver-prep completes. Diff on `(date, asset_name)`; stop-ship signals: `price` delta > $0.001, missing rows from v2, source-tag disagreement. Run for 5 business days (2026-04-13 through 2026-04-17) before proceeding to Phase 4.
- **[0.6.0_AE_PartnerETL]** Phase 4 (after clean parallel week): wrap `bd-price-update` Job 1 in `ENABLE_JOB_1` env var guard defaulting to false. Do NOT touch Job 2 (interpolated_prices.parquet writer -- v2 still reads it for the emergency-rebuild path).
- **[0.6.0_AE_PartnerETL]** Phase 5 rollback plan accessible for 2 weeks post-shipping: env var flip -> gold_dispatch revert -> EventBridge rule disable.
- **[Andrew]** First production run of v2 via this rule fires tonight at 22:00 UTC. If anything misbehaves, Phase 5 rollback options are in the brief.
- **[1.0.0_SA_CTO / 2.0.0_SA_COO]** Org dirt from DS session (task orders .021 / .021b, earlier session log, diagram generator, cross-DS audit docs) is still uncommitted in the working tree. Outside AE's lane -- deferred to whoever picks up the next org-tidy routing.
- **[follow-up, not assigned]** Two EventBridge rule entries in `pipeline_inventory.xml` had stale schedules predating the 2026-04-06 BD schedule shift (transaction shown as 21:40 UTC, should be 21:53; allocation shown as 21:48 UTC, should be 22:00). Not touched in this commit to avoid scope creep. Worth a small cleanup pass.
- **[follow-up, not assigned]** Compiler graph gaps (lambda-to-lambda, lambda-to-EC2, eventbridge-to-lambda reverse direction) make comp-blast / comp-trace near-useless for pipeline infra changes. Logged above + in DS's log earlier today. Small PR to `org/modules/graph/` would help.
