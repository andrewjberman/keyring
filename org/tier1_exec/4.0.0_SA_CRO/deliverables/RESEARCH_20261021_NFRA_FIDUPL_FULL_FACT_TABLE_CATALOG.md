# RESEARCH 2026-10-21 -- NFRA_FIDUPL: the full Fidelity fact-table catalog ("absolutely everything")

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Order:** Andrew-direct ~15:20Z (every Fidelity fact table, incl. tax lots and realized +
unrealized G/L, as silver parquet). **Grounding:** the measured endpoint map `RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md`
and Andrew's HARs. (M) = call seen in a HAR; (A) = available per entitlements, not yet captured.

## Tier A -- the daily EXPORT files (bronze now; silver next) -- 6 fact tables

| silver table | source file | grain | key columns (mapped) |
|---|---|---|---|
| `fact_account` | account.txt (141 col) | account x date | account no (col 0), as-of (col 16) |
| `fact_position` | position.txt (62 col) | account x security x date | date col 0 |
| `fact_balance` | balance.txt (43 col) | account x date | date col 3 |
| `fact_price` | prices.txt (44 col) | security x date | date col 0 |
| `fact_security` | security.txt (45 col) | security x date | date col 0 |
| `fact_transaction` | transact.txt (66 col) | account x txn | as-of col 17 |

These are landing today. Silver = CSV -> parquet, schema from the wizard's step-2 column list (no header row in the files).

## Tier B -- the TAX-LOT / GAIN-LOSS surfaces Andrew named (API, per account) -- the priority adds

| silver table | call (M) | content |
|---|---|---|
| `fact_open_lots` (unrealized at lot grain) | POST `/ssc/open-lots/wc/channel/api/v2/open-lots` | per open tax lot: cusip, acquired date, qty, cost, cost/share, market value, gain/loss, %gain, covered status, wash flag, holding period |
| `fact_realized_gain_loss` | POST `/ssc/positions-apps/wc/channel/v1/previous-sales/retrieve-realized-gain-loss/{summary,detail}` + GET `/ssc/tax-summary/.../v1/realized-gain-loss` | closed lots: acquisition + close dates, proceeds, basis, ST/LT gain/loss, wash-sale amounts |
| `fact_unrealized_gain_loss` | derived from `open-lots` (market value - cost per lot), or the positions file's cost vs market | per-lot and per-position unrealized gain/loss |

**Unrealized G/L note:** Fidelity surfaces it at the lot level inside `open-lots` (market value vs cost per lot), so `fact_open_lots` and
`fact_unrealized_gain_loss` can be one table or two views of it; the CTO/DS decides the grain.

## Tier C -- everything else exposed (A/M) -- the "absolutely everything" remainder

| silver table | call | content |
|---|---|---|
| `fact_estimated_income` | POST `/ssc/tax-summary/.../estimated-income-{summary,detail}` (M) | projected 12-month income per security |
| `fact_tax_income` | GET `/ssc/tax-summary/.../v1/tax-income` (M) | YTD tax income |
| `fact_performance` | GET `/ssc/performance-measurement/.../returns/{standard-period,time-series,historic,account-activity}` (M) | TWR returns per account x period |
| `fact_allocation` | GET `/ssc/performance-measurement/.../accounts/portfolios[/asset-allocations]` (M) | asset allocation per account |
| `fact_risk_metrics` | GET `/ssc/performance-measurement/.../risk-metrics/accounts-summary` (M) | risk stats per account |
| `fact_benchmark` | GET `/ssc/performance-measurement/.../benchmarks/assignments` (M) | benchmark assignment per account |
| `fact_cash_movement` | POST `/ssc/cashmanagement/.../api/v1/history` (M) | money-movement history |
| `fact_option_position` | POST `/OptionsPairingUIC/OPUIC/GetOptionPairData` (M) | option positions / pairings |
| (reference) statements | GET `/ssc/account-documents/.../statements/...` (M) | statement PDFs -- documents, not a fact table |

## The build shape (for the CTO to scope)

1. **Silver converter for Tier A** (6 files -> parquet), modeled on `opal-assets-silver-schwab`. Immediate; schema in hand.
2. **Extractors for Tier B** (open-lots, realized G/L) -- these are per-account JSON APIs, paged per account over the ~5,000 accounts,
   run in the same signed-in session as the daily pull; land JSON bronze, convert to parquet. Andrew's named priority.
3. **Extractors for Tier C** -- the same pattern, one surface at a time. Performance/allocation/risk are per-account; income and cash are
   per-account.

**Two realities to flag:** (a) Tier B/C are **per-account** calls -- ~5,000 accounts x N surfaces is many requests per run, so they need
batching and spacing (the throttle), not a single export; (b) some are heavy (open-lots returned 100+ lots for one account). The CTO
scopes order and cadence (likely: Tier A silver first, then open-lots + realized/unrealized G/L, then the rest).

## Recommendation

Scope this as an addendum to NFRA_FIDUPL (or a sibling `NFRA_FIDUPL_SILVER` project): Tier A silver now; Tier B (tax lots + realized +
unrealized G/L) next as Andrew's named priority; Tier C after. I can write the formal brief to start the canonical loop if the CTO wants
the full process rather than a PRD addendum.

## Not measured
- The exact column schema for each Tier B/C JSON (shapes are in the endpoint map; the silver schema is derived at build).
- The per-account run cost at ~5,000 accounts (batching/cadence is a build decision).

## Tier A2 -- ALIGN TO THE SCHWAB SILVER SCHEMA (Andrew-direct 15:28Z: "formulated the exact same way")

Schwab silver already has the exact tables Andrew wants. Build Fidelity silver to the SAME names/columns/grain so a downstream reader
cannot tell custodian apart; a master gold layer coalesces by a `custodian`/`source` column. Schwab silver tables (measured, `schwab/.../silver/`):
`fact_acc, fact_sec, fact_trn, fact_rps, fact_rps_s2, fact_uln, fact_ult, fact_rld, fact_rlu, fact_rlw, fact_rly, fact_rtu, fact_rty,
fact_upn, fact_upt`, plus `dim_account/position/transaction/asset/balance`.

**Fidelity source -> Schwab silver table (the alignment map):**

| Fidelity source | Schwab silver table | notes |
|---|---|---|
| account.txt | `fact_acc` | |
| position.txt | `fact_rps` | positions |
| balance.txt | `fact_rps_s2` | balances |
| security.txt + prices.txt | `fact_sec` | Schwab folds prices into sec; keep prices as a column or `fact_sec` price fields |
| transact.txt / historical-transactions | `fact_trn` | |
| open-lots (unrealized) | `fact_uln` / `fact_ult` | unrealized lots |
| realized gain/loss | `fact_rld` (+ rlu/rlw/rly/rtu/rty variants) | realized lots |
| (no Fidelity analog yet) | `fact_upn/upt` (pending positions) | leave empty or omit |

**The real work is a per-field schema reconciliation** between each Fidelity source and the matching Schwab silver schema (column names,
types, units, enum values). That is a DS task; the goal is byte-compatible parquet so one reader and one gold model serve both custodians.

## Depth measured (2026-10-21, COO `FIDUPL_depth_experiments_20261021.md`)

- **Transactions:** back to ~**2021-12** (first txn 2021-12-08..10; account age). One call max **366 days** (refused with exact text) ->
  window per year per account.
- **Realized lots:** closes from **2018-07**, acquisition dates from **2013**; 30-year start accepted; 500/page.
- **Other Historical formats:** no deeper than the ~128-day positions floor.
So the deep history is: transactions ~4 years, realized G/L to 2018 (acquisitions 2013), positions/prices ~4 months.
