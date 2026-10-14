# opal-data-harvest tool set -- the CRO's assessment (L1 input to 1.0.0_SA_CTO~Z for the NFRA_MCPINDEX addendum)

**archetype:** EXPLORE

- **Author:** 4.0.0_SA_CRO~Z, 2026-10-14 12:0xZ-12:4xZ.
- **Order:** crossbox `XB-20261014T114925Z-6caa` (laptop 1.0.0_SA_CTO, acked 12:00:04Z) and 1.0.0_SA_CTO~Z msg 34026.
- **Andrew's word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_115xZ_OPAL_DATA_HARVEST_TOOLSET_FOR_ASSET_MANAGERS.md`.
- **Starting map:** list v4, `org/tier1_exec/1.0.0_SA_CTO/deliverables/SERVABLE_PREFIXES_OPAL_DATA_HARVEST_20261013.md` @7e0da2dfee.
- **Bounds kept:** every read was a read; no vendor was called; the S3, DynamoDB and Lambda reads used the Opal admin IAM user.

## 0. Answer in five lines

1. The bucket holds **78 datasets, 58,639 objects** (listed 2026-10-14 ~12:05Z, 59 pages, 58,639 of 58,639 keys grouped) over **251 security keys**.
   95 to 102 names carry the full research stack. The rest carry chatter and peers only.
2. One company search can reach every layer, but only through the **identity crosswalk** and the **gold mention index**.
   - Silver articles carry no security column.
   - Keys come in six conventions.
   - CUSIP is held **nowhere** (0 columns).
   - ISIN is held for 65 names, and FIGI for 1.
3. **The published (platinum) layer already exists as a live API:** `opal-amgt-scoped-api`, 16 routes.
   - The platinum tool should CALL it, not recompose it. A second reader of the same analysis is a shadow path.
   - The gold and silver tools read S3 through the existing `harvest_read` admission.
4. Proposed: **11 tools**, named `harvest_<verb>_<noun>`.
   - Search: resolve and coverage.
   - Platinum: one tool.
   - Gold: chatter, fundamentals, research, filings, peers.
   - Silver: article search and read.
   - Cross-security: describe a dataset, query its columns.
   - Section 4 gives each tool's input, output and layer.
5. **Seven data defects the tools must absorb, or the CTO must route** (section 5). Two change answers silently:
   - The gold snapshot tables repeat their rows across part files (9x for mentions, 20x for chatter_daily); read the newest part only.
   - The gold layer is **3 trading days** behind T-1.

## 1. How this was read (the denominators)

| read | instrument | denominator |
|---|---|---|
| every key | `list_objects_v2`, paginated, page size 1,000 | 59 pages, 58,639 keys, 58,639 grouped into 78 datasets |
| every Parquet footer (schema, row count) | `pyarrow.parquet.ParquetFile(...).metadata`, 32 threads | 4,635 of 4,635 parts, 0 errors, 18 tables |
| JSON field trees | the newest object per JSON dataset (ASML_NA_Equity where present), names and types only | 43 datasets, 1 object each (a sample of 1, not a census) |
| gold and silver values | full read of projected key columns (no text column) of the 5 chatter/mention tables, the 5 silver article tables, silver research-report and SEC filing_source | every part of each table |
| published layer | `lambda invoke opal-amgt-scoped-api`, synthetic GET events with `x-firm-id: opal`, bypassing the edge JWT under admin IAM | 11 calls, 11 answered (10 x 200, the ISIN probe 200/none) |
| DynamoDB | `describe-table` x2; one full `scan` of `opal-harvest-security-metrics` | 6,845 of 6,845 items |
| trading calendar | `lib/trading_calendar.py` (`NYSE/hardcoded-fallback-2010-2027`) | T-1 = 2026-10-13 |

Scratch work stayed in the session scratchpad and is not committed: the key census JSONL, the API response bodies and the scripts.
No article text, report text or vendor HTML was printed or copied here. The worked example quotes derived values and field names only.

## 2. The three layers, measured

### 2.1 Platinum / published: what the portal shows (the live API)

`opal-amgt-scoped-api` (python3.11, last modified 2026-10-14T05:10Z) serves `/api/scoped/amgt/*`.

- **Source:** `lib/research/api/scoped_amgt.py:7523`, `handler()`. Its docstring names the route table as the denominator: 16 routes.
- **Stores:** S3 `opal-data-harvest`, plus two DynamoDB tables from the Lambda environment.

| route (per security unless noted) | what it returns (measured on ASML, 2026-10-14 ~12:2xZ) | size |
|---|---|---|
| `GET /resolve?q=` | `exact` / `candidates` / `none` from crosswalk + names | 0.2-0.5 KB |
| `/security/{k}/overlay` | identity, header figures (Bloomberg, vintage), posture, price movement + rank, chatter standing, peers, top band, provenance | 127 KB |
| `/security/{k}/thesis` | 10 fiscal years, 799 fiscal-year figures, model cases, dossier fields/sections, drafted sections | **1,244 KB** |
| `/security/{k}/peers` | the peer set (12 members) with factors and the rung rule | 60 KB |
| `/security/{k}/coverage`, `/ledger`, `/versions`, `/compare?from&to` | research coverage items; input ledger by class; model-block versions (22); version diff | 1-6 KB |
| `/security/{k}/timeline`, `/timeline/day/{date}` | daily chatter series (281 points from 2026-01-01), events (10), price series (197) | 155 KB |
| `/lead-panel/rankings/{trending,breakout}/{price,chatter}`, `/lead-panel/timeseries/...` | cross-security rankings (DynamoDB) | -- |
| `/freshness`, `/lists`, `/watchlist` | coverage freshness (302 rows), list register, firm watchlist | 1,266 KB |

| DynamoDB table | keys | items | read |
|---|---|---|---|
| `opal-harvest-security-metrics` | `axis_date` (`<AXIS>#<date>[#<generation>]`) + `ticker`; GSI `axis-rank-index` | 6,845 | ranking generations; price axes carry 94 names per generation |
| `opal-harvest-articles` | `security_key` + `published_at`; GSIs on platform, ticker | **0** (0 B) | wired in the Lambda env, empty |

### 2.2 Gold: per-security derived data and the chatter tables

Keys: `security_key` = `<ROOT>_<CC>_Equity` everywhere in gold. The freshness frontier is in trading days behind T-1 (2026-10-13).

| dataset (prefix under `s3://opal-data-harvest/`) | form | securities | rows / objects | newest | columns worth exposing |
|---|---|---|---|---|---|
| `amgt/harvest/gold/chatter_daily/` | Parquet, snapshot per part | 242 | **68,002 in the newest part** (1,338,296 across all 26 parts) | partition 2026-10-08, written 10-09 10:34Z: **3 behind** | day, articles_total, tier_a..tier_d, mention_score, trailing_7d/30d_sum, baseline_30d_sum, cumulative_ytd, publishers_distinct, **data_status**, publishers_found_codes |
| `amgt/harvest/gold/article_security_mention/` | Parquet, snapshot per part | 234 | **52,424 newest part** (459,334 all parts; 20,868 articles) | 2026-10-08: 3 behind | article_key, publisher, security_key, mention_count, mention_in_title/lead, signal_tier, signal_weight, is_roundup, co_mentioned_securities, published_utc, bronze_key |
| `amgt/harvest/gold/chatter_window/` | Parquet, snapshot per part (3 copies) | 233 | 1,953 (651 per copy) | 2026-10-04 (window_end 10-02): 7 behind | window_days (30/90/365), articles_total, scored, voters, **tone** |
| `amgt/harvest/gold/chatter_event/` | Parquet | 69 | 576 rows, 528 events | 2026-10-03: 6 behind | first_day, last_day, days_span, articles_total, tier_a/b, publishers_distinct, lead_article_key, lead_headline, article_keys |
| `amgt/harvest/gold/article_sentiment/` | Parquet, append batches | -- (article grain) | 13,235 articles | 2026-10-03: 6 behind | label (pos/neg/neu), score, confidence, scorer |
| `amgt/harvest/gold/candidate_universe/` | JSON, 2 objects | 2,856 rows (scanner) | 1 per date | 2026-10-02 | ticker, name, country, sector, industryGroup, mktVal, ev, ey, price, 26 preset values, universe weights (284 value codes) |
| `derived/model_block/` | JSON per key per stamp | 102 | 2,038 | 2026-10-12 13:12Z | figures[] (scope, fiscal_year, mnemonic, value, unit, sign, vintage, source; ASML 870 figures, 117 mnemonics), cases (base/upside/downside), currencies |
| `peers/v1/` | JSON per key per stamp | 245 | 1,727 | 2026-10-11 | members[] (name, ticker, country, sector, cap, ev, ey, 26 factors, rung), rungs, denominators |
| `scores/v1/` | JSON | 35 | 70 | 2026-09-30 (ASML's 2026-09-17: 18 behind) | divergence, peers_v, robustness (each status + reason) |
| `posture/v1/` | JSON | 35 | 35 | 2026-10-02 | verdict, comparable, reason, membership (books, weight_by_book) |
| `management/v1/` | JSON | 17 | 25 | 2026-10-02 | officers[] (name, role, tenure, source), roster_status, ceo_profile |
| `filings/v1/` | JSON (`.source` + `.analysis`) | 195 keys, **13 with a resolved filing** (175 `UNRESOLVED-SOURCE`) | 208 | 2026-10-11 | items{guidance, segments, risks, commentary, big_bets, big_challenges}, citations, passage_map |
| `drafting/v1/` | JSON | 12 | 12 | 2026-10-11 | sections[], evidence_records[], thesis_driver, denominators |
| `amgt/harvest/gold/research_dossier/` | JSON per key per as_of | 95 | 1,431 | 2026-10-12 | 24 fields, each {value, citation} or {absent}: thesis_summary, why_we_own, positives, negatives, risks, cases, kpi_set, model_rows, management, ownership, recommendation, team_sheet |
| `amgt/harvest/gold/research-dossier/` (hyphen) | JSON, older generation | 95 | 846 | 2026-09-29 | the same field set without `team_sheet`/`pack_shape`; **superseded by `research_dossier`** (inferred from the field superset and dates) |
| `amgt/harvest/gold/research-continuation/` | JSON | 95 | 320 | 2026-09-29 | thesis_summary, thesis_pillars, kpi_set, last_stated_position |
| `amgt/harvest/gold/ai_fill/` | JSON, 1 per key | 95 | 95 | 2026-10-14 03:19Z | blocks{identity_description, mgmt_bio, mgmt_recent, mgmt_team_view, thesis_pillars}: text, citations, machine_written, reason |
| `amgt/harvest/gold/research-{backlog,fund-form,model-typecast,sector-template}/` | JSON, not per security | -- | 21 / 9 / 4 / 29 | 2026-09-26 or older | fund skeletons, sector templates, typecast (estate-level, not a company answer) |
| `packs/` | JSON | 105 | 106 | 2026-10-12 | input_ledger entries (class, source, outcome, stamp) |
| `crosswalk/v1/`, `identity/v1/`, `universe/v1/` | JSON, one per date | 243 / 37 / 302 | 8 / 1 / 3 | 10-09 / 09-17 / 10-06 | security_key, bloomberg, display_ticker, association_keys, exchange, legal_name, **issuer.cik** (204 of 243), books |

### 2.3 Silver (and the Bloomberg bronze, which is the per-security column store)

The silver articles carry **no `security_key`**. `discovered_for` holds the QUERY ticker that found the article, not its subject:
- every sampled value (2 per publisher) is `BA`;
- ASML matches 0 rows through `discovered_for` and 818 rows through the gold mention join.

The gold mention table is the only company-to-article index.

| dataset | form | rows | articles | newest published (behind T-1) | columns worth exposing (text held, served only on request) |
|---|---|---|---|---|---|
| `bloomberg/harvest/silver/article/` | Parquet, 745 parts, **717 schema variants** | 4,255 | 3,008 | 2026-10-13 00:28Z: **0** | article_key, title, url, published_utc, words, content_status (+ text, body_blocks) |
| `seeking-alpha/harvest/silver/article/` | Parquet, 1,365 parts, 55 variants | 19,477 | 19,472 | 2026-10-11 19:44Z: 1 | title, publishOn, isPaywalled, themes, primaryTickers, commentCount (+ content) |
| `wsj/harvest/silver/article/` | Parquet, 416 parts, 313 variants | 1,044 | 615 | 2026-10-05: 6 | as bloomberg |
| `barrons/harvest/silver/article/` | Parquet, 64 parts | 501 | 203 | 2026-10-06: 5 | as bloomberg |
| `ft/harvest/silver/article/` | Parquet, 95 parts | 355 | 185 | 2026-09-29: 10 | headline, datePublished, description, wordCount (+ articleBody) |
| `*/harvest/silver/listing_hit/` (5 publishers) | Parquet | 217,931 total (SA 214,615) | -- | 10-12 or older | search hits: headline, url, rank, query (discovery plumbing) |
| `amgt/harvest/silver/research-report/` | Parquet | 355 | 94 securities | 2026-09-25 | report_id, file_ext, report_class, period, fund, author, sector_as_written (each with evidence / absent_reason) |
| `sec/harvest/silver/filing_source/` | Parquet | 22 | 13 securities | 2026-10-09 | accession, form, filing_date, entity_name, url, status |
| `bloomberg/harvest/bronze/{bestdata,refdata,histdata}/` | JSON per key per pull | 1,125 / 1,167 / 1,167 | 99 / 100 / 100 securities | 2026-10-12 13:12Z: 1 | BEST_* consensus x FY1-3 (17 fields); refdata 24 fields (CUR_MKT_CAP, EQY_BETA, GICS_SECTOR_NAME, NET_DEBT, EXPECTED_REPORT_DT, ...); histdata 14 annual rows x 29 valuation fields |
| `bloomberg/harvest/bronze/{segments,exec_officers,identity}/` | JSON | 88 / 93 / 68 | 85 / 91 / 68 | 10-07 | PG_REVENUE segments; COMPANY_EXEC_OFFICERS; **ID_ISIN, ID_SEDOL1, COMPOSITE_ID_BB_GLOBAL, CIK, LEI** (65 of 68 filled) |
| `bloomberg/harvest/bronze/price_history_{px_last,tot_return}/` | JSON per date, 94 series | 9 / 1 | -- | 2026-10-14 11:07Z | daily PX_LAST 30d / year; TOT_RETURN 5d |

Withheld from tools as plumbing, still SERVE through `harvest_read`:
- the bronze article HTML and news listings (5.58 GB);
- `run_record`, `pull_log`, `filing_attempt` and `job_record`;
- `lib/` and `social/_measurement`.

## 3. Keys: how a security is identified

| identifier | where it is held | coverage | usable for search |
|---|---|---|---|
| `security_key` `<ROOT>_<CC>_Equity` | every per-security gold and bronze path | 251 distinct | **yes, the join key** |
| Bloomberg `<ROOT> <CC>` / display ticker | crosswalk/v1, refdata | 243 records | yes (resolver takes it today) |
| company / folder / legal name | crosswalk `source_row.folder`, `legal_name`; refdata `LONG_COMP_NAME`; universe `name` | crosswalk names all; legal_name partial | yes, with the defect in 5.D5 |
| CIK | crosswalk `issuer.cik` (claim measured); universe `cik`; bronze identity | 204 of 243 | yes (also groups listings of one issuer) |
| ISIN, SEDOL, LEI | `bloomberg/harvest/bronze/identity/` only | **65 securities** (ASML is not one of them) | partial |
| composite FIGI | gold mention / chatter_daily / chatter_event `composite_figi` | **1 security** filled | no |
| **CUSIP** | **nowhere**: 0 of 18 Parquet tables, 0 of 43 sampled JSON trees | 0 | **no** |
| other conventions | `publication-links/v1/<ROOT>/` (3 keys), `raw/seekingalpha/<ROOT>_<CC>/` (3), `security-<hash16>` association keys, `BP-SLASH-` for a `/` in a key | -- | the resolver maps them; a tool never exposes them |

To answer CUSIP and ISIN for every covered name, the producer has to pull `ID_CUSIP`/`ID_ISIN` for all ~251 keys into `bloomberg/harvest/bronze/identity/`.
- That pull is a Bloomberg queue pull, and so a producer item for AMGT_HARVST that the CTO routes.
- A search must not do it (bound: no vendor call).

## 4. The proposed tools

Common rules:
- Every tool admits through `harvest_read.admit()`, which checks principal, Opal user and served prefix, and writes one audit row per call.
- Every tool answers with `{as_of, source_keys[], denominators, absent_reason}` beside the values.
- Every tool caps its response at **50 KB by default**, with `sections`/`columns`/`limit` to widen it.
- `security` accepts any identifier in section 3 and resolves ONCE. Every other tool takes the resolved `security_key`.

| # | tool | input | output (columns) | reads (layer) |
|---|---|---|---|---|
| 1 | `harvest_resolve_security` | `query` (ticker, Bloomberg ticker, key, name, legal name, CIK, ISIN, SEDOL) | status exact/candidates/none; security_key; display_ticker; bloomberg; name; cik; isin (where held); other_listings[]; aliases per convention; `not_held: [cusip, ...]` | crosswalk/v1, universe/v1, bronze identity; wraps `lib/research/api/name_search.resolve_query` (search) |
| 2 | `harvest_security_coverage` | `security_key` | per dataset: present, objects, newest stamp, trading days behind T-1; layer totals | one `ListObjectsV2` per keyed prefix (~30 calls, `security_key=<k>/` or `<k>/`), plus the newest gold partition (search) |
| 3 | `harvest_get_published_analysis` | `security_key`, `sections` (overlay, thesis, peers, ledger, versions, timeline; default overlay summary) | the published body for each section, PROJECTED: header figures, posture verdict, price movement/rank, chatter standing + reason, peer names, model base/upside/downside with formula, dossier and drafted section titles, version list | **invokes `opal-amgt-scoped-api`** with `x-firm-id` for the Opal principal (platinum) |
| 4 | `harvest_get_chatter` | `security_key`, `from_day`, `to_day` | daily rows (day, articles_total, tier_a..d, mention_score, trailing_7d/30d_sum, **data_status**, publishers_found); windows 30/90/365 (articles, scored, voters, tone); events (first/last day, articles, tier_a, publishers, lead_article_key) | gold chatter_daily / chatter_window / chatter_event, **newest part only** |
| 5 | `harvest_search_articles` | `security_key`, `publisher?`, `from?`, `to?`, `min_tier?`, `in_title?`, `limit` (default 25, max 100) | article_key, publisher, published_utc, signal_tier, mention_in_title, co_mentioned_securities, sentiment label/score; title, url, words joined from silver | gold mention (newest part) + article_sentiment, joined to `<pub>/harvest/silver/article/` on article_key (gold to silver) |
| 6 | `harvest_get_article` | `article_key`, `publisher`, `include_text` (default false) | title, url, published_utc, words, content_status, the security keys it mentions; text/body_blocks only on `include_text` | silver article (newest record per article_key), located by the mention row's `published_utc` date partition (silver) |
| 7 | `harvest_get_fundamentals` | `security_key`, `mnemonics?`, `fiscal_years?`, `kind` (model, consensus, reference, valuation_history, segments, price) | model figures (mnemonic, fiscal_year, value, unit, vintage, source); consensus BEST_* x FY1-3; refdata fields; histdata rows; segments; price series; model_block versions | derived/model_block (+_fye), bloomberg bronze bestdata/refdata/histdata/segments/price_history (gold + bronze) |
| 8 | `harvest_get_research` | `security_key`, `as_of?`, `fields?` | dossier fields (value + citation, or absent reason); continuation thesis/pillars; ai_fill blocks (text, citations, reason); research-report list (class, period, fund, author); management roster | research_dossier (newest as_of), research-continuation, ai_fill, silver research-report, management/v1, bronze exec_officers (gold + silver) |
| 9 | `harvest_get_filing_analysis` | `security_key`, `accession?`, `include_passages` (default false) | form, filing_date, items by category with citations, denominators (items, cited %), thesis driver; drafted sections; passages on request | filings/v1 `.analysis`, drafting/v1, sec silver filing_source (gold + silver) |
| 10 | `harvest_get_peers_and_scores` | `security_key` | peer members (name, ticker, country, sector, cap, factors, rung), rung rule; scores (divergence, peers_v, robustness with status/reason); posture (verdict, books) | peers/v1, scores/v1, posture/v1 (gold) |
| 11a | `harvest_describe_dataset` | `dataset` (or none = the list) | columns + types, grain, key, freshness rule, row count, newest stamp, never-sum rules | a generated schema registry: this assessment's footer read, regenerated (metadata) |
| 11b | `harvest_query_columns` | `dataset` (tabular only: chatter_daily, chatter_window, mention, sentiment, candidate_universe rows, model_block figures), `columns[]`, `security_keys[]?`, `filters` (=, <, >, in), `order_by`, `limit` (max 200) | the projected rows, with the denominator scanned | the newest part / object of that dataset (gold + silver columns, cross-security) |

Tool 11 is Andrew's "individual columns/features" vector, for example:
- the top 20 names by `trailing_30d_sum` on the newest day;
- every covered name's `BEST_PE_RATIO` FY1;
- every candidate-universe name in a sector with `ey` above a value.

It runs only over a declared column list, so it is a read of stored columns and never a free query engine.

**Build notes for the CTO (inferred, not measured):**
- Whether the EC2 gateway image can import `lib/research` was not read.
- Tool 3 avoids the question by invoking the Lambda. Tools 1 and 4-11 need either that import or a small reader in `app/harvest_read.py`'s module family, reusing `harvest_read.admit()`.

## 5. Defects the tools must absorb (measured), with the owner who could fix each at the source

| id | finding | consequence for a tool | owner to route (CTO's call) |
|---|---|---|---|
| D1 | Each part in a chatter_daily / mention / chatter_window partition is a FULL SNAPSHOT: the newest chatter_daily part holds 68,002 rows with 0 duplicate (security, day) pairs, while the table across parts holds 1,338,296; mention: 52,424 vs 459,334 (406,584 repeated pairs) | reading the prefix, as `harvest_list`+`harvest_read` or a naive dataset scan does, multiplies counts about 9x (mention) and 20x (chatter_daily) | tools read the newest part only; AMGT_HARVST may compact or mark the snapshot |
| D2 | silver articles carry no `security_key`; `discovered_for` is the query ticker | an article search must join through gold mention; silver alone cannot answer "articles about X" | tool rule; no fix needed |
| D3 | gold mention and chatter's newest partition is 2026-10-08 (3 trading days behind T-1); chatter_window 7, chatter_event and sentiment 6; silver bloomberg articles are at 0 | a company's chatter reads up to a week old while its silver articles are current | the tool states the lag in trading days; the producer cadence is AMGT_HARVST's |
| D4 | CUSIP held nowhere; ISIN/SEDOL for 65 names; FIGI for 1 | "search by CUSIP" answers `not_held`, never `none` | an identity enrichment pull through the Bloomberg queue (AMGT_HARVST) |
| D5 | the live resolver answers `ASML Holding` with ONLY `ASML_US_Equity` (an uncovered listing), while `ASML` answers `exact ASML_NA_Equity`; the covered record's name is its folder "ASML NA" and its `legal_name` is ABSENT | a name search lands on the wrong listing with no warning | add refdata `LONG_COMP_NAME` / identity `NAME` as stored names (AMGT_RESAPP `name_search`) |
| D6 | published bodies run to 1,244 KB (thesis) and 1,266 KB (freshness); candidate_universe is 3.76 MB | an unprojected tool answer overflows a Claude Desktop turn | the 50 KB default projection (section 4) |
| D7 | 717 schema variants over 745 bloomberg silver parts, 313 over 416 wsj; null-typed columns in some parts (`published_utc` failed a plain max) | a dataset-wide read fails or mis-types | declared column projection with coercion |
| D8 | `opal-harvest-articles` (DynamoDB) has 0 items, though the Lambda env names it | none for these tools (they read S3); a reader of that table would answer empty | AMGT_RESAPP to confirm whether it is retired |
| D9 | chatter rankings: every `TRENDING_CHATTER#<date>` from 10-07 to 10-14 holds only its pointer row, while price generations hold 94 names; the published overlay says "the ranking produced on 2026-10-14 had no names in it"; chatter_daily's last day reads `DENIED` for 174 of 242 names and `PARTIAL` for 68 | `harvest_get_chatter` must surface `data_status` and never present 0 articles as "no chatter"; the chatter standing comes from gold, not the ranking | already on record in AMGT_RESAPP's surprise channel (`INVESTIGATION_v1.md`, lines 16119 and 18506); not re-filed |

## 6. Worked example: ASML Holding NV, end to end

Read 2026-10-14 between 12:15Z and 12:40Z.

**Search.**
- `resolve?q=ASML` returns `exact` `ASML_NA_Equity`, "the listing we cover; also listed as ASML_US_Equity (the same issuer)". CIK 937966 is measured from the 20-F's EDGAR path.
- `resolve?q=ASML Holding` returns `candidates [ASML_US_Equity]` (D5).
- `resolve?q=NL0010273215` returns `none`. ASML's ISIN is not held (D4).
- Coverage: the key appears in **23 datasets** (the most-covered names are BABA 26, BA 25, COST 24, ASML 23).

**Platinum (the live API).**

| section | value |
|---|---|
| identity | MEASURED, crosswalk 2026-10-09, display "ASML NA", name "ASML Holding NV" |
| header | Bloomberg figures, vintage 2026-10-12T13:02:06Z; currency EUR; domicile NL |
| price | TRENDING, rank 12, 30-day window return score 8.78, PX_LAST 1,509.6 on 2026-10-13 (generation 20261014T110715Z) |
| chatter standing | none: "the ranking produced on 2026-10-14 had no names in it" (D9) |
| posture | verdict `absent` (as of 2026-09-16; no held comparable in R-1) |
| peers | 12 members: Intel, Tencent, Cisco, Lam Research, Applied Materials, Oracle, SK hynix, AMD, Dell, Palo Alto, Micron, Samsung |
| model (thesis) | SERVED; FY2016-FY2025; 799 fiscal-year figures; BASE 1,355.23 = BEST_EPS FY1 2026 38.213 x trailing-median P/E 35.47; upside and downside ABSENT |
| dossier / drafting | 5 dossier sections; drafting SERVED, 5 sections |
| versions | 22 model-block versions, latest 20261012T130207Z |
| timeline | 281 daily points from 2026-01-01, 10 events, 197 price points |

**Gold.**

| dataset | value |
|---|---|
| chatter_daily (newest part) | 281 days, 236 articles in total, last day 2026-10-08, status PARTIAL on 279 days and DENIED on 2 |
| chatter_window | 30d: 20 articles, tone +0.054; 90d: 72, +0.140; 365d: 225, +0.092 (window_end 2026-10-02) |
| chatter_event | 13 events, the latest 2026-07-14..07-17 (21 articles, 18 tier A, 4 publishers) |
| article_security_mention | 584 articles (SA 341, FT 170, Bloomberg 60, WSJ 10, Barron's 3); 258 name it in the title; tier A 246; newest 2026-10-05 |
| article_sentiment | 491 of the 584 scored: 175 positive, 174 negative, 142 neutral |
| derived/model_block | 870 figures over 117 mnemonics and 10 fiscal years; base case SERVED |
| scores/v1 | divergence, peers_v and robustness all ABSENT (`ABSENT_SOURCE`), generated 2026-09-17 |
| research_dossier | as_of 2026-10-12; 24 fields, 13 with a value; absent: comparison_set, fund_form_ref, fund_of_record, last_stated_position |
| ai_fill | as_of 2026-10-14; mgmt_bio (1 citation) and mgmt_recent (3) written; identity_description, mgmt_team_view, thesis_pillars empty with a reason |
| filings/v1 | 20-F of 2026-02-25 (accession 000162828026011378): 86 items (guidance 12, segments 12, risks 22, commentary 18, big bets 10, big challenges 12), 100% cited, 90 citations over 549 passages |
| management/v1 | 7 officers, roster from the Bloomberg fallback (filing source unresolved) |
| packs | 13 ledger entries, all market_data OK |

**Silver and bronze.**
- **Articles joined through the mention index:** Bloomberg 109 rows, FT 339, SA 341, WSJ 20, Barron's 9. These are rows, not distinct articles; silver repeats rows.
- **Research reports:** 3, which are two PDFs for PFOE (class A, period 2026-05-05; class B, 2026-Q2) and one xlsx (class OTHER, 2025-07-17).
- **SEC filing source:** 1 (20-F, RESOLVED, "ASML HOLDING NV").
- **Bloomberg bronze:**
  - bestdata: 17 BEST fields x FY1-FY3;
  - refdata: 24 fields, including 189 earnings-announcement dates;
  - histdata: 14 annual rows x 29 valuation fields;
  - segments: 12 revenue rows;
  - exec_officers: 7.
  - The newest pull was 2026-10-12 13:01Z.

## 7. What could not be read, and why

- **Most of each JSON prefix:** 1 object per dataset was opened for field names (a sample of 1). Per-security counts come from key paths, and values from ASML's own objects only.
- **The text columns:** no article, report or filing text was read or reproduced. Their presence comes from the schema.
- **The published API through the edge:** the calls went to the Lambda directly, with a synthetic `x-firm-id: opal`. The JWT edge, and how the gateway would present an Opal principal's firm, were not exercised.
- **Five routes:** `/compare`, `/print`, `/lead-panel/*`, `/lists` and `/watchlist` were not called.
- **The gateway image:** whether it can import `lib/research` (section 4 build notes).
- **Producers:** the writing code of the duplicated snapshot parts (D1) and the cause of the chatter `DENIED` status (D9) were not traced.
- **Licences:** none was read, and none binds under Andrew's ~19:0xZ and ~20:0xZ words for Opal users.
- **Prefixes outside list v4's dataset rows:** `amgt/harvest/gold/ai_fill/`, `amgt/harvest/bronze/research_template/` and `run_record/` are inside the served `amgt/` prefix but have **no catalog row** in `DATA_CATALOG.yaml harvest_datasets` (39 rows). They are new since the 10-13 listing.

-- 4.0.0_SA_CRO~Z
