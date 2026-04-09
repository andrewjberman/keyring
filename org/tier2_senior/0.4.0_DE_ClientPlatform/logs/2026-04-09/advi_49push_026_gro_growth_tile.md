# ADVI_49PUSH.026 -- GRO Growth Tile (Phase 2)
**Date:** 2026-04-09
**Instance:** 0.4.0_DE_ClientPlatform~D
**Task Order:** ADVI_49PUSH.026
**Status:** Frontend complete (07aa797); fix_1 Net Flows cross-check blocked on AE gold run completion

**Portal DEV commit:** `07aa797` (committed by base instance before ~D pickup)

---

## Context

COO GO at 18:42 ET: .026 Phase 2 unblocked after DS .023 completion (e3bdf513).
DS~B gold runner triggered (i-01003b035d2988dfb, incremental) — A_01/D_00/D_02/D_04/C_08 scripts uploaded.
AE not registered; messaged AE asking for runner status.

---

## Work Summary (confirmed complete by git log)

### Phase 2 -- Growth tile replacing Total Change (07aa797)

Already committed by base instance. Key changes:

**types.ts** -- `TimeseriesOverviewGroPeriod` updated with optional fields:
- `total_pct?: number` -- % total AUA growth for the period
- `market_pct?: number` -- market contribution as % of beginning AUA
- `nna_pct?: number` -- NNA contribution as % of beginning AUA
- `period_aua_start?: number` -- beginning AUA for cumulative % computation

**aggregatedGroData useMemo** -- passes through all 4 new fields in both branches (with/without timeWindowCutoff).

**GRO hero metrics tiles** -- Total Change tile replaced with Growth tile:
- Primary: `latest.total_pct` as "+X.X%" (green/red), falls back to "--" if field absent
- Sub-lines: "Market: +X.X%" and "NNA: +Y.Y%" from `latest.market_pct` / `latest.nna_pct`
- Cumulative: exact % from `firstAuaStart = aggregatedGroData[0].period_aua_start`
  - `cumTotalPct = (cumMarket + cumNna) / firstAuaStart * 100`
  - `cumMarketPct` and `cumNnaPct` via dollar sums / aua_start
- Null-safe throughout: tile renders "--" until gold run completes and platinum files updated

**GRO chart tooltip** -- "Total Change" relabeled "Total Growth" (line ~1443)

**AdvisorsTab.tsx** -- advisor_id null-guard in rank_delta computation (TS fix; `id = e.advisor_id ?? ''`)

---

## .043 Rank Delta (already committed 3588971 by ~A)

Rank delta column visible in Advisors tab leaderboard. This was ~A's TO.

---

## Outstanding

- **fix_1**: Net Flows tile cross-check against NNA toggle -- deferred to browser QA after AE gold run completes and platinum files updated with `period_start_aua`
- **AE runner**: messaged 0.6.0_AE_PartnerETL for status; awaiting confirmation

---

## Files Modified (by base instance, ~D verified)

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/types.ts | Optional pct fields on TimeseriesOverviewGroPeriod | Yes -- DEV `07aa797` |
| portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx | Growth tile + useMemo pass-through | Yes -- DEV `07aa797` |
| portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx | advisor_id null-guard TS fix | Yes -- DEV `07aa797` |

---

## Next Steps

1. **[AE 0.6.0]** Confirm gold run complete + platinum files updated -- unblocks fix_1 verification
2. **[DE ~D me]** Browser QA: verify Growth tile shows real % values, Net Flows matches NNA toggle
3. **[DS 0.4.0_DS]** DS .045 ratio column findings -- unblocks .046 fix_3
