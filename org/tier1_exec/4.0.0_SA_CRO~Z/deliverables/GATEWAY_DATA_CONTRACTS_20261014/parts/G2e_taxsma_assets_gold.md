# G2e -- Tax SMA assets gold (`mdpf/<firm>/gold/taxsma_assets/` in the per-firm buckets)

**archetype:** EXPLORE

- **Author:** 4.0.0_SA_CRO~Z, 2026-10-14 ~14:3xZ. Written directly by the CRO; no subagent.
- **Ask:** 1.0.0_SA_CTO~Z msg 34115: contract the uncensused taxsma_assets gold as a G2 part, the Tax SMA adapter's served form.
- **Key path correction:** the table is NOT at the bucket root.
  - `taxsma_assets/` holds 0 keys in both buckets.
  - It lives at `mdpf/<firm>/gold/taxsma_assets/date=YYYY-MM-DD/data.parquet`: 14 keys per firm, 2026-10-01..10-14.
  - Each firm has one sibling state object, `mdpf/<firm>/state/taxsma_membership/dispositions.json`.

## (a) Method

| read | instrument | denominator |
|---|---|---|
| both buckets in full | `list_objects_v2`, paginated | opal-data-49financial 104,494 keys (15 contain `taxsma`); opal-data-cottonwood 7,638 keys (15) |
| schema + rows | pyarrow read of every part | 14 of 14 per firm, 1 schema variant each |
| enums, last-4 | full read of the newest part (account values reduced to shape and last-4 counts, never printed) | 13 rows (49financial), 2 rows (cottonwood) |
| producer | Grep for `taxsma_assets` in `data/` (13 files) and `infra/` (4 files); `lambda get-function-configuration mdpf-gold-lambda` | -- |

## (b)-(c) Analysis

- **What it is:** the dated Tax SMA account ledger, one row per enrolled account. It carries:
  - the custodian-measured value (Schwab `fact_rps_s2.net_mv_plus_cash` for 49F; BD Cottonwood `fact_holdings` market value);
  - the workbook AUM fallback where the custodian has no match (49F only, Andrew-direct 2026-09-30);
  - the membership date and identity status.
- **Freshness:** valuation_date 2026-10-13, 0 trading days behind T-1.
- **Layout:** each date partition is one part holding the full account set, so the newest partition is the answer and partitions are never summed.
- **Firm fence:** the bucket itself (one firm per bucket) plus the `firm` column. A tool reads one bucket per call.
- **Last-4:** 0 collisions within each firm (13 and 2 accounts). It still resolves through `client_resolve_account`, so one rule holds for every client tool.
- **Relation to G2d:** G2d contracted the Tax SMA WORKBOOK (`opal-data-assets/gateway/`, multi-firm, RIA column), which is the membership SOURCE. This table is the served, per-firm, valued FORM. The Tax SMA adapter answers from this table, never from the workbook.

## (d) Contracts

### `opal-data-49financial/mdpf/49financial/gold/taxsma_assets/`

```json
{
 "contract_id": "opal-data-49financial/gold/mdpf.49financial.taxsma_assets",
 "bucket": "opal-data-49financial",
 "s3_prefix": "mdpf/49financial/gold/taxsma_assets/",
 "layer": "gold",
 "format": "parquet",
 "table": "taxsma_assets",
 "grain": "one row per Tax SMA account per (valuation_date, knowledge_date); each date partition is ONE part file holding that date's full account set (newest partition = current answer)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "mdpf-gold-lambda (LastModified 2026-10-13T13:55Z), module data/mdpf/scripts/gold/taxsma_assets.py (S05 TX-m-4 dated-assets builder)",
  "schedule": null,
  "claim": "inferred",
  "basis": "repo Grep of the prefix: build_package.py packages the taxsma modules; the schedule was not read"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "valuation_date": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "claim": "measured"
 },
 "size": {
  "objects": 14,
  "partitions": "2026-10-01..2026-10-14",
  "rows_newest_partition": 13,
  "rows_by_date": {
   "2026-10-01..10-02": 11,
   "2026-10-03..10-08": 12,
   "2026-10-09..10-14": 13
  },
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "observation_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "account_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "valuation_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "knowledge_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "observed_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_effective_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_date_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "workbook_snapshot_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "workbook_row_number",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "business_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "identity_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "technical_enrollment",
   "type": "string",
   "nullable": true
  },
  {
   "name": "canonical_source_ref",
   "type": "string",
   "nullable": true
  },
  {
   "name": "balance_source_ref",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source_hashes",
   "type": "list<string>",
   "nullable": true
  },
  {
   "name": "value_usd",
   "type": "decimal128(20,2)",
   "nullable": true
  },
  {
   "name": "basis",
   "type": "string",
   "nullable": true
  },
  {
   "name": "value_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "reason_codes",
   "type": "list<string>",
   "nullable": true
  },
  {
   "name": "supersedes_observation_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_date_basis",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_source_event_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "firm",
   "type": "string",
   "nullable": true
  },
  {
   "name": "value_basis",
   "type": "string",
   "nullable": true
  }
 ],
 "enums": {
  "identity_status": [
   "EXACT_MATCH",
   "MISSING_CUSTODIAN",
   "STRATEGY_CONFLICT"
  ],
  "business_status": [
   "TRADED_CLAIM"
  ],
  "value_status": [
   "COMPLETE"
  ],
  "value_basis": [
   "CUSTODIAN_MEASURED",
   "WORKBOOK_STATED"
  ],
  "membership_date_status": [
   "OBSERVED_TRADED"
  ],
  "technical_enrollment": [
   "UNAVAILABLE"
  ],
  "membership_date_basis": [
   "FIRST_OBSERVED_UTC"
  ],
  "reason_codes": [
   "MISSING_CUSTODIAN",
   "STRATEGY_CONFLICT"
  ],
  "basis": [
   "schwab 0008335338 fact_rps_s2.net_mv_plus_cash",
   "workbook AUM (Mn) x 1,000,000 (absent-from-custodian fallback, Andrew-direct 2026-09-30)"
  ],
  "claim": "measured on the newest partition"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "bucket opal-data-49financial + key segment mdpf/49financial/ + column firm",
   "values": [
    "49financial"
   ]
  },
  "account": {
   "column": "account_key",
   "shape": "10 digits (custodian account number)",
   "last4_derivation": "last 4 characters of account_key",
   "last4_collisions_within_firm": 0,
   "distinct_accounts": 13,
   "claim": "measured on the newest partition"
  },
  "platform": {
   "column": null,
   "values": [],
   "note": "no platform column; the custodian is named in basis / canonical_source_ref (Schwab fact_rps_s2 or Black Diamond fact_holdings) -- serve it as platform_label with platform_label_source='basis' (v3.1 Ruling 4)"
  }
 },
 "nl_tags": [
  "tax sma accounts",
  "tax-managed sma assets",
  "tax sma aum by account",
  "tax sma membership",
  "which accounts are in the tax sma"
 ],
 "common_queries": [
  "Which accounts are enrolled in the Tax SMA for this firm and what is each one's value?",
  "When did account ****1234 join the Tax SMA?",
  "How much Tax SMA AUM did the firm hold on a given date?",
  "Which Tax SMA accounts have no custodian match?"
 ],
 "never_sum_rules": [
  "one firm per call: the two firms live in two buckets and are never summed in one answer",
  "value_basis WORKBOOK_STATED rows are the workbook's AUM fallback, not custodian-measured: report the basis per row and never present a mixed total as measured",
  "never sum partitions: each date partition is that date's full account set"
 ],
 "existing_gateway_tool": {
  "name": "none reads this table; G2d contracts the Tax SMA WORKBOOK (opal-data-assets gateway/ prefix) as the membership source",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "client_get_taxsma_accounts",
   "inputs": {
    "firm": "49financial|cottonwood (one)",
    "account_last4": "optional; resolves through client_resolve_account",
    "as_of": "date partition, default newest"
   },
   "returns": "account (masked), membership_effective_date, value_usd, value_basis, basis (as platform_label), identity_status, reason_codes, valuation_date, knowledge_date",
   "answers": [
    "Which accounts are enrolled in the Tax SMA for this firm and what is each one's value?",
    "When did account ****1234 join the Tax SMA?",
    "Which Tax SMA accounts have no custodian match?"
   ],
   "admission": "DATA_GRANT class (v3.1 Ruling 2): the firm's data grant"
  }
 ],
 "catalog_entry": {
  "data_catalog_key": null,
  "present": false
 },
 "prior_art": "org/standards/MDPF_TAXSMA_DATA_CONTRACT.json v0.6.0 (cited by the producer's docstring); org/missions/D8/MDPF/MDPF_TAXSMA/",
 "open_items": [
  "the schedule of mdpf-gold-lambda for this table was not read",
  "the sibling state object mdpf/49financial/state/taxsma_membership/dispositions.json (a list, one entry per account) is the membership store the table reads; it is state, not served"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 s3://opal-data-49financial/ (full bucket) and prefix mdpf/49financial/gold/taxsma_assets/: 14 keys",
   "at": "2026-10-14T14:28Z"
  },
  {
   "read": "pyarrow read of all 14 parts (schema + num_rows); full read of the newest part for enums and last-4 (values not printed)",
   "at": "2026-10-14T14:30Z"
  }
 ]
}
```

### `opal-data-cottonwood/mdpf/cottonwood/gold/taxsma_assets/`

```json
{
 "contract_id": "opal-data-cottonwood/gold/mdpf.cottonwood.taxsma_assets",
 "bucket": "opal-data-cottonwood",
 "s3_prefix": "mdpf/cottonwood/gold/taxsma_assets/",
 "layer": "gold",
 "format": "parquet",
 "table": "taxsma_assets",
 "grain": "one row per Tax SMA account per (valuation_date, knowledge_date); each date partition is ONE part file holding that date's full account set (newest partition = current answer)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "mdpf-gold-lambda (LastModified 2026-10-13T13:55Z), module data/mdpf/scripts/gold/taxsma_assets.py (S05 TX-m-4 dated-assets builder)",
  "schedule": null,
  "claim": "inferred",
  "basis": "repo Grep of the prefix: build_package.py packages the taxsma modules; the schedule was not read"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "valuation_date": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "claim": "measured"
 },
 "size": {
  "objects": 14,
  "partitions": "2026-10-01..2026-10-14",
  "rows_newest_partition": 2,
  "rows_by_date": {
   "2026-10-14": 2,
   "other dates": "num_rows not printed"
  },
  "schema_variants": 1,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "observation_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "account_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "valuation_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "knowledge_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "observed_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_effective_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_date_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "workbook_snapshot_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "workbook_row_number",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "business_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "identity_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "technical_enrollment",
   "type": "string",
   "nullable": true
  },
  {
   "name": "canonical_source_ref",
   "type": "string",
   "nullable": true
  },
  {
   "name": "balance_source_ref",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source_hashes",
   "type": "list<string>",
   "nullable": true
  },
  {
   "name": "value_usd",
   "type": "decimal128(20,2)",
   "nullable": true
  },
  {
   "name": "basis",
   "type": "string",
   "nullable": true
  },
  {
   "name": "value_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "reason_codes",
   "type": "list<string>",
   "nullable": true
  },
  {
   "name": "supersedes_observation_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_date_basis",
   "type": "string",
   "nullable": true
  },
  {
   "name": "membership_source_event_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "firm",
   "type": "string",
   "nullable": true
  },
  {
   "name": "value_basis",
   "type": "string",
   "nullable": true
  }
 ],
 "enums": {
  "identity_status": [
   "EXACT_MATCH"
  ],
  "business_status": [
   "TRADED_CLAIM"
  ],
  "value_status": [
   "COMPLETE"
  ],
  "value_basis": [
   "CUSTODIAN_MEASURED"
  ],
  "membership_date_status": [
   "OBSERVED_TRADED"
  ],
  "technical_enrollment": [
   "UNAVAILABLE"
  ],
  "membership_date_basis": [
   "FIRST_OBSERVED_UTC"
  ],
  "reason_codes": [],
  "basis": [
   "blackdiamond/cottonwood fact_holdings SUM(Market Value)"
  ],
  "claim": "measured on the newest partition"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "bucket opal-data-cottonwood + key segment mdpf/cottonwood/ + column firm",
   "values": [
    "cottonwood"
   ]
  },
  "account": {
   "column": "account_key",
   "shape": "10 digits (custodian account number)",
   "last4_derivation": "last 4 characters of account_key",
   "last4_collisions_within_firm": 0,
   "distinct_accounts": 2,
   "claim": "measured on the newest partition"
  },
  "platform": {
   "column": null,
   "values": [],
   "note": "no platform column; the custodian is named in basis / canonical_source_ref (Schwab fact_rps_s2 or Black Diamond fact_holdings) -- serve it as platform_label with platform_label_source='basis' (v3.1 Ruling 4)"
  }
 },
 "nl_tags": [
  "tax sma accounts",
  "tax-managed sma assets",
  "tax sma aum by account",
  "tax sma membership",
  "which accounts are in the tax sma"
 ],
 "common_queries": [
  "Which accounts are enrolled in the Tax SMA for this firm and what is each one's value?",
  "When did account ****1234 join the Tax SMA?",
  "How much Tax SMA AUM did the firm hold on a given date?",
  "Which Tax SMA accounts have no custodian match?"
 ],
 "never_sum_rules": [
  "one firm per call: the two firms live in two buckets and are never summed in one answer",
  "value_basis WORKBOOK_STATED rows are the workbook's AUM fallback, not custodian-measured: report the basis per row and never present a mixed total as measured",
  "never sum partitions: each date partition is that date's full account set"
 ],
 "existing_gateway_tool": {
  "name": "none reads this table; G2d contracts the Tax SMA WORKBOOK (opal-data-assets gateway/ prefix) as the membership source",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "client_get_taxsma_accounts",
   "inputs": {
    "firm": "49financial|cottonwood (one)",
    "account_last4": "optional; resolves through client_resolve_account",
    "as_of": "date partition, default newest"
   },
   "returns": "account (masked), membership_effective_date, value_usd, value_basis, basis (as platform_label), identity_status, reason_codes, valuation_date, knowledge_date",
   "answers": [
    "Which accounts are enrolled in the Tax SMA for this firm and what is each one's value?",
    "When did account ****1234 join the Tax SMA?",
    "Which Tax SMA accounts have no custodian match?"
   ],
   "admission": "DATA_GRANT class (v3.1 Ruling 2): the firm's data grant"
  }
 ],
 "catalog_entry": {
  "data_catalog_key": null,
  "present": false
 },
 "prior_art": "org/standards/MDPF_TAXSMA_DATA_CONTRACT.json v0.6.0 (cited by the producer's docstring); org/missions/D8/MDPF/MDPF_TAXSMA/",
 "open_items": [
  "the schedule of mdpf-gold-lambda for this table was not read",
  "the sibling state object mdpf/cottonwood/state/taxsma_membership/dispositions.json (a list, one entry per account) is the membership store the table reads; it is state, not served"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 s3://opal-data-cottonwood/ (full bucket) and prefix mdpf/cottonwood/gold/taxsma_assets/: 14 keys",
   "at": "2026-10-14T14:28Z"
  },
  {
   "read": "pyarrow read of all 14 parts (schema + num_rows); full read of the newest part for enums and last-4 (values not printed)",
   "at": "2026-10-14T14:30Z"
  }
 ]
}
```

## (e) What could not be read

- The schedule of `mdpf-gold-lambda` for this table (producer claim: inferred).
- Cottonwood's per-date row counts other than the newest: those parts were read for schema and num_rows, but the counts were not printed.

-- 4.0.0_SA_CRO~Z
