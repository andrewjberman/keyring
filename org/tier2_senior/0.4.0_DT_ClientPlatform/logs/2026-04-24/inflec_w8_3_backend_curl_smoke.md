# Session Log — 2026-04-24 — ADVI_INFLEC.W8.3 Backend Curl Smoke

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date  | 2026-04-24 |
| TO    | ADVI_INFLEC.W8.3.dt-backend-curl-smoke |
| Authorization | GO from 2.0.0_SA_COO (20260422 + NUDGE 20260424) |
| Project | ADVI_INFLEC — Inflection Wealth Management Partner Onboarding |

---

## Summary

**PASS** — All 7 live data endpoints return HTTP 200 + `application/json` under both 49F and Inflection partner-firm JWTs. Zero 403/404 under either JWT. auth-validator-edge v7+ universal-auth claim confirmed empirically. W8.1 PROD merge cleared.

---

## Compiler Tools

### Phase 1 — `comp-routes behaviors`

2 custom error responses:
- HTTP 403 → 200 `/index.html` (ttl: 0s)
- HTTP 404 → 200 `/index.html` (ttl: 0s)

**Impact on curl methodology:** A CloudFront-swallowed 403 or 404 returns HTTP 200 with `text/html` body (SPA HTML, ~1KB). Pass criterion requires: HTTP 200 AND `Content-Type: application/json` AND JSON body prefix. An HTML body = FAIL regardless of HTTP status.

### Phase 2 — `comp-routes auth-map`

`/api/general/*` → `EDGE JWT + API GW AUTHORIZER` — auth-validator-edge viewer-request + public-data-router origin-request + cache-control-injector origin-response.

No-auth baseline: `GET /api/general/positioning/model.json` (no Authorization header) → HTTP 401 `{"error":"Missing or invalid Authorization header"}` — auth gate active and correctly rejecting unauthenticated requests.

### Phase 3 — `comp-routes trace`

No failing endpoints. Phase 3 not required (only triggered on failure per mandate).

---

## Endpoint Enumeration

Endpoints resolved from `portal/src/api/portal-proxy.ts` + component imports:

| Page | Getter | Endpoint | React Query Key | Via |
|------|--------|----------|-----------------|-----|
| /cma | getCMAAssumptions | `/api/general/capital-markets/assumptions.json` | `['cma-assumptions']` | portal-proxy |
| /cma | getOpalViews | `/api/general/capital-markets/views.json` | `['opal-views']` | portal-proxy |
| /positioning | getPositioningData | `/api/general/positioning/positioning_data.json` | `['positioning-data']` | portal-proxy |
| /positioning | getHoldingsAttribution | `/api/general/positioning/holdings_attribution_data.json` | — | portal-proxy |
| /macro | getMacroData | `/api/general/macro/macro_data.json` | — | portal-proxy |
| /macro | getVolatilityData | `/api/general/macro/volatility_data.json` | `['volatility-data']` | portal-proxy |
| /macro | getYieldCurveData | `/api/general/macro/yield_curve_fred.json` | — | api-client.ts |

**Dead code excluded:** `getModelData()` → `/api/general/positioning/model.json` — defined in portal-proxy.ts but zero callers in portal/src. S3 file missing (CF custom error returns 200+HTML). Not a product defect — function is unused.

---

## Curl Matrix

**Base URL:** `https://d2n2nzpeqf34ge.cloudfront.net`

**49F JWT:** `travis.penfield@49financial.com` (firmId=49financial, firmRole=admin)

**Inflection JWT:** `test-admin@inflectionwealthmgmt.com` (firmId=inflection, firmRole=admin) — password reset to known value via ONBOARDING.md §4 (Andrew authorized 2026-04-24)

| Endpoint | 49F HTTP | 49F CT | 49F Size | Inflection HTTP | Inflection CT | Inflection Size | Result |
|----------|----------|--------|----------|-----------------|---------------|-----------------|--------|
| `/api/general/capital-markets/assumptions.json` | 200 | application/json | 4146b | 200 | application/json | 4146b | **PASS** |
| `/api/general/capital-markets/views.json` | 200 | application/json | 5992b | 200 | application/json | 5992b | **PASS** |
| `/api/general/positioning/positioning_data.json` | 200 | application/json | 8042b | 200 | application/json | 8042b | **PASS** |
| `/api/general/positioning/holdings_attribution_data.json` | 200 | application/json | 392357b | 200 | application/json | 392357b | **PASS** |
| `/api/general/macro/macro_data.json` | 200 | application/json | 109242b | 200 | application/json | 109242b | **PASS** |
| `/api/general/macro/volatility_data.json` | 200 | application/json | 1450656b | 200 | application/json | 1450656b | **PASS** |
| `/api/general/macro/yield_curve_fred.json` | 200 | application/json | 676309b | 200 | application/json | 676309b | **PASS** |

**No-auth baseline:** HTTP 401 `{"error":"Missing or invalid Authorization header"}` — auth gate active.

Identical response sizes across both JWTs confirm `/api/general/*` is firm-agnostic data (no firm-scoped S3 paths). No data isolation issues.

---

## Acceptance Criteria

| AC | Criterion | Status |
|----|-----------|--------|
| AC1 | Endpoint enumeration matrix committed | **PASS** — 7 live endpoints (model.json dead code documented) |
| AC2 | 49F JWT — all 200 + JSON, no HTML body | **PASS** — all 7 endpoints |
| AC3 | Inflection JWT — all 200 + JSON, no HTML body | **PASS** — all 7 endpoints |
| AC4 | Any failure → CTO escalation packet | **N/A** — zero failures |
| AC5 | Session log with Compiler Tools section | **PASS** — this file |

---

## Cross-Domain

**W8.1 PROD merge:** CLEARED. Zero 403/404 under either partner JWT. auth-validator-edge v7+ universal-auth claim verified. W8.1 can proceed to PROD.

---

## Deliverables

| Deliverable | Path |
|-------------|------|
| Session log | `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-24/inflec_w8_3_backend_curl_smoke.md` |

_Written 2026-04-24 by 0.4.0_DT_ClientPlatform_
