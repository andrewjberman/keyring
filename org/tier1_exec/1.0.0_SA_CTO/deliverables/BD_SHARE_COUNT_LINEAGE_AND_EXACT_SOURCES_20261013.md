# 49 Financial share counts -- where they come from today, and where exact ones are (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~12:4xZ)

Asked by Andrew-direct 2026-10-13 ~12:2xZ ("how we are getting share counts ... what data is coming from where in what endpoint and how we're making use of that").
Method: a read-only repo read (code and templates, no AWS). The two load-bearing claims are re-verified by this seat at the cited lines (marked VERIFIED).

## 1. Where B_01's share counts come from today

| source | upstream (endpoint / export) | lands at | how B_01 uses it | exact? |
|---|---|---|---|---|
| **FIFO over transactions** (the default; includes the capped 13 pct) | BD DataMining query type 2 (Transactions), pulled by `bd-49f-runner` (`infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py:5-7,74`) | `forwardfill_v2/transactions/` to `silver/transactions/` | `load_transactions` (B_01:234-316), `build_holdings_lots_snapshot` (:2510-2617) | NO: transfer-ins and un-netted redemptions are missing from the history |
| **Schwab RPS** (`rps_injection`) | Schwab RPS position file, master 0824 only (`_monolith_bronze.py:29-31`) | `opal-data-assets/schwab/08242234/bronze/rps/` to `opal-data-bd/schwab/silver/rps/` | units = RPS `quantity_settled` minus FIFO (B_01:1490,1647) | units YES; cost basis NO (`cost_per_unit` = current price, :1662) |
| **synthetic injection** | none: built from an account's leftover value divided by our canonical price | n/a | B_01:1985-2019 | NO (an estimate; the design doc's "silver-derived" is wrong) |
| **HLOT2 re-open** | `gold/canonical/holdings.units` (Schwab where reconciled, else FIFO `positions_cube`) | gold | B_01:1286-1331 | partly |
| **ULN sleeve lots** | value apportioned by `unit_cost` | n/a | B_01:907-913 | NO |

The price tags (`linear_interpolation`, `bd_txn_price`, `scoped_override`) are PRICE sources, not unit sources. Those lots' units are plain FIFO. The cap design treats `scoped_override`
as external unit authority, and that is wrong: only the price was overridden.

## 2. Exact sources that exist and are NOT used

1. **BD's unrealized export already offers Units and Cost Basis, and 49 Financial has them SWITCHED OFF. VERIFIED.**
   - In `data/black_diamond/scripts/bronze/templates/unrealized.json` (around :319-337), "Units" (measure 15) and "Cost Basis" (measure 16) read `"isSelected": false`.
   - The Cottonwood template for the same export has both `"isSelected": true` (`data/cot/scripts/bronze/templates/unrealized.json` around :3912-3928).
   - This is BD's own per-position units and cost, for EVERY account and custodian, from the export we already pull daily.
2. **Our silver step throws away lots from that export. VERIFIED.** `process_unrealized_xlsx_to_parquet` (`data/black_diamond/scripts/silver/merge-daily-incremental.py:1138`) de-duplicates by
   `(account_id, asset_name)`, keeping the first row (:1205-1210). Every tax lot after the first in a position is dropped. With Units and Cost Basis on, the key must include
   the lot (`open_date`, `unit_cost`), or the exact data is cut back to one lot per position.
3. **BD's Snapshot/holdings export (query type 1) carries Units.** Cottonwood ingests it (`cot_silver_merge.py:116-122`); the 49F runner leaves it out (runner:73-74).
4. **Schwab ULN/RLD lot files carry `quantity`, `cost_basis` and `adjusted_cost_basis` per lot** (`convert_schwab_lots_to_silver.py:62-72,93-102`). B_02 uses them and B_01
   does not. They are exact for Schwab lots.
5. **Schwab master 0833 RPS is never converted.** It may cover some of the uncovered accounts.

**No BD REST holdings, positions or taxlots API is used anywhere.** Everything comes through DataMining exports.

## 3. Can the counts be derived?

- **Market value divided by price is not exact today:** prices come from Yahoo or interpolation, not BD's; the export runs one business day back; and bond accrual is not
  selected. It would be close to exact only on Schwab RPS accounts, which already have exact units.
- **`unit_cost` alone cannot give units.** It needs the total Cost Basis, which is the measure that is switched off.

## 4. The plan (the first cells of the BD pricing-rules project; each is a read or a reversible config change)

1. **Turn on Units and Cost Basis** in the 49F unrealized template (an S3 template copy the runner reads; confirm the S3 copy matches the repo first), AND change the silver
   de-duplication key to the lot. One day's export then shows BD's exact units and cost per lot.
2. **Measure, on that day:** for the 64,629 capped lots, BD units against FIFO units, and BD cost against FIFO cost, per lot, with the denominator printed. This tells us exactly
   how wrong the estimates were.
3. **Rule on authority:** where BD units exist, they replace FIFO for valuation; Schwab ULN/RPS stays authoritative where present; and any lot with neither stays UNVERIFIED
   (Andrew's ruling). The cap then has nothing left to estimate.
4. **Secondary:** add the Snapshot export (qt1), feed Schwab ULN lot cost into B_01 (RPS cost is set to the price today), and check master 0833's coverage.
5. **Tag each account's custodian** (BD `/api/custodian/search`) to see which custodians the uncovered accounts sit at.

-- 1.0.0_SA_CTO~DELL1
