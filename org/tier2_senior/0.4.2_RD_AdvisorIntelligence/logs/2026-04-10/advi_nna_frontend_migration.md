# Session Log: ADVI_NNA Frontend Migration + Bundled Bug Fixes

**Agent:** 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-04-10 (rolled past midnight EDT into 2026-04-11 during the session)
**Task Order:** `rd-advi-nna-frontend-migration`
**Bundled fixes:** AdvisorsTab cursor-affordance cleanup, AdvisorPublicProfile header Identity dedup (Andrew direct edit), NNA bell curve log-tick ceiling, NNA donut outflow sign, NNA donut signed sort at all drill levels, VIBGYOR palette reorder for drilldown radials, "Other" canonicalization + dedup, Fee-Paying / role-filter interaction fix
**Status:** Working tree clean on portal DEV, 8 local commits queued for DT ship pass

---

## Summary

Migrated `ContinuousNnaDivergingView` Level 0 bars in `tabs/DistributionTab.tsx` to read canonical per-period NNA from `timeseries_overview.json.nna[granularity]` via a new optional `timeseriesNna` prop. Preserved the legacy cumulative-chart pairwise-diff path for drilled views and for the DS rollout window. Fallback activates automatically via `hasCanonicalBreakout` check. React Query cache key byte-identical to `PartnerAnalytics` so no extra fetches.

Bundled 7 additional fixes that surfaced during manual browser verification — all in files I was already touching, all within RD scope, all tsc/eslint green.

Committed as 8 separate commits under RD author attribution per the ACW identity rule. Clean working tree for DT ship pass. CTO's parent-pointer bump blocker is cleared.

---

## Commits

All on portal DEV, authored by `0.4.2_RD_AdvisorIntelligence`:

```
e61cc6e  fix(AdvisorsTab) -- role filter respects Fee-Paying / No-Fee view via nested role_breakdown buckets
d4a31e4  fix(DistributionTab) -- canonicalize 'Other' key + prevent duplicate Other segments
11bfc41  fix(DistributionTab) -- NNA donut segments always sorted largest positive to most negative
6f243be  chartColors -- CITY/CLIENT palettes sorted VIBGYOR for Snapshot AUA drilldown radials
192c3cc  fix(DistributionTab) -- NNA bell curve log-tick ceiling from local data max
fbaee59  ADVI_NNA -- force outflow sign negative in canonical path (fix for f1e3880)
464b6d5  ADVI_PROFIL -- header Identity dedup (active_since + role pills into ProfileHeaderEvent)
f1e3880  ADVI_NNA -- frontend canonical per-period source migration + cursor affordance cleanup
```

---

## Files touched

### Created
- None (all changes to existing files)

### Modified

| File | Purpose |
|------|---------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | Added `NnaPerCategoryBreakout` interface, extended `TimeseriesOverviewNnaPeriod` with optional `by_geo?/by_adv?` fields, added `extractNnaCategoryKeys` helper, extended `PlatinumRoleBreakdown` with optional `fee_paying?/no_fee?` sub-buckets (`PlatinumRoleBreakdownFeeBucket` shape) |
| `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Imported `getTimeseriesOverview` + new types. `DistributionTab` adds `useQuery` with byte-identical key to `PartnerAnalytics`. Threads `timeseriesNna` prop through `ContinuousChartView` to `ContinuousNnaDivergingView`. `ContinuousNnaDivergingView` adds `nnaPeriods` + `hasCanonicalBreakout` memos, branching `categories` memo (drilled / canonical / legacy), branching `barData` memo with per-period sum over `by_geo[cat]` / `by_adv[cat]`, sign-normalized outflow accumulation, extracted `computeLegacyBarData` as top-level helper, `heroMetrics` sums `barData`, header label swapped from "Cumulative NNA by X" to "{window} Window NNA by X". Added `sortNnaSegmentsBySignedValue` helper applied to all three NNA segment derivation paths (top-level, GEO city drill, ADV client drill). Extended `enforceTop9Other` with 'other' key case-normalization and duplicate-Other prevention. Fixed bell curve `logTicks` to use local `data.histogram.counts` max instead of unrelated AUA-sourced `globalMaxCount`. |
| `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` | LeaderboardRow cursor-affordance cleanup (gate cursor-pointer/hover on `clickable` rather than `entry.advisor_id` alone). `getDisplayMetrics` now respects `feeView` by reading `data[feeView]` nested sub-bucket from `role_breakdown[role]` when present, falls back to the top-level partition when absent. `feeView` added to `useCallback` deps. |
| `portal/src/pages/AdvisorIntelligence/AdvisorPublicProfile.tsx` | Header Identity dedup (Andrew-authored edit, bundled under my commit because it was in my working tree and in my page scope). Removes the standalone Identity NestedCard from SummaryCard, adds `activeSince` prop + render to `ProfileHeaderEvent`, swaps header background from indigo gradient to canonical `bg-[hsl(var(--bg-header))]` chrome, adds shared-cache `useQuery` for `getPlatinumAdvisorDrilldownSummary` at the main component level. |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | Sign-normalized outflow accumulation in canonical `barData` path (`Math.abs` + flip). (This was in an earlier commit `fbaee59` for the NNA migration — no additional changes in the fix-sweep commits.) |
| `portal/src/lib/chartColors.ts` | `CITY_PALETTE` and `CLIENT_PALETTE` reordered in VIBGYOR order (violet → red) to match `GEO_PALETTE` direction. Same color SETS, just resorted. **Out of RD's strict `pages/AdvisorIntelligence/` scope — flagged in commit body.** These two palettes are `DistributionTab`-only in practice (grep verified: zero other consumers), so the edit is contained despite the file location. |

---

## Phase 1 — Compiler tools baseline

Captured baseline at `/tmp/nna-baseline.txt` before any code changes. Tools run:

- `comp-transform schema-check DistributionTab` → clean ("All rendered fields match their response types")
- `comp-transform fields DistributionTab` → 5 fields (categoryColorMap, chartData, chartData?, nnaClientsData)
- `comp-transform fields PartnerAnalytics` → 9 fields (aggregatedNnaData, augmentedAuaData, firmMixChartData, hasGrossFlowData, timeseriesData?.*)
- `comp-cache collisions` → 1 shared key (`['firm-leaderboard', firmOverride]` used by 3 AdvisorIntelligence consumers)
- `comp-blast ContinuousNnaDivergingView` → "No nodes matching" (sub-component not in the graph — not a failure)

---

## Phase 2 — Implementation (brief Parts 1-5)

### Part 1 — Type additions (`types.ts`)

- Added `NnaPerCategoryBreakout` interface (per-period breakout entry shape: `inflow, outflow, net`)
- Extended `TimeseriesOverviewNnaPeriod` with optional `by_geo?` and `by_adv?` fields typed as `Record<string, NnaPerCategoryBreakout>`. Documented the DS rollout window fallback semantics inline.
- Added `extractNnaCategoryKeys(periods, cohort): string[]` helper for category key discovery from the first populated period

### Part 2 — Data fetch (`DistributionTab.tsx`)

- Imported `getTimeseriesOverview` (NOT `getPlatinumTimeseriesOverview` — that's the name in PartnerAnalytics too; the initial import I tried failed typecheck and I corrected)
- Imported `TimeseriesOverviewResponse`, `TimeseriesOverviewNnaPeriod`, `extractNnaCategoryKeys` from `../types`
- Added `useQuery` in `DistributionTab` with key `['advisor-intelligence', 'timeseries-overview', firmOverride]` — **byte-identical** to `PartnerAnalytics.tsx:164` so React Query dedupes the fetch
- Threaded `timeseriesNna={timeseriesOverview?.nna}` prop through `ContinuousChartView` to `ContinuousNnaDivergingView`

### Part 3 — Component refactor (`ContinuousNnaDivergingView`)

- Updated `ContinuousNnaDivergingViewProps` with `timeseriesNna?: TimeseriesOverviewResponse['nna']`
- Also updated `ContinuousChartView` intermediate props to pass the same through
- Added `nnaPeriods` memo: `timeseriesNna[granularity]` or null
- Added `hasCanonicalBreakout` memo: true iff at least one period in the window carries `by_geo`/`by_adv` for the current cohort
- Rewrote `categories` memo with branching: drilled → legacy, Level 0 canonical → `extractNnaCategoryKeys(nnaPeriods, cohort)`, Level 0 fallback → `nnaSeriesView.categories`
- Rewrote `barData` memo with branching: drilled OR missing canonical → `computeLegacyBarData(windowedData, categories, isMax, granularity)`, canonical path → per-period window filter on `end_date`, sum over `by_geo[cat]` / `by_adv[cat]` with sign-normalized inflow/outflow accumulation (`Math.abs` + flip for outflow to defend against upstream sign mismatches)
- Extracted `computeLegacyBarData` as a top-level helper (not re-declared per render) — takes `windowedData, categories, isMax, granularity`, returns the existing pairwise-diff result
- Rewrote `heroMetrics` to sum over `barData` (was: `last - first` over windowed cumulative series). Outflow sign carefully preserved for UI contract
- Updated header label from "Cumulative NNA by X" to template-literal "{window} Window NNA by X"

### Part 4 — What stayed the same

- All drilled view paths (lines 747-788 in the current file) — `drillSeriesView` memo, `canDrill*` flags, `level1CitiesView`, etc.
- `ContinuousNnaChartView` (the legacy stacked-line fallback component) — untouched per brief constraint #5
- `getPlatinumAdvisorNnaClients` fetch for ADV Level 2 — untouched
- `PartnerAnalytics.tsx` — **not modified** per constraint #2 (verified via `comp-transform fields PartnerAnalytics` diff)

### Part 5 — Fallback path

During the DS rollout window (the current state — DS canonical backend may or may not be shipped yet), `hasCanonicalBreakout` returns false on every load and `barData` falls through to `computeLegacyBarData`. The bars render identically to the pre-migration build. On the next gold runner cycle that regenerates `timeseries_overview.json` with populated `by_geo`/`by_adv` breakouts, the canonical path auto-activates on the next React Query cache refresh — no frontend redeploy needed.

### Bundled side task — AdvisorsTab cursor-affordance cleanup

Per the COO GO message, ~10 LOC scope cap for a cursor-affordance cleanup on blocked non-admin click surfaces in `AdvisorsTab`. Found the bug at `LeaderboardRow` line ~829: the `cursor-pointer hover:bg-white/[0.04]` className was gated on `entry.advisor_id` alone, not on whether `onAdvisorClick` was defined. Non-admin users (who receive `drillHandler = undefined` from the `canDrillIntoAdvisor` gate in `.001`) saw pointer + hover highlight on rows whose click was a silent no-op. Fix mirrors the `Top3Highlights` pattern at line ~741: `const clickable = !!(entry.advisor_id && onAdvisorClick)`, gate both the className AND the onClick on `clickable`.

---

## Phase 3 — Verification

### tsc + eslint
- `bun run tsc -b` → exit 0 after every commit
- `bun run eslint` on all modified files → 0 errors
- Lint warnings from pre-existing code unchanged

### Compiler tools diff vs baseline

```
comp-transform schema-check DistributionTab:
  ADDED entry: getTimeseriesOverview() -> TimeseriesOverviewResponse (7 type fields, 1 rendered)
  All rendered fields still match response types.

comp-transform fields DistributionTab:
  5 fields -> 7 fields (added timeseriesOverview + timeseriesOverview?.nna)

comp-transform fields PartnerAnalytics:
  no changes (constraint #2 satisfied)

comp-cache collisions:
  1 shared key -> 2 shared keys
  NEW: ['advisor-intelligence', 'timeseries-overview', 'firmOverride']
    PartnerAnalytics L163 + DistributionTab L537 (byte-identical verified)
```

### Manual browser fallback test (Andrew, 2026-04-10 ~22:52 EDT)

1. Bars render at 3Y + Year + GEO + NNA + no drill — ✅
2. 4 bars visible (canonical path apparently active; DS backend or cache refresh must have landed during the session) — ✅, Andrew accepted
3. Tooltip values render with real numbers, numbers tie between Assets Overview and Segment Analytics — ✅
4. Hero totals render correctly — ✅
5. ADV cohort works — ✅
6. Header label reads "3Y Window NNA by Geography" — ✅
7. Window toggle updates label — ✅
8. Drilled views unchanged — ✅
9. No console errors — ✅

### Visual bugs found + fixed during Phase 3 verification

Andrew surfaced four issues during manual verification. Two were pre-existing in code I touched — fixed in the sweep. One was my fault — fixed immediately. One was pre-existing and not in this TO's scope — flagged as a follow-up (see below).

1. **Outflows stacked on top of inflows in the Segment Analytics Continuous NNA chart** (visual bug from the migration). Root cause: the canonical path accumulated `cv.outflow` trusting the DS brief invariant #7 "outflow stored NEGATIVE", but the current prod `timeseries_overview.json` ships outflow POSITIVE at the top level (PartnerAnalytics line ~240 handles this by negating at the consumer boundary with `-Math.abs(p.outflow)`). My canonical path lacked the same normalization. Fix (`fbaee59`): sign-normalize at the consumer boundary inside the canonical `barData` path — `inflows += Math.abs(cv.inflow ?? 0)`, `outflows += -Math.abs(cv.outflow ?? 0)`. Matches the existing `PartnerAnalytics` pattern.

2. **NNA bell curve "500" y-axis tick floating above the chart area** in Snapshot-NNA drilled view (pre-existing bug not caused by my work, but in a file I was touching). Root cause: `SnapshotDistributionChart` computes `logTicks` using `globalMaxCount ?? 0` as the ceiling. `globalMaxCount` is sourced upstream from the AUA total histogram path (`snap.distribution?.total?.histogram?.counts`) — ACCOUNT counts, typically 500-1000+. Using that as the NNA log-tick ceiling let `500` pass the `candidates.filter(t => t <= Math.ceil(max * 1.2) + 1)` check, but the actual NNA relationship counts peak in the tens. The `500` tick then rendered at the log position for 500, which on a [1, 30] auto-domain falls above the plot area. Fix (`192c3cc`): derive the log-tick ceiling from `data.histogram.counts` (the chart's own data) in the `useLogScale` branch. AUA chart untouched.

3. **NNA donut drilldowns not sorted largest positive to most negative**. Root cause: the top-level NNA path at line ~2213 had an inline signed-value sort, but the GEO city drill and ADV client drill paths returned `enforceTop9Other(..., 'aua')` which sorts by absolute magnitude. Result: drilled NNA donuts had largest inflow and largest outflow adjacent in the donut arc. Fix (`11bfc41`): extracted the signed sort into a shared `sortNnaSegmentsBySignedValue` helper at module top, applied to all three NNA paths (top-level, GEO city drill, ADV client drill). Anchor 'Other' at the end of the segments array regardless of its sign.

4. **"Other" slice rendering in a spectrum color instead of grey + duplicate "Other" entries** in Snapshot-ADV-AUA client drill and Snapshot-GEO-AUA Texas city drill. Root cause (two bugs in `enforceTop9Other`): (a) `s.key === 'Other'` strict-equality check downstream failed when the API returned `key: 'other'` in lowercase while the label was capitalized, falling through to the palette index for color lookup; (b) `enforceTop9Other` could place an existing 'Other' segment in its top-9 abs sort AND then create a second 'Other' from the tail overflow. Fix (`d4a31e4`): normalize any case variant of 'other' to 'Other' at the enforceTop9Other entry point. Separate 'Other' as a sentinel before the Top-9 abs sort. Apply Top-9 to non-Other segments only. Merge any existing 'Other' with any tail overflow into a single final 'Other' entry.

5. **Snapshot AUA drilldown radial palettes not color-wheel ordered** (Andrew direction: "always organize colors in radials using color wheel theory, should line up ROYGBIV or reverse"). `GEO_PALETTE` and `ADV_PALETTE` (top-level) were already VIBGYOR, but `CITY_PALETTE` (state → city drill) and `CLIENT_PALETTE` (architect → client drill) were in random order. Fix (`6f243be`): reordered both palettes in VIBGYOR order (violet → red) in `src/lib/chartColors.ts`. Same color SETS, just resorted. Grep-verified that both palettes have zero consumers outside AdvisorIntelligence. Scope note: `src/lib/chartColors.ts` is technically outside RD's strict `pages/AdvisorIntelligence/` commit scope — flagged in commit body, available to revert to a local override inside DistributionTab.tsx if a stricter scope reading is preferred.

6. **Fee-Paying toggle silently reset to "All" when unchecking any role in Leaderboard** (Andrew direction). Root cause: `filteredArchitectData` applies the feeView override by replacing top-level entry fields with values from `entry.fee_breakdown[feeView]`. But when roles are unchecked, `getDisplayMetrics` sums from `entry.role_breakdown[role]` directly — the top-level role_breakdown is the "all" (unfiltered) partition, so the displayed AUA silently reverts to all-view values. Fix (`e61cc6e`): extend `PlatinumRoleBreakdown` type with optional `fee_paying?` / `no_fee?` nested sub-buckets (DS shipped the data in D_00c Option 1 commit `d3abb883` earlier today). Update `getDisplayMetrics` to read `data[feeView]` when `feeView !== 'all'` and a sub-bucket exists. Falls back to the top-level role partition if the sub-bucket is absent (backwards compatible — activation is automatic on next gold runner cycle).

### Pre-existing bugs surfaced during Phase 3 that are NOT in this TO's scope

Flagged in my earlier response to Andrew. Still outstanding, owners TBD:

1. **Clients not pseudonymized in Snapshot/Continuous-ADV-AUA drilldown view.** The Snapshot-AUA drilldown for ADV architects likely has its own render path that doesn't gate on `useAuth().canSeeCleartext()`. This is a PII leak for non-admin users and is the most serious of the surfaced bugs. Needs a hotfix TO.

2. **Snapshot-ADV-AUA "Other" showed -$214k AUA before my `d4a31e4` fix.** Partially addressed by the duplicate-Other fix (there was a phantom second Other from the enforceTop9Other abs-sort bug), but if a negative-AUA Other still appears after the fix, there's a separate classification bug upstream (can't have negative AUA on an aggregate).

---

## Cross-commit scope tracking

| Commit | Files | RD scope | Notes |
|--------|-------|:-:|-------|
| `f1e3880` | types.ts, DistributionTab.tsx, AdvisorsTab.tsx | ✅ | In scope |
| `464b6d5` | AdvisorPublicProfile.tsx | ✅ | In scope (Andrew-authored, bundled) |
| `fbaee59` | DistributionTab.tsx | ✅ | In scope |
| `192c3cc` | DistributionTab.tsx | ✅ | In scope |
| `6f243be` | **src/lib/chartColors.ts** | ⚠️ | **Out of strict RD scope** (`/lib/` not `/pages/AdvisorIntelligence/`). Flagged in commit body. Single-consumer palette grep-verified. DT to decide during ship pass whether to accept or revert to a local override. |
| `11bfc41` | DistributionTab.tsx | ✅ | In scope |
| `d4a31e4` | DistributionTab.tsx | ✅ | In scope |
| `e61cc6e` | types.ts, AdvisorsTab.tsx | ✅ | In scope |

---

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| `comp-transform schema-check DistributionTab` (before) | 1 | baseline captured |
| `comp-transform fields DistributionTab` (before) | 1 | 5 fields — baseline |
| `comp-transform fields PartnerAnalytics` (before) | 1 | 9 fields — baseline |
| `comp-cache collisions` (before) | 1 | 1 shared key |
| `comp-blast ContinuousNnaDivergingView` (before) | 1 | not in graph |
| `comp-transform schema-check DistributionTab` (after) | 3 | ✅ `getTimeseriesOverview` entry added, all rendered fields match |
| `comp-transform fields DistributionTab` (after) | 3 | ✅ 7 fields (added `timeseriesOverview` + `.nna`) |
| `comp-transform fields PartnerAnalytics` (after) | 3 | ✅ unchanged (constraint #2 satisfied) |
| `comp-cache collisions` (after) | 3 | ✅ 2 shared keys — NEW key byte-identical across PartnerAnalytics + DistributionTab |
| `bun run tsc -b` (after each commit) | 3 | ✅ exit 0 after every commit |
| `bun run eslint` on edited files (after each commit) | 3 | ✅ 0 errors |

Compiler-tools-log line appended to `org/compiler-tools-log.md`.

---

## Known caveats

1. The AdvisorPublicProfile.tsx header Identity dedup in `464b6d5` was authored by Andrew directly (via IDE edit, confirmed by him in-session 2026-04-10 ~22:55 EDT). I bundled it into the sweep because (a) it was in my portal working tree when CTO asked me to clear the dirty state, (b) the file is in my RD page scope, and (c) Andrew said "it's your domain". Attribution in the commit body notes he authored the edit.

2. The Fee-Paying / role-filter fix in `e61cc6e` is **latent** until the next gold runner cycle regenerates `employee_leaderboard.json` with the nested `fee_paying`/`no_fee` sub-buckets DS shipped in `d3abb883`. Until then, the fallback behavior matches the previous (buggy) state. Once the file refreshes, the fix activates automatically.

3. The canonical NNA migration in `f1e3880` + `fbaee59` is **conditionally active** depending on whether the current `timeseries_overview.json` has `by_geo`/`by_adv` populated. During Phase 3 manual verification, Andrew confirmed numbers tied between Assets Overview and Segment Analytics and the bar count was 4 for 3Y+Year — consistent with the canonical path being active. If the canonical path is NOT active on a given cache entry, the legacy fallback renders identically to the pre-migration build.

4. The scope crossing in `6f243be` (chartColors.ts) is flagged for DT's review during ship pass. Alternative path: revert that commit and apply the VIBGYOR reorder as a local override inside DistributionTab.tsx. I went with the canonical-file edit because the two palettes are single-consumer and keeping palette definitions in one place is cleaner.

---

## Handoff

Working tree state on portal DEV: clean, 8 commits ahead of `ba90c30`. Per TO requirement 4, RD does NOT push. Broker handoff to 0.4.0_DT_ClientPlatform pending Andrew's final sign-off on the visual verification of the bundled fixes.

---

## Follow-ups

1. Clients-pseudonymization bug in Snapshot-ADV-AUA drilldown — separate hotfix TO needed. PII leak. Surfaced by Andrew in Phase 3 verification.
2. Negative-AUA Other classification bug — may be resolved by `d4a31e4`'s duplicate-Other fix, needs re-verification after DT push.
3. If DT prefers the VIBGYOR palette reorder as a local override, revert `6f243be` and I'll reapply inside DistributionTab.tsx.
4. DS canonical NNA backend ship (ds-brief-advi-nna-canonical-source.md) — still outstanding. When that lands and the next gold runner cycle regenerates `timeseries_overview.json` with `by_geo`/`by_adv`, the canonical path activates automatically and cross-panel NNA parity becomes structural.
