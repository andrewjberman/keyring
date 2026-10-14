# G2f -- 49F Black Diamond: live prefixes in `opal-data-bd/silver/` mapped to G2a's contracts

**archetype:** EXPLORE

- **Author:** 4.0.0_SA_CRO~Z, 2026-10-14 ~15:1xZ, directly (no subagent).
- **Ask:** 1.0.0_SA_CTO~Z msg 34128 (for COO~MI msg 34126, round 14 and the `client_*` BD adapter).
- **Read only.** T-1 = 2026-10-13 (`lib/trading_calendar.py`).

## (a) Method

| read | instrument | denominator |
|---|---|---|
| `opal-data-bd/silver/` | `list_objects_v2`, paginated | 8,119 keys; 36 first-level entries (9 partitioned tables + 27 single-file parquets / manifests) |
| each mapped table | full listing of its prefix; Parquet footer of the newest `.parquet` by LastModified | 8 tables |
| schema compare | live newest footer vs the G2a contract's column list (`schema_union` across its parts) | 8 of 8 |
| firm check | first 3 chars of the account id column on the newest part | 8 tables |

## (b) Map: G2a 49F contract -> live table

| G2a contract (frozen copy) | live prefix | key shape | newest partition | behind T-1 | objects | schema vs contract |
|---|---|---|---|---|---|---|
| `blackdiamond/49financial/silver_legacy/fees/` | `opal-data-bd/silver/fees/` | `silver/fees/<d>.parquet` | 2026-10-12 | 1 | 2006 | EQUAL (same column names; every live type is a member of the contract's type union) |
| `blackdiamond/49financial/silver_legacy/transactions/` | `opal-data-bd/silver/transactions/` | `silver/transactions/<d>.parquet` | 2026-10-14 | 0 | 1929 | LIVE IS A SUBSET (5 contracted column(s) absent live; no new column; types compatible) |
| `blackdiamond/49financial/silver_legacy/transactions_enriched/` | `opal-data-bd/silver/transactions_enriched/` | `silver/transactions_enriched/date=<d>/data.parquet` | 2026-04-20 | 122 | 519 | EQUAL (same column names; every live type is a member of the contract's type union) |
| `blackdiamond/49financial/silver_legacy/allocations/` | `opal-data-bd/silver/allocations/` | `silver/allocations/<d>.parquet` | 2026-10-09 | 2 | 135 | LIVE IS A SUBSET (100 contracted column(s) absent live; no new column; types compatible) |
| `blackdiamond/49financial/silver_legacy/assets/` | `opal-data-bd/silver/assets/` | `silver/assets/<d>.parquet` | 2026-06-18 | 80 | 1890 | EQUAL (same column names; every live type is a member of the contract's type union) |
| `blackdiamond/49financial/silver_legacy/realized/` | `opal-data-bd/silver/realized/` | `silver/realized/<d>.parquet` | 2026-10-14 | 0 | 1359 | LIVE IS A SUBSET (1 contracted column(s) absent live; no new column; types compatible) |
| `blackdiamond/49financial/silver_legacy/unrealized/` | `opal-data-bd/silver/unrealized/` | `silver/unrealized/<d>.parquet` | 2026-10-09 | 2 | 77 | EQUAL (same column names; every live type is a member of the contract's type union) |
| `blackdiamond/49financial/silver_legacy/prices/` | `opal-data-bd/silver/prices/` | `silver/prices/<d>.parquet` | 2026-10-14 | 0 | 176 | EQUAL (same column names; every live type is a member of the contract's type union) |

**G2a 49F contracts with NO live counterpart in `opal-data-bd/silver/`** (they stay where G2a contracted them):

- `blackdiamond/49f/silver/dim_account_xref/`
- `blackdiamond/49f/silver/dim_advisor_fee_role/`
- `blackdiamond/49f/silver/fact_bd_allocation/`
- `blackdiamond/49f/silver/fact_taxsma_report/`
- `blackdiamond/49financial/silver/fact_insurance_insurancerelationshiplist_export/`
- `blackdiamond/49financial/silver/fact_insurance_relationshipaccountdetailsearch/`
- `blackdiamond/49financial/silver/fact_insurance_relationshipdetail/`
- `blackdiamond/49financial/silver_legacy/_single_file/`

- The four `blackdiamond/49f/silver/` tables are written by `opal-assets-bd49f-dim-convert`, out of memory since 2026-09-29 (Z-S110).
- The three insurance tables are written under `blackdiamond/49financial/silver/` itself.

## (c) Notes for the adapter

1. **Key shape.** The partitions are date-NAMED FILES (`silver/<table>/YYYY-MM-DD.parquet`), not `date=` directories. Only `transactions_enriched` uses `date=YYYY-MM-DD/data.parquet`.
   - The adapter derives the partition from the file name.
   - Non-dated siblings are not partitions: `transactions/_README.txt`, `realized/bd_realized_agg.parquet`, `unrealized/unrealized_gain_loss.parquet`, `prices/canonical_prices.parquet` (the newest-WRITTEN prices object) and `prices/backfill_telemetry.json`.
2. **Stale live tables:** `assets` stops at 2026-06-18 and `transactions_enriched` at 2026-04-20.
   - Both are live in name only. Serve them with their lag, or not at all; the CTO's call.
   - The live current tables are fees, transactions, realized, prices (dated to 2026-10-12..14), and allocations and unrealized (2026-10-09).
3. **`allocations`.** The contract's 194 columns are the union of a Title-Case raw generation and the snake_case generation. The live newest has the 94 snake_case columns only, so map the adapter to the snake_case names.
4. **`transactions` drops 5 contracted columns live:** `account_start_date`, `is_new_client`, `is_nna`, `is_nna_inflow`, `is_nna_outflow`. The NNA flags are not in the live table.
5. **`realized` drops `last_sell_date` live.**
6. **Firm:** see each row's `firm_check`. The bucket is single-firm, so the fence is the bucket. A tool never reads it for any firm but `49financial`.
7. **Snapshot check (not run here):** whether each date file is a full snapshot or a daily increment was not measured. The `incremental_*_manifest.json` siblings suggest increments for transactions, realized, unrealized and allocations.
   - Measure one key's row count across two adjacent files before any tool sums dates.

## (d) Per-table records

### `s3://opal-data-bd/silver/fees/`

```json
{
 "table": "fees",
 "contracted": "blackdiamond/49financial/silver_legacy/fees/",
 "live": "s3://opal-data-bd/silver/fees/",
 "key_shape": "silver/fees/<d>.parquet",
 "objects": 2006,
 "parquet_files": 2006,
 "dates": "2020-03-06..2026-10-12",
 "newest_partition": "2026-10-12",
 "newest_write_utc": "2026-10-13T22:21Z",
 "newest_key": "silver/fees/2026-10-12.parquet",
 "trading_days_behind_t1": 1,
 "columns_live": 34,
 "columns_contracted": 34,
 "only_contract": [],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "EQUAL (same column names; every live type is a member of the contract's type union)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 710} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/transactions/`

```json
{
 "table": "transactions",
 "contracted": "blackdiamond/49financial/silver_legacy/transactions/",
 "live": "s3://opal-data-bd/silver/transactions/",
 "key_shape": "silver/transactions/<d>.parquet",
 "objects": 1929,
 "parquet_files": 1928,
 "dates": "2020-03-06..2026-10-14",
 "newest_partition": "2026-10-14",
 "newest_write_utc": "2026-10-14T00:13Z",
 "newest_key": "silver/transactions/2026-10-14.parquet",
 "trading_days_behind_t1": 0,
 "columns_live": 74,
 "columns_contracted": 79,
 "only_contract": [
  "account_start_date",
  "is_new_client",
  "is_nna",
  "is_nna_inflow",
  "is_nna_outflow"
 ],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "LIVE IS A SUBSET (5 contracted column(s) absent live; no new column; types compatible)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 2921} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/transactions_enriched/`

```json
{
 "table": "transactions_enriched",
 "contracted": "blackdiamond/49financial/silver_legacy/transactions_enriched/",
 "live": "s3://opal-data-bd/silver/transactions_enriched/",
 "key_shape": "silver/transactions_enriched/date=<d>/data.parquet",
 "objects": 519,
 "parquet_files": 518,
 "dates": "2024-04-12..2026-04-20",
 "newest_partition": "2026-04-20",
 "newest_write_utc": "2026-04-21T17:07Z",
 "newest_key": "silver/transactions_enriched/date=2026-04-20/data.parquet",
 "trading_days_behind_t1": 122,
 "columns_live": 80,
 "columns_contracted": 80,
 "only_contract": [],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "EQUAL (same column names; every live type is a member of the contract's type union)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 35} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/allocations/`

```json
{
 "table": "allocations",
 "contracted": "blackdiamond/49financial/silver_legacy/allocations/",
 "live": "s3://opal-data-bd/silver/allocations/",
 "key_shape": "silver/allocations/<d>.parquet",
 "objects": 135,
 "parquet_files": 135,
 "dates": "2026-01-16..2026-10-09",
 "newest_partition": "2026-10-09",
 "newest_write_utc": "2026-10-11T00:19Z",
 "newest_key": "silver/allocations/2026-10-09.parquet",
 "trading_days_behind_t1": 2,
 "columns_live": 94,
 "columns_contracted": 194,
 "only_contract": [
  "49 House Split %",
  "49_house_split_%",
  "Account - Billing Notes",
  "Account Allocation",
  "Account Benchmark",
  "Account Billable",
  "Account Category",
  "Account Create Date",
  "Account Discretionary",
  "Account Display Name",
  "Account Display Number",
  "Account Fee Schedule",
  "Account Is Open",
  "Account Market Value",
  "Account Name",
  "Account Number",
  "Account Owner",
  "Account Owner Type",
  "Account Registration Type",
  "Account Subcategory",
  "Account Supervised",
  "Account Type",
  "AccountID",
  "Additional Advisor",
  "Additional Advisor Split %",
  "Address Source City",
  "Address Source Client Name",
  "Address Source State",
  "Address Source Zip Code",
  "Architect",
  "Architect Split %",
  "As of Date",
  "Basis Points",
  "Basis Points.1",
  "Cash Allocation",
  "Cash Market Value",
  "Client City",
  "Client Name",
  "Client State",
  "Client Zip Code",
  "Closed Date",
  "Consultant",
  "Consultant Split %",
  "Fee Schedule Description",
  "Fee Schedule Description.1",
  "Fee Schedule Level",
  "Fee Schedule Level.1",
  "Fee Schedule Rate Type",
  "Fee Schedule Rate Type.1",
  "Fee Schedule Type",
  "Fee Schedule Type.1",
  "Flat Fee",
  "Flat Fee.1",
  "Goal",
  "History Start Date",
  "History Start Date.1",
  "Implementor",
  "Implementor Split %",
  "Investment Strategy Name",
  "Local Ops",
  "Local Ops Split %",
  "Lower Range",
  "Lower Range.1",
  "Managed Account Manager Name",
  "Manager",
  "Manager Strategy",
  "Original Account Name",
  "Original Account Number",
  "Performance Start Date",
  "Portfolio Benchmark",
  "Portfolio Fee Schedule",
  "Portfolio Group",
  "Portfolio Group Market Value",
  "Portfolio Logo",
  "Portfolio Name",
  "Portfolio Reporting Target",
  "PortfolioID",
  "Relationship Display Name",
  "Relationship ID",
  "Relationship Inception Date",
  "Relationship Name",
  "Relationship SEC Client Type",
  "Relationship Termination Date",
  "Rep Code",
  "Reporting Target Description",
  "Reporting Target Description.1",
  "Show Client",
  "Start Date",
  "Style",
  "Tax Lot Methodology",
  "Tax Status",
  "Upper Range",
  "Upper Range.1",
  "account_-_billing_notes",
  "additional_advisor_split_%",
  "architect_split_%",
  "consultant_split_%",
  "implementor_split_%",
  "local_ops_split_%",
  "portfolioid"
 ],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "LIVE IS A SUBSET (100 contracted column(s) absent live; no new column; types compatible)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 7345} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/assets/`

```json
{
 "table": "assets",
 "contracted": "blackdiamond/49financial/silver_legacy/assets/",
 "live": "s3://opal-data-bd/silver/assets/",
 "key_shape": "silver/assets/<d>.parquet",
 "objects": 1890,
 "parquet_files": 1890,
 "dates": "2020-03-06..2026-06-18",
 "newest_partition": "2026-06-18",
 "newest_write_utc": "2026-06-19T22:12Z",
 "newest_key": "silver/assets/2026-06-18.parquet",
 "trading_days_behind_t1": 80,
 "columns_live": 31,
 "columns_contracted": 31,
 "only_contract": [],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "EQUAL (same column names; every live type is a member of the contract's type union)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 25332} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/realized/`

```json
{
 "table": "realized",
 "contracted": "blackdiamond/49financial/silver_legacy/realized/",
 "live": "s3://opal-data-bd/silver/realized/",
 "key_shape": "silver/realized/<d>.parquet",
 "objects": 1359,
 "parquet_files": 1359,
 "dates": "2021-01-04..2026-10-14",
 "newest_partition": "2026-10-14",
 "newest_write_utc": "2026-10-14T00:13Z",
 "newest_key": "silver/realized/2026-10-14.parquet",
 "trading_days_behind_t1": 0,
 "columns_live": 15,
 "columns_contracted": 16,
 "only_contract": [
  "last_sell_date"
 ],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "LIVE IS A SUBSET (1 contracted column(s) absent live; no new column; types compatible)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 45208} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/unrealized/`

```json
{
 "table": "unrealized",
 "contracted": "blackdiamond/49financial/silver_legacy/unrealized/",
 "live": "s3://opal-data-bd/silver/unrealized/",
 "key_shape": "silver/unrealized/<d>.parquet",
 "objects": 77,
 "parquet_files": 77,
 "dates": "2026-03-27..2026-10-09",
 "newest_partition": "2026-10-09",
 "newest_write_utc": "2026-10-11T00:20Z",
 "newest_key": "silver/unrealized/2026-10-09.parquet",
 "trading_days_behind_t1": 2,
 "columns_live": 17,
 "columns_contracted": 17,
 "only_contract": [],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "EQUAL (same column names; every live type is a member of the contract's type union)",
 "firm_check": "account_id first-3-char prefixes on the newest part: {'z08': 108439} (z08 = 49F per G2a; z09 = Cottonwood)"
}
```

### `s3://opal-data-bd/silver/prices/`

```json
{
 "table": "prices",
 "contracted": "blackdiamond/49financial/silver_legacy/prices/",
 "live": "s3://opal-data-bd/silver/prices/",
 "key_shape": "silver/prices/<d>.parquet",
 "objects": 176,
 "parquet_files": 175,
 "dates": "2026-02-22..2026-10-14",
 "newest_partition": "2026-10-14",
 "newest_write_utc": "2026-10-14T12:48Z",
 "newest_key": "silver/prices/canonical_prices.parquet",
 "trading_days_behind_t1": 0,
 "columns_live": 5,
 "columns_contracted": 5,
 "only_contract": [],
 "only_live": [],
 "incompatible_types": [],
 "schema_verdict": "EQUAL (same column names; every live type is a member of the contract's type union)",
 "firm_check": null
}
```

## (e) What could not be read

- Whether the date files are snapshots or increments (note 7).
- The producer of the live `opal-data-bd/silver/` tables: G2a found both scheduled rules DISABLED and did not trace the writer. Not re-traced here.
- The 27 single-file objects at `opal-data-bd/silver/*.parquet` are listed in (a) but not contracted. `bd_assets_dim.parquet` (2026-10-13), `historical_prices.parquet` (2026-10-14) and `interpolated_prices.parquet` (2026-10-14) are live; the rest last wrote between 2026-01 and 2026-06.

-- 4.0.0_SA_CRO~Z
