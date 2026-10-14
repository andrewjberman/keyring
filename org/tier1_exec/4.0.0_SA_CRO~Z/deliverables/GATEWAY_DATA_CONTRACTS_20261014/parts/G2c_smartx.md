# G2c -- SmartX silver layer in s3://opal-data-assets/smartx/ (census part for 4.0.0_SA_CRO~Z)

Author: research subagent of 4.0.0_SA_CRO~Z, 2026-10-14. Read-only. Not committed.
Binding: `_SUBAGENT_BRIEF.md` + `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` sections 2-4.
Repo pin for every code citation: HEAD `7878037d98` (box/sitez, read 2026-10-14).
Session window for every AWS read: 2026-10-14 12:51Z -> 13:25Z.

## (a) Method

| # | read | instrument | denominator |
|---|---|---|---|
| 1 | full `smartx/` tree | boto3 `list_objects_v2` paginator, Prefix=`smartx/` | 924 pages, 923,583 of 923,583 keys, 6,279,790,464 bytes |
| 2 | top-level scopes | `list_objects_v2` Delimiter=`/` | 4 common prefixes (account, allocation, model, platform), IsTruncated=false |
| 3 | `smartx/platform/` tree | paginator | 2 pages, 1,479 of 1,479 keys |
| 4 | Parquet footers, every silver object | pyarrow `read_metadata` over S3 range reads | 1,010 of 1,010 `.parquet` objects under `*/silver/*`, 0 errors, 0 non-parquet objects in silver |
| 5 | schema variants, rows per partition | footer `num_rows` + arrow schema per object | 13 tables; 1 schema variant per table; 0 type drift |
| 6 | content reads (fork keys, grain, dups) | full read of the 2026-10-13 partition of each fact table; 2026-07-14 for the three one-shot tables | 11 of 11 fact tables at 2026-10-13; 3 of 3 one-shot tables at 2026-07-14 |
| 7 | producers | `lambda get-function-configuration` + `get-function-event-invoke-config` | 5 of 5 named SmartX functions |
| 8 | schedules | `scheduler list-schedules` + `get-schedule`; `events list-rules` + `list-targets-by-rule` (default bus) | 33 schedules scanned (3 SmartX); 155 rules scanned (1 SmartX) |
| 9 | newest conversion manifest | `get_object smartx/platform/meta/conversions/20261013/conversion_manifest.json` | 1 object (newest of 91) |
| 10 | catalog + gateway tools | native Grep `(?i)smartx` over `infra/aws/ec2/opal-gateway/app/` | 7 files hit; `DATA_CATALOG.yaml` 5 lines, none a silver row |
| 11 | gold consumers in repo | native Grep `smartx/platform/silver/\w+` over `data/**/*.py` | 21 hits in 8 files |
| 12 | trading calendar | `lib/trading_calendar.py` (hardcoded NYSE fallback, WARN printed) | T-1 frontier for 2026-10-14 = 2026-10-13 |

## (b) Prefix census (s3://opal-data-assets/smartx/, measured 2026-10-14)

Layer census: bronze and meta exist per entity; SILVER exists ONLY at `smartx/platform/silver/`; there is NO gold layer under `smartx/` (measured: 0 keys with a `/gold/` segment of 923,583).

| prefix (scope / layer / feed) | objects | bytes | newest LastModified (UTC) | entities |
|---|---|---|---|---|
| allocation/*/bronze/holdings | 908,231 | 4,517,537,391 | 2026-10-13T13:10:34Z | 10,240 allocation ids |
| account/*/bronze/allocations | 7,066 | 12,320,982 | 2026-07-14T08:58:03Z | 7,066 account ids (one-shot sweep) |
| account/*/bronze/detail | 91 | 499,311 | 2026-07-14T10:31:30Z | 91 account ids (one-shot) |
| model/*/bronze/allocation_accounts (feed 9) | 644 | 113,703,672 | 2026-10-13T13:15:36Z | 7 rmids |
| model/*/bronze/changerequests | 1,012 | 34,629,861 | 2026-10-13T13:03:22Z | 11 rmids |
| model/*/bronze/holdings | 1,012 | 5,932,065 | 2026-10-13T13:03:22Z | 11 rmids |
| model/*/bronze/model_allocations | 1,012 | 313,093,735 | 2026-10-13T13:03:22Z | 11 rmids |
| model/*/bronze/model_aum | 1,012 | 41,314,570 | 2026-10-13T13:03:24Z | 11 rmids |
| model/*/bronze/performance | 1,012 | 213,306,404 | 2026-10-13T13:03:22Z | 11 rmids |
| model/*/meta/pulls | 1,012 | 2,316,468 | 2026-10-13T13:16:40Z | 11 rmids |
| platform/bronze/access_roster | 92 | 854,762 | 2026-10-13T13:02:54Z | - |
| platform/bronze/models_summary | 89 | 464,378,853 | 2026-10-13T13:15:22Z | - |
| platform/bronze/nonzerosleeve | 1 | 394,660 | 2026-07-14T10:33:59Z | - |
| platform/meta/conversions | 91 | 202,566 | 2026-10-13T13:27:46Z | - |
| platform/meta/pulls | 196 | 112,906 | 2026-10-13T13:26:23Z | - |
| **platform/silver/fact_allocation_positions** | 92 | 293,819,996 | 2026-10-13T13:27:14Z | - |
| **platform/silver/fact_allocation_valuation** | 92 | 106,836,169 | 2026-10-13T13:27:14Z | - |
| **platform/silver/fact_allocation_account_map** | 91 | 50,012,592 | 2026-10-13T13:26:37Z | - |
| **platform/silver/fact_model_allocation_roster** | 92 | 52,910,440 | 2026-10-13T13:26:36Z | - |
| **platform/silver/fact_model_aum_daily** | 92 | 7,572,653 | 2026-10-13T13:26:36Z | - |
| **platform/silver/fact_model_holdings** | 92 | 2,348,292 | 2026-10-13T13:26:36Z | - |
| **platform/silver/fact_model_performance** | 92 | 29,635,301 | 2026-10-13T13:26:36Z | - |
| **platform/silver/fact_model_changerequests** | 92 | 6,651,226 | 2026-10-13T13:26:36Z | - |
| **platform/silver/fact_account_allocations** | 91 | 2,696,445 | 2026-10-13T13:27:46Z | - |
| **platform/silver/fact_account_detail** | 91 | 1,330,623 | 2026-10-13T13:27:46Z | - |
| **platform/silver/fact_nonzerosleeve** | 91 | 1,201,083 | 2026-10-13T13:27:46Z | - |
| platform/silver/allocation_positions (DRAFT-SUPERSEDED) | 1 | 3,050,617 | 2026-07-14T06:46:20Z | - |
| platform/silver/allocation_valuation (DRAFT-SUPERSEDED) | 1 | 1,126,821 | 2026-07-14T06:46:21Z | - |

Silver partitions: `date=YYYY-MM-DD/data.parquet`, ONE object per partition (measured: 1,010 objects, every one named `data.parquet`), one partition per CALENDAR day 2026-07-14 -> 2026-10-13 (92 of 92 calendar days present for positions; weekends included). Each partition is a FULL SNAPSHOT as of its run date (the history tables carry the full series in every partition), so a row count is the newest partition's, NEVER a sum across partitions.

## (c) Analysis

**What the tables are.** SmartX is the TAMP / model-delivery platform Opal's models run on. The daily pull
(`smartx-assets-daily-pull`, 13:02 UTC) lands per-entity bronze JSON; its on_success destination invokes the
whole-day converter `opal-assets-silver-smartx`, which writes 11 PLATFORM-SCOPE fact tables (one object per table per
day) under `smartx/platform/silver/`. Three groups:
- Client grain (per allocation = per account sleeve in a model): `fact_allocation_positions` (the atom, one row per
  allocation x ticker), `fact_allocation_valuation` (equity / long / short / cash / accruals per allocation),
  `fact_model_allocation_roster` (every allocation ever, with model, advisor firm, status, value),
  `fact_allocation_account_map` (allocation -> custodian account number; 49 Financial only).
- Model grain (no client data): `fact_model_holdings`, `fact_model_performance` (daily P&L series since 2020-06-29),
  `fact_model_aum_daily` (closing equity series since 2021-09-02), `fact_model_changerequests` (trade requests since
  2021-08-31).
- One-shot account-tier sweeps (rows ONLY in the 2026-07-14 partition, 0 rows in all 90 later partitions):
  `fact_account_allocations`, `fact_account_detail`, `fact_nonzerosleeve`.

**Fork keys (directive section 3).**
- FIRM: there is NO firm segment in the key (`smartx/platform/...` is firm-wide). The firm is a ROW attribute:
  `fact_model_allocation_roster.advisor_id` / `advisor_name` (4 firms measured: 49 Financial Group 10,165 allocations,
  Titleist Asset Management, LLC 66, Canopy Asset Management 6, Parable Wealth Partners 3; 1 advisor_id per name).
  Every client table reaches the firm by joining `allocation_id` to the roster (measured: 0 of 10,240 valuation rows
  and 0 of 123,676 position rows fail that join). `enterprise_name` is NOT the firm on the model tables (it reads
  `Opal Capital LLC` on all 4,782 aum rows: the model provider); on the one-shot account tables it reads `49 Financial
  Group`. partner_roster.json maps `advisor_name` `49 Financial Group` -> `firm_id` `49financial`; the other three firms
  have NO firm_id in the roster (open item).
- ACCOUNT: `fact_allocation_account_map.account_number` is the custodian brokerage number (7,604 of 7,628 are 8
  digits, 24 are 9 digits). `account_id` is the SmartX account UUID (1:1 with account_number, measured 0 violations
  both ways). 5,999 accounts carry 7,628 open/workingClose allocations (1 to 5 allocations per account).
  The map covers 49 Financial ONLY (7,628 of 7,628 rows join to 49 Financial; Parable's 3 open allocations have no
  map row), so for the other three firms account_last4 is ABSENT and a tool must refuse rather than guess.
- LAST-4: `right(account_number, 4)`. MEASURED within 49 Financial at 2026-10-13: 5,999 accounts -> 4,528 distinct
  last-4 values; 1,221 last-4 values shared by more than one account; 2,692 accounts sit in a collision; max 5
  accounts per last-4. Adding the model narrows it but does not remove it (720 of 6,848 firm+model+last4 groups still
  hold more than one account). **Last-4 is NOT a key here**: every lookup tool must return the candidate set (masked)
  and take an optional model / allocation disambiguator.
- PLATFORM / CUSTODIAN: platform is constant `smartx` (the key's source segment). Custodian is `custodian_name` on
  `fact_account_detail` only: `Schwab` on 91 of 91 rows (the one-shot 2026-07-14 sweep). For the daily tables the
  custodian is INFERRED as Schwab master 08242234 (`org/standards/NFRA_OPLGTW_CONTRACT.json:7` names 08242234
  "SmartX"; the 8-digit grammar matches Schwab) -- not measured per row.

**Freshness.** Newest partition 2026-10-13 on all 11 fact tables; vendor `as_of` inside the newest valuation and
positions partitions is 2026-10-13 on 10,240 of 10,240 and 123,676 of 123,676 rows; lag vs the T-1 frontier
2026-10-13 = 0 trading days. The map (feed 9) is EMPTY on weekends and holidays (27 of 91 partitions hold 0 rows: every
Sat/Sun plus 2026-09-07 Labor Day), so a weekend as_of on the map must fall back to the prior trading day. The
one-shot tables hold data at 2026-07-14 only: 64 trading days behind.

**Common questions.** What does account ...1234 hold in SmartX today and in which model? What is its market value,
cash and accruals? Which accounts are in model X, how many open / closed, total value? When was the account opened
into the model? What does model X hold today and what were its recent trades (change requests)? Model daily return and
AUM history? Which advisor firms and models exist on the platform?

**Existing gateway tools.** No gateway tool reads SmartX silver (Grep over `infra/aws/ec2/opal-gateway/app/`:
`tools.py:828` is the SmArtX fee-statement copy tool, a bronze WRITE into `advi`, not this layer;
`refs/silver_families.json` lists `smartx` only as a sweep family; `entity_resolution/disposition_contract.py`
reads the join-disposition contract, not the tables). `DATA_CATALOG.yaml` has NO `silver_datasets` row for any
SmartX table (its 5 rows are blackdiamond_fees and 4 schwab dims); its only SmartX rows are the frozen
`json/benchmarks/_smartx_model_*.json` portal objects (lines 169-210). The MDPF portal tools
(`mdpf_get_aum_metrics`, `mdpf_get_aggregate_aua`, `mdpf_get_account_distribution`) serve platinum aggregates that
gold builds partly from this silver (49F model leg per `data/mdpf/config/partner_roster.json`): verdict KEEP, they
answer firm-scope aggregates, not account-grain questions. Gold readers in repo: `data/assets/scripts/gold/runners_49f/`
(a00, a06, b04) and `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`.

**Proposed tools (all take firm; firm filter applied IN-TOOL on roster.advisor_id because the object is firm-wide).**
1. `smartx_account_lookup(firm, account_last4, platform="smartx", as_of)` -> candidate accounts (masked ****NNNN,
   SmartX account UUID, allocations with model, status, aum_value, opened date); returns ALL collisions, never picks one.
2. `smartx_allocation_by_account(firm, account_last4, platform="smartx", as_of, model=None, allocation_id=None)`
   -> per allocation: valuation envelope (all 5 basis components, gold basis NOT applied) + positions.
3. `smartx_model_assignments(firm, as_of, model=None, status=None, account_last4=None)` -> roster rows / counts /
   value per model for one firm.
4. `smartx_platform_list(as_of)` -> models (rmid, model_id, name), advisor firms (advisor_id, name, mapped firm_id or
   null), allocation counts by firm x model x status. Firm-free counts only; no account numbers.
5. `smartx_model_detail(model, as_of, view=holdings|performance|aum|changerequests, start=None, end=None)` -> the
   model-grain tables (no client data, no firm input).

## (d) Contracts

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_allocation_positions",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_allocation_positions/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_allocation_positions",
  "grain": "one row per (allocation_id, ticker) per run_date; full snapshot per partition (0 duplicate (allocation_id,ticker) in 123,676 rows at 2026-10-13)",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull (bronze allocation/{id}/bronze/holdings) -> on_success -> opal-assets-silver-smartx (silver.py POSITIONS_TABLE_NAME)", "schedule": "Scheduler smartx-assets-daily-pull-daily cron(2 13 * * ? *) UTC daily incl. weekends; converter on the pull's on_success; belt: EventBridge opal-assets-silver-smartx-sweep-daily cron(0 16 * * ? *)", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "basis": "trading-day-frontier", "lag_trading_days": 0, "vendor_as_of_in_latest": "2026-10-13 on 123,676 of 123,676 rows", "claim": "measured"},
  "size": {"objects": 92, "bytes": 293819996, "rows_latest_partition": 123676, "rows_range_across_partitions": "107,167 to 123,676", "rows_sampled": 123676, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "allocation_id", "type": "string", "nullable": true, "description": "SmartX allocation UUID (one account sleeve in one model); join key to roster/map/valuation", "example": "<uuid>"},
    {"name": "owner_id", "type": "string", "nullable": true, "description": "vendor ownerId; unique per allocation (10,240 distinct of 10,240), NOT the account_id (0 matches)", "example": "<uuid>"},
    {"name": "as_of", "type": "string", "nullable": true, "description": "vendor asOf timestamp with offset", "example": "2026-10-13T09:09:12-04:00"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "ticker", "type": "string", "nullable": true, "description": "position symbol (161 distinct at 2026-10-13)", "example": "VTI"},
    {"name": "symbol_id", "type": "string", "nullable": true, "description": "vendor symbol id", "example": "<id>"},
    {"name": "symbol_alias_id", "type": "string", "nullable": true, "description": "vendor symbol alias id", "example": "<id>"},
    {"name": "company", "type": "string", "nullable": true, "description": "security name", "example": "<security name>"},
    {"name": "asset_type", "type": "string", "nullable": true, "description": "vendor bug preserved: uniformly 'equity'; classify in gold", "example": "equity"},
    {"name": "industry", "type": "string", "nullable": true, "description": "vendor bug preserved: 'Unknown / Not Available'", "example": "Unknown / Not Available"},
    {"name": "quantity", "type": "double", "nullable": true, "description": "shares", "example": "12.5"},
    {"name": "price", "type": "double", "nullable": true, "description": "price", "example": "100.0"},
    {"name": "multiplier", "type": "double", "nullable": true, "description": "contract multiplier", "example": "1.0"},
    {"name": "market_value", "type": "double", "nullable": true, "description": "position market value", "example": "1250.0"},
    {"name": "value", "type": "double", "nullable": true, "description": "vendor value field", "example": "1250.0"},
    {"name": "last_seen_date", "type": "string", "nullable": true, "description": "vendor last-seen date", "example": "2026-10-13"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:27:00Z"}
  ],
  "enums": {"asset_type": ["equity (vendor bug, uniform)"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none in key; join allocation_id -> fact_model_allocation_roster.advisor_id/advisor_name", "values": ["49 Financial Group (123,172 rows)", "Titleist Asset Management, LLC (341)", "Canopy Asset Management (118)", "Parable Wealth Partners (45)"], "claim": "measured"},
    "account": {"column": "join allocation_id -> fact_allocation_account_map.account_number (49 Financial only)", "last4_derivation": "right(account_number,4)", "last4_collisions_within_firm": {"49financial": "1,221 shared last-4 values, 2,692 of 5,999 accounts in a collision, max 5 per last-4", "other_firms": "absent: no map rows"}, "claim": "measured"},
    "platform": {"column": "constant smartx (key source segment); custodian inferred Schwab 08242234", "values": ["smartx"], "claim": "measured (platform) / inferred (custodian)"}
  },
  "nl_tags": ["smartx holdings", "positions by account", "positions by allocation", "model sleeve holdings", "what does the account hold"],
  "common_queries": ["What does account ...1234 hold in SmartX today?", "Which tickers sit in the Opal Long Term sleeve of account ...1234?", "How many SmartX accounts hold ticker X?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [{"name": "smartx_allocation_by_account", "inputs": {"firm": "49financial", "account_last4": "1234", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "per candidate allocation: positions (ticker, quantity, price, market_value) + valuation envelope; all last-4 collisions returned masked", "answers": ["What does account ...1234 hold in SmartX today?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_allocation_positions", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/silver.py@7878037d98; data/assets/scripts/gold/investor_reporting/holdings_snapshot.py@7878037d98",
  "open_items": ["closed allocations still carry position rows (Titleist: 66 closed allocations, 0 with equity>0, 341 position rows): tool must filter on roster.status or valuation equity, decide which", "weekend partitions exist (daily pull 7 days); a tool resolving as_of should snap to the trading-day frontier"],
  "evidence": [{"read": "list_objects_v2 smartx/platform/ (1,479 keys); pyarrow footers 92 of 92; get_object smartx/platform/silver/fact_allocation_positions/date=2026-10-13/data.parquet", "at": "2026-10-14T13:00Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_allocation_valuation",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_allocation_valuation/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_allocation_valuation",
  "grain": "one row per allocation_id per run_date (0 duplicates in 10,240 at 2026-10-13); includes closed allocations; full snapshot per partition",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull -> on_success -> opal-assets-silver-smartx (VALUATION_TABLE_NAME, same bronze object as positions)", "schedule": "cron(2 13 * * ? *) UTC daily + on_success; sweep cron(0 16 * * ? *)", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "basis": "trading-day-frontier", "lag_trading_days": 0, "claim": "measured"},
  "size": {"objects": 92, "bytes": 106836169, "rows_latest_partition": 10240, "rows_sampled": 10240, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "allocation_id", "type": "string", "nullable": true, "description": "allocation UUID", "example": "<uuid>"},
    {"name": "owner_id", "type": "string", "nullable": true, "description": "vendor ownerId (per allocation)", "example": "<uuid>"},
    {"name": "as_of", "type": "string", "nullable": true, "description": "vendor asOf", "example": "2026-10-13T09:09:12-04:00"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "equity", "type": "double", "nullable": true, "description": "vendor equity (basis component)", "example": "150000.0"},
    {"name": "long_equity", "type": "double", "nullable": true, "description": "long equity (canonical GROSS basis = long_equity + cash, applied in GOLD)", "example": "145000.0"},
    {"name": "short_equity", "type": "double", "nullable": true, "description": "short equity", "example": "0.0"},
    {"name": "cash", "type": "double", "nullable": true, "description": "cash", "example": "5000.0"},
    {"name": "accrued_dividends", "type": "double", "nullable": true, "description": "accrued dividends", "example": "0.0"},
    {"name": "accrued_fees", "type": "double", "nullable": true, "description": "accrued fees", "example": "0.0"},
    {"name": "accrued_interest", "type": "double", "nullable": true, "description": "accrued interest", "example": "0.0"},
    {"name": "long_position_count", "type": "int32", "nullable": true, "description": "long positions", "example": "15"},
    {"name": "short_position_count", "type": "int32", "nullable": true, "description": "short positions", "example": "0"},
    {"name": "total_count", "type": "int32", "nullable": true, "description": "total positions", "example": "15"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:27:00Z"}
  ],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "join allocation_id -> roster.advisor_id", "values": ["49 Financial Group 10,165 rows (7,599 open)", "Titleist 66 (all close)", "Canopy 6 (all close)", "Parable 3 (open)"], "claim": "measured"},
    "account": {"column": "join allocation_id -> fact_allocation_account_map.account_number", "last4_derivation": "right(account_number,4)", "last4_collisions_within_firm": {"49financial": "1,221 shared values / 2,692 of 5,999 accounts / max 5"}, "claim": "measured"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["account market value", "smartx aum by account", "cash in account", "valuation envelope"],
  "common_queries": ["What is the market value and cash of account ...1234 in SmartX?", "What is total open SmartX equity for 49 Financial today?"],
  "existing_gateway_tool": {"name": "none (mdpf_get_aum_metrics serves the gold aggregate; keep)", "verdict": "none"},
  "proposed_tools": [{"name": "smartx_allocation_by_account", "inputs": {"firm": "49financial", "account_last4": "1234", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "valuation envelope per allocation, all five basis components, basis named not applied", "answers": ["What is the market value and cash of account ...1234 in SmartX?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_allocation_valuation", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/silver.py@7878037d98 (basis register: data/assets/docs/SMARTX_INGESTION_ARCHITECTURE.md section 7b)",
  "open_items": ["never sum equity and long_equity+cash: measured totals differ (1,450,870,272 vs 1,501,279,446 at 2026-10-13); tool must name the basis"],
  "evidence": [{"read": "get_object smartx/platform/silver/fact_allocation_valuation/date=2026-10-13/data.parquet; footers 92 of 92", "at": "2026-10-14T13:10Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_allocation_account_map",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_allocation_account_map/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_allocation_account_map",
  "grain": "one row per living (open or workingClose) allocation with its custodian account number; 49 Financial only; 0 duplicate allocation_id in 7,628",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull feed 9 (model/{rmid}/bronze/allocation_accounts, bundle credential) -> opal-assets-silver-smartx (MAP_TABLE_NAME)", "schedule": "daily pull cron(2 13 * * ? *) UTC; partitions hold 0 rows on weekends and NYSE holidays (27 of 91: every Sat/Sun + 2026-09-07)", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "basis": "trading-day-frontier", "lag_trading_days": 0, "claim": "measured"},
  "size": {"objects": 91, "bytes": 50012592, "rows_latest_partition": 7628, "rows_sampled": 7628, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "model_id", "type": "string", "nullable": true, "description": "SmartX modelId (fetch id space)", "example": "<uuid>"},
    {"name": "rmid", "type": "string", "nullable": true, "description": "reportedModelId (path id space)", "example": "<uuid>"},
    {"name": "allocation_id", "type": "string", "nullable": true, "description": "allocation UUID", "example": "<uuid>"},
    {"name": "account_id", "type": "string", "nullable": true, "description": "SmartX account UUID, 1:1 with account_number", "example": "<uuid>"},
    {"name": "account_number", "type": "string", "nullable": true, "description": "custodian brokerage account number (8 digits 7,604; 9 digits 24)", "example": "****1234"},
    {"name": "account_name", "type": "string", "nullable": true, "description": "client account name (CLIENT DATA, never returned unmasked)", "example": "<client name>"},
    {"name": "aum_value", "type": "double", "nullable": true, "description": "vendor allocation value", "example": "150000.0"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:26:00Z"}
  ],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "join allocation_id -> roster.advisor_id; measured all 7,628 rows = 49 Financial Group", "values": ["49 Financial Group"], "claim": "measured"},
    "account": {"column": "account_number", "last4_derivation": "right(account_number,4)", "last4_collisions_within_firm": {"49financial": "5,999 accounts, 4,528 distinct last-4, 1,221 shared values, 2,692 accounts in a collision, max 5; firm+model still 720 of 6,848 groups collide"}, "claim": "measured"},
    "platform": {"column": "constant smartx; custodian inferred Schwab (8-digit grammar; NFRA_OPLGTW_CONTRACT.json:7 names 08242234 SmartX)", "values": ["smartx"], "claim": "measured (platform) / inferred (custodian)"}
  },
  "nl_tags": ["account lookup", "account number to allocation", "smartx account map", "which model is account in"],
  "common_queries": ["Which SmartX allocations belong to account ...1234?", "Which accounts end in 1234 at 49 Financial?"],
  "existing_gateway_tool": {"name": "none (entity_resolution/disposition_contract.py reads the join-disposition enum only)", "verdict": "none"},
  "proposed_tools": [{"name": "smartx_account_lookup", "inputs": {"firm": "49financial", "account_last4": "1234", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "every candidate account (masked number, account UUID, allocations x model x status x aum_value); weekend as_of snaps to prior trading day", "answers": ["Which accounts end in 1234 at 49 Financial?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_allocation_account_map", "present": false},
  "prior_art": "data/_contracts/smartx_bd_join_disposition.yaml@7878037d98 (JOINED 99.74% to 49F fact_acc at 2026-08-19); data/assets/scripts/gold/runners_49f/a06_dim_identity_crosswalk.py@7878037d98",
  "open_items": ["firms other than 49 Financial have no map rows: account fork absent for Titleist/Canopy/Parable (Parable has 3 open allocations)", "weekend/holiday partitions are EMPTY, not absent: a tool must not read 0 rows as no accounts"],
  "evidence": [{"read": "get_object .../fact_allocation_account_map/date=2026-10-13/data.parquet; footers 91 of 91", "at": "2026-10-14T13:05Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_model_allocation_roster",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_model_allocation_roster/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_model_allocation_roster",
  "grain": "one row per allocation ever opened into a model (open, close, workingClose); 0 duplicate allocation_id in 10,240",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull (model/{rmid}/bronze/model_allocations) -> opal-assets-silver-smartx", "schedule": "cron(2 13 * * ? *) UTC daily + on_success", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "basis": "trading-day-frontier", "lag_trading_days": 0, "claim": "measured"},
  "size": {"objects": 92, "bytes": 52910440, "rows_latest_partition": 10240, "rows_sampled": 10240, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "model_id", "type": "string", "nullable": true, "description": "SmartX modelId", "example": "<uuid>"},
    {"name": "model_name", "type": "string", "nullable": true, "description": "model name (8 distinct)", "example": "Opal Long Term"},
    {"name": "rmid", "type": "string", "nullable": true, "description": "reportedModelId", "example": "<uuid>"},
    {"name": "allocation_id", "type": "string", "nullable": true, "description": "allocation UUID", "example": "<uuid>"},
    {"name": "advisor_id", "type": "string", "nullable": true, "description": "advisor FIRM id: THE firm fork column (4 distinct)", "example": "<uuid>"},
    {"name": "advisor_name", "type": "string", "nullable": true, "description": "advisor firm name", "example": "49 Financial Group"},
    {"name": "advisor_crd", "type": "string", "nullable": true, "description": "advisor firm CRD (0 null; 3 distinct across 4 firms, so two firms share one CRD)", "example": "<crd>"},
    {"name": "value", "type": "double", "nullable": true, "description": "allocation value", "example": "150000.0"},
    {"name": "status", "type": "string", "nullable": true, "description": "allocation status", "example": "open"},
    {"name": "opened_ts", "type": "int64", "nullable": true, "description": "open time, epoch SECONDS (range 2021-09-02 -> 2026-10-12)", "example": "1760000000"},
    {"name": "opened_date_friendly", "type": "string", "nullable": true, "description": "vendor formatted open date", "example": "10/12/2026"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:26:00Z"}
  ],
  "enums": {"status": ["open (7,602)", "close (2,609)", "workingClose (29)"], "model_name": ["Opal Long Term (4,159)", "Opal Intermediate-Term (2,333)", "Opal Ultra Long Term (2,074)", "Opal Short-Term (1,040)", "Opal Ultra Short-Term Income (440)", "Opal Dividend Income (120)", "Pathfinder Focused Opportunities (73)", "Opal Global All Equity Total Return (1)"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "advisor_id / advisor_name", "values": ["49 Financial Group (10,165)", "Titleist Asset Management, LLC (66)", "Canopy Asset Management (6)", "Parable Wealth Partners (3)"], "claim": "measured"},
    "account": {"column": "none here; join allocation_id -> fact_allocation_account_map.account_number", "last4_derivation": "right(account_number,4)", "last4_collisions_within_firm": {"49financial": "1,221 shared values / 2,692 of 5,999 accounts / max 5"}, "claim": "measured"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["model assignments", "accounts in model", "model roster", "allocation status", "advisor firms on smartx"],
  "common_queries": ["How many 49 Financial accounts are open in Opal Long Term?", "When was account ...1234 opened into its model?", "Which advisor firms use Opal models on SmartX?"],
  "existing_gateway_tool": {"name": "none (mdpf_get_account_distribution serves the gold histogram; keep)", "verdict": "none"},
  "proposed_tools": [{"name": "smartx_model_assignments", "inputs": {"firm": "49financial", "account_last4": "optional", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "allocations by model x status with counts and value for ONE firm", "answers": ["How many 49 Financial accounts are open in Opal Long Term?"]}, {"name": "smartx_platform_list", "inputs": {"firm": "not taken", "account_last4": "not taken", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "models + advisor firms + counts, no account data", "answers": ["Which advisor firms use Opal models on SmartX?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_model_allocation_roster", "present": false},
  "prior_art": "data/mdpf/config/partner_roster.json@7878037d98 (feed smartx_model_allocation_roster, 49financial model leg); data/assets/scripts/gold/runners_49f/b04_account_model_membership.py@7878037d98",
  "open_items": ["Titleist, Canopy, Parable have no firm_id in partner_roster.json: a firm input cannot name them until rows exist", "advisor_crd is shared by two of the 4 firms (3 distinct, 0 null): key the firm on advisor_id, never on CRD"],
  "evidence": [{"read": "get_object .../fact_model_allocation_roster/date=2026-10-13/data.parquet; footers 92 of 92", "at": "2026-10-14T13:05Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_model_aum_daily",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_model_aum_daily/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_model_aum_daily",
  "grain": "one row per (rmid, day) closing-equity point; full history 2021-09-02 -> 2026-10-12 in every partition; 0 duplicate (rmid,day)",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull (model/{rmid}/bronze/model_aum) -> opal-assets-silver-smartx", "schedule": "cron(2 13 * * ? *) UTC daily + on_success", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "latest_day_in_series": "2026-10-12 for 7 of 8 rmids, 2026-10-09 for 1", "basis": "trading-day-frontier", "lag_trading_days": "0 (partition); 1 (series day)", "claim": "measured"},
  "size": {"objects": 92, "bytes": 7572653, "rows_latest_partition": 4782, "rows_sampled": 4782, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "rmid", "type": "string", "nullable": true, "description": "reportedModelId (8 funded of 11; 3 unfunded = empty series, named in the conversion manifest)", "example": "<uuid>"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "enterprise_id", "type": "string", "nullable": true, "description": "model-provider enterprise id (single value)", "example": "<uuid>"},
    {"name": "enterprise_name", "type": "string", "nullable": true, "description": "model provider, NOT the advisor firm", "example": "Opal Capital LLC"},
    {"name": "total_aum", "type": "double", "nullable": true, "description": "vendor total AUM header", "example": "1500000000.0"},
    {"name": "day", "type": "date32", "nullable": true, "description": "series day", "example": "2026-10-12"},
    {"name": "performance_ts", "type": "int64", "nullable": true, "description": "epoch seconds", "example": "1760227200"},
    {"name": "performance_date_friendly", "type": "string", "nullable": true, "description": "vendor formatted date", "example": "10/12/2026"},
    {"name": "closing_equity", "type": "double", "nullable": true, "description": "model closing equity on day", "example": "839000000.0"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:26:00Z"}
  ],
  "enums": {"enterprise_name": ["Opal Capital LLC"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none: model-grain, all advisor firms aggregated by the vendor; cannot fork by firm", "values": [], "claim": "measured"},
    "account": {"column": "none (model grain, no client data)", "last4_derivation": "n/a", "last4_collisions_within_firm": "n/a", "claim": "measured"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["model aum history", "model closing equity", "smartx aum by model"],
  "common_queries": ["What was Opal Long Term's SmartX AUM on a date?", "How has model AUM moved since 2021?"],
  "existing_gateway_tool": {"name": "mdpf_get_aggregate_aua (gold, firm-scope; keep)", "verdict": "keep"},
  "proposed_tools": [{"name": "smartx_model_detail", "inputs": {"firm": "not taken (model grain)", "account_last4": "not taken", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "view=aum: (day, closing_equity) series for one model", "answers": ["What was Opal Long Term's SmartX AUM on a date?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_model_aum_daily", "present": false},
  "prior_art": "data/mdpf/config/partner_roster.json@7878037d98 (feed smartx_model_aum_daily)",
  "open_items": ["the series is cross-firm by construction (vendor model total): a firm-scoped answer must come from the roster/valuation, never from this table"],
  "evidence": [{"read": "get_object .../fact_model_aum_daily/date=2026-10-13/data.parquet; conversion_manifest 20261013 aum_named_holes", "at": "2026-10-14T13:10Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_model_holdings",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_model_holdings/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_model_holdings",
  "grain": "one row per (rmid, ticker) model target holding per run_date; 0 duplicates in 165; 11 rmids",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull (model/{rmid}/bronze/holdings) -> opal-assets-silver-smartx", "schedule": "cron(2 13 * * ? *) UTC daily + on_success", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "basis": "trading-day-frontier", "lag_trading_days": 0, "claim": "measured"},
  "size": {"objects": 92, "bytes": 2348292, "rows_latest_partition": 165, "rows_sampled": 165, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "rmid", "type": "string", "nullable": true, "description": "reportedModelId", "example": "<uuid>"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "symbol_id", "type": "string", "nullable": true, "description": "vendor symbol id", "example": "<id>"},
    {"name": "ticker", "type": "string", "nullable": true, "description": "ticker", "example": "VTI"},
    {"name": "company_name", "type": "string", "nullable": true, "description": "security name", "example": "<security name>"},
    {"name": "asset_type", "type": "string", "nullable": true, "description": "vendor bug: uniformly equity (165 of 165)", "example": "equity"},
    {"name": "industry", "type": "string", "nullable": true, "description": "vendor industry", "example": "Unknown / Not Available"},
    {"name": "default_symbol_alias_id", "type": "string", "nullable": true, "description": "vendor alias id", "example": "<id>"},
    {"name": "symbol_multiplier", "type": "double", "nullable": true, "description": "symbol multiplier", "example": "1.0"},
    {"name": "multiplier", "type": "double", "nullable": true, "description": "multiplier", "example": "1.0"},
    {"name": "quantity", "type": "double", "nullable": true, "description": "model quantity", "example": "100.0"},
    {"name": "price", "type": "double", "nullable": true, "description": "price", "example": "100.0"},
    {"name": "market_value", "type": "double", "nullable": true, "description": "model market value", "example": "10000.0"},
    {"name": "percent_of_portfolio", "type": "double", "nullable": true, "description": "weight as fraction; per-model sums 0.91 to 1.00 measured (cash remainder)", "example": "0.12"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:26:00Z"}
  ],
  "enums": {"asset_type": ["equity"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none: model grain, firm-free", "values": [], "claim": "measured"},
    "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": "n/a", "claim": "measured"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["model holdings", "model weights", "what does the model hold"],
  "common_queries": ["What does Opal Intermediate-Term hold on SmartX today, with weights?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [{"name": "smartx_model_detail", "inputs": {"firm": "not taken", "account_last4": "not taken", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "view=holdings: ticker, weight, quantity, market_value", "answers": ["What does Opal Intermediate-Term hold on SmartX today, with weights?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_model_holdings", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/silver.py@7878037d98",
  "open_items": ["11 rmids in model feeds vs 8 model names in the roster: 3 unfunded models carry holdings but no allocations"],
  "evidence": [{"read": "get_object .../fact_model_holdings/date=2026-10-13/data.parquet", "at": "2026-10-14T13:15Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_model_performance",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_model_performance/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_model_performance",
  "grain": "one row per (rmid, grouping, day); grouping=daily on 7,149 of 7,149; full history 2020-06-29 -> 2026-10-12 in every partition; 0 duplicates",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull (model/{rmid}/bronze/performance, fetched by modelId, filed by rmid) -> opal-assets-silver-smartx", "schedule": "cron(2 13 * * ? *) UTC daily + on_success", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "latest_day_in_series": "2026-10-12", "basis": "trading-day-frontier", "lag_trading_days": "0 (partition); 1 (series day)", "claim": "measured"},
  "size": {"objects": 92, "bytes": 29635301, "rows_latest_partition": 7149, "rows_sampled": 7149, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "rmid", "type": "string", "nullable": true, "description": "reportedModelId", "example": "<uuid>"},
    {"name": "model_id", "type": "string", "nullable": true, "description": "modelId (fetch id)", "example": "<uuid>"},
    {"name": "model_name", "type": "string", "nullable": true, "description": "model name (11 distinct)", "example": "Opal Long Term"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "grouping", "type": "string", "nullable": true, "description": "series grouping", "example": "daily"},
    {"name": "record_count", "type": "int64", "nullable": true, "description": "vendor envelope record count", "example": "1500"},
    {"name": "day", "type": "date32", "nullable": true, "description": "series day", "example": "2026-10-12"},
    {"name": "range_start_ts", "type": "int64", "nullable": true, "description": "epoch seconds", "example": "1760227200"},
    {"name": "range_start_friendly", "type": "string", "nullable": true, "description": "vendor date", "example": "10/12/2026"},
    {"name": "range_end_ts", "type": "int64", "nullable": true, "description": "epoch seconds", "example": "1760313600"},
    {"name": "range_end_friendly", "type": "string", "nullable": true, "description": "vendor date", "example": "10/13/2026"},
    {"name": "pnl_dollar", "type": "double", "nullable": true, "description": "daily P&L dollars", "example": "12345.0"},
    {"name": "pnl_percent", "type": "double", "nullable": true, "description": "daily return", "example": "0.0012"},
    {"name": "summary_beginning_market_value", "type": "double", "nullable": true, "description": "envelope summary", "example": "100.0"},
    {"name": "summary_ending_market_value", "type": "double", "nullable": true, "description": "envelope summary", "example": "100.0"},
    {"name": "summary_increase_by_amount", "type": "double", "nullable": true, "description": "envelope summary", "example": "0.0"},
    {"name": "summary_decrease_by_amount", "type": "double", "nullable": true, "description": "envelope summary", "example": "0.0"},
    {"name": "summary_fees", "type": "double", "nullable": true, "description": "envelope summary", "example": "0.0"},
    {"name": "summary_transactions", "type": "double", "nullable": true, "description": "envelope summary", "example": "0.0"},
    {"name": "summary_is_full_range", "type": "bool", "nullable": true, "description": "envelope flag", "example": "true"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:26:00Z"}
  ],
  "enums": {"grouping": ["daily"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none: model grain, firm-free", "values": [], "claim": "measured"},
    "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": "n/a", "claim": "measured"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["model performance", "model daily return", "vendor-reported model return"],
  "common_queries": ["What was Opal Short-Term's SmartX daily return last week?", "Cumulative SmartX-reported return of a model since a date?"],
  "existing_gateway_tool": {"name": "mdpf_get_model_benchmarks (gold; keep)", "verdict": "keep"},
  "proposed_tools": [{"name": "smartx_model_detail", "inputs": {"firm": "not taken", "account_last4": "not taken", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "view=performance: (day, pnl_percent, pnl_dollar) over [start,end]", "answers": ["What was Opal Short-Term's SmartX daily return last week?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_model_performance (portal json/benchmarks/_smartx_model_daily.json is the frozen 2026-05 operator-run sibling, DATA_CATALOG.yaml:169)", "present": false},
  "prior_art": "infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml:169-210@7878037d98",
  "open_items": ["this live daily series could replace the frozen _smartx_model_daily.json portal object (frozen at as_of 2026-05-29): flag for G3/OPLGTW"],
  "evidence": [{"read": "get_object .../fact_model_performance/date=2026-10-13/data.parquet", "at": "2026-10-14T13:10Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_model_changerequests",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_model_changerequests/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_model_changerequests",
  "grain": "one row per model trade request line (ledger; NO natural key asserted by the producer; 0 full-row duplicates in 1,140); history 2021-08-31 -> 2026-10-08 in every partition",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "smartx-assets-daily-pull (model/{rmid}/bronze/changerequests) -> opal-assets-silver-smartx", "schedule": "cron(2 13 * * ? *) UTC daily + on_success", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13", "latest_trade": "2026-10-08T13:18:02Z", "basis": "trading-day-frontier", "lag_trading_days": 0, "claim": "measured"},
  "size": {"objects": 92, "bytes": 6651226, "rows_latest_partition": 1140, "rows_sampled": 1140, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "rmid", "type": "string", "nullable": true, "description": "reportedModelId", "example": "<uuid>"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "pull run date", "example": "2026-10-13"},
    {"name": "activity", "type": "string", "nullable": true, "description": "buy or sell", "example": "buy"},
    {"name": "ticker", "type": "string", "nullable": true, "description": "ticker", "example": "VTI"},
    {"name": "company", "type": "string", "nullable": true, "description": "security name", "example": "<security name>"},
    {"name": "quantity", "type": "double", "nullable": true, "description": "quantity", "example": "10.0"},
    {"name": "price", "type": "double", "nullable": true, "description": "price", "example": "100.0"},
    {"name": "percentage", "type": "double", "nullable": true, "description": "weight change", "example": "0.02"},
    {"name": "from_quantity", "type": "double", "nullable": true, "description": "before quantity", "example": "0.0"},
    {"name": "from_percent", "type": "double", "nullable": true, "description": "before weight", "example": "0.0"},
    {"name": "to_quantity", "type": "double", "nullable": true, "description": "after quantity", "example": "10.0"},
    {"name": "to_percent", "type": "double", "nullable": true, "description": "after weight", "example": "0.02"},
    {"name": "requested_by", "type": "string", "nullable": true, "description": "requesting user (staff name; mask in tools)", "example": "<user>"},
    {"name": "trade_ts", "type": "int64", "nullable": true, "description": "epoch SECONDS", "example": "1759929482"},
    {"name": "trade_friendly", "type": "string", "nullable": true, "description": "vendor MM/DD/YYYY HH:MM:SS (do not string-sort)", "example": "10/08/2026 09:18:02"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "2026-10-13T13:26:00Z"}
  ],
  "enums": {"activity": ["buy (680)", "sell (460)"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none: model grain, firm-free", "values": [], "claim": "measured"},
    "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": "n/a", "claim": "measured"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["model trades", "model rebalance history", "change requests"],
  "common_queries": ["What trades did Opal Long Term make in its last rebalance?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [{"name": "smartx_model_detail", "inputs": {"firm": "not taken", "account_last4": "not taken", "platform": "smartx", "as_of": "YYYY-MM-DD"}, "returns": "view=changerequests: trades by trade_ts in [start,end]", "answers": ["What trades did Opal Long Term make in its last rebalance?"]}],
  "catalog_entry": {"data_catalog_key": "silver_datasets: smartx_fact_model_changerequests", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/silver.py@7878037d98",
  "open_items": [],
  "evidence": [{"read": "get_object .../fact_model_changerequests/date=2026-10-13/data.parquet", "at": "2026-10-14T13:20Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_account_allocations",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_account_allocations/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_account_allocations",
  "grain": "one row per allocation per filing account from the one-shot account-side sweep (open + closed identity history); 0 duplicate allocation_id in 23,213",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "one-shot bundle-credentialed sweep (account/{id}/bronze/allocations, 7,066 objects all 2026-07-14) -> opal-assets-silver-smartx", "schedule": "NONE recurring: rows only in date=2026-07-14; 90 of 91 partitions hold 0 rows", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-13 (empty)", "latest_partition_with_rows": "2026-07-14", "basis": "trading-day-frontier", "lag_trading_days": 64, "claim": "measured"},
  "size": {"objects": 91, "bytes": 2696445, "rows_latest_partition": 0, "rows_2026_07_14": 23213, "rows_sampled": 23213, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "filing_account_id", "type": "string", "nullable": true, "description": "account UUID the bronze was filed under", "example": "<uuid>"},
    {"name": "allocation_id", "type": "string", "nullable": true, "description": "allocation UUID", "example": "<uuid>"},
    {"name": "account_id", "type": "string", "nullable": true, "description": "account UUID", "example": "<uuid>"},
    {"name": "account_name", "type": "string", "nullable": true, "description": "CLIENT DATA", "example": "<client name>"},
    {"name": "advisor_id", "type": "string", "nullable": true, "description": "advisor firm id", "example": "<uuid>"},
    {"name": "advisor_name", "type": "string", "nullable": true, "description": "advisor firm", "example": "49 Financial Group"},
    {"name": "advisor_crd", "type": "string", "nullable": true, "description": "firm CRD", "example": "<crd>"},
    {"name": "model_id", "type": "string", "nullable": true, "description": "modelId", "example": "<uuid>"},
    {"name": "model_name", "type": "string", "nullable": true, "description": "model", "example": "Opal Long Term"},
    {"name": "status", "type": "string", "nullable": true, "description": "open/close", "example": "open"},
    {"name": "type", "type": "string", "nullable": true, "description": "allocation type", "example": "<type>"},
    {"name": "trading_type", "type": "string", "nullable": true, "description": "trading type", "example": "<type>"},
    {"name": "is_apm_allocation", "type": "bool", "nullable": true, "description": "APM flag", "example": "false"},
    {"name": "match_model_leverage", "type": "bool", "nullable": true, "description": "leverage flag", "example": "false"},
    {"name": "leverage", "type": "double", "nullable": true, "description": "leverage", "example": "1.0"},
    {"name": "open_ts", "type": "int64", "nullable": true, "description": "epoch seconds", "example": "1700000000"},
    {"name": "open_friendly", "type": "string", "nullable": true, "description": "vendor date", "example": "<date>"},
    {"name": "close_ts", "type": "int64", "nullable": true, "description": "epoch seconds", "example": "1700000000"},
    {"name": "close_friendly", "type": "string", "nullable": true, "description": "vendor date", "example": "<date>"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "run date", "example": "2026-07-14"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "<ts>"}
  ],
  "enums": {"status": ["open (21,427)", "close (1,786)"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "advisor_id / advisor_name", "values": ["49 Financial Group (23,213 of 23,213)"], "claim": "measured"},
    "account": {"column": "account_id (UUID); number via fact_allocation_account_map or fact_account_detail", "last4_derivation": "right(account_number,4) after join", "last4_collisions_within_firm": "not measured on this snapshot (see map)", "claim": "inferred"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["closed allocation history", "account allocation history"],
  "common_queries": ["Which models has account ...1234 ever been in, including closed?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/key_mapping.py ACCOUNT_TIER_ACCOUNT_FEEDS@7878037d98",
  "open_items": ["one-shot 2026-07-14 snapshot, 64 trading days behind: no tool until a recurring producer exists; the daily roster carries closed rows instead", "converter writes an EMPTY partition every day: an empty partition must not read as no allocations"],
  "evidence": [{"read": "footers 91 of 91; get_object .../fact_account_allocations/date=2026-07-14/data.parquet", "at": "2026-10-14T13:05Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_account_detail",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_account_detail/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_account_detail",
  "grain": "one row per account from the one-shot account-detail enrichment (91 roster-invisible accounts)",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "one-shot bundle sweep (account/{id}/bronze/detail, 91 objects 2026-07-14) -> opal-assets-silver-smartx", "schedule": "NONE recurring: rows only in date=2026-07-14", "claim": "measured"},
  "freshness": {"latest_partition_with_rows": "2026-07-14", "basis": "trading-day-frontier", "lag_trading_days": 64, "claim": "measured"},
  "size": {"objects": 91, "bytes": 1330623, "rows_latest_partition": 0, "rows_2026_07_14": 91, "rows_sampled": 91, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "account_id", "type": "string", "nullable": true, "description": "account UUID", "example": "<uuid>"},
    {"name": "name", "type": "string", "nullable": true, "description": "CLIENT DATA", "example": "<client name>"},
    {"name": "account_title", "type": "string", "nullable": true, "description": "CLIENT DATA", "example": "<client name>"},
    {"name": "account_type", "type": "string", "nullable": true, "description": "registration type", "example": "individual"},
    {"name": "internal_type", "type": "string", "nullable": true, "description": "vendor internal type", "example": "<type>"},
    {"name": "status", "type": "string", "nullable": true, "description": "account status", "example": "<status>"},
    {"name": "access_level", "type": "string", "nullable": true, "description": "", "example": "<level>"},
    {"name": "permission", "type": "string", "nullable": true, "description": "", "example": "view"},
    {"name": "margin_type", "type": "string", "nullable": true, "description": "", "example": "<type>"},
    {"name": "option_level", "type": "string", "nullable": true, "description": "", "example": "<level>"},
    {"name": "brokerage_account_number", "type": "string", "nullable": true, "description": "custodian account number (8 digits, 91 of 91)", "example": "****1234"},
    {"name": "has_rep_code", "type": "bool", "nullable": true, "description": "", "example": "true"},
    {"name": "rep_code_json", "type": "string", "nullable": true, "description": "json", "example": "<json>"},
    {"name": "feature_json", "type": "string", "nullable": true, "description": "json", "example": "<json>"},
    {"name": "enterprise_id", "type": "string", "nullable": true, "description": "advisor firm enterprise id", "example": "<uuid>"},
    {"name": "enterprise_name", "type": "string", "nullable": true, "description": "advisor firm", "example": "49 Financial Group"},
    {"name": "custodian_id", "type": "string", "nullable": true, "description": "custodian id", "example": "<id>"},
    {"name": "custodian_name", "type": "string", "nullable": true, "description": "THE custodian column (only here)", "example": "Schwab"},
    {"name": "created_ts", "type": "int64", "nullable": true, "description": "epoch seconds", "example": "1700000000"},
    {"name": "created_friendly", "type": "string", "nullable": true, "description": "vendor date", "example": "<date>"},
    {"name": "target_weight_id", "type": "string", "nullable": true, "description": "", "example": "<id>"},
    {"name": "should_rebalance", "type": "bool", "nullable": true, "description": "", "example": "true"},
    {"name": "is_apm", "type": "bool", "nullable": true, "description": "", "example": "false"},
    {"name": "is_blacklisted", "type": "bool", "nullable": true, "description": "", "example": "false"},
    {"name": "is_demo", "type": "bool", "nullable": true, "description": "", "example": "false"},
    {"name": "is_excluded", "type": "bool", "nullable": true, "description": "", "example": "false"},
    {"name": "is_trading", "type": "bool", "nullable": true, "description": "", "example": "true"},
    {"name": "equity_dividend_reinvest", "type": "bool", "nullable": true, "description": "", "example": "false"},
    {"name": "mutual_fund_dividend_reinvest", "type": "bool", "nullable": true, "description": "", "example": "false"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "run date", "example": "2026-07-14"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "<ts>"}
  ],
  "enums": {"custodian_name": ["Schwab (91)"], "account_type": ["individual (35)", "joint (25)", "ira (17)", "iraSepRollover (6)", "iraRoth (6)", "other (2)"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "enterprise_name / enterprise_id", "values": ["49 Financial Group (91 of 91)"], "claim": "measured"},
    "account": {"column": "brokerage_account_number", "last4_derivation": "right(brokerage_account_number,4)", "last4_collisions_within_firm": "not measured on 91 rows", "claim": "inferred"},
    "platform": {"column": "custodian_name", "values": ["Schwab"], "claim": "measured"}
  },
  "nl_tags": ["account registration type", "custodian"],
  "common_queries": ["Which custodian holds SmartX account ...1234?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/key_mapping.py ACCOUNT_TIER_ACCOUNT_FEEDS detail@7878037d98",
  "open_items": ["one-shot 91-account enrichment, 64 trading days behind: no tool; the custodian column is not on any daily table"],
  "evidence": [{"read": "get_object .../fact_account_detail/date=2026-07-14/data.parquet", "at": "2026-10-14T13:05Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_fact_nonzerosleeve",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/fact_nonzerosleeve/",
  "layer": "silver",
  "format": "parquet",
  "table": "fact_nonzerosleeve",
  "grain": "one row per non-zero sleeve (account x allocation) with opening/closing valuation envelope, one-shot",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "one-shot bundle pull platform/bronze/nonzerosleeve (1 object 2026-07-14) -> opal-assets-silver-smartx", "schedule": "NONE recurring: rows only in date=2026-07-14", "claim": "measured"},
  "freshness": {"latest_partition_with_rows": "2026-07-14", "basis": "trading-day-frontier", "lag_trading_days": 64, "claim": "measured"},
  "size": {"objects": 91, "bytes": 1201083, "rows_latest_partition": 0, "rows_2026_07_14": 511, "rows_sampled": 511, "schema_variants": 1, "claim": "measured"},
  "columns": [
    {"name": "sleeve_id", "type": "string", "nullable": true, "description": "sleeve id", "example": "<uuid>"},
    {"name": "allocation_id", "type": "string", "nullable": true, "description": "allocation UUID", "example": "<uuid>"},
    {"name": "account_id", "type": "string", "nullable": true, "description": "account UUID", "example": "<uuid>"},
    {"name": "account_name", "type": "string", "nullable": true, "description": "CLIENT DATA", "example": "<client name>"},
    {"name": "brokerage_acct_num", "type": "string", "nullable": true, "description": "custodian number (8 digits 510, 9 digits 1)", "example": "****1234"},
    {"name": "enterprise_id", "type": "string", "nullable": true, "description": "advisor firm id", "example": "<uuid>"},
    {"name": "enterprise_name", "type": "string", "nullable": true, "description": "advisor firm", "example": "49 Financial Group"},
    {"name": "parent_enterprise_id", "type": "string", "nullable": true, "description": "null on 511 of 511", "example": null},
    {"name": "parent_enterprise_name", "type": "string", "nullable": true, "description": "null on 511 of 511", "example": null},
    {"name": "as_of_timestamp", "type": "string", "nullable": true, "description": "vendor as-of", "example": "<ts>"},
    {"name": "opening_equity", "type": "double", "nullable": true, "description": "", "example": "100.0"},
    {"name": "closing_equity", "type": "double", "nullable": true, "description": "", "example": "100.0"},
    {"name": "opening_cash_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "closing_cash_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "opening_dividend_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "closing_dividend_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "opening_fee_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "closing_fee_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "opening_interest_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "closing_interest_value", "type": "double", "nullable": true, "description": "", "example": "0.0"},
    {"name": "long_position_count", "type": "int32", "nullable": true, "description": "", "example": "10"},
    {"name": "short_position_count", "type": "int32", "nullable": true, "description": "", "example": "0"},
    {"name": "run_date", "type": "string", "nullable": true, "description": "run date", "example": "2026-07-14"},
    {"name": "_ingested_at", "type": "string", "nullable": true, "description": "converter timestamp", "example": "<ts>"}
  ],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "enterprise_name / enterprise_id", "values": ["49 Financial Group (511 of 511)"], "claim": "measured"},
    "account": {"column": "brokerage_acct_num", "last4_derivation": "right(brokerage_acct_num,4)", "last4_collisions_within_firm": "not measured on 511 rows", "claim": "inferred"},
    "platform": {"column": "constant smartx", "values": ["smartx"], "claim": "measured"}
  },
  "nl_tags": ["sleeve valuation", "opening closing equity"],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/key_mapping.py ACCOUNT_TIER_PLATFORM_FEEDS@7878037d98",
  "open_items": ["one-shot, 64 trading days behind: no tool"],
  "evidence": [{"read": "get_object .../fact_nonzerosleeve/date=2026-07-14/data.parquet", "at": "2026-10-14T13:05Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_allocation_positions_DRAFT",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/allocation_positions/",
  "layer": "silver",
  "format": "parquet",
  "table": "allocation_positions",
  "grain": "pre-naming-law draft of fact_allocation_positions, one partition",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "draft converter run (superseded by fact_allocation_positions per silver.py silver_keys docstring)", "schedule": "none", "claim": "inferred"},
  "freshness": {"latest_partition": "2026-07-14", "basis": "trading-day-frontier", "lag_trading_days": 64, "claim": "measured"},
  "size": {"objects": 1, "bytes": 3050617, "rows_latest_partition": 107167, "rows_sampled": 0, "schema_variants": 1, "claim": "measured"},
  "columns": [{"name": "(same 17 columns as fact_allocation_positions, footer-measured)", "type": "", "nullable": true, "description": "", "example": ""}],
  "enums": {},
  "fork_keys": {"firm": {"column_or_key_segment": "as fact_allocation_positions", "values": []}, "account": {"column": "", "last4_derivation": "", "last4_collisions_within_firm": "n/a"}, "platform": {"column": "smartx", "values": ["smartx"]}},
  "nl_tags": [],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "retire"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "infra/aws/lambda/opal-assets/opal-assets-silver-smartx/silver.py silver_keys docstring@7878037d98 (DRAFT-SUPERSEDED, queued for Andrew's deletion batch)",
  "open_items": ["never index; deletion is Andrew's batch, not this census"],
  "evidence": [{"read": "footer smartx/platform/silver/allocation_positions/date=2026-07-14/data.parquet", "at": "2026-10-14T13:00Z"}]
}
```

```json
{
  "contract_id": "opal-data-assets/silver/smartx_allocation_valuation_DRAFT",
  "bucket": "opal-data-assets",
  "s3_prefix": "smartx/platform/silver/allocation_valuation/",
  "layer": "silver",
  "format": "parquet",
  "table": "allocation_valuation",
  "grain": "pre-naming-law draft of fact_allocation_valuation, one partition (count columns typed double here vs int32 in the fact table)",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "draft converter run (superseded)", "schedule": "none", "claim": "inferred"},
  "freshness": {"latest_partition": "2026-07-14", "basis": "trading-day-frontier", "lag_trading_days": 64, "claim": "measured"},
  "size": {"objects": 1, "bytes": 1126821, "rows_latest_partition": 9525, "rows_sampled": 0, "schema_variants": 1, "claim": "measured"},
  "columns": [{"name": "(same 15 columns as fact_allocation_valuation, footer-measured)", "type": "", "nullable": true, "description": "", "example": ""}],
  "enums": {},
  "fork_keys": {"firm": {"column_or_key_segment": "as fact_allocation_valuation", "values": []}, "account": {"column": "", "last4_derivation": "", "last4_collisions_within_firm": "n/a"}, "platform": {"column": "smartx", "values": ["smartx"]}},
  "nl_tags": [],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "retire"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "silver.py silver_keys docstring@7878037d98",
  "open_items": ["never index"],
  "evidence": [{"read": "footer smartx/platform/silver/allocation_valuation/date=2026-07-14/data.parquet", "at": "2026-10-14T13:00Z"}]
}
```

## (e) What could not be read, and why

- **Custodian on the daily tables:** no daily table carries a custodian column; Schwab master 08242234 is INFERRED from
  the 8-digit grammar and `NFRA_OPLGTW_CONTRACT.json:7`. Measured custodian exists only on 91 one-shot rows.
- **Account fork for Titleist, Canopy, Parable:** absent. The account map (feed 9) is credentialed to 49 Financial's
  bundle only; no other firm has an account number in silver. Their firm_ids are also absent from
  `partner_roster.json`, so the `firm` input has no canonical value for them yet.
- **Last-4 collisions on the three one-shot tables:** not measured (they are 64 trading days behind and get no tool).
- **comp-find:** two runs over the repo timed out at the 110 s harness ceiling; native Grep was used instead (rail-FREE),
  scoped to `infra/`, `data/`, `org/standards/` and the gateway app. A SmartX reader outside those trees would be missed.
- **Cross-firm hazard (for the CTO addendum):** every SmartX silver object commingles 4 advisor firms in one key, so
  the NEVER cross-firm rule cannot be met by key-prefix or IAM; it can only be met by a row filter on
  `roster.advisor_id` inside the tool. Not filed as a surprise row (the brief forbids writes outside this file);
  4.0.0_SA_CRO~Z may file it on `NFRA_OPLGTW` if it judges it off-spec.
- **Bronze contents:** not read (silver only, per the directive); bronze counts above are listing-only.
- **Catalog line numbers** were read from the working tree at HEAD 7878037d98; the bucket was read live, not through the
  served graph.
