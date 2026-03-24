# DEBT_1STRUN Scan -- 0.2.4_RD_Valuation

**Date:** 2026-03-23
**Scope:** portal/src/pages/Valuation/

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | tabs/RiskPremiumTab.tsx | 226-228 | C1 Dead | Medium | `formatXAxisDate` contains an `if (timeWindow === '1y')` branch that is unreachable -- '1y' is commented out of `TIME_WINDOWS` (line 141) and can never be selected. Dead code path. |
| 2 | types.ts | 19 | C1 Dead | Low | `TimePeriod` union includes `'1Y'` variant marked "kept for backend compatibility" but no UI path can select it. The type is broader than runtime usage. |
| 3 | constants.ts | 30-31 | C1 Dead | Low | `AVAILABLE_INDICES` flat array is created "for backwards compatibility" but is not consumed by any file within the page directory. If nothing external imports it, this is dead code. |
| 4 | panels/ValuationSummaryPanel.tsx | 32-58 | C3 Duplication | High | `getPercentileBgColor` and `getPercentileTextColor` are near-identical copies of the same functions in `ValuationRangePanel.tsx:22-48`. Only difference: null-value fallback colors (`rgba(255,255,255,0.05)` vs `transparent`) and 40-60 range fill (`rgba(107,114,128,0.2)` vs `transparent`). Copy-paste with subtle drift. |
| 5 | panels/ValuationRangePanel.tsx | 22-48 | C3 Duplication | High | Counterpart of finding #4. Same `getPercentileBgColor`/`getPercentileTextColor` functions with minor threshold divergence from SummaryPanel. Should be a shared utility. |
| 6 | panels/ValuationSummaryPanel.tsx | 60-63 | C3 Duplication | Low | `formatPercentile` helper is identical to `ValuationRangePanel.tsx:55-58`. Trivial but exact duplicate. |
| 7 | panels/ValuationRangePanel.tsx | 50-57 | C3 Duplication | Low | `formatValue` and `formatPercentile` -- `formatPercentile` is duplicated from SummaryPanel. `formatValue` is unique to this file. |
| 8 | tabs/RiskPremiumTab.tsx | 140-146 | C3 Drift Risk | Medium | `TIME_WINDOWS` is a separate time-period config from `constants.ts:TIME_PERIODS`. Different types (`TimeWindow` vs `TimePeriod`), different casing (`'5y'` vs `'5Y'`), different shapes (`days: number|null` vs `value/label`). Two independent period configs that can drift. |
| 9 | Valuation.tsx | 52, 68, 82, 98 | C4 Hardcoded | Medium | Accent color `#f59e0b` is hardcoded in 4 separate `PageThemeProvider` instances (loading, error, no-data, and main render). Should be a single constant in `constants.ts`. |
| 10 | panels/ValuationRangePanel.tsx | 79, 86-87 | C4 Hardcoded | Low | Inline CSS color `bg-[#1e1e2d]` hardcoded on dropdown `optgroup` and `option` elements. Should reference theme variable. |
| 11 | tabs/ValuationTimeSeriesTab.tsx | 138 | C4 Hardcoded | Low | Magic date `new Date(1989, 0, 1)` used as the start boundary for 'Max' period. No constant, no comment explaining why 1989. |
| 12 | tabs/RiskPremiumTab.tsx | 219 | C4 Hardcoded | Medium | `creditFredTimestamp` hardcodes timezone offset `T17:00:00-05:00` (EST). During Eastern Daylight Time the offset should be `-04:00`. Produces incorrect timestamp ~7 months/year. |
| 13 | tabs/RiskPremiumTab.tsx | 173 | C6 Stale Error | Medium | Error fallback displays "Data source: /data/risk_premium_data.json" but the actual API endpoint is `/v1/risk-premium/data`. Misleading to anyone debugging. |
| 14 | tabs/ValuationTimeSeriesTab.tsx | 277 | C2 Stale | Low | Hardcoded text "Metrics: Trailing P/E, Fwd P/E, P/B" does not reflect the full set of available metrics (also P/FCF, EV/Sales, P/Sales, Div Yield). Known issue per prompt.md. |
| 15 | types.ts | 35-44 | C2 Stale | Low | `ValuationRangeRow` fields carry inline comments like "Changed from metricLabel to match API", "Changed from latestPercentile to match API". These document a completed migration and are now stale change-tracking noise. |
| 16 | constants.ts | 46 | C2 Stale | Low | Commented-out `{ value: '1Y', label: '1 Year' }` entry with note "Hidden from UI but backend logic remains." If backend no longer needs 1Y, this is stale. If it does, the comment should say so explicitly. |
| 17 | tabs/RiskPremiumTab.tsx | 141 | C2 Stale | Low | Same commented-out `'1y'` entry duplicated independently from `constants.ts:46`. Two files carry the same stale comment. |
| 18 | tabs/ValuationRangePanel.tsx | 108 | C4 Hardcoded | Low | Emoji character in JSX string. CLAUDE.md Rule 13 bans emojis in production code. Frontend-only but violates project standard. |
| 19 | tabs/ValuationTimeSeriesTab.tsx | 281 | C4 Hardcoded | Low | Same emoji character in JSX "no data" fallback. Same Rule 13 violation. |

## Summary

- Total findings: 19
- By category: C1: 3, C2: 4, C3: 5, C4: 5, C5: 0, C6: 2
- C5 (Orphaned Infrastructure): None found -- page routing and lazy-load structure is clean. All defined components are rendered. All hooks are called.
- High severity: 2 (findings #4 and #5 -- duplicated percentile color functions)
- Medium severity: 5 (findings #1, #8, #9, #12, #13)
- Low severity: 12

### Recommended Priority Fixes

1. **Extract shared percentile utilities (findings #4, #5, #6, #7)** -- `getPercentileBgColor`, `getPercentileTextColor`, and `formatPercentile` should move to a shared file within the page (e.g., `utils.ts`). The subtle threshold differences between SummaryPanel and RangePanel are likely unintentional drift and should be reconciled. This is the highest-impact fix: 4 findings resolved, drift risk eliminated.

2. **Fix hardcoded EST timezone offset (finding #12)** -- `RiskPremiumTab.tsx:219` produces an incorrect timestamp 7 months of the year during EDT. Should use `Intl.DateTimeFormat` or a timezone-aware approach.

3. **Extract accent color constant (finding #9)** -- `#f59e0b` appears in 4 `PageThemeProvider` instances in `Valuation.tsx`. A single `ACCENT_COLOR` constant in `constants.ts` eliminates the repetition and makes future theme changes atomic.
