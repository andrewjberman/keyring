# G1 -- opal-data-harvest: data contracts per bucket -> table (gateway data-contract census)

**archetype:** EXPLORE

- **Author:** 4.0.0_SA_CRO~Z, 2026-10-14.
- **Directive:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485, group G1, due 20:00Z.
- **Andrew's word:** `ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md` (same folder).
- **Extends:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md` @eea2acd58e.
  Read that file for the method, the published-layer routes, the key table, the defects D1-D9 and the ASML worked example; they are not repeated here.
- **Read only:** no vendor call; Opal admin IAM; T-1 = 2026-10-13 (`lib/trading_calendar.py`).

## 1. Method and denominators

| read | instrument | denominator |
|---|---|---|
| every key | `list_objects_v2`, paginated, 2026-10-14 ~12:05Z | 59 pages, 58,639 of 58,639 keys, grouped into **78 datasets** |
| Parquet schema + rows | footer of every part (pyarrow) | 4,635 of 4,635 parts, 0 errors, 18 tables |
| JSON columns | top-level fields of the newest object per JSON dataset (ASML where present) | 1 object per dataset (a sample of 1) |
| keys per dataset | `security_key=` path segment or `<key>/` first segment | 32 keyed datasets, 251 distinct keys |
| catalog match | `DATA_CATALOG.yaml harvest_datasets` | 39 rows |

Contracts written: **78 of 78 datasets**.
- **47 research contracts** (sections 3-4): full columns, tags and tools.
- **31 plumbing or raw-store contracts** (section 5): size and freshness only; their columns are not read.

## 2. What the census changes in the catalog (the cleanup list)

1. **Catalog grain.**
   - 26 of 78 datasets have a catalog row at their own prefix.
   - 50 are covered only by a SOURCE-LEVEL row, for example one row for all of `bloomberg/harvest/` (13 tables, bronze and silver).
   - 2 have no row: `amgt/harvest/gold/ai_fill/` and `social/v1/`.
   - The tool index needs table rows, so split each source row into the table rows of section 3.
2. **`read_tool: null` on every harvest row.** The two deployed raw tools, `harvest_list` and `harvest_read` (app/harvest_read.py), are not in `tool_index` (67 tools at 43088464f5).
   - Add them as member b.
   - Point each research row at its typed tool below.
3. **Per-row fields the catalog lacks:** `grain`, `freshness_field`, rows, keys and the never-sum rules all read `NONE -- not read`. Section 3 measures each.
4. **Retire from tools (keep in the bucket):**
   - `publication-links/v1/` and `publications/v1/`: 3-ticker pilot stores of 2026-09-15, superseded by gold `article_security_mention`;
   - `amgt/harvest/gold/research-dossier/` (hyphen): an older generation of `research_dossier` (inferred).
5. **New since the 2026-10-13 listing:** `amgt/harvest/gold/ai_fill/` (95 objects, written 2026-10-14) and `amgt/harvest/bronze/research_template/`.

## 3. Tool registry (the 12 typed tools the contracts point at)

Every tool:
- admits through `harvest_read.admit()` (principal present, Opal user, served prefix) and writes one audit row;
- answers with `as_of`, `source_keys[]`, a denominator and `absent_reason`;
- projects to 50 KB by default;
- forks by **security**, not by firm: this is Opal's own research, served to Opal principals only (list v4). Firm, account-last-4 and platform do not apply.

```json
[
 {
  "name": "harvest_resolve_security",
  "inputs": {
   "query": "ticker, Bloomberg ticker, security_key, company or legal name, CIK, ISIN, SEDOL"
  },
  "returns": "status exact|candidates|none; security_key; display_ticker; bloomberg; name; cik; isin where held; other_listings[]; not_held[] (cusip)",
  "reads": "crosswalk/v1 newest, universe/v1 newest, bloomberg/harvest/bronze/identity newest per key; wraps lib/research/api/name_search.resolve_query",
  "answers": [
   "Which security is 'ASML'?",
   "What is the ISIN of X?"
  ]
 },
 {
  "name": "harvest_security_coverage",
  "inputs": {
   "security_key": "resolved key"
  },
  "returns": "per dataset: present, objects, newest stamp, trading_days_behind_t1; per layer totals",
  "reads": "one ListObjectsV2 per keyed prefix (about 30) + packs/<key>/input_ledger.json",
  "answers": [
   "What do we hold on X, and how fresh is each piece?"
  ]
 },
 {
  "name": "harvest_get_published_analysis",
  "inputs": {
   "security_key": "resolved key",
   "sections": "overlay|thesis|peers|ledger|versions|timeline (default overlay)"
  },
  "returns": "the published (portal) body per section, projected to 50 KB: header figures, posture, price movement and rank, chatter standing, peers, model cases with formula, dossier and drafted section titles, versions",
  "reads": "invokes opal-amgt-scoped-api (the live published layer; no second reader)",
  "answers": [
   "What does the portal's Security Analysis page say about X?"
  ]
 },
 {
  "name": "harvest_get_chatter",
  "inputs": {
   "security_key": "resolved key",
   "from_day": "YYYY-MM-DD",
   "to_day": "YYYY-MM-DD"
  },
  "returns": "daily rows (day, articles_total, tier_a..d, mention_score, trailing_7d/30d_sum, data_status, publishers_found_codes); windows 30/90/365 (articles_total, scored, voters, tone); events (first_day, last_day, articles_total, tier_a, publishers_distinct, lead_article_key)",
  "reads": "gold chatter_daily, chatter_window: NEWEST part of the newest partition only; chatter_event deduped on event_id",
  "answers": [
   "How much has the press written about X this month, and is the tone positive?"
  ]
 },
 {
  "name": "harvest_search_articles",
  "inputs": {
   "security_key": "resolved key",
   "publisher": "sa|bbg|wsj|ft|barrons (optional)",
   "from": "date",
   "to": "date",
   "min_tier": "A|B|C|D",
   "in_title": "bool",
   "limit": "25 default, 100 max"
  },
  "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
  "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
  "answers": [
   "Which articles mention X, newest first, with links and sentiment?"
  ]
 },
 {
  "name": "harvest_get_article",
  "inputs": {
   "article_key": "from a search",
   "publisher": "sa|bbg|wsj|ft|barrons",
   "include_text": "bool, default false"
  },
  "returns": "title, url, published_utc, words, content_status, mentioned security_keys; text/body_blocks only with include_text",
  "reads": "<publisher>/harvest/silver/article, newest record per article_key, partition located from the mention row's published date",
  "answers": [
   "Read me this article."
  ]
 },
 {
  "name": "harvest_get_fundamentals",
  "inputs": {
   "security_key": "resolved key",
   "kind": "model|consensus|reference|valuation_history|segments|price",
   "mnemonics": "list, optional",
   "fiscal_years": "list, optional"
  },
  "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
  "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
  "answers": [
   "What were X's revenue and EPS since 2016?",
   "What is consensus EPS next year?",
   "What is X's P/E history?"
  ]
 },
 {
  "name": "harvest_get_research",
  "inputs": {
   "security_key": "resolved key",
   "as_of": "optional",
   "fields": "optional list"
  },
  "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
  "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
  "answers": [
   "What is our thesis on X, why do we own it, and what are the risks?"
  ]
 },
 {
  "name": "harvest_get_filing_analysis",
  "inputs": {
   "security_key": "resolved key",
   "accession": "optional",
   "include_passages": "bool, default false"
  },
  "returns": "form, filing_date, items by category (guidance, segments, risks, commentary, big_bets, big_challenges) with citations; denominators; drafted sections; passages on request",
  "reads": "filings/v1 .analysis/.source, drafting/v1, sec/harvest/silver/filing_source",
  "answers": [
   "What guidance and risks did X give in its latest annual filing?"
  ]
 },
 {
  "name": "harvest_get_peers_and_scores",
  "inputs": {
   "security_key": "resolved key"
  },
  "returns": "peer members (name, ticker, country, sector, cap, factors, rung); scores (divergence, peers_v, robustness with status/reason); posture (verdict, books, weight_by_book)",
  "reads": "peers/v1 newest, scores/v1, posture/v1 newest",
  "answers": [
   "Who are X's peers and how does it compare?",
   "Do our funds hold X?"
  ]
 },
 {
  "name": "harvest_describe_dataset",
  "inputs": {
   "dataset": "contract_id or prefix; empty = the list"
  },
  "returns": "columns and types, grain, key, freshness rule, rows, newest stamp, never-sum rules, nl_tags",
  "reads": "this census's contracts, regenerated as a registry object (metadata only)",
  "answers": [
   "What columns does chatter_daily have?"
  ]
 },
 {
  "name": "harvest_query_columns",
  "inputs": {
   "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
   "columns": "list",
   "security_keys": "optional list",
   "filters": "[{column, op (= < > in), value}]",
   "order_by": "column [desc]",
   "limit": "50 default, 200 max"
  },
  "returns": "projected rows + the denominator scanned and the part/object read",
  "reads": "the newest part/object of the dataset, declared columns only",
  "answers": [
   "Top 20 names by 30-day chatter today?",
   "Every covered name's FY1 consensus P/E?",
   "Universe names in Health Care with earnings yield above 6%?"
  ]
 }
]
```

## 4. Research contracts (gold, silver, Bloomberg bronze)

### `amgt/harvest/gold/ai_fill/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.ai_fill",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/ai_fill/",
 "layer": "gold",
 "format": "json",
 "table": "ai_fill",
 "grain": "one object per security (overwritten)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": null,
  "schedule": null,
  "claim": "absent",
  "basis": "not traced"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "newest_write_utc": "2026-10-14T03:19:39Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 95,
  "bytes": 782991,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 95,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "blocks",
   "type": "object",
   "nullable": true
  },
  {
   "name": "generated_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "producer",
   "type": "object",
   "nullable": true
  },
  {
   "name": "schema",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "amgt/harvest/gold/ai_fill/security_key=ASML_NA_Equity/ai_fill.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "AI written summary",
  "management bio",
  "recent management news",
  "company description"
 ],
 "common_queries": [
  "Give me a short management bio for X with citations."
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_research",
   "inputs": {
    "security_key": "resolved key",
    "as_of": "optional",
    "fields": "optional list"
   },
   "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
   "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
   "answers": [
    "What is our thesis on X, why do we own it, and what are the risks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": null,
  "present": false,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "no DATA_CATALOG row: new since the 2026-10-13 listing",
  "no DATA_CATALOG harvest_datasets row covers this prefix"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object amgt/harvest/gold/ai_fill/security_key=ASML_NA_Equity/ai_fill.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `amgt/harvest/gold/article_security_mention/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.article_security_mention",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/article_security_mention/",
 "layer": "gold",
 "format": "parquet",
 "table": "article_security_mention",
 "grain": "one row per (article_key, security_key) in the NEWEST part; each part is a full snapshot",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/harvest/publication_gold.py (HVST-h-4 gold article_security_mention, AMGT_HARVST)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-08",
  "newest_write_utc": "2026-10-09T10:34:21Z",
  "trading_days_behind_t1": 3,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 24,
  "bytes": 67289102,
  "parquet_parts": 24,
  "rows_all_parts": 459334,
  "schema_variants": 6,
  "claim": "measured",
  "rows_newest_part": 52424,
  "articles_newest_part": 20868,
  "newest_part": "date=2026-10-08/part-20261009T093755Z.parquet",
  "duplicate_keys_in_newest_part": 0,
  "repeated_pairs_across_all_parts": 406584
 },
 "securities": {
  "distinct_keys": 234,
  "claim": "measured",
  "basis": "distinct security_key column values"
 },
 "columns": [
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "composite_figi",
   "type": "string",
   "nullable": true
  },
  {
   "name": "mention_count",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "mention_in_title",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "mention_in_lead",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "first_mention_block",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "blocks_hit",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "blocks_total",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "match_forms",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "vendor_tagged_primary",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "vendor_tagged_secondary",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "co_mentioned_securities",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "co_mention_count",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "is_roundup",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "signal_tier",
   "type": "string",
   "nullable": true
  },
  {
   "name": "signal_weight",
   "type": "double",
   "nullable": true
  },
  {
   "name": "published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "lag_hours",
   "type": "double",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "published_precision",
   "sentiment_content_key",
   "sentiment_finbert_label",
   "sentiment_finbert_score",
   "sentiment_scorer",
   "title",
   "url"
  ],
  "variant_only_count": 7
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "articles about a company",
  "news mentions",
  "which articles name",
  "press coverage list",
  "mentioned in headline"
 ],
 "common_queries": [
  "Which articles mention ASML, newest first?",
  "How many Bloomberg articles named X in the title this quarter?",
  "Which other companies are co-mentioned with X?"
 ],
 "never_sum_rules": [
  "never read rows as articles across securities: an article naming two securities has two rows",
  "read the newest part only (52,424 rows) never the prefix (459,334)"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_query_columns",
   "inputs": {
    "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
    "columns": "list",
    "security_keys": "optional list",
    "filters": "[{column, op (= < > in), value}]",
    "order_by": "column [desc]",
    "limit": "50 default, 200 max"
   },
   "returns": "projected rows + the denominator scanned and the part/object read",
   "reads": "the newest part/object of the dataset, declared columns only",
   "answers": [
    "Top 20 names by 30-day chatter today?",
    "Every covered name's FY1 consensus P/E?",
    "Universe names in Health Care with earnings yield above 6%?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_article_security_mention",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 24 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `amgt/harvest/gold/article_sentiment/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.article_sentiment",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/article_sentiment/",
 "layer": "gold",
 "format": "parquet",
 "table": "article_sentiment",
 "grain": "one row per scored article (article_key), FinBERT; parts are append batches",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/harvest/finbert_sentiment.py (gold article_sentiment, AMGT_HARVST)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-03",
  "newest_write_utc": "2026-10-03T21:24:20Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 5,
  "bytes": 2096262,
  "parquet_parts": 5,
  "rows_all_parts": 13235,
  "schema_variants": 1,
  "claim": "measured",
  "distinct_articles": 13235
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "label",
   "type": "string",
   "nullable": true
  },
  {
   "name": "confidence",
   "type": "double",
   "nullable": true
  },
  {
   "name": "score",
   "type": "double",
   "nullable": true
  },
  {
   "name": "scorer",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "scored_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "unscorable_reason",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "article sentiment",
  "positive negative neutral",
  "finbert score"
 ],
 "common_queries": [
  "Is the coverage of X positive or negative?",
  "What share of X's articles were negative last month?"
 ],
 "never_sum_rules": [
  "a score is a tone, not a quantity; average within a stated window only"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_query_columns",
   "inputs": {
    "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
    "columns": "list",
    "security_keys": "optional list",
    "filters": "[{column, op (= < > in), value}]",
    "order_by": "column [desc]",
    "limit": "50 default, 200 max"
   },
   "returns": "projected rows + the denominator scanned and the part/object read",
   "reads": "the newest part/object of the dataset, declared columns only",
   "answers": [
    "Top 20 names by 30-day chatter today?",
    "Every covered name's FY1 consensus P/E?",
    "Universe names in Health Care with earnings yield above 6%?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_article_sentiment",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 5 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `amgt/harvest/gold/candidate_universe/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.candidate_universe",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/candidate_universe/",
 "layer": "gold",
 "format": "json",
 "table": "candidate_universe",
 "grain": "one row per scanner universe name (rows[]) per date object; 2,856 rows in the 2026-10-02 object",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/peers/universe.py (candidate_universe_address, AMGT_RESAPP)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-02",
  "newest_write_utc": "2026-10-11T11:11:09Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 2,
  "bytes": 4759738,
  "claim": "measured",
  "rows_in_newest_object": 2856,
  "value_codes": 284
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "csc_member_codes",
   "type": "array",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "preset_retention_basis",
   "type": "string",
   "nullable": true
  },
  {
   "name": "preset_value_codes",
   "type": "array",
   "nullable": true
  },
  {
   "name": "read_failures",
   "type": "object",
   "nullable": true
  },
  {
   "name": "row_value_codes",
   "type": "array",
   "nullable": true
  },
  {
   "name": "rows",
   "type": "array",
   "nullable": true
  },
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "source",
   "type": "object",
   "nullable": true
  },
  {
   "name": "taxonomy_residue",
   "type": "object",
   "nullable": true
  },
  {
   "name": "vintage",
   "type": "string",
   "nullable": true
  },
  {
   "name": "vintages_distinct",
   "type": "array",
   "nullable": true
  },
  {
   "name": "vintages_per_file",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "amgt/harvest/gold/candidate_universe/date=2026-10-02/candidate_universe.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "stock screen",
  "universe",
  "valuation screen",
  "earnings yield",
  "market cap",
  "sector country screen",
  "candidate names"
 ],
 "common_queries": [
  "Which names in the universe are in Health Care with earnings yield above 6%?",
  "What is X's EV and market cap in the scanner?"
 ],
 "never_sum_rules": [
  "universe_weights are index weights per universe; never sum across universes"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_query_columns",
   "inputs": {
    "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
    "columns": "list",
    "security_keys": "optional list",
    "filters": "[{column, op (= < > in), value}]",
    "order_by": "column [desc]",
    "limit": "50 default, 200 max"
   },
   "returns": "projected rows + the denominator scanned and the part/object read",
   "reads": "the newest part/object of the dataset, declared columns only",
   "answers": [
    "Top 20 names by 30-day chatter today?",
    "Every covered name's FY1 consensus P/E?",
    "Universe names in Health Care with earnings yield above 6%?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_candidate_universe",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object amgt/harvest/gold/candidate_universe/date=2026-10-02/candidate_universe.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `amgt/harvest/gold/chatter_daily/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.chatter_daily",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/chatter_daily/",
 "layer": "gold",
 "format": "parquet",
 "table": "chatter_daily",
 "grain": "one row per (security_key, day) in the NEWEST part file of the newest date partition; each part is a full snapshot",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/harvest/publication_gold.py (HVST-h-5 gold chatter_daily, AMGT_HARVST)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-08",
  "newest_write_utc": "2026-10-09T10:41:19Z",
  "trading_days_behind_t1": 3,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 26,
  "bytes": 5137611,
  "parquet_parts": 26,
  "rows_all_parts": 1338296,
  "schema_variants": 4,
  "claim": "measured",
  "rows_newest_part": 68002,
  "newest_part": "date=2026-10-08/part-20261009T103423Z.parquet",
  "duplicate_keys_in_newest_part": 0
 },
 "securities": {
  "distinct_keys": 242,
  "claim": "measured",
  "basis": "distinct security_key column values"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "composite_figi",
   "type": "string",
   "nullable": true
  },
  {
   "name": "day",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "articles_total",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tier_a",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tier_b",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tier_c",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tier_d",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "mention_score",
   "type": "double",
   "nullable": true
  },
  {
   "name": "mention_count_total",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "publishers_distinct",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "trailing_7d_sum",
   "type": "double",
   "nullable": true
  },
  {
   "name": "trailing_30d_sum",
   "type": "double",
   "nullable": true
  },
  {
   "name": "baseline_30d_sum",
   "type": "double",
   "nullable": true
  },
  {
   "name": "baseline_30d_days",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "cumulative_ytd",
   "type": "double",
   "nullable": true
  },
  {
   "name": "first_published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "last_published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "data_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publishers_covered",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "publishers_enabled",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "publishers_covered_codes",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "publishers_found_codes",
   "type": "list<element: string>",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "news chatter",
  "media attention",
  "how much press",
  "mention score",
  "article count by day",
  "trailing 30 day chatter"
 ],
 "common_queries": [
  "How much has the press written about ASML each day this month?",
  "Which names have the highest 30-day chatter today?",
  "Is chatter for X above its 30-day baseline?"
 ],
 "never_sum_rules": [
  "never sum rows across part files: every part is a full snapshot (newest part holds 0 duplicate (security_key, day) pairs)",
  "data_status DENIED/PARTIAL means publishers were not all covered; 0 articles is not 'no chatter'"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_chatter",
   "inputs": {
    "security_key": "resolved key",
    "from_day": "YYYY-MM-DD",
    "to_day": "YYYY-MM-DD"
   },
   "returns": "daily rows (day, articles_total, tier_a..d, mention_score, trailing_7d/30d_sum, data_status, publishers_found_codes); windows 30/90/365 (articles_total, scored, voters, tone); events (first_day, last_day, articles_total, tier_a, publishers_distinct, lead_article_key)",
   "reads": "gold chatter_daily, chatter_window: NEWEST part of the newest partition only; chatter_event deduped on event_id",
   "answers": [
    "How much has the press written about X this month, and is the tone positive?"
   ]
  },
  {
   "name": "harvest_query_columns",
   "inputs": {
    "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
    "columns": "list",
    "security_keys": "optional list",
    "filters": "[{column, op (= < > in), value}]",
    "order_by": "column [desc]",
    "limit": "50 default, 200 max"
   },
   "returns": "projected rows + the denominator scanned and the part/object read",
   "reads": "the newest part/object of the dataset, declared columns only",
   "answers": [
    "Top 20 names by 30-day chatter today?",
    "Every covered name's FY1 consensus P/E?",
    "Universe names in Health Care with earnings yield above 6%?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_chatter_daily",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 26 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `amgt/harvest/gold/chatter_event/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.chatter_event",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/chatter_event/",
 "layer": "gold",
 "format": "parquet",
 "table": "chatter_event",
 "grain": "one row per chatter event (event_id): a run of days with clustered articles for one security",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/harvest/publication_gold.py (HVST-h-6 gold chatter_event, AMGT_HARVST)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-03",
  "newest_write_utc": "2026-10-03T23:09:53Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 10,
  "bytes": 150508,
  "parquet_parts": 10,
  "rows_all_parts": 576,
  "schema_variants": 1,
  "claim": "measured",
  "distinct_events": 528
 },
 "securities": {
  "distinct_keys": 69,
  "claim": "measured",
  "basis": "distinct security_key column values"
 },
 "columns": [
  {
   "name": "event_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "composite_figi",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_day",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "last_day",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "days_span",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "articles_total",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tier_a",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tier_b",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "publishers_distinct",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "lead_article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "lead_headline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_keys",
   "type": "list<element: string>",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "news events",
  "press spikes",
  "news bursts",
  "lead headline"
 ],
 "common_queries": [
  "When were the big news spikes for X this year?",
  "What article led the X news burst in July?"
 ],
 "never_sum_rules": [
  "event_id repeats across partitions; dedupe on event_id"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_chatter",
   "inputs": {
    "security_key": "resolved key",
    "from_day": "YYYY-MM-DD",
    "to_day": "YYYY-MM-DD"
   },
   "returns": "daily rows (day, articles_total, tier_a..d, mention_score, trailing_7d/30d_sum, data_status, publishers_found_codes); windows 30/90/365 (articles_total, scored, voters, tone); events (first_day, last_day, articles_total, tier_a, publishers_distinct, lead_article_key)",
   "reads": "gold chatter_daily, chatter_window: NEWEST part of the newest partition only; chatter_event deduped on event_id",
   "answers": [
    "How much has the press written about X this month, and is the tone positive?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_chatter_event",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 10 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `amgt/harvest/gold/chatter_window/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.chatter_window",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/chatter_window/",
 "layer": "gold",
 "format": "parquet",
 "table": "chatter_window",
 "grain": "one row per (security_key, window_days in 30/90/365) per as_of; 3 identical part copies in the one partition",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/harvest/window_tone.py (HVST-ak-2 gold chatter_window, AMGT_HARVST)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-04",
  "newest_write_utc": "2026-10-05T01:19:35Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 38218,
  "parquet_parts": 3,
  "rows_all_parts": 1953,
  "schema_variants": 1,
  "claim": "measured",
  "rows_per_copy": 651,
  "copies_in_partition": 3
 },
 "securities": {
  "distinct_keys": 233,
  "claim": "measured",
  "basis": "distinct security_key column values"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "window_days",
   "type": "int32",
   "nullable": true
  },
  {
   "name": "window_end",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "window_start_requested",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "window_start_served",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "articles_total",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "scored",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "voters",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "tone",
   "type": "double",
   "nullable": true
  },
  {
   "name": "as_of",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "scorer",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "news tone",
  "sentiment window",
  "media sentiment 30 90 365 days",
  "tone score"
 ],
 "common_queries": [
  "What is the 90-day news tone for X?",
  "Which names have the most negative 30-day tone?"
 ],
 "never_sum_rules": [
  "tone is an average over scored articles, never summed"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_chatter",
   "inputs": {
    "security_key": "resolved key",
    "from_day": "YYYY-MM-DD",
    "to_day": "YYYY-MM-DD"
   },
   "returns": "daily rows (day, articles_total, tier_a..d, mention_score, trailing_7d/30d_sum, data_status, publishers_found_codes); windows 30/90/365 (articles_total, scored, voters, tone); events (first_day, last_day, articles_total, tier_a, publishers_distinct, lead_article_key)",
   "reads": "gold chatter_daily, chatter_window: NEWEST part of the newest partition only; chatter_event deduped on event_id",
   "answers": [
    "How much has the press written about X this month, and is the tone positive?"
   ]
  },
  {
   "name": "harvest_query_columns",
   "inputs": {
    "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
    "columns": "list",
    "security_keys": "optional list",
    "filters": "[{column, op (= < > in), value}]",
    "order_by": "column [desc]",
    "limit": "50 default, 200 max"
   },
   "returns": "projected rows + the denominator scanned and the part/object read",
   "reads": "the newest part/object of the dataset, declared columns only",
   "answers": [
    "Top 20 names by 30-day chatter today?",
    "Every covered name's FY1 consensus P/E?",
    "Universe names in Health Care with earnings yield above 6%?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_chatter_window",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 3 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `amgt/harvest/gold/research-continuation/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research-continuation",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research-continuation/",
 "layer": "gold",
 "format": "json",
 "table": "research-continuation",
 "grain": "one object per (security_key, content hash)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-29",
  "newest_write_utc": "2026-09-29T20:09:12Z",
  "trading_days_behind_t1": 10,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 320,
  "bytes": 12769905,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 95,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "artifact",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fields",
   "type": "object",
   "nullable": true
  },
  {
   "name": "inputs",
   "type": "array",
   "nullable": true
  },
  {
   "name": "method_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "subject",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "amgt/harvest/gold/research-continuation/security_key=ASML_NA_Equity/4b0e6c7ce79b9320.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "thesis continuation",
  "last stated position",
  "thesis pillars"
 ],
 "common_queries": [
  "What was our last stated position on X?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_research",
   "inputs": {
    "security_key": "resolved key",
    "as_of": "optional",
    "fields": "optional list"
   },
   "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
   "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
   "answers": [
    "What is our thesis on X, why do we own it, and what are the risks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_research-continuation",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object amgt/harvest/gold/research-continuation/security_key=ASML_NA_Equity/4b0e6c7ce79b9320.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `amgt/harvest/gold/research-dossier/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research-dossier",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research-dossier/",
 "layer": "gold",
 "format": "json",
 "table": "research-dossier",
 "grain": "one object per (security_key, as_of); OLDER generation (field subset) of research_dossier",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-29",
  "newest_write_utc": "2026-09-29T09:36:58Z",
  "trading_days_behind_t1": 10,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 846,
  "bytes": 62350915,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 95,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "artifact",
   "type": "string",
   "nullable": true
  },
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fields",
   "type": "object",
   "nullable": true
  },
  {
   "name": "inputs",
   "type": "array",
   "nullable": true
  },
  {
   "name": "method_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "subject",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "amgt/harvest/gold/research-dossier/security_key=ASML_NA_Equity/as_of=2026-09-29.9018e7957019788d.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "research dossier (older generation)"
 ],
 "common_queries": [
  "(superseded by research_dossier)"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_research",
   "inputs": {
    "security_key": "resolved key",
    "as_of": "optional",
    "fields": "optional list"
   },
   "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
   "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
   "answers": [
    "What is our thesis on X, why do we own it, and what are the risks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_research-dossier",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "confirm with AMGT_HARVST that research-dossier (hyphen) is superseded by research_dossier and can be dropped from tools (inferred from the field superset and dates)"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object amgt/harvest/gold/research-dossier/security_key=ASML_NA_Equity/as_of=2026-09-29.9018e7957019788d.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `amgt/harvest/gold/research_dossier/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research_dossier",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research_dossier/",
 "layer": "gold",
 "format": "json",
 "table": "research_dossier",
 "grain": "one object per (security_key, as_of); fields{} one entry per dossier field with value+citation or absent",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T00:25:15Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1431,
  "bytes": 133526597,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 95,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "artifact",
   "type": "string",
   "nullable": true
  },
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fields",
   "type": "object",
   "nullable": true
  },
  {
   "name": "inputs",
   "type": "array",
   "nullable": true
  },
  {
   "name": "method_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "subject",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "amgt/harvest/gold/research_dossier/security_key=ASML_NA_Equity/as_of=2026-10-12.b8710f4d077f7afb.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "research dossier",
  "investment thesis",
  "why we own",
  "positives negatives",
  "risks pre-mortem",
  "kpis",
  "recommendation"
 ],
 "common_queries": [
  "What is our thesis on X and why do we own it?",
  "What are the main risks and the bear case for X?",
  "Which KPIs matter for X?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_research",
   "inputs": {
    "security_key": "resolved key",
    "as_of": "optional",
    "fields": "optional list"
   },
   "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
   "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
   "answers": [
    "What is our thesis on X, why do we own it, and what are the risks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_research_dossier",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object amgt/harvest/gold/research_dossier/security_key=ASML_NA_Equity/as_of=2026-10-12.b8710f4d077f7afb.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `crosswalk/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/crosswalk.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "crosswalk/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per date; records[]/names[] one row per security",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/identity/crosswalk.py (CROSSWALK_PREFIX crosswalk/v1/, AMGT_RESAPP)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-09",
  "newest_write_utc": "2026-10-09T17:20:53Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 8,
  "bytes": 4030777,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "coverage_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "registrations_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "coverage_vintage",
   "type": "object",
   "nullable": true
  },
  {
   "name": "key_conventions",
   "type": "array",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "research_universe",
   "type": "object",
   "nullable": true
  },
  {
   "name": "records",
   "type": "array",
   "nullable": true
  },
  {
   "name": "identity_universe",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "crosswalk/v1/2026-10-09.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "security identity",
  "ticker lookup",
  "bloomberg ticker",
  "CIK"
 ],
 "common_queries": [
  "Which security is 'ASML'?",
  "Which names do we cover?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_resolve_security",
   "inputs": {
    "query": "ticker, Bloomberg ticker, security_key, company or legal name, CIK, ISIN, SEDOL"
   },
   "returns": "status exact|candidates|none; security_key; display_ticker; bloomberg; name; cik; isin where held; other_listings[]; not_held[] (cusip)",
   "reads": "crosswalk/v1 newest, universe/v1 newest, bloomberg/harvest/bronze/identity newest per key; wraps lib/research/api/name_search.resolve_query",
   "answers": [
    "Which security is 'ASML'?",
    "What is the ISIN of X?"
   ]
  },
  {
   "name": "harvest_security_coverage",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "per dataset: present, objects, newest stamp, trading_days_behind_t1; per layer totals",
   "reads": "one ListObjectsV2 per keyed prefix (about 30) + packs/<key>/input_ledger.json",
   "answers": [
    "What do we hold on X, and how fresh is each piece?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_crosswalk_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object crosswalk/v1/2026-10-09.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `derived/model_block/`

```json
{
 "contract_id": "opal-data-harvest/gold/derived.model_block",
 "bucket": "opal-data-harvest",
 "s3_prefix": "derived/model_block/",
 "layer": "gold",
 "format": "json",
 "table": "model_block",
 "grain": "one object per (security_key, pull stamp); figures[] one row per (scope, fiscal_year, mnemonic)",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "integrations/bloomberg/research/model_block_pull.py and derive_fye_fixed.py (derived/model_block/, derived/model_block_fye/)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T13:12:39Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 2038,
  "bytes": 702286047,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 102,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "security",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "raw_stamp_used",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fiscal_years",
   "type": "array",
   "nullable": true
  },
  {
   "name": "fiscal_year_row_count",
   "type": "int",
   "nullable": true
  },
  {
   "name": "orphan_price_rows",
   "type": "int",
   "nullable": true
  },
  {
   "name": "history_window",
   "type": "object",
   "nullable": true
  },
  {
   "name": "figures",
   "type": "array",
   "nullable": true
  },
  {
   "name": "unresolved",
   "type": "array",
   "nullable": true
  },
  {
   "name": "forecast_fallback",
   "type": "object",
   "nullable": true
  },
  {
   "name": "cases",
   "type": "object",
   "nullable": true
  },
  {
   "name": "currencies",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "derived/model_block/ASML_NA_Equity/20261012T130207Z/model_block.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "financial model",
  "fundamentals",
  "fiscal year figures",
  "EPS revenue EBITDA history",
  "valuation case",
  "base case price target"
 ],
 "common_queries": [
  "What was ASML's revenue and EPS each year since 2016?",
  "What is the base-case value and how is it computed?",
  "How did the model change between two versions?"
 ],
 "never_sum_rules": [
  "figures carry their own unit and currency; never add across currencies or units"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  },
  {
   "name": "harvest_query_columns",
   "inputs": {
    "dataset": "tabular only: chatter_daily, chatter_window, article_security_mention, article_sentiment, candidate_universe, model_block figures, bestdata",
    "columns": "list",
    "security_keys": "optional list",
    "filters": "[{column, op (= < > in), value}]",
    "order_by": "column [desc]",
    "limit": "50 default, 200 max"
   },
   "returns": "projected rows + the denominator scanned and the part/object read",
   "reads": "the newest part/object of the dataset, declared columns only",
   "answers": [
    "Top 20 names by 30-day chatter today?",
    "Every covered name's FY1 consensus P/E?",
    "Universe names in Health Care with earnings yield above 6%?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_derived",
  "present": false,
  "parent_row_prefix": "derived/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix derived/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object derived/model_block/ASML_NA_Equity/20261012T130207Z/model_block.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `derived/model_block_fye/`

```json
{
 "contract_id": "opal-data-harvest/gold/derived.model_block_fye",
 "bucket": "opal-data-harvest",
 "s3_prefix": "derived/model_block_fye/",
 "layer": "gold",
 "format": "json",
 "table": "model_block_fye",
 "grain": "one object per (security_key, stamp); fiscal_years[] one row per fiscal year end",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "integrations/bloomberg/research/model_block_pull.py and derive_fye_fixed.py (derived/model_block/, derived/model_block_fye/)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-11",
  "newest_write_utc": "2026-09-11T19:18:57Z",
  "trading_days_behind_t1": 22,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 20175,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "security",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "join",
   "type": "string",
   "nullable": true
  },
  {
   "name": "hist_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "dense_price_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fiscal_years",
   "type": "array",
   "nullable": true
  },
  {
   "name": "max_gap_days",
   "type": "int",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "fiscal year end figures",
  "price at fiscal year end"
 ],
 "common_queries": [
  "What were X's fiscal-year-end price and margins?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_derived",
  "present": false,
  "parent_row_prefix": "derived/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix derived/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `drafting/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/drafting.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "drafting/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per security",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/drafting (AMGT_RESAPP drafting writer); the writing function of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-11",
  "newest_write_utc": "2026-10-11T13:12:08Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 12,
  "bytes": 1227491,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 12,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "accession",
   "type": "string",
   "nullable": true
  },
  {
   "name": "form",
   "type": "string",
   "nullable": true
  },
  {
   "name": "filing_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "object",
   "nullable": true
  },
  {
   "name": "model",
   "type": "string",
   "nullable": true
  },
  {
   "name": "analyzer_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "generated",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "sections",
   "type": "array",
   "nullable": true
  },
  {
   "name": "evidence_records",
   "type": "array",
   "nullable": true
  },
  {
   "name": "dropped",
   "type": "int",
   "nullable": true
  },
  {
   "name": "dropped_reasons",
   "type": "object",
   "nullable": true
  },
  {
   "name": "held_no_span",
   "type": "array",
   "nullable": true
  },
  {
   "name": "thesis_driver",
   "type": "object",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "thesis_driver_provenance",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "drafting/v1/ASML_NA_Equity.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "drafted thesis",
  "AI drafted sections",
  "evidence passages"
 ],
 "common_queries": [
  "What does the drafted thesis for X say and what evidence backs it?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_filing_analysis",
   "inputs": {
    "security_key": "resolved key",
    "accession": "optional",
    "include_passages": "bool, default false"
   },
   "returns": "form, filing_date, items by category (guidance, segments, risks, commentary, big_bets, big_challenges) with citations; denominators; drafted sections; passages on request",
   "reads": "filings/v1 .analysis/.source, drafting/v1, sec/harvest/silver/filing_source",
   "answers": [
    "What guidance and risks did X give in its latest annual filing?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_drafting_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object drafting/v1/ASML_NA_Equity.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `filings/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/filings.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "filings/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one .source + one .analysis object per (security_key, accession); 175 of 208 objects are UNRESOLVED-SOURCE markers",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/filings/fetch.py (POOL_PREFIX filings/v1/) and lib/research/filings/batch.py",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-11",
  "newest_write_utc": "2026-10-11T13:11:38Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 208,
  "bytes": 6510649,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 195,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "accession",
   "type": "string",
   "nullable": true
  },
  {
   "name": "form",
   "type": "string",
   "nullable": true
  },
  {
   "name": "filing_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "language",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "object",
   "nullable": true
  },
  {
   "name": "model",
   "type": "string",
   "nullable": true
  },
  {
   "name": "analyzer_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "prompt_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "passage_map",
   "type": "array",
   "nullable": true
  },
  {
   "name": "items",
   "type": "object",
   "nullable": true
  },
  {
   "name": "held_uncited",
   "type": "array",
   "nullable": true
  },
  {
   "name": "thesis_driver",
   "type": "object",
   "nullable": true
  },
  {
   "name": "thesis_driver_record",
   "type": "object",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "passes",
   "type": "object",
   "nullable": true
  },
  {
   "name": "usage",
   "type": "object",
   "nullable": true
  },
  {
   "name": "citations",
   "type": "array",
   "nullable": true
  },
  {
   "name": "text_encoding",
   "type": "object",
   "nullable": true
  },
  {
   "name": "pass_1_text",
   "type": "string",
   "nullable": true
  },
  {
   "name": "generated",
   "type": "bool",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "filings/v1/ASML_NA_Equity/000162828026011378.analysis.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "annual report analysis",
  "10-K 20-F",
  "guidance",
  "risk factors",
  "segments",
  "big bets",
  "filing citations"
 ],
 "common_queries": [
  "What guidance and risks did X state in its latest annual filing?",
  "What are X's big bets according to its 20-F?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_filing_analysis",
   "inputs": {
    "security_key": "resolved key",
    "accession": "optional",
    "include_passages": "bool, default false"
   },
   "returns": "form, filing_date, items by category (guidance, segments, risks, commentary, big_bets, big_challenges) with citations; denominators; drafted sections; passages on request",
   "reads": "filings/v1 .analysis/.source, drafting/v1, sec/harvest/silver/filing_source",
   "answers": [
    "What guidance and risks did X give in its latest annual filing?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_filings_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object filings/v1/ASML_NA_Equity/000162828026011378.analysis.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `identity/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/identity.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "identity/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per date; records[]/names[] one row per security",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/identity/ (crosswalk.py and build_universe.py, AMGT_RESAPP)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-17",
  "newest_write_utc": "2026-09-17T14:41:50Z",
  "trading_days_behind_t1": 18,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 47229,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "card_bound_residue",
   "type": "array",
   "nullable": true
  },
  {
   "name": "card_bound_residue_names",
   "type": "array",
   "nullable": true
  },
  {
   "name": "crosswalk_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "newly_resolved",
   "type": "array",
   "nullable": true
  },
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "identity/v1/2026-09-17-coverage-residue-crossref.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "identity residue",
  "crossref"
 ],
 "common_queries": [
  "Which security is 'ASML'?",
  "Which names do we cover?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_resolve_security",
   "inputs": {
    "query": "ticker, Bloomberg ticker, security_key, company or legal name, CIK, ISIN, SEDOL"
   },
   "returns": "status exact|candidates|none; security_key; display_ticker; bloomberg; name; cik; isin where held; other_listings[]; not_held[] (cusip)",
   "reads": "crosswalk/v1 newest, universe/v1 newest, bloomberg/harvest/bronze/identity newest per key; wraps lib/research/api/name_search.resolve_query",
   "answers": [
    "Which security is 'ASML'?",
    "What is the ISIN of X?"
   ]
  },
  {
   "name": "harvest_security_coverage",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "per dataset: present, objects, newest stamp, trading_days_behind_t1; per layer totals",
   "reads": "one ListObjectsV2 per keyed prefix (about 30) + packs/<key>/input_ledger.json",
   "answers": [
    "What do we hold on X, and how fresh is each piece?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_identity_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object identity/v1/2026-09-17-coverage-residue-crossref.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `management/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/management.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "management/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per (security_key, as_of)",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/management (AMGT_RESAPP management writer)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-02",
  "newest_write_utc": "2026-10-02T19:44:14Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 25,
  "bytes": 102226,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 17,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "roster_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "roster_reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source_accession",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source_item",
   "type": "string",
   "nullable": true
  },
  {
   "name": "parse_strategy",
   "type": "null",
   "nullable": true
  },
  {
   "name": "parser_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_normalization",
   "type": "string",
   "nullable": true
  },
  {
   "name": "officers",
   "type": "array",
   "nullable": true
  },
  {
   "name": "avg_tenure_years",
   "type": "null",
   "nullable": true
  },
  {
   "name": "section_refers_to",
   "type": "null",
   "nullable": true
  },
  {
   "name": "generated",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "generated_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "roster_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fallback",
   "type": "object",
   "nullable": true
  },
  {
   "name": "lusha_enrichment",
   "type": "object",
   "nullable": true
  },
  {
   "name": "ceo_profile",
   "type": "object",
   "nullable": true
  },
  {
   "name": "ceo_public_profile",
   "type": "object",
   "nullable": true
  },
  {
   "name": "absence_reason_class",
   "type": "string",
   "nullable": true
  },
  {
   "name": "absence_reason_evidence",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "management/v1/ASML_NA_Equity/2026-10-02T1840Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "management team",
  "executives",
  "CEO",
  "officers tenure"
 ],
 "common_queries": [
  "Who runs X and how long have they been there?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_research",
   "inputs": {
    "security_key": "resolved key",
    "as_of": "optional",
    "fields": "optional list"
   },
   "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
   "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
   "answers": [
    "What is our thesis on X, why do we own it, and what are the risks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_management_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object management/v1/ASML_NA_Equity/2026-10-02T1840Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `packs/`

```json
{
 "contract_id": "opal-data-harvest/gold/packs",
 "bucket": "opal-data-harvest",
 "s3_prefix": "packs/",
 "layer": "gold",
 "format": "json",
 "table": "packs",
 "grain": "one input_ledger.json per security",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/ledger/ledger.py (packs/<security_key>/input_ledger.json, AMGT_RESAPP)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T16:43:41Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 106,
  "bytes": 494051,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 105,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "entries",
   "type": "array",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "packs/ASML_NA_Equity/input_ledger.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "input ledger",
  "data inputs per name"
 ],
 "common_queries": [
  "Which inputs have landed for X and when?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_security_coverage",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "per dataset: present, objects, newest stamp, trading_days_behind_t1; per layer totals",
   "reads": "one ListObjectsV2 per keyed prefix (about 30) + packs/<key>/input_ledger.json",
   "answers": [
    "What do we hold on X, and how fresh is each piece?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_packs",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object packs/ASML_NA_Equity/input_ledger.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `peers/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/peers.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "peers/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per (security_key, stamp); members[] one row per peer",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/peers/engine.py (PEERS_PREFIX peers/v1/, AMGT_RESAPP)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-11",
  "newest_write_utc": "2026-10-11T11:23:01Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1727,
  "bytes": 56623609,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 245,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "basis",
   "type": "string",
   "nullable": true
  },
  {
   "name": "country_map",
   "type": "object",
   "nullable": true
  },
  {
   "name": "csc_columns",
   "type": "object",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "fit_denominators",
   "type": "object",
   "nullable": true
  },
  {
   "name": "horizon_census",
   "type": "object",
   "nullable": true
  },
  {
   "name": "identity",
   "type": "object",
   "nullable": true
  },
  {
   "name": "member_count",
   "type": "int",
   "nullable": true
  },
  {
   "name": "members",
   "type": "array",
   "nullable": true
  },
  {
   "name": "reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "rungs",
   "type": "array",
   "nullable": true
  },
  {
   "name": "sa_candidates",
   "type": "object",
   "nullable": true
  },
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "sector_map",
   "type": "object",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "subject",
   "type": "object",
   "nullable": true
  },
  {
   "name": "test",
   "type": "string",
   "nullable": true
  },
  {
   "name": "union_universe_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "universe_vintage",
   "type": "string",
   "nullable": true
  },
  {
   "name": "vintage",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "peers/v1/ASML_NA_Equity/2026-10-11T1125Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "peer group",
  "comparables",
  "competitors",
  "peer factors"
 ],
 "common_queries": [
  "Who are ASML's peers and how do they compare on valuation?",
  "Why is Y in X's peer set?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_peers_and_scores",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "peer members (name, ticker, country, sector, cap, factors, rung); scores (divergence, peers_v, robustness with status/reason); posture (verdict, books, weight_by_book)",
   "reads": "peers/v1 newest, scores/v1, posture/v1 newest",
   "answers": [
    "Who are X's peers and how does it compare?",
    "Do our funds hold X?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_peers_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object peers/v1/ASML_NA_Equity/2026-10-11T1125Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `posture/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/posture.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "posture/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per (security_key, as_of)",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/posture/judge.py (AMGT_RESAPP posture writer)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-02",
  "newest_write_utc": "2026-10-02T08:34:37Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 35,
  "bytes": 401427,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 35,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "verdict",
   "type": "string",
   "nullable": true
  },
  {
   "name": "comparable",
   "type": "null",
   "nullable": true
  },
  {
   "name": "comparable_name",
   "type": "null",
   "nullable": true
  },
  {
   "name": "marked",
   "type": "string",
   "nullable": true
  },
  {
   "name": "notice",
   "type": "string",
   "nullable": true
  },
  {
   "name": "reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "basis",
   "type": "array",
   "nullable": true
  },
  {
   "name": "dropped_claims",
   "type": "array",
   "nullable": true
  },
  {
   "name": "cites_validated",
   "type": "int",
   "nullable": true
  },
  {
   "name": "cites_total",
   "type": "int",
   "nullable": true
  },
  {
   "name": "generation",
   "type": "null",
   "nullable": true
  },
  {
   "name": "membership",
   "type": "object",
   "nullable": true
  },
  {
   "name": "comparable_membership",
   "type": "null",
   "nullable": true
  },
  {
   "name": "comparable_selection",
   "type": "object",
   "nullable": true
  },
  {
   "name": "fit",
   "type": "object",
   "nullable": true
  },
  {
   "name": "packs",
   "type": "object",
   "nullable": true
  },
  {
   "name": "sources",
   "type": "object",
   "nullable": true
  },
  {
   "name": "absence_reason_class",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "posture/v1/ASML_NA_Equity/2026-09-16.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "posture",
  "held in our books",
  "fund membership",
  "comparable"
 ],
 "common_queries": [
  "Do our funds hold X, and in which book?",
  "What is the posture verdict for X?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_peers_and_scores",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "peer members (name, ticker, country, sector, cap, factors, rung); scores (divergence, peers_v, robustness with status/reason); posture (verdict, books, weight_by_book)",
   "reads": "peers/v1 newest, scores/v1, posture/v1 newest",
   "answers": [
    "Who are X's peers and how does it compare?",
    "Do our funds hold X?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_posture_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object posture/v1/ASML_NA_Equity/2026-09-16.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `publication-links/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/publication-links.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "publication-links/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per (root ticker, publisher, article_key); 3 pilot tickers",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/opal_data_harvest (publication-links contract: catalog.py, uploads.py, contracts.json), AMGT_HARVST; read by lib/research/coverage/pool_reader.py",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-15",
  "newest_write_utc": "2026-09-15T05:01:08Z",
  "trading_days_behind_t1": 20,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 7,
  "bytes": 1839,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "record_type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "company",
   "type": "string",
   "nullable": true
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "publication-links/v1/HD/barrons/2a6d78f79cfceafe98dc1792eb27504c5371bcf4fbfe5cebd99c3888350b5c11.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "article links (pilot)"
 ],
 "common_queries": [
  "(pilot; superseded by gold mention)"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_publication_links_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object publication-links/v1/HD/barrons/2a6d78f79cfceafe98dc1792eb27504c5371bcf4fbfe5cebd99c3888350b5c11.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `scores/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/scores.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "scores/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per security (plus dated history objects)",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/scores/run_scores.py (AMGT_RESAPP scores writer)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "newest_write_utc": "2026-09-30T15:15:01Z",
  "trading_days_behind_t1": 9,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 70,
  "bytes": 234172,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 35,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "divergence",
   "type": "object",
   "nullable": true
  },
  {
   "name": "generated_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "inputs",
   "type": "object",
   "nullable": true
  },
  {
   "name": "peers_v",
   "type": "object",
   "nullable": true
  },
  {
   "name": "producer",
   "type": "string",
   "nullable": true
  },
  {
   "name": "robustness",
   "type": "object",
   "nullable": true
  },
  {
   "name": "schema_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "scores/v1/ASML_NA_Equity.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "divergence score",
  "robustness",
  "peer valuation score"
 ],
 "common_queries": [
  "What are X's divergence and robustness scores?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_peers_and_scores",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "peer members (name, ticker, country, sector, cap, factors, rung); scores (divergence, peers_v, robustness with status/reason); posture (verdict, books, weight_by_book)",
   "reads": "peers/v1 newest, scores/v1, posture/v1 newest",
   "answers": [
    "Who are X's peers and how does it compare?",
    "Do our funds hold X?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_scores_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object scores/v1/ASML_NA_Equity.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `universe/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/universe.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "universe/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "one object per date; records[]/names[] one row per security",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "lib/research/identity/build_universe.py (UNIVERSE_PREFIX universe/v1/, AMGT_RESAPP)",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-06",
  "newest_write_utc": "2026-10-06T04:10:10Z",
  "trading_days_behind_t1": 5,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 695393,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "as_of",
   "type": "string",
   "nullable": true
  },
  {
   "name": "snapshot_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "coverage_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "holdings_source",
   "type": "object",
   "nullable": true
  },
  {
   "name": "names",
   "type": "array",
   "nullable": true
  },
  {
   "name": "denominators",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "universe/v1/2026-10-06.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "covered universe",
  "coverage list",
  "book membership"
 ],
 "common_queries": [
  "Which security is 'ASML'?",
  "Which names do we cover?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_resolve_security",
   "inputs": {
    "query": "ticker, Bloomberg ticker, security_key, company or legal name, CIK, ISIN, SEDOL"
   },
   "returns": "status exact|candidates|none; security_key; display_ticker; bloomberg; name; cik; isin where held; other_listings[]; not_held[] (cusip)",
   "reads": "crosswalk/v1 newest, universe/v1 newest, bloomberg/harvest/bronze/identity newest per key; wraps lib/research/api/name_search.resolve_query",
   "answers": [
    "Which security is 'ASML'?",
    "What is the ISIN of X?"
   ]
  },
  {
   "name": "harvest_security_coverage",
   "inputs": {
    "security_key": "resolved key"
   },
   "returns": "per dataset: present, objects, newest stamp, trading_days_behind_t1; per layer totals",
   "reads": "one ListObjectsV2 per keyed prefix (about 30) + packs/<key>/input_ledger.json",
   "answers": [
    "What do we hold on X, and how fresh is each piece?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_universe_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object universe/v1/2026-10-06.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `amgt/harvest/silver/research-report/`

```json
{
 "contract_id": "opal-data-harvest/silver/amgt.harvest.silver.research-report",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/silver/research-report/",
 "layer": "silver",
 "format": "parquet",
 "table": "research-report",
 "grain": "one row per research report file (report_id)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST research-report silver; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-25",
  "newest_write_utc": "2026-09-26T00:41:50Z",
  "trading_days_behind_t1": 12,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 5,
  "bytes": 133462,
  "parquet_parts": 5,
  "rows_all_parts": 355,
  "schema_variants": 3,
  "claim": "measured",
  "distinct_reports_note": "355 rows"
 },
 "securities": {
  "distinct_keys": 94,
  "claim": "measured",
  "basis": "distinct security_key column values"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "report_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "extract_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "file_ext",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source_relpath",
   "type": "string",
   "nullable": true
  },
  {
   "name": "size_bytes",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "words_or_pages",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "report_class",
   "type": "string",
   "nullable": true
  },
  {
   "name": "class_evidence",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fund",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fund_evidence",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fund_absent_reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "sector_as_written",
   "type": "string",
   "nullable": true
  },
  {
   "name": "sector_evidence",
   "type": "string",
   "nullable": true
  },
  {
   "name": "sector_absent_reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "period",
   "type": "string",
   "nullable": true
  },
  {
   "name": "period_source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "period_evidence",
   "type": "string",
   "nullable": true
  },
  {
   "name": "period_absent_reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "author",
   "type": "null",
   "nullable": true
  },
  {
   "name": "author_evidence",
   "type": "null",
   "nullable": true
  },
  {
   "name": "author_absent_reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "research reports",
  "investment memos",
  "one pagers",
  "report by fund sector period author"
 ],
 "common_queries": [
  "Which research reports do we hold on X, for which fund and period?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_research",
   "inputs": {
    "security_key": "resolved key",
    "as_of": "optional",
    "fields": "optional list"
   },
   "returns": "dossier fields (value + citation or absent reason); continuation thesis and pillars; ai_fill blocks; research-report list (class, period, fund, author); management roster",
   "reads": "gold research_dossier (newest as_of), research-continuation, ai_fill; silver research-report; management/v1; bloomberg bronze exec_officers",
   "answers": [
    "What is our thesis on X, why do we own it, and what are the risks?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_silver",
  "present": false,
  "parent_row_prefix": "amgt/harvest/silver/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix amgt/harvest/silver/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 5 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `barrons/harvest/silver/article/`

```json
{
 "contract_id": "opal-data-harvest/silver/barrons.harvest.silver.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "barrons/harvest/silver/article/",
 "layer": "silver",
 "format": "parquet",
 "table": "article",
 "grain": "one row per fetched article record (article_key; rows repeat across parts -- dedupe on article_key, newest fetched_at)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T04:19:33Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 64,
  "bytes": 10426017,
  "parquet_parts": 64,
  "rows_all_parts": 501,
  "schema_variants": 43,
  "claim": "measured",
  "distinct_articles": 203
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "record_type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "published",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "body_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "text",
   "type": "string",
   "nullable": true
  },
  {
   "name": "words",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "expected_words",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "body_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "response_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "transport",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "published_offset_min",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "published_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "published_precision",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_rung",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "null",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "null",
   "nullable": true
  },
  {
   "name": "discovered_for",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "__typename",
   "articleBody",
   "articleBodyImages",
   "articleMeta",
   "articleToolsProps",
   "articleTrackingMeta",
   "articleType",
   "attributes",
   "authors",
   "availabilityFlags",
   "body",
   "byline",
   "canonicalUrl",
   "dateType",
   "dek",
   "djmlKeyword",
   "doNotArchive",
   "endpoints",
   "entitlements",
   "flashline",
   "flattenedAltSummaries",
   "flattenedSummary",
   "headline",
   "id",
   "isBICPaywall",
   "isFreeArticle",
   "isServerUnlockedArticle",
   "keywords",
   "languageCode",
   "leadInset",
   "liveDateTimeUtc",
   "originId",
   "page",
   "paywallIndex",
   "printPublicationDate",
   "product",
   "publishedDateTimeUtc",
   "relayCodes",
   "sectionName",
   "sectionType",
   "seoId",
   "seoPath",
   "sidecarConfig",
   "snippet",
   "sourceUrl",
   "standFirst",
   "subjectName",
   "subjects",
   "tickers",
   "type",
   "typeDisplayName",
   "updatedDateTimeUtc",
   "upstreamOriginId",
   "vendor_publisher"
  ],
  "variant_only_count": 54
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "gold article_security_mention join on article_key"
  }
 },
 "nl_tags": [
  "Barron's articles",
  "article text",
  "headline url",
  "news article body"
 ],
 "common_queries": [
  "Show me the Barron's articles about X with links.",
  "Read me the article behind this headline."
 ],
 "never_sum_rules": [
  "no security_key column: reach a company only through gold article_security_mention",
  "discovered_for is the search query ticker, not the subject"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_get_article",
   "inputs": {
    "article_key": "from a search",
    "publisher": "sa|bbg|wsj|ft|barrons",
    "include_text": "bool, default false"
   },
   "returns": "title, url, published_utc, words, content_status, mentioned security_keys; text/body_blocks only with include_text",
   "reads": "<publisher>/harvest/silver/article, newest record per article_key, partition located from the mention row's published date",
   "answers": [
    "Read me this article."
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_barrons_harvest",
  "present": false,
  "parent_row_prefix": "barrons/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix barrons/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 64 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `barrons/harvest/silver/listing_hit/`

```json
{
 "contract_id": "opal-data-harvest/silver/barrons.harvest.silver.listing_hit",
 "bucket": "opal-data-harvest",
 "s3_prefix": "barrons/harvest/silver/listing_hit/",
 "layer": "silver",
 "format": "parquet",
 "table": "listing_hit",
 "grain": "one row per search-result hit (query, page, rank)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T04:46:07Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 224,
  "bytes": 3269333,
  "parquet_parts": 224,
  "rows_all_parts": 1996,
  "schema_variants": 4,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "byline",
   "type": "list<element: struct<type: string, text: string, seoName: string>>",
   "nullable": true
  },
  {
   "name": "commentCount",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "flashline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "headline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "image",
   "type": "struct<url: string, width: int64, height: int64>",
   "nullable": true
  },
  {
   "name": "publishedDateTime",
   "type": "string",
   "nullable": true
  },
  {
   "name": "sectionName",
   "type": "string",
   "nullable": true
  },
  {
   "name": "sectionType",
   "type": "string",
   "nullable": true
  },
  {
   "name": "summary",
   "type": "string",
   "nullable": true
  },
  {
   "name": "type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "wordCount",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "query_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetch_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "Barron's search hits",
  "discovery"
 ],
 "common_queries": [
  "(plumbing) which searches found which articles"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_barrons_harvest",
  "present": false,
  "parent_row_prefix": "barrons/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix barrons/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 224 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `bloomberg/harvest/silver/article/`

```json
{
 "contract_id": "opal-data-harvest/silver/bloomberg.harvest.silver.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/silver/article/",
 "layer": "silver",
 "format": "parquet",
 "table": "article",
 "grain": "one row per fetched article record (article_key; rows repeat across parts -- dedupe on article_key, newest fetched_at)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "newest_write_utc": "2026-10-13T17:03:16Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 745,
  "bytes": 211578674,
  "parquet_parts": 745,
  "rows_all_parts": 4255,
  "schema_variants": 717,
  "claim": "measured",
  "distinct_articles": 3008
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "record_type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "published",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "body_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "text",
   "type": "string",
   "nullable": true
  },
  {
   "name": "words",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "expected_words",
   "type": "null",
   "nullable": true
  },
  {
   "name": "body_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "response_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "transport",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "published_offset_min",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "published_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "published_precision",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_rung",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "null",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "null",
   "nullable": true
  },
  {
   "name": "discovered_for",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "__modelType",
   "abstract",
   "adTargeting",
   "aiSummary",
   "archived",
   "assistance",
   "attributor",
   "audios",
   "authoredRegion",
   "authors",
   "blensSecurities",
   "body",
   "brand",
   "byline",
   "categories",
   "charts",
   "checksum",
   "cobrand",
   "collections",
   "contentAccess",
   "contentTags",
   "corrected",
   "disableAds",
   "disclaimer",
   "facebook",
   "footer",
   "footnotes",
   "franchise",
   "headline",
   "hedAndDekPosition",
   "html_lang",
   "html_meta",
   "id",
   "imageAttachments",
   "isPageTracked",
   "isTrending",
   "json_ld",
   "label",
   "language",
   "lede",
   "ledeImageUrl",
   "locale",
   "magazineIssue",
   "metadata",
   "mostRelevantTags",
   "moved",
   "next_data",
   "nicodes",
   "opinionArticleType",
   "page_analytics",
   "pillar",
   "premium",
   "publishedAt",
   "readingDuration",
   "readingUrl",
   "record",
   "resourceType",
   "revision",
   "secondaryBrands",
   "seoCanonical"
  ],
  "variant_only_count": 85
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "gold article_security_mention join on article_key"
  }
 },
 "nl_tags": [
  "Bloomberg articles",
  "article text",
  "headline url",
  "news article body"
 ],
 "common_queries": [
  "Show me the Bloomberg articles about X with links.",
  "Read me the article behind this headline."
 ],
 "never_sum_rules": [
  "no security_key column: reach a company only through gold article_security_mention",
  "discovered_for is the search query ticker, not the subject"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_get_article",
   "inputs": {
    "article_key": "from a search",
    "publisher": "sa|bbg|wsj|ft|barrons",
    "include_text": "bool, default false"
   },
   "returns": "title, url, published_utc, words, content_status, mentioned security_keys; text/body_blocks only with include_text",
   "reads": "<publisher>/harvest/silver/article, newest record per article_key, partition located from the mention row's published date",
   "answers": [
    "Read me this article."
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 745 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `bloomberg/harvest/silver/listing_hit/`

```json
{
 "contract_id": "opal-data-harvest/silver/bloomberg.harvest.silver.listing_hit",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/silver/listing_hit/",
 "layer": "silver",
 "format": "parquet",
 "table": "listing_hit",
 "grain": "one row per search-result hit (query, page, rank)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "newest_write_utc": "2026-09-30T05:12:57Z",
  "trading_days_behind_t1": 9,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 4,
  "bytes": 57236,
  "parquet_parts": 4,
  "rows_all_parts": 40,
  "schema_variants": 2,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "byline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "eyebrow",
   "type": "string",
   "nullable": true
  },
  {
   "name": "headline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publishedAt",
   "type": "string",
   "nullable": true
  },
  {
   "name": "subtype",
   "type": "string",
   "nullable": true
  },
  {
   "name": "summary",
   "type": "string",
   "nullable": true
  },
  {
   "name": "thumbnail",
   "type": "string",
   "nullable": true
  },
  {
   "name": "type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "resourceId",
   "type": "string",
   "nullable": true
  },
  {
   "name": "readings",
   "type": "list<element: struct<voice: string, duration_ms: int64, url: string>>",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "query_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetch_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "Bloomberg search hits",
  "discovery"
 ],
 "common_queries": [
  "(plumbing) which searches found which articles"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 4 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `ft/harvest/silver/article/`

```json
{
 "contract_id": "opal-data-harvest/silver/ft.harvest.silver.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "ft/harvest/silver/article/",
 "layer": "silver",
 "format": "parquet",
 "table": "article",
 "grain": "one row per fetched article record (article_key; rows repeat across parts -- dedupe on article_key, newest fetched_at)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-02",
  "newest_write_utc": "2026-10-05T02:00:10Z",
  "trading_days_behind_t1": 7,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 95,
  "bytes": 6036444,
  "parquet_parts": 95,
  "rows_all_parts": 355,
  "schema_variants": 7,
  "claim": "measured",
  "distinct_articles": 185
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "@context",
   "type": "string",
   "nullable": true
  },
  {
   "name": "@type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "headline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "datePublished",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "dateModified",
   "type": "string",
   "nullable": true
  },
  {
   "name": "description",
   "type": "string",
   "nullable": true
  },
  {
   "name": "isAccessibleForFree",
   "type": "string",
   "nullable": true
  },
  {
   "name": "isPartOf",
   "type": "struct<@type: list<element: string>, name: string, productID: string>",
   "nullable": true
  },
  {
   "name": "alternativeHeadline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "image",
   "type": "struct<@type: string, @context: string, url: string, width: int64, height: int64>",
   "nullable": true
  },
  {
   "name": "author",
   "type": "list<element: struct<@type: string, @context: string, name: string, url: string, worksFor: struct<@type: string, @context: string, name: string, legalName: string, logo: struct<@type: string, @context: string, url: string, width: int64, height: int64>, url: string, sameAs: list<element: string>>>>",
   "nullable": true
  },
  {
   "name": "articleBody",
   "type": "string",
   "nullable": true
  },
  {
   "name": "wordCount",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "published_offset_min",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "published_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "published_precision",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "retrieval_rung",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "discovered_for",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "body_blocks",
   "body_sha256",
   "content_status",
   "expected_words",
   "html_lang",
   "html_meta",
   "json_ld",
   "published",
   "record_type",
   "response_sha256",
   "schema_version",
   "text",
   "transport",
   "url",
   "vendor_publisher",
   "words"
  ],
  "variant_only_count": 16
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "gold article_security_mention join on article_key"
  }
 },
 "nl_tags": [
  "FT articles",
  "article text",
  "headline url",
  "news article body"
 ],
 "common_queries": [
  "Show me the FT articles about X with links.",
  "Read me the article behind this headline."
 ],
 "never_sum_rules": [
  "no security_key column: reach a company only through gold article_security_mention",
  "discovered_for is the search query ticker, not the subject"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_get_article",
   "inputs": {
    "article_key": "from a search",
    "publisher": "sa|bbg|wsj|ft|barrons",
    "include_text": "bool, default false"
   },
   "returns": "title, url, published_utc, words, content_status, mentioned security_keys; text/body_blocks only with include_text",
   "reads": "<publisher>/harvest/silver/article, newest record per article_key, partition located from the mention row's published date",
   "answers": [
    "Read me this article."
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_ft_harvest",
  "present": false,
  "parent_row_prefix": "ft/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix ft/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 95 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `ft/harvest/silver/listing_hit/`

```json
{
 "contract_id": "opal-data-harvest/silver/ft.harvest.silver.listing_hit",
 "bucket": "opal-data-harvest",
 "s3_prefix": "ft/harvest/silver/listing_hit/",
 "layer": "silver",
 "format": "parquet",
 "table": "listing_hit",
 "grain": "one row per search-result hit (query, page, rank)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-05",
  "newest_write_utc": "2026-10-05T01:49:24Z",
  "trading_days_behind_t1": 6,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 48,
  "bytes": 483045,
  "parquet_parts": 48,
  "rows_all_parts": 1200,
  "schema_variants": 1,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "null",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "query_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetch_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "FT search hits",
  "discovery"
 ],
 "common_queries": [
  "(plumbing) which searches found which articles"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_ft_harvest",
  "present": false,
  "parent_row_prefix": "ft/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix ft/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 48 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `issuer-site/harvest/silver/filing_source/`

```json
{
 "contract_id": "opal-data-harvest/silver/issuer-site.harvest.silver.filing_source",
 "bucket": "opal-data-harvest",
 "s3_prefix": "issuer-site/harvest/silver/filing_source/",
 "layer": "silver",
 "format": "parquet",
 "table": "filing_source",
 "grain": "one row per issuer-site filing source (1 row)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST issuer-site harvest; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T03:31:59Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 283596,
  "parquet_parts": 1,
  "rows_all_parts": 1,
  "schema_variants": 1,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "accession",
   "type": "string",
   "nullable": true
  },
  {
   "name": "accession_raw",
   "type": "null",
   "nullable": true
  },
  {
   "name": "form",
   "type": "null",
   "nullable": true
  },
  {
   "name": "family",
   "type": "string",
   "nullable": true
  },
  {
   "name": "language",
   "type": "string",
   "nullable": true
  },
  {
   "name": "entity_name",
   "type": "string",
   "nullable": true
  },
  {
   "name": "filing_date",
   "type": "null",
   "nullable": true
  },
  {
   "name": "period_end",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "primary_document",
   "type": "null",
   "nullable": true
  },
  {
   "name": "retrieved_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "parser_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "document_bytes",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "document_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "document_text_chars",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "verified_site_reason",
   "type": "null",
   "nullable": true
  },
  {
   "name": "reason",
   "type": "null",
   "nullable": true
  },
  {
   "name": "object_keys",
   "type": "string",
   "nullable": true
  },
  {
   "name": "object_json",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "issuer website filing"
 ],
 "common_queries": [
  "Which non-SEC filing was used for X?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_filing_analysis",
   "inputs": {
    "security_key": "resolved key",
    "accession": "optional",
    "include_passages": "bool, default false"
   },
   "returns": "form, filing_date, items by category (guidance, segments, risks, commentary, big_bets, big_challenges) with citations; denominators; drafted sections; passages on request",
   "reads": "filings/v1 .analysis/.source, drafting/v1, sec/harvest/silver/filing_source",
   "answers": [
    "What guidance and risks did X give in its latest annual filing?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_issuer_site_harvest",
  "present": false,
  "parent_row_prefix": "issuer-site/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix issuer-site/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 1 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `publications/v1/`

```json
{
 "contract_id": "opal-data-harvest/silver/publications.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "publications/v1/",
 "layer": "silver",
 "format": "json",
 "table": "v1",
 "grain": "one object per pilot article",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-15",
  "newest_write_utc": "2026-09-15T05:01:08Z",
  "trading_days_behind_t1": 20,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 7,
  "bytes": 66021,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int",
   "nullable": true
  },
  {
   "name": "record_type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "published",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "body_blocks",
   "type": "array",
   "nullable": true
  },
  {
   "name": "text",
   "type": "string",
   "nullable": true
  },
  {
   "name": "words",
   "type": "int",
   "nullable": true
  },
  {
   "name": "expected_words",
   "type": "int",
   "nullable": true
  },
  {
   "name": "body_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "response_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "transport",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_status",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "publications/v1/barrons/2a6d78f79cfceafe98dc1792eb27504c5371bcf4fbfe5cebd99c3888350b5c11.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "pilot publications"
 ],
 "common_queries": [
  "(pilot)"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_publications_v1",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object publications/v1/barrons/2a6d78f79cfceafe98dc1792eb27504c5371bcf4fbfe5cebd99c3888350b5c11.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `sec/harvest/silver/filing_source/`

```json
{
 "contract_id": "opal-data-harvest/silver/sec.harvest.silver.filing_source",
 "bucket": "opal-data-harvest",
 "s3_prefix": "sec/harvest/silver/filing_source/",
 "layer": "silver",
 "format": "parquet",
 "table": "filing_source",
 "grain": "one row per (security_key, accession) resolved filing source",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST SEC harvest; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-09",
  "newest_write_utc": "2026-10-09T11:41:36Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 10,
  "bytes": 1720558,
  "parquet_parts": 10,
  "rows_all_parts": 22,
  "schema_variants": 3,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 13,
  "claim": "measured",
  "basis": "distinct security_key column values"
 },
 "columns": [
  {
   "name": "security_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "accession",
   "type": "string",
   "nullable": true
  },
  {
   "name": "accession_raw",
   "type": "string",
   "nullable": true
  },
  {
   "name": "form",
   "type": "string",
   "nullable": true
  },
  {
   "name": "family",
   "type": "string",
   "nullable": true
  },
  {
   "name": "language",
   "type": "string",
   "nullable": true
  },
  {
   "name": "entity_name",
   "type": "string",
   "nullable": true
  },
  {
   "name": "filing_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "period_end",
   "type": "null",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "primary_document",
   "type": "string",
   "nullable": true
  },
  {
   "name": "retrieved_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "parser_version",
   "type": "string",
   "nullable": true
  },
  {
   "name": "document_bytes",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "document_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "document_text_chars",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "verified_site_reason",
   "type": "string",
   "nullable": true
  },
  {
   "name": "reason",
   "type": "null",
   "nullable": true
  },
  {
   "name": "object_keys",
   "type": "string",
   "nullable": true
  },
  {
   "name": "object_json",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "SEC filings",
  "accession",
  "filing date",
  "form type"
 ],
 "common_queries": [
  "Which SEC filing is X's analysis based on?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_filing_analysis",
   "inputs": {
    "security_key": "resolved key",
    "accession": "optional",
    "include_passages": "bool, default false"
   },
   "returns": "form, filing_date, items by category (guidance, segments, risks, commentary, big_bets, big_challenges) with citations; denominators; drafted sections; passages on request",
   "reads": "filings/v1 .analysis/.source, drafting/v1, sec/harvest/silver/filing_source",
   "answers": [
    "What guidance and risks did X give in its latest annual filing?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_sec_harvest",
  "present": false,
  "parent_row_prefix": "sec/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix sec/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 10 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `seeking-alpha/harvest/silver/article/`

```json
{
 "contract_id": "opal-data-harvest/silver/seeking-alpha.harvest.silver.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/silver/article/",
 "layer": "silver",
 "format": "parquet",
 "table": "article",
 "grain": "one row per fetched article record (article_key; rows repeat across parts -- dedupe on article_key, newest fetched_at)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T12:08:49Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1365,
  "bytes": 84300542,
  "parquet_parts": 1365,
  "rows_all_parts": 19477,
  "schema_variants": 55,
  "claim": "measured",
  "distinct_articles": 19472
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "commentCount",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "content",
   "type": "string",
   "nullable": true
  },
  {
   "name": "gettyImageUrl",
   "type": "string",
   "nullable": true
  },
  {
   "name": "isLockedPro",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "isPaywalled",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "publishOn",
   "type": "timestamp[us, tz=-04:00]",
   "nullable": true
  },
  {
   "name": "themes",
   "type": "null",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "videoDuration",
   "type": "null",
   "nullable": true
  },
  {
   "name": "videoPreviewUrl",
   "type": "null",
   "nullable": true
  },
  {
   "name": "id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "relationships",
   "type": "struct<author: struct<data: struct<id: string, type: string>>, otherTags: struct<data: list<element: null>>, primaryTickers: struct<data: list<element: struct<id: string, type: string>>>, secondaryTickers: struct<data: list<element: null>>, sentiments: struct<data: list<element: null>>>",
   "nullable": true
  },
  {
   "name": "links",
   "type": "struct<self: string>",
   "nullable": true
  },
  {
   "name": "type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "published_offset_min",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "published_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "published_precision",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "retrieval_rung",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "discovered_for",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "articleActionableItem",
   "audioDuration",
   "availableTranslations",
   "beforeOpeningHours",
   "body_blocks",
   "body_sha256",
   "closestTradingDate",
   "content_status",
   "disabledMessage",
   "disabledStatus",
   "disclosure",
   "excludedByTag",
   "expected_words",
   "inEmbargo",
   "included",
   "innerMarketing",
   "isEarningsSlides",
   "isExclusive",
   "isModerated",
   "isMpwLocked",
   "isNoarchive",
   "isNoindex",
   "isReit",
   "isTranscript",
   "lastModified",
   "likesCount",
   "locale",
   "marketingBio",
   "marketingBullet",
   "marketingBulletVariant",
   "meta",
   "originalTitle",
   "portfolioTemplate",
   "published",
   "quickInsights",
   "record_type",
   "response_sha256",
   "schema_version",
   "status",
   "structuredInsights",
   "summary",
   "text",
   "transcriptPath",
   "translationDisclosure",
   "transport",
   "twitContent",
   "url",
   "videoData",
   "words"
  ],
  "variant_only_count": 49
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "gold article_security_mention join on article_key"
  }
 },
 "nl_tags": [
  "Seeking Alpha articles",
  "article text",
  "headline url",
  "news article body"
 ],
 "common_queries": [
  "Show me the Seeking Alpha articles about X with links.",
  "Read me the article behind this headline."
 ],
 "never_sum_rules": [
  "no security_key column: reach a company only through gold article_security_mention",
  "discovered_for is the search query ticker, not the subject"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_get_article",
   "inputs": {
    "article_key": "from a search",
    "publisher": "sa|bbg|wsj|ft|barrons",
    "include_text": "bool, default false"
   },
   "returns": "title, url, published_utc, words, content_status, mentioned security_keys; text/body_blocks only with include_text",
   "reads": "<publisher>/harvest/silver/article, newest record per article_key, partition located from the mention row's published date",
   "answers": [
    "Read me this article."
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix seeking-alpha/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 1365 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `seeking-alpha/harvest/silver/listing_hit/`

```json
{
 "contract_id": "opal-data-harvest/silver/seeking-alpha.harvest.silver.listing_hit",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/silver/listing_hit/",
 "layer": "silver",
 "format": "parquet",
 "table": "listing_hit",
 "grain": "one row per search-result hit (query, page, rank)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T12:06:05Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1585,
  "bytes": 287114564,
  "parquet_parts": 1585,
  "rows_all_parts": 214615,
  "schema_variants": 2,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "publishOn",
   "type": "string",
   "nullable": true
  },
  {
   "name": "isLockedPro",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "commentCount",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "gettyImageUrl",
   "type": "string",
   "nullable": true
  },
  {
   "name": "videoPreviewUrl",
   "type": "null",
   "nullable": true
  },
  {
   "name": "videoDuration",
   "type": "null",
   "nullable": true
  },
  {
   "name": "themes",
   "type": "null",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "isPaywalled",
   "type": "bool",
   "nullable": true
  },
  {
   "name": "content",
   "type": "string",
   "nullable": true
  },
  {
   "name": "id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "links",
   "type": "struct<self: string>",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "query_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetch_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [],
  "variant_only_count": 0
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "Seeking Alpha search hits",
  "discovery"
 ],
 "common_queries": [
  "(plumbing) which searches found which articles"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix seeking-alpha/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 1585 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `wsj/harvest/silver/article/`

```json
{
 "contract_id": "opal-data-harvest/silver/wsj.harvest.silver.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "wsj/harvest/silver/article/",
 "layer": "silver",
 "format": "parquet",
 "table": "article",
 "grain": "one row per fetched article record (article_key; rows repeat across parts -- dedupe on article_key, newest fetched_at)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T12:14:10Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 416,
  "bytes": 130592033,
  "parquet_parts": 416,
  "rows_all_parts": 1044,
  "schema_variants": 313,
  "claim": "measured",
  "distinct_articles": 615
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "schema_version",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "record_type",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "string",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  },
  {
   "name": "published",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "body_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "text",
   "type": "string",
   "nullable": true
  },
  {
   "name": "words",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "expected_words",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "body_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "response_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "transport",
   "type": "string",
   "nullable": true
  },
  {
   "name": "content_status",
   "type": "string",
   "nullable": true
  },
  {
   "name": "text_blocks",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "published_utc",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "published_offset_min",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "published_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "published_precision",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "first_discovered_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_rung",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "null",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "null",
   "nullable": true
  },
  {
   "name": "discovered_for",
   "type": "list<element: string>",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "articleData",
   "html_lang",
   "html_meta",
   "json_ld",
   "next_data",
   "page_config_json"
  ],
  "variant_only_count": 6
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "gold article_security_mention join on article_key"
  }
 },
 "nl_tags": [
  "WSJ articles",
  "article text",
  "headline url",
  "news article body"
 ],
 "common_queries": [
  "Show me the WSJ articles about X with links.",
  "Read me the article behind this headline."
 ],
 "never_sum_rules": [
  "no security_key column: reach a company only through gold article_security_mention",
  "discovered_for is the search query ticker, not the subject"
 ],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_search_articles",
   "inputs": {
    "security_key": "resolved key",
    "publisher": "sa|bbg|wsj|ft|barrons (optional)",
    "from": "date",
    "to": "date",
    "min_tier": "A|B|C|D",
    "in_title": "bool",
    "limit": "25 default, 100 max"
   },
   "returns": "article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words from silver",
   "reads": "gold article_security_mention (newest part) + gold article_sentiment, joined on article_key to <publisher>/harvest/silver/article",
   "answers": [
    "Which articles mention X, newest first, with links and sentiment?"
   ]
  },
  {
   "name": "harvest_get_article",
   "inputs": {
    "article_key": "from a search",
    "publisher": "sa|bbg|wsj|ft|barrons",
    "include_text": "bool, default false"
   },
   "returns": "title, url, published_utc, words, content_status, mentioned security_keys; text/body_blocks only with include_text",
   "reads": "<publisher>/harvest/silver/article, newest record per article_key, partition located from the mention row's published date",
   "answers": [
    "Read me this article."
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_wsj_harvest",
  "present": false,
  "parent_row_prefix": "wsj/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix wsj/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 416 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `wsj/harvest/silver/listing_hit/`

```json
{
 "contract_id": "opal-data-harvest/silver/wsj.harvest.silver.listing_hit",
 "bucket": "opal-data-harvest",
 "s3_prefix": "wsj/harvest/silver/listing_hit/",
 "layer": "silver",
 "format": "parquet",
 "table": "listing_hit",
 "grain": "one row per search-result hit (query, page, rank)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "newest_write_utc": "2026-09-30T05:12:59Z",
  "trading_days_behind_t1": 9,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 5,
  "bytes": 96855,
  "parquet_parts": 5,
  "rows_all_parts": 80,
  "schema_variants": 2,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "articleUrl",
   "type": "string",
   "nullable": true
  },
  {
   "name": "commerceProduct",
   "type": "string",
   "nullable": true
  },
  {
   "name": "contentTag",
   "type": "string",
   "nullable": true
  },
  {
   "name": "bylineData",
   "type": "list<element: struct<text: string, ref: string, phrase_type: string, id: string, type: string, name: string>>",
   "nullable": true
  },
  {
   "name": "flashline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "headline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "imageAlt",
   "type": "string",
   "nullable": true
  },
  {
   "name": "printHeadline",
   "type": "string",
   "nullable": true
  },
  {
   "name": "printPublicationDate",
   "type": "string",
   "nullable": true
  },
  {
   "name": "seoPathValue",
   "type": "string",
   "nullable": true
  },
  {
   "name": "summary",
   "type": "string",
   "nullable": true
  },
  {
   "name": "timestamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "article_id",
   "type": "null",
   "nullable": true
  },
  {
   "name": "url",
   "type": "string",
   "nullable": true
  },
  {
   "name": "search_rank",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_page",
   "type": "int64",
   "nullable": true
  },
  {
   "name": "search_query",
   "type": "string",
   "nullable": true
  },
  {
   "name": "query_sha256",
   "type": "string",
   "nullable": true
  },
  {
   "name": "source",
   "type": "string",
   "nullable": true
  },
  {
   "name": "publisher",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetch_date_utc",
   "type": "date32[day]",
   "nullable": true
  },
  {
   "name": "bronze_key",
   "type": "string",
   "nullable": true
  },
  {
   "name": "fetched_at",
   "type": "timestamp[us, tz=UTC]",
   "nullable": true
  },
  {
   "name": "retrieval_mode",
   "type": "string",
   "nullable": true
  },
  {
   "name": "run_stamp",
   "type": "string",
   "nullable": true
  },
  {
   "name": "record_hash",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "variant_only_columns": [
   "imageHeight",
   "imageUrl",
   "imageWidth"
  ],
  "variant_only_count": 3
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "WSJ search hits",
  "discovery"
 ],
 "common_queries": [
  "(plumbing) which searches found which articles"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_wsj_harvest",
  "present": false,
  "parent_row_prefix": "wsj/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix wsj/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "pyarrow footer of all 5 parts",
   "at": "2026-10-14T12:10Z"
  }
 ]
}
```

### `bloomberg/harvest/bronze/bestdata/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.bestdata",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/bestdata/",
 "layer": "bronze",
 "format": "json",
 "table": "bestdata",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T13:12:37Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1125,
  "bytes": 2535327,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 99,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "1FY",
   "type": "object",
   "nullable": true
  },
  {
   "name": "2FY",
   "type": "object",
   "nullable": true
  },
  {
   "name": "3FY",
   "type": "object",
   "nullable": true
  },
  {
   "name": "requests",
   "type": "array",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "bloomberg/harvest/bronze/bestdata/security_key=ASML_NA_Equity/20261012T130159Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "consensus estimates",
  "BEST EPS sales EBITDA FY1 FY2 FY3",
  "analyst estimates"
 ],
 "common_queries": [
  "What is consensus EPS for X next year and how many estimates?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/bestdata/security_key=ASML_NA_Equity/20261012T130159Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/exec_officers/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.exec_officers",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/exec_officers/",
 "layer": "bronze",
 "format": "json",
 "table": "exec_officers",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T11:37:24Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 93,
  "bytes": 119017,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 91,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "security",
   "type": "string",
   "nullable": true
  },
  {
   "name": "pulled_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "response",
   "type": "object",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "bloomberg/harvest/bronze/exec_officers/security_key=ASML_NA_Equity/20261002T183557Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "executive officers list"
 ],
 "common_queries": [
  "Who are X's executive officers per Bloomberg?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/exec_officers/security_key=ASML_NA_Equity/20261002T183557Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/histdata/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.histdata",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/histdata/",
 "layer": "bronze",
 "format": "json",
 "table": "histdata",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T13:12:36Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1167,
  "bytes": 20258055,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 100,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "<bloomberg security>",
   "type": "object-key",
   "nullable": false,
   "description": "the Bloomberg security string is the single top-level key"
  },
  {
   "name": "AVERAGE_DIVIDEND_YIELD",
   "type": "double",
   "nullable": true
  },
  {
   "name": "AVERAGE_EV_TO_T12M_EBIT",
   "type": "double",
   "nullable": true
  },
  {
   "name": "AVERAGE_EV_TO_T12M_SALES",
   "type": "double",
   "nullable": true
  },
  {
   "name": "AVERAGE_PRICE_EARNINGS_RATIO",
   "type": "double",
   "nullable": true
  },
  {
   "name": "AVERAGE_PRICE_TO_BOOK_RATIO",
   "type": "double",
   "nullable": true
  },
  {
   "name": "AVERAGE_PRICE_TO_FREE_CASH_FLOW",
   "type": "double",
   "nullable": true
  },
  {
   "name": "AVG_EV_TO_T12M_EBITDA",
   "type": "double",
   "nullable": true
  },
  {
   "name": "CURRENT_EV_TO_T12M_EBITDA",
   "type": "double",
   "nullable": true
  },
  {
   "name": "DIVIDEND_YIELD",
   "type": "double",
   "nullable": true
  },
  {
   "name": "EQY_DVD_YLD_IND",
   "type": "double",
   "nullable": true
  },
  {
   "name": "FREE_CASH_FLOW_YIELD",
   "type": "double",
   "nullable": true
  },
  {
   "name": "HIGH_CLOSING_PRICE_TO_BOOK_RATIO",
   "type": "double",
   "nullable": true
  },
  {
   "name": "HIGH_DIVIDEND_YIELD",
   "type": "double",
   "nullable": true
  },
  {
   "name": "HIGH_EV_TO_T12M_EBIT",
   "type": "double",
   "nullable": true
  },
  {
   "name": "HIGH_EV_TO_T12M_EBITDA",
   "type": "double",
   "nullable": true
  },
  {
   "name": "HIGH_EV_TO_T12M_SALES",
   "type": "double",
   "nullable": true
  },
  {
   "name": "HIGH_PRICE_TO_FREE_CASH_FLOW",
   "type": "double",
   "nullable": true
  },
  {
   "name": "LOW_CLOSING_PRICE_TO_BOOK_RATIO",
   "type": "double",
   "nullable": true
  },
  {
   "name": "LOW_DIVIDEND_YIELD",
   "type": "double",
   "nullable": true
  },
  {
   "name": "LOW_EV_TO_T12M_EBIT",
   "type": "double",
   "nullable": true
  },
  {
   "name": "LOW_EV_TO_T12M_EBITDA",
   "type": "double",
   "nullable": true
  },
  {
   "name": "LOW_EV_TO_T12M_SALES",
   "type": "double",
   "nullable": true
  },
  {
   "name": "LOW_PRICE_TO_FREE_CASH_FLOW",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PE_RATIO",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PX_ERN_RATIO_WITH_HIGH_CLOS_PX",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PX_ERN_RATIO_WITH_LOW_CLOS_PX",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PX_LAST",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PX_TO_BOOK_RATIO",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PX_TO_FREE_CASH_FLOW",
   "type": "double",
   "nullable": true
  },
  {
   "name": "date",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "array of rows",
  "sampled_object": "bloomberg/harvest/bronze/histdata/security_key=ASML_NA_Equity/20261012T130159Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "valuation history",
  "historical PE EV/EBITDA dividend yield",
  "annual multiples"
 ],
 "common_queries": [
  "How has X's P/E and EV/EBITDA moved over the last decade?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/histdata/security_key=ASML_NA_Equity/20261012T130159Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/histdata_daily_px/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.histdata_daily_px",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/histdata_daily_px/",
 "layer": "bronze",
 "format": "json",
 "table": "histdata_daily_px",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T21:27:42Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 2,
  "bytes": 253287,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 2,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "<bloomberg security>",
   "type": "object-key",
   "nullable": false,
   "description": "the Bloomberg security string is the single top-level key"
  },
  {
   "name": "PX_LAST",
   "type": "double",
   "nullable": true
  },
  {
   "name": "date",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "array of rows",
  "sampled_object": "bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/20260922T212739Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "daily price history long"
 ],
 "common_queries": [
  "(2 securities only)"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/20260922T212739Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/identity/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.identity",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/identity/",
 "layer": "bronze",
 "format": "json",
 "table": "identity",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T13:22:14Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 68,
  "bytes": 25294,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 68,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "<bloomberg security>",
   "type": "object-key",
   "nullable": false,
   "description": "the Bloomberg security string is the single top-level key"
  },
  {
   "name": "CENTRAL_INDEX_KEY_NUMBER",
   "type": "string",
   "nullable": true
  },
  {
   "name": "COMPANY_WEB_ADDRESS",
   "type": "string",
   "nullable": true
  },
  {
   "name": "COMPOSITE_ID_BB_GLOBAL",
   "type": "string",
   "nullable": true
  },
  {
   "name": "EXCH_CODE",
   "type": "string",
   "nullable": true
  },
  {
   "name": "ID_BB_GLOBAL",
   "type": "string",
   "nullable": true
  },
  {
   "name": "ID_ISIN",
   "type": "string",
   "nullable": true
  },
  {
   "name": "ID_SEDOL1",
   "type": "string",
   "nullable": true
  },
  {
   "name": "LEGAL_ENTITY_IDENTIFIER",
   "type": "string",
   "nullable": true
  },
  {
   "name": "NAME",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "one record",
  "sampled_object": "bloomberg/harvest/bronze/identity/security_key=ABNB_US_Equity/20261007T132211Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "ISIN SEDOL FIGI LEI CIK",
  "security identifiers"
 ],
 "common_queries": [
  "What is X's ISIN?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_resolve_security",
   "inputs": {
    "query": "ticker, Bloomberg ticker, security_key, company or legal name, CIK, ISIN, SEDOL"
   },
   "returns": "status exact|candidates|none; security_key; display_ticker; bloomberg; name; cik; isin where held; other_listings[]; not_held[] (cusip)",
   "reads": "crosswalk/v1 newest, universe/v1 newest, bloomberg/harvest/bronze/identity newest per key; wraps lib/research/api/name_search.resolve_query",
   "answers": [
    "Which security is 'ASML'?",
    "What is the ISIN of X?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/identity/security_key=ABNB_US_Equity/20261007T132211Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/price_history_px_last/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.price_history_px_last",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/price_history_px_last/",
 "layer": "bronze",
 "format": "json",
 "table": "price_history_px_last",
 "grain": "one object per date; series map keyed by security",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "newest_write_utc": "2026-10-14T11:07:18Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 9,
  "bytes": 922102,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "as_of_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "kind",
   "type": "string",
   "nullable": true
  },
  {
   "name": "schema",
   "type": "string",
   "nullable": true
  },
  {
   "name": "series",
   "type": "object",
   "nullable": true
  },
  {
   "name": "window_end",
   "type": "string",
   "nullable": true
  },
  {
   "name": "window_start",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "bloomberg/harvest/bronze/price_history_px_last/date=2026-10-13/daily_30d.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "daily close prices",
  "price history 30 day 1 year"
 ],
 "common_queries": [
  "What did X close at each day this month?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/price_history_px_last/date=2026-10-13/daily_30d.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/price_history_tot_return/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.price_history_tot_return",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/price_history_tot_return/",
 "layer": "bronze",
 "format": "json",
 "table": "price_history_tot_return",
 "grain": "one object per date; series map keyed by security",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "newest_write_utc": "2026-10-14T11:07:27Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 11515,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "as_of_date",
   "type": "string",
   "nullable": true
  },
  {
   "name": "field",
   "type": "string",
   "nullable": true
  },
  {
   "name": "kind",
   "type": "string",
   "nullable": true
  },
  {
   "name": "schema",
   "type": "string",
   "nullable": true
  },
  {
   "name": "series",
   "type": "object",
   "nullable": true
  },
  {
   "name": "window_end",
   "type": "string",
   "nullable": true
  },
  {
   "name": "window_start",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "bloomberg/harvest/bronze/price_history_tot_return/date=2026-10-13/daily_5d.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [
  "total return 5 day"
 ],
 "common_queries": [
  "What is X's 5-day total return?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/price_history_tot_return/date=2026-10-13/daily_5d.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/refdata/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.refdata",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/refdata/",
 "layer": "bronze",
 "format": "json",
 "table": "refdata",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T13:12:36Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1167,
  "bytes": 13062011,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 100,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "<bloomberg security>",
   "type": "object-key",
   "nullable": false,
   "description": "the Bloomberg security string is the single top-level key"
  },
  {
   "name": "AVG_DAILY_VALUE_TRADED_3M",
   "type": "double",
   "nullable": true
  },
  {
   "name": "CIE_DES",
   "type": "string",
   "nullable": true
  },
  {
   "name": "CIE_DES_BULK",
   "type": "array",
   "nullable": true
  },
  {
   "name": "CNTRY_OF_DOMICILE",
   "type": "string",
   "nullable": true
  },
  {
   "name": "COUNTRY_FULL_NAME",
   "type": "string",
   "nullable": true
  },
  {
   "name": "CRNCY",
   "type": "string",
   "nullable": true
  },
  {
   "name": "CRNCY_ADJ_MKT_CAP",
   "type": "double",
   "nullable": true
  },
  {
   "name": "CURR_ENTP_VAL",
   "type": "double",
   "nullable": true
  },
  {
   "name": "CUR_MKT_CAP",
   "type": "double",
   "nullable": true
  },
  {
   "name": "EQY_BETA",
   "type": "double",
   "nullable": true
  },
  {
   "name": "EQY_DVD_YLD_IND",
   "type": "double",
   "nullable": true
  },
  {
   "name": "EQY_FREE_FLOAT_PCT",
   "type": "double",
   "nullable": true
  },
  {
   "name": "EQY_FUND_CRNCY",
   "type": "string",
   "nullable": true
  },
  {
   "name": "EQY_SH_OUT_REAL",
   "type": "double",
   "nullable": true
  },
  {
   "name": "ERN_ANN_DT_AND_PER",
   "type": "array",
   "nullable": true
  },
  {
   "name": "EXPECTED_REPORT_DT",
   "type": "string",
   "nullable": true
  },
  {
   "name": "GICS_SECTOR_NAME",
   "type": "string",
   "nullable": true
  },
  {
   "name": "LONG_COMP_NAME",
   "type": "string",
   "nullable": true
  },
  {
   "name": "NAME",
   "type": "string",
   "nullable": true
  },
  {
   "name": "NET_DEBT",
   "type": "double",
   "nullable": true
  },
  {
   "name": "PX_LAST",
   "type": "double",
   "nullable": true
  },
  {
   "name": "SHORT_NAME",
   "type": "string",
   "nullable": true
  },
  {
   "name": "VOLUME_AVG_30D",
   "type": "double",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "one record",
  "sampled_object": "bloomberg/harvest/bronze/refdata/security_key=ASML_NA_Equity/20261012T130159Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "reference data",
  "market cap",
  "beta",
  "sector",
  "net debt",
  "next earnings date"
 ],
 "common_queries": [
  "What is X's market cap, beta and next earnings date?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/refdata/security_key=ASML_NA_Equity/20261012T130159Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `bloomberg/harvest/bronze/segments/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.segments",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/segments/",
 "layer": "bronze",
 "format": "json",
 "table": "segments",
 "grain": "one object per (security_key, pull stamp)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T14:59:02Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 88,
  "bytes": 463708,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 85,
  "claim": "measured"
 },
 "columns": [
  {
   "name": "pulled_at",
   "type": "string",
   "nullable": true
  },
  {
   "name": "response",
   "type": "object",
   "nullable": true
  },
  {
   "name": "security",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "object",
  "sampled_object": "bloomberg/harvest/bronze/segments/security_key=ASML_NA_Equity/20261007T115115Z.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [
  "revenue by segment",
  "business segments"
 ],
 "common_queries": [
  "How is X's revenue split by segment?"
 ],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [
  {
   "name": "harvest_get_fundamentals",
   "inputs": {
    "security_key": "resolved key",
    "kind": "model|consensus|reference|valuation_history|segments|price",
    "mnemonics": "list, optional",
    "fiscal_years": "list, optional"
   },
   "returns": "model figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases; BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions",
   "reads": "derived/model_block (+_fye) newest per key; bloomberg/harvest/bronze bestdata/refdata/histdata/segments newest per key; price_history_* newest date",
   "answers": [
    "What were X's revenue and EPS since 2016?",
    "What is consensus EPS next year?",
    "What is X's P/E history?"
   ]
  }
 ],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix bloomberg/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object bloomberg/harvest/bronze/segments/security_key=ASML_NA_Equity/20261007T115115Z.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

### `sec/harvest/bronze/company_tickers/`

```json
{
 "contract_id": "opal-data-harvest/bronze/sec.harvest.bronze.company_tickers",
 "bucket": "opal-data-harvest",
 "s3_prefix": "sec/harvest/bronze/company_tickers/",
 "layer": "bronze",
 "format": "json",
 "table": "company_tickers",
 "grain": "not characterised",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST SEC harvest; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T20:15:07Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 800703,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [
  {
   "name": "<map key>",
   "type": "string"
  },
  {
   "name": "cik_str",
   "type": "int",
   "nullable": true
  },
  {
   "name": "ticker",
   "type": "string",
   "nullable": true
  },
  {
   "name": "title",
   "type": "string",
   "nullable": true
  }
 ],
 "column_notes": {
  "json_shape": "map",
  "sampled_object": "sec/harvest/bronze/company_tickers/date=2026-09-22/company_tickers.json",
  "columns_claim": "measured on 1 object (sample of 1)"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep (escape hatch); extend with the typed tools below"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_sec_harvest",
  "present": false,
  "parent_row_prefix": "sec/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "the catalog row is the source-level prefix sec/harvest/ (one row for several tables): split to a table row"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  },
  {
   "read": "get_object sec/harvest/bronze/company_tickers/date=2026-09-22/company_tickers.json",
   "at": "2026-10-14T13:0xZ"
  }
 ]
}
```

## 5. Plumbing and raw-store contracts (served through `harvest_read` only; no typed tool proposed)

### `amgt/harvest/bronze/research-report-extract/`

```json
{
 "contract_id": "opal-data-harvest/bronze/amgt.harvest.bronze.research-report-extract",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/bronze/research-report-extract/",
 "layer": "bronze",
 "format": "json",
 "table": "research-report-extract",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST research-report extract; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-26",
  "newest_write_utc": "2026-09-26T00:34:15Z",
  "trading_days_behind_t1": 12,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 710,
  "bytes": 124995497,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 94,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_bronze",
  "present": false,
  "parent_row_prefix": "amgt/harvest/bronze/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/bronze/research-report/`

```json
{
 "contract_id": "opal-data-harvest/bronze/amgt.harvest.bronze.research-report",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/bronze/research-report/",
 "layer": "bronze",
 "format": "pdf",
 "table": "research-report",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST research-report extract; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-11",
  "newest_write_utc": "2026-10-11T09:59:50Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 368,
  "bytes": 312748396,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 95,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_bronze",
  "present": false,
  "parent_row_prefix": "amgt/harvest/bronze/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/bronze/research_template/`

```json
{
 "contract_id": "opal-data-harvest/bronze/amgt.harvest.bronze.research_template",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/bronze/research_template/",
 "layer": "bronze",
 "format": "xlsx",
 "table": "research_template",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST research-report extract; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-11",
  "newest_write_utc": "2026-10-11T18:48:14Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 383839,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_bronze",
  "present": false,
  "parent_row_prefix": "amgt/harvest/bronze/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/bronze/run_record/`

```json
{
 "contract_id": "opal-data-harvest/bronze/amgt.harvest.bronze.run_record",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/bronze/run_record/",
 "layer": "bronze",
 "format": "json",
 "table": "run_record",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST research-report extract; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "newest_write_utc": "2026-10-14T12:08:11Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 3205,
  "bytes": 56796658,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_bronze",
  "present": false,
  "parent_row_prefix": "amgt/harvest/bronze/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/gold/research-backlog/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research-backlog",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research-backlog/",
 "layer": "gold",
 "format": "json",
 "table": "research-backlog",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-26",
  "newest_write_utc": "2026-09-26T03:08:30Z",
  "trading_days_behind_t1": 12,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 21,
  "bytes": 1326854,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_research-backlog",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/gold/research-fund-form/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research-fund-form",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research-fund-form/",
 "layer": "gold",
 "format": "json",
 "table": "research-fund-form",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-25",
  "newest_write_utc": "2026-09-25T05:08:29Z",
  "trading_days_behind_t1": 12,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 9,
  "bytes": 7629423,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_research-fund-form",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/gold/research-model-typecast/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research-model-typecast",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research-model-typecast/",
 "layer": "gold",
 "format": "json",
 "table": "research-model-typecast",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-25",
  "newest_write_utc": "2026-09-25T05:09:31Z",
  "trading_days_behind_t1": 12,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 4,
  "bytes": 481973,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_research-model-typecast",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/gold/research-sector-template/`

```json
{
 "contract_id": "opal-data-harvest/gold/amgt.harvest.gold.research-sector-template",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/gold/research-sector-template/",
 "layer": "gold",
 "format": "json",
 "table": "research-sector-template",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "report-derived research table (AMGT_RESAPP); the writing function of this exact table is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-25",
  "newest_write_utc": "2026-09-25T05:07:57Z",
  "trading_days_behind_t1": 12,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 29,
  "bytes": 305012,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_research-sector-template",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/state/filing_attempt/`

```json
{
 "contract_id": "opal-data-harvest/state/amgt.harvest.state.filing_attempt",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/state/filing_attempt/",
 "layer": "state",
 "format": "json",
 "table": "filing_attempt",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST harvest state; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-09",
  "newest_write_utc": "2026-10-09T06:20:48Z",
  "trading_days_behind_t1": 2,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 181,
  "bytes": 85074,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 181,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_state",
  "present": false,
  "parent_row_prefix": "amgt/harvest/state/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/state/freshness_snapshot/`

```json
{
 "contract_id": "opal-data-harvest/state/amgt.harvest.state.freshness_snapshot",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/state/freshness_snapshot/",
 "layer": "state",
 "format": "json",
 "table": "freshness_snapshot",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST harvest state; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "newest_write_utc": "2026-10-13T12:30:44Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 1217597,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_state",
  "present": false,
  "parent_row_prefix": "amgt/harvest/state/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `amgt/harvest/state/pull_log/`

```json
{
 "contract_id": "opal-data-harvest/state/amgt.harvest.state.pull_log",
 "bucket": "opal-data-harvest",
 "s3_prefix": "amgt/harvest/state/pull_log/",
 "layer": "state",
 "format": "json",
 "table": "pull_log",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST harvest state; the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T13:12:37Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1128,
  "bytes": 6368361,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 99,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_amgt_harvest_state",
  "present": false,
  "parent_row_prefix": "amgt/harvest/state/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `barrons/harvest/bronze/article/`

```json
{
 "contract_id": "opal-data-harvest/bronze/barrons.harvest.bronze.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "barrons/harvest/bronze/article/",
 "layer": "bronze",
 "format": "json",
 "table": "article",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T04:19:21Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 203,
  "bytes": 29010224,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_barrons_harvest",
  "present": false,
  "parent_row_prefix": "barrons/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `barrons/harvest/bronze/news_listing/`

```json
{
 "contract_id": "opal-data-harvest/bronze/barrons.harvest.bronze.news_listing",
 "bucket": "opal-data-harvest",
 "s3_prefix": "barrons/harvest/bronze/news_listing/",
 "layer": "bronze",
 "format": "html",
 "table": "news_listing",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T04:45:50Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 571,
  "bytes": 279758718,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_barrons_harvest",
  "present": false,
  "parent_row_prefix": "barrons/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `bloomberg/harvest/bronze/article/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/article/",
 "layer": "bronze",
 "format": "html",
 "table": "article",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "newest_write_utc": "2026-10-13T16:59:58Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 2997,
  "bytes": 1008977667,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `bloomberg/harvest/bronze/news_listing/`

```json
{
 "contract_id": "opal-data-harvest/bronze/bloomberg.harvest.bronze.news_listing",
 "bucket": "opal-data-harvest",
 "s3_prefix": "bloomberg/harvest/bronze/news_listing/",
 "layer": "bronze",
 "format": "xml",
 "table": "news_listing",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-14",
  "newest_write_utc": "2026-10-14T10:16:12Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1147,
  "bytes": 1932027439,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_bloomberg_harvest",
  "present": false,
  "parent_row_prefix": "bloomberg/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `ft/harvest/bronze/article/`

```json
{
 "contract_id": "opal-data-harvest/bronze/ft.harvest.bronze.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "ft/harvest/bronze/article/",
 "layer": "bronze",
 "format": "html",
 "table": "article",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-05",
  "newest_write_utc": "2026-10-05T02:00:01Z",
  "trading_days_behind_t1": 6,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 185,
  "bytes": 28820697,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_ft_harvest",
  "present": false,
  "parent_row_prefix": "ft/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `ft/harvest/bronze/news_listing/`

```json
{
 "contract_id": "opal-data-harvest/bronze/ft.harvest.bronze.news_listing",
 "bucket": "opal-data-harvest",
 "s3_prefix": "ft/harvest/bronze/news_listing/",
 "layer": "bronze",
 "format": "html",
 "table": "news_listing",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-05",
  "newest_write_utc": "2026-10-05T01:49:11Z",
  "trading_days_behind_t1": 6,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 39,
  "bytes": 7667891,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_ft_harvest",
  "present": false,
  "parent_row_prefix": "ft/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `lib/local-publications/`

```json
{
 "contract_id": "opal-data-harvest/gold/lib.local-publications",
 "bucket": "opal-data-harvest",
 "s3_prefix": "lib/local-publications/",
 "layer": "gold",
 "format": "zip",
 "table": "local-publications",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST release build (lib/opal_data_harvest/build_release.py, by name); the upload of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-15",
  "newest_write_utc": "2026-09-15T14:49:53Z",
  "trading_days_behind_t1": 20,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 6,
  "bytes": 445796,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_lib_local_publications",
  "present": true,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `raw/bloomberg/`

```json
{
 "contract_id": "opal-data-harvest/gold/raw.bloomberg",
 "bucket": "opal-data-harvest",
 "s3_prefix": "raw/bloomberg/",
 "layer": "gold",
 "format": "json",
 "table": "bloomberg",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "integrations/bloomberg/research and AMGT_HARVST (raw/bloomberg and raw/seekingalpha); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-30",
  "newest_write_utc": "2026-09-30T15:15:01Z",
  "trading_days_behind_t1": 9,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 123,
  "bytes": 555850,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 39,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_raw",
  "present": false,
  "parent_row_prefix": "raw/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `raw/seekingalpha/`

```json
{
 "contract_id": "opal-data-harvest/gold/raw.seekingalpha",
 "bucket": "opal-data-harvest",
 "s3_prefix": "raw/seekingalpha/",
 "layer": "gold",
 "format": "json",
 "table": "seekingalpha",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "<security_key path segment>"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "integrations/bloomberg/research and AMGT_HARVST (raw/bloomberg and raw/seekingalpha); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-11",
  "newest_write_utc": "2026-09-11T19:18:57Z",
  "trading_days_behind_t1": 22,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 18,
  "bytes": 209361,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_raw",
  "present": false,
  "parent_row_prefix": "raw/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/bronze/analysis/`

```json
{
 "contract_id": "opal-data-harvest/bronze/seeking-alpha.harvest.bronze.analysis",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/bronze/analysis/",
 "layer": "bronze",
 "format": "json",
 "table": "analysis",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T04:54:54Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 18762,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/bronze/article/`

```json
{
 "contract_id": "opal-data-harvest/bronze/seeking-alpha.harvest.bronze.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/bronze/article/",
 "layer": "bronze",
 "format": "json",
 "table": "article",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T12:06:09Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 19472,
  "bytes": 85808257,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/bronze/news/`

```json
{
 "contract_id": "opal-data-harvest/bronze/seeking-alpha.harvest.bronze.news",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/bronze/news/",
 "layer": "bronze",
 "format": "json",
 "table": "news",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T04:54:54Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 43649,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/bronze/news_listing/`

```json
{
 "contract_id": "opal-data-harvest/bronze/seeking-alpha.harvest.bronze.news_listing",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/bronze/news_listing/",
 "layer": "bronze",
 "format": "json",
 "table": "news_listing",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T12:01:38Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 11127,
  "bytes": 797027585,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/bronze/report/`

```json
{
 "contract_id": "opal-data-harvest/bronze/seeking-alpha.harvest.bronze.report",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/bronze/report/",
 "layer": "bronze",
 "format": "json",
 "table": "report",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T04:54:54Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 24116,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/bronze/symbol/`

```json
{
 "contract_id": "opal-data-harvest/bronze/seeking-alpha.harvest.bronze.symbol",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/bronze/symbol/",
 "layer": "bronze",
 "format": "json",
 "table": "symbol",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-09-22",
  "newest_write_utc": "2026-09-22T04:54:53Z",
  "trading_days_behind_t1": 15,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 3,
  "bytes": 58098,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 3,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/silver/quarantine/`

```json
{
 "contract_id": "opal-data-harvest/silver/seeking-alpha.harvest.silver.quarantine",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/silver/quarantine/",
 "layer": "silver",
 "format": "json",
 "table": "quarantine",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-01",
  "newest_write_utc": "2026-10-01T06:48:01Z",
  "trading_days_behind_t1": 8,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 3908,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `seeking-alpha/harvest/state/job_record/`

```json
{
 "contract_id": "opal-data-harvest/state/seeking-alpha.harvest.state.job_record",
 "bucket": "opal-data-harvest",
 "s3_prefix": "seeking-alpha/harvest/state/job_record/",
 "layer": "state",
 "format": "json",
 "table": "job_record",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "security_key"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-12",
  "newest_write_utc": "2026-10-12T12:00:18Z",
  "trading_days_behind_t1": 1,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 238,
  "bytes": 57774,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": 237,
  "claim": "measured"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "path segment / column"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_seeking_alpha_harvest",
  "present": false,
  "parent_row_prefix": "seeking-alpha/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `social/v1/`

```json
{
 "contract_id": "opal-data-harvest/gold/social.v1",
 "bucket": "opal-data-harvest",
 "s3_prefix": "social/v1/",
 "layer": "gold",
 "format": "json",
 "table": "v1",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": null,
  "schedule": null,
  "claim": "absent",
  "basis": "not traced"
 },
 "freshness": {
  "latest_partition": "2026-09-15",
  "newest_write_utc": "2026-09-15T16:56:48Z",
  "trading_days_behind_t1": 20,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 1,
  "bytes": 12088,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: plumbing record"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": null,
  "present": false,
  "parent_row_prefix": null,
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [
  "no DATA_CATALOG harvest_datasets row covers this prefix"
 ],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `wsj/harvest/bronze/article/`

```json
{
 "contract_id": "opal-data-harvest/bronze/wsj.harvest.bronze.article",
 "bucket": "opal-data-harvest",
 "s3_prefix": "wsj/harvest/bronze/article/",
 "layer": "bronze",
 "format": "html",
 "table": "article",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-07",
  "newest_write_utc": "2026-10-07T12:12:52Z",
  "trading_days_behind_t1": 4,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "newest object LastModified (UTC); no date partition",
  "claim": "measured"
 },
 "size": {
  "objects": 615,
  "bytes": 400185610,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_wsj_harvest",
  "present": false,
  "parent_row_prefix": "wsj/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

### `wsj/harvest/bronze/news_listing/`

```json
{
 "contract_id": "opal-data-harvest/bronze/wsj.harvest.bronze.news_listing",
 "bucket": "opal-data-harvest",
 "s3_prefix": "wsj/harvest/bronze/news_listing/",
 "layer": "bronze",
 "format": "xml",
 "table": "news_listing",
 "grain": "not read by this census (plumbing / raw store)",
 "partition": {
  "keys": [
   "date"
  ],
  "claim": "measured"
 },
 "producer": {
  "name": "AMGT_HARVST publisher harvest (lib/opal_data_harvest); the writing code of this exact prefix is not traced by this row",
  "schedule": null,
  "claim": "inferred",
  "basis": "DATA_CATALOG.yaml harvest_datasets producer field"
 },
 "freshness": {
  "latest_partition": "2026-10-13",
  "newest_write_utc": "2026-10-13T18:46:06Z",
  "trading_days_behind_t1": 0,
  "t1": "2026-10-13",
  "basis": "trading-day-frontier",
  "derived_from": "date= partition in the key",
  "claim": "measured"
 },
 "size": {
  "objects": 927,
  "bytes": 1005746236,
  "claim": "measured"
 },
 "securities": {
  "distinct_keys": null,
  "claim": "absent"
 },
 "columns": [],
 "column_notes": {
  "note": "columns not read: raw html/xml/binary documents"
 },
 "enums": {},
 "fork_keys": {
  "firm": {
   "column_or_key_segment": null,
   "values": [],
   "note": "not client data: Opal research, firm-agnostic; Opal principals only (list v4)"
  },
  "account": null,
  "platform": null,
  "security": {
   "key": "security_key",
   "form": "<ROOT>_<CC>_Equity",
   "reached_by": "not per security"
  }
 },
 "nl_tags": [],
 "common_queries": [],
 "never_sum_rules": [],
 "existing_gateway_tool": {
  "name": "harvest_list / harvest_read (raw object read, app/harvest_read.py)",
  "verdict": "keep"
 },
 "proposed_tools": [],
 "catalog_entry": {
  "data_catalog_key": "harvest_wsj_harvest",
  "present": false,
  "parent_row_prefix": "wsj/harvest/",
  "read_tool_in_catalog": null
 },
 "prior_art": "org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPAL_DATA_HARVEST_TOOLSET_ASSESSMENT_20261014.md@eea2acd58e",
 "open_items": [],
 "evidence": [
  {
   "read": "list_objects_v2 opal-data-harvest (59 pages, 58,639 keys)",
   "at": "2026-10-14T12:05Z"
  }
 ]
}
```

## 6. What could not be read, and why

- **Producer schedules:** the `producer` names come from the catalog rows (claim inferred). No schedule or EventBridge target was read for any table, so `schedule` is null throughout.
- **JSON columns:** read from one object per dataset; another object of the same dataset may carry more fields.
- **Plumbing columns:** none read (31 datasets).
- **Text columns:** no text value was read or reproduced.
- **Defects:** the D1-D9 findings of the assessment @eea2acd58e section 5 stand unchanged. They bind the tools in section 3, chiefly newest-part reads and stated trading-day lag.

-- 4.0.0_SA_CRO~Z
