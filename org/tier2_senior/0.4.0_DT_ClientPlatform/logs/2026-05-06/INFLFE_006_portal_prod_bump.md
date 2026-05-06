# DT Session — ADVI_INFLFE.006 Distribution + Books Error Fix

**Author:** 0.4.0_DT_ClientPlatform (acting COO session)
**Date:** 2026-05-06
**Task Order:** ADVI_INFLFE.006 — Inflection frontend: Distribution + Books hard errors + AUA alignment verification

---

## Phase 0 — DS~A Data Verification

- DS~A INFLFE.006-data fix confirmed landed at 16:01Z.
- `partner_analytics_quarterly.json views.aua.donut.total = $199,649,186.31` ✓ (was $182,552,380.96)
- NMNC segment = $19.68M, NMEC = $7.49M, Existing = $172.48M ✓
- GO to Phase 1 issued (DS~A fix verified).

---

## Phase 1 — Root Cause Investigation

### Distribution Tab Hard Error (Root Cause B1)

**Error:** `TypeError: Cannot read properties of undefined (reading 'split')` in `formatSegLabel`

**Path:** User clicks Distribution tab → geo cohort renders with state donut (OK) → user clicks a state to drill down → `SnapshotDistributionView` segments memo maps `parent.cities` → `CitySegment` interface expects `key` field, but Inflection `partner_analytics_quarterly.json` geo donut segments emit `name` not `key` for city entries → `resolvedKey = undefined` → `formatSegLabel(seg, 'geo', true)` calls `seg.key.split('_')` on `undefined` → `TypeError` → React `ErrorBoundary` catches → "Unable to Load Distribution"

**Data evidence:**
```json
"cities": [{"name": "Everett", "aua": 37874692.21, "aua_pct": 22.07, "client_count": 46, "account_count": 146}, ...]
```
Missing: `key`, `label`, `color`, `distribution` fields. Expected: `{"key": "everett_wa", "label": "Everett", ...}`

**Bell curve missing:** `distribution.total` has no `histogram` field. `DistributionStats.histogram?.counts?.some(c > 0)` = false → bell curve panel shows fallback ("Select a state"). Not a crash — render-safe.

### Books Tab Hard Error (Root Cause B2)

**Error:** `TypeError: Cannot read properties of undefined (reading 'taxable')` at `clientsTabData.tax.taxable`

**Path:** `getPlatinumFirmDashboard('inf')` reads `dashboard.json` (split=true) → fetches `getClientsTab('inf')` → Lambda reads `platinum/firm/clients-tab-slim.json` → slim file has no `tax` field + uses `aua` instead of `total_aua` in headline → `dash.clients_tab?.headline` is truthy → `setClientsTabData({...})` sets state with partial data → render: `clientsTabData.tax.taxable` crashes on undefined → React `ErrorBoundary` catches → "Unable to Load Books"

**Data evidence (clients-tab-slim.json):**
```json
{"headline": {"aua": 182552380.96, "client_count": 307, "account_count": 822, "fee_earning_aua": 0.0}}
```
Missing: `tax`, `income_fees`, `portfolio`, `engagement` sections. Wrong field: `aua` instead of `total_aua`. The BD equivalent has all required fields with correct names.

---

## Phase 1 — Fixes Applied

### Fix B1: DistributionTab.tsx — City key/label fallback

File: `portal/src/pages/AdvisorIntelligence/_shared/tabs/DistributionTab.tsx`
Lines: ~2633-2636 → ~2633-2642

Change: City segment mapping now resolves `key` from `city.key ?? city.name ?? ''` and `label` from `city.label ?? city.name`. Prevents `formatSegLabel` from crashing when drilling into a state. City label displays correctly ("Everett", "Seattle", etc.) — title-case formatting still works.

### Fix B2: ClientsTab.tsx — total_aua fallback + tax null guard

File: `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx`
Lines: ~319-333 (setClientsTabData merging) + ~724-729 (CanonicalBookView tax prop)

Changes:
1. `total_aua` fallback: `dash.clients_tab.headline.total_aua ?? slim_aua_field ?? 0` — prevents $0 AUA in Books firm overview
2. `tax` null guard: `clientsTabData.tax ? {...} : null` — prevents TypeError when slim file omits tax section

**comp-transform schema-check:** PASS (NOTE only, no MISSING fields)
**TypeScript compile:** PASS (0 errors)

### Commit

Portal DEV commit: `43411a79`
Portal submodule bump (CLOUD): `f4dfe7149`

---

## 5-Vector AUA Agreement Check

| Vector | Observed Value | Status | Notes |
|--------|---------------|--------|-------|
| 1. Assets Overview main AUA | $199,649,186.31 | PASS | dashboard.json headline |
| 2. AUA toggle NMNC+NMEC+Existing | $19.68M + $7.49M + $172.48M = $199.65M | PASS | views.aua.donut.segments post DS~A fix |
| 3. Mix view (equity+fi+alt+cash) | $110.79M+$59.58M+$16.69M+$12.59M = $199.65M | PASS | mix_summary.json |
| 4. Distribution Segment Analytics | $199,134,271.19 | DELTA $515K | Geographic exclusion (no-state accounts); expected per UI footnote |
| 5. Books advisor sum (QTD) | $161.02M+$20.59M+$16.16M+$1.88M = $199.65M | PASS | leaderboard.json QTD window |

Vectors 1, 2, 3, 5 agree at $199.6M canonical. Vector 4 is $515K lower (geographic coverage exclusion = expected).

---

## Data Gaps Flagged to COO (NOT frontend bugs)

### DG-1: clients-tab-slim.json AUA still $182.5M

`clients-tab-slim.json` headline.aua = $182,552,380.96 even after DS~A INFLFE.006-data fix (generated_at: 16:01Z same run). The `_build_clients_tab_slim` function in INF_D_04 also uses `aum_snapshot` override but was NOT patched in the DS~A fix (which targeted only `_build_aua_view` + `_build_geo_view`). The Books firm overview headline shows wrong AUA until this is fixed. DT frontend fix fallbacks to this value; DS must apply same rep-coverage gate to `_build_clients_tab_slim`.

### DG-2: clients-tab-slim.json schema mismatch

Inflection slim file uses `headline.aua` (not `headline.total_aua`) and omits `tax`, `income_fees`, `portfolio`, `engagement` sections. BD slim file has correct schema. INF_D_04 writes a different slim schema for inflection than for BD. DS must align — specifically: write `total_aua` field and include `tax` section. DT fix deploys null guards + field fallback as immediate stopgap.

### DG-3: geo city segments missing `key` field

Inflection `partner_analytics_quarterly.json` geo donut city segments have `name` field only — missing `key`, `label`, `color`, `distribution`. BD emits full `CitySegment` schema. INF_D_04 `_build_geo_view` city emission logic does not match the expected frontend type. DS must align the city schema. DT fix resolves crash with name-as-key fallback.

### DG-4: No histogram in distribution.total

`partner_analytics_quarterly.json views.geo.distribution.total` has only `{count, sum, mean, p25, p50, p75, min, max}` — no `histogram` field. Bell curve cannot render. DS must add histogram computation to inflection `_build_geo_view`. This is a future enhancement, not a crash.

### DG-5: Distribution geo total ($199.1M) vs canonical ($199.6M)

$514,915.12 delta = accounts with no registered state/city excluded from geo AUA. This is expected behavior per the UI footnote ("Accounts with no registered location are excluded from geographic distributions"). NOT a bug.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-transform schema-check DistributionTab | NOTE only (runtime aliases) — PASS |
| comp-transform schema-check ClientsTab | NOTE only (runtime aliases) — PASS |
| TypeScript tsc --noEmit | 0 errors — PASS |
| comp-routes behaviors | Confirmed `/api/scoped/advisor-intelligence/clients-tab` → APIGateway-portal (Lambda reads platinum/firm/clients-tab-slim.json) |

---

## RAVC to COO

**Root cause:** Two independent hard errors:
1. Distribution: city segments emit `name` not `key` → drilldown crash in `formatSegLabel`
2. Books: `clients-tab-slim.json` missing `tax` field → crash on `clientsTabData.tax.taxable`

**Fixes applied:** Portal commit `43411a79` (both guards). Submodule bump `f4dfe7149`.

**5 AUA vectors post-fix:**
- Assets Overview: $199,649,186.31 ✓
- AUA toggle: NMNC=$19.68M + NMEC=$7.49M + Existing=$172.48M = $199.65M ✓
- Mix view: $199.65M ✓
- Distribution geo: $199.13M (⚠ $515K geographic exclusion — expected behavior)
- Books advisors: $199.65M ✓

**Remaining data gaps flagged (not frontend bugs):** DG-1 through DG-5 above. Highest priority: DG-1 (clients-tab-slim AUA still $182.5M needs same rep-coverage gate as `_build_aua_view`); DG-2 (slim file schema); DG-3 (city `key` field missing).

**RD Playwright sweep:** COO to coordinate INFLFE.006-rd TO now that DT Phase 1 is closed.
