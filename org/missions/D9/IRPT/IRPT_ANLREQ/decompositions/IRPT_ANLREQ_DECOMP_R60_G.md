# IRPT_ANLREQ round 60, workstream ~G (ENGINE) -- decomposition: FWD-10 (Core), the Multi-Comp and Comparison reports on Opal's own math

Issuer `2.0.0_SA_COO~G2`, 2026-10-20. PRD v0.25 @b83ce81b5b (both halves SIGNED, CTO msg 11442). Outcome served: **FWD-10**; FWD-12 rides it (a part Opal cannot fill says so in words). FWD-11 (parity) follows once FWD-10 is met and is NOT in this round.

**Input.** PRD C-MODEL-SOURCE and the CTO's R1 (record `deliverables/1.0.0_SA_CTO~DELL2/CTO_RULINGS_MODEL_WEIGHTS_SWAP_AUDIT_20261020.md`, key corrected @b9de1e559d); CRO brief `docs/briefs/irpt-anlreq-report-engine-core-then-parity-brief-20261020.md` O2; trace `0.9.0_WK_IRPT_ANLREQ~304/MODEL_COMPOSITION_TRACE.md`.

## What was measured before the cut (this seat, 2026-10-20, read-only)

- **The model return series exists at the corrected key, the positioning surface at the second.** `opal-data-portal-v2`: `json/benchmarks/model_portfolio_timeseries.json` (plain JSON, 780,910 B, 3,225 rows, codes UST/ST/INT/LT/ULT, inception 2024-04-30, `data_as_of` 2026-10-19) and `json/positioning/positioning_data.json` (**gzip-compressed JSON**, 6,890 B; `portfolios.<code>.allocation` = percent by asset class, `current_holdings.<code>.holdings` weights sum 1.0, `data_as_of` 2026-10-19). The resident has no grant on either (trace Q5).
- **The comparison and multi maps cannot carry FWD-10 as they stand.** They were made from samples with a FIXED number of comparables: the comparison map has one comparison slot, the multi map has TWO (`key_index` 1 and 2 only), and each element label bakes in the sample's comparable name ("Alpha Opal Ultra Long-Term", "Beta iShares Russell 2000 ETF"). A filer may pick up to FIVE comparables (`submission.py:67-72`), and FWD-10's own example is three (two Opal models and one ETF). Re-pointing the map's elements would therefore serve at most two comparables, under the wrong names.
- **Run `produce` already drops every vendor-call and builder-only element** from the report document and counts them in one NOT_SHOWN line (AR-y-408), and appends its own elements after the last page (the three classified elements, the price table). The resident already carries `report_variant` (overview / comparison / multicomp) and refuses a variant with no map binding (`OPAL_MAP_BINDINGS`, `resident_installed.py:74`).

## Design (ruled here, inside this decomposition)

FWD-10 is built as ONE Opal-authored **comparison section**, appended after the last page exactly as the price table is, for every report that has comparables: five elements `opal.compare.window|chart|returns|risk|allocation`, N-comparable-capable (1 to 5), each comparable named from the catalogue entry the filer picked. The YCharts-structured pages of the comparison and multi maps stay as they are (their vendor-call elements are dropped and counted); FWD-11 (parity) is where they are re-pointed. The two maps are already packaged and bound (AR-g-85: `build_resident_package.py` carries `comparison_map.json` and `multi_map.json`; `OPAL_MAP_BINDINGS` has `opal_map_comparison` and `opal_map_multicomp`), and the whole `ycharts/research` directory is a package member, so the new modules ride the next resident release with no manifest edit.

- **Common window (stated on the page).** START = the latest first observation among the portfolio and every comparable that has a series (a model's first observation is no earlier than its inception, 2024-04-30); END = the earliest last observation among them. A comparable with no series is left out of the window and reads `not available for <name>: <reason>` (FWD-12). All lines are rebased to 100 at START.
- **Periodic total returns** (1m, 3m, YTD, 1y, 3y, 5y, 10y) are computed on the rebased common-window path; a period longer than the window reads `n/a` for every row.
- **Risk figures** (standard deviation, Sharpe, Sortino, max drawdown, alpha, beta) are monthly-return statistics over ONE period for all rows: N whole years = min(5, floor(window years)); N < 1 -> every risk figure reads `not available: the common window is shorter than 1 year`. Reference: benchmark SPY (alpha, beta) and risk-free BIL (alpha, Sharpe, Sortino), the same series and wording as the Overview.
- **Asset allocation, side by side.** Portfolio: the existing `ALLOCATION_ASSET_CLASS` weights. Opal model: `portfolios.<code>.allocation` of the positioning surface, **dated on the page** with that file's `data_as_of`. ETF: 100 percent in its classified asset class (the classifier row), stated in words.
- **Prices.** An ETF comparable is priced through the existing chain (`price_source.resolve_prices`: estate, yfinance, ycharts) over the same window; a model comparable reads `model_source`. No new vendor call. R8: no vendor name on the page.
- **Which comparables.** From the accepted request's frozen configuration (`comparison_keys` resolved through `comparison_catalog`, the same guarded read the vendor job uses: `frozen_worker.py:95`), never from the browser. A catalogue key maps to a model code ONLY through the committed `model_code_map.json` (no display-name matching).

## The frozen contracts (every cell builds to these; they are inlined in each order)

**K1 `ycharts/research/model_source.py`** (pure; the bytes are injected):
`BUCKET="opal-data-portal-v2"`, `SERIES_KEY="json/benchmarks/model_portfolio_timeseries.json"`, `POSITIONING_KEY="json/positioning/positioning_data.json"`, `CODES=("UST","ST","INT","LT","ULT")`, `class ModelSourceRefused(ValueError)`;
`code_for_key(catalogue_key) -> code | None`; `read_series(get_bytes) -> {"as_of","inception","series":{code:[[epoch_ms, level],...]}}` (level 100.0 on a code's first date, every later date multiplies by 1 + model_return, ms = UTC midnight); `read_allocation(get_bytes) -> {"as_of","allocation":{code:{"Cash","Fixed Income","Equity","Hedge","Structured","Commodities","Alternatives": percent}}}`. `get_bytes(key) -> bytes` (gzip detected by magic bytes). A missing key, a non-JSON body or a changed shape raises `ModelSourceRefused`.
**K2 `ycharts/research/comparables.py`** (pure): `build_compare(portfolio, comparables, benchmark, risk_free) -> record`; `build_allocation(portfolio_classes, rows) -> table`. `portfolio = {"name","series":[[ms,level]...]}`; each comparable `{"key","name","kind":"model"|"ticker","series":[[ms,level]...]|None,"reason":str|None}`; benchmark / risk_free `[[ms,level]...]|None`. Record: `{"window":{"start","end","years","rule"},"rows":[{"name","key","kind","status":"VALUE"|"NOT_AVAILABLE","reason","path":[[ms,level]...],"returns":{"1m","3m","ytd","1y","3y","5y","10y"},"risk":{"years","std_dev","sharpe","sortino","max_drawdown","alpha","beta"}}]}`, row 0 the portfolio. Allocation table: `{"classes":[...],"rows":[{"name","weights":{class:percent},"as_of":str|None,"basis":str}]}`.
**K3 layout** (`layout_overview.py`): computed methods `COMPARE_WINDOW`, `COMPARE_CHART`, `COMPARE_RETURNS`, `COMPARE_RISK`, `COMPARE_ALLOCATION`; `compute_all(..., compare=None)` and `compute_element(..., compare=None)` take `{"record": K2 record, "allocation": K2 table}`; with pricing off each reads NOT_AVAILABLE / NOT_IN_THIS_VERSION; the HTML names every row and prints `not available for <name>: <reason>` for a NOT_AVAILABLE row.
**K4 stores** (`opal_producer.produce`): `stores["comparables"]` = the ordered list of catalogue entries (`key`, `label`, `ticker` or None); `stores["model_bytes"]` = `callable(key) -> bytes`. Compare elements are appended only when `comparables` is non-empty AND pricing is on.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-171` | K1 `model_source.py`, the committed `model_code_map.json`, tests | those three files | WORLD (resident package member) |
| `AR-g-172` | the Terraform read grant: GetObject on the two keys, resident role, plan only | `ycharts/iam.tf`, the changelog, the worker folder | WORLD |
| `AR-g-173` | K2 `comparables.py` with its tests | those two files | WORLD |
| `AR-g-174` | K3 the five computed methods, their HTML, `compare=` plumbing, tests | `layout_overview.py`, one test file | WORLD |
| `AR-g-175` | K4 the producer stage, the resident's comparables and model-bytes ports, tests | `opal_producer.py`, `resident_worker.py`, `resident_installed.py`, tests | WORLD |

## Edges and chains

Real data dependencies: 173 consumes the K1 series shape; 174 consumes the K2 record; 175 consumes K1, K2 and K3. 172 is independent of all. Two chains: **chain A** = AR-g-171 -> AR-g-173 -> AR-g-174 -> AR-g-175 (one worker queue, in that order; the contracts above are frozen so each order tests against fixtures); **chain B** = AR-g-172 (its own worker). `fanout: 2 of 2 chains, cap 8`.

## After the drain (not cells; the issuer's steps)

The never-widen pair for the grant (COO + CTO halves), the Terraform apply (CloudOps `safe-apply`), the FWD-10 resident release (the next `r34*` under its own pair), then the one real run: a Multi-Comp filed on the live product (two Opal models and one ETF) read page by page against the independent arithmetic. A real-data control on the two source objects is run at the drain (the checker's fixtures are synthetic).

## Four-postulate record

(i) Domain: the FIVE elements FWD-10's DONE WHEN names (window, chart, returns, risk, allocation) over up to five comparables; the denominator of comparables is the filer's list (1 to 5), printed on the page; the maps' vendor-call counts (Comparison 351, Multi 144) are NOT this round's domain (FWD-11). (ii) One grain per element: a row per portfolio or comparable. (iii) One intent: a reader answers "did this portfolio beat each model I picked, and with how much risk". (iv) What this cut does NOT move: the Overview, the price pages, the maps' vendor-call elements, the Ticket Center, the resident's Overview binding.

fanout: 2 of 2 chains, cap 8, reason: chain A is a data-dependency chain of four cells on frozen contracts; chain B is the independent infrastructure grant.
