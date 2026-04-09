# ADVI_ANONYM.014: Migrate PII Endpoints from S3-Direct to Lambda -- 0.4.0_DE_ClientPlatform

**Date:** 2026-04-06
**Task Order:** ADVI_ANONYM.014.de-pii-endpoint-migration.md
**Project:** ADVI_ANONYM

**Portal DEV commit:** `0a2c441`

---

## Objective

Migrate 5 PII-bearing endpoint functions from S3-direct path (shared-advisor-router)
to Lambda path (opal-partners-data) for pseudonymization coverage. Remove isFirmAdmin
gate on Books tab data fetching while keeping advisor dropdown internal-only.

---

## Work Completed

### 1. PII Endpoint Migrations -- COMPLETE

| Function | Old Path (S3-direct) | New Path (Lambda) |
|---|---|---|
| `getClientsTab` | `/api/scoped/advisor-intelligence/clients_tab.json` | `/api/shared/advisor-intelligence/clients-tab?firmId={firmId}` |
| `getClientDetail` | `/api/scoped/advisor-intelligence/clients/{key}.json` | `/api/shared/advisor-intelligence/clients/{key}/detail?firmId={firmId}` |
| `getBooksClientDetail` | `/api/scoped/advisor-intelligence/clients/{key}.json` | `/api/shared/advisor-intelligence/clients/{key}/detail?firmId={firmId}` |
| `getAdvisorBook` | `/api/scoped/advisor-intelligence/advisors/{id}/book.json` | `/api/shared/advisor-intelligence/advisors/{id}/book?firmId={firmId}` |
| `getBooksAdvisorComposition` | `/api/scoped/advisor-intelligence/advisors/{id}/composition.json` | `/api/scoped/partners/books/advisor/{id}/composition?firmId={firmId}` |

Each migrated function uses `LAMBDA_FIRM_ID` mapping (bd -> 49financial) and appends
`?firmId=` query parameter. Default firmId for non-override calls: `49financial`.

### 2. Non-PII Endpoints Confirmed on S3-Direct -- VERIFIED

These stay untouched (employee data / aggregates, no client PII):
- `getHeaderSummary`, `getHeaderMetrics` -- firm-level aggregates
- `getArchitectLeaderboard`, `getImplementorLeaderboard` -- employee names only
- `getAdvisorRollingFlows` -- advisor-level flows
- `getCumulativeChart` -- timeseries (no client PII)

### 3. isFirmAdmin Gate Removal -- COMPLETE

Removed `!isFirmAdmin` from N1 data fetch guard (ClientsTab.tsx line 262).
Removed `isFirmAdmin` from useEffect dependency array.
Kept advisor dropdown gate at line 614: `{isFirmAdmin && (` -- internal-only per Andrew.

### 4. Type Safety -- VERIFIED

`bunx tsc -b` passes with zero errors. Lambda endpoints return same JSON shape as
S3-direct (same gold files served through opal-partners-data), so no interface changes needed.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/api/endpoints/advisor-intelligence.ts | Migrated 5 PII functions from S3-direct to Lambda path | Yes - DEV `0a2c441` |
| portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx | Removed isFirmAdmin gate on data fetch | Yes - DEV `0a2c441` |

---

## Current State

**Status:** COMPLETE
**Active branch:** portal DEV (commit `0a2c441`)

---

## Next Steps

1. **[DevOps] Push portal DEV and merge to PROD** when authorized
2. **[Dashboard Engineer] Browser verification** after deploy -- confirm Lambda responses match S3-direct shapes, pseudonymization active for partner users
