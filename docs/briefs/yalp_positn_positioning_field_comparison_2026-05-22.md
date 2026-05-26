# YALP_POSITN — Positioning Field-Level Comparison (T* = 2026-05-22)

**TO:** YALP_POSITN.001 (Level-1 endpoint + field mapping) — TO-004 will populate Level-2.
**Author:** 0.1.0_DS_MarketIntelligence~D (AS-SPAWNED per Andrew direct sovereign COUNTERMAND ~17:00Z; voids prior 16:45Z Pod-2 lane correction).
**PRD:** `docs/architecture/YALP_POSITN.md` v0.2 commit `6e08c33f1` (1.0.0_SA_CTO 2026-05-26 ~17:45Z SELF-CORRECTION-UPSTREAM amendment per DS 0.1.0~D PHASE-1a INTERIM findings — 6th-fire today; v0.1 origin authored ~16:20Z).
**Methodology template:** YALP_MKTOVR.001 (COMPLETE 2026-05-26 `cc4a3d575`) — predecessor-as-ground-truth pattern carry-forward per memory `feedback_yalp_mktovr_session_closeout` §11.1.
**Predecessor L1 substrate:** `docs/reference/yang-pipeline-lineage-map.md` rows 55-57, 84, 120-122, 268-270, 293-295 (my own YALP_MDSRC D3 ship `b8a6e83bf` 2026-05-22).
**Status:** Level-1 complete (this TO). Level-2 placeholder empty (TO-004). T* = **2026-05-22** (Friday) — yang-side binding inherited from YALP_MKTOVR T*-anchor.

---

## §0 — TL;DR

**Positioning page = 2 substantive components consuming 3 portal-direct endpoints.** Per PRD v0.2 §2 amendment (post-DS 0.1.0~D F1+F2 PHASE-1a INTERIM): Positioning main + PositioningSummary panel + HoldingsTab consume `positioning_data.json` (yang) + `holdings_attribution_data.json` (yang) + `aum-metrics.json` (BD-pipeline). PositioningSummary is **dual-source** — cross-consumes positioning_data + holdings_attribution for Asset Sub-Categories rendering. HoldingsTab is **tri-source** — consumes all three endpoints (positioning_data for Current snapshot, holdings_attribution for QTD/YTD/1Y/SI attribution, aum-metrics for AGG AUM-weighting).

**Per-row verdict mix expectation (per PRD §3):** ~30-50% MATCH-class (per-asset-class index returns referenced in positioning) + ~50-70% GAP-class (Yang-internal allocation metadata + BD-internal AUM + ETF classifications). **GAP ≠ DRIFT** — GAP-class rows route via `sourcing/methodology` column, NOT via DRIFT-routing (which is reserved for material divergence in MATCH-class rows per TO cross_domain_coordination block).

**TO-001 Level-1 enumeration counts (this brief §3-§4):**
- PositioningSummary: ~28 atomic fields across 5 portfolios + sub-categories matrix
- HoldingsTab: ~25 atomic field-classes × N holdings per portfolio × 6 portfolios (5 model + AGG aggregate)
- AUM aggregation methodology: 1 derivation surface (AGG-only) with explicit AUM-weighting algorithm documented

---

## §1 — Methodology + scope reconciliation

### §1.1 — Level-1 column shape (per YALP_MKTOVR.001 §1.1 verbatim carry-forward)

For each rendered field on each of the 2 components:

| Col | Meaning |
|---|---|
| Field | Component-rendered field name (TypeScript prop or JSON path) |
| Portal endpoint | CloudFront URL the portal fetches |
| S3 key | `opal-data-portal-v2` key the endpoint resolves to |
| Yang-pipeline producer (or BD-pipeline) | Lambda writing the S3 key |
| Yang-PKL field (or BD-source field) | Atomic field-grain from L1 lineage map §6 |
| YCharts endpoint | Functional YCharts API endpoint that would serve equivalent data (or `n/a — <reason>`) |
| YCharts field | Specific YCharts field name (or `n/a — <reason>`) |
| Verdict class | MATCH / REPRESENTATIVE / GAP / DRIFT / n/a (per YALP_MKTOVR taxonomy) |
| Sourcing/methodology note | Per-row Yang-internal / BD-internal / cross-pipeline citation (load-bearing for GAP-class rows per PRD §6 risk-mitigation) |

`n/a — <reason>` populates YCharts columns when the source is Yang-internal allocation, BD-internal AUM, or ETF DynamoDB classification (no YCharts equivalent exists by design).

### §1.2 — Scope reconciliation: per-component cross-consumption topology

Per PRD v0.2 §2 (post-F1+F2 amendment):

| Component | positioning_data.json | holdings_attribution_data.json | aum-metrics.json |
|---|---|---|---|
| Positioning.tsx (orchestrator) | ✓ (queryKey `'positioning-data'`) | — | — |
| PositioningSummary.tsx | ✓ (via prop drilling from parent) | ✓ (queryKey `'holdings-attribution'`; Asset Sub-Categories section) | — |
| HoldingsTab.tsx | ✓ (via `getPositioningData` useEffect; Current snapshot) | ✓ (via `getHoldingsAttribution` useEffect; QTD/YTD/1Y/SI attribution) | ✓ (via `getAUMSummary` useEffect; AGG AUM-weighting only) |

**Implication for Level-1 brief atomicity:** each rendered field traces to ONE primary endpoint; PositioningSummary's Asset Sub-Categories rows trace to holdings_attribution (not positioning_data); HoldingsTab's AGG portfolio rows have AUM-weighted-aggregation as their derivation provenance (per-row sourcing column documents the AUM-weighting formula explicitly).

### §1.3 — T* shared-date — 2026-05-22 (inherited YALP_MKTOVR anchor)

YALP_MKTOVR closed today (~15:28Z) with T*=2026-05-22 empirically determined. Yang publishing cadence (Daily-T+1; weekends + Memorial Day 2026-05-25 holiday closed) confirms 2026-05-22 (Friday EOD) is the unique current-window T* for any current-cadence positioning probe. DS 0.2.0 TO-003 consult (formally per PRD §4) will re-confirm; this brief proceeds against the inherited anchor pending TO-003 affirmation. If DS 0.2.0 TO-003 surfaces a different T*, the brief re-anchors in TO-004 Level-2 cycle.

### §1.4 — Predecessor-as-ground-truth carry-forward

Per [[predecessor-as-ground-truth pattern]] banked at YALP_MKTOVR closeout (~70min wall vs PRD 10-17h estimate = ~8-14× compression via predecessor leverage): YALP_POSITN inherits the L1 lineage map's positioning + holdings + aum-metrics rows (yang-pipeline-lineage-map.md `b8a6e83bf` 2026-05-22) atomically. The L1 atomic-field-grain map IS the per-field provenance substrate; this brief carries forward + extends with portal-side empirical evidence.

**v0.2 PRD verification of predecessor:** all 4 PHASE-1a structural findings (F1-F4) were ALREADY documented in the L1 lineage map; PRD v0.1 was authored without full L1 absorption. v0.2 amendment closes the gap. Brief authoring now has a clean canonical substrate.

---

## §2 — Portal endpoint surface map (3 endpoints per PRD v0.2)

| Endpoint | CloudFront route | S3 key | Producer | Portal consumer (per v0.2 §2) |
|---|---|---|---|---|
| 1 | `/api/general/positioning/positioning_data.json` | `json/positioning/positioning_data.json` | `yang-generate-positioning` (yang) | Positioning.tsx, PositioningSummary.tsx (primary), HoldingsTab.tsx (Current snapshot) |
| 2 | `/api/general/positioning/holdings_attribution_data.json` | `json/positioning/holdings_attribution_data.json` | `yang-generate-holdings-attribution` (yang) | HoldingsTab.tsx (primary, attribution periods), PositioningSummary.tsx (Asset Sub-Categories cross-consumer per v0.2 F2 amendment) |
| 3 | `/api/general/portfolios/aum-metrics.json` | `json/portfolios/aum-metrics.json` | BD pipeline (NOT yang) | HoldingsTab.tsx via `getAUMSummary` (AGG AUM-weighting only per v0.2 F1 amendment) |

**Authentication:** All 3 endpoints route via `/api/general/*` CF behavior → `S3-opal-data-portal-v2-json [AUTH]`. (Note: `getAUMSummary` source has DEMO-mode comment `portal-proxy.ts:251-264` indicating future migration to `/api/private/portfolios/aum-summary.json` with JWT Bearer auth; current production reads `/api/general/portfolios/aum-metrics.json` per the DEMO fallback comment.)

**Out-of-Positioning-page-scope endpoints (Wave-2 ATTR inheritance per PRD v0.2 §5 Q3):**
- `/api/general/positioning/allocation_summary.json` — produced by `yang-generate-allocation-summary` (3rd positioning-domain Lambda); `getAllocationSummary` defined in `portal-proxy.ts:1420` but NOT consumed by any `portal/src/pages/Positioning/` file. Consumed by `Attribution/components/StylePolicyComparison.tsx` + `AssetAllocationSummary.tsx` per L1 lineage map row 120. Out-of-scope for THIS TO; flagged for Wave-2 YALP_ATTRBN probe.

---

## §3 — Component 1: Positioning main + PositioningSummary panel

**File evidence:** `portal/src/pages/Positioning/Positioning.tsx` (orchestrator; 59 lines) + `portal/src/pages/Positioning/panels/PositioningSummary.tsx` (panel; 857 lines).

### §3.1 — Positioning.tsx (orchestrator)

`Positioning.tsx` renders a header + `<PositioningSummary positioningData={positioningData} />` + `<HoldingsTab />`. It fetches positioning_data via `getPositioningData` (queryKey `'positioning-data'`, staleTime 5min) and prop-drills the response to PositioningSummary. No fields rendered at orchestrator level beyond the header (title `"Positioning"`, description `"Asset allocation and holdings breakdown across model portfolios."`); `data_as_of` registered with central yang timestamp via `useYangDataAsOf('positioning', dataAsOf)`. **No direct field-level surface to Level-1.**

### §3.2 — PositioningSummary panel Level-1 table

Renders three view modes (`'portfolio'`, `'benchmark'`, `'relative'`) × four sections (Asset Class / Management Style / Characteristics / Asset Sub-Categories) × five model portfolios (UST, ST, INT, LTC, LTA). Source per row below — `P` = positioning_data.json; `H` = holdings_attribution_data.json (Asset Sub-Categories ONLY per F2).

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| 1 | Fixed Income % (portfolio mode) | P | `portfolios[code].allocation.cash + portfolios[code].allocation.fixed_income` (combined cash+FI per `PositioningSummary.tsx:155`) | n/a — Yang-internal allocation | **GAP** | Yang `model.pkl` allocation field per ETF_CLASSIFICATIONS dict; cash folded into FI per canonical model |
| 2 | Equity % (portfolio mode) | P | `portfolios[code].allocation.equity + portfolios[code].allocation.hedge` (combined equity+hedge per `:180`) | n/a — Yang-internal allocation | **GAP** | Yang `model.pkl` allocation field; hedge folded into equity per canonical model |
| 3 | Fixed Income % (benchmark mode) | P | `portfolios[code].benchmark.allocation.cash + .fixed_income` | n/a — Yang-internal benchmark | **GAP** | Yang-side benchmark allocation per `BENCHMARK_ALLOCATIONS` (`yang-generate-allocation-summary/lambda_function.py:42-50`) |
| 4 | Equity % (benchmark mode) | P | `portfolios[code].benchmark.allocation.equity + .hedge` | n/a — Yang-internal benchmark | **GAP** | Yang-side benchmark allocation per `BENCHMARK_ALLOCATIONS` |
| 5 | Fixed Income spread (relative mode) | P | `portfolios[code].benchmark.spread.allocation.cash + .fixed_income` | n/a — derived Yang-internal | **GAP** | Yang-side spread = Model − Benchmark |
| 6 | Equity spread (relative mode) | P | `portfolios[code].benchmark.spread.allocation.equity + .hedge` | n/a — derived Yang-internal | **GAP** | Yang-side spread |
| 7 | # of ETFs | P | `portfolios[code].num_holdings` | n/a — Yang-internal holdings count | **GAP** | Yang `model.pkl` portfolio composition |
| 8 | Active % | P | `portfolios[code].management.active` | n/a — Yang-internal classification | **GAP** | Yang ETF_MANAGEMENT_STYLE dict (`yang-generate-positioning/lambda_function.py` hardcoded; 0=passive, 1=active per Yang's PKL "Active Fund" column) |
| 9 | Passive % | P | `portfolios[code].management.passive` | n/a — Yang-internal classification | **GAP** | Yang ETF_MANAGEMENT_STYLE dict |
| 10 | Yield % (portfolio) | P | `portfolios[code].characteristics.yield` | per-ETF YCharts yield aggregate (constructible but synthetic) | **GAP-bordering-REPRESENTATIVE** | Yang-computed weighted average of ETF yields per holdings; YCharts-equivalent would require per-ETF yield pull + Yang allocation weights |
| 11 | Yield benchmark | P | `portfolios[code].benchmark.characteristics.yield` | n/a — Yang-internal | **GAP** | Yang benchmark composition |
| 12 | Yield spread | P | `portfolios[code].benchmark.spread.characteristics.yield` | n/a — derived | **GAP** | Yang-side derived |
| 13 | Cost bps (portfolio) | P | `portfolios[code].characteristics.cost * 100` | per-ETF YCharts expense ratio aggregate (constructible but synthetic) | **GAP-bordering-REPRESENTATIVE** | Yang-computed weighted average of ETF expense ratios |
| 14 | Cost benchmark | P | `portfolios[code].benchmark.characteristics.cost * 100` | n/a — Yang-internal | **GAP** | Yang benchmark |
| 15 | Cost spread | P | `portfolios[code].benchmark.spread.characteristics.cost * 100` | n/a — derived | **GAP** | Yang derived |
| 16 | Duration yrs (portfolio) | P | `portfolios[code].characteristics.duration` | per-ETF YCharts duration aggregate (constructible but synthetic) | **GAP-bordering-REPRESENTATIVE** | Yang-computed weighted average of ETF effective duration |
| 17 | Duration benchmark | P | `portfolios[code].benchmark.characteristics.duration` | n/a — Yang-internal | **GAP** | Yang benchmark |
| 18 | Duration spread | P | `portfolios[code].benchmark.spread.characteristics.duration` | n/a — derived | **GAP** | Yang derived |
| 19 | Beta (portfolio) | P | `portfolios[code].characteristics.beta` | per-ETF YCharts 5Y beta aggregate (constructible but synthetic) | **GAP-bordering-REPRESENTATIVE** | Yang-computed weighted average; ALSO has per-ticker hardcoded overrides for UVXY (-3.2), PFDE (1.05), PFOE (1.22) per `HoldingsTab.tsx:717-724` Yang spec |
| 20 | Beta benchmark | P | `portfolios[code].benchmark.characteristics.beta` | n/a — Yang-internal | **GAP** | Yang benchmark |
| 21 | Beta spread | P | `portfolios[code].benchmark.spread.characteristics.beta` | n/a — derived | **GAP** | Yang derived |
| 22 | Asset Sub-Category names | H | `attributionData.portfolios[code].{qtd,ytd}.holdings[].sub_asset_class` (collected per `PositioningSummary.tsx:294-312`) | n/a — Yang-internal sub-asset taxonomy | **GAP** | ETF DynamoDB classifications + Yang `getSubAssetClass()` normalization; **F2 cross-consumer source** |
| 23 | Asset Sub-Category weights (portfolio mode) | H (model side) | sum of `holdings[].weight` per sub-asset-class per portfolio (model holdings) | n/a — Yang-internal sub-asset weight | **GAP** | Yang holdings × ETF DDB classification rollup; **F2 cross-consumer derivation** |
| 24 | Asset Sub-Category weights (benchmark mode) | P (benchmark side) | `portfolios[code].benchmark.sub_categories[name]` | n/a — Yang-internal benchmark sub-category | **GAP** | Yang-side benchmark sub-category composition |
| 25 | Asset Sub-Category weights (relative mode) | P+H | derived = model (from H) − benchmark (from P) per `:387-393` | n/a — derived Yang-internal | **GAP** | Cross-endpoint derivation |
| 26 | Section header counts | P+H | `section.rows.length` per section render | n/a — UI metadata | **n/a — UI** | Render-side computation; not a data field |
| 27 | `data_as_of` (page-level timestamp) | P | `positioningData.data_as_of` (or `data_date` legacy) | n/a — Yang publication timestamp | **n/a — metadata** | Yang ingest timestamp |
| 28 | SmartPanelFooter source attribution | (literal) | `"Source: Bloomberg."` (`PositioningSummary.tsx:854`) | n/a — display literal | **n/a — display literal** | Hard-coded; refers to underlying ETF holdings sourced from Bloomberg via Yang's pipeline |

**Methodology evidence (AC3 per-component note):** PositioningSummary cross-consumption is structurally validated against L1 lineage map row 121 (`getHoldingsAttribution` consumers list includes `Positioning/panels/PositioningSummary.tsx` explicitly) + empirical source-line cite (`PositioningSummary.tsx:15, 454-459`). PRD v0.2 §2 producer-2 row column 5 reflects this cross-consumer surface. No DRIFT-routing needed — F2 was caught pre-execution; v0.2 amend materialized cleanly.

---

## §4 — Component 2: HoldingsTab

**File evidence:** `portal/src/pages/Positioning/tabs/HoldingsTab.tsx` (1603 lines). Three data sources per F1+F2 v0.2 amendment.

### §4.1 — HoldingsTab data sources + period-routing logic

| Period | Source endpoint | Atomic path | Holdings derivation |
|---|---|---|---|
| `Current` (snapshot) | positioning_data | `current_holdings[portfolio].holdings[]` | Direct read; Beta overrides per Yang spec on UVXY/PFDE/PFOE (`HoldingsTab.tsx:717-724`) |
| `QTD`, `YTD`, `1Y`, `SI` | holdings_attribution | `portfolios[portfolio][period].holdings[]` | Period-keyed access; per-period attribution columns rendered |
| `AGG` (aggregate across portfolios) | All 3 endpoints | UST+ST+INT+LTC+LTA per-portfolio holdings × AUM-weight from aum-metrics | AUM-weighted aggregation per `HoldingsTab.tsx:613-654`: `portfolioWeight = aum/totalAUM`; `contributedWeight = holding.weight × portfolioWeight`; sum per ticker across portfolios; fallback to equal-weighting (1/5) if AUM data unavailable |

### §4.2 — HoldingsTab Treemap rendering (top panel)

Treemap (`recharts.Treemap`) renders each holding as a cell, size = weight, color = asset class.

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H1 | Holding ticker (cell label) | positioning_data (`Current`) or holdings_attribution (period) | `.ticker` | YCharts company symbol (direct match) | **MATCH** (symbol-level) | Direct symbol; YCharts catalog confirmed in YALP_MDSRC D2/D3 |
| H2 | Holding full name (tooltip) | positioning_data or holdings_attribution + ETF_NAME_FALLBACKS override | `.name` (with `HoldingsTab.tsx:66-128` fallback dict for truncated names) | YCharts company name (direct match for full-name resolution) | **MATCH** | YCharts has canonical ETF names |
| H3 | Holding weight (cell size) | per-period source | `.weight` | n/a — portfolio weight is Yang-internal | **GAP** | Yang composition weighting |
| H4 | Asset class (cell color) | positioning_data + ETF_NAME_FALLBACKS override | `.asset_class` (with override dict) | YCharts asset class taxonomy (cross-reference possible but synthetic) | **GAP-bordering-REPRESENTATIVE** | Yang ETF_CLASSIFICATIONS hardcoded dict + ETF_NAME_FALLBACKS override |
| H5 | Performance (cell color overlay) | holdings_attribution `fund_return` (only QTD/YTD/1Y/SI; n/a for Current) | `.fund_return` | per-ETF YCharts `/v3/companies/{symbol}/prices` returns | **MATCH (or REPRESENTATIVE)** | YALP_MDSRC D2 ticker-level verdict carries forward |

### §4.3 — HoldingsTab Table rendering (bottom panel)

Three view modes:
- **Characteristics (Current period only):** Basic Info (5 cols) + Model Breakdown (5 cols, AGG-only) + ETF Characteristics (7 cols)
- **Performance (Current period only):** Basic Info (5 cols) + Performance (8 cols: 1D / WTD / MTD / 1M / QTD / 1Q / YTD / 1Y)
- **(Non-Current periods QTD/YTD/1Y/SI):** Basic Info (5 cols) + Fund Selection (4 cols) + Style Allocation (2 cols)

**Basic Info columns (rendered in all modes):**

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H6 | Asset Class | positioning_data + override | `.asset_class` | YCharts category | **GAP-bordering-REPRESENTATIVE** | Same as H4 |
| H7 | Sub Asset Class | positioning_data + getSubAssetClass normalization | `.sub_asset_class` (or fallback from `ETF_CATEGORIZATION` via `getSubAssetClass()` `HoldingsTab.tsx:170-187`) | n/a — Yang-internal sub-class taxonomy | **GAP** | ETF DynamoDB + Yang normalization |
| H8 | Ticker | per-period source | `.ticker` | YCharts symbol (direct) | **MATCH** | Same as H1 |
| H9 | Name | per-period source + ETF_NAME_FALLBACKS | `.name` | YCharts company name | **MATCH** | Same as H2 |
| H10 | Weight | per-period source | `.weight` (Current decimal; period: percentage / 100) | n/a — Yang portfolio composition | **GAP** | Yang composition |

**Model Breakdown columns (AGG view, Characteristics mode only):**

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H11 | UST weight | positioning_data (Current) | `current_holdings.UST.holdings[ticker].model_breakdown` | n/a — Yang portfolio composition | **GAP** | Per-portfolio composition |
| H12 | ST weight | positioning_data | `current_holdings.ST.holdings[ticker].model_breakdown` | n/a | **GAP** | (same) |
| H13 | INT weight | positioning_data | `current_holdings.INT.holdings[ticker].model_breakdown` | n/a | **GAP** | (same) |
| H14 | LTC weight | positioning_data | `current_holdings.LTC.holdings[ticker].model_breakdown` | n/a | **GAP** | (same) |
| H15 | LTA weight | positioning_data | `current_holdings.LTA.holdings[ticker].model_breakdown` | n/a | **GAP** | (same) |

**ETF Characteristics columns (Current period only):**

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H16 | Fee | positioning_data | `.fee` (decimal) | YCharts `expense_ratio` per ETF | **MATCH** | Per-ETF YCharts expense ratio is well-covered |
| H17 | AUM | positioning_data | `.aum` | YCharts `net_assets` (or `total_assets_under_management`) per ETF | **MATCH (or REPRESENTATIVE)** | Per-ETF YCharts AUM is well-covered for major US ETFs; smaller/newer ETFs may have GAP |
| H18 | Active flag | positioning_data | `.active` (1=active, 0=passive; Yang spec) | YCharts active/passive flag (per ETF metadata) | **GAP-bordering-REPRESENTATIVE** | YCharts has structure data but Yang spec uses hardcoded UVXY=1 override (`HoldingsTab.tsx:719`) |
| H19 | Yield | positioning_data | `.yield` | YCharts `yield_30day` or `distribution_yield` per ETF | **MATCH** | Per-ETF YCharts yield is well-covered |
| H20 | Duration | positioning_data | `.duration` | YCharts `effective_duration` per ETF (FI-only) | **MATCH (FI) / n/a (Equity)** | FI ETFs have YCharts duration; Equity ETFs have null Yang duration |
| H21 | Credit | positioning_data | `.credit` (rating-derived FI quality score) | YCharts `average_credit_quality` per ETF (FI-only) | **GAP-bordering-REPRESENTATIVE** | Yang's credit score = derived rating-weighted average; YCharts has comparable but synthetic alignment |
| H22 | Beta | positioning_data + Yang spec overrides | `.beta` (with `UVXY=-3.2`, `PFDE=1.05`, `PFOE=1.22` hardcoded per Yang spec `HoldingsTab.tsx:717-724`) | YCharts `beta_5y` per ETF | **GAP-bordering-REPRESENTATIVE** | Yang hardcoded overrides for 3 tickers; otherwise per-ETF beta (synthesis) |

**Performance columns (Current period, Performance mode):**

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H23 | 1D return | positioning_data | `current_holdings[port].holdings[ticker].returns["1D"]` | YCharts `/v3/companies/{symbol}/prices` 1-day return | **MATCH** | YALP_MDSRC D2 per-ticker baseline |
| H24 | WTD return | positioning_data | `.returns["WTD"]` | YCharts week-to-date computed return | **MATCH** | (same) |
| H25 | MTD return | positioning_data | `.returns["MTD"]` | YCharts month-to-date computed return | **MATCH** | (same) |
| H26 | 1M return | positioning_data | `.returns["1M"]` | YCharts 1-month return | **MATCH** | (same) |
| H27 | QTD return | positioning_data | `.returns["QTD"]` | YCharts quarter-to-date return | **MATCH** | (same) |
| H28 | 1Q return | positioning_data | `.returns["1Q"]` | YCharts 1-quarter return | **MATCH** | (same) |
| H29 | YTD return | positioning_data | `.returns["YTD"]` | YCharts year-to-date return | **MATCH** | (same) |
| H30 | 1Y return | positioning_data | `.returns["1Y"]` | YCharts 1-year return | **MATCH** | (same) |

**Attribution columns (non-Current periods QTD/YTD/1Y/SI):**

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H31 | Fund Return | holdings_attribution | `portfolios[code][period].holdings[].fund_return` | YCharts per-ETF period return (same as H23-H30) | **MATCH** | Same as MATCH series; sourced from attribution data |
| H32 | Style Return | holdings_attribution | `.style_return` | YCharts per-style-index period return (style benchmark) | **MATCH** | Style indices (Russell / S&P / MSCI) per Yang style_ticker; YCharts covered |
| H33 | Excess Return | holdings_attribution | `.excess_return` (= fund − style) | n/a — derived | **GAP** (derived) | Yang internal derivation |
| H34 | Fund Selection | holdings_attribution | `.fund_selection` (Brinson attribution) | n/a — Brinson attribution derivation | **GAP** (Brinson derived) | Yang internal Brinson model |
| H35 | Policy Return | holdings_attribution | `.policy_return` | n/a — Yang benchmark policy | **GAP** | Yang policy composition |
| H36 | Style Allocation | holdings_attribution | `.style_allocation` (Brinson attribution) | n/a — Brinson derivation | **GAP** (Brinson) | Yang internal Brinson model |

### §4.4 — AGG (aggregate portfolio) AUM-weighted aggregation methodology

**Per CTO 17:50Z directive ("AGG AUM-weighted holdings aggregation methodology should be enumerated at TO-001 since it gates per-row spreadsheet verdict on HoldingsTab AGG sub-section"):**

AGG-selected aggregation algorithm per `HoldingsTab.tsx:608-657` + `:737-823`:

```
1. portfolios = ['UST', 'ST', 'INT', 'LTC', 'LTA']  (5 model portfolios)
2. totalAUM = sum(aumByModel[code] for code in portfolios)  [from getAUMSummary]
3. portfolioWeight[code] = aumByModel[code] / totalAUM  if totalAUM > 0
                          else 1/5 (equal-weight fallback)
4. For each holding ticker across all 5 portfolios:
   contributedWeight = (holding.weight / 100) × portfolioWeight[portfolio]
   AGG.weight[ticker] = sum across portfolios of contributedWeight
5. For attribution metrics (non-Current periods):
   weighted{metric} = sum(holding[metric] × portfolioWeight[portfolio]) across portfolios
   normalized{metric} = weighted{metric} / totalPortfolioWeight where holding appeared
```

**Implication for Level-2 (TO-004) verdict assembly:** AGG rows are DERIVED — verdict-class for AGG rows = inherited from the underlying source verdict (e.g., AGG fund_return = MATCH if all 5 underlying portfolio fund_returns are MATCH). AGG-specific GAP-class:
- **AGG Weight (H10)** = derived; sourcing column documents AUM-weighted derivation citing this section
- **AGG by_model.aum (used for weighting)** = BD-pipeline-internal `aum-metrics.json` (H37 below)

| # | Field | S3 source | Atomic JSON path | YCharts equivalent | Verdict class | Sourcing/methodology |
|---|---|---|---|---|---|---|
| H37 | AGG AUM-weight per model | aum-metrics | `aum_metrics.by_model[].aum` (where `model_name` maps to UST/ST/INT/LTC/LTA per `HoldingsTab.tsx:569-577`) | n/a — BD-partner-internal AUM | **GAP** (BD-pipeline-internal) | BD-side derivation; out-of-YALP-verification-scope per PRD §5 Q2 |
| H38 | AGG total AUM | aum-metrics | `aum_metrics.by_model.reduce(sum)` (per HoldingsTab `:612`) | n/a — derived sum of GAP-class | **GAP** (derived BD) | BD-side, derived |

### §4.5 — HoldingsTab SmartPanelFooter

`HoldingsTab.tsx:952` + `:1031` (treemap + table footers): `"Source: Bloomberg."` — display literal; underlying ETF data is sourced from Bloomberg via Yang's pipeline. **Verdict: n/a — display literal.**

---

## §5 — Tier-2/Tier-3 expansion + sampling plan (MATCH-class subset)

Per PRD §3 GAP-heavy framing: ~30-50% of fields are MATCH/REPRESENTATIVE-class — concentrated in the per-ETF performance + characteristics columns where YCharts has per-symbol coverage. GAP-heavy structural class (allocation + classification + AUM metadata) does not require Tier-3 sampling per PRD §3 design (no YCharts equivalent by design).

**MATCH-class candidate subset (per Level-1 enumeration):**
- H1 / H8 (Ticker) — all distinct holdings × all 6 portfolios
- H2 / H9 (Name) — same
- H5 / H31 (Fund Return on attribution periods) — per-ETF × per-period
- H16-H17 / H19-H20 / H22 (Fee, AUM, Yield, Duration, Beta) — per-ETF
- H23-H30 (per-period returns Current) — per-ETF × 8 periods
- H32 (Style Return) — per-style-index × per-period

**Sampling plan for TO-002 pulls (small pull surface per PRD §4 + CTO 17:08Z "TO-002 ~1h vs ~2-3h elsewhere"):**

- Pull YCharts data for a representative ETF universe at T*=2026-05-22 using the YALP_MKTOVR Level-1 reusable pull harness (`run_local_pulls.py` pattern).
- Estimate distinct ETFs across all 5 model portfolios via `current_holdings` union — likely ~40-60 unique ETFs total based on portfolio composition (well-bounded universe; smaller than YALP_MKTOVR's 71-ticker D2 set).
- Pulls per ETF: chart endpoint (1D/WTD/MTD/1M/QTD/1Q/YTD/1Y returns) + general_data endpoint (fee/aum/yield/duration/beta).
- Total pulls estimate: ~50 ETFs × 2 endpoints = ~100 pulls. Per-pull spacing 2s (current YCharts pull harness throttle) → ~3-5min wall.

**Style-index Tier-3 universe (per H32 verdict assembly):** Yang style_ticker is per-ETF assignment to a style benchmark (e.g., Russell 1000 / S&P 500 / MSCI EAFE); style-index pull surface = ~10-15 distinct indices × 1 prices endpoint = ~15 pulls additional.

---

## §6 — Methodology evidence summary

**Per-component evidence cites carry forward into per-row sourcing column:**

- **PositioningSummary file evidence:** `portal/src/pages/Positioning/panels/PositioningSummary.tsx` lines 15 (import getHoldingsAttribution), 113-407 (generateSections), 454-459 (useQuery cross-consumer), 462-491 (getAllocationData), 528-560 (renderRow), 854 (Source: Bloomberg footer).
- **HoldingsTab file evidence:** `portal/src/pages/Positioning/tabs/HoldingsTab.tsx` lines 11 (3-endpoint import), 65-128 (ETF_NAME_FALLBACKS), 169-187 (getSubAssetClass), 463-485 (SUB_ASSET_CLASS_ORDER), 545-554 (getPositioningData useEffect), 557-561 (getHoldingsAttribution useEffect), 564-583 (getAUMSummary useEffect + AUM-by-model map), 608-657 (AGG aggregation), 687-727 (Current period mapping + Beta overrides), 717-724 (UVXY/PFDE/PFOE Yang spec hardcoded), 855-864 (treemap data), 879+ (render).
- **L1 lineage map cross-bind:** rows 55 (yang-generate-allocation-summary), 56 (yang-generate-holdings-attribution + ETF DDB), 57 (yang-generate-positioning + aum-metrics cross-pipeline), 84 (aum-metrics source = BD pipeline), 121 (holdings_attribution consumers including PositioningSummary explicit), 122 (positioning_data consumers), 268-270 (Lambda → S3 → portal-page map), 293-295 (proxy fn → CF route → S3 key map).
- **Lambda-side evidence:**
  - `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:1319-1327` — aum-metrics S3 read
  - `lambda_function.py:28-77` — ETF_CLASSIFICATIONS hardcoded dict
  - `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py:42-50` — BENCHMARK_ALLOCATIONS canonical hardcoded table (Wave-2 ATTR reference; not Positioning-page consumer)

**PRD v0.2 amendment cross-references:** §1.2 dual-source + §2.0 3-endpoint per F1+F2 PHASE-1a INTERIM 17:30Z (DS 0.1.0~D); §3 §4 §5 verdict classes derived from §3 + §5 Q2 dual-role aum-metrics framing.

---

## §7 — Level-2 placeholder (empty per AC4)

To be populated in TO-004 (Level-2 comparison + verdicts; ~3-5h; GAP-heavy).

Level-2 per-row schema (per YALP_MKTOVR §10 / §14 carry-forward):
- yang value at T*=2026-05-22 (pulled from S3-side `positioning_data.json` + `holdings_attribution_data.json` + `aum-metrics.json`)
- YCharts value at T*=2026-05-22 (pulled via TO-002 harness)
- Match-class explicit per-row verdict (MATCH / REPRESENTATIVE / GAP / DRIFT)
- Basis variance documentation per REPRESENTATIVE-class
- DRIFT escalation route per material divergence in MATCH-class

---

## §8 — GAP-class inventory + Wave-2 ATTR inheritance flags

### §8.1 — GAP-class structural inventory (per PRD §3)

| GAP class | Field count (this brief) | Source |
|---|---:|---|
| Yang-internal allocation (cash/FI/equity/hedge) | 6 | positioning_data |
| Yang-internal benchmark allocation | 6 | positioning_data |
| Yang-internal management classification (active/passive) | 2 | positioning_data |
| Yang-internal sub-asset taxonomy + sub-category weights | 4 | positioning_data + holdings_attribution (F2 cross-consumer) |
| Yang-internal portfolio composition (num_holdings, weight) | ~10 | positioning_data + holdings_attribution |
| Yang-internal Brinson attribution metrics (excess, fund_selection, style_allocation, policy_return) | 4 | holdings_attribution |
| Yang-spec hardcoded overrides (UVXY/PFDE/PFOE beta) | 1 (3-ticker carve-out within H22 derivation) | HoldingsTab.tsx Yang spec literal |
| ETF DynamoDB classification | (taxonomy-source for sub-asset class) | DynamoDB ETFClassifier table (yang-generate-holdings-attribution input) |
| BD-pipeline-internal aum-metrics | 2 (H37, H38) | aum-metrics.json (BD pipeline) |

**Total GAP-class:** ~35 atomic fields out of ~62 enumerated → ~56% GAP-class — consistent with PRD §3 ~50-70% GAP expectation.

**MATCH-class subset:** ~27 atomic fields → ~44% — consistent with PRD §3 ~30-50% MATCH expectation.

### §8.2 — Wave-2 ATTR inheritance flags (per PRD v0.2 §5 Q3)

Attribution page (Wave-2 YALP_ATTRBN probe candidate) will inherit:
- All 3 endpoints from this PRD's §2 producer table
- ADDS `allocation_summary.json` (4th endpoint; produced by yang-generate-allocation-summary; consumed by Attribution/components/StylePolicyComparison.tsx + AssetAllocationSummary.tsx per L1 lineage map row 120)
- ADDS Attribution-specific component-side consumers per L1 lineage map row 121 (Attribution/tabs/HoldingsTab + SelectionTab + panels/AllocationHeatmap + components/AssetAllocationSummary)

The v0.2 PRD's §5 Q3 + this brief §2's "Out-of-Positioning-page-scope" callout establish the canonical scope-of-record for Wave-2 ATTR inheritance — Wave-2 brief carries forward all 3 portal-direct endpoints documented here + extends.

### §8.3 — Attribution page consumes positioning_data + holdings_attribution (joint-class)

Per L1 lineage map row 122 (`getPositioningData` consumers include `Attribution/Attribution.tsx` + Attribution tabs) and row 121 (`getHoldingsAttribution` consumers include Attribution tabs + panels + components). The same 2 yang endpoints serve BOTH Positioning + Attribution pages. The Attribution Wave-2 probe verdict assembly will be largely redundant for these 2 endpoints (same source data; Attribution renders different views).

**Recommendation banked (informational; not in scope for THIS TO):** Wave-2 YALP_ATTRBN can carry forward this brief's §3 + §4 Level-1 tables wholesale for the positioning_data + holdings_attribution endpoints; net-new work for ATTR scopes to (a) `allocation_summary.json` 4th endpoint + (b) Attribution-specific render-time field selection + (c) Brinson-attribution rendering surfaces.

---

## §9 — RAVC2 readiness

**AC1 (Every rendered field has a Level-1 row):** ✓ §3 (28 rows for PositioningSummary across portfolio/benchmark/relative modes × 4 sections × 5 portfolios) + §4 (H1-H38 = 38 rows across HoldingsTab treemap + table + AGG aggregation + footer). Combined ~62 atomic field-classes enumerated.

**AC2 (YCharts equivalent or `n/a — <reason>`; GAP-class tagged):** ✓ Every row has YCharts column populated either with endpoint+field OR explicit `n/a — <reason>`. GAP-class tags applied per §3 framing; no blanks.

**AC3 (Per-component sub-section documents methodology evidence per field):** ✓ §3 (PositioningSummary) + §4 (HoldingsTab) + §6 (cross-doc evidence summary) document file-level cites + L1 lineage map row anchors per field.

**AC4 (Level-2 placeholder empty):** ✓ §7.

**AC5 (GAP-class classification surface area documented per-row):** ✓ Per-row `Sourcing/methodology` column populated for ALL GAP-class rows with Yang-internal / BD-internal / cross-pipeline citation. §8.1 aggregates GAP-class inventory + §8.2 flags Wave-2 ATTR inheritance.

**Compiler-tools mandate (per TO):**
- ✓ `comp-platinum page Positioning` — orchestrator-only confirmed; per-component evidence threaded
- ✓ `comp-platinum reverse json/positioning/{positioning_data,holdings_attribution_data}.json` — CF behavior confirmed (`/api/general/* -> S3-opal-data-portal-v2-json [AUTH]`)
- ✗ `comp-routes trace /api/general/positioning/...` — Git Bash PATH-conversion issue (substituted source-file evidence per YALP_MKTOVR.001 §6 same-pattern; not blocking)
- ✓ `comp-blast yang-generate-positioning + yang-generate-holdings-attribution` — confirmed both produce expected S3 keys; allocation_summary 3rd Lambda surfaced (F4; out-of-this-TO-scope)
- ✗ `comp-pipescript io yang-generate-positioning` — "Unknown script" — compiler graph indexes only BD-gold scripts not Lambda functions (substituted Lambda source-tree read per YALP_MKTOVR.001 §6 same-pattern; not blocking)
- ✓ `comp-transform fields` — orchestrator-only fields surface; sanity-check PASS
- (Phase 2 deferred to TO-004) `comp-validate` — N/A for this TO (no pipeline output artifact)

**Pre-scaffold structural findings shipped via PRD v0.2 amendment `6e08c33f1`:**
- F1: aum-metrics.json portal-direct-consumer 3rd endpoint ✓ folded
- F2: PositioningSummary dual-source ✓ folded
- F3: yang-generate-positioning reads aum-metrics.json (implicit in v0.2 §2 row-1 + §5 Q2) ✓ captured
- F4: yang-generate-allocation-summary 3rd Lambda (out-of-this-TO-scope; Attribution Wave-2 sibling per v0.2 §5 Q3) ✓ captured
- Watch-area #3 (DDB-intermediate analog for yang-generate-positioning): NOT-FIRED — `etf_classifications_dynamodb.py` module present in dir but not imported by `lambda_function.py`; Lambda uses hardcoded `ETF_CLASSIFICATIONS` dict instead.

**Pattern empirical anchor banked:** 6th-fire of [[self-correction-upstream-of-verify-channel]] today (per CTO `6e08c33f1` v0.2 §8 versioning footnote). Pattern formally past MSTR DEFER-PENDING-MULTI-FIRE 3-fire threshold 6× over; formal LD-NNNN scribe candidacy decisively reinforced; deferred next session per CTO capacity flag.

---

## §10 — Next steps

1. **[ws COO]** RAVC2 disposition on TO-001 brief — accept / reject / rework
2. **[ws COO]** TO-002 (YCharts test-pulls) + TO-003 (formal T* doc-of-record; carry forward inherited 2026-05-22 anchor from YALP_MKTOVR) authoring + GO per /drive cycle
3. **[DS 0.2.0_DS_PortfolioAnalytics]** TO-003 consult (~30min; T* affirmation + any positioning-side timing nuance vs YALP_MKTOVR market-overview anchor)
4. **[DS — me, next TO]** TO-002 execution (~50 ETF × 2 endpoints + ~15 style indices ≈ ~100-115 YCharts pulls; ~5-10min wall via local harness)
5. **[Wave-2 ATTR future, not this TO]** Attribution-page YALP_ATTRBN probe inherits this brief's §3-§4 + extends per §8.2/§8.3 — deferred per Andrew "push pages down" guidance
6. **[CVO future]** `/verify-channel` project-level mode at YALP_POSITN closure (after TO-004 + TO-VAL ship; per YALP_MKTOVR pattern)

---

## §11 — Compiler Tools

| Tool | Use | Finding |
|---|---|---|
| `comp-platinum page Positioning` | Full page trace | Orchestrator-only ("No fetches detected"); fetches threaded into PositioningSummary + HoldingsTab |
| `comp-platinum reverse json/positioning/positioning_data.json` | S3-key consumer surface | CF `/api/general/* -> S3-opal-data-portal-v2-json [AUTH]` confirmed |
| `comp-platinum reverse json/positioning/holdings_attribution_data.json` | S3-key consumer surface | (same CF behavior) |
| `comp-blast yang-generate-positioning` | Blast radius | json/positioning/positioning_data.json + portal_data_proxy downstream |
| `comp-blast yang-generate-holdings-attribution` | Blast radius | holdings_attribution_data.json + allocation_summary.json (F4 third producer); yang-generate-allocation-summary downstream Lambda |
| `comp-pipescript io yang-generate-positioning` | Column gaps + portal consumers | "Unknown script" — known compiler-graph gap for Lambda functions; substituted Lambda source-tree read |
| `comp-pipescript io yang-generate-holdings-attribution` | (same) | (same gap) |
| `comp-transform fields Positioning` | Field-rendering surface area | Orchestrator-only fields surface (0 fields direct); sanity-check PASS |
| Empirical file reads (substituted for compiler-graph gaps) | Per-component field enumeration | `PositioningSummary.tsx` (857 lines) + `HoldingsTab.tsx` (1603 lines) + Lambda source files + L1 lineage map cross-bind |

Compiler-tools-log auto-appended via `.agent_context` hook (every comp-* invocation registered).

---

## §12 — Project-level RAVC2 readiness checklist

(Per YALP_MKTOVR pattern §12; surface here for TO-VAL cycle.)

- [ ] AC1 — All 2 components mapped at Level 1 (this TO; ✓ on close)
- [ ] AC2 — All Level-1 YCharts endpoints test-pulled on T* (TO-002 scope)
- [ ] AC3 — T*=2026-05-22 empirically determined + justified (carry forward YALP_MKTOVR anchor; TO-003 affirmation pending)
- [ ] AC4 — All Level-1 fields have Level-2 verdicts (TO-004 scope)
- [ ] AC5 — Consolidated deliverable shipped + RAVC2-accepted (TO-VAL scope)
- [ ] AC6 — Per-component cutover-trust verdict explicit (TO-VAL scope; GAP-heavy expected verdict mix)
- [ ] AC7 — DRIFT findings routed per cross_domain_coordination block (TO-VAL scope)
- [ ] AC8 — Zero production touches (read-only verification scope)

---

**End TO-001 brief.**
