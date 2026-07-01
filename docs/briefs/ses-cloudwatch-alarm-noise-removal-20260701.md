# BRIEF — Retire the CloudWatch "health-check" alarm noise (Andrew-direct 2026-07-01)

**Author:** 0.0.0_AB_MSTR · **Owner of execution:** AE (infra lane) · **Priority:** NON-URGENT (must not preempt the 49F/INFREF firefight) · **Account:** 313476888478 (us-east-1 + us-east-2)

## 1. Context & decision

Andrew-direct: the CloudWatch alarm emails he receives ("SES notifications") are unwanted noise — "I don't care about even one of these... I would delete all of them." He characterizes them as noisy, consistent, and probably wrong.

**Already done (instant, reversible):** all 7 SNS **email** subscriptions to `andrew@opalinvest.com` were unsubscribed (verified 0 email subscriptions remain). **The inbox noise has already stopped** without any Terraform change. This brief covers the *durable purge of the alarms themselves*, which Andrew asked to be assessed and planned.

**Key fact:** the alarms are **Terraform-managed**, so a console `delete-alarms` gets **recreated on the next `terraform apply`**. Durable removal = deleting the TF resource blocks + `safe-apply` per module. That is an AE lane task (MSTR does not edit Terraform).

## 2. Assessment — the 67 alarms by IaC source

**Total: 67 alarms** (65 us-east-1 + 2 us-east-2). Two classes:

### Class A — Terraform-managed (~50 alarms, 17 files) → delete blocks + apply

| Terraform file | Alarms (count) | Note |
|---|---|---|
| `bd-pipeline/alarms.tf` | ExecIncrParityFailure, bd-gold-runner-overrun, bd-gold-qa-runner-forgotten (3) | |
| `bd-pipeline/bd-49f-interim.tf` | bd-49f-keepalive-absence, -authtoken-dead, -authtoken-absence, **bd-49f-silver-stale-{allocations,fees,realized,transactions,unrealized}** (8) | last block is **`for_each`** (1 block → 5 alarms) |
| `bd-pipeline/gldinc-ss4c.tf` | gldinc-ss4c-{canary-break, canary-absence, weekly-divergence, weekly-absence} (4) | |
| `cot-pipeline/cot-detection-layer.tf` | bd-cot-keepalive-absence, -authtoken-dead, -authtoken-absence, -served-aua-stale, **bd-cot-silver-stale-{allocations,holdings,realized,transactions,unrealized}** (9) | silver block is **`for_each`** (1 block → 5 alarms) |
| `inf-pipeline/alarms.tf` | orion-otp-timeout-alert, Inflection-JwtResilience-NearExpirySpike, Inflection-HistBackfill-FailureSpike, inf-gold-chain-failed, inf-gold-runner-overrun (5) | |
| `inf-pipeline/inf-silver-chain.tf` | Inflection-SilverChain-DimConversionFailure (1) | |
| `inf-pipeline/inf-nna-partition-checker.tf` | inf-nna-partition-completeness-breach (1) | |
| `inf-pipeline/lambdas.tf` | inf-bronze-trigger-missed-start (1) | alarm colocated with lambda def |
| `mdpf-pipeline/alarms.tf` | mdpf-daily-{trigger-dlq-not-empty, chain-failed, stage5-ownts-failed, freshness-stale} (4) | |
| `portal-auth/cloudwatch-alarms.tf` | FIRMSEP-auth-{advisor-scoping-denied, tier-denied, ownership-map-fetch-failed, ownership-map-schema-mismatch}, FIRMSEP-shared-advisor-router-denied (5) | firm-separation auth guardrails |
| `exec-summary/main.tf` | exec-summary-{advisors-processed-ceiling, tokens-in-anomaly} (2) | also check `exec-summary/outputs.tf` for orphaned ARN outputs |
| `globgrph/d4f1_request_alarm.tf` | globgrph-s3-requests-daily-{warning, high} (2) | |
| `astn-pipeline/orchestrator.tf` | astn-wsjft-orchestrator-errors (1) | |
| `etfs-reports/orchestrator.tf` | etfs-reports-orchestrator-errors (1) | |
| `ycharts-pipeline/cloudwatch.tf` | YChartsSessionEviction (1) | |
| `canonical-schwab-si2-schedule/schedule.tf` | canonical-schwab-si2-schedule-absence (1) | |
| `canonical-schwab-ec2/runner-trigger.tf` | canonical-schwab-xref-sentinel-absence (1) | |

### Class B — NOT in Terraform (~17 alarms) → console/app-deploy created

No literal `alarm_name =` for these in any `.tf` under `infra/aws/terraform` (authoritative — a TF alarm must set `alarm_name`):

- `cloudfront-{high-error-rate, high-origin-latency, low-cache-hit-rate}` (3)
- `opal-partners-data-{duration-high, errors, throttles}` (3)
- `opal-session-analytics-{errors, estimated-monthly-cost, high-invocations, throttles}` (4)
- `semantic-layer{2.5-clustering-failures, 2.5-duration-warning, 3-gpt-curation-failures, 4-portal-publisher-failures}` (4)
- `PortfolioExcelGenerator-Errors` (1)
- **[us-east-2]** `fred-ingestion-{duration, errors}` (2)

**ACTION for Class B:** before CLI-deleting, verify each is truly console-created and **not emitted by an application deploy** (SAM/serverless/CDK/a deploy script — e.g. session-analytics or partners-api app deploy). If it is app-emitted, delete at that source too or it respawns. If genuinely console-only → `aws cloudwatch delete-alarms --alarm-names <...>` (per region; the 2 `fred-*` are **us-east-2**).

## 3. The fixes (execution plan — AE lane)

1. **Class A, per module:** delete the `aws_cloudwatch_metric_alarm` block(s); for the two `for_each` blocks also remove the now-orphaned `for_each` set/local; delete any `aws_sns_topic_subscription` / `alarm_actions` wiring that existed *only* to serve a deleted alarm. Run `.tools/safe-apply.sh` per module; confirm the plan shows **only alarm destroys** (no collateral resource change), reach 0-diff after apply. 17 modules — batchable but keep each apply scoped + reviewed.
2. **Keep the SNS topics.** `opal-*-alerts` topics have **non-email subscribers that are live automation**: lambda `inf-ec2-retry-launch` (on `inf-otp-alert`), sqs `opal-critical-surface-alerts-coo`, and SMS. Deleting the alarms simply stops them *publishing*; the topics + automation stay intact. **Do not delete the topics.**
3. **Class B:** after the source-verify above, CLI `delete-alarms` (respect region for the 2 us-east-2 `fred-*`).
4. **Email subs:** already removed (this session). **SMS subs** to `+17862617679` (ec2-long-running, find-insure-budget, opal-critical-surface, opal-infrastructure) and `+13052010419` (inf-otp) are **still active** — Andrew's call whether those go too (he named email/"SES"; SMS is a separate channel).

## 4. Guardrails / call-outs (informed-purge, not blind)

- **Load-bearing alarms in the set:** the bd-49f / bd-cot **auth + silver-staleness**, **inf** gold-chain/runner, and **mdpf** freshness alarms cover the exact pipelines under active firefight tonight; several are firing **real** right now (`mdpf-daily-freshness-stale`, `inf-gold-runner-overrun`, `bd-49f-silver-stale-fees` were in ALARM). Deleting them removes that safety net. **Andrew has decided to remove them anyway**; recorded here so the purge is informed, not silent.
- **Reversible alternative already in place:** the email delivery is muted. If the intent is only "stop bothering Andrew," that is **already achieved** and the TF purge is optional. If the intent is "physically purge the alarms," proceed per §3.
- **No console edits to TF-managed resources** (they drift + respawn). Terraform-only, `safe-apply` (HALTGT checkpoint) per module.
- **Sequencing: NON-URGENT.** Do not preempt the 49F/INFREF hot-path work. Execute when AE lanes free.

## 5. Rollback

- Class A: every alarm block is in git — `git revert` the removal commit + `safe-apply` restores.
- Class B: recreate from the alarm's saved definition (capture `describe-alarms` JSON per alarm *before* deleting — one `aws cloudwatch describe-alarms --alarm-names <all> > alarms-backup.json` snapshot is the cheap insurance).
- Email/SMS: re-subscribe is one `aws sns subscribe` per topic (email requires a confirmation click).

---
*MSTR brief per Andrew-direct 2026-07-01. Assessment grounded in `infra/aws/terraform` (`alarm_name` literal scan, authoritative) + live `aws cloudwatch describe-alarms` (us-east-1: 65, us-east-2: 2) + `aws sns list-subscriptions`. Execution routes through the AE infra lane via COO.*
