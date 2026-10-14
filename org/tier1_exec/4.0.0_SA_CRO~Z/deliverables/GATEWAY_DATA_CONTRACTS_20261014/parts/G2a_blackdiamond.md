# G2a -- Black Diamond silver census, s3://opal-data-assets/blackdiamond/ (every firm)

Part G2a of `GATEWAY_DATA_CONTRACTS_20261014` for 4.0.0_SA_CRO~Z, under directive
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md`.
All reads were made 2026-10-14 between 12:50Z and 13:10Z and were read-only. T-1 frontier: 2026-10-13
(`lib/trading_calendar.py`, hardcoded NYSE fallback). Every lag below is in trading days behind T-1.

## (a) Method

| # | read | instrument | denominator |
|---|---|---|---|
| 1 | Prefix census of `blackdiamond/` | boto3 `list_objects_v2` paginator | 32 pages, 31,303 of 31,303 keys, 17,989,245,212 bytes |
| 2 | Parquet schema, rows per part | footer-only range GET of every `.parquet` part under every silver, silver_legacy and gold table | 9,732 parts across 32 tables (every part, not a sample) |
| 3 | Fork keys (account, last-4, custodian) | projected-column read of the NEWEST non-empty part of each client table | 24 tables, 1 part each (named per contract in `fork_keys.account.measured_on`) |
| 4 | Same-firm test (49f vs 49financial vs cottonwood) | set intersection of account and relationship ids across 11 columns of 6 newest parts | 11 sets, 55 pairwise intersections |
| 5 | Grain and duplicates | projected reads (keys, trade dates) of the newest 1-2 parts of 9 tables | named in each contract |
| 6 | Producers | `lambda get-function-configuration` (9 functions), `events list-rule-names-by-target` + `describe-rule`, `scheduler list-schedules` + `get-schedule` | 9 functions, 9 rules, 33 of 33 schedules scanned |
| 7 | Producer health | CloudWatch Logs newest stream of 2 converters | 1 stream each |
| 8 | Live 49F silver outside this bucket | `list_objects_v2` of `s3://opal-data-bd/silver/` + footer of the newest part of 6 tables | 9 pages, 8,119 of 8,119 keys |
| 9 | Glue catalog | `glue search_tables SearchText=blackdiamond` | 0 tables (scope: this account's default-region catalog) |
| 10 | Repo producers and prior art | native Grep over `*.py,*.tf,*.json,*.yaml,*.yml,*.ps1,*.sh` | 593 files matched the table and prefix names; producers read in `infra/aws/terraform/opal-assets/` and `infra/aws/lambda/opal-assets/` |

Scratch scripts and raw outputs: `C:\Users\OPALBL~1\AppData\Local\Temp\claude\census_G2a\` (not committed).

## (b) Prefix census

Firm x layer (objects, bytes, newest LastModified UTC):

| firm segment | layer | objects | bytes | newest LastModified |
|---|---|---|---|---|
| 49f | _ops | 6 | 80,986 | 2026-08-27T22:48:18Z |
| 49f | bronze | 5,714 | 3,866,560,755 | 2026-10-14T06:32:04Z |
| 49f | gold | 1 | 31,900 | 2026-07-18T01:50:28Z |
| 49f | meta | 56 | 119,776 | 2026-09-29T07:06:53Z |
| 49f | silver | 108 | 31,037,674 | 2026-09-29T07:06:53Z |
| 49financial | bronze | 7,703 | 1,961,294,442 | 2026-10-14T04:35:20Z |
| 49financial | bronze_legacy | 931 | 7,712,606,358 | 2026-08-25T22:53:47Z |
| 49financial | silver | 186 | 2,153,638 | 2026-10-14T04:35:22Z |
| 49financial | silver_legacy | 7,921 | 2,788,870,598 | 2026-08-25T23:09:05Z |
| cottonwood | bronze | 6,094 | 1,163,397,096 | 2026-10-14T11:45:57Z |
| cottonwood | gold | 66 | 569,970 | 2026-10-13T13:30:40Z |
| cottonwood | meta | 963 | 2,872,014 | 2026-10-14T12:45:54Z |
| cottonwood | silver | 1,554 | 459,650,005 | 2026-10-14T11:46:20Z |
| **total** | | **31,303** | **17,989,245,212** | |

Firm segments found: 3 of 3 (`49f`, `49financial`, `cottonwood`); no other `blackdiamond/<firm>/` exists.

Silver tables (contracted below; 30 contracts, all 32 parquet tables less the 2 gold):

| table | parts | rows newest part | schema variants | newest partition | lag (td) |
|---|---|---|---|---|---|
| 49f/silver/dim_account_xref | 53 | 6,202 | 1 | 2026-09-28 | 11 |
| 49f/silver/dim_advisor_fee_role | 53 | 282,857 | 1 | 2026-09-28 | 11 |
| 49f/silver/fact_bd_allocation | 1 | 30,577 | 1 | 2026-08-18 | 39 |
| 49f/silver/fact_taxsma_report | 1 | 3,361 | 1 | 2026-07-17 | 61 |
| 49financial/silver/fact_insurance_insurancerelationshiplist_export | 46 | 77 | 1 | 2026-10-14 | 0 |
| 49financial/silver/fact_insurance_relationshipaccountdetailsearch | 46 | 77 | 1 | 2026-10-14 | 0 |
| 49financial/silver/fact_insurance_relationshipdetail | 1 | 1 | 1 | 2026-08-27 | 32 |
| 49financial/silver_legacy/fees | 1,957 | 1,066 | 25 | 2026-08-24 | 35 (FROZEN) |
| 49financial/silver_legacy/transactions | 1,878 | 0 (4,990 on 08-23) | 13 | 2026-08-25 | 34 (FROZEN) |
| 49financial/silver_legacy/transactions_enriched | 518 | 45 | 16 | 2026-04-20 | 122 (FROZEN) |
| 49financial/silver_legacy/allocations | 128 | 7,070 | 5 | 2026-08-21 | 36 (FROZEN) |
| 49financial/silver_legacy/assets | 1,890 | 25,332 | 11 | 2026-06-18 | 80 (FROZEN) |
| 49financial/silver_legacy/realized | 1,310 | 31,009 | 4 | 2026-08-25 | 34 (FROZEN) |
| 49financial/silver_legacy/unrealized | 70 | 110,376 | 4 | 2026-08-21 | 36 (FROZEN) |
| 49financial/silver_legacy/prices | 139 | 10,831 | 1 | 2026-08-23 | 36 (FROZEN) |
| 49financial/silver_legacy/_single_file | 20 files | n/a | 20 | 2026-01-28 | n/a (FROZEN) |
| cottonwood/silver/fact_allocations (+_s2) | 144 | 1,524 | 1 | 2026-10-13 | 0 |
| cottonwood/silver/fact_holdings (+_s2) | 93 | 21,412 | 2 | 2026-10-13 | 0 |
| cottonwood/silver/fact_unrealized (+_s2) | 144 | 60,905 | 1 | 2026-10-13 | 0 |
| cottonwood/silver/fact_realized (+_s2) | 122 | 1,501 | 1 | 2026-10-14 | 0 |
| cottonwood/silver/fact_transactions (+_s2) | 124 | 12,984 | 1 | 2026-10-14 | 0 |
| cottonwood/silver/fact_model_assignment | 75 | 995 | 1 | 2026-10-14 | 0 |
| cottonwood/silver/fact_model_definition | 75 | 1,690 | 1 | 2026-10-14 | 0 |
| cottonwood/silver/fact_model_blend | 75 | 129 | 1 | 2026-10-14 | 0 |
| cottonwood/silver/fact_model_roster | 75 | 72 | 1 | 2026-10-14 | 0 |

Bronze and gold (noted, not contracted): 49f bronze `allocation_390224`, `fees_435407`, `template_roster` (128 objects each, newest
2026-10-14 06:3xZ), `reporting_{allocation,costbasis,performance}` (newest 2026-09-01); 49financial bronze `insurance_*`
(daily, newest 2026-10-14 04:35Z), `reporting_performance` (7,551, newest 2026-10-08), `bronze_legacy/` (frozen 2026-08-25);
cottonwood bronze `{account_attributes,allocations,holdings,realized,transactions,unrealized}` xlsx + `rebalancer_*` JSON
(newest 2026-10-14 11:45Z), plus 31 date-named 239-277 byte stubs (`bronze/2026-06-13..2026-07-14`). Gold:
`49f/gold/dim_taxsma_report` (1 part, 45 rows, 2026-07-17), `cottonwood/gold/dim_model_portfolio` (66 parts, 18 rows newest, 2026-10-13).

Live 49F silver OUTSIDE this bucket (`s3://opal-data-bd/silver/`, read for the verdicts; not contracted here): `fees` (2,006 dated
parts, newest 2026-10-12, 710 rows), `transactions` (newest 2026-10-14, 2,921 rows), `allocations` (newest 2026-10-09, 7,345
rows), `realized` (newest 2026-10-14, 45,208 rows), `unrealized` (weekly, newest 2026-10-09, 108,439 rows, 7,395 accounts),
`prices` (newest 2026-10-14). Every account id read there starts `z08`, and every column of each newest part exists in the
`silver_legacy` union of the same table. So `49financial/silver_legacy/` is a frozen 2026-08-25 copy of a store that is still live.

## (c) Analysis

### Is 49f the same firm as 49financial? Yes: one firm, two key segments.

- **Registry.** `infra/logic/registry/scopes.json` row `49financial` (class FIRM, display "49 Financial") declares
  `monolith_scopes.blackdiamond = ["49f", "49financial"]`, and `49f` is one of its aliases. Cottonwood is a separate row
  (`cottonwood`, short `cot`, BD prefix `z09`).
- **Account ids (measured).** Every BD account and relationship id read under both segments starts `z08` (49f xref 6,202 of
  6,202; 49financial legacy allocations 7,070 of 7,070; insurance relationships 77 of 77). Every cottonwood id starts `z09`.
- **Overlap (measured).** 5,824 of the 6,202 `49f` xref `bd_account_id`s are in the `49financial/silver_legacy/allocations`
  2026-08-21 part. 76 of the 77 `49financial` insurance relationship ids are in `49f/silver/fact_bd_allocation`.
  Across the firm boundary there is one shared value, and it is the placeholder relationship id `"0"`. No account id is shared.
- **Why there are two segments.** `49f/` is the D1 REST-template pipeline (`opal-assets-bd49f-*`, scope added 2026-07-14).
  `49financial/` is the PRD s.11 Ruling 1 canonical segment ("blackdiamond/49financial/ ... NOT the legacy 49f/ alias",
  `infra/aws/terraform/opal-assets/bd49f_reporting_pull.tf:87`). It holds the insurance leg and the frozen legacy copy.
- **Rule for tools.** A tool takes `firm=49financial` and reads both segments under that one firm key. It never takes `49f` as a
  firm value.

### Last-4 is NOT unique within a firm (measured). Every tool must resolve, never assume.

| firm | population (newest part) | distinct accounts | distinct last-4 | accounts sharing a last-4 |
|---|---|---|---|---|
| 49financial | `49f/silver/dim_account_xref.bd_account_number` | 6,186 | 4,683 | 2,741 (44.3%) |
| 49financial | same table, `schwab_account_id` | 5,376 | 4,180 | 2,207 |
| 49financial | `silver_legacy/unrealized.account_number` (largest 49F book) | 7,734 | 5,420 | 4,156 |
| cottonwood | `silver/fact_holdings."Account Number"` | 998 | 932 | 84 (8.4%) |
| cottonwood | `silver/fact_allocations."Account Number"` | 863 | 808 | 63 |

- **The collisions are what chance predicts.** 49F's ~6-7k eight-digit Schwab numbers spread over 10,000 possible last-4
  values, and the collision count is close to the random expectation. A larger book will collide more.
- **Derive last-4 from the custodian number.** That is `account_number`, `bd_account_number` or `"Account Number"`, taking the
  last 4 alphanumerics, since some Cottonwood numbers carry letters.
- **Never use the BD internal id for last-4.** `z08...` and `z09...` give only 1,000 distinct last-4 over about 6,000 accounts.
- **What the tool must do.** `account_last4` returns a candidate list: masked number, BD id, account type and custodian. A
  second input (`account_last6`, or the BD id the list returns) is needed to pin one account. Per the brief, the counts above are
  counts only.

### Platform / custodian column

| firm | column | values |
|---|---|---|
| cottonwood | `Custodian` (transactions, allocations) | 25-26 values; Fidelity IWS has 1,308 of 1,524 allocation rows |
| cottonwood | `Data Provider` | 8 values |
| 49financial | `billing_custodian` (dim_advisor_fee_role) | Schwab, non-null on 9,169 of 282,857 rows |
| 49financial | `billing_account_custodian` (fees) | Schwab / ByAll Accounts / Fidelity IWS |

- **No custodian column:** 49F allocation, holdings (unrealized) and transactions.
- **Rebalancer `custodian_id`:** 0 on 995 of 995 rows, so it is not populated.

### What the tables are

- **Cottonwood (live, 0 lag).**
  - *Five daily BD export facts:* allocations (account profile and market value), holdings (positions), unrealized (tax lots),
    realized (closed lots) and transactions. Each has a `_s2` twin: the 5-row xlsx header (Created, Template, Start/End Date,
    Date Range).
  - *Four rebalancer facts:* model assignment per account, model definition (security target weights), blend (model-to-child
    edges) and roster.
  - *Snapshot vs window.* Holdings, unrealized and allocations are FULL SNAPSHOTS per report date. Realized and transactions
    are ROLLING WINDOWS: 12,755 of the newest 12,905 TransactionIDs repeat in the prior partition. A tool reads ONE partition
    and never sums across partitions.
- **49financial in this bucket.**
  - *Current:* the insurance relationship list and account detail (daily, 0 lag).
  - *Stale:* the 49f REST dims (xref, advisor/fee roles), stalled since 2026-09-29. Producer `opal-assets-bd49f-dim-convert`
    ends `Runtime.OutOfMemory` at 1,024 MB on today's run. `dim_advisor_fee_role` rewrites its whole SCD history into every
    daily partition: 282,857 rows, +5,338 a day. That growth is the likely cause (inferred).
  - *One-off parts:* `fact_bd_allocation` (2026-08-18) and `fact_taxsma_report` (one account, Q2).
  - *Frozen copy:* `silver_legacy/`, the 2026-08-25 copy of `opal-data-bd/silver/`. The live 49F fees, transactions,
    allocations, realized, unrealized and prices are still written to `s3://opal-data-bd/silver/`, not here (F11 move pending).

### Common questions (the gateway has only fees today; catalog gap E-8)

"What does account ...1234 hold?", "what is it worth and where is it custodied?", "what trades, dividends, contributions and
withdrawals hit it this month?", "what fees were charged?", "what is the unrealized / realized gain?", "which model is it on and
what are the model's target weights?", "who are the advisors on it and what is the fee rate?", "what insurance does household X hold?".

### Proposed tools (firm + account_last4 + as_of; one firm per call, firm from the principal)

| tool | cottonwood source | 49financial source | answers |
|---|---|---|---|
| `blackdiamond_resolve_account` | fact_allocations / fact_holdings | 49f dim_account_xref (stale 11 td), else opal-data-bd allocations | last-4 -> candidate list (mandatory first hop) |
| `blackdiamond_get_account_profile` | fact_allocations (contact columns projected out) | opal-data-bd silver/allocations (live); 49f fact_bd_allocation fallback | value, custodian, type, household, fee schedule |
| `blackdiamond_get_holdings` | fact_holdings (daily snapshot) | opal-data-bd silver/unrealized (WEEKLY; the envelope says so) | positions, cash, totals of one partition |
| `blackdiamond_get_unrealized_lots` | fact_unrealized | opal-data-bd silver/unrealized | lots, cost basis, ST/LT gain |
| `blackdiamond_list_realized` | fact_realized (2-week window) | opal-data-bd silver/realized | realized gains in the window |
| `blackdiamond_list_transactions` | fact_transactions (window, dedupe TransactionID) | opal-data-bd silver/transactions | trades, income, flows, fees |
| `blackdiamond_get_model_assignment` + `blackdiamond_get_model_targets` | fact_model_* (+ gold dim_model_portfolio) | none (49F has no rebalancer silver) | model on account, target weights |
| `blackdiamond_get_account_fee_roles` | none | 49f dim_advisor_fee_role is_current (stale until OOM fixed) | advisors, splits, bps |
| `blackdiamond_list_insurance` | none | 49financial fact_insurance_* | insurance by household |
| `blackdiamond_list_fees` (existing) | extend: Management Fee rows of fact_transactions | keep: opal-data-bd silver/fees | fees |

- **Existing tool.** `blackdiamond_list_fees` (catalog `tool_index` and `silver_datasets.blackdiamond_fees`) is **keep** for
  49financial. It reads the live `opal-data-bd silver/fees` (newest 2026-10-12, 1 td), not `silver_legacy/fees`.
  - Extend it to Cottonwood only as a separate firm branch with its own read fence: prefix `blackdiamond/cottonwood/` and
    account prefix `z09`.
  - Its `z08` assertion is the model for every tool above. Each tool fences ONE firm segment and refuses a foreign BD prefix.
- **Repoint after F11.** When F11 moves the 49F writer into `opal-data-assets/blackdiamond/49financial/silver/`, the 49F
  sources in the table repoint there. Until then, they need the read role widened to the named `opal-data-bd silver/<table>/`
  prefixes. That widening needs a never-widen sign-off, and this census does not pre-decide it.
- **Catalog.** No `silver_datasets` row exists for any table in this part (0 of 30). Each proposed tool brings its row.

## (d) Contracts -- one JSON block per bucket -> table (30)

### blackdiamond/49f/silver/dim_account_xref/

```json
{
 "contract_id": "opal-data-assets/silver/49f/dim_account_xref",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49f/silver/dim_account_xref/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_account_xref",
 "grain": "one row per Black Diamond account (bd_account_id) per as-of date: the BD -> Schwab account bridge",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-bd49f-dim-convert (Lambda; source data/assets/scripts/silver/bd49f_dim_conversion.py)",
  "schedule": "EventBridge Scheduler opal-assets-bd49f-dim-convert-daily cron(5 7 * * ? *) UTC, ENABLED",
  "upstream": "opal-assets-bd49f-daily-pull rules cron(30 6 * * ? *) and cron(30 8 * * ? *) ENABLED -> blackdiamond/49f/bronze/{allocation_390224,fees_435407,template_roster}/",
  "status": "FAILING: the 2026-10-14 07:05Z invocations ended Runtime.OutOfMemory at 1024 MB (Max Memory Used 1023-1024 MB); last silver write 2026-09-29T07:06:53Z",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-28",
  "trading_days_behind_t1": 11,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-09-29T07:06:53Z",
  "claim": "measured"
 },
 "size": {
  "objects": 53,
  "bytes": 12089220,
  "parquet_parts": 53,
  "schema_variants": 1,
  "rows_all_parts": 328649,
  "rows_newest_part": 6202,
  "newest_part": "date=2026-09-28/data.parquet",
  "rows_sampled": 6202,
  "row_count_rule": "full snapshot per date partition (6,202 rows newest); never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "bd_account_id",
   "type": "string",
   "nullable": true,
   "description": "Black Diamond internal account id (z08 + digits); unique key",
   "example": "z08********"
  },
  {
   "name": "bd_account_number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number as BD holds it (some vendor-masked with leading *)",
   "example": "****1234"
  },
  {
   "name": "bd_original_account_number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "schwab_account_id",
   "type": "string",
   "nullable": true,
   "description": "10-digit Schwab account id (null when unresolved)",
   "example": "****1234"
  },
  {
   "name": "match_method",
   "type": "string",
   "nullable": true,
   "description": "seed-xref or unresolved",
   "example": ""
  },
  {
   "name": "match_as_of",
   "type": "string",
   "nullable": true,
   "description": "date the bridge was resolved",
   "example": ""
  },
  {
   "name": "in_0833_universe",
   "type": "bool",
   "nullable": true,
   "description": "account is in the Schwab 0833 master universe",
   "example": ""
  },
  {
   "name": "account_is_open",
   "type": "string",
   "nullable": true,
   "description": "BD open flag (string)",
   "example": ""
  },
  {
   "name": "feed_seen_date",
   "type": "string",
   "nullable": true,
   "description": "last feed date the account appeared",
   "example": ""
  },
  {
   "name": "schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (53 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "match_method": {
   "n_distinct": 2,
   "values_top": [
    "seed-xref",
    "unresolved"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  },
  "account_is_open": {
   "n_distinct": 2,
   "values_top": [
    "True",
    "False"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  },
  "in_0833_universe": {
   "n_distinct": 2,
   "values_top": [
    "True",
    "False"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49f/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "bd_account_number",
   "last4_derivation": "last 4 alphanumerics of bd_account_number (custodian number); bd_account_id last-4 is NOT usable (6,202 ids -> 1,000 last-4)",
   "last4_collisions_within_firm": 2741,
   "measured_on": "bd_account_number, newest partition date=2026-09-28/data.parquet: 6186 distinct accounts -> 4683 distinct last-4; 1238 last-4 values shared by 2+ accounts, covering 2741 accounts",
   "claim": "measured",
   "note": "schwab_account_id gives 5,376 accounts -> 4,180 last-4, 2,207 in collision"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "account crosswalk",
  "black diamond to schwab account",
  "account id mapping",
  "49 financial accounts"
 ],
 "common_queries": [
  "Which Schwab account is Black Diamond account ...1234?",
  "Is account ...1234 open in Black Diamond?",
  "How many 49F BD accounts are unresolved to Schwab?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_resolve_account",
   "inputs": {
    "firm": "49financial|cottonwood",
    "account_last4": "1234",
    "platform": "optional custodian filter",
    "as_of": "YYYY-MM-DD (default newest)"
   },
   "returns": "candidate accounts (masked number, bd_account_id, account_type, open flag, custodian) -- a list, because last-4 is not unique within a firm",
   "answers": [
    "Which Schwab account is Black Diamond account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/bd49f_dim_conversion.py@HEAD",
 "open_items": [
  "producer OOM since 2026-09-29: 11 trading days behind T-1 (surprise row owed on NFRA_OPLGTW channel; not written by this subagent per brief)"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49f/silver/dim_account_xref/date=2026-09-28/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + scheduler get-schedule opal-assets-bd49f-dim-convert",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "CloudWatch Logs newest stream /aws/lambda/opal-assets-bd49f-dim-convert (REPORT Status: error Runtime.OutOfMemory)",
   "at": "2026-10-14T13:07Z"
  }
 ]
}
```

### blackdiamond/49f/silver/dim_advisor_fee_role/

```json
{
 "contract_id": "opal-data-assets/silver/49f/dim_advisor_fee_role",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49f/silver/dim_advisor_fee_role/",
 "layer": "silver",
 "format": "parquet",
 "table": "dim_advisor_fee_role",
 "grain": "one row per account per effective period (SCD-2: effective_from/effective_to, is_current); each date partition re-writes the WHOLE history",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-bd49f-dim-convert (Lambda; source data/assets/scripts/silver/bd49f_dim_conversion.py)",
  "schedule": "EventBridge Scheduler opal-assets-bd49f-dim-convert-daily cron(5 7 * * ? *) UTC, ENABLED",
  "upstream": "opal-assets-bd49f-daily-pull rules cron(30 6 * * ? *) and cron(30 8 * * ? *) ENABLED -> blackdiamond/49f/bronze/{allocation_390224,fees_435407,template_roster}/",
  "status": "FAILING: the 2026-10-14 07:05Z invocations ended Runtime.OutOfMemory at 1024 MB (Max Memory Used 1023-1024 MB); last silver write 2026-09-29T07:06:53Z",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-09-28",
  "trading_days_behind_t1": 11,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-09-29T07:06:53Z",
  "claim": "measured"
 },
 "size": {
  "objects": 53,
  "bytes": 14917026,
  "parquet_parts": 53,
  "schema_variants": 1,
  "rows_all_parts": 7636531,
  "rows_newest_part": 282857,
  "newest_part": "date=2026-09-28/data.parquet",
  "rows_sampled": 282857,
  "row_count_rule": "each partition is a full SCD history (282,857 rows newest, 5,338 is_current=true, 0 duplicate current accounts); rows grow ~5,338 per day, never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "account_id",
   "type": "string",
   "nullable": true,
   "description": "10-digit Schwab account id",
   "example": "z08********"
  },
  {
   "name": "bd_account_id",
   "type": "string",
   "nullable": true,
   "description": "BD internal id (z08...)",
   "example": "z08********"
  },
  {
   "name": "bd_account_number",
   "type": "string",
   "nullable": true,
   "description": "custodian number (8 digit)",
   "example": "****1234"
  },
  {
   "name": "architect",
   "type": "string",
   "nullable": true,
   "description": "advisor role: architect",
   "example": ""
  },
  {
   "name": "manager",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "implementor",
   "type": "string",
   "nullable": true,
   "description": "advisor role",
   "example": ""
  },
  {
   "name": "consultant",
   "type": "string",
   "nullable": true,
   "description": "advisor role",
   "example": ""
  },
  {
   "name": "local_ops",
   "type": "string",
   "nullable": true,
   "description": "advisor role",
   "example": ""
  },
  {
   "name": "additional_advisor",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "architect_split_pct",
   "type": "double",
   "nullable": true,
   "description": "revenue split percent",
   "example": ""
  },
  {
   "name": "implementor_split_pct",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "consultant_split_pct",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "local_ops_split_pct",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "additional_advisor_split_pct",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "house_split_pct",
   "type": "double",
   "nullable": true,
   "description": "49F house split percent",
   "example": ""
  },
  {
   "name": "architect_split_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "implementor_split_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "consultant_split_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "local_ops_split_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "additional_advisor_split_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "annual_fee_bps",
   "type": "double",
   "nullable": true,
   "description": "annual fee in basis points",
   "example": ""
  },
  {
   "name": "annual_fee_pct",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "flat_fee",
   "type": "double",
   "nullable": true,
   "description": "flat fee amount",
   "example": ""
  },
  {
   "name": "fee_schedule",
   "type": "string",
   "nullable": true,
   "description": "fee schedule name",
   "example": ""
  },
  {
   "name": "fee_rate_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_basis",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_level",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "billable",
   "type": "string",
   "nullable": true,
   "description": "Billable / Non-Billable",
   "example": ""
  },
  {
   "name": "billing_custodian",
   "type": "string",
   "nullable": true,
   "description": "billing custodian (Schwab when set)",
   "example": ""
  },
  {
   "name": "fee_schedule_conflict",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_alternates",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "architect_matches_xref",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "effective_from",
   "type": "string",
   "nullable": true,
   "description": "SCD period start",
   "example": ""
  },
  {
   "name": "effective_to",
   "type": "string",
   "nullable": true,
   "description": "SCD period end",
   "example": ""
  },
  {
   "name": "is_current",
   "type": "bool",
   "nullable": true,
   "description": "true on the current period row",
   "example": ""
  },
  {
   "name": "absent_from_feed_since",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "period_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "roles_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "roles_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "bridge_method",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "bridge_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (53 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "billing_custodian": {
   "n_distinct": 1,
   "values_top": [
    "Schwab"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  },
  "is_current": {
   "n_distinct": 2,
   "values_top": [
    "False",
    "True"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  },
  "fee_rate_type": {
   "n_distinct": 2,
   "values_top": [
    "Flat Rate",
    "No Rate Type"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  },
  "billable": {
   "n_distinct": 2,
   "values_top": [
    "Billable",
    "Non-Billable"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-09-28/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49f/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "bd_account_number",
   "last4_derivation": "last 4 digits of bd_account_number (equivalently of account_id, the Schwab id)",
   "last4_collisions_within_firm": 2182,
   "measured_on": "bd_account_number, newest partition date=2026-09-28/data.parquet: 5338 distinct accounts -> 4157 distinct last-4; 1001 last-4 values shared by 2+ accounts, covering 2182 accounts",
   "claim": "measured",
   "note": "billing_custodian is non-null on 9,169 of 282,857 rows of the newest partition"
  },
  "platform": {
   "column": "billing_custodian",
   "values": [
    "Schwab"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "advisor splits",
  "fee schedule by account",
  "who is the advisor on account",
  "billing rate",
  "revenue split"
 ],
 "common_queries": [
  "Who are the architect and implementor on account ...1234 and what are their splits?",
  "What is the annual fee rate (bps) on account ...1234?",
  "Which accounts are non-billable?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_get_account_fee_roles",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "",
    "as_of": "YYYY-MM-DD (reads is_current rows of that partition)"
   },
   "returns": "current advisor roles, split percents, fee schedule, bps / flat fee, billable flag for the matched account(s)",
   "answers": [
    "Who are the architect and implementor on account ...1234 and what are their splits?",
    "What is the annual fee rate (bps) on account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/bd49f_dim_conversion.py@HEAD; ADVI_BILLING contracts in org/standards/ not found by name (see section e)",
 "open_items": [
  "the full-history-per-partition design grows the partition daily and is the likely cause of the converter OOM (inferred)",
  "producer OOM since 2026-09-29: 11 trading days behind"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49f/silver/dim_advisor_fee_role/date=2026-09-28/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "projected read of is_current/effective_from (0 duplicate current accounts)",
   "at": "2026-10-14T13:08Z"
  },
  {
   "read": "CloudWatch Logs /aws/lambda/opal-assets-bd49f-dim-convert",
   "at": "2026-10-14T13:07Z"
  }
 ]
}
```

### blackdiamond/49f/silver/fact_bd_allocation/

```json
{
 "contract_id": "opal-data-assets/silver/49f/fact_bd_allocation",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49f/silver/fact_bd_allocation/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_bd_allocation",
 "grain": "one row per account x portfolio x fee-schedule tier line of the BD allocation report (30,577 rows, 6,155 accounts, 24,422 repeat accountid rows)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/bd49f_fact_allocation.py (manual run; no Lambda or schedule found)",
  "schedule": "none: one partition only",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-08-18",
  "trading_days_behind_t1": 39,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-19T22:46:03Z",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 3726932,
  "parquet_parts": 1,
  "schema_variants": 1,
  "rows_all_parts": 30577,
  "rows_newest_part": 30577,
  "newest_part": "date=2026-08-18/data.parquet",
  "rows_sampled": 30577,
  "row_count_rule": "one partition, one part: row count is that part's (30,577)",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "portfolio_group",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "original_account_number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "relationship_id",
   "type": "string",
   "nullable": true,
   "description": "BD relationship (household) id",
   "example": "z08********"
  },
  {
   "name": "relationship_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_display_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_sec_client_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_inception_date",
   "type": "date32[day]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_termination_date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolioid",
   "type": "string",
   "nullable": true,
   "description": "BD portfolio id",
   "example": ""
  },
  {
   "name": "portfolio_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "show_client",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "basis_points",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "fee bps",
   "example": ""
  },
  {
   "name": "portfolio_benchmark",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_level",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "flat_fee",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "history_start_date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "address_source_client_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "address_source_city",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "address_source_state",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "address_source_zip_code",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number",
   "example": "****1234"
  },
  {
   "name": "accountid",
   "type": "string",
   "nullable": true,
   "description": "BD internal id (z08...)",
   "example": "z08********"
  },
  {
   "name": "account_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "flat_fee_1",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "basis_points_1",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_billing_notes",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "start_date",
   "type": "date32[day]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "performance_start_date",
   "type": "date32[day]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "as_of_date",
   "type": "date32[day]",
   "nullable": true,
   "description": "row as-of (mostly 2026-08-17)",
   "example": ""
  },
  {
   "name": "account_is_open",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "closed_date",
   "type": "date32[day]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "history_start_date_1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "client_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_city",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_state",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_zip_code",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "49_house_split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "additional_advisor",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "additional_advisor_split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "architect_split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "architect",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "consultant_split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "consultant",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "implementor",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "local_ops",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "implementor_split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "local_ops_split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "investment_strategy_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "manager_strategy",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_create_date",
   "type": "date32[day]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_type",
   "type": "string",
   "nullable": true,
   "description": "IRA, Brokerage, RothIRA, ...",
   "example": ""
  },
  {
   "name": "account_registration_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "managed_account_manager_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_level_1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "lower_range",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "fee tier lower bound",
   "example": ""
  },
  {
   "name": "upper_range",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "fee tier upper bound",
   "example": ""
  },
  {
   "name": "fee_schedule_rate_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_description",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_discretionary",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_fee_schedule",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_billable",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_supervised",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_benchmark",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "reporting_target_description",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "tax_lot_methodology",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "tax_status",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_subcategory",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_category",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "goal",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_owner_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_owner",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "manager",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "style",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "rep_code",
   "type": "string",
   "nullable": true,
   "description": "rep code",
   "example": ""
  },
  {
   "name": "account_display_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "original_account_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_display_number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "fee_schedule_rate_type_1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_type_1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "upper_range_1",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "lower_range_1",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_description_1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_fee_schedule",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "reporting_target_description_1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_reporting_target",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_logo",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_allocation",
   "type": "decimal128(30, 24)",
   "nullable": true,
   "description": "account weight in portfolio group",
   "example": ""
  },
  {
   "name": "account_market_value",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "account market value",
   "example": ""
  },
  {
   "name": "portfolio_group_market_value",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "cash_market_value",
   "type": "decimal128(28, 6)",
   "nullable": true,
   "description": "cash market value",
   "example": ""
  },
  {
   "name": "cash_allocation",
   "type": "decimal128(30, 24)",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_key",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_row_sha256",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "account_type": {
   "n_distinct": 30,
   "values_top": [
    "IRA",
    "Brokerage",
    "RothIRA",
    "Joint",
    "Trust",
    "InheritedIRA",
    "SEP",
    "SIMPLE",
    "Insurance",
    "401K"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-08-18/data.parquet"
  },
  "account_is_open": {
   "n_distinct": 2,
   "values_top": [
    "true",
    "false"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-08-18/data.parquet"
  },
  "as_of_date": {
   "n_distinct": 102,
   "values_top": [
    "2026-08-17",
    "2026-06-23",
    "2026-04-16",
    "2026-06-24",
    "2026-06-25",
    "2026-06-22",
    "2026-07-14",
    "2026-04-10",
    "2026-04-06",
    "2026-03-18"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-08-18/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49f/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 2716,
   "measured_on": "account_number, newest partition date=2026-08-18/data.parquet: 6138 distinct accounts -> 4651 distinct last-4; 1229 last-4 values shared by 2+ accounts, covering 2716 accounts",
   "claim": "measured",
   "note": "no custodian column; account_type is the nearest platform-like field"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "account profile",
  "account market value",
  "fee schedule",
  "relationship",
  "allocation report"
 ],
 "common_queries": [
  "What was the market value of account ...1234 on the report date?",
  "Which relationship does account ...1234 belong to?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_get_account_profile",
   "inputs": {
    "firm": "49financial",
    "account_last4": "1234",
    "platform": "",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "account type, registration, relationship, portfolio, market value, cash, fee schedule tiers; for 49F read the LIVE opal-data-bd silver/allocations (newest 2026-10-09), this one-off partition only as a fallback",
   "answers": [
    "What was the market value of account ...1234 on the report date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "data/assets/scripts/silver/bd49f_fact_allocation.py@HEAD",
 "open_items": [
  "a single 2026-08-18 partition, 39 trading days behind; the live 49F allocation silver is opal-data-bd silver/allocations/ (out of this bucket)"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49f/silver/fact_bd_allocation/date=2026-08-18/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "projected read accountid/portfolioid duplicates",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/49f/silver/fact_taxsma_report/

```json
{
 "contract_id": "opal-data-assets/silver/49f/fact_taxsma_report",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49f/silver/fact_taxsma_report/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_taxsma_report",
 "grain": "one row per account x feed (performance|costbasis|allocation) x level (Account|Class|Segment|Asset) x window",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "data/assets/scripts/silver/build_fact_taxsma_report.py over blackdiamond/49f/bronze/reporting_* (written by opal-assets-bd49f-reporting-pull)",
  "schedule": "none found: one partition (quarter end 2026-06-30)",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-07-17",
  "trading_days_behind_t1": 61,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-07-18T01:26:07Z",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 304496,
  "parquet_parts": 1,
  "schema_variants": 1,
  "rows_all_parts": 3361,
  "rows_newest_part": 3361,
  "newest_part": "date=2026-07-17/data.parquet",
  "rows_sampled": 3361,
  "row_count_rule": "one partition; ONE account in it (Tax SMA pilot)",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "schwab_account_id",
   "type": "string",
   "nullable": true,
   "description": "10-digit Schwab id",
   "example": "****1234"
  },
  {
   "name": "bd_account_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "z08********"
  },
  {
   "name": "bd_external_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<external id>"
  },
  {
   "name": "bd_account_number_masked",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "account_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "bridge_method",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "bridge_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "feed",
   "type": "string",
   "nullable": true,
   "description": "performance / costbasis / allocation",
   "example": ""
  },
  {
   "name": "source_hierarchy",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "level",
   "type": "string",
   "nullable": true,
   "description": "Account / Class / Segment / Asset",
   "example": ""
  },
  {
   "name": "level_key",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "level_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "level_ordinal",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "symbol",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "issue_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "q_end",
   "type": "string",
   "nullable": true,
   "description": "quarter end",
   "example": ""
  },
  {
   "name": "window_label",
   "type": "string",
   "nullable": true,
   "description": "period label (AsOf, CY2025, ...)",
   "example": ""
  },
  {
   "name": "window_start",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "window_end",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "data_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "pull_asof",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "twr",
   "type": "double",
   "nullable": true,
   "description": "time-weighted return",
   "example": ""
  },
  {
   "name": "mwr",
   "type": "double",
   "nullable": true,
   "description": "money-weighted return",
   "example": ""
  },
  {
   "name": "accrual",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "adjustmentDate",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_accrual",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_allocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_beginningAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_beginningMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_marketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_shortAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_shortMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_parent_units",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_accrual",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_allocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_beginningAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_beginningMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_marketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_shortAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_shortMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alloc_total_units",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "allocationOfParent",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "allocationOfTotal",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "beginningAccrual",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "beginningMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "benchmarks_json",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "containsHistory",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "containsPartialAllocation",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "currentPrice",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "currentUnits",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "daysHeld",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "descriptor_json",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "endingAccrual",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "endingMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fees",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "gainType",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "heldEntirePeriod",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "income",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "level_filters_json",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "marketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "money_weighted_returns_json",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "netAdditions",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "netGains",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "notHeldInPeriod",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "openDate",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "originalInvestment",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "paydownFactor",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "performingBmv",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "performingEmv",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "periodLength",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "positionClosed",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "positionOnlyBmv",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "positionOnlyEmv",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "proceeds",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedAdjustedCostBasis",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedAmortization",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedCostBasis",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedLongTerm",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedLongTermGain",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedLongTermLoss",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedShortTerm",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedShortTermGain",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedShortTermLoss",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "realizedTotal",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "returnsAnnualized",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "shortAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "shortMarketValue",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "soldUnits",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "time_weighted_returns_json",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "tradeDate",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unitCost",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "units",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedAdjustedCostBasis",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedAllocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedAmortization",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedCostBasis",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedLongTerm",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedLongTermGain",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedLongTermLoss",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedShortTerm",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedShortTermGain",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedShortTermLoss",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unrealizedTotal",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "feed": {
   "n_distinct": 3,
   "values_top": [
    "performance",
    "costbasis",
    "allocation"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-07-17/data.parquet"
  },
  "level": {
   "n_distinct": 4,
   "values_top": [
    "Asset",
    "Segment",
    "Class",
    "Account"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-07-17/data.parquet"
  },
  "window_label": {
   "n_distinct": 5,
   "values_top": [
    "2026-04-08_2026-06-30",
    "AsOf",
    "CY2025",
    "CY2024",
    "2026-03-16_2026-06-30"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-07-17/data.parquet"
  },
  "q_end": {
   "n_distinct": 1,
   "values_top": [
    "2026-06-30"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-07-17/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49f/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "schwab_account_id",
   "last4_derivation": "last 4 digits of schwab_account_id",
   "last4_collisions_within_firm": 0,
   "measured_on": "schwab_account_id, newest partition date=2026-07-17/data.parquet: 1 distinct accounts -> 1 distinct last-4; 0 last-4 values shared by 2+ accounts, covering 0 accounts",
   "claim": "measured",
   "note": "a single account: collisions trivially 0"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "tax sma report",
  "quarterly performance",
  "cost basis",
  "realized gains",
  "twr"
 ],
 "common_queries": [
  "What was the Q2 TWR of the Tax SMA account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none (taxsma gateway IAM exists: infra/aws/terraform/opal-gateway/taxsma_gateway_iam.tf)",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "org/standards/MDPF_TAXSMA_DATA_CONTRACT.json",
 "open_items": [
  "one account, one quarter: not a general table; covered by the MDPF TaxSMA contract, no new tool proposed"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49f/silver/fact_taxsma_report/date=2026-07-17/data.parquet",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### blackdiamond/49financial/silver/fact_insurance_insurancerelationshiplist_export/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/fact_insurance_insurancerelationshiplist_export",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver/fact_insurance_insurancerelationshiplist_export/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_insurance_insurancerelationshiplist_export",
 "grain": "one row per insurance relationship (household) per pull date: issuer, product type, contract count, total value",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-bd49finsurance (Lambda) on S3 ObjectCreated of blackdiamond/49financial/bronze/insurance_relationshipaccountdetailsearch/ and insurance_insurancerelationshiplist_export/",
  "schedule": "chain: bd-49f-session-chain rule (04:35Z daily, runner=insurance) -> opal-assets-bd49f-reporting-pull {leg: insurance} -> bronze -> S3 notification -> converter",
  "claim": "measured (Lambda config, S3 notification in infra/aws/terraform/opal-assets/silver.tf:855-870); chain inferred from infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf:319"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T04:35:22Z",
  "claim": "measured"
 },
 "size": {
  "objects": 92,
  "bytes": 583007,
  "parquet_parts": 46,
  "schema_variants": 1,
  "rows_all_parts": 3542,
  "rows_newest_part": 77,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 77,
  "row_count_rule": "full snapshot per date (77 rows newest); never sum across partitions; as_of_date column carries the vendor value date (2026-10-12 on 74 of 77 rows)",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "relationship_id",
   "type": "string",
   "nullable": true,
   "description": "BD relationship id (z08...)",
   "example": "z08********"
  },
  {
   "name": "relationship_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "teams",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "issuer",
   "type": "string",
   "nullable": true,
   "description": "insurance carrier",
   "example": ""
  },
  {
   "name": "product_type",
   "type": "string",
   "nullable": true,
   "description": "INSURANCE_OTHER / LIFEINSURANCE / ANNUITY (comma lists)",
   "example": ""
  },
  {
   "name": "rep_code",
   "type": "string",
   "nullable": true,
   "description": "rep code",
   "example": ""
  },
  {
   "name": "contracts",
   "type": "int64",
   "nullable": true,
   "description": "number of contracts",
   "example": ""
  },
  {
   "name": "total_value",
   "type": "double",
   "nullable": true,
   "description": "total contract value",
   "example": ""
  },
  {
   "name": "as_of_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "vendor value date",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (46 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "product_type": {
   "n_distinct": 10,
   "values_top": [
    "INSURANCE_OTHER",
    "INSURANCE_LIFEINSURANCE",
    "INSURANCE_OTHER, INSURANCE_ANNUITY",
    "INSURANCE_LIFEINSURANCE, INSURANCE_OTHER",
    "INSURANCE_OTHER, INSURANCE_LIFEINSURANCE",
    "INSURANCE_ANNUITY, INSURANCE_LIFEINSURANCE, INSURANCE_OTHER",
    "INSURANCE_ANNUITY",
    "Annuity - IRA",
    "INSURANCE_ANNUITY, INSURANCE_OTHER",
    "Insurance"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "as_of_date": {
   "n_distinct": 4,
   "values_top": [
    "2026-10-12",
    "2025-11-17",
    "2024-03-28",
    "2026-02-06"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "relationship_id",
   "last4_derivation": "no account column: the grain is the relationship; last-4 of relationship_id is unique here (77 -> 77) but it is not an account number",
   "last4_collisions_within_firm": 0,
   "measured_on": "relationship_id, newest partition date=2026-10-14/data.parquet: 77 distinct accounts -> 77 distinct last-4; 0 last-4 values shared by 2+ accounts, covering 0 accounts",
   "claim": "measured",
   "note": "carrier is the platform-like field"
  },
  "platform": {
   "column": "issuer",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "insurance",
  "annuities",
  "life insurance",
  "insurance by household",
  "contract value"
 ],
 "common_queries": [
  "What insurance and annuity contracts does relationship X hold and what are they worth?",
  "What is total insurance value across 49F?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_list_insurance",
   "inputs": {
    "firm": "49financial",
    "account_last4": "optional (resolved to relationship via fact_insurance_relationshipaccountdetailsearch.accounts)",
    "platform": "issuer filter",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "per relationship: issuer, product types, contracts, total value, vendor as_of_date",
   "answers": [
    "What insurance and annuity contracts does relationship X hold and what are they worth?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-bd49finsurance/bd49f_insurance_conversion.py@HEAD",
 "open_items": [],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver/fact_insurance_insurancerelationshiplist_export/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-bd49finsurance",
   "at": "2026-10-14T13:06Z"
  }
 ]
}
```

### blackdiamond/49financial/silver/fact_insurance_relationshipaccountdetailsearch/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/fact_insurance_relationshipaccountdetailsearch",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver/fact_insurance_relationshipaccountdetailsearch/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_insurance_relationshipaccountdetailsearch",
 "grain": "one row per insurance relationship per pull date with its account list (JSON string), custodian names and reporting dates",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-bd49finsurance (Lambda) on S3 ObjectCreated of blackdiamond/49financial/bronze/insurance_relationshipaccountdetailsearch/ and insurance_insurancerelationshiplist_export/",
  "schedule": "chain: bd-49f-session-chain rule (04:35Z daily, runner=insurance) -> opal-assets-bd49f-reporting-pull {leg: insurance} -> bronze -> S3 notification -> converter",
  "claim": "measured (Lambda config, S3 notification in infra/aws/terraform/opal-assets/silver.tf:855-870); chain inferred from infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf:319"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T04:35:14Z",
  "claim": "measured"
 },
 "size": {
  "objects": 92,
  "bytes": 1541966,
  "parquet_parts": 46,
  "schema_variants": 1,
  "rows_all_parts": 3542,
  "rows_newest_part": 77,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 77,
  "row_count_rule": "full snapshot per date (77 rows newest)",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "id",
   "type": "string",
   "nullable": true,
   "description": "BD relationship id (z08...)",
   "example": "z08********"
  },
  {
   "name": "internalId",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "displayName",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "clientTypeId",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "teams",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "accountCount",
   "type": "int64",
   "nullable": true,
   "description": "accounts in the relationship",
   "example": ""
  },
  {
   "name": "accounts",
   "type": "string",
   "nullable": true,
   "description": "JSON array of the relationship's accounts (client data)",
   "example": ""
  },
  {
   "name": "custodianNames",
   "type": "string",
   "nullable": true,
   "description": "JSON array of custodian / carrier names",
   "example": ""
  },
  {
   "name": "accountRegistrationTypeIdentifiers",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "reportingDates",
   "type": "string",
   "nullable": true,
   "description": "JSON reporting dates",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (46 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "custodianNames": {
   "n_distinct": 11,
   "values_top": [
    "[\"Brighthouse Financial - Financial Professional\"]",
    "[\"AXA Equitable\"]",
    "[\"Allianz Life\",\"Brighthouse Financial - Financial Professional\"]",
    "[\"Allianz Life\"]",
    "[\"North American Company\"]",
    "[\"Charles Schwab\"]",
    "[\"Brighthouse Financial (FKA MetLife)\"]",
    "[\"Brighthouse Financial - Financial Professional\",\"EquatePlus\"]",
    "[\"Vanguard\"]",
    "[\"Brighthouse Financial - Financial Professional\",\"Fidelity Investments - Fidelity.com Quicken Download\"]"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "clientTypeId": {
   "n_distinct": 1,
   "values_top": [
    "0"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "id",
   "last4_derivation": "account numbers live inside the accounts JSON; last-4 must be derived after parsing it (not measured)",
   "last4_collisions_within_firm": 0,
   "measured_on": "id, newest partition date=2026-10-14/data.parquet: 77 distinct accounts -> 77 distinct last-4; 0 last-4 values shared by 2+ accounts, covering 0 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "custodianNames",
   "values": [
    "Brighthouse Financial - Financial Professional",
    "AXA Equitable",
    "Allianz Life",
    "..."
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "insurance accounts",
  "insurance custodians",
  "relationship accounts"
 ],
 "common_queries": [
  "Which carrier holds the insurance accounts of relationship X?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "same as above",
 "open_items": [
  "accounts is a JSON string: an account_last4 lookup needs the JSON parsed; collisions inside it not measured"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver/fact_insurance_relationshipaccountdetailsearch/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### blackdiamond/49financial/silver/fact_insurance_relationshipdetail/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/fact_insurance_relationshipdetail",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver/fact_insurance_relationshipdetail/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_insurance_relationshipdetail",
 "grain": "one row per relationship detail record (one row total)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-bd49finsurance (relationshipdetail leg)",
  "schedule": "none observed: one partition 2026-08-27",
  "claim": "inferred"
 },
 "freshness": {
  "latest_partition": "2026-08-27",
  "trading_days_behind_t1": 32,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-30T02:21:51Z",
  "claim": "measured"
 },
 "size": {
  "objects": 2,
  "bytes": 28665,
  "parquet_parts": 1,
  "schema_variants": 1,
  "rows_all_parts": 1,
  "rows_newest_part": 1,
  "newest_part": "date=2026-08-27/data.parquet",
  "rows_sampled": 0,
  "row_count_rule": "one partition, 1 row; 8 of 31 columns typed null",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "z08********"
  },
  {
   "name": "internalId",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "displayName",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "inceptionDate",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "terminationDate",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "imageUrl",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "financialTeamTemplateId",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "financialTeam",
   "type": "string",
   "nullable": true,
   "description": "JSON",
   "example": ""
  },
  {
   "name": "teams",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolios",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "accounts",
   "type": "string",
   "nullable": true,
   "description": "JSON (client data)",
   "example": ""
  },
  {
   "name": "contacts",
   "type": "string",
   "nullable": true,
   "description": "JSON (client data)",
   "example": "<client data: redacted>"
  },
  {
   "name": "addresses",
   "type": "string",
   "nullable": true,
   "description": "JSON (client data)",
   "example": "<client data: redacted>"
  },
  {
   "name": "users",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "clientTypeId",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "userDefined",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "outsideIdentifiers",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "targets",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "benchmarks",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "notes",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "phoneNumbers",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "emailAddresses",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationshipType",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "segmentation",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "description",
   "type": "null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "relationship detail"
 ],
 "common_queries": [],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "none",
 "open_items": [
  "a probe artifact (1 row, 32 trading days behind); not a tool candidate; holds contact JSON, keep out of any tool"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver/fact_insurance_relationshipdetail/date=2026-08-27/data.parquet",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/fees/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/fees (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/fees/",
 "layer": "silver",
 "format": "parquet",
 "table": "fees (silver_legacy)",
 "grain": "one row per fee transaction line (transaction_id) per trade_date",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-08-24",
  "trading_days_behind_t1": 35,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:02:52Z",
  "claim": "measured"
 },
 "size": {
  "objects": 1957,
  "bytes": 210273646,
  "parquet_parts": 1957,
  "schema_variants": 25,
  "rows_all_parts": 3068821,
  "rows_newest_part": 1066,
  "newest_part": "date=2026-08-24/2026-08-24.parquet",
  "rows_sampled": 1066,
  "row_count_rule": "partition = trade_date; rows additive across partitions after de-dup on transaction_id (1,057 unique of 1,066 newest)",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "transaction_id",
   "type": "int64",
   "nullable": true,
   "description": "BD transaction id",
   "example": ""
  },
  {
   "name": "trade_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "trade date (= partition)",
   "example": ""
  },
  {
   "name": "settle_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "z08********"
  },
  {
   "name": "account_number",
   "type": "string",
   "nullable": true,
   "description": "custodian number",
   "example": "****1234"
  },
  {
   "name": "account_id",
   "type": "string",
   "nullable": true,
   "description": "BD id z08...",
   "example": "z08********"
  },
  {
   "name": "original_account_number",
   "type": "int64|string",
   "nullable": true,
   "description": "(type drifts across parts: int64|string)",
   "example": "****1234"
  },
  {
   "name": "account_display_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "original_account_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_owner_type",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_owner",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "asset_id",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_display_name",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "units",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "market_value",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "transaction_fee",
   "type": "double",
   "nullable": true,
   "description": "fee on the trade",
   "example": ""
  },
  {
   "name": "income",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_fee",
   "type": "double|int64",
   "nullable": true,
   "description": "advisory account fee (type drifts across parts: double|int64)",
   "example": ""
  },
  {
   "name": "tax_status",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "billing_account_custodian",
   "type": "string",
   "nullable": true,
   "description": "Schwab / ByAll Accounts / Fidelity IWS",
   "example": ""
  },
  {
   "name": "billing_account",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "billing_end_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "billing_start_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "flat_fee",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "basis_points",
   "type": "double|int64",
   "nullable": true,
   "description": "(type drifts across parts: double|int64)",
   "example": ""
  },
  {
   "name": "fee_schedule_level",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_rate_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fee_schedule_description",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_fee_schedule",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_billable",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "cusip",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1957 parts, 25 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "billing_account_custodian": {
   "n_distinct": 3,
   "values_top": [
    "Schwab",
    "ByAll Accounts",
    "Fidelity IWS"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-08-24/2026-08-24.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 6,
   "measured_on": "account_number, newest partition date=2026-08-24/2026-08-24.parquet: 200 distinct accounts -> 197 distinct last-4; 3 last-4 values shared by 2+ accounts, covering 6 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "billing_account_custodian",
   "values": [
    "Schwab",
    "ByAll Accounts",
    "Fidelity IWS"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "fees",
  "advisory fees",
  "transaction fees"
 ],
 "common_queries": [
  "What fees were charged to account ...1234 on a trade date?"
 ],
 "existing_gateway_tool": {
  "name": "blackdiamond_list_fees",
  "verdict": "keep (it reads opal-data-bd silver/fees, the live original, not this copy)"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/fees/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/fees/ until F11 moves the writer here. Live opal-data-bd silver/fees newest 2026-10-12 (710 rows, z08 only, 34 columns = this schema)."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/fees/date=2026-08-24/2026-08-24.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/fees/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/transactions/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/transactions (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/transactions/",
 "layer": "silver",
 "format": "parquet",
 "table": "transactions (silver_legacy)",
 "grain": "one row per transaction line; partition is the PULL date and holds a trade-date window (newest: trade dates 2026-06-30..2026-08-21, 1,035 unique transaction_id of 4,990 rows)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-08-25",
  "trading_days_behind_t1": 34,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:05:55Z",
  "claim": "measured"
 },
 "size": {
  "objects": 1879,
  "bytes": 562965982,
  "parquet_parts": 1878,
  "schema_variants": 13,
  "rows_all_parts": 6641006,
  "rows_newest_part": 0,
  "newest_part": "date=2026-08-25/2026-08-25.parquet",
  "rows_sampled": 4990,
  "row_count_rule": "newest two parts hold 0 rows; never sum across partitions, de-dup on transaction_id",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "transaction_id",
   "type": "int64|null|string",
   "nullable": true,
   "description": "BD id (type drifts across parts: int64|null|string)",
   "example": ""
  },
  {
   "name": "return_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "action",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "transaction_type",
   "type": "null|string",
   "nullable": true,
   "description": "Buy, Sale, Dividend, ...",
   "example": ""
  },
  {
   "name": "transaction_sub_type",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "external_flow",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "description",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "price",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "trade_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "trade date (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "entry_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "settle_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "relationship_id",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "z08********"
  },
  {
   "name": "relationship_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_display_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_sec_client_type",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_termination_date",
   "type": "double|null|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|timestamp[ns])",
   "example": ""
  },
  {
   "name": "relationship_inception_date",
   "type": "double|null|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "previous_system_key",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_id",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_display_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "history_start_date",
   "type": "double|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|timestamp[ns])",
   "example": ""
  },
  {
   "name": "account_number",
   "type": "int64|null|string",
   "nullable": true,
   "description": "(type drifts across parts: int64|null|string)",
   "example": "****1234"
  },
  {
   "name": "account_id",
   "type": "null|string",
   "nullable": true,
   "description": "z08...",
   "example": "z08********"
  },
  {
   "name": "original_account_number",
   "type": "int64|null|string",
   "nullable": true,
   "description": "(type drifts across parts: int64|null|string)",
   "example": "****1234"
  },
  {
   "name": "account_display_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "original_account_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "manager",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_owner_type",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_owner",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "history_start_date_1",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "closed_date",
   "type": "double|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|timestamp[ns])",
   "example": ""
  },
  {
   "name": "account_is_open",
   "type": "bool|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "performance_start_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "start_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "asset_id",
   "type": "int64|null|string",
   "nullable": true,
   "description": "(type drifts across parts: int64|null|string)",
   "example": ""
  },
  {
   "name": "asset_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_display_name",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fund_manager",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "units",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "market_value",
   "type": "double|null",
   "nullable": true,
   "description": "trade value",
   "example": ""
  },
  {
   "name": "transaction_fee",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "income",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_fee",
   "type": "double|int64|null",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|null)",
   "example": ""
  },
  {
   "name": "house_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "additional_advisor",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "additional_advisor_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "architect_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "consultant",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "architect",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "consultant_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "implementor_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "implementor",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "local_ops_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "investment_strategy_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "manager_strategy",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_create_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "managed_account_manager_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "local_ops",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "tax_status",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "expense_ratio",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "custodial_cost_basis_sync",
   "type": "bool|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_group",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "tax_status_1",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "goal",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "as_of_date",
   "type": "null|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: null|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "client_city",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_state",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_zip_code",
   "type": "double|int64|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_start_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "(present in 1717 of 1878 parts)",
   "example": ""
  },
  {
   "name": "is_new_client",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 1717 of 1878 parts)",
   "example": ""
  },
  {
   "name": "is_nna_inflow",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 1717 of 1878 parts)",
   "example": ""
  },
  {
   "name": "is_nna_outflow",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 1717 of 1878 parts)",
   "example": ""
  },
  {
   "name": "is_nna",
   "type": "null|string",
   "nullable": true,
   "description": "net new assets flag (present in 1717 of 1878 parts)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_ingested_at",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "cusip",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 1876 of 1878 parts)",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1878 parts, 13 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "transaction_type": {
   "n_distinct": 11,
   "values_top": [
    "Buy",
    "Sale",
    "Cash Deposit",
    "Transfer In",
    "Cash Withdrawal",
    "Dividend",
    "Journal",
    "Dividend Reinvestment",
    "Expense",
    "Valuation"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-08-23/2026-08-23.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 12,
   "measured_on": "account_number, newest partition date=2026-08-23/2026-08-23.parquet: 235 distinct accounts -> 229 distinct last-4; 6 last-4 values shared by 2+ accounts, covering 12 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "cash flows",
  "net new assets"
 ],
 "common_queries": [
  "What trades did account ...1234 make last month?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/transactions/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/transactions/ until F11 moves the writer here. Live opal-data-bd silver/transactions newest 2026-10-14 (2,921 rows, z08, 74 columns)."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/transactions/date=2026-08-25/2026-08-25.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/transactions/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/transactions_enriched/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/transactions_enriched (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/transactions_enriched/",
 "layer": "silver",
 "format": "parquet",
 "table": "transactions_enriched (silver_legacy)",
 "grain": "one row per transaction with Schwab-imputed enrichment (source_system)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-04-20",
  "trading_days_behind_t1": 122,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:06:29Z",
  "claim": "measured"
 },
 "size": {
  "objects": 519,
  "bytes": 188230783,
  "parquet_parts": 518,
  "schema_variants": 16,
  "rows_all_parts": 1598709,
  "rows_newest_part": 45,
  "newest_part": "date=2026-04-20/data.parquet",
  "rows_sampled": 45,
  "row_count_rule": "diagnostic artifact (_DIAGNOSTIC_ARTIFACT.txt in prefix)",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "transaction_id",
   "type": "double|int64|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|string)",
   "example": ""
  },
  {
   "name": "return_date",
   "type": "double|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "action",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "transaction_type",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "transaction_sub_type",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "external_flow",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "description",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "price",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "trade_date",
   "type": "double|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "entry_date",
   "type": "double|string|timestamp[ns]|timestamp[us]",
   "nullable": true,
   "description": "(type drifts across parts: double|string|timestamp[ns]|timestamp[us])",
   "example": ""
  },
  {
   "name": "settle_date",
   "type": "double|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "relationship_id",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": "z08********"
  },
  {
   "name": "relationship_name",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_display_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_sec_client_type",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "relationship_termination_date",
   "type": "double|null|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|timestamp[ns])",
   "example": ""
  },
  {
   "name": "relationship_inception_date",
   "type": "double|null|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "previous_system_key",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "portfolio_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "portfolio_id",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "portfolio_display_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "history_start_date",
   "type": "double|null|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|timestamp[ns])",
   "example": ""
  },
  {
   "name": "account_number",
   "type": "double|int64|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|string)",
   "example": "****1234"
  },
  {
   "name": "account_id",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": "z08********"
  },
  {
   "name": "original_account_number",
   "type": "double|int64|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|string)",
   "example": "****1234"
  },
  {
   "name": "account_display_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_name",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "original_account_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "manager",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "account_owner_type",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "account_owner",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_name",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "history_start_date_1",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "closed_date",
   "type": "double|null|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|timestamp[ns])",
   "example": ""
  },
  {
   "name": "account_is_open",
   "type": "bool|double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: bool|double|null|string)",
   "example": ""
  },
  {
   "name": "performance_start_date",
   "type": "double|null|string|timestamp[ns]|timestamp[us]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string|timestamp[ns]|timestamp[us])",
   "example": ""
  },
  {
   "name": "start_date",
   "type": "double|null|string|timestamp[ns]|timestamp[us]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string|timestamp[ns]|timestamp[us])",
   "example": ""
  },
  {
   "name": "asset_id",
   "type": "double|int64|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|null|string)",
   "example": ""
  },
  {
   "name": "asset_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "asset_display_name",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "fund_manager",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "units",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "market_value",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "transaction_fee",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "income",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_fee",
   "type": "double|int64|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|string)",
   "example": ""
  },
  {
   "name": "house_split_pct",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "additional_advisor",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "additional_advisor_split_pct",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "architect_split_pct",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "consultant",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "architect",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "consultant_split_pct",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "implementor_split_pct",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "implementor",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "local_ops_split_pct",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "investment_strategy_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "manager_strategy",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "account_create_date",
   "type": "double|null|string|timestamp[ns]|timestamp[us]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string|timestamp[ns]|timestamp[us])",
   "example": ""
  },
  {
   "name": "managed_account_manager_name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "local_ops",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "tax_status",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "expense_ratio",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "custodial_cost_basis_sync",
   "type": "bool|double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: bool|double|null|string)",
   "example": ""
  },
  {
   "name": "portfolio_group",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "tax_status_1",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "goal",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "as_of_date",
   "type": "double|null|string|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "client_city",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_state",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_zip_code",
   "type": "double|int64|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|int64|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_start_date",
   "type": "double|null|timestamp[ns]",
   "nullable": true,
   "description": "(type drifts across parts: double|null|timestamp[ns])",
   "example": ""
  },
  {
   "name": "is_new_client",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "is_nna_inflow",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "is_nna_outflow",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "is_nna",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "_ingested_at",
   "type": "double|string",
   "nullable": true,
   "description": "(type drifts across parts: double|string)",
   "example": ""
  },
  {
   "name": "cusip",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "source_system",
   "type": "string",
   "nullable": true,
   "description": "schwab_imputed",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (518 parts, 16 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "source_system": {
   "n_distinct": 1,
   "values_top": [
    "schwab_imputed"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-04-20/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 0,
   "measured_on": "account_number, newest partition date=2026-04-20/data.parquet: 32 distinct accounts -> 32 distinct last-4; 0 last-4 values shared by 2+ accounts, covering 0 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "transactions enriched"
 ],
 "common_queries": [],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/transactions_enriched/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/transactions_enriched/ until F11 moves the writer here. Its live original also stops 2026-04-20: a retired diagnostic."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/transactions_enriched/date=2026-04-20/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/transactions_enriched/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/allocations/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/allocations (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/allocations/",
 "layer": "silver",
 "format": "parquet",
 "table": "allocations (silver_legacy)",
 "grain": "one row per account per allocation report date (newest 7,070 rows, 7,070 accounts)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-08-21",
  "trading_days_behind_t1": 36,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T22:59:44Z",
  "claim": "measured"
 },
 "size": {
  "objects": 128,
  "bytes": 139748736,
  "parquet_parts": 128,
  "schema_variants": 5,
  "rows_all_parts": 856480,
  "rows_newest_part": 7070,
  "newest_part": "date=2026-08-21/2026-08-21.parquet",
  "rows_sampled": 7070,
  "row_count_rule": "full snapshot per date; never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "portfolio_group",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "original_account_number",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "****1234"
  },
  {
   "name": "relationship_id",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "z08********"
  },
  {
   "name": "relationship_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_display_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "relationship_sec_client_type",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "relationship_inception_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "relationship_termination_date",
   "type": "double|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: double|timestamp[ns])",
   "example": ""
  },
  {
   "name": "portfolio_id",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolio_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "show_client",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "basis_points",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolio_benchmark",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_level",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "flat_fee",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "history_start_date",
   "type": "double|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: double|timestamp[ns])",
   "example": ""
  },
  {
   "name": "address_source_client_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "address_source_city",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "address_source_state",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "address_source_zip_code",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_number",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "****1234"
  },
  {
   "name": "account_id",
   "type": "null|string",
   "nullable": true,
   "description": "z08... (present in 125 of 128 parts)",
   "example": "z08********"
  },
  {
   "name": "account_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "flat_fee_1",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "basis_points_1",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_billing_notes",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "start_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "performance_start_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "as_of_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "account_is_open",
   "type": "bool|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "closed_date",
   "type": "double|string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: double|string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "history_start_date_1",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "client_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_city",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_state",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "client_zip_code",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "house_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "additional_advisor",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "additional_advisor_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "architect_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "architect",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "consultant_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "consultant",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "implementor",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "local_ops",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "implementor_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "local_ops_split_pct",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "investment_strategy_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "manager_strategy",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_create_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 125 of 128 parts) (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "account_type",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_registration_type",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "managed_account_manager_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_level_1",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "lower_range",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "upper_range",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_rate_type",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_type",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_description",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_discretionary",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_fee_schedule",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_billable",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_supervised",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_benchmark",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "reporting_target_description",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "tax_lot_methodology",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "tax_status",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_subcategory",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_category",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "goal",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_owner_type",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_owner",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "manager",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "style",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "rep_code",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_display_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "original_account_name",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_display_number",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": "****1234"
  },
  {
   "name": "fee_schedule_rate_type_1",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_type_1",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "upper_range_1",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "lower_range_1",
   "type": "int64|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "fee_schedule_description_1",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolio_fee_schedule",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "reporting_target_description_1",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolio_reporting_target",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolio_logo",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_allocation",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_market_value",
   "type": "double|null",
   "nullable": true,
   "description": "market value (present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolio_group_market_value",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "cash_market_value",
   "type": "double|null",
   "nullable": true,
   "description": "cash (present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "cash_allocation",
   "type": "double|null",
   "nullable": true,
   "description": "(present in 125 of 128 parts)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "_ingested_at",
   "type": "null|string",
   "nullable": true,
   "description": "(present in 43 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Group",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Original Account Number",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "****1234"
  },
  {
   "name": "Relationship ID",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "z09********"
  },
  {
   "name": "Relationship Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Relationship Display Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Relationship SEC Client Type",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Relationship Inception Date",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Relationship Termination Date",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "PortfolioID",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Show Client",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Basis Points",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Benchmark",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Level",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Flat Fee",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "History Start Date",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Address Source Client Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Address Source City",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Address Source State",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Address Source Zip Code",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Account Number",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "****1234"
  },
  {
   "name": "AccountID",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "z09********"
  },
  {
   "name": "Account Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Flat Fee.1",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Basis Points.1",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account - Billing Notes",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Start Date",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Performance Start Date",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "As of Date",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Is Open",
   "type": "bool",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Closed Date",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "History Start Date.1",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Client Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client City",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client State",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client Zip Code",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "49 House Split %",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Additional Advisor",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Additional Advisor Split %",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Architect Split %",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Architect",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Consultant Split %",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Consultant",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Implementor",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Local Ops",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Implementor Split %",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Local Ops Split %",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Investment Strategy Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Manager Strategy",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Create Date",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Type",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Registration Type",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Managed Account Manager Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Level.1",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Lower Range",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Upper Range",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Rate Type",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Type",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Description",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Discretionary",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Fee Schedule",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Billable",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Supervised",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Benchmark",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Reporting Target Description",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Tax Lot Methodology",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Tax Status",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Subcategory",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Category",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Goal",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Owner Type",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Owner",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Manager",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Style",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Rep Code",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Display Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Original Account Name",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Display Number",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Rate Type.1",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Type.1",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Upper Range.1",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Lower Range.1",
   "type": "int64",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Fee Schedule Description.1",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Fee Schedule",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Reporting Target Description.1",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Reporting Target",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Logo",
   "type": "string",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Allocation",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Account Market Value",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Portfolio Group Market Value",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Cash Market Value",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "Cash Allocation",
   "type": "double",
   "nullable": true,
   "description": "(present in 3 of 128 parts)",
   "example": ""
  },
  {
   "name": "portfolioid",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "account_-_billing_notes",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "49_house_split_%",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "additional_advisor_split_%",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "architect_split_%",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "consultant_split_%",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "implementor_split_%",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  },
  {
   "name": "local_ops_split_%",
   "type": "string",
   "nullable": true,
   "description": "(present in 82 of 128 parts)",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (128 parts, 5 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 3470,
   "measured_on": "account_number, newest partition date=2026-08-21/2026-08-21.parquet: 7055 distinct accounts -> 5137 distinct last-4; 1552 last-4 values shared by 2+ accounts, covering 3470 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "account allocation",
  "account market value"
 ],
 "common_queries": [
  "What is account ...1234 worth?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/allocations/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/allocations/ until F11 moves the writer here. Live opal-data-bd silver/allocations newest 2026-10-09 (7,345 rows, z08, 94 columns); 5 schema variants here mix snake_case and Title Case names."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/allocations/date=2026-08-21/2026-08-21.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/allocations/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/assets/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/assets (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/assets/",
 "layer": "silver",
 "format": "parquet",
 "table": "assets (silver_legacy)",
 "grain": "one row per asset-bearing transaction line per trade date (dividends, reinvestments, ...)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-06-18",
  "trading_days_behind_t1": 80,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:00:44Z",
  "claim": "measured"
 },
 "size": {
  "objects": 1890,
  "bytes": 135268048,
  "parquet_parts": 1890,
  "schema_variants": 11,
  "rows_all_parts": 3682869,
  "rows_newest_part": 25332,
  "newest_part": "date=2026-06-18/2026-06-18.parquet",
  "rows_sampled": 25332,
  "row_count_rule": "partition = trade_date",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "transaction_id",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "z08********"
  },
  {
   "name": "account_id",
   "type": "string",
   "nullable": true,
   "description": "z08...",
   "example": "z08********"
  },
  {
   "name": "asset_super_class",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_class",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_segment",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_id",
   "type": "string",
   "nullable": true,
   "description": "BD asset id",
   "example": ""
  },
  {
   "name": "asset_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Asset Display Name",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Original Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "last_dividend",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "symbol",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "ticker",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "cusip",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "alternative_identifier",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": ""
  },
  {
   "name": "custodial_cost_basis_sync",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "coupon_rate",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "first_payment_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "last_payment_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "trade_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "settle_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "entry_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "price",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "transaction_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "transaction_sub_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "external_flow",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "has_contra_account",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "contra_account_number",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Contra Account Name",
   "type": "double|null|string",
   "nullable": true,
   "description": "(type drifts across parts: double|null|string)",
   "example": "<client data: redacted>"
  },
  {
   "name": "Description",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Action",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1890 parts, 11 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "transaction_type": {
   "n_distinct": 13,
   "values_top": [
    "Dividend",
    "Dividend Reinvestment",
    "Sale",
    "Buy",
    "Transfer Out",
    "Cash Deposit",
    "Expense",
    "Transfer In",
    "Cash Withdrawal",
    "Capital Gains"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-06-18/2026-06-18.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_id",
   "last4_derivation": "bd internal id only: last-4 of account_id is NOT usable (5,321 ids -> 997 last-4)",
   "last4_collisions_within_firm": 5292,
   "measured_on": "account_id, newest partition date=2026-06-18/2026-06-18.parquet: 5321 distinct accounts -> 997 distinct last-4; 968 last-4 values shared by 2+ accounts, covering 5292 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "asset transactions",
  "dividends"
 ],
 "common_queries": [],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/assets/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/assets/ until F11 moves the writer here. Its live original also stops 2026-06-18."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/assets/date=2026-06-18/2026-06-18.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/assets/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/realized/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/realized (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/realized/",
 "layer": "silver",
 "format": "parquet",
 "table": "realized (silver_legacy)",
 "grain": "one row per realized lot closing (account x asset x open/trade date)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-08-25",
  "trading_days_behind_t1": 34,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:03:57Z",
  "claim": "measured"
 },
 "size": {
  "objects": 1310,
  "bytes": 71802093,
  "parquet_parts": 1310,
  "schema_variants": 4,
  "rows_all_parts": 2798029,
  "rows_newest_part": 31009,
  "newest_part": "date=2026-08-25/2026-08-25.parquet",
  "rows_sampled": 31009,
  "row_count_rule": "partition = trade_date; plus _undated aggregate parts",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "account_id",
   "type": "string",
   "nullable": true,
   "description": "z08...",
   "example": "z08********"
  },
  {
   "name": "asset_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "last_sell_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "(present in 1 of 1310 parts)",
   "example": ""
  },
  {
   "name": "open_date",
   "type": "string|timestamp[ns]",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts) (type drifts across parts: string|timestamp[ns])",
   "example": ""
  },
  {
   "name": "trade_date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "unit_cost",
   "type": "double",
   "nullable": true,
   "description": "unit cost (present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "account_number",
   "type": "int64|string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts) (type drifts across parts: int64|string)",
   "example": "****1234"
  },
  {
   "name": "asset_id",
   "type": "int64|string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts) (type drifts across parts: int64|string)",
   "example": ""
  },
  {
   "name": "symbol",
   "type": "string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "cusip",
   "type": "string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "asset_display_name",
   "type": "double",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "original_asset_name",
   "type": "string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "last_dividend",
   "type": "double",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  },
  {
   "name": "_ingested_at",
   "type": "string",
   "nullable": true,
   "description": "(present in 1309 of 1310 parts)",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (1310 parts, 4 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 2409,
   "measured_on": "account_number, newest partition date=2026-08-25/2026-08-25.parquet: 5643 distinct accounts -> 4338 distinct last-4; 1104 last-4 values shared by 2+ accounts, covering 2409 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "realized gains",
  "closed lots"
 ],
 "common_queries": [
  "What gains did account ...1234 realize this year?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/realized/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/realized/ until F11 moves the writer here. Live opal-data-bd silver/realized newest 2026-10-14 (45,208 rows, z08)."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/realized/date=2026-08-25/2026-08-25.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/realized/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/unrealized/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/unrealized (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/unrealized/",
 "layer": "silver",
 "format": "parquet",
 "table": "unrealized (silver_legacy)",
 "grain": "one row per open tax lot (account x asset x open_date) per weekly snapshot",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-08-21",
  "trading_days_behind_t1": 36,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:06:47Z",
  "claim": "measured"
 },
 "size": {
  "objects": 70,
  "bytes": 143621297,
  "parquet_parts": 70,
  "schema_variants": 4,
  "rows_all_parts": 5921647,
  "rows_newest_part": 110376,
  "newest_part": "date=2026-08-21/2026-08-21.parquet",
  "rows_sampled": 110376,
  "row_count_rule": "weekly snapshot (69 dated parts since 2026-03-27); never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "open_date",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "unit_cost",
   "type": "double|null",
   "nullable": true,
   "description": "unit cost",
   "example": ""
  },
  {
   "name": "inherited_date",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_id",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "z08********"
  },
  {
   "name": "account_number",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "account_id",
   "type": "null|string",
   "nullable": true,
   "description": "z08...",
   "example": "z08********"
  },
  {
   "name": "asset_id",
   "type": "int64|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "last_dividend",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "original_asset_name",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_display_name",
   "type": "double|null",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "symbol",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "ticker",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "cusip",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_ingested_at",
   "type": "null|string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "market_value",
   "type": "double|null",
   "nullable": true,
   "description": "lot market value (present in 18 of 70 parts) (present in 18 of 70 parts)",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (70 parts, 4 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number",
   "last4_collisions_within_firm": 4156,
   "measured_on": "account_number, newest partition date=2026-08-21/2026-08-21.parquet: 7734 distinct accounts -> 5420 distinct last-4; 1842 last-4 values shared by 2+ accounts, covering 4156 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "holdings",
  "tax lots",
  "unrealized gains",
  "positions"
 ],
 "common_queries": [
  "What does account ...1234 hold?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/unrealized/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/unrealized/ until F11 moves the writer here. Live opal-data-bd silver/unrealized newest 2026-10-09 (108,439 rows, 7,395 accounts, z08). This is the nearest 49F HOLDINGS table."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/unrealized/date=2026-08-21/2026-08-21.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/unrealized/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/prices/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/prices (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/prices/",
 "layer": "silver",
 "format": "parquet",
 "table": "prices (silver_legacy)",
 "grain": "one row per asset (ticker) per price date",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-08-23",
  "trading_days_behind_t1": 36,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:09:05Z",
  "claim": "measured"
 },
 "size": {
  "objects": 140,
  "bytes": 143946486,
  "parquet_parts": 139,
  "schema_variants": 1,
  "rows_all_parts": 13532348,
  "rows_newest_part": 10831,
  "newest_part": "date=2026-08-23/2026-08-23.parquet",
  "rows_sampled": 0,
  "row_count_rule": "partition = price date",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "date",
   "type": "timestamp[ns]",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "asset_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": true,
   "description": "ticker",
   "example": ""
  },
  {
   "name": "price",
   "type": "double",
   "nullable": true,
   "description": "price",
   "example": ""
  },
  {
   "name": "source",
   "type": "string",
   "nullable": true,
   "description": "price source",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (139 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent: no account column",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "prices",
  "security prices"
 ],
 "common_queries": [
  "What price did BD use for ticker X on date D?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/prices/ (live original)",
 "open_items": [
  "FROZEN copy: do not build a tool on this prefix; read the live opal-data-bd silver/prices/ until F11 moves the writer here. Live opal-data-bd silver/prices newest 2026-10-14 (11,143 rows)."
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/49financial/silver_legacy/prices/date=2026-08-23/2026-08-23.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "footer + account-column read of the newest opal-data-bd silver/prices/ part (schema subset equal)",
   "at": "2026-10-14T13:09Z"
  }
 ]
}
```

### blackdiamond/49financial/silver_legacy/_single_file/

```json
{
 "contract_id": "opal-data-assets/silver/49financial/_single_file (silver_legacy)",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/49financial/silver_legacy/_single_file/",
 "layer": "silver",
 "format": "parquet",
 "table": "_single_file (silver_legacy)",
 "grain": "20 unrelated single-file Parquet tables (daily_positions, daily_aua, interpolated_prices, nna_timeseries, ...), each its own grain",
 "partition": {
  "keys": [],
  "claim": "measured (no partition: single files)"
 },
 "producer": {
  "name": "one-time copy of s3://opal-data-bd/silver/<table>/ made 2026-08-25 22:59-23:09Z (ADVI_FIRMBKTS F11 move, scopes.json tier_live note); no writer since",
  "schedule": "none (frozen). The LIVE writer still writes opal-data-bd silver/ (bd-49f runners; rules bd-49f-runner-daily and bd-49f-fees-runner-daily read DISABLED, so the live trigger is another path, not traced)",
  "claim": "measured (LastModified window, live opal-data-bd newest partitions) / inferred (copy semantics)"
 },
 "freshness": {
  "latest_partition": "2026-01-28",
  "trading_days_behind_t1": null,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-08-25T23:06:58Z",
  "claim": "measured"
 },
 "size": {
  "objects": 28,
  "bytes": 1193013527,
  "parquet_parts": 20,
  "schema_variants": 20,
  "rows_all_parts": 142813111,
  "rows_newest_part": 1280,
  "newest_part": "nna_timeseries.parquet",
  "rows_sampled": 0,
  "row_count_rule": "per file; see single_files",
  "claim": "measured"
 },
 "columns": [],
 "columns_note": "names and types are the union of every part's Parquet footer (20 parts, 20 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/49financial/",
   "values": [
    "49financial (key segment alias 49f; registry infra/logic/registry/scopes.json monolith_scopes.blackdiamond = [49f, 49financial])"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent (per file)",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "aua history",
  "daily positions history",
  "nna history"
 ],
 "common_queries": [],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "s3://opal-data-bd/silver/*.parquet (live originals)",
 "open_items": [
  "20 schema variants = 20 different tables; not a tool candidate; daily_positions.parquet (116,189,990 rows) is a Feb-2026 history artifact"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  }
 ],
 "single_files": [
  {
   "file": "aua_validation_log.parquet",
   "rows": 1
  },
  {
   "file": "bd_allocations.parquet",
   "rows": 6385
  },
  {
   "file": "bd_assets.parquet",
   "rows": 3449107
  },
  {
   "file": "bd_assets_dim.parquet",
   "rows": 10937
  },
  {
   "file": "bd_aua_timeseries.parquet",
   "rows": 71
  },
  {
   "file": "bd_canonical_timeline.parquet",
   "rows": 5672
  },
  {
   "file": "bd_nna_by_architect.parquet",
   "rows": 85
  },
  {
   "file": "bd_nna_daily.parquet",
   "rows": 1589
  },
  {
   "file": "bd_transactions_backup_2026-01-20.parquet",
   "rows": 2567534
  },
  {
   "file": "bd_transactions_backup_2026-01-28.parquet",
   "rows": 2572605
  },
  {
   "file": "daily_aua.parquet",
   "rows": 7635276
  },
  {
   "file": "daily_aua_firm.parquet",
   "rows": 2038
  },
  {
   "file": "daily_flows.parquet",
   "rows": 9757
  },
  {
   "file": "daily_positions.parquet",
   "rows": 116189990
  },
  {
   "file": "historical_dividends.parquet",
   "rows": 12887
  },
  {
   "file": "historical_prices.parquet",
   "rows": 5775200
  },
  {
   "file": "historical_prices_20260213.parquet",
   "rows": 243
  },
  {
   "file": "historical_prices_final.parquet",
   "rows": 252
  },
  {
   "file": "interpolated_prices.parquet",
   "rows": 4572202
  },
  {
   "file": "nna_timeseries.parquet",
   "rows": 1280
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_allocations/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_allocations",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_allocations/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_allocations",
 "grain": "one row per account x relationship/portfolio line of the BD allocation export (1,524 rows, 865 accounts; 659 repeat AccountID rows)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:05Z",
  "claim": "measured"
 },
 "size": {
  "objects": 144,
  "bytes": 12676990,
  "parquet_parts": 144,
  "schema_variants": 1,
  "rows_all_parts": 122735,
  "rows_newest_part": 1524,
  "newest_part": "date=2026-10-13/data.parquet",
  "rows_sampled": 1524,
  "row_count_rule": "full snapshot per report date; never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "Account Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Registration Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Original Account Number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "Team",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Team Display Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Team Description",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Address 1",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Address 2",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "State",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "City",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Phone",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Primary Email",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Zip Code",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Relationship ID",
   "type": "string",
   "nullable": true,
   "description": "BD relationship (household) id (z09...)",
   "example": "z09********"
  },
  {
   "name": "Relationship Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "PortfolioID",
   "type": "string",
   "nullable": true,
   "description": "BD portfolio id",
   "example": ""
  },
  {
   "name": "Fee Schedule Level",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Fee Schedule Rate Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Fee Schedule Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "BD3 Report Template Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "BD3 Report Template Description",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Portfolio Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Flat Fee",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number (mostly 9-digit Fidelity)",
   "example": "****1234"
  },
  {
   "name": "AccountID",
   "type": "string",
   "nullable": true,
   "description": "BD internal account id (z09 + digits); unique per account",
   "example": "z09********"
  },
  {
   "name": "Data Provider",
   "type": "string",
   "nullable": true,
   "description": "feed provider",
   "example": ""
  },
  {
   "name": "DST Rep Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "SEC Client Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Rep Code",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Custodian",
   "type": "string",
   "nullable": true,
   "description": "custodian / data feed name",
   "example": ""
  },
  {
   "name": "Manager",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "External Style ID",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Owner",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Account Owner Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Configuration Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Configuration Description",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Rep Fee Split",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Discount Percentage",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Notes",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Team Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Include Non-Billable",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account - Billing Breakpoint Portfolio",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Strategy ID",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Strategy Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Advisor of Record Name & B2B ID",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Authorized Person",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "NFS Account Number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "Team Name - Salentica",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Manager Strategy",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Investment Strategy Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Managed Account Manager Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Allocation",
   "type": "double",
   "nullable": true,
   "description": "account weight",
   "example": ""
  },
  {
   "name": "Account Market Value",
   "type": "double",
   "nullable": true,
   "description": "account market value",
   "example": ""
  },
  {
   "name": "Relationship Market Value",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Cash Market Value",
   "type": "double",
   "nullable": true,
   "description": "cash",
   "example": ""
  },
  {
   "name": "Cash Allocation",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "bronze xlsx key",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "report as-of date (= partition)",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "feed family",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "silver schema version",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (144 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "Custodian": {
   "n_distinct": 25,
   "values_top": [
    "Fidelity IWS",
    "Alternative Investment",
    "Investor Manual Accounts",
    "Schwab",
    "Bank of America",
    "Voya Financial - Participant Retirement",
    "Chase",
    "American Airlines Credit Union",
    "Fidelity Investments",
    "Fidelity CGF"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-13/data.parquet"
  },
  "Data Provider": {
   "n_distinct": 8,
   "values_top": [
    "Fidelity IWS",
    "ByAll Accounts",
    "Alternative Investment",
    "Investor Manual Accounts",
    "Schwab",
    "Fidelity CGF",
    "Strata Trust Company",
    "Manual"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-13/data.parquet"
  },
  "Account Type": {
   "n_distinct": 31,
   "values_top": [
    "IRA",
    "Brokerage",
    "RothIRA",
    "Joint",
    "Trust",
    "No Account Type Assigned",
    "InheritedIRA",
    "UTMA",
    "Bank",
    "401K"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-13/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account Number",
   "last4_derivation": "last 4 alphanumerics of Account Number (custodian number); AccountID last-4 is NOT usable",
   "last4_collisions_within_firm": 63,
   "measured_on": "Account Number, newest partition date=2026-10-13/data.parquet: 863 distinct accounts -> 808 distinct last-4; 8 last-4 values shared by 2+ accounts, covering 63 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "Custodian",
   "values": [
    "Fidelity IWS",
    "Alternative Investment",
    "Investor Manual Accounts",
    "Schwab",
    "Bank of America",
    "..."
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account profile",
  "account market value",
  "custodian",
  "fee schedule",
  "household",
  "allocation"
 ],
 "common_queries": [
  "What is account ...1234 worth and where is it custodied?",
  "What fee schedule applies to account ...1234?",
  "Which accounts are in household X?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_resolve_account",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "optional Custodian",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "candidate accounts with masked number, AccountID, account type, custodian -- a list when last-4 collides",
   "answers": []
  },
  {
   "name": "blackdiamond_get_account_profile",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "optional Custodian",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "account type, registration, custodian, relationship, portfolio, market value, cash, fee schedule and billing fields (client contact columns never returned)",
   "answers": [
    "What is account ...1234 worth and where is it custodied?",
    "What fee schedule applies to account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "holds client contact columns (Address 1/2, Phone, Primary Email, Zip, City, State): a tool must project them out"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_allocations/date=2026-10-13/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_holdings/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_holdings",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_holdings/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_holdings",
 "grain": "one row per account x asset (position) per report date (21,412 rows, 1,001 accounts; 102 duplicate (AccountID, AssetID) rows)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:04Z",
  "claim": "measured"
 },
 "size": {
  "objects": 93,
  "bytes": 38612498,
  "parquet_parts": 93,
  "schema_variants": 2,
  "rows_all_parts": 1517469,
  "rows_newest_part": 21412,
  "newest_part": "date=2026-10-13/data.parquet",
  "rows_sampled": 21412,
  "row_count_rule": "full snapshot per report date (93 dated parts since 2026-06-09); never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "Market Value",
   "type": "double",
   "nullable": true,
   "description": "market value",
   "example": ""
  },
  {
   "name": "Units",
   "type": "double",
   "nullable": true,
   "description": "units / shares",
   "example": ""
  },
  {
   "name": "Unaccrued Market Value",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Accrual",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Relationship ID",
   "type": "string",
   "nullable": true,
   "description": "BD relationship (household) id (z09...)",
   "example": "z09********"
  },
  {
   "name": "PortfolioID",
   "type": "string",
   "nullable": true,
   "description": "BD portfolio id",
   "example": ""
  },
  {
   "name": "AccountID",
   "type": "string",
   "nullable": true,
   "description": "BD internal account id (z09 + digits); unique per account",
   "example": "z09********"
  },
  {
   "name": "Account Number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number (mostly 9-digit Fidelity)",
   "example": "****1234"
  },
  {
   "name": "AssetID",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Asset Display Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Original Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Last Dividend",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Symbol",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Ticker",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "CUSIP",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Alternative Identifier",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Expense Ratio",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Cash Equivalent",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "bronze xlsx key",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "report as-of date (= partition)",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "feed family",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "silver schema version",
   "example": ""
  },
  {
   "name": "Account Supervised",
   "type": "string",
   "nullable": true,
   "description": "(present in 38 of 93 parts)",
   "example": ""
  },
  {
   "name": "Holding Supervised",
   "type": "string",
   "nullable": true,
   "description": "(present in 38 of 93 parts)",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (93 parts, 2 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "Cash Equivalent": {
   "n_distinct": 2,
   "values_top": [
    "false",
    "true"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-13/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account Number",
   "last4_derivation": "last 4 alphanumerics of Account Number (custodian number); AccountID last-4 is NOT usable",
   "last4_collisions_within_firm": 84,
   "measured_on": "Account Number, newest partition date=2026-10-13/data.parquet: 998 distinct accounts -> 932 distinct last-4; 18 last-4 values shared by 2+ accounts, covering 84 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "holdings",
  "positions",
  "what does the account own",
  "market value by security"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "How much of account ...1234 is in cash?",
  "Which accounts hold ticker X?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_get_holdings",
   "inputs": {
    "firm": "cottonwood|49financial",
    "account_last4": "1234",
    "platform": "optional",
    "as_of": "YYYY-MM-DD (newest partition on or before)"
   },
   "returns": "positions: asset, ticker, CUSIP, units, market value, accrual, cash flag; totals = sum of Market Value of ONE partition; for 49financial the source is opal-data-bd silver/unrealized (weekly), stated in the envelope",
   "answers": [
    "What does account ...1234 hold today?",
    "How much of account ...1234 is in cash?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "2 schema variants: Account Supervised / Holding Supervised present in 38 of 93 parts",
  "102 duplicate (AccountID, AssetID) rows on 2026-10-13: a tool must sum per key, not dedupe blindly (cause not traced)"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_holdings/date=2026-10-13/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_unrealized/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_unrealized",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_unrealized/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_unrealized",
 "grain": "one row per open tax lot (account x asset x open date) per report date (60,905 rows, 808 accounts; 47 exact-duplicate rows)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:08Z",
  "claim": "measured"
 },
 "size": {
  "objects": 144,
  "bytes": 314124756,
  "parquet_parts": 144,
  "schema_variants": 1,
  "rows_all_parts": 7894328,
  "rows_newest_part": 60905,
  "newest_part": "date=2026-10-13/data.parquet",
  "rows_sampled": 60905,
  "row_count_rule": "full snapshot per report date; never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "Open Date",
   "type": "string",
   "nullable": true,
   "description": "lot open date",
   "example": ""
  },
  {
   "name": "Relationship ID",
   "type": "string",
   "nullable": true,
   "description": "BD relationship (household) id (z09...)",
   "example": "z09********"
  },
  {
   "name": "Account Number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number (mostly 9-digit Fidelity)",
   "example": "****1234"
  },
  {
   "name": "AccountID",
   "type": "string",
   "nullable": true,
   "description": "BD internal account id (z09 + digits); unique per account",
   "example": "z09********"
  },
  {
   "name": "Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Security Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Ticker",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "CUSIP",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Units",
   "type": "double",
   "nullable": true,
   "description": "units / shares",
   "example": ""
  },
  {
   "name": "Cost Basis",
   "type": "double",
   "nullable": true,
   "description": "cost basis",
   "example": ""
  },
  {
   "name": "Market Value",
   "type": "double",
   "nullable": true,
   "description": "market value",
   "example": ""
  },
  {
   "name": "Short-Term Gain/Loss",
   "type": "double",
   "nullable": true,
   "description": "ST gain",
   "example": ""
  },
  {
   "name": "Long-Term Gain/Loss",
   "type": "double",
   "nullable": true,
   "description": "LT gain",
   "example": ""
  },
  {
   "name": "Total Gain Loss",
   "type": "double",
   "nullable": true,
   "description": "total gain",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "bronze xlsx key",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "report as-of date (= partition)",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "feed family",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "silver schema version",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (144 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "Security Type": {
   "n_distinct": 1,
   "values_top": [
    "MUTUAL FUNDS-BONDS"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-13/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account Number",
   "last4_derivation": "last 4 alphanumerics of Account Number (custodian number); AccountID last-4 is NOT usable",
   "last4_collisions_within_firm": 57,
   "measured_on": "Account Number, newest partition date=2026-10-13/data.parquet: 806 distinct accounts -> 754 distinct last-4; 5 last-4 values shared by 2+ accounts, covering 57 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "tax lots",
  "unrealized gains",
  "cost basis",
  "holdings by lot"
 ],
 "common_queries": [
  "What is the unrealized gain on account ...1234?",
  "What are the tax lots of ticker X in account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_get_unrealized_lots",
   "inputs": {
    "firm": "cottonwood|49financial",
    "account_last4": "1234",
    "platform": "",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "lots with open date, units, cost basis, market value, ST/LT/total gain; totals per account",
   "answers": [
    "What is the unrealized gain on account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_unrealized/date=2026-10-13/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_realized/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_realized",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_realized/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_realized",
 "grain": "one row per realized lot closing (account x asset x open/trade date); the partition holds a trailing trade-date window (newest: 2026-09-30..2026-10-12)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:01Z",
  "claim": "measured"
 },
 "size": {
  "objects": 122,
  "bytes": 30912188,
  "parquet_parts": 122,
  "schema_variants": 1,
  "rows_all_parts": 1461537,
  "rows_newest_part": 1501,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 1501,
  "row_count_rule": "rolling window: consecutive partitions overlap; read ONE partition, never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "Open Date",
   "type": "string",
   "nullable": true,
   "description": "lot open date",
   "example": ""
  },
  {
   "name": "Trade Date",
   "type": "string",
   "nullable": true,
   "description": "trade date",
   "example": ""
  },
  {
   "name": "Relationship ID",
   "type": "string",
   "nullable": true,
   "description": "BD relationship (household) id (z09...)",
   "example": "z09********"
  },
  {
   "name": "Account Number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number (mostly 9-digit Fidelity)",
   "example": "****1234"
  },
  {
   "name": "AccountID",
   "type": "string",
   "nullable": true,
   "description": "BD internal account id (z09 + digits); unique per account",
   "example": "z09********"
  },
  {
   "name": "Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Security Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Ticker",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "CUSIP",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Units",
   "type": "double",
   "nullable": true,
   "description": "units / shares",
   "example": ""
  },
  {
   "name": "Cost Basis",
   "type": "double",
   "nullable": true,
   "description": "cost basis",
   "example": ""
  },
  {
   "name": "Proceeds",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Short-Term Gain/Loss",
   "type": "double",
   "nullable": true,
   "description": "ST gain",
   "example": ""
  },
  {
   "name": "Long-Term Gain/Loss",
   "type": "double",
   "nullable": true,
   "description": "LT gain",
   "example": ""
  },
  {
   "name": "Total Gain Loss",
   "type": "double",
   "nullable": true,
   "description": "total gain",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "bronze xlsx key",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "report as-of date (= partition)",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "feed family",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "silver schema version",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (122 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "Security Type": {
   "n_distinct": 1,
   "values_top": [
    "MUTUAL FUNDS-BONDS"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account Number",
   "last4_derivation": "last 4 alphanumerics of Account Number (custodian number); AccountID last-4 is NOT usable",
   "last4_collisions_within_firm": 0,
   "measured_on": "Account Number, newest partition date=2026-10-14/data.parquet: 310 distinct accounts -> 310 distinct last-4; 0 last-4 values shared by 2+ accounts, covering 0 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "realized gains",
  "closed lots",
  "tax"
 ],
 "common_queries": [
  "What gains did account ...1234 realize in the last two weeks?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_list_realized",
   "inputs": {
    "firm": "cottonwood|49financial",
    "account_last4": "1234",
    "platform": "",
    "as_of": "YYYY-MM-DD (the window ends there)"
   },
   "returns": "realized lots in the partition's window with proceeds, cost basis, ST/LT gain; the window bounds are returned",
   "answers": [
    "What gains did account ...1234 realize in the last two weeks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "window length is ~2 weeks: a year-to-date realized answer is NOT available from one partition (needs a stitched history not built)"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_realized/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_transactions/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_transactions",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_transactions/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_transactions",
 "grain": "one row per transaction (TransactionID) ; the partition holds a trailing trade-date window (newest: 2026-09-27..2026-10-13; 12,755 of 12,905 TransactionIDs repeat in the prior partition; 79 in-partition repeats)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:20Z",
  "claim": "measured"
 },
 "size": {
  "objects": 124,
  "bytes": 52996926,
  "parquet_parts": 124,
  "schema_variants": 1,
  "rows_all_parts": 1086772,
  "rows_newest_part": 12984,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 12984,
  "row_count_rule": "rolling window: de-dup on TransactionID, read the newest partition covering the asked range; never sum across partitions",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "TransactionID",
   "type": "int64",
   "nullable": true,
   "description": "BD transaction id",
   "example": ""
  },
  {
   "name": "Units",
   "type": "double",
   "nullable": true,
   "description": "units / shares",
   "example": ""
  },
  {
   "name": "Market Value",
   "type": "double",
   "nullable": true,
   "description": "market value",
   "example": ""
  },
  {
   "name": "Transaction Fee",
   "type": "double",
   "nullable": true,
   "description": "trade fee",
   "example": ""
  },
  {
   "name": "Income",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Fee",
   "type": "double",
   "nullable": true,
   "description": "advisory fee amount",
   "example": ""
  },
  {
   "name": "Return Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Action",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Transaction Type",
   "type": "string",
   "nullable": true,
   "description": "Buy, Sale, Dividend, Management Fee, ...",
   "example": ""
  },
  {
   "name": "Transaction Sub Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "External Flow",
   "type": "string",
   "nullable": true,
   "description": "None / Contribution / Withdrawal",
   "example": ""
  },
  {
   "name": "Backdated Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "User Notes",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Internal Notes",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Entry Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Settle Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Description",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Price",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Trade Date",
   "type": "string",
   "nullable": true,
   "description": "trade date",
   "example": ""
  },
  {
   "name": "Has Contra Account",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Contra Account Number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "Contra Account Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Relationship ID",
   "type": "string",
   "nullable": true,
   "description": "BD relationship (household) id (z09...)",
   "example": "z09********"
  },
  {
   "name": "Relationship Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Relationship Display Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Relationship Inception Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Relationship Termination Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Portfolio Strategy ID",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Portfolio Strategy Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "PortfolioID",
   "type": "string",
   "nullable": true,
   "description": "BD portfolio id",
   "example": ""
  },
  {
   "name": "Portfolio Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number (mostly 9-digit Fidelity)",
   "example": "****1234"
  },
  {
   "name": "AccountID",
   "type": "string",
   "nullable": true,
   "description": "BD internal account id (z09 + digits); unique per account",
   "example": "z09********"
  },
  {
   "name": "Original Account Number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "****1234"
  },
  {
   "name": "Account Display Number",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Account Display Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "DST Rep Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Custodian",
   "type": "string",
   "nullable": true,
   "description": "custodian / data feed name",
   "example": ""
  },
  {
   "name": "Account Owner Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Owner",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Account Category",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Account Subcategory",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Tax Status",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Tax Lot Methodology",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Client Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client Street Address",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client City",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client State",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "Client Zip Code",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "AssetID",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Asset Display Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Original Asset Name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Last Dividend",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Symbol",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Ticker",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "CUSIP",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Bond Duration",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Coupon Rate",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Expense Ratio",
   "type": "double",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Issue Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Share Class Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Call Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Called Date",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Tax Status__2",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "SEC Asset Type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "Cash Equivalent",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "bronze xlsx key",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "report as-of date (= partition)",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "feed family",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "silver schema version",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (124 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "Custodian": {
   "n_distinct": 26,
   "values_top": [
    "Fidelity IWS",
    "Voya Financial - Participant Retirement",
    "Schwab",
    "Bank of America",
    "American Express Credit Card",
    "American Funds",
    "Transamerica",
    "Empower Retirement - Your Retirement Plan - Participant",
    "Capital One",
    "Fidelity Investments"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "Transaction Type": {
   "n_distinct": 13,
   "values_top": [
    "Dividend",
    "Buy",
    "Sale",
    "Dividend Reinvestment",
    "Management Fee",
    "Interest",
    "Cash Deposit",
    "Cash Withdrawal",
    "Expense",
    "Journal"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "Action": {
   "n_distinct": 58,
   "values_top": [
    "Dividend",
    "Sale",
    "Buy Money Market ",
    "Dividend Reinvestment",
    "Buy",
    "Management Fee",
    "Corporate/Government Bond Interest",
    "Cash Deposit",
    "Cash Withdrawal",
    "ADR tax/fee"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "External Flow": {
   "n_distinct": 3,
   "values_top": [
    "None",
    "Withdrawal",
    "Contribution"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "Account Number",
   "last4_derivation": "last 4 alphanumerics of Account Number (custodian number); AccountID last-4 is NOT usable",
   "last4_collisions_within_firm": 22,
   "measured_on": "Account Number, newest partition date=2026-10-14/data.parquet: 819 distinct accounts -> 808 distinct last-4; 11 last-4 values shared by 2+ accounts, covering 22 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "Custodian",
   "values": [
    "Fidelity IWS",
    "Alternative Investment",
    "Investor Manual Accounts",
    "Schwab",
    "Bank of America",
    "..."
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "transactions",
  "trades",
  "dividends",
  "contributions",
  "withdrawals",
  "fees charged",
  "cash flows"
 ],
 "common_queries": [
  "What trades did account ...1234 make this month?",
  "What contributions or withdrawals hit account ...1234?",
  "What management fees were charged to account ...1234?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_list_transactions",
   "inputs": {
    "firm": "cottonwood|49financial",
    "account_last4": "1234",
    "platform": "optional Custodian",
    "as_of": "YYYY-MM-DD",
    "date_from": "YYYY-MM-DD",
    "date_to": "YYYY-MM-DD",
    "transaction_type": "optional"
   },
   "returns": "transactions de-duplicated on TransactionID with type, action, trade/settle dates, units, price, market value, fees, external flow; capped rows + window bounds",
   "answers": [
    "What trades did account ...1234 make this month?",
    "What contributions or withdrawals hit account ...1234?"
   ]
  },
  {
   "name": "blackdiamond_list_fees (extend)",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "",
    "as_of": ""
   },
   "returns": "Transaction Type = Management Fee rows + Account Fee",
   "answers": [
    "What management fees were charged to account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "holds Client Name / Client Street Address / City / State / Zip columns: a tool must project them out",
  "window: history before ~3 weeks back needs older partitions (each a window)"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_transactions/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_allocations_s2/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_allocations_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_allocations_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_allocations_s2",
 "grain": "one row per report-header line of the xlsx (5 rows: Created (Eastern), Template Name, Start Date, End Date, Date Range) as c1 label / c2 value",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:06Z",
  "claim": "measured"
 },
 "size": {
  "objects": 144,
  "bytes": 668326,
  "parquet_parts": 144,
  "schema_variants": 1,
  "rows_all_parts": 797,
  "rows_newest_part": 5,
  "newest_part": "date=2026-10-13/data.parquet",
  "rows_sampled": 0,
  "row_count_rule": "5 rows per partition; metadata only",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "c1",
   "type": "string",
   "nullable": true,
   "description": "header label",
   "example": ""
  },
  {
   "name": "c2",
   "type": "string",
   "nullable": true,
   "description": "header value (date or template name)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (144 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent: no account column",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "report header",
  "export window"
 ],
 "common_queries": [
  "What date range did the allocations export cover?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "section-2 (header) sheet of the export: use it to state the window of the main table, not as a tool of its own"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_allocations_s2/date=2026-10-13/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_holdings_s2/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_holdings_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_holdings_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_holdings_s2",
 "grain": "one row per report-header line of the xlsx (5 rows: Created (Eastern), Template Name, Start Date, End Date, Date Range) as c1 label / c2 value",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:04Z",
  "claim": "measured"
 },
 "size": {
  "objects": 93,
  "bytes": 426451,
  "parquet_parts": 93,
  "schema_variants": 1,
  "rows_all_parts": 493,
  "rows_newest_part": 5,
  "newest_part": "date=2026-10-13/data.parquet",
  "rows_sampled": 0,
  "row_count_rule": "5 rows per partition; metadata only",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "c1",
   "type": "string",
   "nullable": true,
   "description": "header label",
   "example": ""
  },
  {
   "name": "c2",
   "type": "string",
   "nullable": true,
   "description": "header value (date or template name)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (93 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent: no account column",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "report header",
  "export window"
 ],
 "common_queries": [
  "What date range did the holdings export cover?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "section-2 (header) sheet of the export: use it to state the window of the main table, not as a tool of its own"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_holdings_s2/date=2026-10-13/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_unrealized_s2/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_unrealized_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_unrealized_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_unrealized_s2",
 "grain": "one row per report-header line of the xlsx (5 rows: Created (Eastern), Template Name, Start Date, End Date, Date Range) as c1 label / c2 value",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:08Z",
  "claim": "measured"
 },
 "size": {
  "objects": 144,
  "bytes": 665081,
  "parquet_parts": 144,
  "schema_variants": 1,
  "rows_all_parts": 797,
  "rows_newest_part": 5,
  "newest_part": "date=2026-10-13/data.parquet",
  "rows_sampled": 0,
  "row_count_rule": "5 rows per partition; metadata only",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "c1",
   "type": "string",
   "nullable": true,
   "description": "header label",
   "example": ""
  },
  {
   "name": "c2",
   "type": "string",
   "nullable": true,
   "description": "header value (date or template name)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (144 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent: no account column",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "report header",
  "export window"
 ],
 "common_queries": [
  "What date range did the unrealized export cover?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "section-2 (header) sheet of the export: use it to state the window of the main table, not as a tool of its own"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_unrealized_s2/date=2026-10-13/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_realized_s2/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_realized_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_realized_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_realized_s2",
 "grain": "one row per report-header line of the xlsx (5 rows: Created (Eastern), Template Name, Start Date, End Date, Date Range) as c1 label / c2 value",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:01Z",
  "claim": "measured"
 },
 "size": {
  "objects": 122,
  "bytes": 559302,
  "parquet_parts": 122,
  "schema_variants": 1,
  "rows_all_parts": 646,
  "rows_newest_part": 5,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 0,
  "row_count_rule": "5 rows per partition; metadata only",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "c1",
   "type": "string",
   "nullable": true,
   "description": "header label",
   "example": ""
  },
  {
   "name": "c2",
   "type": "string",
   "nullable": true,
   "description": "header value (date or template name)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (122 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent: no account column",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "report header",
  "export window"
 ],
 "common_queries": [
  "What date range did the realized export cover?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "section-2 (header) sheet of the export: use it to state the window of the main table, not as a tool of its own"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_realized_s2/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_transactions_s2/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_transactions_s2",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_transactions_s2/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_transactions_s2",
 "grain": "one row per report-header line of the xlsx (5 rows: Created (Eastern), Template Name, Start Date, End Date, Date Range) as c1 label / c2 value",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (Lambda, mirror_conversion.py + mirror_schemas.py)",
  "schedule": "S3 ObjectCreated on blackdiamond/cottonwood/bronze/ suffix .xlsx (bronze landed by opal-assets-ingest-mirror, Scheduler opal-assets-ingest-mirror-cot-daily-et cron(45 7 * * ? *) America/New_York) + rule opal-assets-silver-blackdiamond-sweep-daily cron(0 13 * * ? *) ENABLED",
  "claim": "measured (rules, schedule, Lambda config); trigger wiring from infra/aws/terraform/opal-assets/silver.tf:247,284"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:46:20Z",
  "claim": "measured"
 },
 "size": {
  "objects": 124,
  "bytes": 574018,
  "parquet_parts": 124,
  "schema_variants": 1,
  "rows_all_parts": 658,
  "rows_newest_part": 5,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 0,
  "row_count_rule": "5 rows per partition; metadata only",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "c1",
   "type": "string",
   "nullable": true,
   "description": "header label",
   "example": ""
  },
  {
   "name": "c2",
   "type": "string",
   "nullable": true,
   "description": "header value (date or template name)",
   "example": ""
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (124 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent: no account column",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "report header",
  "export window"
 ],
 "common_queries": [
  "What date range did the transactions export cover?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [
  "section-2 (header) sheet of the export: use it to state the window of the main table, not as a tool of its own"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_transactions_s2/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_model_assignment/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_model_assignment",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_model_assignment/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_model_assignment",
 "grain": "one row per rebalancer account per pull date (995 rows, 0 duplicate account_id) with its assigned strategy",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (rebalancer_conversion.py) over blackdiamond/cottonwood/bronze/rebalancer_{models,model_detail,accounts}/ written by cot-rebalancer-runner",
  "schedule": "cot-rebalancer-runner: rule cot-rebalancer-runner-daily cron(45 12 * * ? *) ENABLED, rule cot-bronze-complete (event), Scheduler cot-bd-session-daily-et cron(30 7 * * ? *) America/New_York -> cot-bd-session-trigger; bronze lands ~11:32Z (07:32 ET), so the session chain is the live path (inferred)",
  "claim": "measured (rules) / inferred (which path fired)"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:32:37Z",
  "claim": "measured"
 },
 "size": {
  "objects": 75,
  "bytes": 3710242,
  "parquet_parts": 75,
  "schema_variants": 1,
  "rows_all_parts": 71125,
  "rows_newest_part": 995,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 995,
  "row_count_rule": "full snapshot per date",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "account_id",
   "type": "string",
   "nullable": true,
   "description": "BD rebalancer account id (8 digits)",
   "example": "z08********"
  },
  {
   "name": "external_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<external id>"
  },
  {
   "name": "account_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": "<client data: redacted>"
  },
  {
   "name": "account_number",
   "type": "string",
   "nullable": true,
   "description": "custodian account number",
   "example": "****1234"
  },
  {
   "name": "strategy_name",
   "type": "string",
   "nullable": true,
   "description": "assigned strategy (model) name",
   "example": ""
  },
  {
   "name": "program_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "tax_status",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "custodian_id",
   "type": "int64",
   "nullable": true,
   "description": "0 on every row (not populated)",
   "example": ""
  },
  {
   "name": "allow_sma",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_sma",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_rebalancer_uma",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_uma_sleeve_account",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_system_sleeve",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "exclude",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "can_rebalance",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_closed",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "discretionary",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_managed",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_in_rebalance_group",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "user_can_view_restricted_plan_team",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (75 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "custodian_id": {
   "n_distinct": 1,
   "values_top": [
    "0"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "account_type": {
   "n_distinct": 1,
   "values_top": [
    "Rebalancer"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "tax_status": {
   "n_distinct": 3,
   "values_top": [
    "Taxable",
    "TaxDeferred",
    "NonTaxable"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "is_closed": {
   "n_distinct": 1,
   "values_top": [
    "False"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "account_number",
   "last4_derivation": "last 4 alphanumerics of account_number (custodian number); AccountID last-4 is NOT usable",
   "last4_collisions_within_firm": 80,
   "measured_on": "account_number, newest partition date=2026-10-14/data.parquet: 991 distinct accounts -> 927 distinct last-4; 16 last-4 values shared by 2+ accounts, covering 80 accounts",
   "claim": "measured"
  },
  "platform": {
   "column": "custodian_id",
   "values": [
    "0"
   ],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "model assignment",
  "which model is the account on",
  "rebalancer"
 ],
 "common_queries": [
  "Which model / strategy is account ...1234 assigned to?",
  "How many accounts are on strategy X?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_get_model_assignment",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "1234",
    "platform": "",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "assigned strategy, program, tax status, rebalance flags; plus the strategy's target weights joined from fact_model_definition / fact_model_blend",
   "answers": [
    "Which model / strategy is account ...1234 assigned to?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_model_assignment/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_model_definition/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_model_definition",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_model_definition/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_model_definition",
 "grain": "one row per model x security leaf (1,690 rows) with absolute and relative target weights",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (rebalancer_conversion.py) over blackdiamond/cottonwood/bronze/rebalancer_{models,model_detail,accounts}/ written by cot-rebalancer-runner",
  "schedule": "cot-rebalancer-runner: rule cot-rebalancer-runner-daily cron(45 12 * * ? *) ENABLED, rule cot-bronze-complete (event), Scheduler cot-bd-session-daily-et cron(30 7 * * ? *) America/New_York -> cot-bd-session-trigger; bronze lands ~11:32Z (07:32 ET), so the session chain is the live path (inferred)",
  "claim": "measured (rules) / inferred (which path fired)"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:32:41Z",
  "claim": "measured"
 },
 "size": {
  "objects": 75,
  "bytes": 1970416,
  "parquet_parts": 75,
  "schema_variants": 1,
  "rows_all_parts": 85520,
  "rows_newest_part": 1690,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 1690,
  "row_count_rule": "full snapshot per date",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "model_id",
   "type": "string",
   "nullable": true,
   "description": "rebalancer model GUID",
   "example": ""
  },
  {
   "name": "model_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_opal",
   "type": "bool",
   "nullable": true,
   "description": "model is an Opal model",
   "example": ""
  },
  {
   "name": "rebalance_model_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "sleeve_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "sleeve_depth",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "component_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "symbol",
   "type": "string",
   "nullable": true,
   "description": "security symbol",
   "example": ""
  },
  {
   "name": "asset_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "absolute_allocation",
   "type": "double",
   "nullable": true,
   "description": "target weight of total",
   "example": ""
  },
  {
   "name": "relative_allocation",
   "type": "double",
   "nullable": true,
   "description": "target weight within parent",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (75 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "rebalance_model_type": {
   "n_distinct": 2,
   "values_top": [
    "Strategy",
    "Model"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "is_opal": {
   "n_distinct": 2,
   "values_top": [
    "True",
    "False"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "model targets",
  "model weights",
  "model holdings"
 ],
 "common_queries": [
  "What are the target weights of model X?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "blackdiamond_get_model_targets",
   "inputs": {
    "firm": "cottonwood",
    "account_last4": "",
    "platform": "",
    "as_of": "YYYY-MM-DD",
    "model": "model name or id"
   },
   "returns": "security leaves with absolute / relative target weights and the blend tree",
   "answers": [
    "What are the target weights of model X?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_model_definition/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_model_blend/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_model_blend",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_model_blend/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_model_blend",
 "grain": "one row per model -> child-model edge (129 rows)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (rebalancer_conversion.py) over blackdiamond/cottonwood/bronze/rebalancer_{models,model_detail,accounts}/ written by cot-rebalancer-runner",
  "schedule": "cot-rebalancer-runner: rule cot-rebalancer-runner-daily cron(45 12 * * ? *) ENABLED, rule cot-bronze-complete (event), Scheduler cot-bd-session-daily-et cron(30 7 * * ? *) America/New_York -> cot-bd-session-trigger; bronze lands ~11:32Z (07:32 ET), so the session chain is the live path (inferred)",
  "claim": "measured (rules) / inferred (which path fired)"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:32:41Z",
  "claim": "measured"
 },
 "size": {
  "objects": 75,
  "bytes": 703927,
  "parquet_parts": 75,
  "schema_variants": 1,
  "rows_all_parts": 5906,
  "rows_newest_part": 129,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 129,
  "row_count_rule": "full snapshot per date",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "model_id",
   "type": "string",
   "nullable": true,
   "description": "rebalancer model GUID",
   "example": ""
  },
  {
   "name": "model_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_opal",
   "type": "bool",
   "nullable": true,
   "description": "model is an Opal model",
   "example": ""
  },
  {
   "name": "child_model_id",
   "type": "string",
   "nullable": true,
   "description": "child model in a blend",
   "example": ""
  },
  {
   "name": "child_model_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "child_rebalance_model_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "child_depth",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "absolute_allocation",
   "type": "double",
   "nullable": true,
   "description": "target weight of total",
   "example": ""
  },
  {
   "name": "relative_allocation",
   "type": "double",
   "nullable": true,
   "description": "target weight within parent",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (75 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "child_rebalance_model_type": {
   "n_distinct": 1,
   "values_top": [
    "Model"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "is_opal": {
   "n_distinct": 2,
   "values_top": [
    "False",
    "True"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "model blend",
  "strategy composition"
 ],
 "common_queries": [
  "Which models make up strategy X and in what split?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_model_blend/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

### blackdiamond/cottonwood/silver/fact_model_roster/

```json
{
 "contract_id": "opal-data-assets/silver/cottonwood/fact_model_roster",
 "bucket": "opal-data-assets",
 "s3_prefix": "blackdiamond/cottonwood/silver/fact_model_roster/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_model_roster",
 "grain": "one row per rebalancer strategy (72 rows) with account, portfolio and relationship counts",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "opal-assets-silver-blackdiamond (rebalancer_conversion.py) over blackdiamond/cottonwood/bronze/rebalancer_{models,model_detail,accounts}/ written by cot-rebalancer-runner",
  "schedule": "cot-rebalancer-runner: rule cot-rebalancer-runner-daily cron(45 12 * * ? *) ENABLED, rule cot-bronze-complete (event), Scheduler cot-bd-session-daily-et cron(30 7 * * ? *) America/New_York -> cot-bd-session-trigger; bronze lands ~11:32Z (07:32 ET), so the session chain is the live path (inferred)",
  "claim": "measured (rules) / inferred (which path fired)"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "trading_days_behind_t1": 0,
  "t1_frontier": "2026-10-13",
  "basis": "trading-day-frontier",
  "newest_last_modified_utc": "2026-10-14T11:32:37Z",
  "claim": "measured"
 },
 "size": {
  "objects": 75,
  "bytes": 1048884,
  "parquet_parts": 75,
  "schema_variants": 1,
  "rows_all_parts": 4838,
  "rows_newest_part": 72,
  "newest_part": "date=2026-10-14/data.parquet",
  "rows_sampled": 72,
  "row_count_rule": "full snapshot per date",
  "claim": "measured"
 },
 "columns": [
  {
   "name": "model_id",
   "type": "string",
   "nullable": true,
   "description": "rebalancer model GUID",
   "example": ""
  },
  {
   "name": "model_name",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_opal",
   "type": "bool",
   "nullable": true,
   "description": "model is an Opal model",
   "example": ""
  },
  {
   "name": "rebalance_model_type",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "provider",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "team",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "team_external_id",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "account_count",
   "type": "int64",
   "nullable": true,
   "description": "accounts on the model",
   "example": ""
  },
  {
   "name": "rebalance_assignment_count",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "portfolio_count",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "relationship_count",
   "type": "int64",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "is_uma_strategy",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "admin_only_model",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "aggregate_managed_accounts_only",
   "type": "bool",
   "nullable": true,
   "description": "",
   "example": ""
  },
  {
   "name": "last_update",
   "type": "string",
   "nullable": true,
   "description": "",
   "example": ""
  }
 ],
 "columns_note": "names and types are the union of every part's Parquet footer (75 parts, 1 schema variants); nullable is inferred (Parquet optional), null rates not measured",
 "enums": {
  "rebalance_model_type": {
   "n_distinct": 1,
   "values_top": [
    "Strategy"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  },
  "is_opal": {
   "n_distinct": 2,
   "values_top": [
    "False",
    "True"
   ],
   "claim": "measured",
   "scope": "newest partition date=2026-10-14/data.parquet"
  }
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "key segment blackdiamond/cottonwood/",
   "values": [
    "cottonwood"
   ],
   "claim": "measured"
  },
  "account": {
   "column": "",
   "last4_derivation": "absent",
   "last4_collisions_within_firm": null,
   "measured_on": "absent: no account column",
   "claim": "absent"
  },
  "platform": {
   "column": "",
   "values": [],
   "claim": "absent"
  }
 },
 "nl_tags": [
  "model roster",
  "list of models",
  "opal models"
 ],
 "common_queries": [
  "How many Opal strategies does Cottonwood run and how many accounts use each?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/@HEAD",
 "open_items": [],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator s3://opal-data-assets/blackdiamond/ (32 pages, 31,303 of 31,303 keys)",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "Parquet footer (range GET of the tail) of every .parquet part under the prefix",
   "at": "2026-10-14T12:58Z"
  },
  {
   "read": "projected-column read of blackdiamond/cottonwood/silver/fact_model_roster/date=2026-10-14/data.parquet",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration opal-assets-silver-blackdiamond + list-rule-names-by-target",
   "at": "2026-10-14T13:06Z"
  },
  {
   "read": "projected key-duplicate / trade-date-window reads",
   "at": "2026-10-14T13:08Z"
  }
 ]
}
```

## (e) What could not be read, and why

- **Null rates per column.** Not measured: footers were read, not column statistics. `nullable` is `true` (inferred) everywhere.
- **Account last-4 inside JSON columns.** `fact_insurance_relationshipaccountdetailsearch.accounts` is a JSON string and was not
  parsed (it is client data). Its collisions are not measured.
- **Cottonwood holdings duplicates.** 102 duplicate `(AccountID, AssetID)` rows on 2026-10-13, and 47 exact-duplicate rows in
  unrealized. The cause was not traced: it could be a multi-portfolio account, or an export defect.
- **Live 49F trigger.** The writer of `opal-data-bd silver/` was not traced. Both `bd-49f-runner-daily` (02:00Z) and
  `bd-49f-fees-runner-daily` read DISABLED, yet fees landed 2026-10-13 22:21Z, so the live trigger is another path.
- **Which Cottonwood rebalancer path fires.** Three triggers target `cot-rebalancer-runner`. The ~11:32Z bronze time points to
  the 07:30 ET session chain (inferred).
- **`ADVI_BILLING_*` and `IRPT_DASHBD_*` contracts.** Grep over `org/standards/` for blackdiamond / fact_holdings /
  fact_unrealized / dim_advisor_fee_role matched only 3 files: `MDPF_TAXSMA_DATA_CONTRACT.json`, `NAMING_LEGACY_READS.json` and
  `NAMING_SCHEMA.json`. No ADVI_BILLING contract names these tables by those tokens. The IRPT Cottonwood account dim lives at
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~161/COTTONWOOD_ACCOUNT_DIM.json` and was not diffed
  against `fact_allocations`.
- **Surprise row.** One is owed and was NOT written, because the brief limits this subagent to its part file. 4.0.0_SA_CRO~Z
  should file it on `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`:
  - `spec_asserts`: `opal-assets-bd49f-dim-convert` runs daily at 07:05Z and refreshes `blackdiamond/49f/silver/dim_*`.
  - `world_is`: OOM at 1,024 MB; newest partition 2026-09-28, 11 trading days behind; the Scheduler reads ENABLED and the
    bronze is current (2026-10-14 06:3xZ).
- **Gold tables.** Noted, not contracted (the task is SILVER only).

