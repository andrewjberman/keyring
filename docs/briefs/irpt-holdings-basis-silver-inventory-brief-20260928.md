# Investor Reporting -- holdings-basis performance for every firm: the silver inventory per firm, per account, per day, and the gap to one gold shape

**Mode:** MIDSTREAM on `IRPT_BCKEND` (L1 brief; its consumer is the CTO's `/endpoint --forward` and L4 addendum). **By:** `4.0.0_SA_CRO`, asked by `1.0.0_SA_CTO` msg 102463 as placement item 2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`.
**Andrew's word (verbatim, that record):** "Yes, I think we need to move to holding-based strategy for all channels. In order for this to work, we need to assess what asset tables we have per account per day, so we can design a consistent structure across all firm channels. I believe that the way that it should work is that we just assess what is needed in opal-data-assets silver tables for the various asset/holdings info per firm, and then create a consolidated shape in Gold that is the singular form that the IRPT page reads. We run this on a daily basis, and then verification is a function of finding the \"official\" performance reporting for pre-set periods as displayed in Black Diamond/Orion/Etc. and we compare our methodology at those defined points."
**The basis (call 3, verbatim, `ANDREW_DIRECT_20260928_222xZ_...`):** "cash movements should not matter at all, performance should be measured as the daily, pro-rated by weight, performance of any securities in a given basket on a given day. It is important that this is handled explicitly at the asset level, looking at the weight of the assets relative to the account in question on the subject day, tracking the delta from the previous day. We cannot get involved with inflow/outflow logic, or be calculating performance in any other basis other than end of day asset holdings values, otherwise it will get too complicated."
**Register (the source of every table here):** `docs/briefs/irpt-holdings-basis-silver-inventory-20260928.json`. **Measured at:** 2026-09-28T22:5xZ-23:3xZ, on live S3 in both keyspaces. **Calendar frontier:** 2026-09-28 (Monday, read from lib/trading_calendar.py expected_last_trading_day at 23:0xZ; the last custody business date landed is Friday 2026-09-25 for 49F and COT).

## PART 0 -- how the blind constraint was honoured, and where it bent

- **Honoured:** no IRPT_BCKEND task order, `phase` or `blocking` field was read for this brief. Every table row is a live S3 read; every code fact is a file read at HEAD.
- **Bent (named):** (1) the three 49F facts in IV.2 come from `0.4.0_DS_ClientPlatform~E` (msg 102466, forwarded by `2.0.0_SA_COO~P` 102467) and were measured under a task order that was then HALTED; they are carried as that seat's measurements, not re-measured here except where this seat's own reads agree (closing_price on every `canonical_positions` row). (2) This seat signed a never-widen half on the 49F adapter today and read `STATUS~P/~M/~Y` for it, so it knows the round-19 workstream shape; nothing in Part I ratifies an open order. (3) The CTO's two records of today name in-flight orders (IB-pr-192, S181, W61-S2); they are cited as the CTO's routing, not read as orders. (4) The existing PRD's ENDPOINT block (FWD-1..FWD-9) and the 09-10 brief's O2/O5 were read, as the mode allows.
- **Unchanged, stated:** the endpoint's DIRECTION has moved (vendor calculation -> holdings basis) by Andrew's word, not by this brief. What this brief adds is the measured substrate and the gap; the outcomes in Part I are cut so the CTO's addendum can cite them.

## PART I -- the outcome territory

### O1

An advisor at any of the three firms reads, for one account, a daily return series and its period figures computed from that account's own end-of-day holdings only: each day's return is the weight-pro-rated return of the securities it held, weights relative to the account on that day, the delta taken from the previous day, with no inflow or outflow logic (Andrew's call-3 basis, verbatim in the CTO record).

*CANDIDATE THREAD (FWD-1 at L2): a 49 Financial advisor, one invested Schwab account, the YTD window, because 49F has one custody partition per trading day with a closing price on every position (IV.2) and its served figure is the one Andrew has seen wrong (IV.12).*

### O2

The advisor reads the SAME figure on the Performance page and in the export for every firm, because the page reads ONE gold shape in which the firm is a column, not a code path.

### O3

An Opal operator can state, for any firm and any day, which silver table supplied the positions and the values, how many accounts were computable, how many were not, and why (no position row, no price, zero value), from the gold's own manifest rather than from a query.

### O4

An advisor is never shown a return for a day whose holdings did not land: an absent day is absent, the page names the last day it has, and nothing rolls forward or fills with zero.

### O5

An Opal analyst compares Opal's holdings-basis figure against the vendor's official figure at pre-set periods (Black Diamond for 49F and Cottonwood, Orion for Inflection) and reads the difference with both bases stated, as a bounded check at defined points, never as a standing comparator or a second pipeline.

### O6

The gold is produced every trading day on a schedule of its own, and its completion manifest names the silver partitions it consumed, so a missed day and a late day read differently from a completed one.

### O7

A security whose price is missing, stale or zero on a day is handled by one stated rule and surfaced on the account's row, never silently priced at zero or dropped; the account's cash and cash-equivalent balances are handled by one stated rule the face can name.

### O8

A relationship or client figure composes its accounts' daily returns by the same weight-pro-rated rule, and never by summing or averaging period returns (FWD-3's rule against a fabricated aggregate carries).

## PART II -- where the boundary sits

| owner | owns | this project's relation |
|---|---|---|
| IRPT_BCKEND (this project) | the gold shape and its contract, the daily runner, its manifest, the adapter that serves it, the comparison points, the retained-report invalidation | FWD-3's vendor-calculation rule is replaced by the CTO's L4 addendum; `3.0.0_SA_CVO` re-signs the ratified-text half |
| IRPT_FNTEND / DSGN_IRPTV1 (`2.0.0_SA_COO~D`) | the Performance page and export that read the gold | the master UI guidance brief of today already asks for one readable figure per firm (AD-14) |
| OPAL_ASSETS silver family (Schwab, SmartX, BD Rebalancer conversions; `data/assets/scripts/silver/`) | the monolith silver tables and their daily landing | relied on, never written by this project; a missing feed is a silver gap to raise, not a workaround |
| inf-pipeline (system orion; `data/inf/scripts/silver/`) | Orion positions, accounts and weekly performance silver; the legacy `opal-data-inf` keyspace | relied on; the D14 full-name migration moves the keyspace later |
| cot-pipeline (system blackdiamond) | the Cottonwood BD session fetch, bronze and silver sentinels | relied on; COT has no performance feed to rely on |
| ADVI (account_gains, twr_daily, prices) | the existing flow-based golds and the canonical price tables | PRIOR ART ONLY; the README's rule stands: this project has no silent dependency on another page's gold |
| `0.4.0_DS_ClientPlatform` lane seated by call 2 | the 49F engine and data fixes (rows S181, W61-S2) | the CTO placement redirects its work into the 49F slice of the consolidated gold once the addendum lands |
| LGIC_NAMING / LGIC_ENFORCE | the gold's address and resource names | rule 30: every address from `lib/opal_naming.py address()`, cited in the L4 PRD |
| ETFS_* / POSN_* (classifier, asset classes) | the security classification the page colours by | not needed for the return; needed for any class-level breakdown |
| MDPF_* (model AUA, SmartX and Eclipse model registries) | model membership and model-level performance | an overlay on the account figure, never its basis |

## PART III -- the qualitative bar

An advisor who opens an invested account at any of the three firms reads a year-to-date figure that an Opal analyst can reproduce with a pencil from that day's landed holdings: the weights, each security's day-over-day price move, the sum. It is the figure they would otherwise open Black Diamond or Orion for. Where the page cannot compute it, it says which day's holdings are missing or which position had no price, and shows no figure. The same account, opened from the Global view or the firm view, reads the same number.

## PART IV -- the substrate: what exists, measured

### IV.0 -- the inventory, per firm

Partition counts are per table; `tdays` is the NYSE trading-day count between `first` and `last` (`lib/trading_calendar.py`), so `partitions / tdays` reads 1.00 for one-per-trading-day, above 1 where non-trading days also land, below 1 where days are missing.

| firm | role | bucket / prefix | scheme | partitions | first | last | tdays | latest partition read | value and price basis |
|---|---|---|---|---|---|---|---|---|---|
| 49financial | custody_positions | `opal-data-assets/schwab/08335338/silver/dim_position/` | date=YYYY-MM-DD/data.parquet | 559 | 2024-07-08 | 2026-09-25 | 558 | date=2026-09-25: 106,835 rows, 6,347 accounts; closing_price non-null on all rows, > 0 on 106,785; market value > 0 on 105,280 | Schwab statement closing price per position (factored pair), value = market_value_settled_unsettled |
| 49financial | custody_balance | `opal-data-assets/schwab/08335338/silver/dim_balance/` | date=YYYY-MM-DD/data.parquet | 559 | 2024-07-08 | 2026-09-25 | 558 | date=2026-09-25: 7,548 accounts; net_mv_plus_cash > 0 on 6,654 | Schwab statement account value; V(t) = net_mv_plus_cash (B_00 rule) |
| 49financial | custody_positions_second_master | `opal-data-assets/schwab/08242234/silver/dim_position/` | date=YYYY-MM-DD/data.parquet | 587 | 2024-05-24 | 2026-09-25 | - | not read | as 08335338 |
| 49financial | model_overlay | `opal-data-assets/smartx/platform/silver/fact_allocation_account_map/` | date=YYYY-MM-DD/data.parquet | 76 | 2026-07-14 | 2026-09-28 | - | date=2026-09-28: 7,542 rows | SmartX intraday allocation value on the overlay date (never ties to Schwab to the cent, holdings_49f.py header) |
| 49financial | vendor_model_performance | `opal-data-assets/smartx/platform/silver/fact_model_performance/` | date=YYYY-MM-DD/data.parquet | 77 | 2026-07-14 | 2026-09-28 | - | date=2026-09-28: 7,028 rows | SmartX's own model-level daily P&L |
| 49financial | vendor_official_performance | `opal-data-assets/blackdiamond/49f/bronze/reporting_performance/` | YYYY-MM-DD/reporting_performance_<relationship>_<date>.json (BRONZE only) | 4 | 2026-07-17 | 2026-09-01 | - | 4 pull dates; per-relationship JSON | Black Diamond's own TWR for the relationship at the pull's periods |
| 49financial | gold_prior_art_engine | `opal-data-49financial/gold/advi/canonical/twr_daily/` | date=YYYY-MM-DD/ | 559 | 2024-07-08 | 2026-09-25 | 558 | date=2026-09-25: 7,545 rows | flow-adjusted daily TWR from canonical_valuation + flow_ledger (c02_twr_engine.py) |
| 49financial | gold_prior_art_positions | `opal-data-49financial/gold/advi/canonical/canonical_positions/` | date=YYYY-MM-DD/ | 559 | 2024-07-08 | 2026-09-25 | 558 | date=2026-09-25: 106,835 rows | passthrough of dim_position with quality flags (b01_canonical_positions.py) |
| 49financial | gold_prior_art_valuation | `opal-data-49financial/gold/advi/canonical/canonical_valuation/` | date=YYYY-MM-DD/ | 559 | 2024-07-08 | 2026-09-25 | 558 | date=2026-09-25: 7,545 rows | V(t) = dim_balance.net_mv_plus_cash, never reconstructed (b00) |
| cottonwood | custody_positions | `opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/` | date=YYYY-MM-DD/data.parquet | 81 | 2026-06-09 | 2026-09-25 | 77 | date=2026-09-25: 19,784 rows, 984 accounts, 908 with market value > 0 | Black Diamond holdings value; NO price column (price is derivable as Market Value / Units where Units is present: 14,616 of 19,784 rows on 09-25) |
| cottonwood | custody_balance | `opal-data-assets/blackdiamond/cottonwood/silver/fact_allocations/` | date=YYYY-MM-DD/data.parquet | 132 | 2026-04-22 | 2026-09-25 | 109 | date=2026-09-25: 1,592 rows, 940 accounts | Black Diamond account market value |
| cottonwood | model_overlay | `opal-data-assets/blackdiamond/cottonwood/silver/fact_model_assignment/` | date=YYYY-MM-DD/data.parquet | 59 | 2026-07-21 | 2026-09-28 | - | not read | BD Rebalancer assignment |
| cottonwood | vendor_official_performance | `opal-data-assets/blackdiamond/cottonwood/bronze/` | feed folders | 0 | - | - | - | bronze feeds: account_attributes, allocations, holdings, realized, rebalancer_accounts, rebalancer_model_detail, rebalancer_models, transactions, unrealized | - |
| cottonwood | gold_prior_art_holdings | `opal-data-cot/gold/canonical/holdings/` | YYYY-MM-DD.parquet (flat) | 124 | 2026-04-22 | 2026-09-25 | 109 | 2026-09-25: 19,684 rows | price computed in gold (02b), BD vs Schwab units reconciled |
| cottonwood | gold_prior_art_gains | `opal-data-cot/gold/canonical/account_gains/` | YYYY-MM-DD.parquet (flat) | 48 | 2026-04-23 | 2026-06-09 | 33 | last 2026-06-09 | AUA(t)-AUA(t-1) = growth + NNA, NNA the residual (B_03.account_gains.py) |
| inflection | custody_positions | `opal-data-assets/orion/inflection/silver/fact_positions/` | date=YYYY-MM-DD/data.parquet | 2343 | 2020-04-24 | 2026-09-27 | 1613 | date=2026-09-27: 36,103 rows, 960 accounts | Orion position price and value per row (prior close on the snapshot date, 4.0.0_SA_CRO 10f3cf6f9f) |
| inflection | custody_balance | `opal-data-inf/silver/api_dims/accounts_v2/` | snapshot_date=YYYY-MM-DD/data.parquet | 2463 | 2020-01-01 | 2026-09-28 | 1693 | 916 rows on the latest partition read; holdings_inf.py header: 876 accounts with current_value, positions tie to current_value to the cent on 876 of 876 | Orion account ending market value |
| inflection | model_overlay | `opal-data-assets/eclipse/inflection/silver/fact_portfolios_simple/` | date=YYYY-MM-DD/data.parquet | 122 | 2026-05-15 | 2026-09-28 | 92 | not read | Eclipse model membership; 786 accounts -> exactly one portfolio; 663 portfolios carry a model id, 181 do not (holdings_inf.py header) |
| inflection | vendor_official_performance | `opal-data-assets/orion/inflection/silver/fact_performance/` | date=YYYY-MM-DD/data.parquet | 121 | 2026-05-03 | 2026-09-27 | 101 | date=2026-09-27: 477,762 rows, 313 clients | Orion WEEKLY TWR factor per CLIENT (household), inception-based cumulative index (legacy twin opal-data-inf/silver/performance: week_date, twr_factor, cumulative_twr, inception_date) |
| inflection | gold_prior_art_holdings | `opal-data-inf/gold/holdings/` | YYYY-MM-DD.parquet (flat) | 2566 | 2019-09-17 | 2026-09-25 | 1766 | 2026-09-25: 14,571 rows | gold-computed price with price_source |
| all | prices | `opal-data-bd/silver/prices/` | YYYY-MM-DD.parquet (flat, cumulative) | 161 | 2026-02-22 | 2026-09-27 | 150 | 2026-09-27: 12,482,017 rows (cumulative history per file) | yfinance/BD blended history (bd_price_update.py, build_interpolated_prices.py) |

Key and value columns per table, and each table's note, are in the register; the notes carry the qualifications (second sections, calendar-day partitions, stopped chains).

### IV.1 -- Two keyspaces are live and the IRPT builders read BOTH.

The monolith `opal-data-assets` (`{source}/{scope}/silver/{feed}/date=YYYY-MM-DD/data.parquet`, `data/assets/scripts/silver/silver_registry.py`) and the legacy firm buckets `opal-data-bd`, `opal-data-inf`, `opal-data-cot` (`silver/<feed>/<date>.parquet`, flat, plus `gold/canonical/`). `holdings_snapshot.py` reads the monolith for 49F (`schwab/08335338`, `smartx/platform`) and COT (`blackdiamond/cottonwood`) and the LEGACY bucket for INF (`opal-data-inf/silver/api_dims`, `silver/eclipse`; `build_inf`, `INF_SOURCE_BUCKET`). The 49F engine reads the monolith (`runner_common.py` SILVER_BUCKET = opal-data-assets, scope schwab/08335338) and writes gold to `opal-data-49financial`. The LGIC resource registry (`infra/logic/registry/resources.json`, 465 rows) carries no S3 table row of any kind (types are IAM, Lambda, event rules, secrets), so no silver table has a registry address to cite; the gold's address is minted at L4 from `lib/opal_naming.py` (rule 30).

### IV.2 -- 49 Financial has the deepest per-account per-day custody: one Schwab partition per trading day since 2024-07-08, with a closing price on every position.

`dim_position` 559 partitions over 558 trading days; 6,347 accounts with positions on 09-25, closing_price non-null on 106,835 of 106,835 rows. `dim_balance` gives the account value (7,548 accounts). DS~E measured the day-over-day priceability at 99.2% (6,288 of 6,341). The engine's own `canonical_positions` already carries the price and three quality flags (price_stale_days, zero_price_flag, zero_qty_nonzero_mv_flag). A SECOND Schwab master (08242234) has the same silver depth and no gold.

### IV.3 -- Cottonwood has daily holdings VALUES but no price column, and no landed vendor performance at all.

`fact_holdings` (81 partitions, 2026-06-09..09-25) carries Market Value and Units per position; price is derivable where Units is present (14,616 of 19,784 rows on 09-25) and not where it is not. The account value is in `fact_allocations` (from 2026-04-22). No performance feed exists under `blackdiamond/cottonwood/bronze/` or in `opal-data-cot`; the legacy `gold/canonical/account_gains` and `performance` stopped on 2026-06-09 and `silver/prices` on 2026-06-07. The served COT Performance today is the adapter's per-use Black Diamond plan, answering DEPENDENCY_UNAVAILABLE on 53 of 53 reads.

### IV.4 -- Inflection has the longest history (Orion positions daily since 2020-04-24 with price and value per row) and a WEEKLY household-grain official TWR.

`fact_positions` 2,343 partitions (a partition per calendar day, so 1.45 per trading day: weekend partitions repeat the prior close); 960 accounts on 09-27 with currentPrice and currentValue per row; `accounts_v2` gives ending_mv per account (876 tie to the cent). The official Orion performance landed is `fact_performance`: a weekly TWR factor per client_id (313 households), not per account and not daily. A legacy gold `opal-data-inf/gold/holdings` already holds a daily per-account per-security table with price and price_source back to 2019-09-17.

### IV.5 -- The basis Andrew named is implemented NOWHERE measured; the two calculations that exist are both flow-based.

The 49F engine (`c02_twr_engine.py`) links r_net = (emv - bmv - cf) / bmv from `canonical_valuation` and `flow_ledger`, which is how a zero-EMV day with no flow becomes -100% (S177). The three per-firm `account_gains` golds (`data/black_diamond/scripts/gold/B_03.account_gains.py`, `data/cot/.../B_03.account_gains.py`, `data/inf/.../INF_B_03.account_gains.py`, and `runners_49f/c00_account_gains.py`) decompose AUA(t)-AUA(t-1) = growth + NNA with NNA the residual, a transaction-classified identity. Neither computes a weight-pro-rated security return from end-of-day holdings. The nearest surface to Andrew's basis is the per-position price/value columns themselves, which exist on 49F and INF rows and are derivable on COT rows.

### IV.6 -- The served HoldingsSnapshot already answers 'which accounts, which positions, which values, on which day' per firm, with reconciliation and one identity normalizer.

`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` with `holdings_49f.py` (Schwab meshed with SmartX), `holdings_inf.py` (Orion meshed with Eclipse) and `build_cot` (BD Rebalancer) resolves per firm the account set, the custody clock, the position rows and the tie of positions to the account value, and mints node ids through `_ids/ids.py` and `_ids/raw_keys.json` (the same normalizer the handlers use, rows W1-S7/W2-S11). It is a one-as-of snapshot, not a series, and it runs ad hoc (the served as-of is 2026-09-22 while every silver is at 09-25 or later; row S152). Its reads are the same reads a daily holdings-basis gold needs.

### IV.7 -- Per account per day, measured on the latest custody partition.

49F: 6,347 accounts with positions of 7,548 with a balance (1,201 cash-only or empty), 99.2% priceable day over day. COT: 984 accounts with holdings rows, 908 with market value > 0, of 940 accounts in fact_allocations. INF: 960 accounts with positions of 876 accounts that tie to a balance (916 rows on the accounts dim read). Absent days inside each table's span: none for 49F (one partition per trading day); COT and INF carry extra non-trading-day partitions rather than gaps. Data starts differ: 49F 2024-07-08, COT 2026-06-09 (values from 2026-04-22), INF 2020-04-24, so 'since inception' is a per-account first-holdings-day, not a firm constant.

### IV.8 -- Official vendor performance already landed is thin and uneven: 4 Black Diamond pulls for 49F, weekly household factors for INF, nothing for COT.

49F: `blackdiamond/49f/bronze/reporting_performance/` has 4 pull dates (2026-07-17..2026-09-01), per-relationship JSON from performancePeriod, never converted. INF: weekly TWR factors per household (IV.4). COT: none. SmartX `fact_model_performance` gives a daily model-level P&L for 49F MODEL sleeves. A comparison at pre-set periods therefore has landed material for 49F relationships at 4 dates and INF households weekly; anything else is a NEW vendor pull and needs Andrew's per-use word.

### IV.9 -- Cash is a different object at each firm and the basis speaks of securities.

49F `dim_balance` splits cash_balance_settled_only, money_mkt_funds, bank_sweep_ibf, bank_cash and margin_balance; COT `fact_holdings` flags Cash Equivalent per holding; INF `fact_positions` flags isCustodialCash per position. Whether a money-market or sweep balance carries a daily return, and whether it sits inside or outside the security basket's weights, is not stated anywhere measured and changes the figure for the 1,201 cash-only 49F accounts.

### IV.10 -- The legacy Black Diamond 49F silver is retired in place and must not be read by the new gold.

`opal-data-bd/silver/assets` ends 2026-06-18; `silver/transactions` latest partition has 0 rows and an all-null schema; `silver/unrealized` 0 rows; the monolith mirror `blackdiamond/49financial/silver_legacy/` ends 2026-08-25. The 49F chain moved to Schwab (registry `pipeline_trees`, `trees.advi.silver_master` = 08335338).

### IV.11 -- Silver lands on schedules; the IRPT gold does not.

Registered event rules: Schwab conversions ride `silver_registry.py` daily; Orion `inf-api-positions-daily`, `inf-api-assets-v2-daily`, `inf-accounts-v2-daily`, `inf-performance-daily`; COT `cot-session-complete` -> `cot-bronze-complete` -> `cot-silver-complete` sentinels and `cot-rebalancer-runner-daily`; SmartX platform daily (77 partitions, 2026-07-14..09-28). The IRPT holdings snapshot and the 49F engine gold are ad hoc or QA-fired (S152; the twr_daily partitions exist because the ADVI chain runs, not because IRPT schedules them).

### IV.12 -- The served Performance surface today, per firm (from the CRO walks of 2026-09-28).

49F: PERFORMANCE_PARTIAL with a computed figure and no benchmark or values; one account -100.00% (NEW-01), a guard `hcZpXDDo` live but bypassed by retained-report reopen (D1 NOT MET). COT: DEPENDENCY_UNAVAILABLE on every read. INF: OBJECT_NOT_COVERED on every read. 3Y and Since inception: UNSUPPORTED_OPERATION. The Holdings tab serves a 2026-09-22 snapshot at every firm.

## PART V -- what must be true, without scoping it now

- A per-firm SOURCE DECLARATION as data (table, key column, date column, position value column, price column or 'derived as value/units', account value column), readable by the runner and the manifest; the tables in the register are the candidates.
- The day axis is `lib/trading_calendar.py`; a calendar-day partition (INF, some COT days) is folded to its trading day, and a missing trading-day partition is ABSENT (O4).
- A PRICE-MISSING rule for the day-over-day return of a position (49F: 48 non-positive t-1 prices and 5 missing t prices on one day; COT: Units absent on 5,168 of 19,784 rows; INF: currentPrice null on some rows, unmeasured count).
- A CASH rule (IV.9): which balances are in the basket, and what return they carry.
- An ACCOUNT FIRST-DAY rule: since-inception starts at the account's first landed holdings day, per account (data starts 2024-07-08 / 2026-06-09 / 2020-04-24).
- A COMPOSITION rule for relationships and clients (O8), and a statement of what a multi-account weight is relative to.
- COMPARISON POINTS: 49F relationships at the 4 landed Black Diamond pull dates; INF households at weekly Orion factors; COT has nothing landed, so a comparison there is a new vendor pull and needs Andrew's word per use.
- The second Schwab master 08242234: in or out of the 49F population (IV.2).
- The retained-report store is invalidated or bypassed when the gold changes (today's D1 finding: a reopened report bypasses a deployed guard).
- The DS lane and `2.0.0_SA_COO~P` are the two writers of the 49F path today; the addendum names which one owns the 49F slice of the gold.
- The gold's home and name come from the naming builders (rule 30); `opal-data-49financial` holds gold today, `opal-data-cottonwood` and `opal-data-inflection` hold only `irpt/<firm>/gold/holdings`.

## PART VI -- status (NOT OUTCOME-BEARING)

Measured 2026-09-28T22:5xZ-23:3xZ. Calendar frontier 2026-09-28 (Monday, read from lib/trading_calendar.py expected_last_trading_day at 23:0xZ; the last custody business date landed is Friday 2026-09-25 for 49F and COT). Latest custody partitions: 49F 2026-09-25 (Schwab), COT 2026-09-25 (fact_holdings), INF 2026-09-27 (fact_positions) and 2026-09-28 (fact_assets, accounts_v2). Served Performance today: 49F PARTIAL with a computed figure and one -100.00% account (the guard `hcZpXDDo` is live and bypassed by retained-report reopen, D1 NOT MET at 22:1xZ); COT DEPENDENCY_UNAVAILABLE; INF OBJECT_NOT_COVERED; 3Y and Since inception UNSUPPORTED_OPERATION. Served Holdings snapshot as-of 2026-09-22 at every firm. The 49F engine gold `twr_daily` is at 2026-09-25 with the S176/S177 defect class in 26 rows.

## PART VII -- what this brief does not claim

- Row-level quality was read on ONE partition per table (the latest); coverage is partition counts against trading days, not row counts per day.
- The SmartX per-account and per-allocation trees (7,066 and 10,101 folders) were not enumerated; only `smartx/platform/silver` was read.
- The 08242234 Schwab master's account population was not compared with the IRPT directory.
- No vendor endpoint was called; every figure is a landed object read.
- Cash rules, price-missing counts on INF, and the COT price derivation were not exercised, only their columns read.
- No LGIC address or name was minted; that is the CTO's L4.
- The register's `trading_days_in_window` is `total_trading_days_in_window(first, last)` from `lib/trading_calendar.py` (NYSE); a null means the window was not counted.

## Refs

```
  BRIEF PATH        docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md
  REGISTER          docs/briefs/irpt-holdings-basis-silver-inventory-20260928.json
  PROJECT           IRPT_BCKEND (midstream); counterpart IRPT_FNTEND; page DSGN_IRPTV1
  EXISTING PRD      org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md (v0.18; FWD-3 is the rule the addendum replaces)
  ORIGINAL BRIEF    docs/briefs/investor-reporting-ir-bk-brief-20260910.md (O2 vendor semantics, O5 holdings joins, IV.3 adapter recipe)
  ANDREW RECORDS    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md;
                    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md
  SIBLING PROJECTS  IRPT_FNTEND, DSGN_IRPTV1, LGIC_NAMING, LGIC_ENFORCE, ETFS_POSITIONING, MDPF_* (Part II)
  PRIOR ART         holdings_snapshot.py + holdings_49f.py + holdings_inf.py (per-firm reads and reconciliation); runners_49f b00/b01/c02 (49F canonical tables);
                    B_03.account_gains.py x3 (flow-based daily gains); opal-data-inf/gold/holdings (daily priced holdings gold since 2019); silver_registry.py (the keyspace)
  SURPRISE ROWS     IRPT_BCKEND-S152 (INF holdings lag), S176/S177 (NEW-01 cause), S180 (selection create 500)
  MEASURED AT       2026-09-28T22:5xZ-23:3xZ UTC (every Part IV and Part VI claim)
```
