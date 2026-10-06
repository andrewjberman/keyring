# FEASIBILITY ANALYSIS -- running the Analysis-tab report generation in house, without YCharts

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-05 ~19:4xZ (3:4x PM Eastern).
- **Order:** Andrew-direct 2026-10-05 ~19:3xZ, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_194xZ_YCHARTS_INHOUSE_FEASIBILITY_ANALYSIS.md`.
- **Input:** `2.0.0_SA_COO~Y`'s handoff,
  `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/HANDOFF_TO_CRO_ONPREM_GENERATION_20261005.md`
  (called "the handoff" below). Base brief: `docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md`.
- **Consumer:** Andrew; then `1.0.0_SA_CTO` for the IRPT_YCDGEN endpoint revision (msgs 105307 / 105308). This file
  stands as the brief addendum those messages asked for.
- **Claim marks:** MEASURED = read by this seat today from the live store or the file named. INHERITED = taken from the
  handoff and not re-read. INFERRED = reasoned, not read. No ticker, amount or client name appears here.

---

## 1. Verdict

**Feasible. The report can be generated entirely in house, and the first working version needs no new vendor.**

1. **Nothing in the report is YCharts-only knowledge.** YCharts receives Opal's holdings and settings and returns a PDF.
   Every figure in that PDF is either Opal's own input, layout, arithmetic on price histories, or public reference data
   about each holding (INHERITED, handoff sections 2 and 5; the element counts were re-counted today, section 3).
2. **Opal's price coverage of a real client portfolio is far better than the handoff states.** The handoff measured
   Bloomberg only: 37 of 99 holdings. Opal's own Yahoo price table covers **96 of the same 99 holdings, 99.5 percent of
   the portfolio by dollar weight** (MEASURED, section 2). The return and risk half of the report is therefore buildable
   now for windows up to five years.
3. **The real work is one thing: look-through data for fund holdings.** Sector, region, bond and market-cap breakdowns
   of each ETF or mutual fund a client holds. Funds are at least 39 percent of the reference portfolio by weight, and up
   to 83 percent (MEASURED). Opal holds this for its own four ETFs only. Each gap has a named light channel (section 5).
4. **The wait disappears.** Today 15 of every 17 to 19 minutes is a fixed 900-second hold for YCharts' firewall
   (INHERITED, measured by `2.0.0_SA_COO~Y` on 6 of 6 jobs). In house there is no session, no firewall and no request
   budget. The compute time of an in-house run is not yet measured; it is arithmetic over data already in Opal's store.
5. **Sensitivity runs stop costing anything.** YCharts challenges the 7th request in a window, so every extra comparison
   or variant queues behind a firewall. In house, a second or tenth variant of the same portfolio is a recompute over
   series already loaded (INFERRED from the request counts in the handoff section 8).

**What "feasible" does not mean:** a byte-for-byte copy of the YCharts report. Some YCharts figures use Morningstar
definitions Opal has no licence for (sector scheme, style box). Opal's report states its own method for those or omits
them; it never imitates (base brief, bar 5).

---

## 2. What this seat measured today (new evidence)

Reference case: the 99 holdings of frozen request `REQ-a618aa83407689bc95193a01` (firm cottonwood), read from the
research run record `opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/run.json`.
Denominator in every row is those 99 holdings; weights are dollar weights of that one portfolio.

| # | Question | Result (MEASURED) | Source read |
|---|---|---|---|
| M1 | How many holdings have a daily price series in Opal's Yahoo table? | **96 of 99 (99.5 percent of weight)**. 94 series start in 2020, 2 start in 2025. 95 end on 2026-10-02 (the last trading day), 1 ended 2026-04-02. Median 1,691 daily rows | `opal-data-bd/silver/historical_prices.parquet` (5,865,202 rows, 3,628 tickers, 2020-01-02 to 2026-10-02, one source: yahoo_finance) |
| M2 | How many have Bloomberg characteristics? | 37 of 99 (14.3 percent of weight). Confirms the handoff's count; the weight is new | `opal-data-etfs/bbg/2026-10-02/characteristics.parquet` (114 rows) |
| M3 | Yahoo or Bloomberg, either one | 97 of 99 (99.7 percent of weight) | M1 and M2 joined |
| M4 | How many holdings are funds, which need look-through? | 12 labelled `fund` (39.0 percent of weight); 49 labelled `single_security` (16.6 percent); **38 carry no kind label (44.4 percent)** | DynamoDB `etf-classifications`, field `instrument_kind` (3,492 items; 2,504 of them carry no kind) |
| M5 | Asset-class label | 97 of 99 labelled: 93 equity (88.2 percent of weight), 4 fixed income (11.6 percent) | DynamoDB `etf-classifications`, field `asset_class` |
| M6 | Is the risk-free series usable? | **No, as it stands.** Last written 2026-08-05; last observation 2026-08-04; 499 observations from 2024-08-05 | `opal-data-portal-v2/json/macro/yield_curve_fred.json`. Filed as surprise row `IRPT_YCDGEN-S9` |
| M7 | Report elements by what they need (all three variants) | 1,252 elements: 34 Opal's input, 279 layout or boilerplate, 219 computed from series, 720 holding reference data | The three maps in `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/` and the handoff's class table, summed |
| M8 | Overview census, why 72 reference rows are not held | 30 bond-sleeve look-through; 14 market-cap bucket and style box; 11 no table; 4 multi-column; 13 single reasons (expense ratio, distribution yield, cash, convertible, preferred, beta, alpha, duration, holdings count, level series) | `overview_coverage.json` (176 rows) |

**Two readings that change the handoff's picture:**

- The handoff says "62 have no price series". That is true of the Bloomberg feed. It is not true of Opal's estate: the
  Yahoo table Opal already refreshes every day holds 96 of the 99 (M1).
- The 86 Overview rows the census marks as held are thinner than the count suggests. They stand on the 37 stock
  holdings, which are 14.3 percent of the portfolio's weight (M2), and each stock is placed whole in one sector and one
  country. For a fund-heavy portfolio those rows are not yet a fair picture of the portfolio.

**Limits of these measurements:** one portfolio, one firm. The Yahoo table's universe is the securities held in Black
Diamond accounts, so a prospect's file with unusual holdings will match less well. The 38 unlabelled holdings (M4) mean
the fund share is a range, not a figure.

---

## 3. The report, element by element: what in-house takes

Element counts are the handoff's classes, summed over the three variants (Overview 254, Comparison 574, Multi 424).
All 1,252 placements are INFERRED from printed labels (handoff caveat); only the Overview has a coverage census.

| Class | Elements | Share | What it needs | In-house readiness |
|---|---|---|---|---|
| (a) Opal's own input echoed | 34 | 3 percent | holdings, settings, cover fields | **Ready.** Already Opal's (upload, normalization, profile) |
| (b) Layout, boilerplate, dates | 279 | 22 percent | a renderer | **Ready.** Opal-branded HTML builder and `render_pdf.cjs` exist; a 39-page Opal Overview was produced 2026-10-04 (INHERITED) |
| (c) Computed from series | 219 | 17 percent | daily total-return histories per holding and comparison; benchmark; risk-free | **Methods ready, data mostly ready.** Methods are in `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` (returns, standard deviation, max drawdown, alpha, beta, Sharpe, Sortino, monthly value-at-risk; windows 1 month to 15 years). Series: 96 of 99 holdings to about 5.8 years (M1). Gaps: total-return convention, 10- and 15-year windows, risk-free (section 5) |
| (d) Holding reference data | 720 | 58 percent | per-holding snapshot: sector, region, asset mix, bond breakdown, market-cap and style, fundamentals, prospectus fields, top-25 constituents | **Partial.** Single stocks: the right fields exist, for Opal's own ETF constituents only. Funds: look-through is held for Opal's four ETFs only. This is the build |

**Read across the classes:** 25 percent of the report is ready today, another 17 percent needs data Opal already
pulls, and 58 percent depends on a reference-data mart that does not exist yet for client holdings.

---

## 4. The process today, and what replaces each step

| Step today (handoff section 2) | In house | Change |
|---|---|---|
| Upload, correction, variant and comparison choice (portal, intake Lambda) | unchanged | none |
| Acceptance, job row, queue `irpt-generation` | unchanged | none |
| Resident worker signs in to YCharts, uploads holdings, saves a model portfolio | removed | no session, no shared-account eviction |
| Fixed 900-second firewall hold, then read-back | removed | the 15 minutes |
| Validate, generate, download the vendor PDF | replaced by: read holdings, read the data mart, compute, render | Opal's own figures |
| Extractor re-reads each figure from the PDF by page and coordinates, then certifies (about 1.5 minutes) | removed in this form: the figures are data before they are a page, so each section is written directly with its method and source | certification becomes a check of inputs and coverage, not a PDF re-read (INFERRED) |
| Status READY, page opens sections, export | unchanged in shape | contract note below |

**Contract note for the CTO (not a design).** `AnalysisReport` (v1) requires `vendor_artifact` and
`effective_inputs.read_back`; both describe a vendor PDF. An Opal-generated report has neither. `PerformanceReport`
already carries `provider: OPAL_ENGINE`, so the precedent for an Opal producer exists in the same contract family.

**Compute and render home (INHERITED):** the always-on resident host already renders exports with Playwright; the
IRPT Lambdas run at 512 to 2,048 MB. No new compute class is needed.

---

## 5. Data gaps, the light channel for each, and what needs Andrew's word

Order is by how much of the report each gap blocks. "Word" marks vendor or online egress that needs Andrew's
authorization before any call (CLAUDE.md, Agent Autonomy).

| # | Gap | Blocks | Lightest channel | Word needed | Confidence |
|---|---|---|---|---|---|
| G1 | **Total-return convention of the Yahoo series.** Close only; the backfill is dividend-adjusted and the daily fetch is not (INHERITED, handoff family 6) | every class (c) figure for dividend payers | fix the convention in the pipeline Opal already runs: one adjusted series per ticker, or close plus dividends | no new vendor; it is the existing scheduled Yahoo pull | high |
| G2 | **History depth.** Yahoo table starts 2020; Bloomberg backfill is 5.6 years | 10-year and 15-year windows, since-inception, calendar years before 2020 | extend the Yahoo backfill start date for the client-holdings universe, one time | yes, as a change to an existing vendor pull | high |
| G3 | **Risk-free series** stale since 2026-08-05 and 2 years long (M6) | alpha, Sharpe, Sortino in every window | the Bloomberg 3-month yield Opal already receives daily in the morning pull (no new call; INHERITED, handoff family 5), or repair and lengthen the FRED pull | none for the Bloomberg series; yes for FRED | high |
| G4 | **Benchmark and comparison series** | benchmark lines, comparison columns | held: 84 index series since 1989 including the S&P 500 total return, and Opal's own models (INHERITED, family 4). ETF comparisons come from G1/G2 | none | high for Opal models and indices |
| G5 | **Single-stock reference fields** (sector, country, market cap, dividend yield) beyond Opal's ETF constituents | class (d) rows for the stock part of a portfolio | Bloomberg reference request for the union of client-held stocks, through the existing `EXTRA_SECURITIES` precedent | yes; Bloomberg quota is unmeasured and Andrew has called it the binding constraint | high that it works; unknown quota cost |
| G6 | **Fund sector and country look-through** | about 200 elements per variant; the largest single block | Bloomberg `HB_INDUSTRY_SECTOR_ALLOCATION` and `HB_GEO_CNTRY_ALLOC` per fund ticker: one call per fund per day, served today without the query-language entitlement | yes | proven on ETFs; **untested on mutual funds** |
| G7 | **Fund fundamentals** (expense ratio, yield, holdings count, inception date) | fundamentals tables | Bloomberg fund fields once fund tickers are on the pulled list; SEC prospectus data as the free alternative | yes | medium: the expense-ratio field was empty in the census because no fund ticker was ever pulled |
| G8 | **Bond-sleeve breakdown** (credit quality, maturity buckets, bond sector, duration, yield) | 30 Overview elements, more in the other two | first probe Bloomberg fund-level duration and yield fields; then SEC N-PORT filings (every registered fund's full holdings, free, about 60 days behind); credit quality needs ratings from Bloomberg or issuer fact sheets | yes | medium to low: no field of this kind exists anywhere in the repo today |
| G9 | **Market-cap buckets and style box** | 14 elements per variant | fund holdings (N-PORT or issuer files) times per-stock market cap, with Opal-defined breakpoints. The style box needs Opal's own value and growth scores | yes for the holdings source | low for the style box: recommend replacing it |
| G10 | **Top-25 constituents of each fund** | Comparison and Multi holdings tables | issuer daily holdings files (Opal already runs two such channels); N-PORT quarterly | yes | medium |
| G11 | **Prospectus fields** (loads, SEC yields, waivers) | Comparison and Multi tables | SEC prospectus data; issuer pages for daily SEC yields | yes | medium |

**Three properties that shape the build:**

- **Capture starts the clock.** Bloomberg serves the fund allocation fields for the current day only, with no history
  (`integrations/bloomberg/READ_HERE.md` section 4). A report as of last month cannot be rebuilt from a pull made
  today. The earlier capture starts for the client-holdings universe, the more history Opal owns.
- **Bloomberg runs on one Terminal seat.** Every Bloomberg call is a scheduled batch on that box, not a call at
  report time. The report reads a cache; it never waits on Bloomberg.
- **The cache is keyed by what Opal already resolves.** The upload step resolves each row to a ticker. The data mart
  is one series store and one reference snapshot per resolved security, refreshed for the union of securities in live
  client portfolios. A security seen for the first time is backfilled once.

---

## 6. Sequence: one working report first, then enrichment

The canonical rule applies: the first round is one live journey end to end; later rounds enrich it.

| Stage | What Andrew can do when it lands | New data needed | Word needed |
|---|---|---|---|
| **1. The thread** | Submit the reference portfolio on the Analysis tab and open an Opal-generated Overview within the same sitting: cover, holdings, allocation by label, return and risk tables for windows to 5 years against the S&P 500 total return. Rows Opal cannot yet compute say so with the reason | G1 (total-return fix), G3 (risk-free from the Bloomberg series), G4 (held) | none, if G1 is a fix inside the existing pull |
| **2. Fair exposures** | The sector and region pages reflect what the client's funds actually hold | G5, G6, started as a daily capture | yes: Bloomberg scope |
| **3. Long windows** | 10-year, 15-year and since-inception columns | G2 | yes: backfill extension |
| **4. Comparison and Multi** | Two-column and multi-column reports; sensitivity runs across comparisons at no vendor cost | reuse of 1 to 3 for each comparison key | none new |
| **5. Fund detail** | Fundamentals, bond breakdown, top-25 constituents, prospectus tables | G7, G8, G10, G11 | yes: SEC and issuer sources |
| **6. Acceptance and retirement** | One side-by-side per variant against a YCharts report of the same inputs, each difference named; then the YCharts calls stop | none | none (YCharts egress is already cleared for `2.0.0_SA_COO~Y`) |

Stage 6 is a one-time check. A standing comparison against YCharts is barred (CLAUDE.md, no shadow pipeline).

---

## 7. Risks

| Risk | Why it matters | What contains it |
|---|---|---|
| Wrong total returns from a mixed price series (G1) | The headline numbers would be quietly low for dividend payers | Fix the convention before stage 1 prints a return; the stage 6 side-by-side would also catch it |
| Coverage on portfolios unlike the reference case | 96 of 99 was measured on one Cottonwood portfolio; a prospect's file may hold securities Opal has never priced | The report states coverage per figure (the trace exists); first-seen securities are backfilled; a coverage floor decides print or "not available" |
| Mutual-fund look-through unproven (G6) | The reference portfolio has fund-shaped holdings; the Bloomberg allocation fields are proven on ETFs only | One probe on a handful of mutual-fund tickers settles it before stage 2 is scoped |
| Bloomberg quota and the single Terminal seat | Client-holdings universes are larger than Opal's ETF constituents; Andrew refused a 2,600-security pull | Pull only the union of live client holdings; measure the quota on the first extension |
| Method differences from YCharts | YCharts does not state its risk-free rate, return frequency or fee treatment (INHERITED) | Opal publishes its own method on the report; stage 6 names each difference once |
| Morningstar-defined elements (sector scheme, style box) | No licence, no data | State Opal's scheme (GICS sectors), replace or drop the style box |
| Contract change on a served page | `AnalysisReport` assumes a vendor PDF | The CTO's endpoint revision owns it; the served YCharts path stays up until stage 6 |
| Stale inputs go unnoticed | M6 was two months stale and nobody had read it | Each input's as-of date is printed on the report; a stale input fails the run instead of printing |

---

## 8. Decisions for Andrew, each with a recommendation

1. **Opal's own method, or a YCharts look-alike?** Recommend Opal's own: GICS sectors, Opal-defined market-cap
   buckets, no style box in the first version, each method stated on the page.
2. **Standing authorization for data pulls scoped to live client holdings.** Recommend one standing word covering:
   the Yahoo backfill extension, Bloomberg reference and fund-allocation fields for client-held tickers, and SEC
   public filings. Without it each stage after the first stops for a per-use word.
3. **Start the daily Bloomberg fund-allocation capture now, before the build.** Recommend yes: the fields have no
   history, so every day not captured is lost.
4. **Order of variants.** Recommend Overview first as the thread, then Comparison and Multi together, since they
   share every data need.
5. **The Bloomberg query-language entitlement (a purchase).** Recommend not buying it for this: SEC filings and
   issuer files cover fund holdings without it.

---

## 9. What this analysis does not claim

- **In-house run time is not measured.** No in-house run over the data mart exists yet. "Minutes to seconds" is the
  handoff's estimate and is INFERRED here.
- **No figure was compared with YCharts.** Whether Opal's computed returns match YCharts' on the same inputs is the
  stage 6 check, not a finding of this analysis.
- **No vendor or online source was called.** Yahoo depth before 2020, Bloomberg fund fields on mutual funds, SEC
  filing coverage and Bloomberg quota are all unprobed; each needs Andrew's word first.
- **The Comparison and Multi element classes are by rule,** not by census (handoff caveat). Their counts may move.
- **The fund share of the portfolio is a range** (39 to 83 percent of weight) because 38 holdings carry no kind label.
- **The handoff's statements about code and infrastructure were not re-read** except where section 2 says MEASURED:
  the Yahoo adjustment mix, the 84 index series, the resident host's renderer and the YCharts timings are INHERITED.
- **Why the risk-free object stopped updating is unknown** (row `IRPT_YCDGEN-S9`).

---

## REFS

```
  THIS FILE         docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md
  PROJECT           IRPT_YCDGEN (org/missions/D9/IRPT/IRPT_YCDGEN/); PRD v0.1 prd/IRPT_YCDGEN_PRD.md
  ORDER             org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_194xZ_YCHARTS_INHOUSE_FEASIBILITY_ANALYSIS.md
  INPUT             org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/HANDOFF_TO_CRO_ONPREM_GENERATION_20261005.md @d87bed6db6
  BASE BRIEF        docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md
  PRECEDENTS        org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_YCDGEN_ADDENDUM_A_DRAFT_HANDOFF_20261005.md section A
  SURPRISE ROW      IRPT_YCDGEN-S9 (risk-free object stale since 2026-08-05)
  SURFACES READ     maps/{overview,comparison,multi}_map.json, maps/overview_coverage.json; research/held_data.py,
                    research/layout_overview.py (function index); IRPT_MVP_Y/Y6/Y6_BACKEND_SUMMARY.md;
                    integrations/bloomberg/READ_HERE.md; S3 and DynamoDB reads listed in section 2
  OPEN FOR ANDREW   section 8, five decisions
  MEASURED AT       2026-10-05 19:3xZ to 19:4xZ
```
