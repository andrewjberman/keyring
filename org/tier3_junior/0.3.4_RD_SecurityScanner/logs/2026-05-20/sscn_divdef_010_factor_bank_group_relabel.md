# SSCN_DIVDEF.010 -- Factor Bank group relabel + 4-color polish

**Agent:** 0.3.4_RD_SecurityScanner
**Date:** 2026-05-20
**Task order:** SSCN_DIVDEF.010-RD (PM: 0.3.0_DE_TradingOperations)
**PRD:** docs/architecture/SSCN_DIVDEF.md v0.6 §6.9 TO-8

## Re-scope note

This RD TO is the COO-confirmed RE-SCOPE of the parent TO. DE's Phase 1 check
found `utils/categoryOrder.ts` ALREADY encodes the correct 18-group master
taxonomy (migrated 2026-03-05) -- the parent TO's "wrong 11-category" premise was
about the registry data, not this portal file. So NO 11->18 change was made.
`CANONICAL_CATEGORY_ORDER` membership and order are untouched.

## Files changed (2, both in portal/src/pages/SecurityScanner/)

### FILE 1: tabs/FactorBankTab.tsx -- 3 user-facing "Category" -> "Group" relabels

| Site | Before | After |
|------|--------|-------|
| Sortable column header (~line 277) | `<SortableTh label="Category" col="category" ... />` | `label="Group"` -- `col="category"` KEPT (internal field name, PRD v0.6 §D) |
| Filter dropdown label (~line 117) | `<label ...>Category:</label>` | `Group:` |
| Filter "all" option text (~line 125) | `{c === 'all' ? 'All Categories' : c}` | `'All Groups'` |

Filter LOGIC untouched: `categoryFilter` state, the `categories` useMemo
auto-derivation, `col="category"`, and all `f.category` reads are unchanged.
Label text only.

### FILE 2: utils/categoryOrder.ts -- 4-color separability polish

`CANONICAL_CATEGORY_ORDER` unchanged. Only 4 `CATEGORY_COLORS` entries re-hued --
the 4 that previously clustered in a ~40deg green/teal band (145/160/175/185, all
~70% S / ~55% L, hard to tell apart on the dark factor table).

| Group | Before (HSL) | After (HSL) | Reading |
|-------|-------------|-------------|---------|
| solvency | `160, 65%, 52%` | `112, 60%, 50%` | yellow-green |
| growth | `145, 70%, 55%` | `132, 70%, 58%` | vivid green (kept green per TO) |
| efficiency | `175, 70%, 55%` | `152, 55%, 48%` | dark sea-green |
| liquidity | `185, 70%, 55%` | `170, 72%, 60%` | bright teal |

**Rationale:** spread across a 58deg band (112-170) instead of the old 40deg, and
alternate lightness/saturation between hue-neighbors so adjacent groups separate
on both axes. Hue band bounded by neighbors management(85) and volatility(195):
solvency(112) sits 27deg off management; liquidity(170) sits 25deg off
volatility. Adjacent pairs are ~20deg apart in hue and additionally separated by
lightness (48/50/58/60%) and saturation (55/60/70/72%) contrast -- the TO's
permitted ">=25-30deg OR clear sat/lightness contrast where hues stay closer"
criterion. No collision with the other 14 in-use hues (0,12,25,40,48,85,195,210,
220,235,265,280,320,345 -- nearest is 85/195, both >=25deg clear). All 4 keep
lightness 48-60% and saturation >=55% for dark-bg legibility.

DE reviews the rendered colors in the /frontend-dev smoke screenshot; iterate if
the first pass still looks crowded.

## Acceptance criteria

| AC | Status |
|----|--------|
| AC1 -- 18 master groups, each ordered + distinct color, no gray fallthrough; green/teal cluster legibly separable | Implemented (4-color polish); visual confirm by DE /frontend-dev |
| AC2 -- no user-facing "Category" label on Factor Bank tab (header, filter label, "all" option all read Group/All Groups); filter logic unchanged | Implemented |
| AC3 -- /frontend-dev smoke green; typecheck clean; lint clean | typecheck + lint PASS (below); smoke run by DE |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-transform schema-check FactorBankTab` | "All rendered fields match their response types." -- no MISSING from the relabel (label text only, no field/prop change). |

DE runs the full compiler mandate (schema-check + /frontend-dev smoke) +
visual color review + commit + RAVC2 per the TO handback.

## typecheck + lint transcript

```
$ bun run typecheck
$ tsc -b --noEmit
typecheck exit: 0

$ bun run lint
... 11 problems (0 errors, 11 warnings)
lint exit: 0
```

All 11 lint warnings are pre-existing in files outside this TO's scope
(`.frontend-dev/runners/sscn_divdef_001_runner.mjs`, `src/api/endpoints/portfolio.ts`,
`src/components/PerformanceHeatMap.tsx`, `src/components/market-performance/RSIBars.tsx`,
`src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`). Zero
warnings/errors in FactorBankTab.tsx or categoryOrder.ts. Both commands exit 0.

## Handback

2-file change on the portal working tree (DEV branch, uncommitted). MCP sent to
0.3.0_DE_TradingOperations with files changed + 4 proposed HSL values + rationale
+ typecheck/lint result. DE reviews relabel + colors visually, runs the compiler
mandate, commits, and RAVC2s to COO. TO not self-flipped (DE closes the loop).
