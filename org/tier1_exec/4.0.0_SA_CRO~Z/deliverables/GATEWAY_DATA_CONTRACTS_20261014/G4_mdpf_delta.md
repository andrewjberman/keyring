# G4 -- opal-data-mdpf: the delta portal-v2 does not already hold (census part for 4.0.0_SA_CRO~Z, 2026-10-14)

Directive: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` section 2 row G4.
Overlap baseline: `../G3_portal_v2.md` (served MDPF set, section "G4 overlap set"). Catalog: `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` @75585f9027. Workspace HEAD at read: 217282fadd.

## 0. Verdict first

**The delta is NOT empty, but it is small, and none of it is the served MDPF figures.**

- **OVERLAP (100%, measured): every gold table opal-data-mdpf holds.** `mdpf/global/gold/{aum_metrics, account_distribution, aggregate_aua_timeseries, account_units}` are the parquet mirror of the global-scope gold JSON in `opal-data-assets/portal/gold/mdpf/global/`, and that JSON is byte-for-value what portal-v2 serves at `platinum/mdpf/global/` (section 3). Andrew's guess holds for the numbers: they are already in portal-v2. No contract is written for these.
- **DELTA: the FEED layer under the gold, plus one reference index.** Portal-v2 holds only firm/model aggregates. It does not hold the account-grain model AUA, the per-model security composition, or the AI security-classification index. Those are contracted below (6 contracts).
- Two delta tables are **delta-but-do-not-serve**: `partner_held_etf/49financial` rolls a 2026-07-23 Schwab RPS value forward (57 trading days old), and `non_model_aua/49financial` is a superseded v0_9 methodology whose figure differs from the served one by about 69M USD. G5 and the platinum timeseries already answer both questions with current values.
- Everything else in the bucket is plumbing (code, diagnostics, telemetry, state), a moved bronze home, or a frozen 2026-06-01 evidence pack.

## (a) Method

| # | read | instrument | denominator |
|---|---|---|---|
| 1 | full listing `s3://opal-data-mdpf` | boto3 `list_objects_v2` paginator, no prefix | 4 pages, **3,248 of 3,248 keys**, 128,408,528 bytes, read 2026-10-14T13:49Z |
| 2 | `s3://opal-data-assets/portal/gold/mdpf/` (the true producer side of portal-v2) | same paginator | 1 page, 808 of 808 keys, 53,686,180 bytes |
| 3 | `s3://opal-data-portal-v2/platinum/mdpf/` | same paginator | 1 page, 558 of 558 keys (matches G3: 18 live + 96 manifests + 444 archive) |
| 4 | Parquet footers, every parquet family in opal-data-mdpf | pyarrow footer read, first + last + every N/10th object | 12 families; 3 to 12 footers each (all 3 for account_units); schema variants counted in the sample |
| 5 | Leaf-level overlap, gold parquet vs gold JSON vs platinum | flatten JSON to dotted paths; compare with parquet `path/value_num/value_text` rows or wide columns | aum_metrics 173 of 173 paths; account_distribution 550 of 550; aggregate_aua_timeseries 17,360 of 17,360 cells (496 dates x 35 columns); account_units count 1 of 1 |
| 6 | Platinum vs gold JSON, same day | flatten both, drop `_provenance` | global aum-metrics 175/175, account-distribution 551/551, aggregate-aua-timeseries 33,376/33,376, inflection aum-metrics 146/146 leaves equal |
| 7 | Feed vs served quantities | group-by sums of newest feed partitions vs platinum fields | 49F: 5 of 5 core models; inflection non_model_aua: 3 dates; partner_held_etf, etf_net_assets: ticker-level vs category-views (no ticker fields in any of 16 platinum per-scope files) |
| 8 | Last-4 collisions | distinct `account_id` in newest partition, last 4 chars | 49F 7,607 accounts; inflection 579 accounts |
| 9 | Producers | `scheduler get-schedule` x7, `events describe-rule` + `list-targets-by-rule` x1, `lambda get-function-configuration` x7, CloudWatch Logs newest streams x3, `comp-find --corpus aws 'mdpf'` | graph: 91 hits across 2,929 nodes (vintage 2026-10-14 13:45:40Z) |
| 10 | Gateway reach | `iam simulate-principal-policy` opal-gateway-role, s3:GetObject | 3 delta keys implicitDeny; positive control `platinum/mdpf/global/aum-metrics.json` allowed |
| 11 | Catalog coverage | grep of DATA_CATALOG.yaml (3,825 lines) | `opal-data-mdpf` 0 lines; `portal/gold/mdpf` 0 lines; `ai_classified`/`etf-classifications` 0 lines; positive control `mdpf_get_aum_metrics` hits |
| 12 | Trading calendar | `lib.trading_calendar` (hardcoded NYSE fallback, warned) | T-1 frontier = 2026-10-13 |

## (b) Prefix census -- s3://opal-data-mdpf (3,248 keys)

| prefix (dataset) | objects | bytes | newest LastModified (UTC) | class |
|---|---|---|---|---|
| `bmkaud-evidence/20260601T1445Z/` (MANIFEST, 2 Bloomberg PKLs, 7 JSON copies of portal benchmarks/peers) | 10 | 25,808,987 | 2026-06-01T14:49:01Z | frozen evidence pack (93 TD); OVERLAP-by-family with portal-v2 `json/benchmarks/`, older vintage |
| `code/` (scripts, config, backfill, diag, shell) | 74 | 2,107,707 | 2026-10-13T13:48:14Z | plumbing (deployed code) |
| `diagnostics/aec-irpt-iam1/` | 3 | 14,808 | 2026-09-12T12:20:06Z | plumbing |
| `mdpf/bronze/orion_model_composition/<date>/` | 1,030 | 8,603,727 | 2026-10-09T12:52:47Z | bronze, MOVED: `code/config/bronze_homes.json` (2026-10-11) now homes it at `opal-data-assets/mdpf/inflection/bronze/orion_model_composition` (G2d) |
| `mdpf/feeds/model_aua_positions/49financial/` | 125 | 43,728,677 | 2026-10-14T03:31:41Z | **DELTA** (account grain) |
| `mdpf/feeds/model_aua_positions/inflection/` | 105 | 1,683,640 | 2026-10-12T12:52:59Z | **DELTA** (account grain) |
| `mdpf/feeds/model_composition/49financial/` | 125 | 1,323,418 | 2026-10-14T03:31:41Z | **DELTA** |
| `mdpf/feeds/model_composition/inflection/` | 105 | 1,136,427 | 2026-10-12T12:52:59Z | **DELTA** |
| `mdpf/feeds/non_model_aua/49financial/` | 100 | 746,730 | 2026-10-12T12:54:12Z | DELTA, do-not-serve (superseded methodology) |
| `mdpf/feeds/non_model_aua/inflection/` | 506 | 3,721,188 | 2026-10-12T12:52:59Z | OVERLAP (value = served, one trading day later label) |
| `mdpf/feeds/partner_held_etf/49financial/` | 293 | 1,532,926 | 2026-10-14T03:30:47Z | DELTA, do-not-serve (57-TD-old RPS rolled forward; G5 holds current) |
| `mdpf/feeds/etf_net_assets/` | 267 | 1,237,357 | 2026-10-12T12:52:58Z | DELTA vs portal-v2; covered upstream by G5/G2d |
| `mdpf/feeds/derivation_manifests/49financial/` | 3 | 12,198 | 2026-07-16T12:09:17Z | plumbing, frozen |
| `mdpf/global/gold/aum_metrics/date=*/` | 36 | 194,392 | 2026-10-14T13:31:50Z | OVERLAP |
| `mdpf/global/gold/account_distribution/date=*/` | 40 | 432,953 | 2026-10-14T13:31:50Z | OVERLAP |
| `mdpf/global/gold/aggregate_aua_timeseries/date=*/` | 45 | 3,072,933 | 2026-10-14T13:31:50Z | OVERLAP |
| `mdpf/global/gold/account_units/date=*/` | 3 | 3,873 | 2026-10-14T13:31:50Z | OVERLAP (count served at `account-distribution.total.account_units`) |
| `mdpf/global/gold/ai_classified_securities/date=*/index.json` | 2 | 743,031 | 2026-10-08T21:31:20Z | **DELTA** (reference, not client data) |
| `mdpf/global/state/taxsma_control/current.json` | 1 | 139 | 2026-10-14T13:31:46Z | plumbing (run status pointer) |
| `telemetry/mdpf-daily-runner/` (accrual-bridge-runs 101, history 131, logs 133, legacy-emit-runs 10, status.json 1) | 376 | 32,301,427 | 2026-10-14T13:40:29Z | plumbing |
| **total** | **3,248** | **128,408,528** | | |

Top-level prefixes measured: exactly 5 (bmkaud-evidence, code, diagnostics, mdpf, telemetry). `gold/`, `silver/`, `platinum/`: 0 keys each in the 3,248-key listing.

## (c) Analysis

### 3. Overlap table (measured)

| opal-data-mdpf table | same quantity in portal-v2? | measurement | verdict |
|---|---|---|---|
| `mdpf/global/gold/aum_metrics` date=2026-10-13 | `platinum/mdpf/global/aum-metrics.json` (period 2026-10-13) | 173 of 173 parquet paths present in the gold JSON; 131 equal values + 42 null-vs-NaN (both empty) = 173/173; the only JSON-only leaves are 11 run-clock fields (`_provenance.*`, `last_updated`), which `mdpf_gold_parquet.py` VOLATILE_KEYS drops by design. Gold JSON vs platinum: 175/175 equal | OVERLAP |
| `mdpf/global/gold/account_distribution` date=2026-10-14 | `platinum/mdpf/global/account-distribution.json` (period 2026-10-14) | 550 of 550 paths; 548 equal + 2 null-vs-NaN. Gold JSON vs platinum: 551/551 | OVERLAP |
| `mdpf/global/gold/aggregate_aua_timeseries` date=2026-10-13 | `platinum/mdpf/global/aggregate-aua-timeseries.json` | 496 dates (2024-11-01..2026-10-13) x 35 series columns = 17,360 of 17,360 cells equal. Gold JSON vs platinum: 33,376/33,376 leaves | OVERLAP |
| `mdpf/global/gold/account_units` date=2026-10-14 | `platinum/mdpf/global/account-distribution.json` `total.account_units.count` | parquet count 8,493 = platinum 8,493, same basis text, same value_date 2026-10-14 | OVERLAP |
| `mdpf/feeds/model_aua_positions/49financial` 2026-10-14 | `platinum/mdpf/49financial/aum-metrics.json` by_model (period 2026-10-13) | sums by model_key vs platinum aum, 5 of 5 core models: diffs -0.85, +849.15, -8,267.77, -14.74, -10.32 USD (max 0.003%). Feed label D carries served period D-1: gold 2026-10-12 matched feed 2026-10-13 (sum abs diff 374.72) and gold 2026-10-13 matched feed 2026-10-14 (9,142.84) | aggregate = OVERLAP; **account grain = DELTA** (no platinum file carries an account id: 0 `account_id` paths across 16 per-scope files) |
| `mdpf/feeds/model_aua_positions/inflection` | same, inflection scope | not value-compared (feed last label 2026-10-12, behind the served period) | aggregate = OVERLAP (inferred, same writer path); account grain = DELTA |
| `mdpf/feeds/model_composition/{49financial,inflection}` | none in `platinum/mdpf/` (0 `ticker` or `target_weight` paths in 16 files); `json/benchmarks/model_portfolio_benchmarks.json` holds Yang model-design RETURNS and benchmark-ETF compositions (UST..ULT), not the as-implemented model holdings | field-level: no `ticker`/`target_weight` leaf in any served MDPF file | **DELTA** |
| `mdpf/feeds/non_model_aua/inflection` 2026-10-12 | `platinum/mdpf/inflection/aggregate-aua-timeseries.json` `non_model_aua[]` | 60,781,893.12 = served value at 2026-10-09 (exact). Feed label 2026-10-12 = served date 2026-10-09 (one trading day earlier) | OVERLAP |
| `mdpf/feeds/non_model_aua/49financial` 2026-10-12 | `platinum/mdpf/49financial/aggregate-aua-timeseries.json` `non_model_aua[]` | feed 238,687,767.34 (v0_9, "straight RPS custody minus SmartX model"); served 2026-10-09..10-13 = 306.3M..313.4M (C2 spec: `net_mv_plus_cash`). The feed value appears nowhere in the served series or the gold JSON | DIVERGENT: DELTA, do-not-serve |
| `mdpf/feeds/partner_held_etf/49financial` 2026-10-14 | `category-views.json` ETF Strategies: IDVZ/PFDE member `aum` = null for 49F; no DIVZ/PFOE held-value leaf | feed DIVZ 180.28M with `rps_date_used` 20260723 on every recent partition; G5 `opal-data-etfs daily/49financial/` holds 49F DIVZ ~187M on 2026-10-13 with source_as_of = date | DELTA vs portal-v2; superseded by G5 |
| `mdpf/feeds/etf_net_assets` 2026-10-12 | none in portal-v2 MDPF; G5 contracts fund net assets / NAV / shares (proposed `etfs_get_fund_nav_history`) | 4 tickers; source trueshares/filepoint, the same issuer files G2d and G5 census | DELTA vs portal-v2; covered upstream |
| `mdpf/global/gold/ai_classified_securities` | none (no portal-v2 key, no catalog row) | 2,303 entries in the 2026-10-08 index | **DELTA** |

### 3.1 Where the served numbers are really produced (open item for the CRO)

- **Chain, measured:** `mdpf-gold-lambda` (`mdpf_gold_consolidator`, schedule `mdpf-scheduled-floor` cron(30 13 * * ? *) UTC) writes the legacy per-scope JSON to `s3://opal-data-assets/portal/gold/mdpf/<scope>/<leaf>/<date>.json`. `opal-assets-mdpf-portal-publisher` (schedule cron(50 13 * * ? *) UTC; env GOLD_BUCKET=opal-data-assets, GOLD_ROOT=portal/gold/mdpf, SERVE_BUCKET=opal-data-portal-v2, SERVE_ROOT=platinum/mdpf) copies the latest to platinum. Today's publish landed 2026-10-14T13:50:52-53Z.
- The same Lambda writes the dated parquet mirror (`data/mdpf/scripts/gold/mdpf_gold_parquet.py`, "THE ONE WRITER of the new gold") at `lib/opal_naming.address("mdpf", scope, "gold", ...)`. Only the `global` scope lands in opal-data-mdpf. Firm scopes land in **`s3://opal-data-49financial/mdpf/49financial/gold/`** (165 keys, plus `taxsma_assets/` 14), **`s3://opal-data-inflection/mdpf/inflection/gold/`** (165), and **`s3://opal-data-cottonwood/mdpf/cottonwood/gold/`** (169, plus `taxsma_assets/` 14). All were listed in full, and their newest objects are dated 2026-10-14T13:31:4xZ.
- **Coverage gap:** no census group owns `opal-data-assets/portal/gold/mdpf/` (808 keys). G2d classed it "G3/G4 territory", and G3 measured only platinum. The three per-firm buckets above are not named in any group row either. The latest date is OVERLAP (measured, section 3). What they add is **dated history** per scope (for example 45 dated aum-metrics files for global, 27 dated category-views for 49F), which platinum does not keep. The `taxsma_assets` gold for 49F and Cottonwood is uncensused.

### 3.2 What the delta tables are, and the questions they answer

- **model_aua_positions** (client data, account grain): one row per account per day with the canonical Opal `model_key`, `cohort_class` (model/sma) and `model_value`. 49F comes from SmartX and Inflection from Eclipse (`source_pipeline`). It feeds `dim_mdpf_account_distribution.py` (the served histograms) and the 49F non-model residual. Questions: "Which model is account ...1234 in, and how much is in it?" "List 49F accounts in Ultra-Short Term over 1M." Portal-v2 can answer neither.
- **model_composition**: one row per (firm, model, ticker) with `target_weight`, `product_class` and `is_opal_etf`. It is the as-implemented model holdings per platform. Questions: "What does 49F's Long Term model hold?" "Which Opal ETFs are in Inflection's Intermediate model, and at what weight?"
- **ai_classified_securities**: the listing of the security-classification rows the AI leg landed (`classified_by = model`, with confidence). The canonical table is DynamoDB `etf-classifications` (`org/standards/MDPF_SECCLASS_CONTRACT.json`). Questions: "Which classifications are model-made and low-confidence?" A tool should read the canonical table, with this index as provenance.
- **partner_held_etf / non_model_aua(49F)**: contracted so they are on record, with a verdict of no tool. Current answers come from G5 `etfs_get_partner_ownership` and from `mdpf_get_aggregate_aua`.
- **etf_net_assets**: contracted, with no new tool. G5's proposed `etfs_get_fund_nav_history` reads the issuer silver that this feed copies.

### 3.3 Existing gateway mdpf tools (`DATA_CATALOG.yaml` tool_index, member a, `app/integrations/portal_index/integration.py:361-378`)

| tool | reads | verdict | why |
|---|---|---|---|
| `mdpf_get_aum_metrics` | `platinum/mdpf/{scope}/aum-metrics.json` | **KEEP; optional EXTEND** with `as_of` reading the dated gold (section 3.1) | opal-data-mdpf adds no new figure. The only gain is history by date, which lives in the dated gold, not in opal-data-mdpf. Any extension is a never-widen read grant |
| `mdpf_get_account_distribution` | `platinum/mdpf/{scope}/account-distribution.json` | **KEEP; optional EXTEND** as above | same |
| `mdpf_get_aggregate_aua` | `platinum/mdpf/{scope}/aggregate-aua-timeseries.json` | **KEEP** | already full history (496 dates global) |
| `mdpf_get_model_benchmarks` | `json/benchmarks/model_portfolio_benchmarks.json` | **KEEP** | model-design returns. It does not answer "what does the model hold"; `mdpf_get_model_composition` (new) does |

**Proposed new tools: 2.** `mdpf_get_account_model_aua` (firm-forked, account last-4 with a candidate list) and `mdpf_get_model_composition` (firm-forked). Both need a never-widen read grant on `opal-data-mdpf/mdpf/feeds/` (simulated implicitDeny today). A third tool, `mdpf_get_security_classification`, is proposed against the canonical DynamoDB table. It is outside this bucket and listed as an open item.

## (d) Contracts (DELTA tables only)

```json
{
 "contract_id": "opal-data-mdpf/feeds/model_aua_positions_49financial",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/feeds/model_aua_positions/49financial/",
 "layer": "silver",
 "format": "parquet",
 "table": "model_aua_positions (49financial)",
 "grain": "one row per (account_id, as_of_date); each daily file is a full snapshot of model-enrolled accounts",
 "partition": {"keys": ["file name <YYYY-MM-DD>.parquet (pull date; the values are the previous trading day's, see freshness)"], "claim": "measured"},
 "producer": {"name": "Lambda wsb-49f-model-aua-daily (lambda_function.lambda_handler, python3.11; code infra/aws/lambda/mdpf-pipeline/wsb-49f-model-aua-daily/)", "schedule": "EventBridge Scheduler wsb-49f-model-aua-pull-daily cron(30 3 ? * TUE-SAT *) UTC", "claim": "measured (schedule target + log stream 2026-10-14T03:31:40Z = object LastModified 03:31:41Z)"},
 "freshness": {"latest_partition": "2026-10-14", "basis": "trading-day-frontier", "lag_trading_days": 0, "value_date_of_latest": "2026-10-13 (feed 2026-10-14 sums match served period 2026-10-13 within 9,142.84 USD over 5 models; feed 2026-10-13 matches gold 2026-10-12)", "claim": "measured"},
 "size": {"objects": 125, "first_partition": "2026-05-18", "bytes": 43728677, "rows_sampled": 7607, "rows_newest_partition": 7607, "schema_variants_in_sample": 1, "footers_sampled": 12, "claim": "measured"},
 "columns": [
  {"name": "firm_id", "type": "string", "nullable": false, "description": "firm scope", "example": "49financial"},
  {"name": "partner_name", "type": "string", "nullable": false, "description": "partner display name (1 distinct value)", "example": "<partner name>"},
  {"name": "model_key", "type": "string", "nullable": false, "description": "canonical Opal model key (7 distinct)", "example": "opal_long_term_conservative"},
  {"name": "model_key_unmapped", "type": "null", "nullable": true, "description": "source model key when unmapped; all null for 49F", "example": null},
  {"name": "cohort_class", "type": "string", "nullable": false, "description": "model or sma", "example": "model"},
  {"name": "account_id", "type": "string", "nullable": false, "description": "SmartX account UUID (36 chars; 7,607 of 7,607 UUID-shaped), NOT a custodian account number", "example": "<uuid>****"},
  {"name": "household_id", "type": "null", "nullable": true, "description": "all null for 49F", "example": null},
  {"name": "as_of_date", "type": "string", "nullable": false, "description": "pull date label (= file date)", "example": "2026-10-14"},
  {"name": "model_value", "type": "double", "nullable": false, "description": "USD value of the account in the model; 3 rows <= 0", "example": "123456.78"},
  {"name": "custodian", "type": "null", "nullable": true, "description": "all null for 49F (custodian is Schwab, inferred from the firm's estate)", "example": null},
  {"name": "source_pipeline", "type": "string", "nullable": false, "description": "upstream platform", "example": "smartx"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "write time", "example": "2026-10-14T03:31:41Z"}
 ],
 "enums": {"model_key": ["opal_ultra_short_term", "opal_short_term", "opal_intermediate", "opal_long_term_conservative", "opal_long_term_aggressive", "opal_growth_sma", "opal_div_sma"], "cohort_class": ["model", "sma"], "source_pipeline": ["smartx"]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "key segment 4 mdpf/feeds/model_aua_positions/<firm>/ and column firm_id", "values": ["49financial"]},
  "account": {"column": "account_id", "last4_derivation": "last 4 chars of the SmartX UUID. This is NOT the custodian account number's last 4, so a user's '...1234' needs the SmartX account map crosswalk (G2c smartx_fact_allocation_account_map) first", "last4_collisions_within_firm": 409, "last4_collision_detail": "7,607 accounts -> 7,185 distinct UUID last-4; 409 last-4 values shared by 831 accounts (measured 2026-10-14 partition)"},
  "platform": {"column": "source_pipeline", "values": ["smartx"]}
 },
 "nl_tags": ["account model AUA", "which model is an account in", "accounts by model", "model enrolment", "49 Financial model accounts"],
 "common_queries": ["Which model is 49F account ...1234 in and how much is in it?", "List 49F accounts in Ultra-Short Term above 1M USD", "How many 49F accounts moved into the Long Term model since 2026-09-30?"],
 "existing_gateway_tool": {"name": "mdpf_get_account_distribution (aggregate histograms only)", "verdict": "keep"},
 "proposed_tools": [{"name": "mdpf_get_account_model_aua", "inputs": {"firm": "49financial (REQUIRED, one firm)", "account_last4": "custodian last-4 resolved through the SmartX account map; returns a candidate list when more than one account matches", "platform": "smartx (implicit)", "as_of": "served date D (reads file D+1 trading day) or latest"}, "returns": "rows {account ref masked to last-4, model_key, cohort_class, model_value, value_date} for ONE firm", "answers": ["Which model is 49F account ...1234 in and how much is in it?", "List 49F accounts in Ultra-Short Term above 1M USD"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py; data/mdpf/scripts/gold/dim_mdpf_account_distribution.py (consumer) @217282fadd",
 "open_items": ["the file date is one trading day ahead of the value date (measured twice); a tool must translate it or it will answer the wrong day", "account_id is a SmartX UUID: last-4 lookup needs the SmartX account map (G2c)", "gateway opal-gateway-role s3:GetObject = implicitDeny (simulated): a never-widen read grant is required", "upstream overlap with G2c smartx silver (fact_account_allocations / fact_allocation_*) is inferred, not value-measured"],
 "evidence": [{"read": "list_objects_v2 s3://opal-data-mdpf (3,248 keys)", "at": "2026-10-14T13:49Z"}, {"read": "get mdpf/feeds/model_aua_positions/49financial/2026-10-12,13,14.parquet; group-by model_key vs platinum/mdpf/49financial/aum-metrics.json and opal-data-assets gold 2026-10-12/13", "at": "2026-10-14T14:0xZ"}, {"read": "scheduler get-schedule wsb-49f-model-aua-pull-daily; logs describe-log-streams /aws/lambda/wsb-49f-model-aua-daily", "at": "2026-10-14T14:0xZ"}]
}
```

```json
{
 "contract_id": "opal-data-mdpf/feeds/model_aua_positions_inflection",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/feeds/model_aua_positions/inflection/",
 "layer": "silver",
 "format": "parquet",
 "table": "model_aua_positions (inflection)",
 "grain": "one row per (account_id, as_of_date); full daily snapshot",
 "partition": {"keys": ["file name <YYYY-MM-DD>.parquet (run date)"], "claim": "measured"},
 "producer": {"name": "mdpf-daily-runner EC2 i-02448edb624a7a7cf feeder chain (data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py), dispatched by Lambda mdpf-feeder-trigger", "schedule": "Scheduler mdpf-feeder-backstop-daily cron(52 12 * * ? *) UTC + EventBridge rule mdpf-feeder-accelerator (S3 Object Created opal-data-inf gold/meta/pipeline-complete.json); dispatches only when s3://opal-data-inf/gold/eclipse/<run_date>/_meta/gold_complete.json exists", "claim": "measured (schedule, rule, Lambda env RUNNER_INSTANCE_ID, log events)"},
 "freshness": {"latest_partition": "2026-10-12", "basis": "trading-day-frontier", "lag_trading_days": 1, "note": "feeder-trigger logged NOT-YET on 2026-10-13 (12:52Z, 13:00Z) and 2026-10-14 (12:52Z, 12:53Z): the inf gold_complete marker for the run date was absent, so no partition was written for 2026-10-13 or 2026-10-14", "claim": "measured"},
 "size": {"objects": 105, "first_partition": "2026-05-18", "bytes": 1683640, "rows_newest_partition": 579, "schema_variants_in_sample": 1, "footers_sampled": 12, "claim": "measured"},
 "columns": [
  {"name": "firm_id", "type": "string", "nullable": false, "description": "firm scope", "example": "inflection"},
  {"name": "partner_name", "type": "string", "nullable": false, "description": "partner display name (1 distinct)", "example": "<partner name>"},
  {"name": "model_key", "type": "string", "nullable": false, "description": "canonical Opal model key (7 distinct in newest)", "example": "opal_intermediate"},
  {"name": "model_key_unmapped", "type": "string", "nullable": true, "description": "source model key when unmapped (0 non-null in newest)", "example": null},
  {"name": "cohort_class", "type": "string", "nullable": false, "description": "model (579 of 579 in newest)", "example": "model"},
  {"name": "account_id", "type": "string", "nullable": false, "description": "Eclipse account id: 562 of 579 digits-only, lengths 2-14", "example": "****"},
  {"name": "household_id", "type": "string", "nullable": true, "description": "household id; 260 distinct, 2.9% null", "example": "<id>"},
  {"name": "as_of_date", "type": "timestamp[ns]", "nullable": false, "description": "date label (TYPE DIFFERS from 49F, which is string)", "example": "2026-10-12"},
  {"name": "model_value", "type": "double", "nullable": false, "description": "USD value in the model", "example": "123456.78"},
  {"name": "custodian", "type": "string", "nullable": true, "description": "custodian label; 562 Fidelity_Inflection, 17 null", "example": "Fidelity_Inflection"},
  {"name": "source_pipeline", "type": "string", "nullable": false, "description": "upstream platform", "example": "eclipse"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "write time", "example": "2026-10-12T12:52:5xZ"}
 ],
 "enums": {"cohort_class": ["model"], "source_pipeline": ["eclipse"], "custodian": ["Fidelity_Inflection", null]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "key segment 4 and column firm_id", "values": ["inflection"]},
  "account": {"column": "account_id", "last4_derivation": "last 4 chars of the Eclipse account id; 562 ids are 2-4 chars, so for them last-4 is the whole id. Whether this id is the custodian account number is not measured", "last4_collisions_within_firm": 2, "last4_collision_detail": "579 accounts -> 577 distinct last-4; 2 values shared by 4 accounts (2026-10-12 partition)"},
  "platform": {"column": "source_pipeline + custodian", "values": ["eclipse / Fidelity_Inflection"]}
 },
 "nl_tags": ["account model AUA", "Inflection model accounts", "accounts by model", "household model value"],
 "common_queries": ["Which model is Inflection account ...1234 in?", "How much does household <id> hold across Opal models at Inflection?"],
 "existing_gateway_tool": {"name": "mdpf_get_account_distribution (aggregate only)", "verdict": "keep"},
 "proposed_tools": [{"name": "mdpf_get_account_model_aua", "inputs": {"firm": "inflection (REQUIRED, one firm)", "account_last4": "last-4 of the Eclipse id; candidate list on collision", "platform": "eclipse/Fidelity (implicit)", "as_of": "date or latest"}, "returns": "rows {account ref masked, household ref masked, model_key, model_value, as_of} for ONE firm", "answers": ["Which model is Inflection account ...1234 in?"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py @217282fadd",
 "open_items": ["no partition for 2026-10-13 or 2026-10-14 (feeder NOT-YET), yet platinum inflection aggregate-aua-timeseries carries 2026-10-13: the served gold reads inflection from another source now (inferred), so this feed may no longer be load-bearing for the served figure", "gateway read = implicitDeny (simulated on the sibling model_composition/inflection key)", "upstream overlap with G2b eclipse/inflection silver: inferred, not measured"],
 "evidence": [{"read": "get mdpf/feeds/model_aua_positions/inflection/2026-10-12.parquet (ids profiled, never printed)", "at": "2026-10-14T14:1xZ"}, {"read": "logs get-log-events /aws/lambda/mdpf-feeder-trigger newest 3 streams", "at": "2026-10-14T14:0xZ"}]
}
```

```json
{
 "contract_id": "opal-data-mdpf/feeds/model_composition",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/feeds/model_composition/<firm>/",
 "layer": "silver",
 "format": "parquet",
 "table": "model_composition (firm dimension declared: 49financial, inflection)",
 "grain": "one row per (firm_id, model_key, ticker, as_of_date); full daily snapshot per firm",
 "partition": {"keys": ["key segment 4 <firm>", "file name <YYYY-MM-DD>.parquet"], "claim": "measured"},
 "producer": {"name": "49financial: Lambda wsb-49f-model-aua-daily (same write second as model_aua_positions); inflection: mdpf-daily-runner feeder chain via mdpf-feeder-trigger", "schedule": "49F cron(30 3 ? * TUE-SAT *) UTC; inflection cron(52 12 * * ? *) UTC backstop + S3-event accelerator", "claim": "measured for the schedules; the 49F writer is inferred from identical LastModified 03:31:41Z"},
 "freshness": {"latest_partition": "49financial 2026-10-14 (0 TD); inflection 2026-10-12 (1 TD)", "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 230, "objects_by_firm": {"49financial": 125, "inflection": 105}, "bytes": 2459845, "rows_newest_partition": {"49financial": 130, "inflection": 171}, "schema_variants_in_sample": {"49financial": 1, "inflection": 1}, "footers_sampled": 24, "claim": "measured"},
 "columns": [
  {"name": "firm_id", "type": "string", "nullable": false, "description": "firm scope", "example": "49financial"},
  {"name": "model_key", "type": "string", "nullable": false, "description": "canonical Opal model key", "example": "opal_long_term_conservative"},
  {"name": "as_of_date", "type": "string (49F) | timestamp[ns] (inflection)", "nullable": false, "description": "date label; type differs by firm", "example": "2026-10-14"},
  {"name": "ticker", "type": "string", "nullable": false, "description": "security ticker", "example": "DIVZ"},
  {"name": "security_name", "type": "string", "nullable": true, "description": "security name", "example": "<security name>"},
  {"name": "product_class", "type": "string", "nullable": true, "description": "platform-specific class vocabulary (see enums)", "example": "equity"},
  {"name": "target_weight", "type": "double", "nullable": false, "description": "model target weight as a fraction; sums to 1.0 per model (measured, every model, both firms)", "example": "0.05"},
  {"name": "actual_weight", "type": "null (49F) | double (inflection)", "nullable": true, "description": "0% populated in both newest partitions", "example": null},
  {"name": "is_opal_etf", "type": "bool", "nullable": false, "description": "true for Opal-issued ETFs", "example": "true"},
  {"name": "source_pipeline", "type": "string", "nullable": false, "description": "upstream platform", "example": "smartx"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "write time", "example": "2026-10-14T03:31:41Z"}
 ],
 "enums": {"model_key_49financial": ["opal_ultra_short_term", "opal_short_term", "opal_intermediate", "opal_long_term_conservative", "opal_long_term_aggressive", "opal_growth_sma", "opal_div_sma"], "model_key_inflection_extra": ["opal_blend_5050_int_ltc", "opal_blend_5050_st_int"], "product_class_49financial": ["equity", "cash"], "product_class_inflection": ["LV", "LG", "MS-FB", "MS-LB", "MS-HY", "MS Style 4", "Cash or Equivalent", "MS-CI", "MS-UB", "MS-GS", "MS Style 5", "MS-FV", "MS-CS", "MS Style 2", "MS-EM", "MS-IS", "MS-S1", "MS-TW", "MS-MB", "MS Style 8"], "is_opal_etf_tickers_49financial": ["DIVZ", "IDVZ", "PFDE", "PFOE"], "source_pipeline": ["smartx", "eclipse"]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "key segment 4 and column firm_id", "values": ["49financial", "inflection"]},
  "account": {"column": "none -- model level, no account", "last4_derivation": "n/a", "last4_collisions_within_firm": null},
  "platform": {"column": "source_pipeline", "values": ["smartx (49financial)", "eclipse (inflection)"]}
 },
 "nl_tags": ["model holdings", "model composition", "what does the model hold", "model target weights", "Opal ETFs in models"],
 "common_queries": ["What does 49F's Long Term model hold and at what weights?", "Which Opal ETFs are in Inflection's Intermediate model?", "How did the Short Term model's DIVZ weight change since 2026-09-01?"],
 "existing_gateway_tool": {"name": "mdpf_get_model_benchmarks (returns, not holdings)", "verdict": "keep"},
 "proposed_tools": [{"name": "mdpf_get_model_composition", "inputs": {"firm": "49financial|inflection (REQUIRED, one)", "account_last4": "n/a", "platform": "implicit from firm", "as_of": "date or latest", "model_key": "optional"}, "returns": "rows {model_key, ticker, security_name, product_class, target_weight, is_opal_etf, as_of} for ONE firm", "answers": ["What does 49F's Long Term model hold and at what weights?", "Which Opal ETFs are in Inflection's Intermediate model?"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py; data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py @217282fadd",
 "open_items": ["product_class vocabularies differ by platform (equity/cash vs Morningstar-style codes): a tool must not merge them unlabelled", "Cottonwood has no feed here (its model data is Black Diamond, G2a)", "upstream overlap with G2c smartx_fact_model_holdings and G2b eclipse fact_model_composition: inferred, not value-measured", "gateway read = implicitDeny (simulated)"],
 "evidence": [{"read": "get mdpf/feeds/model_composition/49financial/2026-10-14.parquet, inflection/2026-10-12.parquet; footers x24", "at": "2026-10-14T13:5xZ"}, {"read": "flatten 16 platinum/mdpf per-scope files: 0 ticker/target_weight leaves; get json/benchmarks/model_portfolio_benchmarks.json (models[] = returns, etf_compositions = benchmark ETFs)", "at": "2026-10-14T14:0xZ"}]
}
```

```json
{
 "contract_id": "opal-data-mdpf/feeds/partner_held_etf_49financial",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/feeds/partner_held_etf/49financial/",
 "layer": "silver",
 "format": "parquet",
 "table": "partner_held_etf (49financial)",
 "grain": "one row per (Opal ETF ticker, as_of_date); 4 rows per file",
 "partition": {"keys": ["file name <YYYY-MM-DD>.parquet (calendar-daily, 293 files since 2026-01-19)"], "claim": "measured"},
 "producer": {"name": "Lambda wsd-49f-partner-held-etf-daily (reads s3://opal-data-bd/schwab/silver/rps/date=<latest on or before as_of>/data.parquet; rolls the latest RPS forward)", "schedule": "Scheduler wsd-49f-partner-held-etf-pull-daily cron(30 3 ? * TUE-SAT *) UTC", "claim": "measured (schedule + code infra/aws/lambda/mdpf-pipeline/wsd-49f-partner-held-etf-daily/wsd_partner_held_etf.py:72-73)"},
 "freshness": {"latest_partition": "2026-10-14", "basis": "trading-day-frontier", "lag_trading_days": 0, "value_date": "2026-07-23 (rps_date_used on 2026-10-13 and 2026-10-14) = 57 trading days behind T-1", "claim": "measured"},
 "size": {"objects": 293, "bytes": 1532926, "rows_newest_partition": 4, "schema_variants_in_sample": 1, "claim": "measured"},
 "columns": [
  {"name": "firm_id", "type": "string", "nullable": false, "description": "firm", "example": "49financial"},
  {"name": "ticker", "type": "string", "nullable": false, "description": "Opal ETF", "example": "DIVZ"},
  {"name": "as_of_date", "type": "timestamp[ns]", "nullable": false, "description": "requested date", "example": "2026-10-14"},
  {"name": "rps_date_used", "type": "string", "nullable": false, "description": "Schwab RPS date actually valued (YYYYMMDD)", "example": "20260723"},
  {"name": "held_value", "type": "double", "nullable": false, "description": "USD held across 49F accounts", "example": "1.80e8"},
  {"name": "account_count", "type": "int64", "nullable": false, "description": "accounts holding the ETF (count only)", "example": "5555"},
  {"name": "source_pipeline", "type": "string", "nullable": false, "description": "source", "example": "schwab_rps"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "write time", "example": "2026-10-14T03:30:4xZ"}
 ],
 "enums": {"ticker": ["DIVZ", "IDVZ", "PFDE", "PFOE"], "source_pipeline": ["schwab_rps"]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "key segment 4 and firm_id", "values": ["49financial"]},
  "account": {"column": "none (account_count only)", "last4_derivation": "n/a", "last4_collisions_within_firm": null},
  "platform": {"column": "source_pipeline", "values": ["schwab_rps"]}
 },
 "nl_tags": ["partner ETF holdings", "how much DIVZ does 49F hold"],
 "common_queries": ["How much DIVZ does 49 Financial hold?"],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "routing": "answer with G5 etfs_get_partner_ownership (opal-data-etfs daily/<partner>/, source_as_of = date on 1,424 of 1,424 rows per G5); do NOT build a tool on this feed",
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "data/mdpf/scripts/feeders/wsd_partner_held_etf.py; ../G5_etfs.md etfs_get_partner_ownership contract",
 "open_items": ["SURPRISE CANDIDATE: the feed writes a fresh date label every day over a 2026-07-23 valuation (57 TD), because its RPS source opal-data-bd/schwab/silver/rps has no newer partition; 49F DIVZ 180.28M here vs about 187M on 2026-10-13 in G5", "retire-or-repoint candidate: the RPS home moved to opal-data-assets/schwab/08242234/silver (49-schwab-conv skill)"],
 "evidence": [{"read": "get mdpf/feeds/partner_held_etf/49financial/2026-10-13,14.parquet", "at": "2026-10-14T14:0xZ"}, {"read": "get platinum/mdpf/{49financial,global}/category-views.json ETF Strategies nodes", "at": "2026-10-14T14:0xZ"}]
}
```

```json
{
 "contract_id": "opal-data-mdpf/feeds/etf_net_assets",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/feeds/etf_net_assets/",
 "layer": "silver",
 "format": "parquet",
 "table": "etf_net_assets",
 "grain": "one row per (Opal ETF ticker, issuer as_of_date); 2 to 4 rows per file",
 "partition": {"keys": ["file name <YYYY-MM-DD>.parquet (267 files since 2026-01-19)"], "claim": "measured"},
 "producer": {"name": "mdpf-daily-runner feeder chain (data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py) via mdpf-feeder-trigger", "schedule": "cron(52 12 * * ? *) UTC backstop + S3-event accelerator; NOT-YET on 2026-10-13 and 2026-10-14", "claim": "measured (schedule, logs); writer script inferred from repo grep"},
 "freshness": {"latest_partition": "2026-10-12", "basis": "trading-day-frontier", "lag_trading_days": 1, "value_dates": "DIVZ/IDVZ 2026-10-09 (2 TD), PFDE/PFOE 2026-10-12 (1 TD)", "claim": "measured"},
 "size": {"objects": 267, "bytes": 1237357, "rows_newest_partition": 4, "schema_variants_in_sample": 1, "claim": "measured"},
 "columns": [
  {"name": "ticker", "type": "string", "nullable": false, "description": "Opal ETF", "example": "PFDE"},
  {"name": "as_of_date", "type": "timestamp[ns]", "nullable": false, "description": "issuer file date", "example": "2026-10-12"},
  {"name": "net_assets", "type": "double", "nullable": false, "description": "fund net assets USD", "example": "172174500.0"},
  {"name": "nav", "type": "double", "nullable": false, "description": "NAV per share", "example": "28.648"},
  {"name": "shares_outstanding", "type": "double", "nullable": false, "description": "shares outstanding", "example": "6010000.0"},
  {"name": "source", "type": "string", "nullable": false, "description": "issuer/administrator file", "example": "filepoint"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "write time", "example": "2026-10-12T12:52:57Z"}
 ],
 "enums": {"ticker": ["DIVZ", "IDVZ", "PFDE", "PFOE"], "source": ["trueshares", "filepoint"]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "none -- Opal fund level, not client data", "values": ["opal-internal"]},
  "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null},
  "platform": {"column": "source", "values": ["trueshares", "filepoint"]}
 },
 "nl_tags": ["ETF AUM", "fund net assets", "NAV", "shares outstanding"],
 "common_queries": ["What were PFDE's net assets on 2026-10-12?"],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "routing": "answer with G5's proposed etfs_get_fund_nav_history (issuer silver, fresher and wider); no tool on this feed",
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py; ../G5_etfs.md; parts/G2d_schwab_and_other.md (trueshares/filepoint silver)",
 "open_items": ["calendar-daily file label over business-day issuer dates: two tickers are 2 TD behind in the newest file"],
 "evidence": [{"read": "get mdpf/feeds/etf_net_assets/2026-10-12.parquet; footers x12", "at": "2026-10-14T14:0xZ"}]
}
```

```json
{
 "contract_id": "opal-data-mdpf/feeds/non_model_aua",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/feeds/non_model_aua/<firm>/",
 "layer": "silver",
 "format": "parquet",
 "table": "non_model_aua (firm dimension declared: 49financial, inflection)",
 "grain": "one row per (firm_id, as_of_date)",
 "partition": {"keys": ["key segment 4 <firm>", "file name <YYYY-MM-DD>.parquet"], "claim": "measured"},
 "producer": {"name": "mdpf-daily-runner feeder chain: 49F build_mdpf_wse_49f_non_model_aua.py (WS-E); inflection build_mdpf_wsc_inflection_feeder.py (WS-C)", "schedule": "cron(52 12 * * ? *) UTC backstop + accelerator; NOT-YET 2026-10-13 and 2026-10-14", "claim": "measured (schedule, logs); writer scripts inferred from repo grep"},
 "freshness": {"latest_partition": "2026-10-12 (both firms)", "basis": "trading-day-frontier", "lag_trading_days": 1, "claim": "measured"},
 "size": {"objects": 606, "objects_by_firm": {"49financial": 100, "inflection": 506}, "first_partition": {"49financial": "2026-05-18", "inflection": "2024-11-01"}, "bytes": 4467918, "rows_per_file": 1, "schema_variants_in_sample": {"49financial": 2, "inflection": 2}, "claim": "measured"},
 "columns": [
  {"name": "firm_id", "type": "string", "nullable": false, "description": "firm", "example": "inflection"},
  {"name": "as_of_date", "type": "timestamp[ns]", "nullable": false, "description": "date label", "example": "2026-10-12"},
  {"name": "non_model_aua", "type": "double", "nullable": false, "description": "custody total minus model and SMA AUA", "example": "60781893.12"},
  {"name": "partner_custody_total", "type": "double", "nullable": false, "description": "custody total used", "example": "2.08e8"},
  {"name": "model_aua_input", "type": "double", "nullable": false, "description": "model AUA subtracted", "example": "1.47e8"},
  {"name": "sma_aua_input", "type": "double", "nullable": false, "description": "SMA AUA subtracted", "example": "0.0"},
  {"name": "method", "type": "string", "nullable": false, "description": "method tag", "example": "inflection_client_performance_spine_minus_opal_model_and_sma"},
  {"name": "custody_scope", "type": "string", "nullable": false, "description": "custody basis", "example": "client_performance_daily_spine"},
  {"name": "methodology_version", "type": "string", "nullable": true, "description": "49F only, newer variant", "example": "v0_9"},
  {"name": "source_pipeline", "type": "string", "nullable": false, "description": "source", "example": "client_performance_spine"},
  {"name": "_ingested_at", "type": "string | timestamp[ns, UTC]", "nullable": false, "description": "write time; type varies across inflection variants", "example": "2026-10-12T12:52:5xZ"},
  {"name": "_spine_date", "type": "string", "nullable": true, "description": "inflection backfill variant only", "example": "2026-10-09"}
 ],
 "enums": {"source_pipeline": ["black_diamond (49financial)", "client_performance_spine (inflection)"]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "key segment 4 and firm_id", "values": ["49financial", "inflection"]},
  "account": {"column": "none -- firm aggregate", "last4_derivation": "n/a", "last4_collisions_within_firm": null},
  "platform": {"column": "custody_scope", "values": ["schwab_native_rps_assets_only_08242234_fact_rps (49F)", "client_performance_daily_spine (inflection)"]}
 },
 "nl_tags": ["non-model assets", "assets outside models"],
 "common_queries": ["How much of Inflection's custody is outside Opal models?"],
 "existing_gateway_tool": {"name": "mdpf_get_aggregate_aua (serves non_model_aua[] per date)", "verdict": "keep"},
 "proposed_tools": [],
 "routing": "answer from platinum aggregate-aua-timeseries non_model_aua[] through mdpf_get_aggregate_aua. Inflection: the same value (feed 2026-10-12 = served 2026-10-09, exact). 49F: the feed is a superseded methodology and must not be served",
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py @217282fadd",
 "open_items": ["49F DIVERGENT: feed 238,687,767.34 (v0_9, RPS assets only) vs served 307,484,594.60 on 2026-10-12 (C2 spec net_mv_plus_cash, per platinum meta.latest_cross_section.custody_source); retire candidate"],
 "evidence": [{"read": "get mdpf/feeds/non_model_aua/{49financial,inflection}/2026-10-12.parquet + last 6 49F files; platinum/mdpf/{49financial,inflection,global}/aggregate-aua-timeseries.json", "at": "2026-10-14T14:0xZ"}]
}
```

```json
{
 "contract_id": "opal-data-mdpf/gold/ai_classified_securities",
 "bucket": "opal-data-mdpf",
 "s3_prefix": "mdpf/global/gold/ai_classified_securities/date=<YYYY-MM-DD>/index.json",
 "layer": "gold",
 "format": "json",
 "table": "ai_classified_securities (index of model-classified rows)",
 "grain": "one entry per security key the AI leg classified; the listing is rewritten on each classifier run",
 "partition": {"keys": ["date=<run_day>"], "claim": "measured"},
 "producer": {"name": "MDPF_SECCLASS AI leg (classify-residual-model writer; infra/aws/lambda/mdpf-secclass/ai-index/index_writer.py)", "schedule": "per classifier run; 2 runs seen (2026-10-07T22:32Z, 2026-10-08T21:31Z); the change-management records name a laptop-run AI leg", "claim": "inferred (PRD MDPF_SECCLASS C-AIINDEX + change-management file names; no schedule read)"},
 "freshness": {"latest_partition": "2026-10-08", "basis": "trading-day-frontier", "lag_trading_days": 3, "note": "event-driven listing, not a daily table: lag is not staleness by itself", "claim": "measured"},
 "size": {"objects": 2, "bytes": 743031, "entries_latest": 2303, "claim": "measured"},
 "columns": [
  {"name": "classified_by", "type": "string", "nullable": false, "description": "document-level: classifier kind", "example": "model"},
  {"name": "count", "type": "int", "nullable": false, "description": "entries in the listing", "example": "2303"},
  {"name": "run_day", "type": "string date", "nullable": false, "description": "run day", "example": "2026-10-08"},
  {"name": "generated_at", "type": "string ts", "nullable": false, "description": "write time", "example": "2026-10-08T21:30:18Z"},
  {"name": "entries[].key", "type": "string", "nullable": false, "description": "security ticker/key", "example": "AAAGX"},
  {"name": "entries[].name", "type": "string", "nullable": true, "description": "security name", "example": "<security name>"},
  {"name": "entries[].asset_class", "type": "string", "nullable": false, "description": "asset class (table vocabulary)", "example": "equity"},
  {"name": "entries[].sub_asset_class", "type": "string", "nullable": false, "description": "sub asset class", "example": "US Large Cap"},
  {"name": "entries[].classification_confidence", "type": "float", "nullable": false, "description": "model confidence", "example": "0.88"},
  {"name": "entries[].low_confidence", "type": "bool", "nullable": false, "description": "low-confidence flag", "example": "false"},
  {"name": "entries[].written_at", "type": "string ts", "nullable": false, "description": "row write time", "example": "2026-10-08T20:51:57Z"}
 ],
 "enums": {"classified_by": ["model"]},
 "fork_keys": {
  "firm": {"column_or_key_segment": "none -- security reference data, scope segment 'global'", "values": ["global"]},
  "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null},
  "platform": {"column": "none", "values": []}
 },
 "nl_tags": ["security classification", "asset class of a fund", "AI classified securities", "low confidence classification"],
 "common_queries": ["What asset class is AAAGX classified as, and was it model-made?", "Which classifications are low-confidence?"],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [{"name": "mdpf_get_security_classification", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "ticker": "<key>"}, "returns": "asset_class, sub_asset_class, classified_by, confidence, low_confidence -- read from the CANONICAL DynamoDB etf-classifications, with this index as provenance", "answers": ["What asset class is AAAGX classified as, and was it model-made?"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md:440-445 (C-AIINDEX); org/standards/MDPF_SECCLASS_CONTRACT.json",
 "open_items": ["the canonical table DynamoDB etf-classifications is not censused by any group (G5 names it only as existing)", "gateway read = implicitDeny (simulated)"],
 "evidence": [{"read": "get mdpf/global/gold/ai_classified_securities/date=2026-10-08/index.json (keys + first entry only)", "at": "2026-10-14T14:0xZ"}]
}
```

## (e) What could not be read, and why

- **Upstream value overlap with G2 silver** (SmartX, Eclipse) for `model_aua_positions` and `model_composition` was not measured. Andrew's question was overlap with portal-v2 only, so it is marked inferred in each contract.
- **Inflection `model_aua_positions` vs served aggregates** was not value-compared, because the feed stops at 2026-10-12 and the served period is 2026-10-13. Overlap of the aggregate is inferred.
- **The 49F `account_id` crosswalk** (SmartX UUID -> custodian account number) was not read. The last-4 collision count is therefore on the UUID's last 4. The count on custodian numbers is not measured.
- **The writer scripts for the runner-chain feeds** are named from a repo grep plus docstrings. The EC2 runner's command line was not read (no SSM).
- **The `ai_classified_securities` producer schedule** was not read. Only the PRD and the change-management file names were.
- **Not opened:** `bmkaud-evidence` PKLs (Bloomberg-derived, frozen 2026-06-01, 93 TD), `code/`, `diagnostics/`, `telemetry/` bodies. The exception is `telemetry/mdpf-daily-runner/status.json`, which was read (see open items).
- **Open items for 4.0.0_SA_CRO~Z** (candidate surprise rows on NFRA_OPLGTW; I wrote no file outside this part):
  1. **COVERAGE:** no group owns `opal-data-assets/portal/gold/mdpf/` (808 keys, the true producer of the served MDPF set) or the per-firm gold buckets `opal-data-{49financial,inflection,cottonwood}/mdpf/<firm>/gold/` (499 keys, including `taxsma_assets`). Latest date = OVERLAP (measured). Dated history and taxsma gold are uncensused.
  2. **Feeder chain idle:** `mdpf-feeder-trigger` logged NOT-YET 4 times on 2026-10-13 and 2026-10-14. The opal-data-inf eclipse gold_complete marker is absent, so the inflection feeds, `non_model_aua` and `etf_net_assets` stop at the 2026-10-12 label. The served inflection timeseries still advanced to 2026-10-13.
  3. **`partner_held_etf/49financial`** rolls a 2026-07-23 RPS value forward (57 TD) under fresh daily labels. Its source `opal-data-bd/schwab/silver/rps` has no newer partition.
  4. **`non_model_aua/49financial`** is v0_9 and differs from the served C2 figure by about 69M USD on 2026-10-12.
  5. **Runner self-report vs world:** `telemetry/mdpf-daily-runner/status.json` (run 2026-10-12) says "complete" with STAGE6-REVAMP status "error". Its last_output claims `platinum/mdpf/aggregate_aua/2026-10-12.json` was refreshed, but opal-data-mdpf holds 0 `platinum/` keys and portal-v2 holds those snapshots only under the frozen `archive/` (G3).
  6. **Graph drift:** the AWS graph (vintage 2026-10-14 13:45:40Z) lists S3Key nodes in opal-data-mdpf at `gold/eclipse/{*}/model_portfolio_accounts.parquet`, `silver/eclipse/{*}/portfolios_full.parquet`, `silver/netassets_daily.parquet` and `platinum/mdpf/aggregate_aua_timeseries.json`. The full 3,248-key listing holds 0 keys under `gold/`, `silver/` or `platinum/`.
  7. **The feed date label is one trading day ahead of the value date** for 49F `model_aua_positions` (measured twice) and inflection `non_model_aua` (measured once). Any tool on the feeds must translate it.
  8. **Every proposed tool needs a never-widen read grant:** opal-gateway-role simulates implicitDeny on all `opal-data-mdpf` keys tried (3), and allowed on the platinum control.
