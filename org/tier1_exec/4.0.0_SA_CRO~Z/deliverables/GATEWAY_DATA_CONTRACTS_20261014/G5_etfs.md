# G5 -- opal-data-etfs: the ETF tracking estate, its monthly run, and 36 table contracts

**Census part G5 for 4.0.0_SA_CRO~Z** under `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` (group row G5).
Read-only. Measured 2026-10-14 12:56Z-13:40Z UTC. T-1 frontier = 2026-10-13 (`lib/trading_calendar.prev_trading_day('2026-10-14')`, hardcoded NYSE fallback 2010-2027).

## 0. The answer to Andrew's question, first

**The monthly ETF tracking run is `etfs-reports-monthly-run`** (EventBridge Scheduler, `cron(0 10 1 * ? *)` America/New_York, ENABLED,
input `{"mode":"run"}`) -> Lambda **`etfs-reports-orchestrator`** -> a transient reporter EC2 that runs
`data/etfs/scripts/presentation/render_month_end.py` -> writes **`platinum/reports/{YYYY-MM}/`** (`etf_ownership.pdf/.html`,
`opaletfs_<partner>_<YYYYMM>.csv` x3, `coverage_verdict.json`) -> the Lambda SES-sends the PDF to two internal recipients.
It last ran 2026-10-01 for September (log: `OK: month-end report SES send month=2026-09`, 2 destinations). Next run 2026-11-01.

**What it reads tells us what is useful:** the renderer reads only `daily/{partner}/{date}.json` (Opal ETF ownership value and
account count per partner firm per day) and `config/etf_universe.json`. Those daily slices are written by three daily Lambdas:
`bd-49f-etf-ownership-daily` (49 Financial, 10:45Z), `cot-etf-ownership-daily` (Cottonwood, 10:30Z), `inf-etf-ownership-daily`
(Inflection, 15:00Z). The same slices feed `etf-ownership-dashboard` (16:00Z, `platinum/etf_ownership_dashboard.json`) and
`opal-assets-daily-emitter` (17:15Z), and are meant to feed `etfs-canon-fanin` (15:45Z), **which fails every day: its DynamoDB
target `opal-etfs-ownership-daily` does not exist** (measured, section 5).

The bucket holds two other live planes beside the ownership plane:
- **Opal fund plane** (the four funds DIVZ, IDVZ, PFDE, PFOE): `etfs-netassets-daily` (22:00Z daily) writes issuer holdings + NAV/AUM
  silver; the site-Z Bloomberg terminal lands `bbg/{as_of}/`; `etf-positioning-producer` (13:00Z) writes `gold/{book,holding}`,
  which feed the portal's ETF positioning object (served from portal-v2, read by the existing gateway tool `etfs_get_positioning`).
- **Rival funds plane** (ETFS_RIVALS, weekday): issuer-site + Bloomberg holdings for 13 funds in two peer groups (IDVZ: TXUE, BIDD,
  CGIC, INEQ, SCHY; PFOE: WCMG, GQGU, TSEL, BASG, ETFT, PCLG) -> 13 gold tables (holdings, inferred trades, flows, buying trend,
  contribution, coverage, AI notes) -> a daily HTML page the gateway already serves at `/rivalfunds` (HTML route, not an MCP tool).

## (a) Method -- each read, its instrument, its denominator

| # | read | instrument | denominator / result |
|---|---|---|---|
| 1 | full bucket listing | boto3 `list_objects_v2` paginator, `s3://opal-data-etfs` | **17 pages, 16,098 of 16,098 keys, 506,706,300 B** at 12:56:54Z (re-list 13:24Z: 17 pages, 16,127 keys -- the bucket grows during the day) |
| 2 | parquet schemas + row counts | pyarrow footer read (range GET of the tail) of every `.parquet` outside `bbg-testpull/` | **10,491 of 10,491 objects, 0 errors**; per dataset: schema variants, union columns, rows |
| 3 | newest-partition content | pandas full read of the newest partition (newest part for snapshot tables) of each of 27 parquet datasets | 27 of 27 datasets; column type / nulls / example / enums |
| 4 | snapshot (re-run) check | duplicate-key test across parts of one partition; older-part keys vs newest part | canonical_shape 2026-10-13 + 3 more dates; trade_schedule 3 dates; flow_reconciliation 3 dates |
| 5 | JSON/CSV objects | `get_object` | all 356 `daily/<partner>/` files (1,424 rows); all 124 `snapshots/`; `etf_history.csv` (389 lines); dashboard; 2026-09 report folder; manifests |
| 6 | producers | `lambda list_functions` + `get-function-configuration` env | **237 functions scanned; 18 match etf/rival or name opal-data-etfs in env**; 15 write or read this bucket |
| 7 | schedules | `events list_rules` + `list_targets_by_rule`; `scheduler list_schedules` + `get_schedule` | **155 EventBridge rules + 33 Scheduler schedules scanned**; 16 rules (2 cot-satellites rules matched by name only) + 5 schedules |
| 8 | trading-day lag / gaps | `lib/trading_calendar` (`is_trading_day`, `trading_days_behind`) over every date-keyed dataset | 44 date-keyed prefixes |
| 9 | gateway access | `iam list_roles` (304) + inline policies of 8 gateway roles; `simulate_principal_policy` x8 | only `gateway-rivalfunds-read-policy` names this bucket (page prefix) |
| 10 | DynamoDB fan-in target | `dynamodb describe_table` + `list_tables` | `opal-etfs-ownership-daily` ResourceNotFound; 46 tables, 1 etf-named (`etf-classifications`) |
| 11 | run logs | `logs get_log_events`, newest stream of 2 functions | etfs-canon-fanin 2026/10/13 (errors), etfs-reports-orchestrator 2026/10/01 (OK) |
| 12 | prior art | Read: 3 atom-decomp runs, ETFS_GUARDRAIL + ETFS_RIVALS PRDs, RIV-w-1 TO, DATA_CATALOG.yaml | **no `rectangle.final.certified.json` exists under any `etfs-*` run** (each holds DECOMP.md only; etfs-ingest also run.json) |

## (b) Prefix census (listing #1, 16,098 keys; LastModified UTC)

| prefix | objects | bytes | newest LastModified | what it is |
|---|---|---|---|---|
| `bbg/{as_of}/` | 599 | 6,467,774 | 2026-10-14T11:07:08Z | Bloomberg terminal landing for the 4 Opal funds, 38 as-of dates 2026-08-20..2026-10-13 |
| `bbg-testpull/` | 357 | 19,197,061 | 2026-10-06T19:25:55Z | FROZEN QA reference (code, combined books, per-ticker history); not contracted |
| `bloomberg/etfs/bronze/holdings/` | 2,286 | 62,779,148 | 2026-10-14T11:07:58Z | raw BQL holdings captures + sidecars (rivals); bronze, not contracted |
| `bloomberg/etfs/silver/holdings/` | 4,114 | 39,165,914 | 2026-10-14T11:08:04Z | rival + home Bloomberg holdings silver, 511 report dates |
| `bloomberg/etfs/silver/history_gaps/` | 1 | 69,406 | 2026-10-13T13:01:32Z | price-history gap record |
| `config/etf_universe.json` | 1 | 2,969 | 2026-10-09T14:14:17Z | the 4-fund universe |
| `daily/49financial/` | 114 | 145,228 | 2026-10-14T10:45:12Z | ownership slices, 2026-05-01..2026-10-13 |
| `daily/cottonwood/` | 86 | 110,705 | 2026-10-14T10:30:29Z | ownership slices, 2026-06-08..2026-10-12 |
| `daily/inflection/` | 156 | 188,032 | 2026-10-13T15:00:41Z | ownership slices, 2026-05-01..2026-10-13 (calendar days) |
| `daily/_archive/` | 1 | 1,345 | 2026-09-10T03:45:24Z | one archived cottonwood slice |
| `etf_history.csv` | 1 | 121,819 | 2026-10-13T22:00:17Z | NAV/AUM history CSV |
| `gold/book/`, `gold/holding/` | 33 + 33 | 735,654 + 1,465,275 | 2026-10-13T13:01:38Z | Opal fund positioning gold, 2026-08-21..2026-10-09 at census |
| `gold/_manifests/` | 63 | 162,997 | 2026-10-13T13:01:38Z | positioning run manifests; not contracted |
| `issuer-site/etfs/bronze/holdings/` | 1,300 | 11,395,723 | 2026-10-14T11:00:35Z | raw issuer files (Brown Advisory, GQG); bronze |
| `issuer-site/etfs/silver/holdings/` | 650 | 9,692,481 | 2026-10-14T11:00:40Z | issuer holdings silver, 335 report dates |
| `mdpf/etfs/gold/new_securities/` | 6 | 28,080 | 2026-10-13T14:00:26Z | MDPF new-security queue |
| `platinum/etf_ownership_dashboard.json` | 1 | 6,407 | 2026-10-13T16:00:04Z | ownership dashboard |
| `platinum/reports/{YYYY-MM}/` | 24 | 1,452,651 | 2026-10-01T14:01:39Z | monthly reports 2026-05..2026-09 |
| `platinum/reports/_archive/`, `corrections/` | 10 + 3 | 683,884 + 6,295 | 2026-09-10T00:20:33Z | superseded renders; the July Orion label correction |
| `rivalfunds/etfs/gold/` (13 tables) | 4,859 | 140,783,607 | 2026-10-14T11:12:43Z | rival gold |
| `rivalfunds/etfs/platinum/page/` | 334 | 203,541,787 | 2026-10-14T11:13:04Z | the published rival page, 12 page days |
| `rivalfunds/etfs/state/` (11 stages) | 402 | 1,557,971 | 2026-10-14T11:13:04Z | stage markers that trigger the next stage; not contracted |
| `silver/holdings/` | 123 | 2,689,784 | 2026-10-13T22:00:16Z | Opal fund issuer holdings |
| `silver/netassets/` + `silver/netassets_daily.parquet` | 416 + 1 | 3,873,315 + 21,478 | 2026-10-13T22:00:16Z | Opal fund NAV/AUM |
| `snapshots/` | 124 | 359,510 | 2026-10-13T22:00:16Z | daily fund snapshot JSON |
| **total** | **16,098** | **506,706,300** | | the rows sum to the listing denominator |

**Absent (zero keys in 16,098):** `gold/` was greenfield on 2026-08-24 and is now live; `monthly/` (read by the dashboard and the
renderer) does not exist; `bbg-testpull/` stays frozen.

### Producers and schedules (reads #6, #7)

| writer | trigger (all ENABLED) | writes under opal-data-etfs |
|---|---|---|
| `etfs-reports-orchestrator` (+ EC2 renderer) | Scheduler `etfs-reports-monthly-run` cron(0 10 1 * ? *) America/New_York | `platinum/reports/{YYYY-MM}/` -- **the monthly run** |
| `bd-49f-etf-ownership-daily` | rule `bd-49f-etf-ownership-scheduled-floor` cron(45 10 * * ? *) | `daily/49financial/` |
| `cot-etf-ownership-daily` | rule `cot-etf-ownership-daily-schedule` cron(30 10 * * ? *) | `daily/cottonwood/` |
| `inf-etf-ownership-daily` | rule `inf-etf-ownership-daily-schedule` cron(0 15 * * ? *) | `daily/inflection/` |
| `etf-ownership-dashboard` | rule `etf-ownership-dashboard-daily` cron(0 16 * * ? *) | `platinum/etf_ownership_dashboard.json` |
| `etfs-canon-fanin` | rule `etfs-canon-fanin-daily` cron(45 15 * * ? *) | nothing here (reads `daily/`; DynamoDB write FAILS) |
| `opal-assets-daily-emitter` | rule `opal-assets-daily-emitter-daily` cron(15 17 * * ? *) | nothing here (reads `daily/`; writes opal-data-assets) |
| `etfs-netassets-daily` | rule `etfs-netassets-daily` cron(0 22 * * ? *) | `silver/holdings/`, `silver/netassets/`, `silver/netassets_daily.parquet`, `snapshots/`, `etf_history.csv` |
| `etf-positioning-producer` | rule `etf-positioning-producer-daily` cron(0 13 * * ? *) | `gold/book/`, `gold/holding/`, `gold/_manifests/` |
| site-Z Bloomberg terminal (not a Lambda) | scheduled task ~07:00 ET (inferred) | `bbg/{as_of}/`; rival `bloomberg/etfs/bronze/`; enrichment gold `security_market`, `corporate_actions` (inferred) |
| `etfs-rivalfunds-fetch-holdings-lambda` | Scheduler `etfs-rivalfunds-daily` cron(0 7 ? * MON-FRI *) America/New_York | `issuer-site/etfs/bronze/`, `rivalfunds/etfs/state/fetch_holdings/` |
| `rivalfunds-build-silver-lambda` | 2 S3-marker rules (fetch_holdings/, fetch_bloomberg/) | `issuer-site/etfs/silver/`, `bloomberg/etfs/silver/holdings/` |
| `rivalfunds-build-canonical-shape-lambda` | 2 S3-marker rules (build_silver/, build_bloomberg_silver/) | `rivalfunds/etfs/gold/canonical_shape/` (+ coverage, flow, trades: inferred) |
| `rivalfunds-publish-page-lambda` | S3-marker rule (build_trade_schedule/) | `rivalfunds/etfs/platinum/page/` (+ buying_trend, holding_contribution, input_census: inferred) |
| `etfs-rivalfunds-daily-lambda` (sweep) | Scheduler `etfs-rivalfunds-sweep-daily` cron(0 9 ? * MON-FRI *) America/New_York | any stage missing its marker; peer_group_map, research_hypotheses, security_universe/names (inferred) |
| `mdpf-secclass-new-security-lambda` | Scheduler `mdpf-secclass-new-security-daily` cron(0 10 ? * MON-FRI *) America/New_York | `mdpf/etfs/gold/new_securities/` |
| `opal-assets-silver-etf` | rule `opal-assets-silver-etf-sweep-daily` cron(30 23 * * ? *) | nothing here (env MONOLITH_BUCKET opal-data-assets; vendor silver) |

Two matched functions do not touch this bucket: `wsd-49f-partner-held-etf-daily` (writes opal-data-mdpf `mdpf/feeds/`) and
`yang-generate-etf-returns` (writes portal `json/benchmarks/etf_returns.json`).

## (c) Analysis

**What the tables are.** 36 contracts in four planes: (1) **ownership** -- 3 contracts (daily partner slices, the dashboard, the
monthly report); (2) **Opal funds** -- 15 (issuer holdings and NAV/AUM silver, the snapshots/CSV twins, the universe config, gold
book + holding, 7 Bloomberg landing tables); (3) **rivals** -- 17 (2 Bloomberg silver, 1 issuer silver, 13 gold, the page); (4)
**MDPF** -- 1 (new securities). Bronze, state markers, manifests, archives and `bbg-testpull/` are censused, not contracted.

**Reading rules that a tool must carry** (each measured):
- **Re-run parts supersede, never add.** 10 rival gold tables keep several parts per date. The newest part (max `revision` /
  `dataset_revision`) is the complete snapshot. Summing parts over-counts: canonical_shape totals 692,547 rows across all parts and
  321,049 in the newest part per date. Older parts are not subsets of the newest: on 2026-09-29, 48 trade_schedule keys are absent
  from the newest part, because the inference version changed.
- **Three dates in one Opal silver row:** the file key (run date), `data_as_of` (the issuer date, usually the day before) and
  `_ingested_at`. Weekend files exist and carry Friday's data. They are not staleness.
- **Units differ by layer:** weights are pct-points in Opal silver and gold/holding, but a fraction in rival canonical_shape (`weight_basis` net_assets).
- **Claims are in the data:** rival gold carries `claim` MEASURED/INFERRED per row. Trades, flows, buying trend and contribution are
  INFERRED. research_hypotheses is LLM text (`model_version`). A tool must pass the claim through.

**Common questions (what an asset manager asks of this bucket):** How much of each Opal ETF does each partner hold, and how has it moved
this month? Did the monthly report go out, and was it complete? What does DIVZ/IDVZ/PFDE/PFOE hold, and with what sector or country
mix, on a date? What are the fund's AUM, NAV and shares outstanding over time? Who are IDVZ's and PFOE's rivals, what do they hold,
what did they buy or sell this week, where are the flows going, and which holdings drove their returns? Which funds hold a given stock?

**Proposed tools (15 new, 1 extended; the /rivalfunds HTML routes kept), keyed by fund ticker and as_of:**

| tool | backing tables | key inputs |
|---|---|---|
| `etfs_get_partner_ownership` | daily/{partner} | firm (REQUIRED), as_of range, etf_ticker |
| `etfs_get_ownership_rollup` | platinum dashboard | firm optional (the cross-partner whole needs a ruling) |
| `etfs_get_monthly_report` | platinum/reports | month, firm for the CSV series |
| `etfs_get_fund_holdings` | gold/holding -> silver/holdings (Opal); canonical_shape (rivals) | fund_ticker, as_of |
| `etfs_get_fund_nav_history` | silver/netassets(_daily), snapshots | fund_ticker, start..end |
| `etfs_get_fund_bloomberg_profile` | bbg/{as_of} fund_daily + derived_* | fund_ticker, as_of |
| `etfs_get_positioning` (EXTEND: add as_of, fund_ticker) | today portal-v2 platinum; history gold/book + holding | as_of, fund_ticker |
| `etfs_get_peer_group` | peer_group_map | home_ticker |
| `etfs_get_fund_trades` | trade_schedule | fund_ticker or group, range, action |
| `etfs_get_fund_flows` | flow_reconciliation | fund_ticker, range |
| `etfs_compare_peers` | buying_trend + holding_contribution | home_ticker, period, axis |
| `etfs_who_holds` | canonical_shape + security_universe (+ gold/holding) | security, as_of, peer_group |
| `etfs_get_security_reference` | security_market + corporate_actions | security, as_of |
| `etfs_get_coverage` | holdings_coverage + input_census | as_of, fund_ticker |
| `etfs_get_research_notes` | research_hypotheses (AI-labelled) | fund_ticker, as_of |
| `etfs_get_new_securities` | mdpf new_securities | as_of |

**Every proposed tool needs a read-grant widening.** `opal-gateway-role` simulates `implicitDeny` for `s3:GetObject` on
`gold/book`, `daily/49financial` and `rivalfunds/etfs/gold/canonical_shape`, and `allowed` only on the page prefix. The
`gateway-global-internal-reader-role` is denied on all four. Each tool is therefore a never-widen act.

**Existing tool verdicts:** `etfs_get_positioning` (catalog `portal_etfs_positioning` / `etfs.01.positioning-data`,
`app/integrations/portal_index/integration.py:397`) reads the portal-v2 platinum object that is built from this bucket's
`gold/book` + `gold/holding`. Verdict: **keep**, and **extend** it with as_of history from the gold tables. Its catalog freshness reads
2026-10-13, and its history depth 2026-10-09. The `/rivalfunds` HTML routes: **keep**. No catalog row covers any other table here
(`DATA_CATALOG.yaml` has no `rival`, `ownership` or `opal-data-etfs` row).

## (d) Contracts -- one JSON block per table

### opal-data-etfs/gold/daily_partner_ownership

```json
{
 "contract_id": "opal-data-etfs/gold/daily_partner_ownership",
 "bucket": "opal-data-etfs",
 "s3_prefix": "daily/{partner}/{YYYY-MM-DD}.json",
 "layer": "gold",
 "format": "json",
 "table": "daily_partner_ownership",
 "grain": "one row per (partner firm, date, Opal ETF ticker); one file per partner per date holding 4 rows (DIVZ, IDVZ, PFDE, PFOE)",
 "partition": {"keys": ["partner (key segment)", "date (file name)"], "claim": "measured"},
 "producer": {"name": "bd-49f-etf-ownership-daily (49financial) | cot-etf-ownership-daily (cottonwood) | inf-etf-ownership-daily (inflection)", "schedule": "EventBridge cron(45 10 * * ? *) | cron(30 10 * * ? *) | cron(0 15 * * ? *), all UTC, all ENABLED; env OUTPUT_PREFIX daily/<partner>/", "claim": "measured"},
 "freshness": {"latest_partition": {"49financial": "2026-10-13", "cottonwood": "2026-10-12", "inflection": "2026-10-13"}, "trading_days_behind_T-1": {"49financial": 0, "cottonwood": 1, "inflection": 0}, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "cottonwood writes date D on D+2 (the 2026-10-12 file landed 2026-10-14T10:30:29Z); inflection also writes non-trading days (42 weekend/holiday files); missing trading days since first file: 49financial 0, cottonwood 2 (2026-06-23, 2026-06-24), inflection 0"},
 "size": {"objects": {"49financial": 114, "cottonwood": 86, "inflection": 156, "_archive": 1}, "rows_all_files": {"49financial": 456, "cottonwood": 344, "inflection": 624}, "first_date": {"49financial": "2026-05-01", "cottonwood": "2026-06-08", "inflection": "2026-05-01"}, "field_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "schema_version", "type": "string", "nullable": false, "description": "row schema version (1.0 on 1,424 of 1,424 rows)", "example": "1.0"},
  {"name": "partner", "type": "string", "nullable": false, "description": "partner firm key; equals the key segment", "example": "49financial"},
  {"name": "date", "type": "string(date)", "nullable": false, "description": "ownership date (the file name)", "example": "2026-10-13"},
  {"name": "etf_ticker", "type": "string", "nullable": false, "description": "Opal ETF ticker", "example": "DIVZ"},
  {"name": "ownership_value", "type": "double", "nullable": false, "description": "USD market value of the ETF held across the partner's accounts on that date", "example": "1.87e8 (aggregate, firm-level)"},
  {"name": "account_count", "type": "int", "nullable": false, "description": "count of partner accounts holding the ETF (a count, no account ids)", "example": "5881"},
  {"name": "source_artifact", "type": "string(s3 uri)", "nullable": false, "description": "the firm silver/gold object the value was computed from", "example": "s3://opal-data-assets/schwab/08242234/silver/fact_rps/..."},
  {"name": "source_as_of", "type": "string(date)", "nullable": false, "description": "as-of of the source artifact; equals date on 1,424 of 1,424 rows", "example": "2026-10-13"}
 ],
 "enums": {"partner": ["49financial", "cottonwood", "inflection"], "etf_ticker": ["DIVZ", "IDVZ", "PFDE", "PFOE"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment daily/<partner>/ and column partner", "values": ["49financial", "cottonwood", "inflection"]}, "account": {"column": "none (aggregate: account_count only, no account id)", "last4_derivation": "not applicable", "last4_collisions_within_firm": null}, "platform": {"column": "derived from source_artifact bucket/prefix", "values": ["schwab fact_rps (49financial; opal-data-bd earlier, opal-data-assets now)", "blackdiamond fact_holdings (cottonwood; opal-data-cot earlier, opal-data-assets now)", "orion via opal-data-inf gold/canonical (inflection)"]}},
 "nl_tags": [
  "etf ownership",
  "who holds our ETFs",
  "partner holdings of DIVZ",
  "ETF AUM by partner",
  "monthly ETF report input",
  "account count holding an ETF"
 ],
 "common_queries": [
  "How much DIVZ did 49 Financial hold on 2026-10-13?",
  "How many Cottonwood accounts hold IDVZ?",
  "What is Inflection's PFOE ownership trend over September?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_partner_ownership", "inputs": {"firm": "<partner, REQUIRED: 49financial|cottonwood|inflection>", "account_last4": "n/a", "platform": "n/a", "as_of": "<date or start..end>", "etf_ticker": "<optional>"}, "returns": "rows {date, etf_ticker, ownership_value, account_count, source_as_of} for ONE partner, with trading-day coverage and missing-day list", "answers": ["How much DIVZ did 49 Financial hold on 2026-10-13?", "What is Inflection's PFOE ownership trend over September?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D8/ETFS/ETFS_GUARDRAIL/prd/ETFS_GUARDRAIL_PRD.md@a6cbb6f3c3; workflows/atom_decomposition/runs/etfs-positioning/20260821T194927Z/DECOMP.md@20c092c0da (no certified rectangle) (boundary cell ETFS-a-7)",
 "open_items": [
  "etfs-canon-fanin (cron(45 15) daily) reads these files and BatchWriteItem's into DynamoDB opal-etfs-ownership-daily, which does NOT exist (describe-table ResourceNotFound; 46 tables listed, 1 etf-named: etf-classifications); its last log stream 2026/10/13 shows [ERROR] ResourceNotFoundException x3 retries. The fan-in fails every day.",
  "the IDVZ display name differs: config/etf_universe.json says 'Opal International Dividend Income ETF', silver/netassets says 'Polen International Dividend Income ETF' (measured both; which is current is not measured)",
  "gateway role opal-gateway-role: s3:GetObject on daily/49financial/2026-10-13.json simulates implicitDeny -- any tool here is a read-grant widening (never-widen sign-off)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "get_object of all 356 daily/<partner>/ files (row, field, source_as_of census)", "at": "2026-10-14T13:3xZ"},
  {"read": "lambda get-function-configuration x3 + events list_targets_by_rule (155 rules scanned)", "at": "2026-10-14T13:01:33Z"},
  {"read": "logs get_log_events /aws/lambda/etfs-canon-fanin newest stream; dynamodb describe_table opal-etfs-ownership-daily -> ResourceNotFound", "at": "2026-10-14T13:2xZ"}
 ]
}
```

### opal-data-etfs/platinum/etf_ownership_dashboard

```json
{
 "contract_id": "opal-data-etfs/platinum/etf_ownership_dashboard",
 "bucket": "opal-data-etfs",
 "s3_prefix": "platinum/etf_ownership_dashboard.json",
 "layer": "platinum",
 "format": "json",
 "table": "etf_ownership_dashboard",
 "grain": "one object, overwritten daily: cross-partner rollup of the latest daily slice per partner (internal_only=true)",
 "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "etf-ownership-dashboard (data/etfs/scripts/etf_ownership_dashboard.py; infra/aws/lambda/etfs-pipeline/etf-ownership-dashboard)", "schedule": "EventBridge etf-ownership-dashboard-daily cron(0 16 * * ? *) UTC, ENABLED", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13 (run_as_of; per-partner as_of 2026-10-12 for 49financial)", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "LastModified 2026-10-13T16:00:04Z; next fire 2026-10-14T16:00Z"},
 "size": {"objects": 1, "bytes": 6407, "claim": "measured"},
 "columns": [
  {"name": "schema_version", "type": "string", "nullable": false, "description": "1.0", "example": "1.0"},
  {"name": "generated_utc", "type": "string(ts)", "nullable": false, "description": "UTC build time", "example": "2026-10-13T16:00:02Z"},
  {"name": "run_as_of", "type": "string(date)", "nullable": false, "description": "run date", "example": "2026-10-13"},
  {"name": "universe", "type": "list[4]", "nullable": false, "description": "the four Opal ETFs", "example": "[DIVZ, IDVZ, PFDE, PFOE]"},
  {"name": "internal_only", "type": "bool", "nullable": false, "description": "Opal-internal artifact flag", "example": "true"},
  {"name": "grand_total_ownership_value", "type": "double", "nullable": false, "description": "sum over partners and ETFs, USD", "example": "6.6e8"},
  {"name": "rollup_total_by_partner[]", "type": "list[3] {partner, display_name, freshness, as_of, total_ownership_value}", "nullable": false, "description": "per-partner totals", "example": "{partner: 49financial, freshness: current}"},
  {"name": "rollup_by_etf[]", "type": "list[4] {etf, total_ownership_value, partners[]}", "nullable": false, "description": "per-ETF totals with partner split", "example": "{etf: DIVZ}"},
  {"name": "per_partner[]", "type": "list[3] {partner, as_of, source_as_of_worstcase, freshness, basis, days_stale, total_ownership_value, etfs{4}}", "nullable": false, "description": "per-partner detail", "example": "{basis: daily-granular, days_stale: 1}"},
  {"name": "monthly_context", "type": "dict {available}", "nullable": false, "description": "AVGCAP monthly average block; available=false because monthly/ is absent", "example": "{available: false}"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "per_partner[].partner and rollup_by_etf[].partners[] -- ALL THREE partners in one object", "values": ["49financial", "cottonwood", "inflection"]}, "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF ownership dashboard",
  "total ETF ownership by partner",
  "Opal ETF AUM held at partners"
 ],
 "common_queries": [
  "What is total Opal ETF ownership across partners today?",
  "Which partner holds the most PFDE?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_ownership_rollup", "inputs": {"firm": "<partner, optional filter; omitted = the Opal-internal cross-partner rollup (needs a CTO ruling under directive rule 2)>", "account_last4": "n/a", "platform": "n/a", "as_of": "latest only"}, "returns": "the dashboard object, or the one partner's per_partner block when firm is given", "answers": ["What is total Opal ETF ownership across partners today?", "Which partner holds the most PFDE?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-positioning/20260821T194927Z/DECOMP.md@20c092c0da (no certified rectangle) (sec 2.1: live served artifact owned by ETFS_CANON)",
 "open_items": [
  "the object holds three firms by design (internal_only=true); a gateway tool returning it whole reads three firms in one call -- needs an explicit ruling",
  "monthly_context.available=false: monthly/ prefix absent (0 of 16,098 keys)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "get_object platinum/etf_ownership_dashboard.json (shape only)", "at": "2026-10-14T13:1xZ"},
  {"read": "events list_targets_by_rule etf-ownership-dashboard-daily", "at": "2026-10-14T13:01:33Z"}
 ]
}
```

### opal-data-etfs/platinum/monthly_ownership_report

```json
{
 "contract_id": "opal-data-etfs/platinum/monthly_ownership_report",
 "bucket": "opal-data-etfs",
 "s3_prefix": "platinum/reports/{YYYY-MM}/",
 "layer": "platinum",
 "format": "csv+html+pdf+json",
 "table": "monthly_ownership_report",
 "grain": "one folder per calendar month: etf_ownership.{html,pdf} (the emailed deck), opaletfs_<partner>_<YYYYMM>.csv per partner (rows = Date + one row per ETF, columns = calendar days, last line '# coverage: ...'), coverage_verdict.json (PUBLISH/REFUSE + per-partner coverage)",
 "partition": {"keys": ["month (YYYY-MM)"], "claim": "measured"},
 "producer": {"name": "etfs-reports-orchestrator -> transient reporter EC2 -> data/etfs/scripts/presentation/render_month_end.py; SES send of the PDF to two internal recipients", "schedule": "EventBridge Scheduler etfs-reports-monthly-run cron(0 10 1 * ? *) America/New_York, input {mode: run}, ENABLED -- THE MONTHLY ETF TRACKING RUN", "claim": "measured"},
 "freshness": {"latest_partition": "2026-09", "basis": "month-end (calendar); next run 2026-11-01 10:00 ET for 2026-10", "claim": "measured", "note": "2026-09 rendered 2026-10-01T14:01:39Z; orchestrator log 2026/10/01: 'OK: month-end report SES send month=2026-09 destinations=[2 recipients]'"},
 "size": {"objects": {"2026-05": 2, "2026-06": 2, "2026-07": 5, "2026-08": 7, "2026-09": 8, "_archive": 10, "corrections": 3}, "bytes_months": 1452651, "claim": "measured"},
 "columns": [
  {"name": "etf_ownership.pdf / .html", "type": "pdf / html", "nullable": false, "description": "the month-end deck: average-level partner aggregates, per-partner/ETF deltas, daily matrix", "example": "platinum/reports/2026-09/etf_ownership.pdf (253,593 B)"},
  {"name": "opaletfs_<partner>_<YYYYMM>.csv: Date", "type": "csv header row", "nullable": false, "description": "first row: 'Date' then every calendar day of the month", "example": "Date,2026-09-01,...,2026-09-30"},
  {"name": "opaletfs_<partner>_<YYYYMM>.csv: <ETF> rows", "type": "csv rows DIVZ, IDVZ, PFDE, PFOE", "nullable": false, "description": "daily ownership value per ETF (calendar-day carry-forward)", "example": "DIVZ,<value>,..."},
  {"name": "opaletfs_<partner>_<YYYYMM>.csv: # coverage", "type": "comment line", "nullable": false, "description": "trading-day coverage statement on the report's face", "example": "# coverage: 21/21 trading days; 0 carried for missing data"},
  {"name": "coverage_verdict.json", "type": "json {month, verdict, per_partner{summary, coverage_line, holes}, holes, unresolved, forcing{14}}", "nullable": false, "description": "the pre-publish gate verdict", "example": "{verdict: PUBLISH, holes: 0}"}
 ],
 "enums": {"verdict": ["PUBLISH", "REFUSE (inferred from the guardrail PRD; not observed in 2026-09)"]},
 "fork_keys": {"firm": {"column_or_key_segment": "file name opaletfs_<partner>_<YYYYMM>.csv; the pdf/html and coverage_verdict.json hold all three partners", "values": ["49financial", "cottonwood", "inflection"]}, "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "monthly ETF report",
  "ETF ownership report",
  "month-end ETF tracking",
  "report coverage",
  "September ETF report"
 ],
 "common_queries": [
  "Did the September ETF ownership report go out, and was it complete?",
  "What was Cottonwood's average DIVZ ownership in September?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_monthly_report", "inputs": {"firm": "<partner, REQUIRED for the CSV series; omitted returns only verdict + links>", "account_last4": "n/a", "platform": "n/a", "as_of": "<YYYY-MM>"}, "returns": "coverage verdict + that partner's CSV series and coverage line + the pdf key", "answers": ["Did the September ETF ownership report go out, and was it complete?", "What was Cottonwood's average DIVZ ownership in September?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D8/ETFS/ETFS_GUARDRAIL/prd/ETFS_GUARDRAIL_PRD.md@a6cbb6f3c3",
 "open_items": [
  "MEASURED DISAGREEMENT in 2026-09: coverage_verdict.json says 21/21 trading days, 0 carried for all three partners, while the same run's CSVs say cottonwood '20/21 trading days; 1 carried' and inflection '18/21 trading days; 3 carried' (49financial agrees 21/21). All three partners have a daily/ file for every September trading day and source_as_of==date on every row, so the CSV's 'carried' basis is not file absence; cause not measured. Surprise row for ETFS_GUARDRAIL/NFRA_OPLGTW owed (not filed: brief bars writes outside this file).",
  "2026-09/ also holds coverage_egress_ask.json + coverage_unresolved.json written 2026-09-10T01:20Z (a test run before the month closed) beside the 2026-10-01 PUBLISH verdict; a reader must take coverage_verdict.json",
  "renderer load_monthly_avg reads monthly/{YYYY-MM}.json in a try/except returning {} -- monthly/ is absent; the deck's average is the in-render calendar-day AVGCAP (render_month_end.py:325-331, inferred from source)",
  "render_month_end.py docstring says it reads ONLY opal-data-etfs, but load_inf_canonical (:226-246) lists opal-data-inf gold/canonical/holdings_ on its preview path (source read, path not exercised here)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "scheduler get_schedule etfs-reports-monthly-run (33 schedules scanned)", "at": "2026-10-14T13:01:33Z"},
  {"read": "get_object platinum/reports/2026-09/coverage_verdict.json + 3 CSVs", "at": "2026-10-14T13:2xZ"},
  {"read": "logs /aws/lambda/etfs-reports-orchestrator stream 2026/10/01", "at": "2026-10-14T13:2xZ"}
 ]
}
```

### opal-data-etfs/silver/holdings

```json
{
 "contract_id": "opal-data-etfs/silver/holdings",
 "bucket": "opal-data-etfs",
 "s3_prefix": "silver/holdings/{YYYY-MM-DD}.parquet",
 "layer": "silver",
 "format": "parquet",
 "table": "holdings",
 "grain": "one row per (run date, Opal fund, holding) from the issuer files (TrueShares sheet for DIVZ/IDVZ, Pathfinder filepoint for PFDE/PFOE)",
 "partition": {"keys": ["run date (file name; the issuer as-of is the data_as_of column, usually the prior day)"], "claim": "measured"},
 "producer": {"name": "etfs-netassets-daily (infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:134-138)", "schedule": "EventBridge etfs-netassets-daily cron(0 22 * * ? *) UTC, ENABLED (fires 7 days/week)", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "123 files 2026-05-18..2026-10-13; 12 trading days missing (May-June); 32 weekend files carry the prior trading day (NOT staleness)"},
 "size": {"objects": 123, "bytes": 2689784, "rows_all_parts": 17013, "rows_newest_part_per_partition": 17013, "rows_newest_partition": 186, "schema_variants": 5, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "timestamp[ns]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-12 00:00:00"},
  {"name": "run_date", "type": "string", "nullable": false, "description": "run date (the file key)", "example": "2026-10-13"},
  {"name": "fund_key", "type": "string", "nullable": false, "description": "lower-case fund key", "example": "divz"},
  {"name": "fund_ticker", "type": "string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "DIVZ"},
  {"name": "holding_ticker", "type": "string", "nullable": false, "description": "holding ticker (US/ADR line for IDVZ)", "example": "PM"},
  {"name": "cusip", "type": "string", "nullable": false, "description": "CUSIP as used by the row", "example": "718172109"},
  {"name": "security_name", "type": "string", "nullable": false, "description": "security long name", "example": "Philip Morris International Inc"},
  {"name": "shares", "type": "double", "nullable": false, "description": "shares held", "example": "97905.0"},
  {"name": "price", "type": "double", "nullable": true, "description": "price per share (often null for TrueShares rows)", "example": "0.0"},
  {"name": "market_value", "type": "double", "nullable": false, "description": "position market value, USD", "example": "19776810.0"},
  {"name": "weight_pct", "type": "double", "nullable": false, "description": "position weight in pct-points (sums ~100 per fund)", "example": "6.49"},
  {"name": "is_cash", "type": "bool", "nullable": true, "description": "cash line flag", "example": "False"},
  {"name": "run_class", "type": "string", "nullable": false, "description": "scheduled or adhoc (ad-hoc rows are never production evidence)", "example": "scheduled"},
  {"name": "cash_basis", "type": "string", "nullable": false, "description": "how is_cash was set (presence-flag / field-absent)", "example": "field-absent"},
  {"name": "id_kind", "type": "string", "nullable": false, "description": "identifier kind of cusip (cusip, bbgid, vendor-sentinel, unclassified)", "example": "cusip"},
  {"name": "cusip_as_delivered", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "718172109"},
  {"name": "cusip_basis", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "as-delivered"},
  {"name": "as_of_basis", "type": "string", "nullable": false, "description": "source of data_as_of", "example": "issuer-holdings-file"},
  {"name": "fund_net_assets", "type": "double", "nullable": false, "description": "fund net assets on the issuer file", "example": "304854991.4"},
  {"name": "fund_shares_outstanding", "type": "double", "nullable": false, "description": "fund shares outstanding on the issuer file", "example": "8170000.0"},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "trueshares"},
  {"name": "source_system", "type": "string", "nullable": false, "description": "producing system tag", "example": "etf_netassets_watch"},
  {"name": "data_as_of", "type": "timestamp[ns]", "nullable": false, "description": "as-of date of the data in the row", "example": "2026-10-12 00:00:00"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "UTC ingest time", "example": "2026-10-13T22:00:09+00:00"},
  {"name": "vendor_filepoint_Account", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "PFDE"},
  {"name": "vendor_filepoint_CreationUnits", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "601.000000000000"},
  {"name": "vendor_trueshares_Date", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "2026-10-12"},
  {"name": "vendor_trueshares_Account", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "DIVZ"},
  {"name": "vendor_trueshares_NetAssets", "type": "null", "nullable": true, "description": "name-evident; see producer source", "example": null}
 ],
 "enums": {"fund_ticker": ["DIVZ", "IDVZ", "PFDE", "PFOE"], "source": ["trueshares", "filepoint"], "id_kind": ["cusip", "bbgid", "vendor-sentinel", "unclassified"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "Opal ETF holdings",
  "DIVZ holdings",
  "PFDE constituents",
  "fund holdings history",
  "issuer holdings file"
 ],
 "common_queries": [
  "What did DIVZ hold on 2026-09-30?",
  "When did PFDE add NVDA?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_fund_holdings", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<DIVZ|IDVZ|PFDE|PFOE or a rival ticker>"}, "returns": "holdings rows with weight, market value, shares, identifiers and the row's data_as_of; Opal funds from gold/holding (2026-08-21+) falling back to silver/holdings (2026-05-18+), rivals from rivalfunds canonical_shape", "answers": ["What did DIVZ hold on 2026-09-30?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists)",
 "open_items": [
  "three date semantics in one artifact (key = run date, data_as_of = issuer date, _ingested_at) -- ETFS_INGEST INGEST-T2-4; a tool must key on data_as_of"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object silver/holdings/2026-10-13.parquet (186 rows)", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/netassets

```json
{
 "contract_id": "opal-data-etfs/silver/netassets",
 "bucket": "opal-data-etfs",
 "s3_prefix": "silver/netassets/{YYYY-MM-DD}.parquet",
 "layer": "silver",
 "format": "parquet",
 "table": "netassets",
 "grain": "one row per (run date, Opal fund): NAV, market price, shares outstanding, net assets",
 "partition": {"keys": ["run date (file name)"], "claim": "measured"},
 "producer": {"name": "etfs-netassets-daily (infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:134-138)", "schedule": "EventBridge etfs-netassets-daily cron(0 22 * * ? *) UTC, ENABLED (fires 7 days/week)", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "416 files 2025-05-30..2026-10-13; 83 non-trading-day files; 12 trading days missing"},
 "size": {"objects": 416, "bytes": 3873315, "rows_all_parts": 1078, "rows_newest_part_per_partition": 1078, "rows_newest_partition": 4, "schema_variants": 2, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "timestamp[ns]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13 00:00:00"},
  {"name": "key", "type": "string", "nullable": false, "description": "lower-case fund key", "example": "divz"},
  {"name": "ticker", "type": "string", "nullable": false, "description": "ticker", "example": "DIVZ"},
  {"name": "name", "type": "string", "nullable": false, "description": "name (fund or security)", "example": "Polen Dividend Income ETF"},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "trueshares"},
  {"name": "source_system", "type": "string", "nullable": false, "description": "producing system tag", "example": "etf_netassets_watch"},
  {"name": "nav", "type": "double", "nullable": false, "description": "net asset value per share", "example": "37.31"},
  {"name": "market_price", "type": "double", "nullable": false, "description": "closing market price", "example": "37.32"},
  {"name": "shares_outstanding", "type": "double", "nullable": false, "description": "fund shares outstanding", "example": "8170000.0"},
  {"name": "shares_basis", "type": "string", "nullable": false, "description": "issuer_reported", "example": "issuer_reported"},
  {"name": "net_assets_reported", "type": "double", "nullable": false, "description": "issuer-reported net assets", "example": "304854991.4"},
  {"name": "net_assets", "type": "double", "nullable": false, "description": "computed net assets (nav x shares)", "example": "304904400.0"},
  {"name": "inferred", "type": "bool", "nullable": false, "description": "true when the value was carried or computed", "example": "False"},
  {"name": "data_as_of", "type": "timestamp[ns]", "nullable": false, "description": "as-of date of the data in the row", "example": "2026-10-12 00:00:00"},
  {"name": "staleness_days", "type": "int64", "nullable": false, "description": "days the value is carried", "example": "0"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "UTC ingest time", "example": "2026-10-13T22:00:09+00:00"}
 ],
 "enums": {"ticker": ["DIVZ", "IDVZ", "PFDE", "PFOE"], "source": ["trueshares", "filepoint", "stale_carryforward", "trueshares_carryforward"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF NAV",
  "fund AUM",
  "net assets",
  "shares outstanding",
  "DIVZ AUM history"
 ],
 "common_queries": [
  "What was IDVZ's AUM on 2026-09-30?",
  "How have PFOE's shares outstanding changed this quarter?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_nav_history", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<start..end>", "fund_ticker": "<Opal ticker>"}, "returns": "daily nav, market_price, shares_outstanding, net_assets(_reported), source, inferred flag; trading days only by default", "answers": ["What was IDVZ's AUM on 2026-09-30?", "How have PFOE's shares outstanding changed this quarter?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-positioning/20260821T194927Z/DECOMP.md@20c092c0da (no certified rectangle) (ETFS-a-2)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"}
 ]
}
```

### opal-data-etfs/silver/netassets_daily

```json
{
 "contract_id": "opal-data-etfs/silver/netassets_daily",
 "bucket": "opal-data-etfs",
 "s3_prefix": "silver/netassets_daily.parquet",
 "layer": "silver",
 "format": "parquet",
 "table": "netassets_daily",
 "grain": "one row per (run date, Opal fund), the consolidated history in one file (rewritten each run)",
 "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "etfs-netassets-daily (infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:134-138)", "schedule": "EventBridge etfs-netassets-daily cron(0 22 * * ? *) UTC, ENABLED (fires 7 days/week)", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13 (max date column)", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "388 rows = 97 run dates x 4 funds, from 2026-07-09; same rows as etf_history.csv (388 data lines)"},
 "size": {"objects": 1, "bytes": 21478, "rows_all_parts": 388, "rows_newest_part_per_partition": 388, "rows_newest_partition": 388, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "timestamp[ns]", "nullable": false, "description": "partition / report date of the row", "example": "2026-07-09 00:00:00"},
  {"name": "key", "type": "string", "nullable": false, "description": "lower-case fund key", "example": "divz"},
  {"name": "ticker", "type": "string", "nullable": false, "description": "ticker", "example": "DIVZ"},
  {"name": "name", "type": "string", "nullable": false, "description": "name (fund or security)", "example": "Polen Dividend Income ETF"},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "trueshares"},
  {"name": "source_system", "type": "string", "nullable": false, "description": "producing system tag", "example": "etf_netassets_watch"},
  {"name": "nav", "type": "double", "nullable": false, "description": "net asset value per share", "example": "38.14"},
  {"name": "market_price", "type": "double", "nullable": false, "description": "closing market price", "example": "38.16"},
  {"name": "shares_outstanding", "type": "double", "nullable": false, "description": "fund shares outstanding", "example": "7210000.0"},
  {"name": "shares_basis", "type": "string", "nullable": false, "description": "issuer_reported", "example": "issuer_reported"},
  {"name": "net_assets_reported", "type": "double", "nullable": false, "description": "issuer-reported net assets", "example": "274962771.0"},
  {"name": "net_assets", "type": "double", "nullable": false, "description": "computed net assets (nav x shares)", "example": "275133600.0"},
  {"name": "inferred", "type": "bool", "nullable": false, "description": "carried/computed flag", "example": "False"},
  {"name": "data_as_of", "type": "timestamp[ns]", "nullable": false, "description": "as-of date of the data in the row", "example": "2026-07-08 00:00:00"},
  {"name": "staleness_days", "type": "double", "nullable": true, "description": "days carried (null on 24 rows)", "example": "0.0"},
  {"name": "_ingested_at", "type": "string", "nullable": false, "description": "UTC ingest time", "example": "2026-07-09T22:00:09+00:00"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF NAV history",
  "fund AUM time series"
 ],
 "common_queries": [
  "Give me DIVZ daily net assets since July."
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_nav_history", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<start..end>", "fund_ticker": "<Opal ticker>"}, "returns": "as silver/netassets; this file is the one-read backing for ranges since 2026-07-09", "answers": ["Give me DIVZ daily net assets since July."]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-positioning/20260821T194927Z/DECOMP.md@20c092c0da (no certified rectangle) (ETFS-a-8 legacy root)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"}
 ]
}
```

### opal-data-etfs/silver/snapshots

```json
{
 "contract_id": "opal-data-etfs/silver/snapshots",
 "bucket": "opal-data-etfs",
 "s3_prefix": "snapshots/snapshot_{YYYY-MM-DD}.json",
 "layer": "silver",
 "format": "json",
 "table": "snapshots",
 "grain": "one file per run date, one record per Opal fund (nav, price, shares, net assets each with its own as-of)",
 "partition": {"keys": ["run date (file name)"], "claim": "measured"},
 "producer": {"name": "etfs-netassets-daily (infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:134-138)", "schedule": "EventBridge etfs-netassets-daily cron(0 22 * * ? *) UTC, ENABLED (fires 7 days/week)", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "124 files 2026-05-15..2026-10-13 (494 records; 123 files hold 4, 1 holds 2)"},
 "size": {"objects": 124, "bytes": 359510, "rows_all_files": 494, "claim": "measured"},
 "columns": [
  {"name": "ticker", "type": "string", "nullable": false, "description": "fund ticker", "example": "DIVZ"},
  {"name": "name", "type": "string", "nullable": false, "description": "fund name", "example": "Polen Dividend Income ETF"},
  {"name": "nav", "type": "double", "nullable": false, "description": "NAV per share", "example": "37.31"},
  {"name": "nav_as_of", "type": "string(date)", "nullable": false, "description": "NAV as-of", "example": "2026-10-12"},
  {"name": "market_price", "type": "double", "nullable": false, "description": "closing price", "example": "37.32"},
  {"name": "market_price_as_of", "type": "string(date)", "nullable": false, "description": "price as-of", "example": "2026-10-12"},
  {"name": "shares_outstanding", "type": "double", "nullable": false, "description": "shares outstanding", "example": "8170000"},
  {"name": "shares_outstanding_as_of", "type": "string(date)", "nullable": false, "description": "as-of", "example": "2026-10-12"},
  {"name": "net_assets_reported", "type": "double", "nullable": false, "description": "issuer net assets", "example": "3.05e8"},
  {"name": "net_assets_as_of", "type": "string(date)", "nullable": false, "description": "as-of", "example": "2026-10-12"},
  {"name": "market_value_computed", "type": "double", "nullable": false, "description": "nav x shares", "example": "3.05e8"},
  {"name": "computed_vs_reported_pct", "type": "double", "nullable": false, "description": "pct gap computed vs reported", "example": "0.0162"},
  {"name": "source", "type": "string", "nullable": false, "description": "issuer source", "example": "trueshares"},
  {"name": "staleness_days", "type": "int", "nullable": false, "description": "days carried", "example": "0"},
  {"name": "note", "type": "string", "nullable": false, "description": "free text", "example": "TrueShares live draw"},
  {"name": "key", "type": "string", "nullable": false, "description": "fund key", "example": "divz"},
  {"name": "run_date", "type": "string(date)", "nullable": false, "description": "run date", "example": "2026-10-13"},
  {"name": "run_ts_utc", "type": "string(ts)", "nullable": false, "description": "run time", "example": "2026-10-13T22:00:09Z"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF daily snapshot",
  "fund NAV snapshot"
 ],
 "common_queries": [
  "What was PFDE's NAV and net assets on the last run?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_nav_history", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<Opal ticker>"}, "returns": "the snapshot record (per-field as-of)", "answers": ["What was PFDE's NAV and net assets on the last run?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-positioning/20260821T194927Z/DECOMP.md@20c092c0da (no certified rectangle) (ETFS-a-4)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "get_object of all 124 snapshots/ files (row census)", "at": "2026-10-14T13:3xZ"}
 ]
}
```

### opal-data-etfs/silver/etf_history_csv

```json
{
 "contract_id": "opal-data-etfs/silver/etf_history_csv",
 "bucket": "opal-data-etfs",
 "s3_prefix": "etf_history.csv",
 "layer": "silver",
 "format": "csv",
 "table": "etf_history",
 "grain": "one line per (run date, Opal fund); the CSV twin of netassets_daily (388 data lines + header, 18 columns)",
 "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "etfs-netassets-daily (infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:134-138)", "schedule": "EventBridge etfs-netassets-daily cron(0 22 * * ? *) UTC, ENABLED (fires 7 days/week)", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13 (last line run_date)", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "first line 2026-07-09"},
 "size": {"objects": 1, "bytes": 121819, "rows": 388, "claim": "measured"},
 "columns": [
  {"name": "run_date", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "run_ts_utc", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "key", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "ticker", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "name", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "source", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "staleness_days", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "nav", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "nav_as_of", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "market_price", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "market_price_as_of", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "shares_outstanding", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "shares_outstanding_as_of", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "net_assets_reported", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "net_assets_as_of", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "market_value_computed", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "computed_vs_reported_pct", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null},
  {"name": "note", "type": "string(csv)", "nullable": false, "description": "same meaning as the snapshots field of that name", "example": null}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF history csv"
 ],
 "common_queries": [
  "Download the ETF NAV history."
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-positioning/20260821T194927Z/DECOMP.md@20c092c0da (no certified rectangle) (ETFS-a-8 legacy root)",
 "open_items": [
  "duplicate of netassets_daily.parquet in CSV form; no tool proposed (read the parquet)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "get_object etf_history.csv (389 lines)", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/config/etf_universe

```json
{
 "contract_id": "opal-data-etfs/config/etf_universe",
 "bucket": "opal-data-etfs",
 "s3_prefix": "config/etf_universe.json",
 "layer": "served",
 "format": "json",
 "table": "etf_universe",
 "grain": "one object: the Opal ETF universe (tickers, full names, SMA name rules)",
 "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "hand-maintained config (owner field 0.4.0_DS_ClientPlatform); read at runtime by cot/inf ownership Lambdas, the dashboard and the renderer", "schedule": "on edit; last_updated 2026-10-09 (LastModified 2026-10-09T14:14:17Z)", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-09 (last_updated)", "basis": "config, not time-series", "claim": "measured"},
 "size": {"objects": 1, "bytes": 2969, "claim": "measured"},
 "columns": [
  {"name": "tickers", "type": "list[4]", "nullable": false, "description": "DIVZ, IDVZ, PFDE, PFOE", "example": "DIVZ"},
  {"name": "full_names", "type": "dict ticker -> {name, source}", "nullable": false, "description": "display names with provenance", "example": "Polen Dividend Income ETF"},
  {"name": "sma_name_rules", "type": "list[4] {member, pattern, source}", "nullable": false, "description": "regex rules mapping SMA/model names to the fund", "example": "Pathfinder\\s+Disciplined"},
  {"name": "owner / last_updated / deployed_to / description / schema_version", "type": "string", "nullable": false, "description": "metadata", "example": "2026-10-09"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "Opal ETF list",
  "which ETFs does Opal run"
 ],
 "common_queries": [
  "Which ETFs are in the Opal universe?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (INGEST-INV-3)",
 "open_items": [
  "no tool proposed: fold the universe into etfs_get_fund_nav_history's ticker enum"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"}
 ]
}
```

### opal-data-etfs/gold/book

```json
{
 "contract_id": "opal-data-etfs/gold/book",
 "bucket": "opal-data-etfs",
 "s3_prefix": "gold/book/date={YYYY-MM-DD}/book.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "book",
 "grain": "one row per (date, Opal fund): AUM, NAV, allocation, management style, characteristics, sector/geography/industry-group mix as JSON",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "etf-positioning-producer (source data/etfs/scripts/gold, per lambda-source-map.json)", "schedule": "EventBridge etf-positioning-producer-daily cron(0 13 * * ? *) UTC, ENABLED", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13 (re-listed 2026-10-14T13:24Z; census listing at 12:57Z showed 2026-10-09)", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "33 partitions at census 2026-08-21..2026-10-09; trading days missing: 2026-09-03, 2026-09-22, and 2026-10-12 (skipped: the 10-13 13:00Z run wrote date=2026-10-09, the 10-14 run wrote date=2026-10-13)"},
 "size": {"objects": 33, "bytes": 735654, "rows_all_parts": 132, "rows_newest_part_per_partition": 132, "rows_newest_partition": 4, "schema_variants": 3, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "date32[day]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-09"},
  {"name": "code", "type": "string", "nullable": false, "description": "fund ticker", "example": "DIVZ"},
  {"name": "name", "type": "string", "nullable": false, "description": "name (fund or security)", "example": "Polen Dividend Income ETF"},
  {"name": "data_as_of", "type": "date32[day]", "nullable": false, "description": "as-of date of the data in the row", "example": "2026-10-08"},
  {"name": "as_of_basis", "type": "string", "nullable": false, "description": "row-sourced", "example": "row-sourced"},
  {"name": "prior_date", "type": "date32[day]", "nullable": false, "description": "previous book date", "example": "2026-10-07"},
  {"name": "holdings_status", "type": "string", "nullable": false, "description": "full / shell / book_only", "example": "full"},
  {"name": "num_holdings", "type": "int64", "nullable": false, "description": "holding count", "example": "31"},
  {"name": "aum", "type": "double", "nullable": false, "description": "assets under management (fund) or holding market cap (gold/holding)", "example": "301948200.0"},
  {"name": "nav", "type": "double", "nullable": false, "description": "net asset value per share", "example": "37.12"},
  {"name": "alloc_cash", "type": "int64", "nullable": false, "description": "cash allocation pct (int64 in some parts, double in others)", "example": "0"},
  {"name": "alloc_fixed_income", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "1.13"},
  {"name": "alloc_equity", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "98.87"},
  {"name": "alloc_hedge", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.0"},
  {"name": "mgmt_active", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "100.0"},
  {"name": "mgmt_passive", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.0"},
  {"name": "char_yield", "type": "double", "nullable": false, "description": "fund yield", "example": "1.4904"},
  {"name": "char_cost", "type": "double", "nullable": false, "description": "expense ratio", "example": "0.65"},
  {"name": "char_duration", "type": "null", "nullable": true, "description": "duration (null for equity funds)", "example": null},
  {"name": "char_beta", "type": "double", "nullable": false, "description": "beta", "example": "0.586"},
  {"name": "segment_sector_json", "type": "string", "nullable": false, "description": "JSON sector -> pct", "example": "{\"Information Technology\": 17.98, \"Financials..."},
  {"name": "segment_geography_json", "type": "string", "nullable": false, "description": "JSON region -> pct", "example": "{\"Emerging\": 0.0, \"International\": 2.77, \"Oth..."},
  {"name": "segment_industry_group_json", "type": "string", "nullable": false, "description": "JSON GICS industry group -> pct", "example": "{\"Capital Goods\": 3.0, \"Energy\": 16.53, \"Fina..."},
  {"name": "industry_group_covered_rows", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "28"},
  {"name": "industry_group_eligible_rows", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "29"},
  {"name": "industry_group_covered_weight", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "96.7"},
  {"name": "industry_group_eligible_weight", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "98.87"},
  {"name": "industry_group_book_weight", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "100.0"},
  {"name": "industry_group_weight_basis", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "raw-book-weight-unnormalised"}
 ],
 "enums": {"holdings_status": ["full", "shell", "book_only"], "code": ["DIVZ", "IDVZ", "PFDE", "PFOE"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF positioning",
  "fund allocation",
  "sector mix",
  "ETF characteristics",
  "fund positioning over time"
 ],
 "common_queries": [
  "What was PFDE's sector mix on 2026-09-15?",
  "How has DIVZ's yield changed since August?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_positioning (extend)", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date, NEW>", "fund_ticker": "<Opal ticker, NEW optional>"}, "returns": "today: the served portal-v2 platinum/etfs/positioning_data.json; extended: the gold book + holdings rows for a past date (history from 2026-08-21)", "answers": ["What was PFDE's sector mix on 2026-09-15?", "How has DIVZ's yield changed since August?"]}
 ],
 "catalog_entry": {"data_catalog_key": "portal_etfs_positioning / etfs.01.positioning-data (the platinum object built FROM this table; the gold table itself is not rowed)", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (INGEST-T3-1 gold home re-point, landed)",
 "open_items": [
  "gold skips a trading day when the Bloomberg L1 landing (bbg/<D>/) arrives after 13:00Z (bbg/2026-10-12 landed 14:39:56Z) -- 3 trading days missing",
  "gateway role: GetObject on gold/book simulates implicitDeny (read-grant widening needed)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "list_objects_v2 Prefix gold/book/ re-list", "at": "2026-10-14T13:24:51Z"},
  {"read": "iam simulate_principal_policy opal-gateway-role s3:GetObject gold/book -> implicitDeny", "at": "2026-10-14T13:3xZ"}
 ]
}
```

### opal-data-etfs/gold/holding

```json
{
 "contract_id": "opal-data-etfs/gold/holding",
 "bucket": "opal-data-etfs",
 "s3_prefix": "gold/holding/date={YYYY-MM-DD}/holding.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "holding",
 "grain": "one row per (date, Opal fund, holding) with classification, characteristics and period returns",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "etf-positioning-producer (source data/etfs/scripts/gold, per lambda-source-map.json)", "schedule": "EventBridge etf-positioning-producer-daily cron(0 13 * * ? *) UTC, ENABLED", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-09 at census (2026-10-13 inferred landed with gold/book at 13:01Z)", "trading_days_behind_T-1": 2, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "same partition set as gold/book"},
 "size": {"objects": 33, "bytes": 1465275, "rows_all_parts": 6126, "rows_newest_part_per_partition": 6126, "rows_newest_partition": 188, "schema_variants": 3, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "date32[day]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-09"},
  {"name": "book", "type": "string", "nullable": false, "description": "fund ticker (the positioning book)", "example": "DIVZ"},
  {"name": "ticker", "type": "string", "nullable": false, "description": "ticker", "example": "PM"},
  {"name": "name", "type": "string", "nullable": false, "description": "name (fund or security)", "example": "Philip Morris International Inc"},
  {"name": "cusip", "type": "string", "nullable": true, "description": "CUSIP as used by the row", "example": "718172109"},
  {"name": "asset_class", "type": "string", "nullable": false, "description": "Equity / Fixed Income", "example": "Equity"},
  {"name": "sub_asset_class", "type": "string", "nullable": true, "description": "GICS sector (ratified 12-value vocabulary)", "example": "Consumer Staples"},
  {"name": "industry_group", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Food, Beverage & Tobacco"},
  {"name": "industry_group_basis", "type": "string", "nullable": false, "description": "observed / not-applicable-non-equity / security-not-in-characteristics", "example": "observed"},
  {"name": "weight", "type": "double", "nullable": false, "description": "weight in pct-points", "example": "6.47"},
  {"name": "market_value", "type": "double", "nullable": false, "description": "position market value, USD", "example": "19629952.5"},
  {"name": "shares", "type": "double", "nullable": true, "description": "shares held", "example": "97905.0"},
  {"name": "price", "type": "double", "nullable": true, "description": "price per share (often null for TrueShares rows)", "example": "0.0"},
  {"name": "is_cash", "type": "bool", "nullable": false, "description": "cash line flag", "example": "False"},
  {"name": "fee", "type": "null", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "aum", "type": "double", "nullable": true, "description": "holding market cap (from Bloomberg)", "example": "313577437792.41"},
  {"name": "yield", "type": "double", "nullable": true, "description": "dividend yield", "example": "3.1815470746507417"},
  {"name": "duration", "type": "null", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "credit", "type": "null", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "beta", "type": "double", "nullable": true, "description": "adjusted beta", "example": "0.31195226739276233"},
  {"name": "active", "type": "bool", "nullable": false, "description": "active flag", "example": "True"},
  {"name": "domicile", "type": "string", "nullable": true, "description": "country of domicile", "example": "US"},
  {"name": "geography", "type": "string", "nullable": false, "description": "US / International / Emerging / Other", "example": "US"},
  {"name": "return_1D", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "4.0531"},
  {"name": "return_WTD", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "6.956"},
  {"name": "return_MTD", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "5.9695"},
  {"name": "return_1M", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "10.7825"},
  {"name": "return_QTD", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "5.9695"},
  {"name": "return_1Q", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "8.0939"},
  {"name": "return_YTD", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "28.2462"},
  {"name": "return_1Y", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "34.3155"}
 ],
 "enums": {"book": ["DIVZ", "IDVZ", "PFDE", "PFOE"], "geography": ["US", "International", "Emerging", "Other"], "asset_class": ["Equity", "Fixed Income"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF holdings with sectors",
  "fund holdings returns",
  "DIVZ top holdings",
  "holding contribution"
 ],
 "common_queries": [
  "What are IDVZ's top 10 holdings and their YTD returns?",
  "Which PFOE holdings are international?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_fund_holdings", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<Opal ticker>"}, "returns": "holdings rows with sector, geography, characteristics and returns", "answers": ["What are IDVZ's top 10 holdings and their YTD returns?", "Which PFOE holdings are international?"]}
 ],
 "catalog_entry": {"data_catalog_key": "etfs.01.positioning-data (platinum object built from this table)", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"}
 ]
}
```

### opal-data-etfs/silver/bbg_characteristics

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_characteristics",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/characteristics.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_characteristics",
 "grain": "one row per (as_of, security in the Opal fund universe + extras): Bloomberg reference fields (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 38, "rows_all_parts": 6291, "rows_newest_partition": 172, "schema_variants": 8, "claim": "measured"},
 "columns": [
  {"name": "security", "type": "large_string", "nullable": false, "description": "Bloomberg security string", "example": "AMX US Equity"},
  {"name": "NAME", "type": "large_string", "nullable": false, "description": "Bloomberg name", "example": "AMERICA MOVIL SAB DE CV"},
  {"name": "EQY_DVD_YLD_IND_NET", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "2.8621309137872224"},
  {"name": "BETA_ADJ_OVERRIDABLE", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "0.47039964329613737"},
  {"name": "GICS_SECTOR_NAME", "type": "large_string", "nullable": true, "description": "name-evident; see producer source", "example": "Communication Services"},
  {"name": "GICS_INDUSTRY_GROUP_NAME", "type": "large_string", "nullable": true, "description": "name-evident; see producer source", "example": "Telecommunication Services"},
  {"name": "GICS_INDUSTRY_GROUP", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "5010.0"},
  {"name": "CNTRY_OF_DOMICILE", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "MX"},
  {"name": "CUR_MKT_CAP", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "64739732000.0"},
  {"name": "FUND_EXPENSE_RATIO", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "0.14"},
  {"name": "FUND_TOTAL_ASSETS", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "62356.84218912"},
  {"name": "TOTAL_NUMBER_OF_HOLDINGS_IN_PORT", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "111.0"},
  {"name": "HB_OAS_EFF_DURTN", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "0.1689249479252354"},
  {"name": "YAS_ISPREAD_TO_GOVT", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "772.2893278892893"},
  {"name": "TRACKING_ERROR", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "2.004533290863037"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "holding characteristics",
  "Bloomberg fields for ETF holdings"
 ],
 "common_queries": [
  "What is the beta and dividend yield of each DIVZ holding?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [
  "run_class lives only in run_manifest.json; a reader counting landings must read it (a prefix can mix scheduled and adhoc sets, ETFS_INGEST F7)",
  "8 schema variants; one part carries an __error__ column"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bbg_fund_daily

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_fund_daily",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/fund_daily.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_fund_daily",
 "grain": "one row per (as_of, Opal fund): price, total assets, NAV, yield, beta from Bloomberg (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 38, "rows_all_parts": 152, "rows_newest_partition": 4, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "large_string", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13"},
  {"name": "PX_LAST", "type": "double", "nullable": false, "description": "last price", "example": "37.2658"},
  {"name": "FUND_TOTAL_ASSETS", "type": "double", "nullable": false, "description": "fund total assets (USD mm)", "example": "304.2993"},
  {"name": "FUND_NET_ASSET_VAL", "type": "double", "nullable": false, "description": "NAV", "example": "37.2459"},
  {"name": "EQY_DVD_YLD_IND_NET", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "1.4861"},
  {"name": "BETA_ADJ_OVERRIDABLE", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.5851"},
  {"name": "security", "type": "large_string", "nullable": false, "description": "Bloomberg security string", "example": "DIVZ US Equity"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF NAV Bloomberg",
  "fund total assets"
 ],
 "common_queries": [
  "What does Bloomberg show for DIVZ's NAV and yield yesterday?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_fund_bloomberg_profile", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<Opal ticker>"}, "returns": "fund_daily + derived_summary + sector/geo allocation for one fund and as-of (one read of bbg/<as_of>/)", "answers": ["What does Bloomberg show for DIVZ's NAV and yield yesterday?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bbg_history_topup

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_history_topup",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/history_topup.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_history_topup",
 "grain": "one row per (security, date): last price + daily gross total return, the window since the prior landing (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 38, "rows_all_parts": 9718, "rows_newest_partition": 177, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "large_string", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13"},
  {"name": "PX_LAST", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "341.27"},
  {"name": "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS", "type": "double", "nullable": true, "description": "daily gross total return pct", "example": "0.088"},
  {"name": "security", "type": "large_string", "nullable": false, "description": "Bloomberg security string", "example": "AAPL US Equity"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "holding price history",
  "daily returns"
 ],
 "common_queries": [
  "What was AAPL's total return yesterday?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bbg_constituents_issuer_fill

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_constituents_issuer_fill",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/constituents/constituents_issuer_fill.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_constituents_issuer_fill",
 "grain": "one row per (Opal fund, holding): the issuer constituent list used for the Bloomberg leg (copy of silver/holdings + fill_source) (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 37, "rows_all_parts": 6589, "rows_newest_partition": 186, "schema_variants": 5, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "timestamp[ns]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-12 00:00:00"},
  {"name": "run_date", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-13"},
  {"name": "fund_key", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "divz"},
  {"name": "fund_ticker", "type": "large_string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "DIVZ"},
  {"name": "holding_ticker", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "PM"},
  {"name": "cusip", "type": "large_string", "nullable": false, "description": "CUSIP as used by the row", "example": "718172109"},
  {"name": "security_name", "type": "large_string", "nullable": false, "description": "security long name", "example": "Philip Morris International Inc"},
  {"name": "shares", "type": "double", "nullable": false, "description": "shares held", "example": "97905.0"},
  {"name": "price", "type": "double", "nullable": true, "description": "price per share (often null for TrueShares rows)", "example": "0.0"},
  {"name": "market_value", "type": "double", "nullable": false, "description": "position market value, USD", "example": "19776810.0"},
  {"name": "weight_pct", "type": "double", "nullable": false, "description": "position weight in pct-points (sums ~100 per fund)", "example": "6.49"},
  {"name": "is_cash", "type": "bool", "nullable": true, "description": "cash line flag", "example": "False"},
  {"name": "run_class", "type": "large_string", "nullable": false, "description": "scheduled or adhoc (ad-hoc rows are never production evidence)", "example": "scheduled"},
  {"name": "cash_basis", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "field-absent"},
  {"name": "id_kind", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "cusip"},
  {"name": "cusip_as_delivered", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "718172109"},
  {"name": "cusip_basis", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "as-delivered"},
  {"name": "as_of_basis", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "issuer-holdings-file"},
  {"name": "fund_net_assets", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "304854991.4"},
  {"name": "fund_shares_outstanding", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "8170000.0"},
  {"name": "source", "type": "large_string", "nullable": false, "description": "vendor/source of the row", "example": "trueshares"},
  {"name": "source_system", "type": "large_string", "nullable": false, "description": "producing system tag", "example": "etf_netassets_watch"},
  {"name": "data_as_of", "type": "timestamp[ns]", "nullable": false, "description": "as-of date of the data in the row", "example": "2026-10-12 00:00:00"},
  {"name": "_ingested_at", "type": "large_string", "nullable": false, "description": "UTC ingest time", "example": "2026-10-13T22:00:09+00:00"},
  {"name": "vendor_filepoint_Account", "type": "large_string", "nullable": true, "description": "name-evident; see producer source", "example": "PFDE"},
  {"name": "vendor_filepoint_CreationUnits", "type": "large_string", "nullable": true, "description": "name-evident; see producer source", "example": "601.000000000000"},
  {"name": "vendor_trueshares_Date", "type": "large_string", "nullable": true, "description": "name-evident; see producer source", "example": "2026-10-12"},
  {"name": "vendor_trueshares_Account", "type": "large_string", "nullable": true, "description": "name-evident; see producer source", "example": "DIVZ"},
  {"name": "vendor_trueshares_NetAssets", "type": "null", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "fill_source", "type": "large_string", "nullable": false, "description": "which silver object filled the leg", "example": "pathfinder:silver/holdings/2026-10-13.parquet"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "ETF constituents"
 ],
 "common_queries": [
  "Which constituents were used for PFDE's Bloomberg enrichment?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bbg_derived_summary

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_derived_summary",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/constituents/derived_summary.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_derived_summary",
 "grain": "one row per Opal fund: Bloomberg holdings count and top-10 concentration (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 37, "rows_all_parts": 148, "rows_newest_partition": 4, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "fund_ticker", "type": "large_string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "DIVZ"},
  {"name": "as_of_source", "type": "large_string", "nullable": false, "description": "name-evident; see producer source", "example": "bloomberg"},
  {"name": "name", "type": "large_string", "nullable": false, "description": "name (fund or security)", "example": "ELEVATION SERIES TRUST - POL"},
  {"name": "total_number_of_holdings_in_port", "type": "int64", "nullable": false, "description": "holdings count per Bloomberg", "example": "31"},
  {"name": "fund_pct_top_ten_hold", "type": "double", "nullable": false, "description": "top-10 weight pct", "example": "49.18164"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "fund concentration",
  "number of holdings"
 ],
 "common_queries": [
  "How concentrated is IDVZ in its top 10?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_fund_bloomberg_profile", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<Opal ticker>"}, "returns": "fund_daily + derived_summary + sector/geo allocation for one fund and as-of (one read of bbg/<as_of>/)", "answers": ["How concentrated is IDVZ in its top 10?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bbg_derived_sector_allocation

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_derived_sector_allocation",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/constituents/derived_sector_allocation.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_derived_sector_allocation",
 "grain": "one row per (Opal fund, Bloomberg sector) (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 37, "rows_all_parts": 1547, "rows_newest_partition": 42, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "fund_ticker", "type": "large_string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "DIVZ"},
  {"name": "sector_name", "type": "large_string", "nullable": false, "description": "Bloomberg industry sector label", "example": "Technology (Equity)"},
  {"name": "pct_of_fund", "type": "double", "nullable": false, "description": "percent of fund", "example": "18.066033"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "sector allocation Bloomberg"
 ],
 "common_queries": [
  "What is DIVZ's sector allocation per Bloomberg?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_fund_bloomberg_profile", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<Opal ticker>"}, "returns": "fund_daily + derived_summary + sector/geo allocation for one fund and as-of (one read of bbg/<as_of>/)", "answers": ["What is DIVZ's sector allocation per Bloomberg?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bbg_derived_geo_allocation

```json
{
 "contract_id": "opal-data-etfs/silver/bbg_derived_geo_allocation",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bbg/{YYYY-MM-DD as_of}/constituents/derived_geo_allocation.parquet",
 "layer": "silver",
 "format": "parquet (+ csv twin)",
 "table": "bbg_derived_geo_allocation",
 "grain": "one row per (Opal fund, region) (Bloomberg landing; no bronze tier -- INGEST-T1-4)",
 "partition": {"keys": ["as_of (key segment = Bloomberg as-of, T-1)"], "claim": "measured"},
 "producer": {"name": "site-Z Bloomberg terminal scheduled task (OPAL_BBGTML_daily_pull; integrations/bloomberg/pipeline/etf_daily_pull.py + etf_constituents_pull.py)", "schedule": "~07:00 America/New_York trading days (objects land ~11:05-11:10Z; run_manifest run_class=scheduled)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "37-38 as-of prefixes 2026-08-20/21..2026-10-13, 0 trading days missing"},
 "size": {"objects_parquet": 37, "rows_all_parts": 1258, "rows_newest_partition": 34, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "fund_ticker", "type": "large_string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "DIVZ"},
  {"name": "region", "type": "large_string", "nullable": false, "description": "Bloomberg country/region label", "example": "U.S.A."},
  {"name": "pct_of_fund", "type": "double", "nullable": false, "description": "percent of fund", "example": "95.984279"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "geographic allocation"
 ],
 "common_queries": [
  "What is IDVZ's country mix?"
 ],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [
  {"name": "etfs_get_fund_bloomberg_profile", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<Opal ticker>"}, "returns": "fund_daily + derived_summary + sector/geo allocation for one fund and as-of (one read of bbg/<as_of>/)", "answers": ["What is IDVZ's country mix?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/DECOMP.md@fcdf042972 (UNCERTIFIED; no rectangle.final.certified.json exists) (F7, INGEST-T6-3)",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object bbg/2026-10-13/run_manifest.json + parquet read", "at": "2026-10-14T13:1xZ"}
 ]
}
```

### opal-data-etfs/silver/bloomberg_etf_holdings

```json
{
 "contract_id": "opal-data-etfs/silver/bloomberg_etf_holdings",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bloomberg/etfs/silver/holdings/date={D}/{FUND}-{batch}.parquet",
 "layer": "silver",
 "format": "parquet",
 "table": "bloomberg_etf_holdings",
 "grain": "one row per (report date, fund, Bloomberg holding) from a dated BQL holdings capture; one part per fund per batch",
 "partition": {"keys": ["date (report date)", "fund (file-name prefix)"], "claim": "measured"},
 "producer": {"name": "fetch-bloomberg stage on the terminal machine (data/etfs/scripts/rivalfunds/collector_bloomberg.py) -> marker -> rivalfunds-build-silver-lambda (rule rivalfunds-build-silver-bloomberg-on-marker-created)", "schedule": "terminal daily ~07:07 ET trading days, then S3-marker event", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "511 report dates 2024-09-30..2026-10-13 (backfilled), 0 trading days missing; 2026-10-13 holds 9 funds (BIDD, ETFT, IDVZ, INEQ, PCLG, PFOE, TSEL, TXUE, WCMG)"},
 "size": {"objects": 4114, "bytes": 39165914, "rows_all_parts": 311911, "rows_newest_part_per_partition": 309334, "rows_newest_partition": 431, "schema_variants": 2, "claim": "measured", "note": "25 (date, fund) slots carry re-run parts; newest part per slot sums 309,334 rows"},
 "columns": [
  {"name": "id", "type": "string", "nullable": false, "description": "Bloomberg holding id", "example": "USD Curncy"},
  {"name": "dates", "type": "date32[day]", "nullable": false, "description": "requested date", "example": "2026-10-13"},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "ETF"},
  {"name": "position", "type": "double", "nullable": false, "description": "position (shares/units)", "example": "8130443.650912"},
  {"name": "position_change", "type": "double", "nullable": false, "description": "position change vs prior", "example": "8063197.035959"},
  {"name": "weights", "type": "double", "nullable": false, "description": "weight pct", "example": "2.13412638448893"},
  {"name": "currency", "type": "string", "nullable": false, "description": "currency", "example": "USD"},
  {"name": "reported_mkt_val", "type": "double", "nullable": false, "description": "reported market value", "example": "0.0"},
  {"name": "report_date", "type": "date32[day]", "nullable": false, "description": "holdings report date the issuer or Bloomberg delivered", "example": "2026-10-13"},
  {"name": "orig_ids", "type": "string", "nullable": false, "description": "fund Bloomberg id", "example": "BIDD US Equity"},
  {"name": "position_type", "type": "string", "nullable": false, "description": "L long / S short", "example": "L"},
  {"name": "id_expr", "type": "string", "nullable": false, "description": "id expression", "example": "USD Curncy"},
  {"name": "name", "type": "string", "nullable": false, "description": "name (fund or security)", "example": "US Dollar Spot"},
  {"name": "fund_ticker", "type": "string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "BIDD"},
  {"name": "requested_date", "type": "date32[day]", "nullable": false, "description": "date requested from Bloomberg", "example": "2026-10-13"},
  {"name": "bronze_uri", "type": "string", "nullable": false, "description": "raw capture this row was parsed from", "example": "s3://opal-data-etfs/bloomberg/etfs/bronze/hol..."},
  {"name": "sha256", "type": "string", "nullable": false, "description": "sha256 of the bronze capture", "example": "4ec22a670c4ae68b9907effa6e7dac3a20741dd6a81bb..."},
  {"name": "captured_at", "type": "string", "nullable": false, "description": "UTC capture time", "example": "2026-10-14T11:07:53Z"},
  {"name": "parser_version", "type": "string", "nullable": false, "description": "silver parser version", "example": "silver_bloomberg/1"}
 ],
 "enums": {"source": ["ETF", "REG"], "position_type": ["L", "S"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "rival ETF holdings Bloomberg",
  "competitor fund holdings"
 ],
 "common_queries": [
  "What did INEQ hold on 2026-10-13 per Bloomberg?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_holdings", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<rival ticker>"}, "returns": "served from gold canonical_shape (this silver is its input)", "answers": ["What did INEQ hold on 2026-10-13 per Bloomberg?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"}
 ]
}
```

### opal-data-etfs/silver/bloomberg_history_gaps

```json
{
 "contract_id": "opal-data-etfs/silver/bloomberg_history_gaps",
 "bucket": "opal-data-etfs",
 "s3_prefix": "bloomberg/etfs/silver/history_gaps/as_of={D}/gap_record.json",
 "layer": "silver",
 "format": "json",
 "table": "bloomberg_history_gaps",
 "grain": "one object per as_of: per-security count of Bloomberg vendor observations vs stored rows over a 365-day requirement (188 securities)",
 "partition": {"keys": ["as_of"], "claim": "measured"},
 "producer": {"name": "unattributed (written 2026-10-13T13:01:32Z, co-timed with etf-positioning-producer)", "schedule": "one object only", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-09", "trading_days_behind_T-1": 2, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "1 object"},
 "size": {"objects": 1, "bytes": 69406, "claim": "measured"},
 "columns": [
  {"name": "as_of / basis / required_days / securities_tracked / securities_with_listed_days", "type": "scalars", "nullable": false, "description": "header", "example": "required_days 365"},
  {"name": "securities", "type": "dict[188] ticker -> {7 fields}", "nullable": false, "description": "per-security gap record", "example": "AAPL"},
  {"name": "listed / partitions_read", "type": "list", "nullable": false, "description": "securities with listed gap days; partitions read", "example": "36 partitions"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "price history gaps"
 ],
 "common_queries": [
  "Which holdings are missing price history?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "none",
 "open_items": [
  "producer not attributed; single object -- no tool proposed (ops artifact)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"}
 ]
}
```

### opal-data-etfs/silver/issuer_site_holdings

```json
{
 "contract_id": "opal-data-etfs/silver/issuer_site_holdings",
 "bucket": "opal-data-etfs",
 "s3_prefix": "issuer-site/etfs/silver/holdings/date={D}/{issuer}-{batch}.parquet",
 "layer": "silver",
 "format": "parquet",
 "table": "issuer_site_holdings",
 "grain": "one row per (report date, issuer fund, holding) parsed from the issuer web file; one part per issuer file (basg = Brown Advisory family file carrying BAFE/BASV/BAIV/BASG/...; gqgu = GQG)",
 "partition": {"keys": ["date (report date)", "issuer (file-name prefix)"], "claim": "measured"},
 "producer": {"name": "etfs-rivalfunds-fetch-holdings-lambda (bronze) -> marker -> rivalfunds-build-silver-lambda (rule rivalfunds-build-silver-on-marker-created)", "schedule": "Scheduler etfs-rivalfunds-daily cron(0 7 ? * MON-FRI *) America/New_York -> etfs-rivalfunds-fetch-holdings-lambda; then S3-marker EventBridge rules (rivalfunds-build-silver-*, rivalfunds-build-canonical-shape-*, rivalfunds-publish-page-on-marker-created); Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York -> etfs-rivalfunds-daily-lambda re-runs any stage missing its marker", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "335 report dates 2025-06-13..2026-10-13, 0 trading days missing"},
 "size": {"objects": 650, "bytes": 9692481, "rows_all_parts": 61173, "rows_newest_part_per_partition": 60997, "rows_newest_partition": 211, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "date", "type": "date32[day]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13"},
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "4822"},
  {"name": "fund_name", "type": "string", "nullable": false, "description": "issuer fund name", "example": "Brown Advisory Flexible Equity ETF"},
  {"name": "fund_cusip", "type": "string", "nullable": false, "description": "fund CUSIP", "example": "00775Y322"},
  {"name": "fund_ticker", "type": "string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "BAFE"},
  {"name": "security_group", "type": "string", "nullable": false, "description": "issuer security group", "example": "Cash"},
  {"name": "security_type", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "security_number", "type": "string", "nullable": true, "description": "issuer security number", "example": "CAD"},
  {"name": "security_cusip", "type": "string", "nullable": true, "description": "CUSIP", "example": "016255101"},
  {"name": "security_sedol", "type": "string", "nullable": true, "description": "SEDOL", "example": "2679204"},
  {"name": "security_isin", "type": "string", "nullable": true, "description": "ISIN", "example": "US0162551016"},
  {"name": "security_ticker", "type": "string", "nullable": true, "description": "security ticker", "example": "ALGN"},
  {"name": "security_description", "type": "string", "nullable": false, "description": "issuer description", "example": "Cash"},
  {"name": "quantity", "type": "double", "nullable": false, "description": "quantity held", "example": "34225798.26"},
  {"name": "market_value", "type": "double", "nullable": false, "description": "position market value, USD", "example": "34225798.26"},
  {"name": "notional_value", "type": "double", "nullable": true, "description": "notional (derivatives)", "example": null},
  {"name": "percent_of_market_value", "type": "double", "nullable": false, "description": "pct of market value", "example": "1.94"},
  {"name": "percent_of_net_assets", "type": "double", "nullable": false, "description": "pct of net assets", "example": "1.9"},
  {"name": "bronze_uri", "type": "string", "nullable": false, "description": "raw capture this row was parsed from", "example": "s3://opal-data-etfs/issuer-site/etfs/bronze/h..."},
  {"name": "sha256", "type": "string", "nullable": false, "description": "sha256 of the bronze capture", "example": "14463a540e41818cf490665a0eb13a77ccdb980569ce5..."},
  {"name": "captured_at", "type": "string", "nullable": false, "description": "UTC capture time", "example": "2026-10-14T11:00:33Z"},
  {"name": "parser_version", "type": "string", "nullable": false, "description": "silver parser version", "example": "silver_issuer/1"}
 ],
 "enums": {"fund_ticker (2026-10-13)": ["BAIV", "BAFE", "BASV", "GQGU", "BASG"], "security_group": ["Stock - Common", "Stock - Foreign", "Cash", "Currency"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "issuer holdings file",
  "Brown Advisory ETF holdings",
  "GQG holdings"
 ],
 "common_queries": [
  "What did GQGU hold on 2026-10-13 per the issuer?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "the Brown Advisory file carries 4 non-peer funds (BAFE, BASV, BAIV and others) beside BASG; only BASG is in the peer map"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"}
 ]
}
```

### opal-data-etfs/gold/canonical_shape

```json
{
 "contract_id": "opal-data-etfs/gold/canonical_shape",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/canonical_shape/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "canonical_shape",
 "grain": "one row per (report date, fund, position) across home and rival funds, with identity resolution, GICS and provenance",
 "partition": {"keys": ["date (report date)"], "claim": "measured"},
 "producer": {"name": "rivalfunds-build-canonical-shape-lambda (rules rivalfunds-build-canonical-shape-on-marker-created / -bloomberg-on-marker-created)", "schedule": "S3-marker event after each silver build; Scheduler etfs-rivalfunds-daily cron(0 7 ? * MON-FRI *) America/New_York -> etfs-rivalfunds-fetch-holdings-lambda; then S3-marker EventBridge rules (rivalfunds-build-silver-*, rivalfunds-build-canonical-shape-*, rivalfunds-publish-page-on-marker-created); Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York -> etfs-rivalfunds-daily-lambda re-runs any stage missing its marker", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "511 partitions 2024-09-30..2026-10-13"},
 "size": {"objects": 1382, "bytes": 88341384, "rows_all_parts": 692547, "rows_newest_part_per_partition": 321049, "rows_newest_partition": 500, "schema_variants": 2, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "4823"},
  {"name": "fund_ticker", "type": "string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "BASG"},
  {"name": "fund_name", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Brown Advisory Sustainable Growth ETF"},
  {"name": "fund_cusip", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "00775Y272"},
  {"name": "report_date", "type": "date32[day]", "nullable": false, "description": "holdings report date the issuer or Bloomberg delivered", "example": "2026-10-13"},
  {"name": "snapshot_id", "type": "string", "nullable": false, "description": "fund-date-capture snapshot id", "example": "BASG-2026-10-13-14463a540e41"},
  {"name": "position_id", "type": "string", "nullable": false, "description": "position key within the snapshot", "example": "4823:Cash|Cash:0"},
  {"name": "dataset_revision", "type": "string", "nullable": false, "description": "revision id of the canonical_shape build this row came from", "example": "20261014T110753Z-151ac337dbc8"},
  {"name": "security_id", "type": "string", "nullable": true, "description": "security key in crosswalk grammar (e.g. ABNB_US_Equity)", "example": "ABNB_US_Equity"},
  {"name": "raw_identifier", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "Cash"},
  {"name": "raw_identifier_kind", "type": "string", "nullable": false, "description": "bloomberg_security / cusip / description", "example": "description"},
  {"name": "resolution_status", "type": "string", "nullable": false, "description": "RESOLVED / UNRESOLVED identifier", "example": "UNRESOLVED"},
  {"name": "resolution_method", "type": "string", "nullable": false, "description": "how the identifier was resolved", "example": "not-applicable-cash"},
  {"name": "resolution_source", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "alias of an earlier measured issuer-Bloomberg..."},
  {"name": "resolution_note", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "alias measured on 2026-10-09: CUSIP 009066101..."},
  {"name": "security_bloomberg", "type": "string", "nullable": true, "description": "Bloomberg security string", "example": "ABNB US Equity"},
  {"name": "security_name", "type": "string", "nullable": false, "description": "security long name", "example": "Cash"},
  {"name": "security_ticker", "type": "string", "nullable": true, "description": "security ticker", "example": "ABNB"},
  {"name": "security_cusip", "type": "string", "nullable": true, "description": "CUSIP", "example": "009066101"},
  {"name": "security_isin", "type": "string", "nullable": true, "description": "ISIN", "example": "US0090661010"},
  {"name": "security_sedol", "type": "string", "nullable": true, "description": "SEDOL", "example": "BMGYYH4"},
  {"name": "quantity", "type": "double", "nullable": false, "description": "quantity held", "example": "10413020.53"},
  {"name": "market_value", "type": "double", "nullable": false, "description": "position market value, USD", "example": "10413020.53"},
  {"name": "notional_value", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "weight", "type": "double", "nullable": false, "description": "position weight (fraction in rival gold; pct-points in Opal gold/holding)", "example": "0.019799999999999998"},
  {"name": "weight_basis", "type": "string", "nullable": false, "description": "net_assets", "example": "net_assets"},
  {"name": "position_type", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "cash"},
  {"name": "provider_security_group", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "Cash"},
  {"name": "provider_security_type", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Curncy"},
  {"name": "provider_taxonomy", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "issuer security_group/security_type (not GICS)"},
  {"name": "asset_class", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "Cash"},
  {"name": "asset_class_status", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "RESOLVED"},
  {"name": "sub_asset_class", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Cash & Cash Equivalents"},
  {"name": "sub_asset_class_status", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "RESOLVED"},
  {"name": "classification_source", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "etf_positioning_gold.classify(is_cash) from s..."},
  {"name": "gics_sector", "type": "string", "nullable": true, "description": "GICS sector", "example": "Consumer Discretionary"},
  {"name": "gics_sector_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "gics_industry_group", "type": "string", "nullable": true, "description": "GICS industry group", "example": "Consumer Services"},
  {"name": "gics_industry_group_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "2530"},
  {"name": "gics_industry", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Hotels, Restaurants & Leisure"},
  {"name": "gics_industry_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "253010"},
  {"name": "gics_sub_industry", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Hotels, Resorts & Cruise Lines"},
  {"name": "gics_sub_industry_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "25301020"},
  {"name": "gics_status", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "UNRESOLVED"},
  {"name": "gics_source", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "none (GICS is Bloomberg enrichment)"},
  {"name": "unresolved_identifier", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "False"},
  {"name": "weight_missing", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "False"},
  {"name": "cash_representation", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "issuer-cash-line"},
  {"name": "enrichment_status", "type": "string", "nullable": false, "description": "BLOOMBERG-ONLY / ISSUER-ONLY", "example": "ISSUER-ONLY"},
  {"name": "source_used", "type": "string", "nullable": false, "description": "bloomberg or issuer", "example": "issuer"},
  {"name": "is_cash_line", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "True"},
  {"name": "corporate_action_adjusted", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "False"},
  {"name": "source_channel", "type": "string", "nullable": false, "description": "bloomberg:holdings / issuer-site:<file>", "example": "issuer-site:basg"},
  {"name": "silver_uri", "type": "string", "nullable": false, "description": "silver part this row was built from", "example": "s3://opal-data-etfs/issuer-site/etfs/silver/h..."},
  {"name": "silver_row", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "44"},
  {"name": "bronze_uri", "type": "string", "nullable": false, "description": "raw capture this row was parsed from", "example": "s3://opal-data-etfs/issuer-site/etfs/bronze/h..."},
  {"name": "sha256", "type": "string", "nullable": false, "description": "sha256 of the bronze capture", "example": "14463a540e41818cf490665a0eb13a77ccdb980569ce5..."},
  {"name": "captured_at", "type": "string", "nullable": false, "description": "UTC capture time", "example": "2026-10-14T11:00:33Z"},
  {"name": "parser_version", "type": "string", "nullable": false, "description": "silver parser version", "example": "silver_issuer/1"},
  {"name": "gold_version", "type": "string", "nullable": false, "description": "gold_canonical_shape/<n>", "example": "gold_canonical_shape/2"},
  {"name": "extra_attributes", "type": "string", "nullable": false, "description": "JSON of vendor columns not in the spine", "example": "{\"basg\": {\"percent_of_market_value\": 2.02, \"p..."}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "rival fund holdings",
  "competitor positions",
  "who holds a stock",
  "IDVZ peer holdings",
  "fund holdings over time"
 ],
 "common_queries": [
  "What does BIDD hold today, and how does it compare with IDVZ?",
  "Which IDVZ rivals hold Petrobras?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_holdings", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<home or rival ticker>"}, "returns": "newest-revision holdings snapshot with weights (fraction), identifiers, GICS, source_used", "answers": ["What does BIDD hold today, and how does it compare with IDVZ?"]},
  {"name": "etfs_who_holds", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "security": "<ticker|cusip|bloomberg id>", "peer_group": "<IDVZ|PFOE optional>"}, "returns": "every tracked fund holding the security with weight and market value", "answers": ["Which IDVZ rivals hold Petrobras?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "2026-10-13 newest part covers 11 of 13 peer funds (CGIC and SCHY absent); holdings_coverage reports them as gaps"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/canonical_shape (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/trade_schedule

```json
{
 "contract_id": "opal-data-etfs/gold/trade_schedule",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/trade_schedule/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "trade_schedule",
 "grain": "one row per (date, fund, security, inferred action) between consecutive holdings snapshots",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "the stage after build-canonical-shape (state markers build_coverage / build_flow_reconciliation / build_trade_schedule are written 1-2 min after canonical_shape; no dedicated rule) -- inferred to run in rivalfunds-build-canonical-shape-lambda", "schedule": "same event chain", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "510 partitions 2024-10-01..2026-10-13"},
 "size": {"objects": 1562, "bytes": 23059679, "rows_all_parts": 55540, "rows_newest_part_per_partition": 21057, "rows_newest_partition": 51, "schema_variants": 5, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "fund_ticker", "type": "string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "BIDD"},
  {"name": "security_key", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "000660_KS_Equity"},
  {"name": "security_key_kind", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "security_id"},
  {"name": "key_resolved", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "True"},
  {"name": "counterpart_security_key", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "action", "type": "string", "nullable": false, "description": "inferred trade action: entry, exit, add, trim, below_tolerance", "example": "trim"},
  {"name": "date", "type": "date32[day]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13"},
  {"name": "window_start", "type": "date32[day]", "nullable": false, "description": "first day of the window", "example": "2026-10-12"},
  {"name": "window_end", "type": "date32[day]", "nullable": false, "description": "last day of the window", "example": "2026-10-13"},
  {"name": "window_trading_days", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "1"},
  {"name": "shares_before", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "9369.0"},
  {"name": "shares_after", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "8650.0"},
  {"name": "flow_factor", "type": "double", "nullable": false, "description": "creation/redemption flow factor", "example": "1.0"},
  {"name": "discretionary_shares", "type": "double", "nullable": false, "description": "share change net of flows", "example": "-719.0"},
  {"name": "est_price", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "1097.3559787336417"},
  {"name": "est_price_band", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "est_price_band_reason", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "bloomberg-band-enrichment"},
  {"name": "est_notional", "type": "double", "nullable": true, "description": "estimated trade notional, USD (INFERRED)", "example": "-788998.9487094884"},
  {"name": "weight_before", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.028684667109846705"},
  {"name": "weight_after", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.024915495727800416"},
  {"name": "confidence", "type": "string", "nullable": false, "description": "CLEAN / other confidence class", "example": "CLEAN"},
  {"name": "window_widened", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "False"},
  {"name": "flow_adjusted", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "False"},
  {"name": "corporate_actions_applied", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "G3@20260930-95af6e3d1a1c+20261009-03f579b8850..."},
  {"name": "dividends_applied", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "G3@20260930-95af6e3d1a1c+20261009-03f579b8850..."},
  {"name": "dataset_revision", "type": "string", "nullable": false, "description": "revision id of the canonical_shape build this row came from", "example": "20261014T110753Z-151ac337dbc8"},
  {"name": "prior_dataset_revision", "type": "string", "nullable": false, "description": "revision compared against", "example": "20261014T110753Z-44303a3d5969"},
  {"name": "inference_version", "type": "string", "nullable": false, "description": "gold_trade_schedule/<n>", "example": "gold_trade_schedule/4"},
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "BIDD"},
  {"name": "security_id", "type": "string", "nullable": false, "description": "security key in crosswalk grammar (e.g. ABNB_US_Equity)", "example": "000660 KS Equity"},
  {"name": "shares_before_adjusted", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "9369.0"},
  {"name": "shares_delta", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "-719.0"},
  {"name": "flow_factor_f", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "1.0"},
  {"name": "residual_pct_prior", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "-0.07674244850037357"},
  {"name": "price_band_lo", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "price_band_hi", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "est_notional_base", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "-788998.9487094884"},
  {"name": "income_funded", "type": "bool", "nullable": false, "description": "trade funded by income", "example": "False"},
  {"name": "corporate_action_ref", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "corporate_actions_revision", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "20260930-95af6e3d1a1c+20261009-03f579b88503+2..."},
  {"name": "key_resolution", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "RESOLVED"},
  {"name": "est_price_source", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "prior_valuation"},
  {"name": "window_start_delivered", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-12"},
  {"name": "window_end_delivered", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-13"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "rival fund trades",
  "what did competitors buy",
  "entries and exits",
  "position changes"
 ],
 "common_queries": [
  "What did the PFOE rivals buy or sell this week?",
  "When did WCMG exit a position?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_trades", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<start..end>", "fund_ticker": "<ticker or peer group>", "action": "<entry|exit|add|trim optional>"}, "returns": "inferred trades (claim INFERRED) with shares delta, est notional, confidence", "answers": ["What did the PFOE rivals buy or sell this week?", "When did WCMG exit a position?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "5 schema variants (gold_trade_schedule versions); older parts of a date are superseded revisions with different keys (2026-09-29: 48 keys absent from the newest part) -- read the newest revision only"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/trade_schedule (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/flow_reconciliation

```json
{
 "contract_id": "opal-data-etfs/gold/flow_reconciliation",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/flow_reconciliation/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "flow_reconciliation",
 "grain": "one row per (date, fund): cash-line delta reconciled against income, corporate actions and trades",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "the stage after build-canonical-shape (state markers build_coverage / build_flow_reconciliation / build_trade_schedule are written 1-2 min after canonical_shape; no dedicated rule) -- inferred to run in rivalfunds-build-canonical-shape-lambda", "schedule": "same event chain", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "510 partitions 2024-10-01..2026-10-13"},
 "size": {"objects": 1238, "bytes": 17564616, "rows_all_parts": 11698, "rows_newest_part_per_partition": 4397, "rows_newest_partition": 11, "schema_variants": 2, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "BASG"},
  {"name": "fund_ticker", "type": "string", "nullable": false, "description": "fund (ETF) ticker the row belongs to", "example": "BASG"},
  {"name": "window_start", "type": "date32[day]", "nullable": false, "description": "first day of the window", "example": "2026-10-12"},
  {"name": "window_end", "type": "date32[day]", "nullable": false, "description": "last day of the window", "example": "2026-10-13"},
  {"name": "window_trading_days", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "1"},
  {"name": "flow_factor_f", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "1.0"},
  {"name": "cash_line_delta_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "-8829.35000000149"},
  {"name": "income_received_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.0"},
  {"name": "fx_conversion_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.0"},
  {"name": "income_cash_check_passed", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "False"},
  {"name": "corporate_action_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "share_event_applied_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "share_event_pending_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "income_funded_trade_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "unexplained_residual_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.0"},
  {"name": "cash_line_value_before_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "10421849.88"},
  {"name": "cash_line_value_after_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "10413020.53"},
  {"name": "cash_lines_excluded", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "1"},
  {"name": "income_event_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "income_unconverted_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "income_implausible_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "income_ignored_event_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "unknown_event_type_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "unapplied_share_event_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "trade_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "trade_net_notional_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "0.0"},
  {"name": "dataset_revision", "type": "string", "nullable": false, "description": "revision id of the canonical_shape build this row came from", "example": "20261014T110753Z-151ac337dbc8"},
  {"name": "prior_dataset_revision", "type": "string", "nullable": false, "description": "revision compared against", "example": "20261014T110753Z-44303a3d5969"},
  {"name": "corporate_actions_revision", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "20260930-95af6e3d1a1c+20261009-03f579b88503+2..."},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261014T110753Z-151ac337dbc8"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-14T11:10:37Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_flow_reconciliation/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"canonical_shape\": \"s3://opal-data-etfs/riva..."},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "INFERRED"},
  {"name": "inputs_claim", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "MEASURED"},
  {"name": "status", "type": "string", "nullable": true, "description": "row status", "example": null},
  {"name": "reason", "type": "string", "nullable": true, "description": "reason text", "example": null}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "fund flows",
  "creations redemptions",
  "cash reconciliation"
 ],
 "common_queries": [
  "Did BIDD have net flows on 2026-10-13?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_fund_flows", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<start..end>", "fund_ticker": "<ticker>"}, "returns": "flow factor, cash-line delta, unexplained residual, trade counts per day (claim INFERRED)", "answers": ["Did BIDD have net flows on 2026-10-13?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/flow_reconciliation (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/holdings_coverage

```json
{
 "contract_id": "opal-data-etfs/gold/holdings_coverage",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/holdings_coverage/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "holdings_coverage",
 "grain": "one row per (expected date, fund): did a holdings report arrive, from which source, gap/new status",
 "partition": {"keys": ["date (expected date)"], "claim": "measured"},
 "producer": {"name": "the stage after build-canonical-shape (state markers build_coverage / build_flow_reconciliation / build_trade_schedule are written 1-2 min after canonical_shape; no dedicated rule) -- inferred to run in rivalfunds-build-canonical-shape-lambda", "schedule": "same event chain", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "511 partitions 2024-09-30..2026-10-13"},
 "size": {"objects": 511, "bytes": 3714586, "rows_all_parts": 4520, "rows_newest_part_per_partition": 4520, "rows_newest_partition": 13, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "IDVZ"},
  {"name": "expected_date", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-13"},
  {"name": "source", "type": "string", "nullable": true, "description": "vendor/source of the row", "example": "issuer"},
  {"name": "actual_report_date", "type": "date32[day]", "nullable": true, "description": "name-evident; see producer source", "example": "2026-10-13"},
  {"name": "status", "type": "string", "nullable": false, "description": "row status", "example": "gap"},
  {"name": "row_count", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "weight_sum", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "1.0"},
  {"name": "selected", "type": "bool", "nullable": false, "description": "name-evident; see producer source", "example": "True"},
  {"name": "selection_reason", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "no source delivered a report for this day: th..."},
  {"name": "g1_source_used", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "issuer"},
  {"name": "source_policy", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "bloomberg_primary"},
  {"name": "cadence_gap_median", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "1.0"},
  {"name": "capture_id", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "20261014T110033Z-0d89df972c6d"},
  {"name": "capture_status", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "OK"},
  {"name": "sidecar_uri", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "s3://opal-data-etfs/issuer-site/etfs/bronze/h..."},
  {"name": "bronze_uri", "type": "string", "nullable": true, "description": "raw capture this row was parsed from", "example": "s3://opal-data-etfs/issuer-site/etfs/bronze/h..."},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"},
  {"name": "gold_version", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "gold_holdings_coverage/1"},
  {"name": "map_version", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "2"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "holdings coverage",
  "data gaps",
  "missing fund report"
 ],
 "common_queries": [
  "Which rival funds are missing holdings for 2026-10-13?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_coverage", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<optional>"}, "returns": "per-fund coverage status + input_census reasons", "answers": ["Which rival funds are missing holdings for 2026-10-13?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "INCONSISTENT AT READ: holdings_coverage date=2026-10-13 (written 11:03:27Z, before the 11:07Z Bloomberg batch) says 11 of 13 funds 'gap', while canonical_shape date=2026-10-13 newest part holds 11 funds -- the coverage table was not rewritten after the Bloomberg leg (state/build_coverage has a later batch marker at 11:10:36Z)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/holdings_coverage (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "one part per partition"
 ]
}
```

### opal-data-etfs/gold/peer_group_map

```json
{
 "contract_id": "opal-data-etfs/gold/peer_group_map",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/peer_group_map/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "peer_group_map",
 "grain": "one row per (peer group, fund): home/rival role and source policy",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "etfs-rivalfunds-daily-lambda sweep (writes at ~13:00-13:08Z)", "schedule": "Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "10 partitions 2026-09-30..2026-10-13"},
 "size": {"objects": 11, "bytes": 52330, "rows_all_parts": 143, "rows_newest_part_per_partition": 130, "rows_newest_partition": 13, "schema_variants": 1, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "group_id", "type": "string", "nullable": false, "description": "peer group (= home fund)", "example": "IDVZ"},
  {"name": "home_fund_id", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "IDVZ"},
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "IDVZ"},
  {"name": "ticker", "type": "string", "nullable": false, "description": "ticker", "example": "IDVZ"},
  {"name": "role", "type": "string", "nullable": false, "description": "home (Opal fund) or rival", "example": "home"},
  {"name": "source_policy", "type": "string", "nullable": false, "description": "bloomberg_primary / issuer_first", "example": "bloomberg_primary"},
  {"name": "effective_from", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-09-30"},
  {"name": "map_version", "type": "int64", "nullable": false, "description": "peer map version", "example": "2"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "2-6431e76360d7"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-13T13:00:14Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_peer_group_map/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"map\": \"data/etfs/scripts/rivalfunds/peer_gr..."},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "peer group",
  "rival funds list",
  "competitors of IDVZ"
 ],
 "common_queries": [
  "Who are PFOE's rivals?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_peer_group", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date optional>", "home_ticker": "<IDVZ|PFOE>"}, "returns": "rival list with role and source policy", "answers": ["Who are PFOE's rivals?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "only IDVZ and PFOE have peer groups; DIVZ and PFDE have none (Andrew's ask names all four)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/peer_group_map (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/buying_trend

```json
{
 "contract_id": "opal-data-etfs/gold/buying_trend",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/buying_trend/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "buying_trend",
 "grain": "one row per (page day, fund, period, axis, bucket): net estimated buying into/away from a security or sector",
 "partition": {"keys": ["date (page day)"], "claim": "measured"},
 "producer": {"name": "rivalfunds-publish-page-lambda (rule rivalfunds-publish-page-on-marker-created on state/build_trade_schedule/) -- the page manifest lists these as a1_produced", "schedule": "S3-marker event; sweep re-publish 09:00 ET", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-14", "trading_days_behind_T-1": "0 (page day 2026-10-14 = T; data to T-1)", "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "11 partitions 2026-09-30..2026-10-14"},
 "size": {"objects": 37, "bytes": 1872695, "rows_all_parts": 31059, "rows_newest_part_per_partition": 11684, "rows_newest_partition": 1522, "schema_variants": 3, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "IDVZ"},
  {"name": "role", "type": "string", "nullable": false, "description": "home (Opal fund) or rival", "example": "home"},
  {"name": "period", "type": "string", "nullable": false, "description": "window label (MTD, QTD, YTD, R30, R90, R365)", "example": "YTD"},
  {"name": "window_start", "type": "date32[day]", "nullable": false, "description": "first day of the window", "example": "2026-01-02"},
  {"name": "window_end", "type": "date32[day]", "nullable": false, "description": "last day of the window", "example": "2026-10-14"},
  {"name": "n_trading_days", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "197"},
  {"name": "axis", "type": "string", "nullable": false, "description": "security or sector", "example": "security"},
  {"name": "bucket", "type": "string", "nullable": false, "description": "security id or sector name the row measures", "example": "AZN_LN_Equity"},
  {"name": "security_name", "type": "string", "nullable": true, "description": "security long name", "example": "AstraZeneca PLC"},
  {"name": "net_notional_base", "type": "double", "nullable": false, "description": "net estimated notional over the window, USD (INFERRED)", "example": "5726202.23"},
  {"name": "n_windows", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "2"},
  {"name": "lean", "type": "string", "nullable": false, "description": "into / away", "example": "into"},
  {"name": "rank", "type": "int64", "nullable": true, "description": "name-evident; see producer source", "example": "1.0"},
  {"name": "reading", "type": "string", "nullable": false, "description": "bet / tilt", "example": "bet"},
  {"name": "trend_mark", "type": "string", "nullable": false, "description": "per-window +/- marks", "example": "0 0 0 0 0 + 0 0 + 0"},
  {"name": "n_refused_windows", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "gross_notional_base", "type": "double", "nullable": false, "description": "name-evident; see producer source", "example": "5726202.23"},
  {"name": "bet_share", "type": "double", "nullable": false, "description": "share of gross notional that is a bet", "example": "0.616036335831611"},
  {"name": "sector_source", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "own"},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "INFERRED"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261014T110511Z-14e3b1fc06c3"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-14T11:05:11Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_buying_trend/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"bet_share\": 0.5, \"g1\": [\"s3://opal-data-etf..."}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "rival buying trend",
  "what are competitors buying",
  "sector tilts of rivals"
 ],
 "common_queries": [
  "What sectors have IDVZ's rivals been buying YTD?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_compare_peers", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<page day>", "home_ticker": "<IDVZ|PFOE>", "period": "<MTD|QTD|YTD|R30|R90|R365>", "axis": "<security|sector>"}, "returns": "home vs rival buying trend + holding contribution, ranked (claim INFERRED)", "answers": ["What sectors have IDVZ's rivals been buying YTD?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "9 of 11 partitions carry re-run parts; newest part is the snapshot"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/buying_trend (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/holding_contribution

```json
{
 "contract_id": "opal-data-etfs/gold/holding_contribution",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/holding_contribution/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "holding_contribution",
 "grain": "one row per (page day, fund, period, axis, bucket): return contribution",
 "partition": {"keys": ["date (page day)"], "claim": "measured"},
 "producer": {"name": "rivalfunds-publish-page-lambda (rule rivalfunds-publish-page-on-marker-created on state/build_trade_schedule/) -- the page manifest lists these as a1_produced", "schedule": "S3-marker event; sweep re-publish 09:00 ET", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-14", "trading_days_behind_T-1": "0 (page day 2026-10-14; period_end 2026-10-13)", "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "11 partitions 2026-09-30..2026-10-14"},
 "size": {"objects": 37, "bytes": 3515336, "rows_all_parts": 171302, "rows_newest_part_per_partition": 55920, "rows_newest_partition": 6185, "schema_variants": 5, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "IDVZ"},
  {"name": "role", "type": "string", "nullable": false, "description": "home (Opal fund) or rival", "example": "home"},
  {"name": "period", "type": "string", "nullable": false, "description": "window label (MTD, QTD, YTD, R30, R90, R365)", "example": "MTD"},
  {"name": "period_start", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-01"},
  {"name": "period_end", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-13"},
  {"name": "period_nominal_start", "type": "date32[day]", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-01"},
  {"name": "period_clipped", "type": "bool", "nullable": false, "description": "period clipped to available history", "example": "False"},
  {"name": "axis", "type": "string", "nullable": false, "description": "security or sector", "example": "security"},
  {"name": "bucket", "type": "string", "nullable": false, "description": "security id or sector name the row measures", "example": "IBDRY_US_Equity"},
  {"name": "security_name", "type": "string", "nullable": true, "description": "security long name", "example": "Iberdrola SA"},
  {"name": "contribution", "type": "double", "nullable": true, "description": "return contribution of the bucket over the period (INFERRED)", "example": "0.0005611185054473413"},
  {"name": "price_coverage", "type": "string", "nullable": false, "description": "full / partial / missing", "example": "partial"},
  {"name": "n_days_priced", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "8"},
  {"name": "n_days_period", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "9"},
  {"name": "n_days_holding_implied", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "2"},
  {"name": "price_source", "type": "string", "nullable": false, "description": "g4_tri / holding_implied / mixed / missing", "example": "mixed"},
  {"name": "rank_best", "type": "int64", "nullable": true, "description": "name-evident; see producer source", "example": "14.0"},
  {"name": "rank_worst", "type": "int64", "nullable": true, "description": "name-evident; see producer source", "example": "30.0"},
  {"name": "n_ranked", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "43"},
  {"name": "n_missing", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "n_days_refused", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "refused_reasons", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "{\"corporate_action_suspected\": 1}"},
  {"name": "refused_days", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "[[\"2026-02-02\", 2.020737, \"corporate_action_s..."},
  {"name": "missing_reason", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "no_price"},
  {"name": "sector_source", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "own"},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "INFERRED"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261014T110415Z-f4b35d38ba4e"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-14T11:04:15Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_holding_contribution/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"g1\": [\"s3://opal-data-etfs/rivalfunds/etfs/..."}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "return contribution",
  "what drove rival performance"
 ],
 "common_queries": [
  "Which holdings drove PFOE's rivals' MTD return?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_compare_peers", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<page day>", "home_ticker": "<IDVZ|PFOE>", "period": "<period>", "axis": "<security|sector>"}, "returns": "as above", "answers": ["Which holdings drove PFOE's rivals' MTD return?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/holding_contribution (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/input_census

```json
{
 "contract_id": "opal-data-etfs/gold/input_census",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/input_census/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "input_census",
 "grain": "one row per (as_of, input kind, subject): did each page input arrive, fall back, go stale or go missing",
 "partition": {"keys": ["date (page day)"], "claim": "measured"},
 "producer": {"name": "rivalfunds-publish-page-lambda (rule rivalfunds-publish-page-on-marker-created on state/build_trade_schedule/) -- the page manifest lists these as a1_produced", "schedule": "S3-marker event; sweep re-publish 09:00 ET", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-14", "trading_days_behind_T-1": "0 (page day 2026-10-14; as_of 2026-10-13)", "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "11 partitions 2026-09-30..2026-10-14"},
 "size": {"objects": 37, "bytes": 550153, "rows_all_parts": 57926, "rows_newest_part_per_partition": 17296, "rows_newest_partition": 1592, "schema_variants": 2, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "date", "type": "date32[day]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13"},
  {"name": "input_kind", "type": "string", "nullable": false, "description": "holdings / price / gics / market_reading", "example": "holdings"},
  {"name": "subject", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "IDVZ"},
  {"name": "fund_id", "type": "string", "nullable": true, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "IDVZ"},
  {"name": "role", "type": "string", "nullable": true, "description": "home (Opal fund) or rival", "example": "home"},
  {"name": "status", "type": "string", "nullable": false, "description": "row status", "example": "covered_by_fallback"},
  {"name": "as_of", "type": "string", "nullable": true, "description": "as-of date", "example": "2026-10-12"},
  {"name": "location", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "s3://opal-data-etfs/rivalfunds/etfs/gold/cano..."},
  {"name": "reason", "type": "string", "nullable": true, "description": "reason text", "example": "no G1 report dated 2026-10-13 for IDVZ; its n..."},
  {"name": "fallback", "type": "string", "nullable": true, "description": "prior_report_within_allowance / holding_implied / g4_prior", "example": "prior_report_within_allowance"},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261014T110548Z-044db022daf8"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-14T11:05:48Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_input_census/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"as_of\": \"2026-10-13\", \"page_day\": \"2026-10-..."}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "page inputs",
  "data freshness of rival page"
 ],
 "common_queries": [
  "Which inputs were missing for today's rival page?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_coverage", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<optional>"}, "returns": "as holdings_coverage", "answers": ["Which inputs were missing for today's rival page?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/input_census (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/research_hypotheses

```json
{
 "contract_id": "opal-data-etfs/gold/research_hypotheses",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/research_hypotheses/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "research_hypotheses",
 "grain": "one row per (fund, item): AI-written activity and direction readings with cited rows and an invalidation clause",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "etfs-rivalfunds-daily-lambda sweep (writes at ~13:00-13:08Z)", "schedule": "Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "10 partitions 2026-09-30..2026-10-13"},
 "size": {"objects": 11, "bytes": 849964, "rows_all_parts": 276, "rows_newest_part_per_partition": 252, "rows_newest_partition": 26, "schema_variants": 1, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "fund_id", "type": "string", "nullable": false, "description": "fund key (ticker, or issuer fund number for issuer-site funds)", "example": "IDVZ"},
  {"name": "run_id", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "20261013T130018Z-ai"},
  {"name": "item_id", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "1"},
  {"name": "kind", "type": "string", "nullable": false, "description": "activity_30d / direction_verdict", "example": "activity_30d"},
  {"name": "text", "type": "string", "nullable": false, "description": "the reading", "example": "From 2026-09-12 to 2026-10-12, the unusual fe..."},
  {"name": "observed", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "[\"In the last 30 days, Petroleo Brasileiro SA..."},
  {"name": "inferred", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "[\"The thirty-day pattern looks unusual becaus..."},
  {"name": "cited_rows", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "[{\"table\": \"holding_contribution\", \"key\": \"ID..."},
  {"name": "invalidation", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "This reading would be wrong if position-level..."},
  {"name": "input_vintages", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "{\"fear_greed/fear_greed_index\": \"2026-10-12T2..."},
  {"name": "web_reads", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "[]"},
  {"name": "grounding", "type": "string", "nullable": false, "description": "PASS / FAIL grounding check", "example": "PASS"},
  {"name": "grounding_reason", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": null},
  {"name": "model_version", "type": "string", "nullable": false, "description": "LLM used", "example": "gpt-5.4"},
  {"name": "prompt_version", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "a1-chain/8"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"attached_figures\": 0, \"corrections\": 0, \"da..."},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-13T13:00:57Z"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "AI research notes rival funds",
  "unusual activity"
 ],
 "common_queries": [
  "What unusual activity did the model flag for TXUE?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_research_notes", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "fund_ticker": "<ticker>"}, "returns": "text + observed/inferred lists + cited rows; every row labelled AI-generated (model_version)", "answers": ["What unusual activity did the model flag for TXUE?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "AI-generated text (model_version gpt-5.4 on 2026-10-13); a tool must carry the claim and model on every answer"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/research_hypotheses (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/security_market

```json
{
 "contract_id": "opal-data-etfs/gold/security_market",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/security_market/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "security_market",
 "grain": "one row per (date, security): close, total return index, GICS (Bloomberg reference)",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "pull-enrichment stage on the terminal machine (data/etfs/scripts/rivalfunds/enrichment_bloomberg.py; producer_version enrichment_bloomberg/1, source blp_client.reference_data)", "schedule": "terminal daily ~07:07 ET", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "10 partitions 2026-09-29..2026-10-13"},
 "size": {"objects": 13, "bytes": 492068, "rows_all_parts": 6517, "rows_newest_part_per_partition": 5143, "rows_newest_partition": 585, "schema_variants": 3, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "security_id", "type": "string", "nullable": false, "description": "security key in crosswalk grammar (e.g. ABNB_US_Equity)", "example": "007903107"},
  {"name": "security_bloomberg", "type": "string", "nullable": false, "description": "Bloomberg security string", "example": "/cusip/007903107"},
  {"name": "date", "type": "date32[day]", "nullable": false, "description": "partition / report date of the row", "example": "2026-10-13"},
  {"name": "px_close", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "605.53"},
  {"name": "total_return_index", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "1.899906"},
  {"name": "currency", "type": "string", "nullable": false, "description": "currency", "example": "USD"},
  {"name": "gics_sector", "type": "string", "nullable": true, "description": "GICS sector", "example": "Information Technology"},
  {"name": "gics_industry_group", "type": "string", "nullable": true, "description": "GICS industry group", "example": "Semiconductors & Semiconductor"},
  {"name": "gics_industry_group_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "4530"},
  {"name": "gics_industry", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Semiconductors & Semiconductor"},
  {"name": "gics_industry_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "453010"},
  {"name": "gics_sub_industry", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Semiconductors"},
  {"name": "gics_sub_industry_code", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "45301020"},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "blp_client.reference_data"},
  {"name": "as_of", "type": "date32[day]", "nullable": false, "description": "as-of date", "example": "2026-10-14"},
  {"name": "as_of_source", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "pull"},
  {"name": "security_name", "type": "string", "nullable": false, "description": "security long name", "example": "Advanced Micro Devices Inc"},
  {"name": "security_parsekey", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "AMD US Equity"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261014T110757Z-2319923827b5"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-14T11:07:57Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "enrichment_bloomberg/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"as_of_source_counts\": {\"historical\": 0, \"pu..."},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "security price",
  "GICS classification",
  "total return index"
 ],
 "common_queries": [
  "What GICS industry is AMD in, and its close on 2026-10-13?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_security_reference", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "security": "<id>"}, "returns": "price, TRI, GICS levels, name, corporate actions", "answers": ["What GICS industry is AMD in, and its close on 2026-10-13?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "2026-09-30 partition missing (1 trading day)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/security_market (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/corporate_actions

```json
{
 "contract_id": "opal-data-etfs/gold/corporate_actions",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/corporate_actions/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "corporate_actions",
 "grain": "one row per (as_of, security, event): dividends and splits from DVD_HIST_ALL, plus a status row per security",
 "partition": {"keys": ["date (as_of)"], "claim": "measured"},
 "producer": {"name": "pull-enrichment stage on the terminal machine (data/etfs/scripts/rivalfunds/enrichment_bloomberg.py; producer_version enrichment_bloomberg/1, source blp_client.reference_data)", "schedule": "terminal daily ~07:07 ET", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "10 partitions 2026-09-30..2026-10-13"},
 "size": {"objects": 11, "bytes": 345812, "rows_all_parts": 9745, "rows_newest_part_per_partition": 8358, "rows_newest_partition": 161, "schema_variants": 1, "claim": "measured", "note": "row count of the table = rows_newest_part_per_partition (each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts)"},
 "columns": [
  {"name": "security_id", "type": "string", "nullable": false, "description": "security key in crosswalk grammar (e.g. ABNB_US_Equity)", "example": "ABNB US Equity"},
  {"name": "security_bloomberg", "type": "string", "nullable": false, "description": "Bloomberg security string", "example": "ABNB US Equity"},
  {"name": "record_seq", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "0"},
  {"name": "row_kind", "type": "string", "nullable": false, "description": "event / status", "example": "status"},
  {"name": "status", "type": "string", "nullable": false, "description": "OK / NOT_APPLICABLE_TO_REF_DATA", "example": "NOT_APPLICABLE_TO_REF_DATA"},
  {"name": "status_detail", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "{\"category\": \"BAD_FLD\", \"code\": 9, \"message\":..."},
  {"name": "event_type", "type": "string", "nullable": true, "description": "cash_div / split", "example": "split"},
  {"name": "raw_event_type", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Stock Split"},
  {"name": "ratio", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "4.0"},
  {"name": "amount", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "1.35"},
  {"name": "raw_amount", "type": "double", "nullable": true, "description": "name-evident; see producer source", "example": "4.0"},
  {"name": "currency", "type": "string", "nullable": true, "description": "currency", "example": "USD"},
  {"name": "declared_date", "type": "date32[day]", "nullable": true, "description": "name-evident; see producer source", "example": "2024-11-07"},
  {"name": "ex_date", "type": "date32[day]", "nullable": true, "description": "name-evident; see producer source", "example": "2024-12-04"},
  {"name": "record_date", "type": "date32[day]", "nullable": true, "description": "name-evident; see producer source", "example": "2026-09-16"},
  {"name": "pay_date", "type": "date32[day]", "nullable": true, "description": "name-evident; see producer source", "example": "2026-09-30"},
  {"name": "frequency", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "None"},
  {"name": "date_anomalies", "type": "string", "nullable": true, "description": "name-evident; see producer source", "example": "Record Date='Record Date ='; Payable Date='Pa..."},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "DVD_HIST_ALL"},
  {"name": "as_of", "type": "date32[day]", "nullable": false, "description": "as-of date", "example": "2026-10-13"},
  {"name": "source_class", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "daily"},
  {"name": "capture_origin", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "blp_client.reference_data@2026-10-14T11:07:57Z"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261013-c833c167b849"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-14T11:07:57Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "enrichment_bloomberg/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"batches\": 1, \"field\": \"DVD_HIST_ALL\", \"kind..."},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "dividends",
  "stock splits",
  "corporate actions"
 ],
 "common_queries": [
  "What dividends did ABNB pay in the last year?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_security_reference", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "security": "<id>"}, "returns": "as above", "answers": ["What dividends did ABNB pay in the last year?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/corporate_actions (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "each partition may hold several parts (re-runs); the NEWEST part (max revision / dataset_revision) is the complete snapshot for that date and SUPERSEDES earlier parts -- never sum across parts (verified on canonical_shape 2026-10-13: newest part 500 rows, 0 duplicate (snapshot_id, position_id), all 11 delivered funds present; earlier part 69 rows all repeated)"
 ]
}
```

### opal-data-etfs/gold/security_universe

```json
{
 "contract_id": "opal-data-etfs/gold/security_universe",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/security_universe/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "security_universe",
 "grain": "one row per security ever seen in a tracked fund: identifiers, first/last seen, funds",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "etfs-rivalfunds-daily-lambda sweep (writes at ~13:00-13:08Z)", "schedule": "Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-12", "trading_days_behind_T-1": 1, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "7 partitions 2026-10-02..2026-10-12"},
 "size": {"objects": 7, "bytes": 407421, "rows_all_parts": 7327, "rows_newest_part_per_partition": 7327, "rows_newest_partition": 1053, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "security_key", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "000270 KS Equity"},
  {"name": "security_id", "type": "string", "nullable": true, "description": "security key in crosswalk grammar (e.g. ABNB_US_Equity)", "example": "000270_KS_Equity"},
  {"name": "security_bloomberg", "type": "string", "nullable": true, "description": "Bloomberg security string", "example": "000270 KS Equity"},
  {"name": "security_cusip", "type": "string", "nullable": true, "description": "CUSIP", "example": "00206R102"},
  {"name": "security_isin", "type": "string", "nullable": true, "description": "ISIN", "example": "US00206R1023"},
  {"name": "security_ticker", "type": "string", "nullable": false, "description": "security ticker", "example": "000270"},
  {"name": "security_name", "type": "string", "nullable": true, "description": "security long name", "example": "Midea Group Co Ltd"},
  {"name": "first_seen", "type": "date32[day]", "nullable": false, "description": "first report date", "example": "2025-07-09"},
  {"name": "last_seen", "type": "date32[day]", "nullable": false, "description": "last report date", "example": "2026-01-26"},
  {"name": "funds", "type": "string", "nullable": false, "description": "space/comma list of fund ids", "example": "BIDD"},
  {"name": "n_report_dates", "type": "int64", "nullable": false, "description": "name-evident; see producer source", "example": "136"},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261013T130825Z-fbae6cd1cf90"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-13T13:08:25Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_security_universe/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"as_of\": \"2026-10-12\", \"floor\": null, \"mode\"..."}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "security master rival funds"
 ],
 "common_queries": [
  "Which funds have ever held 000270 KS?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_who_holds", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>", "security": "<id>"}, "returns": "first/last seen and funds list", "answers": ["Which funds have ever held 000270 KS?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/security_universe (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "one part per partition"
 ]
}
```

### opal-data-etfs/gold/security_names

```json
{
 "contract_id": "opal-data-etfs/gold/security_names",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/gold/security_names/date={D}/<part>.parquet",
 "layer": "gold",
 "format": "parquet",
 "table": "security_names",
 "grain": "one row per security id: long company name (LONG_COMP_NAME)",
 "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "etfs-rivalfunds-daily-lambda sweep (writes at ~13:00-13:08Z)", "schedule": "Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-08", "trading_days_behind_T-1": 3, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "2 partitions 2026-10-06..2026-10-08"},
 "size": {"objects": 2, "bytes": 17563, "rows_all_parts": 300, "rows_newest_part_per_partition": 300, "rows_newest_partition": 172, "schema_variants": 1, "claim": "measured"},
 "columns": [
  {"name": "security_id", "type": "string", "nullable": false, "description": "security key in crosswalk grammar (e.g. ABNB_US_Equity)", "example": "000270_KS_Equity"},
  {"name": "security_name", "type": "string", "nullable": false, "description": "security long name", "example": "Kia Corp"},
  {"name": "named_on", "type": "string", "nullable": false, "description": "name-evident; see producer source", "example": "2026-10-06"},
  {"name": "source", "type": "string", "nullable": false, "description": "vendor/source of the row", "example": "LONG_COMP_NAME"},
  {"name": "claim", "type": "string", "nullable": false, "description": "row claim: MEASURED or INFERRED (the producer's own field)", "example": "MEASURED"},
  {"name": "revision", "type": "string", "nullable": false, "description": "producer revision id of this part", "example": "20261008T122122Z-7f3a1a91711d"},
  {"name": "produced_at", "type": "string", "nullable": false, "description": "UTC time the producer wrote the row", "example": "2026-10-08T12:21:22Z"},
  {"name": "producer_version", "type": "string", "nullable": false, "description": "producer module/version", "example": "gold_security_names/1"},
  {"name": "input_manifest", "type": "string", "nullable": false, "description": "JSON of the inputs read (uris, shas)", "example": "{\"buying_trend\": \"s3://opal-data-etfs/rivalfu..."}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "security names"
 ],
 "common_queries": [
  "What is the name of 000270_KS_Equity?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae",
 "open_items": [
  "2 partitions only (2026-10-06, 2026-10-08); 3 trading days behind"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "pyarrow footer read of every parquet object (10,491 of 10,491, 0 errors)", "at": "2026-10-14T13:08:07Z"},
  {"read": "get_object newest part of rivalfunds/etfs/gold/security_names (pandas, full columns)", "at": "2026-10-14T13:1xZ"}
 ],
 "served_day_rules": [
  "one part per partition"
 ]
}
```

### opal-data-etfs/platinum/rivalfunds_page

```json
{
 "contract_id": "opal-data-etfs/platinum/rivalfunds_page",
 "bucket": "opal-data-etfs",
 "s3_prefix": "rivalfunds/etfs/platinum/page/date={D}/{index.html,manifest.json,audit}",
 "layer": "platinum",
 "format": "html+json",
 "table": "rivalfunds_page",
 "grain": "one published page per page day: index.html (~1.5 MB) + manifest.json (inputs, checks, per-fund charts) + audit",
 "partition": {"keys": ["date (page day)"], "claim": "measured"},
 "producer": {"name": "rivalfunds-publish-page-lambda (rule rivalfunds-publish-page-on-marker-created) + sweep re-publish", "schedule": "Scheduler etfs-rivalfunds-daily cron(0 7 ? * MON-FRI *) America/New_York -> etfs-rivalfunds-fetch-holdings-lambda; then S3-marker EventBridge rules (rivalfunds-build-silver-*, rivalfunds-build-canonical-shape-*, rivalfunds-publish-page-on-marker-created); Scheduler etfs-rivalfunds-sweep-daily cron(0 9 ? * MON-FRI *) America/New_York -> etfs-rivalfunds-daily-lambda re-runs any stage missing its marker", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-14 (page day; manifest generated_at 2026-10-14T13:11:53Z)", "basis": "page day = T; data as_of T-1 2026-10-13", "claim": "measured"},
 "size": {"objects": 334, "bytes": 203541787, "partitions": 12, "claim": "measured"},
 "columns": [
  {"name": "manifest.funds", "type": "dict[13] '<group>/<fund>' -> {13}", "nullable": false, "description": "per-fund section metadata", "example": "IDVZ/BIDD"},
  {"name": "manifest.checks", "type": "list[6] {check, status, reason}", "nullable": false, "description": "publish checks (e.g. report_date_freshness PASS)", "example": "report_date_freshness"},
  {"name": "manifest.inputs", "type": "list[123] {kind, uri, sha256, revision}", "nullable": false, "description": "every gold input read", "example": "peer_group_map"},
  {"name": "manifest.a1_produced / ai_grounding / charts / funds_total / generated_at", "type": "mixed", "nullable": false, "description": "AI-stage outputs, grounding counts, chart specs", "example": "funds_total 13"},
  {"name": "index.html", "type": "html", "nullable": false, "description": "the rendered rival-funds page", "example": "1,470,288 B"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "rival funds page",
  "competitor ETF page"
 ],
 "common_queries": [
  "Show me today's rival-funds page."
 ],
 "existing_gateway_tool": {"name": "gateway HTML routes /rivalfunds, /rivalfunds/{day}, /rivalfunds/archive (app/rivalfunds_view.py; not an MCP tool, not in tool_index)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@a0db38c8ae; org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-RIV-w-1.gateway-routes-and-read-grant.md",
 "open_items": [
  "the gateway's only live grant into this bucket is gateway-rivalfunds-read-policy (page prefix only; simulate: page GetObject allowed, gold/canonical_shape implicitDeny)"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"},
  {"read": "get_object manifest.json date=2026-10-14 (shape)", "at": "2026-10-14T13:1xZ"},
  {"read": "iam get_role_policy opal-gateway-role gateway-rivalfunds-read-policy + simulate_principal_policy x8", "at": "2026-10-14T13:3xZ"}
 ]
}
```

### opal-data-etfs/gold/mdpf_new_securities

```json
{
 "contract_id": "opal-data-etfs/gold/mdpf_new_securities",
 "bucket": "opal-data-etfs",
 "s3_prefix": "mdpf/etfs/gold/new_securities/date={D}/new_securities.json",
 "layer": "gold",
 "format": "json",
 "table": "mdpf_new_securities",
 "grain": "one object per run date: stocks newly appearing in Opal fund silver or rival canonical_shape vs the previous day, for MDPF security classification",
 "partition": {"keys": ["date (run date)"], "claim": "measured"},
 "producer": {"name": "mdpf-secclass-new-security-lambda (infra/aws/lambda/mdpf-secclass/new-security-classifier; env SILVER_PREFIX silver/holdings/, CANONICAL_PREFIX rivalfunds/etfs/gold/canonical_shape/)", "schedule": "Scheduler mdpf-secclass-new-security-daily cron(0 10 ? * MON-FRI *) America/New_York, input {write: true}", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "trading_days_behind_T-1": 0, "t1_frontier": "2026-10-13", "basis": "trading-day-frontier", "claim": "measured", "note": "6 partitions 2026-10-06..2026-10-13"},
 "size": {"objects": 6, "bytes": 28080, "claim": "measured"},
 "columns": [
  {"name": "canonical_shape {day, previous, funds[10], stocks}", "type": "dict", "nullable": false, "description": "rival side read", "example": "stocks 33"},
  {"name": "opal_silver {day, previous, funds_read, opal_funds, stocks, ignored_rows}", "type": "dict", "nullable": false, "description": "Opal fund side read", "example": "stocks 106"},
  {"name": "counts {new_stocks, planned_writes, present, unresolved, written}", "type": "dict", "nullable": false, "description": "run counts", "example": "new_stocks 0"},
  {"name": "items[]", "type": "list", "nullable": false, "description": "the new securities", "example": "[] on 2026-10-13"},
  {"name": "output / run_date / sources / write", "type": "mixed", "nullable": false, "description": "run metadata", "example": "2026-10-13"}
 ],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal-side fund data, no client firm dimension", "values": []}, "account": {"column": "none", "last4_derivation": "not applicable (no account grain)", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": [
  "new securities in ETFs",
  "security classification queue"
 ],
 "common_queries": [
  "Which new stocks entered the ETFs yesterday?"
 ],
 "existing_gateway_tool": {"name": "", "verdict": "none"},
 "proposed_tools": [
  {"name": "etfs_get_new_securities", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "<date>"}, "returns": "the day's new securities with source fund", "answers": ["Which new stocks entered the ETFs yesterday?"]}
 ],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "none",
 "open_items": [
  "'mdpf/' prefix inside the ETF bucket is an MDPF consumer's output; ownership is MDPF_SECCLASS, not ETFS"
 ],
 "evidence": [
  {"read": "boto3 list_objects_v2 paginator s3://opal-data-etfs (17 pages, 16,098 keys)", "at": "2026-10-14T12:56:54Z"}
 ]
}
```


## (e) What could not be read, and why

- **The terminal-side producers (`bbg/`, Bloomberg rival captures, `security_market`, `corporate_actions`) are inferred.** They run
  on the site-Z Bloomberg terminal, not in Lambda, so no `get-function-configuration` or rule exists to read. The attribution rests on
  write times (~11:05-11:10Z), `run_manifest.json` `run_class=scheduled`, `producer_version`/`source` fields and the
  `collector_bloomberg.py` docstring. `schtasks /query` was not run (it needs the terminal box).
- **Stage-to-table mapping inside the rivalfunds chain is inferred** for coverage, flow_reconciliation, trade_schedule,
  buying_trend, holding_contribution, input_census, peer_group_map, research_hypotheses, security_universe and security_names. Only 5
  marker rules and 2 schedules exist; the rest is co-timing of state markers and parts plus the page manifest's `a1_produced`. Function
  code was not downloaded.
- **Live IAM was simulated for 4 resources on 2 roles only.** The other 6 gateway roles were checked only by a literal-name scan of
  their inline policies, so a wildcard grant on them was not evaluated.
- **The 2026-09 coverage disagreement has no measured cause** (CSV coverage line vs `coverage_verdict.json`). Every September
  trading-day file exists, and its `source_as_of` equals its date. The CSV's "carried" basis is therefore something else, and it was not traced
  in `render_month_end.py`.
- **`gold/holding` date=2026-10-13 was not re-listed** (only `gold/book` was, after the 13:00Z fire). It is taken as landed
  with the book (inferred, same manifest).
- **`bbg-testpull/` (357), bronze (3,586), `rivalfunds/etfs/state/` (402) and `gold/_manifests/` (63)** are counted in the census
  but their objects were not opened (out of the silver/gold/platinum scope).
- **No client data is present** in any contracted table. The ownership plane is firm-level aggregates (value + account count, no
  account ids), so last-4 forking does not apply. The firm dimension is declared on each ownership contract.
- **Surprise rows NOT filed.** The brief bars writes outside this part file. Two findings are owed to a surprise channel by the
  reviewing seat:
  1. ARMED: the `etfs-canon-fanin` DynamoDB target is absent, so the scheduled job fails daily.
  2. INERT: the 2026-09 report coverage-line disagreement.
