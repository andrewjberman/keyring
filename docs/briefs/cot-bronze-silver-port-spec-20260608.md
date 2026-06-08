# ADVI_COTETL — COT (Cottonwood) Bronze/Silver Port Spec: Recreating the bd-pipeline Tables

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-08 · **Project:** ADVI_COTETL (was ADVI_CCAETL)
**Companions:** Brief 1 (DataMining API), table↔endpoint cross-ref (`864419a80`), Brief 3 (medallion).
**Goal (Andrew-direct):** specify exactly how to structure scripts to recreate each bd-pipeline bronze/silver table for COT, so we **largely port the same scripts**.

---

## 0. Headline — the port is "1 new script + env-repoint"

The bd-pipeline silver layer is **already a generic, firm-agnostic engine**. The entire bronze→silver path for the 4 incremental BD tables is one script, `silver/merge-daily-incremental.py`, parameterized per table, and its bucket is **already** `os.environ.get('BD_S3_BUCKET', 'opal-data-bd')`.

```
process_xlsx_to_parquet():                  process_alloc_xlsx_to_parquet():   (same shape)
  df = read_excel(sheet_name='Sheet1')      one generic converter per table:
  df.columns = [to_snake_case(c) ...]   <-- THE compatibility hinge
  file_date = read 'End Date' from the 'Timestamps' sheet
  7-day dedup on transaction_id -> write silver/{table}/{date}.parquet
```

**`to_snake_case`**: `strip` → `% → pct` → `49 House → house` → spaces/`.`/`-` → `_` → lowercase → collapse `__`.

**The compatibility guarantee:** `silver column name == to_snake_case(BD DataMining dimension display-name)`. So **if the COT template selects dimensions with the same display-names 49F selected, the silver schema is identical and every downstream script (silver + gold) ports unchanged.** The target schema per table is the live 49F silver parquet (pulled from S3 below — authoritative).

**What's genuinely new vs. ported:**

| Layer | Effort | Detail |
|---|---|---|
| **Bronze ingest** | **NEW (the only new code)** | Per table: a DataMining template (queryTypeId + the dimension/fact selection below) → `v1/run` → poll → `ExportResults` xlsx → land at `opal-data-cot/forwardfill_v2/{table}/{TABLE}_DAILY_{date}.xlsx`. BD emits the `Timestamps` sheet natively, so silver's date-detection works untouched. |
| **Silver merge** | **PORT as-is** | `merge-daily-incremental.py` + `compact-realized.py` + `build_bd_assets_dim.py`, run with `BD_S3_BUCKET=opal-data-cot`. Handles transactions/allocations/realized/unrealized generically. |
| **Gold** | parameterized (separate TOs) | per Brief 3 / P4 |

---

## 1. The 5 tables → query type → target silver schema (authoritative, from S3)

For each table: the queryTypeId, the consuming script, and the **exact 49F silver column set** (read live from `s3://opal-data-bd/silver/`). The COT DataMining template must select the dimensions whose display-names snake_case to these columns (minus the silver-*derived* columns, noted).

### 1.1 Transactions — `qt=2` → `silver/transactions` (79 cols; ~71 BD dims + 8 derived)
Consumer: `merge-daily-incremental.py` (`FORWARDFILL_PREFIX=forwardfill_v2/transactions`). 49F asserts `CORRECT_COL_COUNT=71` raw export cols.

Silver cols: `transaction_id, return_date, action, transaction_type, transaction_sub_type, external_flow, description, price, trade_date, entry_date, settle_date, relationship_id, relationship_name, relationship_display_name, relationship_sec_client_type, relationship_termination_date, relationship_inception_date, previous_system_key, portfolio_name, portfolio_id, portfolio_display_name, history_start_date, account_number, account_id, original_account_number, account_display_name, account_name, original_account_name, manager, account_owner_type, account_owner, client_name, history_start_date_1, closed_date, account_is_open, performance_start_date, start_date, asset_id, asset_name, asset_display_name, fund_manager, units, market_value, transaction_fee, income, account_fee, house_split_pct, additional_advisor, additional_advisor_split_pct, architect_split_pct, consultant, architect, consultant_split_pct, implementor_split_pct, implementor, local_ops_split_pct, investment_strategy_name, manager_strategy, account_create_date, managed_account_manager_name, local_ops, tax_status, expense_ratio, custodial_cost_basis_sync, portfolio_group, tax_status_1, goal, as_of_date, client_city, client_state, client_zip_code, account_start_date`

**Derived in silver (do NOT select; computed downstream):** `is_new_client, is_nna_inflow, is_nna_outflow, is_nna` (NNA classification), `_source_file, _ingested_at` (provenance), `cusip` (joined from `bd_assets_dim`).

**vs. CW_Transactions_Rich:** Andrew's CSV selected 63 dims; 49F's transaction table needs **71** — the delta is mostly **advisor roles + splits + fee/units/market_value**. COT's template must add: `architect/implementor/consultant/local_ops/additional_advisor` (+ `_split_%` each), `house_split_%`, `units`, `market_value`, `transaction_fee`, `income`, `account_fee`, `fund_manager`, `manager`, `managed_account_manager_name`, `investment_strategy_name`, `manager_strategy`, `relationship_sec_client_type`, `previous_system_key`, `goal`, etc.

### 1.2 Allocations — `qt=5` (Andrew's `CW_Allocation` #225472) → `silver/allocations` (92 cols)
Consumer: `merge-daily-incremental.py` `process_alloc_xlsx_to_parquet` (`FORWARDFILL_ALLOC_PREFIX=forwardfill_v2/allocations`).

Carries: fee schedule (`basis_points, flat_fee, fee_schedule_*, account_billable, account_discretionary`), `account_type, account_registration_type, account_category, account_subcategory, tax_status, tax_lot_methodology`, advisor roles (`architect/implementor/consultant/local_ops/additional_advisor` + `_split_%`), `account_market_value, account_allocation, portfolio_group_market_value, cash_market_value, cash_allocation, rep_code, manager, style`, client/address fields. **This is the AUA + account-metadata + fee snapshot** — A_00's enrichment source. Andrew's `CW_Allocation` currently selects only `Market Value`; the full port needs the fee/account/advisor dimensions too.

### 1.3 Realized G/L — `qt=3` → `silver/realized` (15 cols)
Consumer: `merge-daily-incremental.py` (`FORWARDFILL_REALIZED_PREFIX`) + `compact-realized.py`.
Silver cols: `open_date, trade_date, unit_cost, account_number, account_id, asset_name, asset_id, symbol, ticker, cusip, asset_display_name, original_asset_name, last_dividend` + `_source_file, _ingested_at`. (Closed-lot cost-basis records → `gold/canonical/account_gains` B_03, C_05 tax.)

### 1.4 Unrealized G/L — `qt=4` → `silver/unrealized` (16 cols)
Consumer: `merge-daily-incremental.py` (`FORWARDFILL_UNREALIZED_PREFIX`).
Silver cols: `open_date, unit_cost, inherited_date, relationship_id, account_number, account_id, asset_id, asset_name, last_dividend, original_asset_name, asset_display_name, symbol, ticker, cusip` + `_source_file, _ingested_at`. (Open-lot cost basis → unrealized gain vs. current price in gold; `gold/canonical/lots_unrealized` → C_05.)

### 1.5 Assets/Securities dim — derived → `silver/bd_assets_dim` (22 cols)
Consumer: `build_bd_assets_dim.py` (NOT a direct export — **built** from asset dims across the other tables' Holding-level fields). Cols: `asset_id, cusip, alternative_identifier, symbol, ticker, asset_name, asset_display_name, original_asset_name, asset_super_class_bd, asset_class, asset_segment, coupon_rate, first_payment_date, last_payment_date, custodial_cost_basis_sync, first_seen_trade_date, last_seen_trade_date, txn_count, asset_super_class_blend, super_class_source, opal_asset_class, built_at`. Ports as-is (re-pointed); no separate COT query needed — its inputs ride on the transaction/realized/unrealized Holding dims.

---

## 2. The COT bronze ingest script — structure (the one new build)

One module, table-driven (mirrors how `merge-daily-incremental.py` is table-driven). Pseudocode:

```python
# cot_bronze_ingest.py  (runs on the COT exporter VM / Lambda, behind P0 auth)
SESSION = load_bd_session()                  # .bd.identity cookie from Secrets Manager (Brief 1 §4)
TOKEN   = GET /datamining/auth/token         # -> Bearer

TABLES = {
  'transactions': {qt:2, dims:[...display names per §1.1...], facts:[]},
  'allocations' : {qt:5, dims:[...§1.2...],  facts:['Market Value']},
  'realized'    : {qt:3, dims:[...§1.3...],  facts:['Proceeds','Short-Term Gain/Loss','Long-Term Gain/Loss','Cost Basis']},
  'unrealized'  : {qt:4, dims:[...§1.4...],  facts:['Unaccrued Market Value','Cost Basis','Unaccrued Short-Term Gain/Loss','Unaccrued Long-Term Gain/Loss']},
}
for name, spec in TABLES.items():
    body = build_template(spec, date_range)               # the v1/run template JSON (Brief 1 §3)
    run  = POST /datamining/request/v1/run {template:body}; guid = run['resultGuid']
    poll GET /datamining/request/v1/run/{run.templateId}/status until isComplete
    xlsx = GET /Api/DataMining/ExportResults/{guid}
    s3.put(opal-data-cot/forwardfill_v2/{name}/{NAME}_DAILY_{date}.xlsx, xlsx)   # silver picks it up unchanged
```

The `build_template` selection lists are the §1 dimensions; the realized/unrealized **measures** (Tax-Lot facts) come from the qt=3/qt=4 catalogs (HAR-2). The export's native `Timestamps` sheet satisfies silver's date-detection. After this lands the xlsx, `merge-daily-incremental.py` (env `BD_S3_BUCKET=opal-data-cot`) produces silver with **zero code change**.

---

## 3. COT deltas to handle (small, enumerated)

1. **`to_snake_case` hardcode `'49 House' → 'house'`** (line 188) is 49F-specific (the house-split dimension is literally named "49 House Split %"). COT's house/firm split dimension, if present, will have a different display-name → either it snake_cases cleanly (no special case needed) or we generalize the rule. **Verify COT's split-column display name; likely drop the 49F special-case.**
2. **Advisor roles (§6.1 link):** the 49F advisor dimension is sourced from the transaction/allocation `architect/implementor/consultant/local_ops/additional_advisor` (+ `_split_%`) columns — **not** a separate query. COT must select these in its templates; **whether they're populated is the §6.1 probe** (alongside `accountUDF1` Advisor-of-Record / `manager`). If empty → advisor-dim analytics N/A (Outcome B); geo/AUA/NNA/client unaffected.
3. **Schwab custodian path** (`convert_schwab_*`, `silver/{rps,uln,trn,acc}`) — **N/A for COT** (98.8% Fidelity). Drop from the COT port.
4. **`CORRECT_COL_COUNT=71`** transaction assertion is 49F-specific — set to COT's actual selected-dim count (or relax the assert).
5. **Date window / cadence:** Andrew's templates used `Last6Months` (txn) and `CurrentDay` (allocation). For daily incremental, the ingest runs per-day (CurrentDay/yesterday) like 49F's daily exports; a one-time backfill uses a wide window.

---

## 4. Port checklist (what gets copied, what gets written)

| Script | Action | Change |
|---|---|---|
| `silver/merge-daily-incremental.py` | **PORT** | env `BD_S3_BUCKET=opal-data-cot`; drop `'49 House'` special-case; set `CORRECT_COL_COUNT` |
| `silver/compact-realized.py` | **PORT** | env repoint |
| `silver/build_bd_assets_dim.py` | **PORT** | env repoint |
| `silver/convert_assets_to_silver.py`, `convert_fees_to_silver.py`, price builders | **PORT** | env repoint (prices = public, firm-agnostic) |
| `bronze/convert_daily_{transaction,allocation}_to_parquet.py` | PORT (if still used vs the generic merger) | env repoint |
| `bronze/convert_schwab_*`, `sync_schwab_onedrive_to_s3.py` | **DROP** | Schwab N/A for COT |
| **`cot_bronze_ingest.py`** | **NEW** | the API-first DataMining ingest, §2 — 5 templates → `forwardfill_v2/{table}/` |

---

## 5. Bottom line

Recreating COT's bronze/silver is **not a rewrite — it's one new ingest script + an env repoint.** The silver engine (`merge-daily-incremental.py`) is generic and bucket-parameterized; `silver column == snake_case(BD display-name)`, so selecting the same display-named dimensions 49F selected (the §1 schemas, pulled authoritatively from S3) reproduces byte-identical silver, and silver+gold port unchanged. The only new code is the COT DataMining ingest (§2): 5 templates (qt 2/3/4/5 + the assets-via-Holding projection), each `v1/run → ExportResults → forwardfill_v2/{table}/`, behind the P0 auth infra (Brief 1 §4). Deltas are small and enumerated (§3). The advisor-role columns tie directly to the §6.1 probe. Schwab is dropped.
