# FRED Macro-Sourcing Audit — Macroeconomics Portal Page

| Field | Value |
|---|---|
| Task Order | YALP_MDSRC.F1 (dsa-macro-page-input-audit-and-fred-exploration) |
| Project | YALP_MDSRC |
| Author | 0.2.0_DS_PortfolioAnalytics~A |
| Date | 2026-05-20 |
| Issued by | 2.0.0_SA_COO (Andrew-direct) |
| Audience | 1.0.0_SA_CTO (v0.4 amendment input) / COO (RAVC) |
| Companion | `docs/briefs/mdsrc-fred-macro-mapping-20260520.tsv` (machine-readable 79-row mapping table) |
| Scope | AUDIT ONLY — no code/Terraform/portal change authored (PRD v0.2) |

---

## 1. Executive summary

The portal Macroeconomics page consumes **4 JSON artifacts** behind **4 components**. The
dominant artifact — `macro_data.json`, 79 indicators in 12 groups — is today sourced entirely
from the manual Bloomberg `data_pkl`. Two of the other three artifacts are **already on FRED**
(the yield-curve overlay; the VIX half of volatility).

Headline verdict, quantifying the v0.3 WS1-MAC-01 "Bloomberg-leaning hybrid" call:

- **Of the 79 served macro indicators: 50 (63%) are cleanly FRED-replaceable** — 33 are the
  identical official series on FRED (BLS/BEA/Census/Fed/Treasury/DOL/UMich), 17 need only a
  FRED-native `units=` transform (no custom math).
- **+6 (8%) have a FRED proxy** that is close but not identical (ICE-BofA credit spreads vs
  Bloomberg index OAS; trade-weighted dollar vs ICE DXY; onshore vs offshore yuan).
- **23 (29%) are genuine non-FRED residue** — licensed survey data or proprietary indices.
- FRED-replaceable fraction: **63% clean / 71% if proxies are accepted / 29% hard residue.**

The residue is not scattered — it concentrates in **two entire groups**: Leading Indicator
(8/8 licensed survey: ISM, S&P Global PMI, Conference Board LEI, NFIB) and Investor Sentiment
(7/7 licensed/proprietary: AAII x6, Fed NLP). Those two groups are 15 of the 23 residue rows.
The other 8 are individually-named (Bloomberg FCI, ADP, Conf Board Consumer Confidence, NAHB,
NAR Pending Home Sales, UMich 5-10yr, Ted Spread, Bloomberg Agg OAS).

FRED is a strong fit for this page: the existing VIX and yield-curve integrations prove the
mechanism, the official API computes the MoM/YoY/QoQ transforms server-side, and a full daily
refresh of all 50 FRED-replaceable indicators is ~50 requests — well inside the 120-req/min
rate limit. The implementation (a later TO) is low-risk and pattern-identical to
`ingest_yield_curve_fred.py` which already exists.

---

## 2. PHASE 1 — Macroeconomics page input map

### 2.1 Page structure

Page: `portal/src/pages/Macroeconomics/Macroeconomics.tsx`. Four components:

| # | Component | Role | Artifact consumed |
|---|---|---|---|
| 1 | `panels/MacroHeatmap.tsx` | "Macroeconomic Indicators" heatmap (always shown) — 12 groups, value/position toggle | `macro_data.json` |
| 2 | `tabs/YieldCurveTab.tsx` | Tab 1 (default) — Treasury yield curve, current/1M/1Y snapshots | `macro_data.json` (Treasury Yields group, current+1M) **and** `yield_curve_fred.json` (1Y-ago overlay) |
| 3 | `tabs/VolatilityTab.tsx` | Tab 2 — VIX + MOVE gauge, AI summary, historical chart | `volatility_data.json` |
| 4 | `components/MacroTimeSeriesModal.tsx` | Drill-down modal (click any heatmap indicator) | `macro/timeseries/{slug}.json` (per-indicator) |

### 2.2 The 4 artifacts — structured inventory

| Artifact | Serving path | S3 key | Producer | Source today | Refresh cadence (actual) |
|---|---|---|---|---|---|
| `macro_data.json` | `/api/general/macro/macro_data.json` | `json/macro/macro_data.json` | `yang-generate-macro` Lambda | Bloomberg `data_pkl` (`price_monthly`) | Weekly, on `data_pkl` upload (Step Functions). Served copy `data_as_of` 2026-05-18 |
| `yield_curve_fred.json` | `/api/general/macro/yield_curve_fred.json` | `json/macro/yield_curve_fred.json` | `ingest_yield_curve_fred.py` | **FRED** (10 DGS series) | Intended daily; **ACTUALLY STALE — `data_as_of` 2026-01-15, ~4 months old** (see Finding F3) |
| `volatility_data.json` | `/api/general/macro/volatility_data.json` | `json/macro/volatility_data.json` | `opal-portal-volatility-fetcher` Lambda | **FRED** VIXCLS (VIX) + **Yahoo Finance** ^MOVE | Daily, weekdays (`cron(30 12 ? * MON-FRI *)`). Served copy `data_as_of` 2026-05-19 |
| `macro/timeseries/{slug}.json` | `/api/general/macro/timeseries/{slug}.json` | `json/macro/timeseries/{slug}.json` | `yang-generate-macro-timeseries` Lambda | Bloomberg `data_pkl` (`price_monthly`) | Weekly, on `data_pkl` upload. 79 files present in S3 |

Serving-path anchor: `comp-routes behaviors` — behavior 16 `/api/general/*` -> S3
`opal-data-portal-v2` via `public-data-router` (origin-request) + `cache-control-injector`
(origin-response). All four artifacts resolve through this behavior. (Confirmed, matches PRD §5
router/origin; the `/api/general/` prefix vs PRD's `/api/public/json*` is the same delta the
WS-2 audit already recorded.)

### 2.3 `macro_data.json` — the 79 indicators

12 groups, 79 served indicators. Per-indicator unit + transform are carried in the Lambda's
`INDICATOR_UNITS` map and the served JSON. Full per-indicator detail (name, Bloomberg ticker,
unit, FRED mapping) is in the companion TSV. Group summary:

| Group | Served | Bloomberg-ticker family | What it feeds |
|---|---|---|---|
| Leading Indicator | 8 | ISM/S&P PMI, NFIB, Conf Board LEI | Heatmap rows + timeseries modal |
| Lagging Indicator | 7 | BEA GDP, Fed/Census output series | Heatmap + modal |
| Financial Condition | 6 | Bloomberg/Chicago Fed FCI, Fed funds, balance sheet | Heatmap + modal |
| Inflation | 8 | BLS CPI/PPI, BEA PCE, UMich expectations | Heatmap + modal |
| Labor Market | 9 | BLS/DOL employment series, ADP | Heatmap + modal |
| Consumer | 7 | Census retail, UMich/Conf Board sentiment | Heatmap + modal |
| Housing Market | 6 (config'd 7) | Census/NAR housing series, NAHB | Heatmap + modal |
| Investor Sentiment | 7 | AAII surveys, Fed NLP | Heatmap + modal |
| Treasury Yields | 10 | Treasury CMT (USGG*) | Heatmap + modal + **Yield Curve tab** |
| Credit Spread | 5 | Bloomberg index OAS, BSBY-TED | Heatmap + modal |
| Market Indicator | 1 (config'd 2) | VIX (MOVE config'd, dropped) | Heatmap + modal |
| Currency | 5 | Bloomberg/ICE FX rates | Heatmap + modal |

Transforms applied by `yang-generate-macro`: trailing-12-month windowing; min-max normalized
percentile (1-100 scale) per indicator over full history; percentile threshold values
(p10/p25/p50/p75/p90); unit-aware rounding. The Bloomberg tickers carry the transform in the
name (`CPI CHNG` = CPI MoM change, `MTIBYOY` = YoY) — the Lambda does NOT recompute; it ingests
whatever `price_monthly` row Bloomberg supplies. This matters for the FRED mapping (§3.3).

### 2.4 Pipeline-mechanism findings (Phase 1)

- **F1 — 2 indicators silently dropped.** `MACRO_GROUPS` configures **81** indicators;
  `macro_data.json` serves **79**. `MOVE` (`MOVE Index`) and `S&P CoreLogic CS Home Price MoM`
  (`SPCS20SM`) have no `data_pkl` row, and `yang-generate-macro` does
  `if len(ind_data) == 0: continue` — silent skip, no warning surfaced to the portal. The
  Housing group object carries `count: 7` while serving 6 indicators (count/content mismatch).
- **F2 — `vix_data.json` dual-writer.** Both `yang-generate-macro` (writes
  `json/macro/vix_data.json` from the Bloomberg pkl `VIX` row) **and**
  `opal-portal-volatility-fetcher` (writes the same key as its `LEGACY_KEY` from FRED VIXCLS)
  target `json/macro/vix_data.json`. Last writer wins; the two sources differ. The page does
  not consume `vix_data.json` (it uses `volatility_data.json`), so this is latent not active,
  but it is a real dual-writer on one S3 key.
- **F3 — `yield_curve_fred.json` is ~4 months stale.** Served `data_as_of` 2026-01-15.
  `ingest_yield_curve_fred.py` is a script with a `lambda_handler`, but there is no deployed
  EventBridge schedule firing it — it has not run since Jan 15. The Yield Curve tab's "1Y Ago"
  toggle silently serves 4-month-old FRED data. (The macro page docstring claims yield curve
  updates "Daily at 6:30 PM ET" — false.)
- **F4 — CloudFront invalidation path mismatch.** `yang-generate-macro` invalidates
  `/api/public/macro/*`; the served behavior is `/api/general/*` (comp-routes behavior 16).
  The invalidation does not cover the path the portal actually reads.
- **F5 — doc staleness.** `MacroHeatmap.tsx` header says "73 indicators in 10 groups" (actual
  79/12). `api/endpoints/macro.ts` says the timeseries data source is "FRED API" and the slug
  is a "FRED series ID" — both wrong (it is Bloomberg-pkl; slug is a slugified indicator name).
  `portal-proxy.ts` `getVolatilityData` says "via yang-generate-macro Lambda" — wrong (producer
  is `opal-portal-volatility-fetcher`). `portal/etl/pages/macroeconomics/README.md` (dated
  2025-12-17) describes a `MacroSummaryPanel` and `VIXTab` that no longer exist.
- **F7 — drill-down timeseries: 16 of 80 files ~4 months stale; depth uneven; ~36yr not 40yr.**
  The `MacroTimeSeriesModal` drill-down consumes `json/macro/timeseries/{slug}.json`. S3 holds
  80 files (79 served indicators + 1 orphan `fed_balance_sheet_as_pct_of_gdp.json` from a
  superseded slug scheme). The current `yang-generate-macro-timeseries` Lambda's `INDICATORS`
  list has only **64 entries** — 64 files regenerate weekly (LastModified 2026-05-19), **16 are
  frozen at 2026-01-12** (~4 months stale): all 5 Currency (DXY, EUR/USD, USD/JPY, GBP/USD,
  USD/CNH), Factory Orders MoM, Trade Balance, Net Long Term TIC Flows, Unit Labor Cost YoY,
  Retail Sales ex Auto MoM, Retail Sales ex Auto and Gas MoM, Wards Total Vehicle Sales,
  S&P PMI Manufacturing, S&P PMI Services, Fed NLP Sentiment (+ the orphan). These 15 were
  generated once by a fuller/older process and never refresh — clicking e.g. DXY in the modal
  shows a chart ending 2026-01-09 while the heatmap row beside it shows May data (visible
  internal inconsistency). Same failure class as F1 (config list shorter than rendered set).
  Separately: history runs **1990 -> 2026 (~36 years, ~437 monthly points)** — not 40 years
  (the Bloomberg `data_pkl` `price_monthly` history starts ~1990); and depth is uneven —
  `unemployment_rate` carries only 145 points where a monthly series should have ~432
  (`gdp_qoq`'s 145 is correct — GDP is natively quarterly). Fix: extend the Lambda's
  `INDICATORS` list from 64 to the full 79 + delete the orphan file.

These are recorded for the implementation TO and for COO/CTO; F1/F3/F7 have user-visible impact.

---

## 3. PHASE 2 — FRED API capability exploration + mapping

### 3.1 FRED API surface

FRED (Federal Reserve Economic Data, St. Louis Fed) is a free public-data API over 800,000+
US and international economic time series from 100+ sources.

- **Authentication:** a free API key (instant self-service registration), passed as the
  `api_key` query parameter. No OAuth, no per-call signing.
- **Rate limit:** 120 requests/minute per key.
- **Formats:** `file_type=json` or `xml`.
- **Endpoint families:**
  - Series — `/fred/series`, `/series/observations`, `/series/search`,
    `/series/search/tags`, `/series/categories`, `/series/release`, `/series/tags`,
    `/series/updates`, `/series/vintagedates`.
  - Categories — `/fred/category`, `/category/children`, `/category/series`,
    `/category/tags`, `/category/related`.
  - Releases — `/fred/releases`, `/release`, `/release/series`, `/release/dates`,
    `/release/tables` (release calendar — useful for cadence/timeliness planning).
  - Sources — `/fred/sources`, `/source`, `/source/releases`.
  - Tags — `/fred/tags`, `/related_tags`, `/tags/series`.
  - Geo — GeoFRED / Maps API (not relevant here).
- **`/series/observations` parameters that matter for this page:**
  - `units` — server-side transform: `lin` (level), `chg` (change), `ch1` (year-ago change),
    `pch` (% change = MoM on a monthly series), `pc1` (year-ago % change = YoY), `pca`
    (compounded annual rate), `cch`, `cca`, `log`. **This eliminates custom transform math
    for all 17 "FRED-TRANSFORM" indicators.**
  - `frequency` + `aggregation_method` — resample (e.g. weekly series -> monthly avg/eop/sum).
  - `observation_start` / `observation_end`, `limit` (up to 100000), `offset`, `sort_order`.
  - `realtime_start` / `realtime_end` + `vintage_dates` — ALFRED revision/vintage history.
- **Observation limits:** no hard cap beyond `limit` (100000) + `offset` pagination; every
  series this page needs is far under one page.

Note: the FRED HTML documentation pages are WAF-gated against automated fetch (HTTP 403 to
WebFetch), and the official API returns HTTP 400 without a key — but the keyless CSV endpoint
(`fred.stlouisfed.org/graph/fredgraph.csv?id=`) is fully open and was used for this audit's
fidelity probes (§3.4). The API surface above is established/stable FRED behavior.

### 3.2 The existing FRED integration baseline

FRED is **already integrated in this pipeline by two distinct mechanisms** — this is the
proven extension path, not a greenfield build:

**(a) Official API path** — `api.stlouisfed.org/fred/series/observations`, key from Secrets
Manager, `requests` library. Used by:
- `opal-portal-volatility-fetcher` (`infra/.../07_macroeconomics/lambdas/`) — pulls VIXCLS,
  35y history, writes `volatility_data.json`. Key via `get_fred_api_key()` reading Secrets
  Manager secret `opal/external-apis` (key field `FRED_API_KEY` or `fred_api_key`),
  **region us-east-1**.
- `ingest_yield_curve_fred.py` (`portal/etl/orchestration/green/fred/lambda/`) — loops 10 DGS
  Treasury series, computes 1d/1w/1m returns, writes `yield_curve_fred.json`. Key via
  `FRED_API_KEY` **environment variable**.

**(b) Keyless CSV path** — `fred.stlouisfed.org/graph/fredgraph.csv?id=`, no key, `urllib`.
Used by `yang-pipeline/outputs/refresh-fred-cache` — weekly pull of `BAMLC0A0CM` (IG) and
`BAMLH0A0HYM2` (HY) credit-spread series, cached to `s3://opal-data-portal-v2/cache/fred/`,
consumed by `yang-generate-risk-premium` (Valuation page). Level data only — no `units=`
transform on the CSV endpoint.

**Key storage:** Secrets Manager secret `opal/external-apis`. **Region inconsistency
(Finding F6):** `yang-pipeline/outputs/generate-volatility` reads the secret from
**us-east-2**; `opal-portal-volatility-fetcher` reads it from **us-east-1**. An
implementation TO must standardize this. (Per the TO `<do_not>`, the key value is not
handled in this audit — only its storage location is confirmed.)

**Extension assessment (AC2):** the `ingest_yield_curve_fred.py` pattern — loop series IDs ->
`/series/observations` -> write one JSON to S3 — extends **directly** to all 50 FRED-replaceable
macro indicators with no new mechanism. It needs new pull code only in the trivial sense of a
new series list + the `units=` parameter per indicator; the auth, the S3 write, the Lambda
shape are all already proven. A full daily refresh of 50 indicators = ~50 requests in one
burst, vs the 120/min limit — no batching needed.

### 3.3 Mapping every Phase-1 input onto FRED

Full 79-row table in `mdsrc-fred-macro-mapping-20260520.tsv`. Classification:

| Class | Count | % | Meaning |
|---|---|---|---|
| FRED-DIRECT | 33 | 42% | Identical official series on FRED; ingest as-is (`units=lin`) |
| FRED-TRANSFORM | 17 | 22% | On FRED as a level; needs a `units=` transform (`pch`/`pc1`/`chg`) — FRED computes it server-side |
| FRED-PROXY | 6 | 8% | FRED has a near-equivalent, not identical (credit-spread index family, dollar basket, onshore yuan) |
| NON-FRED | 23 | 29% | Licensed survey / proprietary / FRED-discontinued — genuine residue |
| **FRED-replaceable** | **50** | **63%** | DIRECT + TRANSFORM |

Per group (served counts):

| Group | DIRECT | TRANSFORM | PROXY | NON-FRED |
|---|---|---|---|---|
| Leading Indicator (8) | 0 | 0 | 0 | 8 |
| Lagging Indicator (7) | 3 | 4 | 0 | 0 |
| Financial Condition (6) | 3 | 1 | 1 | 1 |
| Inflation (8) | 1 | 6 | 0 | 1 |
| Labor Market (9) | 6 | 2 | 0 | 1 |
| Consumer (7) | 2 | 4 | 0 | 1 |
| Housing Market (6) | 4 | 0 | 0 | 2 |
| Investor Sentiment (7) | 0 | 0 | 0 | 7 |
| Treasury Yields (10) | 10 | 0 | 0 | 0 |
| Credit Spread (5) | 0 | 0 | 3 | 2 |
| Market Indicator (1) | 1 | 0 | 0 | 0 |
| Currency (5) | 3 | 0 | 2 | 0 |

Two groups — Lagging Indicator and Treasury Yields — are 100% FRED. Two groups — Leading
Indicator and Investor Sentiment — are 0% FRED.

### 3.4 Value-fidelity check (FRED vs the portal's current Bloomberg-pkl values)

Method: pulled the served `macro_data.json` (`data_as_of` 2026-05-18) from S3 and the matching
FRED series via the keyless `fredgraph.csv` endpoint; compared latest values. 33+ FRED series
probed. Representative results:

| Indicator | Bloomberg (macro_data.json) | FRED | Verdict |
|---|---|---|---|
| GDP QoQ | Mar 2.0 | A191RL1Q225SBEA Q1 2.0 | **EXACT** |
| Capacity Utilization | Apr 76.12 | TCU Apr 76.1194 | **EXACT** |
| Trade Balance | Mar -60.3 B | BOPGSTB Mar -60307 M (= -60.3 B) | **EXACT** (unit scale) |
| Fed Fund Rate | Apr 3.64 | FEDFUNDS Apr 3.64 | **EXACT** |
| US Job Openings | Mar 6866 | JTSJOL Mar 6866 | **EXACT** |
| Labor Force Participation | Apr 61.8 | CIVPART Apr 61.8 | **EXACT** |
| Weekly Hours | Apr 34.3 | AWHAETP Apr 34.3 | **EXACT** |
| New Home Sales | Mar 682 | HSN1F Mar 682 | **EXACT** |
| Housing Starts | Mar 1502 | HOUST Mar 1502 | **EXACT** |
| Building Permits | Mar 1363 | PERMIT Mar 1363 | **EXACT** |
| Unemployment Rate | Mar 4.34 | UNRATE Apr 4.3 | MATCH (same BLS series; rounding + as-of) |
| Treasury 10Y | May 4.59 | DGS10 4.67 | MATCH (Bloomberg monthly snapshot vs FRED daily) |
| VIX | May 17.82 | VIXCLS 18.06 | MATCH (monthly snapshot vs daily) |
| IG / HY spread | May 0.74 / 2.72 | BAMLC0A0CM 0.76 / BAMLH0A0HYM2 2.86 | MATCH (monthly vs daily; index-family proxy) |
| EUR/USD, USD/JPY, GBP/USD | May 1.17 / 158.82 / 1.34 | DEXUSEU 1.16 / DEXJPUS 158.7 / DEXUSUK 1.33 | MATCH |

**Finding:** wherever FRED and Bloomberg both carry the official government/UMich series,
fidelity is **HIGH to EXACT** — because they are the *same underlying source* (BLS, BEA,
Census, Federal Reserve, Treasury, DOL, U. Michigan). The differences are exactly three,
all benign and handled at implementation:
1. **Transform** — Bloomberg pre-computes MoM/YoY (`CPI CHNG`, `MTIBYOY`); FRED gives the index
   level. Resolved by the FRED `units=` parameter (no custom math).
2. **Cadence** — Bloomberg `price_monthly` carries a monthly snapshot; FRED carries the native
   frequency (weekly claims, daily yields/FX/VIX). The heatmap is a monthly grid, so a monthly
   snapshot of the FRED series (`frequency=m`) reproduces it; the Yield Curve and Volatility
   tabs already consume FRED at daily frequency successfully.
3. **Rounding** — Bloomberg occasionally carries one more decimal (4.34 vs 4.3). Cosmetic.

The FRED-PROXY rows are the only genuine value-divergence: ICE-BofA OAS index families differ
slightly from Bloomberg index OAS; FRED `DTWEXBGS` (~119) is a different basket and scale from
the ICE Dollar Index (`DXY` ~99) — **not a drop-in for DXY**; FRED `DEXCHUS` is onshore CNY,
the page tracks offshore CNH (they diverge in stress periods).

### 3.5 The genuine non-FRED residue (AC4) — 23 indicators

| Residue indicator(s) | Why not FRED | Alternative source |
|---|---|---|
| ISM Manufacturing/Services PMI, ISM New Orders x2 (4) | ISM withdrew its series from FRED in 2016; licensed survey | ISM subscription (or keep Bloomberg) |
| S&P Global PMI Manufacturing/Services (2) | S&P Global/Markit licensed survey | S&P Global subscription (or keep Bloomberg) |
| Conference Board Leading Index (1) | Conference Board licensed; FRED's Philly Fed `USSLIND` discontinued 2020-02 | Conference Board subscription; OECD CLI is a different-methodology proxy |
| NFIB Small Business Optimism (1) | NFIB licensed survey | NFIB direct |
| AAII Sentiment x3 + Allocation x3 (6) | AAII licensed survey | AAII (aaii.com publishes the weekly survey — semi-public download worth evaluating) |
| Fed NLP Sentiment (1) | Opal/Bloomberg proprietary NLP score | none — proprietary, stays |
| Bloomberg Financial Condition Index (1) | Bloomberg proprietary composite | Chicago Fed NFCI (already a separate indicator on this same page) is the FRED-native substitute |
| ADP Employment Change (1) | ADP National Employment Report not freely on FRED | ADP Research (licensed) |
| Conference Board Consumer Confidence (1) | Conf Board licensed | OECD Consumer Confidence (FRED `USACSCICP02STSAM`) is a normalized proxy — different scale |
| NAHB Housing Market Index (1) | NAHB/Wells Fargo licensed builder survey | NAHB direct |
| NAR Pending Home Sales (1) | NAR licenses Pending separately; FRED carries NAR Existing but not Pending | NAR direct |
| UMich 5-10yr Inflation Expectation (1) | FRED carries only the 1-yr UMich expectation | UMich subscription; market 5y breakeven `T5YIE` is a different-concept proxy |
| Ted Spread (1) | FRED `TEDRATE` discontinued 2022-01 (LIBOR retirement); the Bloomberg ticker is itself a BSBY-based TED replacement | no FRED equivalent; a SOFR-based funding-stress spread is a different-concept substitute |
| Bloomberg US Aggregate OAS ("AGG") (1) | Bloomberg index OAS is licensed | ICE BofA US Broad Market OAS (non-FRED proxy) |

Pattern: **the residue is survey data and proprietary indices.** No public statistical agency
produces ISM/S&P PMI, the AAII survey, NFIB, NAHB, the Conference Board indices, or a
financial-conditions composite — they are private products. FRED carries government data
comprehensively and that is exactly the 50 indicators it covers.

---

## 4. v0.3 WS1-MAC-01 verdict upgrade

PRD v0.3 §5.2 classified WS1-MAC-01 (Macroeconomics macro indicators) as a "Bloomberg-leaning
hybrid." This audit makes that exact:

- **`macro_data.json`: 63% cleanly FRED-replaceable** (50/79), **71% with proxies** (56/79),
  **29% hard residue** (23/79).
- **`yield_curve_fred.json`: already 100% FRED** (10/10 Treasury tenors) — but stale (F3).
- **`volatility_data.json`: VIX already FRED** (VIXCLS); **MOVE is Yahoo Finance**, not
  Bloomberg and not FRED (ICE MOVE is licensed; FRED has no MOVE).
- **`macro/timeseries/*`: same 79 indicators** as `macro_data.json` — same 63/71/29 split.

So the Macroeconomics page as a whole is **already a genuine hybrid** (yield curve + VIX on
FRED; MOVE on Yahoo; everything else Bloomberg), and the FRED-replaceable fraction of the
Bloomberg portion is **63% clean**. The residue floor is **~29%** (the two licensed-survey
groups + 8 named indices) and cannot move without paid survey subscriptions.

---

## 5. Recommendations (for the v0.4 amendment / implementation TO — NOT executed here)

1. **A FRED macro-ingestion Lambda is well-justified and low-risk.** Pattern-identical to the
   existing `ingest_yield_curve_fred.py`. It would move 50 indicators (63%) off the manual
   Bloomberg pkl onto a free, official, daily-fresh source. Scope it as: series list (50) +
   `units=` per indicator (from the companion TSV) + monthly-snapshot resample for the heatmap
   grid + S3 write. ~50 requests/run, no batching.
2. **Keep the 23 residue on Bloomberg** (or evaluate the named subscriptions). Do NOT chase a
   FRED substitute for licensed survey data — the proxies (OECD CCI, market breakevens) are
   different concepts and would silently change what the page reports.
3. **Decide the 6 FRED-PROXY cases explicitly.** Credit spreads (AAA/IG/HY): the ICE-BofA
   family is already trusted (`refresh-fred-cache` uses it for Valuation) — acceptable. DXY:
   `DTWEXBGS` is NOT a drop-in — either keep DXY on Bloomberg or relabel the page metric.
   USD/CNH: onshore CNY proxy is acceptable in calm regimes, not in stress.
4. **Fix the Phase-1 mechanism findings independent of the FRED migration:** F3 (deploy the
   yield-curve ingestion on a schedule — it is 4 months stale and user-visible), F7 (extend the
   `yang-generate-macro-timeseries` `INDICATORS` list 64 -> 79 so the 16 stale drill-down files
   refresh, and delete the orphan file — also user-visible), F1 (surface the 2 silently-dropped
   indicators, or remove them from config), F2 (resolve the `vix_data.json` dual-writer), F4
   (correct the CloudFront invalidation path), F6 (standardize the Secrets Manager region).
5. **Free option already on the page:** Bloomberg FCI's FRED substitute (Chicago Fed NFCI) is
   *already rendered as a separate indicator on the same heatmap* — the page could drop the
   proprietary Bloomberg FCI row at zero data cost.

---

## 6. Compiler Tools

| Tool | Command | Result | vs expect |
|---|---|---|---|
| comp-routes | `comp-routes behaviors` | 23 CF behaviors; behavior 16 `/api/general/*` -> S3 `opal-data-portal-v2` via `public-data-router` + `cache-control-injector` | MATCH — anchors the §2.2 serving-path column. `/api/general/` prefix vs PRD `/api/public/json*` recorded (same delta as the WS-2 audit) |
| comp-pipescript | `comp-pipescript io yang-generate-macro` + `... yang-generate-macro-timeseries` | "Unknown script" — yang generators are not comp-graph nodes (BD-gold IDs only) | MISMATCH handled per TO `<if_mismatch>`: fell back to direct source read of `infra/aws/lambda/v2_portal/yang_pipeline/` — both Lambdas + `refresh-fred-cache` + `generate-volatility` + `opal-portal-volatility-fetcher` read in full |
| FRED probe | keyless `fredgraph.csv?id=` x33+ series | empirical value-fidelity §3.4 | MATCH — official-series fidelity HIGH/EXACT confirmed; residue + proxies confirmed |
| Phase 2/3 gates | (none — audit doc, no `.py` authored) | no `py_compile`/`ruff`/`ds-precommit` applies | per TO `<compiler_tools_mandate>` phase 2/3 = documented-none |

comp-routes auto-logged to `org/compiler-tools-log.md` via `.comp-graph/.agent_context`.

---

## 7. Deliverables

- This brief — `docs/briefs/mdsrc-fred-macro-sourcing-audit-20260520.md`.
- Machine-readable mapping — `docs/briefs/mdsrc-fred-macro-mapping-20260520.tsv` (79 rows:
  group, indicator, bbg_ticker, unit, served, fred_series_id, fred_class, fred_units_param,
  fidelity, residue_alt_source, notes).
- Session log — `org/tier2_senior/0.2.0_DS_PortfolioAnalytics/logs/2026-05-20/`.

RAVC2 to `1.0.0_SA_CTO` — feeds the v0.4 amendment + upgrades the v0.3 WS1-MAC-01 verdict.
