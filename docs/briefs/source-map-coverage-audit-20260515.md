# Source-Map Coverage Audit — what in the cloud lacks drift tracking

**Author:** 1.0.0_SA_CTO
**Date:** 2026-05-15
**Trigger:** Andrew directive — "establish what in our cloud/system does not have source maps and make sure those are mapped too (specific for high-traffic, active resources, not vestigial stuff that hasn't been invoked/accessed in months)."
**Home project:** ADHC_DRIFTD (this is the v0.2 scoping inventory; v0.1 hardened Lambda deploy-records).
**Status:** INVENTORY — Andrew reviews coverage + recommendation before any mapping work is authored.

---

## 1 — What a "source map" is, and the two drift surfaces

A source map ties a deployed cloud resource back to its repo source-of-truth so drift is *detectable*. There are exactly two drift surfaces worth a map — and one that needs no map at all:

| Drift surface | What it means | Detected by |
|---|---|---|
| **Code-artifact drift** | A deployable code blob (Lambda zip, EC2 service code, data script, portal build) is *copied* to the cloud; the copy can silently fall behind the repo. | content-hash / commit compare — `lambda-source-map.json` (`artifact_sha256`), `EC2_MANIFEST.json` (`deployed_commit`), `comp-pipescript deployed` (S3 ETag) |
| **Committed-but-unapplied Terraform** | A `.tf` change is committed but `terraform apply` was never run. The repo is ahead of what's live. | `{module}-resource-map.json` + `drift-check-resource-map.sh` — `git log -1 -- <tf_file>` vs `last_deployed_commit` (pure git, no AWS calls) |
| ~~Reality-vs-state drift~~ | Someone changes a resource in the AWS console, diverging from Terraform state. | `terraform plan` 0-diff — **already universal; needs no source map.** |

The third row is the important disclaimer: every Terraform-managed resource already has reality-vs-state drift detection via `terraform plan`. A source map only adds value for the *other two* surfaces. This is what keeps the audit from ballooning into "map all 871 resources."

---

## 2 — Current coverage (verified 2026-05-15)

| Surface | Map / mechanism | Scope | Status |
|---|---|---|---|
| Lambda function code | `infra/aws/lambda/ci/lambda-source-map.json` | all pipelines, 100+ functions | COVERED |
| Lambda layers | `infra/aws/lambda/ci/lambda-layer-map.json` | 8 layers | COVERED (3 unmanaged layers flagged — pre-existing AE cleanup item, not this audit) |
| EC2 service code | `infra/aws/ec2/EC2_MANIFEST.json` | ~18 instances (exporters, runners, moltbot) | COVERED |
| shared-infra non-Lambda Terraform | `infra/aws/lambda/ci/shared-infra-resource-map.json` | S3 / DynamoDB / IAM / layer / API Gateway in `shared-infra/` | COVERED (created today per Andrew directive) |
| Data pipeline scripts (gold/silver/bronze) | `comp-pipescript deployed` (on-the-fly) + `safe-deploy.sh` deploy-cycle gate | bd + inf S3 `code/` prefixes | COVERED by tooling (no persistent manifest — see §4) |

Tooling already generic: `drift-check-resource-map.sh [module]` defaults to shared-infra but works for **any** module with a `{module}-resource-map.json`. Extending coverage = adding JSON files, **not writing new tools.**

---

## 3 — Gap analysis (right-sized to the "active, not vestigial" filter)

There are 21 Terraform modules. Their **Lambda code** is covered everywhere by `lambda-source-map.json`. The gaps are in *non-Lambda* resources and *non-Lambda* code artifacts:

| Gap | Drift surface | Covered today? | Active / high-traffic? | Verdict |
|---|---|---|---|---|
| **EventBridge crons** outside shared-infra | committed-but-unapplied TF | NO | YES — 67 cron/schedule rules; these *trigger the daily pipelines* | **MAP** |
| **Portal frontend build** (S3 + CloudFront assets) | code-artifact | NO | YES — the customer-facing product | **MAP** |
| Pipeline-local DynamoDB / SQS / SNS / ECR / Step Functions / SSM docs / IAM / API Gateway / CloudFront | committed-but-unapplied TF | NO (only shared-infra mapped) | LOW config-churn; `terraform plan` covers reality drift | **DECLINE** — see §4 |
| `causality` + `seeking-alpha` Terraform modules | TF | NO | NO — not even on the S3 Terraform backend; dormant | **DECLINE** — vestigial |
| Data-scripts *persistent* manifest | code-artifact audit trail | tool only, no manifest | YES, but tool already suffices | **DECLINE** — see §4 |

EventBridge cron distribution (67 rules, 23 files): news-pipeline 25, inf-pipeline 17, bd-pipeline 12, market-overview 6, smartx-pipeline 3, seeking-alpha 2, exec-summary 1, portal-auth 1 (a CloudWatch-alarm rule, not a cron). The cron is the one non-Lambda resource class where a silent commit-but-unapplied drift **changes production behavior invisibly** — a pipeline runs on the wrong schedule, or doesn't run at all. (Note: inf-pipeline crons live in per-Lambda `.tf` files, so they are *not* caught by `lambda-source-map.json`, which tracks code in `source_dir`, not the `.tf`.)

---

## 4 — Recommendation: map 2, decline the rest

### Map (both extend existing patterns — minimal new surface)

1. **EventBridge crons for the active daily pipelines** — `inf`, `bd`, `news`, `market-overview`, `smartx` — the five modules that declare cron rules (`yang` declares none; it orchestrates via Step Functions, so its daily-trigger path is confirmed during triage, not assumed). Add a `{module}-resource-map.json` per pipeline scoped to its `aws_cloudwatch_event_rule` / `aws_scheduler_schedule` (and, free, its Lambda *infra-config* — memory/timeout, which `lambda-source-map.json` also doesn't track). Zero new tooling; `drift-check-resource-map.sh` already handles any module. TO authoring will confirm which of the 67 rules are genuinely live vs dormant before mapping them — per the "not vestigial" directive.

2. **Portal frontend deployment manifest** — a lightweight manifest tying the S3 + CloudFront deployed assets back to the `portal` submodule PROD commit. It is the only customer-facing code artifact today with *zero* drift tracking; "did prod get the latest build" is currently answerable only by manual inspection.

### Decline (explicitly, with reason — the discipline Andrew asked for)

- **Pipeline-local DynamoDB / SQS / SNS / ECR / Step Functions / SSM / IAM / API Gateway / CloudFront** — all 100% Terraform-managed; `terraform plan` 0-diff already detects reality drift, and config-churn is low. Per-resource maps here are exactly the vestigial busywork to avoid. (If the EventBridge work pulls portal-auth in, CloudFront rides along free — but it is not standalone-worth.)
- **`causality` + `seeking-alpha` modules** — dormant, not on the S3 Terraform backend. Vestigial. Skip.
- **Data-scripts persistent manifest** — already covered: `comp-pipescript deployed` answers MATCH/STALE/MISSING on demand, and `safe-deploy.sh` (Rule 13) gates the deploy cycle atomically with the same check. A persistent manifest would add only an audit trail — not worth a new artifact.

---

## 5 — Decision gate + next step

**Andrew reviews §2–§4.** If the two-item recommendation holds (or is adjusted), the work becomes **ADHC_DRIFTD v0.2**, decomposed into TOs owned by 0.7.0_AE_CloudOps:

- TO-4 — EventBridge cron resource-maps for the 5 cron-declaring active pipelines (live-vs-dormant triage first, then `{module}-resource-map.json` + `record-resource-deploy.sh` wiring).
- TO-5 — portal frontend deployment manifest + drift check.

No mapping is started until Andrew confirms the scope.
