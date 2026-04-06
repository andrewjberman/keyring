# ETFS_SECIDX.003 Recommendations Report -- 0.2.0_DS_PortfolioAnalytics

**Date:** 2026-04-06
**Start Time:** 16:49 ET
**End Time:** 17:05 ET
**Task Order:** ETFS_SECIDX.003.ds-recommendations-report.md
**GO Signal:** COO 2026-04-06T16:49Z

## Objective

Synthesize DS .001 inventory + DE .002 portal audit into D4 recommendations report
for CTO Phase 1 planning.

---

## Work Completed

### D4: Recommendations Report (ETFS_SECIDX_recommendations.md)

Produced 6-section report covering:

1. **Gap Summary:** 102 securities with zero portal coverage, 10 of 18 indices not in portal,
   7 new data field categories needed (holding weights, holding returns, screening fundamentals,
   trade analysis, FX impact, dividend calendar, competitive funds).

2. **Existing Infrastructure Reuse:** 
   - Tier 1 (config): Add M1WDUDY/MXWDU/MXUSAHDV to cloudfront_market_generator, fix 6 DQ issues
   - Tier 2 (moderate): 3 new yang-pattern Lambdas (etf-holdings, etf-performance, etf-attribution)
   - Cannot extend: real-time Bloomberg/FactSet feeds require licensing + API infrastructure

3. **New Pipeline Needs:** Proposed `etf-pipeline` with Excel upload trigger -> 3 generator Lambdas
   -> JSON to S3 -> CloudFront. Follows exact yang-pipeline pattern.

4. **Proposed Portal Pages:** ETF Overview, Holdings, Performance, Attribution (Phase 1);
   Screening, Trade Analysis, IDVZ-specific, Competitive Funds (Phase 2).

5. **Priority Ordering:** 18 items in 4 tiers. Phase 1 core = 8 items (DQ fixes + 3 Lambdas + portal nav).

6. **PFDE Status:** Missing from zip, portal has tab placeholder, same schema when provided.

### Key Recommendation

Phase 1 should use Excel upload (same as yang attribution_excel), NOT Bloomberg/FactSet APIs.
This gives 80% of the dashboard value with 20% of the complexity. Real-time feeds are Phase 2.

---

## Files Modified

| File | Change |
|------|--------|
| `data/etf_dashboards/ETFS_SECIDX_recommendations.md` | D4 recommendations report |
| `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/ETFS_SECIDX.003.ds-recommendations-report.md` | Status: staged -> pending -> complete |
| `org/projects/ETFS_SECIDX.json` | Phase updated to "Phase 0 COMPLETE" |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD
**ETFS_SECIDX Phase 0:** All 3 task orders complete (.001 DS, .002 DE, .003 DS).

---

## Next Steps

1. **[CTO] Issue Phase 1 PRD** based on D4 recommendations (Tier 1 + Tier 2 items)
2. **[Andrew] Provide PFDE dashboard** -- blocks full ETF fund coverage
3. **[DE] Fix DQ-001 through DQ-006** (tickerRegistry cleanup -- can be independent task order)
4. **[DS] Write ETF holdings parser** when Phase 1 task orders are issued
