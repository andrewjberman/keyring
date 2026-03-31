# Portal PROD Deploy + CloudFront API Routing Fix -- 0.4.0_DT_ClientPlatform

**Date:** 2026-03-31
**Start Time:** 10:25 AM ET
**End Time:** 11:00 AM ET

## Objective

Merge portal DEV forward to PROD and deploy via CI pipeline. During deployment, discovered and fixed a critical CloudFront routing gap that caused all `/api/scoped/partners/*` endpoints to silently fail on production.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Merge DEV->PROD (28 commits) | Fast-forward `5712f8a..be539ab` |
| 2 | Push PROD (CI run 1) | FAILED -- ESLint: 12 unused imports in Attribution tabs |
| 3 | Fix: remove unused imports (HoldingsTab, SelectionTab) | `3349969` |
| 4 | Push PROD (CI run 2) | FAILED -- ESLint: constant truthiness in SelectionTab, more unused imports |
| 5 | Fix: collapse dead `false &&`/`true &&` branches in SelectionTab | `a39d447` (-220 lines dead code) |
| 6 | Fix: remove unused imports in FactorTilts, PortfolioManagement | `418c279` |
| 7 | Push PROD (CI run 3) | Lint PASSED, Build FAILED -- TS errors |
| 8 | Fix: restore DailyReturn/PeriodReturns types to performanceUtils.ts | `6d30153` |
| 9 | Fix: re-add ASSET_CLASS_COLORS import to HoldingsTab | same commit |
| 10 | Fix: add missing Hedge key to SEGMENT_ORDER in etf-categories.ts | same commit |
| 11 | Push PROD (CI run 4) | ALL GREEN -- Lint, Build, Deploy, Tag |
| 12 | CI auto-tagged | `portal-v2.1.18` |

## CloudFront API Routing Fix (Critical)

### Problem

The Books tab asset mix / top holdings breakdown and quarterly lookback metrics worked on localhost but NOT on production. Andrew reported the discrepancy.

### Root Cause

CloudFront distribution `EVTSA9VEHNZVH` had **no cache behavior** for `/api/scoped/partners/*` or `/api/partners`. These paths route to the `opal-partners-data` Lambda via API Gateway (`7k3ed8px20.execute-api.us-east-1.amazonaws.com`).

On localhost, `vite.config.ts` proxy forwards these paths to API Gateway directly. On production, requests hit the CloudFront **default behavior** which serves `index.html` (the SPA). The frontend received HTML instead of JSON, `response.json()` threw, and the catch handlers silently set composition/timeseries data to `null`.

### Affected Endpoints (all `/api/scoped/partners/*`)

| Function | Path | Feature |
|----------|------|---------|
| `getBooksFirmComposition` | `/api/scoped/partners/books/firm/all/composition` | N1: Firm asset mix + top holdings |
| `getBooksRelationshipComposition` | `/api/scoped/partners/books/relationship/{id}/composition` | L3: Client asset mix + top holdings |
| `getBooksAccountComposition` | `/api/scoped/partners/books/account/{id}/composition` | L4: Account asset mix + top holdings |
| `getAdvisorTimeseries` | `/api/scoped/partners/books/advisor/{id}/timeseries` | L2: Advisor AUA timeseries (quarterly bar input) |
| `getAdvisorMixTimeseries` | `/api/scoped/partners/books/advisor/{id}/mix-timeseries` | L2: Advisor mix timeseries (quarterly bar input) |
| `getMixTimeseries` | `/api/scoped/partners/books/relationship/{id}/mix-timeseries` | L3: Client mix timeseries (quarterly bar input) |
| `getFirmMixViews` | `/api/scoped/partners/books/firm/all/mix-views` | N1: Firm quarterly mix views |
| `getBooksRelationshipTimeseries` | `/api/scoped/partners/books/relationship/{id}/timeseries` | L3: Client AUA timeseries |
| `getBooksAccountTimeseries` | `/api/scoped/partners/books/account/{id}/timeseries` | L4: Account AUA timeseries |
| `getConcentrationTimeseries` | `/api/scoped/partners/books/relationship/{id}/concentration-timeseries` | L3: Concentration over time |
| `getAllowedPartners` | `/api/partners` | Partner list |

### Fix Applied

Added 2 new CloudFront cache behaviors to distribution `EVTSA9VEHNZVH`:

| Path Pattern | Origin | Cache Policy | Origin Request Policy |
|---|---|---|---|
| `/api/scoped/partners/*` | `APIGateway-portal` (7k3ed8px20) | `4135ea2d-6df8-44a3-9df3-4b5a84be39ad` | `b689b0a8-53d0-40ab-baf2-68738e2966ac` |
| `/api/partners` | `APIGateway-portal` (7k3ed8px20) | same | same |

Config cloned from existing `/api/scoped/advisor-intelligence/clients/*` behavior (same origin, same policies).

- ETag before: `EU68KLQFY69KU` -> after: `E3PD1DBIXH44AJ`
- Invalidation: `I8TLVAD1SMUQVV4DELBUV24PB4` on `/api/scoped/partners/*`
- Distribution status: **Deployed** (confirmed live)
- Behavior count: 12 -> 14

### Impact

ALL composition, timeseries, and quarterly lookback features in the Books tab are now functional on production:
- N1 (Firm): asset mix donut, top holdings, quarterly metrics bar
- L2 (Advisor): asset mix donut, top holdings, quarterly metrics bar (was COMPLETELY BROKEN on prod)
- L3 (Client): asset mix donut, top holdings, quarterly metrics bar
- L4 (Account): asset mix donut, top holdings

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Added behaviors via AWS CLI, not Terraform | Distribution EVTSA9VEHNZVH is console-managed (per ADVI_ANONYM.001 constraint). Terraform import is a separate initiative. |
| Cloned config from existing clients/* behavior | Same origin, same auth pattern, same cache/ORQ policies. Proven working. |
| Restored DailyReturn/PeriodReturns types | DEBT_1STRUN deleted them but 3 files still import them. |
| Added Hedge to SEGMENT_ORDER | Type union includes 'Hedge' but Record was missing the key, causing TS2741. |

---

## Files Modified

### Portal (DEV/PROD)

| File | Change | Committed |
|------|--------|-----------|
| `src/pages/Attribution/tabs/SelectionTab.tsx` | Remove dead false/true branches (-220 lines), unused imports | Yes -- `3349969`, `a39d447` |
| `src/pages/Attribution/tabs/HoldingsTab.tsx` | Remove unused imports, re-add ASSET_CLASS_COLORS | Yes -- `3349969`, `6d30153` |
| `src/pages/FactorTilts/panels/SummaryMetricsTable.tsx` | Remove unused AVAILABLE_PORTFOLIOS, FACTOR_KEYS imports | Yes -- `418c279` |
| `src/pages/PortfolioManagement/hooks/useFinalSummaryCalculations.ts` | Remove unused SYSTEMATIC_FACTORS import | Yes -- `418c279` |
| `src/lib/performanceUtils.ts` | Restore DailyReturn, PeriodReturns interfaces | Yes -- `6d30153` |
| `src/pages/Attribution/constants/etf-categories.ts` | Add Hedge key to SEGMENT_ORDER | Yes -- `6d30153` |

### AWS (CloudFront)

| Resource | Change | Evidence |
|----------|--------|----------|
| CloudFront EVTSA9VEHNZVH | +2 cache behaviors: `/api/scoped/partners/*`, `/api/partners` | ETag `E3PD1DBIXH44AJ`, Status: Deployed |

---

## Deployment Tags

| Pipeline | Tag | Source |
|----------|-----|--------|
| Portal | `portal-v2.1.18` | CI auto-tag on `6d30153` (PROD) |

---

## Verification

- CI pipeline run `23803216917`: all 4 jobs green (Lint, Build, S3 Deploy, Tag)
- CloudFront distribution `EVTSA9VEHNZVH`: Status Deployed, 14 behaviors
- Invalidation `I8TLVAD1SMUQVV4DELBUV24PB4`: completed

---

## Current State

> **Status:** COMPLETE

Portal `portal-v2.1.18` deployed to production. All DEBT_1STRUN lint/TS breakage resolved. CloudFront now routes `/api/scoped/partners/*` and `/api/partners` to API Gateway, fixing the Books tab composition and quarterly lookback at all drill levels (firm, advisor, client, account).

**Active branch:** portal DEV/PROD at `6d30153`, parent CLOUD

---

## Next Steps

1. **[ADVI_ANONYM project awareness]** The CloudFront behavior list is now security-relevant -- ADVI_ANONYM P1+ should inventory ALL 14 behaviors when designing pseudonymization. The new `/api/scoped/partners/*` behavior does NOT have the auth-validator-edge Lambda@Edge attached (it was cloned from the clients/* behavior which also lacks it). If the role gate needs to cover partners endpoints, a separate task is needed.
2. **[1.0.0_SA_CTO]** CloudFront distribution EVTSA9VEHNZVH remains console-managed. Consider Terraform import to prevent future drift.
3. **[0.4.0_DT_ClientPlatform]** Portal submodule is not registered in parent repo .gitmodules -- investigate and restore.

**Do NOT:**
- Assume auth-validator-edge covers `/api/scoped/partners/*` -- it only covers `/api/scoped/advisor-intelligence/*`
- Deploy CloudFront changes via Terraform until the distribution is imported
