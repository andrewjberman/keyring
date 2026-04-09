# Portal Auth & Data Serving Flow Reference
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Project:** ADVI_GLDOPS (reference documentation)

---

## Summary

Complete mapping of how gold layer data reaches the portal: the two serving paths
(direct S3 via CloudFront vs Lambda proxy), the auth chain, and which S3 files
map to which API routes.

---

## Architecture Overview

```
Domain:       opalinvest.dev (+ www.opalinvest.dev)
CloudFront:   EVTSA9VEHNZVH (d2n2nzpeqf34ge.cloudfront.net)
Terraform:    infra/aws/terraform/portal-auth/cloudfront-distribution.tf
```

---

## Auth Flow (NO Cognito -- custom JWT throughout)

### Layer 1: CloudFront Edge -- auth-validator-edge

| | |
|---|---|
| **Type** | Lambda@Edge (viewer-request) |
| **Source** | `infra/aws/lambda-edge/auth-validator-edge/index.mjs` |
| **Fires on** | Every request EXCEPT `/auth/*` and `OPTIONS` |
| **Validates** | JWT token (RS256) using public key from AWS Secrets Manager (`opal/auth/jwt-public-key`) |
| **Injects headers** | `X-User-Email`, `X-User-Name`, `X-User-Tier`, `X-User-Role`, `X-Firm-Id`, `X-User-Type`, `X-Origin-Verify` |
| **On failure** | Returns 401 (blocks request at edge, never reaches origin) |

### Layer 2: API Gateway -- opal-portal-authorizer

| | |
|---|---|
| **Type** | CUSTOM authorizer (ID `naqxlm` on API GW `7k3ed8px20`) |
| **Source** | `infra/aws/users/lambda/portal-authorizer/` (Node.js ESM) |
| **Fires on** | All `/api/scoped/*` and `/api/partners` routes that hit the API GW origin |
| **Validates** | JWT token (same as edge, but independent validation) |
| **Returns to Lambda context** | `allowedFirmIds`, `email`, `tier`, `role`, `firmId`, `advisorId` |
| **NOT Cognito** | This is a custom authorizer. No Cognito user pool involved. |

### Layer 3: Lambda-level checks

| Lambda | Check |
|--------|-------|
| `opal-partners-data` | Validates `firmId` query param against `allowedFirmIds` from authorizer context |
| `bd-client-detail` | Requires `role === 'admin'` |
| `portfolio-optimization-loader` | Requires `X-User-Tier === 'internal'` (edge header) |

### Token Lifecycle

| Step | Mechanism |
|------|-----------|
| **Login** | `POST /auth/login` -> returns JWT access token + sets refresh cookie |
| **Storage** | `localStorage.accessToken` in browser |
| **Attach** | Every request: `Authorization: Bearer {token}` header |
| **Refresh** | `POST /auth/refresh` (cookie-based, proactive at 10-minute token age) |
| **Context** | `portal/src/contexts/AuthContext.tsx` manages lifecycle |

---

## CloudFront Origins (5)

| # | Origin ID | Target | Description |
|---|-----------|--------|-------------|
| 1 | `S3-opalinvest-portal` | S3 bucket (OAI) | SPA static assets (default) |
| 2 | `S3-opal-data-portal-v2-json` | S3 bucket (OAC `E24L6358YRRKAE`) | Yang, market overview, benchmarks, SmartX JSON |
| 3 | `S3-opal-data-bd` | S3 bucket (OAI `E139998VWH0PD`) | Gold layer advisor intelligence |
| 4 | `APIGateway-portal` | `7k3ed8px20.execute-api.us-east-1.amazonaws.com` | Portal API (partners, auth, scoped routes) |
| 5 | `APIGateway-portfolio` | `f61h681z9g.execute-api.us-east-1.amazonaws.com/prod` | Portfolio management API |

---

## Path Routing Table

| Path Pattern | Origin | Auth Layers | Edge Functions |
|---|---|---|---|
| `/*` (default) | S3 SPA | None | None |
| `/auth/*` | API GW portal | None | None |
| `/api/general/*` | S3 portal-v2 | JWT edge | auth-validator-edge, public-data-router, cache-control-injector |
| `/api/general/json-tiered/*` | S3 portal-v2 | JWT edge | auth-validator-edge, public-data-router, cache-control-injector |
| `/api/scoped/advisor-intelligence/artifacts/*` | S3 opal-data-bd | JWT edge | auth-validator-edge, shared-advisor-router |
| `/api/scoped/advisor-intelligence/entities/*` | S3 opal-data-bd | JWT edge | auth-validator-edge, shared-advisor-router |
| `/api/scoped/advisor-intelligence/*.json` | S3 opal-data-bd | JWT edge | auth-validator-edge, shared-advisor-router |
| `/api/scoped/advisor-intelligence/*` (catch-all) | API GW portal | JWT edge + API GW authorizer | auth-validator-edge |
| `/api/scoped/partners/*` | API GW portal | JWT edge + API GW authorizer | auth-validator-edge |
| `/api/partners` | API GW portal | JWT edge + API GW authorizer | auth-validator-edge |
| `/api/private/portfolio*` | API GW portfolio | JWT edge (tier=internal) | auth-validator-edge |
| `/api/private/*` | API GW portal | JWT edge | auth-validator-edge |
| `/v1/*` | API GW portal | JWT edge | auth-validator-edge |
| `/api/scoped/security-scanner/*` | API GW portal | None | None |
| `/api/scoped/data-refresh/*` | API GW portal | JWT edge | auth-validator-edge |
| `/api/general/trades/*` | API GW portal | JWT edge | auth-validator-edge |

---

## Two Serving Paths for Gold Data

### Path A: Direct S3 (fast path, no Lambda)

```
Browser --> CloudFront --> auth-validator-edge (JWT) --> shared-advisor-router
  --> rewrites URL to gold/ S3 key --> S3 opal-data-bd --> response
```

**Edge function `shared-advisor-router`** (`infra/aws/lambda-edge/shared-advisor-router/index.mjs`):
- Intercepts `/api/scoped/advisor-intelligence/artifacts/*` and `/entities/*`
- Rewrites to the corresponding S3 key under `gold/`
- Routes to firm-specific bucket based on `X-Firm-Id` header
- No Lambda invocation at all -- pure S3 read through CloudFront

**Files served this way (all pre-computed JSON from gold runner):**

| S3 Key | Producing Script |
|--------|-----------------|
| `gold/artifacts/timeseries_chart.json` | D_00 |
| `gold/artifacts/architect_leaderboard.json` | D_00 |
| `gold/artifacts/employee_leaderboard.json` | D_00 |
| `gold/artifacts/clients_tab.json` | D_00 |
| `gold/artifacts/summary/header_metrics.json` | D_00 |
| `gold/artifacts/filters/dimensions.json` | D_00 |
| `gold/artifacts/snapshots/aua_by_architect.json` | D_00 |
| `gold/artifacts/snapshots/aua_by_tax_status.json` | D_00 |
| `gold/artifacts/snapshots/aua_by_state.json` | D_00 |
| `gold/artifacts/snapshots/aua_by_region.json` | D_00 |
| `gold/artifacts/advisor_rolling_flows.json` | D_00 |
| `gold/artifacts/advisor_fee_efficiency.json` | C_08 |
| `gold/artifacts/implementor_leaderboard.json` | D_02 |
| `gold/artifacts/firm_mix_views.json` | D_03 |
| `gold/artifacts/firm_mix_views_daily.json` | D_03 |
| `gold/artifacts/partner_analytics/header_metrics_quarterly.json` | D_01 |
| `gold/artifacts/partner_analytics/header_metrics_monthly.json` | D_01 |
| `gold/artifacts/partner_analytics/header_metrics_annual.json` | D_01 |
| `gold/entities/advisors/{id}/book.json` | D_02 |
| `gold/entities/advisors/{id}/timeseries.json` | D_02 |
| `gold/entities/advisors/{id}/mix_timeseries.json` | D_02/D_03 |
| `gold/entities/advisors/{id}/composition.json` | D_03 |
| `gold/entities/advisors/{id}/mix.json` | D_03 |
| `gold/entities/advisors/{id}/mix_daily.json` | D_03 |
| `gold/entities/clients/{rel_id}/detail.json` | D_02 |
| `gold/entities/clients/{rel_id}/aua_timeseries.json` | D_02 |
| `gold/entities/clients/{rel_id}.json` | C_06 |
| `gold/entities/clients/{rel_id}_views.json` | C_06 |
| `gold/entities/clients/{rel_id}_composition.json` | D_03 |
| `gold/entities/accounts/{acct_id}/aua_timeseries.json` | D_02 |
| `gold/views/firm_composition.json` | D_03 |

### Path B: Lambda Proxy (dynamic path)

```
Browser --> CloudFront --> auth-validator-edge (JWT)
  --> API GW 7k3ed8px20 --> opal-portal-authorizer (JWT, firm scoping)
  --> Lambda (opal-partners-data) --> reads S3 / computes --> response
```

**Used for:** Routes that need firm-scoping logic, parquet reads, or fallback logic.

**Lambda: opal-partners-data** (`infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`)

| API Route | S3 File Read | Notes |
|-----------|-------------|-------|
| `GET /api/scoped/advisor-intelligence/timeseries/{dim}` | `gold/timeseries/nna_by_{dim}.json` | 11 dimensions |
| `GET /api/scoped/advisor-intelligence/snapshots/{dim}` | `gold/artifacts/snapshots/aua_by_{dim}.json` | 7 dimensions |
| `GET /api/scoped/advisor-intelligence/filters` | `gold/artifacts/filters/dimensions.json` | |
| `GET /api/scoped/advisor-intelligence/clients-tab` | `gold/artifacts/clients_tab.json` | |
| `GET /api/scoped/advisor-intelligence/clients/{id}/detail` | `gold/entities/clients/{id}/detail.json` | |
| `GET /api/scoped/advisor-intelligence/clients/growth` | `gold/artifacts/clients_tab.json` (filtered) | |
| `GET /api/scoped/advisor-intelligence/clients/tax-breakdown` | `gold/artifacts/clients_tab.json` (filtered) | |
| `GET /api/scoped/advisor-intelligence/summary` | `gold/artifacts/summary/header_metrics.json` | |
| `GET /api/scoped/advisor-intelligence/partner-analytics` | `gold/artifacts/partner_analytics/hm_{gran}.json` | |
| `GET /api/scoped/advisor-intelligence/advisors/{id}/book` | `gold/entities/advisors/{id}/book.json` | |
| `GET /api/scoped/advisor-intelligence/advisors/{id}/mix-views` | `gold/entities/advisors/{id}/mix.json` | |
| `GET /api/scoped/partners/books/relationship/{id}/timeseries` | `gold/entities/clients/{id}/aua_timeseries.json` | Falls back to `client_performance.parquet` |
| `GET /api/scoped/partners/books/account/{id}/timeseries` | `gold/entities/accounts/{id}/aua_timeseries.json` | Falls back to `account_performance.parquet` |
| `GET /api/scoped/partners/books/*/composition` | `gold/snapshots/holdings_lots/{date}.parquet` | |
| `GET /api/scoped/partners/books/firm/all/composition` | `gold/views/firm_composition.json` | |
| `GET /api/scoped/partners/books/firm/all/mix-views` | `gold/artifacts/firm_mix_views.json` | |
| `GET /api/scoped/partners/books/advisor/{id}/timeseries` | Advisor-level timeseries | |
| `GET /api/scoped/partners/books/advisor/{id}/mix-timeseries` | Advisor mix timeseries | |
| `GET /api/scoped/partners/books/advisor/{id}/composition` | Advisor composition | |
| `GET /api/health/advisor-intelligence` | Health check | |

**Note on overlap:** Some routes in Path B serve the same files available via Path A (e.g., `clients_tab.json`, `header_metrics.json`). The Lambda path exists because it enforces `allowedFirmIds` scoping at the authorizer level. The direct S3 path relies on `shared-advisor-router` for firm routing.

---

## Other Lambdas Serving Portal Data

### opal-portal-data-proxy (legacy v1)

| | |
|---|---|
| **Routes** | All `/v1/*` (market, AUM, benchmarks, positioning, valuation, correlations, macro, factor-tilts, CMA, news, trending) |
| **Reads** | S3 `opal-data-portal-v2/json/*`, DynamoDB `opal-portal-market-data` |
| **Auth** | JWT edge only |

### bd-client-detail

| | |
|---|---|
| **Route** | `GET /api/shared/advisor-intelligence/clients/{clientKey}.json` |
| **Reads** | `gold/clients/{relationship_id}.json` |
| **Auth** | JWT edge + API GW authorizer + `role === 'admin'` |

### portfolio-optimization-loader

| | |
|---|---|
| **Route** | `/api/private/portfolio*` |
| **Reads** | `s3://opal-data-pm/` (alpha.pkl, optimization.xlsx) |
| **Auth** | JWT edge + `X-User-Tier === 'internal'` |

---

## Non-Gold Pipeline Data (also served to portal)

These Lambdas write to S3 buckets that CloudFront serves via the `opal-data-portal-v2-json` origin:

| Lambda | Writes To | Portal Path |
|--------|----------|-------------|
| `yang-model-portfolio-benchmarks` | `opal-data-portal-v2/json/benchmarks/*.json` | `/api/general/json/benchmarks/*` |
| `smartx-ingestion-pipeline` | `opal-data-portal-v2/json/portfolios/*.json` | `/api/general/json/portfolios/*` |
| `market-overview-tiered-generator` | `opal-data-portal-v2/json-tiered/market-overview/**` | `/api/general/json-tiered/market-overview/**` |

---

## S3 Buckets in Play

| Bucket | Purpose | Access Method |
|--------|---------|---------------|
| `opalinvest-portal` | SPA static assets (HTML/JS/CSS) | CloudFront default origin (OAI) |
| `opal-data-portal-v2` | Yang, market, benchmarks, SmartX JSON | CloudFront S3 origin (OAC) |
| `opal-data-bd` | Gold layer: all advisor intelligence | CloudFront S3 origin (OAI) + Lambda reads |
| `opal-data-smartx-v2` | SmartX raw exports | Lambda reads only |
| `opal-data-pm` | Portfolio management data | Lambda reads only |

---

## Key Source Files

| File | Purpose |
|------|---------|
| `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` | CloudFront distribution + origins |
| `infra/aws/terraform/portal-auth/cloudfront.tf` | Cache policies |
| `infra/aws/terraform/partners-api/api-gateway.tf` | API GW routes (partners-api) |
| `infra/aws/terraform/bd-pipeline/api-gateway.tf` | API GW routes (bd-pipeline) |
| `infra/aws/lambda-edge/auth-validator-edge/index.mjs` | Edge JWT validator |
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | S3 path rewriter for gold data |
| `infra/aws/users/lambda/portal-authorizer/` | API GW custom authorizer |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | Main data-serving Lambda |
| `portal/src/api/api-client.ts` | Frontend API client |
| `portal/src/api/endpoint-mapping.ts` | Frontend endpoint map |
| `portal/src/api/endpoints/advisor-intelligence.ts` | Advisor intelligence API calls |
| `portal/src/contexts/AuthContext.tsx` | Frontend auth context |
| `data/black_diamond/scripts/gold/lib/s3_layout.py` | S3 key registry for all gold scripts |

---

## Files Modified

None -- reference documentation only.

---

## Current State

Reference log. No code changes.
