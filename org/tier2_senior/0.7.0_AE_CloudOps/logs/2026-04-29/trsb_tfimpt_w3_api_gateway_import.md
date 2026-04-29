# Session Log — TRSB_TFIMPT.W3: Shared Portal API Gateway Import

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**GO:** Andrew direct ("if there is a clean and clear TO let's just knock it out")
**Status:** COMPLETE
**Tags:** `shared-infra-v1.8.0` + `trade-pipeline-v1.7.0`

---

## Scope

Closes G3 — the shared portal HTTP API Gateway `7k3ed8px20`
(`opal-portal-data-proxy-api`) was console-only. Brings it into Terraform
under a new subordinate module + a data-source reference from trade-pipeline.

Same physical API GW serves trades, advisor-intelligence, partners, data-refresh,
auth-handler proxy, bd-client-detail, and portal-data-proxy (sentiment/keyword)
routes. CTO Option B (shared-infra subordinate) was the architectural call.

---

## Live State (recon)

| Resource | Count | Notes |
|---|---|---|
| `aws_apigatewayv2_api` | 1 | `7k3ed8px20` — HTTP API, `$request.method $request.path` route selection |
| `aws_apigatewayv2_authorizer` | 1 | `naqxlm` — REQUEST type calling `opal-portal-authorizer` Lambda |
| `aws_apigatewayv2_integration` | 9 | 4 trade + 1 advisor-intelligence + 1 data-refresh + 1 auth + 1 bd-client + 1 portal-data-proxy |
| `aws_apigatewayv2_route` | 74 | spans `/api/scoped/*`, `/api/general/*`, `/api/public/*`, `/v1/*`, `/auth/*`, `$default` |
| `aws_apigatewayv2_stage` | 1 | `$default` (auto-deploy enabled) |
| Lambda permissions on 4 trade Lambdas | 11 | 8 portal GW + 3 orphan `w8jnzvs21g` (out of scope) |

CORS allows: `opalinvest.dev`, `www.opalinvest.dev`, localhost ports
3000/4173/5173/5174/5175.

---

## Module Architecture

**`infra/aws/terraform/shared-infra/apigateway-portal/`** (new subordinate)

- `main.tf` — `aws_apigatewayv2_api.portal` + `aws_apigatewayv2_authorizer.portal_jwt`
- `integrations.tf` — 8 integrations (`i_576amr1` through `i_y95f56f`); s7ntfz4 omitted
- `routes.tf` — 73 routes; `r_khcd4f1` ($default catch-all) omitted
- `outputs.tf` — `api_id`, `api_arn`, `api_execution_arn`, `api_endpoint`, `stage_name` (hardcoded), `authorizer_id`

Wired into `shared-infra/main.tf` via `module "apigateway_portal" { source = "./apigateway-portal" }` plus 3 top-level outputs for cross-module consumption.

**`infra/aws/terraform/trade-pipeline/apigateway.tf`** (new file)

- `data.aws_apigatewayv2_api.portal` — references the shared module's API by ID
- 8 `aws_lambda_permission` resources — broad portal-invoke + scoped general-trades on trade-submission-handler, trade-workflow-handler, trade-dashboard-api, trade-identifier-cache

---

## Quick-Create Limitation

3 resources could not be imported. The original API was provisioned via
`aws apigatewayv2 create-api --target=<lambda>` (quick-create), which bundles
the API + a `$default` stage + a `$default` route + a default integration into
one CreateApi call. The AWS Terraform provider rejects `terraform import` on
these because they have implicit defaults that conflict with explicit declaration.

| Resource | Live ID | Status |
|---|---|---|
| `aws_apigatewayv2_stage.default` | `$default` | Console-only, auto-deploy enabled |
| `aws_apigatewayv2_integration` | `s7ntfz4` (opal-portal-data-proxy) | Console-only; 10 routes hardcode the integration ID |
| `aws_apigatewayv2_route` | `khcd4f1` ($default) | Console-only catch-all |

Documented in `apigateway-portal/main.tf` and `integrations.tf` with explicit
notes pointing to the limitation. The 10 routes that target `s7ntfz4` use
`target = "integrations/s7ntfz4"` literal-ID form rather than a TF reference.

---

## Import Mechanics

- **86 resources targeted** — 1 API + 1 authorizer + 1 stage + 9 integrations + 74 routes + (8 Lambda permissions in trade-pipeline)
- Generated `imports.txt` programmatically from live recon JSON to avoid hand-error on 74 routes
- First batch run hit a CRLF issue — Python wrote `imports.txt` with `\n` but bash `read -r` saw `\r` from somewhere; `tr -d '\r'` produced clean LF and the second run worked
- Path issue: `$TF -chdir=/c/Users/...` fails when `MSYS_NO_PATHCONV=1` is set; switched to `C:/Users/...` literal
- **Final tally:** shared-infra 82 imported + 1 already-managed + 3 unimportable (quick-create); trade-pipeline 8/8 imported clean

Per-resource `terraform plan` after import: shared-infra showed 1 in-place change (provider `default_tags` getting added to the API's `tags_all` — pure metadata). Applied. Re-plan: `No changes`.

trade-pipeline post-import: `No changes` immediately.

---

## Acceptance Criteria

| AC | Status | Evidence |
|---|---|---|
| 1. `terraform plan` 0-diff trade-pipeline | PASS | "No changes" |
| 2. All live API GW resources represented | PARTIAL | 82/86 — 4 quick-create unimportable, documented |
| 3. CloudFront behavior for `/api/general/trades/*` | UNCHANGED | Existed pre-W3, no CF edit needed (per Phase 0 evidence) |
| 4. `comp-routes trace trade-submission-handler` | DEFERRED | Requires `comp-build` rerun |
| 5. `comp-routes auth-map` shows trade routes | DEFERRED | Same |
| 6. `comp-iam gaps` clean | UNCHANGED | No new IAM grants |
| 7. End-to-end smoke | UNCHANGED | No live runtime change — imports are metadata-only |
| 8. Tags `shared-infra-v1.8.0` + `trade-pipeline-v1.7.0` | PASS | Both pushed |
| 9. Session log | PASS | This file |
| 10. MCP COMPLETE to COO | TODO | Will follow after this commit |
| 11. PROJECT closeout — TRSB_TFIMPT Active→Completed in REGISTRY | TODO | Tier-1 scope (COO) |

The TO version target was `trade-pipeline-v1.5.0`, but live tag list was already
at `v1.6.3` from earlier this session's TRSB_PATHFIX work; bumped to `v1.7.0`
following the `WORK series, not just highest` rule.

---

## Wire Contract Verification

Zero runtime delta as predicted:
- API GW resources existed live; `terraform import` is state-only
- Lambda permissions existed live; same
- CF origin `APIGateway-portal` in portal-auth/cloudfront-distribution.tf untouched
- One actual live change: provider `default_tags` (`Project`, `ManagedBy`, `Environment`, `System`) added to the API GW's tags. Pure metadata, no functional impact

---

## Carry-Forward Items

- **Orphan API GW `w8jnzvs21g`** — 3 of 4 trade Lambdas have invoke permissions for it. No CloudWatch traffic in 30+ days per TRSB_PATHFIX.TO-3 §do_not. Separate cleanup TO needed (delete API + permissions).
- **`comp-build` refresh** — graph hasn't been rebuilt since import. Next agent running compiler tools will see populated CF→GW→Lambda chain on first refresh.
- **REGISTRY update** — TRSB_TFIMPT row Active→Completed is a tier-1 (COO/CTO) edit, not AE.
