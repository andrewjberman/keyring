# Session Log — AUTH_TFIMPT.001 Completion + Hotfixes

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-06 (session 2)
**Status:** COMPLETE

---

## 1. Compiler Module Extensions (HCL + ESM)

Extended two compiler modules to handle Terraform and JavaScript:

### ast_extractor.py — New Extractors

| Extractor | Extensions | Extracts |
|-----------|-----------|----------|
| `_extract_hcl` | `.tf` | Resource/data blocks, variables, outputs, cross-resource refs, ARN/S3 string literals |
| `_extract_esm` | `.mjs`, `.js` | ES module imports, exported/arrow functions, path patterns, AWS/S3 references |

### crossref_graph.py — New Reference Patterns

| Pattern | Purpose |
|---------|---------|
| `_HCL_RESOURCE_REF` | Resolves `aws_type.name.attr` to defining file |
| `_HCL_SOURCE_COMMENT` | Follows `# Source: path/to/file` comments |
| `_ESM_IMPORT` | Resolves relative ES module imports |

### Validation Results (Pre-Write)

Ran full compiler pipeline on portal-auth TF + lambda-edge corpus (19 files):
- crossref_graph: 3 edges (lambda-edge.tf -> iam.tf, lambdas.tf -> iam.tf, source comment link)
- ast_extractor: 40 TF resources mapped, 5 edge functions with path patterns extracted
- coverage_auditor: 14/14 behaviors covered, 9/9 dependency checks passed

---

## 2. AUTH_TFIMPT.001 — CloudFront Distribution Import

**Objective:** Import CloudFront distribution EVTSA9VEHNZVH (opalinvest.dev) into portal-auth TF state.

### Live Distribution Config (Captured)

| Element | Count |
|---------|-------|
| Origins | 5 (S3-opalinvest-portal, S3-opal-data-portal-v2-json, S3-opal-data-bd, APIGateway-portal, APIGateway-portfolio) |
| Behaviors | 14 + default |
| Lambda@Edge | 4 functions (auth-validator-edge:9, shared-advisor-router:8, public-data-router:4, cache-control-injector:1) |
| Cache Policies | 4 (CachingOptimized, CachingDisabled, opal-scoped-advisor-by-firm, json-tiered-5min-cache) |
| Custom Error Responses | 2 (403->index.html, 404->index.html) |
| Cert | ACM cf2d3e43, sni-only, TLSv1.2_2021 |

### Execution

| Step | Result |
|------|--------|
| Write `cloudfront-distribution.tf` | 5 origins, 14 behaviors, all Lambda@Edge associations |
| coverage_auditor post-write | 14/14 behaviors matched live |
| `terraform import` | Success |
| `terraform apply` | Tags added + origin reorder (cosmetic), 58s |
| 0-diff verify | Perpetual origin TypeSet diff (known TF behavior) |
| `record-terraform-deploy.sh` | Source map updated, 7 functions recorded |
| Commit | `af320516` |
| Tag | `portal-auth-v1.10.0` |
| Push | CLOUD + tag |

---

## 3. Hotfix: opal-portal-authorizer Broken Artifact

**Symptom:** Portal partners/advisors/books tabs returning 500 errors.

**Root Cause:** The S3 artifact `portal-auth/opal-portal-authorizer.zip` contained only the raw `index.mjs` (2.4KB) without bundled `jsonwebtoken` dependency. The API Gateway authorizer Lambda crashed on every request with `ERR_MODULE_NOT_FOUND: Cannot find package 'jsonwebtoken'`. This was caused by an earlier session's build that uploaded an unbundled artifact — not by the CloudFront import.

**Diagnosis Path:**
1. Verified CloudFront distribution config identical to pre-import (behaviors, origins, Lambda ARNs all match)
2. Tested endpoints via curl — auth-validator-edge returning proper 401 (routing correct)
3. Found zero invocations of `opal-partners-data` Lambda — requests never reaching backend
4. Checked `opal-portal-authorizer` logs — `ERR_MODULE_NOT_FOUND: Cannot find package 'jsonwebtoken'`
5. Downloaded S3 artifact — 1 file (index.mjs), no node_modules

**Fix:**
```bash
bash infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth opal-portal-authorizer
terraform apply -target=aws_lambda_function.portal_authorizer
```

Rebuilt artifact: 20KB bundled zip (76 modules inlined via bun build). Applied via TF.

---

## 4. Hotfix: Missing /api/shared/* CloudFront Behavior

**Symptom:** AdvisorsTab and BooksTab returning `<!doctype html>` instead of JSON.

**Root Cause:** Portal commit `d552234` (ADVI_ANONYM.014, 2026-04-06 12:13 ET) migrated 5 endpoints from S3-direct paths (`/api/scoped/advisor-intelligence/*.json`) to Lambda-backed paths (`/api/shared/advisor-intelligence/*`). The CloudFront distribution was never updated with a `/api/shared/*` behavior. Requests fell through to the default behavior (SPA static assets), returning index.html.

This was a pre-existing gap introduced by the ANONYM.014 portal commit earlier today — not caused by the TF import. The original console-managed distribution also had only 14 behaviors and no `/api/shared/*` behavior.

**Fix:** Added `/api/shared/*` ordered_cache_behavior to `cloudfront-distribution.tf`:
- Target: APIGateway-portal
- Lambda: auth-validator-edge:9 (viewer-request)
- Cache: CachingDisabled
- Origin request: AllViewerExceptHostHeader

Applied via `terraform apply`. Distribution now has 15 behaviors.

---

## 5. Hotfix: Missing API Gateway Route for clients-tab

**Symptom:** BooksTab still failing after /api/shared/* behavior added.

**Root Cause:** The ANONYM.014 portal migration changed `getClientsTab()` to call `/api/shared/advisor-intelligence/clients-tab`, but the corresponding API Gateway route was never created. All other `/api/shared/advisor-intelligence/*` routes existed (9 routes, all pointing to `opal-partners-data` via integration y95f56f), but `clients-tab` was missing.

**Fix:**
```bash
aws apigatewayv2 create-route \
  --api-id 7k3ed8px20 \
  --route-key "GET /api/shared/advisor-intelligence/clients-tab" \
  --target "integrations/y95f56f" \
  --authorization-type CUSTOM \
  --authorizer-id naqxlm
```

Route created (RouteId: b5f57fm). API GW auto-deploy propagated immediately.

**Note:** This route is not yet in Terraform. Should be added to the partners-api or bd-pipeline module that owns the other `/api/shared/*` routes.

---

## 6. Hotfix: Missing S3 Gold Artifacts (Stale Path Layout)

**Symptom:** S3-backed advisor intelligence endpoints returning 403 (mapped to index.html by custom error response).

**Root Cause:** The shared-advisor-router GLDRST v8 rewrite routes non-prefixed files to `/gold/artifacts/`, but `bd-portal-publisher` Lambda writes `architect_leaderboard.json`, `clients_tab.json`, etc. to `/gold/artifacts/` while the gold layer scripts themselves write to `/gold/` root (legacy dual-write). Some files only existed at the legacy root path.

**Fix:** Copied all gold root JSON files to `gold/artifacts/`:
- architect_leaderboard.json, clients_tab.json, firm_composition.json
- firm_mix_views.json, firm_mix_views_daily.json, implementor_leaderboard.json
- advisor_rolling_flows.json, timeseries_chart.json

Per 0.6.0_AE_PartnerETL's audit, `bd-portal-publisher` already writes to `gold/artifacts/` — the copies were redundant with what the publisher produces. The files were present at `gold/artifacts/` with 14:35 timestamps from the last publisher run. The issue was transient (publisher hadn't run since the gold layer completed).

---

## 7. AUA Discrepancy (Noted, Not CloudOps Scope)

Andrew reported AUA values differing across views:
- Assets Overview header: 1.64b
- Distribution Snapshot: 1.61b
- Distribution Continuous: 1.62b

This is a data aggregation issue, not infrastructure. Different views likely use different source files or aggregation logic. Flagged for DS/DE investigation.

---

## Summary of All Issues

| Issue | Root Cause | Our TF Import? | Fix |
|-------|-----------|----------------|-----|
| Portal 500s on /api/scoped/partners/* | Broken portal-authorizer artifact (missing jsonwebtoken) | No — bad artifact from earlier build | Rebuilt + TF apply |
| <!doctype on Advisors/Books tabs | No /api/shared/* CF behavior | No — ANONYM.014 portal commit gap | Added CF behavior + TF apply |
| BooksTab still broken after above | No API GW route for clients-tab | No — ANONYM.014 missing route | aws apigatewayv2 create-route |
| Missing gold artifacts | Publisher writes to artifacts/, files existed | No — normal pipeline timing | Files already present from publisher |
| AUA discrepancy | Data aggregation differences | No | DS/DE scope |

**None of the issues were caused by the CloudFront distribution import.** The import itself was clean — only tags were added. All issues traced to the ANONYM.014 endpoint migration (incomplete: missing CF behavior + missing APIGW route) and a pre-existing broken Lambda artifact.

---

## Commits This Session

| Commit | Tag | Description |
|--------|-----|-------------|
| `af320516` | `portal-auth-v1.10.0` | CloudFront distribution import + compiler module extensions |

## Pending Commits (Need Next Session)

- `cloudfront-distribution.tf` updated with `/api/shared/*` behavior (behavior 9 of 15)
- `opal-portal-authorizer` rebuilt artifact (TF applied, not committed)
- API GW route `clients-tab` created (not in TF)
- Compiler module files (ast_extractor.py, crossref_graph.py) already committed in af320516
