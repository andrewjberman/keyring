# Session Log — 0.4.2_RD_AdvisorIntelligence
# Inflection Segment Analytics — New Clients emit gap + GEO L1 State bell-curve median

**Date:** 2026-05-15
**Mode:** Andrew-direct investigation x2 (Continuous "New Clients" tile; Snapshot bell-curve median)
**Portal commit:** `1ac05055` (DEV) — GEO L1 State median fix
**DS handoff:** brief to DS~A for `new_clients_by_period` emit (shipped by DS~A as `4e4a3c321`)

---

## Task 1 — Continuous view "0 New Clients" (Inflection)

**Symptom:** ADVI Distribution > Segment Analytics > Continuous shows `0 New Clients`, both AUA + NNA modes.

**Verdict:** Gold emit gap (DS lane). FE is correct.

- Both tiles in `DistributionTab.tsx` (NNA-mode L1655-1687, AUA-mode L2491-2522) read `data?.new_clients_by_period?.[periodKey]`, sum within window, fall back to 0 when absent.
- `s3://opal-data-inf/platinum/firm/cumulative_chart.json` has **no** `new_clients_by_period` key. `s3://opal-data-bd/.../cumulative_chart.json` (49F) has it — same FE code path works there.
- Inflection's `INF_D_00d.cumulative_chart.py` `main()` never emits the block; 49F's `D_04.client_portal_summary.py:2129-2172` does.

**Action:** wrote `deliverables/brief_ds_inflection_new_clients_by_period.md` — full drop-in (builder fn + main() wiring + exact FE-contract shape + ground-truth verification counts). Source = `accounts_v2.account_start_date`, household grain. MCP'd DS~A.

**Outcome:** DS~A shipped `4e4a3c321` (INF_D_00d, +59 lines, additive). Builder verified vs my section-5 ground truth — exact match (296 households, formats verbatim). Materializes on the 2026-05-16 06:00Z chain run. Zero FE change.

## Task 2 — Snapshot bell curve: no Median at GEO L1 (State)

**Symptom:** median account bell curve shows for L0 firm, GEO L2 city, ADV L1 advisor — but not GEO L1 (State).

**Verdict:** FE mapping issue, not data gap. RD lane. Fixed.

Inspected `s3://opal-data-inf/platinum/firm/partner_analytics_quarterly.json`:

| Level | FE data source | `percentiles.p50` | `median` field | FE handling |
|---|---|---|---|---|
| L0 firm | `geo.current.distribution.total` | present | `null` | `withSynthesizedPercentiles` -> p50->median ✓ |
| GEO L2 city | `segment.cities[].distribution` | present | populated | raw (has median) ✓ |
| ADV L1 | `adv` donut seg inline `.distribution` | present | populated | raw (has median) ✓ |
| GEO L1 state | `distribution.by_segment[STATE]` | **present** | **`null`** | **raw — not wrapped** -> N/A |

GEO state donut segments carry no inline `.distribution`, so the `distributionData` memo resolves the L1 bell curve from `distribution.by_segment[STATE]`. All 18 GEO `by_segment` entries have a valid histogram + `percentiles.p50` but `median:null`. The four L1 `parentSegment` returns (`DistributionTab.tsx:3187-3201`) returned the object raw — unlike the L0 path which wraps in `withSynthesizedPercentiles` (the INFFIN.023 `p50 -> median` propagation).

**Fix (`1ac05055`):** wrapped all four L1 `parentSegment` returns in `withSynthesizedPercentiles`. No-op when median already populated (ADV L1). Post-fix WA state Median chip renders `$100,566` (was N/A).

DS~A not needed for Task 2 — no gold change.

## Task 3 — GEO Snapshot counts show households where UI says "Accounts"

**Symptom (Andrew, AUA-mode GEO Snapshot):** bell curve container shows 801 at L0 (correct = accounts) but 251 when drilled into Washington — yet the L0 donut legend calls WA "685 Accounts". Counts must canonically be account-grain.

**Verdict:** FE grain bug, two sites. RD lane. Fixed (`79a512bd`).

Inspected `partner_analytics_quarterly.json` — WA donut segment: `account_count=685`, `client_count=251`; `by_segment['WA'].count=251` (households).

1. **Bell curve container, GEO L1 (State):** `distributionData` memo returned `by_segment[STATE]` (and the city-agg fallback) without an account-grain count override. `by_segment[*].count` is household-grain on Inflection → container read 251. Fix: override every L1 `parentSegment` return with `_getBellCount(parentSegment)` (`account_count ?? client_count`), same invariant as the L0 path's `firmAccountCount`. WA L1 → 685.
2. **GEO city-drill donut legend:** `segments` memo's city map (L2989) dropped `account_count`/`relationship_count`, so `getRadialCount` fell back to `client_count` — Everett rendered "46 Accounts" (households) vs true 144. Fix: carry both fields through the map.

Also removed `grainView`/`geoAuaGrain` from the `distributionData` dep array — unreferenced after the L1 override replaced the `getRadialCount` call.

## Task 4 — errant route: Continuous GEO L2 city click goes to Books tab

**Symptom (Andrew):** Continuous-GEO-AUA, drilled into a state — clicking an L2 city navigates to Books tab L0 instead of showing the city's period-over-period.

**Verdict:** FE errant route. RD lane. Fixed (`92365e05`).

`ContinuousChartView`'s drilled-legend click handler (`DistributionTab.tsx:2596-2610`) computes `isInflectionHh = !isOther && firmOverride === 'inflection' && !!onNavigateToBooksClient` with no cohort gate. The INFFIN.024 §3.5d HH-to-Books navigation is correct for the **ADV** cohort (advisor drill lists households; HH click opens Books) — but the **GEO** cohort's drilled children are **cities** (state→city is terminal). So every Inflection GEO city click hit `onNavigateToBooksClient(drillParent, cat)` → Books L0.

**Fix:** gate `isInflectionHh` on `cohort === 'adv'`. GEO city clicks now fall through to `setSelectedChildKey` (collapse-to-series) → city period-over-period. 49F unaffected.

---

## Compiler Tools

| Tool | Target | Result |
|---|---|---|
| `bun run tsc --noEmit` | portal full | 0 errors (exit 0) |
| `bun run lint` | portal full | 10 warnings, 0 errors — unchanged from baseline; this patch added 0 |
| `comp-transform schema-check` | — | Not run — no component-contract change; pure data-resolution logic inside an existing memo, no new rendered field |

Direct S3 artifact inspection (`aws s3 cp` + python json) was the decisive tool for both tasks — confirmed emit presence/absence and the median/p50 field divergence.

---

## Files Modified

| File | Repo/Branch | Change | Commit |
|---|---|---|---|
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx` | portal/DEV | Task 2: 4 L1 returns wrapped in `withSynthesizedPercentiles` | `1ac05055` |
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx` | portal/DEV | Task 3: L1 account-grain count override + city-map `account_count` carry-through | `79a512bd` |
| `portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx` | portal/DEV | Task 4: gate `isInflectionHh` on `cohort==='adv'` — GEO city click no longer routes to Books | `92365e05` |
| `org/.../deliverables/brief_ds_inflection_new_clients_by_period.md` | workspace/CLOUD | new — DS~A brief | (this log's commit) |
| `org/.../logs/2026-05-15/...` | workspace/CLOUD | this log | (this commit) |

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Push portal DEV (`1ac05055` + `79a512bd` + `92365e05`) + bundle for release — GEO L1 State median + account-grain counts + errant-route fix, all FE-only (no artifact dependency).
2. **[2026-05-16 06:00Z chain]** materializes `new_clients_by_period` in Inflection `cumulative_chart.json` — Continuous "New Clients" tile goes live, no FE work.
3. **[Andrew]** visual confirm both surfaces post-deploy.

## Blockers

None.
