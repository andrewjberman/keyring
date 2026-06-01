# MDPF_SCOPED P1 — FE Structure Inventory + Linkage-Matrix FE Rows (Model Portfolios page)

- **Author:** 0.4.2_RD_AdvisorIntelligence~B (RD leg, pod 4)
- **Date:** 2026-06-01
- **Trigger:** COO [DRIVE] dispatch 20260601T130151Z — MDPF_SCOPED P1, Andrew-direct FIRST priority: "be categorically sure all FE + BE are linked for the Model Portfolios page across all three firm segments (GLOBAL / 49 / INFLECTION)."
- **Companion (BE columns):** `docs/briefs/mdpf-fe-be-linkage-matrix-be-columns-20260601.md` (0.4.0_DE, CLOUD `31f3b09ed`)
- **Page source:** `portal/src/pages/ModelPortfolios.tsx` (1642 lines), DEV branch (Rule 19 verified: portal main tree on DEV)
- **Join key:** React Query `queryKey` (matches DE's BE columns exactly)

---

## 0. Firm-segment selector (the routing spine)

- **Control:** header dropdown, `ModelPortfolios.tsx:583-589` (`PageSurfaceControl as="dropdown"`).
- **State:** `selectedFirmId` (`:198`), default `'global'`.
- **Options:** `ALL_MDPF_PARTNER_FIRMS` (`:90-94`) — `global` ("Global (All)") / `49financial` ("49 Financial") / `inflection` ("Inflection Wealth Management").
- **Visibility:** rendered ONLY for `internal` users (`isInternal() || isDev()`, `:196-197`). External users never see the selector → always Global.
- **Routing mechanism:** two per-firm queries are `enabled: selectedFirmId !== 'global'` (`:206`, `:217`). When a firm is selected, panels that branch on `isPerFirm`/`selectedFirmId !== 'global'` re-scope to per-firm data; all other queries remain global-only.

---

## 1. FE Linkage Matrix — FE rows (join to DE BE cols by queryKey)

Legend: RE-SCOPES = panel switches data source on the firm selector; GLOBAL-ONLY = same data for all 3 segments.

| # | Panel / Component | Source line | queryKey (join key) | FE data field(s) consumed | Firm-selector routing | Segment fit |
|---|---|---|---|---|---|---|
| 1 | **AUA-by-Model donut** ("AUA by Model") | `:630-771` | `aum-metrics` (global) / `mdpf-per-firm-timeseries` (firm `.by_model`) | `portfoliosWithNonModel[].{modelName,currentAUM}` + center `totalAUM` | **RE-SCOPES** ✓ — `modelPortfolios` branches on `perFirmMdpfData.by_model` (`:316-324`); center `totalAUM` ← `partner_custody_total` (`:473-475`); Non-Model slice ← `perFirmMdpfData.non_model_aua` (`:550`) | GLOBAL / 49 / INF — all 3 ✓ |
| 2 | **Custom vertical legend** | `:773-817` | same as #1 | `modelPortfolios[].modelName` + Non-Model | **RE-SCOPES** ✓ (same `modelPortfolios`). *Minor:* the Non-Model legend item visibility (`:803`) is gated on global `nonModelData` presence even in firm view, while the donut Non-Model slice uses per-firm value — cosmetic inconsistency, not an empty-view. | all 3 ✓ |
| 3 | **AUA Growth Metrics** (`AUMGrowthMetrics`) | `:820-891` | `aum-metrics` / `mdpf-per-firm-timeseries` + `mdpf-per-firm-distribution` | total + Q0–Q3 `{change,growth,priorLevel}`, `account_count` | **RE-SCOPES** ✓ — `isPerFirm` branch (`:841-862`) derives growth from `partner_custody_total` at quarter-end dates; `account_count` ← `perFirmDistribution.total.account_count` | all 3 ✓ |
| 4 | **Account Distribution bell** ("Client Holdings") | `:902-995` | `account-distribution` / `mdpf-per-firm-distribution` | `activeDistribution.{total, by_model}` | **RE-SCOPES** ✓ — `activeDistribution = isPerFirm ? perFirmDistribution : distributionData` (`:569`) | all 3 ✓ |
| 5 | **AUA / Account Trend Analysis** (growth tab) — Bar + Area chart | `:1044-1490` | `aum-timeseries` / `mdpf-per-firm-timeseries` | `timeSeriesData.{aggregate, by_model}`; per-period `aum` (value) or `account_count` (count) | **RE-SCOPES (value mode)** ✓ — `timeSeriesData` branches on `perFirmMdpfData` (`:384-402`, `isPerFirm` flag). **Two sub-flags below (F4, F5).** | value ✓ / count ✗ (see F4) |
| 6 | **Benchmark Comparison** (`BenchmarkHeatmap`, performance tab) | `:1492-1601` | `model-portfolio-benchmarks` + `etf-benchmark-returns` | `benchmarkData`, `etfBenchmarkData`, `benchmarkType` (ETF default, F1), `benchmarkReturnType` | **GLOBAL-ONLY** — no firm param; gated only by `activeTab === 'performance'` (`:269,277`). **FLAG F1 below.** | model-level, firm-invariant (DE) |
| 7 | **Peers** (`PeersTab`, peers tab) | `:1605-1606` | `peer-performance` | `peerData` (passed as `data={peerData}`) | **GLOBAL-ONLY** — no firm param to `PeersTab`; gated only by `activeTab === 'peers'` (`:284`). **FLAG F1 below.** | model/peer-level, firm-invariant (DE) |
| 8 | **Data Source note** (bottom, always visible) | `:1611-1637` | — (uses `nonModelData` freshness only) | static text + `getLastActualDataDate(nonModelData.time_series)` | **NOT firm-aware** — static. **FLAG F2 below (hardcoded "49Financial:").** | n/a |

**BE-side corroboration (DE `31f3b09ed`):** every growth-tab panel (#1–5) has a real, VERIFIED-PRESENT S3 source for all 3 segments (published 2026-05-29 by DS~B); 49 & INF aggregate files are schema-identical (402 dates); per-firm account-distribution is a superset of global. **The D1 "empty firm view" reopen defect does NOT recur.** Query keys confirmed matching.

---

## 2. Gap flags (FE rows)

### F1 — Performance (Benchmark) + Peers tabs are NOT firm-gated  *(corroborated by DE — joint flag)*
Panels #6, #7 show global/model-level data for all 3 segments (gated only by `activeTab`, never by `selectedFirmId`). DE's rationale: a model's benchmark/return series is **firm-invariant by design** (the "Long Term" model returns the same regardless of which firm holds it), so this is *arguably correct* — but **the page gives the user no signal** that these tabs ignore the firm selector. A user who selects "Inflection" and clicks Benchmark/Peers sees global numbers with no indication they didn't re-scope.
- **Severity:** classification call, not a defect. **No DE fix pending** until adjudicated.
- **COO decision needed (Q):** (a) accept as-is, (b) add a "model-level — same across firms" label/badge on these two tabs under firm scope, or (c) hide/disable these tabs when a non-global firm is selected. RD can implement (b) or (c) on one portal DEV cycle.

### F2 — Data Source note hardcodes "49Financial:" label  *(FE defect — hardcoded-label class, matches Andrew's prior smoke family)*
`ModelPortfolios.tsx:1624` — the Non-Model explainer reads `<span ...>49Financial:</span> Non-Model AUA = ...`. This literal "49Financial:" renders **even when Inflection is selected**, mislabeling Inflection's footnote with the wrong firm name.
- **Severity:** low-medium (cosmetic but visibly wrong in the INF demo view). **FE fix, RD-owned:** make the label track `selectedFirmId` (resolve from `ALL_MDPF_PARTNER_FIRMS` name) or generalize to "Non-Model AUA = …" without a firm prefix. One-line.

### F4 — Count-mode trend renders all-zeros in firm (49/INF) views  *(needs adjudication — likely BE coverage gap)*
The trend chart's Count mode (`trendMetricType === 'count'`, `:1214`) reads `periodData.account_count` per model. In **global** mode this comes from `aum-timeseries.by_model[].account_count`. In **per-firm** mode, `timeSeriesData.by_model` is built from `perFirmMdpfData` carrying only `aum` / `model_value` (`:391-398`) — **there is no per-model `account_count` in the per-firm aggregate artifact** → every model resolves to `0`. So selecting 49 or Inflection and toggling Count shows an empty (all-zero) trend.
- **Severity:** medium (silent zeros, not an error). **Adjudication:** either (a) per-firm aggregate artifact should emit per-model `account_count` over time (BE — DE/DS), or (b) FE should hide/disable the Count toggle under firm scope. Flagging DE for source-coverage confirm.

### F5 — Per-firm "extra" models (49 SMA sleeves, INF blends) appear in donut but are dropped from the trend chart + trend legend  *(FE inconsistency)*
The donut (#1) renders `Object.values(by_model)` so it shows the data-driven per-firm model set (DE: 49 = 5 base + 2 SMA; INF = 5 base + 2 blends). But the **trend stacked chart** (`:1209`) and **trend legend** (`:524`, `renderTrendLegend`) iterate the fixed global `MODEL_ORDER` (5 canonical models) — so the 49 SMA sleeves / INF blends are silently absent from the trend bars/area + legend in firm view, even though their AUA exists in `perFirmMdpfData.by_model`.
- **Severity:** medium (the donut total and trend total still reconcile via Non-Model/aggregate, but the per-model decomposition differs between the two panels in firm view). **FE fix, RD-owned:** drive the trend model iteration from the active per-firm model key-set (same `Object.values` approach as the donut) instead of the fixed `MODEL_ORDER` when `isPerFirm`.

### Status of Andrew's prior portal-smoke findings (re-confirmed this pass)
- **"empty firm views"** → **RESOLVED** for growth-tab panels (#1–5): per-firm S3 files present + correct shape (DE-verified); D1 reopen defect does not recur.
- **"~34 hardcoded titles vs alias-map"** → model labels on this page now route through `getCanonicalModelName()` (MDPF S4 canonical naming adopted). **One residual hardcoded label found: F2 ("49Financial:")**. (Page-scoped finding; the broader ~34-component sweep is outside this page.)
- **"panels not dropdown-wired"** → growth-tab panels ARE wired (re-scope ✓). Performance + Peers are NOT wired by design (F1) but unsignaled.

---

## 3. Bottom line for COO

- **Growth tab (panels #1–5, value mode): FULLY LINKED across all 3 segments.** FE re-scopes, BE sources verified-present (DE). This is the demo-critical surface and it is categorically linked.
- **Open items requiring a call:** F1 (Performance/Peers not firm-gated — classification), F2 (hardcoded "49Financial:" label — RD one-line fix, no decision needed), F4 (Count-mode firm zeros — BE-vs-FE adjudication), F5 (per-firm extra-model trend dropout — RD fix).
- **RD can land F2 + F5 immediately on portal DEV** (FE-only, no decision); F1 awaits COO classification; F4 awaits DE source-coverage confirm.
