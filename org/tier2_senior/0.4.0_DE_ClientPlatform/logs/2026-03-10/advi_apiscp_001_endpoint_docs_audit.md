# ADVI_APISCP.001: Endpoint Mapping Docs Audit — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-10
**Portal DEV commits:** `0a759de`
**Workspace CLOUD commit:** pending (to be committed by DT)

## Objective

Update `endpoint-mapping.ts` and `advisor-intelligence.ts` to accurately reflect the new
scoped routing architecture after Lambda@Edge v4 deploys. Audit frontend API calls for
correctness. Ensure no frontend code references the eliminated `opal-data-portal-v2/json/advisor-intelligence` path.

---

## Work Completed

### 1. endpoint-mapping.ts — SCOPED Comment Fix (Req 1)

Fixed line 13 in the Path Structure header comment:

| Before | After |
|--------|-------|
| `/api/scoped/* -> S3 origin (s3://opal-data-portal-v2/json/) via shared-advisor-router` | `/api/scoped/* -> S3 origin (s3://opal-data-{firmId}/gold/) via shared-advisor-router (dynamic per-firm)` |

### 2. endpoint-mapping.ts — SCOPED Section Added (Req 2)

Added a 32-line documentation comment block to `ENDPOINT_MAPPING` before the PRIVATE ENDPOINTS
section. The block explains:
- shared-advisor-router constructs `opal-data-{firmId}` from `X-Firm-Id` header (injected by auth-validator-edge)
- URI rewrite: `/api/scoped/advisor-intelligence/*` -> `/gold/*`
- Full enumeration of static file calls (no firmId query param) vs dynamic API calls (firmId query param)
- Pointer to `advisor-intelligence.ts` for the full client

No object entry added — the routing is comment-only because advisor-intelligence does not
participate in the `ENDPOINT_MAPPING` type system (routed via separate Lambda@Edge, not `public-data-router`).

### 3. advisor-intelligence.ts Audit (Req 3)

**Static file calls (X-Firm-Id from header — no firmId query param):**

| Function | URL | firmId? |
|----------|-----|---------|
| `getHeaderSummary` | `/api/scoped/.../summary/header_metrics.json` | No — correct |
| `getHeaderMetrics` | `/api/scoped/.../summary/header_metrics.json` | No — correct |
| `getPartnerAnalytics` | `/api/scoped/.../partner_analytics/header_metrics_{suffix}.json` | No — correct |
| `getCumulativeChart` | `/api/scoped/.../timeseries_chart.json` | No — correct |
| `getClientsTab` | `/api/scoped/.../clients_tab.json` | No — correct |
| `getClientDetail` | `/api/scoped/.../clients/{clientKey}.json` | No — correct |
| `getArchitectLeaderboard` | `/api/scoped/.../architect_leaderboard.json` | No — correct |
| `getImplementorLeaderboard` | `/api/scoped/.../implementor_leaderboard.json` | No — correct |
| `getAdvisorBook` | `/api/scoped/.../advisors/{advisorId}/book.json` | No — correct |
| `getAdvisorRollingFlows` | `/api/scoped/.../advisor_rolling_flows.json` | No — correct |
| `getBooksClientDetail` | `/api/scoped/.../clients/{clientKey}.json` | No — correct |

**Dynamic calls (firmId query param — API Gateway-backed):**

| Function | URL | firmId? |
|----------|-----|---------|
| `getTimeSeries` | `/api/scoped/.../timeseries/${dimension}?firmId=` | Yes — correct |
| `getSnapshot` | `/api/scoped/.../snapshots/${dimension}?firmId=` | Yes — correct |
| `getFilters` | `/api/scoped/.../filters?firmId=` | Yes — correct |
| `getClientGrowth` | `/api/scoped/.../clients/growth?firmId=` | Yes — correct |
| `getTaxBreakdown` | `/api/scoped/.../clients/tax-breakdown?firmId=` | Yes — correct |
| `getTaxDeferredCandidates` | `/api/scoped/.../clients/tax-deferred?firmId=` | Yes — correct |

**Separation is correct.** Static files use header-based routing; dynamic calls pass firmId
explicitly via query string as confirmed by PRD section 5.2.

### 4. Stale Comments Fixed in advisor-intelligence.ts

Two outdated comments corrected:

| Function | Old Comment | New Comment |
|----------|-------------|-------------|
| `getAdvisorRollingFlows` | "opal-data-portal-v2 bucket" | "shared-advisor-router routes to opal-data-{firmId}/gold/" |
| `getSnapshot` | "Routes to opal-partners-data Lambda via API Gateway. firmId is passed as query param; will be removed once Lambda reads from portal-authorizer context" | "Dynamic API call — firmId is passed as query param. Routes via CloudFront /api/scoped/ -> shared-advisor-router -> opal-data-{firmId}/gold/" |

### 5. opal-data-portal-v2 Reference Audit

Grep of `portal/src` for `opal-data-portal-v2` found zero occurrences in advisor-intelligence
request URLs. The one comment hit (`getAdvisorRollingFlows`) is fixed in this commit.

The remaining `opal-data-portal-v2` references in `portal/src` are in other endpoints/pages
(market, sentiment, macro, positioning, etc.) — all correctly document GENERAL data written
to `opal-data-portal-v2/json/`. These are correct and untouched.

### 6. TypeScript Validation

`bunx tsc -b --noEmit` — clean, no errors.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| SCOPED section is comment-only in ENDPOINT_MAPPING (no typed object entry) | advisor-intelligence does not use ENDPOINT_MAPPING at runtime; adding a typed entry would require adding `endpoints` key which is empty — misleading. Comments provide documentation value without false structure. |
| Leave getSnapshot firmId query param in place | PRD 5.2 lists `snapshots/{dimension}?firmId=` as "dynamic dimension call" — firmId param is intentional. Removing it would require coordinating with backend Lambda. |
| Do not modify getSnapshot URL structure | This is "docs + audit only". Routing correctness for dynamic calls is DT/backend scope. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/api/endpoint-mapping.ts` | Fix SCOPED comment + add SCOPED documentation block | Yes — portal DEV `0a759de` |
| `portal/src/api/endpoints/advisor-intelligence.ts` | Fix `getAdvisorRollingFlows` stale bucket comment; fix `getSnapshot` stale Lambda comment | Yes — portal DEV `0a759de` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_APISCP.001.endpoint-mapping-docs-audit.md` | status -> complete | No — local only |

---

## Blockers

Post-deploy verification (req 4) blocked on DT deploying Lambda@Edge v4.
Evidence: `0.4.0_DT_ClientPlatform` task order `ADVI_APISCP.001.lambda-edge-v4-dynamic-routing`
is status=pending. No 2026-03-10 DT logs exist. DT has not started deploy.

---

## Current State

**Status:** COMPLETE (reqs 1-3 done; req 4 blocked on DT deploy)
**Active branch:** portal `DEV`, workspace `CLOUD`

Reqs 1-3 committed at `0a759de` on portal DEV. `endpoint-mapping.ts` now correctly describes
SCOPED routing as `opal-data-{firmId}/gold/` (dynamic per-firm) with a full enumeration of static
vs dynamic advisor-intelligence calls. All stale `opal-data-portal-v2` references in
`advisor-intelligence.ts` removed from comments. No request URLs ever directly referenced
`opal-data-portal-v2/json/advisor-intelligence` — acceptance criterion 2 confirmed clean.
Req 4 (browser DevTools network verification) requires DT to deploy Lambda@Edge v4 first.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Deploy Lambda@Edge v4** — task order `ADVI_APISCP.001.lambda-edge-v4-dynamic-routing` is pending. DT must complete preflight (requirements 0a-0c) and deploy.
2. **[0.4.0_DT_ClientPlatform] Push portal DEV** — commits `9c1881a` + `3367cd8` + `1433d2e` + `0a759de` pending push. DT QA gate.
3. **[0.4.0_DT_ClientPlatform] Commit org changes to CLOUD** — this session log + task order status updates.
4. **[0.4.0_DE_ClientPlatform] Post-deploy verification (req 4)** — after DT deploys, load AdvisorIntelligence in dev browser, confirm Network tab shows `data_as_of` matching current gold date for all scoped responses. Then mark task order fully complete.

**Do NOT:**
- Remove firmId query params from dynamic calls (`getTimeSeries`, `getSnapshot`, `getFilters`, etc.) — these are intentional per PRD
- Add firmId query params to static file calls — X-Firm-Id header handles routing
