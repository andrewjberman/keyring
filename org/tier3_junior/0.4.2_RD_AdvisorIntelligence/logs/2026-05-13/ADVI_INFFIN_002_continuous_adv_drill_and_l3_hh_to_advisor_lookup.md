# Session Log — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-05-13 (evening continuation)
**TO:** ADVI_INFFIN.002 rd-advisor-context-wiring (COO dispatch d231643cb)
**Mode:** dispatched RAVC1 (in same flight as .001) → Phase 1 investigation → Phase 2 implementation → ship

---

## Summary

Phase 2 RD ship for ADVI_INFFIN.002 — 2 advisor-context-resolution defects:
1. **Surface #3:** Continuous-ADV-NNA L1 click-to-drill wired; New Clients tile null-elimination
2. **Surface #4:** HH→advisor reverse lookup via FE-iteration of 4 Inflection advisor book.json files, so L3 ClientDetailPage entered via BI deeplink materializes the canonical breadcrumb (advisor book_name + client display_name) and Back-to-Book button

Both surfaces ship same as .001 (no dispatch_held). Routing decision per AC6: FE-iteration (Inflection-gated, 4 advisors only); .004 DS~A directory artifact remains available for when 49F/BD need the same flow.

---

## Portal DEV commits

| Hash | Subject |
|------|---------|
| `25bc115d` | 0.4.2_RD_AdvisorIntelligence: AdvisorIntelligence -- INFFIN.002 ship: Continuous-ADV drill wiring + New Clients null-elim + L3 HH-to-advisor reverse lookup |

---

## Surfaces

### #3 — Continuous-ADV-NNA L1 drill + New Clients tile

**Symptom A root cause:** `ContinuousNnaDivergingView.tsx:1660` left-rail click handler gated on `cohort === 'geo'` for drill behavior:
```
const drillsOnClick = !isOther && !isDrilled && cohort === 'geo' && canDrill
const selectsOnClick = !isOther && !drillsOnClick
```
ADV cohort fell through to `selectsOnClick` — clicking Peter Lee only set `selectedCat` (highlight-only); never set `drillParent`. The per-advisor series in `nna_adv_drill[...]` was therefore never consumed by `barData`; chart stayed firm-aggregate.

**Symptom A fix:**
```
const drillsOnClick = !isOther && !isDrilled && canDrill && (cohort === 'geo' || cohort === 'adv')
```
`canDrill` already includes `canDrillAdv = cohort === 'adv' && (!!(data?.nna_adv_drill) || !!(nnaSeriesView?.categories?.length))` so the click only drills when the data substrate supports it.

After click → `drillParent = peter_lee_key` → `drillSeriesView` resolves via `data.nna_adv_drill[peter_lee]` (DS .033 issue_3 emit) → `barData` recomputes from the per-advisor series → chart re-renders with Peter's per-period inflows/outflows/net. The chart Line color is `NNA_BAR.net` (amber) per the existing canonical wiring; tooltip via `DataTooltip` primitive (already canonical).

Header chip handled by the existing drilled-state ternary at `DistributionTab.tsx:1543` — flips from "{window} Window NNA by Advisor" (firm-aggregate label) to the advisor's display name once `drillParent` is set.

**Symptom B (New Clients tile = '--') fix:** L1565-1589 unchanged structurally; final return now `(newClientCount ?? 0).toLocaleString()` instead of conditional with `'--'` em-dash fallback. Null-elimination rule satisfied per AC2.

**Per-advisor scoping at L1 (Symptom B follow-up):** `data.new_clients_by_period` is firm-wide on `PlatinumCumulativeChartResponse` (`types.ts:2126`); no `by_advisor` breakdown. At L1 drilled-into-advisor view, the tile currently renders firm-wide count. To scope per-advisor would require either:
- (a) DS-side extension: add `new_clients_by_period.by_advisor` to partner_analytics.json
- (b) FE-side fetch: hoist firmOverride into `ContinuousNnaDivergingView` and add a per-drilled-advisor `getPlatinumAdvisorSummary` useQuery to count clients[].relationship_since in the active window

Surfaced to COO as scope-limited follow-up. Not blocking AC2 (which requires "no `--`"). Tile now renders integer (firm-wide); per-advisor scoping is a refinement not a correctness fix.

### #4 — L3 ClientDetailPage unified chrome (HH→advisor reverse lookup)

**Root cause:** `BooksTab.tsx:516` `handleClientClick` is the single handler for both entry paths:
- Inline drill from advisor's book: parent component already has `selectedAdvisorId` set (from the L2 advisor click); calling `setSelectedClientKey` from the AdvisorBookClientList completes the L3 entry. `advisorBookData` is populated from the L2 useEffect; breadcrumb + back button + display_name title materialize.
- BI deeplink (InflectionInsightsPanel HH table click): the click fires `onHouseholdClick: handleClientClick` through the cloned `revenueOpsSlot` (`ClientsTab.tsx:525-530`); `selectedClientKey` gets set but `selectedAdvisorId` stays null. The L3 render at `ClientsTab.tsx:590` proceeds with `advisorBookData = null` → breadcrumb at L601 falls back to `'Advisor'` placeholder; clientName at L592 falls back to raw `selectedClientKey` (the household_id integer).

The InflectionInsightsPanel data rows (`InflectionActivityScanRow`, `InflectionCashDragRow`, `FirmConcentrationsArtifact.securities[].top_holders[]`) have `household_id` but no `advisor_id` field — so the BI click cannot pre-populate advisor context. Reverse lookup is required.

**Fix — FE-iteration approach (AC6 routing decision):**

Per the TO's Phase 1 step 3 ("RD picks path at implementation time. If FE-iteration suffices, .004 DS~A directory artifact deliverable still ships as standalone deliverable but RD doesn't gate on it") and AC6 ("documented in session log — FE-iteration OR .004 directory artifact consumed"), the routing decision: **FE-iteration**, gated to Inflection.

Implementation at `ClientsTab.tsx:518-580`:

1. Derive `inflecAdvisorIds` from `periodAdvisors` (Inflection-only via `isInflectionFirm`).
2. `needsHhLookup = isInflectionFirm && !!selectedClientKey && !selectedAdvisorId && inflecAdvisorIds.length > 0`.
3. `hhAdvisorMap` useQuery: when `needsHhLookup`, parallel-fetch all 4 Inflection advisor books via `getPlatinumAdvisorSummary(advisorId, firmOverride)` (using `Promise.allSettled` so a single fetch failure doesn't deadlock the map). For each successful fetch, iterate `plat.book.clients[]` and accumulate `map[String(client.client_key)] = advisorId`. 5-min staleTime, no refetch-on-mount/window-focus.
4. Follow-up effect: when `hhAdvisorMap` resolves and contains the active `selectedClientKey`, `setSelectedAdvisorId(advisorId)`. This triggers the existing L2 advisorBookData useEffect (L368-405), which fetches the advisor's full book → breadcrumb book_name + Back-to-Book button + clientName lookup all materialize.

**UX nit:** there's a brief window (1 paint + ~150ms book fetches) where the user lands on L3 with the placeholder breadcrumb before the lookup resolves. Functionally correct per AC4-5; for further polish a loading skeleton could be added at L590 gated on `needsHhLookup`. Out of scope for this ship.

**Routing decision (AC6):** FE-iteration, Inflection-gated. Documented inline in the new useQuery's JSDoc. For 49F/BD when the same flow is needed, switch to .004 DS~A directory artifact (`platinum/firm/client_directory.json` O(1) lookup).

---

## Acceptance Criteria

| AC | Surface | Status |
|----|---------|--------|
| AC1 | #3 chart filtering | ✓ Click Peter Lee → bars/line redraw with his series; header chip flips to per-advisor label via existing drilled-state ternary; All Advisors → firm aggregate |
| AC2 | #3 New Clients null-elim | ✓ `(newClientCount ?? 0).toLocaleString()` — no `--` em-dashes |
| AC3 | #3 L0 sum | Partial — firm-wide count at L0 already correct (existing wiring). At L1 drilled-into-advisor, tile shows firm-wide (per-advisor scoping deferred — see Symptom B follow-up note above). Andrew/COO call on whether the L1 per-advisor refinement is required for closure. |
| AC4 | #4 unified chrome | ✓ After hhAdvisorMap resolves, BI-deeplink L3 renders identical chrome to From-Peter's-Book path — advisor breadcrumb book_name + Back-to-Book + clientName lookup. Note: L3 page does NOT have Profile/Book toggle (that's at L2 via AdvisorPublicProfile); the TO's description of "L3 chrome includes Profile/Book toggle" describes what exists upstream when navigating to L3 — not added to the L3 page itself. |
| AC5 | #4 lookup | ✓ All 4 Inflection advisors iterated in parallel; Promise.allSettled keeps partial map on single-advisor failure |
| AC6 | #4 routing | ✓ FE-iteration approach documented (see Surface #4 above). Gated to Inflection. For 49F/BD route to .004 DS~A directory artifact. |
| AC7 | NNA canonical primitive consumption | ✓ Surface #3 NNA chart uses existing canonical NNA_BAR colors + DataTooltip primitive (consumes the .001 primitives in pattern, not in literal import — the chart's bar+line shape already canonical). The new `<NnaBarLineChart>` primitive available for future migration if the chart's interaction logic warrants the rebind. |
| AC8 | tsc | ✓ 0 errors after every Edit |
| AC9 | dev smoke | Dev server :5175 stayed live through HMR cycle. Visual smoke pending Andrew confirmation on Patrick + Peter Lee Continuous-ADV-NNA flow and BI → L3 deeplink chrome. |

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `comp-transform schema-check` | DistributionTab, ContinuousNnaDivergingView | Ran during .001 phase 1; ternary-audit surfaced cohort gaps already-patched in progressive shipments. No new gaps in scope of #3 fix (the click handler gate is at L1660 — drillsOnClick wiring, not a ternary inside a render). |
| `comp-transform fields` | AdvisorPublicProfile, PlatinumAdvisorSummary | Located NNA `inflows_canonical` / `outflows_canonical` / `nna_canonical` fields on `AdvisorTimeseriesPoint`; `clients[].client_key` + `clients[].relationship_since` on `PlatinumAdvisorSummary.book` — confirmed both paths data-available client-side. |
| `bun run tsc --noEmit` | portal full | 0 errors after each Edit |
| `curl http://localhost:5175/` | dev server | 200 throughout |

---

## Routing Decisions (AC6 explicit)

| Decision | Surface | Outcome |
|---|---|---|
| Continuous chart accessor — exists or adapter needed | #3 | Exists: `data.nna_adv_drill[advisorKey]` resolves to per-advisor NNASeriesPoint[] via `drillSeriesView` useMemo at L1306-1342. Wiring fix at the click-handler gate suffices; no shape mismatch. **Not routed to .003 DS~C.** |
| HH→advisor lookup approach | #4 | FE-iteration. 4 advisors parallel-fetched via `getPlatinumAdvisorSummary`. Gated to Inflection (`isInflectionFirm`). **.004 DS~A directory artifact NOT consumed today** — remains available as O(1) substitute if 49F/BD need the same flow. |
| Per-advisor New Clients tile scoping | #3 sub | Deferred — surfaced to COO as scope-limited follow-up. Null-elim AC2 fully met; per-advisor refinement not blocking. |

---

## Pending Items at Session End

| Item | Owner | Status |
|---|---|---|
| ADVI_INFFIN.002 RAVC2 → COO | COO | Sending |
| Visual smoke (Andrew) | Andrew | Standing by for confirmation on Continuous-ADV-NNA Peter Lee drill + BI → L3 deeplink chrome |
| ADVI_INFFIN.006 Phase 2 wiring | RD 0.4.2 | dispatch_held — awaiting COO unblock post .007 AE chain |
| Per-advisor New Clients tile (Symptom B follow-up) | RD 0.4.2 if needed | Scope-limited; deferred per AC2 satisfaction. Recommend DS-side `by_advisor` extension OR FE firmOverride hoist + per-advisor book.json useQuery in ContinuousNnaDivergingView. |

---

## Status

Ready to send RAVC2 to COO. Bench-available for .006 unblock + Andrew visual smoke confirmations.
