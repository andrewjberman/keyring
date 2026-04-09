# ADVI_GLDRST.021 -- Migrate Portal S3 Reads to New Structured Paths

**Date:** 2026-04-06
**Agent:** 0.4.0_DE_ClientPlatform
**Project:** ADVI_GLDRST
**Status:** COMPLETE

---

## Summary

Migrated all S3-direct portal read paths from legacy flat `gold/` layout to the new
structured layout defined in `data/black_diamond/scripts/gold/lib/s3_layout.py`.

CloudFront behavior (`/api/scoped/advisor-intelligence/*` -> `gold/*`) is a simple
prefix swap -- no CF config changes needed. Updating the URL suffix is sufficient.

## Changes (portal/src/api/endpoints/advisor-intelligence.ts)

### Artifact paths (flat -> gold/artifacts/)

| Function | Old suffix | New suffix |
|---|---|---|
| getHeaderSummary | `summary/header_metrics.json` | `artifacts/summary/header_metrics.json` |
| getHeaderMetrics | `summary/header_metrics.json` | `artifacts/summary/header_metrics.json` |
| getPartnerAnalytics | `partner_analytics/header_metrics_*.json` | `artifacts/partner_analytics/header_metrics_*.json` |
| getCumulativeChart | `timeseries_chart.json` | `artifacts/timeseries_chart.json` |
| getArchitectLeaderboard | `architect_leaderboard.json` | `artifacts/architect_leaderboard.json` |
| getImplementorLeaderboard | `implementor_leaderboard.json` | `artifacts/implementor_leaderboard.json` |
| getAdvisorRollingFlows | `advisor_rolling_flows.json` | `artifacts/advisor_rolling_flows.json` |

### Entity paths (gold/client_timeseries/ -> gold/entities/clients/)

| Function | Old suffix | New suffix |
|---|---|---|
| getRelationshipMixViews | `client_timeseries/{id}_views.json` | `entities/clients/{id}_views.json` |
| getRelationshipCompositionStatic | `client_timeseries/{id}_composition.json` | `entities/clients/{id}_composition.json` |

### JSDoc updates

- `getAdvisorMixViews`: `gold/advisors/{id}/mix.json` -> `gold/entities/advisors/{id}/mix.json`
- `getRelationshipMixViews`: `gold/client_timeseries/` -> `gold/entities/clients/`
- `getRelationshipCompositionStatic`: `gold/client_timeseries/` -> `gold/entities/clients/`

## Not changed (Lambda-routed, no S3 path in portal)

- `getClientsTab` -- Lambda via `/clients-tab?firmId=`
- `getClientDetail` -- Lambda via `/clients/{key}/detail?firmId=`
- `getAdvisorBook` -- Lambda via `/advisors/{id}/book?firmId=`
- `getBooksClientDetail` -- Lambda via `/clients/{key}/detail?firmId=`
- `getBooksAdvisorComposition` -- Lambda via `/books/advisor/{id}/composition?firmId=`
- `getFilters` -- Lambda via `/filters?firmId=`
- All timeseries/composition/mix-timeseries -- Lambda via `/api/scoped/partners/`

## Verification

- `grep` for all old path patterns across `portal/src/`: zero matches
- `bunx tsc -b`: clean, no errors
- CloudFront: no config changes needed (prefix swap handles new subdirectories)

---

## Next Steps

1. **[DevOps] Push portal DEV** and merge to PROD after AE confirms new S3 paths are populated
2. **This unblocks GLDRST.010** -- old key cleanup / dual-write removal in gold scripts
