# B -- Seeking Alpha REST + PEERS: field-level channel map

Scope: `integrations/seekingalpha/`, the SA endpoints it calls, the `seeking-alpha/harvest/{bronze,silver}` stores,
the SA forecast fallback (Model), and the PEERS component end to end (C-PEER-SET-SA, `lib/research/peers/`,
`peers/v1/`, `amgt/harvest/gold/candidate_universe`, the Peers tab). Read-only. Measured 2026-09-22 on SITEZ.
No SA or other vendor call was made. Cookie, proxy and secret VALUES were not read. Author names, bios, profile
URLs and user ids in the SA payloads are PERSONAL and are shown here as field names only.

Starting points I relied on and verified, not re-derived:
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESAPP_DATA_SHAPE_INVENTORY_20260918.md` s.2 rows 11 and 17, s.11a/11b
  (the two `peers/v1` shapes) and s.17a/17b (the SA JSON:API envelope). Its vintage is 09-18: the SA objects were
  still under `raw/seekingalpha/` then.
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` s.5.4 (the SA proposed
  grammar), and rows `candidate universe` and `peers` at `:395`, `:401`.
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BRIEF_PEERS_CURRENT_TO_DESIRED_20260918.md` s.2 (the SA peers page,
  measured through `rest_fetch.py` with 15 GETs and nothing landed).

What is new in this file: the field dictionaries at every stored layer, the SA peers-page calls mapped against the
code (none is built), the per-component trace, and five hazards nobody had recorded (H1-H5 below).

---

## CHANNEL 1 -- Seeking Alpha REST (symbol / report / analysis / news / article)

### 1.1 Channel
- **Vendor and mechanism:** Seeking Alpha's private JSON:API (`https://seekingalpha.com/api/v3/...`, from
  `integrations/seekingalpha/config.json:3`). The calls are GETs only. The client is `curl_cffi` with Chrome TLS
  impersonation, egressing through the Bright Data **residential** proxy (`rest_fetch.py:105-150`).
- **Session / cookie mechanism (described, no value quoted):**
  - The cookie jar is harvested somewhere else, by a browser-based harvester (`sa_harvest_session.py`, which this
    module never runs; `rest_fetch.py:10-12`). It is parked in Secrets Manager under the name that `config.json:7`
    `secrets.session_secret_name` gives. `build_session` reads the bundle's `all_cookies` list and `user_agent`
    (`rest_fetch.py:109-110`, `:148-149`).
  - It refuses the bundle unless it carries the identity cookie named at `config.json:11` (`rest_fetch.py:111-116`).
  - The jar must also carry the short-TTL PerimeterX cookies (`:10-11`).
  - The proxy credentials come from a second secret (`config.json:8`). The proxy username gets a random
    `-session-saNNNNNN` suffix on each build, so there is one sticky exit IP per run (`:117-124`).
  - `verify=False`, because the proxy re-signs TLS; this rests on Andrew's per-use word (`:125-137`).
  - Every request carries a per-ticker `Referer` (`:170-174`). Without it, SA answers 200 with a near-empty body
    (`:13-14`).
  - `detectors.classify` (`detectors.py:39-48`) returns OK / FAILURE (empty body) / REHARVEST (a small 403 carrying
    the challenge marker, meaning the PX cookies aged out) / AUTH_FAIL.
  - On REHARVEST the run STOPS. It never signs in, never retries and never launches a browser (`rest_fetch.py:16-19`,
    `:333-334`).
  - `credentials_secret_name` is named in the config but never read (`config.json:9`, `:15`).
- **Entry point:** `python integrations/seekingalpha/rest_fetch.py run-ticker <SA_TICKER> --security-key <KEY>
  --state-dir <dir>` (`rest_fetch.py:32-34`, `main` `:468-557`), one ticker per invocation. `finalize` rolls the state
  up (`:536-553`). Pacing is `pace_seconds` 2.0, and `articles_per_ticker` is 2 (`config.json:12-13`). Each call is
  logged to `<state-dir>/request_log.json`, and `sa_ids.json` maps ticker -> {sa_id, slug, status}. Both files are
  LOCAL (`:266-298`). A ledger row goes through `lib/research/ledger/ledger.py record_run(key,"sa","seekingalpha",...)`
  (`:515-522`).
- **Sequence** (`run_ticker`, `rest_fetch.py:303-465`):
  1. `GET /api/v3/symbols/{TICKER}` returns sa_id and slug (`:327-351`).
  2. `GET /api/v3/virtual_analysts/{sa_id}` returns the report (`:357-378`). It needs the sa_id. The Referer is the
     virtual-analyst page, which is never itself fetched.
  3. `GET /api/v3/symbols/{ticker}/analysis?...&page[size]=2&include=author,primaryTickers,sentiments`
     (`:383-400`).
  4. `GET /api/v3/symbols/{ticker}/news?...` with the same shape (`:405-427`).
  5. `GET /api/v3/articles/{id}?include=author` for up to 2 of the listed ids (`:430-452`). This call is skipped when
     `harvest_grammar.article_known("sa", id)` is already true (C-DEDUPE-BY-KEY).
- **Endpoints NOT called by any production code** (native Grep for `suggested|peers_similarities|related-stocks|
  peers/comparison` over `*.py`: 0 production hits):
  - `/symbols/{slug}/suggested` (the peers)
  - `/tickers?filter[slugs]=...&include[gics]=true`
  - `/ticker_metric_grades` (quant factor grades)
  - `/searches` (used only by the CRO's seat script `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py:55`,
    which is not production)

  `/metrics` is called ONLY by the forecast fallback (Channel 2).
- **Trigger / cadence today:** manual, one hand run. Every object that exists was fetched on 2026-09-11 between
  04:02 and 04:03Z, for 3 tickers (BABA, BA, COST). Nothing is scheduled. The PRD records Andrew's terms clearance
  (v0.13) and the production lift for exactly two paths, C-PEER-SET-SA and the SA_FALLBACK cells of
  C-MODEL-FORECASTS (`AMGT_RESAPP_PRD.md:1262-1263`). `BACKFILL_SCOPE_PROPOSAL_20260922.md:55` holds the backfill
  (B3): "0 of 96 records carry an SA symbol, and the session needs re-harvest".

### 1.2 Storage (live counts via `bash .tools/aws s3 ls --recursive`, 2026-09-22)
| layer | key pattern | live objects |
|---|---|---|
| bronze (form a) | `seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/security_key=<slash-safe key>/<YYYYMMDDTHHMMSSZ>.json`. The partition comes from `store.entity_partition` -> `crosswalk.security_key_partition` (`lib/research/harvest/store.py:82-92`); the object name comes from `form_a_object` (`:113-115`) | symbol 3, report 3, analysis 3, news 3 |
| bronze (article) | `seeking-alpha/harvest/bronze/article/article_hash=<sha256("sa:"+article_id)>/<stamp>.json` (`lib/opal_data_harvest/harvest_grammar.py:48-58,70-81`) | 6 |
| bronze (metrics) | `seeking-alpha/harvest/bronze/metrics/security_key=<k>/<stamp>.json`. Only the fallback writes it | **0** |
| **total bronze** | | **18** (BABA_US_Equity, BA_US_Equity, COST_US_Equity) |
| silver | `seeking-alpha/harvest/silver/{symbol_profile,news_item}/date=<fetch date>/part-<run_stamp>.parquet` (`store.py:348-401`, `date_partition` `:95-101`) | **0** (whole silver prefix is empty) |
| legacy | `raw/seekingalpha/<ROOT>_<CC>/<stamp>/{symbol,report,analysis,news,article_<id>}.json` | **18, still present**. These are the same bytes: the bronze LastModified reads 2026-09-22 00:54 (M3 copy) while the stamps read 09-11. `land_raw` is retired (`rest_fetch.py:218-225`), and nothing reads raw/ now |
| served JSON / DynamoDB | none. No served SA folder exists. | -- |

### 1.3 Field dictionaries

**A. bronze `symbol`** (sample `.../symbol/security_key=BA_US_Equity/20260911T040253Z.json`, 17,945 B; BABA
21,084 B). This is SA's unaltered JSON:API envelope: 231 leaf paths, of which 57 are `meta.routesData` entries.
| path | type | null? | shape | meaning |
|---|---|---|---|---|
| `data.id` | str | no | `"769"` | **sa_id** (numeric string). The same id is the ticker's `tag` id in `primaryTickers` on news and analysis |
| `data.type` | str | no | `"ticker"` | |
| `data.attributes.slug` | str | no | `"ba"` | **SA slug, lower-case** (the peers URL key) |
| `data.attributes.name` | str | no | `"BA"` | **the TICKER, not the company** (see H1) |
| `data.attributes.companyName` / `.company` | str | no | `"The Boeing Company"` | company name (the entity-test input) |
| `data.attributes.equityType` / `fundType` / `tickerType` | str | no | `"stocks"` / `"Stock"` / `"primary"` | |
| `data.attributes.exchange` / `exchangeTitle` / `tradingViewSlug` | str | no | `"NYSE"` / `"NYSE:BA"` | listing venue. BABA reads NYSE (the ADR) |
| `data.attributes.currency` / `companyPrimaryCurrency` | str | no | `"USD"` | |
| `data.attributes.sectorDisplay` / `industryDisplay` | str | no | `"Industrials"` / `"Aerospace and Defense"` | SA (GICS-style) sector and industry |
| `data.relationships.sector.data.id` / `subIndustry.data.id` | str | no | `"20"` / `"20101010"` | GICS sector and sub-industry codes |
| `data.relationships.companyInfo.data.id` | str | no | `"370857"` | |
| `data.attributes.{isBdc,isReit,isEtn,visible,searchable,private,pending,isDefunct}` | bool/null | isEtn null | | flags |
| `data.attributes.{followersCount,articleRtaCount,newsRtaCount,fundTypeId}` | int | no | `379748` | |
| `data.attributes.{mergedTickers,mergedInto}` | list[str] | may be [] | `["SPR"]` | M&A lineage |
| `data.attributes.{divYieldType,primaryEpsConsensusMeanType}` | str | no | `"historic"` / `"normalized"` | |
| `data.attributes.{indexGroup,exchangeDescription,mergedOn}` | null | yes | | |
| `data.meta.companyLogoUrl{Light,Dark}` | str (URL) | no | | |
| `included[]` (3) | obj | | `{id,type:"sector",attributes:{name,quant_tickers_count},meta.screener_links}` | sector / sub-industry objects |
| `meta.marketData.{open,openTime,refreshRate}` | bool/str/int | | | |
| `meta.chartTimes.*` (12) | str | | `"09/11/2026 16:00"` | |
| `meta.contentCounters.*` (22) | int | | `analysis 2391, news 5061, transcripts 128, sec_filings 80` | content depth. A cheap SA **density** signal |
| `meta.showRatings.*` (4), `meta.availableData.*` (20) | bool | | `virtual_analyst_report true, related_stocks true` | availability flags |
| `meta.routesData` (57) | dict | | keys include `/peers/comparison`, `/peers/related-stocks`, `/valuation/metrics`, `/earnings/estimates` | page routes. Shows a peers page exists; not used |

**B. bronze `report`** (`.../report/security_key=BA_US_Equity/20260911T040258Z.json`, 7,446 B; 11 leaves)
| path | type | shape | meaning |
|---|---|---|---|
| `data.id` / `data.attributes.id` | str / int | `"143141"` / `143141` | report id |
| `data.type` | str | `"virtualAnalyst"` | |
| `data.attributes.slug` | str | `"BA"` | **upper-case** here, unlike `symbol.slug` |
| `data.attributes.responseContent` | str (Markdown) | 5,212 chars; `###` sections: Company Description / Competitors and Unique Value / Positives raised by SA analysts / Concerns raised by SA analysts | the SA-generated ("virtual analyst") report |
| `data.attributes.ratingsResponse` | str (Markdown) | 1,865 chars; `### Seeking Alpha Quant Rating Explanation`, `#### Sector Metrics Comparative Analysis` | quant-rating narrative |
| `data.attributes.createdAt` / `updatedAt` / `previousReportDate` | str ISO-8601 with offset | `"2026-09-08T00:24:33.381-04:00"` | report vintage (regenerated about daily) |
| `data.attributes.sectionHighlight` | str | `"no_highlight"` | |
| `data.attributes.enoughAnalysis` | bool | `true` | SA's own coverage-sufficiency flag |

**C. bronze `analysis` and `news` listings** (BA analysis 7,359 B, 61 leaves; BA news 17,247 B). The page size is 2.
| path | type | shape | meaning |
|---|---|---|---|
| `data[]` | list[2] | | listed items |
| `data[].id` | str | `"4943496"` | **sa_article_id** (the key into `article` bronze) |
| `data[].type` | str | `"article"` (analysis) / `"news"` | |
| `data[].attributes.title` | str | | headline |
| `data[].attributes.publishOn` | str ISO-8601 -04:00 | `"2026-09-07T03:54:49-04:00"` | publish time, US-Eastern offset |
| `data[].attributes.{isLockedPro,isPaywalled}` | bool | | paywall flags |
| `data[].attributes.commentCount` | int | | |
| `data[].attributes.{gettyImageUrl,videoPreviewUrl,videoDuration,themes,structuredInsights}` | str/null/dict | | media and themes |
| `data[].attributes.content` | str HTML | **news only** | the full news-item body, inline |
| `data[].relationships.author.data.{id,type}` | str | `type` `author` / `newsAuthorUser` | author ref (PERSONAL, redacted) |
| `data[].relationships.sentiments.data[]` | list[{id,type}] | analysis 5 / news 0 | sentiment refs |
| `data[].relationships.primaryTickers.data[].id` | str | `"769"` | = the subject's sa_id |
| `data[].relationships.{secondaryTickers,otherTags}.data` | list | | |
| `data[].links.self` | str | `/article/<id>-<slug>` / `/news/<id>-<slug>` | |
| `included[]` | list | analysis: author 2, sentiment 8, tag 1; news: newsAuthorUser 2, tag 1 | `sentiment.attributes = {articleId, createdAt, type, typeId}`; `tag.attributes = {company, equityType, name, slug, tagKind}`; the author attributes `{slug, userId, nick, bio, image.*, memberSince, followersCount, links.*}` are **PERSONAL, redacted** |
| `meta.page.{title,description,listTitle,proStatus,size,totalPages,total,minmaxPublishOn.{min,max}}` | str/int | `total 2391` | the full listing size (only 2 fetched) |
| `meta.mone.params.pu` | str | | |

**D. bronze `article`** (`.../article/article_hash=4bdd69a3.../20260911T040307Z.json`, 13,353 B; 143 leaves). The
hash was verified as `sha256("sa:4943496")`.
| path | type | shape | meaning |
|---|---|---|---|
| `data.id` / `data.type` | str | `"4943496"` / `"fullArticle"` | |
| `data.attributes.title` / `originalTitle` | str | | |
| `data.attributes.summary` | list[str] | 4 bullets | the author's summary bullets |
| `data.attributes.content` | str HTML | about 10 KB | **full article body** |
| `data.attributes.quickInsights[]` | list[{question, answer}] | 3 | SA-generated Q&A |
| `data.attributes.{publishOn,lastModified}` | str ISO-8601 | | |
| `data.attributes.closestTradingDate` | str | `"2026-09-08"` | |
| `data.attributes.{beforeOpeningHours,isExclusive,isTranscript,isEarningsSlides,isPaywalled,isLockedPro,isMpwLocked,inEmbargo,isModerated}` | bool | | |
| `data.attributes.locale` / `availableTranslations` | str / list[str] | `"en"` / 7 langs | |
| `data.attributes.themes.<slug>.{id,slug,kind,path,title,sasource,non_theme}` | dict of dict | 9 themes, one `kind:"sector"` | article taxonomy |
| `data.attributes.disclosure` | str HTML | | the author's position disclosure |
| `data.attributes.{twitContent,innerMarketing,marketingBullet,marketingBio}` | str | marketingBio is PERSONAL | marketing text |
| `data.attributes.{audioDuration,likesCount,commentCount,status,disabledStatus}` | float/int/str | | |
| `data.relationships.primaryTickers.data[]` | list | 5 | tickers the article is about (tag ids) |
| `data.relationships.otherTags.data[]` | list | 17 | |
| `data.links.{self,canonical,uriImage,schemaImage[]}` | str | | |
| `included[]` (author 1) | obj | | PERSONAL, redacted |
| `meta.{proStatus,page.*,path,redirectPath}` | | `meta.path "/api/v3/articles/4943496"` | |

**E. silver `symbol_profile`** (0 objects). The writer is `harvest_grammar.symbol_rows`
(`lib/opal_data_harvest/harvest_grammar.py:121-131`): one row per symbol call. Every `data.attributes.*` key is kept
at the top level (about 33 columns, names as in table A), plus:
`security_key` (str, ours) · `sa_id` (str, `data.id`) · `fetched_at` (tz-aware ts) · `bronze_key` (str lineage) ·
`record_hash` (added by `store.silver_append`, `store.py:361-369`). **Dropped:** `relationships` (so GICS
sector/sub-industry CODES are lost; only the display strings survive), `included`, `meta` (contentCounters, the
availability flags, routes). Dedupe key: `("security_key",)` (`rest_fetch.py:341`). It is Parquet, so the nested
attribute lists (`mergedTickers`, `mergedInto`) become list columns.

**F. silver `news_item`** (0 objects). The writer is `harvest_grammar.news_rows` (`:134-146`): one row per
`data[]` item. It keeps every `attributes.*` key (title, publishOn, isLockedPro, isPaywalled, commentCount,
gettyImageUrl, videoPreviewUrl, videoDuration, themes, **content** for news), plus `security_key`, `sa_article_id`,
`fetched_at`, `bronze_key`, `record_hash`. Dedupe key: `("security_key","sa_article_id")` (`rest_fetch.py:422`).
**Dropped:** relationships (author, sentiments, the primaryTickers ids), `links.self` (the URL), `included`, and
`meta.page.total`. **Only `/news` feeds this table. `/analysis` lands bronze only, with no silver row**
(`rest_fetch.py:396-399`), although `news_rows`' docstring says it would take either.

**Silver `article` for SA:** none. `put_article_bronze` lands bronze only. The `article` silver shaper
(`harvest_grammar.py:100-107`) takes a `publication_article` record, not an SA envelope.

### 1.4 Transformations
- bronze = the exact vendor bytes (`response.content`), with no parse before landing (`rest_fetch.py:258-261`).
- silver = flatten one level plus our key plus lineage. There is no rename, no scoring and no model call. Timestamps
  are parsed tz-aware (`harvest_grammar.py:84-97`).
- **No SA field reaches any served JSON or the page.** `scoped_amgt.py` touches SA bronze only as KEY NAMES
  (stamps), for the FWD-7 freshness row (`lib/research/api/scoped_amgt.py:3218-3240`, `:3350-3355`, route
  `GET .../freshness` `:3909-3910`). It never makes a GetObject on SA.
- `lib/research/coverage/run_reader.py:81-130` does read SA bronze bodies, and it writes to a worker deliverables
  folder. It is not served (see H3).

### 1.5 Component map
| component | reads | trace |
|---|---|---|
| Lead Panel | NONE of the SA fields. The overlay shows only the peer count and basis (Channel 3) | -- |
| Thesis | NONE. The SA report (`responseContent`: description, competitors, positives, concerns) is landed for 3 names and read by nothing | grep `virtual_analyst` over `lib/research`: 0 readers |
| Exec Mgmt | NONE | -- |
| Peers | NONE today (C-PEER-SET-SA is unbuilt, Channel 3) | -- |
| Model | NONE of the bronze above. The forecast fallback is Channel 2 | -- |
| (outside the five) freshness | the SA bronze key stamps -> `per_input.seekingalpha` | `scoped_amgt.py:3335-3355` |

---

## CHANNEL 2 -- SA forecast fallback (Model tab, C-MODEL-FORECASTS)

- **Mechanism:** `integrations/bloomberg/research/sa_forecast_fallback.py`. The Bloomberg model-block producer calls
  it (`model_block_pull.py:282-290`, `:825-852`) ONLY for FY1-FY3 `BEST_*` cells that Bloomberg left empty. It rides
  `rest_fetch.py`'s `load_config` / `build_session` / `_do_get` / `land_harvest`, loaded by path
  (`sa_forecast_fallback.py:113-123`).
- **Steps:**
  1. Candidate symbol = the crosswalk `sa_symbol` if one exists, else the Bloomberg root. A numeric root returns
     None, and the attempt ends "UNRESOLVED: no SA symbol candidate" (`:101-110`, `:217-219`).
  2. `GET /api/v3/symbols/{cand}` lands `symbol` bronze (`:222-235`).
  3. Entity test (`:66-78`, `:239-248`).
  4. `GET /api/v3/metrics?filter[fields]=<candidates>&filter[slugs]=<slug>` lands `metrics` bronze (`:259-279`).
  5. Fill a cell only when `meaningful` is true and the value is non-empty (`:290-317`).
- **Field map** (`:85-91`): `BEST_PE_RATIO -> pe_nongaap_fy{n}` is MEASURED (from the CRO peers brief). `BEST_EPS ->
  eps_normalized_fy{n}`, `BEST_SALES -> revenue_fy{n}`, `BEST_EBITDA -> ebitda_fy{n}` and `BEST_DPS -> dps_fy{n}` are
  UNMEASURED candidates. `/metrics`' response shape is unmeasured, so `_extract_metric_values` tolerates two shapes
  (`:126-154`).
- **Storage:** `metrics` bronze is **0 objects**. The fill lands inside the model block
  (`derived/model_block/<key>/<stamp>/model_block.json`, 122 objects) as a `figures[]` entry with `scope:"forecast"`,
  `source:"SA_FALLBACK"`, `sa_field`, `sa_symbol`, `sa_raw_key`, `estimate_basis:"consensus"`
  (`model_block_pull.py:854-875`). There is also a per-block `forecast_fallback` record: `{sa_symbol_candidates,
  sa_symbol, entity_test, classification, gaps_before, filled_by_sa, sa_raw_key, reason, sa_field_map}`
  (`sa_forecast_fallback.py:157-192`, `:319-332`). Unfilled gaps become `unresolved[]` rows carrying a
  `fallback_status` (`model_block_pull.py:877-887`).
- **Live state:** 3 of the newest blocks (CAT_US, 6861_JP, CSL_AU at `20260919T1521xxZ`) each read
  `forecast_fallback.reason = "no Bloomberg gap -- nothing to fill"`, with forecast sources `BBG: 15`. So **SA has
  filled 0 cells in the blocks sampled.** The 0 metrics objects bound this across the whole store: no metrics call
  has ever succeeded.
- **Component map:**
  - **API:** `scoped_amgt.py:2850-2909` serves `forecast_figures` and `forecast_source_counts {BBG, SA_FALLBACK,
    ABSENT}` on the `/thesis` payload.
  - **Model tab:** `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx:110` renders `fiscal_year_figures` only.
    Grep for `forecast`, `forecast_figures` and `SA_FALLBACK` over the portal `.ts/.tsx` files finds only comments
    (`:25`, `:82`). **So no component renders any forecast cell today, BBG or SA_FALLBACK.**
  - The overlay's `ProvenanceLine` prints `figure.source` (`components/ProvenanceLine.tsx:37`) for header figures
    only.

---

## CHANNEL 3 -- PEERS (C-PEER-SET-SA contract vs the scanner ranker that is live)

### 3.1 The contract (PRD `AMGT_RESAPP_PRD.md:700-726`, floors `:728-735`)
- SA suggested peers, 5 per subject: `GET /api/v3/symbols/{slug}/suggested?source_type=peers_similarities`, through
  the EXISTING `rest_fetch.py`, GET only. `basis` = `sa | absent` with a named reason (`:701-704`).
- An ENTITY test before any peer call. `ROG`-is-Rogers-not-Roche is the negative control. Each PEER's Bloomberg join
  is name-checked too (`:705-708`).
- The table uses SA's shape, all 17 of 17 CSC columns. Preferred + Minority is one column, `other_cap_struct`
  (`:709`).
- Source rule: SA first, then Bloomberg (`<TICKER> US Equity`), then SA's nearest measure, labelled as such. Every
  cell carries `source` = `SA | BBG | SA_FALLBACK:<field>`. Each summary row prints its source mix (`:710-714`).
  `meaningful:false` shows as ABSENT and is never filled (`:715-716`).
- REHARVEST stops the run. Raw lands before any derivation, at an `opal_naming` address (`:717-719`).
- Authorized by name, and the terms are cleared (`:720-723`). Peers V floors are 5 / 5 / 3 (`:728-732`).
- **The SA page's calls, as the CRO measured them** (`BRIEF_PEERS_CURRENT_TO_DESIRED_20260918.md:63-68`):
  `/symbols/{slug}/suggested?source_type=peers_similarities&variation=ds_v2`, `/tickers?filter[slugs]=...&include[gics]=true`,
  `/metrics?filter[fields]=...&filter[slugs]=...`, `/ticker_metric_grades?...&filter[algos][]=main_quant`. The SA
  fields for the 17 columns (`:84-95`): `close, marketcap, tev, total_debt, total_cash, other_cap_struct (12/18),
  pe_nongaap_fy1/2/3, revenue_growth5`. Bloomberg fills 5-yr EBIT and FCF growth (`GEO_GROW_OPER_INC`,
  `FREE_CASH_FLOW_5_YEAR_GROWTH`). Shares and the three leverage ratios are derived.
- **BUILT STATE: NONE.** No code calls `/suggested`, `/tickers` or `/ticker_metric_grades` (the Grep above). No
  bronze table exists for them. `peers/v1` carries no `basis:"sa"` object. The live engine still hard-codes the SA
  input as `ABSENT-ACCESS, called:false` (`lib/research/peers/engine.py:286-325`), and its reasoning is now stale: it
  cites the CRO's `sa_rest_fetch.py` and "not reachable under this session's egress", while `rest_fetch.py` has since
  been used for exactly these calls. The PRD's "no bronze table" note for the peers table
  (`BACKFILL_SCOPE_PROPOSAL_20260922.md:55`) matches.

### 3.2 What is live: the scanner ranker
- **Candidate universe** (`lib/research/peers/universe.py`). One database: the 6 Security Scanner files
  `s3://opal-data-portal-v2/json/security_scanner/latest/universes/{sp500,r1000,r1000v,acwx,eafe,eafev}/universe_data.json`
  (`:64-69`, `:412-467`) UNION the model-block header scalars (`GICS_SECTOR_NAME`, `CUR_MKT_CAP`,
  `CNTRY_OF_DOMICILE`, `CRNCY`) (`:471-554`). One row per ticker. Units are normalised: the scanner reports USD
  millions, and block caps are divided by 1e6 with no FX applied (`:24-33`, `:490`, `:534-545`). A non-US block does
  not join a scanner row by root (`:35-41`, `:496-505`). Built by hand (`main` `:759`, `refresh_candidate_universe`
  `:737`).
- **gold `amgt/harvest/gold/candidate_universe/date=2026-08-06/candidate_universe.json`** (1 object, 1,000,578 B,
  written 2026-09-18 21:25; address from `opal_naming.address` `:98-104`):
  - top level: `schema_version` (int, **1** here although the code writes 2, `:171`), `vintage "2026-08-06"`,
    `vintages_per_file{6}`, `vintages_distinct`, `read_at "2026-09-15T09:15:54Z"`, `source{bucket,prefix,
    universe_ids,source_columns{sp500:"wt_ivv",...},model_block_dir,model_block_skipped_unclassified}`,
    `read_failures{}`, `row_value_codes[284]`, `denominators{}`, `taxonomy_residue`, `rows[2851]`.
  - denominators: `database 2851 = scanner_unique_tickers 2849 + model_block_rows_added 2`; `scanner_rows_read 5282`;
    `model_block_files_read 4` (one skipped unclassified).
  - `rows[]`: `ticker` (str; the US symbol, or a `*`-prefixed or SEDOL-shaped id for non-US, e.g. `"*ABX"`),
    `name` (str), `mktVal` (float, USD mm), `country` (str, a full name such as `"United States"`), `sector` and
    `industryGroup` (str, scanner vocabulary), `price` (float), `universe_weights{<id>: float}`, `sources`
    (list[`scanner`|`model_block`]), `security_key` (str|null, **set on 3 of 2851**), `sector_vocabulary`,
    `currency` (str|null), `cap_fx_caveat` (bool|null).
  - **The schema-2 fields the code now writes are NOT in the landed object:** `preset_values`, `fx_basis`,
    `cap_currency`, `cap_vintage`, `cap_source`, `size_band_basis` (`:370-377`).
  - Country mix: US 1045, CN 329, HK 179, JP 168, IN 165 ...
- **Ranker** (`lib/research/peers/engine.py`). Four lexicographic rungs (sector -> 0.2x-5x size band -> country ->
  industry group), with ties broken by |log cap ratio|. Members come from depth >= 2, max 12 (`:1-39`, `:65-136`).
  Identities resolve through the crosswalk, widened by the positioning-chain FIGI/CUSIP/SEDOL identity set
  (`:206-283`). It writes to `peers/v1/<security_key>/<as_of>.json` (`pool_key` `:1134`, `write_pool_object`
  `:1138`), by hand (`run_batch` `:1228`, `main` `:1426`).
- **gold (legacy served) `peers/v1/`**: **797 objects over 191 subject keys**. There are two grammars: 573 carry an
  ISO stamp `<YYYY-MM-DDTHHMMZ>.json`, and the rest are `<date>.json` (inventory s.11a/b, H-3). The newest batch is
  `2026-09-17T0240Z` (LastModified 09-16 22:42). Subjects by exchange suffix: US 168, LN 7, SW 3, NA 2, and 1 each for
  MM IM FP GY JP TT GR BZ SP HK IN. Field dictionary of the stamped shape (sample `peers/v1/BA_US_Equity/2026-09-17T0240Z.json`,
  46,976 B):
  | path | type | shape / example | meaning |
  |---|---|---|---|
  | `security_key` | str | `"BA_US_Equity"` | subject key |
  | `as_of` / `vintage` | str | `"2026-09-17T0240Z"` / `"2026-09-17T02:41Z"` | run stamp |
  | `basis` | str enum | `"derived"` (`analyst`/`derived`/`absent`) | |
  | `test` / `reason` | str | long prose | the rule, and the per-subject verdict with denominators |
  | `rungs[4]` | list[{rung,name,field,test}] | | |
  | `members[12]` | list[obj] | | the peers |
  | `members[].ticker` / `name` | str | `"DE"` / `"Deere & Company"` | scanner identity |
  | `members[].identity.{security_key,resolution,matched_as,raw_identifier}` | obj | `resolution "UNRESOLVED"` on **12 of 12** for BA | our key for the peer (none resolved) |
  | `members[].{sector,industry_group,country}` | str | | |
  | `members[].{market_cap_musd,cap_ratio_to_subject,log_cap_distance}` | float | `165968.0`, `1.04`, `0.039` | size |
  | `members[].{cap_currency,cap_source,cap_vintage,fx_basis,size_band_basis}` | str | `"USD"`, `"scanner:sp500"`, `"2026-08-06"` | size provenance |
  | `members[].{rung_reached,rung_name}` | int/str | `3` / `"country"` | |
  | `members[].factors{<code>: float}` + `factor_horizons{}`, `factors_basis`, `factors_denominator`, `horizon*` | dict | 26 preset codes (e.g. `accruals_bs`, `days_to_cover`) | scanner factor values |
  | `members[].universe_weights{}` | dict | | |
  | `subject{23}` | obj | `name "BOEING CO/THE"`, `market_cap_musd 159623.1`, `cap_source "model_block:BA_US_Equity:CUR_MKT_CAP"`, `country_raw "US"`, `sector_raw`, `sector_mapped[]`, `industry_group null`, `cross_vintage_caveat` | the subject, from the model block |
  | `csc_columns{14}` | obj | `columns[17]`; `present[5]` = Price/`price`, Mkt Cap/`mkt_val_sec`, EV/`ev`, P/E 2025/`ey`, P/E 2026/`ey_ntm`; `absent[12]` each `{column,reason,nearest_code,derivable_from}` | the CSC map |
  | `denominators{14}`, `fit_denominators{9}`, `horizon_census{5}`, `sector_map{8}`, `country_map{6}` | obj | `database 2851 - 1 self` | MECE accounting |
  | `sa_candidates{9}` | obj | `status "ABSENT-ACCESS"`, `called false`, `comparables_endpoint null` | the stale SA stub (3.1) |
  | `universe_vintage` / `union_universe_source` | str | `"2026-08-06"` / `s3://opal-data-harvest/universe/v1/2026-09-16.json` | |
  | `schema_version` | int | `1` | |
- **Downstream:** `scores/v1` Peers V (`lib/research/scores/run_scores.py:71`, per inventory s.2 row 11) reads the
  peer set. It is ABSENT on 33 of 33 (CRO brief `:45`).

### 3.3 Transformations
The scanner rows become the candidate universe (fold 5282 rows to 2849 tickers, add model-block rows, normalise
caps). The universe becomes a peer set (rung depth, band, sort, cap 12). `csc.py` then maps 17 columns to 5 present
and 12 absent. No model call is involved. Under C-PEER-SET-SA, all of this is replaced by SA's 5 plus the sourced
17-column table. That transformation is unbuilt.

### 3.4 Component map
| component | fields | API side | portal side |
|---|---|---|---|
| **Peers** | whole R-1 object: `basis`, `members[].{name,ticker,market_cap_musd}`, `subject.{name,market_cap_musd}`, `csc_columns.{columns,present,absent}`, `universe_vintage`, `as_of`, `test`, `reason`, `vintage`, `peer_read` | `read_peer_set` `scoped_amgt.py:1277-1311`; route `GET .../security/<key>/peers` `:3869-3872` | `usePeerSet` -> `portal/src/api/endpoints/amgt-lead-panel.ts:138`; `tabs/PeersTab.tsx:140-178`; table `cscTable.ts:86-134`. **Only ONE column carries per-row values**: `MEMBER_FIELD_FOR_CODE = {mkt_val_sec: 'market_cap_musd'}` (`cscTable.ts:30-32`). Price, EV and the two P/E columns are "present" but render "not carried" (`:97-108`), and the 26 `members[].factors` are never read |
| **Lead Panel** (overlay) | `peers.basis`, `peers.members.length`, `peers.reason` | `read_security_overlay` payload key `peers` `scoped_amgt.py:1949` | `components/SecurityOverlay.tsx:150-154` ("N peer(s), basis -- see Peers tab") |
| **Model** | Peers V (from `scores/v1`, which is computed over the peer set) | `/thesis` payload `scores` | `tabs/ModelTab.tsx:89` `ScoreLine label="Peers V"` |
| Thesis / Exec Mgmt | NONE | -- | -- |
| (Posture, out of scope) | peers via `usePeerSet` | | `PostureTab.tsx:339,347` |

---

## KEYING -- how SA keys a security vs ours

- **SA keys:**
  - The **slug** is lower-case (`symbol.data.attributes.slug "ba"`). It is the URL key for `/suggested` and `/metrics
    filter[slugs]`.
  - The **ticker** is upper-case in the path (`/symbols/BA`), and appears as `attributes.name "BA"` and as
    `report.slug "BA"`.
  - The **sa_id** is a numeric string (`"769"`). It is the virtual_analysts key and equals the tag id in
    `primaryTickers`.
  - The **article id** is numeric.
- **Ours:**
  - `security_key` is ticker-derived (`BA_US_Equity`). It is the partition on all SA bronze (`security_key=`),
    passed in by the caller (`--security-key`) and never derived from SA.
  - The SA ticker comes from the operator on the command line (`run-ticker <SA_TICKER>`).
  - The legacy raw used a different key form, `BA_US` (inventory s.17).
- **No stored crosswalk SA <-> security_key:**
  - `crosswalk/v1/2026-09-19.json`: 96 records, and **0 carry an `sa_symbol` field at all** (the record keys are
    `association_keys, bloomberg, display_ticker, exchange, model_key, provenance, raw_identifier, resolution,
    security_key, share_class, source_row`).
  - `universe/v1/2026-09-16.json`: 250 names, 0 with `sa_symbol`.
  - The only SA-id map is the local `sa_ids.json` in a run's state dir (`rest_fetch.py:342-349`).
  - `resolver.infer_sa_symbol` (`lib/research/identity/resolver.py:80-110`) INFERS a US root and returns
    UNRESOLVED for every ex-US ticker. It is never MEASURED.
- **Composite FIGI:** SA exposes no FIGI in any sampled payload. The join to a FIGI key has to go
  FIGI -> our listing -> (ADR ticker) -> SA slug, with the entity test at the last hop.

## NON-US COVERAGE -- does SA cover a JP/EU local listing?

**Measured answer: only through a US line (NYSE/Nasdaq ADR or OTC ADR/F-share), never the home listing.**
- The CRO resolve pass records "the Bloomberg root 404s for every non-US name, only the US ADR resolves"
  (`org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py:6-8`, citing HARVEST_BACKFILL_PLAN s.18).
- The peers measurement resolved KDDI through its OTC ADR `KDDIY`. Every SA peer ticker returned was "a US listing
  or ADR, priced in USD" (CRO brief `:58`, `:78`). BABA's SA symbol is the NYSE ADR (`exchange "NYSE"`, currency
  USD, in bronze).
- In code, a numeric root (JP `6861`, TT `2317`, HK `992`) yields no candidate at all
  (`sa_forecast_fallback.py:107-109`).
- An alphabetic ex-US root is sent as-is (e.g. `ROG` from ROG SW, which gives Rogers Corp). Only the entity test
  stands between that and a wrong company.
- Consequences:
  - (a) every non-US subject needs an ADR-mapping step that nobody has built;
  - (b) a name with no US line has no SA peers, and its `basis` must be `absent` with reason "no SA slug";
  - (c) the SA table is USD/ADR-scaled, while our Model tab is in the home currency at the home listing, so the
    subject's figures differ across tabs;
  - (d) coverage density on OTC ADRs is thin (KDDI and SK Telecom carried no SA estimates, CRO brief `:101-103`).

---

## GAPS AND HAZARDS

- **H1 (new, fallback correctness).** `sa_forecast_fallback.py:239` sets `sa_name = attributes.name or
  attributes.companyName`, but in SA's real symbol envelope **`name` is the TICKER** (`"BA"`, `"BABA"`) and the
  company is in `companyName`. So the entity test compares our company name with a ticker.
  - Exercised offline on the module's own `entity_test` with names from the landed bronze: Boeing is REFUSED
    (should PASS). COST and BABA PASS only by accidental substring containment (`"cost"` in `costcowholesalecorp`,
    `"baba"` in `alibaba...`). The ROG control still refuses, so the standing negative control cannot see this defect.
  - The offline tests plant `attributes.name = "Caterpillar Inc."` (`tests/test_forecast_fallback.py:163,194,213,233,296`),
    a shape SA does not serve.
  - The defect will matter the first time a Bloomberg gap exists. The same trap applies to C-PEER-SET-SA's entity
    test and to the per-peer name check. Compare `companyName`.
- **H2. C-PEER-SET-SA is entirely unbuilt.** No `/suggested`, `/tickers`, `/metrics` (peers) or grades fetcher; no
  bronze table name; no silver; no gold peer_set of `basis sa`; no `source` per cell. The engine's
  `sa_candidates()` stub carries a stale ABSENT-ACCESS reason into every one of the 797 objects. PRD-required fields
  the data lacks: the 5-peer SA set, `other_cap_struct`, `pe_nongaap_fy1..3`, `total_debt/total_cash/tev`,
  `revenue_growth5`, per-cell `source`, the per-summary source mix, and the `meaningful` flag.
- **H3. The SA reader in coverage parses the wrong shape.** `lib/research/coverage/run_reader.py:126` reads a
  top-level `payload["attributes"]`, but every SA bronze object nests under `data` (a list for news and analysis).
  Every SA coverage item would get `title None`. Its comment says the shape was "not yet measured". It is measured
  now (above).
- **H4. The landed data is 3 US names, one 11-day-old run, with no silver.** 18 bronze objects, 0 silver, 0 metrics.
  The session was captured 2026-09-11T02:13Z (CRO brief `:59`), and the backfill proposal says it needs re-harvest.
  The legacy `raw/seekingalpha/` copies (18) still exist beside bronze, so there are two copies of the same bytes.
- **H5. Peers tab under-renders what R-1 carries.** Only `market_cap_musd` maps to a column (`cscTable.ts:30-32`).
  Price/EV/P-E are "present" in `csc_columns` but shown "not carried", although values exist in
  `members[].factors`. That tab is about to be replaced by the SA table anyway.
- **Other hazards:**
  - **Gold candidate_universe is schema 1 while the code writes 2.** The landed object lacks the size-band provenance
    fields the ranker now expects (`fx_basis`, `cap_vintage`, `size_band_basis`, `preset_values`). Its scanner
    vintage is 2026-08-06 (six-plus weeks old).
  - **Peer identities are unresolved:** 12 of 12 BA members read `UNRESOLVED`, and 160 of 372 members across 33
    subjects carry SEDOL-stem tickers (CRO brief `:43`).
  - **The plan text disagrees with the code on the article hash.** PLAN s.5.4 (`:273-274`) says
    `sha256("seeking-alpha:"+id)`. The code (`harvest_grammar.py:51`) and the landed keys use `sha256("sa:"+id)`
    (verified on article 4943496). Any second channel that follows the plan text will not dedupe against these
    objects.
  - **Time zones:** SA timestamps carry the -04:00 US-Eastern offset (publishOn, createdAt). The silver parse keeps
    them tz-aware.
  - **Language:** SA articles are `locale "en"` with `availableTranslations`. No foreign-language body was seen.
  - **Legacy pipeline:** `infra/aws/terraform/seeking-alpha/main.tf` declares the analysis and news scrapers into
    `opal-data-news-av/seeking-alpha/{analysis,news}/`, with 7 Lambdas (`:27-33`, `:142-144`). Their EventBridge
    rules `seeking-alpha-analysis-daily` (cron 0 21) and `seeking-alpha-news-daily` (cron 0 14) read **DISABLED**
    live (`events describe-rule`, 2026-09-22). They play no part in AMGT.

---

## SUMMARY
1. SA REST (`integrations/seekingalpha/rest_fetch.py`) rides a parked, browser-minted cookie jar (identity plus
   PerimeterX) from Secrets Manager over the residential proxy. A REHARVEST 403 stops the run. It makes 5 GETs per
   ticker: symbol, virtual_analysts report, analysis, news, and 2 articles. It was run once by hand (2026-09-11) for
   BABA, BA and COST.
2. Live store: 18 bronze objects under `seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/security_key=<k>/`
   plus `article/article_hash=sha256("sa:"+id)/`. Silver `symbol_profile`/`news_item` holds 0 objects, metrics bronze
   0. The 18 legacy `raw/seekingalpha/` duplicates remain.
3. No SA field reaches Lead Panel, Thesis, Exec Mgmt, Peers or Model today. The API reads SA bronze key NAMES only,
   for freshness. The landed virtual-analyst report (description, competitors, positives, concerns) has no reader.
4. The Model tab's SA_FALLBACK path exists in the producer and the API, but SA has filled 0 cells (0 metrics
   objects; the sampled blocks show "no Bloomberg gap"), and ModelTab renders no forecast cells at all.
5. Peers today = the scanner ranker (`peers/v1/`, 797 objects over 191 subjects, 12 members, only 5 of 17 CSC
   columns, peer identities UNRESOLVED) over the gold candidate_universe (2851 rows, scanner vintage 2026-08-06,
   schema 1). The Peers tab renders only market cap per row.
6. C-PEER-SET-SA (SA `/suggested` x5 + `/tickers` + `/metrics` + grades, 17 sourced columns) is entirely unbuilt.
   The engine still stamps a stale `sa_candidates: ABSENT-ACCESS` into every object.
7. Keying: SA uses a lower-case slug, an upper-case ticker and a numeric sa_id, with no FIGI. We use the
   ticker-derived security_key, and no stored crosswalk carries any SA symbol (0 of 96 crosswalk records, 0 of 250
   universe names).
8. Non-US: SA covers a JP/EU name only via its US ADR/OTC line, never the home listing. Numeric roots get no
   candidate, so ADR mapping is an unbuilt prerequisite, and the SA table is USD/ADR-scaled.
9. NEW defect H1: the fallback's entity test reads `attributes.name`, which is SA's TICKER. Boeing would be refused,
   and COST and BABA pass only by accident. Its tests plant a shape SA does not serve. The same trap awaits
   C-PEER-SET-SA; the entity test should compare `companyName`.
10. Also: the coverage run_reader parses the SA envelope at the wrong level (H3); the plan's article-hash text
    disagrees with the code; and the legacy SA terraform rules are live-DISABLED.
