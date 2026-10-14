# G6 news -- gateway data-contract census part (subagent of 4.0.0_SA_CRO~Z, 2026-10-14 12:5xZ-13:3xZ)

- **Scope:** the NEWS pipeline. DynamoDB `opal-news-articles`, `opal-news-trending-daily`, `semantic-news-trending-daily`,
  `opal-harvest-articles`, `seeking-alpha-article-urls`; plus the three further tables the same name sweep found
  (`opal-keyword-intelligence`, `market-updates`, `opal-harvest-security-metrics`) and the S3 buckets the pipeline writes
  (`opal-data-news-v2`, `opal-data-news-av`, and the news keys of `opal-data-portal-v2`).
- **Binding:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md`
  sections 2-4; `parts/_SUBAGENT_BRIEF.md`.
- **Prior art:** `workflows/atom_decomposition/runs/news-subsystem/20260811T2330Z/rectangle.final.certified.json`
  (CERTIFIED; 4 entities, all on the S3 `json/sentiment/` tree, none on DynamoDB). Read in full.
- **Bounds kept:** every AWS call was a read (describe, list, query with `Select=COUNT` or a projection, scan with
  `Limit<=50` per segment, get-function-configuration, list-targets, get-role-policy, S3 list/get of small JSON and one
  projected Parquet read). No Lambda invoke, no write, no vendor call. No article body, summary or title text is copied here.
- **Trading calendar:** `lib/trading_calendar.py` (NYSE hardcoded fallback 2010-2027); T-1 = 2026-10-13.

## (a) Method: each read, its instrument and its denominator

| # | read | instrument | denominator |
|---|---|---|---|
| M1 | DynamoDB table list | boto3 `list_tables` paginator, us-east-1 | 46 of 46 tables; 8 match the name sweep (news, trend, article, seeking, keyword, sentiment, harvest, semantic, market-update, headline) |
| M2 | table metadata | `describe_table` + `describe_time_to_live` + `list_tags_of_resource` | 8 of 8 tables, 2026-10-14T12:56:59Z |
| M3 | attribute names and types | `scan Limit=50` (1 segment) per table; then `scan Segment=s TotalSegments=20 Limit=50` for `opal-news-articles` and `seeking-alpha-article-urls`, 10x50 on the `source_date_index` GSI | 50 items per table (semantic: 50 of 113); 1,000 items of 381,261 for `opal-news-articles`; 1,000 of 50,648 for SA urls; 500 of 9,905 GSI items. A SAMPLE, not a census |
| M4 | items per day (`opal-news-articles`) | `query article_date=<d> Select=COUNT`, paginated, every calendar day 2023-01-01..2026-10-14 | 1,383 days queried; 651 days non-empty; 381,354 items summed (376,352 on 318 of 318 days 2025-12-01..2026-10-14; 5,002 on 333 days 2023-10-13..2025-11-30) vs ItemCount 381,261 (ItemCount refreshes ~6h; +93 is inferred to be today's ingestion) |
| M5 | items per day (trending, semantic, keyword-intel, SA urls) | `query <hash>=<d> Select=COUNT` per calendar day (keyword-intel through GSI `date-index`; SA urls for both `<d>` and `<d>_news`) | trending 5,780 on 314 of 318 days (ItemCount 5,814); semantic 113 on 12 days (ItemCount 113, exact); keyword-intel 4,755 on 197 of 234 days (ItemCount 4,735); SA urls 36,580 + 14,068 = 50,648 (ItemCount 50,648, exact) |
| M6 | value distributions, newest 3 days of `opal-news-articles` | `query` with projection (source, entity_type, query_set, finbert label, ingestion_timestamp) | 985 + 864 + 158 = 2,007 of 2,007 items on 2026-10-12..14 |
| M7 | GSI `source_date_index` per source | `query` newest/oldest `Limit=1` + `Select=COUNT` per source seen in M3 | 41 sources; 7,055 of 9,905 GSI items (the sources not in the 500-item sample are not counted) |
| M8 | trending ticker coverage | `query date=<d>` projecting affected_tickers, affected_sectors, gpt_model, every day 2025-12-01..2026-10-14 | 5,780 of 5,780 items |
| M9 | Lambda producers | `list_functions` paginator; env vars naming any of the 8 tables or a news bucket, or a news-like name | 237 of 237 functions; 21 matched; plus `finbert-batch-processor`, `irpt-narrative`, `daily-agenda-generator` found by M11 / role map |
| M10 | schedules | `events list_rules` (155 of 155) + `list_targets_by_rule` per rule; `scheduler list_schedules` + `get_schedule` | 39 rule->target pairs onto the matched Lambdas; 1 Scheduler schedule |
| M11 | estate graph | `comp-find --corpus aws 'news'` (vintage 2026-10-14 13:28:12Z) | 91 hits across 2,929 aws nodes (2 pages read, 91 of 91) |
| M12 | IAM readers/writers | `get_role_policy` x3; Lambda->role map over 237 functions | 3 inline policies; 8 functions on the 6 news roles |
| M13 | S3 census | `list_objects_v2` paginator | `opal-data-news-v2` 8 pages, 7,735 of 7,735 keys; `opal-data-news-av` 11 pages, 10,246 of 10,246; `opal-data-portal-v2` prefixes json/sentiment/ (722), sentiment/ (5), json/trending/ (1), json/semantic-trending/ (1), and 0 under trending/, semantic_clusters/, json/keyword-intelligence/, json/news/, news/ |
| M14 | S3 object shapes | `get_object` of 6 small JSON objects, top-level field names and types only | 6 objects (a sample of 1 per family) |
| M15 | harvest overlap | `opal-data-harvest` list of seeking-alpha/, ft/, gold article_security_mention/; projected Parquet read (article_id, published_utc, type) of every SA silver article part; per-day `query` of `opal-news-articles` projecting url, source | 1,365 of 1,365 SA silver parts, 19,477 rows, 19,472 distinct ids; window 2026-09-28..2026-10-11 (+-1 day on the news side) |

## (b) Census

### b.1 DynamoDB (us-east-1, describe at 2026-10-14T12:56:59Z)

| table | keys | GSIs | ItemCount | bytes | avg item | TTL | stream | created | newest (measured) | trading days behind T-1 |
|---|---|---|---|---|---|---|---|---|---|---|
| `opal-news-articles` | HASH `article_date` (S, YYYY-MM-DD) + RANGE `url_hash` (N) | `source_date_index` (`source` + `published_at`), ALL, 9,905 items (sparse) | 381,261 | 255,062,433 | 669 B | DISABLED | none | 2025-12-23 | 2026-10-14 (158 items by 10:01Z) | 0 |
| `opal-news-trending-daily` | HASH `date` + RANGE `topic_rank` (`bullish-1..10`, `bearish-1..10`) | none | 5,814 | 40,239,871 | 6,921 B | DISABLED | none | 2025-12-23 | 2026-10-14 (20 items, created 11:20:57Z) | 0 |
| `semantic-news-trending-daily` | HASH `date` + RANGE `topic_rank` | none | 113 | 242,721 | 2,148 B | DISABLED | none | 2026-02-13 | 2026-02-24 | 160 (FROZEN) |
| `opal-harvest-articles` | HASH `security_key` + RANGE `published_at` | `platform_date_index`, `ticker_date_index` (0 items each) | 0 | 0 | -- | DISABLED | none | 2026-09-11 | EMPTY: scan `Select=COUNT` Count 0, ScannedCount 0, no LastEvaluatedKey (13:1xZ) | n/a |
| `seeking-alpha-article-urls` | HASH `run_date` (`YYYY-MM-DD` = analysis, `YYYY-MM-DD_news` = news) + RANGE `article_id` | none | 50,648 | 7,421,714 | 147 B | DISABLED | none | 2026-02-18 | 2026-04-13 (both families) | 127 (FROZEN) |
| `opal-keyword-intelligence` | HASH `keyword` + RANGE `generated_date` | `date-index` (`generated_date` + `keyword`), ALL | 4,735 | 28,642,658 | 6,049 B | DISABLED | none | 2026-02-23 | 2026-10-14 (20 items) | 0 |
| `market-updates` | HASH `update_id` | `CreatedByIndex` | 1 | 300 | 300 B | ENABLED (`ttl`) | none | 2026-01-21 | 2026-01-21, one `status=draft` test item | 183 |
| `opal-harvest-security-metrics` | HASH `axis_date` (`<AXIS>#<date>[#<generation>]`) + RANGE `ticker` | `axis-rank-index` | 6,845 | 3,646,892 | 533 B | DISABLED | none | 2026-09-11 | `TRENDING_CHATTER#2026-10-14`; price axes to 2026-10-13 (computed_at 2026-10-14T11:07Z) | 0 |

Daily volume of `opal-news-articles` (M4): Dec-2025 30,455; Jan 24,482; Feb 31,636; Mar 42,862; Apr 41,523; May 39,987;
Jun 37,847; Jul 38,785; Aug 39,176; Sep 36,799; Oct 1-14 12,800. Weekdays 2026-09-25..10-13 run 985-1,229 items, weekends
703-756. No empty day in 318 of 318 days since 2025-12-01.

### b.2 Producers and schedules (M9, M10, M12; read 2026-10-14T13:01:15Z)

| Lambda | writes (env var) | reads | schedule (EventBridge, UTC) | state |
|---|---|---|---|---|
| `news-ingestion-scheduler` | `opal-news-articles` (DYNAMODB_TABLE); `opal-data-news-v2` logs/ (S3_BUCKET) | NewsAPI + RSS (vendor) | 22 rules `news-api-*` and `news-rss-*` (e.g. rss 01/04/09/12/15/18/21 ET; api 01/03/05/07/08:45/13/15:45/16/18/19:45/23 ET); `news-api-1100am` DISABLED | 21 of 22 ENABLED |
| `finbert-batch-processor` | `opal-news-articles` sentiment_finbert* (inferred from the attribute and the rule name; env is empty) | same table | `finbert-scoring-post-ingestion` cron(10 2,4,12,14,16,17,18,20,21,22,23) and `-45min` cron(55 0,13,20) | ENABLED |
| `news-trending-analysis` | `opal-news-trending-daily` (TRENDING_TABLE); portal-v2 `json/sentiment/keyword-sentiments.json` (env S3_KEY says `sentiment/...`; live writes land under `json/`); `opal-data-news-v2` trending_reports/ (inferred: same-minute write) | `opal-news-articles` (SOURCE_TABLE) | `news-trending-analysis-daily` cron(15 11,21) | ENABLED |
| `keyword-intelligence-generator` | `opal-keyword-intelligence` (INTELLIGENCE_TABLE) | `opal-news-articles` | own rule `keyword-intelligence-generator-daily` DISABLED; rows still land daily, so it is invoked by another function (role `news-ingestion-lambda-role` holds `lambda:InvokeFunction` on it; inferred caller `news-trending-analysis`) | live by invoke |
| `opal-trending-topics-portal-publisher` | portal-v2 `json/trending/latest.json` (inferred; written 11:21:00Z, 3 min after trending) | trending table | its 3 rules DISABLED; `opal-news-lambda-role` holds invoke on it | live by invoke (inferred) |
| `opal-news-layer3-curation` | `opal-news-trending-daily` (TARGET_TABLE) | `opal-news-articles` | `layer3-gpt-curation-daily` DISABLED | dormant or invoked (not resolved) |
| `opal-keyword-drilldown-generator` | portal-v2 `json/sentiment/keyword-history-*` | `opal-news-articles` | `keyword-drilldown-generator-daily` DISABLED | FROZEN since 2026-04-07 (prior art news.04) |
| `opal-portal-fear-greed-fetcher` | portal-v2 `json/sentiment/fear-greed-index.json` | CNN Fear and Greed (vendor) | `fear-greed-daily-update` cron(30 14,21) | ENABLED |
| `news-semantic-clustering`, `semantic-news-layer3-curation`, `semantic-trending-topics-portal-publisher` | `opal-data-news-v2` semantic_clusters/; `semantic-news-trending-daily` (no table env var; inferred from name); portal-v2 `json/semantic-trending/latest.json` | `opal-news-articles` | no rule or schedule targets any of the three | FROZEN since 2026-02-24 |
| `seeking-alpha-news-coordinator`, `-dedup`, `-scraper`; `seeking-alpha-analysis-coordinator`, `-dedup`, `-listing-parser`, `-scraper` | `seeking-alpha-article-urls` (DEDUP_TABLE); `opal-news-articles` (scrapers); `opal-data-news-av` seeking-alpha/ | seekingalpha.com | `seeking-alpha-news-daily` cron(0 14) DISABLED; `seeking-alpha-analysis-daily` cron(0 21) DISABLED | FROZEN since 2026-04-13 |
| `opal-amgt-scoped-api` | none of these | `opal-harvest-articles` (HARVEST_ARTICLES_TABLE env), `opal-harvest-security-metrics` | Scheduler `amgt-global-freshness-snapshot-daily` cron(30 12 ? * MON-FRI) | ENABLED |
| readers outside the pipeline | -- | `irpt-narrative` (role `irpt-narrative-role`: Query/GetItem/Scan on `opal-news-trending-daily` + `opal-news-articles`, GetObject on news-v2 trending_reports/*); `daily-agenda-generator` (role `news-ingestion-lambda-role`, reads not traced) | -- | -- |

### b.3 S3 prefix census (M13, listed 2026-10-14T13:07:01Z and 13:12Z; LastModified in UTC)

| bucket / prefix | objects | bytes | oldest | newest LastModified | trading days behind | what it is |
|---|---|---|---|---|---|---|
| `opal-data-news-v2/trending_reports/<yyyy>/<mm>/<dd>/trending_report_<hhmmss>.json` | 763 | 444,268,816 | 2025-12-23 (copy-in) | 2026-10-14T11:18:07Z | 0 | per-run trending analysis archive, 311 days 2025-12-01..2026-10-14, 2 per day |
| `opal-data-news-v2/trending_reports/latest.json` | 1 | 494,866 | -- | 2026-10-14T11:18:07Z | 0 | pointer copy of the newest run |
| `opal-data-news-v2/logs/ingestion_<yyyymmdd>_<hhmmss>_<run>.json` | 6,901 | 1,123,460 | 2025-12-23 | 2026-10-14T11:45:06Z | 0 | one ingestion-run record (counts of rss/newsapi articles, errors); 312 days, 26 per day |
| `opal-data-news-v2/semantic_clusters/<date>.json` + `latest.json` | 13 | 476,769,338 | 2026-02-13 | 2026-02-24T14:05:53Z | 160 | FROZEN semantic cluster dumps (17-40 MB each) |
| `opal-data-news-v2/rss_trending/2025/11/...` | 10 | 7,859,946 | 2025-12-23 | 2025-12-23 | -- | legacy, copied in at bucket creation |
| `opal-data-news-v2/market_update/weekly_trending.json` | 1 | 58,030 | 2025-12-23 | 2025-12-23 | -- | legacy singleton |
| `opal-data-news-v2/{codebuild,lambda-deployments,lambda-packages,layer3_package,tmp}/`, root `ec2_layer3_curation.py` | 46 | 203,361,368 | 2025-12-23 | 2026-09-11 | -- | build and deploy artifacts, not data (incl. 31 `codebuild/anatomy-h/` zips unrelated to news) |
| `opal-data-news-av/seeking-alpha/news/{articles,deduped-batches,manifests}/<date>/` | 5,286 / 552 / 324 | 4,955,445 / 783,245 / 148,230 | 2026-02-18 | articles 2026-04-13T14:03Z; manifests 2026-07-30T14:00:57Z | 127 (articles) | per-article JSON; manifests after 04-13 report 0 URLs discovered (read 3 of 324: 07-30 and 04-14 = 0, 04-13 = 402) |
| `opal-data-news-av/seeking-alpha/analysis/{articles,batches,debug,deduped-batches,layer3-batches,manifests}/<date>/` | 2,499 / 37 / 2 / 11 / 778 / 756 | 5,749,221 total | 2026-02-18 | 2026-04-13T21:06:51Z | 127 | per-article JSON (article dates 2025-12-10..2026-02-23) + run manifests |
| `opal-data-news-av/lambda-packages/` | 1 | 71,189,204 | -- | 2026-02-18 | -- | deploy artifact |
| `opal-data-portal-v2/json/sentiment/` | 722 | 3,376,604 | 2026-01-05 | 2026-10-14T11:18:08Z | 0 for 2 keys; 131 for 720 keys | prior-art news.01/02 (720 frozen 2026-04-07) + news.03 (2 live) -- counts unchanged since the certified run |
| `opal-data-portal-v2/sentiment/` | 5 | 809,781 | 2025-12-23 | 2026-01-08T21:31:16Z | ~190 | legacy root copy, superseded by `json/sentiment/` |
| `opal-data-portal-v2/json/trending/latest.json` | 1 | 93,766 | -- | 2026-10-14T11:21:00Z | 0 | served trending top-10 bullish / top-10 bearish |
| `opal-data-portal-v2/json/semantic-trending/latest.json` | 1 | 30,603 | -- | 2026-02-24T14:20:44Z | 160 | FROZEN (catalog hazard already says do not serve) |

## (c) Analysis

**Where news accrues.** In DynamoDB, not S3. `opal-news-articles` is the one live article store: 381,261 items, about 1,000
a weekday from 22 enabled NewsAPI/RSS schedules, FinBERT-scored by `finbert-batch-processor` on 14 more. Everything
downstream reads it: trending (`opal-news-trending-daily`, 20 ranked topics a day), keyword intelligence
(`opal-keyword-intelligence`, ~20 GPT topic briefs a run), and the portal singletons in `opal-data-portal-v2`. The two
news buckets are archives and run logs: `opal-data-news-v2` holds the trending run archive (live) and the semantic
clusters (frozen); `opal-data-news-av` holds the Seeking Alpha scraper output (frozen since 2026-04-13).

**The pipeline is split live / frozen along its schedules**, as the certified prior art found for json/sentiment/:
- LIVE (0 trading days behind): `opal-news-articles`, `opal-news-trending-daily`, `opal-keyword-intelligence`, news-v2
  trending_reports/ and logs/, portal-v2 json/trending/ and the 2 json/sentiment singletons.
- FROZEN: `semantic-news-trending-daily` and semantic_clusters/ (2026-02-24, 160 behind; no schedule targets the three
  semantic Lambdas); `seeking-alpha-article-urls` and news-av seeking-alpha/ (2026-04-13, 127 behind; both rules
  DISABLED; the news coordinator kept writing 0-URL manifests to 2026-07-30); the keyword-history families (2026-04-07).
- EMPTY: `opal-harvest-articles` (0 items, created 2026-09-11; its coverage read was moved to the S3 pool, see
  `infra/aws/terraform/harvest/scoped-amgt-api.tf:332`, while the Lambda env still names it at `:510`).

**Keyed by security? No, nowhere in the news tables.** `opal-news-articles` is keyed by day and URL hash and carries no
ticker, security key or entity column (44 attribute names in a 1,000-item sample; `entity_type` is the feed type
RSS/NEWSAPI, not an entity). `opal-news-trending-daily.affected_tickers` is an empty list on every item since 2026-02:
0 of 618 items in the last 30 days, and the last ticker-bearing items are in 2026-01 (51 of 429). `opal-keyword-intelligence`
is keyed by a free-text topic keyword. A "news for a ticker" answer from these tables is a text match on the title, and
that is the precision a tool must say it has.

**Relation to the harvest (`opal-data-harvest`, G1).** The AMGT harvest is a separate collection with its own fetchers
(SA, FT, Bloomberg, WSJ, Barron's), and its gold `article_security_mention` is the only article-to-security index in the
estate (G1 / `OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md` section 2.2: 52,424 rows in the newest part, 234
securities, 3 trading days behind). Measured overlap on the one publisher both collect, Seeking Alpha, window
2026-09-28..2026-10-11: harvest silver holds 117 distinct SA ids, `opal-news-articles` holds 2,670 SA ids (every one an
`/article/` analysis URL from RSS), and the intersection is **0**. The streams are disjoint by content type: the harvest
SA silver is 19,384 of 19,472 ids of type `news`, the news table's SA rows are analysis articles. So: different
publishers mix, different SA content type, no shared key. The two do not double count; neither substitutes for the
other. The news tables answer "what is the market reading today"; the harvest answers "what was written about this name".

**Common questions** (from the catalog `news`, `market_regime_trending`, `sentiment_news_mood` rows and the table shapes):
1. Any news on rate cuts / tariffs / AI today, or this week? (articles by day window + text match)
2. What themes are trending today, bullish and bearish, and why? (trending by date)
3. How has a theme trended over the last N days? (trending by date range, matched on raw_keyword/headline)
4. Why is sentiment on a topic bearish, and what are the counterarguments? (keyword intelligence)
5. What is the market mood (fear/greed, keyword FinBERT)? (portal singletons; already linked by two gateway tools)
6. What has been written about ticker X? (harvest mention index first; news-table text match as a stated fallback)
7. How many articles did we ingest yesterday, from which sources, with what sentiment mix? (articles per day, run logs)

**Gateway tools today.** None of the 67 tools reads a news DynamoDB table or a news bucket: 0 code hits for news,
trending or keyword intelligence in `infra/aws/ec2/opal-gateway/app/**/*.py`; the 6 files that touch DynamoDB are
access-state, grants and Schwab. Two tools carry `news.03.live-singletons` as a catalog LINK (`gateway_query_catalog`
`DATA_CATALOG.yaml:1453`, `opal_asker_query` `:1858`); that is discovery, not a read of the tables.
Catalog row `news` (`:867`) names the three live tables and was right about their keys, but its sizes are stale
(it says 298K items and about 350 a day; measured 381,261 and about 1,000 a weekday).

**Proposed tools (5; all Opal-internal, no firm fork; each reads one store):**

| tool | store | inputs | returns | answers |
|---|---|---|---|---|
| `news_search_articles` | `opal-news-articles` | `date_from`, `date_to` (max 14 days), `text` (case-folded match on title + summary), `source`, `sentiment_label`, `limit` | per article: published, source, title, url, finbert label/score, entity_type; plus per-day counts and the denominator scanned | Q1, Q7; Q6 as a fallback with the precision stated |
| `news_trending_topics` | `opal-news-trending-daily` (+ news-v2 `trending_reports/<date>` run metadata) | `date` (default T, else T-1), `side` (bullish/bearish/all), `days` (1-30 for a theme history), `match` | 20 ranked topics: rank, headline, raw_keyword, trending_score, momentum, velocity, article_count, sources, citations, sentiment map, gpt_model, created_at | Q2, Q3 |
| `news_keyword_intelligence` | `opal-keyword-intelligence` | `keyword` (exact) or `date` (GSI `date-index`) | headline_summary, sentiment label/score/pattern, key_drivers, counterarguments, confidence, article list (titles+urls), generated_at | Q4 |
| `news_market_mood` | portal-v2 `json/sentiment/fear-greed-index.json` + `keyword-sentiments.json` | none | current fear/greed + 251-day history; keyword FinBERT set; each with its `generated_at` | Q5 (extend the existing catalog link into a direct read) |
| `news_for_security` | harvest gold `article_security_mention` (G1), then `news_search_articles` | `security_key` or `ticker`, `window_days` | mention rows (publisher, published_utc, title flag, tier) from the harvest; then the text-match fallback, labelled `match: text` | Q6 |

**Not proposed:** no semantic-trending tool (table and clusters frozen 160 trading days; serving it would present February
as today -- the revive-or-retire decision is Andrew's); no Seeking Alpha URL tool (a dedup ledger, frozen); no tool on
`opal-harvest-articles` (empty, retire candidate); no `market-updates` tool (one test draft).

## (d) Contracts

```json
{
  "contract_id": "dynamodb/dynamodb/opal-news-articles",
  "bucket": "none (DynamoDB us-east-1, account 313476888478)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "opal-news-articles",
  "grain": "one item per article URL per article_date (HASH article_date YYYY-MM-DD, RANGE url_hash N)",
  "partition": {"keys": ["article_date"], "claim": "measured"},
  "producer": {"name": "news-ingestion-scheduler (NewsAPI + RSS); finbert-batch-processor (sentiment_finbert*); legacy seeking-alpha-news-scraper / seeking-alpha-analysis-scraper (frozen 2026-04-13)", "schedule": "22 EventBridge rules news-api-* / news-rss-* (21 ENABLED, news-api-1100am DISABLED), e.g. cron(0 6,8,9,10,18,21,23,4 * * ? *); finbert-scoring-post-ingestion cron(10 2,4,12,14,16,17,18,20,21,22,23) + -45min cron(55 0,13,20), ENABLED", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-14", "basis": "trading-day-frontier", "trading_days_behind_t1": 0, "claim": "measured"},
  "size": {"objects": 381261, "bytes": 255062433, "rows_sampled": 1000, "days_with_items": 651, "per_day_sum": 381354, "claim": "measured"},
  "columns": [
    {"name": "article_date", "type": "S", "nullable": false, "description": "partition key, the article day YYYY-MM-DD", "example": "2026-10-13"},
    {"name": "url_hash", "type": "N", "nullable": false, "description": "sort key, numeric hash of url", "example": "19765875171689741"},
    {"name": "url", "type": "S", "nullable": false, "description": "article URL", "example": "https://<publisher>/<path>"},
    {"name": "title", "type": "S", "nullable": false, "description": "publisher headline (publisher text; never quote as Opal's view)", "example": "<headline>"},
    {"name": "summary", "type": "S", "nullable": false, "description": "feed summary (publisher text; may be empty)", "example": "<summary>"},
    {"name": "source", "type": "S", "nullable": false, "description": "publisher display name; 40+ values a day", "example": "Seeking Alpha"},
    {"name": "entity_type", "type": "S", "nullable": true, "description": "feed type, 950 of 1000 sampled", "example": "RSS"},
    {"name": "query_set", "type": "S", "nullable": true, "description": "NewsAPI query set; absent on RSS items", "example": "primary"},
    {"name": "published_date", "type": "S", "nullable": true, "description": "RFC-2822 publish time from the feed (943 of 1000)", "example": "Wed, 26 Aug 2026 11:58:40 -0400"},
    {"name": "ingestion_timestamp", "type": "S", "nullable": true, "description": "UTC ingest time (943 of 1000)", "example": "2026-10-14T10:01:07Z"},
    {"name": "sentiment_finbert", "type": "N", "nullable": true, "description": "FinBERT score (972 of 1000)", "example": "0"},
    {"name": "sentiment_finbert_label", "type": "S", "nullable": true, "description": "positive / negative / neutral", "example": "neutral"},
    {"name": "sentiment_finbert_confidence", "type": "N", "nullable": true, "description": "FinBERT confidence 0-1", "example": "0.7087"},
    {"name": "sentiment_gpt, sentiment_gpt_label, sentiment_gpt_model, sentiment_gpt_at", "type": "N/S", "nullable": true, "description": "GPT gap-fill sentiment (33 of 1000)", "example": "<label>"},
    {"name": "published_at, ingested_at, author, source_feed, published_raw, tags, sentiment_* (finsen polarity/coverage, bull_bear, risk_appetite, legal_risk, ...), ttl", "type": "S/N/L", "nullable": true, "description": "LEGACY shape (57 of 1000; 50 with the multi-axis sentiment set); published_at is what feeds the sparse GSI", "example": "2025-11-25T12:01:06Z"},
    {"name": "full_text, content_type, categories, fetch_method, embedding_384", "type": "S/S/L/S/L", "nullable": true, "description": "Seeking Alpha scraper items only (7 of 1000; embedding 25 of 1000). full_text is article body: never serve verbatim", "example": "<body text>"}
  ],
  "enums": {"entity_type": ["RSS", "NEWSAPI"], "query_set": ["primary", "secondary-a", "secondary-b", "<absent>"], "sentiment_finbert_label": ["positive", "negative", "neutral"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- market news, not client data; Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none (source is the publisher, not a custodian)", "values": []}
  },
  "nl_tags": ["news", "articles", "headlines", "coverage", "press", "what happened", "news sentiment", "finbert"],
  "common_queries": ["Any news on rate cuts today?", "What was the coverage on tariffs this week?", "How many articles did we ingest yesterday and from which sources?", "What share of yesterday's articles were negative?"],
  "existing_gateway_tool": {"name": "none (catalog row `news` names the table; no tool reads it)", "verdict": "none"},
  "proposed_tools": [{"name": "news_search_articles", "inputs": {"date_from": "YYYY-MM-DD", "date_to": "YYYY-MM-DD (<=14 days)", "text": "", "source": "", "sentiment_label": "", "limit": "50"}, "returns": "articles (published, source, title, url, finbert label/score) + per-day counts + items scanned", "answers": ["Any news on rate cuts today?", "What was the coverage on tariffs this week?", "How many articles did we ingest yesterday and from which sources?"]}],
  "catalog_entry": {"data_catalog_key": "news (DATA_CATALOG.yaml:867, tables.articles)", "present": true},
  "prior_art": "workflows/atom_decomposition/runs/news-subsystem/20260811T2330Z/rectangle.final.certified.json (producer of news.01/02 reads this table; table itself not decomposed)",
  "open_items": [
    "Not keyed by security: no ticker/security column; a ticker answer is a title/summary text match and must say so",
    "GSI source_date_index is SPARSE (9,905 of 381,261) and covers only the legacy published_at shape; newest 2026-04-13 (Seeking Alpha News), most sources end 2025-11. A tool must never query it for current news",
    "Two item shapes coexist (943 ingestion-shape vs 57 legacy of 1000 sampled); 5,002 items carry article_date 2023-10-13..2025-11-30 (backfill)",
    "ttl attribute present on 50 of 1000 sampled items but table TTL is DISABLED: never enforced (inferred)",
    "Catalog row sizes stale: '298K items; one day ~350' -> 381,261 and 985-1,229 per weekday (2026-09-25..10-13); extend the row",
    "Today's partition is partial until the 23:00 ET run; T-1 is the complete day"
  ],
  "evidence": [
    {"read": "describe_table opal-news-articles", "at": "2026-10-14T12:56:59Z"},
    {"read": "query article_date=<d> Select=COUNT, 2023-01-01..2026-10-14", "at": "2026-10-14T13:00:34Z..13:10:18Z"},
    {"read": "scan Segment 0..19 of 20 Limit=50 (attribute union)", "at": "2026-10-14T13:0xZ"},
    {"read": "query 2026-10-12..14 projected source,entity_type,query_set,label", "at": "2026-10-14T13:0xZ"},
    {"read": "events list_targets_by_rule (155 rules)", "at": "2026-10-14T13:01:15Z"}
  ]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/opal-news-trending-daily",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "opal-news-trending-daily",
  "grain": "one item per ranked trending topic per day: HASH date, RANGE topic_rank in bullish-1..10 / bearish-1..10 (20 a day; a later same-day run overwrites the same keys)",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "news-trending-analysis (TRENDING_TABLE); opal-news-layer3-curation also names it as TARGET_TABLE (rule layer3-gpt-curation-daily DISABLED)", "schedule": "news-trending-analysis-daily cron(15 11,21 * * ? *) ENABLED", "claim": "measured"},
  "freshness": {"latest_partition": "2026-10-14", "basis": "trading-day-frontier", "trading_days_behind_t1": 0, "claim": "measured"},
  "size": {"objects": 5814, "bytes": 40239871, "rows_sampled": 5780, "days_with_items": "314 of 318 (missing 2025-12-08, 12-09, 12-31, 2026-01-01)", "claim": "measured"},
  "columns": [
    {"name": "date", "type": "S", "nullable": false, "description": "partition key YYYY-MM-DD", "example": "2026-10-14"},
    {"name": "topic_rank", "type": "S", "nullable": false, "description": "sort key side-rank", "example": "bearish-1"},
    {"name": "headline, subtext, analysis, initial_analysis, rationale, market_implication", "type": "S", "nullable": true, "description": "GPT-written topic text (machine-written; may be empty strings)", "example": "<generated text>"},
    {"name": "raw_keyword, original_keyword, topic_name", "type": "S", "nullable": true, "description": "topic keyword the cluster was built on (topic_name often empty)", "example": "inheritance"},
    {"name": "trending_score, velocity, avg_quality_score, avg_time_decay, avg_escalation_score, layer2_trending_rank", "type": "N", "nullable": false, "description": "ranking inputs", "example": "7.5"},
    {"name": "momentum", "type": "S", "nullable": false, "description": "trend direction word", "example": "steady"},
    {"name": "article_count, source_count", "type": "N", "nullable": false, "description": "cluster size", "example": "10"},
    {"name": "sources", "type": "L<S>", "nullable": false, "description": "publisher names", "example": "[\"MarketWatch\"]"},
    {"name": "top_articles", "type": "L<M>", "nullable": false, "description": "cluster articles (url, title, ...); up to ~5 KB", "example": "[{url, title, ...}]"},
    {"name": "citations", "type": "L", "nullable": true, "description": "citation strings", "example": "[]"},
    {"name": "sentiment", "type": "M", "nullable": false, "description": "multi-axis sentiment map (positive_negative, emotional_intensity, risk_appetite, ...)", "example": "{positive_negative: 0, ...}"},
    {"name": "affected_tickers, affected_sectors", "type": "L", "nullable": false, "description": "EMPTY on every item since 2026-02 (0 of 618 in the last 30 days)", "example": "[]"},
    {"name": "confidence_level", "type": "S", "nullable": false, "description": "low / medium / high", "example": "medium"},
    {"name": "gpt_model", "type": "S", "nullable": true, "description": "model that wrote the text; gpt-4o to 2026-09, gpt-5.6-sol from 2026-09 (399 of 599 Sep items)", "example": "gpt-5.6-sol"},
    {"name": "enhancement_metadata", "type": "M", "nullable": true, "description": "curation metadata, often empty", "example": "{}"},
    {"name": "created_at", "type": "S", "nullable": false, "description": "UTC write time of the item (the vintage to quote)", "example": "2026-10-14T11:20:57Z"}
  ],
  "enums": {"topic_rank": ["bullish-1..bullish-10", "bearish-1..bearish-10"], "confidence_level": ["low", "medium", "high"], "gpt_model": ["gpt-4o", "gpt-5.1", "gpt-5.6-sol", "<absent>"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- market-wide, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["trending", "themes", "what's moving", "bullish themes", "bearish themes", "hot topics", "news trends"],
  "common_queries": ["What themes are trending today?", "What are the top bearish stories this morning?", "Has the tariff theme been trending all week?"],
  "existing_gateway_tool": {"name": "none (catalog row `news` names it; served copy json/trending/latest.json is in row `market_regime_trending`, read by tools/portal_lookup.py, not a gateway tool)", "verdict": "none"},
  "proposed_tools": [{"name": "news_trending_topics", "inputs": {"date": "YYYY-MM-DD (default today, else T-1)", "side": "bullish|bearish|all", "days": "1-30", "match": ""}, "returns": "ranked topics with headline, keyword, score, momentum, sources, citations, sentiment, gpt_model, created_at; for days>1 one row per (date, rank) matching `match`", "answers": ["What themes are trending today?", "What are the top bearish stories this morning?", "Has the tariff theme been trending all week?"]}],
  "catalog_entry": {"data_catalog_key": "news (DATA_CATALOG.yaml:887, tables.trending)", "present": true},
  "prior_art": "none for the table; news.03 prior art covers its keyword-sentiments.json side output",
  "open_items": [
    "Not ticker-keyed in practice: affected_tickers empty since 2026-02; do not offer 'trending names' from this table",
    "The text is machine-written; the model changed in 2026-09, so a multi-month theme history mixes two writers -- the tool returns gpt_model per row",
    "Two runs a day write the same 20 keys: the morning answer is overwritten at ~21:15Z; quote created_at",
    "irpt-narrative reads this table (role irpt-narrative-role) -- a second consumer to keep in mind for any shape change"
  ],
  "evidence": [
    {"read": "describe_table opal-news-trending-daily", "at": "2026-10-14T12:56:59Z"},
    {"read": "query date=<d> Select=COUNT and projected affected_tickers,gpt_model, 2025-12-01..2026-10-14", "at": "2026-10-14T13:0xZ-13:10Z"},
    {"read": "get_role_policy irpt-narrative-role/irpt-narrative-news-read", "at": "2026-10-14T13:3xZ"}
  ]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/semantic-news-trending-daily",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "semantic-news-trending-daily",
  "grain": "one item per semantic theme per day: HASH date, RANGE topic_rank (bullish-n / bearish-n)",
  "partition": {"keys": ["date"], "claim": "measured"},
  "producer": {"name": "semantic-news-layer3-curation (inferred from name; no table env var) over news-semantic-clustering output", "schedule": "none: no EventBridge rule or Scheduler schedule targets the semantic Lambdas", "claim": "inferred"},
  "freshness": {"latest_partition": "2026-02-24", "basis": "trading-day-frontier", "trading_days_behind_t1": 160, "claim": "measured"},
  "size": {"objects": 113, "bytes": 242721, "rows_sampled": 50, "days_with_items": "12 (2026-02-13..2026-02-24)", "claim": "measured"},
  "columns": [
    {"name": "date", "type": "S", "nullable": false, "description": "partition key", "example": "2026-02-18"},
    {"name": "topic_rank", "type": "S", "nullable": false, "description": "sort key", "example": "bearish-1"},
    {"name": "headline, analysis, cluster_synthesis", "type": "S", "nullable": false, "description": "GPT-written theme text", "example": "<generated text>"},
    {"name": "sentiment_score", "type": "N", "nullable": false, "description": "theme sentiment", "example": "-0.69005"},
    {"name": "confidence", "type": "N", "nullable": false, "description": "0-1", "example": "0.86"},
    {"name": "article_count", "type": "N", "nullable": false, "description": "articles in the theme", "example": "10"},
    {"name": "selected_articles", "type": "L<M>", "nullable": false, "description": "articles (title, ...)", "example": "[{title, ...}]"},
    {"name": "source_clusters", "type": "L<N>", "nullable": false, "description": "cluster ids from semantic_clusters/<date>.json", "example": "[377, 399]"},
    {"name": "top_sources, citations", "type": "L<S>", "nullable": false, "description": "publishers and citation strings", "example": "[\"Decrypt\"]"},
    {"name": "curation_method", "type": "S", "nullable": false, "description": "method tag", "example": "semantic_synthesis"},
    {"name": "generated_at", "type": "S", "nullable": false, "description": "UTC write time", "example": "2026-02-18T14:16:13Z"}
  ],
  "enums": {"curation_method": ["semantic_synthesis"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- market-wide, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["semantic trending", "themes", "news clusters"],
  "common_queries": ["What semantic themes were trending in late February?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "news.hazards ('semantic-news-trending-daily dormant since Feb-26 ... do not serve')", "present": true},
  "prior_art": "none",
  "open_items": [
    "FROZEN 160 trading days; no tool proposed. The decision is revive (schedule the 3 semantic Lambdas) or retire (table + news-v2 semantic_clusters/ 476 MB + portal-v2 json/semantic-trending/latest.json) -- Andrew's call via the CTO",
    "Catalog hazard says 'since Feb-26'; measured newest partition 2026-02-24"
  ],
  "evidence": [
    {"read": "describe_table semantic-news-trending-daily", "at": "2026-10-14T12:56:59Z"},
    {"read": "query date=<d> Select=COUNT 2026-01-01..2026-10-14 (113 of 113)", "at": "2026-10-14T13:0xZ"}
  ]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/opal-harvest-articles",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "opal-harvest-articles",
  "grain": "declared: one item per article per security (HASH security_key, RANGE published_at); no item exists",
  "partition": {"keys": ["security_key"], "claim": "measured"},
  "producer": {"name": "none found: no Lambda env names it as a write target; the only env reference is opal-amgt-scoped-api HARVEST_ARTICLES_TABLE (a reader)", "schedule": "none", "claim": "measured"},
  "freshness": {"latest_partition": "none (empty)", "basis": "trading-day-frontier", "claim": "measured"},
  "size": {"objects": 0, "bytes": 0, "rows_sampled": 0, "claim": "measured"},
  "columns": [
    {"name": "security_key", "type": "S", "nullable": false, "description": "declared hash key", "example": "<ROOT>_<CC>_Equity"},
    {"name": "published_at", "type": "S", "nullable": false, "description": "declared range key", "example": "2026-10-01T00:00:00Z"},
    {"name": "platform", "type": "S", "nullable": false, "description": "declared GSI platform_date_index key (publisher platform, not a custodian)", "example": "<platform>"},
    {"name": "ticker", "type": "S", "nullable": false, "description": "declared GSI ticker_date_index key", "example": "<ticker>"}
  ],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- Opal-internal research store", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "platform (publisher platform, declared only)", "values": []}
  },
  "nl_tags": ["harvest articles"],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md section 2.1 (0 items, 'wired in the Lambda env, empty')",
  "open_items": [
    "EMPTY confirmed: scan Select=COUNT Count 0 / ScannedCount 0, describe ItemCount 0, both GSIs 0 (2026-10-14 13:1xZ); matches the 12:2xZ read",
    "RETIRE-CANDIDATE: the coverage route now reads the S3 pool (infra/aws/terraform/harvest/scoped-amgt-api.tf:332, AMGT-rj-10) yet the env still sets HARVEST_ARTICLES_TABLE (:510). Disposition is the AMGT_RESAPP owner's; no act taken",
    "The harvest's article-to-security index is the S3 gold article_security_mention (G1), not this table"
  ],
  "evidence": [
    {"read": "describe_table opal-harvest-articles", "at": "2026-10-14T12:56:59Z"},
    {"read": "scan Select=COUNT opal-harvest-articles", "at": "2026-10-14T13:1xZ"},
    {"read": "infra/aws/terraform/harvest/dynamodb.tf:19,46; scoped-amgt-api.tf:332,510", "at": "2026-10-14T13:3xZ"}
  ]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/seeking-alpha-article-urls",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "seeking-alpha-article-urls",
  "grain": "one item per discovered Seeking Alpha article id per run day: HASH run_date ('YYYY-MM-DD' for analysis, 'YYYY-MM-DD_news' for news), RANGE article_id",
  "partition": {"keys": ["run_date"], "claim": "measured"},
  "producer": {"name": "seeking-alpha-news-coordinator / -news-dedup (news family); seeking-alpha-analysis-dedup / -analysis-listing-parser (analysis family); DEDUP_TABLE env", "schedule": "seeking-alpha-news-daily cron(0 14) DISABLED; seeking-alpha-analysis-daily cron(0 21) DISABLED", "claim": "measured"},
  "freshness": {"latest_partition": "2026-04-13", "basis": "trading-day-frontier", "trading_days_behind_t1": 127, "claim": "measured"},
  "size": {"objects": 50648, "bytes": 7421714, "rows_sampled": 1000, "news_items": 14068, "analysis_items": 36580, "claim": "measured"},
  "columns": [
    {"name": "run_date", "type": "S", "nullable": false, "description": "partition key; suffix _news marks the news family", "example": "2026-04-12_news"},
    {"name": "article_id", "type": "S", "nullable": false, "description": "sort key, SA numeric id", "example": "4505476"},
    {"name": "url", "type": "S", "nullable": false, "description": "SA URL", "example": "https://seekingalpha.com/news/<id>"},
    {"name": "discovered_at", "type": "S", "nullable": false, "description": "UTC discovery time", "example": "2026-04-12T14:01:51Z"},
    {"name": "content_type", "type": "S", "nullable": true, "description": "news family only", "example": "news"},
    {"name": "categories", "type": "L<S>", "nullable": true, "description": "SA categories, news family only", "example": "[\"Budget/Regulation\"]"},
    {"name": "found_by_chunk", "type": "N", "nullable": true, "description": "listing chunk index, analysis family (455 of 1000)", "example": "3"}
  ],
  "enums": {"content_type": ["news", "<absent>"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- vendor URL ledger, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["seeking alpha", "article urls", "dedup ledger"],
  "common_queries": ["Which Seeking Alpha articles did the old scraper discover in March?"],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "none",
  "open_items": [
    "A dedup ledger, not a content store: no tool proposed. FROZEN 127 trading days with both rules DISABLED",
    "The news coordinator kept running after the last discovery: news-av manifests to 2026-07-30 report urls_discovered 0 (read 07-30 and 04-14; 04-13 read 402). Silent zero-yield for ~75 trading days (127 - 52) before the rule was disabled (when disabled: not measured)",
    "Seeking Alpha is now collected by the AMGT harvest (opal-data-harvest seeking-alpha/harvest/, newest 2026-10-12) -- retire-or-revive decision for this chain belongs to the news pipeline owner"
  ],
  "evidence": [
    {"read": "describe_table seeking-alpha-article-urls", "at": "2026-10-14T12:56:59Z"},
    {"read": "query run_date=<d> and <d>_news Select=COUNT 2026-01-01..2026-10-14", "at": "2026-10-14T13:0xZ-13:10Z"},
    {"read": "s3 get seeking-alpha/news/manifests/{2026-04-13,2026-04-14,2026-07-30}/dedup_report.json", "at": "2026-10-14T13:3xZ"}
  ]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/opal-keyword-intelligence",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "opal-keyword-intelligence",
  "grain": "one item per topic keyword per generation day: HASH keyword, RANGE generated_date; GSI date-index (generated_date, keyword)",
  "partition": {"keys": ["keyword", "generated_date"], "claim": "measured"},
  "producer": {"name": "keyword-intelligence-generator (INTELLIGENCE_TABLE; reads opal-news-articles; OpenAI secret opal/openai/news-trending)", "schedule": "own rule keyword-intelligence-generator-daily DISABLED; rows land daily (~20 per run, 37-40 a day), so it is invoked by another function -- news-ingestion-lambda-role holds InvokeFunction on it; caller inferred to be news-trending-analysis", "claim": "inferred"},
  "freshness": {"latest_partition": "2026-10-14", "basis": "trading-day-frontier", "trading_days_behind_t1": 0, "claim": "measured"},
  "size": {"objects": 4735, "bytes": 28642658, "rows_sampled": 50, "days_with_items": "197 of 234 since 2026-02-23 (37 gap days, all in 2026-04-11..05-27)", "claim": "measured"},
  "columns": [
    {"name": "keyword", "type": "S", "nullable": false, "description": "hash key, free-text topic (not a ticker)", "example": "pentagon ai deal"},
    {"name": "generated_date", "type": "S", "nullable": false, "description": "range key YYYY-MM-DD", "example": "2026-03-04"},
    {"name": "generated_at, cloud_generated_at", "type": "S", "nullable": true, "description": "UTC write time (the vintage to quote)", "example": "2026-03-04T13:33:52Z"},
    {"name": "headline_summary, pattern_explanation, counterarguments, confidence_reason, web_context_note", "type": "S", "nullable": false, "description": "GPT-written brief", "example": "<generated text>"},
    {"name": "sentiment_label", "type": "S", "nullable": false, "description": "Bullish / Bearish / ...", "example": "Bearish"},
    {"name": "sentiment_score", "type": "N", "nullable": false, "description": "-1..1", "example": "-0.6719"},
    {"name": "sentiment_pattern", "type": "S", "nullable": false, "description": "pattern tag", "example": "breakout_driven"},
    {"name": "confidence", "type": "S", "nullable": false, "description": "low / medium / high", "example": "high"},
    {"name": "key_drivers", "type": "L<M>", "nullable": false, "description": "driver descriptions", "example": "[{description}]"},
    {"name": "articles", "type": "L<M>", "nullable": false, "description": "supporting articles (source, published, title, url)", "example": "[{source, published, title, url}]"},
    {"name": "article_count", "type": "N", "nullable": false, "description": "articles behind the brief", "example": "10"},
    {"name": "signal_conflict", "type": "M", "nullable": true, "description": "detected + resolution (21 of 50)", "example": "{detected: true, resolution}"},
    {"name": "web_enriched, web_queries", "type": "BOOL / L<S>", "nullable": false, "description": "whether web search was used, and the queries", "example": "true"},
    {"name": "inputs_fingerprint", "type": "S", "nullable": true, "description": "input hash (14 of 50)", "example": "<hash>"}
  ],
  "enums": {"confidence": ["low", "medium", "high"], "sentiment_label": ["Bullish", "Bearish", "<others not enumerated: 50-item sample>"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- market-wide, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["keyword intelligence", "topic sentiment", "why is sentiment", "drivers", "counterarguments", "news sentiment"],
  "common_queries": ["Why is sentiment on AI capex bearish?", "What are the counterarguments on the tariff story?", "Which topics got an intelligence brief today?"],
  "existing_gateway_tool": {"name": "none (catalog row `news` tables.keywords names it)", "verdict": "none"},
  "proposed_tools": [{"name": "news_keyword_intelligence", "inputs": {"keyword": "", "date": "YYYY-MM-DD"}, "returns": "brief per keyword: summary, sentiment label/score/pattern, drivers, counterarguments, confidence, articles, generated_at", "answers": ["Why is sentiment on AI capex bearish?", "What are the counterarguments on the tariff story?", "Which topics got an intelligence brief today?"]}],
  "catalog_entry": {"data_catalog_key": "news (DATA_CATALOG.yaml:886, tables.keywords)", "present": true},
  "prior_art": "rectangle.final.certified.json news.01 notes: the portal KeywordSentimentModal renders getKeywordIntelligence (portal side of this table; API route not traced here)",
  "open_items": [
    "Keyword is free text: an exact-match key; a tool needs the day's keyword list (GSI date-index) before a keyword lookup",
    "Machine-written briefs (web-enriched): a tool must label them as generated, with generated_at"
  ],
  "evidence": [
    {"read": "describe_table opal-keyword-intelligence", "at": "2026-10-14T12:56:59Z"},
    {"read": "query date-index generated_date=<d> Select=COUNT 2026-01-01..2026-10-14", "at": "2026-10-14T13:0xZ"},
    {"read": "get_role_policy news-ingestion-lambda-role/keyword-intelligence-dynamodb-and-invoke", "at": "2026-10-14T13:3xZ"}
  ]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/market-updates",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "market-updates",
  "grain": "one item per authored market update (HASH update_id); GSI CreatedByIndex (created_by, created_at)",
  "partition": {"keys": ["update_id"], "claim": "measured"},
  "producer": {"name": "not resolved (tags pipeline=market-overview, System=MarketOverview); no Lambda env names it", "schedule": "none found", "claim": "inferred"},
  "freshness": {"latest_partition": "2026-01-21", "basis": "trading-day-frontier", "trading_days_behind_t1": 183, "claim": "measured"},
  "size": {"objects": 1, "bytes": 300, "rows_sampled": 1, "claim": "measured"},
  "columns": [
    {"name": "update_id", "type": "S", "nullable": false, "description": "MARKET-UPDATE-<yyyymmdd>-<hhmmss>", "example": "MARKET-UPDATE-20260121-220136"},
    {"name": "created_by", "type": "S", "nullable": false, "description": "author email (staff; not client data)", "example": "<staff email>"},
    {"name": "created_at", "type": "S", "nullable": false, "description": "ISO time", "example": "2026-01-21T22:01:36"},
    {"name": "status", "type": "S", "nullable": false, "description": "draft / ...", "example": "draft"},
    {"name": "generated_content, edited_content, market_metrics, selected_topics", "type": "M", "nullable": true, "description": "update body parts", "example": "{}"},
    {"name": "selected_earnings, selected_macro", "type": "L", "nullable": true, "description": "selections", "example": "[]"},
    {"name": "ttl", "type": "N", "nullable": false, "description": "epoch expiry (TTL ENABLED)", "example": "1800568896"}
  ],
  "enums": {"status": ["draft"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- Opal-internal authoring table", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["market update"],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "news.hazards ('market-updates empty -- do not serve')", "present": true},
  "prior_art": "none",
  "open_items": ["Catalog says empty; measured 1 item, a test draft. Effectively empty; no tool. Retire-candidate for the market-overview owner"],
  "evidence": [{"read": "describe_table + scan Limit=50 market-updates", "at": "2026-10-14T12:56:59Z"}]
}
```

```json
{
  "contract_id": "dynamodb/dynamodb/opal-harvest-security-metrics",
  "bucket": "none (DynamoDB us-east-1)",
  "s3_prefix": "none",
  "layer": "dynamodb",
  "format": "dynamodb",
  "table": "opal-harvest-security-metrics",
  "grain": "one item per (axis, as-of date, generation, ticker): HASH axis_date '<AXIS>#<date>[#<generation>]', RANGE ticker; plus generation_pointer items (record_type) per axis-date",
  "partition": {"keys": ["axis_date"], "claim": "measured"},
  "producer": {"name": "AMGT_RESAPP chatter/price axis job (infra/aws/terraform/harvest/chatter-axis-schedule.tf; daily 10:00 UTC clock trigger per its comment); read by opal-amgt-scoped-api /lead-panel routes", "schedule": "daily (TRENDING_CHATTER generations stamped ~10:00Z; price generations ~11:0xZ)", "claim": "inferred"},
  "freshness": {"latest_partition": "TRENDING_CHATTER#2026-10-14; TRENDING_PRICE_90D#2026-10-13", "basis": "trading-day-frontier", "trading_days_behind_t1": 0, "claim": "measured"},
  "size": {"objects": 6845, "bytes": 3646892, "rows_sampled": 992, "claim": "measured"},
  "columns": [
    {"name": "axis_date", "type": "S", "nullable": false, "description": "hash key", "example": "TRENDING_PRICE_90D#2026-10-13#20261014T110718Z-a41dd910e684"},
    {"name": "ticker", "type": "S", "nullable": false, "description": "range key, Bloomberg-style ticker", "example": "2317 TT"},
    {"name": "axis", "type": "S", "nullable": false, "description": "axis name", "example": "PRICE"},
    {"name": "rank, rank_sort, score", "type": "N/S/N", "nullable": true, "description": "rank within the generation; GSI axis-rank-index sorts on rank_sort", "example": "21 / 00021 / -4.5627"},
    {"name": "px_start, px_end, px_start_date, px_end_date, trading_days_observed, window_days", "type": "N/S", "nullable": true, "description": "price-window figures (price axes)", "example": "263 / 251 / 2026-08-11 / 2026-09-10 / 23 / 30"},
    {"name": "raw_chatter_count, window_total_count, movement, movement_basis, movement_measure, movement_raw_score", "type": "N/S", "nullable": true, "description": "chatter-axis figures", "example": "<n>"},
    {"name": "security_key, subject, identity_status", "type": "S", "nullable": true, "description": "identity of the ranked name (15 of 50)", "example": "<ROOT>_<CC>_Equity"},
    {"name": "record_type, generation_id, run_id, payload_hash, written_at, state, row_count, coverage_vintage, empty_reason", "type": "S/N/M", "nullable": true, "description": "generation_pointer bookkeeping items", "example": "generation_pointer"},
    {"name": "source, as_of_date, computed_at", "type": "S", "nullable": true, "description": "provenance", "example": "bloomberg-dapi / 2026-09-10 / 2026-09-11T18:27Z"}
  ],
  "enums": {"axis prefixes (992-item sample)": ["BREAKOUT_PRICE", "BREAKOUT_PRICE_90D", "BREAKOUT_PRICE_365D", "TRENDING_PRICE", "TRENDING_PRICE_90D", "TRENDING_PRICE_365D", "TRENDING_CHATTER", "BREAKOUT_CHATTER", "PRICE"], "record_type": ["generation_pointer", "<absent>"]},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- covered-universe rankings, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["trending names", "breakout names", "chatter ranking", "most talked about stocks", "price breakout"],
  "common_queries": ["Which covered names are trending on chatter today?", "Which names broke out on price over 90 days?"],
  "existing_gateway_tool": {"name": "none (served by opal-amgt-scoped-api /lead-panel/rankings/*; G1 proposes the platinum harvest tool that calls that API)", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md section 2.1 (6,845 of 6,845 full scan)",
  "open_items": ["Answers 'trending NAMES on a day' -- the ticker-keyed ranking the news trending table cannot give. Route the tool to G1's platinum harvest tool (call the API, do not recompose), not a second news tool"],
  "evidence": [{"read": "describe_table + scan Segment 0..19 of 20 Limit=50 (axis census)", "at": "2026-10-14T12:56:59Z..13:10Z"}]
}
```

```json
{
  "contract_id": "opal-data-news-v2/gold/trending_reports",
  "bucket": "opal-data-news-v2",
  "s3_prefix": "trending_reports/",
  "layer": "gold",
  "format": "json",
  "table": "trending_reports",
  "grain": "one JSON object per trending-analysis run: trending_reports/<yyyy>/<mm>/<dd>/trending_report_<hhmmss>.json, plus latest.json",
  "partition": {"keys": ["yyyy", "mm", "dd"], "claim": "measured"},
  "producer": {"name": "news-trending-analysis (inferred: latest.json generated_at equals keyword-sentiments.json generated_at to the microsecond, 2026-10-14T11:18:06.275091Z)", "schedule": "news-trending-analysis-daily cron(15 11,21 * * ? *)", "claim": "inferred"},
  "freshness": {"latest_partition": "2026-10-14", "basis": "trading-day-frontier", "trading_days_behind_t1": 0, "claim": "measured"},
  "size": {"objects": 764, "bytes": 444763682, "rows_sampled": 1, "days": "311 (2025-12-01..2026-10-14)", "claim": "measured"},
  "columns": [
    {"name": "generated_at", "type": "string", "nullable": false, "description": "run time UTC", "example": "2026-10-14T11:18:06Z"},
    {"name": "analysis_window_days, decay_lambda", "type": "int/float", "nullable": false, "description": "run parameters", "example": "<n>"},
    {"name": "total_articles", "type": "int", "nullable": false, "description": "articles considered", "example": "<n>"},
    {"name": "filtering_system, sentiment_system", "type": "string", "nullable": false, "description": "method tags", "example": "<tag>"},
    {"name": "sentiment_sources", "type": "object", "nullable": false, "description": "finbert / gpt / none counts, gapfill flags", "example": "{finbert, gpt, none}"},
    {"name": "direction_judge", "type": "object", "nullable": false, "description": "GPT direction-judge counters (clusters, bullish, bearish, mixed, tokens, errors)", "example": "{...}"},
    {"name": "finbert_coverage", "type": "object", "nullable": false, "description": "scored / meaningful coverage pct", "example": "{...}"},
    {"name": "sentiment_breakdown", "type": "object", "nullable": false, "description": "bullish / bearish / neutral counts", "example": "{...}"},
    {"name": "<further fields>", "type": "", "nullable": true, "description": "top-level shape printed to 30 keys only (one object); the topic lists are not enumerated here", "example": ""}
  ],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- market-wide, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["trending report", "news run summary", "sentiment breakdown", "finbert coverage"],
  "common_queries": ["How many articles went into this morning's trending run, and what was the sentiment split?"],
  "existing_gateway_tool": {"name": "none (read by irpt-narrative via IAM grant trending_reports/*)", "verdict": "none"},
  "proposed_tools": [{"name": "news_trending_topics", "inputs": {"date": "YYYY-MM-DD"}, "returns": "run_meta block (total_articles, sentiment_breakdown, finbert_coverage, generated_at) beside the 20 topics", "answers": ["How many articles went into this morning's trending run, and what was the sentiment split?"]}],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "none",
  "open_items": ["Bucket is LIVE-no-DECLARED in the estate graph (not Terraform-managed)", "Field tree read from 1 object; a second run variant (pre-2026-09 model) not compared"],
  "evidence": [{"read": "list_objects_v2 opal-data-news-v2 trending_reports/ (764 of 764)", "at": "2026-10-14T13:12Z"}, {"read": "get_object trending_reports/latest.json (top-level shape)", "at": "2026-10-14T13:3xZ"}]
}
```

```json
{
  "contract_id": "opal-data-news-v2/gold/semantic_clusters",
  "bucket": "opal-data-news-v2",
  "s3_prefix": "semantic_clusters/",
  "layer": "gold",
  "format": "json",
  "table": "semantic_clusters",
  "grain": "one JSON per day semantic_clusters/<date>.json (17-40 MB), plus latest.json",
  "partition": {"keys": ["date (file name)"], "claim": "measured"},
  "producer": {"name": "news-semantic-clustering (OUTPUT_BUCKET opal-data-news-v2, OUTPUT_KEY semantic_clusters/latest.json)", "schedule": "none: no rule or schedule targets it", "claim": "measured"},
  "freshness": {"latest_partition": "2026-02-24", "basis": "trading-day-frontier", "trading_days_behind_t1": 160, "claim": "measured"},
  "size": {"objects": 13, "bytes": 476769338, "rows_sampled": 0, "claim": "measured"},
  "columns": [{"name": "<not read>", "type": "", "nullable": true, "description": "objects are 17-40 MB; not opened (a frozen tree gets no tool)", "example": ""}],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["semantic clusters"],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "none",
  "open_items": ["FROZEN with semantic-news-trending-daily; moves with that table's revive/retire decision (one chain, one freeze date)"],
  "evidence": [{"read": "list_objects_v2 opal-data-news-v2 (7,735 of 7,735)", "at": "2026-10-14T13:07:01Z"}]
}
```

```json
{
  "contract_id": "opal-data-news-av/silver/seeking-alpha",
  "bucket": "opal-data-news-av",
  "s3_prefix": "seeking-alpha/{news,analysis}/",
  "layer": "silver",
  "format": "json",
  "table": "seeking-alpha (news + analysis families)",
  "grain": "one JSON per scraped article: seeking-alpha/<family>/articles/<date>/article_<id>.json; plus batches, deduped-batches, layer3-batches and per-run manifests",
  "partition": {"keys": ["family", "kind", "date"], "claim": "measured"},
  "producer": {"name": "seeking-alpha-{news,analysis}-{coordinator,dedup,scraper} and -analysis-listing-parser (OUTPUT_BUCKET opal-data-news-av)", "schedule": "seeking-alpha-news-daily DISABLED; seeking-alpha-analysis-daily DISABLED", "claim": "measured"},
  "freshness": {"latest_partition": "2026-04-13 (articles); manifests to 2026-07-30 with 0 URLs", "basis": "trading-day-frontier", "trading_days_behind_t1": 127, "claim": "measured"},
  "size": {"objects": 10245, "bytes": 11636141, "news_articles": 5286, "analysis_articles": 2499, "rows_sampled": 0, "claim": "measured"},
  "columns": [{"name": "<article JSON not opened>", "type": "", "nullable": true, "description": "article bodies are publisher text; not read. Manifest dedup_report.json fields: run_date, pipeline, urls_discovered, new_articles, already_in_db, dedup_rate, batches_created, scrapers_triggered, duration_seconds, cost_saved_by_dedup", "example": ""}],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- vendor content, Opal-internal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["seeking alpha articles (legacy)"],
  "common_queries": [],
  "existing_gateway_tool": {"name": "none", "verdict": "none"},
  "proposed_tools": [],
  "catalog_entry": {"data_catalog_key": "", "present": false},
  "prior_art": "none",
  "open_items": ["FROZEN 127 trading days; superseded in practice by opal-data-harvest seeking-alpha/harvest/ (live to 2026-10-12). Retire-candidate with seeking-alpha-article-urls; no act taken", "Bucket LIVE-no-DECLARED (not Terraform-managed)"],
  "evidence": [{"read": "list_objects_v2 opal-data-news-av seeking-alpha/ (10,245 of 10,245, 11 pages)", "at": "2026-10-14T13:12Z"}]
}
```

```json
{
  "contract_id": "opal-data-portal-v2/served/news-trending-and-sentiment",
  "bucket": "opal-data-portal-v2",
  "s3_prefix": "json/trending/latest.json; json/sentiment/{fear-greed-index,keyword-sentiments}.json; json/sentiment/keyword-history-{summary,articles}/; json/semantic-trending/latest.json; sentiment/ (legacy)",
  "layer": "served",
  "format": "json",
  "table": "portal news singletons and families",
  "grain": "json/trending/latest.json: one day's top-10 bullish + top-10 bearish; fear-greed-index.json: current + 251-day history; keyword-sentiments.json: one run's keyword FinBERT set (44 keywords on 2026-10-14); keyword-history-*: one file per keyword (360 + 360, frozen)",
  "partition": {"keys": ["none (singletons) / keyword (families)"], "claim": "measured"},
  "producer": {"name": "opal-trending-topics-portal-publisher (json/trending, inferred); news-trending-analysis (keyword-sentiments); opal-portal-fear-greed-fetcher (fear-greed); opal-keyword-drilldown-generator (keyword-history, DISABLED); semantic-trending-topics-portal-publisher (json/semantic-trending, no schedule)", "schedule": "trending/keyword-sentiments ~11:2xZ and ~21:2xZ via news-trending-analysis-daily; fear-greed cron(30 14,21)", "claim": "inferred"},
  "freshness": {"latest_partition": "json/trending 2026-10-14 (data_as_of 2026-10-14); keyword-sentiments generated_at 2026-10-14T11:18:06Z; fear-greed generated_at 2026-10-13T21:30:41Z; keyword-history 2026-04-07 (131 behind); semantic-trending 2026-02-24 (160 behind)", "basis": "trading-day-frontier", "claim": "measured"},
  "size": {"objects": 729, "bytes": 4310754, "rows_sampled": 3, "claim": "measured"},
  "columns": [
    {"name": "json/trending/latest.json: generated_at, data_as_of, date, bullish[10], bearish[10]", "type": "object", "nullable": false, "description": "served trending lists", "example": "date=2026-10-14"},
    {"name": "keyword-sentiments.json: generated_at, days_back, total_articles_scanned, total_unique_keywords, keywords[]", "type": "object", "nullable": false, "description": "keyword FinBERT set", "example": "keywords[44]"},
    {"name": "fear-greed-index.json: current{value, description, last_update, previous_close, previous_1_week/month/year, components}, historical[251], generated_at, source, scale, components_info", "type": "object", "nullable": false, "description": "CNN Fear and Greed", "example": "historical[251]"}
  ],
  "enums": {},
  "fork_keys": {
    "firm": {"column_or_key_segment": "none -- market-wide, served to the portal", "values": []},
    "account": {"column": "none", "last4_derivation": "not applicable", "last4_collisions_within_firm": 0},
    "platform": {"column": "none", "values": []}
  },
  "nl_tags": ["fear and greed", "market mood", "sentiment", "trending today", "keyword sentiment"],
  "common_queries": ["What is the fear and greed index today?", "What is the market mood?", "What is trending on the portal today?"],
  "existing_gateway_tool": {"name": "gateway_query_catalog and opal_asker_query carry news.03.live-singletons as a catalog link (DATA_CATALOG.yaml:1453, :1858)", "verdict": "extend"},
  "proposed_tools": [{"name": "news_market_mood", "inputs": {}, "returns": "fear/greed current + history and the keyword FinBERT set, each with its generated_at", "answers": ["What is the fear and greed index today?", "What is the market mood?"]}],
  "catalog_entry": {"data_catalog_key": "sentiment_news_mood (:1069; artifacts news.01/02/03) and market_regime_trending (:565, paths.trending)", "present": true},
  "prior_art": "workflows/atom_decomposition/runs/news-subsystem/20260811T2330Z/rectangle.final.certified.json (news.01-04)",
  "open_items": [
    "G3 (portal-v2) owns the served-key diff; this block is the news-producer view. Measured today: json/sentiment/ still 722 keys (720 frozen at 2026-04-07 + 2 live), unchanged from the certified run",
    "news-trending-analysis env S3_KEY reads 'sentiment/keyword-sentiments.json' while the live write lands at json/sentiment/; the root sentiment/ copy (5 objects) last moved 2026-01-08 -- legacy residue",
    "Never join the frozen keyword-history families to the live singletons to draw a trend (prior art news.03 verdict)"
  ],
  "evidence": [
    {"read": "list_objects_v2 opal-data-portal-v2 json/sentiment/, sentiment/, json/trending/, json/semantic-trending/ and 5 empty prefixes", "at": "2026-10-14T13:07:01Z"},
    {"read": "get_object json/trending/latest.json, json/sentiment/keyword-sentiments.json, json/sentiment/fear-greed-index.json (top-level shape)", "at": "2026-10-14T13:3xZ"}
  ]
}
```

## (e) What could not be read, and why

- **Producer code was not read.** Write targets come from Lambda env vars and IAM grants; where a Lambda has no env var
  (`finbert-batch-processor`, the semantic and publisher Lambdas), the target is inferred from names, grants and
  same-minute writes. That covers which function invokes `keyword-intelligence-generator` and
  `opal-trending-topics-portal-publisher`. No CloudWatch logs or invoke history were read.
- **`opal-news-layer3-curation`:** its rule is DISABLED and it names the trending table, so it is dormant or invoked.
  Not resolved.
- **When the SA and keyword-drilldown rules were disabled:** not measured (CloudTrail not read).
- **`opal-news-articles` attributes** come from 1,000 sampled items of 381,261. Rare attributes outside the sample are not
  listed. The GSI per-source table covers 41 sources and 7,055 of 9,905 GSI items.
- **Not opened:** the semantic_clusters dumps (17-40 MB each) and the Seeking Alpha article JSONs. Both are frozen, and no
  tool is proposed on them. The `trending_reports` field tree comes from one object, cut at 30 top-level keys.
- **The portal API** that serves `opal-keyword-intelligence` (`getKeywordIntelligence`; candidate `sentiment_query_api`,
  nodejs18.x) was not traced.
- **The harvest overlap** compares Seeking Alpha ids only, over one 14-day window. The news table's other publishers
  (FT 23-29 a day, Bloomberg 3 on 10-13) were not joined to the harvest FT and Bloomberg silver tables. Id matching
  treats `/news/` and `/article/` ids as one id space. The disjointness also rests on the content-type split (harvest SA
  is `news`, the news table's SA is `article`).
- **Out of reach under the brief:** no surprise row was filed, because this part writes no file outside itself. The odd
  findings are in each contract's `open_items` for 4.0.0_SA_CRO~Z to route:
  - the sparse GSI;
  - the empty `affected_tickers`;
  - the zero-yield SA manifests;
  - `opal-harvest-articles` still in the env;
  - the stale catalog sizes;
  - the S3_KEY env/path mismatch.
