# Session Log — ADVI_INFLEC AUA Reconciliation (Priority Override)

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-06
**GO source:** COO 20260506T204549Z (CRITICAL — Andrew personal portal smoke)
**Session type:** FE diagnosis + fix

---

## Context

Andrew hit AUA reconciliation failures in portal smoke. Canonical total_aua = $199,649,186.31.

Discrepancies observed:
1. Assets Overview → AUA → Clients mode: Total $189M (off $10.5M), NMNC $0, NMEC $0
2. Assets Overview → AUA → Mix mode: $187.3M (off $12.2M)

---

## Fetch Chain

- Component: `PartnerAnalytics.tsx`
- Query: `useQuery(['advisor-intelligence', 'timeseries-overview', firmOverride])`
- Function: `getTimeseriesOverview(firmOverride)` → `advisor-intelligence.ts:462`
- Endpoint: `GET /api/scoped/advisor-intelligence/artifacts/timeseries_chart.json?firm=inf`

---

## Phase 0 FE Diagnosis

### Finding 1 — Mix $187.3M (FE BUG, confirmed)

`firmMixChartData` useMemo (line 254-268):
- Mapped: equity, fixed_income, alternatives — NO cash
- `FirmMixPeriodPoint.cash` IS in type (types.ts:1530) but not mapped
- Bar stack (line 1359): `['alternatives', 'fixed_income', 'equity']` — no cash Bar
- Stats tiles (line 1704): no cash tile
- Tooltip CLASS_LABELS (line 1323): no cash entry

Effect: Mix total = $199.6M - $12.3M cash = $187.3M — matches Andrew's observation.

### Finding 2 — AUA Clients $189M / NMNC $0 / NMEC $0 (FE passthrough — DS~A lane)

- `barCategories = timeseriesData.aua.quarterly.categories` — gold artifact driven
- `auaNewClient = src['NMNC'] || src['nmnc'] || 0` — FE reads both casing variants
- FE sums exactly what gold provides; does NOT filter or modify
- `lifecycle_aua` not used in PartnerAnalytics — NMNC/NMEC come from period data fields
- $189M = sum of whatever is in `categories[]` for Inflection
- NMNC = $0, NMEC = $0 → artifact doesn't have `NMNC`/`NMEC` field names (or they're 0)
- Root cause: DS~A gold artifact `timeseries_chart.json` field naming / lifecycle coverage

---

## Fix — Finding 1 (4 changes to PartnerAnalytics.tsx)

1. `firmMixChartData` useMemo: added `cash: pt.cash?.value ?? 0, cash_pct: pt.cash?.pct ?? 0`
2. Bar stack: `['cash', 'alternatives', 'fixed_income', 'equity']` (cash = bottom, amber500)
3. Tooltip CLASS_LABELS: added `'cash': 'Cash'`
4. Stats tiles: added `'cash'` / `'Cash'` to tile array

After fix: Mix bars = equity + fixed_income + alternatives + cash ≈ $199.6M ✓

### Commit

`960c289a` (portal DEV, 2a9dcf97..960c289a)

---

## RAVC Log

| # | To | Subject | Status |
|---|----|---------|--------|
| RAVC1 | 2.0.0_SA_COO | GO ACK — Phase 0 executing | Sent 20260506T204600Z |
| RAVC2 | 2.0.0_SA_COO | Phase 0 complete — 2 findings | Sent 20260506T205039Z |
| RAVC2 | 0.4.0_DS_ClientPlatform | Coordination — categories[] question | Sent 20260506T205044Z |
| RAVC1 | 2.0.0_SA_COO | Finding 1 GO ACK — implementing | Sent 20260506T205141Z |
| RAVC3 | 2.0.0_SA_COO | Finding 1 fix 960c289a LIVE | Sent 20260506T205301Z |
| RAVC ACK | 2.0.0_SA_COO | Finding 1 confirmed LIVE; standby F2 | Rcvd 20260506T205345Z |
| RAVC ACK reply | 2.0.0_SA_COO | F1 RAVC closed; standby DS~A | Sent 20260506T205405Z |

Finding 1 RAVC CLOSED. Finding 2 pending DS~A.

---

## Current State

| Item | Status |
|------|--------|
| Finding 1 (Mix cash) | FIXED + LIVE — `960c289a` portal DEV |
| Finding 2 (NMNC/NMEC) | DS~A lane — standby |
| RD Mix verification | RUNNING |
| TS check | PASS |
| DE queue | Empty — standby for F2 DS~A result |
