# Session Log — ADVI_RDVSDS TO 004 — FIRM_ACCOUNT_NAME Fix
**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-24
**TO:** ADVI_RDVSDS TO 004 (CTO GO received 20260424)
**Portal DEV commit:** `2c19352`

## Summary

Parameterized `FIRM_ACCOUNT_NAME` in `AdvisorsTab.tsx`. Added `firmAccountName?: string` prop (default `'49F House'`). Replaced the module-level `PINNED_BOTTOM_NAMES` const with a `buildPinnedSet()` factory function. Threaded `pinnedNames: Set<string>` through all 7 sub-components/functions that reference it. Updated `inflection/index.tsx` to pass `firmAccountName={FIRM_DISPLAY_NAME}` (`'Inflection Wealth Management'`).

49F leaderboard behavior is unchanged — no prop passed = default `'49F House'`. Inflection's firm-aggregate row (`advisor_id: 'firm'`, `name: 'Inflection Wealth Management'`) will now be pinned to the bottom of the leaderboard instead of sorting into the main ranking.

## Work Performed

### 1. Pre-work
- `comp-blast AdvisorIntelligence` — audit-phase finding from TO 002 session
- `comp-cache collisions` — 0 new collisions from this change

### 2. `AdvisorsTab.tsx` changes

| Change | Detail |
|--------|--------|
| Module level | Replaced `const PINNED_BOTTOM_NAMES = new Set(...)` with `function buildPinnedSet(firmAccountName: string): Set<string>` |
| `AdvisorsTabProps` | Added `firmAccountName?: string` with doc comment |
| Component destructure | Added `firmAccountName` to params |
| Component body | `const pinnedNames = useMemo(() => buildPinnedSet(firmAccountName ?? FIRM_ACCOUNT_NAME), [firmAccountName])` |
| `Top3HighlightsProps` | Added `pinnedNames: Set<string>` |
| `Top3Highlights` | Destructure + replace `PINNED_BOTTOM_NAMES` + add `pinnedNames` to useMemo deps |
| `LeaderboardNnaBar` | Props + replace + update useMemo deps `[entries, pinnedNames]` |
| `prepareEntries` | Added `pinnedNames: Set<string>` parameter; replaced both usages |
| `LeaderboardCards` | Props + pass `pinnedNames` to `prepareEntries` + update useMemo deps |
| `LeaderboardNnaCards` | Props + pass through to `LeaderboardCards` |
| `LeaderboardAuaView` | Props + pass to `prepareEntries` + pass to `LeaderboardCards` + update useMemo deps |
| `LeaderboardGrowthView` | Props + pass to `prepareEntries` + pass to `LeaderboardCards` + update useMemo deps |

Call sites updated (main component JSX): `Top3Highlights`, `LeaderboardNnaBar`, `LeaderboardNnaCards`, `LeaderboardAuaView`, `LeaderboardGrowthView` — all receive `pinnedNames={pinnedNames}`.

### 3. `inflection/index.tsx`
Added `firmAccountName={FIRM_DISPLAY_NAME}` to `<AdvisorsTab>` JSX (line 225). `FIRM_DISPLAY_NAME = 'Inflection Wealth Management'` already imported from `./constants`.

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| After write | `bunx tsc -b --noEmit` | 0 errors |
| After write | `comp-cache collisions` | 0 new collisions |
| After write | `/frontend-dev advi_49f_regression_w5_refactor.json --scenario 49f-leaderboard-renders` | PASS (iter 1/1) |

## /frontend-dev

| Iteration | Status | Blocking | Notes |
|-----------|--------|----------|-------|
| 1 | PASS | 0 | 0 console errors; leaderboard renders; no crash |

**Constitution:** `portal/.frontend-dev/testing/advi_49f_regression_w5_refactor.json`
**Scenario:** `49f-leaderboard-renders`
**Screenshots:** `.frontend-dev-results/20260424T204931Z/`

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/AdvisorsTab.tsx` | FIRM_ACCOUNT_NAME parameterization — props + factory + threading | Yes — portal DEV `2c19352` |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/index.tsx` | `firmAccountName={FIRM_DISPLAY_NAME}` prop added | Yes — portal DEV `2c19352` |

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|---------|
| 1. `firmAccountName?: string` added to `AdvisorsTabProps` | PASS | `AdvisorsTab.tsx` updated |
| 2. Default `'49F House'` preserved (no 49F regression) | PASS | `firmAccountName ?? FIRM_ACCOUNT_NAME` fallback; `/frontend-dev` PASS |
| 3. `inflection/index.tsx` passes `firmAccountName={FIRM_DISPLAY_NAME}` | PASS | Line 225 updated |
| 4. All PINNED_BOTTOM_NAMES usages replaced | PASS | 7 sub-components/functions updated; no remaining `PINNED_BOTTOM_NAMES` references |
| 5. bunx tsc -b clean | PASS | 0 errors |
| 6. /frontend-dev PASS | PASS | iter 1, 0 console errors |
| 7. Portal DEV commit | PASS | `2c19352` |

## Next Steps

- [DT] Push portal DEV `2c19352` to remote; update CLOUD submodule pointer
- [CTO] MCP COMPLETE — TO 004 done; RD visual validation pending (blank-view root cause remains DS artifact gap per TO 002 findings)

## Status

TO 004 FIRM_ACCOUNT_NAME fix: **complete**
