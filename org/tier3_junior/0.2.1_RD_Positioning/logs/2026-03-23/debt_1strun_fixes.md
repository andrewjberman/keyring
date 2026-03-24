# DEBT_1STRUN Fixes -- 0.2.1_RD_Positioning

**Date:** 2026-03-23
**Scope:** portal/src/pages/Positioning/

## Objective

Fix priority debt findings from DEBT_1STRUN scan. Remove all dead code, stale TODOs, emojis in code, and legacy fetch patterns.

---

## Work Completed

### 1. Dead file removal (7 files, ~2,400 lines)

| File | Lines | Why dead |
|------|-------|----------|
| tabs/AttributionTab.tsx | 25 | Not imported by Positioning.tsx (tabs removed) |
| tabs/SelectionTab.tsx | ~1,100 | Not imported by Positioning.tsx (tabs removed) |
| components/HoldingsTable.tsx | 251 | Never imported; README confirmed unused |
| components/StylePolicyComparison.tsx | 288 | Only consumer was dead AttributionTab |
| components/AssetAllocationSummary.tsx | 276 | Only consumer was dead StylePolicyComparison |
| panels/PortfolioRadialCharts.tsx | 137 | Superseded by inline bars in PositioningSummary |
| utils/buildAttributionData.ts | 258 | Only consumed by dead SelectionTab flow |

Removed empty `components/` and `utils/` directories.

### 2. Dead code within active files

| File | Change |
|------|--------|
| tabs/HoldingsTab.tsx | Removed `_getHoldingMetadata` dead function + `void` suppress trick (16 lines) |
| tabs/HoldingsTab.tsx | Removed dead `getTickerMetadata` import |
| types.ts | Cleared all unused types (Instrument, InstrumentAnalytics, Portfolio, DurationByAssetClass, DurationByBucket, PortfolioSummary, PositioningData, AssetClass, DurationBucket, InstrumentType, PortfolioHolding). No active file imports from types.ts. |
| constants/etf-categories.ts | Removed `'Hedge'` from ETFCategory type union, ASSET_CLASS_ORDER, and SEGMENT_ORDER (no ETF uses Hedge asset class) |

### 3. Emoji removal

| File | Lines | Fix |
|------|-------|-----|
| Positioning.tsx | 25-27 | Replaced 3x `// ✅` comment lines with single ASCII comment |
| tabs/HoldingsTab.tsx | 635, 651, 670 | Removed `// ✅ PHASE1_PS_REQ_*` emoji prefixed comments |

### 4. Stale comment cleanup

| File | Fix |
|------|-----|
| constants/etf-categories.ts | Updated header comment from "for Attribution Tab" to "for Positioning page holdings" |

### 5. Legacy fetch pattern fix

| File | Before | After |
|------|--------|-------|
| panels/PositioningSummary.tsx | `useEffect` + `useState` for `getHoldingsAttribution()` with `console.error` catch | `useQuery` with `staleTime: 5min`, `gcTime: 10min`. React Query provides automatic retry, error state, and caching. |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Delete AssetAllocationSummary (not just StylePolicyComparison) | Only consumer was StylePolicyComparison which was itself dead. Entire chain unreachable. |
| Clear types.ts instead of deleting it | Barrel export in index.ts still references it. Empty file is cleaner than removing the re-export. |
| Remove Hedge from ETFCategory union | No ETF in ETF_CATEGORIZATION uses assetClass 'Hedge'. UVXY is classified as 'Equity'. Dead type variant. |
| Convert PositioningSummary to useQuery | Consistent with rest of page (Positioning.tsx, former AssetAllocationSummary). Gains automatic retry, caching, refetch-on-focus. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| tabs/AttributionTab.tsx | Deleted | No -- local only |
| tabs/SelectionTab.tsx | Deleted | No -- local only |
| components/HoldingsTable.tsx | Deleted | No -- local only |
| components/StylePolicyComparison.tsx | Deleted | No -- local only |
| components/AssetAllocationSummary.tsx | Deleted | No -- local only |
| panels/PortfolioRadialCharts.tsx | Deleted | No -- local only |
| utils/buildAttributionData.ts | Deleted | No -- local only |
| Positioning.tsx | Emoji removal | No -- local only |
| tabs/HoldingsTab.tsx | Dead function + import + emoji removal | No -- local only |
| types.ts | Cleared unused types | No -- local only |
| constants/etf-categories.ts | Hedge removal + comment fix | No -- local only |
| panels/PositioningSummary.tsx | useEffect->useQuery conversion | No -- local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD (portal submodule on DEV)

All priority fixes from DEBT_1STRUN scan applied locally. 7 dead files deleted (~2,400 lines), emojis removed from 2 active files, dead Hedge type variant removed, PositioningSummary converted from legacy useEffect fetch to React Query. Remaining page structure: Positioning.tsx -> PositioningSummary + HoldingsTab, with shared gridConfig and etf-categories constants.

---

## Next Steps

1. **[0.2.0_DE_PortfolioAnalytics] Review and commit** -- all changes are local, need DE to review and commit to portal DEV
2. **[0.4.0_DT_ClientPlatform] Push portal DEV** -- after DE commit, DT pushes
3. **README.md update** -- file structure section references deleted files (AttributionTab, HoldingsTable, etc.) -- needs refresh after commit
