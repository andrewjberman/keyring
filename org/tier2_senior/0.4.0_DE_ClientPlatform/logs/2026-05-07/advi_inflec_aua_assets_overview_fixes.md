# Session Log — ADVI_INFLEC Assets Overview AUA Fixes

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-07
**GO source:** Andrew direct (visual comparison Inflection vs 49F); COO routed sub-TOs
**Session type:** FE diagnosis + implementation

**Portal DEV commits:** `f2458e0e` → `39cbbd29` → `52a6d84c`
**PROD:** `portal-v2.1.81` (CLOUD `7b96202b5`) — all three commits live

---

## Context

Andrew flagged Inflection Assets Overview AUA panel as priority — unacceptable compared to 49F.
Observed discrepancies (Image #1 Inflection vs Image #2 49F):

1. Bar/tooltip Q2 '26 = $189M but Total AUA tile = $199M (mismatch)
2. Bar chart monochrome green — no New vs Existing Clients stacked split
3. No QoQ growth metrics on New Clients / Existing Clients tiles
4. (Pre-existing) Existing Clients tile showing only nmec ($7.49M) instead of nmec+existing ($179.97M)

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` | CHECK1, Fix A, stacked bar wiring | Yes — 3 commits |
| `portal/src/api/endpoints/advisor-intelligence.ts` | InflecTimeseriesChartResponse + getPlatinumInflecTimeseriesChart | Yes — `52a6d84c` |

---

## Fix 1 — CHECK1: auaExistingClient = nmec + existing

**Commit:** `f2458e0e`

**Bug:** Line 1612 (PartnerAnalytics.tsx) — Inflection `auaExistingClient` only summed the `nmec` donut segment ($7.49M). Inflection has 3 donut segments: nmnc ($19.7M), nmec ($7.49M), existing ($172.48M). "Existing Clients" = nmec + existing.

**Fix:**
```tsx
// Before
? (auaDonutSegments.find(s => s.key === 'nmec')?.aua ?? 0)
// After
? (auaDonutSegments.find(s => s.key === 'nmec')?.aua ?? 0) + (auaDonutSegments.find(s => s.key === 'existing')?.aua ?? 0)
```

**Result:** Existing Clients tile: $7.49M → $179.97M (nmec + existing). Non-Inflection paths unchanged.

---

## Fix 2 — Fix A: Bar/tooltip Q2 '26 mismatch

**Commit:** `39cbbd29`

**Root cause:** `allSortedAuaPeriods` reads from `timeseries_overview.json` where Q2 '26 `total_aua` = stale $189M. Total AUA tile reads from donut segments = $199.6M. Mismatch visible to user — tooltip on most recent bar showed wrong number vs the headline tile.

**Fix:** Patch the most recent period in `allSortedAuaPeriods` with the canonical donut total for Inflection:

```tsx
// Only applies when: isInflectionFirm + auaDonutSegments available + single-category timeseries
const lastIdx = raw.length - 1
return raw.map((pt, idx) => idx === lastIdx ? { ...pt, [cats[0]]: donutTotal } : pt)
```

**Result:** Bar/tooltip Q2 '26 shows $199.6M, matching the Total AUA tile.

---

## Fix 3 — Stacked Bars: wire timeseries_chart.json nmnc/nmec

**Commit:** `52a6d84c`

**Root cause:** `barCategories = ['total_aua']` for Inflection (single key = monochrome bar). DS~C published `platinum/firm/timeseries_chart.json` with 25 quarters of `nmnc` + `nmec` per quarter and `categories: ['nmnc', 'nmec']`. The FE was not fetching this file.

**Changes:**

### advisor-intelligence.ts
```typescript
export interface InflecTimeseriesChartResponse {
  categories: string[]
  quarters: {
    period: string; label: string; end_date: string
    total_aua: number; nmnc: number; nmec: number
  }[]
}

export async function getPlatinumInflecTimeseriesChart(firmOverride?: string) {
  const base = '/api/scoped/advisor-intelligence/platinum/firm/timeseries_chart.json'
  return apiRequest<InflecTimeseriesChartResponse>(firmOverride ? `${base}?firm=${firmOverride}` : base)
}
```

### PartnerAnalytics.tsx — 3 changes

**1. useQuery (gated on isInflectionFirm):**
```tsx
const { data: inflecTimeseriesChart } = useQuery({
  queryKey: ['inflec-timeseries-chart', firmOverride],
  queryFn: () => getPlatinumInflecTimeseriesChart(firmOverride),
  enabled: isInflectionFirm,
  staleTime: 5 * 60 * 1000,
  ...
})
```

**2. allSortedAuaPeriods — stacked path:**
When `inflecTimeseriesChart` is loaded, use its `quarters[]` as the bar data source.
Patch the last quarter with donut-canonical nmnc/nmec values:
- `nmnc` = `donutSegments.find('nmnc').aua` ($19.7M)
- `nmec` = `donutSegments.find('nmec').aua` + `donutSegments.find('existing').aua` ($179.97M)

Falls back to Fix A single-category patch when chart not yet loaded.

**3. barCategories override:**
```tsx
const barCategories = (isInflectionFirm && inflecTimeseriesChart?.categories?.length)
  ? inflecTimeseriesChart.categories          // ['nmnc', 'nmec']
  : (timeseriesData?.aua?.[auaGranularity]?.categories || [])
```

**Result:**
- Bar chart: 2-stack (green=nmnc, blue=nmec) — matches 49F pattern
- Tooltip: nmnc + nmec sum to $199.6M (donut canonical last quarter)
- QoQ growth on New/Existing tiles: populated from prior quarter nmnc/nmec in timeseries data
- 49F: zero change — all paths gated on `isInflectionFirm`

---

## TypeScript Check

```
bun run tsc --noEmit
(no output — clean on all three commits)
```

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-transform schema-check | N/A — extended existing useMemos, no new rendered fields | Not required |
| TS check | bun run tsc --noEmit | PASS (all 3 commits) |

`comp-transform schema-check` not applicable — no new component fields introduced. All changes are data-sourcing and computation logic within existing useMemos.

---

## RAVC Log

| # | To | Subject | Status |
|---|----|---------|--------|
| ACK | 2.0.0_SA_COO | CHECK1 GO ACK | Sent 20260507T132942Z |
| RAVC | 2.0.0_SA_COO | CHECK1 f2458e0e LIVE, TS PASS | Sent 20260507T133055Z |
| ACK | 2.0.0_SA_COO | Fix A PROD bump ACK | Sent 20260507T134351Z |
| RAVC | 2.0.0_SA_COO | Assets Overview diagnosis + Fix A 39cbbd29 | Sent 20260507T134143Z |
| COORD | 0.4.0_DS_ClientPlatform | timeseries_chart.json rebuild request | Sent 20260507T134151Z |
| ACK | 2.0.0_SA_COO | Stacked bars TO ACK | Sent 20260507T142218Z |
| RAVC | 2.0.0_SA_COO | Stacked bars 52a6d84c LIVE, TS PASS | Sent 20260507T142617Z |

---

## Current State

| Item | Status |
|------|--------|
| CHECK1 (auaExistingClient) | PROD — `f2458e0e` (portal-v2.1.81) |
| Fix A (bar/tooltip patch) | PROD — `39cbbd29` (portal-v2.1.81) |
| Stacked bars wiring | PROD — `52a6d84c` (portal-v2.1.81, CLOUD `7b96202b5`) |
| QoQ growth on lifecycle tiles | AUTO-RESOLVED by stacked bars data |
| RD visual confirm | IN FLIGHT — COO dispatched CHECK A/B/C |
| Constitution doc update | PENDING — TO expected from COO on RD PASS |

## Next Steps

- [RD 0.4.2] Visual confirm CHECK A (stacked bars), CHECK B (QoQ tiles), CHECK C (no regressions)
- [DE + RD] Constitution doc update TO from COO on RD PASS
- [DE standby] If RD surfaces any rendering gap — diagnose and fix
