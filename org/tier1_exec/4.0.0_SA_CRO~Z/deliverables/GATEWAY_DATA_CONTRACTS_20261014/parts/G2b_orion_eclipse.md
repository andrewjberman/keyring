# G2b -- opal-data-assets ORION and ECLIPSE silver (census part for 4.0.0_SA_CRO~Z, 2026-10-14)

Directive: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` (G2, Orion+Eclipse fan-out).
Brief: `parts/_SUBAGENT_BRIEF.md`. Read-only throughout: S3 list/get, Parquet footers, Lambda/EventBridge describe. No AWS write, no invoke.
Reads ran 2026-10-14 12:40Z..13:25Z. Repo pins are workspace HEAD `86003ec188` (box/sitez). T-1 frontier = 2026-10-13 (`lib/trading_calendar.prev_trading_day('2026-10-14')`; the module warned it answered from its hardcoded NYSE fallback 2010-2027).

## (a) Method

| # | read | instrument | denominator |
|---|---|---|---|
| 1 | prefix census of `orion/` and `eclipse/` | boto3 `list_objects_v2` paginator (no `--no-paginate`) | 15 pages, 14,313 of 14,313 keys |
| 2 | Parquet footer of every silver part (schema, num_rows) | pyarrow `read_metadata` over S3 range reads, 32 threads | 5,542 of 5,542 `.parquet` keys under `*/silver/`, 0 errors |
| 3 | newest-partition content (fork keys, enums, collisions, dupes) | pandas full read of the newest part of each of 9 tables (transactions: 22 projected columns) | 9 of 9 tables, newest part each; plus prior part of fact_transactions and fact_performance (snapshot test) and fact_assets 2026-08-06 (alien test) |
| 4 | snapshot test | id-set diff newest vs prior part | fact_transactions 1,520,410 vs 1,520,357 ids; fact_performance 482,341 vs 482,026 keys |
| 5 | bronze <-> silver partition parity | key-date sets from read 1 | 8 silver tables against their bronze feed dates |
| 6 | trading-day gaps and lag | `lib/trading_calendar` `is_trading_day`, `trading_days_behind` | every calendar date in each table's span |
| 7 | producers | `lambda get-function-configuration` + `get-policy` (3 functions), `events describe-rule` + `list-targets-by-rule` (4 rules), `s3api get-bucket-notification-configuration` | 2 Lambda notification configs on the bucket name an orion/eclipse prefix |
| 8 | converter status | `meta/backfill-status.json` + newest `meta/conversions/*.json` per family | 2 of 2 families |
| 9 | 4698 provenance | manifest.json; `infra/logic/registry/scopes.json`; `comp-find 'account_performance_gross' --files --all` | 22 hits across 201,891 files scanned (corpus all) |
| 10 | catalog and tools | Grep of `DATA_CATALOG.yaml` for `orion|eclipse|4698|inflection` | 8 hit lines in the whole file; 0 in `silver_datasets` (5 rows) and 0 in `tool_index` (67 tools) |
| 11 | consumers in the estate | Grep `fact_positions|fact_assets|fact_portfolios_full|fact_transactions` over `infra/aws` `*.{py,ts,tf}` | 19 files |

## (b) Prefix census (s3://opal-data-assets, LastModified UTC)

| prefix | objects | bytes | newest LastModified |
|---|---:|---:|---|
| `orion/inflection/bronze/` (assets 2,358; positions 2,357; transactions 146; performance 134) | 4,995 | 13,164,086,058 | 2026-10-13T13:05:24Z |
| `orion/inflection/silver/` | 4,997 | 9,209,737,635 | 2026-10-13T13:06:50Z |
| `orion/inflection/meta/` (conversions 517 + backfill-status.json) | 518 | 467,086 | 2026-10-13T16:00:47Z |
| `orion/4698/silver/` | 2 | 41,943 | 2026-10-09T06:58:44Z |
| `eclipse/inflection/bronze/` (137 date dirs x 13 files, `_history` 55, `_meta` 1, `eclipse_membership_map` 2) | 1,839 | 260,227,989 | 2026-10-13T13:05:31Z |
| `eclipse/inflection/silver/` | 544 | 32,337,330 | 2026-10-13T13:05:35Z |
| `eclipse/inflection/meta/` (conversions 1,410 + backfill-status.json) | 1,411 | 2,731,138 | 2026-10-13T16:00:08Z |
| `eclipse/inflection/reconstructed/` (7 `vintage=` dirs, one reconstruction.json each) | 7 | 662,706 | 2026-08-14T15:49:31Z |
| **total** | **14,313** | | |

Firms found: `orion/` holds `inflection` and `4698` (the same firm, see below); `eclipse/` holds `inflection` only. No other `orion/<firm>/` or `eclipse/<firm>/` exists (census 14,313 of 14,313 keys). **No gold layer** exists under either vendor tree (0 keys); gold built from these tables lives elsewhere (IRPT holdings-performance gold prefixes and MDPF platinum, inferred from their IAM/consumer code, not listed here).

Silver tables (9):

| table | parts | schema variants | rows, newest part | rows, sum of parts | first .. newest partition | trading days behind T-1 | shape |
|---|---:|---:|---:|---:|---|---:|---|
| orion/inflection fact_positions | 2,359 | 1 | 36,931 | 58,502,916 | 2020-04-24 .. 2026-10-13 | 0 | daily snapshot |
| orion/inflection fact_assets | 2,360 | 2 | 36,931 | 58,577,379 | 2020-04-28 .. 2026-10-13 | 0 | daily snapshot, DUPLICATE of fact_positions |
| orion/inflection fact_transactions | 145 | 1 | 1,520,410 | 204,990,973 | 2026-05-12 .. 2026-10-13 | 0 | FULL CUMULATIVE snapshot per part |
| orion/inflection fact_performance | 133 | 1 | 482,341 | 58,980,812 | 2026-05-03 .. 2026-10-12 | 1 | FULL CUMULATIVE snapshot per part |
| orion/4698 account_performance_gross | 1 | 1 | 3,129 | 3,129 | 2026-10-08 only | 3 | one-shot snapshot, no schedule |
| eclipse/inflection fact_portfolios_simple | 133 | 1 | 846 | 112,105 | 2026-05-15 .. 2026-10-09 | 2 | daily snapshot, STALLED |
| eclipse/inflection fact_portfolios_full | 137 | 1 | 863 | 117,117 | 2026-05-15 .. 2026-10-13 | 0 | daily snapshot |
| eclipse/inflection fact_models | 137 | 1 | 18 | 2,466 | 2026-05-15 .. 2026-10-13 | 0 | daily snapshot |
| eclipse/inflection fact_model_composition | 137 | 1 | 9 | 1,233 | 2026-05-15 .. 2026-10-13 | 0 | daily snapshot |

## (c) Analysis

**What "4698" is.** The Orion Connect database id (a vendor-issued MASTER) of Inflection Wealth Management. Evidence, measured:
the partition's `manifest.json` reads `"master": "4698", "firm": "inflection", "vendor": "orion", "query.database_id": 4698`;
`infra/logic/registry/scopes.json@86003ec188` carries key `4698`, class `MASTER`, firm `inflection`, vendor `orion`, and the
firm row `inflection` lists `masters: ["4698"]` and `monolith_scopes: {"orion": ["inflection"], "eclipse": ["inflection"]}`.
So `orion/` uses TWO key spellings for ONE firm: the firm slug (`inflection`, the converter families) and the master
(`4698`, written by one worker script through `opal_naming.address('orion','4698',...)`). A tool must resolve the firm to
both segments through the registry lookup, never type either.

**What the tables are.** Orion is Inflection's portfolio accounting system (custodian Fidelity): daily positions
(`fact_positions`; `fact_assets` is the same data from a second bronze feed), the full transaction history
(`fact_transactions`), a household-level daily performance factor (`fact_performance`) and one gross-of-fees 3-year TWR
snapshot per account (`orion/4698`). Eclipse is Orion's rebalancer: the portfolio-to-account bridge
(`fact_portfolios_simple`), portfolio state with drift, cash need and model (`fact_portfolios_full`), the model list
(`fact_models`) and model targets down to the security-set level (`fact_model_composition`). The join key across all of
them is the Orion `accountId` (Eclipse `accountId` matches 753 of 753; 4698 `account_id` matches 927 of 3,129 to today's
positions). Values tie out: positions currentValue sum 207.7M vs Eclipse totalValue sum 206.6M.

**Fork keys (directive section 3 rule 1).** Firm = S3 key segment 2 (no firm column in any row). Account = `accountNumber`,
custodial format `999-999999`; Orion appends a sleeve suffix (`_NNN`, `_AAA`, ...) so ONE custodial number maps to up to 6
Orion accounts. Last-4 must be taken from the base number before `_`; the raw string leaks suffix digits (52 colliding
values vs 30). Last-4 is NOT unique within the firm in any client table: positions 30 colliding values over 61 base
numbers (of 899), transactions 27 over 54 (of 826), Eclipse 22 over 44 (of 753), 4698 joined 29 over 58 (of 878). Every
account tool therefore needs a collision path: return the masked candidate list (accountId, sleeveType, model) and accept
`account_id` as the disambiguator. Platform = `custodian` / `custodianName` (`Fidelity_Inflection`, `Fidelity_LH`); the
Eclipse and performance tables have no platform column and inherit it through accountId.

**Read hazards a tool must encode.** (1) `fact_transactions` and `fact_performance` rewrite the FULL history into every
partition: read the newest partition only; summing parts counts each transaction ~145 times. (2) `fact_assets` duplicates
`fact_positions` (58 shared columns equal as strings on 36,931 rows): serve one. (3) `fact_portfolios_simple` is stalled at
2026-10-09 (VendorDriftError, extra column `defaultTradingEngineId`, since bronze 2026-10-10). (4) `orion/4698` is one ad-hoc
snapshot with no schedule. (5) `costBasis`, `isin`, `orderId` and `tradeOrderId` are null on every row of the newest
parts. (6) Eclipse model composition stops at security-set level: no ticker weights.

**Common questions.** What does account ...1234 hold today, and its value? What is its asset-class mix? Which accounts hold
ticker X? What transactions, fees, contributions and distributions did it have in a window? Which model and Eclipse
portfolio is it on, how far has it drifted, when was it last rebalanced, does it need cash? What is its 3-year gross TWR?
What models does Inflection run and what are their targets and AUM?

**Proposed tools (all take `firm`; account tools take `account_last4` + optional `platform`, `account_id`, `as_of`).**

| tool | reads | answers |
|---|---|---|
| `orion_resolve_account` | fact_positions newest <= as_of | last4 (+platform) -> masked candidates with accountId, sleeveType, modelName; the shared resolver every account tool calls |
| `orion_get_holdings` | fact_positions | positions and value of one account on one date |
| `orion_get_allocation` | fact_positions | weights by assetClass / productCategory / productType / ticker, inside one account or household and one date |
| `orion_find_holders` | fact_positions | which accounts of ONE firm hold a ticker on a date |
| `orion_list_transactions` | fact_transactions newest partition | transactions in a transDate window, by type and status |
| `orion_get_flows` | fact_transactions newest partition | contributions, distributions, fees, income sums for one account (Complete only, de-duplicated on id) |
| `orion_get_household_performance` | fact_performance newest partition | household factor series (HOLD until factor semantics are read) |
| `orion_get_account_performance` | orion/4698 account_performance_gross | 3-year annualized gross TWR of one account (labelled one-shot until scheduled) |
| `eclipse_get_portfolio` | fact_portfolios_simple + fact_portfolios_full | portfolio, model, drift, cash need, status, last rebalance of one account |
| `eclipse_list_portfolios` | fact_portfolios_full | firm-level portfolio list filtered by model / status / cash need / drift |
| `eclipse_list_models` | fact_models UNION fact_model_composition | models, portfolio counts, AUM, security-set targets |

Existing gateway tools: none reads these tables (CD1 baseline in `infra/aws/ec2/opal-gateway/tests/test_og_cd1.py`:
"orion served by no channel"); `mdpf_get_aggregate_aua` / `mdpf_get_aum_metrics` serve DERIVED Inflection totals that
`opal-assets-daily-emitter` computes from fact_assets and fact_portfolios_full (verdict keep, unrelated grain). The
`schwab_query` pattern (typed query over silver under a per-principal grant, `DATA_CATALOG.yaml` tool_index) is the reuse
model for the read path; no new IAM is proposed here (any read role is a never-widen act for the CTO addendum).
Catalog: no `silver_datasets` row covers any of the 9 tables; 4 rows are proposed (positions, transactions, performance,
4698 gross) plus 2 Eclipse rows (portfolios, models).

## (d) Contracts (one block per bucket -> table)

### opal-data-assets/silver/orion/inflection/fact_positions

```json
{
 "contract_id": "opal-data-assets/silver/orion/inflection/fact_positions",
 "bucket": "opal-data-assets",
 "s3_prefix": "orion/inflection/silver/fact_positions/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_positions",
 "grain": "one row per Orion asset (position) per account per snapshot date; id unique in the partition (0 dupes of 36,931)",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "one DAILY SNAPSHOT per partition (not cumulative): each part holds that day's holdings; calendar days incl. weekends; 5 calendar / 2 trading days absent in the 2020-04-24..2026-10-13 span (latest absent trading days 2026-07-01, 2026-09-28)"
 },
 "producer": {
  "name": "opal-assets-silver-orion (python3.11, FAMILY=orion, OPAL_BUILD_COMMIT fdf2b07a9e)",
  "schedule": "S3 ObjectCreated on orion/inflection/bronze/*.jsonl.gz (notification silver-orion) + EventBridge opal-assets-silver-orion-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands from opal-data-inf via opal-assets-ingest-mirror (cron(5 13 * * ? *) and cron(5 17 * * ? *), {\"firm\":\"inf\"})",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-orion/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "earliest_partition": "2020-04-24",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 0,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": "pulled ~13:05Z on the partition date; asOfDate equals the partition. Whether currentValue is the prior close is inferred, not verified"
 },
 "size": {
  "objects": 2359,
  "bytes": 2073379756,
  "parts": 2359,
  "schema_variants": 1,
  "rows_newest_partition": 36931,
  "rows_sum_all_parts": 58502916,
  "rows_sampled": 36931,
  "claim": "measured",
  "note": "rows_sum_all_parts is a sum of 2,359 independent daily snapshots: valid only as a row-day count"
 },
 "columns": [
  {
   "name": "costBasis",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "cost basis; all null in the newest part",
   "example": null
  },
  {
   "name": "name",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "name (see table notes)",
   "example": "Thrivent Income S"
  },
  {
   "name": "accountNumber",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "custodial account number; base format 999-999999, sleeves carry a _SUFFIX",
   "example": "***-***1234"
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "security ticker; FID:CASH is custodial cash",
   "example": "LBIIX"
  },
  {
   "name": "currentShares",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "quantity held",
   "example": 0.0
  },
  {
   "name": "currentValue",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "market value (USD)",
   "example": 0.0
  },
  {
   "name": "currentPrice",
   "type": "double",
   "nullable": true,
   "nulls_in_newest": 24184,
   "description": "price",
   "example": 78.5
  },
  {
   "name": "isManaged",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "assetClass",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Morningstar-style category",
   "example": "Corporate Bond"
  },
  {
   "name": "productCategory",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Equity / Bond / Money Market",
   "example": "Bond"
  },
  {
   "name": "productCategoryAbbreviation",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "B"
  },
  {
   "name": "isCustodialCash",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "secondaryAccountNumber",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36876,
   "description": "",
   "example": "<secondary account number>"
  },
  {
   "name": "productId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 178313
  },
  {
   "name": "assetLevelStrategyId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "assetLevelStrategy",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "status",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "record status",
   "example": 1
  },
  {
   "name": "isStrategyOverride",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "createdBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "createdDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2020-06-05T03:09:31.773-05:00"
  },
  {
   "name": "editedBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "editedDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2025-07-21T11:24:44.843-05:00"
  },
  {
   "name": "accountId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion account id (join key to Eclipse accountId and orion/4698 account_id)",
   "example": "<orion account id, int>"
  },
  {
   "name": "registrationId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion registration id",
   "example": "<orion registration id, int>"
  },
  {
   "name": "clientId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion client (household) id; equals householdId in fact_transactions",
   "example": "<orion client id, int>"
  },
  {
   "name": "isActive",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "downloadSymbol",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 291378
  },
  {
   "name": "accountType",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "registration type, long form",
   "example": "Individual Retirement Account"
  },
  {
   "name": "fundFamily",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "Fidelity"
  },
  {
   "name": "custodian",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "custodian / platform label",
   "example": "Fidelity_Inflection"
  },
  {
   "name": "asOfDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor as-of date, equals the partition date in the newest part",
   "example": "2026-10-13"
  },
  {
   "name": "registrationName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<registration name>"
  },
  {
   "name": "managementStyle",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 936,
   "description": "",
   "example": "Managed Account"
  },
  {
   "name": "sleeveType",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 35183,
   "description": "Custodial account / Normal / Distribution / Contribution sleeve; null when unsleeved",
   "example": "Custodial account"
  },
  {
   "name": "productType",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Stock/ETF, Mutual Fund, CD, Bond, Miscellaneous",
   "example": "Mutual Fund"
  },
  {
   "name": "productSubType",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1,
   "description": "",
   "example": "Mutual Fund"
  },
  {
   "name": "isGlobalExcluded",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isFeeExcluded",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "excludeAmountType",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36126,
   "description": "",
   "example": "Percent"
  },
  {
   "name": "excludeAmount",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "excludePercentOf",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36126,
   "description": "",
   "example": "Undefined"
  },
  {
   "name": "excludeFromMargin",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isRebalance",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "isAdvisorOnly",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isAdvReportable",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "is13FReportable",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "mscsFundAccountNumber",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": "<fund account number>"
  },
  {
   "name": "lastReconDate",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "isOrionVision",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "assetPercentOfAccount",
   "type": "double",
   "nullable": true,
   "nulls_in_newest": 24184,
   "description": "position weight in the account",
   "example": 5.4635
  },
  {
   "name": "householdName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<household name>"
  },
  {
   "name": "riskCategory",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 580,
   "description": "",
   "example": "Uncategorized"
  },
  {
   "name": "modelName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion model name on the account",
   "example": "Opal Intermediate Growth"
  },
  {
   "name": "registrationType",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "registration type code (IRA, ROTH, TOD, ...)",
   "example": "IRA"
  },
  {
   "name": "accountStatusId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "isin",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "ISIN; all null in the newest part",
   "example": null
  },
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 33029
  },
  {
   "name": "isDataSharingEntity",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "snapshot_date",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "partition date (fact_positions only)",
   "example": "2026-10-13"
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "2026-10-13.jsonl.gz"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-13"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "orion"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "positions"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "custodian": [
   "Fidelity_Inflection",
   "Fidelity_LH"
  ],
  "productCategory": [
   "Equity",
   "Bond",
   "Money Market"
  ],
  "productType": [
   "Stock/ETF",
   "Mutual Fund",
   "CD",
   "Bond",
   "Miscellaneous"
  ],
  "sleeveType": [
   "Custodial account",
   "Normal sleeve",
   "Distribution sleeve",
   "Contribution sleeve",
   null
  ],
  "managementStyle": [
   "Managed Account",
   null
  ],
  "riskCategory": [
   "Uncategorized",
   null
  ],
  "registrationType": "22 codes (IRA, ROTH, TOD, JNT, BIRA, ROLL, SEP, IND, TRU, INH, SIMP, IROTH, KEO, EST, INV, ...)",
  "assetClass": "125 values",
  "modelName": "24 values",
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "accountNumber (custodial); accountId is the Orion internal id",
   "last4_derivation": "base = accountNumber.split(\"_\")[0] (drops the sleeve suffix); last4 = last 4 digits of base with non-digits removed. Raw last-4 of the full string is WRONG: suffix digits (_01, _02) leak in.",
   "last4_collisions_within_firm": 30,
   "collision_detail": "newest part: 980 Orion accounts -> 899 distinct base numbers -> 868 distinct last4; 30 last4 values shared by 61 base numbers (max 3 per last4). Separately, one base number carries up to 6 Orion accounts (81 sleeve accounts with a _SUFFIX). Raw last-4 of the full string: 52 colliding values over 151 accounts. accountId last-4: 0 collisions of 980.",
   "claim": "measured"
  },
  "platform": {
   "column": "custodian",
   "values": [
    "Fidelity_Inflection",
    "Fidelity_LH"
   ],
   "claim": "measured",
   "note": "newest part: 978 accounts Fidelity_Inflection, 2 accounts Fidelity_LH; fundFamily is Fidelity on every row"
  }
 },
 "nl_tags": [
  "holdings",
  "positions",
  "positions by account",
  "Inflection holdings",
  "Orion positions",
  "account market value",
  "asset allocation"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of account ...1234 as of a date?",
  "Which Inflection accounts hold VOO?",
  "What is the asset-class mix of account ...1234?",
  "Which model is account ...1234 on in Orion?",
  "Total Inflection AUM on a date (sum currentValue)"
 ],
 "existing_gateway_tool": {
  "name": "none (CD1 baseline: orion served by no channel); indirect: mdpf_get_aggregate_aua serves an Inflection total derived from fact_assets by opal-assets-daily-emitter",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "orion_get_holdings",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234",
    "platform": "Fidelity_Inflection (optional)",
    "as_of": "YYYY-MM-DD (default newest partition <= T-1)",
    "account_id": "optional disambiguator"
   },
   "returns": "positions rows (ticker, name, currentShares, currentValue, currentPrice, assetClass, productType, assetPercentOfAccount, sleeveType, modelName) plus partition date; on a last4 collision returns the candidate list (masked number, accountId, sleeveType, modelName) and no rows",
   "answers": [
    "What does account ...1234 hold today?",
    "What is the market value of account ...1234 as of a date?"
   ]
  },
  {
   "name": "orion_get_allocation",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234 (or household_id)",
    "platform": "optional",
    "as_of": "YYYY-MM-DD",
    "group_by": "assetClass|productCategory|productType|ticker"
   },
   "returns": "weights and values grouped, summing currentValue only within one account (or one household) and one partition",
   "answers": [
    "What is the asset-class mix of account ...1234?"
   ]
  },
  {
   "name": "orion_find_holders",
   "inputs": {
    "firm": "inflection",
    "ticker": "VOO",
    "platform": "optional",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "masked account list with shares and value for one ticker, one firm, one partition",
   "answers": [
    "Which Inflection accounts hold VOO?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "orion_inflection_fact_positions (proposed)",
  "present": false
 },
 "prior_art": "infra/aws/terraform/investor-reporting/holdings-performance/iam.tf@86003ec188 (the IRPT Inflection holdings-performance role reads exactly this prefix)",
 "open_items": [
  "fact_assets is a byte-for-byte duplicate of this table on 58 shared columns (newest part, compared as strings, 36,931 rows); pick ONE as the tool read surface (recommend fact_positions: carries snapshot_date)",
  "costBasis and isin are null on every row of the newest part: no tax-lot or ISIN answer is possible from this table",
  "silver-only partitions 2026-08-06 and 2026-09-29 have no bronze source (guard verdict FAIL, alien 4); they were converted from a since-removed coerced .parquet bronze",
  "Fidelity_LH: 2 accounts under a second custodian label; whether LH is a separate entity inside the Inflection tenancy is not verified"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of orion/inflection/silver/fact_positions/date=2026-10-13/data.parquet (all columns, 36,931 rows)",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-orion; events describe-rule/list-targets-by-rule opal-assets-silver-orion-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/orion/inflection/meta/backfill-status.json + meta/conversions/20261013T160043Z-4270325c.json",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "Grep fact_positions over infra/aws (19 files): consumers opal-assets-daily-emitter, investor-reporting holdings-performance",
   "at": "2026-10-14T13:15Z"
  }
 ]
}
```

### opal-data-assets/silver/orion/inflection/fact_assets

```json
{
 "contract_id": "opal-data-assets/silver/orion/inflection/fact_assets",
 "bucket": "opal-data-assets",
 "s3_prefix": "orion/inflection/silver/fact_assets/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_assets",
 "grain": "one row per Orion asset per account per snapshot date; identical content to fact_positions (from the bronze assets feed)",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "daily snapshot, 2020-04-28..2026-10-13; 2 schema variants (2026-08-06, 2026-08-07 typed 6 all-null columns as null instead of string)"
 },
 "producer": {
  "name": "opal-assets-silver-orion (python3.11, FAMILY=orion, OPAL_BUILD_COMMIT fdf2b07a9e)",
  "schedule": "S3 ObjectCreated on orion/inflection/bronze/*.jsonl.gz (notification silver-orion) + EventBridge opal-assets-silver-orion-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands from opal-data-inf via opal-assets-ingest-mirror (cron(5 13 * * ? *) and cron(5 17 * * ? *), {\"firm\":\"inf\"})",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-orion/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "earliest_partition": "2020-04-28",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 0,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": "same landing as fact_positions"
 },
 "size": {
  "objects": 2360,
  "bytes": 2075305741,
  "parts": 2360,
  "schema_variants": 2,
  "rows_newest_partition": 36931,
  "rows_sum_all_parts": 58577379,
  "rows_sampled": 36931,
  "claim": "measured",
  "note": "rows_sum_all_parts is a sum of daily snapshots"
 },
 "columns": [
  {
   "name": "costBasis",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "cost basis; all null in the newest part",
   "example": null
  },
  {
   "name": "name",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "name (see table notes)",
   "example": "Thrivent Income S"
  },
  {
   "name": "accountNumber",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "custodial account number; base format 999-999999, sleeves carry a _SUFFIX",
   "example": "***-***1234"
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "security ticker; FID:CASH is custodial cash",
   "example": "LBIIX"
  },
  {
   "name": "currentShares",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "quantity held",
   "example": 0.0
  },
  {
   "name": "currentValue",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "market value (USD)",
   "example": 0.0
  },
  {
   "name": "currentPrice",
   "type": "double",
   "nullable": true,
   "nulls_in_newest": 24184,
   "description": "price",
   "example": 78.5
  },
  {
   "name": "isManaged",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "assetClass",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Morningstar-style category",
   "example": "Corporate Bond"
  },
  {
   "name": "productCategory",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Equity / Bond / Money Market",
   "example": "Bond"
  },
  {
   "name": "productCategoryAbbreviation",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "B"
  },
  {
   "name": "isCustodialCash",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "secondaryAccountNumber",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36876,
   "description": "",
   "example": "<secondary account number>"
  },
  {
   "name": "productId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 178313
  },
  {
   "name": "assetLevelStrategyId",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "assetLevelStrategy",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "status",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "record status",
   "example": 1
  },
  {
   "name": "isStrategyOverride",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "createdBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "createdDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2020-06-05T03:09:31.773-05:00"
  },
  {
   "name": "editedBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "editedDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2025-07-21T11:24:44.843-05:00"
  },
  {
   "name": "accountId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion account id (join key to Eclipse accountId and orion/4698 account_id)",
   "example": "<orion account id, int>"
  },
  {
   "name": "registrationId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion registration id",
   "example": "<orion registration id, int>"
  },
  {
   "name": "clientId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion client (household) id; equals householdId in fact_transactions",
   "example": "<orion client id, int>"
  },
  {
   "name": "isActive",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "downloadSymbol",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 291378
  },
  {
   "name": "accountType",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "registration type, long form",
   "example": "Individual Retirement Account"
  },
  {
   "name": "fundFamily",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "Fidelity"
  },
  {
   "name": "custodian",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "custodian / platform label",
   "example": "Fidelity_Inflection"
  },
  {
   "name": "asOfDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor as-of date, equals the partition date in the newest part",
   "example": "2026-10-13"
  },
  {
   "name": "registrationName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<registration name>"
  },
  {
   "name": "managementStyle",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 936,
   "description": "",
   "example": "Managed Account"
  },
  {
   "name": "sleeveType",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 35183,
   "description": "Custodial account / Normal / Distribution / Contribution sleeve; null when unsleeved",
   "example": "Custodial account"
  },
  {
   "name": "productType",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Stock/ETF, Mutual Fund, CD, Bond, Miscellaneous",
   "example": "Mutual Fund"
  },
  {
   "name": "productSubType",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1,
   "description": "",
   "example": "Mutual Fund"
  },
  {
   "name": "isGlobalExcluded",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isFeeExcluded",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "excludeAmountType",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36126,
   "description": "",
   "example": "Percent"
  },
  {
   "name": "excludeAmount",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "excludePercentOf",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 36126,
   "description": "",
   "example": "Undefined"
  },
  {
   "name": "excludeFromMargin",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isRebalance",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "isAdvisorOnly",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isAdvReportable",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "is13FReportable",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "mscsFundAccountNumber",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": "<fund account number>"
  },
  {
   "name": "lastReconDate",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "isOrionVision",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "",
   "example": null
  },
  {
   "name": "assetPercentOfAccount",
   "type": "double",
   "nullable": true,
   "nulls_in_newest": 24184,
   "description": "position weight in the account",
   "example": 5.4635
  },
  {
   "name": "householdName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<household name>"
  },
  {
   "name": "riskCategory",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 580,
   "description": "",
   "example": "Uncategorized"
  },
  {
   "name": "modelName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion model name on the account",
   "example": "Opal Intermediate Growth"
  },
  {
   "name": "registrationType",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "registration type code (IRA, ROTH, TOD, ...)",
   "example": "IRA"
  },
  {
   "name": "accountStatusId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "isin",
   "type": "null|string",
   "nullable": true,
   "nulls_in_newest": 36931,
   "description": "ISIN; all null in the newest part",
   "example": null
  },
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 33029
  },
  {
   "name": "isDataSharingEntity",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "2026-10-13.jsonl.gz"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-13"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "orion"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "assets"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "custodian": [
   "Fidelity_Inflection",
   "Fidelity_LH"
  ],
  "productCategory": [
   "Equity",
   "Bond",
   "Money Market"
  ],
  "productType": [
   "Stock/ETF",
   "Mutual Fund",
   "CD",
   "Bond",
   "Miscellaneous"
  ],
  "sleeveType": [
   "Custodial account",
   "Normal sleeve",
   "Distribution sleeve",
   "Contribution sleeve",
   null
  ],
  "managementStyle": [
   "Managed Account",
   null
  ],
  "riskCategory": [
   "Uncategorized",
   null
  ],
  "registrationType": "22 codes (IRA, ROTH, TOD, JNT, BIRA, ROLL, SEP, IND, TRU, INH, SIMP, IROTH, KEO, EST, INV, ...)",
  "assetClass": "125 values",
  "modelName": "24 values",
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "accountNumber (custodial); accountId is the Orion internal id",
   "last4_derivation": "base = accountNumber.split(\"_\")[0] (drops the sleeve suffix); last4 = last 4 digits of base with non-digits removed. Raw last-4 of the full string is WRONG: suffix digits (_01, _02) leak in.",
   "last4_collisions_within_firm": 30,
   "collision_detail": "newest part: 980 Orion accounts -> 899 distinct base numbers -> 868 distinct last4; 30 last4 values shared by 61 base numbers (max 3 per last4). Separately, one base number carries up to 6 Orion accounts (81 sleeve accounts with a _SUFFIX). Raw last-4 of the full string: 52 colliding values over 151 accounts. accountId last-4: 0 collisions of 980.",
   "claim": "measured"
  },
  "platform": {
   "column": "custodian",
   "values": [
    "Fidelity_Inflection",
    "Fidelity_LH"
   ],
   "claim": "measured",
   "note": "newest part: 978 accounts Fidelity_Inflection, 2 accounts Fidelity_LH; fundFamily is Fidelity on every row"
  }
 },
 "nl_tags": [
  "holdings",
  "positions",
  "positions by account",
  "Inflection holdings",
  "Orion positions",
  "account market value",
  "asset allocation"
 ],
 "common_queries": [
  "What does account ...1234 hold today?",
  "What is the market value of account ...1234 as of a date?",
  "Which Inflection accounts hold VOO?",
  "What is the asset-class mix of account ...1234?",
  "Which model is account ...1234 on in Orion?",
  "Total Inflection AUM on a date (sum currentValue)"
 ],
 "existing_gateway_tool": {
  "name": "none direct; opal-assets-daily-emitter reads it for the MDPF Inflection total (served by mdpf_get_aggregate_aua)",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "none -- serve through orion_get_holdings on fact_positions",
   "inputs": {
    "firm": "",
    "account_last4": "",
    "platform": "",
    "as_of": ""
   },
   "returns": "n/a",
   "answers": []
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "none proposed (duplicate of fact_positions); document as alias",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-daily-emitter/channel_sources.py@86003ec188 (ORION_ASSETS prefix)",
 "open_items": [
  "duplicate of fact_positions: one bronze pull lands twice (bronze/assets and bronze/positions, ~3.45 GB each) and converts twice; a consolidation candidate, not a tool",
  "columns typed null in 2 parts (2026-08-06/07): a reader must union-coerce"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of orion/inflection/silver/fact_assets/date=2026-10-13/data.parquet and equality test against fact_positions",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-orion; events describe-rule/list-targets-by-rule opal-assets-silver-orion-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/orion/inflection/meta/backfill-status.json + meta/conversions/20261013T160043Z-4270325c.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### opal-data-assets/silver/orion/inflection/fact_transactions

```json
{
 "contract_id": "opal-data-assets/silver/orion/inflection/fact_transactions",
 "bucket": "opal-data-assets",
 "s3_prefix": "orion/inflection/silver/fact_transactions/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_transactions",
 "grain": "one row per Orion transaction id (0 dupes of 1,520,410 in the newest part); EACH PARTITION IS A FULL CUMULATIVE SNAPSHOT",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "the partition records the PULL date (pull_date), not transDate. Newest part spans transDate 2020-06-03..2026-10-12 and is a strict superset of the prior part (+53 ids, 0 dropped). Read ONLY the newest partition; never union parts"
 },
 "producer": {
  "name": "opal-assets-silver-orion (python3.11, FAMILY=orion, OPAL_BUILD_COMMIT fdf2b07a9e)",
  "schedule": "S3 ObjectCreated on orion/inflection/bronze/*.jsonl.gz (notification silver-orion) + EventBridge opal-assets-silver-orion-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands from opal-data-inf via opal-assets-ingest-mirror (cron(5 13 * * ? *) and cron(5 17 * * ? *), {\"firm\":\"inf\"})",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-orion/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "earliest_partition": "2026-05-12",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 0,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": "max transDate 2026-10-12 in the 2026-10-13 pull"
 },
 "size": {
  "objects": 145,
  "bytes": 4594523597,
  "parts": 145,
  "schema_variants": 1,
  "rows_newest_partition": 1520410,
  "rows_sum_all_parts": 204990973,
  "rows_sampled": 1520410,
  "claim": "measured",
  "note": "TABLE ROW COUNT = rows_newest_partition (1,520,410). rows_sum_all_parts (204,990,973) counts the same transactions ~145 times"
 },
 "columns": [
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 5658274
  },
  {
   "name": "assetId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 109512
  },
  {
   "name": "productName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "iShares Core S&P Mid-Cap ETF"
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "security ticker; FID:CASH is custodial cash",
   "example": "IJH"
  },
  {
   "name": "accountId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion account id (join key to Eclipse accountId and orion/4698 account_id)",
   "example": "<orion account id, int>"
  },
  {
   "name": "accountNumber",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "custodial account number; base format 999-999999, sleeves carry a _SUFFIX",
   "example": "***-***1234"
  },
  {
   "name": "registrationId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion registration id",
   "example": "<orion registration id, int>"
  },
  {
   "name": "registrationName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<registration name>"
  },
  {
   "name": "registrationCode",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<registration code>"
  },
  {
   "name": "householdId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<orion household id, int>"
  },
  {
   "name": "fundFamilyName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "Fidelity"
  },
  {
   "name": "custodianName",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "custodian / platform label",
   "example": "Fidelity_Inflection"
  },
  {
   "name": "status",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "record status",
   "example": "Pending"
  },
  {
   "name": "transDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "transaction date",
   "example": "2026-07-13"
  },
  {
   "name": "transactionDescription",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "transaction type label (46 values)",
   "example": "Buy Exchange"
  },
  {
   "name": "transAmount",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "amount (USD)",
   "example": 529.83
  },
  {
   "name": "navPrice",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "price",
   "example": 75.69
  },
  {
   "name": "noUnits",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "units",
   "example": 7.0
  },
  {
   "name": "notes",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 10,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "orderId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "blockId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "orderCreatedBy",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "avgPrice",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "executionTime",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "transTypeId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "transaction type id",
   "example": 10
  },
  {
   "name": "contributionCodeId",
   "type": "double",
   "nullable": true,
   "nulls_in_newest": 1519145,
   "description": "",
   "example": 34.0
  },
  {
   "name": "distributionCodeId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "clientId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion client (household) id; equals householdId in fact_transactions",
   "example": "<orion client id, int>"
  },
  {
   "name": "registrationSleeveStrategyName",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "tradeOrderId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1520410,
   "description": "",
   "example": null
  },
  {
   "name": "pull_date",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "date the puller ran; equals the partition",
   "example": "2026-10-13"
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "2026-10-13.jsonl.gz"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-13"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "orion"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "transactions"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "custodianName": [
   "Fidelity_Inflection",
   "Fidelity_LH"
  ],
  "status": [
   "Complete",
   "Pending",
   "Rejected",
   "Reversed",
   "Pending Corporate Action",
   "Inactive"
  ],
  "transactionDescription": "46 values; top: Buy Exchange, Sell Exchange, Income Reinvested, Dividend to Cash, Management Fee, Trading Expense, Merge In from Other Account, Long Term Gain to Cash, Client Distribution, Client Contribution, Short Term Gain to Cash, Interest Paid in Cash, Federal Tax Withheld",
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "accountNumber (custodial); accountId Orion id",
   "last4_derivation": "base = accountNumber.split(\"_\")[0] (drops the sleeve suffix); last4 = last 4 digits of base with non-digits removed. Raw last-4 of the full string is WRONG: suffix digits (_01, _02) leak in.",
   "last4_collisions_within_firm": 27,
   "collision_detail": "newest part: 871 accounts -> 826 base numbers; 27 last4 values shared by 54 base numbers",
   "claim": "measured"
  },
  "platform": {
   "column": "custodianName",
   "values": [
    "Fidelity_Inflection",
    "Fidelity_LH"
   ],
   "claim": "measured",
   "note": "1,520,286 rows Fidelity_Inflection, 124 rows Fidelity_LH"
  }
 },
 "nl_tags": [
  "transactions",
  "activity",
  "trades",
  "contributions",
  "distributions",
  "management fees",
  "dividends",
  "cash flows",
  "Orion transactions"
 ],
 "common_queries": [
  "What transactions did account ...1234 have last month?",
  "What management fees were charged to account ...1234 this quarter?",
  "What contributions and distributions did account ...1234 have year to date?",
  "Which trades are pending or rejected for account ...1234?",
  "What dividends did account ...1234 receive in a date range?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "orion_list_transactions",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234",
    "platform": "optional",
    "as_of": "pull partition (default newest)",
    "date_from": "YYYY-MM-DD",
    "date_to": "YYYY-MM-DD",
    "type": "optional transactionDescription filter",
    "status": "optional, default Complete"
   },
   "returns": "transaction rows (transDate, transactionDescription, ticker, transAmount, noUnits, navPrice, status) from the ONE newest partition, filtered by transDate",
   "answers": [
    "What transactions did account ...1234 have last month?",
    "What management fees were charged to account ...1234 this quarter?",
    "Which trades are pending or rejected for account ...1234?"
   ]
  },
  {
   "name": "orion_get_flows",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234",
    "platform": "optional",
    "as_of": "pull partition",
    "date_from": "",
    "date_to": ""
   },
   "returns": "sums of Client Contribution / Client Distribution / Management Fee / income types for one account, status Complete only, de-duplicated on id",
   "answers": [
    "What contributions and distributions did account ...1234 have year to date?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "orion_inflection_fact_transactions (proposed)",
  "present": false
 },
 "prior_art": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~371/IB187-2_transaction_source_mapping.json@86003ec188",
 "open_items": [
  "never_sum rule for the catalog: never sum across partitions (each is the full history); never sum Pending/Rejected/Reversed with Complete",
  "orderId, tradeOrderId and registrationSleeveStrategyName are null on every row of the newest part",
  "bronze partitions 2026-07-11..07-15 absent by producer death; covered by the 2026-07-16 pull window (bronze/transactions/_meta/window-coverage-20260716.json)",
  "a 34 MB part per call: the tool needs projected columns + an accountId predicate pushdown"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of orion/inflection/silver/fact_transactions/date=2026-10-13 (22 projected columns) and id-set diff against date=2026-10-12",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-orion; events describe-rule/list-targets-by-rule opal-assets-silver-orion-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/orion/inflection/meta/backfill-status.json + meta/conversions/20261013T160043Z-4270325c.json",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "s3://opal-data-assets/orion/inflection/bronze/transactions/_meta/window-coverage-20260716.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### opal-data-assets/silver/orion/inflection/fact_performance

```json
{
 "contract_id": "opal-data-assets/silver/orion/inflection/fact_performance",
 "bucket": "opal-data-assets",
 "s3_prefix": "orion/inflection/silver/fact_performance/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_performance",
 "grain": "one row per Orion client (household) per value date; (client_id, date) unique (0 dupes of 482,341); EACH PARTITION IS A FULL CUMULATIVE SNAPSHOT",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "partition = pull_date; newest part spans 2020-05-26..2026-10-12 for 315 clients and is a superset of the prior part (+315 rows, 0 factor changes on 482,026 shared keys). 30 calendar / 21 trading days absent in 2026-05-03..2026-10-12 (latest 2026-09-28..09-30)"
 },
 "producer": {
  "name": "opal-assets-silver-orion (python3.11, FAMILY=orion, OPAL_BUILD_COMMIT fdf2b07a9e)",
  "schedule": "S3 ObjectCreated on orion/inflection/bronze/*.jsonl.gz (notification silver-orion) + EventBridge opal-assets-silver-orion-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands from opal-data-inf via opal-assets-ingest-mirror (cron(5 13 * * ? *) and cron(5 17 * * ? *), {\"firm\":\"inf\"})",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-orion/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "earliest_partition": "2026-05-03",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 1,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": "newest pull 2026-10-12; no 2026-10-13 bronze performance object"
 },
 "size": {
  "objects": 133,
  "bytes": 466528541,
  "parts": 133,
  "schema_variants": 1,
  "rows_newest_partition": 482341,
  "rows_sum_all_parts": 58980812,
  "rows_sampled": 482341,
  "claim": "measured",
  "note": "TABLE ROW COUNT = rows_newest_partition (482,341); rows_sum_all_parts double-counts"
 },
 "columns": [
  {
   "name": "client_id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion client (household) id",
   "example": "<orion client id, int>"
  },
  {
   "name": "date",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "value date",
   "example": "2020-06-04"
  },
  {
   "name": "factor",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "per-client daily performance factor (semantics not verified; see open items)",
   "example": 1.0
  },
  {
   "name": "pull_date",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "date the puller ran; equals the partition",
   "example": "2026-10-12"
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "2026-10-12.jsonl.gz"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-12"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "orion"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "performance"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "absent: the grain is client_id (Orion household); 315 of 315 client_id values match fact_positions.clientId",
   "last4_derivation": "not forkable by account directly: resolve last4 -> accountId -> clientId through fact_positions, then read the household series",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "absent (no custodian column); inherit from the account resolved in fact_positions",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "performance",
  "household performance",
  "daily performance factor",
  "returns",
  "Orion performance"
 ],
 "common_queries": [
  "What is the performance history of the household that owns account ...1234?",
  "What was the household return between two dates?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "orion_get_household_performance",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234 (resolved to clientId)",
    "platform": "optional",
    "as_of": "pull partition",
    "date_from": "",
    "date_to": ""
   },
   "returns": "the (date, factor) series for one client_id from the newest partition, with the factor semantics stated once verified",
   "answers": [
    "What is the performance history of the household that owns account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "orion_inflection_fact_performance (proposed, HOLD until factor semantics are read)",
  "present": false
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~X/deliverables/inf_performance_trace_20261001/EVIDENCE.json@86003ec188",
 "open_items": [
  "factor semantics NOT verified: median 1.186, min -25.15, max 170.73 over the newest part; a daily return, a growth index or a cumulative factor each change the tool. Read the puller or Orion docs before contracting the return math",
  "household grain, not account: a per-account return comes from orion/4698 account_performance_gross (annualized, one snapshot) or is computed elsewhere"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of orion/inflection/silver/fact_performance/date=2026-10-12 and 2026-10-11 (all 9 columns), key diff",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-orion; events describe-rule/list-targets-by-rule opal-assets-silver-orion-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/orion/inflection/meta/backfill-status.json + meta/conversions/20261013T160043Z-4270325c.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### opal-data-assets/silver/orion/4698/account_performance_gross

```json
{
 "contract_id": "opal-data-assets/silver/orion/4698/account_performance_gross",
 "bucket": "opal-data-assets",
 "s3_prefix": "orion/4698/silver/account_performance_gross/",
 "layer": "silver",
 "format": "parquet",
 "table": "account_performance_gross",
 "grain": "one row per Orion account id (0 dupes of 3,129): annualized gross-of-fees account TWR over a Rolling 3-Year window",
 "partition": {
  "keys": [
   "snapshot_date"
  ],
  "object": "snapshot_date=YYYY-MM-DD/{data.parquet,manifest.json}",
  "claim": "measured",
  "note": "ONE partition only (2026-10-08)"
 },
 "producer": {
  "name": "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~57/orion_gross_silver.py --land (task order IRPT_DASHBD.TO-DB-b-79; Orion Connect saved query \"Performance Dim\", feeMethod Gross Of Fees)",
  "schedule": "NONE: a one-shot worker run (pulled_at_utc 2026-10-09T06:58Z); no Lambda, rule or schedule found. comp-find account_performance_gross: 22 hits across 201,891 files, every producer hit is this worker deliverable",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-08",
  "earliest_partition": "2026-10-08",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 3,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": "one-shot snapshot; it will not advance without a re-run"
 },
 "size": {
  "objects": 2,
  "bytes": 41943,
  "parts": 1,
  "schema_variants": 1,
  "rows_newest_partition": 3129,
  "rows_sum_all_parts": 3129,
  "rows_sampled": 3129,
  "claim": "measured",
  "note": "manifest.json rows 3129 agrees with the footer"
 },
 "columns": [
  {
   "name": "account_id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "Orion account id",
   "example": "<orion account id, int>"
  },
  {
   "name": "twr_gross_value",
   "type": "double",
   "nullable": true,
   "nulls_in_newest": 1236,
   "description": "annualized gross-of-fees TWR, percent number",
   "example": 16.06
  },
  {
   "name": "twr_gross_raw",
   "type": "large_string",
   "nullable": true,
   "nulls_in_newest": 1236,
   "description": "vendor string, shape \"9.9 %\"",
   "example": "16.06 %"
  },
  {
   "name": "fee_method",
   "type": "large_string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "fee method of the pull",
   "example": "Gross of Fees"
  },
  {
   "name": "date_range_start",
   "type": "large_string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "window start (Rolling 3-Year, later for younger accounts)",
   "example": "2023-10-09"
  },
  {
   "name": "date_range_end",
   "type": "large_string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "window end",
   "example": "2026-10-08"
  },
  {
   "name": "as_of",
   "type": "large_string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "snapshot date",
   "example": "2026-10-08"
  }
 ],
 "enums": {
  "fee_method": [
   "Gross of Fees"
  ],
  "date_range_end": [
   "2026-10-08"
  ],
  "claim": "measured"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 = \"4698\": the Orion database id (master) of Inflection, NOT a firm slug",
   "values": [
    "4698 -> inflection"
   ],
   "claim": "measured",
   "evidence": "manifest.json {\"master\":\"4698\",\"firm\":\"inflection\",\"vendor\":\"orion\",\"query.database_id\":4698}; infra/logic/registry/scopes.json@86003ec188 key 4698 class MASTER firm inflection vendor orion (\"Inflection's Orion database/firm id, the databaseIdList value every Inflection Orion pull carries\")"
  },
  "account": {
   "column": "account_id (Orion account id); no account number in the table",
   "last4_derivation": "join account_id -> fact_positions.accountId -> accountNumber, then the base-number rule. 927 of 3,129 ids join to the 2026-10-13 positions; the other 2,202 are not in today's holdings (inferred closed/inactive)",
   "last4_collisions_within_firm": 29,
   "collision_detail": "over the 927 joined accounts: 878 base numbers, 849 distinct last4, 29 colliding values covering 58 base numbers",
   "claim": "measured"
  },
  "platform": {
   "column": "absent; inherit custodian from fact_positions",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "account performance",
  "gross of fees",
  "TWR",
  "3-year return",
  "annualized return",
  "Inflection performance"
 ],
 "common_queries": [
  "What is the 3-year annualized gross-of-fees return of account ...1234?",
  "Which Inflection accounts have no gross TWR?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "orion_get_account_performance",
   "inputs": {
    "firm": "inflection (resolves to master 4698)",
    "account_last4": "1234",
    "platform": "optional",
    "as_of": "snapshot_date (only 2026-10-08 exists)"
   },
   "returns": "twr_gross_value, fee_method, date_range_start/end, as_of; null twr returned as null with the count, never 0",
   "answers": [
    "What is the 3-year annualized gross-of-fees return of account ...1234?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "orion_4698_account_performance_gross (proposed)",
  "present": false
 },
 "prior_art": "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~57/ORION_GROSS_SILVER.json@86003ec188",
 "open_items": [
  "NOT a production table: one ad-hoc snapshot, no schedule (CLAUDE.md: ad-hoc artifacts are never production evidence). A tool on it must say so, or the producer must be scheduled first",
  "twr_gross_value null on 1,236 of 3,129 rows; outliers min -697.74, max 348.73 (percent)",
  "two key spellings for ONE firm under orion/: \"inflection\" (firm slug) and \"4698\" (master). A tool must resolve firm -> both through lib/opal_naming lookup, never by typing the segment"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "s3://opal-data-assets/orion/4698/silver/account_performance_gross/snapshot_date=2026-10-08/manifest.json and data.parquet (all columns)",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "Read infra/logic/registry/scopes.json lines 122-140, 285-297",
   "at": "2026-10-14T13:15Z"
  },
  {
   "read": "comp-find 'account_performance_gross' --files --all (22 hits, 201,891 files scanned)",
   "at": "2026-10-14T13:20Z"
  }
 ]
}
```

### opal-data-assets/silver/eclipse/inflection/fact_portfolios_simple

```json
{
 "contract_id": "opal-data-assets/silver/eclipse/inflection/fact_portfolios_simple",
 "bucket": "opal-data-assets",
 "s3_prefix": "eclipse/inflection/silver/fact_portfolios_simple/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_portfolios_simple",
 "grain": "one row per Eclipse portfolio-account link per snapshot date (id = portfolio id, unique: 0 dupes of 846); the ACCOUNT BRIDGE of Eclipse",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "daily snapshot; 7 trading days absent in 2026-05-15..2026-10-09"
 },
 "producer": {
  "name": "opal-assets-silver-eclipse (python3.11, FAMILY=eclipse, OPAL_BUILD_COMMIT b915719f25)",
  "schedule": "S3 ObjectCreated on eclipse/inflection/bronze/*.json (notification silver-eclipse) + EventBridge opal-assets-silver-eclipse-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands via opal-assets-ingest-mirror (cron(5 13 * * ? *), cron(5 17 * * ? *))",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-09",
  "earliest_partition": "2026-05-15",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 2,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": "STOPPED: bronze 2026-10-10..10-13 portfolios_simple.json landed but conversion fails with VendorDriftError (extra column defaultTradingEngineId; declared 22 cols in mirror_schemas.py). Guard verdict FAIL, missing 4"
 },
 "size": {
  "objects": 133,
  "bytes": 7658153,
  "parts": 133,
  "schema_variants": 1,
  "rows_newest_partition": 846,
  "rows_sum_all_parts": 112105,
  "rows_sampled": 846,
  "claim": "measured",
  "note": "daily snapshot; table row count = newest partition"
 },
 "columns": [
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "name",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "name (see table notes)",
   "example": "<client name>"
  },
  {
   "name": "tags",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 359,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "custodialAccountNumber",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 846,
   "description": "",
   "example": "***-***1234"
  },
  {
   "name": "source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "Team"
  },
  {
   "name": "accountId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 93,
   "description": "Orion account id (join key to Eclipse accountId and orion/4698 account_id)",
   "example": "<orion account id, int>"
  },
  {
   "name": "accountNumber",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 93,
   "description": "custodial account number; base format 999-999999, sleeves carry a _SUFFIX",
   "example": "***-***1234"
  },
  {
   "name": "accountName",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 93,
   "description": "",
   "example": "<client name>"
  },
  {
   "name": "hasDistribution",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "hasContribution",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "modelId",
   "type": "int64",
   "nullable": true,
   "nulls_in_newest": 179,
   "description": "Eclipse model id",
   "example": 3.0
  },
  {
   "name": "sleevePortfolio",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "1 = sleeve portfolio",
   "example": 0
  },
  {
   "name": "isDeleted",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "createdOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2025-08-13T19:39:10.000Z"
  },
  {
   "name": "createdBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "editedOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-01-15T17:52:42.000Z"
  },
  {
   "name": "editedBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "macStatus",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "needAnalytics",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "analyticsEditedDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-10-07T19:35:16.000Z"
  },
  {
   "name": "failedReason",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 752,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "hasTaxLossHarvest",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "portfolios_simple.json"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-09"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "eclipse"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "portfolios_simple"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "source": [
   "Team"
  ],
  "sleevePortfolio": [
   0
  ],
  "hasTaxLossHarvest": [
   0,
   1
  ],
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "accountNumber (custodial; custodialAccountNumber is null on every row); accountId = Orion accountId (753 of 753 match)",
   "last4_derivation": "last 4 digits of accountNumber (no sleeve suffix in this table: patterns 999-999999 x749, A99-999999 x4)",
   "last4_collisions_within_firm": 22,
   "collision_detail": "753 account numbers -> 731 distinct last4; 22 values shared by 44 numbers; 93 portfolios have no account",
   "claim": "measured"
  },
  "platform": {
   "column": "absent; inherit custodian via accountId -> orion fact_positions",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "Eclipse",
  "portfolio",
  "account to portfolio",
  "rebalancer",
  "model assignment",
  "tax loss harvest flag"
 ],
 "common_queries": [
  "Which Eclipse portfolio and model is account ...1234 in?",
  "Does account ...1234 have tax-loss harvesting on?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "eclipse_get_portfolio",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234",
    "platform": "optional",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "portfolio id, modelId, hasTaxLossHarvest, needAnalytics, joined to fact_portfolios_full (model, values, drift, cash need, status, lastRebalancedOn)",
   "answers": [
    "Which Eclipse portfolio and model is account ...1234 in?",
    "Does account ...1234 have tax-loss harvesting on?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "eclipse_inflection_portfolios (proposed, one row for simple+full)",
  "present": false
 },
 "prior_art": "org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/MDPF_STRATID.TO-ST-t4.eclipse-sleeve-name-census.proof_of_spec.json@86003ec188",
 "open_items": [
  "SURPRISE ROW owed (not filed by this subagent: write surface is the part file only): eclipse/portfolios_simple silver stalled at 2026-10-09 on VendorDriftError since the 2026-10-10 bronze; 12 DLQ messages drained in run 20261013T160005Z-e6eaf217. Disarm = a reviewed mirror_schemas.py edit",
  "name and accountName are client names: never returned unmasked"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of eclipse/inflection/silver/fact_portfolios_simple/date=2026-10-09 (all 27 columns); join to orion fact_positions 2026-10-13",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-eclipse; events describe-rule/list-targets-by-rule opal-assets-silver-eclipse-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/eclipse/inflection/meta/backfill-status.json + meta/conversions/20261013T160005Z-e6eaf217.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### opal-data-assets/silver/eclipse/inflection/fact_portfolios_full

```json
{
 "contract_id": "opal-data-assets/silver/eclipse/inflection/fact_portfolios_full",
 "bucket": "opal-data-assets",
 "s3_prefix": "eclipse/inflection/silver/fact_portfolios_full/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_portfolios_full",
 "grain": "one row per Eclipse portfolio per snapshot date (id unique: 0 dupes of 863; 846 are in fact_portfolios_simple, 17 are sleeve portfolios)",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "daily snapshot; 7 trading days absent in 2026-05-15..2026-10-13"
 },
 "producer": {
  "name": "opal-assets-silver-eclipse (python3.11, FAMILY=eclipse, OPAL_BUILD_COMMIT b915719f25)",
  "schedule": "S3 ObjectCreated on eclipse/inflection/bronze/*.json (notification silver-eclipse) + EventBridge opal-assets-silver-eclipse-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands via opal-assets-ingest-mirror (cron(5 13 * * ? *), cron(5 17 * * ? *))",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "earliest_partition": "2026-05-15",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 0,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": ""
 },
 "size": {
  "objects": 137,
  "bytes": 15184093,
  "parts": 137,
  "schema_variants": 1,
  "rows_newest_partition": 863,
  "rows_sum_all_parts": 117117,
  "rows_sampled": 863,
  "claim": "measured",
  "note": "daily snapshot; table row count = newest partition. totalValue sum 206.6M, managedValue 192.7M"
 },
 "columns": [
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1195
  },
  {
   "name": "name",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "name (see table notes)",
   "example": "<client name>"
  },
  {
   "name": "model",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 179,
   "description": "Eclipse model name",
   "example": "50/50 Opal Intermediate/Opal Long Term"
  },
  {
   "name": "modelId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 179,
   "description": "Eclipse model id",
   "example": "28"
  },
  {
   "name": "sleevePortfolio",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "1 = sleeve portfolio",
   "example": 0
  },
  {
   "name": "team",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<team or advisor name>"
  },
  {
   "name": "managedValue",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "managed value (USD)",
   "example": 1098.84
  },
  {
   "name": "excludedValue",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "totalValue",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "total value (USD)",
   "example": 1098.84
  },
  {
   "name": "action",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 863,
   "description": "",
   "example": null
  },
  {
   "name": "tradesPending",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "percentDeviations",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "drift from model, percent",
   "example": 38.48
  },
  {
   "name": "cashNeedPercentage",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": -19.24
  },
  {
   "name": "cashNeedAmount",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "cash need (USD)",
   "example": -211.44
  },
  {
   "name": "tags",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 863,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "tradingInstruction",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 863,
   "description": "",
   "example": null
  },
  {
   "name": "taxQualification",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 93,
   "description": "T / TE / TD",
   "example": "T"
  },
  {
   "name": "numOfAssociatedAccounts",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "accounts in the portfolio",
   "example": 1
  },
  {
   "name": "distributionAmt",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "reserveCashTarget",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "reserveCashActual",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "setAsideCashTarget",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "setAsideCashActual",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "targetCash",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 8.68
  },
  {
   "name": "targetCashPercent",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.79
  },
  {
   "name": "currentCash",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 220.12
  },
  {
   "name": "currentCashPercent",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 20.03
  },
  {
   "name": "pendingCash",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 220.12
  },
  {
   "name": "pendingCashPercent",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 20.03
  },
  {
   "name": "cashOverage",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "cashOveragePercent",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "cashUnderage",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "cashUnderagePercent",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "pendingValue",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1098.84
  },
  {
   "name": "pendingValuePercent",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 100.0
  },
  {
   "name": "autoRebalanceOn",
   "type": "int64",
   "nullable": true,
   "nulls_in_newest": 861,
   "description": "",
   "example": 1.0
  },
  {
   "name": "OUB",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "contribution",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0.0
  },
  {
   "name": "tradeBlocked",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "status",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "record status",
   "example": "Warning"
  },
  {
   "name": "statusInfo",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "TLH",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "style",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 783,
   "description": "",
   "example": "Growth"
  },
  {
   "name": "lastRebalancedOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "last rebalance date",
   "example": "2026-10-08 00:00:00"
  },
  {
   "name": "isDisabled",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "nextAutoRebalanceDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "0"
  },
  {
   "name": "isDeleted",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "createdOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2025-08-14T14:29:02.000Z"
  },
  {
   "name": "createdBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "editedOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-07-10T03:01:12.000Z"
  },
  {
   "name": "editedBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "needAnalyticsStatus",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "No"
  },
  {
   "name": "needAnalyticsToTradeStatus",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "No"
  },
  {
   "name": "portfolioDisabledReason",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 863,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "needAnalyticsFailedReason",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 769,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "isMAC",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "fixedIncomeTradeBlockDate",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 863,
   "description": "",
   "example": null
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "portfolios_full.json"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-13"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "eclipse"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "portfolios_full"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "status": [
   "Warning",
   "Ok"
  ],
  "taxQualification": [
   "TD",
   "T",
   "TE",
   null
  ],
  "style": [
   "Balanced",
   "Growth",
   "Aggressive",
   "Conservative",
   null
  ],
  "team": "3 values: the firm name and 2 advisor-named teams (names not reproduced)",
  "model": "19 values incl. null (e.g. Opal Intermediate Growth, Opal Long Term, IWM Moderate Taxable)",
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "absent: portfolio grain; reach the account through fact_portfolios_simple.id -> accountNumber",
   "last4_derivation": "via fact_portfolios_simple (22 collisions there)",
   "last4_collisions_within_firm": 22,
   "claim": "measured"
  },
  "platform": {
   "column": "absent",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "Eclipse",
  "portfolio drift",
  "rebalance",
  "cash need",
  "model assignment",
  "portfolio value",
  "trade blocked"
 ],
 "common_queries": [
  "How far is account ...1234 drifted from its model?",
  "When was account ...1234 last rebalanced?",
  "Which portfolios need cash?",
  "How many Inflection portfolios are on each model?"
 ],
 "existing_gateway_tool": {
  "name": "none direct; opal-assets-daily-emitter reads it for the MDPF Inflection Opal-scoped model value",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "eclipse_get_portfolio",
   "inputs": {
    "firm": "inflection",
    "account_last4": "1234",
    "platform": "optional",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "see fact_portfolios_simple contract (one tool over both tables)",
   "answers": [
    "How far is account ...1234 drifted from its model?",
    "When was account ...1234 last rebalanced?"
   ]
  },
  {
   "name": "eclipse_list_portfolios",
   "inputs": {
    "firm": "inflection",
    "account_last4": "",
    "platform": "",
    "as_of": "YYYY-MM-DD",
    "filter": "model|status|cash_need>0|drift>x"
   },
   "returns": "masked portfolio list with model, totalValue, percentDeviations, cashNeedAmount, status",
   "answers": [
    "Which portfolios need cash?",
    "How many Inflection portfolios are on each model?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "eclipse_inflection_portfolios (proposed)",
  "present": false
 },
 "prior_art": "infra/aws/lambda/opal-assets/opal-assets-daily-emitter/channel_sources.py@86003ec188",
 "open_items": [
  "name is a client name; team carries advisor names: mask both"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of eclipse/inflection/silver/fact_portfolios_full/date=2026-10-13 (all 62 columns)",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-eclipse; events describe-rule/list-targets-by-rule opal-assets-silver-eclipse-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/eclipse/inflection/meta/backfill-status.json + meta/conversions/20261013T160005Z-e6eaf217.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### opal-data-assets/silver/eclipse/inflection/fact_models

```json
{
 "contract_id": "opal-data-assets/silver/eclipse/inflection/fact_models",
 "bucket": "opal-data-assets",
 "s3_prefix": "eclipse/inflection/silver/fact_models/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_models",
 "grain": "one row per Eclipse model visible to the Inflection team per snapshot date (18 rows, id unique)",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "daily snapshot from bronze models.json"
 },
 "producer": {
  "name": "opal-assets-silver-eclipse (python3.11, FAMILY=eclipse, OPAL_BUILD_COMMIT b915719f25)",
  "schedule": "S3 ObjectCreated on eclipse/inflection/bronze/*.json (notification silver-eclipse) + EventBridge opal-assets-silver-eclipse-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands via opal-assets-ingest-mirror (cron(5 13 * * ? *), cron(5 17 * * ? *))",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "earliest_partition": "2026-05-15",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 0,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": ""
 },
 "size": {
  "objects": 137,
  "bytes": 4103927,
  "parts": 137,
  "schema_variants": 1,
  "rows_newest_partition": 18,
  "rows_sum_all_parts": 2466,
  "rows_sampled": 18,
  "claim": "measured",
  "note": "daily snapshot; table row count = newest partition"
 },
 "columns": [
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 28
  },
  {
   "name": "name",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "name (see table notes)",
   "example": "50/50 Opal Intermediate/Opal Long Term"
  },
  {
   "name": "sleeveCount",
   "type": "int64",
   "nullable": true,
   "nulls_in_newest": 14,
   "description": "",
   "example": 1.0
  },
  {
   "name": "portfolioCount",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "portfolios on the model",
   "example": 165
  },
  {
   "name": "source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "Eclipse"
  },
  {
   "name": "hasSubstitute",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "statusId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "status",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "record status",
   "example": "Approved"
  },
  {
   "name": "nameSpace",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "owning namespace",
   "example": "Inflection Wealth Management"
  },
  {
   "name": "currentStatusId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 18,
   "description": "",
   "example": null
  },
  {
   "name": "tags",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 18,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "isDynamic",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "isSubstitutedForPortfolio",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "description",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 1,
   "description": "",
   "example": "50/50 blend of Intermediate and LTC mode"
  },
  {
   "name": "ownerUserId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1120668
  },
  {
   "name": "ownerUser",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "managementStyleId",
   "type": "int64",
   "nullable": true,
   "nulls_in_newest": 5,
   "description": "",
   "example": 2.0
  },
  {
   "name": "managementStyle",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 5,
   "description": "",
   "example": "Aggressive"
  },
  {
   "name": "isCommunityModel",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "communityModelId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 18,
   "description": "",
   "example": null
  },
  {
   "name": "lastSyncDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-05-13T02:31:41.000Z"
  },
  {
   "name": "approvedByUserId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1120668
  },
  {
   "name": "approvedByUser",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "isDeleted",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "createdOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-05-13T02:31:41.000Z"
  },
  {
   "name": "editedOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-10-08T14:50:57.000Z"
  },
  {
   "name": "createdBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "editedBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "hasEditAccess",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "isMAC",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "portfolioFlags",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<json list of account ids and flags>"
  },
  {
   "name": "teams",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<json list of team names>"
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "models.json"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-13"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "eclipse"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "models"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "status": [
   "Approved"
  ],
  "source": [
   "Eclipse"
  ],
  "nameSpace": [
   "Inflection Wealth Management",
   "Opal Capital"
  ],
  "managementStyle": [
   "Balanced",
   "Aggressive",
   "Conservative",
   "Growth",
   null
  ],
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "n/a: firm-level reference table, no account grain",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "n/a",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "models",
  "model list",
  "Eclipse models",
  "model portfolios",
  "IWM models"
 ],
 "common_queries": [
  "What models does Inflection run in Eclipse?",
  "How many portfolios are on each model?"
 ],
 "existing_gateway_tool": {
  "name": "none; mdpf_get_aum_metrics serves per-model AUM from platinum, a different (derived) surface",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "eclipse_list_models",
   "inputs": {
    "firm": "inflection",
    "account_last4": "n/a",
    "platform": "n/a",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "models (id, name, nameSpace, status, managementStyle, portfolioCount) unioned with fact_model_composition rows (modelAUM, security-set targets)",
   "answers": [
    "What models does Inflection run in Eclipse?",
    "How many portfolios are on each model?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "eclipse_inflection_models (proposed, one row for models+composition)",
  "present": false
 },
 "prior_art": "none",
 "open_items": [
  "fact_models (18) and fact_model_composition (9) share only 1 id: the models list is NOT the superset of the composed models; the Opal-namespace models appear only in composition. A tool must union, not join"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of eclipse/inflection/silver/fact_models/date=2026-10-13 (all 37 columns)",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-eclipse; events describe-rule/list-targets-by-rule opal-assets-silver-eclipse-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/eclipse/inflection/meta/backfill-status.json + meta/conversions/20261013T160005Z-e6eaf217.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

### opal-data-assets/silver/eclipse/inflection/fact_model_composition

```json
{
 "contract_id": "opal-data-assets/silver/eclipse/inflection/fact_model_composition",
 "bucket": "opal-data-assets",
 "s3_prefix": "eclipse/inflection/silver/fact_model_composition/",
 "layer": "silver",
 "format": "parquet",
 "table": "fact_model_composition",
 "grain": "one row per composed Eclipse model per snapshot date (9 rows; one bronze model_composition_<id>.json each); modelDetail holds the target tree as a JSON string",
 "partition": {
  "keys": [
   "date"
  ],
  "object": "date=YYYY-MM-DD/data.parquet",
  "claim": "measured",
  "note": "daily snapshot"
 },
 "producer": {
  "name": "opal-assets-silver-eclipse (python3.11, FAMILY=eclipse, OPAL_BUILD_COMMIT b915719f25)",
  "schedule": "S3 ObjectCreated on eclipse/inflection/bronze/*.json (notification silver-eclipse) + EventBridge opal-assets-silver-eclipse-sweep-daily cron(0 16 * * ? *) {\"mode\":\"sweep\"}. Bronze lands via opal-assets-ingest-mirror (cron(5 13 * * ? *), cron(5 17 * * ? *))",
  "source": "infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_conversion.py",
  "claim": "measured"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "earliest_partition": "2026-05-15",
  "t1_frontier": "2026-10-13",
  "trading_days_behind": 0,
  "basis": "trading-day-frontier",
  "claim": "measured",
  "note": ""
 },
 "size": {
  "objects": 137,
  "bytes": 5391157,
  "parts": 137,
  "schema_variants": 1,
  "rows_newest_partition": 9,
  "rows_sum_all_parts": 1233,
  "rows_sampled": 9,
  "claim": "measured",
  "note": "daily snapshot; table row count = newest partition"
 },
 "columns": [
  {
   "name": "id",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 3
  },
  {
   "name": "updateStatus",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "needsUpdate",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "name",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "name (see table notes)",
   "example": "Opal Long Term"
  },
  {
   "name": "description",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 7,
   "description": "",
   "example": "50/50 blend of Intermediate and LTC mode"
  },
  {
   "name": "nameSpace",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "owning namespace",
   "example": "Opal Capital LTC"
  },
  {
   "name": "statusId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "status",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "record status",
   "example": "Approved"
  },
  {
   "name": "currentStatusId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentStatus",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentTags",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentName",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentNameSpace",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentDescription",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "tags",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": "<free text>"
  },
  {
   "name": "ownerUserId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1120668
  },
  {
   "name": "ownerUser",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "managementStyleId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "managementStyle",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "isCommunityModel",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "communityModelId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "isSubstitutedForSleeve",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "lastSyncDate",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2025-08-15T19:36:00.000Z"
  },
  {
   "name": "approvedByUserId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1120668
  },
  {
   "name": "approvedByUser",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "isDynamic",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "isDeleted",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "createdOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2025-08-15T19:36:00.000Z"
  },
  {
   "name": "editedOn",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "2026-08-18T15:49:35.000Z"
  },
  {
   "name": "createdBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "editedBy",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<user name>"
  },
  {
   "name": "hasEditAccess",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 8,
   "description": "",
   "example": "1"
  },
  {
   "name": "macStatus",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "havePendingModel",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "astroEnabled",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "astroTemplateId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "astroUsage",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 3
  },
  {
   "name": "syncToAstro",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "isSMA",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "sleeveSuffix",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 5,
   "description": "",
   "example": "LTC"
  },
  {
   "name": "currentSleeveSuffix",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "optionLevel",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "primeBrokerage",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "marginAgreement",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "orionConnectProductClass",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentOrionConnectProductClass",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "orionConnectRiskCategory",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentOrionConnectRiskCategory",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "currentManagementStyleId",
   "type": "string",
   "nullable": true,
   "nulls_in_newest": 9,
   "description": "",
   "example": null
  },
  {
   "name": "excludeRebalanceSleeve",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": false
  },
  {
   "name": "modelTypeId",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 1
  },
  {
   "name": "modelDetail",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": "<json model tree>"
  },
  {
   "name": "portfolioCount",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "portfolios on the model",
   "example": 0
  },
  {
   "name": "sleeveCount",
   "type": "int64",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": 0
  },
  {
   "name": "modelAUM",
   "type": "double",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "model AUM (USD)",
   "example": 15449473.08
  },
  {
   "name": "canPortfolioAssignToModel",
   "type": "bool",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "",
   "example": true
  },
  {
   "name": "_source_file",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze object the row came from",
   "example": "model_composition_3.json"
  },
  {
   "name": "_source_as_of",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze as-of date",
   "example": "2026-10-13"
  },
  {
   "name": "_source",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "vendor",
   "example": "eclipse"
  },
  {
   "name": "_feed",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "bronze feed",
   "example": "model_composition"
  },
  {
   "name": "_schema_version",
   "type": "string",
   "nullable": false,
   "nulls_in_newest": 0,
   "description": "silver schema version",
   "example": "1.0"
  }
 ],
 "enums": {
  "name": [
   "Opal Long Term",
   "Opal Ultra Long Term",
   "Opal Intermediate Growth",
   "Opal Short Term",
   "Opal Ultra Short Term",
   "Opal Growth SMA",
   "Opal DIV SMA",
   "50/50 Opal Intermediate/Opal Long Term",
   "50/50 Opal Short Term/Intermediate"
  ],
  "modelDetail.children.modelType": [
   "Security Set"
  ],
  "claim": "measured (newest partition)"
 },
 "fork_keys": {
  "firm": {
   "column_or_key_segment": "S3 key segment 2 (<vendor>/<firm>/silver/...): \"inflection\"; no firm column in the rows",
   "values": [
    "inflection"
   ],
   "claim": "measured",
   "note": "only one firm exists under orion/ and eclipse/ (prefix census, 14,313 of 14,313 keys)"
  },
  "account": {
   "column": "n/a: model reference table",
   "last4_derivation": "n/a",
   "last4_collisions_within_firm": null,
   "claim": "measured"
  },
  "platform": {
   "column": "n/a",
   "values": [],
   "claim": "measured"
  }
 },
 "nl_tags": [
  "model composition",
  "model targets",
  "security set",
  "model AUM",
  "blend weights"
 ],
 "common_queries": [
  "What is the target mix of the 50/50 Opal Intermediate/Opal Long Term model?",
  "What is the AUM of each Opal model at Inflection?"
 ],
 "existing_gateway_tool": {
  "name": "none",
  "verdict": "none"
 },
 "proposed_tools": [
  {
   "name": "eclipse_list_models",
   "inputs": {
    "firm": "inflection",
    "account_last4": "n/a",
    "platform": "n/a",
    "as_of": "YYYY-MM-DD"
   },
   "returns": "see fact_models contract; flattens modelDetail to (model, security_set, targetPercent, tolerance)",
   "answers": [
    "What is the target mix of the 50/50 Opal Intermediate/Opal Long Term model?",
    "What is the AUM of each Opal model at Inflection?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "eclipse_inflection_models (proposed)",
  "present": false
 },
 "prior_art": "none",
 "open_items": [
  "the tree stops at the Security Set level (targetPercent per set, e.g. 50.56/49.44); no ticker-level weights exist in any Eclipse silver table. \"What tickers are in model X\" is NOT answerable here (bronze has no security-set feed either: 13 files per date, none a security set)"
 ],
 "evidence": [
  {
   "read": "boto3 list_objects_v2 paginator, Prefix orion/ and eclipse/, 15 pages, 14,313 keys",
   "at": "2026-10-14T12:45Z"
  },
  {
   "read": "pyarrow read_metadata over S3 range reads, 5,542 of 5,542 silver parquet parts",
   "at": "2026-10-14T12:50Z"
  },
  {
   "read": "pandas read of eclipse/inflection/silver/fact_model_composition/date=2026-10-13 (all 61 columns) and a walk of each modelDetail tree",
   "at": "2026-10-14T13:00Z"
  },
  {
   "read": "lambda get-function-configuration + get-policy opal-assets-silver-eclipse; events describe-rule/list-targets-by-rule opal-assets-silver-eclipse-sweep-daily; s3api get-bucket-notification-configuration opal-data-assets",
   "at": "2026-10-14T13:05Z"
  },
  {
   "read": "s3://opal-data-assets/eclipse/inflection/meta/backfill-status.json + meta/conversions/20261013T160005Z-e6eaf217.json",
   "at": "2026-10-14T13:00Z"
  }
 ]
}
```

## (e) What could not be read, and why

- **fact_performance `factor` semantics**: not read. The puller and Orion's definition were not opened inside the budget; the
  value range (median 1.186, min -25.15, max 170.73) does not settle daily return vs growth index. The tool is HELD on it.
- **Whether position values are the prior close**: inferred only. `asOfDate` equals the partition and bronze lands ~13:05Z,
  which fits a T-1 close, but no read established it.
- **Upstream bronze puller** (the API runner writing `s3://opal-data-inf/bronze/...` that `opal-assets-ingest-mirror` copies
  in): not described; only the mirror's two EventBridge rules were read. The mirror also carries a Scheduler target
  (`opal-assets-ingest-mirror-cot-daily-et`, a Cottonwood leg) that was not read.
- **Older partitions' content**: fork-key and collision counts are measured on the NEWEST part of each table only. History
  parts were read for schema (footers, all 5,542) but not for content, except the prior part of the two cumulative tables and
  fact_assets 2026-08-06.
- **Fidelity_LH**: 2 accounts (124 transactions) under a second custodian label; whether it is a separate entity inside the
  Inflection tenancy was not established.
- **`eclipse/inflection/bronze/_history`, `_meta/holes.json`, `eclipse_membership_map`, `reconstructed/`**: counted, not
  contracted (bronze or derived JSON, out of this SILVER scope). The `_history` set (auditlog_model 18, auditlog_portfolio
  18, trade_instances 18, closed_trades 1) is the only place Eclipse trade history exists and has no silver table.
- **Surprise rows**: two are owed and NOT filed (this subagent's write surface is the part file only). For 4.0.0_SA_CRO~Z to
  file on `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`:
  (1) `eclipse/inflection/silver/fact_portfolios_simple` stalled at 2026-10-09 on VendorDriftError (`defaultTradingEngineId`),
  backfill-status guard FAIL missing 4; (2) `orion/inflection` guard FAIL alien 4: silver-only partitions 2026-08-06 and
  2026-09-29 of fact_assets and fact_positions with no bronze object.
- **Open deploy touching this producer**: `org/critical_paths/.open_deploys/nfra-oplgtw-fd2-orion-drain.json` (HELD, leg L3
  open: the 16:00Z orion sweep's dlq_drain record). Read, not acted on; it changes the converter's DLQ handling, not the
  silver schema.
