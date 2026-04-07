# DEBT_1STRUN — Pod 2 (PortfolioAnalytics) Aggregate Report

**Agent:** 0.2.5_RD_Macroeconomics (covering DE 0.2.0)
**Date:** 2026-04-07
**Scope:** Pod 2 shared infrastructure scan + aggregation of all Pod 2 RD/DS scans

---

## Part 1: DE Shared Infrastructure Scan

Scope: `portal/src/api/`, `portal/src/hooks/`, `portal/src/lib/`, shared types/components used by Pod 2 pages (Positioning, Attribution, FactorTilts, Valuation, Macroeconomics, Correlation).

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| DE-1 | api/portal-proxy.ts | 52-56 | C1 Dead | Medium | `clearCache()` is a no-op function ("Kept for backwards compatibility"). No caller exists in the codebase. Dead export. |
| DE-2 | api/portal-proxy.ts | 87-95 | C2 Deprecated | High | 401 redirect logic commented out with "TEMPORARILY DISABLED - Causing infinite redirect loop for Model Portfolios". Stale workaround -- the underlying auth issue should be fixed and the redirect re-enabled or permanently removed. |
| DE-3 | api/portal-proxy.ts | 247-264 | C2 Deprecated | Medium | `getAUMSummary()` has DEMO mode: uses public endpoint instead of private auth-required endpoint. TODO comments reference a "revert to private for production" that was never done. |
| DE-4 | api/portal-proxy.ts | 87,247,258 | C2 Deprecated | Low | Emoji characters in comments/code violate CLAUDE.md rule 13. |
| DE-5 | api/endpoint-mapping.ts | 136-137 | C2 Deprecated | Low | `factorTilts.data` endpoint marked "(deprecated)" in notes but still defined. Legacy entry that should be removed once all consumers use tiered endpoints. |
| DE-6 | api/endpoint-mapping.ts | 242-243 | C2 Deprecated | Low | `marketOverviewTiered.tickerTimeSeries` marked "(deprecated - use tickerDetails instead)" but still defined. |
| DE-7 | api/portal-proxy.ts | 164-167 | C5 Orphaned | Medium | `getMarketDataForTicker()` -- grep shows no caller in the portal codebase. Dynamic single-ticker fetch that no page uses. |
| DE-8 | api/portal-proxy.ts | 180-187 | C5 Orphaned | Medium | `getMarketDataByEntityType()` -- grep shows no caller. Dead API function. |
| DE-9 | hooks/useYangData.ts | - | C1 Dead | Low | Need to verify usage -- hook may be superseded by `useDataSource`/`useDataFreshness`. |
| DE-10 | hooks/useRSIValues.ts | - | C3 Drift | Low | RSI hook exists alongside `marketOverviewTiered.rsiSummary` endpoint. Verify they're not duplicating fetch logic. |
| DE-11 | lib/chartColors.ts (PALETTE) | 17-87 | C3 Drift | Medium | PALETTE `green500` maps to `#10b981` (Tailwind emerald-500), not Tailwind's actual green-500 (`#22c55e`). This naming mismatch caused confusion during ADHC_DESIGN.005 and required adding `nativeGreen500`. The naming convention should be documented or corrected. |

---

## Part 2: RD/DS Scan Aggregation

### Source Logs (all from 2026-03-23)

| Agent | Findings | High | Status |
|-------|----------|------|--------|
| 0.2.0_DS_PortfolioAnalytics | 28 | 4 | Complete |
| 0.2.1_RD_Positioning | 36 | 9 | Complete (fixes applied) |
| 0.2.2_RD_Attribution | 34 | 7 | Complete (fixes applied) |
| 0.2.3_RD_FactorTilts | 20 | 4 | Complete |
| 0.2.4_RD_Valuation | 19 | 2 | Complete |
| 0.2.5_RD_Macroeconomics | 31 | 4 | Complete (all 31 fixed) |
| 0.2.6_RD_Correlation | 17 | 0 | Complete (fixes applied) |
| **TOTAL** | **185** | **30** | |
| + DE shared infra | **11** | **1** | |
| **GRAND TOTAL** | **196** | **31** | |

### Deduplicated Cross-References

These findings appeared in multiple scans from different angles:

| ID | Finding | Agents | Merged Perspective |
|----|---------|--------|--------------------|
| X-1 | **HoldingsTab/SelectionTab massive duplication** (~500 lines each) | Positioning #15-28, Attribution #8-17 | Both RDs found the same copy-paste pattern from opposite directions. Attribution RD fixed it by extracting `constants/holdings-shared.tsx`. **RESOLVED.** |
| X-2 | **ASSET_CLASS_COLORS duplicated in 5+ files** | Positioning #28, Attribution #23,#26, FactorTilts (implicit) | 5 copies of the same FI/Equity color map. Attribution extracted some to holdings-shared.tsx but 3 copies remain in AssetAllocationSummary, StylePolicyComparison, buildAttributionData. **PARTIALLY RESOLVED.** |
| X-3 | **Hardcoded `#1e1e2d` tooltip background** | Macroeconomics #20, FactorTilts #15 | Same hardcoded hex in 4+ files across two pages. Should be a CSS variable. Macroeconomics #20 was fixed in ADHC_DESIGN.005 color migration. FactorTilts still has it. **PARTIALLY RESOLVED.** |
| X-4 | **Emoji in production code** | Macroeconomics #27-31, Attribution #6, Valuation #18-19, DS #21 | All pages and backend Lambdas had emoji in console.log/comments. Most page-level instances fixed by respective RDs. DS Lambda emojis still present. **PARTIALLY RESOLVED.** |
| X-5 | **Silent error swallowing (console.error only)** | Macroeconomics #24-25, Positioning #35-36, Attribution #31-32, FactorTilts #19-20, Valuation #13, Correlation #17, DS #24-25 | Pod-wide anti-pattern: fetch errors logged to console with no user feedback. Every page has at least one instance. Correlation RD fixed theirs. Others remain. **MOSTLY UNRESOLVED.** |
| X-6 | **Hardcoded EST timezone offset** | Macroeconomics #22, Valuation #12 | Both VolatilityTab and RiskPremiumTab hardcode `-05:00` EST instead of handling EDT. Wrong 7 months/year. Neither fixed. **UNRESOLVED.** |
| X-7 | **deploy.sh scripts using aws lambda update-function-code** | DS #5-6 | 7 deprecated deploy scripts violate Terraform-only mandate. Backend-only issue. **UNRESOLVED.** |
| X-8 | **Benchmark Lambda duplication** | DS #9 | `yang-model-portfolio-benchmarks` is 90% copy of `yang-generate-benchmark-returns` (400+ lines). Largest single duplication in the pod. **UNRESOLVED.** |

---

## Top 10 Pod Debt Items (Ranked by Severity + Blast Radius)

| Rank | Finding | Source | Category | Effort | Rationale |
|------|---------|--------|----------|--------|-----------|
| 1 | **X-5: Silent error swallowing across all 6 pages** | All RDs, DS | C6 | SIGNIFICANT | Every Pod 2 page has fetch errors that are console.error'd with no user feedback. Users see blank panels, permanent spinners, or stale data with no indication of failure. ~15 fetch calls affected across 6 pages. Requires error UI pattern + page-by-page application. |
| 2 | **X-8: Benchmark Lambda 400+ line duplication** | DS #9 | C3 | SIGNIFICANT | `yang-model-portfolio-benchmarks` is 90% identical to `yang-generate-benchmark-returns`. Any bug fix must be applied twice. Extracting shared lib requires coordinated Lambda deploy. |
| 3 | **DE-2: 401 redirect disabled in portal-proxy** | DE scan | C2 | MODERATE | Auth redirect permanently "temporarily disabled" -- users with expired tokens get silent 401 errors instead of being redirected to login. Affects all authenticated endpoints across all pages. |
| 4 | **X-6: Hardcoded EST timezone (wrong 7 months/year)** | Macro #22, Val #12 | C4 | QUICK WIN | Two pages show incorrect timestamps during EDT (March-November). Simple fix: use `Intl.DateTimeFormat` or conditional offset. |
| 5 | **Positioning dead files (~1800 lines)** | Positioning #1-6 | C1 | QUICK WIN | AttributionTab, SelectionTab, StylePolicyComparison, HoldingsTable, PortfolioRadialCharts, buildAttributionData are all unreachable. Massive dead weight. Note: Attribution RD already deleted some of these -- verify current state. |
| 6 | **X-2: ASSET_CLASS_COLORS still in 3+ files** | Pos #28, Attr #23 | C3 | QUICK WIN | After Attribution's holdings-shared extraction, 3 copies remain. Move to `chartColors.ts` ASSET_CLASS semantic (already exists). |
| 7 | **Macroeconomics hardcoded month index** | Macro #17 | C4 | MODERATE | YieldCurveTab hardcodes current month to December. Shows stale yield curve data 11 months/year. Requires dynamic month detection from API response. |
| 8 | **DE-3: AUM API stuck in DEMO mode** | DE scan | C2 | MODERATE | `getAUMSummary()` uses public unauthenticated endpoint instead of private firm-scoped endpoint. TODO never completed. Requires auth flow testing. |
| 9 | **FactorTilts duplicated color/conviction logic** | FT #10-11 | C3 | QUICK WIN | `getFactorCellBg`, `getFactorTextColor`, and conviction/consensus logic duplicated between FactorTiltOverviewPanel and SummaryMetricsTable. Extract to constants.ts. |
| 10 | **X-7: 7 deprecated deploy.sh scripts** | DS #5-6 | C2 | QUICK WIN | deploy.sh scripts using `aws lambda update-function-code` violate Terraform mandate. Delete them to prevent accidental use. |

### Effort Key
- **QUICK WIN** (< 1 hour): Safe deletion, simple extraction, one-line fixes
- **MODERATE** (1-4 hours): Requires testing, affects multiple files, needs coordination
- **SIGNIFICANT** (> 4 hours): Cross-page patterns, Lambda deploys, auth flow changes

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total findings across pod | 196 |
| Already fixed by RDs | ~80 (Macro: 31, Attribution: ~30, Correlation: 13, Positioning partial) |
| Remaining unfixed | ~116 |
| Cross-referenced dedupes | 8 clusters |
| Quick wins in top 10 | 4 |
| Significant efforts in top 10 | 2 |

## Note on Scan Freshness

RD/DS scans are from 2026-03-23 (15 days ago). Some findings may have been addressed by subsequent work (e.g., ADHC_DESIGN color migration resolved hardcoded hex across Macroeconomics). The Attribution RD applied extensive fixes during their scan session. Current state should be verified before starting fix task orders.
