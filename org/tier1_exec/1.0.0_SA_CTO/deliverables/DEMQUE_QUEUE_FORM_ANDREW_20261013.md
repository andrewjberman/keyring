# MDPF_DEMQUE queue form: Andrew's answers, item by item (kept by `1.0.0_SA_CTO~DELL1`, opened 2026-10-13 ~14:3xZ)

Source of facts: `deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md` @6132ed27c9. Law: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md`
(earliest client record, 365 days before need for non-client, 2012-01-01 floor, about a 2-week Bloomberg budget).

**Each item's form:** surface; who uses it; priority; history depth; field breadth; securities; schedule; budget; decision.

## Surface level (Andrew, 2026-10-13 ~14:3xZ)

> I agree with your recs on 1 and 2. Regarding 3, not sure what the issue is here, if these are needed for the research app they shouldnt be dropped, merely included in the research apps surface/needs.

1. **Surface order: A Production daily, then B Client history, then E Opal ad-hoc, then C Product history, then D Research.** AGREED.
2. **Opal ad-hoc reserve:** 10 pct of the daily Bloomberg allowance is held for surface E (requests through the Opal agent, currently `0.0.3_BG_BBGTerminal`). Any part unused by
   the day's ad-hoc requests is released to the other surfaces that day. AGREED.
3. **"Consumer: none found" is NOT a reason to drop.** The AMGT_RESAPP items (ABNB model block, ICT identity, the CRNCY scanner slices) are the RESEARCH APP's needs. Their
   consumer is recorded as **the research app (AMGT_RESAPP)**, under surface D's research-app needs. They are kept. The TR comparison (Andrew-direct 2026-10-09) and the
   Cottonwood 15-fund fill (ADVI_COTBKF) are likewise kept under their own owners' needs.

## Items

### Surface A: production daily (Andrew, 2026-10-13 ~14:4xZ)

**The 7:00 am ET (11:00Z) site Z job** (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`) runs four legs in order: the MODELS pull (the original pull feeding the dashboard's
market data and models), PUBLISH, the ETF pull, and the CONSTITUENTS pull. Each leg gets its own card.

#### A2 Daily ETF pull (`integrations/bloomberg/pipeline/etf_daily_pull.py`): APPROVED as written

> This is all correect. I also agree with the recommendation on the fund fields only for funds, please note that in some persistent plact on a document which we will append all our notes/decisions as some of this will need to go to sitez as the bloomberg device.

1. **Who uses it:** the Positioning page (the Opal ETFs and their holdings) and MDPF_SECHIST's per-security price history.
2. **Priority:** A, second (after the models pull, which runs first in the same job).
3. **History depth:** one day per run. Any security holding less than a year is topped up to 365 days before the need (`DEPTH_START_DAYS` 372 to 365).
4. **Field breadth:**
   - reference: about 15 fields (`NAME`, `FUND_EXPENSE_RATIO`, `FUND_TOTAL_ASSETS`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `TRACKING_ERROR`, `EQY_DVD_YLD_IND_NET`,
     `HB_OAS_EFF_DURTN`, `YAS_ISPREAD_TO_GOVT`, `BETA_ADJ_OVERRIDABLE`, the GICS sector and industry fields, `CNTRY_OF_DOMICILE`, `CUR_MKT_CAP`);
   - history: `PX_LAST`, `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`, and the total-return level;
   - Opal funds only: `PX_LAST`, `FUND_TOTAL_ASSETS`, `FUND_NET_ASSET_VAL`, `EQY_DVD_YLD_IND_NET`, `BETA_ADJ_OVERRIDABLE`.
5. **Securities:** 172. That is the 4 Opal ETFs (DIVZ, IDVZ, PFDE, PFOE), their 166 constituents (re-derived daily from `silver/holdings`), and GLD and VXX.
6. **Schedule:** daily at 7:00 am ET, trading days, for the prior trading day.
7. **Budget:** about 2,600 reference cells and about 520 history cells a day, plus small one-off depth top-ups (412 estimated on 10-12, under a 120,000 limit).

**DECISION, Andrew-approved: FUND FIELDS ONLY ON FUNDS.** `FUND_EXPENSE_RATIO`, `FUND_TOTAL_ASSETS`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT` and `TRACKING_ERROR` are requested
only for funds (the 4 Opal ETFs plus fund-type extras), never for the 164 single stocks, which return NOT_APPLICABLE (manifest `field_exceptions`, 2026-10-09). That
cuts about a quarter of the leg's reference cells with no loss.

**Site Z:** today's 7:00 am ET run (as-of 2026-10-12) did not land (no `bbg/2026-10-12/` at 14:4xZ). Andrew: "that is already being rectified on sitez".

#### A3/C1 Rival Funds daily run (ETFS_RIVALS, 7:00 am ET / 11:00Z vehicle at site Z): APPROVED, with both recommendations

> I aprove your recommendations. Regarding ACWI and IWM, we do not need full holdings depth for these.

1. **Who uses it:** the Rival Funds page (13 rival funds set against the Opal funds).
2. **Priority:** today's data is A, third (after the models pull and the ETF pull). History still owed is C.
3. **History depth:**
   - holdings and market data: the prior trading day only;
   - dividends: see the DECISION below;
   - history still owed: 365 days before the need.
4. **Field breadth:**
   - holdings: one multi-fund Excel BQL query a day (`id`, `name` per holding);
   - dividends: `DVD_HIST_ALL` and `DVD_CRNCY`;
   - market: GICS names and codes, `PX_LAST`, `CRNCY`, `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`;
   - history still owed: the close only.
5. **Securities:** every holding of the rival funds (742 securities owed history on 10-08).
6. **Schedule:** daily at 7:00 am ET, trading days, for the prior trading day.
7. **Budget:** its own ceiling of 150,000 rows a day, 30,000 of them reserved for production. History still owed is capped at 20,000 cells a run.

**DECISION, Andrew-approved: DIVIDENDS ONCE, THEN INCREMENTAL.** Today `enrichment_bloomberg.py` re-pulls `DVD_HIST_ALL` over `DEFAULT_WINDOW_DAYS = 730` for every
security, every day. Instead:
- ONE pull of 365 days per security, when it first enters the universe;
- after that, a daily window of only the last few trading days.

**DECISION, Andrew: ACWI and IWM do NOT need full holdings depth** (about 2,200 and 2,000 holdings a day today).

**ACWI and IWM: REMOVED from the rival-funds holdings pull** (Andrew, ~16:2xZ: "we do not need to track these for Rivalfunds, we do not need holdings data for these in any context, they arent even displayed on Rivalfunds").

#### A4 Research app daily pull (AMGT_RESAPP, `integrations/bloomberg/research/price_axis_pull.py`, about 9:00 am ET at site Z): APPROVED, with its recommendation

> Approved as well as recommendations for A4. In general I think the last 5 trading days is a good incrememntal strategy as a means to cover potential trading holidays/missed data for whatever reason/etc, across the various surfaces once we move to incremental mode (after backfill is already covered for the relevant needs). I also aree with model data depth on financials back to 2016. Regarding ACWI and IWM, we do not need to track these for Rivalfunds, we do not need holdings data for these in any context, they arent even displayed on Rivalfunds.

1. **Who uses it:** the research app (each covered company's 30, 90 and 365-day price rankings and breakout flags).
2. **Priority:** A, fourth.
3. **History depth:** `WINDOW_DAYS` 30 is re-pulled daily today. It becomes INCREMENTAL (the rule below); the stored year is extended by `price_series_persist.py`.
4. **Field breadth:** `PX_LAST` only.
5. **Securities:** every covered company (about 100, counted at the next run).
6. **Schedule:** daily, trading days, after the 7:00 am ET job.
7. **Budget:** about 3,000 history cells a day today, about 500 under the incremental rule.

**DECISION, Andrew: research-app model data (`model_block_pull.py`, `HIST_START` 2016-01-01) keeps fiscal-year financials back to 2016.** This is a named exception to the
365-day non-client rule: a company model needs several fiscal years. The pull is one-time per newly covered company (about 1,000 cells; ABNB is 989).

#### A5 ETF breakdown pull (`integrations/bloomberg/pipeline/etf_constituents_pull.py`, the 7:00 am ET job's last leg): APPROVED as is

> A5 is good as is.

1. **Who uses it:** the Positioning page (each Opal ETF's sector and country breakdown, and its holding weights).
2. **Priority:** A, fifth.
3. **History depth:** today only. Bloomberg returns no history for these derived fields (measured 2026-08-24), so a missed day is lost and cannot be refilled. **This is the one
   named exception to the 5-day incremental rule.**
4. **Field breadth:**
   - reference: `NAME`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `FUND_PCT_TOP_TEN_HOLD`;
   - bulk: `HB_INDUSTRY_SECTOR_ALLOCATION`, `HB_GEO_CNTRY_ALLOC`;
   - one BQL `holdings().weights` query per fund.
5. **Securities:** the 4 Opal ETFs (DIVZ, IDVZ, PFDE, PFOE).
6. **Schedule:** daily at 7:00 am ET, trading days.
7. **Budget:** about 20 reference cells and about 170 holding rows a day.

### Surface B: client history (Andrew, 2026-10-13 ~16:4xZ)

> I would prefer to rely on BBG for this generally rather than yahoo finance because I don't trust resolution for yahoo finance. There should be a "porting" mechanism, where if the reformulated yahoo finance pricing (price + dividend/interest/etc, i believe they call it "adj close" or something like that), is within 10bps of the bloomberg price on some several test intervals, then we can use the yahoo finance price.

**DECISION, Andrew: BLOOMBERG IS THE DEFAULT SOURCE FOR CLIENT HISTORY. A security may use Yahoo only after it passes a PORTING TEST against Bloomberg.**
- The comparison is Yahoo's adjusted close (split and distribution adjusted) against Bloomberg on the same security.
- It must agree within 10 bps on several test intervals.
- The exact test is proposed by this seat below. It stays OPEN until Andrew confirms it.

**Proposed porting test** (this seat, for Andrew's confirmation):
- **Compare returns, never levels.** Yahoo's adjusted close is re-based backward at every dividend, so its LEVEL moves while its returns do not.
  - Interval return, Yahoo: `adjclose(end) / adjclose(start) - 1`.
  - Interval return, Bloomberg: `TOT_RETURN_INDEX_GROSS_DVDS(end) / TOT_RETURN_INDEX_GROSS_DVDS(start) - 1`.
- **Pass:** the two returns differ by at most 10 bps (0.10 percentage points) on EVERY test interval. One miss fails the security.
- **Intervals:** 5 per security, a deterministic sha256 draw over the security's own held window, with lengths of 1 month, 1 quarter and 1 year plus 2 drawn lengths. No
  interval may start before the security's first held date.
- **Cost:** at most 10 Bloomberg cells per security (2 endpoints by 5 intervals).
- **A pass ports the security to Yahoo.** It is re-tested only when Yahoo restates the security (a split or another corporate action). A fail keeps the security on
  Bloomberg at the B1 depth.

**CONFIRMED, Andrew (~16:5xZ):** the porting test as proposed above, and Yahoo-sourced client prices already stored read **UNVERIFIED** until their security passes.

> The premise is that we always need to account for TWR pricing on ALL surfaces, so if Yahoo can accomodate that and its proven to be accurate within some interval, then great, we can manage that. Moving to your recs, yes that is correct.

**STANDING RULE, Andrew: TIME-WEIGHTED RETURN (TWR) PRICING ON EVERY SURFACE.** Every price series a surface keeps must support a total-return (TWR) reading: price plus
distributions (dividends, interest), not price alone. Yahoo is admitted only through the porting test, which compares total returns.

**This seat's census against that rule** (field lists as carded above; "n/a" is a series that is not a priced security):

| item | total return today | gap |
|---|---|---|
| A1 models pull | daily and monthly `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` on indices and model ETFs; macro levels n/a | none |
| A2 ETF pull | `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` and the total-return level | none |
| A3 rival funds, today's data | `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`, plus dividend history | none |
| A3 rival funds, history still owed | the close only | **GAP**: add the total return field |
| A4 research price axis | `PX_LAST` only | **GAP**: add the total return field (about 500 cells a day at 5 days) |
| A5 ETF breakdown | n/a (allocations, not prices) | none |
| B1 Cottonwood history | `PX_LAST` only | **OPEN**: the basis is a decision (below) |
| B2 Yahoo client history | the close, and adjusted close where stored | the porting test |


**Porting test, short held windows** (this seat's ruling on `2.0.0_SA_COO~Q1` msg 4975; the test is built @567a058ddb: 326 securities, 2,497 cells, no draw):
- 182 of the 326 held windows are under a year. The test still uses **5 intervals**, Andrew's "several".
- A fixed length (1 month, 1 quarter, 1 year) that does not fit the held window is replaced by a sha256-drawn length that does. Overlap is allowed, the minimum interval is 5
  trading days, and every interval must be within 10 bps.
- A held window under 10 trading days stays on Bloomberg as **UNTESTABLE** (a reason, not a FAIL).
- The adjusted close is reformulated from the store: the as-traded close, with split-undone gross dividends reinvested on the ex-date close.

**Porting-test size** (`2.0.0_SA_COO~Q1` msg 4947):
- **326 securities** have Yahoo-sourced client prices landed today: 3,260 cells, about 1.2 days of allowance.
- **965 are requested** across items 11 to 17: 9,650 cells, about 3.6 days.
- **The 8 mutual funds Yahoo rejected in the Cottonwood 15-fund fill are NOT in CARD-A's 606:** ABNFX, AGTHX, BALCX, MEIIX, NFFFX, PRILX, VEIRX, VGHAX. They have no
  price source until a Bloomberg request is filed for them under B1.

### Andrew, ~17:2xZ: "Go with your rec." This seat reads it as covering all five open recommendations

> Go with your rec.

1. **A1 MODELS PULL** (`integrations/bloomberg/pipeline/tplus1/src/market_indices_data_pull.ipynb` and `model_portfolio_regression_analysis.ipynb`, the first leg of the 7:00 am ET
   job): **APPROVED with the incremental change.**
   - Card: it feeds the dashboard's market data and models. Its 152 market and macro series (daily price and total return; monthly valuations back to 1989-12-31) and the
     model portfolios' ETFs and benchmarks (6 years) are re-pulled in full every day today.
   - Change:
     - keep each series' history stored once;
     - daily pull = the last 5 trading days;
     - monthly series = the latest month-end plus month-to-date only;
     - valuation fields at month-end only;
     - model ETFs on the same 5-day rule.
   - Add a real meter: today the run logs as rows-unreadable.
2. **B1 COTTONWOOD DEPTH: option (c)**, the dates money moved plus month-ends (daily after 2026-04-22, where Black Diamond has data). Floor: max(first held date, 2012-01-01).
3. **$1.00 MONEY MARKET FUNDS SKIP BLOOMBERG:** each of the 227 cash equivalents is checked against its fund type. A fund whose price is fixed at $1.00 is priced at $1.00 with
   that reason on the value, and is not pulled. UNREAD types are pulled.
4. **THE COTTONWOOD PRICE BASIS:**
   - 595 securities use `PX_LAST` plus the client's own recorded income (11,154 dated rows, `2.0.0_SA_COO~Q1` @54a77c0e82);
   - the 11 long-held Fixed Income names with no income rows also get `TOT_RETURN_INDEX_GROSS_DVDS` (2,492 cells, 0.9 day).
5. **THE 8 MUTUAL FUNDS YAHOO REJECTED JOIN B1:** ABNFX, AGTHX, BALCX, MEIIX, NFFFX, PRILX, VEIRX, VGHAX. Bloomberg from their first held date (the 15-fund fill starts
   2020-07-06), at the same depth (c), on the same basis.
- **Also ruled (not part of the form): restart 2.0.0_SA_COO~W1 and 2.0.0_SA_COO~V1; the three CloudOps seats stay down.**

**B1 total at this depth: about 13 days of the daily allowance** (12 for the 606, plus under 1 for the 11 bonds' total-return field, plus the 8 funds), less the $1.00 funds.

**A4 amendment (bj-5, `2.0.0_SA_COO~R1`; via `2.0.0_SA_COO~Q1` msg 4980):** the price axis also pulls `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` over the last 5 trading days, about
+500 cells a day (A4 about 1,000 a day). **This seat's ruling: the field accrues FORWARD ONLY. No 365-day back year is pulled (it would be 25,100 cells, 9 days).** The rankings
stay on price. If a back year of total return is ever needed, it is derived from the stored `PX_LAST` year plus `DVD_HIST_ALL` (about 100 bulk requests), with dividends
reinvested on the ex-date close, the porting test's formula.

## STANDING RULE, Andrew: INCREMENTAL MODE = THE LAST 5 TRADING DAYS, on every surface

Once a need's backfill is complete, every daily pull asks for **the last 5 trading days** (from `lib/trading_calendar.py`), not a single day and not a long window. That
covers holidays, a missed run and late vendor corrections. A security with a gap wider than 5 trading days gets a targeted refill for just that gap, never a wider
standing window. It applies to every surface (A through E) after its backfill is covered.
- **Yahoo reading** (this seat, on `2.0.0_SA_COO~Q1` msg 4935): a 5-day window saves no Yahoo request (one request per symbol either way). The rule still applies:
  - the last 5 trading days normally;
  - a FULL re-pull of a name only when a split or another restatement lands, as the targeted refill.
  It is a served change under its own pair.

## FOR SITE Z (the Bloomberg device): changes to carry, appended as decided

| # | change | file | source decision |
|---|---|---|---|
| Z1 | Fund-only fields (`FUND_EXPENSE_RATIO`, `FUND_TOTAL_ASSETS`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `TRACKING_ERROR`) are requested only for funds | `integrations/bloomberg/pipeline/etf_daily_pull.py`, the `CHAR` request | A2, Andrew 2026-10-13 |
| Z3 | Dividends: one 365-day `DVD_HIST_ALL` pull per security on first entry, then the last 5 trading days daily (replacing the 730-day daily re-pull) | `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (`DEFAULT_WINDOW_DAYS`, `build_plan`) | A3 plus the incremental rule, Andrew 2026-10-13 |
| Z4 | ACWI and IWM REMOVED from the rival-funds holdings pull entirely (not displayed; no holdings needed in any context) | `data/etfs/scripts/rivalfunds/collector_bloomberg.py` and the rival-funds universe | A3, Andrew 2026-10-13 |
| Z5 | The research price axis pulls the last 5 trading days daily (not 30), with stored history extended by `price_series_persist.py` and a targeted refill for any wider gap | `integrations/bloomberg/research/price_axis_pull.py` (`WINDOW_DAYS` for the daily pull) | A4 plus the incremental rule, Andrew 2026-10-13 |
| Z6 | INCREMENTAL MODE everywhere: once a need's backfill is complete, daily pulls ask for the last 5 trading days | every site Z daily pull (the ETF pull's history top-up, rival funds, research, the models pull) | the standing rule, Andrew 2026-10-13 |
| Z2 | `DEPTH_START_DAYS` 372 becomes 365 (non-client need: 365 days before the need; the trading calendar resolves the first business day) | `integrations/bloomberg/pipeline/etf_daily_pull.py` | backfill law ADDENDUM 2 item 4 |
| Z7 | Client-history porting test (Yahoo adjusted close against Bloomberg total-return index, 5 intervals, 10 bps, at most 10 cells per security), drawn through the queue under surface B | the DEMQUE drawer (the request is filed by `2.0.0_SA_COO~Q1`) | Surface B, Andrew 2026-10-13 (the test is pending his confirmation) |
| Z8 | The models pull goes incremental: last 5 trading days daily, the latest month-end plus month-to-date for monthly series, valuations at month-end only, with stored history | `integrations/bloomberg/pipeline/tplus1/src/market_indices_data_pull.ipynb`, `model_portfolio_regression_analysis.ipynb` (both copies: `tplus1` and `tzero`) | A1, Andrew 2026-10-13 |
| Z9 | The models pull gets a real meter (rows read from the run, not rows-unreadable) | `data/mdpf/scripts/demque/bbgtml_meter.py`, `integrations/bloomberg/pipeline/tplus1/tools/run_daily_pull.py` | A1, Andrew 2026-10-13 |
