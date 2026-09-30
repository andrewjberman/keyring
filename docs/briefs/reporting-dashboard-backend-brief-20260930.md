# BRIEF: the client reporting dashboard -- BACKEND (gold shape, total return, serving)

- Author: `4.0.0_SA_CRO` (base), 2026-09-30. Mode: NEW (L1). Consumer: `1.0.0_SA_CTO` (L2 endpoint, L3 register, L4 PRD); execution by `2.0.0_SA_COO~P` (Andrew's seating: backend on ~P, frontend on ~D, run in concert).
- Companion: `docs/briefs/reporting-dashboard-frontend-brief-20260930.md` (the views and how they read this backend). Neither brief is complete without the other.
- Andrew's words, verbatim, in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md` (request, scope answers, gold-is-the-Opal-shape, total-return rulings; @88b526bf27, @3b6d4b4b71, @ebb66316e0). The COO~P record that started it: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_052xZ_PRECOMPUTED_GZIP_JSON_REPORTING_UNDER_2S_AND_PUSH_MANAGED.md` @6f884618c3.
- Claim classes: READ (file:line seen, by this seat or a research subagent of this seat, not each re-opened), MEASURED (a call run), PROPOSED (this seat's design), OPEN (needs a ruling), ABSENT (searched, scope stated). Every path below is a SHAPE: real addresses are `lib/opal_naming.py address()` output (CLAUDE.md rule 30).
- Standing law this brief obeys: **gold is the one Opal shape and the adapter layer** (annex rule 17c, landed @1fef5f680e; Andrew's words in the record above): bronze holds each source's raw shape, silver holds it typed and de-duplicated in the source's own shape, gold coalesces every firm into ONE Opal shape with one schema contract file per gold table under `org/standards/`; **serving JSON is platinum**, gold stays parquet (annex 17b).

## PART I -- THE OUTCOME TERRITORY

### The candidate thread (for FWD-1)

**O1. An advisor opens one 49 Financial account and sees its daily total-return history, and picks any start and end date, and the answer is on screen in under two seconds, with nobody having run anything that day.** One account, one firm, one real day's data, end to end from custodian file to a chart. It is the thread round 1 builds. It is chosen because 49 Financial has the deepest data (Andrew: 49 Financial first).

### The rest of the territory

**O2. Any account of any firm the gold covers loads the same way.** Inflection and Cottonwood join through their adapters into the same gold shape; nothing in the served files says which firm's plumbing produced them.
**O3. A person sees how each asset class performed, and how the asset-class mix changed between two dates,** using Opal's canonical ETF-Classifier classes (five classes plus Cash, Other and Unclassified in the portal).
**O4. A person sees realized and unrealized gain over any window, and an activity summary for it:** beginning value, contributions, withdrawals, gain or loss split market realized, market unrealized and income, ending value.
**O5. A person sees the transactions,** date, asset, action, type, symbol, units, price, amount, custodian, for any account and window.
**O6. At the biggest drawdown in the chosen window, a person sees the topics that were trending then** (Cottonwood asked for this; Andrew's signature view).
**O7. A household or a client is the sum of its accounts, built from the account grain,** with no separate pipeline.
**O8. A return figure a person can defend.** It is total return on a conservative GIPS methodology, gross of fees and labelled so, and a day the data cannot support says so instead of showing a wrong number.

### Out of scope (Andrew, scratched)

Net worth, held-away accounts and liabilities. The activity summary does not toggle to a net-worth view. Fees are not computed (a rail is reserved, section 5).

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the Opal-shape gold tables for reporting, their schema contract, the per-firm adapters into them, the total-return method, the platinum publisher that builds the served files, and the acceptance of the served numbers.

**It relies on, and does not own:**

| Sibling | Relationship |
|---|---|
| `IRPT_BCKEND` (COO~P; D9) | The existing holdings-based performance gold and the performance adapter (`irpt-performance-adapter`); this project extends its gold and retires nothing in it without that project's word. |
| `MDPF_SECCLASS` (D8) | The canonical classification table `etf-classifications`; this project reads it and adds no classification. |
| The news pipeline (DS_MarketIntelligence) | Daily topic tables and reports; this project reads them. |
| `LGIC_NAMING` / `LGIC_CANON` (D14) | Every address and name; a builder refusal is a registry row to add. |
| `OPAL_ASSETS` conversion (silver) | The typed silver this project's adapters read. |
| `IRPT_FNTEND` and the portal | Consumers; the frontend brief is theirs. |

## PART III -- THE QUALITATIVE BAR

- **O1 passes when** Andrew picks an account and two dates on a page and sees a total-return curve within two seconds, the next morning, with no one having started a job. It fails if a date range triggers a computation on the server.
- **O2 passes when** the same view loads for an Inflection account, and a reader cannot tell from the file which firm produced it.
- **O8 passes when** the 49 Financial total return for an account and window agrees with Black Diamond's own time-weighted return within a tolerance Andrew accepts, and every day where they disagree carries a stated reason. Today Opal's price-only figure sits a median of about 1.6 points below (READ, `TO-IB-er-302` proof).
- **O6 passes when** Andrew looks at the deepest drawdown of an account and the topics shown are ones he recognises from that week.

## PART IV -- THE SUBSTRATE: FINDINGS (READ, research subagents, 2026-09-30)

1. **The tiering is already ratified,** and it settles the serving question: bronze raw, silver typed parquet, gold parquet in a per-firm or per-product bucket, platinum JSON as the ONLY JSON producer; client-confidential platinum lives in the firm bucket (`docs/doctrine/CLAUDE_ANNEX.md` 17b; `infra/logic/02_DOCTRINE.md` tier table, R6). So the "precomputed gzipped JSON in under 2 s" is a PLATINUM product built from Opal-shape gold parquet.
2. **The naming builder resolves the address shapes** for all three firms: `address("irpt","<firm>","gold","reporting","account=<id>")` returns `s3://opal-data-<firm>/irpt/<firm>/gold/reporting/account=<id>`; `date=YYYY-MM-DD` resolves too; a partition with a slash (`account=X/date=D`) is refused (READ, COO~P and a subagent's read-only calls). No table called `reporting` is registered in `reporting_policies.json` (ABSENT); `address()` accepts any table name, so registration is the CTO's policy step.
3. **The existing daily performance gold is per account and price-only** (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py:12-29`): weight-pro-rated price return over end-of-day holdings, "NO inflow/outflow term", positive cash in the denominator at zero return; columns `account_id, business_date, daily_return, account_value, excluded_count, excluded_weight, status` (+ `leveraged`, `negative_value`, `held_count`). It covers 49 Financial for 557 trading days (2024-07-09 to 2026-09-25) (`TO-IB-er-202`); Inflection and Cottonwood golds are marked complete. It has no asset-class column, no flows, no income, no gains.
4. **Its label is wrong.** It is served as `TIME_WEIGHTED`, `NET` (`holdings_gold.py:259`) and the portal shows "Time-weighted, net of fees" (`MethodAndSources.tsx:32-63`), but it carries no fees and no income.
5. **Latency baseline** (COO~P, `PERFORMANCE_REPORT_LATENCY_AND_DAILY_HOLDINGS_ASSESSMENT_20260930.md` @f0b8685a15): a fresh report takes a median 6.7 s, p90 15.2 s; 84% is the read of one file per date, about 24-28 ms per date; since-inception is about 13.6 s. Recommended: a per-account series object (gzipped JSON or parquet), estimated under 1 s. Only 49 Financial has a scheduled daily producer today.
6. **Data by firm** (register `docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md:75-97`):
   - **49 Financial (Schwab master):** daily positions `dim_position` since 2024-07-08 (559 partitions), `dim_balance`, transactions `fact_trn` (about 130 columns) with a classified code table (187 codes), open lots `fact_uln`, realized lots `fact_rld`, accounts and a household union-find (7,039 accounts into 3,289 households, currently in an older bucket tree).
   - **Inflection (Orion):** positions since 2020-04-24, accounts (`accounts_v2`, with `household_id`), transactions with 47 type ids and a ratified cash-flow taxonomy (`orion_cashflow_taxonomy.yaml`), cost basis only as totals; NO realized-lot detail in either Orion product; Eclipse tax lots are not ingested and unconfirmed as populated; whether Orion's own returns include dividends is not established.
   - **Cottonwood (Black Diamond):** holdings since 2026-06-09, allocations and transactions since 2026-04-22, open and realized lots ingested (silver `fact_unrealized`/`fact_realized`), income on transactions. Black Diamond's own `performancePeriod` returns time-weighted and money-weighted returns with income in net gains; `performanceSeries` returns a daily series; an `activitySummary` endpoint carries the screenshot's fields (contributions, withdrawals, fees, `marketRgl`, `marketUgl`, income, values). The last is not ingested; IRPT calls the first two one account at a time behind a per-use gate.
7. **Total-return machinery exists only in part** (READ): a retiring flow-based 49F engine (`runners_49f/c02_twr_engine.py`: r = (EMV - CF)/BMV - 1, end-of-day flows, income left inside EMV; retired by `IB-pr-201`); a draft spec `docs/research/bd_dashboard_teardown/FACT_ACCOUNT_RETURN_BUILD_SPEC_20260721.md` (daily TWR geometrically linked, Modified-Dietz alongside, income split dividend/interest/coupon, lot-based P&L, `recon_residual` guardrail; a non-build draft held for CTO ratification; no emitted table found); the Schwab code table `SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`; the flow ledger `c00_flow_ledger.py` (EXTERNAL / INTERNAL / FEE-MANAGEMENT / FEE-ADMIN / UNRESOLVED, no income class).
8. **News, for the signature view** (MEASURED 2026-09-30): `opal-news-trending-daily` has curated topics (about 20 a day, headline, keyword, score, sentiment) from 2025-11-21 with 199 of the last 200 calendar days present; `opal-data-news-v2 trending_reports/YYYY/MM/DD/*` has the weighted phrase list (`trending_topics[]`: keyword, mention count, trending score, sentiment, `is_phrase`) from 2025-12-01; `affected_tickers` is EMPTY on every 2026 date probed, so topics cannot be filtered to a portfolio; the keyword drilldown files keep only a rolling 14 days. Prior art: `irpt-narrative` already finds peak, trough and recovery episodes in a daily return series (trough of at least 50 bp and 2 days; rolling 5-point moves of at least 50 bp) and reads the seven days of topics before each event (`narrative/events.py`, `evidence.py`).
9. **Asset classes** (READ): `etf-classifications` (DynamoDB, key `ticker`): fixed_income, equity, commodities, structured, alternatives; the portal adds cash, unclassified, other (`portal/.../holdings/assetClass.ts:30,66-76`). No row means unclassified; nothing is guessed. The scheduled classifier (MDPF_SECCLASS FWD-7) is not confirmed live.
10. **Open data-quality rows that bear on it** (`STATUS~P.md`): S184 two near-total-loss accounts read about -100%; S189 the 49F silver disagrees with itself on the position total for 0.45% of account-rows; S212 `map_account` scans every key (a latency risk); S173 the Cottonwood gold host lacks access to the securities table, so its classification falls back to name patterns; S152 the Inflection snapshot lags the trading frontier.

## PART V -- THE DESIGN (PROPOSED)

### 1. The gold tables (Opal shape; one schema contract per table under `org/standards/`)

All at ACCOUNT grain (Andrew: account level is what matters; household and client are aggregates). Parquet, `{table}/date={D}/` per the estate's gold pattern, in each firm's bucket. Every table carries `firm`, `account_id`, `method_version`, and a `coverage` column with a closed vocabulary (below).

| Table | Grain | Contents |
|---|---|---|
| `account_return_daily` | account x business day | `market_value_eod` (whole account incl. cash), `income_received`, `external_flow` (signed), `total_return_daily`, `return_basis` (closed), `holdings_price_return` (the existing gold's value, kept as the guard rail), `fee_amount` (RAIL, null), `coverage` |
| `account_class_daily` | account x day x asset class | `market_value`, `weight`, `class_return_daily` (contribution to the account's total return), `coverage` |
| `account_activity_daily` | account x day | `contributions`, `withdrawals`, `fees` (RAIL), `income`, `market_rgl`, `market_ugl_change`, `coverage`: the columns a window sums into the activity summary |
| `account_transaction` | account x transaction | Opal-normalised: `trade_date`, `settle_date`, `action` and `txn_type` (Opal closed enums), `symbol`, `asset_name`, `units`, `price`, `amount`, `fee`, `custodian`, `flow_class` (EXTERNAL_IN, EXTERNAL_OUT, INCOME, FEE, INTERNAL, CORPORATE_ACTION, UNRESOLVED), `source_txn_id`, `coverage` |
| `account_lot_realized` | account x lot closing | `closing_date`, `symbol`, `proceeds`, `cost_basis`, `gain_loss`, `holding_term`, `acquired_date`, `coverage` |
| `account_lot_unrealized_daily` | account x day (summary) | `cost_basis`, `market_value`, `unrealized_gl` (lot detail is a later table) |
| `account_dim` | account | `firm`, `household_id`, `client_id`, `custodian`, `tax_status`, `registration`, `opened_date`, `first_data_date` |
| `market_topic_daily` (general, non-client) | day x rank | `phrase`, `score`, `sentiment`, `source_kind` (curated or trending), for the topic view |

**`coverage` vocabulary (closed, one axis):** `FULL`, `PARTIAL_HISTORY` (the firm's data starts later), `NO_LOTS` (gain not computable from lots), `FLOW_UNRECONCILED` (see 3), `UNCLASSIFIED_HOLDINGS`, `SOURCE_LAG`. A null is legal only with a coverage value that says why. There are no firm-specific columns. Inflection's missing realized lots and Cottonwood's short history are `NO_LOTS` and `PARTIAL_HISTORY`, which is how the gold stays one shape when Black Diamond's backfill "one day just clicks" (Andrew).

### 2. The adapters (silver in the firm's shape -> gold in the Opal shape)

One adapter per firm, each a Python job reading that firm's silver and writing the eight tables above. The firm knowledge lives ONLY here: Schwab's `sb_cd` codes, Orion's 47 type ids, Black Diamond's `Transaction Type` and `External Flow`, and each firm's price and cash conventions. Adapter contract test: the same schema hash across firms (the annex 17c conformance check).
- **49 Financial (round 1):** positions `dim_position`, balances, `fact_trn` classified by the 187-code table, `fact_uln` and `fact_rld` for lots, the household dimension.
- **Inflection:** positions and `assets_v2`, transactions classified by the ratified Orion taxonomy; lots `NO_LOTS` until Eclipse tax lots are shown populated (a research item, section 8).
- **Cottonwood:** holdings, transactions and `fact_realized`/`fact_unrealized`; Black Diamond's `performancePeriod` and `activitySummary` are NOT the source of gold (that would be a second shape) but are the TIE-OUT against which the Opal figure is checked.

### 3. Total return: conservative GIPS methodology (Andrew's rulings; details this seat's to fill)

Andrew's words, verbatim in the record: external flows matter because they change the weighting; avoid flows hyper-exaggerating performance; conservative GIPS; "no need to reinvent the wheel"; income on receipt; gross of fees; a fee rail for later. This narrows his 2026-09-28 holdings-only ruling: flows return as a weighting input governed by rules, not as an unguarded term. **This brief claims GIPS-ALIGNED methodology, not GIPS compliance** (no composite construction, no verification).

**The method (PROPOSED):**
- **Daily valuation of the whole account, cash included.** Each business day the account is valued at end of day. Daily returns are geometrically linked; any window's return is the product of its days (custom start and end dates need no server work).
- **The daily return.** `r_t = (V_t - F_t) / V_(t-1) - 1`, where `V` is the whole-account value at end of day and `F_t` is the net EXTERNAL flow on day `t` (contributions, in-kind transfers in, minus withdrawals, in-kind transfers out, valued at market on the transfer date). Flows are taken at END of day, matching the estate's existing flow engine and the custodians' end-of-day valuation, so a flow does not earn or lose that day's market move. Income and fees paid inside the account are not flows: income raises `V_t` through cash and stays in the return, which is what makes it TOTAL return.
- **Flow-timing convention is decided by measurement, not by argument.** End of day is the default (it matches the custodians' end-of-day values and the retiring engine). The round-1 tie-out scores three conventions against Black Diamond's own time-weighted return on the 49 Financial sample: flows at the start of the day, at the end, and at the midpoint (the middle convention halves the distortion of a misdated flow in either direction). The winner is written into the method contract; the exact intraday time is not available, so a true sub-period valuation is not possible and is not claimed.
- **Modified Dietz is the cross-check and the fallback, never a second headline.** Daily geometrically linked TWR is exact when every day is valued and flows are timed correctly, and it gives the right answer for ANY custom start and end; Modified Dietz approximates it (close for small flows, drifting with large flows and volatile markets). So: TWR is the one headline. Modified Dietz is computed from the same daily columns (beginning value, ending value, dated flows) (a) as a per-window reconciliation check, where a large disagreement flags the window, and (b) as a labelled fallback for a window with missing days or an account with sparse valuations ("approximated: some days missing"). A money-weighted return (Black Diamond exposes one) can be shown as optional detail, since it answers a different question (what the client experienced, timing included).
- **The data question that decides correctness:** the whole-account value `V` must contain the cash that income produces. If a firm's value excludes sweep or cash, income is missed (or, if added on top, double counted). The existing holdings gold puts positive cash at zero return and excludes negative cash (READ); the adapters must take cash from each firm's balance table (Schwab `dim_balance`, Orion's custodial-cash flag, Black Diamond's allocations) and the round-1 acceptance verifies `V` per firm before any figure is served.
- **Security-level returns are a different calculation from the portfolio return** and are labelled so: position gain and contribution come from lots and class contributions (sections 4), never from a buy-sell transaction return presented as the account's return.
- **Income:** recognised when the cash is received (Andrew). **A declared departure from GIPS,** which asks for accrual accounting for income-bearing securities; it is recorded in the method contract, not hidden.
- **Reinvested dividends** count once, on receipt of the dividend; the reinvestment purchase is internal and neither a flow nor a second income (READ: Orion DRIP is Internal, Schwab RD/RID reinvestments).
- **Fees and trading costs:** returns are GROSS of advisory fees and labelled so everywhere (Andrew); the label reads "before advisory fees", because trading costs are already inside the custodian's cash and value when commissions debit the account (GIPS asks a gross-of-fees return to reflect trading costs; to be VERIFIED per firm in the round-1 tie-out, not assumed). The rail is section 5.
- **Guard against hyper-exaggeration (the part Andrew asked for):**
  1. A flow ledger can be wrong (a missing or misdated contribution reads as a huge gain or a -100%, the retired engine's known failure: READ `c02_twr_engine.py`, S184). So each day the flow-adjusted return is compared to the holdings-based price return (`holdings_price_return`, the existing gold) plus the day's income return; if they differ by more than a tolerance stated in the method contract, the day is flagged `FLOW_UNRECONCILED` and the day's `total_return_daily` falls back to price return plus income with `return_basis = HOLDINGS_INCOME_FALLBACK`, never the unreconciled figure.
  2. A large external flow (a stated share of prior value, a firm policy in the contract) is valued at its date, which daily valuation already does; the day is marked `LARGE_FLOW` so the client sees why.
  3. A day with prior value at or below zero, or a return beyond a plausibility band, is `NOT_MEASURABLE`, and the link is broken with a stated gap rather than compounding a nonsense figure (the existing gold voids returns at or beyond +-100% as IMPLAUSIBLE, READ `holdings_performance.py:739-742`).
- **Periods:** no annualization of any period under one year (GIPS); since-inception is annualized only when at least a year of days exists (Account365 is the working day-count default, pending Andrew's confirm per the draft spec).
- **In-kind transfers** (ACAT) are valued at quantity times the same-day close; an unpriced leg is flagged and excluded from the flow with `FLOW_UNRECONCILED` rather than zero-buried (READ: the earlier zero-burial defect).
- **Corporate actions** (Schwab RO/IC/JR lanes, Orion splits and expiries) are their own class and do not enter as flows or income.
- **Method contract row:** `dim_return_method` (a row per `method_version`): daily TWR, end-of-day flows, `income_basis: cash_when_received`, `fees: RAIL_UNUSED`, tolerance, large-flow share, plausibility band, day-count. A change to any of these is a new `method_version` and the served files carry it.

**Open items inside this design (carried, with defaults, none blocks round 1):** the tolerance and the large-flow share (defaults proposed in the PRD from the 49F data's own distribution, not invented here); Schwab bank-sweep interest (FC codes mix sweep and interest: only clearly classified interest counts as income, the rest stays `UNRESOLVED`); Schwab foreign-tax `WD` is withholding, not a withdrawal (READ).

### 4. Realized and unrealized gain, activity, and asset-class performance

- **Realized gain over a window:** the sum of `account_lot_realized.gain_loss` by `closing_date` (49 Financial from `fact_rld`). **Unrealized change:** the change in `account_lot_unrealized_daily.unrealized_gl` over the window, from open-lot snapshots (`fact_uln`). Income is separate. All three feed `account_activity_daily`, so the activity summary for any window is a sum over a slice of one file.
- **Cost-basis caveats carried as coverage:** Schwab realized lots have overlapping vintages (RLD, RLU, RLW, RLY and the RT* set); the brief names RLD as the source (READ) and the PRD confirms which vintage. Inflection and Cottonwood are `NO_LOTS` until their lot feeds exist; for Cottonwood, Black Diamond's `costBasis` endpoint is available and not ingested.
- **Asset-class performance:** each holding maps to a class through `etf-classifications`; `class_return_daily` is the class's contribution to the account's daily return, so class contributions sum to the account return. Unclassified holdings are their own class, never folded in.

### 5. The fee rail (Andrew: a rail for later; do not get distracted)

The contract reserves the fields and semantics and computes nothing: `fee_amount` in `account_return_daily` and `account_activity_daily` (null, coverage `FEE_RAIL_UNUSED`), `fee_basis` in `dim_return_method` (`GROSS_ONLY` now), and a named place in the flow classes (`FEE`) so advisory fees are already separable from external flows when a proper fee field exists. No net return is emitted. Adding fees later is a new `method_version` that fills these fields; it changes no column name.

### 6. Serving: platinum, precomputed, gzipped (COO~P's recommendation adopted)

A platinum publisher reads the gold parquet and writes, per account, per day of build, in the firm bucket: (a) `series.json.gz`, the whole daily history in columnar arrays (date, value, daily total return, flow, income, class weights by day); (b) `activity.json.gz` if separate from series; (c) transactions in pages (`transactions/page=N.json.gz`, newest first); (d) a `manifest.json` (method version, data as-of date, coverage summary, byte sizes). A shared, non-client `topics` file for the topic view lives in the general platinum home. The browser computes any window from `series` (chaining daily returns, summing flows and income), so no per-window request exists. Household and client files are built from the account files by the publisher with the same rules. Addresses come from `address()`; the PRD cites builder output, and the CTO refuses a PRD that types one. Size and latency are TO BE MEASURED on 49 Financial (555 days of about ten short columns is well inside a small compressed file; that is an estimate, not a measurement).

### 7. The topic snapshot (Andrew's signature view)

- **Drawdown episodes** are detected on the served daily total-return series with the `irpt-narrative` peak, trough, recovery logic, on the client side of the series or in the publisher (PROPOSED: the publisher writes the episode list into `series` so the page does not compute it).
- **Topics for an episode** are a merge of `market_topic_daily` over the days around the trough (the narrative Lambda's window is the seven days before the event). Because ticker tagging is empty after December 2025, these topics are MARKET-WIDE, not filtered to the portfolio; the view says so. Portfolio relevance needs a keyword-to-sector map (a later enrichment).
- **Coverage:** topics exist from 2025-11-21 (curated) and 2025-12-01 (weighted phrases); a window before that returns `MISSING_HISTORY`, never an empty cloud that looks like "quiet".

## PART VI -- ROUND STRUCTURE (for the CTO's decomposition)

Round 1 builds the thread (O1): one 49 Financial account, gold `account_return_daily` (with the guard), the platinum `series.json.gz` and `manifest.json`, read by a page (COO~D) that draws a curve with custom bookends. Schema contract file for that table lands in the same round. Each later round enriches: allocation (`account_class_daily`), activity and gains, transactions, the topic view, then Inflection, then Cottonwood, then household and client aggregation, then the fee rail's first use. A round-1 build carries at most three mechanical criteria (spine v3.18); repo-wide hygiene runs at the drain.

## PART VII -- DECISIONS AND CALLS (none blocks round 1)

Ruled by Andrew: total return on conservative GIPS; income on receipt; gross of fees and labelled; a fee rail; account grain; 49 Financial first; net worth out; gold is the Opal shape. To confirm in the PRD, not asked of Andrew now: day-count convention; the reconciliation tolerance and large-flow share; whether the retiring flow engine's parity work is reused as the flow ledger or rebuilt in the adapter; where the household union-find lands (it sits in an older bucket tree). For the CTO: registering a `reporting` table family and its platinum publisher under the tenancy rules.

## PART VIII -- WHAT THIS BRIEF DOES NOT CLAIM

- It has not read any parquet or served object; every data-shape claim is from code, docs and registers as cited.
- It did not establish whether Cottonwood's or Inflection's transaction silver is populated and keyed by account and date, whether Eclipse tax lots are populated, whether Orion's own returns include dividends, whether anything downstream still reads the retiring engine's `twr_daily`, or whether the draft return spec was ever ratified.
- The served file sizes and the under-two-seconds result are the targets and the COO's estimate, not measurements of this design.
- The tolerance, the large-flow share and the plausibility band are not numbers in this brief on purpose.
- No live vendor call was made; any new Black Diamond or Orion pull needs Andrew's per-use word.
- The Ticket Center and the commentary pipeline are separate work and are not touched here.

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/reporting-dashboard-backend-brief-20260930.md
COMPANION         docs/briefs/reporting-dashboard-frontend-brief-20260930.md
PROJECT           NONE-YET (unregistered); siblings IRPT_BCKEND (performance gold), MDPF_SECCLASS (classifier), news pipeline, LGIC_NAMING
LAW               docs/doctrine/CLAUDE_ANNEX.md 17, 17a, 17b, 17c ; infra/logic/02_DOCTRINE.md
PRIOR ART         docs/research/bd_dashboard_teardown/{BD_REPLACEMENT_ROADMAP,FACT_ACCOUNT_RETURN_BUILD_SPEC,BD_DASHBOARD_HAR_TEARDOWN}_20260721.md
                  org/tier1_exec/2.0.0_SA_COO/deliverables/PERFORMANCE_REPORT_LATENCY_AND_DAILY_HOLDINGS_ASSESSMENT_20260930.md
                  data/assets/scripts/gold/irpt_holdings_performance/ ; docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md
                  data/canonical/schwab/docs/ ; data/inf/scripts/silver/orion_cashflow_taxonomy.yaml
                  infra/aws/lambda/investor-reporting/narrative/ (drawdown events and dated evidence)
MEASURED AT       2026-09-30 by research subagents (READ from files; news tables MEASURED live)
```
