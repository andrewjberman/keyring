# PLAN -- the bronze / silver / gold format of every AMGT_RESAPP ingestion channel in `opal-data-harvest`

**From** `4.0.0_SA_CRO~Z`. **To** `1.0.0_SA_CTO~Z`, for the L4. **Date** 2026-09-21 ~17:3xZ.
**Why now:** Andrew-direct ~17:2xZ today (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_172xZ_AMGT_RESAPP_PROMOTE_IF_FEATURES_NO_WATER_IN_PIPES_BACKFILL_HELD_FOR_BRONZE_SILVER_SHAPE.md`):
he is holding the coordinated backfill until *"the format of the bronze/silver opal-data-harvest for the various
vendor/publication ingestion channels"* is settled. This document is that format, one channel at a time, with each call
reduced to a recommendation.
**Status:** a PLAN. It writes no S3 object, no registry row, no doctrine line and no code. Every S3 read below was
read-only.

**What it builds on.** `PLAN_RESAPP_DATA_STRUCTURE_20260918.md` (@`0756d2897d`) did land on 09-18 beside its two
measured halves; the CTO's record calls it undelivered, and that is fair in one sense: it gave one target table for all
streams, ran no builder call per channel, gave no dedupe rule and no reader list, and did not separate the R4 doctrine
act from plain registry rows. This document supersedes its s.4 table and keeps its s.5 defects and s.6 move order.

---

## 1. The answer in one screen

1. **One scope token for everything: `harvest`.** It is the only registered scope for this bucket
   (`scopes.json` row landed @`e44380a9d1`). The **vendor is the `{source}` for bronze and silver**; **`amgt` is the
   `{source}` for gold, platinum, state and code**. So the tier and the origin can be read from the first three segments
   of every key.
2. **Bronze** = the vendor's bytes exactly as they came back, **one object per fetch, never overwritten**, with the
   channel's FETCH KEY in the partition. Three leaf forms, chosen by what the fetch key is (s.5 per channel):
   - **(a) an entity fetched repeatedly** (Bloomberg requests, Seeking Alpha endpoints, publisher articles):
     `{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`;
   - **(b) an immutable document** (an SEC accession, an issuer or ESEF document): the document id and the vendor's
     own file name as the leaf, under the entity partition, e.g. `sec/harvest/bronze/filing/cik={cik}/{accession}/{primary_document}`;
   - **(c) a request, not an entity** (SERP, social snapshot, Lusha, the SEC ticker table):
     `{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request_sha256 or file}.{ext}`.
   **Correction 2026-09-21 ~17:5xZ:** this item first gave form (a) alone, which seven s.5 bronze addresses do not follow (SEC filing, SEC ticker table, issuer document, ESEF filing, social snapshot, SERP, Lusha); found
   by this seat while reviewing PRD v0.14, which quoted form (a) as the whole contract.
3. **Silver** = typed **parquet** (R10), `date=` partitions, **one `part-<run stamp>.parquet` per run** (append-only,
   so it can never overwrite), deduplicated on a **record key** stated per channel below.
   `{vendor}/harvest/silver/{table}/date=YYYY-MM-DD/part-{stamp}.parquet`.
4. **Gold** = **parquet** (R11), one row per entity per generation:
   `amgt/harvest/gold/{table}/date=YYYY-MM-DD/{table}_{stamp}.parquet`. **Platinum** = a JSON publisher output the API
   reads (R12), because the API Lambda has no parquet reader today.
5. **The registry needs exactly two kinds of change, and only one of them is a doctrine act:**
   - **R4 doctrine act (laptop CRO lane, Andrew's option (ii)):** a NEW tenancy whose six tier cells are all
     `home: scope`, and the `harvest` scope row moved onto it. **This one act moves all 28 AMGT bronze/silver addresses
     from `opal-data-assets` to `opal-data-harvest`, and the platinum address from `opal-data-portal-v2`.** Nothing else
     can do it: a scope row cannot change a tenancy's cells.
   - **Plain registry rows (no doctrine):** five `systems.json` VENDOR rows -- `barrons`, `wsj`, `ft`, and two filing
     sources, `filings-xbrl` and `issuer-site`. **No new scope row is needed.**
6. **Measured, both ways** (s.2): on the LIVE registry, 50 of 60 proposed addresses resolve; **28 AMGT bronze/silver
   addresses print `opal-data-assets`** and 9 are refused for a missing `systems.json` row. On a simulated registry with
   the tenancy change and the five rows, **59 of 60 resolve, every AMGT address in `opal-data-harvest`**; the 60th is
   the slash-key control, refused as designed; the four control scopes (etfs, mdpf, 49financial, global) **do not move**.
7. **What the backfill actually waits on:** bronze and silver formats, the R4 act, the five rows, and the dedupe
   authority moving from a desktop SQLite file into the bucket (s.5.5). **Gold and platinum formats do NOT gate the
   backfill**: gold is re-derivable from silver, so it can follow.

---

## 2. How this was measured

| claim | instrument | denominator / vintage |
|---|---|---|
| live bucket contents | `boto3 list_objects_v2`, paginated to `IsTruncated=False` | **1,461 objects / 43,248,501 bytes / 2 pages**, read 2026-09-21 ~17:1xZ (was 1,333 on 09-18) |
| sample shapes | `get_object` + a key-skeleton printer, one object per new leaf type | 8 objects read; no values quoted |
| addresses | `lib/opal_naming.py` `address()` imported by path, then `grade(key, "S3Key")` on every result | **60 channel rows** (`scratchpad/fmt/channels.json`), live registry and a simulated copy |
| registry vintage | `registry_hash()` | `93ea36e7d295...a3d2` at HEAD `0687d98335` (SITEZ) |
| doctrine | `infra/logic/02_DOCTRINE.md` bytes printed at R4 `:358-368`, R8 `:414-421`, R9-R12 `:425-470` | HEAD; the laptop branch `origin/CLOUD` checked: **no R4 change there either** (its `02_DOCTRINE.md` diff is `:224` and s.6 only) |
| readers | native `Grep` over `lib/research`, `lib/opal_data_harvest`, `integrations/`, `infra/aws/terraform/harvest/` | named per channel, `file:line` |

**The simulation** copied `infra/logic/registry/` to `scratchpad/fmt/registry_sim/`, added tenancy `PRODUCT-CONTAINED`
(six cells `home: scope`), set the `harvest` row's tenancy to it, and added the five VENDOR rows. `validate()` on it:
**0 refusals** (only the pre-existing owner-directive warnings). **Negative control:** the same copy with the `harvest`
tenancy set to `NOSUCHTENANCY` returns **1 refusal** (`'NOSUCHTENANCY' has no tier home rule in tiers.json`), so the
0 is not a constant. The repo registry was not written.

**Two cross-bucket checks, read-only:** `opal-data-assets` holds **0 objects** under `sec/`, `bloomberg/`, `lusha/`,
`bright-data/` and `amgt/`. So no AMGT byte has landed in the client-custodial bucket; nothing needs moving back.

---

## 3. The registry, and which change each channel needs

### 3.1 What the live builder prints today

| tier | live `address()` for scope `harvest` | right per Andrew? |
|---|---|---|
| bronze, silver | `s3://opal-data-assets/...` (tenancy PRODUCT, `tiers.json` shared cell) | **NO** -- his 09-18 ~21:5xZ and ~22:0xZ words |
| gold, state, code | `s3://opal-data-harvest/...` | yes |
| platinum | `s3://opal-data-portal-v2/...` | **NO** -- *"the whole pipeline will exist within opal-data-harvest"* (quoted in the `harvest` row's own note) |

**Superseded for platinum by PRD v0.15:** `1.0.0_SA_CTO~Z` ruled platinum follows the canon's R6 general home as the
builder prints it (`opal-data-portal-v2`), and is surfacing to Andrew that this departs from his "whole pipeline"
phrasing. The platinum rows below (s.1 item 5, s.5.9) are this plan's original recommendation; the PRD contract binds.

### 3.2 Recommendation on the R4 act: a new tenancy, never an edit of PRODUCT

**Recommend: add a fifth tenancy with all six cells `home: scope`, and move only the `harvest` row onto it.**
Editing the PRODUCT tenancy's cells instead would re-home `etfs` and `mdpf` bronze, silver and platinum in the same act,
and their live data would not move with it. The controls in the simulation are the evidence that the new-tenancy form
does not do that: `bloomberg/etfs/silver`, `bloomberg/mdpf/bronze`, `schwab/49financial/bronze` still print
`opal-data-assets` and `mdpf/global/platinum` still prints `opal-data-portal-v2`. The tenancy's NAME is the laptop
lane's call; `PRODUCT-CONTAINED` is only the simulation's placeholder. The doctrine line quotes Andrew:
*"opal-data-assets is very specifically for client/partner custodial information"*.

**Owner:** the laptop `4.0.0_SA_CRO` lane (lane PLATFORM_LOGIC_DOCS; `infra/logic/**` is not this lane's on site Z).
**Not landed on either branch as of this read.**

### 3.3 The marks used in s.5

- **[R4]** -- the address prints `opal-data-assets` (or `opal-data-portal-v2`) until the R4 act lands. Every bronze and
  silver address, and the platinum address. **28 bronze/silver + 1 platinum.**
- **[ROW]** -- the builder refuses today for a missing `systems.json` row; a plain row fixes it. **9 addresses across
  5 tokens.**
- **[OK]** -- resolves in `opal-data-harvest` today. Gold, state, code.

---

## 4. The format rules every channel follows

**Bronze (R9).** The response bytes exactly as they arrived: JSON stays JSON, PDF stays PDF, a zip stays a zip. No
parsing, no trimming, no re-serialising (today `json.dumps` of a parsed response is NOT the bytes; the bronze writer
stores the body as received). One object per fetch, and the leaf is the compact UTC fetch stamp, so **a write can never
land on an existing key**. The partition carries the channel's fetch key -- an entity key (`security_key=`, `cik=`, `article_hash=`)
where the channel fetches an entity, `date=` where it fetches a request (s.1 item 2, forms a-c).

**Silver (R10).** Parquet. Every vendor field kept, typed; no filtering to "what Opal cares about". `date=` is the
FETCH date. One part file per run. Every row carries `bronze_key` (the object it came from), `fetched_at` and
`record_hash` (sha256 of the row's vendor fields).

**The dedupe rule, one form for every channel:** each channel names a **record key**. A silver writer (a) skips a row
whose `(record key, record_hash)` is already in silver, and (b) writes a changed row as a NEW row, never an update.
**A reader takes the newest `fetched_at` per record key.** For the fetch itself, each channel names a **fetch key**
and the writer checks the bucket for it BEFORE calling the vendor -- that is the rule that stops a second pull of the
same article, filing or query.

**Gold (R11).** Parquet, one row per entity per generation, `date=` = generation date, the stamp in the file name (his
words: *"dated/timestamped-in-title parquets and each day we just add a row"*). Nested content (citations, passages,
peer members) goes in list/struct columns.

**State (R21).** Run logs, attempts and pointers, under `amgt/harvest/state/`. Append a new object per event. The
one exception is a `current.json` pointer, which may move (versioning keeps its history).

**The security key must be slash-safe before it reaches a builder.** Measured: `security_key=BP/_LN_Equity` as a
partition is **REFUSED** by the builder (`partition must be ... no '/'`). That is the right result -- and it only
happens because the entity sits in the PARTITION. If it sat in the free-form `object` argument, the builder accepts `/`
there, and the 10-object phantom-`BP` defect would carry straight into the new grammar. **Recommend: mint one slash-safe
form in `lib/research/identity/crosswalk.py` (e.g. `/` becomes `-SLASH-`), and never put an entity id in `object`.**

**Metadata on every object:** `document-sha256` and `schema-version`, written by ONE writer (today there are four
`write_pool*` copies plus five raw `put_object`s; inventory H-9).

---

## 5. Channel by channel

Each block gives: **live today** (prefix, count, shape), **proposed** (builder output; `[mark]`), **record key and
dedupe**, **readers that must change**, **recommendation**. "Post-R4" addresses are the simulated registry's output,
verbatim; the live registry's differ only in the bucket name.

### 5.1 Bloomberg (Terminal DAPI) -- refdata, histdata, bestdata, identity, exec_officers

**Live:** `raw/bloomberg/<security_key>/<stamp>/<request>.json`, **119 objects**: refdata 48, histdata 48,
histdata_daily_px 1, bestdata 6, identity 3, exec_officers 4, pull_log 9. Metadata `{}` on all. The body is the client
library's parsed dict re-serialised, keyed by the SPACED Bloomberg id (`"CSL AU Equity": {...}`); `exec_officers.json`
wraps it as `{security, pulled_at, response: {NAME, COMPANY_EXEC_OFFICERS[14]}}`; `bestdata.json` carries its own
`requests[3]` beside the 1FY/2FY/3FY blocks. Silver today: `derived/model_block/<key>/<stamp>/model_block.json`,
**122 objects** (47 on 09-18), metadata `{}`; `derived/model_block_fye/` 3 objects, **no reader**.

**Proposed:**

| request | bronze (post-R4) `[R4]` | silver table `[R4]` |
|---|---|---|
| refdata | `s3://opal-data-harvest/bloomberg/harvest/bronze/refdata/security_key=CSL_AU_Equity/20260921T162530Z.json` | `security_reference` |
| histdata | `.../bronze/histdata/security_key=.../<stamp>.json` | `model_block` (row per security x fiscal year x mnemonic) |
| histdata_daily_px | `.../bronze/histdata_daily_px/security_key=.../<stamp>.json` | `security_price_daily` |
| bestdata | `.../bronze/bestdata/security_key=.../<stamp>.json` | `security_estimate` |
| identity | `.../bronze/identity/security_key=.../<stamp>.json` | `security_identity` |
| exec_officers | `.../bronze/exec_officers/security_key=.../<stamp>.json` | `executive_officer` |

Silver form, verbatim: `s3://opal-data-harvest/bloomberg/harvest/silver/model_block/date=2026-09-21/part-20260921T162530Z.parquet`.
Live registry prints the same keys in `opal-data-assets`. `pull_log.json` is a run log, not vendor data: it moves to
state, `s3://opal-data-harvest/amgt/harvest/state/bloomberg_pull_log/date=2026-09-21/20260921T162530Z.json` `[OK]`.

**Record key / dedupe.** Fetch key `(security_key, request)` with a freshness window: identity once per security;
refdata and bestdata once per trading day; histdata when a new fiscal period is due; exec_officers weekly. Silver record
keys: reference `(security_key, field, as_of_date)`; model_block `(security_key, fiscal_year, mnemonic)`; price
`(security_key, date)`; estimate `(security_key, field, horizon, as_of_date)`; identity `(security_key)`; officer
`(security_key, normalised name, title)`.

**Readers that must change:** `integrations/bloomberg/research/model_block_pull.py:198,242-243,375-376,453` (writer and
its own reader); `lib/research/management/bloomberg_fallback.py:54`; `lib/research/identity/add_security.py:130`;
`lib/research/freshness/build_view.py:188`; `lib/research/coverage/run_reader.py:86` and `run_sa_reexercise.py:68,89`;
`lib/research/api/scoped_amgt.py:181` (model block) and `:2973` (freshness by key names);
`lib/research/peers/universe.py:82`; `lib/research/scores/run_scores.py:70`;
`integrations/bloomberg/research/pull_consumer.py:57` (the pack status carries raw key names); the IAM list
`infra/aws/terraform/harvest/scoped-amgt-api.tf:118-162` (`raw/`, `derived/model_block/`).

**Recommendation:** adopt as tabled. **Keep `model_block` as a Bloomberg SILVER table** (it is a typed restatement of
Bloomberg's own fields, inventory s.3 D) rather than splitting histdata into two silver tables. **Retire
`model_block_fye`** (3 objects, 0 readers). Store the response body as received, not re-dumped.

### 5.2 SEC / EDGAR

**Live:** `filings/v1/<security_key>/<accession>.source.json`, **13 EDGAR accessions**, plus **180
`UNRESOLVED-SOURCE.source.json`** markers (one per security, overwritten each run: the cause of 506 non-latest versions
on 09-18). The `.source.json` embeds a 137,314-character excerpt and `document_sha256` over the full document, **which is
stored nowhere**. Also, in code only: `lib/research/identity/build_universe.py:456-462` already builds the SEC
ticker-to-CIK cache's address with the builder.

**Proposed:**

| object | address (post-R4) | mark |
|---|---|---|
| the filing, as fetched | `s3://opal-data-harvest/sec/harvest/bronze/filing/cik=0000012927/000162828026004357/ba-20251231.htm` | [R4] |
| ticker table | `s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=2026-09-21/sec_ticker_cik_cache.json` | [R4] |
| sections | `s3://opal-data-harvest/sec/harvest/silver/filing_section/date=2026-09-21/part-20260921T000000Z.parquet` (row per accession x item) | [R4] |
| ticker rows | `.../sec/harvest/silver/company_ticker/date=.../part-*.parquet` | [R4] |
| failed attempts | `s3://opal-data-harvest/amgt/harvest/state/filing_attempt/security_key=CSL_AU_Equity/20260919T064900Z.json` | [OK] |

**Record key / dedupe.** Fetch key = **accession number** (immutable at the SEC): if any object exists under
`.../cik=<cik>/<accession>/`, never fetch it again. Silver key `(accession, item_key)`. Ticker table: one fetch per day,
skipped silently if the body hash is unchanged. A failed attempt is a new state object per attempt, never an overwrite.

**A live exposure this surfaced (not an incident):** `load_sec_cache()` reads the ticker table at the builder's
address, which today resolves to `opal-data-assets/sec/harvest/bronze/company_tickers/`, where **0 objects** exist. So a
pool-mode universe rebuild refuses loudly today unless a local override is passed (`build_universe.py:511-519`). It
refuses; it does not misread. The R4 act fixes it by construction.

**Readers that must change:** `lib/research/filings/fetch.py:61,462`; `filings/batch.py:43,138,239`;
`filings/analyze.py:1012`; `lib/research/management/roster.py:99,492-498`; `lib/research/api/scoped_amgt.py:1934`;
the IAM list (`filings/v1/`).

**Recommendation:** adopt. **Bronze retention is the one change that cannot wait for the backfill**: every filing
fetched before it lands is a filing whose parse can never be re-run.

### 5.3 Company IR and the other filing routes (non-EDGAR)

**Live:** the filings battery has five routes (`edgar-ticker`, `edgar-bloomberg-cik`, `esef-lei`, `company-site`,
`national-regulator`), read from the object's own `battery.order`. **One company-site document is live:**
`filings/v1/6861_JP_Equity/doc-1defdb68a7ffd3b7.source.json` (965,303 B; Keyence's Japanese annual securities report,
PDF from `www.keyence.co.jp`, `family: YUHO`, `language: ja`). The PDF itself is not stored.

**Proposed:**

| route | bronze (post-R4) | mark |
|---|---|---|
| company-site | `s3://opal-data-harvest/issuer-site/harvest/bronze/document/security_key=6861_JP_Equity/1defdb68a7ffd3b7/AnnualSecuritiesReport_202606_ja.pdf` | [R4] + [ROW] `issuer-site` |
| esef-lei | `s3://opal-data-harvest/filings-xbrl/harvest/bronze/filing/lei=529900T8BM49AURSDO55/<package_sha256>.zip` | [R4] + [ROW] `filings-xbrl` |
| national-regulator | same shape, one `systems.json` row per regulator, minted when a route first returns a document | [R4] + [ROW] |

Silver: `{source}/harvest/silver/filing_section/date=.../part-*.parquet`, the SAME columns as SEC's, so one gold reader
unions them.

**Record key / dedupe.** Fetch key = `sha256(canonical URL)[:16]` (the live id is 16 hex; this fixes what it hashes).
Silver key `(source, document id, item_key)`. The same bytes found at a second URL (`document_sha256` equal) are an
alias row in silver, not a second bronze object.

**Readers:** the same as 5.2.

**Recommendation:** adopt, with the two rows. The TOKENS `issuer-site` and `filings-xbrl` are this plan's proposal and
the registry lane's to fix. Classing an issuer's own site as a VENDOR row is a fit question, not a blocker: the class
exists for the `{source}` slot, as the `sec` row's own note already says for a government source.

### 5.4 Seeking Alpha (REST API)

**Live:** `raw/seekingalpha/<ROOT>_<CC>/<stamp>/{symbol,report,analysis,news,article_<id>}.json`, **18 objects**, all
dated 2026-09-11. Clean bronze: the untouched JSON:API envelope. Its folder uses `BABA_US`, not `BABA_US_Equity` (a
second security-key convention beside Bloomberg's).

**Proposed:** `s3://opal-data-harvest/seeking-alpha/harvest/bronze/symbol/security_key=BABA_US_Equity/20260911T040211Z.json`
(and `report`, `analysis`, `news`); articles by article, not by security:
`s3://opal-data-harvest/seeking-alpha/harvest/bronze/article/article_hash=<sha256>/20260915T042900Z.json`. Silver:
`symbol_profile`, `news_item`, `article`. All **[R4]**.

**Record key / dedupe.** Symbol-level fetch key `(security_key, endpoint)`, daily. Article: `article_hash =
sha256("seeking-alpha:" + article_id)`, **the same hash the browser channel's `sa` articles get** (5.5), so an article
reached by both channels is stored once.

**Readers:** `integrations/seekingalpha/rest_fetch.py` (writer; bucket from `config.json` `store_bucket`);
`lib/research/api/scoped_amgt.py:2973` (key names only); `coverage/run_reader.py:86`.

**Recommendation:** adopt; key the folder by the one minted `security_key`, not `<ROOT>_<CC>`.

### 5.5 Publications -- barrons, bbg, ft, sa, wsj (browser session on a signed-in desktop)

**Live:** `publications/v1/<publisher>/<sha256>.json`, **7 objects** (barrons 2, bbg 2, ft 1, sa 1, wsj 1; newest
2026-09-15) and `publication-links/v1/<ROOT>/<publisher>/<sha256>.json`, **7 objects**. The body object is a DERIVED
record (`body_blocks`, `text`, `words`, `body_sha256`); **the publisher's response is not kept**, only `response_sha256`.
Identity: `article_key = publisher + ":" + article_id` (`lib/opal_data_harvest/catalog.py:67`), object name =
`sha256(article_key)` (`:71`). Sample: `barrons:WP-BAR-0001888253`.

**The dedupe authority today is a SQLite file on the desktop** (`catalog.py:44-49`: `article_objects`,
`article_aliases`, `upload_outbox`). A second machine, or a rebuilt one, has no memory of what was pulled and would
pull it all again. That is the exact failure Andrew named on 09-15: *"articles have to be keyed on some kind of stable
key so we dont keep pulling the same ones."* **The stable key already exists; its memory lives in the wrong place.**

**Proposed:**

| publisher | `{source}` | bronze (post-R4) | mark |
|---|---|---|---|
| barrons | `barrons` | `s3://opal-data-harvest/barrons/harvest/bronze/article/article_hash=<sha256>/20260915T050100Z.json` | [R4] + [ROW] |
| wsj | `wsj` | `.../wsj/harvest/bronze/article/article_hash=.../<stamp>.json` | [R4] + [ROW] |
| ft | `ft` | `.../ft/harvest/bronze/article/article_hash=.../<stamp>.html` | [R4] + [ROW] |
| bbg | `bloomberg` | `.../bloomberg/harvest/bronze/article/article_hash=.../<stamp>.json` | [R4] |
| sa | `seeking-alpha` | `.../seeking-alpha/harvest/bronze/article/article_hash=.../<stamp>.json` | [R4] |

Silver per publisher: `article` (row per article: key, url, title, published, blocks, text, words, body_sha256,
bronze_key) and `search_result` (row per listing hit: query, article_key, rank, discovered_at), e.g.
`s3://opal-data-harvest/barrons/harvest/silver/article/date=2026-09-15/part-x.parquet`. The security-to-article LINK is
Opal's association, so it moves to gold: `amgt/harvest/gold/article_security_link/...` [OK].

**Record key / dedupe.** Fetch key = `article_hash` = sha256 of `publisher:article_id` -- **unchanged from today**, so
the 7 live objects keep their identity. **Before fetching a body, the harvester checks the bucket for
`.../article_hash=<h>/`; present means skip.** Before fetching at all, it compares the listing's article ids against the
silver `article` table. The desktop SQLite file becomes a cache of the bucket, never the authority. Record key in
silver: `article_key`. Canonical-URL aliases are rows in `search_result`, not a second body.

**Readers that must change:** `lib/opal_data_harvest/catalog.py:69,74` and `uploads.py:76` (writer, key form);
`lib/research/coverage/pool_reader.py:73-74`; `lib/research/metrics/chatter_axis.py` (reads bodies); the IAM list
(`publications/v1/`, `publication-links/v1/`).

**Recommendation:** adopt. **Store the publisher's response as bronze**: the body is what the page renders and the
response is what the next parser change will need. Map `bbg` and `sa` to the existing `bloomberg` and `seeking-alpha`
rows rather than minting publisher-only tokens; mint `barrons`, `wsj`, `ft`. **Retire the DynamoDB
`opal-harvest-articles` table** (0 items on 09-18, PITR on): the bucket is the index.

### 5.6 Social / chatter

**Live:** `social/v1/_measurement/<date>.json`, **1 object** (2026-09-15), a measurement summary of one Bright Data
dataset job (job id, `request_sha256`, delivery counts, a relevance sample). **The vendor's snapshot is not in the
bucket**: `lib/research/social/collect.py:452-470` writes it to a local job directory. Collection is RESERVED and OFF by
Andrew's 09-15 hold. The chatter axis (the one scheduled producer) reads publications and the universe, and writes
DynamoDB.

**Proposed:** bronze `s3://opal-data-harvest/bright-data/harvest/bronze/social_snapshot/date=2026-09-15/<request_sha256>.json`;
silver `.../bright-data/harvest/silver/social_post/date=.../part-*.parquet` (row per post). The measurement summary is
gold (`amgt/harvest/gold/social_measurement/...` [OK]). Bronze and silver **[R4]**.

**Record key / dedupe.** Fetch key = `request_sha256` (`collect.py:541`, already computed): the same request inside
the same window is not re-submitted (it is billed). Silver record key `(platform, post_id)`: a post seen in two windows
is one row.

**Readers:** `lib/research/social/collect.py:468,479-492` (writer). No served reader (the prefix is deliberately
ungranted).

**Recommendation:** adopt the format now, while collection is off, so the first live collection lands in the right
place. The format does not switch collection on.

### 5.7 Lusha

**Live:** **no Lusha object of its own.** The result is folded into each management document as `lusha_enrichment`
(status, credits used, matched count, `contact_keys_removed`), measured on
`management/v1/CSL_AU_Equity/2026-09-19.json`. The raw response is not kept, and the writer already strips contact
fields.

**Proposed:** bronze `s3://opal-data-harvest/lusha/harvest/bronze/company_contacts/date=2026-09-21/<request_sha256>.json`;
silver `.../lusha/harvest/silver/contact_match/date=.../part-*.parquet`. **[R4]**.

**Record key / dedupe.** Fetch key `(company domain, endpoint)`, never re-queried inside a window (credits). Silver key
`(domain, person id)`.

**This channel carries a call the others do not:** a byte-for-byte Lusha bronze holds personal phone numbers and email
addresses, which today's writer deliberately drops. **Recommendation: do NOT keep Lusha bronze; land silver only, with
the contact fields removed, as an R20 register entry stating the reason (personal-data minimisation) for Andrew to
acknowledge.** The alternative, keeping it, needs his word, because it creates a store of personal contact data that
does not exist today.

**Readers:** `lib/research/management/enrich.py:571-630`.

### 5.8 Bright Data SERP (the CEO public-profile step)

**Live:** no SERP object of its own; the result is folded into the management document as `ceo_profile.search` /
`triage` / `counts` / `cost`. Raw responses not kept. Every call is billed and runs only under Andrew's per-use word
(the `bright-data` row's own note).

**Proposed:** bronze `s3://opal-data-harvest/bright-data/harvest/bronze/serp/date=2026-09-21/<query_sha256>.json`;
silver `.../bright-data/harvest/silver/serp_result/date=.../part-*.parquet` (row per result). **[R4]**.

**Record key / dedupe.** Fetch key `query_sha256` = sha256 of (normalised query, engine, locale): a stored answer is
reused inside its window instead of paying again. Silver key `(query_sha256, rank)`.

**Readers:** `lib/research/management/enrich.py`; `lib/research/api/scoped_amgt.py` around `:2305-2437` (the CEO
reading). **Recommendation:** adopt; it is the cheapest channel to fix and the one where keeping the response saves
money directly.

### 5.9 The derived sets (Opal's own output -- `{source}` is `amgt`)

All gold, state and code addresses below resolve in `opal-data-harvest` **today** `[OK]`; only their FORMAT and prefix
change. Addresses verbatim from the builder, e.g.
`s3://opal-data-harvest/amgt/harvest/gold/peer_set/date=2026-09-21/peer_set_20260921T0240Z.parquet`.

| set | live today (objects) | tier / table | record key | readers that must change |
|---|---|---|---|---|
| crosswalk | `crosswalk/v1/<date>.json` (2) | gold `security_crosswalk` | `security_key` | `identity/crosswalk.py:68,688`; `scores/run_scores.py:69,84-91`; `api/scoped_amgt.py:1692`; `integrations/bloomberg/research/management_posture_batch.py:47` |
| universe | `universe/v1/<date>.json` (2) | gold `union_universe` | `(security_key, book)` | `identity/build_universe.py:449,862`; `peers/engine.py:77`; `posture/membership.py:49`; `price/generation.py:110`; `metrics/chatter_axis.py:156`; `management/enrich.py:52`; `filings/batch.py:43`; `api/scoped_amgt.py:2969` |
| identity residue | `identity/v1/...` (1, one-off, no reader) | state `coverage_residue` | run | none |
| candidate universe | `amgt/harvest/gold/candidate_universe/date=2026-08-06/candidate_universe.json` (1, **already the builder's address**) | gold, but **JSON under gold** (R11) | `(ticker, universe_id)` | `peers/universe.py:98-104` -- re-serialise to parquet |
| model block | see 5.1 | Bloomberg SILVER | -- | -- |
| filing analysis | `filings/v1/<key>/<acc>.analysis.json` (12) | gold `filing_analysis` (Claude's reading is Opal's judgment, not "what the vendor said") | `(security_key, accession, analyzer_version, prompt_version)` | `filings/analyze.py:1038,1143`; `posture/packs.py`; `api/scoped_amgt.py:1913` |
| drafting | `drafting/v1/<key>.json` (12, **overwritten**) | gold `thesis_draft` (row per sentence) | `(security_key, accession, generation)` | `filings/drafting_build.py:398`; `filings/analyze.py:1485`; `posture/packs.py:107`; `api/scoped_amgt.py:1356-1357` |
| management | `management/v1/<key>/<date>.json` (16) | gold `management_roster` (row per officer) -- it joins EDGAR, Bloomberg, Lusha and SERP | `(security_key, officer, as_of)` | `management/enrich.py:50,621`; `posture/packs.py:109`; `api/scoped_amgt.py:166,2305` |
| management pool | `management/v1/_pool/<date>.json` (2) | gold `management_pool` | `as_of` | `management/enrich.py:576,630`; `posture/packs.py:112` |
| peers | `peers/v1/<key>/<date or stamp>.json` (797, **two shapes**) | gold `peer_set` (row per subject x member) | `(subject_key, generation, member_key)` | `peers/engine.py:76,1143`; `posture/comparable.py:39`; `scores/run_scores.py:71`; `posture/packs.py:114`; `posture/judge.py:437`; `api/scoped_amgt.py:165,1244` |
| posture | `posture/v1/<key>/<date>.json` (33, **31 overwritten in place**) | gold `posture_verdict` | `(security_key, generation)` | `posture/judge.py:69,290`; `api/scoped_amgt.py:168,2437` |
| scores | `scores/v1/...` (66: 33 canonical + 31 orphans) | gold `security_score` | `(security_key, generation)` | `scores/run_scores.py:72,231`; `api/scoped_amgt.py:174,2374` |
| packs ledger | `packs/<key>/input_ledger.json` (39, read-modify-write) | state `input_ledger`, one object per entry | `(security_key, stamp)` | `ledger/ledger.py:70,87`; `api/scoped_amgt.py:2894,2972`; `freshness/build_view.py:194` |
| pack status | `packs/<key>/status.json` (1) | state `pull_request/request_id=<id>/status.json` | `request_id` | `pull_consumer.py:57`; `api/scoped_amgt.py:2837` |
| pack template | `packs/_template/` (0; cited by code) | code or retire | -- | `print/render_pack.py:71-73` |
| security metrics | DynamoDB `opal-harvest-security-metrics` | not an S3 key; stays the serving store, fed from a gold `security_metric` table | `(axis, date, generation, ticker)` | out of this plan's key scope |
| release artifact | `lib/local-publications/...` (6, source code) | code: `s3://opal-data-harvest/amgt/harvest/code/bronze/local-publications-0.1.0/local-publications-0.1.0.zip` | version | `lib/opal_data_harvest/build_release.py:65` and the installer |
| page payload | none (the API serves gold/silver JSON directly) | platinum: `s3://opal-data-harvest/amgt/harvest/platinum/security_analysis/security_key=<k>/security-analysis.json` **[R4]** (graded CONFORMANT; the leaf is kebab, the table snake) | `(security_key, generation)` | `api/scoped_amgt.py` reads this instead of gold |

**Two reclassifications from the 09-18 plan, argued:** the crosswalk and universe were called silver there. R10 says a
silver partition answers *"what did the vendor say," never "what does Opal care about"*, and both are filtered to Opal's
coverage and carry Opal's resolution decisions, so they are gold. Filing analysis moves to gold for the same reason.

**The cost of gold-as-parquet, stated:** `infra/aws/terraform/harvest/` names no parquet library (0 hits for
`pyarrow`, `pandas`, `parquet`), so the API Lambda cannot read parquet today. **Recommend a platinum publisher** (R12:
reads parquet, writes one JSON per security), so the API stays JSON-only. This is why gold and platinum are the LAST
step, after the backfill, not a precondition of it.

---

## 6. Readers, consolidated

- **One IAM list moves with every prefix:** `infra/aws/terraform/harvest/scoped-amgt-api.tf:118-162`. Its entries were
  each landed under a never-widen co-sign; **replacing them is an IAM grant change and carries the same CTO+COO
  sign-off**, on the new prefixes, before any reader switches.
- **One API module holds most of the served reads:** `lib/research/api/scoped_amgt.py`, whose prefix constants sit at
  `:165`, `:166`, `:168`, `:174`, `:181`, `:1357`, `:1692`, `:1934`, `:2969`, `:2972`, `:2973` (11 constants, read
  from the file) plus the read functions they feed.
- **Two builder callers are already correct** and need only the R4 act: `build_universe.py:456-462` (SEC table) and
  `peers/universe.py:98-104` (candidate universe; format still owed).
- **Tests carry the old keys as literals** (`lib/research/**/tests/*`); they move with their modules.
- **Off-repo:** the local publication harvester's `config.json` names a worker deliverables file as its live
  `universe_source` (inventory H-12); it must read gold `union_universe` instead.

---

## 7. Order of the move

**Corrected 2026-09-21 ~17:5xZ** (PRD v0.15 `C-FORMAT-SEQUENCE`, which binds): this section first carried the 09-18
plan's order -- writers dual-write for one cycle, readers fall back, the old prefixes stay until a census reads zero.
**That leaves the old path serving beside the new one, a standing duplicate output path the shadow-pipeline veto
forbids.** The order is instead: registry first; then per served prefix, ONE move under its own never-widen pair in
which the objects are copied with their vintage, the readers switch, and the source path retires, all in the SAME
window, with same-window rollback. Two additions:

1. **The backfill's gate is bronze + silver only:** the R4 act, the five rows, the bronze writers for 5.1-5.8, the
   silver writers with their record keys, and the fetch-key check against the bucket. Gold and platinum can be rebuilt
   from silver afterwards, so they do not hold the backfill.
2. **Nothing existing is re-fetched to fill bronze.** The 1,461 live objects are copied to their new addresses with
   their vintage. The only bronze that does not exist -- the 13 EDGAR documents, 1 IR document and 7 publisher
   responses -- is filled by the backfill's own first fetch under its fetch key (INFERRED, not tested: that the
   sources still serve those documents). A copy is never a re-derivation.

---

## 8. The calls, each reduced to a recommendation

| # | call | owner | recommendation |
|---|---|---|---|
| 1 | Form of the R4 act | laptop `4.0.0_SA_CRO` lane, under Andrew's option (ii) | **A new tenancy, six cells `home: scope`, `harvest` moved onto it.** Never edit PRODUCT (it re-homes etfs and mdpf). The doctrine line quotes his *"client/partner custodial"* words. |
| 2 | Five `systems.json` VENDOR rows | the registry lane (landed the last four under Andrew's override; `1.0.0_SA_CTO~Z` on SITEZ) | **Add `barrons`, `wsj`, `ft`, `filings-xbrl`, `issuer-site`.** Map `bbg` to `bloomberg` and `sa` to `seeking-alpha`. |
| 3 | Bronze form | `1.0.0_SA_CTO~Z` at L4 | **Entity partition + compact UTC stamp leaf, bytes as received, one object per fetch.** |
| 4 | Silver form | `1.0.0_SA_CTO~Z` at L4 | **Parquet, `date=` fetch partitions, one part per run, record keys as in s.5.** |
| 5 | Dedupe authority for articles | `1.0.0_SA_CTO~Z` at L4 | **The bucket, not the desktop SQLite file.** Keep today's `article_hash`. Retire `opal-harvest-articles`. |
| 6 | Lusha bronze | Andrew | **Do not keep it; silver without contact fields, as an R20 entry he acknowledges.** |
| 7 | Security key | `1.0.0_SA_CTO~Z` at L4 | **One slash-safe form minted in the crosswalk; an entity id never goes in `object`.** |
| 8 | Gold and platinum | `1.0.0_SA_CTO~Z` at L4 | **Parquet gold, a JSON platinum publisher the API reads, sequenced AFTER the backfill.** |
| 9 | Placement | `1.0.0_SA_CTO~Z` routes, `2.0.0_SA_COO~Z` cuts | **Its own chain, not a rider on a round-19 cell** (Rule 30 R19). |

---

## 9. What this plan does not claim

- It wrote nothing: no S3 object, no registry row, no doctrine line, no code. The simulation wrote only
  `scratchpad/fmt/registry_sim/`.
- It did not run any vendor call. Every shape is read from an object already in the bucket.
- The freshness windows in 5.1 are recommendations, not measured needs; the L4 fixes them.
- Tokens (`issuer-site`, `filings-xbrl`, `PRODUCT-CONTAINED`) and table names are proposals. The builder accepts them
  and the grader reads them CONFORMANT; the names are the registry lane's and the L4's to fix.
- **The grader is not a format check:** it reads `candidate_universe.json` under `gold/` CONFORMANT although R11 says
  JSON leaves gold. A CONFORMANT grade in this document certifies the KEY, never the bytes.
- Whether AMGT data is "general" in the canon's sense is not argued here: Andrew ruled where it lives and what
  `opal-data-assets` is for.
