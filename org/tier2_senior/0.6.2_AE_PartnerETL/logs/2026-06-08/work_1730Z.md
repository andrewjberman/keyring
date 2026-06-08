# 0.6.2_AE_PartnerETL — Session Log 2026-06-08T1730Z

**archetype:** IMPLEMENT
**TO:** ADVI_CCAETL P0 (startup orientation + P0 scaffolding)

## Summary

First session. Read CTO PRD 899cb4e9f (`docs/architecture/ADVI_CCAETL.md` v0.1), MSTR inbox directive, Discovery Briefs 1/2/3, ADVI_FIRMSEP context, and inf-pipeline reference patterns (inf-jwt-trigger Lambda + secrets.tf + iam.tf). Built complete P0 Terraform scaffolding + OIDC session-refresh Lambda skeleton for Cottonwood Black Diamond pipeline. RAVC2 to COO pending.

## Work done

### P0 infrastructure scaffolded (bucket HOLD maintained)

**Files created:**

| File | Purpose |
|---|---|
| `infra/aws/terraform/cot-pipeline/main.tf` | Module scaffold — mirrors inf-pipeline/main.tf; TF state key `cot-pipeline/tfstate`; locals: account_id, region, cot_bucket=opal-data-cot |
| `infra/aws/terraform/cot-pipeline/secrets.tf` | SM secrets: `blackdiamond/cw/credentials` (username/password for OIDC login-mode) + `blackdiamond/cw/session` (.bd.identity cookie bundle, initial sentinel value) |
| `infra/aws/terraform/cot-pipeline/iam.tf` | (1) `cw-bd-session-trigger-lambda-role` — EC2 start + DescribeInstances + S3 mode marker write + SSM SendCommand (cot-tagged resources) + SM read credentials + read/write session; (2) `cot-gold-layer-ec2-role` + instance profile — S3 full-access opal-data-cot + SM session+credentials read + SSM managed core |
| `infra/aws/terraform/cot-pipeline/lambdas.tf` | `cw-bd-session-trigger` Lambda via yang-lambda module; EventBridge schedule stub COMMENTED (deferred to P1); EXPORTER_INSTANCE_ID empty pending EC2 provisioning |
| `infra/aws/lambda/cot-pipeline/cw-bd-session-trigger/lambda_function.py` | OIDC session-refresh Lambda — analog of inf-jwt-trigger; two modes: session-refresh (EC2 start + SSM dispatch opal-cw-bd-session-fetch) + session-check (SM read + BD /datamining/auth/token probe); graceful P1-pending path when EXPORTER_INSTANCE_ID unset |
| `infra/aws/lambda/ci/lambda-source-map.json` | Added `cw-bd-session-trigger` entry |

### HOLDS maintained

- **HOLD: `aws_s3_bucket.cot_data` resource** — NOT in any .tf file. Bucket creation gated on Andrew §6.2 ruling (opal-data-cot vs opal-data-cw). IAM policies and Lambda env vars reference `opal-data-cot` (FIRMSEP-canonical name) as a string only.
- **HOLD: EventBridge schedule** — commented stub in lambdas.tf. Deferred to P1 (requires cw-exporter EC2 instance ID).
- **HOLD: SSM document `opal-cw-bd-session-fetch`** — deferred to P1. This document runs the actual headless Playwright OIDC login on EC2. Equivalent to `opal-inf-jwt-fetch`.
- **HOLD: EC2 cw-exporter provisioning** — deferred to P1.

### Key design decisions

1. **Secrets hierarchy:** `blackdiamond/cw/credentials` (username/password) + `blackdiamond/cw/session` (session bundle). Mirrors the YCharts/Inflection split cleanly.
2. **Lambda modes:** `session-refresh` (full EC2+SSM flow) + `session-check` (SM read + BD token probe). The check mode is cheap — can be called before any bronze pull to gate on fresh session.
3. **IAM scope:** S3 `StartInstances` + `SSM:SendCommand` scoped to `System=CottonwoodPipeline` tag condition until exact instance ID is known at P1. Strict firm-compartmentalization — no cross-bucket access.
4. **P1-pending graceful degradation:** Lambda returns 503 when EXPORTER_INSTANCE_ID is unset (pre-EC2 state). Allows deploy now, wire EC2 at P1.

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp-iam service | N/A pre-deploy (new Lambda not yet in state) — deferred to P1 terraform apply |
| comp-iam gaps | N/A pre-apply — iam.tf new; cross-reference at P1 post-apply |
| comp-blast | N/A — no existing graph nodes for cot-pipeline yet; comp-build needed post-P1 |

Note: All three N/A calls are legitimately pre-deployment (Lambda and IAM resources don't exist in AWS yet). Mandatory comp-iam service + gaps deferred to immediately after first `terraform plan/apply` in P1.

## HOLD / blockers

- Andrew §6.2 ruling: opal-data-cot vs opal-data-cw canonical bucket name. **Gates the P0 bucket creation.**
- COO P0-P5 TO decomposition: TOs not yet issued. RAVC2 to COO this turn.

## Next actions

1. RAVC2 to COO: P0 oriented, scaffolding built, P0 plan ready.
2. COO issues P0 TOs.
3. P0 deploy: `terraform plan` (0 errors expected on new module except missing bucket) → after §6.2 resolves, `terraform apply` to create SM secrets + IAM roles.
4. After §6.2: create bucket, apply.
5. P1: provision cw-exporter EC2 + SSM document `opal-cw-bd-session-fetch` (Playwright OIDC login script).
