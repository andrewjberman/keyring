# Session Log — Node.js 22 Upgrade (Wave A) + Precompute/CloudFront Generator Retirement

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**GO:** Andrew (direct session)
**Status:** COMPLETE
**Commits:**
- `44c95a5a1` — portal-auth Node.js 20→22 upgrade (Wave A)
- `aab5bd878` — market-overview + portal-notifications retirement TF (4 files, 161 deletions)
- `819246aa` — portal: remove legacy precomputed fallback + delete market-precomputed.ts
- `160924b17` — portal submodule pointer bump
- `e1ceff927` — ci: record deploy market-overview @ 7051d45c [skip ci]
**Tags:** `portal-auth-v1.15.0` | `market-overview-v1.10.0` | `portal-notifications-v1.0.0`
**Push:** CLOUD → remote + all tags; portal DEV → remote

---

## Scope

Two distinct workstreams executed in this session:

**Wave A — Node.js 22 Runtime Upgrade (portal-auth pipeline)**
Upgrade `opalinvest-auth-handler` and `opal-portal-authorizer` from `nodejs20.x` to `nodejs22.x` ahead of AWS end-of-support for Node 20.

**Retirement — `opal-precompute-market-metrics` + `opal-cloudfront-market-generator`**
Full decommission of two dormant market-overview Lambda functions and all associated infrastructure following investigation confirming both were non-functional and non-essential.

---

## Wave A: Node.js 22 Upgrade

### Scope Analysis

Audit of all Lambda runtimes across every Terraform pipeline identified 5 Node.js functions:

| Function | Runtime | Location |
|---|---|---|
| `opalinvest-auth-handler` | nodejs20.x | portal-auth/lambdas.tf (managed) |
| `opal-portal-authorizer` | nodejs20.x | portal-auth/lambdas.tf (managed) |
| `opal-precompute-market-metrics` | nodejs20.x | market-overview/lambdas.tf (placeholder.zip) |
| `opal-cloudfront-market-generator` | nodejs20.x | market-overview/lambdas.tf (placeholder.zip) |
| Lambda@Edge functions (5x) | nodejs20.x | portal-auth/lambda-edge.tf (externally deployed) |

Wave A = in-repo managed functions with S3 artifact backing. Wave B (Lambda@Edge) deferred — edge functions have CloudFront replication constraints requiring separate planning.

### Compatibility Check

- `opalinvest-auth-handler`: deps are AWS SDK v3, bcryptjs ^2.4.3, jsonwebtoken ^9.0.0 — all Node 22 compatible. `@types/node ^20.0.0` is devDep only, irrelevant at runtime.
- `opal-portal-authorizer`: pure ESM, imports jsonwebtoken + AWS SDK v3 — all Node 22 compatible.

### Execution

Changed `runtime = "nodejs20.x"` → `"nodejs22.x"` in `infra/aws/terraform/portal-auth/lambdas.tf` for both resources (lines 16 and 56). No code changes required — same artifact, runtime bump only.

terraform plan: 2 to change, 0 to add, 0 to destroy.
terraform apply: complete.
0-diff plan confirmed.
Tagged `portal-auth-v1.15.0`, pushed.

---

## Retirement: opal-precompute-market-metrics + opal-cloudfront-market-generator

### Investigation

CloudWatch metrics showed `opal-precompute-market-metrics` had 0 Lambda invocations over 30 days (EventBridge showed 60 scheduled firings → 60 FailedInvocations). Root cause: EventBridge rule `opal-precompute-metrics-schedule` target had `RoleArn: arn:aws:iam::313476888478:role/service-role/opal-eventbridge-lambda-role` — that role was deleted during CDN decommission work on 2026-04-15. Result: all EventBridge invocations failed at IAM level before reaching Lambda. Only 1 direct invocation recorded (manual, 2026-04-15).

`opal-cloudfront-market-generator` was downstream: it fired only on S3 `ObjectCreated` events when precompute wrote `market-metrics.json`. Since precompute never ran, the generator never ran either.

### Downstream Analysis (comp-blast / comp-trace)

- `opal-precompute-market-metrics` had no active consumers downstream in the portal API layer. The primary tiered endpoint path (`json-tiered/market-overview/` via Python generators) had been live since 2026-01-13 and was covering all portal consumers with no incidents.
- `opal-cloudfront-market-generator` consumed `market-metrics.json` from S3 and pushed to CDN `E2LPCXXBLDGWXY`, which was decommissioned 2026-04-15. No active consumers of that CDN distribution remained.
- Portal TypeScript had a SECONDARY fallback in `market.getAllReturns()` calling `precomputed.getMetricsFromEdge()` — confirmed that 30+ days of broken precompute produced zero user impact, confirming the tiered path fully covered demand.

### Infrastructure Removed

**market-overview pipeline (terraform destroy):**
- `aws_lambda_function.precompute_market_metrics` (opal-precompute-market-metrics, nodejs20.x, 1024MB, 300s)
- `aws_cloudwatch_log_group.precompute_market_metrics`
- `aws_lambda_function.cloudfront_market_generator` (opal-cloudfront-market-generator, nodejs20.x, 512MB, 60s)
- `aws_cloudwatch_log_group.cloudfront_market_generator`
- `aws_iam_role.market_metrics_role` (opal-lambda-market-metrics-role)
- `aws_iam_role_policy_attachment.market_metrics_basic`
- `aws_iam_role_policy.market_metrics_dynamodb`
- `aws_iam_role_policy.market_metrics_lambda_invoke`
- `aws_iam_role_policy.market_metrics_s3`
- `output.market_metrics_role_arn`

Total: 9 resources destroyed. Plan: `0 to add, 0 to change, 9 to destroy`. 0-diff confirmed.

**portal-notifications pipeline (terraform update):**
- `aws_lambda_permission.cloudfront_market_generator` (auto-removed by AWS when function deleted; Terraform pruned from state on refresh)
- `aws_s3_bucket_notification.portal_triggers` — updated in-place, removing `cloudfront-market-generator-trigger` lambda_function block

Total: `0 to add, 1 to change, 0 to destroy`. 0-diff confirmed.

**EventBridge (AWS CLI, unmanaged):**
- `aws events remove-targets --rule opal-precompute-metrics-schedule --ids 1`
- `aws events delete-rule --name opal-precompute-metrics-schedule`
- Verified: `ResourceNotFoundException` on describe-rule confirms deletion.

**lambda-source-map.json:**
- Removed `opal-precompute-market-metrics` entry
- Removed `opal-cloudfront-market-generator` entry

**Portal TypeScript:**
- `portal/src/api/endpoints/market.ts`: removed `import * as precomputed from './market-precomputed'` and SECONDARY try/catch block (9 lines). Relabeled former TERTIARY block as SECONDARY.
- `portal/src/api/endpoints/market-precomputed.ts`: deleted (~487 lines). File had `getMetricsFromEdge()` (active) + 3 `@deprecated` functions. Fully unreferenced after import removal.

### Tagging

- `market-overview-v1.10.0` — previous was `market-overview-v1.9.0`
- `portal-notifications-v1.0.0` — first formal tag for this pipeline

---

## Wave B Status (Lambda@Edge — DEFERRED)

5 Lambda@Edge functions at nodejs20.x remain:

| Function | ARN pattern |
|---|---|
| `auth-validator-edge` | CloudFront origin-request |
| `cors-headers-edge` | CloudFront response |
| `portal-index-router-edge` | CloudFront viewer-request |
| `portal-auth-handler-edge` | CloudFront viewer-request |
| `security-headers-edge` | CloudFront response |

Lambda@Edge requires US East 1 deployment + CloudFront replication propagation (15-30 min). Separate GO needed from Andrew before proceeding. AWS Node 20 EOL timeline: November 2025 (invocations blocked) → these are already past support cutoff but still running. Flag for priority scheduling.
