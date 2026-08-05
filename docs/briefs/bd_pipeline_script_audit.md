# BD Pipeline Script Audit — For Data Scientist Review

**Date:** 2026-02-25
**Issue:** `bd-portal-advisor-publisher` reports Total AUA of ~$68.5M on latest date. Firm-wide AUA should be ~$1.57B. Something in the pipeline is producing an incorrect or incomplete figure.

**Action Required:** Review the data flow from positions_cube → prices → account_performance to identify where AUA diverges from reality.

---

## Pipeline Overview

```
Bronze (Excel/CSV)
  → silver/transactions/*.parquet     (bd-exporter EC2 + bd-allocation-processor Lambda)
  → silver/prices/canonical_prices.parquet  (bd-price-update Lambda)

Silver → Gold (EC2 scripts, run in order)
  00 → accounts_dimension_latest.parquet
  01 → advisor_assignments_history
  02 → positions_cube/{date}.parquet
  03 → holdings_lots/{date}.parquet
  04 → client_dimension.parquet
  05 → client_performance.parquet          (relationship grain)
  05b → account_performance.parquet        (account grain, ~350MB / ~10M rows)
  06 → views/client_tax_liability.parquet

Gold → Portal JSON (Lambdas, triggered by pipeline-complete.json sentinel)
  bd-portal-publisher       → leaderboard, timeseries, snapshots, filters, summary
  bd-portal-advisor-publisher → implementor_leaderboard, advisors/*/book.json, clients/*.json
```

---

## Script-by-Script Summary

### 00_build_accounts_dimension.py
- **Path:** `data/black_diamond/scripts/gold/00_build_accounts_dimension.py`
- **Reads:** `silver/transactions/` (full history — only source with all accounts ever seen)
- **Writes:** `gold/accounts_dimension_latest.parquet`
- **Grain:** One row per account_id
- **Logic:** Takes latest transaction row per account for current metadata. Derives account_open_date (min trade_date), relationship_first_seen_date. Left-joins allocations for account_type, registration_type. Maps tax status: Taxable → taxable, Tax-Deferred → tax_deferred, Non-Taxable → tax_exempt.
- **Figures Logged:** Account count, relationship count

### 01_build_advisor_assignments_history.py
- **Path:** `data/black_diamond/scripts/gold/01_build_advisor_assignments_history.py`
- **Reads:** `gold/accounts_dimension_latest.parquet` + transaction history
- **Writes:** Advisor assignment timeline
- **Logic:** Tracks how advisor assignments change over time for historical accuracy

### 02_build_positions_cube.py
- **Path:** `data/black_diamond/scripts/gold/02_build_positions_cube.py`
- **Reads:** `silver/transactions/` (deduplicated)
- **Writes:** `gold/positions_cube/{YYYY-MM-DD}.parquet` (~1500 date partitions)
- **Grain:** (account_id, asset_name, units) per calendar day
- **Logic:** Processes accounts in FIFO order. Categorizes transactions: BUY, SELL, CORPORATE_ACTION. Computes cumulative units per (account, asset) over time. Flushes date partitions when safe. Peak memory 2-4 GB.
- **Key Question:** Are all accounts represented? Missing accounts here = missing AUA downstream.

### 03_build_holdings_lots.py
- **Path:** `data/black_diamond/scripts/gold/03_build_holdings_lots.py`
- **Reads:** `silver/transactions/`, `silver/prices/canonical_prices.parquet`, `gold/accounts_dimension_latest.parquet`
- **Writes:** `gold/holdings_lots/{YYYY-MM-DD}.parquet` (daily snapshot)
- **Grain:** One row per open lot
- **Logic:** FIFO lot tracking. Computes cost_basis, accrued_gain, holding_period_days, term (short/long). Qualified/non-qualified from accounts_dimension.

### 04_build_client_dimension.py
- **Path:** `data/black_diamond/scripts/gold/04_build_client_dimension.py`
- **Reads:** `gold/accounts_dimension_latest.parquet`, `silver/transactions/`
- **Writes:** `gold/client_dimension.parquet`
- **Grain:** One row per relationship_id
- **Logic:** Aggregates by household. Counts total/active accounts, derives primary_architect/implementor (modal), computes first_seen_date, boolean tax flags.

### 05_build_client_performance.py
- **Path:** `data/black_diamond/scripts/gold/05_build_client_performance.py`
- **Reads:** `gold/positions_cube/{date}.parquet` (one partition at a time), `silver/prices/canonical_prices.parquet`, `gold/accounts_dimension_latest.parquet`, `silver/transactions/`
- **Writes:** `gold/client_performance.parquet`
- **Grain:** (date, relationship_id)
- **Logic:**
  - AUA = sum(units x price) per relationship per day
  - Forward-fills missing prices within each asset
  - NNA flows: INFLOW = {Cash Deposit, Transfer In}, OUTFLOW = {Cash Withdrawal, Transfer Out}
  - Cumulative flows via cumsum
  - AUA breakdown by tax_status
  - Outlier guard: caps per-event flows at $50M
  - Computes pct_priced (fraction with real prices)
- **Figures Logged:** Total AUA, NNA, client/account counts, date range
- **Key Question:** Does total_aua on latest date match expected $1.57B?

### 05b_build_account_performance.py (**PRIMARY SUSPECT**)
- **Path:** `data/black_diamond/scripts/gold/05b_build_account_performance.py`
- **Reads:** Same as 05 + denormalizes advisor fields from accounts_dimension
- **Writes:** `gold/account_performance.parquet` (~350 MB, ~10M rows)
- **Grain:** (date, account_id)
- **Logic:** Same as 05 but at account grain with parallelization (ThreadPoolExecutor, max_workers=16). Denormalizes architect, implementor, local_relationship, manager, investment_strategy_name, tax_status.
- **Output Columns:** date, account_id, relationship_id, architect, implementor, local_relationship, manager, investment_strategy_name, tax_status, total_aua, cum_inflows, cum_outflows, nna, num_positions, pct_priced
- **Built-in Verification:** SUM(total_aua) on latest date must equal 05 client_performance sum; GROUP BY (date, relationship_id) SUM(total_aua) must match 05 row-for-row.
- **Key Question:** Is 05b producing the same total AUA as 05? Are all accounts from positions_cube represented?

### 06_build_client_tax_liability.py
- **Path:** `data/black_diamond/scripts/gold/06_build_client_tax_liability.py`
- **Reads:** `gold/holdings_lots/` (latest snapshot)
- **Writes:** `gold/views/client_tax_liability.parquet`
- **Grain:** (relationship_id, account_id, asset_name, purchase_year)
- **Logic:** Groups open lots, aggregates cost basis/market value/gains by term

---

## Lambdas That Produce Portal JSON

### bd-portal-advisor-publisher
- **Path:** `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py`
- **Reads:** `gold/account_performance.parquet`, `gold/views/client_tax_liability.parquet`, `gold/client_dimension.parquet`, `gold/holdings_lots/` (latest)
- **Writes:** `gold/implementor_leaderboard.json`, `gold/advisors/{id}/book.json`, `gold/clients/{id}.json`
- **AUA Calculation:** `acct[acct['date'] == latest_date]['total_aua'].sum()` → reports $68.5M
- **This is where the $68.5M figure comes from.** It's a straight sum of total_aua on latest date from account_performance.parquet.

### bd-portal-publisher
- **Path:** `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`
- **Reads:** `gold/client_performance.parquet`, `gold/accounts_dimension_latest.parquet`, `gold/client_dimension.parquet`, `gold/views/client_tax_liability.parquet`
- **Writes:** Aggregate portal JSON (leaderboard, timeseries, snapshots, filters, summary)
- **Key Question:** Does this Lambda's header_metrics.json show a different AUA figure?

### bd-gold-layer (Lambda)
- **Path:** `infra/aws/lambda/bd-pipeline/bd-gold-layer/lambda_function.py`
- **Reads:** `silver/bd_transactions.parquet`, `silver/bd_accounts.parquet`
- **Writes:** 23 gold layer files (1 parquet + 22 JSONs): timeseries, snapshots, clients, filters, summary
- **Logs:** Total AUA, NNA YTD/12M

---

## Supporting Lambdas (Not Data Transformation)

| Lambda | Purpose |
|--------|---------|
| bd-allocation-processor | Converts daily ALLOC_DAILY_*.xlsx → silver/allocations/{date}.parquet, triggers bd-price-update |
| bd-price-update | Maintains canonical_prices.parquet (4-tier: T1 transaction, T2 yahoo, T3 interpolation, T4 carry-forward) |
| bd-gold-trigger | Starts EC2 gold layer instance |
| bd-gold-foundation | Maintains canonical timeline (first_seen_date per relationship) |
| bd-gold-detail-checker | Polls EC2 completion marker |
| bd-client-detail | Auth gate + S3 GET proxy (no computation) |

---

## Investigation Starting Points

1. **Check 05b output directly:**
   ```python
   df = pd.read_parquet('s3://opal-data-bd/gold/account_performance.parquet')
   latest = df['date'].max()
   print(f"Latest date: {latest}")
   print(f"Total AUA: ${df[df['date'] == latest]['total_aua'].sum():,.0f}")
   print(f"Unique accounts: {df[df['date'] == latest]['account_id'].nunique()}")
   print(f"Unique relationships: {df[df['date'] == latest]['relationship_id'].nunique()}")
   ```

2. **Compare 05 vs 05b:**
   ```python
   cp = pd.read_parquet('s3://opal-data-bd/gold/client_performance.parquet')
   ap = pd.read_parquet('s3://opal-data-bd/gold/account_performance.parquet')
   latest = cp['date'].max()
   print(f"client_performance AUA: ${cp[cp['date'] == latest]['total_aua'].sum():,.0f}")
   print(f"account_performance AUA: ${ap[ap['date'] == latest]['total_aua'].sum():,.0f}")
   ```

3. **Check positions_cube coverage:**
   ```python
   # Latest date partition
   pos = pd.read_parquet(f's3://opal-data-bd/gold/positions_cube/{latest}.parquet')
   print(f"Accounts in positions_cube: {pos['account_id'].nunique()}")
   ```

4. **Check price coverage:**
   ```python
   prices = pd.read_parquet('s3://opal-data-bd/silver/prices/canonical_prices.parquet')
   # How many assets have prices on latest date?
   print(prices[prices['date'] == latest]['asset_name'].nunique())
   ```

5. **Check bd-portal-publisher's header_metrics.json for a different AUA figure**

The most likely causes:
- **Price gaps:** Assets in positions_cube without matching prices → AUA = 0 for those positions
- **Missing accounts in positions_cube:** 02 not processing all transaction files
- **Date mismatch:** 05b latest date != actual latest allocation date
- **Filter/join dropping rows:** Left join in 05b losing accounts without dimension matches
