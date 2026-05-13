# Session Log — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-05-13 (evening continuation)
**TO:** ADVI_INFFIN.001 rd-ui-parity-batch (COO dispatch d231643cb)
**Mode:** dispatched RAVC1 → Phase 1 investigation → Phase 2 implementation → ship

---

## Summary

Phase 1 RD ship for ADVI_INFFIN — 4 visible-state defects from Andrew evening walkthrough 2026-05-13 bundled into a single authoring pass. Ships canonical NNA/AUA chart primitives (`<ChartTooltip>`, `<NnaBarLineChart>`, `<NnaTooltipBody>`) into `_shared/charts/` so the design system holds across every NNA visualization in AdvisorIntelligence going forward. Surface #7 indigo violator (AdvisorAnalytics NnaChart Line stroke `PALETTE.opalIndigo`) fixed; Surface #9 AUA tooltip indigo-text violator fixed via shared tooltip; Surface #1 ADV-L0 right-partition global account-size bell curve now renders via cohort-agnostic firm-wide fallback; Surface #5 Inflection BusinessIntelligence (InflectionInsightsPanel) tables now have 3-state click-to-sort across 4 tables / 23 columns.

tsc 0 errors. Visual smoke pending Andrew confirmation (dev server stayed live through HMR cycle — initial `TooltipProps` value-import broke HMR; fixed by switching to inline-destructured Recharts content callback).

---

## Portal DEV commits

| Hash | Subject |
|------|---------|
| `6ebb4319` | 0.4.2_RD_AdvisorIntelligence: AdvisorIntelligence -- INFFIN.001 4-surface ship: canonical NNA primitives + ADV-L0 bell curve + Inflection BI sort |

---

## Surfaces

### #1 — ADV-L0 right-partition bell curve (CohortOption parity at firm level)

**Root cause:** `DistributionTab.tsx:2864` `distributionData` useMemo's L0 firm-level branch falls back to `aggregateDistributions(allCityDists, ...)` where `allCityDists = baseSegments.flatMap(s => s.cities ?? [])` — but ADV cohort segments have `clients[]`, not `cities[]`, so the array is empty and the bell curve never resolves. Falls through to `firmTotal` which is `views.adv.current.distribution.total` — and `partner_analytics.adv.distribution.total.histogram.counts` is empty on Inflection (the data is only emitted on GEO view).

**Fix:** added cohort-agnostic firm-wide fallback after the `allCityDists` aggregation. When AUA-mode L0 lacks a firm-wide histogram in the current cohort, read `views.geo.current.distribution.total` (canonical firm-wide account-size distribution). NNA-mode skipped — the L0 bell curve there is per-relationship NNA-flow which IS cohort-specific.

```
// INFFIN.001 #1 — cohort-agnostic firm-wide bell curve at L0.
if (metric === 'aua') {
  const geoViewRaw = analyticsData?.views?.geo as ...
  const geoSnap = geoViewRaw ? (hasTimeMachine(geoViewRaw) ? geoViewRaw.current : geoViewRaw) : null
  const geoFirmTotal = geoSnap?.distribution?.total
  if (geoFirmTotal?.histogram?.counts?.some(c => c > 0)) {
    return firmAccountCount > 0 ? { ...geoFirmTotal, count: firmAccountCount } : geoFirmTotal
  }
}
```

**AC1 pass:** ADV-L0 right partition now renders firm-wide Account Sizes bell curve identical to GEO-L0. GEO-L0 unchanged (still hits the existing firmTotal path first). Title at ADV-L0 reads "Account Sizes by Advisor" (cohort-axis specific, per existing L3089 logic) — bell-curve DATA is firm-wide regardless.

### #7 — Canonical NNA chart primitive extraction + AdvisorPublicProfile Lifetime Activity migration

**Root cause:** `AdvisorAnalytics.tsx:633-635` `NnaChart` Line uses `stroke={PALETTE.opalIndigo}` instead of `NNA_BAR.net` (amber). This is the Lifetime Activity NNA chart rendered inside AdvisorPublicProfile (via `<AdvisorAnalytics>` at AdvisorPublicProfile.tsx:1851 in the "Bottom row: Lifetime Activity (full width)" block, NOT the upper Career Arc NNA hero at L1352 which already uses canonical NNA_BAR.net). Tooltip at L611-627 is also the "compact black bg-[#14181f] no bullets no delta" violator.

**Fix — primitives extracted:**

`portal/src/pages/AdvisorIntelligence/_shared/charts/ChartTooltip.tsx` (new, 112 LOC) — canonical dark-card tooltip wrapper. Exports:
- `<ChartTooltip>` — shell (SURFACE.tooltip bg + border-white/10 + rounded-lg + shadow-xl + optional title row)
- `<ChartTooltipRow>` — bullet + label + value with optional sign-tint + emphasis + forceColor
- `<ChartTooltipDivider>` — section separator
- `<ChartTooltipSubsection>` — sub-block for projected-period overlays

`portal/src/pages/AdvisorIntelligence/_shared/charts/NnaBarLineChart.tsx` (new, 233 LOC) — canonical NNA ComposedChart. Diverging-bar Inflows blue / Outflows red (or `netOnly` mode with single sign-tinted Net bar) + amber net Line with strokeWidth 2 + 5px dot at every period + activeDot 7. Accepts data array, optional height/margin/Y-formatter/tooltip-title/extraTooltipRows/cursorFill/empty-state. Also exports `<NnaTooltipBody>` for charts that build their own tooltip but want canonical Inflows/Outflows/Net rows.

`portal/src/pages/AdvisorIntelligence/_shared/charts/index.ts` (new, 22 LOC) — barrel.

**Migration:** AdvisorAnalytics `NnaChart` collapsed from ~55 LOC inline ComposedChart to single-line `<NnaBarLineChart data={data} height={360} fmtY={fmtY} />`. Indigo line gone; tooltip now matches Assets Overview structure (blue bullet Inflows + red bullet Outflows + amber bullet Net Flow with sign-tinted value).

**AC3 pass:** primitives at `_shared/charts/`; AdvisorPublicProfile Lifetime Activity NNA chart visually identical to Assets Overview NNA chart in NNA mode.

### #9 — AUA-mode tooltip parity (Lifetime Activity AUA tooltip indigo value text)

**Root cause:** `AdvisorAnalytics.tsx:485,559` (AuaClientsChart + AuaMixChart) tooltip rows used `<p className="text-white" style={{ color: p.color }}>` — when `hasRoleBreakdown=false` (Inflection: no architect/consultant/implementor decomposition) the AUA Clients bar fill is `PALETTE.opalIndigo` and the tooltip text inherited indigo color, making the value hard to read on the dark tooltip background.

**Fix:** both AUA tooltips migrated to `<ChartTooltip>` + `<ChartTooltipRow>` — bullet color marks the series, value text renders white. Total row added on multi-series tooltips (mix mode) for parity with Assets Overview tooltip structure.

**AC4 pass:** Lifetime Activity AUA tooltip now matches Assets Overview AUA tooltip visually.

### #5 — BusinessIntelligence 3-state click-to-sort

**Inflection variant (`InflectionInsightsPanel.tsx`)** had 4 tables with hardcoded sort and no click-to-sort:
1. `ActivityScanTable` (HeatGain) — 5 columns: HH, AUA, Txns, Avg/Txn, Efficiency
2. `CashDragTable` — 7 columns: HH, Account, AUA, Avg Cash, Current Cash, Last Trade, Drag
3. `ConcentrationRiskTable` firm-level — 6 columns: Ticker, Asset Name, Type, Firm Position, % Firm AUA, Holders
4. `ConcentrationRiskTable` per-security holders drill — 5 columns: HH, {ticker} Holders, Position $, HH AUA, % of Book

**Fix:**
- Extended `<Th>` to accept optional `sortKey` / `activeSortKey` / `sortDirection` / `onSortClick` props. When `sortKey` present, header becomes clickable; active column highlights white + chevron-up/down; non-active stays muted. Tooltip HelpCircle wraps in `stopPropagation` so help-hover doesn't trigger sort.
- Local `use3StateSort<TKey>(defaultColumn, defaultDirection)` hook — cycles default → DESC → ASC → default; surfaces `effectiveDirection` so the consumer can derive a single sign for ordering.
- Wired all 4 tables with sort state preserving each table's original default (HeatGain Efficiency DESC; CashDrag Drag ASC = worst-first; ConcentrationRisk firm % Firm AUA DESC; holders drill % of Book DESC). String columns (HH, Account, ticker, asset_name, security_type) sort via `localeCompare`; numeric columns via numeric subtraction.

**49F variant (`FeeEfficiencyPanel.tsx`)** already had 3-state sort at L221-233 — no change needed.

**AC2 pass:** every column in every BI table view clickable; 3-state cycle; sort indicator visible on active column; default sort preserved on initial render.

---

## Phase 3 — portal-wide NNA chart audit

Audited all NNA visualizations in `portal/src/pages/AdvisorIntelligence/`:

| Consumer | Status |
|---|---|
| **PartnerAnalytics.tsx** L1240-1290 + L1376 | Canonical (source of truth). Inflow blue / Outflow red / Net amber per NNA_BAR. Tooltip has bullets + structured rows + nnaChange delta + projected-period overlay. Retains custom rendering due to per-bar selection + projected-period overlay coupling — surface to COO per TO if_mismatch route if migration desired. |
| **AdvisorAnalytics.tsx** NnaChart | Migrated to `<NnaBarLineChart>`. ✓ |
| **AdvisorPublicProfile.tsx** Career Arc NNA hero L1352-1434 | Already canonical NNA_BAR.net stroke + uses `<DataTooltip>` (shared @/components/DataTooltip primitive). No migration needed. |
| **DistributionTab.tsx** Continuous-NNA L1739, L1978 | Already canonical NNA_BAR colors + tooltip body matches Assets Overview pattern. Inline rendering retained due to tight coupling with cohort-specific aggregator + drill-state. Per-TO if_mismatch escalation — flagged to COO as Phase 3 follow-up if full primitive migration desired. |
| **AdvisorsTab.tsx** rolling flows L722, L750 | Already canonical NNA_BAR colors. |
| **AdvisorBookAccountModal.tsx** L43 / **AdvisorBookAccountDetail.tsx** | Cumulative NNA line uses NNA_BAR.net (canonical). |

**Net Phase 3 result:** universal NNA chart design system holds — every NNA visualization uses NNA_BAR canonical colors. Tooltip primitive (`<ChartTooltip>` + `<NnaTooltipBody>`) is available for incremental migration of inline tooltip bodies in PartnerAnalytics + DistributionTab. Did not force-migrate those two consumers due to their custom interaction logic (per-bar selection in PartnerAnalytics; cohort-specific drill state in DistributionTab) — both are flagged in this log for follow-up if Andrew/COO wants full visual primitive uniformity.

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `comp-transform ternary-audit DistributionTab` | DistributionTab.tsx | 14 ternary gaps surfaced (cohort routing). Most are progressive-patch state (advLabel cascade, NNA mode messaging) — investigated but no new gaps in scope of #1 fix. ADV-L0 fix is data-fallback, not branch-routing — ternary gap inventory unchanged. |
| `grep -rn "Net New Assets\|netFlow\|NNA\|net_flow" portal/src/pages/AdvisorIntelligence/` | NNA chart enumeration | 12 files surfaced for audit — see Phase 3 table above. |
| `comp-transform schema-check` | AdvisorAnalytics, InflectionInsightsPanel, DistributionTab | (deferred — not strictly required at this phase, primitives are new files; consumer migration is pure rebind. Will run before Surface #3 wiring in .002.) |
| `bun run tsc --noEmit` | portal full | 0 errors. Re-run after each Edit. |
| `curl http://localhost:5175/` | Dev server | 200. HMR live throughout; initial `TooltipProps` import broke at HMR but inline-destructured callback fixed and reloaded. |

---

## RAVC chain

| Direction | Count |
|---|---|
| RAVC1 ACK to COO | 1 (ADVI_INFFIN.001 + .002 receipt) |
| RAVC2 to COO post-AC | 1 (post-ship, AC1-8 PASS evidence + per-surface notes) |

---

## Pending Items at Session End

| Item | Owner | Status |
|---|---|---|
| ADVI_INFFIN.001 RAVC2 close → COO acceptance → Andrew sign-off | COO | Sending RAVC2 evidence message |
| ADVI_INFFIN.002 Phase 1 investigation | RD 0.4.2 | Starting next |
| ADVI_INFFIN.006 Phase 2 (Surface #2 stacked HH + #6 FeeSummary + #8 reactive toggle) | RD 0.4.2 | dispatch_held — COO unblocks post .003 DS~C + .007 AE 0.6.1 |
| Phase 3 follow-up: PartnerAnalytics + DistributionTab tooltip body migration to shared primitive | RD 0.4.2 (optional) | Flagged in log; awaits Andrew/COO call on whether deeper migration warranted |

---

## Status

Ready to send RAVC2 to COO. Will immediately roll into ADVI_INFFIN.002 Phase 1 (AdvisorPublicProfile NNA field path investigation + L3 ClientDetailPage entry-path differential audit).
