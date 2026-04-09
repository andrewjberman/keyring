# Session Summary -- 0.4.0_DE_ClientPlatform

**Date:** 2026-04-06
**Start Time:** 2:18 PM ET
**End Time:** ongoing
**Projects:** ADVI_GLDRST, ADVI_ANONYM

**Portal DEV commits:** `a428ac5` -> `0a2c441` -> `478badb` -> `e24dab6` (revert) -> `d552234`
**Workspace CLOUD:** Lambda change to handle_books_timeseries (committed by DT as part of partners-api-v1.13.1)

---

## Work Completed

### 1. ADVI_GLDRST.003 -- Wire Pre-Computed Views (a428ac5)

CTO GO received via MCP inbox. Wired L2/L3 drill levels to server-side pre-computed
period views, eliminating client-side `deriveQuarterlyFromTimeseries()`.

- **WS1:** L2 advisor quarterly bar -> `getAdvisorMixViews()` Lambda endpoint
- **WS2:** L3 relationship quarterly bar -> `_views.json` static S3 artifact
- **WS3:** L3 composition -> static `_composition.json` with Lambda fallback
- **WS4:** Removed `deriveQuarterlyFromTimeseries()` (60 lines, 4 state vars)

Net: -52 lines. All N1/L2/L3 now use script 06b pre-computed views.

### 2. ADVI_ANONYM.014 -- PII Endpoint Migration (0a2c441, REVERTED, then d552234)

Migrated 5 PII-bearing endpoint functions from S3-direct to Lambda path:
- `getClientsTab`, `getClientDetail`, `getBooksClientDetail`, `getAdvisorBook`, `getBooksAdvisorComposition`

**First attempt (0a2c441):** Committed and merged to PROD. BROKE 5 endpoints -- Lambda
handlers did not exist yet. Task order XML had stale `status="complete"` on .012/.013
dependencies; project JSON correctly showed STAGED.

**Revert (e24dab6):** Restored all 5 to S3-direct. DT pushed to PROD (`397e6fc`).

**Second attempt (d552234):** After DT deployed .012 + .013 (partners-api-v1.13.1,
portal-auth-v1.6.0), re-executed with proper validation:
- Confirmed .012/.013 COMPLETE via `query_project` (project JSON)
- Verified all 5 Lambda route handlers exist (grep lines 1267, 1271, 1295)
- DT pushed to PROD (`de62fde`)

Also removed `isFirmAdmin` gate on Books tab data fetch (kept advisor dropdown internal-only).

### 3. ADVI_GLDRST.018 -- Market Growth Wiring (478badb)

Wired `market_growth` and `synthetic_correction` from `client_performance.parquet`
into the portal:
- Added fields to `BooksTimeseriesPoint` type (`number | null`)
- Added columns to Lambda `handle_books_timeseries()` (DT deployed as partners-api-v1.13.1)
- New `AuaDecompositionPanel` at L3: trailing 90d NNA + Market Growth + AUA Reconciliation
- Hidden when fields null (graceful for pre-.017 data)

### 4. ADVI_GLDRST.012 -- Portal E2E Validation (report only)

Code-level audit of all Advisor Intelligence API wiring. 8/9 PASS, verdict CLEAR.
- Check 8 FAIL (by design): no client-side fallback after .003 removed `deriveQuarterlyFromTimeseries`
- **Critical find:** Caught ANONYM.014 broken endpoints during this validation

---

## Postmortem: ADVI_ANONYM.014 PROD Outage

### Root Cause
Task order XML marked .012/.013 dependencies as `status="complete"` but they were
still STAGED. DE trusted the XML. Lambda had no route handlers for 3 of the 5
migrated paths (`/clients-tab`, `/clients/{key}/detail`, `/advisors/{id}/book`).

### Impact
Books tab, client detail, and advisor book returned 404 on PROD between the initial
merge and the revert (~15 minutes).

### Resolution
1. Revert committed (`e24dab6`), DT pushed to PROD
2. After .012/.013 deployed, re-executed with crossref validation
3. COO issued new rule: run `crossref_graph` before any frontend-to-backend wiring commits
4. Going forward: verify dependencies via `query_project` (project JSON), never trust task order XML status attributes

---

## Files Modified

| File | Change | Commits |
|------|--------|---------|
| portal/src/api/endpoints/advisor-intelligence.ts | Added 3 new API functions (GLDRST.003), migrated 5 PII endpoints (ANONYM.014), reverted, re-migrated | `a428ac5`, `0a2c441`, `e24dab6`, `d552234` |
| portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx | Replaced L2/L3 timeseries derivation with pre-computed views, removed deriveQuarterlyFromTimeseries, added AuaDecompositionPanel, removed isFirmAdmin gate | `a428ac5`, `0a2c441`, `478badb` |
| portal/src/pages/AdvisorIntelligence/types.ts | Added market_growth, synthetic_correction to BooksTimeseriesPoint | `478badb` |
| infra/aws/.../opal-partners-data/lambda_function.py | Added market_growth, synthetic_correction to handle_books_timeseries columns | Committed by DT (partners-api-v1.13.1) |

---

## Task Order Status

| Task Order | Project | Status |
|---|---|---|
| ADVI_GLDRST.003 | ADVI_GLDRST | COMPLETE |
| ADVI_GLDRST.012 | ADVI_GLDRST | COMPLETE |
| ADVI_GLDRST.018 | ADVI_GLDRST | COMPLETE |
| ADVI_ANONYM.014 | ADVI_ANONYM | COMPLETE |

All DE task orders for both ANONYM and GLDRST are COMPLETE. No remaining DE work on either project.

---

## Next Steps

1. **No unblocked DE work on ANONYM or GLDRST** -- remaining GLDRST items are AE/DT chain (.009 -> .013 -> .010 -> .014)
2. **DEBT_1STRUN.001** (tech debt scan) is pending but deprioritized per Andrew
3. **Browser validation** of Checks 1-9 (GLDRST.012) should be done when an interactive session is available
