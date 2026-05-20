# BRIEF: YALP_MDSRC WS-2 — Portfolio Analytics Domain Audit

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` (Portal Market-Data Sourcing Strategy) |
| Workstream | WS-2 — Portfolio Analytics domain |
| Task Order | `YALP_MDSRC.002` |
| Author | `0.2.0_DS_PortfolioAnalytics` |
| Date | 2026-05-20 |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO` (WS-5 synthesis input) |
| Status | COMPLETE — audit deliverable (no code/Terraform/portal change, per PRD v0.2 audit-only) |
| Companion | `mdsrc-ws2-matrix-slice-20260520.tsv` — the WS-2 migration-matrix slice (14-col common schema) |

---

## 1. Executive summary

WS-2 audited the **portfolio-analytics** domain end-to-end: the YCharts analytics capability,
the four portal pages (Factor Tilts, Positioning/Attribution, CMA, the Model Portfolios
analytics surfaces), and the per-surface source classification.

**Headline verdict — the portfolio-analytics domain is the portal's proprietary core, and it
stays proprietary.** Of 13 WS-2 data surfaces:

- **2 are cleanly YCharts-replaceable** — ETF benchmark returns and (with a benchmark-side
  caveat) the index-benchmark legs of the Model Portfolios returns tables. These are public
  ETF / Bloomberg-index total returns.
- **5 are hybrid** — the Model Portfolios benchmark/peer surfaces and the Factor *spread*
  series. Each has a public-market-data leg that YCharts can serve and a proprietary leg
  (Opal model returns, Opal peer-universe construction, Opal factor regressions) that it
  cannot.
- **6 are Bloomberg-pkl-only / proprietary** — all of Factor Tilts' regression output,
  all of Positioning/Attribution, and both CMA surfaces. These are Opal model holdings,
  Opal attribution methodology, and Opal forward-looking assumptions/house views. **No
  YCharts endpoint and no official-API metric can produce them**, because they are not
  market data — they are Opal intellectual property computed from Opal's model portfolios.

**This is the designed outcome, not a coverage failure.** WS-2 is the domain Andrew's
directive flagged as "model portfolio performance ... maybe SmartX" and "proprietary Opal
analytics." The migration end-state for this domain is a *small* automated slice (ETF/index
benchmark returns) layered onto a *retained* proprietary Bloomberg-pkl core. The portfolio-
analytics domain is the answer to the PRD's framing question — "how much of the portal stays
permanently Bloomberg-pkl" — and the answer is: most of WS-2's domain does.

**YCharts analytics catalog is deep but orthogonal.** The 3 MB `all_calc_menu` catalog
carries 3,077 distinct metrics including 287 return metrics, 256 risk metrics, 159 model-
portfolio metrics. YCharts can compute Sharpe (34 variants), beta (89), alpha (88), standard
deviation (106), tracking error (18), max drawdown (31). But every one of those is computed
**against a public security or a YCharts-hosted portfolio** — none of them is Opal's
6-factor-pair tilt regression, Opal's holdings attribution decomposition, or Opal's CMA. The
catalog depth is real and matters for WS-1's market-data domain; for WS-2 it confirms the
*opposite* of replaceability — the metrics exist, but the inputs (Opal model holdings) are
proprietary, so YCharts cannot run them on Opal's models without Opal first replicating its
models inside YCharts.

**Two open questions returned, not pre-decided** (per `<do_not>`): Q1 (official API vs
session-scrape) and Q7 (ToS) — see §7. Both are Andrew calls and gate v0.3, not this audit.

---

## 2. Method & evidence base

| Evidence | Detail |
|---|---|
| HAR | `C:\Users\AndrewBerman\Downloads\ycharts.com.har` (92,608,012 bytes, 1,894 entries). Parsed with `jq` (`.tools/jq.exe`). |
| `all_calc_menu` catalog | **Response body fully captured in the HAR** (3,052,123 bytes) — extracted to `.runtmp/ws2_har/all_calc_menu.json` and parsed directly. WS-2 did NOT need to wait on WS-1's parse; the catalog body was in-HAR. 27 categories, 3,077 distinct metrics. |
| yang Lambda source | 8 WS-2 generator Lambdas under `infra/aws/lambda/v2_portal/yang_pipeline/` — read in full for output shape + input source. |
| Portal surfaces | `portal/src` fetch-path grep (per PRD §5 — comp-blast has no yang->portal edges); `portal/src/api/endpoint-mapping.ts`, `portal-proxy.ts`, and the page components. |
| Pipeline map | `infra/aws/lambda/v2_portal/yang_pipeline/PORTAL_DATA_FLOW.md`. |

**HAR limitation (confirmed, per recon doc §3.4):** of all WS-2 data endpoints, **only
`all_calc_menu.json` has a captured response body.** `scatter_plot_data.json`, `calc_info`,
`metric_sets`, `attribution_contributors_detractors`, `classifications/sectors`,
`model_portfolios/*`, `general_data.json`, `fund_data.json` all show `content.text` empty
(WebInspector did not preserve large bodies). Endpoint paths, methods, status codes, and
request parameters ARE fully captured. Response **schemas** for those endpoints would need a
live probe — which is WAF-gated (see §6). WS-2's classification does **not** depend on those
schemas: the WS-2 verdict is driven by what the *portal* renders (proprietary Opal model
output) vs what YCharts *can* serve (public market data), and that cut is decidable from the
yang Lambda inputs alone.

---

## 3. YCharts capability — the portfolio-analytics endpoints

### 3.1 Analytics endpoints observed in the HAR (ycharts.com web app)

| Endpoint | Method | Observed | Resp size | Data class | WS-2 relevance |
|---|---|---|---|---|---|
| `/charts/scatter_plot_data.json` | POST | 2x | 2,150 B | risk/return metric | Risk-vs-return scatter; params `xAxisMetric`/`yAxisMetric` (observed: `monthly_standard_deviation_annualized_5y`, `annualized_five_year_total_return`) |
| `/calculations/calc_info` | GET | 3x | 424-609 B | metric metadata | Per-metric descriptor lookup |
| `/calculations/metric_sets` | GET | 1x | 5,733 B | metric grouping | Metric-set definitions (PRESENT in HAR — recon doc/PRD §3.3 listed it; confirmed) |
| `static.ycharts.com/calculations/all_calc_menu.*.json` | GET | 4x | **3.05 MB (body captured)** | metric catalog | The full metric dictionary — 3,077 metrics. See §3.2. |
| `static.ycharts.com/calculations/all_calc_menu_labels.*.json` | GET | 5x | 597 KB | metric labels | Display-label sidecar |
| `static.ycharts.com/calculations/index_calc_menu.*.json` | GET | 3x | 164 KB | index metric catalog | Index-specific metric subset |
| `static.ycharts.com/calculations/aggregate_calc_menu.*.json` | GET | 1x | — | aggregate metric catalog | Portfolio-aggregate metric subset |
| `/securities/attribution_contributors_detractors/{ticker}` | GET | 1x | 3,709 B | attribution | **INDEX contributors/detractors** (observed: `^DJI`) — NOT portfolio holdings attribution; see §5.2 |
| `/classifications/sectors.json` + `/classifications/sectors` | GET | 2x | 9.8 KB / 61 KB | classification | GICS-style sector taxonomy |
| `/model_portfolios/` | GET | 2x | 6,343 B | model portfolio | YCharts-hosted model-portfolio list/detail |
| `/model_portfolios/list/` | GET | 2x | 61 KB | model portfolio | Model-portfolio library |
| `/model_portfolios/collection_status` | GET | 2x | 3,334 B | model portfolio | — |
| `/model_portfolios/transition_analysis/list` | GET | 7x | 2 B (empty array) | model portfolio | Transition analysis (none configured in captured session) |
| `/data_templates/library_menu/model_portfolio` | GET | 2x | — | model portfolio | Model-portfolio template menu |
| `/dashboard/fund_chart_module_data/{id}` | GET | 8x | 79 B | chart module | Dashboard chart modules |
| `/charts/general_data.json` | GET | 4x | 250-276 B | time series | Multi-security time series (params: `securities`, `metrics`, `startDate`/`endDate`, `resampleFrequency`) |
| `/charts/fund_data.json` | GET | 3x | 10-44 KB | time series | Fund/ETF time series |

The `model_portfolios/*` endpoints belong primarily to **WS-3** (model-portfolio performance
sourcing) — see §8 seam. WS-2 records them here for completeness.

### 3.2 The `all_calc_menu` catalog — 3,077 metrics (Q5 evidence)

The catalog body was fully captured. 27 categories; WS-2-relevant slices:

| Category | Metric count | WS-2 use |
|---|---|---|
| Returns and Performance | 287 | Full return ladder: `mtd/qtd/ytd/1m/3m/6m/1y/3y/5y/10y/15y/20y` price & total returns, annualized variants |
| Risk | 256 | `market_alpha`/`market_beta` at 12/36/60/120/180/240-month windows, `rsquared_*`, quarterly variants |
| Means and Medians | 93 | Cross-sectional aggregates |
| Relative Metrics | 48 | `relative_*_market/sector/industry` |
| Model Portfolio Specific | 159 | `*_total_monthly_return_max_fee`, tax-adjusted variants, `drift`, ESG scores |
| Asset Allocation Metrics | 15 | `*_stock/bond_allocation_generic`, cap-tier, credit-grade allocations |
| SMA Specific | 122 | `net_max_fee_return_index`, SMA return ladder |
| Fund/ETF Specific | 1,375 | ETF metric universe |

**Coverage probe — keyword presence in catalog internal_names:**

| Metric concept | Variants in catalog |
|---|---|
| `sharpe` | 34 | `sortino` | 29 | `standard_deviation` | 106 |
| `tracking_error` | 18 | `information_ratio` | 20 | `correlation` | 18 |
| `max_drawdown` | 31 | `downside` | 79 | `treynor` | 67 |
| `calmar` | 28 | `market_beta` | 89 | `market_alpha` | 88 | `rsquared` | 18 |

**Gaps found:** `capture_ratio` (upside/downside capture) returned **0** matches under that
name — a minor catalog gap to note for any surface that renders capture ratios (none of the
WS-2 portal surfaces currently do).

**The Q5 finding for WS-2 is a paradox worth stating plainly:** YCharts' analytics catalog is
*more* extensive than anything the WS-2 portal pages render. Coverage of the *metric
vocabulary* is effectively complete. But **catalog coverage is not surface replaceability**
for this domain — every WS-2 proprietary surface (factor tilts, attribution, positioning,
CMA) is computed from **Opal model holdings**, and YCharts can only run its 3,077 metrics on
(a) public securities or (b) portfolios constructed inside the YCharts platform. Opal's
models are neither. The catalog depth is decisive evidence for WS-1's market-data domain; for
WS-2 it confirms the proprietary classification rather than weakening it.

### 3.3 Official YCharts Data API (AC5 / Q1 — input, NOT pre-decided)

The HAR captured the YCharts **web application** (Django session-cookie auth — see §6). YCharts
separately markets an **official Data API product** (key-authenticated). For the WS-2 data
classes specifically:

- The official API can plausibly serve **security/fund/ETF/index metrics** — the return and
  risk metrics in §3.2 — for **public securities**, on the same metric vocabulary. This would
  cover the YCharts-replaceable WS-2 surfaces (ETF returns, index-benchmark legs).
- The official API **cannot** produce Opal's proprietary surfaces regardless of tier — they
  are not market data (§4, §5).
- Whether the official API exposes the **model-portfolio** analytics endpoints for
  *user-created* portfolios, and whether Opal's subscription includes API entitlement at all,
  **cannot be determined from the HAR** (the HAR is browser traffic; an API entitlement
  leaves no web trace). This is **Q1** — an Andrew/CTO business call at v0.3. WS-2 does not
  pre-decide it and records no rate-limit or pricing claim (none is evidenced).

---

## 4. Portal surfaces — the WS-2 pages

Serving path for all WS-2 pages (Phase-1 compiler mandate — see §9): CloudFront
`/api/general/*` and `/json-tiered/*` -> S3 `opal-data-portal-v2` via the `public-data-router`
Lambda@Edge (rewrites `/api/general/X` -> `/json/X`).

### 4.1 Factor Tilts (`/factor-tilts`)

`yang-generate-factor-tilts` (model_pkl, weekly) writes a 3-tier output:

| Tier artifact | Content | Component |
|---|---|---|
| `json/factor-tilts/tier1-snapshot.json` (~46 KB) | `summary` (per model/window regression: r2, alpha, 6 factor betas), `factorTiltsByWindow`, `aggregateTilts` | `FactorTilts.tsx` (page mount) + `FactorTiltBarsTab` |
| `json/factor-tilts/tier2-spreads.json` (~196 KB) | `factorSpreads` — market factor-spread series (current / 30d avg/min/max / 504-day series) | `FactorTiltTimeSeriesTab` ("Factor Spreads" tab) |
| `json/factor-tilts/tier3-timeseries.json` (~2.1 MB) | `timeSeries` (market factor-spread history) + `modelTiltTimeSeries` (per-model rolling-regression history) | Time Series toggle |

**Data nature.** The Lambda is a **reshaper, not a compute** — `model_pkl` already contains
`summary` (regression results), `factor_spread`, and `regression` (per-model/window rolling
regressions). The factor analysis is done **upstream in Yang's Bloomberg workflow**. The 6
factor pairs are a fixed Opal taxonomy: `Equity vs FI`, `Growth vs Value`, `US vs Foreign`,
`Large vs Small`, `Agg vs Short`, `HY vs Agg` — regressed against the 5 Opal model portfolios
(`UST/ST/INT/LTC/LTA`).

**Classification.** The regression output (tilts, betas, r2, alpha) is **proprietary** —
YCharts has CAPM single-factor `market_alpha`/`market_beta` vs *one* benchmark, not a custom
6-factor-pair decomposition of private models. The **`factorSpreads` / `timeSeries`** series
are the *market* factor spreads themselves (e.g. a Growth-index-minus-Value-index spread) —
those are **reconstructable** from YCharts index pairs, so they are **hybrid** (the spread
inputs are public; the current source is the proprietary pkl). `modelTiltTimeSeries` is
proprietary regression output.

### 4.2 Positioning (`/positioning`) and Attribution (`/attribution`)

Note: the portal renders the PRD's "Positioning" page #3 as **two** pages — `Positioning` and
`Attribution` — both consuming the same three artifacts. Both are in WS-2 scope.

| Artifact | Producer | Source | Cadence | Content |
|---|---|---|---|---|
| `json/positioning/positioning_data.json` (gzip) | `yang-generate-positioning` | model_pkl | weekly | Per-model holdings, allocation (cash/fixed_income/equity/hedge), benchmark allocation, allocation spread |
| `json/positioning/holdings_attribution_data.json` | `yang-generate-holdings-attribution` | attribution_excel | monthly | Per-portfolio per-period (QTD/YTD/1Y/SI) holdings with `asset_class`, `sub_asset_class`, `total_attribution`; asset-class subtotals carry Fund Selection / Style Allocation / Asset Allocation effects |
| `json/positioning/allocation_summary.json` (gzip) | `yang-generate-allocation-summary` | reads `holdings_attribution_data.json` | weekly | Per-model per-period asset-class `style_weight`, `policy_weight`, `bet`, `asset_allocation`, `total` |

Components: `Positioning.tsx`/`Attribution.tsx`, `HoldingsTab`, `SelectionTab`,
`PositioningSummary`, `AssetAllocationSummary`, `StylePolicyComparison`, `AllocationHeatmap`.

**Classification — all three are Bloomberg-pkl-only / proprietary.** Every field is derived
from **Opal model portfolio holdings** (model_pkl) and **Opal's attribution workbook**
(attribution_excel). `policy_weight` is an Opal mandate (`BENCHMARK_ALLOCATIONS` hard-coded
per model); `style_weight` is the actual Opal model allocation; the attribution effects are
Opal's Brinson-style decomposition. YCharts' `attribution_contributors_detractors` endpoint
(§5.2) is a *security-index* contributors view — a different thing entirely. **No migration
candidate.**

### 4.3 Capital Market Assumptions (`/cma`)

`yang-generate-cma` processes **two** Excel uploads:

| Artifact | Source upload | Content | Tab |
|---|---|---|---|
| `json/capital-markets/assumptions.json` | `cma_excel` ("CMA Official YYYY.xlsx") | Per-asset-class 10-year `expectedReturn` + `expectedVolatility` | "Expectations" |
| `json/capital-markets/views.json` | `saa_excel` ("Opal SAA YYYYMMDD v2.xlsx") | Opal Strategic & Tactical asset-allocation views (Strong UW -2 ... Strong OW +2) for asset-class pairs / FI / equity | "Views" |

Component: `CapitalMarketAssumptions.tsx` (fetches `getCMAAssumptions` + `getOpalViews`).

**Classification — both are proprietary, definitionally.** CMA is Opal's **forward-looking**
10-year return/volatility methodology; SAA/TAA views are Opal's **house views**. Neither is
market data — there is no historical series to pull. YCharts has no equivalent. **Permanently
manual** (Q6 answered for `cma_excel`).

### 4.4 Model Portfolios page (`/model-portfolios`) — WS-2 analytics surfaces

`ModelPortfolios.tsx` has 3 tabs: `growth | performance | peers`.

- **`growth` tab** — AUM metrics + account distribution. **WS-3 domain (client/AUM data) — out of WS-2 scope.**
- **`performance` tab** — fetches `getModelPortfolioBenchmarks()` + `getETFBenchmarkReturns()`.
- **`peers` tab** — fetches `getPeerPerformance()` -> `PeersTab`.
- `ReturnVolatilityScatter.tsx` — fetches `getModelPortfolioTimeseries()` (risk/return scatter).

`yang-model-portfolio-benchmarks` (data_pkl, weekly) is the **consolidated producer** of
three artifacts (see §6.4 staleness note):

| Artifact | Content |
|---|---|
| `json/benchmarks/benchmark_returns.json` | Legacy format — per model, per period: `model` return, `benchmark` (= index benchmark), `spread`, volatilities |
| `json/benchmarks/model_portfolio_benchmarks.json` | Comprehensive — per model, per period: `model`, `index_benchmark`, `etf_benchmark` returns + `index_spread`/`etf_spread` + all three volatilities |
| `json/benchmarks/model_portfolio_timeseries.json` | Daily rows `{date, model_code, model_return, benchmark_return, rfr}` |

`yang-generate-etf-returns` (model_pkl, weekly) -> `json/benchmarks/etf_returns.json` — period
returns for 5 benchmark ETFs (BIL, VGSH, AGG, IVV, ACWI).

`yang-generate-peer-performance` (peer_excel, monthly) -> `json/peers/peer_performance.json` —
per model, per period: peer percentiles (p5/p25/p50/p75/p95), `model` return, `benchmark`.

**Classification — hybrid, and this IS the WS-2/WS-3 seam (§8):**

- **Index-benchmark + ETF-benchmark returns** (the `index_benchmark`, `etf_benchmark`,
  `etf_returns.json`, and `rfr` legs) are **public market data — YCharts-replaceable.** The
  Bloomberg-index blends ("85% Bloomberg Agg / 15% MSCI ACWI") and the ETF blends are
  composed from public constituents; the constituent index/ETF total returns and the Treasury
  `rfr` are exactly what YCharts serves. The blend *weights* are an Opal mandate but trivially
  re-applied.
- **Model returns** (`model`, `model_return`, `model_volatility`, `index_spread`,
  `etf_spread`) are **Opal model-portfolio performance** — the WS-3 sourcing question
  (YCharts `/model_portfolios/*` vs SmartX vs `model.pkl`).
- **Peer percentiles** in `peer_performance.json` are an Opal/Yang-constructed **peer
  universe** distribution — YCharts has `*_vs_category` / `*_vs_pg` peer-group metrics, but
  matching them to Opal's exact peer universe is unverified; treat as **partial**.

So `etf_returns.json` is the one cleanly **YCharts-replaceable** surface; the benchmark/peer
tables are **hybrid** — benchmark legs migratable, model legs are the WS-3 seam.

---

## 5. Q6 — `peer_excel` / `attribution_excel` / `cma_excel`: sourceable or permanently manual?

This is the WS-2 TO's sharpest question. Answer, with evidence:

### 5.1 `cma_excel` (+ `saa_excel`) -> CMA assumptions & Opal views — **PERMANENTLY MANUAL.**
Opal's forward-looking 10-year CMA and house SAA/TAA views are intellectual property, not
market data. No vendor — YCharts included — sells Opal's own assumptions back to Opal. No
candidate endpoint. Note: `saa_excel` is a manifest file-type **not listed in PRD §2.1**
(which lists `cma_excel`, `peer_excel`, `attribution_excel`, `regression_csv`) — see §6.4.

### 5.2 `attribution_excel` -> holdings attribution — **PERMANENTLY MANUAL (proprietary).**
`holdings_attribution_data.json` is a Brinson-style decomposition (Fund Selection / Style
Allocation / Asset Allocation effects) of **Opal model holdings vs an Opal policy benchmark**.
YCharts' `/securities/attribution_contributors_detractors/{ticker}` is **not** an equivalent —
it returns the top contributors/detractors *within a public index* (observed: `^DJI`), i.e. a
security-level decomposition of an index, not a portfolio-vs-benchmark Brinson attribution of
a privately-managed model. Different artifact, different purpose. YCharts cannot produce
Opal's holdings attribution because it does not hold Opal's model holdings or Opal's policy
benchmark definitions. **Permanently manual** unless Opal replicates its models inside the
YCharts model-portfolio feature (a workflow change, not a data pull — flagged for WS-5).

### 5.3 `peer_excel` -> peer performance — **HYBRID / mostly manual.**
`peer_performance.json` has two parts. The **model returns** within it are Opal model
performance (WS-3 seam). The **peer percentile distribution** (p5-p95) is a peer-universe
construction. YCharts *does* carry peer-group analytics (`market_alpha_Xy_vs_pg`,
`rsquared_Xy_vs_category`, and category percentile metrics). **But** whether YCharts'
category/peer-group universe matches the peer universe Yang uses in the "Models Performance vs
Peers" workbook is **unverified** and likely divergent (Opal's peer set is curated to its
model mandates). Verdict: **partial** YCharts coverage; the surface stays manual unless WS-5
+ Andrew accept YCharts' peer-group definition as the peer universe — a methodology decision,
not a feasibility one.

**Q6 summary:** all three Excel-fed surfaces are proprietary or methodology-bound. `cma_excel`
and `attribution_excel` are **permanently manual**. `peer_excel` is **hybrid** — the peer
distribution *could* be YCharts-sourced only if Opal adopts YCharts' peer-group taxonomy.

---

## 6. Shared YCharts auth / WAF finding (PRD §4 — recorded for WS-3/WS-4; no re-probe)

WS-2 did **not** independently re-probe the auth layer (PRD §4 — "do not triplicate"). The
auth mechanism is taken from the recon doc-of-record (`3987616d8` §3.3) and confirmed against
the HAR headers:

- Auth is **Django session cookie** (`ycsessionid`) + **CSRF** (`csrftoken` cookie +
  `x-csrftoken` header) + **AWS WAF challenge token** (`aws-waf-token`; the HAR shows 102
  hits to `*.edge.sdk.awswaf.com`, host `fdb400f6cad7.edge.sdk.awswaf.com`). **Zero**
  `Authorization` headers on any `ycharts.com` data call.
- **Implication for WS-2 live-probing:** filling the §3.1 response schemas (`scatter_plot_data`,
  `calc_info`, etc.) requires a logged-in, WAF-cleared browser session — i.e. the Playwright-
  capture path WS-4 designs. WS-2's classification did not require it (see §2). If WS-5 wants
  the analytics response schemas pinned, that is a live-probe task gated on the WS-4 capture
  mechanism — recommend it be folded into v0.3, not Phase 0.
- This is the same finding WS-1 will hit; WS-2 contributes the corroboration, not a fourth
  probe. WS-4 consumes it for Q2/Q3.

**WS-1 shared-probe results (MCP `20260520T211916Z` — consumed, not re-probed):** WS-1
reached the auth layer first and replayed the captured HAR cookie bundle ~5.5h post-capture.
Three findings materially affect the WS-2 operational picture:

1. **AWS WAF does NOT block headless replayed-token requests.** `curl` carrying the captured
   `aws-waf-token` returned HTTP 200 + JSON. The WAF gates *initial token acquisition* only
   (needs a real browser once); a captured token then works headless. Lowers the WS-4
   capture-mechanism risk (Q3) — but see below.
2. **YCharts enforces a SINGLE CONCURRENT SESSION.** Mid-probe WS-1's session died with HTTP
   403 *"You have been signed out due to a concurrent sign in using your credentials."* **A
   programmatic pull on a shared YCharts seat is mutually evicted with any human user of that
   seat.** For WS-2 this is decisive on the operational shape: a daily automated analytics
   pull cannot share a seat with a YCharts analyst — it forces either a **dedicated
   integration seat** or the **official Data API**. This is a direct input to Q1 and is
   flagged in the matrix slice `notes` for every migration-candidate row.
3. **Feature/endpoint access is plan-tier gated.** WS-1 saw `/classifications/sectors.json`
   return 403 *"You don't have access to this feature"*. The WS-2 analytics endpoints
   (`scatter_plot_data.json`, `/calculations/*`) **may or may not be in the current seat's
   tier** — unverified. Treat tier-gating of the analytics endpoints as an **open risk**: any
   v0.3 plan that depends on the session-scrape path for WS-2 surfaces must first confirm the
   seat tier includes them. (Does not affect the proprietary classifications — those have no
   YCharts endpoint regardless of tier.)

### 6.4 Pipeline-mechanism findings (deltas surfaced during the audit)

Recorded as findings per the Phase-1 `<if_mismatch>` mandate; none change a classification.

1. **`yang-generate-benchmark-returns` source absent.** The Step Functions definition
   (`yang-pipeline-definition.json`) has a `GenerateBenchmarkReturns` state ->
   `arn:...:function:yang-generate-benchmark-returns`, but **no source directory exists** for
   it under `v2_portal/yang_pipeline/`. The actual producer of `benchmark_returns.json` is
   `yang-model-portfolio-benchmarks` (its docstring is even titled "Generate Benchmark Returns
   Lambda" and it writes all three benchmark artifacts). Either the SFN state is orphaned/
   legacy or there is source/deploy drift. **Flag to AE 0.5.0 (yang-pipeline consult) +
   WS-5.** Audit-only — not fixed here.
2. **`saa_excel` is an undeclared manifest field.** `yang-generate-cma` consumes both
   `cma_excel` and `saa_excel`, but PRD §2.1 and `PORTAL_DATA_FLOW.md` list only `cma_excel`.
   The Opal SAA Views surface depends on `saa_excel`. WS-5 should add it to the manifest
   inventory.
3. **`PORTAL_DATA_FLOW.md` CMA path stale.** The doc says CMA writes `json/cma/*.json`; the
   Lambda actually writes `json/capital-markets/*.json`. `endpoint-mapping.ts` is correct
   (`capital-markets/`) and self-documents the discrepancy.
4. **`endpoint-mapping.ts` peer path stale.** Line 83 maps peer performance to
   `/api/general/benchmarks/peer_performance.json`, but the live fetch in `portal-proxy.ts`
   (`getPeerPerformance`) uses `/api/general/peers/peer_performance.json`, matching the Lambda
   output key `json/peers/peer_performance.json`. The `endpoints` block entry is stale; the
   actual call is correct.
5. **Serving-path delta vs PRD §5.** PRD §5 anchored the serving path as `/api/public/json*`.
   The live CloudFront behaviors (`comp-routes behaviors`) and `endpoint-mapping.ts` both show
   `/api/general/*` + `/json-tiered/*` via `public-data-router`. The *router and origin are
   as PRD §5 states*; only the path prefix differs (`general`, not `public`). Matrix
   `serving_path` column uses the live `/api/general/...` prefix.

---

## 7. Open questions returned (NOT pre-decided — per `<do_not>`)

| Q | WS-2 position |
|---|---|
| **Q1** — official API vs session-scrape | Returned open. Official API *could* serve the 2 YCharts-replaceable + the benchmark legs of the 5 hybrid surfaces; it changes nothing for the 6 proprietary surfaces. **WS-1's single-concurrent-session finding (§6) pushes hard toward the official API or a dedicated seat** — a shared-seat scrape is operationally non-viable for a daily pull. Andrew/CTO call at v0.3. |
| **Q5** — catalog coverage | Answered: YCharts catalog coverage of the *metric vocabulary* is effectively complete (§3.2), but it is **orthogonal** to WS-2 replaceability because the proprietary surfaces' inputs (Opal model holdings) are not YCharts-resident. Minor named gap: `capture_ratio`. |
| **Q6** — peer/attribution/cma sourceability | Answered §5: `cma_excel` + `attribution_excel` permanently manual; `peer_excel` hybrid/methodology-bound. |
| **Q7** — ToS / licensing | Surfaced, not adjudicated. Programmatic extraction from a YCharts *seat* (the session-scrape path) carries ToS exposure; the official API path would be contractually clean. Andrew business call. |

---

## 8. WS-2 <-> WS-3 Model Portfolios seam (AC6)

Coordination opened with `0.4.0_DS_ClientPlatform` — MCP `20260520T210045Z` (CC'd WS-1's
schema thread). The agreed cut:

- **WS-2 owns** the Model Portfolios **analytics/benchmark** surfaces: index-benchmark
  returns, ETF-benchmark returns, benchmark volatilities/spreads, the peer-percentile
  distribution, the risk/return scatter axes.
- **WS-3 owns** model-portfolio **performance sourcing**: the `model` / `model_return` /
  `model_volatility` numbers embedded in `benchmark_returns.json`,
  `model_portfolio_benchmarks.json`, `model_portfolio_timeseries.json`, and
  `peer_performance.json` — the question of whether they come from `model.pkl`, SmartX, or
  YCharts `/model_portfolios/*`.
- **Open item put to WS-3:** `model_portfolio_timeseries.json` — WS-2's read is that the
  `model_return` column is WS-3 and the `benchmark_return` + `rfr` columns are WS-2/WS-1;
  awaiting WS-3 confirmation.
- The `growth` tab of the Model Portfolios page (AUM / account distribution) is **entirely
  WS-3** — WS-2 does not audit it.

No surface is dropped and none is double-classified: the matrix slice marks the hybrid Model
Portfolios rows with a `notes` seam flag pointing at WS-3 for the model-return leg. WS-5
reconciles the two slices.

---

## 9. Compiler Tools

| Phase | Mandate `<run>` | Observed result | vs `<expect>` |
|---|---|---|---|
| 1 | `comp-routes behaviors` | 23 CloudFront behaviors. Behaviors 14-16: `/api/general/json-tiered/*`, `/json-tiered/*`, `/api/general/*` -> S3 `opal-data-portal-v2-json` via `public-data-router` (origin-request) + `cache-control-injector` (origin-response). | **PARTIAL MATCH.** Router + origin exactly as PRD §5. Path prefix is `/api/general/*` not the PRD's `/api/public/json*`. Recorded as finding §6.4(5); matrix `serving_path` uses the live prefix. |
| 1 | yang->portal map via `PORTAL_DATA_FLOW.md` + `portal/src` fetch grep (NOT comp-blast) | `PORTAL_DATA_FLOW.md` + grep of `endpoint-mapping.ts`/`portal-proxy.ts`/page components produced the full surface map (§4). | MATCH. comp-blast correctly not used (PRD §5 — no yang->portal edges). `PORTAL_DATA_FLOW.md` staleness recorded §6.4(1-3). |
| 1 | YCharts side — no comp-* applicability (external system) | Evidence = HAR `jq` parse + the in-HAR `all_calc_menu` body. | MATCH — documented-none per PRD §5. |
| 2 | none (audit deliverable, no code) | No `.py` written — no `py_compile`/`ruff`/`ds-precommit` gate applies. | MATCH — documented-none. |
| 3 | none (matrix slice is self-validation) | Matrix slice completeness checked against AC1-AC7. | MATCH — documented-none. |

`comp-routes` run auto-logged to `org/compiler-tools-log.md` via `.comp-graph/.agent_context`.

---

## 10. WS-2 migration-matrix slice

Common 14-column schema (agreed with WS-1, MCP `20260520T210037Z`). Machine-parseable TSV:
`docs/briefs/mdsrc-ws2-matrix-slice-20260520.tsv`. Markdown rendering:

| surface_id | portal_page | component | surface | json_artifact | current_source | data_class | ycharts_coverage | classification |
|---|---|---|---|---|---|---|---|---|
| WS2-FT-01 | Factor Tilts | FactorTilts.tsx / FactorTiltBarsTab | Factor tilt snapshot (per-model/window regression betas, r2, alpha) | json/factor-tilts/tier1-snapshot.json | model_pkl | factor | none | proprietary |
| WS2-FT-02 | Factor Tilts | FactorTiltTimeSeriesTab | Market factor-spread series (current/30d/504d) | json/factor-tilts/tier2-spreads.json | model_pkl | factor | partial | hybrid |
| WS2-FT-03 | Factor Tilts | FactorTilts Time Series toggle | Factor-spread history + per-model rolling-regression history | json/factor-tilts/tier3-timeseries.json | model_pkl | factor | partial | hybrid |
| WS2-POS-01 | Positioning | Positioning.tsx / PositioningSummary | Model holdings + allocation + benchmark spread | json/positioning/positioning_data.json | model_pkl | holdings/allocation | none | Bloomberg-pkl-only |
| WS2-POS-02 | Positioning / Attribution | AssetAllocationSummary / StylePolicyComparison | Allocation summary (style/policy weight, bet, attribution) | json/positioning/allocation_summary.json | model_pkl (via attribution) | attribution | none | proprietary |
| WS2-POS-03 | Attribution | HoldingsTab / SelectionTab / AllocationHeatmap | Holdings attribution (Fund Selection / Style / Asset Allocation effects) | json/positioning/holdings_attribution_data.json | attribution_excel | attribution | none | proprietary |
| WS2-CMA-01 | CMA | CapitalMarketAssumptions.tsx | 10Y expected return + volatility per asset class | json/capital-markets/assumptions.json | cma_excel | assumptions | none | proprietary |
| WS2-CMA-02 | CMA | CapitalMarketAssumptions.tsx | Opal Strategic/Tactical allocation views | json/capital-markets/views.json | saa_excel | views | none | proprietary |
| WS2-MP-01 | Model Portfolios | ModelPortfolios.tsx (performance tab) | Benchmark returns table (legacy: model + index benchmark + spread) | json/benchmarks/benchmark_returns.json | data_pkl | metric | partial | hybrid |
| WS2-MP-02 | Model Portfolios | ModelPortfolios.tsx (performance tab) | Comprehensive benchmark table (index + ETF benchmark, spreads, volatilities) | json/benchmarks/model_portfolio_benchmarks.json | data_pkl | metric | partial | hybrid |
| WS2-MP-03 | Model Portfolios | ReturnVolatilityScatter.tsx | Daily model/benchmark return + rfr series (risk/return scatter) | json/benchmarks/model_portfolio_timeseries.json | data_pkl | metric/risk | partial | hybrid |
| WS2-MP-04 | Model Portfolios | ModelPortfolios.tsx (performance tab) | ETF benchmark period returns (BIL/VGSH/AGG/IVV/ACWI) | json/benchmarks/etf_returns.json | model_pkl | ETF | full | YCharts-replaceable |
| WS2-MP-05 | Model Portfolios | PeersTab | Peer performance (p5-p95 percentiles + model + benchmark) | json/peers/peer_performance.json | peer_excel | metric/peer | partial | hybrid |

**Slice tally:** YCharts-replaceable 1 · hybrid 5 · proprietary 5 · Bloomberg-pkl-only 1
(`Bloomberg-pkl-only` and `proprietary` are both "stays manual"; split only by whether the
artifact is methodology IP vs raw Opal model state). **Stays-manual total: 7 of 13.**

---

## 11. Recommendation to WS-5 (synthesis input — not a v0.3 decision)

1. **The portfolio-analytics domain is the proprietary core.** Plan the migration end-state
   as: automate `etf_returns.json` and the **benchmark legs** of the Model Portfolios tables
   (index + ETF benchmark returns + rfr) onto a daily YCharts pull; **retain Bloomberg-pkl /
   Excel** for Factor Tilts, Positioning, Attribution, CMA, and the model-return legs.
2. **The Bloomberg-pkl upload does not shrink much for WS-2.** `model_pkl` still feeds Factor
   Tilts + Positioning; `cma_excel`/`saa_excel`/`attribution_excel`/`peer_excel` all stay.
   The automation win in this domain is narrow and concentrated on the Model Portfolios
   benchmark surfaces.
3. **Resolve the seam with WS-3 before v0.3** — the hybrid Model Portfolios rows (MP-01/02/03/05)
   are only "hybrid" because they bundle a benchmark leg (WS-2, migratable) with a model-return
   leg (WS-3). v0.3 should either split the artifacts or accept the hybrid producer.
4. **Flag the `yang-generate-benchmark-returns` source gap** (§6.4-1) to AE 0.5.0 before any
   v0.3 implementation touches the benchmark Lambdas.
5. **If Andrew wants Opal analytics *inside* YCharts** — the only path to YCharts-computed
   attribution/tilts is to replicate Opal's model holdings into the YCharts model-portfolio
   feature. That is a workflow + IP-exposure decision, not a data-sourcing one; WS-5 should
   surface it as such, not as a migration candidate.

---

## Appendix — HAR parse method

- `jq` (`.tools/jq.exe`) over `ycharts.com.har`: host histogram, endpoint enumeration
  (method + path + status + response size + body-capture flag), `scatter_plot_data` request
  param extraction, `all_calc_menu` body extraction (3.05 MB, in-HAR) + category/metric parse.
- Working files under `.runtmp/ws2_har/` (transient, not committed).
- Limitation: response bodies for the non-catalog WS-2 endpoints not captured (§2) — does not
  affect the WS-2 classification, which is decided on the portal/yang input side.
