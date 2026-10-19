# Gateway tool-call audit, part 2: harvest, news, ETFs, portal, MDPF and discovery

**Author:** 4.0.0_SA_CRO~Z, 2026-10-19 ~18:0xZ (2:0x PM ET).
**Order:** Andrew-direct ~16:2xZ, record @634d368d98. **Part 1** (opal-data-assets):
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_TOOL_AUDIT_OPAL_DATA_ASSETS_20261019.md` @216dfc8144.
**Routing of part 1:** CTO @473f5177a8. **Part 1 rows:** NFRA_OPLGTW-Z-S409..Z-S412 @a4832d37e1.

**Instrument.** The same as part 1:
- one live call per tool through the served gateway (opalgateway MCP, Andrew@, master_admin), read
  2026-10-19 17:2xZ-17:5xZ;
- read-only checks of answers against S3 and DynamoDB;
- source at HEAD for every cause named.

Three forks of this seat ran the three buckets in parallel. Their tables are below as returned; the compilation and the
cross-bucket reading are mine.

## 1. Answer first

**Denominator.** 62 tools called, one call each, from part 2's scope lists (from the gateway's tool list and the
catalog's buckets, not a census of the served page):

| Part | Tools | PASS | of which a caveat | FAIL |
|---|---|---|---|---|
| 2a harvest + news | 18 | 17 | 6: 5 stale, 1 degraded | 1 |
| 2b ETFs | 19 | 19 | 4 | 0 |
| 2c portal + MDPF + discovery | 25 | 21 | 6: 4 oversize, 2 stale | 4 |
| **total** | **62** | **57** | **16** | **5** |

The chatter tool is counted as a PASS. Its freshness is FAIL-class (6 trading days behind), and it is listed under H1.

No answer contradicted its source where checked: 16 spot-checks against S3/DynamoDB, all equal. Routing is correct by
bucket for 58 of 62 tools. The other 4 read somewhere other than the catalog says:
- `harvest_get_published_analysis` reads through the AMGT scoped API;
- `etfs_get_positioning` reads portal-v2 by default;
- `etfs_get_security_reference` also reads `security_universe`, which the catalog does not list;
- `mdpf_get_security_classification` reads a DynamoDB table with no catalog row.

**The real failures are of three kinds, not wrong data.**

1. **Size handling breaks answers: 4 of the 5 FAILs.** The fifth is `news_for_security` (H2).
   - The 50 KB projection is measured on compact JSON while the reply is sent indented (P4). Five more replies arrive
     over the limit.
   - The trimming nulls whole fields (P5): `portal_get_macro` loses all its macro data, and `portal_get_valuation`
     shrinks to 420 bytes.
   - The MDPF envelope has no projection at all (P6): `mdpf_get_aggregate_aua` returns 743 KB.
   - `opal_discover` over-matches and has no cap (P7): 137 datasets, 585 KB.
   - Fix owner: NFRA_OPLGTW (`harvest_typed._size` / `project`, and the MDPF and discover envelopes).
2. **Stale producers behind correct tools.** The gateway reports these lags honestly; the cause is upstream.
   - Article mentions and chatter stopped 10-08 (H1), which takes down `news_for_security` (H2).
   - Security scanner 10-02.
   - ETF classifications 09-30.
   - Harvest posture and scores about 21-22 trading days old.
   - Capital-markets views 2026-01-09.
3. **A data gap that changes a number Andrew reads.** 49F ownership of Opal's ETFs is built from one Schwab master
   only (E1). DIVZ alone is understated by $1,673,459.07 across 17 accounts, and the ownership rollup inherits it. This
   is the same two-master shape as part 1's Schwab finding.

**Lesser:**
- two prices for one ETF holding on one date (E2);
- unlabelled units on `etfs_get_positioning` (E4);
- two freshness rules contradicting each other (P8);
- URL, duplicate-key and metadata hygiene (H4, H5, E5).

## 2. Part 2a -- opal-data-harvest and news (18 tools)

Read 2026-10-19 ~17:2xZ-17:4xZ through the served gateway (Andrew@). Test securities: ASML (well covered), AAPL and NVDA.
18 of 18 called:
- 16 PASS, 6 of them verified against the source and 5 stale;
- 1 PASS whose freshness is FAIL-class (chatter);
- 1 FAIL (news_for_security).

Every call took under 60 s.

| Tool | Verdict | Routed to | Catalog bucket matches? | Note |
|---|---|---|---|---|
| harvest_resolve_security | PASS, stale input | `crosswalk/v1/2026-10-09`, `universe/v1/2026-10-06` | yes | resolves names the harvest holds nothing for (H3) |
| harvest_list | PASS | `packs/` (105 prefixes) | yes | duplicate key spellings (H5) |
| harvest_read | PASS, verified | `packs/ASML_NA_Equity/input_ledger.json` | yes | |
| harvest_security_coverage | PASS, verified | 31 dataset prefixes | yes | |
| harvest_get_fundamentals | PASS, verified | `bloomberg/harvest/bronze/price_history_px_last/date=2026-10-16` | yes | current |
| harvest_get_peers_and_scores | PASS, verified, stale parts | `peers/v1` 10-11, `posture/v1` 09-16, `scores/v1` | yes | peers 5, posture 22, scores 21 trading days old |
| harvest_get_filing_analysis | PASS | `filings/v1`, `drafting/v1`, sec silver | yes | 55 KB reply (H6) |
| harvest_get_research | PASS | dossier 10-18, continuation, ai_fill 10-16 | yes | one ai_fill sentence graded UNSUPPORTED inside a block whose validation reads PASS |
| harvest_get_published_analysis | PASS | `opal-amgt-scoped-api` overlay | **partly** (H7) | feed's newest item is 10-05 |
| harvest_get_chatter | PASS, stale (FAIL-class) | `chatter_daily/date=2026-10-08`, `chatter_window/date=2026-10-04` | yes | `trading_days_behind_t1` 6 (H1) |
| harvest_search_articles | PASS, stale | `article_security_mention/date=2026-10-08`, `article_sentiment/date=2026-10-03` | yes | url null for sa, ft and barrons items (H4) |
| harvest_get_article | PASS, stale | mention 10-08 + SA silver 10-02 | yes | url, words and content_status null |
| harvest_query_columns | PASS, verified | `chatter_daily` 10-08 part | yes | |
| news_for_security | **FAIL** | `article_security_mention/date=2026-10-08` only | yes | H2 |
| news_keyword_intelligence | PASS | DynamoDB `opal-keyword-intelligence` 10-16 | yes | 61 KB reply (H6) |
| news_market_mood | PASS, verified | portal-v2 `json/sentiment/` | yes | current |
| news_search_articles | PASS | DynamoDB `opal-news-articles` 10-14..16 | yes | the same article is not deduplicated across RSS and NEWSAPI copies |
| news_trending_topics | PASS, degraded | DynamoDB `opal-news-trending-daily` 10-16 | yes | H8 |

**Harvest and news defects:**

- **H1 -- the article-mention and chatter producers stopped on 10-08/10-09.**
  - Newest partitions: `article_security_mention` 10-08, `chatter_daily` 10-08, `chatter_window` 10-04, `article_sentiment`
    10-03.
  - Every per-security news and chatter answer is therefore 6-9 trading days old. The gateway states the lag; the cause is
    upstream.
- **H2 -- `news_for_security` answers 0 for an active name.**
  - Its index is H1's stale partition, and its fallback matches only the ticker text.
  - NVDA, 7 days: 0 mentions, with no reason given, while `news_search_articles` finds 35 Nvidia articles for 10-14..10-16.
- **H3 -- the resolver's universe is far wider than what the harvest holds.** AAPL resolves `exact`, but nothing
  downstream holds research or market data for it.
- **H4 -- the same article has a URL in one tool and not another.** For one Seeking Alpha item, the URL is null in
  `harvest_search_articles` and `harvest_get_article` but present in `harvest_get_published_analysis`.
- **H5 -- duplicate key spellings under `packs/`.** For example `BABA_US/` beside `BABA_US_Equity/`. Hygiene only.
- **H6 -- replies over the 50 KB projection.** `news_keyword_intelligence` 61 KB, `harvest_get_filing_analysis` 55 KB.
- **H7 -- `harvest_get_published_analysis` is catalogued in opal-data-harvest but reads through `opal-amgt-scoped-api`.**
  The same misgrouping as P2.
- **H8 -- `news_trending_topics` returns a hollow sentiment block.** Citations are empty, and 6 of 7 sentiment axes are 0
  on every row.

Not exercised: paging, the full-text flags, fundamentals kinds other than price, and the `as_of` arguments.

## 3. Part 2b -- opal-data-etfs (19 tools)

Read 2026-10-19 ~17:2xZ-17:5xZ through the served gateway (Andrew@). 19 of 19 called: 19 PASS (4 with a caveat), 0 FAIL.
Five answers match the S3 objects exactly: nav_history, fund_holdings, partner_ownership, rival_fund_holdings and who_holds.
Every call took under 60 s. Every source is at T-1 (10-16) or later, except four rivals at 10-15, within their declared
one-trading-day allowance.

| Tool | Verdict | Routed to | Catalog bucket matches? | Note |
|---|---|---|---|---|
| etfs_compare_peers | PASS | opal-data-etfs `rivalfunds/etfs/gold/{peer_group_map,buying_trend,holding_contribution}` 10-19 | yes | valid periods are listed when one is rejected |
| etfs_get_coverage | PASS, truncated | `holdings_coverage` 10-16, `input_census`, `canonical_shape` | yes | the no-argument call shows 2 of 13 funds (1,642-byte projection cap); a per-fund call is complete |
| etfs_get_fund_bloomberg_characteristics | PASS | `bbg/2026-10-16/` | yes | |
| etfs_get_fund_flows | PASS | `rivalfunds/etfs/gold/flow_reconciliation` | yes | claim INFERRED per row |
| etfs_get_fund_holdings | PASS, S3-verified | `gold/holding` + `gold/book` 10-16 | yes | |
| etfs_get_fund_nav_history | PASS, S3-verified | `silver/netassets_daily.parquet` | yes | |
| etfs_get_fund_snapshot | PASS | `snapshots/snapshot_2026-10-18.json` | yes | the file is dated Sunday 10-18; the NAV is as of 10-16 |
| etfs_get_fund_trades | PASS, metadata gap | `rivalfunds/etfs/gold/trade_schedule` | yes | per-row claim null |
| etfs_get_monthly_report | PASS | `platinum/reports/2026-09/` | yes | |
| etfs_get_new_securities | PASS | `mdpf/etfs/gold/new_securities/date=2026-10-19` | yes (an `mdpf/` prefix) | |
| etfs_get_ownership_rollup | PASS | `platinum/etf_ownership_dashboard.json` | yes | grand total $662.6M; understated, see E1 |
| etfs_get_partner_ownership | PASS, S3-verified; upstream gap | `daily/49financial/2026-10-16.json` | yes | E1 |
| etfs_get_peer_group_members | PASS | `rivalfunds/etfs/gold/peer_group_map` | yes | |
| etfs_get_positioning | PASS | **opal-data-portal-v2** `platinum/etfs/positioning_data.json` (opal-data-etfs `gold/book` only for another as_of) | partly | E4 |
| etfs_get_research_notes | PASS | `rivalfunds/etfs/gold/research_hypotheses` | yes | labelled AI-generated |
| etfs_get_rival_fund_holdings | PASS, S3-verified | `rivalfunds/etfs/gold/canonical_shape` | yes | |
| etfs_get_rival_page_status | PASS | `rivalfunds/etfs/platinum/page/date=2026-10-19` | yes | 13 of 13 funds updated |
| etfs_get_security_reference | PASS | `security_universe`, `security_market`, `corporate_actions`; `security_names` 10-08 | partly | also reads `security_universe`, which the catalog does not list; `total_return_index` holds a one-day return |
| etfs_who_holds | PASS, S3-verified | `security_universe` + `canonical_shape` | yes | |

**ETF defects:**

- **E1 -- 49F ownership of Opal's ETFs is understated (DIVZ by $1,673,459.07, 17 accounts).**
  - Cause: the producer of `daily/49financial/<date>.json` reads Schwab master 08242234 only.
  - Master 08335338 holds the same 5,899 accounts plus 17 more.
  - Only DIVZ was measured; IDVZ, PFDE and PFOE are not checked.
  - The rollup inherits the gap. The owner is the producer, not the gateway.
- **E2 -- one holding, two values on one date.** PFOE's ASML on 10-16 is:
  - $5,534,192.16 at price 1,657.44 in `etfs_get_fund_holdings`;
  - $5,481,035.28 at price 1,641.52 in `etfs_who_holds`.

  The two producers price at different vintages under the same date label.
- **E3 -- the coverage answer is truncated when no fund is given.** Also, its coverage table lags the holdings for BASG
  (10-15 vs 10-16).
- **E4 -- `etfs_get_positioning`'s source depends on its arguments, and its units are not labelled.**
  - Its `aum` is about 10^6 smaller than in `etfs_get_fund_holdings`.
  - Its weights are fractions where `etfs_get_fund_holdings` uses percentage points.
  - It is filed under portal-v2 while it shows opal-data-etfs indexes.
- **E5 -- minor metadata.** The trades rows carry a null claim, and `total_return_index` is misnamed.

## 4. Part 2c -- opal-data-portal-v2, opal-data-mdpf and discovery (25 tools)

Read 2026-10-19 ~17:2xZ-17:5xZ through the served gateway (Andrew@), firm 49financial where one is asked.
- 25 of 25 called: 21 PASS (6 with a caveat), 4 FAIL.
- 5 answers match S3, and a head check confirms 6 routed keys: etf_returns, aum_metrics, peer_performance, correlations,
  and the valuation summary.
- Every call took under 60 s.

| Tool | Verdict | Routed to | Catalog bucket matches? | Note |
|---|---|---|---|---|
| portal_get_cma_assumptions | PASS | portal-v2 `json/capital-markets/assumptions.json` | yes | 5 of 27 members are null category headers |
| portal_get_correlations | PASS, S3-checked | portal-v2 `json/correlations/correlation_data.json` | yes | 10-16 |
| portal_get_etf_returns | PASS, S3-checked | portal-v2 `json/benchmarks/etf_returns.json` | yes | |
| portal_get_factor_tilts | PASS | portal-v2 `json/factor-tilts/tier1-snapshot.json` | yes | a bad `part` is refused under a guard-denial label |
| portal_get_macro | **FAIL** | portal-v2 macro, volatility and yield-curve keys | yes | `macro: null`, truncated; the source is 93 KB (P5) |
| portal_get_market_regime | PASS | portal-v2 `json/market/market-regime.json` | yes | the history holds a Saturday (10-17) point |
| portal_get_market_returns | PASS, oversize | portal-v2 `json-tiered/market-overview/summary/all-returns.json` | yes | 55.7 KB served (P4) |
| portal_get_model_attribution | PASS | portal-v2 `json/positioning/holdings_attribution_data.json` | yes | monthly, 09-30 |
| portal_get_model_portfolio_timeseries | PASS, oversize | portal-v2 `json/benchmarks/model_portfolio_timeseries.json` | yes | 64.9 K characters against "projected 51,100" (P4) |
| portal_get_model_positioning | PASS, oversize | portal-v2 positioning keys | yes | 75.9 K characters against "projected 48,954" (P4) |
| portal_get_peer_performance | PASS, S3-checked | portal-v2 `json/peers/peer_performance.json` | yes | |
| portal_get_pipeline_freshness | PASS, contradiction | portal-v2 `json/latest/manifest.json` | key not in the catalog | calls `peer_excel` and `attribution_excel` stale (trading-day rule) while `peer_performance` calls the same data current (month-end rule) |
| portal_get_security_scan | PASS, **stale** | portal-v2 `json/security_scanner/latest/` | yes | as of 10-02, 10 trading days |
| portal_get_trending | PASS | portal-v2 `json/trending/latest.json` | yes | 10-19 |
| portal_get_valuation | **FAIL** | portal-v2 `json/valuation/valuation_data.json` + `risk_premium_data.json` | yes | 420 bytes: ranges emptied, time_series nulled (P5) |
| mdpf_get_account_distribution | PASS | portal-v2 `platinum/mdpf/49financial/account-distribution.json` | yes | 10-19 |
| mdpf_get_aggregate_aua | **FAIL** | portal-v2 `platinum/mdpf/49financial/aggregate-aua-timeseries.json` | yes | 743,469 characters, no projection (P6) |
| mdpf_get_aum_metrics | PASS, S3-checked | portal-v2 `platinum/mdpf/49financial/aum-metrics.json` | yes | $1,804,123,100.01, 7,502 accounts |
| mdpf_get_category_views | PASS | portal-v2 `platinum/mdpf/49financial/category-views.json` | yes | total equals aum_metrics |
| mdpf_get_model_benchmarks | PASS | portal-v2 `json/benchmarks/model_portfolio_benchmarks.json` | yes | 10-16 |
| mdpf_get_model_composition | PASS, oversize | opal-data-mdpf `mdpf/feeds/model_composition/49financial/2026-10-19.parquet` | yes | 59.1 KB (P4) |
| mdpf_get_security_classification | PASS, **stale** | DynamoDB `etf-classifications` | no catalog row | 09-30, 12 trading days; `classified_by: seed` |
| opal_discover | **FAIL** | the catalog | n/a | "client account holdings" matched 137 datasets, 585 KB (P7) |
| opal_describe | PASS | the catalog | n/a | its "measured" facts are dated (newest partition stated as 10-14) |
| gateway_query_catalog | PASS | portal-v2 `json/capital-markets/views.json` | yes | the data is from 2026-01-09; an off-catalog key gets a correct 404 refusal |

**Portal, MDPF and discovery defects:**

- **P4 -- the size check runs on compact JSON, but the reply is sent indented.**
  - `harvest_typed._size()` measures `json.dumps` with no indent, and the served text is pretty-printed.
  - Replies "projected" to 50 KB arrive 27-55% larger and overflow the client's tool-result limit.
- **P5 -- the trimming discards more than it must.**
  - `harvest_typed.project()` empties the largest list first, and nulls a non-list field only after no list is left.
  - `portal_get_macro` returns `macro: null`, and `portal_get_valuation` shrinks to 420 bytes.
- **P6 -- the MDPF reply envelope has no projection at all.** `mdpf_get_aggregate_aua` returns 743 KB.
- **P7 -- `opal_discover` over-matches and has no size cap.**
- **P8 -- two freshness rules contradict each other.** `portal_get_pipeline_freshness` applies the trading-day rule to
  monthly sources, and reads a manifest key the catalog does not hold.

**Stale producers:**
- the security scanner (10-02);
- the ETF classifications (09-30);
- the capital-markets views (2026-01-09).

## 5. Who fixes what (proposed; the CTO routes)

| Item | Kind | Proposed owner |
|---|---|---|
| P4, P5, P6, P7 (size and projection) | gateway code | NFRA_OPLGTW (`2.0.0_SA_COO~O`) |
| H2 (`news_for_security` fallback by name, and a reason when 0) | gateway code | NFRA_OPLGTW |
| H7, E4, P8 key, and the 4 routing mismatches | catalog | NFRA_MCPINDEX (`2.0.0_SA_COO~MI`) |
| H1 article-mention and chatter producers (10-08) | producer | its pipeline's owner (AMGT harvest / news) |
| E1 49F ETF ownership built from one Schwab master | producer | the ETF ownership (`daily/<firm>/`) producer's owner |
| security scanner (10-02), ETF classifications (09-30), capital-markets views (2026-01-09), harvest posture and scores | producer | each pipeline's owner |
| E2, E3, E5, H3, H4, H5, H6, H8 | hygiene | NFRA_OPLGTW / NFRA_MCPINDEX at the battery's next round |

## 6. Bounds

- **Coverage.** One call per tool with one realistic input. Not exercised: paging, `as_of`, full-text flags, and the
  other `kind`/`part` values. A defect that bites only another input would not show here.
- **What is not in parts 1-2.** Every Microsoft 365 tool, the YCharts and Bloomberg integrations, `graph_cypher` /
  `graph_status`, `opal_asker_query`, and the two Teams-poll tools. Those are part 3. Send and write tools would run only
  on their preview path (`confirm=false`), never sending.
- **Writes.** Nothing was written anywhere but this file.
