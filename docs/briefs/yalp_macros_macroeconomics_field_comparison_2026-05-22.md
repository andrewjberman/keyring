# YALP_MACROS — Macroeconomics Field-Level Comparison (T* = 2026-05-22)

**TO:** YALP_MACROS.001 (Level-1 endpoint + field mapping) — TO-004 will populate Level-2.
**Author:** 0.1.0_DS_MarketIntelligence~A (tilde-lane for Macroeconomics probe; same actor as YALP_MKTOVR + YALP_MDSRC D2/D3 lead).
**PRD:** `docs/architecture/YALP_MACROS.md` v0.2 amendment `~17:05Z` (1.0.0_SA_CTO SELF-CORRECTION-UPSTREAM per DS 0.1.0~A pre-scaffold structural finding — VolatilityTab added as 4th component Option (A) Include; v0.1 origin commit `ff1defa6c`); lane-correction `02519793e` confirms ~A stays DS 0.1.0 (Andrew direct).
**TO:** `org/tier2_senior/0.1.0_DS_MarketIntelligence~A/task_orders/YALP_MACROS.001.macroeconomics-l1-endpoint-field-mapping.md` — ws COO GO dispatched `20260526T~17:05Z` (/drive #101).
**Methodology template:** `docs/architecture/YALP_MKTOVR.md` v0.4 + `docs/briefs/yalp_mktovr_market_overview_field_comparison_2026-05-22.md` (576-line precedent; 8/8 ACs; 0 DRIFT; project CLOSED 2026-05-26 ~15:28Z).
**Predecessor ground truth:** `docs/reference/yang-pipeline-lineage-map.md` (YALP_MDSRC L1 §6.4 + §6.5 + §6.6 — atomic field-grain for `macro_data.json` + `vix_data.json` + `timeseries/{slug}.json`; §2a — `volatility_data.json` canonical attribution to `opal-portal-volatility-fetcher`).
**Status:** Level-1 COMPLETE for 4-component scope per PRD v0.2 + TO-001 GO. STANDBY-PREP scaffold + execute compressed to single ship per [[standby-prep-compress-to-delivery-when-context-sufficient]] (ws COO ACCEPT `20260526T~16:59Z` + scaffold-execute-compression accepted in TO-001 GO MCP `~17:05Z`). Level-2 placeholder empty per AC4 (TO-004 scope). T* = **2026-05-22** (Friday) — yang-side binding inherited from YALP_MKTOVR.

---

## §0 — TL;DR

Macroeconomics portal page mapped at Level-1 across **4 components** per PRD v0.2 (4th component VolatilityTab added via [[self-correction-upstream-of-verify-channel]] amendment from DS 0.1.0~A pre-scaffold structural finding `~17:00Z`; CTO Option (A) Include ruling absorbed `~17:05Z`):

- **YieldCurveTab** + **MacroHeatmap** + **MacroTimeSeriesModal** — yang-pipeline-fed (canonical Macroeconomics yang surface)
- **VolatilityTab** — market-overview-pipeline-fed via `opal-portal-volatility-fetcher` Lambda → `json/macro/volatility_data.json` (VIX from FRED `VIXCLS`, MOVE from Yahoo Finance)

**Endpoint surface consolidates to 4 distinct portal endpoints** + 1 FRED-historical augment (`yield_curve_fred.json` for YieldCurveTab 1Y-ago overlay) served by **2 yang-pipeline Lambdas** (`yang-generate-macro` + `yang-generate-macro-timeseries`) + **1 market-overview-pipeline Lambda** (`opal-portal-volatility-fetcher`) + **1 FRED-ingestion Lambda** (`fred-data-ingestion` parallel to yang). YCharts equivalents at endpoint-class resolved for all 4 components — UST yields + 84 BBG macro indicators + per-indicator timeseries + VIX/MOVE volatility indices; deep per-tenor + per-indicator value cross-reference is TO-004 scope (full L2 per PRD §5 Q2 lean given bounded universe). Per YALP_MKTOVR Fear & Greed precedent + Option (A) ruling, VolatilityTab Level-1-enumerated for page-completeness with Level-2 verdicts conditional on YCharts ^VIX/^MOVE coverage at TO-002.

---

## §1 — Methodology + scope reconciliation

### §1.1 — Level-1 column shape (per PRD methodology mirror)

For each rendered field on each substantive component:

| Col | Meaning |
|---|---|
| Field | Component-rendered field name (TypeScript prop or JSON path) |
| Portal endpoint | CloudFront URL the portal fetches |
| S3 key | `opal-data-portal-v2` key the endpoint resolves to |
| Yang-pipeline producer | Lambda writing the S3 key |
| Intermediate | DynamoDB / cache / FRED layer (if any) |
| Yang-PKL field | Atomic field-grain from L1 lineage map §6.4 / §6.5 / §6.6 |
| YCharts endpoint | The functional YCharts API endpoint that would serve equivalent data |
| YCharts field | The specific YCharts field name |

`n/a — <reason>` populates YCharts columns when the source is out-of-cutover-scope (e.g., orphaned exports). Per YALP_MKTOVR precedent + Andrew per-page charter framing, the scope is "for each Portal UI page" (full rendered page surface), not "yang-pipeline-fed only" — see §1.2 disposition.

### §1.2 — Scope reconciliation: VolatilityTab (4th component) — **RESOLVED via PRD v0.2 Option (A) Include**

**Pre-scaffold empirical finding `~16:34Z`:** `portal/src/pages/Macroeconomics/Macroeconomics.tsx:42-49` renders a `<VolatilityTab>` (VIX + MOVE) inside the `'vix'` tab branch. Active page consumer via `getVolatilityData()` (`portal/src/api/portal-proxy.ts:1666` → `/api/general/macro/volatility_data.json`). PRD v0.1 §1 listed only 3 components — silently omitted VolatilityTab.

**Upstream-pipeline classification (L1 §2a authoritative):**

| S3 key | Producer Lambda | Upstream pipeline | Active portal consumer |
|---|---|---|---|
| `json/macro/macro_data.json` | `yang-generate-macro` | **yang-pipeline** | YieldCurveTab + MacroHeatmap |
| `json/macro/timeseries/{slug}.json` | `yang-generate-macro-timeseries` | **yang-pipeline** | MacroTimeSeriesModal |
| `json/macro/volatility_data.json` | **`opal-portal-volatility-fetcher`** | **market-overview pipeline (NOT yang)** | **VolatilityTab** (VIX FRED + MOVE Yahoo Finance) |
| `json/macro/vix_data.json` | `yang-generate-macro` | yang-pipeline | NO ACTIVE CONSUMER (orphan; PRD §1 correctly identifies) |
| `json/yang/volatility_data.json` | `yang-generate-volatility` | yang-pipeline | NO ACTIVE CONSUMER (orphan; L1 §2a — distinct from canonical key above) |

L1 lineage map §2a explicit: "Canonical volatility data is from opal-portal-volatility-fetcher (has MOVE data via Yahoo)."

**ws CTO disposition `~17:05Z` = Option (A) Include** — PRD v0.2 self-correction-upstream amendment (4th-fire today; sister to DS 0.2.0 DDB-intermediate + DE 0.4 useTenantLayout + DS 0.1.0~C scribe-consistency). Lean (A) accepted per YALP_MKTOVR Fear & Greed precedent (n/a-YCharts surfaces enumerated at Level-1 for page-completeness; Level-2 conditional on YCharts coverage at TO-002). VolatilityTab Level-1 mapping canonical in §6 below.

**Pattern banked:** [[self-correction-upstream-of-verify-channel]] worker-side variant — empirical-read-of-consumer-side at scaffold-phase surfaces PRD scope-omissions PRE-EXECUTION enabling PRD precision-amend rather than REPAIR-AMENDMENT route. Sister to CTO-side self-correction; this is the DS-worker-side analog. Banking candidate per session log §9.

### §1.3 — Architectural structure: single-layer yang→S3 (no DDB intermediate for macro)

Unlike YALP_MKTOVR's Market Overview branch (which has the DDB-intermediated `opal-portal-market-data` layer between yang-ingest and the `market-overview-tiered-generator`), the Macroeconomics yang-pipeline-fed surface is **direct yang→S3** with no intermediate layer:

```
yang-pipeline producer:    yang-generate-macro (reads data.pkl, writes json/macro/*.json)
                           yang-generate-macro-timeseries (reads data.pkl, writes json/macro/timeseries/*.json)
                           ↓
portal endpoint:           /api/general/macro/{macro_data,timeseries/{slug}}.json
```

No DDB-intermediate flag for any of YieldCurveTab/MacroHeatmap/MacroTimeSeriesModal. Confirmed by:
- L1 lineage map §1a (write-side ground truth) — both Lambdas listed with direct S3 output keys; no DDB sidecar
- `getMacroData()` source `portal/src/api/portal-proxy.ts:1580` — direct CF→S3 fetch; no DDB hop
- `getMacroTimeSeries()` source `portal/src/api/endpoints/macro.ts:26-28` — direct CF→S3 fetch

**Special case — YieldCurveTab 1Y-ago FRED augment:** `getYieldCurveData()` (`portal/src/api/endpoints/yield-curve.ts:46-48`) fetches `/api/general/macro/yield_curve_fred.json` for historical 1Y-ago tenor values used in the 3-curve overlay (current + 1M ago from yang `macro_data.json`; 1Y ago from FRED). This is a **separate FRED ingest** (`portal/etl/orchestration/green/fred/lambda/fred-data-ingestion/ingest_yield_curve_fred.py` per source comment); it's a parallel data source to yang, NOT an intermediate on top of yang. Treated as a sister-endpoint within the YieldCurveTab Level-1 mapping (§3).

**VolatilityTab (if Option A confirmed):** market-overview-pipeline-mediated (single-layer market-overview→S3); architecturally distinct from yang surfaces but parallel in shape. Detailed in §6.

### §1.4 — T* shared-date — 2026-05-22

Inheriting from YALP_MKTOVR TO-003 consult (0.2.0_DS_PortfolioAnalytics `8d1d6fcad`): yang-side `data_pkl` `data_as_of = 2026-05-22`. Empirically verified across 7 yang-side artifacts (incl. `macro_data.json` per L1 §6.4 `data_as_of` field — same upstream `data.pkl`). Calendar windowing identical: 2026-05-23/24 weekend; 2026-05-25 Memorial Day; 2026-05-26 EOD not yet published. → **2026-05-22 is the unique current-window T*** for the probe.

DS 0.2.0_DS_PortfolioAnalytics ~A consult-only on YALP_MACROS.003 (per /allocation #10 deliverable) likely re-confirms T*=2026-05-22 specifically for `macro_data.json` (same `data.pkl` source). Holding pending confirmation; substantive carry-forward applies.

YCharts coverage on 2026-05-22 — Friday EOD; menachem-bundled cookie last successfully pulled D2/D3 2026-05-22 (71/71 entities); macro indicators per D2 coverage scan = well-covered in YCharts FRED-proxy endpoints per YALP_MDSRC D2 baseline. Cookie-stale-OK per PRD §4 + ws COO direct: use YALP_MKTOVR TO-002 `dcbc50710` baseline + existing corpus; fresh pulls deferred to TO-002 execution phase only if needed for delta confirmation.

### §1.5 — Macro indicator depth — full L2 (per PRD §5 Q2 lean)

PRD §5 Q2 leans `full L2` (bounded universe) for MacroHeatmap. L1 §6.4 ground truth: **12 groups × 84 Bloomberg macro series** (NOT 73/10 as the `MacroHeatmap.tsx:1` comment suggests — comment is stale; L1 is authoritative).

12 groups:
- Leading Indicator (8)
- Lagging Indicator (7)
- Financial Condition (6)
- Inflation (8)
- Labor Market (9)
- Consumer (7)
- Housing Market (7)
- Investor Sentiment (7)
- Treasury Yields (10) — feeds YieldCurveTab
- Credit Spread (5)
- Market Indicator (2 — VIX/MOVE) — embedded in macro_data.json (Treasury Yields are read by both YieldCurveTab and MacroHeatmap; VIX/MOVE Market Indicators are read ONLY by MacroHeatmap from this key, vs `volatility_data.json` separate ingest for VolatilityTab)
- Currency (5)

**Cross-component embedding observation:** Treasury Yields group (10 indicators, `1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y`) is consumed by BOTH MacroHeatmap (as macro group) AND YieldCurveTab (filtered for the 10-tenor curve construction; per `YieldCurveTab.tsx:185` `treasuryGroup = macroData.groups.find(g => g.category === 'Treasury Yields')`). Level-2 verdict for Treasury Yields applies to both component contexts.

**VIX/MOVE Market Indicator embedding:** `macro_data.json` contains VIX + MOVE as part of the "Market Indicator (2)" group (per L1 §6.4 group enumeration). These are consumed by MacroHeatmap directly. SEPARATELY, VolatilityTab reads `volatility_data.json` (different S3 key, different pipeline, different field structure). **TO-004 verification observation:** cross-check VIX values appear consistently between `macro_data.json` Market Indicator and `volatility_data.json` (Macro VIX value should match Volatility VIX `current.current` on T*=2026-05-22) — independent integrity gate.

### §1.6 — Tier-2 expansion + Tier-3 timeseries sampling

For MacroHeatmap full-L2: per-group enumeration (12 groups × 84 indicators) = 84 row-level verdicts at Level-2; each row checks (a) yang value vs YCharts FRED-proxy value on T* and (b) yang percentile vs YCharts-computed percentile (if attempted).

For MacroTimeSeriesModal Tier-3 sampling (per L1 §6.6: 79 timeseries files):
- 5 most-clicked indicators (per PRD §6 risk row) — TBD via product analytics OR sample top-5 by group-leading-indicator convention (e.g., CPI, Core CPI, UNRATE, GDP, M2)
- 2 from clean-MATCH set (D2 baseline anchors)
- 2 from coverage-uncertain set (specialty/proprietary BBG series likely GAP)
- 1 random per top-4 groups (Leading/Inflation/Labor/Consumer)

= **~10-12 indicator timeseries × 1 endpoint = 10-12 Tier-3 pulls** at TO-002 (cookie-stale-OK; use existing corpus where possible).

For YieldCurveTab: full 10 tenor pulls (UST 1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y) — bounded universe, no sampling needed.

For FRED 1Y-ago augment: 10 tenor × `/api/general/macro/yield_curve_fred.json` returns full historical per tenor; single endpoint pull yields all 10.

For VolatilityTab (if Option A): 2 indices (VIX + MOVE) × current + historical = 2 endpoint surfaces; small bounded universe.

Concrete TO-002 endpoint pull plan in §7.

---

## §2 — Endpoint surface map

All Macroeconomics portal fetches go through `portal/src/api/portal-proxy.ts` + `portal/src/api/endpoints/macro.ts` + `portal/src/api/endpoints/yield-curve.ts`. CloudFront serves via `/api/general/*` → behavior `/api/general/macro/*` (per `endpoint-mapping.ts:53-62`).

| Endpoint fn | Tier | Path | S3 key | Producer Lambda | Consumed by |
|---|---|---|---|---|---|
| `getMacroData` | T1 | `/api/general/macro/macro_data.json` | `json/macro/macro_data.json` | `yang-generate-macro` | YieldCurveTab + MacroHeatmap |
| `getMacroTimeSeries(slug)` | T1 | `/api/general/macro/timeseries/{slug}.json` | `json/macro/timeseries/{slug}.json` | `yang-generate-macro-timeseries` | MacroTimeSeriesModal |
| `getYieldCurveData` | T1 | `/api/general/macro/yield_curve_fred.json` | `json/macro/yield_curve_fred.json` | `fred-data-ingestion` (separate; via `ingest_yield_curve_fred.py`) | YieldCurveTab (1Y-ago augment only) |
| `getVolatilityData` | T1 | `/api/general/macro/volatility_data.json` | `json/macro/volatility_data.json` | `opal-portal-volatility-fetcher` (market-overview pipeline) | VolatilityTab (§6 conditional) |

**4 endpoints total** (3 yang-fed + 1 non-yang). No Tier-2 fan-out for macro surfaces. Tier-3 per-slug timeseries is dynamic-key (slug-resolved client-side via `slugify()` per L1 §6.6).

Orphans for completeness (no consumer, no Level-2 verdict):
- `/api/general/macro/vix_data.json` → `json/macro/vix_data.json` (yang-generate-macro side; per L1 §5a)
- (no CF route) → `json/yang/volatility_data.json` (yang-generate-volatility side; per L1 §5a)

---

## §3 — Component 1: YieldCurveTab

**File:** `portal/src/pages/Macroeconomics/tabs/YieldCurveTab.tsx`. Renders 3-curve overlay (Current + 1M Ago + 1Y Ago) of UST yield curve across 10 tenors (1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y) + bottom bar chart of 1M yield changes + 5 stat cards (2Y/10Y/30Y yields + 2s10s spread + curve shape).

### §3.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Producer | Intermediate | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|
| Current tenor yields (10 tenors; `data[].current`) | `/api/general/macro/macro_data.json` | `json/macro/macro_data.json` | `yang-generate-macro` | none | `data.pkl` → `price_monthly` Treasury Yields group → per-tenor `groups[i:Treasury Yields].indicators[name=<tenor>].values[currentMonth].value` | `/v3/companies/I:US{1M\|3M\|1Y\|2Y\|3Y\|5Y\|7Y\|10Y\|20Y\|30Y}YLD/prices` (per-tenor direct) OR FRED-proxy `/v3/series/DGS{1MO\|3MO\|1\|2\|3\|5\|7\|10\|20\|30}/values` | `last_yield` (or last-observation value) on T*=2026-05-22 EOD |
| 1-Month-Ago tenor yields (`data[].oneMonthAgo`) | same | same | same | none | `data.pkl` → Treasury Yields group → `groups[i].indicators[name=<tenor>].values[oneMonthAgoMonth].value` (per `YieldCurveTab.tsx:224-231` index math) | same per-tenor YCharts endpoint as above, queried at 2026-04-22 (1M lookback) | `last_yield` on 2026-04-22 |
| 1-Year-Ago tenor yields (`data[].oneYearAgo`) | `/api/general/macro/yield_curve_fred.json` | `json/macro/yield_curve_fred.json` | **`fred-data-ingestion`** (parallel to yang; `portal/etl/orchestration/green/fred/lambda/fred-data-ingestion/`) | FRED API direct | FRED `DGS{1MO\|3MO\|1\|2\|3\|5\|7\|10\|20\|30}` historical observations | same per-tenor YCharts endpoint, queried at 2025-05-22 (1Y lookback) | `last_yield` on 2025-05-22 |
| `tenorYears` (x-axis position) | (derived client-side) | n/a | n/a | n/a | derived: `TENOR_TO_YEARS[tenor]` map per `YieldCurveTab.tsx:97-109` | n/a | n/a |
| `spread2s10s` (10Y − 2Y) | (derived client-side) | n/a | n/a | n/a | derived from `data[i:10Y].current - data[i:2Y].current` | derived from 10Y − 2Y endpoint queries | derived |
| `curveShape` ('Inverted' / 'Flat' / 'Normal') | (derived client-side) | n/a | n/a | n/a | derived from `spread2s10s` thresholds (< -0.1 / -0.1 to 0.1 / > 0.1) | n/a | derived |
| 1M-change bar values (`(current - oneMonthAgo) * 100` bps) | (derived client-side) | n/a | n/a | n/a | derived | derived | derived |

### §3.2 — Methodology evidence

- Direct source read `portal/src/pages/Macroeconomics/tabs/YieldCurveTab.tsx:177-244` (data assembly logic; explicit two-source merge)
- Direct source read `portal/src/api/endpoints/yield-curve.ts:46-48` (FRED endpoint path)
- L1 lineage map §6.4 (Treasury Yields group atomic field-grain; 10 tenors enumerated)
- L1 lineage map §5a (orphan/canonical resolution) — no DDB intermediate for `yang-generate-macro`
- YALP_MDSRC D2 coverage — UST yields are well-covered in YCharts (per D2 ticker-level evidence; Treasury Yields are a clean-MATCH set candidate)

### §3.3 — Methodology notes + open observations

- **Date-window subtlety:** YieldCurveTab uses `data_as_of` month to determine `currentMonth` rather than rolling-window scan (per `YieldCurveTab.tsx:192-203` explicit anti-bug comment about "rolling-window bug where scanning backwards always finds December"). At T*=2026-05-22, `currentMonthIdx = May (4)`, `oneMonthAgoIdx = Apr (3)`. **TO-004 implication:** YCharts queries for 1M-ago must use 2026-04-22 (not "1 month before 2026-05-26 today"), to match yang's month-resolution semantics.
- **FRED proxy is approximate-match:** `yield_curve_fred.json` per FRED key matches with ±7-day tolerance window (`YieldCurveTab.tsx:82`). TO-004 verdict for 1Y-ago tenors should classify as **REPRESENTATIVE** (within ±7d) unless exact-date match achieved.
- **Bloomberg-vs-FRED 1M/3M short-end:** Bloomberg Treasury yields use Constant Maturity Treasury (CMT) curve construction; FRED DGS1MO/DGS3MO are direct CMT publishers. High prior on MATCH at the 10-tenor level. Will verify in TO-004.

---

## §4 — Component 2: MacroHeatmap

**File:** `portal/src/pages/Macroeconomics/panels/MacroHeatmap.tsx`. Renders 12-group × 84-indicator trailing-12-month value/percentile grid with click-to-modal drilldown (Value mode + Position mode toggle). Value mode shows month-by-month values with percentile-color background; Position mode shows latest %-ile + value + percentile-threshold columns (p10/p25/p50/p75/p90).

### §4.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Producer | Intermediate | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|
| 12 group categories (`groups[].category`) | `/api/general/macro/macro_data.json` | `json/macro/macro_data.json` | `yang-generate-macro` | none | `data.pkl` MACRO_GROUPS rubric (dc_macro): Leading/Lagging/Financial Condition/Inflation/Labor Market/Consumer/Housing Market/Investor Sentiment/Treasury Yields/Credit Spread/Market Indicator/Currency | n/a (grouping is yang-side) | n/a |
| 84 macro indicator names (`groups[i].indicators[j].name`) | same | same | same | none | `data.pkl` MACRO_GROUPS rubric per-indicator name | n/a (display name) | n/a |
| 84 Bloomberg tickers (`groups[i].indicators[j].bbg_ticker`) | same | same | same | none | MACRO_GROUPS per-indicator BBG ticker | (used as YCharts lookup key) | (FRED-proxy alias if YCharts ticker not direct) |
| Indicator units (`groups[i].indicators[j].unit`) — %, K, M, B, bps, hrs, or empty | same | same | same | none | rubric per-indicator unit field | n/a (yang-side derived) | n/a (FRED publishes unit-bearing series; alignment is structural) |
| 12-month trailing values (`groups[i].indicators[j].values[Jan..Dec].value`) | same | same | same | none | `data.pkl` → `price_monthly` last 12 months from `data_as_of` (T* = 2026-05-22 = May 2026 → Jun 2025 through May 2026 inclusive) | per-indicator FRED-proxy endpoint OR direct YCharts (per BBG ticker mapping table TBD in TO-002 — see §7) | per-indicator monthly observation value × 12 months |
| Percentile values (`groups[i].indicators[j].values[Jan..Dec].percentile`) — 1-100 min-max | same | same | same | none | yang-side min-max normalized rank over full history (per L1 §6.4) | derived: query full history from YCharts/FRED → compute min-max rank for current value | derived |
| Threshold values (`groups[i].indicators[j].thresholds.{p10,p25,p50,p75,p90}`) | same | same | same | none | yang-side historical percentile thresholds | derived: query full history → compute p10/p25/p50/p75/p90 | derived |
| Trailing-12-month column order (`getTrailing12Months()`) — derived client-side | (no fetch) | n/a | n/a | n/a | client-side: `new Date()` rolling | n/a | n/a |
| Position mode "Latest %-ile" (`latestData.percentile`) — derived from values walk | (no fetch) | n/a | n/a | n/a | client-side: per `MacroHeatmap.tsx:567-577` newest-nonNull walk | n/a | n/a |
| Position mode "Latest Value" + "Date" | same logic as above | n/a | n/a | n/a | client-side derive | n/a | n/a |

### §4.2 — Methodology evidence

- Direct source read `portal/src/pages/Macroeconomics/panels/MacroHeatmap.tsx:58-90` (data fetch + state) + `MacroHeatmap.tsx:177-365` (rendering shape) + `MacroHeatmap.tsx:567-577` (Position mode latest-data walk)
- Direct source read `portal/src/pages/Macroeconomics/types.ts` (MacroDataResponse / MacroGroup / MacroIndicator / MacroMonthlyValue / MacroPercentileThresholds — exact shape contract)
- L1 lineage map §6.4 (84-series enumeration; 12 groups; monthly-value cadence; min-max percentile method)
- L1 lineage map §1a (write-side ground truth — `yang-generate-macro` direct yang→S3)

### §4.3 — Methodology notes + open observations

- **Group/count discrepancy with code comment:** `MacroHeatmap.tsx:1-4` comment says "73 macroeconomic indicators in 10 expandable groups" — STALE. L1 §6.4 ground truth = **12 × 84**. Brief uses L1 ground truth; flagging code comment as cosmetic-cleanup candidate for DE 0.1.0 pod follow-on (NOT MY LANE TO DISPATCH).
- **Unit-format discipline:** `formatValueWithUnit()` from `utils/percentileColor.ts` formats display per `unit` field (%, K, M, B, bps, hrs). TO-004 value-comparison should compare RAW values not formatted strings (e.g., CPI YoY value `0.024` not `2.4%`). YCharts pulls return raw; yang stores raw with separate unit; comparison axis is raw-vs-raw.
- **Percentile method asymmetry:** yang-side uses **min-max normalization (1-100)** per L1 §6.4 — sensitive to history-window extremes. YCharts/FRED queries can compute **rank-based percentile** (more standard) OR min-max if matching yang's method. TO-004 verdict for percentile-class rows should classify as **REPRESENTATIVE** (method-variance) unless yang-rebuild on YCharts-data confirms min-max match.
- **Trailing 12-month rolling window vs `data_as_of`:** `getTrailing12Months()` (client-side, `MacroHeatmap.tsx:36-54`) uses `new Date()` (today's wall clock) to derive the column order. `data_as_of` is 2026-05-22. At test time today (2026-05-26), the rolling window includes Jun 2025 through May 2026 with current month = May 2026. Yang's `values[month]` is keyed by month-abbreviation only (no year). Column-rendering subtly assumes the most recent month in the window matches `data_as_of` month. TO-004 verdict should validate this alignment holds on T*=2026-05-22 boundary.
- **VIX/MOVE Market Indicator group embedded:** `groups[Market Indicator]` contains VIX + MOVE values from `data.pkl` — separate ingest path from VolatilityTab's `volatility_data.json` (which is market-overview-pipeline-fed). **Independent integrity gate:** TO-004 should cross-check VIX/MOVE values appear consistently between `macro_data.json.groups[Market Indicator]` and `volatility_data.json` on T*=2026-05-22.

---

## §5 — Component 3: MacroTimeSeriesModal

**File:** `portal/src/pages/Macroeconomics/components/MacroTimeSeriesModal.tsx`. Opens on indicator-click from MacroHeatmap; renders per-indicator historical timeseries chart with percentile bands + summary stats (current value + percentile + as-of date + vs-median). Time-window dropdown (1Y / 5Y / 10Y / Max). Display-mode toggle (Value / Percentile).

### §5.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Producer | Intermediate | Yang-PKL field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|
| Full historical timeseries (`time_series[].{date,value,percentile}` OR simple-format `data[].{date,value}`) | `/api/general/macro/timeseries/{slug}.json` | `json/macro/timeseries/{slug}.json` (gzip-compressed; 79 files per L1 §6.6) | `yang-generate-macro-timeseries` | none | `data.pkl` → `price_monthly` full history (per indicator series) | per-indicator FRED-proxy endpoint OR direct YCharts (per BBG ticker mapping per §7) | full historical observation series |
| Slug resolution (`slugify(indicator.name)`) | (client-side derive) | n/a | n/a | n/a | client-side: lowercase + `&`→`and`, `%`→`pct`, `/`→`_`, `-`→`_`, ` `→`_`, strip non-alphanum/_, collapse `_`, strip leading/trailing `_` | n/a | n/a |
| `current.value` + `current.percentile` + `current.date` + `current.vs_median` | same endpoint | same | same | none | yang-side derived from full history; `current.value` = last observation; `current.percentile` = min-max rank; `current.date` = last observation date; `current.vs_median` = value − p50 threshold | derived: query full history → compute current value + rank + last-observation-date | derived |
| `thresholds.{p10,p25,p50,p75,p90}` | same | same | same | none | yang-side full-history percentile thresholds | derived: query full history → compute percentile thresholds | derived |
| `date_range.{start,end,count}` | same | same | same | none | yang-side: first observation date / last observation date / total count | derived: query full history → first/last/count | derived |
| `stats.{min,max,mean,latest,count}` (simple-format only) | same | same | same | none | yang-side derived statistics | derived | derived |
| Filtered-by-window timeseries (1Y/5Y/10Y/Max) | (client-side filter via `useMemo`) | n/a | n/a | n/a | client-side filter from full series | n/a | n/a |
| `currentPercentile` + `vsMedian` + `filteredThresholds` (window-recomputed) | (client-side derive via `useMemo`) | n/a | n/a | n/a | client-side recompute per current window | n/a | n/a |

### §5.2 — Methodology evidence

- Direct source read `portal/src/pages/Macroeconomics/components/MacroTimeSeriesModal.tsx:42-78` (type definitions) + `MacroTimeSeriesModal.tsx:227-310` (data fetch + two-format unify) + `MacroTimeSeriesModal.tsx:186-198` (slugify rule)
- Direct source read `portal/src/api/endpoints/macro.ts:26-28` (endpoint path)
- L1 lineage map §6.6 (atomic field-grain — 79 indicator series, slug rule, gzip encoding, full schema)

### §5.3 — Methodology notes + open observations

- **Two-format handling:** S3 stores either "full format" (`{ time_series, thresholds, current, ... }`) OR "simple format" (`{ indicator, as_of, data }`). Client transforms simple-format on the fly (`MacroTimeSeriesModal.tsx:243-296`). L1 §6.6 documents the simple-format schema; per-slug check at TO-002 may surface which format each file uses. Both shapes carry the same underlying yang-side data; verification axis is unchanged (data values).
- **79-files-vs-84-indicators discrepancy:** L1 §6.6 says 79 timeseries files (64 original + 15 added by YALP_MDSRC.F3); L1 §6.4 says 84 indicators in `macro_data.json`. **5-indicator gap** — 5 indicators in MacroHeatmap have NO drilldown timeseries (clicking them likely produces a "data not available" modal). Surfaced as a follow-on R&D candidate: enumerate the 5-indicator gap + recommend backfill OR explicit no-drilldown disable in UI. Out-of-YALP_MACROS-scope per probe boundary; flag-only.
- **Tier-3 sampling for TO-002:** 10-12 sample indicators × 1 endpoint each = 10-12 Tier-3 pulls; selected per §1.6 rubric. Concrete sample plan in §7.
- **Slug-resolution risk:** client-side `slugify()` must match yang-side file-naming exactly. Mismatched slugs result in 404 modal. TO-002 sample list should verify at least 5 slug-resolution successes.

---

## §6 — Component 4: VolatilityTab (per PRD v0.2 Option A Include)

**File:** `portal/src/pages/Macroeconomics/tabs/VolatilityTab.tsx`. Renders VIX (top) + MOVE (bottom) volatility indices with toggle, speedometer/gauge, AI summary panel, historical chart with percentile bands. VIX uses asymmetric log-compression on y-axis above threshold (per `VolatilityTab.tsx:497-522`).

VIX uses asymmetric log-compression on y-axis above threshold (per `VolatilityTab.tsx:497-522`). Per PRD v0.2 ruling + YALP_MKTOVR Fear & Greed precedent, Level-1 enumerated unconditionally; Level-2 verdicts conditional on YCharts ^VIX/^MOVE coverage at TO-002 (lean: ^VIX direct OR FRED `VIXCLS` proxy = clean coverage; ^MOVE direct coverage TBD).

### §6.1 — Level-1 mapping

| Field | Portal endpoint | S3 key | Producer | Intermediate | Source field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|---|
| VIX current value (`data.vix.current.{current,regime,percentile,change1D,change1W,change1M}`) | `/api/general/macro/volatility_data.json` | `json/macro/volatility_data.json` | **`opal-portal-volatility-fetcher`** (market-overview pipeline; `infra/aws/lambda/v2_portal/07_macroeconomics/lambdas/opal-portal-volatility-fetcher/`) | external FRED (per `VolatilityTab.tsx:692` `'Source: Federal Reserve Economic Data (FRED).'`) | FRED `VIXCLS` series last observation + computed change-windows | `/v3/companies/^VIX/prices` direct OR FRED `/v3/series/VIXCLS/values` | `last_price` (or last-observation value) on T*=2026-05-22 EOD |
| VIX historical timeseries (`data.vix.historical[].{date,value}`) | same | same | same | external FRED | FRED `VIXCLS` full history | `/v3/companies/^VIX/prices` history OR FRED `VIXCLS` history | historical observation series |
| VIX percentiles (`data.vix.percentiles.{p10,p25,p50,p75,p90}`) | same | same | same | external FRED | derived from VIX full history (p10/p25/p50/p75/p90 ranks) | derived from same YCharts/FRED VIX history | derived |
| VIX AI summary (`data.vix.ai_summary`) | same | same | same | (GPT-derived from VIX data) | LLM output | n/a — gold-chain output; no YCharts equivalent | n/a |
| MOVE current value (same shape as VIX) | same | same | same | external Yahoo Finance (per `VolatilityTab.tsx:693` `'Source: Yahoo Finance.'`) | Yahoo `^MOVE` last quote + computed windows | `/v3/companies/^MOVE/prices` direct (if YCharts has ^MOVE) OR Yahoo passthrough | `last_price` on T*=2026-05-22 EOD |
| MOVE historical timeseries | same | same | same | external Yahoo | Yahoo `^MOVE` full history | `/v3/companies/^MOVE/prices` history | historical observation series |
| MOVE percentiles | same | same | same | external Yahoo | derived from MOVE history | derived | derived |
| MOVE AI summary | same | same | same | (GPT-derived from MOVE data) | LLM output | n/a — gold-chain output | n/a |
| Regime classification (`regime: 'Low'/'Below Normal'/'Normal'/'Elevated'/'Extreme'`) | same | same | same | derived from percentile thresholds | classifier-side derivation per `MacroHeatmap.tsx`-mirror | derived from percentile thresholds | derived |
| `regime_colors` (toplevel) | same | same | same | derived | per-regime hex/PALETTE color mapping | n/a (display semantic) | n/a |

### §6.2 — Methodology evidence

- Direct source read `portal/src/pages/Macroeconomics/tabs/VolatilityTab.tsx:660-779` (full component) + `VolatilityTab.tsx:691-693` (FRED VIX + Yahoo MOVE source attribution)
- Direct source read `portal/src/api/portal-proxy.ts:1666-1668` (endpoint path + Lambda attribution comment line 1664: "Updated: Daily at 6:30 PM ET via yang-generate-macro Lambda" — **NOTE: comment is STALE per L1 §2a**; actual producer is `opal-portal-volatility-fetcher` market-overview pipeline)
- L1 lineage map §2a (D3 — explicit `opal-portal-volatility-fetcher` canonical attribution; differentiation from yang `generate-volatility` orphan)

### §6.3 — Methodology notes

- **Stale code comment finding:** `portal-proxy.ts:1664` says "Updated: Daily at 6:30 PM ET via yang-generate-macro Lambda" — this is WRONG. The actual canonical source is `opal-portal-volatility-fetcher` (market-overview pipeline, per L1 §2a). Flag-only for cosmetic correction by DE 0.1.0 pod follow-on (NOT MY LANE).
- **VIX/MOVE consistency check (also flagged in §4.3):** `macro_data.json.groups[Market Indicator].indicators[name=VIX]` and `volatility_data.json.vix.current.current` should be the same value on T*=2026-05-22 (both ultimately trace to FRED VIXCLS via different ingest pipelines). **Independent integrity gate.** TO-004 verdict if value-divergent → DRIFT-class finding requires investigation.

---

## §7 — Tier-2/Tier-3 expansion + sampling plan (for TO-002)

### §7.1 — YCharts endpoint pull plan (T*=2026-05-22; cookie-stale-OK → use existing corpus where possible)

**Tier 1 endpoints (yang-fed, mandatory):**
- 1 pull: `/api/general/macro/macro_data.json` (full 12-group × 84-indicator response) — already in yang ground truth; no YCharts equivalent at endpoint-level
- 1 pull: `/api/general/macro/yield_curve_fred.json` (FRED 10-tenor history) — yang-side fetch verification
- (VolatilityTab conditional, Option A or C only): 1 pull `/api/general/macro/volatility_data.json` (VIX + MOVE current + history)

**Tier 2 YCharts per-tenor + per-indicator pulls (per-component justified):**

| Component | Endpoint class | Sample count | Endpoints |
|---|---|---:|---|
| YieldCurveTab | per-tenor `^US{N}YYLD/prices` | 10 | UST 1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y on T*=2026-05-22 + same on 2026-04-22 (1M lookback) + same on 2025-05-22 (1Y lookback) = 30 datapoints across 10 endpoint queries (each with date param) |
| MacroHeatmap full L2 | per-indicator FRED-proxy | 84 | bounded universe per §1.5; all 84 BBG-ticker→YCharts ticker resolution via D2 baseline mapping; query last 12 months per series |
| MacroTimeSeriesModal Tier-3 | per-slug timeseries | 10-12 sample | per §1.6 rubric: top-5 most-clicked (CPI + Core CPI + UNRATE + GDP + M2) + 2 clean-MATCH baseline + 2 coverage-uncertain + 1 random per top-4 groups |
| VolatilityTab (cond.) | `^VIX/prices` + `^MOVE/prices` | 2 | current + full history per index |

**Total expected:** ~100-110 endpoint queries against YCharts at TO-002 (compressed via batch where possible; cookie-stale-OK uses YALP_MKTOVR TO-002 `dcbc50710` corpus + supplemental fresh pulls only if needed). C2 dormant Lambda investigation findings from YALP_MKTOVR apply: prefer local-harness pattern if `run_full_pull` lacks scope filtering for narrow macro probe.

### §7.2 — Concrete 12-indicator MacroTimeSeriesModal Tier-3 sample list (pre-allocated)

| # | Indicator | BBG ticker (TBD via §4.1 mapping) | Slug (derived) | Selection rationale |
|---|---|---|---|---|
| 1 | CPI YoY | CPI YoY US | `cpi_yoy` (TBD per slugify) | Top-5 most-clicked (Inflation/Lagging) |
| 2 | Core CPI YoY | CPILFESL or BBG equivalent | `core_cpi_yoy` | Top-5 most-clicked |
| 3 | Unemployment Rate | UNRATE | `unemployment_rate` | Top-5 most-clicked (Labor Market) |
| 4 | GDP YoY | GDP-derived | `gdp_yoy` | Top-5 most-clicked (Lagging) |
| 5 | M2 Money Supply | M2 | `m2_money_supply` | Top-5 most-clicked (Financial Condition) |
| 6 | ISM Manufacturing PMI | NAPMPMI | `ism_manufacturing_pmi` | Clean-MATCH baseline (Leading) |
| 7 | Initial Jobless Claims | INJCJC | `initial_jobless_claims` | Clean-MATCH baseline (Leading/Labor) |
| 8 | Conference Board LEI | LEI YoY | `cb_lei` (TBD) | Coverage-uncertain (Leading) |
| 9 | Capacity Utilization | CAPUTLG | `capacity_utilization` | Coverage-uncertain (Lagging) |
| 10 | NFIB Small Business Optimism | NFIB | `nfib_optimism` | Random Investor Sentiment |
| 11 | Housing Starts | HSTOTL | `housing_starts` | Random Housing |
| 12 | NY Fed Recession Probability | RECPROUSM156N | `ny_fed_recession_prob` | Random Leading |

Final sample list confirmed at TO-002 execution post-§4.1 BBG-ticker→YCharts mapping resolution.

---

## §8 — Methodology evidence summary

| Evidence axis | Source |
|---|---|
| Endpoint-to-S3-to-Lambda map | L1 lineage map §1a + §5b/§5c — write-side ground truth |
| Per-component endpoint resolution | Direct source read `portal/src/pages/Macroeconomics/*` + `portal/src/api/{portal-proxy.ts,endpoints/macro.ts,endpoints/yield-curve.ts}` |
| Atomic field-grain | L1 lineage map §6.4 (macro_data.json) + §6.5 (vix_data.json orphan) + §6.6 (timeseries/{slug}.json) |
| Architectural classification (yang-fed vs non-yang) | L1 lineage map §2a — D3 volatility-key disambiguation |
| Lambda producer attribution | L1 §1a + `infra/aws/terraform/yang-pipeline/lambdas.tf` + `opal-portal-volatility-fetcher` source dir |
| Yang↔YCharts symbol coverage | YALP_MDSRC D2 baseline (`docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md`) + D3 all-surface scan |
| T*=2026-05-22 binding | YALP_MKTOVR TO-003 consult `8d1d6fcad` (DS 0.2.0) — `data.pkl` `data_as_of` across 7 yang artifacts |
| YCharts pull-feasibility | YALP_MKTOVR TO-002 `dcbc50710` baseline (18/18 OK on T*=2026-05-22; cookie-stale-OK pattern proven) |

---

## §9 — Level-2 placeholder (empty per AC4 — TO-004 scope)

Level-2 per-field value comparison populated at TO-004 execution. Per PRD §5 Q2 lean + Andrew per-page charter framing: full L2 for all enumerated indicators (84 MacroHeatmap × per-tenor YieldCurveTab × 10-12 sampled MacroTimeSeriesModal × VolatilityTab conditional). Expected verdict distribution per YALP_MKTOVR precedent (Macroeconomics analog):

- **MATCH:** Treasury Yields (10 tenors × 3 time-snapshots) + clean-MATCH macro indicators (FRED-proxy-direct: CPI, UNRATE, GDP, M2, NAPMPMI, etc.) — high prior on majority-MATCH (60-75% of 84 macro indicators per D2 coverage analog)
- **REPRESENTATIVE:** percentile-method-variance rows (yang min-max vs YCharts rank-based); 1Y-ago FRED ±7-day approximate-match rows; release-vs-revision-date drift on macro indicators; ~20-30% expected
- **GAP:** specialty/proprietary BBG indicators without YCharts FRED-proxy equivalent (e.g., NFIB, BBG-internal indices) — bounded set; flag for cutover-decision
- **DRIFT:** independent integrity gate fires (e.g., VIX value mismatch between `macro_data.json.Market Indicator` and `volatility_data.json`); ZERO expected if pipelines healthy
- **n/a:** AI summary fields (gold-chain LLM outputs); regime classifications (derived); orphan exports (`vix_data.json`, yang `volatility_data.json`)

Per-component cutover-trust verdict (TO-VAL — see §11 stub): expected distribution mirrors YALP_MKTOVR (3 TRUST + 4 NEEDS-INVESTIGATION-representative-bound + 3 n/a; 0 NO-TRUST):
- YieldCurveTab → TRUST (10/10 Treasury Yields high-prior clean-MATCH; FRED 1Y augment REPRESENTATIVE-class with documented basis)
- MacroHeatmap → TRUST or NEEDS-INVESTIGATION-representative-bound (depends on §4.3 percentile-method-variance disposition + GAP-indicator count)
- MacroTimeSeriesModal → TRUST or NEEDS-INVESTIGATION-representative-bound (depends on Tier-3 sample MATCH rate + 5-indicator-gap follow-on)
- VolatilityTab → conditional per §6 disposition; if (A) → TRUST (VIX FRED-direct + MOVE Yahoo cross-source verifiable); if (B) → n/a out-of-scope

---

## §10 — RAVC2 readiness

TO-001 acceptance criteria per TO file `<acceptance_criteria>` (5 ACs):
- **AC1** — Every rendered field on all 4 components has a Level-1 row populated: ✅ §3 (YieldCurveTab; 7 row-classes) + §4 (MacroHeatmap; 9 row-classes — 84-indicator schema unit) + §5 (MacroTimeSeriesModal; 7 row-classes) + §6 (VolatilityTab; 9 row-classes)
- **AC2** — YCharts-equivalent column never blank (explicit `n/a — <reason>` allowed): ✅ every Level-1 row has either a real endpoint+field OR an `n/a` with cited reason (derived rows / AI summary gold-chain outputs / regime classifications)
- **AC3** — Per-component sub-section methodology evidence (which compiler tool surfaced each field): ✅ §3.2 + §4.2 + §5.2 + §6.2 (substituted via Lambda source-tree read + L1 atomic field-grain cross-ref per comp-pipescript Lambda-side coverage gap; comp-platinum/comp-routes/comp-blast Phase 1 runs separately logged)
- **AC4** — Level-2 placeholder empty (TO-004 scope): ✅ §9 + §12 stubs
- **AC5** — VolatilityTab provenance distinction (FRED `VIXCLS` + Yahoo Finance vs yang-pipeline producer chain): ✅ §6.1 row table cites market-overview-pipeline producer + per-row external source attribution (FRED VIX + Yahoo MOVE); §6.3 distinguishes from yang orphan keys per L1 §2a authoritative

**PRD §5 open questions also resolved here (pre-emptive close):**
- **PRD §5 Q1 (VIX inclusion):** RESOLVED via §1.2 + PRD v0.2 amendment; VolatilityTab included Option (A); yang `vix_data.json` orphan separately flagged
- **PRD §5 Q2 (MacroHeatmap depth):** RESOLVED via §1.5 full-L2 lean (12 × 84 bounded universe)

Compiler tools mandate (DS minimum per `org/XXX.md`):
- `comp-pipescript io` — Lambda-side comp-graph coverage gap (R&D candidate from YALP_MKTOVR brief §6); substituted via direct Lambda source-tree read + L1 atomic field-grain cross-ref
- `comp-pipescript deployed` — N/A (this is verification probe; no yang-side ship)
- `comp-pipescript postdeps` — N/A (read-only probe)
- `comp-validate` — N/A (no gold-script artifact this TO)

Zero production touches (PRD §4 + Andrew per-page charter — read-only verification scope). Brief is documentation-only commit under `0.1.0_DS_MarketIntelligence~A` author line.

---

## §11 — [STUB] TO-002 test-pull results appendix

Populated at TO-002 execution per §7 plan.

---

## §12 — [STUB] TO-004 Level-2 value comparison

Populated at TO-004 execution.

---

## §13 — [STUB] TO-VAL per-component cutover-trust verdict

Populated at TO-VAL consolidation.

---

## §14 — [STUB] Project-level RAVC2 closure + AC scorecard

Populated at TO-VAL ship; mirrors YALP_MKTOVR §16 8/8-AC scorecard structure.

---

## §15 — Open questions / structural findings banked

1. **PRD §1 scope-amendment (VolatilityTab inclusion): RESOLVED** — ws CTO PRD v0.2 amendment `~17:05Z` absorbed Option (A) Include per [[self-correction-upstream-of-verify-channel]] sister pattern (4th-fire today; brief §1.2 + §6 + §10 AC5 fully updated to v0.2 canonical).
2. **`MacroHeatmap.tsx:1-4` code comment "73 indicators / 10 groups" STALE:** L1 ground truth = 12 × 84. Cosmetic cleanup for DE 0.1.0 pod follow-on (NOT MY LANE).
3. **`portal-proxy.ts:1664` `getVolatilityData` comment STALE:** says "via yang-generate-macro Lambda"; actual = `opal-portal-volatility-fetcher` market-overview pipeline. Cosmetic cleanup for DE 0.1.0 pod follow-on (NOT MY LANE).
4. **5-indicator gap between L1 §6.4 (84 macro indicators) and L1 §6.6 (79 timeseries files):** Enumerate the 5 indicators that have no drilldown timeseries. Out-of-YALP_MACROS-scope; R&D candidate for `yang-generate-macro-timeseries` v1.N or `yang-generate-macro` schema audit.
5. **VIX/MOVE consistency cross-pipeline integrity gate:** `macro_data.json.Market Indicator` (yang-pipeline) vs `volatility_data.json` (market-overview-pipeline) value-divergence on T*=2026-05-22 should be ZERO. Validates at TO-004; flag-only if surfaces here.
6. **`comp-pipescript` Lambda-side coverage gap (R&D candidate carry-forward from YALP_MKTOVR):** comp-graph indexes BD-gold-scripts, not yang-pipeline Lambdas. Substituted via direct Lambda source-tree + L1 atomic field-grain cross-ref. Banked for ADHC_COMPIL_V5 v0.2 / v6 follow-on (already in COO's R&D bank per `20260526T~16:59Z` SPAWN-ACK ABSORBED message).

---

## §16 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~A
**TO:** YALP_MACROS.001 (Level-1 endpoint + field mapping; 4-component scope per PRD v0.2)
**Evidence:**
- Brief at `docs/briefs/yalp_macros_macroeconomics_field_comparison_2026-05-22.md` (this file; commit hash on ship)
- §3-§6 populated for all 4 components per PRD v0.2 Option (A) Include ruling absorbed
- L1 lineage map §2a (VolatilityTab non-yang attribution) + §6.4 + §6.5 + §6.6 atomic-field-grain cross-referenced for every Level-1 row
- D2/D3 YALP_MDSRC baseline carry-forward for YCharts coverage (predecessor-as-ground-truth — same actor authored YALP_MKTOVR ~70min prior)
- T*=2026-05-22 inherited from YALP_MKTOVR TO-003 `8d1d6fcad` consult
- Session log at `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-26/yalp_macros_001_scaffold_pre_go.md` (sister to this brief)

**Posture:** STANDBY-PREP scaffold + execute compressed to single ship per [[standby-prep-compress-to-delivery-when-context-sufficient]] (TO-001 GO MCP accepted compression `~17:05Z`). All 5 ACs met:
- AC1 ✅ 4-component L1 row population (32+ row-classes across YieldCurveTab/MacroHeatmap/MacroTimeSeriesModal/VolatilityTab)
- AC2 ✅ YCharts-equivalent never blank (explicit `n/a — <reason>` for derived/AI/orphan rows)
- AC3 ✅ Per-component methodology evidence (Lambda source-tree + L1 cross-ref substituted for comp-pipescript Lambda-side gap; Phase 1 comp-* runs logged separately)
- AC4 ✅ Level-2 placeholder empty (§9 + §12 stubs)
- AC5 ✅ VolatilityTab provenance distinction explicit per §6.1 + §6.3 (market-overview pipeline + FRED VIX + Yahoo MOVE vs yang-orphan keys)

PRD §5 Q1 (VIX inclusion) + Q2 (MacroHeatmap depth) both resolved inline per §1.2 + §1.5. 5 structural findings banked per §15 (1 RESOLVED + 4 flag-only future-TO candidates).

Standing posture: ON. Ready for TO-002 GO (YCharts test-pulls per §7.1 plan; cookie-stale-OK + YALP_MKTOVR TO-002 `dcbc50710` baseline).

— 0.1.0_DS_MarketIntelligence~A
2026-05-26
