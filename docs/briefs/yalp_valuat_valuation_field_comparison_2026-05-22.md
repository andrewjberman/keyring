# YALP_VALUAT — Valuation page YCharts-vs-Yang field comparison

**Brief — Level-1 endpoint+field mapping** (TO-001 deliverable)
**Author:** 0.1.0_DS_MarketIntelligence~B
**T\*:** 2026-05-22 (inherited from YALP_MKTOVR per ws COO `20260526T...REOPEN_GO`; portal `valuation_data.json.data_as_of` and `risk_premium_data.json.data_as_of` both confirm `2026-05-22`).
**TO:** YALP_VALUAT.001 (`org/tier2_senior/0.1.0_DS_MarketIntelligence~B/task_orders/YALP_VALUAT.001.valuation-l1-endpoint-field-mapping.md`)
**PRD:** `docs/architecture/YALP_VALUAT.md` v0.1
**Methodology template:** YALP_MKTOVR brief `docs/briefs/yalp_mktovr_market_overview_field_comparison_2026-05-22.md` (mirrored verbatim).
**Status:** Level-1 COMPLETE — Level-2 placeholder per AC4 (TO-004 scope).

---

## §0 — TL;DR

- **2 endpoints in scope:** `/api/general/valuation/valuation_data.json` + `/api/general/valuation/risk_premium_data.json`.
- **2 components per PRD §1:** Valuation main view (3 portal-surface projections: `ValuationSummaryPanel` + `ValuationRangePanel` + `ValuationTimeSeriesTab` — all consume same endpoint via `useValuationData` hook) + `RiskPremiumTab` (separate fetch).
- **Level-1 field coverage:** 8 atomic fields × ~37 equity indices (valuation rubric) + 8 atomic fields × T-1 series count (risk-premium rubric) = full enumeration per portal-consumed schema.
- **Level-2 placeholder:** empty per AC4 — TO-004 will populate verdicts (MATCH / REPRESENTATIVE / DRIFT / GAP).
- **GAP-class fields confirmed (AC5):** Yang ERP (`erp.value` = `earnings_yield - treasury_rate` Yang-derived from `data.pkl.return_monthly.pe_ntm` + `data.pkl.price_monthly.10Y_Treasury`); also `erp.data[].earnings_yield` + `erp.data[].treasury_rate` (intermediate Yang-derived sub-fields rendered in ERP tooltip).
- **ICE BofA OAS rows mapped:** YCharts FRED-proxy `series/BAMLC0A0CM` (IG) + `series/BAMLH0A0HYM2` (HY) candidates; direct ICE access optional. NOTE: live JSON 2026-05-22 currently sourcing from Yang PKL Bloomberg OAS fallback (FRED count <= 1000 threshold gate fired) — §5.F1.
- **5 structural findings surfaced** (§5): PRD/lineage drift relative to live producer state. Banked for /verify-channel + future PRD-amendment cycle.

---

## §1 — Methodology + scope reconciliation

### §1.1 — Level-1 column shape (per PRD §3.1)

Per YALP_MKTOVR mirror — 7-column Level-1 row per atomic field:

| Component field | Portal endpoint | S3 key | Producer Lambda | Yang-pipeline upstream | Yang-processed PKL field | YCharts API endpoint | YCharts field |

For YALP_VALUAT specifically: PRD §2 establishes that Valuation uses the **direct `json/valuation/*.json` flow** (NOT the DDB-intermediated branch which is Market-Overview-specific per YALP_MKTOVR §1.3). Producer Lambda column = `yang-generate-valuation` or `yang-generate-risk-premium` directly; upstream = `data.pkl` Bloomberg fields per L1 lineage map §6.1 + §6.2.

### §1.2 — Scope reconciliation: PRD "2 components" vs portal "4 surfaces"

PRD §1 lists 2 components; portal `Valuation.tsx` renders **4 visual surfaces**:
1. `ValuationSummaryPanel` (Latest Percentile heatmap; `data.summary[]`)
2. `ValuationRangePanel` (Selected-index percentile ranges + current values; `data.ranges[selectedIndex]`)
3. `ValuationTimeSeriesTab` (Historical time series with percentile bands; `data.time_series`)
4. `RiskPremiumTab` (ERP + IG/HY credit spreads; separate `risk_premium_data.json` fetch)

**Reconciled per endpoint-centric framing:** PRD's "Valuation main view" = surfaces 1+2+3 (all consume same `valuation_data.json` via `useValuationData` hook). Level-1 mapping is endpoint-centric so per-endpoint enumeration covers ALL rendered fields cleanly. The 3 portal-side surfaces are different *projections* of one underlying dataset.

**Not a structural finding — clean per-endpoint framing.** Distinct from YALP_MACROS DS 0.1.0~A's VolatilityTab catch (which surfaced a *missing* component in PRD §1 = legitimately needs PRD amendment). Here PRD §1 collapsed 3 portal surfaces into 1 endpoint = methodologically correct.

### §1.3 — T\* shared-date — 2026-05-22

Per ws COO `[REOPEN + GO]` directive: T\*=2026-05-22 inherited from YALP_MKTOVR rather than firing fresh DS 0.2.0 TO-003 consult (saves ~30min wall; T\*=2026-05-22 well-vetted across YALP_MKTOVR + sister Wave-1 pages). Live JSON confirmed: both endpoints `data_as_of: 2026-05-22`. If DS 0.2.0 surfaces a different T\* via their parallel YALP_POSITN/CORREL/FACTOR work, swap at TO-004 time (Level-1 mapping is T\*-agnostic).

### §1.4 — Sampling plan

Per PRD §1 / AC1 — Level-1 enumerates **every rendered field** across both endpoints. No sampling at Level-1. At Level-2 (TO-004), bounded universe per atomic-field-grain: per `summary[]` ticker × 7 metrics + per `ranges[idx][m]` band thresholds + per `erp.data[]` series + per `credit.ig.data[]` (denormalized IG+HY) — full census fits cleanly in TO-004 scope.

---

## §2 — Endpoint family

| Portal endpoint | S3 key | Tier | Consumer surfaces |
|---|---|---|---|
| `/api/general/valuation/valuation_data.json` | `opal-data-portal-v2/json/valuation/valuation_data.json` | Tier-1 page-mount | `ValuationSummaryPanel` + `ValuationRangePanel` + `ValuationTimeSeriesTab` (via `useValuationData` hook) |
| `/api/general/valuation/risk_premium_data.json` | `opal-data-portal-v2/json/valuation/risk_premium_data.json` | Tier-1 (RiskPremiumTab mount) | `RiskPremiumTab` (direct `getRiskPremiumData` via React Query) |

Both are **direct yang-pipeline JSON** (NOT DDB-intermediated like Market Overview).

CF mapping per `infra/aws/cloudfront/...` + portal endpoint-mapping: `/api/general/*` → S3-opal-data-portal-v2-json [AUTH]. `comp-platinum reverse` confirms producer column linkage (Lambda `yang-generate-valuation` → S3 `json/valuation/valuation_data.json`; Lambda `yang-generate-risk-premium` → S3 `json/valuation/risk_premium_data.json`).

---

## §3 — Component 1: Valuation main view

Endpoint: `/api/general/valuation/valuation_data.json` → Producer: `yang-generate-valuation` → Upstream: `data.pkl.price_monthly` (Bloomberg) METRIC_MAPPING (pe_ntm→fwd_pe, pe_ltm→trailing_pe, pfcf→p_fcf, ev_sales, pb→p_b, ps→p_sales, dy→div_yield) × ~37 EQUITY_INDICES (`dc_index` rubric).

### §3.1 — Level-1 mapping (Valuation main view)

| Portal field | S3 key | Producer Lambda | Yang upstream | data.pkl field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|
| `data.data_as_of` | json/valuation/valuation_data.json | yang-generate-valuation | latest `price_monthly` date | derived | n/a — metadata | n/a |
| `data.summary[].index` | "" | "" | EQUITY_INDICES list | derived | per-ticker companies endpoint | n/a (key) |
| `data.summary[].fwd_pe` | "" | "" | price_monthly pe_ntm percentile | pe_ntm | `/v3/companies/{ticker}/key-stats` | `forward_pe_ratio` (NOTE: portal exposes %ile, YCharts likely raw — Level-2 verdict REPRESENTATIVE-class) |
| `data.summary[].trailing_pe` | "" | "" | price_monthly pe_ltm percentile | pe_ltm | `/v3/companies/{ticker}/key-stats` | `pe_ratio` |
| `data.summary[].p_fcf` | "" | "" | price_monthly pfcf percentile | pfcf | `/v3/companies/{ticker}/key-stats` | `price_to_free_cash_flow` |
| `data.summary[].ev_sales` | "" | "" | price_monthly ev_sales percentile | ev_sales | `/v3/companies/{ticker}/key-stats` | `enterprise_value_to_revenue` |
| `data.summary[].p_b` | "" | "" | price_monthly pb percentile | pb | `/v3/companies/{ticker}/key-stats` | `price_to_book_value` |
| `data.summary[].p_sales` | "" | "" | price_monthly ps percentile | ps | `/v3/companies/{ticker}/key-stats` | `price_to_revenue` |
| `data.summary[].div_yield` | "" | "" | price_monthly dy percentile | dy | `/v3/companies/{ticker}/key-stats` | `dividend_yield` (inverted scale — portal renders raw %ile; UI inverts at render time per `getPercentileBgColor` exception) |
| `data.ranges[idx][m].metric` | "" | "" | METRIC_MAPPING key | derived | n/a — key | n/a |
| `data.ranges[idx][m].label` | "" | "" | METRIC_LABELS lookup | derived | n/a — display | n/a |
| `data.ranges[idx][m].percentile` | "" | "" | latest percentile of metric vs history | same as summary[m] | `/v3/companies/{ticker}/key-stats` | same field (derived rank) |
| `data.ranges[idx][m].current` | "" | "" | latest raw value of metric | metric latest value | `/v3/companies/{ticker}/key-stats` | same field (raw value) |
| `data.ranges[idx][m].p10` | "" | "" | historical 10th-pct value | metric distribution | n/a — derived stat | n/a |
| `data.ranges[idx][m].p25` | "" | "" | historical 25th-pct value | metric distribution | n/a — derived stat | n/a |
| `data.ranges[idx][m].p50` | "" | "" | historical median value | metric distribution | n/a — derived stat | n/a |
| `data.ranges[idx][m].p75` | "" | "" | historical 75th-pct value | metric distribution | n/a — derived stat | n/a |
| `data.ranges[idx][m].p90` | "" | "" | historical 90th-pct value | metric distribution | n/a — derived stat | n/a |
| `data.time_series[idx][m].data[].date` | "" | "" | price_monthly date index | row date | YCharts series endpoint | n/a (key) |
| `data.time_series[idx][m].data[].value` | "" | "" | price_monthly metric column | metric value | `/v3/companies/{ticker}/historical/{metric}` | per-metric historical series |
| `data.time_series[idx][m].data[].percentile` | "" | "" | rolling-percentile rank vs metric distribution | derived | n/a — derived stat | n/a |
| `data.time_series[idx][m].thresholds` | "" | "" | distribution thresholds (frontend-recomputes from windowed data per RiskPremiumTab pattern) | derived | n/a — derived stat | n/a |

**Equity ticker universe (`dc_index` rubric, ~37 indices per L1 §6.1):** S&P 500, Dow Jones, Nasdaq, Russell 1000, Russell 2000, MSCI USA, MSCI World, MSCI ACWI, MSCI EAFE, MSCI Emerging Markets, MSCI Europe, MSCI Japan, MSCI Pacific ex-Japan, MSCI Latin America, MSCI BRIC, S&P 500 Growth, S&P 500 Value, Russell 1000 Growth, Russell 1000 Value, Russell 2000 Growth, Russell 2000 Value, etc. (live `ranges` keys top-5 confirmed: `S&P 500, Dow Jones, Nasdaq, Russell 1000, MSCI USA`).

### §3.2 — Methodology evidence (Component 1)

| Compiler tool / inspection | Use | Finding |
|---|---|---|
| `comp-platinum reverse json/valuation/valuation_data.json` | S3 key → producer | Producer node not explicitly named in graph; SERVED VIA: `/api/general/json/valuation/valuation_data.json` CF→S3 [AUTH] confirmed; CONSUMERS: no components-found (hook-indirect via `useValuationData` — graph artifact; portal source grep confirmed `useValuationData → getValuationData → portalProxy.getValuationData → apiRequest('/api/general/valuation/valuation_data.json')`) |
| `comp-blast yang-generate-valuation` | Lambda blast radius | LAMBDA(5): portal_data_proxy×2, opal-portal-data-proxy, _build_tmp×2; S3_ARTIFACT(2): json/valuation/valuation_data.json (×2); 7 downstream nodes affected |
| Portal source grep | Per-field consumer surfacing | `portal/src/pages/Valuation/types.ts` declares `ValuationMetric` union (7 metrics matching `data.summary[]` columns); `ValuationSummaryRow` + `ValuationRangeRow` + `ValuationTimeSeriesPoint` interfaces match live JSON schema |
| Live JSON inspection T\*=2026-05-22 | Schema ground-truth | `top-level keys`: data_as_of, summary, ranges, time_series; `summary[0]`: S&P 500 with all 7 metrics populated; `ranges[S&P 500]`: list of 7 metric rows with `{metric, label, current, percentile, p10, p25, p50, p75, p90}`; `time_series[S&P 500][trailing_pe]`: `{data: list, thresholds: dict}` with 433 historical points back to 1990-05-31 |
| Lineage map §6.1 cross-check | Field-grain alignment | All 8 summary/ranges metrics present in lineage map; thresholds + time_series shape aligned; **F4 deviation** flagged §5 |

### §3.3 — Open Level-2 questions for TO-004 (Valuation main view)

1. Equity index ticker mapping: Yang's `MSCI World` etc. → YCharts ticker (e.g., `^MSCIWORLD`, `^MSCIACWI`)? Lineage from YALP_MDSRC D2 D3 — re-use prior `ticker_map.py` resolution.
2. Percentile-vs-raw rendering: portal shows percentile rank (0–100) in summary heatmap + ranges panel; YCharts gives raw metric value. Level-2 verdict shape: REPRESENTATIVE if portal-side percentile derived from same metric distribution YCharts surfaces; MATCH if both expose %-ile.
3. P/E methodology bound (trailing vs forward; including/excluding negatives): YCharts vs Bloomberg methodology may differ → REPRESENTATIVE-class flag prepared per PRD §6.

---

## §4 — Component 2: RiskPremiumTab

Endpoint: `/api/general/valuation/risk_premium_data.json` → Producer: `yang-generate-risk-premium` → Upstream: Yang PKL (`data.pkl.return_monthly.pe_ntm` for S&P 500 earnings yield + `data.pkl.price_monthly` 10Y Treasury) for ERP series; FRED cache `cache/fred/BAMLC0A0CM.csv` (IG) + `cache/fred/BAMLH0A0HYM2.csv` (HY) for credit spreads (with Yang PKL Bloomberg OAS fallback — §5.F1).

### §4.1 — Level-1 mapping (RiskPremiumTab)

| Portal field | S3 key | Producer Lambda | Yang upstream | Source field | YCharts endpoint | YCharts field |
|---|---|---|---|---|---|---|
| `data.data_as_of` | json/valuation/risk_premium_data.json | yang-generate-risk-premium | latest date in PKL | derived | n/a — metadata | n/a |
| `data.generated_at` | "" | "" | Lambda run timestamp | derived | n/a — metadata | n/a |
| `data.data_source.erp` | "" | "" | provenance string (Lambda emits "Yang PKL (S&P 500 P/E + 10Y Treasury)") | derived | n/a — provenance label | n/a |
| `data.data_source.credit_spreads` | "" | "" | provenance string (Lambda emits "FRED (ICE BofA BAML Indices)" if count>1000, else "Yang PKL (Bloomberg OAS)") | derived | n/a — provenance label | n/a |
| `data.note` | "" | "" | count summary string | derived | n/a — metadata | n/a |
| `data.erp.data[].date` | "" | "" | monthly merged date | data.pkl merge | n/a — key | n/a |
| `data.erp.data[].value` | "" | "" | **GAP: erp = earnings_yield - treasury_rate** | data.pkl return_monthly.pe_ntm + price_monthly.10Y_Treasury | **GAP — Yang-internal derived** | **GAP — no YCharts equivalent** (per PRD §5 Q1, sourcing/methodology cell explicit) |
| `data.erp.data[].earnings_yield` | "" | "" | **GAP: 100 / pe_ntm** (S&P 500) | data.pkl return_monthly.pe_ntm | **GAP — Yang-derived intermediate** | partial: `/v3/companies/^SPX/historical/earnings_yield` (if YCharts surfaces it directly — TO-002 to probe) |
| `data.erp.data[].treasury_rate` | "" | "" | 10Y Treasury yield | data.pkl price_monthly (10Y key) | FRED proxy: `series/DGS10` OR `series/GS10` | per-series historical value (REPRESENTATIVE — Bloomberg-10Y vs FRED-10Y are independent observations of same underlying) |
| `data.erp.thresholds.{p10,p25,p50,p75,p90}` | "" | "" | distribution percentile thresholds | derived | n/a — derived stat | n/a |
| `data.credit.ig.data[].date` | "" | "" | daily (FRED) or monthly (Yang PKL fallback) date | FRED CSV row date OR data.pkl date | n/a — key | n/a |
| `data.credit.ig.data[].ig_spread` | "" | "" | ICE BofA US Corporate OAS | FRED BAMLC0A0CM (primary) OR data.pkl Bloomberg OAS (fallback) | YCharts FRED-proxy `series/BAMLC0A0CM` OR direct `/v3/economic_indicators/BAMLC0A0CM` | per-series historical value |
| `data.credit.ig.data[].hy_spread` | "" | "" | ICE BofA US High Yield OAS (denormalized into IG array — §5.F3) | FRED BAMLH0A0HYM2 (primary) OR data.pkl Bloomberg OAS (fallback) | YCharts FRED-proxy `series/BAMLH0A0HYM2` OR direct `/v3/economic_indicators/BAMLH0A0HYM2` | per-series historical value |
| `data.credit.ig.thresholds.{p10,p25,p50,p75,p90}` | "" | "" | IG OAS distribution thresholds | derived | n/a — derived stat | n/a |
| `data.credit.ig.current_oas_pct` | "" | "" | latest IG OAS % | derived | n/a — derived stat | n/a |
| `data.credit.ig.current_oas_bps` | "" | "" | latest IG OAS bps | derived | n/a — derived stat | n/a |
| `data.credit.hy.thresholds.{p10,p25,p50,p75,p90}` | "" | "" | HY OAS distribution thresholds | derived | n/a — derived stat | n/a |
| `data.credit.hy.current_oas_pct` | "" | "" | latest HY OAS % | derived | n/a — derived stat | n/a |
| `data.credit.hy.current_oas_bps` | "" | "" | latest HY OAS bps | derived | n/a — derived stat | n/a |

**Coverage summary:**
- Renderable atomic time-series fields: 4 (`erp.value`, `erp.earnings_yield`, `erp.treasury_rate`, `credit.ig.data.ig_spread`, `credit.ig.data.hy_spread`) — wait, that's 5; corrected: 5 renderable time series.
- GAP-class (no YCharts equivalent): `erp.value` (Yang-derived) + `erp.earnings_yield` (Yang-derived; partial YCharts surface tentative TO-002).
- MATCH/REPRESENTATIVE candidates: `treasury_rate` (FRED `DGS10` / `GS10`), `ig_spread` (FRED `BAMLC0A0CM`), `hy_spread` (FRED `BAMLH0A0HYM2`).
- Derived-stat (no YCharts equivalent — local computation): all `thresholds.*` + `current_oas_*` rows.

### §4.2 — Methodology evidence (Component 2)

| Compiler tool / inspection | Use | Finding |
|---|---|---|
| `comp-blast yang-generate-risk-premium` | Lambda blast radius | LAMBDA(3): portal_data_proxy, opal-portal-data-proxy, _build_tmp; S3_ARTIFACT(2): json/valuation/risk_premium_data.json (×2); 5 downstream nodes affected |
| `comp-platinum reverse json/valuation/risk_premium_data.json` | S3 key → producer | Producer node not explicitly named in graph; SERVED VIA: `/api/general/json/valuation/risk_premium_data.json` CF→S3 [AUTH] confirmed; CONSUMERS: no components-found (hook-indirect via `useQuery` in RiskPremiumTab — graph artifact; portal source grep confirmed `RiskPremiumTab → getRiskPremiumData → apiRequest('/api/general/valuation/risk_premium_data.json')`) |
| Portal source grep | Per-field consumer surfacing | `portal/src/pages/Valuation/tabs/RiskPremiumTab.tsx:191-207` ERP_DATA transform + CREDIT_DATA transform; `erp.data[].value/earnings_yield/treasury_rate` rendered in tooltip; `credit.ig.data[].ig_spread/hy_spread` rendered as separate Line series |
| Live JSON inspection T\*=2026-05-22 | Schema ground-truth | `top-level keys`: generated_at, data_as_of, data_source, note, erp, credit; `data_source.erp`: 'Yang PKL (S&P 500 P/E + 10Y Treasury)'; `data_source.credit_spreads`: **'Yang PKL (Bloomberg OAS)'** (fallback fired — §5.F1); `note`: 'Credit spreads: monthly (786 pts). ERP: monthly (437 pts). NO SAMPLING.'; `erp.data` length=437 back to 1990-01-31; `credit.ig.data[0]`: `{date: '2023-05-23', ig_spread: 1.44, hy_spread: 4.6}` (denormalized — §5.F3); `credit.hy.data`: KEY NOT PRESENT (only `thresholds + current_oas_*`) |
| Lambda source grep `infra/aws/lambda/v2_portal/yang_pipeline/valuation/yang-generate-risk-premium/lambda_function.py` | Lambda logic ground-truth | line 8 ERP+IG/HY canonical methodology comment; line 35-36 FRED cache keys; line 67-69 fallback to Yang PKL when FRED unavailable/incomplete; line 93 provenance toggle at `credit_count > 1000` threshold; line 145-244 `calculate_erp_canonical` (`pe_ntm` → earnings_yield = 100/pe_ntm; 10Y Treasury merge; erp = earnings_yield - treasury_rate); line 246+ `calculate_credit_spreads_from_fred` (primary path); line 67-69 `calculate_credit_spreads_from_pkl` (fallback path — Bloomberg OAS monthly) |
| Lineage map §6.2 cross-check | Field-grain alignment | Partial — fallback path (Bloomberg OAS) NOT documented in lineage; `credit.ig.data[]` schema mismatch (denormalized in live JSON, separate-array in lineage); `erp.data[]` extra fields (`earnings_yield + treasury_rate`) not in lineage; **F1+F3+F5 §5** |

### §4.3 — Open Level-2 questions for TO-004 (RiskPremiumTab)

1. **YCharts FRED-proxy vs direct ICE for IG/HY OAS:** lean = FRED-proxy is the cleanest comparator (Bloomberg OAS at fallback time vs FRED-cached ICE BofA — both ultimately ICE-sourced). TO-002 to verify YCharts surfaces the BAMLC0A0CM + BAMLH0A0HYM2 series tickers.
2. **Yang PKL Bloomberg OAS fallback active on T\*=2026-05-22:** Level-2 verdict on `ig_spread/hy_spread` is REPRESENTATIVE-class (Bloomberg OAS vs FRED-cached ICE OAS — both observe same ICE BofA underlying via different vendor pipes); DRIFT-class only if material delta surfaces.
3. **YCharts `earnings_yield` surface for ^SPX:** if YCharts exposes it directly, can validate `erp.data[].earnings_yield` field via REPRESENTATIVE-class; else GAP-class.

---

## §5 — Structural findings (PRD/lineage drift relative to live producer state)

Five findings worth surfacing — none of them blocking TO-001, but candidates for PRD-amendment cycle (CTO surface) + lineage-map update (DS 0.2.0 lineage-owner surface) + /verify-channel BACKSTOP context.

### §5.F1 — PRD §2 + lineage map §6.2 missing fallback path

PRD §2 documents only the FRED-cache path for `credit.ig.data` + `credit.hy.data`. Live `yang-generate-risk-premium/lambda_function.py:67-69` has a fallback: when FRED cache unavailable OR `credit_count <= 1000`, the Lambda calls `calculate_credit_spreads_from_pkl(data_pkl)` which sources Bloomberg OAS monthly from `data.pkl`. **Currently active on T\*=2026-05-22 live JSON** (`data_source.credit_spreads: 'Yang PKL (Bloomberg OAS)'`; `note: Credit spreads: monthly (786 pts)`; 786 <= 1000 threshold gate fires → fallback path active).

Impact: Level-2 verdict on `ig_spread + hy_spread` against YCharts must factor in current-state-Bloomberg-not-FRED. The two series are independent observations of same ICE BofA underlying via different vendor pipes — REPRESENTATIVE-class verdict expected.

Surface to: ws CTO (PRD §2 amendment to include fallback path) + DS 0.2.0 (lineage map §6.2 extension).

### §5.F2 — PRD §2 "Yang monthly ERP fallback" wording misleading

PRD §2 lists `data.pkl Yang monthly ERP fallback` for `yang-generate-risk-premium`. Lambda actually computes ERP only from Yang PKL (no FRED-side ERP path). It's the **primary** ERP source, not a fallback. The "fallback" terminology applies only to credit spreads (§5.F1).

Surface to: ws CTO (PRD §2 wording clarification).

### §5.F3 — Lineage map §6.2 schema mismatch on credit data

Lineage map §6.2 declares:
- `credit.ig.data` — list[{date,value}] — IG OAS daily — FRED BAMLC0A0CM
- `credit.hy.data` — list[{date,value}] — HY OAS daily — FRED BAMLH0A0HYM2

Live JSON 2026-05-22 actually:
- `credit.ig.data[]` — denormalized: each row `{date, ig_spread, hy_spread}` (both spreads in IG array)
- `credit.hy.data` — KEY NOT PRESENT (only `credit.hy.thresholds + current_oas_pct + current_oas_bps`)

Portal source matches live JSON (reads `data.credit.ig.data[].ig_spread + data.credit.ig.data[].hy_spread`); lineage map shows separate arrays = incorrect.

Surface to: DS 0.2.0 (lineage map §6.2 schema correction).

### §5.F4 — Lineage map §6.1 missing thresholds field

Lineage map §6.1 declares `ranges[i][m].thresholds` + `ranges[i][m].values` but does NOT call out `summary[].* percentile` semantic (the summary fields ARE percentile ranks 0-100, not raw values — established empirically: live JSON `summary[0].fwd_pe = 83` = "83rd percentile", not "fwd P/E ratio of 83"). Portal renders accordingly via `formatPercentile`.

This is documented in lineage §6.1 prose ("Percentile rank of pe_ntm (0–100)") but worth calling out the rendering-semantic distinction more explicitly in lineage map.

Surface to: DS 0.2.0 (lineage map §6.1 prose clarification — non-blocking).

### §5.F5 — Lineage map §6.2 missing `erp.data[]` extras + `current_oas_*`

Lineage map §6.2 declares `erp.data` as `list[{date,value,percentile}]`. Live JSON adds `earnings_yield + treasury_rate` (per-row Yang-derived intermediates rendered in RiskPremiumTab tooltip). Lineage map also missing `credit.ig.current_oas_pct + current_oas_bps + credit.hy.current_oas_pct + current_oas_bps` derived stats (not currently rendered, candidates for future-render).

Surface to: DS 0.2.0 (lineage map §6.2 extension).

### §5 — Pattern banking

These five F1-F5 findings together are **6th-fire of `[[self-correction-upstream-of-verify-channel]]` today** (sister to DS 0.2.0 DDB-intermediate / DE 0.4 useTenantLayout / DS 0.1.0~C scribe-consistency / DS 0.1.0~A VolatilityTab / and now ~B credit-spreads-fallback-not-documented). Pattern past MSTR DEFER-PENDING-MULTI-FIRE 3-fire maturation threshold; formal LD-NNNN proposal candidacy lit per CTO message 17:10Z. **Catches fire at TO-001 Phase 1 mapping time** (pre-execution would have been at PRD-authoring-time; this is post-PRD-shipped + pre-Level-2-execution = mapping-substrate-time). Empirical envelope extension — fire site reaches Level-1 mapping evidence-gathering itself.

Sister to ~A's VolatilityTab fire which surfaced a *missing component*; my F1-F5 surface *fallback-path-omission + schema-drift between live producer state and PRD/lineage docs*. Different finding-shape, same pattern.

---

## §6 — Level-2 placeholder (per AC4)

Empty per AC4. TO-004 will populate verdicts (MATCH / REPRESENTATIVE / DRIFT / GAP) per atomic field on T\*=2026-05-22. Anticipated:
- ~30-40% MATCH (`treasury_rate` vs FRED proxy; raw equity metrics if methodology-aligned)
- ~30-40% REPRESENTATIVE (P/E methodology bound, Bloomberg vs FRED OAS, MSCI/Russell vendor variants)
- ~10-15% GAP (Yang-derived ERP + intermediates)
- ~5-10% DRIFT (any material deltas, route per PRD DRIFT rule)

---

## §7 — TO-001 AC scorecard

| AC | Status | Evidence |
|---|---|---|
| AC1 — Every rendered field on both components has a Level-1 row | **MET** | §3.1 + §4.1 — 22 rows Component 1 + 18 rows Component 2 = 40 atomic field rows enumerated |
| AC2 — YCharts-equivalent column is real endpoint+field OR explicit `n/a — <reason>` | **MET** | All 40 rows populated; n/a-reasons span GAP-class (Yang-derived), derived-stat (no equivalent), metadata (provenance/timestamp keys) |
| AC3 — Per-component sub-section documents methodology evidence per field | **MET** | §3.2 + §4.2 — compiler tool findings + portal source grep + live JSON inspection + lineage cross-check per component |
| AC4 — Level-2 table empty placeholder | **MET** | §6 placeholder; TO-004 scope |
| AC5 — Yang ERP GAP-class with sourcing/methodology; ICE BofA OAS rows verify-mapped against YCharts FRED-proxy OR direct ICE | **MET** | §4.1 erp.value row tagged GAP-class with explicit `earnings_yield - treasury_rate` Yang-derived methodology; ig_spread row mapped to YCharts FRED-proxy `series/BAMLC0A0CM` OR direct `/v3/economic_indicators/BAMLC0A0CM`; hy_spread row mapped to `series/BAMLH0A0HYM2` OR `/v3/economic_indicators/BAMLH0A0HYM2`; §5.F1 documents fallback-path active on T\*=2026-05-22 (Bloomberg OAS not FRED) so verdict-class expected REPRESENTATIVE not MATCH |

---

## §8 — Next steps

1. **[ws COO]** RAVC2-Request → disposition (ACCEPT / REWORK).
2. **[ws CTO — optional, non-blocking]** PRD §2 amendment cycle absorbing F1 (fallback path documented) + F2 (ERP-fallback wording corrected). Could fold into next /ws-charter cycle.
3. **[DS 0.2.0 — optional, non-blocking]** Lineage map §6.1 + §6.2 amendment cycle absorbing F3 (denormalized credit array) + F4 (summary percentile semantic) + F5 (erp.data extras + current_oas_* derived stats).
4. **[DS 0.1.0~B — me, next TO]** TO-002 YCharts test-pulls on T\*=2026-05-22 (~1-2h scope; cookie-stale-OK per `dcbc50710` baseline; menachem-bundled cookie per `[[project_ycharts_dedicated_seat_403_session_eviction]]`); per-field probe surface = ~5 renderable atomic time series + ~22 raw equity metric fields (^SPX/^DJI/etc. companies key-stats × 7 metrics). Adapt YALP_MKTOVR §13 pull-harness; flag any 403-session-eviction class hits.
5. **[CVO surface — TO-VAL closeout, future]** /verify-channel project-level mode pass — F1-F5 findings absorbed as banked observations (not blocking project close); pattern-banking entry for sixth-fire empirical reinforcement.

---

## §9 — Footer: pattern-banking

- **6th-fire of `[[self-correction-upstream-of-verify-channel]]`** (today) — fallback-path-omission + schema-drift between live producer state and PRD/lineage docs (§5.F1-F5). Empirical envelope extension to TO-001 Phase 1 mapping evidence-gathering time. Sister to ~A's pre-scaffold VolatilityTab catch.
- **Authority-timeline-cross-fires-during-rapid-revision-cycle 5th-fire candidate** (today) — my respawn cross-fire pattern documented in `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-26/session_yalp_valuat_respawn_reopen_ask.md`. Banked for /govern next-cycle surface alongside MSTR DEFER-PENDING-MULTI-FIRE 3-fire maturation.
- **STANDBY-PREP compression in fast-lane regime** — ~28min wall RESPAWN → REOPEN-ASK → REOPEN+GO crossed-in-transit → TO-001 brief ship. Empirical reinforcement of `[[standby-prep-compress-to-delivery-when-context-sufficient]]`. Spawn-msg + parallel prep-read + crossed-in-transit COO REOPEN combine to flatten wall-time meaningfully under the YALP_MKTOVR ~50min benchmark.
