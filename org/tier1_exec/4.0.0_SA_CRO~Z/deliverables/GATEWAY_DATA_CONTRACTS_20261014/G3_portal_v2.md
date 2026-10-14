# G3 -- opal-data-portal-v2: what the portal actually serves (census part G3 for 4.0.0_SA_CRO~Z)

- **Author:** census subagent G3 of 4.0.0_SA_CRO~Z, 2026-10-14 12:4xZ-13:4xZ.
- **Binds:** `parts/_SUBAGENT_BRIEF.md`; directive `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` sections 2 (G3 row), 3, 4.
- **Bounds kept:** every read was a read (S3 list/head/get, CloudFront/API Gateway/Lambda/DynamoDB describe, DynamoDB COUNT scan and a 31+33-item attribute-name census). No write, no invoke, no vendor call. Nothing committed.
- **Trading frontier:** `lib/trading_calendar.py` (NYSE hardcoded fallback 2010-2027): `prev_trading_day('2026-10-14')` = **2026-10-13** (T-1). Every lag below is in trading days (TD) behind T-1.
- **Portal source read:** portal `origin/PROD` @6a5926fc11 (fetched 2026-10-14 ~13:00Z; local checkout was DEV @ce3b0cc4, 256 commits behind origin/DEV @97c66c9364). PROD is what users are served.

## 0. Answer in eight lines

1. The bucket holds **4,851 objects, 7,424,623,517 bytes** (5 pages, 4,851 of 4,851 keys), grouped into **84 dataset groups** (0 unmatched).
2. **55 of the 84 groups (1,984 objects, 1,124,869,586 bytes)** sit under the three URL-reachable trees (`json/`, `json-tiered/`, `platinum/`); the other 29 groups (2,867 objects, 6,299,753,931 bytes) are pipeline inputs, ops reports, a dead static-site build and frozen top-level legacy twins.
3. **Certified-page diff (33 key rows covering the 42 certified entities of 10 pages, section 2.2):** 22 UNCHANGED-LIVE, 8 UNCHANGED-FROZEN (as certified), **1 CONSUMER-GONE** (`json/portfolios/aum-metrics.json`, entities att.03/ft.04/pos.03: no PROD page reads it any more), **1 GONE** (`json/mdpf/**`, 0 keys today), **1 MOVED** (`platinum/mdpf/aggregate_aua/` daily snapshots now only under `archive/`); 0 new members inside certified families.
4. **New since certification, read by pages, uncertified and mostly uncatalogued:** `json/positioning/opal_aggregate.json`, `platinum/mdpf/{scope}/category-views.json` (x4), `json/market/market-regime*.json`, `json-tiered/market-overview/{rsi-*,timeseries/*}`, `json/trending/latest.json`, `json/sentiment/{fear-greed-index,keyword-sentiments}.json`, `platinum/advi/49financial/perfrp_*` (x3).
5. **The 3 uncertified pages barely touch this bucket:** advisor-intelligence reads `opal-data-bd`/`-inf`/`-cot` (G2) plus 3 perfrp leaves here; ticket-center reads DynamoDB `opal-tickets` (31 items); trade-submission reads DynamoDB `opal-trade-submissions` (33 items) + S3 `opal-data-trade-submissions` (27 objects). None of the 3 reads `json/`.
6. **Pages request 8 keys that do not exist** (404 class): `json/portfolios/non_model_assets.json`, `json/sentiment/aaii-latest.json`, `json/metadata/yang.json`, `json/trending/topics/{date}`, `json/market/ticker/{t}`, and 3 perfrp leaf families.
7. **Firm-partitioned keys:** `platinum/mdpf/{global|49financial|cottonwood|inflection}/` (segment 3), `platinum/advi/{49financial}/` (segment 3), legacy `json/portfolios/{49financial|inflection}/`. Every other served dataset is opal-internal (book/market level, no firm).
8. **Gateway:** 5 purpose-built `portal_index` tools + `gateway_query_catalog` reach 26 catalogued rows; verdicts KEEP for all 5, EXTEND the catalog for 9 uncatalogued live datasets, RE-RULE 1 row (`ft.04` aum-metrics) to deny, RETIRE `portal_lookup.py` channel `mdpf` (target tree gone). 9 purpose-built tools proposed (section 3.4).

## 1. Method (each read, its instrument, its denominator)

| read | instrument | denominator |
|---|---|---|
| every key | boto3 `list_objects_v2` paginator, 2026-10-14T12:55:42Z | 5 pages, 4,851 of 4,851 keys; grouped into 84 groups, 0 unmatched |
| certified rectangles | `rectangle.final.certified.json` ONLY, regex for `s3://` + relative keys, per-entity cells | 10 of 13 page runs carry one (see 2.1); 42 entities |
| served objects (exists, size, LastModified, vintage fields, top-level shape) | `head_object` + whole `get_object` (gzip-decoded) for objects <= 6 MB | 81 keys probed: 74 exist, 7 absent; 1 skipped (>6 MB, shape read separately) |
| nested shape (names + counts only, no values) | `get_object`, 2-level key walk | 34 objects |
| client-data identifiers (count only) | perfrp leaves: key shape classes, last-4 groups and collisions; no value printed | 3 objects, 10,165 entries |
| page -> key map | `git grep` + a Python walk over portal `origin/PROD` `src/api`, `src/hooks`, `src/contexts`: path literal -> enclosing exported accessor -> files that reference it | 64 `/api/general/*` path literals (excl. `trades/*`), 61 accessors |
| routing (URL -> bucket key) | live CloudFront `list_distributions` (2 scanned, 1 with a portal-v2 origin: EVTSA9VEHNZVH) + repo `infra/aws/lambda-edge/public-data-router/index.mjs` | 5 behaviors touch portal-v2 or `/api/general` |
| API backends for the 3 uncertified pages | `apigatewayv2 get-routes/get-integrations` on 7k3ed8px20; Lambda `get_function_configuration` | 121 routes, 21 integrations, 5 functions read |
| producers | Lambda `list_functions` env scan for the bucket name; bucket notification config; object `_provenance` fields | 237 functions scanned, 14 env hits; 2 S3 notifications |
| DynamoDB (ticket, trade) | `describe_table`, `scan Select=COUNT`, full-scan attribute-NAME census (values not copied) | opal-tickets 31 of 31; opal-trade-submissions 33 of 33 |
| catalog | `DATA_CATALOG.yaml` parsed (yaml.safe_load) | 16 channels, 37 artifact rows, 5 portal_datasets, 67 tool_index rows |
| trading lag | `lib/trading_calendar.trading_days_behind(d, '2026-10-13')` | 21 dates |

Scratch (not committed): `C:\Users\OPALBL~1\AppData\Local\Temp\claude\census_G3\` (bucket.jsonl, probe.json, shape.json, accessors.json, scripts).

**Routing law (measured live + repo):** CloudFront EVTSA9VEHNZVH behavior `/api/general/*` -> origin opal-data-portal-v2 with Lambda@Edge `auth-validator-edge:23` + `public-data-router:7`; the router rewrites `/api/general/json-tiered/* -> json-tiered/*`, `/api/general/json/* -> json/*`, `/api/general/mdpf/* -> platinum/mdpf/*`, `/api/general/etfs/* -> platinum/etfs/*`, `/api/general/* -> json/*`. `/api/general/trades/*` goes to API Gateway. **Consequence: every key under `json/`, `json-tiered/`, `platinum/mdpf/`, `platinum/etfs/` is URL-reachable by any authenticated user, whether or not a page reads it.** `platinum/advi/{firm}/` is reached only through `/api/scoped/advisor-intelligence/*` (`shared-advisor-router:28`, firm-asserting; inferred from `portal/src/api/endpoints/adviKeyRepoint.ts:19-43`, not exercised).

## 2. Census

### 2.1 Which page runs are certified (confirmed)

| page | run | `rectangle.final.certified.json` | entities |
|---|---|---|---|
| attribution | 20260811T1834Z | present | 4 |
| cma | 20260811T1801Z (the 1729Z run has none) | present | 2 |
| correlations | 20260811T1918Z | present | 1 |
| factor-tilts | 20260811T1855Z | present | 4 |
| macro | 20260811T1940Z | present | 4 |
| market | 20260811T2020Z | present | 2 |
| portfolios | 20260811T1640Z | present | 16 |
| positioning | 20260811T1818Z | present | 3 |
| security-scanner | 20260812T0158Z | present (24 Plane-B/C cells UNMEASURED per catalog `absent_semantics_units`) | 4 |
| valuations | 20260811T1902Z | present | 2 |
| advisor-intelligence | 20260812T0411Z | **absent** (rectangle.c0..c18 only) | -- |
| ticket-center | 20260812T0637Z | **absent** (final.json + verify.json; not read, per PRD 9.8.1 A) | -- |
| trade-submission | 20260812T1805Z | **absent** (no rectangle at all; enumerations + HANDOFF only) | -- |

Confirmed: 10 certified, 3 not, exactly as the directive states.

### 2.2 (a) Certified-page served keys vs the live bucket today

States: UNCHANGED-LIVE (exists, advancing); UNCHANGED-FROZEN (exists, not advancing, as certified); CONSUMER-GONE (exists, but no PROD page reads it any more); GONE (0 keys); MOVED. Aug value = the certified rectangle's vintage cell; today = probe 2026-10-14 ~13:0xZ-13:2xZ.

| page(s) | entity | key | Aug as-of | today: exists / size / LastModified / as-of | lag TD | state |
|---|---|---|---|---|---|---|
| attribution, positioning | att.04 / pos.01 | `json/positioning/positioning_data.json` (gzip) | 2026-08-10 | yes / 6,883 / 2026-10-14T11:06:02Z / data_as_of 2026-10-13 | 0 | UNCHANGED-LIVE |
| attribution | att.01 | `json/positioning/allocation_summary.json` (gzip) | 2026-08-10 | yes / 962 / 2026-10-14T11:06:06Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| attribution, positioning | att.02 / pos.02 | `json/positioning/holdings_attribution_data.json` | 2026-07-31 | yes / 403,939 / 2026-10-06T20:24:47Z / 2026-09-30 | 9 (month-end cadence: healthy) | UNCHANGED-LIVE |
| attribution, factor-tilts, positioning | att.03 / ft.04 / pos.03 | `json/portfolios/aum-metrics.json` | period 2026-07-22 | yes / 7,234 / 2026-07-23T20:57:17Z / period 2026-07-22 | 58 | **CONSUMER-GONE + FROZEN.** `getAUMSummary`/`getAUMMetrics` are referenced only inside `src/api` (0 page/component files) at PROD. The OWNED-UNKNOWN is answered by the source comment `ModelPortfolios.tsx:571-574` ("frozen 2026-07-23, writer flag-disabled, the F1 finding @b48634789a") -- inferred, not re-measured at the writer |
| cma | cma.01 | `json/capital-markets/assumptions.json` | '2026' (year) | yes / 4,146 / 2026-03-11T00:45:53Z / '2026' | n/a (annual edition) | UNCHANGED-FROZEN (by design) |
| cma | cma.02 | `json/capital-markets/views.json` | 2026-01-09 | yes / 5,992 / 2026-01-09T18:28:35Z / 2026-01-09 | 190 | UNCHANGED-FROZEN (no refresh since certification) |
| cma, positioning | (footer) | `json/latest/manifest.json` | -- | yes / 1,551 / 2026-10-14T11:07:12Z | 0 | UNCHANGED-LIVE |
| correlations | cor.01 | `json/correlations/correlation_data.json` | 2026-08-10 | yes / 152,549 / 2026-10-14T11:06:00Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| factor-tilts | ft.01-03 | `json/factor-tilts/{tier1-snapshot,tier2-spreads,tier3-timeseries}.json` | 2026-08-10 | yes x3 / 10,697 + 125,909 + 4,059,298 / 2026-10-14T11:06:02Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| macro | mac.01 | `json/macro/macro_data.json` | 2026-08-10 | yes / 197,329 / 2026-10-14T11:06:01Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| macro | mac.02 | `json/macro/timeseries/{slug}.json` | 79 members | 79 of 79 written 2026-10-14T11:06:00-09Z; sample `10y` as_of 2026-10-13 | 0 | UNCHANGED-LIVE (member count unchanged) |
| macro | mac.03 | `json/macro/volatility_data.json` | 2026-08-07 | yes / 1,462,638 / 2026-10-14T12:30:36Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| macro | mac.04 | `json/macro/yield_curve_fred.json` | 2026-08-05 | yes / 672,088 / 2026-10-13T23:01:26Z / 2026-10-13 | 0 | UNCHANGED-LIVE (the Aug 5-day lag is gone) |
| market | mkt.01 | `json-tiered/market-overview/summary/all-returns.json` | 2026-08-10 | yes / 51,553 / 2026-10-14T11:06:54Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| market | mkt.02 | `json/market/all_returns.json` (fallback leg) | 2026-04-15 write | yes / 35,648 / 2026-04-15T20:19:39Z / data_as_of 2026-04-10 | 128 | UNCHANGED-FROZEN (DENY stands; fallback leg still in `market.ts`) |
| portfolios | mp.01-03 | `platinum/mdpf/{scope}/{aum-metrics,account-distribution,aggregate-aua-timeseries}.json` | 2026-08-10 | 12 of 12 (4 scopes) / 2026-10-13T13:50:5xZ / source_vintages 2026-10-12 (account-distribution period 2026-10-13 for global/49f/inflection) | 1 at 13:29:52Z, before the day's publish (prior runs 13:31-13:50Z) | UNCHANGED-LIVE |
| portfolios | mp.04-06 | `json/benchmarks/{model_portfolio_timeseries,model_portfolio_benchmarks,etf_returns}.json` | 2026-08-10 | yes x3 / 2026-10-14T11:06:0xZ / 2026-10-13 | 0 | UNCHANGED-LIVE |
| portfolios | mp.07 | `json/peers/peer_performance.json` | month | yes / 8,531 / 2026-10-01T14:29:41Z / 2026-09-30 | 9 (monthly: healthy) | UNCHANGED-LIVE |
| portfolios | mp.08 | `json/benchmarks/benchmark_returns.json` | 2026-08-10 | yes / 13,000 / 2026-10-14T11:06:00Z / 2026-10-13 | 0 | UNCHANGED-LIVE, still 0 callers (held at Andrew) |
| portfolios | mp.09-10 | `json/benchmarks/_smartx_model_{daily,monthly}.json` | 2026-05-29 / 2026-05 | yes x2 / 2026-06-01T13:36:11Z / 2026-05-29, 2026-05 | 94 | UNCHANGED-FROZEN (DENY) |
| portfolios | mp.11 | `platinum/mdpf/global/non-model-assets.json` | 2026-08-07 | yes / 100,081 / 2026-10-13T13:50:53Z / 2026-10-12 | 1 | UNCHANGED-LIVE, 0 callers. NEW DEFECT: `getNonModelAssets` now HAS a caller (`ModelPortfolios.tsx`) and targets `json/portfolios/non_model_assets.json`, which is ABSENT -> every call 404s |
| portfolios | mp.12 | `platinum/mdpf/cottonwood/account-units.json` | current | yes / 9,949 / 2026-10-13T13:50:52Z / 2026-10-12 | 1 | UNCHANGED-LIVE, 0 callers (held at Andrew) |
| portfolios | mp.13 | `platinum/mdpf/_manifests/**` | 10 keys | 96 keys, newest 2026-10-13T13:50:54Z | -- | UNCHANGED-LIVE (grew 10 -> 96) |
| portfolios | mp.14 | `platinum/mdpf/archive/**` | 444 keys, all 2026-08-06 | 444 keys, min = max 2026-08-06 | -- | UNCHANGED-FROZEN |
| portfolios | mp.15 | `json/mdpf/**` | frozen legacy tree | **0 keys** | -- | **GONE** (catalog row, `never_serve` line and `portal_lookup.py` channel `mdpf` still name it) |
| portfolios | mp.16 | `json/yang/volatility_data.json` | 2026-01-14 | yes / 180 / 2026-01-14T22:56:01Z / 2026-01-14 | 187 | UNCHANGED-FROZEN (DENY) |
| portfolios (catalog path) | -- | `platinum/mdpf/aggregate_aua/YYYY-MM-DD.json` | named by catalog `mdpf_model_portfolios.paths.daily_history` | 0 keys there; 439 daily snapshots live under `platinum/mdpf/archive/aggregate_aua/`, frozen 2026-08-06 | -- | **MOVED** (into the frozen archive) |
| security-scanner | sscn.01 | `json/security_scanner/latest/factor_metadata.json` | 2026-08-06 upload | yes / 69,350 / 2026-10-02T16:38:03Z / 289 factors | 7 (manual monthly FactSet upload) | UNCHANGED-LIVE |
| security-scanner | sscn.02-03 | `json/security_scanner/latest/universes/{acwx,eafe,eafev,r1000,r1000v,sp500}/{universe_data,scanner_data}.json` | 6 of 6 | 12 of 12 / 2026-10-02T16:38:0x-31Z | 7 | UNCHANGED-LIVE |
| security-scanner | sscn.04 | `.../universes/{msciusa,rmidcap,sp400}/*.json` | orphaned | 6 keys / 2026-05-20T15:43Z | 100 | UNCHANGED-FROZEN (unrequestable) |
| valuations | val.01 | `json/valuation/valuation_data.json` | 2026-08-10 | yes / 2,198,978 / 2026-10-14T11:06:29Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| valuations | val.02 | `json/valuation/risk_premium_data.json` | 2026-08-10 | yes / 145,523 / 2026-10-14T11:05:59Z / 2026-10-13 | 0 | UNCHANGED-LIVE |
| valuations | (twin) | `valuation/valuation_data.json` | frozen | yes / 291,246 / 2026-01-04T04:46:14Z / as_of 2025-12-31 | 196 | UNCHANGED-FROZEN (not URL-reachable) |

### 2.3 (b) The three uncertified pages, contracted from source + live

| page | what it reads (PROD source) | where the data lives (measured) | portal-v2 share |
|---|---|---|---|
| advisor-intelligence (`src/pages/AdvisorIntelligence`, 68 files) | `/api/scoped/advisor-intelligence/*` (CF -> `opal-data-bd` with `shared-advisor-router:28`, or API GW 7k3ed8px20), `/api/scoped/partners/books/*` | per-firm buckets `opal-data-bd` / `opal-data-inf` / `opal-data-cot` (G2 scope) | ADVI twins `platinum/advi/49financial/*`: route LIVE, **0 of 15 registry keys flipped** (`adviKeyRepoint.ts` registry: 14 held, 1 structural) -> 0 reads. perfrp leaves `platinum/advi/{firm}/perfrp_*`: the page fetches 8 leaf families; **3 exist** (book_advisor, gainloss_account, gainloss_relationship, as_of 2026-09-01, 29 TD); 5 (performance_*, allocation_*, transactions_*_sample) absent -> 404 -> null by design (`advisor-intelligence.ts:1636-1648`) |
| ticket-center (`src/pages/TicketCenter`, 6 files) | `/api/scoped/tickets*` (10 routes) | Lambda `opal-ticket-api` (env TABLE_NAME=opal-tickets, USERS_TABLE=opal-users-v2) -> DynamoDB `opal-tickets`: 31 items, hash `ticket_id`, GSI `status-index` | none |
| trade-submission (`src/pages/TradeSubmission`, 23 files) | `/api/general/trades/*` (CF -> API GW, not the S3 router) | `trade-dashboard-api` + `trade-submission-handler` -> DynamoDB `opal-trade-submissions` (33 items, hash `submission_id`, 4 GSIs) + S3 `opal-data-trade-submissions` (27 objects: submissions/ 25, parquet/ 2; newest 2026-07-20) | none |

### 2.4 Prefix census (84 groups; 4,851 of 4,851 objects)

Lag = TD behind T-1 of the newest object's data (served datasets use the payload as-of; others LastModified date). "URL" = reachable through `/api/general/*`. "page" = a PROD page/component reads it (accessor walk, 2.5).

| group | objects | bytes | newest LastModified (UTC) | URL | page |
|---|---:|---:|---|---|---|
| `json/positioning/positioning_data.json` | 1 | 6,883 | 2026-10-14T11:06:02Z | yes | yes |
| `json/positioning/allocation_summary.json` | 1 | 962 | 2026-10-14T11:06:06Z | yes | yes |
| `json/positioning/holdings_attribution_data.json` | 1 | 403,939 | 2026-10-06T20:24:47Z | yes | yes |
| `json/positioning/opal_aggregate.json` | 1 | 3,893 | 2026-10-14T11:06:02Z | yes | yes |
| `json/benchmarks/model_portfolio_benchmarks.json` | 1 | 19,691 | 2026-10-14T11:06:00Z | yes | yes |
| `json/benchmarks/model_portfolio_timeseries.json` | 1 | 776,041 | 2026-10-14T11:06:01Z | yes | yes |
| `json/benchmarks/etf_returns.json` | 1 | 1,282 | 2026-10-14T11:06:00Z | yes | yes |
| `json/benchmarks/benchmark_returns.json` | 1 | 13,000 | 2026-10-14T11:06:00Z | yes | no |
| `json/benchmarks/_smartx_model_*` | 2 | 254,605 | 2026-06-01T13:36:11Z | yes | no |
| `json/peers/` | 1 | 8,531 | 2026-10-01T14:29:41Z | yes | yes |
| `json/capital-markets/assumptions.json` | 1 | 4,146 | 2026-03-11T00:45:53Z | yes | yes |
| `json/capital-markets/views.json` | 1 | 5,992 | 2026-01-09T18:28:35Z | yes | yes |
| `json/correlations/` | 1 | 152,549 | 2026-10-14T11:06:00Z | yes | yes |
| `json/factor-tilts/` | 3 | 4,195,904 | 2026-10-14T11:06:02Z | yes | yes |
| `json/macro/macro_data.json` | 1 | 197,329 | 2026-10-14T11:06:01Z | yes | yes |
| `json/macro/macro_data_fred.json` | 1 | 76,394 | 2026-10-13T23:31:05Z | yes | no |
| `json/macro/timeseries/` | 79 | 151,702 | 2026-10-14T11:06:09Z | yes | yes |
| `json/macro/volatility_data.json` | 1 | 1,462,638 | 2026-10-14T12:30:36Z | yes | yes |
| `json/macro/vix_data.json` | 1 | 787,143 | 2026-10-14T12:30:36Z | yes | no (`getVIXData` 0 callers) |
| `json/macro/yield_curve_fred.json` | 1 | 672,088 | 2026-10-13T23:01:26Z | yes | yes |
| `json/valuation/valuation_data.json` | 1 | 2,198,978 | 2026-10-14T11:06:29Z | yes | yes |
| `json/valuation/risk_premium_data.json` | 1 | 145,523 | 2026-10-14T11:05:59Z | yes | yes |
| `json/valuations/` (legacy twins) | 2 | 84,431 | 2025-12-26T18:56:56Z | yes | no |
| `json-tiered/market-overview/summary/` | 1 | 51,553 | 2026-10-14T11:06:54Z | yes | yes |
| `json-tiered/market-overview/rsi-*` | 4 | 1,872,129 | 2026-10-14T11:06:56Z | yes | yes |
| `json-tiered/market-overview/timeseries/` | 157 | 10,619,201 | 2026-10-14T11:07:01Z (84 written today, 73 frozen Jan-Feb) | yes | yes |
| `json-tiered/market-overview/details/` | 213 | 24,518,752 | 2026-10-14T11:07:00Z (71 written today, 142 frozen Jan) | yes | no (`getMarketOverviewDetails` 0 callers) |
| `json/market/market-regime*` | 2 | 741,896 | 2026-10-14T11:07:11Z | yes | yes |
| `json/market/all_returns.json` | 1 | 35,648 | 2026-04-15T20:19:39Z | yes | fallback only |
| `json/market-overview/` | 1 | 107,839 | 2026-01-13T17:06:03Z | yes | no |
| `json/sentiment/fear-greed-index.json` | 1 | 244,595 | 2026-10-13T21:30:42Z | yes | yes |
| `json/sentiment/keyword-sentiments.json` | 1 | 176,043 | 2026-10-14T11:18:08Z | yes | yes |
| `json/sentiment/keyword-history-*` | 720 | 2,955,966 | 2026-04-07T14:40:49Z | yes | no (both accessors 0 callers) |
| `json/trending/` | 1 | 93,766 | 2026-10-14T11:21:00Z | yes | yes |
| `json/semantic-trending/` | 1 | 30,603 | 2026-02-24T14:20:44Z | yes | flag-off only (`USE_SEMANTIC_TRENDING` false) |
| `json/security_scanner/latest/factor_metadata.json` | 1 | 69,350 | 2026-10-02T16:38:03Z | yes | yes (via `opal-data-refresh-api` route) |
| `json/security_scanner/latest/universes/` | 18 | 171,499,054 | 2026-10-02T16:38:31Z | yes | 12 of 18 (6 orphans) |
| `json/security_scanner/` dated snapshots | 76 | 710,242,192 | 2026-10-02T16:38:31Z | yes | no |
| `json/latest/manifest.json` | 1 | 1,551 | 2026-10-14T11:07:12Z | yes | yes (`useDataFreshness`, DataRefresh) |
| `json/latest/*` source pointers | 5 | 1,994 | 2026-10-14T11:03:49Z | yes | no |
| `json/yang-pipeline-metadata.json` | 1 | 254 | 2026-10-14T11:03:49Z | yes | no |
| `json/portfolios/` (legacy, incl. 2 firm dirs) | 5 | 313,947 | 2026-07-27T15:10:07Z | yes | 1 key (`aum-timeseries.json`, frozen) |
| `json/model_portfolios/` | 25 | 128,283,594 | 2026-06-01T14:16:37Z | yes | no |
| `json/returns/` | 1 | 14,578 | 2025-12-23T23:40:00Z | yes | no |
| `json/yang/` | 1 | 180 | 2026-01-14T22:56:01Z | yes | no |
| `platinum/mdpf/{4 scopes}/{4 leaves}` | 16 | 1,883,308 | 2026-10-13T13:50:54Z | yes | yes |
| `platinum/mdpf/global/non-model-assets.json` | 1 | 100,081 | 2026-10-13T13:50:53Z | yes | no |
| `platinum/mdpf/cottonwood/account-units.json` | 1 | 9,949 | 2026-10-13T13:50:52Z | yes | no |
| `platinum/mdpf/_manifests/` | 96 | 911,619 | 2026-10-13T13:50:54Z | yes | no |
| `platinum/mdpf/archive/` | 444 | 2,888,714 | 2026-08-06T21:42:10Z | yes | no |
| `platinum/etfs/positioning_data.json` | 1 | 147,472 (147,516 at 13:01:42Z re-read) | 2026-10-14T13:01:42Z | yes | yes |
| `platinum/etfs/_manifests/` | 65 | 53,801 | 2026-10-13T13:01:41Z | yes | no |
| `platinum/advi/49financial/perfrp_*` | 3 | 34,316,561 | 2026-09-01T07:27:05Z | scoped route only | yes (advisor router, inferred) |
| `platinum/advi/49financial/` twins + `_manifests/` | 15 | 21,059,752 | 2026-09-01T11:06:00Z | scoped route only | no (0 of 15 flipped) |
| `benchmarks/` (data/model PKL inputs + LATEST.json) | 231 | 2,790,520,867 | 2026-10-14T11:03:54Z | no | no |
| `canon/` (archive, data_pkl parquet canon, state) | 302 | 953,272,218 | 2026-10-14T11:06:17Z | no | no |
| `data-refresh/` (archive, pending, staging, varflag) | 694 | 2,293,259,852 | 2026-10-14T11:07:38Z | no | DataRefresh via API |
| `uploads/` (manual Excel/PKL drops) | 14 | 36,327,885 | 2026-10-06T19:01:10Z | no | no |
| `security_scanner/uploads/` (FactSet Excel) | 6 | 51,261,833 | 2026-10-02T16:37:50Z | no | upload via API |
| `cache/` (FRED csv) | 2 | 25,398 | 2026-10-11T06:00:06Z | no | no |
| `config/` | 1 | 10,188 | 2026-04-22T14:29:05Z | no | no |
| `portfolio-management/` (ETF PM drafts; keyed by fund) | 50 | 16,722,552 | 2026-10-12T13:52:12Z | no | PM page via `/api/private/portfolio*` |
| `daily-reports/` (QA HTML) | 95 | 6,348,935 | 2026-10-13T20:13:51Z | no | no |
| `security-reports/` | 978 | 24,881,847 | 2026-10-14T12:02:27Z | no | no |
| `security-checkpoints/` | 1 | 6,146 | 2026-02-17T17:33:05Z | no | no |
| `infrastructure/` | 257 | 35,819,602 | 2026-10-14T12:50:15Z | no | no |
| `sprint/` | 4 | 122,676 | 2026-10-04T21:46:26Z | no | no |
| `assets/`, `logos/`, `index.html`, `favicon.png`, `vite.svg` (old static build) | 199 | 16,767,684 | 2026-02-06T21:42:41Z | no | no |
| `generated-images/`, `image-references/` | 12 | 11,765,967 | 2025-12-23T23:40:00Z | no | no |
| `lambda-packages/` | 1 | 58,785,015 | 2026-01-14T21:10:21Z | no | no |
| `market-metrics.json` + `.gz` | 2 | 1,300,842 | 2026-04-15T20:19:37Z | no (v1 Lambda proxy reads it) | no |
| `macro/` | 2 | 242,715 | 2026-10-14T11:06:01Z (`macro/macro_data.json` written today) | no | no |
| `metadata/`, `metrics/`, `positioning/`, `raw/`, `returns/`, `sentiment/`, `valuation/` (Dec-Jan legacy) | 16 | 2,311,709 | 2026-01-08T21:31:16Z | no | no |

### 2.5 (c) Served prefixes no page reads (URL-reachable, 0 PROD page/component callers)

| key or family | objects | state | why it matters |
|---|---:|---|---|
| `json/benchmarks/benchmark_returns.json` | 1 | live | held at Andrew (catalog `held_at_andrew`) |
| `json/benchmarks/_smartx_model_{daily,monthly}.json` | 2 | frozen 94 TD | catalog DENY |
| `json/macro/vix_data.json` | 1 | live | co-emitted with volatility_data; legacy `/macro/vix` |
| `json/macro/macro_data_fred.json` | 1 | live-written, data_as_of 2026-09-01 (29 TD) | catalog channel `macro_rates.paths.primary` names it; no row |
| `json-tiered/market-overview/details/*` | 213 | 71 live, 142 frozen | `getMarketOverviewDetails` 0 callers; mixed vintages in one family |
| `json/market-overview/trending-topics.json` | 1 | frozen 188 TD | -- |
| `json/sentiment/keyword-history-{articles,summary}/*` | 720 | frozen since 2026-04-07 (131 TD) | catalog DENY; accessors exist, 0 callers |
| `json/semantic-trending/latest.json` | 1 | frozen 160 TD | feature flag permanently off |
| `json/security_scanner/{2026-02-26,2026-05-18,2026-08-06,2026-10-02,20260519,20260521}/**` | 76 | dated snapshots | two date-key conventions (`YYYY-MM-DD` and `YYYYMMDD`) |
| `json/security_scanner/latest/universes/{msciusa,rmidcap,sp400}/*` | 6 | frozen 100 TD | structurally unrequestable |
| `json/latest/{data_pkl,model_pkl,attribution_excel,peer_excel,cma_excel}.json`, `json/yang-pipeline-metadata.json` | 6 | live | pipeline-input pointers (manifest.json is the read one) |
| `json/portfolios/{aum-metrics,account-distribution}.json`, `json/portfolios/{49financial,inflection}/account-distribution.json` | 4 | frozen 57-58 TD (firm dirs 2026-05-29) | firm-partitioned legacy, still URL-reachable |
| `json/model_portfolios/**` | 25 | frozen 93 TD | 128 MB; catalog `never_serve` |
| `json/returns/etf_period_returns.json`, `json/valuations/*`, `json/yang/volatility_data.json` | 4 | frozen 187-218 TD | same-basename twins of live keys |
| `platinum/mdpf/global/non-model-assets.json`, `platinum/mdpf/cottonwood/account-units.json` | 2 | live | DENY / held |
| `platinum/mdpf/_manifests/**`, `platinum/mdpf/archive/**`, `platinum/etfs/_manifests/**` | 605 | ops / frozen | provenance only |
| `platinum/advi/49financial/{10 twin leaves, _manifests/}` | 15 | frozen 36 TD | reached only by the scoped route, 0 keys flipped |

## 3. Analysis

### 3.1 What the datasets are

- **Yang model-book family (opal-internal, daily at ~11:03-11:07Z after the data-refresh trigger):** positioning, allocation, opal aggregate, benchmarks, correlations, factor tilts, macro, valuation, market overview/regime. All carry `data_as_of` = T-1 (0 TD today). They describe the five Opal model portfolios (UST/ST/INT/LT/ULT) and the market; none is a client's holding.
- **Monthly/annual uploads:** holdings attribution and peers (month-end, 2026-09-30), CMA assumptions (annual edition '2026') and views (2026-01-09, 190 TD, no refresh), security scanner (manual FactSet upload, 2026-10-02).
- **MDPF platinum (firm-partitioned, daily ~13:31-13:50Z):** aum-metrics, account-distribution, aggregate-aua-timeseries, category-views per scope `global|49financial|cottonwood|inflection`, written by `opal-assets-mdpf-portal-publisher` from `opal-data-assets/portal/gold/mdpf/{scope}/...` (measured in `_provenance.source_keys`). G4 must measure its overlap against these 18 keys.
- **ETF platinum (opal-internal):** `platinum/etfs/positioning_data.json` (DIVZ, IDVZ, PFDE, PFOE), producer `etf_positioning_publisher` (manifest), daily ~13:01Z.
- **ADVI platinum (49financial client data, PII):** 3 perfrp leaves (account keys, relationship names, advisor names) and 10 twin leaves. Catalog v0.4: `platinum/advi NOT YET` (held).
- **News/sentiment singletons (opal-internal):** fear-greed, keyword sentiments, trending topics; producers named in Lambda env (`opal-portal-fear-greed-fetcher`, `news-trending-analysis`, `keyword-intelligence-generator`). G6 owns the DynamoDB side.

### 3.2 Firm scoping

- Firm key segment: `platinum/mdpf/<scope>/` and `platinum/advi/<firm>/` (path segment 3), `json/portfolios/<firm>/` (segment 3, legacy). `global` is the enterprise aggregate, never the sum of the three firm scopes (catalog `never_sum_rules`).
- Firm vocabulary differs by axis: key segment `49financial` vs bucket suffix `bd` (`advisor-intelligence.ts:1615-1622`). A tool must take the long form for portal-v2 keys.
- No contract below mixes firms: the per-scope contracts declare `firm` as the scope segment, and the tool proposals take one `scope` per call (the existing `portal_index` gate already refuses another firm's member).
- Account/last-4: only the perfrp leaves carry account-grain keys. `perfrp_gainloss_account`: 6,183 entries, 1 key shape (10 characters), 4,637 last-4 groups, **1,280 colliding last-4 groups covering 2,826 of 6,183 entries** (last-4 is NOT unique within 49financial). The relationship leaf keys are name-shaped (3,058 shape classes of 3,836) and the advisor leaf keys are names: both are PII and must never be echoed by a tool.

### 3.3 Common questions (what a seat asks of this bucket)

- What do the Opal models hold / how are they positioned / what is our aggregate book? (C01, C02, C04)
- Did model X beat its benchmark over period P? What did the ETF equivalents do? (C05-C08)
- What are the house CMA assumptions and tactical views? (C11, C12)
- How correlated are asset classes over window W? What factor tilts do the models carry? (C13, C14)
- Where is the yield curve, VIX/MOVE regime, a macro indicator, an index valuation or the ERP/credit spread? (C15-C20)
- What did index/sector X return over P? What market regime are we in? (C21, C22)
- What is market sentiment / what is trending in the news? (C24, C26)
- Which stocks in universe U score best on factor F? (C27)
- Is the pipeline current, and as of what date? (C28)
- What is firm F's AUM / account-size distribution / AUA trend / category mix? (C31-C34, one firm per call)

### 3.4 Gateway tools: verdicts and proposals

Existing (`tool_index`, member a): `mdpf_get_aum_metrics`, `mdpf_get_account_distribution`, `mdpf_get_aggregate_aua`, `mdpf_get_model_benchmarks`, `etfs_get_positioning` (all `app/integrations/portal_index/integration.py`, catalog-keyed, firm-gated): **KEEP**. `gateway_query_catalog` and `opal_asker_query` (26 linked rows): **KEEP, EXTEND** by adding catalog rows for 9 live datasets (opal_aggregate, category-views, market-regime, json-tiered rsi/timeseries, trending, fear-greed + keyword-sentiments, security scanner, pipeline manifest); **RE-RULE** link `ft.04.portfolios-aum-metrics` to deny (frozen 58 TD, no page). Repo tool `org/tier0_utility/0.0.3_BG_BBGTerminal/tools/portal_lookup.py`: **RETIRE channel `mdpf`** (`json/mdpf/`, 0 keys), correct channel `mdpf-platinum` note (daily snapshots are in `archive/`, frozen), add `json-tiered`, `security_scanner`, `platinum/etfs`.

Proposed purpose-built tools (same pattern: one whole object per call, key from the catalog row, answer carries the object's own as-of):

| tool | object(s) | firm input | answers |
|---|---|---|---|
| `mdpf_get_category_views` | `platinum/mdpf/{scope}/category-views.json` | scope (one) | firm AUA by category (Models/SMA/Client/Alternatives/Insurance) |
| `portal_get_model_positioning` | `json/positioning/positioning_data.json` + `opal_aggregate.json` | none (opal-internal) | model allocation, holdings, deltas vs benchmark; aggregate book |
| `portal_get_model_attribution` | `json/positioning/{holdings_attribution_data,allocation_summary}.json` | none | QTD/YTD/1Y/SI attribution per model |
| `portal_get_market_returns` | `json-tiered/market-overview/summary/all-returns.json`, `timeseries/{ticker}.json` | none | index/sector period returns and price history |
| `portal_get_market_regime` | `json/market/market-regime.json` (+history) | none | current regime, signals, history |
| `portal_get_macro` | `json/macro/{macro_data,volatility_data,yield_curve_fred}.json`, `timeseries/{slug}.json` | none | indicator level/series, curve, VIX/MOVE |
| `portal_get_valuation` | `json/valuation/{valuation_data,risk_premium_data}.json` (project one index) | none | P/E etc. vs range; ERP; IG/HY OAS |
| `portal_get_security_scan` | `json/security_scanner/latest/universes/{u}/scanner_data.json` + `factor_metadata.json` | none | top/bottom names in a universe by factor percentile |
| `portal_get_pipeline_freshness` | `json/latest/manifest.json` | none | each source's data_as_of and last run |

Not proposed (blocked, with reason): perfrp / ADVI twins (catalog v0.4 holds `platinum/advi`; PII); tickets (catalog RESOLVER FLOOR, D7 sec.7.3 at Andrew); trade submissions (initiator/approver email + name fields; same floor class); frozen DENY rows.

## 4. Contracts (one JSON block per bucket -> dataset)

Common claims: `size.objects` and LastModified measured from the 12:55:42Z listing; payload fields measured by the 13:0xZ-13:2xZ probe; producer `measured` where the certified rectangle or `_provenance`/manifest names it, else `inferred`. `rows_sampled` counts the main array/map members in the one object read.

```json
{"contract_id": "opal-data-portal-v2/served/positioning_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/positioning/positioning_data.json", "layer": "served", "format": "json (ContentEncoding gzip)", "table": "positioning_data",
 "grain": "one object; one member per model portfolio (UST, ST, INT, LT, ULT) plus 2 benchmark blocks (etf, index)", "partition": {"keys": [], "claim": "measured", "note": "single overwritten object"},
 "producer": {"name": "yang-generate-positioning (ProcessBothPKLs branch)", "schedule": "daily after the data-refresh trigger, written 11:06Z", "claim": "measured (rectangle pos.01) + inferred (schedule from LastModified)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 6883, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date (T-1)", "example": "2026-10-13"}, {"name": "generated_at", "type": "string instant", "nullable": false, "description": "run time, never the vintage", "example": "2026-10-14T11:06:01Z"}, {"name": "data_date", "type": "string YYYYMMDD", "nullable": false, "description": "compact data date", "example": "20261013"}, {"name": "benchmarks.{etf,index}.{cash,fixed_income,equity,structured,commodities,alternatives}", "type": "object", "nullable": false, "description": "benchmark asset-class mix", "example": "{...}"}, {"name": "portfolios.<model>.{code,name,allocation,management,characteristics,segment,benchmark,delta,management_delta,num_holdings,holdings,data_as_of,prior_date}", "type": "object", "nullable": false, "description": "per-model positioning and deltas vs benchmark", "example": "UST"}, {"name": "current_holdings.<model>.{holdings[],aum}", "type": "object", "nullable": false, "description": "holdings rows (14 fields each) and model AUM", "example": "11 rows for UST"}],
 "enums": {"model": ["UST", "ST", "INT", "LT", "ULT"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal book level", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["model positioning", "model holdings", "asset allocation", "overweight underweight", "positioning vs benchmark", "book level"],
 "common_queries": ["How is the LT model positioned versus its benchmark?", "What does the UST model hold today?", "How many holdings does each model carry?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row att.04.positioning-data)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_model_positioning", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest only", "model": "UST|ST|INT|LT|ULT"}, "returns": "allocation, deltas and holdings for one model with data_as_of", "answers": ["How is the LT model positioned versus its benchmark?"]}],
 "catalog_entry": {"data_catalog_key": "channels.positioning_holdings.artifacts[json/positioning/positioning_data.json]", "present": true},
 "prior_art": "workflows/atom_decomposition/runs/portal-page-positioning/20260811T1818Z/rectangle.final.certified.json (pos.01)",
 "open_items": ["BOOK-LEVEL, never a client's holdings (certified caveat)"],
 "evidence": [{"read": "head+get s3://opal-data-portal-v2/json/positioning/positioning_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/allocation_summary", "bucket": "opal-data-portal-v2", "s3_prefix": "json/positioning/allocation_summary.json", "layer": "served", "format": "json (gzip)", "table": "allocation_summary",
 "grain": "one object; per model x period (qtd, ytd, 1y, si)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-allocation-summary", "schedule": "daily, written 11:06Z", "claim": "measured (rectangle att.01) + inferred schedule"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 962, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date", "example": "2026-10-13"}, {"name": "generated_at", "type": "string instant", "nullable": false, "description": "run time", "example": "2026-10-14T11:06:05Z"}, {"name": "portfolios.<model>.{qtd,ytd,1y,si}", "type": "object (2 fields each)", "nullable": false, "description": "allocation/policy comparison by period", "example": "{...}"}],
 "enums": {"model": ["UST", "ST", "INT", "LT", "ULT"], "period": ["qtd", "ytd", "1y", "si"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["allocation summary", "policy comparison", "style drift", "asset class allocation"],
 "common_queries": ["Is the INT model where its policy says it should be?", "What is the YTD allocation summary for each model?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row att.01.allocation-summary)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_model_attribution", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest only", "model": "one model"}, "returns": "allocation summary by period with data_as_of", "answers": ["What is the YTD allocation summary for each model?"]}],
 "catalog_entry": {"data_catalog_key": "channels.positioning_holdings.artifacts[json/positioning/allocation_summary.json]", "present": true},
 "prior_art": "workflows/atom_decomposition/runs/portal-page-attribution/20260811T1834Z/rectangle.final.certified.json (att.01)",
 "open_items": ["Certified R: the StylePolicyComparison footer binds manifest attribution_excel (2026-09-30), not this artifact's date"],
 "evidence": [{"read": "head+get json/positioning/allocation_summary.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/holdings_attribution_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/positioning/holdings_attribution_data.json", "layer": "served", "format": "json", "table": "holdings_attribution_data",
 "grain": "one object; per model x period (qtd, ytd, 1y, si) attribution", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-holdings-attribution (attribution_excel branch)", "schedule": "on the monthly attribution Excel upload (uploads/Model Portfolio Attribution YYYYMMDD.xlsx)", "claim": "measured (rectangle att.02) + inferred cadence"},
 "freshness": {"latest_partition": "2026-09-30", "field": "data_as_of", "lag_trading_days": 9, "basis": "trading-day-frontier (month-end cadence; 9 TD is healthy)", "claim": "measured"},
 "size": {"objects": 1, "bytes": 403939, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "data_as_of", "type": "string date", "nullable": false, "description": "month-end of the attribution", "example": "2026-09-30"}, {"name": "as_of_date", "type": "string date", "nullable": false, "description": "same as data_as_of", "example": "2026-09-30"}, {"name": "generated_at", "type": "string instant", "nullable": false, "description": "processing time", "example": "2026-10-06T20:24:46Z"}, {"name": "note", "type": "string", "nullable": true, "description": "producer note", "example": "<text>"}, {"name": "portfolios.<model>.{code,name,qtd,ytd,1y,si}", "type": "object", "nullable": false, "description": "attribution per period", "example": "ULT"}],
 "enums": {"model": ["ULT", "LT", "INT", "ST", "UST"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["attribution", "performance attribution", "selection effect", "allocation effect", "what drove returns"],
 "common_queries": ["What drove the LT model's QTD return?", "Which holdings contributed most YTD?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row att.02.holdings-attribution)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_model_attribution", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest month-end", "model": "one model", "period": "qtd|ytd|1y|si"}, "returns": "attribution block with data_as_of", "answers": ["What drove the LT model's QTD return?"]}],
 "catalog_entry": {"data_catalog_key": "channels.positioning_holdings.artifacts[json/positioning/holdings_attribution_data.json]", "present": true},
 "prior_art": "rectangle.final.certified.json att.02 / pos.02",
 "open_items": ["Explains PAST performance only; month grain"],
 "evidence": [{"read": "head+get json/positioning/holdings_attribution_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/opal_aggregate", "bucket": "opal-data-portal-v2", "s3_prefix": "json/positioning/opal_aggregate.json", "layer": "served", "format": "json (gzip)", "table": "opal_aggregate",
 "grain": "one object; the AUM-weighted aggregate book (AGG) across the five models, with weights and reconciliation", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-positioning (same write second as positioning_data)", "schedule": "daily 11:06Z", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 3893, "rows_sampled": 29, "claim": "measured"},
 "columns": [{"name": "status", "type": "string", "nullable": false, "description": "OK or refusal status", "example": "OK"}, {"name": "reason", "type": "string|null", "nullable": true, "description": "why not OK", "example": null}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date", "example": "2026-10-13"}, {"name": "current_holdings.AGG.{holdings[],total_aum}", "type": "object", "nullable": false, "description": "aggregate holdings (15 fields per row)", "example": "29 rows"}, {"name": "weights.<model>", "type": "float", "nullable": false, "description": "AUM weight per model", "example": 0.2}, {"name": "weights_source.{key,version_id,period}", "type": "object", "nullable": false, "description": "the MDPF platinum object the weights came from", "example": "platinum/mdpf/global/aum-metrics.json, period 2026-10-12"}, {"name": "members", "type": "object", "nullable": false, "description": "AUM per model plus blends", "example": "{...}"}, {"name": "left_out", "type": "list", "nullable": false, "description": "models excluded", "example": []}, {"name": "reconciliation", "type": "object", "nullable": false, "description": "five_primary_sum, members_sum, file_total_model_aum, gap", "example": "{...}"}],
 "enums": {"status": ["OK"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal aggregate; weights read from the global MDPF scope", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["aggregate book", "opal aggregate", "total holdings", "AUM weighted portfolio", "firm wide positioning"],
 "common_queries": ["What does Opal hold in aggregate across all models?", "What weight does each model carry in the aggregate book?"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"},
 "proposed_tools": [{"name": "portal_get_model_positioning", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "model": "AGG"}, "returns": "aggregate holdings, weights, reconciliation gap, data_as_of and weights_source.period", "answers": ["What does Opal hold in aggregate across all models?"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "portal/src/pages/Positioning/README.md (origin/PROD); none certified",
 "open_items": ["Not certified, not catalogued: needs a catalog row before any tool", "Cross-dataset dependency: weights come from platinum/mdpf/global/aum-metrics.json (G4 overlap)", "Two vintages in one object: data_as_of (T-1) and weights_source.period (MDPF, one day older at 11:06Z)"],
 "evidence": [{"read": "get json/positioning/opal_aggregate.json (gzip)", "at": "2026-10-14T13:3xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/model_portfolio_benchmarks", "bucket": "opal-data-portal-v2", "s3_prefix": "json/benchmarks/model_portfolio_benchmarks.json", "layer": "served", "format": "json", "table": "model_portfolio_benchmarks",
 "grain": "one object; per model x period (10 periods, 1D through SI) vs index and ETF benchmarks", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-model-portfolio-benchmarks (ProcessBothPKLs branch)", "schedule": "daily 11:06Z", "claim": "measured (rectangle mp.05)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 19691, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date", "example": "2026-10-13"}, {"name": "periods", "type": "list[string]", "nullable": false, "description": "10 period labels", "example": "1D"}, {"name": "inception_date", "type": "string date", "nullable": false, "description": "series start", "example": "<date>"}, {"name": "models[].{code,name,benchmark_last_date,returns}", "type": "list[object]", "nullable": false, "description": "returns per period incl. spreads vs index_benchmark and etf_benchmark", "example": "UST"}, {"name": "index_compositions / etf_compositions / model_names", "type": "map model->string", "nullable": false, "description": "benchmark definitions", "example": "<composition text>"}, {"name": "source / model_source_note", "type": "string", "nullable": false, "description": "provenance text", "example": "<text>"}],
 "enums": {"model": ["UST", "ST", "INT", "LT", "ULT"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["model performance", "vs benchmark", "relative performance", "track record", "model returns"],
 "common_queries": ["Did the ST model beat its index benchmark YTD?", "What is each model's since-inception return vs its ETF benchmark?"],
 "existing_gateway_tool": {"name": "mdpf_get_model_benchmarks", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "portal_datasets.portal_mdpf_model_benchmarks + channels.benchmarks_and_models", "present": true},
 "prior_art": "rectangle.final.certified.json mp.05 (portal-page-portfolios/20260811T1640Z)",
 "open_items": ["MODEL-DESIGN returns, never a client's realized return (tool already carries the caveat)"],
 "evidence": [{"read": "head+get json/benchmarks/model_portfolio_benchmarks.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/model_portfolio_timeseries", "bucket": "opal-data-portal-v2", "s3_prefix": "json/benchmarks/model_portfolio_timeseries.json", "layer": "served", "format": "json", "table": "model_portfolio_timeseries",
 "grain": "one row per trading day x model", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-model-portfolio-benchmarks", "schedule": "daily 11:06Z", "claim": "measured (rectangle mp.04)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 776041, "rows_sampled": 3205, "claim": "measured"},
 "columns": [{"name": "timeseries[].date", "type": "string date", "nullable": false, "description": "trading day", "example": "2026-10-13"}, {"name": "timeseries[].model_code", "type": "string", "nullable": false, "description": "model", "example": "INT"}, {"name": "timeseries[].model_return", "type": "float", "nullable": true, "description": "daily model-design return", "example": 0.0012}, {"name": "timeseries[].benchmark_return / index_benchmark_return / etf_benchmark_return", "type": "float", "nullable": true, "description": "daily benchmark returns", "example": 0.0011}, {"name": "timeseries[].rfr", "type": "float", "nullable": true, "description": "risk-free rate", "example": 0.0001}, {"name": "rfr_tenors.<model>", "type": "string", "nullable": false, "description": "RFR tenor per model", "example": "<tenor>"}, {"name": "series_note", "type": "string", "nullable": false, "description": "says these are model-design returns", "example": "<text>"}],
 "enums": {"model_code": ["UST", "ST", "INT", "LT", "ULT"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["model return series", "daily returns", "sharpe", "drawdown", "volatility", "capture ratio"],
 "common_queries": ["What is the LT model's 1-year volatility and Sharpe?", "Plot the INT model vs its benchmark since inception"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mp.04)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.benchmarks_and_models.artifacts[mp.04]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.04",
 "open_items": ["MODEL-DESIGN returns caveat travels with every figure"],
 "evidence": [{"read": "head+get json/benchmarks/model_portfolio_timeseries.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/etf_returns", "bucket": "opal-data-portal-v2", "s3_prefix": "json/benchmarks/etf_returns.json", "layer": "served", "format": "json", "table": "etf_returns",
 "grain": "one object; per benchmark ETF x period (9 periods)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-etf-returns (ProcessModelPKLOnly branch)", "schedule": "daily 11:06Z", "claim": "measured (rectangle mp.06)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 1282, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "etfs.<ticker>.{name,asset_class,returns}", "type": "object", "nullable": false, "description": "period returns of the benchmark ETF", "example": "AGG"}, {"name": "periods", "type": "list[string]", "nullable": false, "description": "period labels", "example": "YTD"}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date", "example": "2026-10-13"}],
 "enums": {"ticker": ["BIL", "VGSH", "AGG", "IVV", "ACWI"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["ETF benchmark returns", "AGG return", "IVV return", "investable benchmark"],
 "common_queries": ["What did AGG return YTD?", "What did the ETF benchmarks do this quarter?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mp.06)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.benchmarks_and_models.artifacts[mp.06]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.06", "open_items": [],
 "evidence": [{"read": "head+get json/benchmarks/etf_returns.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/benchmark_returns", "bucket": "opal-data-portal-v2", "s3_prefix": "json/benchmarks/benchmark_returns.json", "layer": "served", "format": "json", "table": "benchmark_returns",
 "grain": "one object; per model benchmark x period (10), with benchmark compositions in words", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-model-portfolio-benchmarks", "schedule": "daily 11:06Z", "claim": "measured (rectangle mp.08)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 13000, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "benchmark_compositions.<model>", "type": "string", "nullable": false, "description": "what each benchmark is, in words", "example": "<composition text>"}, {"name": "models / model_names / periods / inception_date / source", "type": "mixed", "nullable": false, "description": "index-leg period returns", "example": "{...}"}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date", "example": "2026-10-13"}],
 "enums": {"model": ["UST", "ST", "INT", "LT", "ULT"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["benchmark composition", "what is the benchmark", "index benchmark returns"],
 "common_queries": ["What is the UST model's benchmark made of?"],
 "existing_gateway_tool": {"name": "none (row mp.08 is deny + pending-andrew)", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.benchmarks_and_models.artifacts[mp.08]; held_at_andrew", "present": true},
 "prior_art": "rectangle.final.certified.json mp.08",
 "open_items": ["Held at Andrew; 0 page callers (getBenchmarkReturns defined, never called)"],
 "evidence": [{"read": "head+get json/benchmarks/benchmark_returns.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/smartx_model_performance", "bucket": "opal-data-portal-v2", "s3_prefix": "json/benchmarks/_smartx_model_{daily,monthly}.json", "layer": "served", "format": "json", "table": "_smartx_model_daily + _smartx_model_monthly",
 "grain": "daily: per model x trading day; monthly: per model x 7 periods", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "data/smartx/scripts/pull_smartx_model_monthly_performance.py --upload (operator-run)", "schedule": "manual; last run 2026-06-01", "claim": "measured (rectangle mp.09-10)"},
 "freshness": {"latest_partition": "2026-05-29", "field": "as_of_date / as_of_month", "lag_trading_days": 94, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 2, "bytes": 254605, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "models", "type": "object (5)", "nullable": false, "description": "SmartX-reported model performance", "example": "{...}"}, {"name": "as_of_date | as_of_month", "type": "string", "nullable": false, "description": "vendor as-of", "example": "2026-05-29"}, {"name": "schema, source, cadence, return_units, model_source_label, periods, period_definitions", "type": "mixed", "nullable": true, "description": "metadata", "example": "<text>"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": ["smartx"]}},
 "nl_tags": ["smartx model performance", "vendor reported returns"],
 "common_queries": ["What does SmartX report for the models? (DENY: frozen)"],
 "existing_gateway_tool": {"name": "none (rows mp.09-10 deny)", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.benchmarks_and_models.artifacts[mp.09, mp.10]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.09, mp.10",
 "open_items": ["UNRESOLVED since certification: retired vs silently stopped (opposite remedies)"],
 "evidence": [{"read": "head+get both keys", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/peer_performance", "bucket": "opal-data-portal-v2", "s3_prefix": "json/peers/peer_performance.json", "layer": "served", "format": "json", "table": "peer_performance",
 "grain": "one object; per model x 6 periods vs peer group", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-peer-performance (peer_excel branch)", "schedule": "monthly, on the peer Excel upload", "claim": "measured (rectangle mp.07)"},
 "freshness": {"latest_partition": "2026-09-30", "field": "data_as_of", "lag_trading_days": 9, "basis": "trading-day-frontier (monthly; healthy)", "claim": "measured"},
 "size": {"objects": 1, "bytes": 8531, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "models.<code>.{code,name,periods}", "type": "object", "nullable": false, "description": "model vs peer stats per period", "example": "LTA"}, {"name": "periods", "type": "list[string]", "nullable": false, "description": "6 periods", "example": "1Y"}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "month-end", "example": "2026-09-30"}],
 "enums": {"model": ["UST", "INT", "ST", "LTC", "LTA"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["peer comparison", "peer rank", "vs peers", "percentile rank"],
 "common_queries": ["How does the INT model rank against peers over 1 year?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mp.07)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.peers.artifacts[mp.07]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.07",
 "open_items": ["Model code set differs from the Yang family (LTC/LTA vs LT/ULT): a tool must not join on code"],
 "evidence": [{"read": "head+get json/peers/peer_performance.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/cma_assumptions", "bucket": "opal-data-portal-v2", "s3_prefix": "json/capital-markets/assumptions.json", "layer": "served", "format": "json", "table": "assumptions",
 "grain": "one row per asset class (27)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-cma (cma_excel-gated)", "schedule": "on the annual CMA Excel upload", "claim": "measured (rectangle cma.01)"},
 "freshness": {"latest_partition": "2026 (year edition)", "field": "data_as_of", "lag_trading_days": null, "basis": "annual edition; not a trading-day series", "claim": "measured"},
 "size": {"objects": 1, "bytes": 4146, "rows_sampled": 27, "claim": "measured"},
 "columns": [{"name": "assumptions[].assetClass", "type": "string", "nullable": false, "description": "asset class", "example": "US Large Cap"}, {"name": "assumptions[].expectedReturn", "type": "number", "nullable": false, "description": "forward expected return", "example": 0.06}, {"name": "assumptions[].expectedVolatility", "type": "number", "nullable": false, "description": "forward volatility", "example": 0.15}, {"name": "assumptions[].category", "type": "string", "nullable": false, "description": "group", "example": "Equity"}, {"name": "data_as_of", "type": "string (year)", "nullable": false, "description": "edition year", "example": "2026"}, {"name": "source_file, pipeline_execution_id, generated_at", "type": "string", "nullable": false, "description": "provenance", "example": "<file>"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["capital market assumptions", "CMA", "expected returns", "long term assumptions"],
 "common_queries": ["What is our long-term expected return for US equities?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row cma.01)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.capital_markets.artifacts[cma.01]", "present": true},
 "prior_art": "rectangle.final.certified.json cma.01",
 "open_items": ["FORECASTS, not realized; quote the YEAR, never the footer's 2026-12-31"],
 "evidence": [{"read": "head+get json/capital-markets/assumptions.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/cma_views", "bucket": "opal-data-portal-v2", "s3_prefix": "json/capital-markets/views.json", "layer": "served", "format": "json", "table": "views",
 "grain": "3 view blocks (overall, fixed income, equity), 3 entries each", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-cma", "schedule": "on CMA upload; none since 2026-01-09", "claim": "measured (rectangle cma.02)"},
 "freshness": {"latest_partition": "2026-01-09", "field": "data_as_of", "lag_trading_days": 190, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 5992, "rows_sampled": 9, "claim": "measured"},
 "columns": [{"name": "overall_views / fixed_income_views / equity_views", "type": "list or map (3)", "nullable": false, "description": "tactical over/underweight stances", "example": "<view text>"}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "strike date", "example": "2026-01-09"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["house view", "tactical views", "market views", "overweight", "underweight"],
 "common_queries": ["What is the house view on fixed income?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row cma.02)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.capital_markets.artifacts[cma.02]", "present": true},
 "prior_art": "rectangle.final.certified.json cma.02",
 "open_items": ["190 TD old with no refresh: state the strike date loudly; footer shows a different artifact's date"],
 "evidence": [{"read": "head+get json/capital-markets/views.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/correlation_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/correlations/correlation_data.json", "layer": "served", "format": "json", "table": "correlation_data",
 "grain": "59 x 59 matrix per window (1M, 3M, 6M, 1Y, 2Y)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-correlation", "schedule": "daily 11:06Z", "claim": "measured (rectangle cor.01)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 152549, "rows_sampled": 59, "claim": "measured"},
 "columns": [{"name": "tickers", "type": "list[string] (59)", "nullable": false, "description": "row/column order", "example": "<ticker>"}, {"name": "correlations.<window>.matrix", "type": "list[list[float]]", "nullable": false, "description": "pairwise correlations", "example": 0.42}, {"name": "correlations.<window>.data_points", "type": "int", "nullable": false, "description": "sample size n", "example": 21}, {"name": "metadata.{generated_at,ticker_count,periods_available}", "type": "object", "nullable": false, "description": "provenance", "example": "{...}"}],
 "enums": {"window": ["1M", "3M", "6M", "1Y", "2Y"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["correlation", "diversification", "stock bond correlation", "correlation matrix"],
 "common_queries": ["What is the 1Y correlation between US equities and Treasuries?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row cor.01)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_correlation", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "a": "ticker", "b": "ticker", "window": "1M|3M|6M|1Y|2Y"}, "returns": "r, window, n, data_as_of", "answers": ["What is the 1Y correlation between US equities and Treasuries?"]}],
 "catalog_entry": {"data_catalog_key": "channels.correlations_factors.artifacts[cor.01]", "present": true},
 "prior_art": "rectangle.final.certified.json cor.01 + SEMANTICS_CVO_PLANE_BC_correction1.json",
 "open_items": ["Always quote window and n"],
 "evidence": [{"read": "head+get json/correlations/correlation_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/factor_tilts", "bucket": "opal-data-portal-v2", "s3_prefix": "json/factor-tilts/{tier1-snapshot,tier2-spreads,tier3-timeseries}.json", "layer": "served", "format": "json", "table": "factor_tilts (3 co-emitted tiers)",
 "grain": "tier1: model x window x factor snapshot; tier2: factor spreads; tier3: time series (14,915 model-tilt points)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-factor-tilts", "schedule": "daily 11:06:02Z, one write second for all three", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 3, "bytes": 4195904, "rows_sampled": 14915, "claim": "measured"},
 "columns": [{"name": "summary[].{model,window,r2,alpha,factors}", "type": "list (25)", "nullable": false, "description": "tier1 regression summary", "example": "INT 1Y"}, {"name": "factorTiltsByWindow.<window>.<model>", "type": "object (6 factors)", "nullable": false, "description": "tier1 tilts", "example": "{...}"}, {"name": "aggregateTilts.<window>", "type": "object", "nullable": false, "description": "book-level tilt per factor pair", "example": "Growth vs Value"}, {"name": "factorSpreads", "type": "object (6)", "nullable": false, "description": "tier2 spread per factor", "example": "{...}"}, {"name": "timeSeries / modelTiltTimeSeries", "type": "object / list", "nullable": false, "description": "tier3 history (4 MB: project)", "example": "[...]"}],
 "enums": {"window": ["1M", "2M", "3M", "6M", "1Y"], "factor": ["Equity vs FI", "Growth vs Value", "US vs Foreign", "Large vs Small", "Agg vs Short", "HY vs Agg"], "model": ["UST", "ST", "INT", "LT", "ULT"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["factor tilts", "growth vs value", "large vs small", "style tilt", "factor exposure"],
 "common_queries": ["Is the LT model tilted toward growth or value over 6 months?", "How has the book's US vs foreign tilt moved?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (rows ft.01-03)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.correlations_factors.artifacts[ft.01-03]", "present": true},
 "prior_art": "rectangle.final.certified.json ft.01-03",
 "open_items": ["Catalog link ft.04 (json/portfolios/aum-metrics.json) should be re-ruled deny: frozen 58 TD, no page reads it"],
 "evidence": [{"read": "head+get all 3 keys", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/macro_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/macro/macro_data.json (+ macro_data_fred.json)", "layer": "served", "format": "json", "table": "macro_data",
 "grain": "12 indicator groups -> indicators (macro_data); 9 groups (macro_data_fred)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-macro (macro_data); FRED producer (macro_data_fred)", "schedule": "daily 11:06Z; FRED 23:31Z", "claim": "measured (rectangle mac.01) / inferred (fred)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier; macro_data_fred data_as_of 2026-09-01 (29 TD, monthly series)", "claim": "measured"},
 "size": {"objects": 2, "bytes": 273723, "rows_sampled": 12, "claim": "measured"},
 "columns": [{"name": "groups[].{category,count,indicators}", "type": "list", "nullable": false, "description": "indicator values by category", "example": "Inflation"}, {"name": "year", "type": "int", "nullable": false, "description": "heatmap year", "example": 2026}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "file strike date, not each indicator's reference period", "example": "2026-10-13"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["macro indicators", "inflation", "employment", "GDP", "macro heatmap"],
 "common_queries": ["What is the latest CPI reading?", "Show the macro heatmap categories"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mac.01)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_macro", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "indicator": "name or slug"}, "returns": "indicator value + its own reference date + file data_as_of", "answers": ["What is the latest CPI reading?"]}],
 "catalog_entry": {"data_catalog_key": "channels.macro_rates.artifacts[mac.01]; macro_data_fred has no row", "present": true},
 "prior_art": "rectangle.final.certified.json mac.01",
 "open_items": ["Duplicate output path: top-level macro/macro_data.json is ALSO written today (same 197,329 bytes, 11:06:01Z) -- not URL-reachable; CLAUDE.md NEVER duplicate output path"],
 "evidence": [{"read": "head+get json/macro/macro_data.json, json/macro/macro_data_fred.json, macro/macro_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/macro_timeseries", "bucket": "opal-data-portal-v2", "s3_prefix": "json/macro/timeseries/{slug}.json", "layer": "served", "format": "json (gzip)", "table": "macro timeseries family (79 members)",
 "grain": "one object per indicator slug; one point per observation", "partition": {"keys": ["slug"], "claim": "measured"},
 "producer": {"name": "yang-generate-macro-timeseries", "schedule": "daily 11:06:00-09Z", "claim": "measured (rectangle mac.02)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "as_of", "lag_trading_days": 0, "basis": "trading-day-frontier (sample 10y)", "claim": "measured (1 member read)"},
 "size": {"objects": 79, "bytes": 151702, "rows_sampled": 442, "claim": "measured"},
 "columns": [{"name": "indicator", "type": "string", "nullable": false, "description": "indicator name", "example": "10Y"}, {"name": "as_of", "type": "string date", "nullable": false, "description": "series end", "example": "2026-10-13"}, {"name": "data[]", "type": "list", "nullable": false, "description": "observations", "example": "442 points"}, {"name": "stats", "type": "object (5)", "nullable": false, "description": "summary stats", "example": "{...}"}],
 "enums": {"slug": ["79 members; e.g. 10y, 1m, 1y, 20y, 2y"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["indicator history", "time series", "treasury yield history", "macro series"],
 "common_queries": ["Show the 10-year Treasury yield history"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mac.02, family axis slug)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_macro", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "indicator": "slug"}, "returns": "series + stats + as_of", "answers": ["Show the 10-year Treasury yield history"]}],
 "catalog_entry": {"data_catalog_key": "channels.macro_rates.artifacts[mac.02] (declared_members 79)", "present": true},
 "prior_art": "rectangle.final.certified.json mac.02",
 "open_items": ["Catalog paths.tenor_series says 84 objects and portal_lookup.py says 84; measured 79"],
 "evidence": [{"read": "list json/macro/timeseries/ (79 of 79) + get 10y.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/volatility_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/macro/volatility_data.json (+ vix_data.json)", "layer": "served", "format": "json", "table": "volatility_data",
 "grain": "VIX and MOVE: current, percentiles, history, regime", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "opal-portal-volatility-fetcher", "schedule": "midday, written 12:30:36Z", "claim": "measured (rectangle mac.03)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 2, "bytes": 2249781, "rows_sampled": 8836, "claim": "measured (vix_data historical 8,836)"},
 "columns": [{"name": "vix.current.{current,regime,percentile,change1D,change1W,change1M}", "type": "object", "nullable": false, "description": "VIX snapshot", "example": 17.2}, {"name": "move.current.*", "type": "object", "nullable": false, "description": "MOVE snapshot", "example": 95.0}, {"name": "vix|move.{percentiles,historical,ai_summary}", "type": "mixed", "nullable": true, "description": "distribution, history, generated text", "example": "<text>"}, {"name": "regimes / regime_colors", "type": "object", "nullable": false, "description": "regime thresholds", "example": "Elevated"}],
 "enums": {"regime": ["Low", "Normal", "Elevated", "High", "Extreme"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["VIX", "MOVE index", "volatility regime", "implied volatility"],
 "common_queries": ["What is the VIX and what regime is it in?", "Where is MOVE versus its history?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mac.03)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_macro", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "indicator": "vix|move"}, "returns": "current, regime, percentile, data_as_of", "answers": ["What is the VIX and what regime is it in?"]}],
 "catalog_entry": {"data_catalog_key": "channels.macro_rates.artifacts[mac.03]", "present": true},
 "prior_art": "rectangle.final.certified.json mac.03",
 "open_items": ["NAME THE KEY: frozen twin json/yang/volatility_data.json (187 TD) shares the basename", "vix_data.json has 0 page callers"],
 "evidence": [{"read": "head+get json/macro/volatility_data.json, json/macro/vix_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/yield_curve_fred", "bucket": "opal-data-portal-v2", "s3_prefix": "json/macro/yield_curve_fred.json", "layer": "served", "format": "json", "table": "yield_curve_fred",
 "grain": "10 Treasury tenors x 497 observations", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "FRED yield-curve producer", "schedule": "daily 23:01Z", "claim": "measured (rectangle mac.04: name not given) / inferred schedule"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 672088, "rows_sampled": 497, "claim": "measured"},
 "columns": [{"name": "US Treasury {1M,3M,1Y,2Y,3Y,5Y,7Y,10Y,20Y,30Y}", "type": "list (497 each)", "nullable": false, "description": "yield history per tenor", "example": "4.05"}, {"name": "series / preserved_tenors / source", "type": "mixed", "nullable": true, "description": "metadata", "example": "FRED"}, {"name": "data_as_of", "type": "string date", "nullable": false, "description": "data date", "example": "2026-10-13"}],
 "enums": {"tenor": ["1M", "3M", "1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "20Y", "30Y"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["yield curve", "treasury yields", "2s10s", "curve inversion"],
 "common_queries": ["Is the 2s10s curve inverted?", "Where was the 10-year a year ago?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mac.04)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_macro", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "date within series", "indicator": "tenor"}, "returns": "yield(s) at date + data_as_of", "answers": ["Is the 2s10s curve inverted?"]}],
 "catalog_entry": {"data_catalog_key": "channels.macro_rates.artifacts[mac.04]", "present": true},
 "prior_art": "rectangle.final.certified.json mac.04", "open_items": [],
 "evidence": [{"read": "head+get json/macro/yield_curve_fred.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/valuation_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/valuation/valuation_data.json", "layer": "served", "format": "json", "table": "valuation_data",
 "grain": "39 indices: summary multiples, historical ranges, time series", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-valuation", "schedule": "daily 11:06Z", "claim": "measured (rectangle val.01)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 2198978, "rows_sampled": 39, "claim": "measured"},
 "columns": [{"name": "summary[].{index,fwd_pe,trailing_pe,p_fcf,ev_sales,p_b,p_sales,div_yield}", "type": "list (39)", "nullable": true, "description": "current multiples", "example": "S&P 500"}, {"name": "ranges.<index>", "type": "list (7 x 9 fields)", "nullable": false, "description": "historical range per metric", "example": "{...}"}, {"name": "time_series.<index>.{trailing_pe,fwd_pe,p_b}", "type": "object", "nullable": false, "description": "history (2.2 MB: project one index)", "example": "{...}"}],
 "enums": {"index": ["39 members, e.g. S&P 500, Nasdaq, Russell 2000, MSCI USA Value"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["valuation", "P/E", "forward PE", "expensive vs history", "multiples"],
 "common_queries": ["What is the S&P 500 forward P/E versus its range?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row val.01)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_valuation", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "index": "one of 39", "metric": "fwd_pe|trailing_pe|p_b|..."}, "returns": "current value, range, percentile, data_as_of", "answers": ["What is the S&P 500 forward P/E versus its range?"]}],
 "catalog_entry": {"data_catalog_key": "channels.valuation.artifacts[val.01]", "present": true},
 "prior_art": "rectangle.final.certified.json val.01",
 "open_items": ["Frozen twins: valuation/valuation_data.json (196 TD) and json/valuations/valuation-data.json (2025-12-26)"],
 "evidence": [{"read": "head+get json/valuation/valuation_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/risk_premium_data", "bucket": "opal-data-portal-v2", "s3_prefix": "json/valuation/risk_premium_data.json", "layer": "served", "format": "json", "table": "risk_premium_data",
 "grain": "ERP monthly series (442) and IG/HY OAS daily series (786)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang-generate-risk-premium", "schedule": "daily 11:05Z", "claim": "measured (rectangle val.02)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 145523, "rows_sampled": 1228, "claim": "measured"},
 "columns": [{"name": "erp.{data[],thresholds}", "type": "object", "nullable": false, "description": "equity risk premium history", "example": "4 fields per point"}, {"name": "credit.{ig,hy}.{data[],thresholds,current_oas_pct,current_oas_bps}", "type": "object", "nullable": false, "description": "credit spreads", "example": 310}, {"name": "data_source.{erp,credit_spreads}, note", "type": "string", "nullable": true, "description": "provenance", "example": "<text>"}],
 "enums": {"credit": ["ig", "hy"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["equity risk premium", "ERP", "credit spreads", "high yield OAS", "IG spread"],
 "common_queries": ["Where are high-yield spreads today in bps?", "Is the equity risk premium below average?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row val.02)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_valuation", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "index": "erp|ig|hy"}, "returns": "current, thresholds, data_as_of", "answers": ["Where are high-yield spreads today in bps?"]}],
 "catalog_entry": {"data_catalog_key": "channels.valuation.artifacts[val.02]", "present": true},
 "prior_art": "rectangle.final.certified.json val.02", "open_items": ["A spread moves on either leg: name the leg"],
 "evidence": [{"read": "head+get json/valuation/risk_premium_data.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/market_overview_tiered", "bucket": "opal-data-portal-v2", "s3_prefix": "json-tiered/market-overview/{summary/all-returns.json, rsi-summary.json, rsi-details-{equities,fixedIncome,commodities}.json, timeseries/{ticker}.json, details/{ticker}.json}", "layer": "served", "format": "json", "table": "market overview (tiered)",
 "grain": "summary: one row per index (71); rsi: per asset class; timeseries/details: one object per ticker", "partition": {"keys": ["ticker (timeseries, details)"], "claim": "measured"},
 "producer": {"name": "tiered market-overview summary producer", "schedule": "daily 11:06:54-11:07:01Z", "claim": "measured (rectangle mkt.01, name unstated) / inferred schedule"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of / as_of_date", "lag_trading_days": 0, "basis": "trading-day-frontier; timeseries 84 of 157 and details 71 of 213 written today, the rest frozen 2026-01-13..02-26 (188 TD)", "claim": "measured"},
 "size": {"objects": 375, "bytes": 37061635, "rows_sampled": 71, "claim": "measured"},
 "columns": [{"name": "indices[].{ticker,ticker_id,name,entity_type,asset_class,latest_price,latest_date,period_returns}", "type": "list (71)", "nullable": false, "description": "index period returns", "example": "Bloomberg Aggregate"}, {"name": "rsi_summary / indices / sectors / aggregate", "type": "object", "nullable": false, "description": "RSI by asset class", "example": "{...}"}, {"name": "timeseries: {ticker,ticker_id,entity_type,data_points,start_date,end_date,historical_prices}", "type": "object", "nullable": false, "description": "price history", "example": "62 points (10Y)"}],
 "enums": {"asset_class_file": ["equities", "fixedIncome", "commodities"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["market returns", "index returns", "sector returns", "RSI", "overbought oversold", "price history"],
 "common_queries": ["What did the Bloomberg Aggregate return YTD?", "Which sectors are overbought on RSI?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row mkt.01, summary only)", "verdict": "extend"},
 "proposed_tools": [{"name": "portal_get_market_returns", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "ticker": "name or ticker", "period": "label"}, "returns": "period return or price series with as_of_date", "answers": ["What did the Bloomberg Aggregate return YTD?"]}],
 "catalog_entry": {"data_catalog_key": "channels.market_regime_trending.artifacts[mkt.01] (summary only)", "present": true},
 "prior_art": "rectangle.final.certified.json mkt.01",
 "open_items": ["CATALOG CONTRADICTION: never_serve lists json-tiered/ as frozen (01-13) while mkt.01 serves it; measured live today", "Mixed-vintage families: a per-ticker tool must check each member's own date (142 details + 73 timeseries frozen)", "Live CF behavior /json-tiered/* -> portal-v2 carries NO edge auth Lambda (measured config; not exercised)"],
 "evidence": [{"read": "list json-tiered/ (375); head+get summary, rsi-summary, rsi-details-commodities, timeseries/10Y, details/10Y", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/market_regime", "bucket": "opal-data-portal-v2", "s3_prefix": "json/market/market-regime.json (+ market-regime-history.json)", "layer": "served", "format": "json", "table": "market_regime",
 "grain": "current regime + 4 signals + 106-point history; history file 1,065 regime points", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "market regime producer (co-written with the tiered market overview)", "schedule": "daily 11:07Z", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 2, "bytes": 741896, "rows_sampled": 1065, "claim": "measured"},
 "columns": [{"name": "regime / description / triggeredBy", "type": "string", "nullable": false, "description": "current regime", "example": "risk-on"}, {"name": "signals.{momentum,volatility,correlation,rateRegime}.{value,label,change,breakdown}", "type": "object", "nullable": false, "description": "regime signals", "example": "{...}"}, {"name": "history[].{date,regime,confidence}", "type": "list (106)", "nullable": false, "description": "recent regime path", "example": "2026-10-13"}, {"name": "periodStats / regimeThresholds / tickerDates / sharedTradingDays", "type": "mixed", "nullable": false, "description": "context", "example": "{...}"}],
 "enums": {"regime": ["risk-on", "risk-off", "volatile", "rotation", "neutral"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["market regime", "risk on risk off", "regime signals"],
 "common_queries": ["What market regime are we in and why?", "How long has the regime held?"],
 "existing_gateway_tool": {"name": "none (channel market_regime_trending names the path; no artifact row)", "verdict": "extend"},
 "proposed_tools": [{"name": "portal_get_market_regime", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest"}, "returns": "regime, signals, history tail, data_as_of", "answers": ["What market regime are we in and why?"]}],
 "catalog_entry": {"data_catalog_key": "channels.market_regime_trending.paths.regime (no artifact row)", "present": false},
 "prior_art": "none certified", "open_items": ["Needs a catalog artifact row"],
 "evidence": [{"read": "head+get json/market/market-regime.json, market-regime-history.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/market_all_returns_legacy", "bucket": "opal-data-portal-v2", "s3_prefix": "json/market/all_returns.json", "layer": "served", "format": "json", "table": "all_returns (fallback leg)",
 "grain": "one entry per ticker (84)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "NOT DETERMINED (April cohort)", "schedule": "none since 2026-04-15", "claim": "measured (rectangle mkt.02)"},
 "freshness": {"latest_partition": "2026-04-10", "field": "data_as_of", "lag_trading_days": 128, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 35648, "rows_sampled": 84, "claim": "measured"},
 "columns": [{"name": "tickers", "type": "object (84)", "nullable": false, "description": "per-ticker returns", "example": "{...}"}, {"name": "data_as_of, as_of_date, generated_at, cache_until, count", "type": "string/int", "nullable": false, "description": "vintage fields", "example": "2026-04-10"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["legacy market returns"],
 "common_queries": ["(DENY: frozen 128 TD; answer from market_overview_tiered)"],
 "existing_gateway_tool": {"name": "none (row mkt.02 deny)", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.market_regime_trending.artifacts[mkt.02]; never_serve", "present": true},
 "prior_art": "rectangle.final.certified.json mkt.02",
 "open_items": ["Refresh-or-retire proposal from certification still unanswered; fallback leg still in portal market.ts"],
 "evidence": [{"read": "head+get json/market/all_returns.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/sentiment_singletons", "bucket": "opal-data-portal-v2", "s3_prefix": "json/sentiment/{fear-greed-index,keyword-sentiments}.json", "layer": "served", "format": "json", "table": "fear_greed_index + keyword_sentiments",
 "grain": "fear-greed: current + 251-day history; keyword-sentiments: 44 keywords", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "opal-portal-fear-greed-fetcher (S3_KEY env = json/sentiment/fear-greed-index.json); keyword-sentiments writer inferred keyword-intelligence-generator / news pipeline", "schedule": "fear-greed 21:30Z; keywords 11:18Z", "claim": "measured (fear-greed env) / inferred (keywords)"},
 "freshness": {"latest_partition": "2026-10-13 (fear-greed generated 2026-10-13T21:30Z); keywords generated 2026-10-14T11:18Z", "field": "generated_at (no data_as_of field)", "lag_trading_days": 0, "basis": "trading-day-frontier on generated_at date", "claim": "measured"},
 "size": {"objects": 2, "bytes": 420638, "rows_sampled": 295, "claim": "measured"},
 "columns": [{"name": "current.{value,description,last_update,previous_close,previous_1_week,previous_1_month,previous_1_year,components}", "type": "object", "nullable": false, "description": "fear and greed now", "example": 55}, {"name": "historical[].{date,value,description}", "type": "list (251)", "nullable": false, "description": "history", "example": "Greed"}, {"name": "keywords[].{keyword,sentiment,sentiment_raw,voters,count,rank,direction_judged,direction_reason,bullish,bearish,neutral,articles}", "type": "list (44)", "nullable": true, "description": "keyword sentiment", "example": "<keyword>"}],
 "enums": {"fear_greed_scale": ["extreme_fear", "fear", "neutral", "greed", "extreme_greed"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market/news data", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["fear and greed", "market sentiment", "keyword sentiment", "news sentiment"],
 "common_queries": ["What is the fear and greed index today?", "Which keywords are most bearish this week?"],
 "existing_gateway_tool": {"name": "gateway_query_catalog (row news.03.live-singletons)", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.sentiment_news_mood.artifacts[fear-greed-index + keyword-sentiments]", "present": true},
 "prior_art": "workflows/atom_decomposition/runs/news-subsystem/ (G6)",
 "open_items": ["No data_as_of field: vintage is generated_at", "news-trending-analysis env S3_KEY points at top-level sentiment/keyword-sentiments.json (frozen 2026-01-08): a writer env names a dead key"],
 "evidence": [{"read": "head+get both keys; lambda list_functions env scan", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/keyword_history", "bucket": "opal-data-portal-v2", "s3_prefix": "json/sentiment/keyword-history-{articles,summary}/{keyword}.json", "layer": "served", "format": "json", "table": "keyword history family (2 x 360)",
 "grain": "one object per keyword per family", "partition": {"keys": ["keyword"], "claim": "measured"},
 "producer": {"name": "opal-keyword-drilldown-generator (env S3_BUCKET_PORTAL)", "schedule": "none since 2026-04-07", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-04-07", "field": "LastModified", "lag_trading_days": 131, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 720, "bytes": 2955966, "rows_sampled": 0, "claim": "measured (list only)"},
 "columns": [], "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["keyword history"], "common_queries": ["(DENY: frozen)"],
 "existing_gateway_tool": {"name": "none (rows deny)", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.sentiment_news_mood.artifacts[keyword-history-*]", "present": true},
 "prior_art": "none certified", "open_items": ["Accessors exist in sentiment.ts with 0 callers; catalog declared_members 360 matches"],
 "evidence": [{"read": "list json/sentiment/ (722)", "at": "2026-10-14T12:55:42Z"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/trending_latest", "bucket": "opal-data-portal-v2", "s3_prefix": "json/trending/latest.json", "layer": "served", "format": "json", "table": "trending_latest",
 "grain": "10 bullish + 10 bearish news topics for one date", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "opal-trending-topics-portal-publisher (per portal features.ts) from DynamoDB opal-news-trending-daily", "schedule": "daily 11:21Z", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-14", "field": "data_as_of / date", "lag_trading_days": 0, "basis": "same-day news (ahead of T-1 by design)", "claim": "measured"},
 "size": {"objects": 1, "bytes": 93766, "rows_sampled": 20, "claim": "measured"},
 "columns": [{"name": "bullish[] / bearish[].{topic,subtext,context,article_count,sentiment_bull_bear,sentiment_confidence_fear,sentiment_risk_appetite,sentiment_positive_negative,sentiment_emotional_intensity,top_sources,trending_rank,top_articles}", "type": "list (10 each)", "nullable": true, "description": "curated topics", "example": "<topic>"}, {"name": "date, data_as_of, generated_at", "type": "string", "nullable": false, "description": "vintage", "example": "2026-10-14"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- news", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["trending topics", "bullish news", "bearish news", "what is the market talking about"],
 "common_queries": ["What are today's top bearish news themes?"],
 "existing_gateway_tool": {"name": "none", "verdict": "extend (catalog row, or a G6 news tool)"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.market_regime_trending.paths.trending (no artifact row)", "present": false},
 "prior_art": "G6 news-subsystem",
 "open_items": ["json/semantic-trending/latest.json frozen 160 TD (flag off); json/trending/topics/{date} requested by api/trending.ts but no such keys (404)"],
 "evidence": [{"read": "head+get json/trending/latest.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/security_scanner", "bucket": "opal-data-portal-v2", "s3_prefix": "json/security_scanner/latest/{factor_metadata.json, universes/{universe}/{universe_data,scanner_data}.json}", "layer": "served", "format": "json", "table": "security scanner",
 "grain": "factor_metadata: one row per factor (289); universe/scanner: one row per security in the universe (sp500: 503)", "partition": {"keys": ["universe"], "claim": "measured"},
 "producer": {"name": "opal-security-scanner-processor (S3 ObjectCreated on security_scanner/uploads/*.xlsx)", "schedule": "manual FactSet Excel upload; last 2026-10-02", "claim": "measured (bucket notification + rectangle sscn.01)"},
 "freshness": {"latest_partition": "2026-10-02", "field": "asOf", "lag_trading_days": 7, "basis": "trading-day-frontier (monthly manual)", "claim": "measured"},
 "size": {"objects": 19, "bytes": 171568404, "rows_sampled": 792, "claim": "measured (latest/ only; 76 dated-snapshot objects not contracted)"},
 "columns": [{"name": "factors[].{code,name,category,relationship,ic,coveragePct,autocorrelationPct,assetClass,systematic}", "type": "list (289)", "nullable": true, "description": "factor catalog", "example": "<factor>"}, {"name": "securities[] / rows[].{ticker,name,mktVal,country,sector,industryGroup,universeWeight,divzWeight,price,values[,pctls]}", "type": "list", "nullable": true, "description": "per-security factor values (+ percentiles in scanner_data)", "example": "AAPL"}, {"name": "asOf, universeId, sourceUniverseColumn", "type": "string", "nullable": false, "description": "vintage + universe", "example": "sp500"}],
 "enums": {"universe_live": ["acwx", "eafe", "eafev", "r1000", "r1000v", "sp500"], "universe_orphaned": ["msciusa", "rmidcap", "sp400"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- market data (divzWeight is an Opal ETF weight)", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": ["factset"]}},
 "nl_tags": ["security scanner", "stock screen", "factor scores", "quality stocks", "DIVZ weight"],
 "common_queries": ["Which S&P 500 names score highest on quality?", "What is DIVZ's weight in names with the best momentum percentile?"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"},
 "proposed_tools": [{"name": "portal_get_security_scan", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest", "universe": "one of 6", "factor": "code", "top_n": "int"}, "returns": "ranked securities with values, percentiles and asOf (projected; objects up to 31 MB)", "answers": ["Which S&P 500 names score highest on quality?"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "rectangle.final.certified.json sscn.01-04 (24 Plane-B/C cells UNMEASURED; no analyst verdict)",
 "open_items": ["No CVO serve verdict exists (canonical_name/verdict cells null in the certified rectangle)", "Dated snapshots use two conventions (YYYY-MM-DD and YYYYMMDD)"],
 "evidence": [{"read": "get factor_metadata + sp500 universe_data/scanner_data; list json/security_scanner/", "at": "2026-10-14T13:2xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/pipeline_manifest", "bucket": "opal-data-portal-v2", "s3_prefix": "json/latest/manifest.json (+ json/latest/{data_pkl,model_pkl,attribution_excel,peer_excel,cma_excel}.json)", "layer": "served", "format": "json", "table": "pipeline manifest",
 "grain": "one entry per source input (5)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "yang pipeline (via opal-data-refresh-api trigger)", "schedule": "each data refresh, ~11:03-11:07Z", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-10-13 (data_pkl, model_pkl); 2026-09-30 (attribution, peer); 2026-12-31 label (cma)", "field": "sources.<s>.data_as_of", "lag_trading_days": 0, "basis": "trading-day-frontier for the daily sources", "claim": "measured"},
 "size": {"objects": 6, "bytes": 3545, "rows_sampled": 5, "claim": "measured"},
 "columns": [{"name": "sources.<source>.{data_as_of,timestamp,frequency,pipeline_execution_id,updated_at}", "type": "object", "nullable": false, "description": "per-input vintage", "example": "data_pkl"}, {"name": "generated_at, pipeline_execution_id, pipeline_started_at, source_count", "type": "mixed", "nullable": false, "description": "run metadata", "example": "5"}],
 "enums": {"source": ["attribution_excel", "cma_excel", "data_pkl", "model_pkl", "peer_excel"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- pipeline", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["data freshness", "as of date", "pipeline status", "last refresh"],
 "common_queries": ["As of what date is the portal's model data?", "When did the last data refresh run?"],
 "existing_gateway_tool": {"name": "opal_data_refresh_status (different object: execution record)", "verdict": "keep"},
 "proposed_tools": [{"name": "portal_get_pipeline_freshness", "inputs": {"firm": "n/a", "account_last4": "n/a", "platform": "n/a", "as_of": "latest"}, "returns": "per-source data_as_of and the run id", "answers": ["As of what date is the portal's model data?"]}],
 "catalog_entry": {"data_catalog_key": "channels.pipeline_freshness (no tool, no artifact row)", "present": false},
 "prior_art": "footer bindings in the certified rectangles",
 "open_items": ["Footers bind manifest dates, not artifact dates (certified R across 5 pages): a freshness answer must say which"],
 "evidence": [{"read": "head+get json/latest/*.json (6)", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/portfolios_legacy", "bucket": "opal-data-portal-v2", "s3_prefix": "json/portfolios/{aum-metrics,account-distribution,aum-timeseries}.json + json/portfolios/<firm>/account-distribution.json", "layer": "served", "format": "json", "table": "portfolios legacy tree",
 "grain": "enterprise-level objects plus per-firm account-size distribution", "partition": {"keys": ["firm (key segment 3, 2 of 5 objects)"], "claim": "measured"},
 "producer": {"name": "yang-generate-positioning aum leg (writer flag-disabled per ModelPortfolios.tsx:571-574) / legacy firm writer", "schedule": "none since 2026-07-27 (firm dirs 2026-05-29)", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-07-22 (aum-metrics period); 2026-07-23 (account-distribution); firm dirs 2026-05-29", "field": "period", "lag_trading_days": 58, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 5, "bytes": 313947, "rows_sampled": 450, "claim": "measured"},
 "columns": [{"name": "aum-metrics: period,last_updated,dates,total,by_model,meta", "type": "object", "nullable": false, "description": "legacy AUM", "example": "2026-07-22"}, {"name": "aum-timeseries: aggregate[],by_model,periods[],meta", "type": "object", "nullable": false, "description": "450 periods", "example": "{...}"}, {"name": "<firm>/account-distribution: firm_id,firm_name,generated_at,period,source,total,by_model", "type": "object", "nullable": false, "description": "per-firm histogram stats", "example": "49financial"}],
 "enums": {"firm_segment": ["49financial", "inflection"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 json/portfolios/<firm>/ (2 firms) + unsegmented enterprise objects (firm_id absent = opal-wide)", "values": ["49financial", "inflection", "(unsegmented)"]}, "account": {"column": "none -- aggregates", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["legacy AUM", "do not use"],
 "common_queries": ["(DENY: frozen; answer AUM from platinum/mdpf/{scope})"],
 "existing_gateway_tool": {"name": "gateway_query_catalog link ft.04.portfolios-aum-metrics", "verdict": "retire (re-rule the row to deny)"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.positioning_holdings.artifacts[json/portfolios/aum-metrics.json] (serve-with-caveat)", "present": true},
 "prior_art": "rectangle.final.certified.json att.03 / ft.04 / pos.03",
 "open_items": ["0 page readers of aum-metrics at PROD (was 3 pages)", "aum-timeseries.json still read by ModelPortfolios.tsx (frozen 57 TD; source comment claims it is served from opal-data-assets, but live CF /api/general/* routes to this bucket)", "Firm-partitioned frozen keys are URL-reachable by any authenticated user"],
 "evidence": [{"read": "head+get json/portfolios/* (3 probed); portal PROD accessor walk", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/served/model_portfolios_views", "bucket": "opal-data-portal-v2", "s3_prefix": "json/model_portfolios/views/{by_assetclass,by_period}/*.json + latest/manifest/summary.json", "layer": "served", "format": "json", "table": "model_portfolios views (frozen)",
 "grain": "one object per asset class (5) and per month (17)", "partition": {"keys": ["assetclass", "period YYYYMM"], "claim": "measured"},
 "producer": {"name": "unknown legacy writer", "schedule": "none since 2026-06-01", "claim": "absent"},
 "freshness": {"latest_partition": "202606", "field": "LastModified", "lag_trading_days": 93, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 25, "bytes": 128283594, "rows_sampled": 0, "claim": "measured (list only)"},
 "columns": [], "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "none in key path; content not read", "values": []}, "account": {"column": "not read", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "not read", "values": []}},
 "nl_tags": ["frozen model views"], "common_queries": ["(DENY: frozen; catalog never_serve)"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "never_serve", "present": true},
 "prior_art": "none", "open_items": ["202603 and 202604 objects are 4 KB and 3 KB vs 3-5 MB neighbours (likely empty months)"],
 "evidence": [{"read": "list json/model_portfolios/ (25)", "at": "2026-10-14T12:55:42Z"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_aum_metrics", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/{scope}/aum-metrics.json", "layer": "platinum", "format": "json", "table": "aum-metrics",
 "grain": "one object per scope; total + per-model AUM and 4 quarter-end snapshots", "partition": {"keys": ["scope"], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher (from opal-data-assets/portal/gold/mdpf/{scope}/aum-metrics/YYYY-MM-DD.json)", "schedule": "daily ~13:31-13:50Z", "claim": "measured (_provenance.written_by + source_keys)"},
 "freshness": {"latest_partition": "2026-10-12", "field": "period (_provenance.source_vintages)", "lag_trading_days": 1, "basis": "trading-day-frontier, read 13:29:52Z before the day's publish", "claim": "measured"},
 "size": {"objects": 4, "bytes": 23719, "rows_sampled": 31, "claim": "measured (by_model rows across 4 scopes: 7+5+12+7)"},
 "columns": [{"name": "total.{account_count,aum,model_aum,non_model_aum,q0,q1,q2,q3,series_start,tax_additive_aum}", "type": "object", "nullable": true, "description": "scope totals", "example": 123456789}, {"name": "by_model[].{model_name,aum,account_count,q0,q1,q2,q3}", "type": "list", "nullable": true, "description": "per-model AUM", "example": "<model name>"}, {"name": "dates.{q0..q3}", "type": "string date", "nullable": false, "description": "quarter-end dates", "example": "2026-09-30"}, {"name": "period, last_updated, scope, meta, non_model_assets_detail, _provenance", "type": "mixed", "nullable": true, "description": "vintage, basis definitions, provenance", "example": "2026-10-12"}],
 "enums": {"scope": ["global", "49financial", "cottonwood", "inflection"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 platinum/mdpf/<scope>/ (+ field scope); global = enterprise aggregate, NOT the sum of firm scopes", "values": ["global", "49financial", "cottonwood", "inflection"]}, "account": {"column": "none -- aggregate", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "meta.*_basis (custodian basis text)", "values": ["not enumerated"]}},
 "nl_tags": ["AUM", "firm AUM", "model AUM", "non-model assets", "account count", "quarter end AUM"],
 "common_queries": ["What is Cottonwood's total AUM as of the latest period?", "How much of 49financial's AUM is in models?"],
 "existing_gateway_tool": {"name": "mdpf_get_aum_metrics", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "portal_datasets.portal_mdpf_aum_metrics + channels.mdpf_model_portfolios[mp.01]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.01",
 "open_items": ["G4 overlap: these 4 keys are the served mirror of opal-data-assets gold"],
 "evidence": [{"read": "head+get platinum/mdpf/{4 scopes}/aum-metrics.json; head at 13:29:52Z", "at": "2026-10-14T13:29:52Z"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_account_distribution", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/{scope}/account-distribution.json", "layer": "platinum", "format": "json", "table": "account-distribution",
 "grain": "one object per scope; histogram + percentiles per model and total", "partition": {"keys": ["scope"], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher", "schedule": "daily ~13:31-13:50Z", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13 (global, 49financial, inflection); 2026-10-12 (cottonwood)", "field": "period", "lag_trading_days": 0, "basis": "trading-day-frontier; cottonwood 1 TD", "claim": "measured"},
 "size": {"objects": 4, "bytes": 39845, "rows_sampled": 38, "claim": "measured (by_model 14+5+12+7)"},
 "columns": [{"name": "total.{account_count,account_units,active_accounts_count,...}", "type": "object (12)", "nullable": true, "description": "scope account stats", "example": 1500}, {"name": "by_model.<model name>.{account_count,active_accounts_count,excluded_unfunded_count,histogram,max,mean,median,min,percentiles,std_dev,total_aum}", "type": "object", "nullable": true, "description": "per-model distribution", "example": "<model name>"}, {"name": "firm_id, firm_name, period, generated_at, basis, source, meta, _provenance", "type": "mixed", "nullable": true, "description": "vintage and provenance", "example": "global"}],
 "enums": {"scope": ["global", "49financial", "cottonwood", "inflection"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 + field firm_id", "values": ["global", "49financial", "cottonwood", "inflection"]}, "account": {"column": "none -- distribution only", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["account size distribution", "median account", "bell curve", "histogram"],
 "common_queries": ["What is the median account size in the Intermediate model at 49financial?"],
 "existing_gateway_tool": {"name": "mdpf_get_account_distribution", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "portal_datasets.portal_mdpf_account_distribution", "present": true},
 "prior_art": "rectangle.final.certified.json mp.02",
 "open_items": ["by_model keys are model display names (one names an individual-labelled model; do not echo labels verbatim to partner users without the firm filter)"],
 "evidence": [{"read": "head+get platinum/mdpf/{4 scopes}/account-distribution.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_aggregate_aua_timeseries", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/{scope}/aggregate-aua-timeseries.json", "layer": "platinum", "format": "json", "table": "aggregate-aua-timeseries",
 "grain": "one point per trading day per scope (486-495 dates since 2024-11-01), parallel arrays", "partition": {"keys": ["scope"], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher", "schedule": "daily ~13:31-13:50Z", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-12", "field": "as_of_last", "lag_trading_days": 1, "basis": "trading-day-frontier, read before the day's publish", "claim": "measured"},
 "size": {"objects": 4, "bytes": 1794070, "rows_sampled": 1962, "claim": "measured (495+486+495+486 dates)"},
 "columns": [{"name": "dates[]", "type": "list[string date]", "nullable": false, "description": "trading days", "example": "2026-10-12"}, {"name": "model_aua / non_model_aua / opal_aggregate_aua / partner_custody_total / base_excluding_tax_aua / tax_additive_aua / sma_additive_aua", "type": "list[float] (parallel)", "nullable": true, "description": "AUA legs per date", "example": 1.0e8}, {"name": "account_count_total / account_count_total_raw / count_as_of / count_basis / count_provenance / point_class / cohort_provenance / tax_coverage", "type": "list (parallel)", "nullable": true, "description": "count lineage per point", "example": "measured"}, {"name": "by_model", "type": "object (7-20 models)", "nullable": true, "description": "per-model series", "example": "{...}"}, {"name": "as_of_first, as_of_last, n_dates, firm_id, partner_name, aggregate_basis, meta, source_vintage_last, unidentified_strategies, _provenance", "type": "mixed", "nullable": true, "description": "vintage and basis", "example": "2024-11-01"}],
 "enums": {"scope": ["global", "49financial", "cottonwood", "inflection"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 + field firm_id", "values": ["global", "49financial", "cottonwood", "inflection"]}, "account": {"column": "none -- aggregate", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "aggregate_basis / meta (custodian basis)", "values": ["not enumerated"]}},
 "nl_tags": ["AUA trend", "assets under advisement", "AUA history", "growth", "net flows proxy"],
 "common_queries": ["How has Inflection's AUA moved since January?", "What was global model AUA on 2026-09-30?"],
 "existing_gateway_tool": {"name": "mdpf_get_aggregate_aua", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "portal_datasets.portal_mdpf_aggregate_aua", "present": true},
 "prior_art": "rectangle.final.certified.json mp.03",
 "open_items": ["Quote a count only with its point_class (certified caveat)", "Never sum across Schwab masters (catalog never_sum_rules)"],
 "evidence": [{"read": "head+get platinum/mdpf/{4 scopes}/aggregate-aua-timeseries.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_category_views", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/{scope}/category-views.json", "layer": "platinum", "format": "json", "table": "category-views",
 "grain": "one object per scope; 5 category nodes (Alternatives, Client, Insurance, Models, SMA) with members and AUM", "partition": {"keys": ["scope"], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher (from opal-data-assets/portal/gold/mdpf/{scope}/category-views/YYYY-MM-DD.json)", "schedule": "daily ~13:31-13:50Z", "claim": "measured (_provenance)"},
 "freshness": {"latest_partition": "2026-10-12", "field": "as_of", "lag_trading_days": 1, "basis": "trading-day-frontier, read before the day's publish", "claim": "measured"},
 "size": {"objects": 4, "bytes": 25674, "rows_sampled": 20, "claim": "measured"},
 "columns": [{"name": "nodes.<category>.{aum,display_label,members}", "type": "object (5)", "nullable": true, "description": "AUA by category", "example": "Models"}, {"name": "sums.{gold_plane,insurance_excluded,total_aua,view_plane}", "type": "object", "nullable": false, "description": "reconciliation sums", "example": 1.0e8}, {"name": "view_plane.{excluded,peers}", "type": "object", "nullable": false, "description": "what the view leaves out", "example": "Insurance"}, {"name": "taxsma_coverage.{covered_accounts,expected_accounts,freshness,value_status,...}", "type": "object (17)", "nullable": true, "description": "tax-SMA coverage (absent on inflection)", "example": "{...}"}, {"name": "as_of, scope, scope_note, scope_set, schema_version, taxsma_contract_version, firm_id, _provenance", "type": "mixed", "nullable": true, "description": "vintage and scope", "example": "1.0"}],
 "enums": {"scope": ["global", "49financial", "cottonwood", "inflection"], "category": ["Alternatives", "Client", "Insurance", "Models", "SMA"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 + fields scope/firm_id", "values": ["global", "49financial", "cottonwood", "inflection"]}, "account": {"column": "none -- aggregate", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["AUA by category", "SMA assets", "insurance assets", "models vs SMA", "category mix"],
 "common_queries": ["How is 49financial's AUA split between Models, SMA and Client assets?"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"},
 "proposed_tools": [{"name": "mdpf_get_category_views", "inputs": {"firm": "scope (one of 4)", "account_last4": "n/a", "platform": "n/a", "as_of": "latest; must equal as_of or no data"}, "returns": "category AUA, sums, exclusions and as_of", "answers": ["How is 49financial's AUA split between Models, SMA and Client assets?"]}],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "none certified; ModelPortfolios.tsx (PROD) reads it via getCategoryViewsByFirm",
 "open_items": ["New since certification; needs a catalog row (family axis scope, 4 members) before the tool", "G4 overlap: mirror of opal-data-assets gold"],
 "evidence": [{"read": "head+get platinum/mdpf/{4 scopes}/category-views.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_non_model_assets", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/global/non-model-assets.json", "layer": "platinum", "format": "json", "table": "non-model-assets",
 "grain": "latest + 498-point time series of enterprise non-model AUM (global only)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher", "schedule": "daily", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-12", "field": "_provenance.source_vintages", "lag_trading_days": 1, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 100081, "rows_sampled": 498, "claim": "measured"},
 "columns": [{"name": "latest", "type": "object (5)", "nullable": false, "description": "latest split", "example": "{...}"}, {"name": "time_series[]", "type": "list (498)", "nullable": false, "description": "history", "example": "{...}"}, {"name": "meta, generated_at, _provenance", "type": "mixed", "nullable": true, "description": "provenance", "example": "<text>"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 = global only (enterprise aggregate)", "values": ["global"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["non-model assets"], "common_queries": ["(DENY: superseded by aggregate-aua-timeseries.non_model_aua)"],
 "existing_gateway_tool": {"name": "none (row mp.11 deny)", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.mdpf_model_portfolios.artifacts[mp.11]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.11",
 "open_items": ["Portal getNonModelAssets now called by ModelPortfolios.tsx but targets absent json/portfolios/non_model_assets.json (404 every call)"],
 "evidence": [{"read": "head+get platinum/mdpf/global/non-model-assets.json; probe json/portfolios/non_model_assets.json = absent", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_cottonwood_account_units", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/cottonwood/account-units.json", "layer": "platinum", "format": "json", "table": "account-units (Cottonwood only)",
 "grain": "unit values: 384 total points, per model (12)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher", "schedule": "daily", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-12", "field": "value_date (never assignment_date)", "lag_trading_days": 1, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 1, "bytes": 9949, "rows_sampled": 384, "claim": "measured"},
 "columns": [{"name": "total_unit_values[]", "type": "list[float] (384)", "nullable": false, "description": "unit values (no account identifiers present)", "example": 10.12}, {"name": "by_model_unit_values.<model key>", "type": "list[float]", "nullable": false, "description": "per model", "example": "opal_intermediate"}, {"name": "firm_id, generated_at, assignment_date, value_date, basis, _provenance", "type": "string", "nullable": false, "description": "vintage", "example": "cottonwood"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 = cottonwood + field firm_id", "values": ["cottonwood"]}, "account": {"column": "none -- values only, no account key", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "basis", "values": ["not enumerated"]}},
 "nl_tags": ["account units", "unit values", "cottonwood"], "common_queries": ["(HELD at Andrew)"],
 "existing_gateway_tool": {"name": "none (row mp.12 deny + pending-andrew)", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.mdpf_model_portfolios.artifacts[mp.12]; held_at_andrew", "present": true},
 "prior_art": "rectangle.final.certified.json mp.12", "open_items": ["Held at Andrew; 0 callers"],
 "evidence": [{"read": "head+get platinum/mdpf/cottonwood/account-units.json", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/mdpf_manifests_and_archive", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/mdpf/{_manifests/,archive/}", "layer": "platinum", "format": "json", "table": "publish manifests + frozen archive",
 "grain": "_manifests: one per publish run (+ latest.json, 18 rows); archive: 439 daily aggregate_aua snapshots + 4 etf_ownership_timeseries + 1 series", "partition": {"keys": ["date"], "claim": "measured"},
 "producer": {"name": "opal-assets-mdpf-portal-publisher (manifests); archive written once 2026-08-06", "schedule": "manifests daily; archive none", "claim": "measured"},
 "freshness": {"latest_partition": "2026-10-13 (manifests); 2026-08-06 (archive)", "field": "LastModified", "lag_trading_days": 0, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 540, "bytes": 3800333, "rows_sampled": 18, "claim": "measured"},
 "columns": [{"name": "run_id, manifest_key, rows", "type": "mixed", "nullable": false, "description": "publish provenance (latest.json)", "example": "20261013T135047Z-4fca44fb"}],
 "enums": {},
 "fork_keys": {"firm": {"column_or_key_segment": "manifest rows name scope keys; archive is global", "values": ["global", "49financial", "cottonwood", "inflection"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["did the publish run", "mdpf manifest"], "common_queries": ["Did today's MDPF publish run? (ops only)"],
 "existing_gateway_tool": {"name": "none (rows mp.13-14 deny)", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "channels.mdpf_model_portfolios.artifacts[_manifests/**, archive/**]", "present": true},
 "prior_art": "rectangle.final.certified.json mp.13, mp.14",
 "open_items": ["Catalog paths.daily_history and portal_lookup.py point at platinum/mdpf/aggregate_aua/ (0 keys): the snapshots are only in archive/, frozen"],
 "evidence": [{"read": "list platinum/mdpf/ (558); get _manifests/latest.json", "at": "2026-10-14T13:3xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/etfs_positioning_data", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/etfs/positioning_data.json (+ _manifests/)", "layer": "platinum", "format": "json", "table": "etfs positioning_data",
 "grain": "one member per Opal ETF (DIVZ, IDVZ, PFDE, PFOE)", "partition": {"keys": [], "claim": "measured"},
 "producer": {"name": "etf_positioning_publisher (manifest producer; run_class scheduled)", "schedule": "daily ~13:01Z", "claim": "measured (manifest)"},
 "freshness": {"latest_partition": "2026-10-13", "field": "data_as_of (+ data_as_of_spread)", "lag_trading_days": 0, "basis": "trading-day-frontier (object rewritten 2026-10-14T13:01:42Z)", "claim": "measured"},
 "size": {"objects": 66, "bytes": 201317, "rows_sampled": 4, "claim": "measured"},
 "columns": [{"name": "portfolios.<fund>.{code,name,data_as_of,as_of_basis,prior_date,holdings_status,num_holdings,aum,allocation,management,characteristics,segment,holdings}", "type": "object", "nullable": true, "description": "per-fund positioning", "example": "DIVZ"}, {"name": "data_as_of_spread", "type": "list (2)", "nullable": false, "description": "min/max as-of across funds", "example": "2026-10-13"}, {"name": "note, data_date, generated_at", "type": "string", "nullable": true, "description": "vintage", "example": "2026-10-13"}],
 "enums": {"fund": ["DIVZ", "IDVZ", "PFDE", "PFOE"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- opal-internal (firm_scope_rule opal-internal-only)", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["ETF holdings", "ETF AUM", "DIVZ", "PFDE", "fund positioning"],
 "common_queries": ["What does PFDE hold and what is its AUM?"],
 "existing_gateway_tool": {"name": "etfs_get_positioning", "verdict": "keep"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "portal_datasets.portal_etfs_positioning + channels.etfs_positioning", "present": true},
 "prior_art": "workflows/atom_decomposition/runs/etfs-positioning/ (G5)",
 "open_items": ["G5 owns the ETF pipeline"],
 "evidence": [{"read": "head+get platinum/etfs/positioning_data.json; get one _manifests object", "at": "2026-10-14T13:1xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/advi_49financial_twins", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/advi/49financial/{mix_summary,leaderboard,ownership_map,timeseries_overview,cumulative_chart,clients-tab-slim,timeseries_chart,timeseries_chart_full,partner_analytics_quarterly,partner_analytics_annual}.json + _manifests/", "layer": "platinum", "format": "json", "table": "ADVI 49financial certified twins",
 "grain": "firm dashboards: leaderboard per window (146 advisor entries), time series, partner analytics", "partition": {"keys": ["firm (segment 3)"], "claim": "measured"},
 "producer": {"name": "DS~B ADVI publisher (manifest 2026-08-20/933dfc1bf6b1)", "schedule": "none since 2026-09-01", "claim": "measured (manifest key) / inferred cadence"},
 "freshness": {"latest_partition": "2026-08-21", "field": "data_as_of / LastModified", "lag_trading_days": 36, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 15, "bytes": 21059752, "rows_sampled": 146, "claim": "measured (leaderboard only)"},
 "columns": [{"name": "leaderboard.windows.<QTD|YTD|MAX|1Y|3Y>.{entries[],entry_count,summary}", "type": "object", "nullable": true, "description": "advisor ranking (15 fields per entry; advisor identity = PII)", "example": "<advisor name>"}, {"name": "firm_id, data_as_of, generated_at, window_bounds, available_windows", "type": "mixed", "nullable": false, "description": "vintage", "example": "49financial"}],
 "enums": {"window": ["QTD", "YTD", "MAX", "1Y", "3Y"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 platinum/advi/<firm>/ (long form 49financial, never the bucket suffix bd)", "values": ["49financial"]}, "account": {"column": "inside entries (not measured here)", "last4_derivation": "not measured", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["advisor leaderboard", "partner analytics", "49financial book"],
 "common_queries": ["(HELD: catalog v0.4 platinum/advi NOT YET; 0 of 15 portal keys flipped)"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "portal/src/api/endpoints/adviKeyRepoint.ts (origin/PROD) registry: 14 held, 1 structural",
 "open_items": ["Malformed key platinum/advi/49financial/_manifests//4b36d4f5743c.json (empty date segment)", "5 registry leaves absent: header_metrics, dashboard, fee_efficiency, partner_analytics_monthly, advisor_nna_canonical", "CVO diff found 9 of 10 twins carry material regressions (adviKeyRepoint.ts:110-118)"],
 "evidence": [{"read": "list platinum/advi/ (18); get leaderboard.json shape", "at": "2026-10-14T13:2xZ"}]}
```

```json
{"contract_id": "opal-data-portal-v2/platinum/advi_49financial_perfrp", "bucket": "opal-data-portal-v2", "s3_prefix": "platinum/advi/49financial/perfrp_{book_advisor,gainloss_account,gainloss_relationship}.json", "layer": "platinum", "format": "json", "table": "perfrp leaves (49financial)",
 "grain": "one entry per advisor (146) / account (6,183) / relationship (3,836) for one window", "partition": {"keys": ["firm (segment 3)", "level (advisor|account|relationship)"], "claim": "measured"},
 "producer": {"name": "perfrp_emit_core (data/assets/scripts/gold/runners_49f/perfrp_contract.py per portal contract.ts)", "schedule": "none since 2026-09-01", "claim": "inferred"},
 "freshness": {"latest_partition": "2026-09-01", "field": "as_of", "lag_trading_days": 29, "basis": "trading-day-frontier", "claim": "measured"},
 "size": {"objects": 3, "bytes": 34316561, "rows_sampled": 10165, "claim": "measured"},
 "columns": [{"name": "entries[].key", "type": "string", "nullable": false, "description": "account id (account leaf, 10-char single shape) / relationship name / advisor name -- PII", "example": "****1234 / <client name> / <advisor name>"}, {"name": "entries[].{accounts,cost_basis,cost_basis_column,lots,market_value,realized,total_gain_loss,unrealized_long_term,unrealized_short_term,unrealized_term_undeclared,unrealized_total}", "type": "number/string", "nullable": true, "description": "gain/loss leaves", "example": 1234.5}, {"name": "entries[].{accounts,client_table,re_keyed_clients,relationship_partition,role_sum_would_be,tiles}", "type": "mixed", "nullable": true, "description": "book_advisor leaf", "example": "{...}"}, {"name": "as_of, contract_version, declared_absent_columns(10), family, generated_by, level, periods(6), si_label, window", "type": "mixed", "nullable": false, "description": "contract metadata", "example": "2026-09-01"}],
 "enums": {"level": ["advisor", "account", "relationship"]},
 "fork_keys": {"firm": {"column_or_key_segment": "key segment 3 = 49financial (only firm present)", "values": ["49financial"]}, "account": {"column": "entries[].key (account leaf)", "last4_derivation": "last 4 digits of key", "last4_collisions_within_firm": 1280}, "platform": {"column": "cost_basis_column / window.cost_basis_basis (custodian basis)", "values": ["not enumerated"]}},
 "nl_tags": ["gain loss", "realized gains", "unrealized gains", "cost basis", "advisor book performance"],
 "common_queries": ["(HELD) What are unrealized gains for 49financial account ****1234?"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"}, "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "portal/src/api/endpoints/advisor-intelligence.ts:1601-1648, 1748, 1815 (origin/PROD)",
 "open_items": ["last-4 is NOT unique: 1,280 colliding last-4 groups cover 2,826 of 6,183 account entries -- any tool must take the full account id or a disambiguator", "Relationship and advisor keys are names (PII): never echo", "Page requests 5 more leaf families (performance, allocation, transactions_sample) that do not exist (404 -> null by design)", "Catalog v0.4 holds platinum/advi: no tool until Andrew lifts the hold"],
 "evidence": [{"read": "get all 3 leaves; key-shape and last-4 counts only, no value printed", "at": "2026-10-14T13:2xZ"}]}
```

```json
{"contract_id": "dynamodb/opal-tickets", "bucket": "dynamodb (not opal-data-portal-v2)", "s3_prefix": "n/a -- table opal-tickets", "layer": "dynamodb", "format": "dynamodb", "table": "opal-tickets",
 "grain": "one item per ticket", "partition": {"keys": ["ticket_id (HASH)", "GSI status-index"], "claim": "measured"},
 "producer": {"name": "opal-ticket-api (POST /api/scoped/tickets*, 10 routes) + trade-submission-handler (TICKETS_TABLE)", "schedule": "on user action", "claim": "measured (API GW routes + Lambda env)"},
 "freshness": {"latest_partition": "2026-10-14 (newest created_at)", "field": "created_at", "lag_trading_days": 0, "basis": "event table; not a trading-day series", "claim": "measured"},
 "size": {"objects": 31, "rows_sampled": 31, "claim": "measured (COUNT scan, 1 page)"},
 "columns": [{"name": "ticket_id", "type": "S", "nullable": false, "description": "key", "example": "TKT-..."}, {"name": "ticket_type", "type": "S", "nullable": true, "description": "type", "example": "analysis_request"}, {"name": "status", "type": "S", "nullable": true, "description": "lifecycle", "example": "completed"}, {"name": "title, description, resolution, source, assignee, created_by", "type": "S", "nullable": true, "description": "text and people (created_by/assignee are user identities: PII)", "example": "<text>"}, {"name": "created_at, claimed_at, completed_at, first_response_at", "type": "S", "nullable": true, "description": "timestamps", "example": "2026-10-14T03:33:25"}, {"name": "requester, routing, claimed_by, completed_by, answers, attachment, package, report_ref, draft_commentary, commentary_sent", "type": "M", "nullable": true, "description": "structured blocks", "example": "{...}"}, {"name": "events, client_updates, tags", "type": "L", "nullable": true, "description": "history", "example": "[...]"}, {"name": "time_to_claim_s, time_to_resolve_s, reopened_count, schema_version", "type": "N", "nullable": true, "description": "metrics", "example": 3600}, {"name": "category, priority, linked_submission_id", "type": "NULL in every item read", "nullable": true, "description": "unused", "example": null}],
 "enums": {"status": ["completed", "in_progress", "open"], "ticket_type": ["analysis_request", "service_request", "trade_request", "other"]},
 "fork_keys": {"firm": {"column_or_key_segment": "requester (M) -- firm not a top-level attribute; not measured", "values": []}, "account": {"column": "none top-level", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "none", "values": []}},
 "nl_tags": ["tickets", "service requests", "analysis requests", "ticket status"],
 "common_queries": ["How many tickets are open?", "What is the average time to resolve an analysis request?"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "RESOLVER FLOOR forbids any ticket row until D7 sec.7.3 (ticket-API authorization design) lands at Andrew", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/portal-page-ticket-center/20260812T0637Z (NOT certified; rectangle not read)",
 "open_items": ["Cannot fork by firm without reading requester maps; tool blocked by the resolver floor regardless"],
 "evidence": [{"read": "dynamodb describe_table + scan Select=COUNT + attribute-name census", "at": "2026-10-14T13:3xZ"}]}
```

```json
{"contract_id": "dynamodb/opal-trade-submissions", "bucket": "dynamodb + s3://opal-data-trade-submissions (not opal-data-portal-v2)", "s3_prefix": "n/a -- table opal-trade-submissions; files at opal-data-trade-submissions/{submissions,parquet}/", "layer": "dynamodb", "format": "dynamodb", "table": "opal-trade-submissions",
 "grain": "one item per trade submission (a fund rebalance request through approval and execution)", "partition": {"keys": ["submission_id (HASH)", "GSIs by-date, by-initiator, by-approver-decided, by-status"], "claim": "measured"},
 "producer": {"name": "trade-submission-handler (POST /api/general/trades/submit), trade-workflow-handler", "schedule": "on user action", "claim": "measured (API GW + Lambda env)"},
 "freshness": {"latest_partition": "2026-09-25 (newest submission_date)", "field": "submission_date", "lag_trading_days": null, "basis": "event table; not a trading-day series", "claim": "measured"},
 "size": {"objects": 33, "rows_sampled": 33, "claim": "measured (COUNT scan, 1 page); S3 side 27 objects"},
 "columns": [{"name": "submission_id", "type": "S", "nullable": false, "description": "key", "example": "<uuid>"}, {"name": "status", "type": "S", "nullable": false, "description": "workflow state", "example": "PENDING_APPROVAL"}, {"name": "fund, brokerage", "type": "S", "nullable": false, "description": "fund traded and executing broker", "example": "<fund>"}, {"name": "securities, model_securities, audit_events", "type": "L", "nullable": true, "description": "trade lines and history", "example": "[...]"}, {"name": "submission_date, created_at, submitted_at, decided_at, approved_at, rejected_at, executed_at, completed_at, weights_as_of, proposed_trades_as_of", "type": "S", "nullable": true, "description": "timestamps", "example": "2026-09-25"}, {"name": "initiator_email, initiator_name, approver_email, approver_name, executor_email, executor_name", "type": "S", "nullable": true, "description": "user identities (PII)", "example": "<email>"}, {"name": "excel_s3_key, json_s3_key, trade_csv_key", "type": "S", "nullable": true, "description": "file pointers into opal-data-trade-submissions", "example": "submissions/<id>.xlsx"}, {"name": "attestations (M), brokerage_email_sent (BOOL), weight_unit, template_version, portfolio_version_id, trade_comments, other_comments, rejection_reason, cash_trade_indicated, source", "type": "mixed", "nullable": true, "description": "workflow detail", "example": "<text>"}],
 "enums": {"status": ["PENDING_APPROVAL", "APPROVED", "REJECTED", "EXECUTED", "COMPLETE"]},
 "fork_keys": {"firm": {"column_or_key_segment": "none -- Opal ETF funds, opal-internal", "values": ["opal-internal"]}, "account": {"column": "none", "last4_derivation": "n/a", "last4_collisions_within_firm": null}, "platform": {"column": "brokerage", "values": ["not enumerated"]}},
 "nl_tags": ["trade submissions", "pending trades", "trade approval", "rebalance requests"],
 "common_queries": ["How many trade submissions are pending approval?", "When was the last PFDE trade executed?"],
 "existing_gateway_tool": {"name": "none", "verdict": "none"},
 "proposed_tools": [],
 "catalog_entry": {"data_catalog_key": "", "present": false},
 "prior_art": "workflows/atom_decomposition/runs/portal-page-trade-submission/20260812T1805Z (NOT certified; no rectangle)",
 "open_items": ["Carries user emails/names on every item: same caller-identity class as the ticket resolver floor; propose no tool until Andrew rules", "S3 side newest object 2026-07-20 while DynamoDB newest submission is 2026-09-25 (excel/json keys set on 15 and 2 of 33 items)"],
 "evidence": [{"read": "dynamodb describe_table + scan Select=COUNT + attribute-name census; s3 list opal-data-trade-submissions (27)", "at": "2026-10-14T13:3xZ"}]}
```

## 5. Cross-checks

### 5.1 DATA_CATALOG `channels` (16) vs live

| channel | tool | live state today | verdict |
|---|---|---|---|
| benchmarks_and_models | portal_lookup | 4 live, 2 frozen (as ruled) | keep |
| capital_markets | portal_lookup | 2 unchanged (views 190 TD) | keep |
| correlations_factors | portal_lookup | 4 live | keep |
| etfs_positioning | portal_lookup | live | keep |
| macro_rates | portal_lookup | 4 rows live; `paths.tenor_series` says 84 objects, measured 79; `macro_data_fred` has no row | fix count |
| market_overview | none | `market-metrics.json.gz` frozen since 2026-04-15 (128 TD) | retire or repoint to json-tiered |
| market_regime_trending | portal_lookup | 2 rows (mkt.01 live, mkt.02 frozen); regime and trending live but unrowed | extend |
| mdpf_model_portfolios | portal_lookup | 8 rows; `json/mdpf/**` GONE; `paths.daily_history` MOVED into archive; category-views unrowed | fix + extend |
| news | none | G6 | -- |
| peers | portal_lookup | live monthly | keep |
| pipeline_freshness | none | manifest live | extend (tool) |
| positioning_holdings | portal_lookup | 3 live; aum-metrics row frozen + 0 readers | re-rule aum-metrics |
| sentiment_news_mood | portal_lookup | 1 row live, 2 frozen (as ruled) | keep |
| valuation | portal_lookup | 2 live | keep |
| sharepoint_documents | M365 MCP | out of scope | -- |
| bloomberg_standing_read | portal_lookup | out of scope | -- |

`never_serve` drift: `json/mdpf/**` no longer exists; `json-tiered/ (01-13)` is wrong (summary, rsi, 84 timeseries and 71 details written 2026-10-14).

### 5.2 DATA_CATALOG `portal_datasets` (5)

All 5 objects exist and are fresh: portal_etfs_positioning (0 TD), portal_mdpf_account_distribution (0-1 TD), portal_mdpf_aggregate_aua (1 TD), portal_mdpf_aum_metrics (1 TD), portal_mdpf_model_benchmarks (0 TD). The family axis `scope` has exactly 4 live members (global, 49financial, cottonwood, inflection): matches. Missing: a 6th row for category-views.

### 5.3 Served dataset prefixes (for G4's overlap measurement)

MDPF-related (the G4 overlap set, 18 + 2 families):
- `platinum/mdpf/{global,49financial,cottonwood,inflection}/aum-metrics.json`
- `platinum/mdpf/{global,49financial,cottonwood,inflection}/account-distribution.json`
- `platinum/mdpf/{global,49financial,cottonwood,inflection}/aggregate-aua-timeseries.json`
- `platinum/mdpf/{global,49financial,cottonwood,inflection}/category-views.json`
- `platinum/mdpf/global/non-model-assets.json`, `platinum/mdpf/cottonwood/account-units.json`
- `platinum/mdpf/_manifests/` (96), `platinum/mdpf/archive/` (444, incl. 439 `aggregate_aua/YYYY-MM-DD.json`)
- `json/benchmarks/model_portfolio_{benchmarks,timeseries}.json` (Yang model-design, not MDPF gold, but the same "model portfolios" questions)
- legacy `json/portfolios/` (5, frozen)
- source of the 18 platinum keys (measured `_provenance.source_keys`): `s3://opal-data-assets/portal/gold/mdpf/{scope}/{leaf}/YYYY-MM-DD.json` -- not `opal-data-mdpf`.

All other served prefixes: `json/positioning/`, `json/benchmarks/`, `json/peers/`, `json/capital-markets/`, `json/correlations/`, `json/factor-tilts/`, `json/macro/`, `json/valuation/`, `json/valuations/`, `json-tiered/market-overview/`, `json/market/`, `json/market-overview/`, `json/sentiment/`, `json/trending/`, `json/semantic-trending/`, `json/security_scanner/`, `json/latest/`, `json/yang-pipeline-metadata.json`, `json/model_portfolios/`, `json/returns/`, `json/yang/`, `platinum/etfs/`, `platinum/advi/49financial/`.

## 6. What could not be read, and why

- **Deployed edge code not diffed:** `public-data-router:7` and `shared-advisor-router:28` were read as live config (version numbers) only; the rewrite rules are from the repo copy. The `platinum/advi -> portal-v2` origin override is inferred from portal source comments, not exercised.
- **No authenticated 200 through any route** was exercised (read-only bounds; no JWT). Reachability statements are routing-config statements.
- **Producer schedules** for the Yang family, market regime, tiered market overview and keyword sentiments are inferred from LastModified clustering, not from EventBridge rules (not enumerated).
- **Objects not opened:** `json/model_portfolios/**` (128 MB), the 76 dated security-scanner snapshots, `json/sentiment/keyword-history-*` (720), the 10 ADVI twin leaves other than leaderboard, everything under `benchmarks/`, `canon/`, `data-refresh/` (pipeline inputs; not served).
- **Firm column inside `opal-tickets.requester`** (a map) was not opened: the ticket table's firm fork is unmeasured.
- **The trade-submission `fund` and `brokerage` values** were not enumerated (kept out of the record; counts only).
- **The ticket-center `rectangle.final.json` and `rectangle.verify.json`** were deliberately not read (PRD 9.8.1 A); the advisor-intelligence c18 rectangle was not read either (not a certified artifact).

### Open items for the CRO (surprise-row candidates; this part writes no file outside itself)

1. `json/mdpf/**` GONE (0 keys) while catalog row, `never_serve` and `portal_lookup.py` channel `mdpf` still name it.
2. Catalog `never_serve` says `json-tiered/` frozen 01-13; measured live today, and `mkt.01` serves it.
3. Duplicate output path: top-level `macro/macro_data.json` written 2026-10-14T11:06:01Z, byte-equal size to `json/macro/macro_data.json`.
4. Pages request 8 absent keys (404 class), incl. `json/portfolios/non_model_assets.json` from ModelPortfolios and `json/metadata/yang.json` from YangDataContext.
5. `json/portfolios/aum-metrics.json`: 0 page readers at PROD but still a serve-with-caveat catalog row linked to `gateway_query_catalog` (ft.04): re-rule.
6. CloudFront behavior `/json-tiered/*` -> portal-v2 carries no edge auth Lambda (config read, not exercised).
7. `platinum/advi/49financial/_manifests//4b36d4f5743c.json`: malformed key with an empty segment.
8. `news-trending-analysis` env `S3_KEY=sentiment/keyword-sentiments.json` names a key frozen since 2026-01-08.
9. perfrp account last-4 collides: 1,280 groups / 2,826 of 6,183 entries.
