# A. Publications and ticker-specific news: field-level channel map

Scope: Barron's, WSJ, FT, Bloomberg news articles and Seeking Alpha articles/news landed by the
signed-in-browser publications harvester (`lib/opal_data_harvest`). Also covered: the legacy
served folders `publications/v1/` and `publication-links/v1/`, the new-grammar
`{src}/harvest/{bronze,silver}/article/`, the chatter-axis Lambda feeding DynamoDB
`opal-harvest-security-metrics`, and every page surface that reads news.

Vintage: all S3 and DynamoDB reads were taken 2026-09-22 ~09:05 local through `.tools/aws`, and
the code was read at the working tree on SITEZ @78106b9cea. Sample objects were streamed to the
scratch dir `fieldmap/pubs/` and never into the repo.

Prior inventories I relied on and re-verified:
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESAPP_DATA_SHAPE_INVENTORY_20260918.md`, rows 18/19 at `:52-53` and shapes at `:303-315`.
- `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` s.5.5 `:282-330`.

**Two corrections to those inventories:**
- The 09-18 inventory labels the records `record_type: "publication_body"` and `"publication_link"` (`:305`, `:314`). The live objects and the schemas carry **`publication_article`** and **`security_article`**. Both schemas refuse unknown values: `lib/opal_data_harvest/article.schema.json:9`, `security-article.schema.json:9`.
- The 09-21 plan (`:299-303`) assumes that all five publishers get a bronze article object, FT as `.html`. The code writes bronze **only for SA and Bloomberg** (hazard H1 below).

---

## 1. Channel

| Item | Value |
|---|---|
| Vendor(s) | Seeking Alpha (`sa`), Financial Times (`ft`), Wall Street Journal (`wsj`), Bloomberg.com news (`bbg`), Barron's (`barrons`). Publisher enum: `article.schema.json:11`. |
| Mechanism | Signed-in subscriber sessions. A headful browser harvests cookies once, and Windows DPAPI encrypts them locally. Collection is then paced HTTP/JSON under those cookies (`lib/opal_data_harvest/README.md:32-53`, `publishers.py:125-149`). Credentials and sessions are Secrets Manager references in `contracts.json:14-101`. No values are quoted here. |
| Entry point | `python -m lib.opal_data_harvest run [--new-only] [--all-securities] [--tickers ...]` (`__main__.py:38-91`). Wrapper: `run-local.ps1:1-15`, which always passes `--new-only` and uploads only when `-UploadLimit` > 0. Core loop: `worker.py:87-218` (`Worker.run_job`). |
| Order per security | sa, ft, wsj, bbg, barrons (`contracts.json:6-12`). Up to 5 accepted articles per publisher job (`config.json:5`) out of 20 candidates (`config.json:6`), 15 s + jitter 10 s between requests (`config.json:8-9`). |
| Security universe | Default: 5 pilots BA, COST, HD, HAL, VLO (`config.json:14-20`). `--all-securities` = the 89-name universe (`__main__.py:12-35`). |
| Trigger / cadence today | **None.** The Windows task "Opal Data Harvest - Local Publications" exists with **State = Disabled** and no triggers (measured with `Get-ScheduledTask`). `config.json:10-12` sets `recurring_schedule_enabled: false` and `automatic_uploads_enabled: false`. The cadence is reserved to Andrew (PRD `C-ONE-STORE` `:635-636`; BACKFILL_SCOPE_PROPOSAL row 11 `:60`). |
| Upload | Manual: `python -m lib.opal_data_harvest upload --max-objects N` -> `uploads.Uploader` (`__main__.py:81-85`, `uploads.py:17-100`). It writes **legacy keys only** (`uploads.py:56-57` refuses any other prefix). |
| New-grammar path | `uploads.HarvestUploader` (`uploads.py:103-162`) plus `harvest_grammar.put_article_bronze` (`harvest_grammar.py:70-81`). It is **not wired to the CLI**: `__main__` builds `Worker(root, config)` without `harvest_client` (`:74`), `config.json` has no `harvest_grammar` key (so the default is False, `worker.py:142,157`), and the `upload` command calls only `Uploader` (`:82`). The local `progress.sqlite3` has **no `harvest_raw_outbox` table**, so harvest mode has never run on this box. |

### What "ticker-specific news" means, per source

No publisher is queried by ticker except SA. Discovery is a **company-name search**. An item is
linked to a security only if the company name, or an alias, appears **anywhere in the title or
body** as a word-bounded, case-insensitive match (`publishers.py:99-105`). Search ranking alone is
never enough.

| Publisher | Discovery call (what "about this security" means) | Body source | Cite |
|---|---|---|---|
| sa | `/api/v3/symbols/{sa_symbol}/news?...include=author,primaryTickers,sentiments`. This is the only **symbol-keyed** listing. The body is embedded in the listing (`attributes.content`, HTML). It needs a resolved `sa_symbol`, else `ContractUnavailable`. | `data[].attributes.content` -> BeautifulSoup `p,li,h2,h3,blockquote,table` | `publishers.py:197-221`, `contracts.json:24-25` |
| bbg | `nemo-next/api/search/query?query="<company>"` (quoted, up to 3 pages); `subtype == "Article"` only | `article/api/story/id/{resourceId}?languagePreference=en` -> `story.body.content` typed blocks | `publishers.py:223-253`, `contracts.json:73-75` |
| ft | `ft.com/search?q=<company>`, `.o-teaser__heading a[href*="/content/"]` | JSON-LD `NewsArticle.articleBody` and `wordCount`; last resort is HTML | `publishers.py:255-281` |
| wsj | `wsj.com/search?query=<company>` -> `__NEXT_DATA__...searchResults[].articleUrl`; slugs ending in 8 hex characters, same host | `__NEXT_DATA__.props.pageProps.articleData.flattenedBody` | `publishers.py:321-341, 354-365` |
| barrons | `barrons.com/search?query=<company>` -> `searchData.articles[]` with `type=="article"`; 8-hex slug, same host | `/articles/api/articles/{slug}` -> `body` or `articleData.body` or `snippet` | `publishers.py:328-353` |

**Measured consequence:** in 4 of the 5 live bodies I sampled, the linked company appears
**exactly once, in the body, and not in the title**. Examples:
- `HD` is linked to a Bloomberg "YouTube Inks Amazon Partnership" story.
- `HD` is linked to a Barron's Williams-Sonoma tariff story.
- `HD` is linked to an SA "Earnings Scoreboard: All 12 key S&P 500..." roundup.
- `COST` is linked to an FT macro piece.

Only WSJ/BA was about the company (28 mentions, name in title). So "ticker-specific" today means
"mentions the company name at least once." The chatter score counts these mentions as signal.

---

## 2. Storage (live counts, 2026-09-22)

| # | Layer | Key pattern | Live objects | Writer |
|---|---|---|---|---|
| L0 | Local runtime (SITEZ desktop only) | `.runtime/opal-data-harvest/publications/v1/...` plus `progress.sqlite3` | `article_objects`: barrons 15, bbg 19, ft 14, sa 20, wsj 15 = **83 bodies**. `article_links`: **84** over **3** keys (BA 34, COST 25, HD 25). `upload_outbox`: **167 pending, 0 uploaded**. | `catalog.py:61-83` |
| L1 | Legacy served body | `s3://opal-data-harvest/publications/v1/{publisher}/{sha256(article_key)}.json` | **7** (barrons 2, bbg 2, ft 1, sa 1, wsj 1; newest 2026-09-15 01:01) | `uploads.py:76-78` (key `catalog.py:69`) |
| L2 | Legacy served link | `publication-links/v1/{harvester security_key}/{publisher}/{sha256(article_key)}.json` | **7** (BA 2, COST 2, HD 3) | `uploads.py:76-78` (key `catalog.py:74`) |
| L3 | New-grammar bronze | `{barrons,wsj,ft,bloomberg,seeking-alpha}/harvest/bronze/article/article_hash=<sha256(pub:id)>/<stamp>.<ext>` | barrons 0, wsj 0, ft 0, **bloomberg/article 0**. **seeking-alpha/article 6**, all stamped 20260911T04xxZ and landed 2026-09-22 00:54. These 6 come from the **SA REST channel's** migration, not from this harvester (see L3 notes). | `harvest_grammar.py:70-81` |
| L4 | New-grammar silver | `{src}/harvest/silver/article/` (parquet via `store.silver_append`, `uploads.py:139-141`) | **0** for all five publishers | `uploads.HarvestUploader` (unwired) |
| L5 | Gold link (planned) | `amgt/harvest/gold/article_security_link/...` (plan `:307-308`) | not built | none |
| L6 | DynamoDB `opal-harvest-security-metrics` | `axis_date` = `{TRENDING,BREAKOUT}_CHATTER#<date>#<generation_id>` (HASH), `ticker` (RANGE), GSI `axis-rank-index` on `rank_sort`; pointer item `ticker="_CURRENT"` at `<AXIS>#<date>` | Daily. 2026-09-22: TRENDING **2 rows COMPLETE**; BREAKOUT **0 rows EMPTY** (`NO_SIGNAL_IN_WINDOW` 189 of 191) | `lib/research/metrics/chatter_axis.py` in Lambda `amgt-resapp-chatter-axis` |
| (retired) | DynamoDB `opal-harvest-articles` | none | 0 items per the 09-18 inventory `:59`. No writer, no reader. | none |

Notes on L3:
- The 6 SA bronze `article_hash` values use `sha256("sa:" + id)`. Measured: `sa:4944152` -> `f6be7eef...a13d` matches the object key. So both channels share one hash rule (`harvest_grammar.py:46-52`). The plan's `"seeking-alpha:"` prefix (`:274`) is not what the code or the data use.
- The other `bloomberg/harvest/bronze/*` (110 objects: bestdata 6, exec_officers 4, histdata 48, histdata_daily_px 1, identity 3, refdata 48) are **Terminal data**, not news, and are out of this scope.

---

## 3. Field dictionary

### 3.1 Bronze: vendor payload as received (new grammar)

**Only SA and Bloomberg can ever produce bronze.** In `normalize()`, `raw_bytes` is passed only by
the SA path (`publishers.py:217-221`) and the Bloomberg path (`:244-249`). FT (`:272-273`,
`:278-281`) and Dow Jones/WSJ/Barron's (`:371-374`) pass `raw_hash` only. `worker.py:157` writes
bronze only `if article.get("raw_bytes")`.

**SA `fullArticle` envelope.** Measured on
`seeking-alpha/harvest/bronze/article/article_hash=f6be.../20260911T040224Z.json` (8,496 B). The
browser harvester's SA bronze would instead be ONE listing item, `json.dumps(item)` (`publishers.py:217`).

| Field | Type | Shape | Meaning |
|---|---|---|---|
| `data.id` | str | `"4944152"` | SA article id -> `article_id` |
| `data.type` | str | `"fullArticle"` / `"news"` | item class |
| `data.attributes.title`, `.originalTitle` | str | headline | -> `title` |
| `data.attributes.publishOn` | str | `"2026-09-09T02:01:31-04:00"` | -> `published` (offset kept) |
| `data.attributes.lastModified` | str | ISO with offset | dropped |
| `data.attributes.content` | str(HTML) | `<p ...>` | -> `body_blocks` / `text` |
| `data.attributes.summary` | list[str] | 4 bullets | dropped |
| `data.attributes.isPaywalled`, `.isLockedPro`, `.isMpwLocked` | bool | `false` / `false` / `true` | **paywall flags. Dropped. The SA path hard-codes `unlocked=True`** (the `normalize` default, `publishers.py:77`) |
| `data.attributes.locale` | str | `"en"` | **language. Dropped** |
| `data.attributes.availableTranslations` | list[str] | 7 locales (`"de"`, ...) | dropped |
| `data.attributes.translationDisclosure` | str / null | null | dropped |
| `data.attributes.disclosure` | str(HTML) | analyst disclosure | dropped |
| `data.attributes.themes` | obj | `{slug: {id, title, kind, path}}` | dropped |
| `data.attributes.closestTradingDate`, `.beforeOpeningHours` | str, bool | `"2026-09-09"`, `true` | dropped |
| `data.attributes.isNoarchive` / `.isNoindex` | bool | `true` / `false` | licensing-adjacent robots flags. Dropped |
| `data.attributes.commentCount`, `.likesCount` | int | 2, 0 | discussion counts. Dropped (the header says "most-discussed: not measured") |
| `data.relationships.primaryTickers.data[]` | list[{id, type:"tag"}] | `[{"id":"137271","type":"tag"}]` | **vendor ticker tags, as SA tag ids (not symbols). Dropped** |
| `data.relationships.secondaryTickers`, `.sentiments`, `.otherTags`, `.author`, `.coAuthors` | obj | `{data: [...]}` | dropped |
| `data.links.self` / `.canonical` | str | `/article/4944152-...` | `self` -> `url` via `urljoin` (`publishers.py:218`) |
| `included[]` | list[obj] | `author` / `newsAuthorUser` records | **personal names. Not quoted.** Dropped |
| `meta.page.{title,description,robots_meta_tag}` | obj | `"noarchive, max-image-preview:large"` | dropped |

The SA `news` listing (`.../bronze/news/security_key=BA_US_Equity/20260911T040304Z.json`, SA REST
channel) has item attribute keys `commentCount, content, gettyImageUrl, isLockedPro, isPaywalled,
publishOn, themes, title, videoDuration, videoPreviewUrl`, relationships `author, sentiments,
primaryTickers, secondaryTickers, otherTags`, and `meta.page.total = 5061`. There is **no `locale`
on news items**.

**Bloomberg story (no bronze object exists).** The shape is read from the code, not the data:
- `story.id` -> `article_id`
- `story.headline` -> `title`
- `story.publishedAt` -> `published`
- `story.url` -> `url`
- `story.body.content[]` typed blocks -> `body_blocks`
- `story.isPreview` -> `unlocked = not isPreview`

Source: `publishers.py:243-249`. The fetch pins `languagePreference=en` (`contracts.json:74`). Every
other story field is UNKNOWN because no bronze has landed.

**FT / WSJ / Barron's.** These are never persisted as bronze (H1). The flags read in flight and then
dropped are:
- WSJ: `isServerUnlockedContent`, `articleData.meta.metrics.wordCount`, `articleData.id`, `canonicalUrl`, `publishedDateTimeUtc` (`publishers.py:360-373`).
- Barron's: `isSubscriber`, `isServerUnlockedArticle`, `articleData.articleTrackingMeta.articleWordCount` (`:350-353`).
- FT: JSON-LD `headline`, `datePublished`, `wordCount` (`:269-273`).

### 3.2 Legacy served body `publications/v1/{publisher}/{digest}.json`: `publication_article` v1

Schema: `article.schema.json:6-24`, which forbids additional properties. Extra rules in
`catalog.py:26-38`. The shapes below were measured on all 7 live bodies.

| Field | Type | Null? | Shape | Meaning |
|---|---|---|---|---|
| `schema_version` | int const 1 | no | `1` | |
| `record_type` | const | no | `"publication_article"` | |
| `article_key` | str | no | `"barrons:WP-BAR-0001888253"`, `"sa:4635742"`, `"wsj:096c2a41-...-7dc3b710dc56"`, `"bbg:TKNDM8T96OSI00"`, `"ft:0894ec54b086fefb99c57b69"` | `publisher + ":" + article_id`, the stable global identity |
| `publisher` | enum | no | `sa, ft, wsj, bbg, barrons` | **source** |
| `article_id` | str | no | native id; if none, `sha256(url)[:24]` (`publishers.py:111`) | FT uses the fallback: a 24-hex value, not the FT uuid |
| `url` | str https | no | canonicalized: lower scheme and host, no query or fragment (`catalog.py:21-23`) | article link |
| `title` | str | no | headline | |
| `published` | str date-time | no | `"2026-08-26T15:59:00Z"`, `"2026-09-01T11:00:00.002Z"`, `"2026-08-22T09:35:27-04:00"` (mixed offsets) | publication clock, the ONLY day-bucketing field (`pool_reader.py:429-439`) |
| `fetched_at` | str date-time | no | `"2026-09-15T04:52:04.504380+00:00"` | retrieval clock |
| `body_blocks` | list[str] >= 3 | no | 12-27 blocks | ordered paragraphs, zero-width characters stripped |
| `text` | str | no | `"\n\n".join(body_blocks)`, 2,083-5,452 chars in the sample | **full body, not an excerpt** |
| `words` | int >= 120 | no | 337-877 | whitespace token count of `text` |
| `expected_words` | int / null | yes | 347 (barrons), 896 (ft), 851 (wsj); null for sa and bbg | publisher word count; must be >= 80% (`catalog.py:35-36`) |
| `body_sha256` | hex64 | no | | sha256 of `text` |
| `response_sha256` | hex64 / null | yes | | sha256 of the raw response. **The raw bytes themselves are not stored** (inventory 09-18 `:676`) |
| `transport` | enum | no | `json`, `http_jsonld`, `http_embedded_json`, `http_html_last_resort` | how the body was obtained |
| `content_status` | const | no | `"complete_candidate"` | all automatic checks passed (`publishers.py:84-107`) |

**Absent by design:** `language`/`locale`, any ticker/tag list, `author`, `summary`/excerpt,
paywall or licence flags, `section`, and a vendor sentiment field. `issues` and `review_status`
exist on the in-flight dict (`publishers.py:115-116`) but are **not persisted**, because
`catalog.store` copies only `ARTICLE_FIELDS` (`catalog.py:14-15, 64`).

### 3.3 Legacy served link `publication-links/v1/{security_key}/{publisher}/{digest}.json`: `security_article` v1

Schema: `security-article.schema.json:6-16`. Written once, and never rewritten if it already exists
(`catalog.py:74-80`). Measured on `publication-links/v1/HD/sa/5666...a882.json` (245 B).

| Field | Type | Null? | Shape | Meaning |
|---|---|---|---|---|
| `schema_version` | const 1 | no | `1` | |
| `record_type` | const | no | `"security_article"` | |
| `security_key` | str `^[A-Za-z0-9_.-]+$` | no | `"HD"` (pilot) or `"security-<16 hex>"` (non-pilot) | **the HARVESTER's key, not the page's canonical `HD_US_Equity`** |
| `company` | str | no | `"Home Depot"` | the name that was searched and matched |
| `ticker` | str / null | yes | `"HD"` (pilot); a Bloomberg ticker value for non-pilots (`__main__.py:30`) | display only |
| `article_key` | str | no | `"sa:4635742"` | join to the body |
| `publisher` | enum | no | `"sa"` | |
| `first_discovered_at` | date-time | no | `"2026-09-15T04:24:27.415631+00:00"` | association clock |

**How an article is linked to a security:**
1. The worker runs one job per (security, publisher) (`worker.py:87-165`).
2. Every accepted article is stored ONCE as a body.
3. That job's security gets a link row. The same body can carry many links, one per security whose job found it (`catalog.py:61-83`).
4. The link inherits no score or confidence. Relevance is the binary name-mention test.

### 3.4 New-grammar silver `{src}/harvest/silver/article/` (designed, 0 rows)

Per `harvest_grammar.article_silver_row` (`:100-107`), each row is the 18-field
`publication_article` record, with `fetched_at` cast to a tz-aware datetime, plus `bronze_key`.
`store.silver_append` adds `record_hash` and keys on `("article_key",)` (`uploads.py:139-141`).

The SA `news_item` and `symbol_profile` silver rows (`harvest_grammar.py:121-146`) belong to the
SA REST channel. They keep every `attributes` field, so `isPaywalled` and `publishOn` would survive
there. The relationships (ticker tags) are **not** flattened into them.

### 3.5 DynamoDB `opal-harvest-security-metrics`: chatter generation row

Measured on `TRENDING_CHATTER#2026-09-22#20260922T100027Z-d09ee37a8f3b`. The builder is
`chatter_axis.py:472-522`.

| Field | Type | Shape | Meaning |
|---|---|---|---|
| `axis_date` | S (HASH) | `"TRENDING_CHATTER#2026-09-22#<gen>"` | partition = axis + date + generation |
| `ticker` | S (RANGE) | `"BA US"` | Bloomberg form from the crosswalk |
| `rank_sort` | S (GSI range) | `"00001"` | zero-padded rank |
| `security_key` | S / null | `"BA_US_Equity"` | canonical id; null when UNRESOLVED |
| `identity_status` | S | `"MEASURED"` | |
| `axis` / `movement` / `subject` | S | `TRENDING_CHATTER` / `TRENDING` / `CHATTER` | |
| `movement_basis` / `movement_measure` | S | `MEASURED` / `ABSOLUTE_COUNT_ON_AS_OF_DAY` | from `movement_gate.py` |
| `rank` | N | 1..10 | |
| `score` | N | 0-100 | min-max normalized (`:411-438`) |
| `raw_chatter_count` | N | 0 | article count ON the as-of day |
| `window_total_count` | N | 1, 2 | article count over the 30-day window |
| `movement_raw_score` | N | 0 | pre-normalization score |
| `window_days` | N | 30 | `chatter_gate.py:45` |
| `as_of_date`, `computed_at`, `generation_id` | S | | |

The pointer item (`ticker="_CURRENT"`) carries `generation_id, run_id, coverage_vintage,
payload_hash, row_count, state (COMPLETE/EMPTY/FAILED), written_at, record_type,
empty_reason{reason,count,denominator}`. Measured `coverage_vintage` =
`pool:universe/v1/2026-09-16.json#as_of=2026-09-16`.

---

## 4. Transformations

1. **Vendor payload -> in-flight article** (`publishers.normalize`, `:76-122`):
   - Strips zero-width characters.
   - Joins blocks with `"\n\n"`.
   - Counts words.
   - Rejects the article on any of: `publisher_did_not_unlock_body`, `short_or_partial_body` (<120 words or <3 blocks), `missing_metadata`, `invalid_publication_date`, `publisher_word_count_mismatch` (<80%), `markup_or_code`, `company_not_mentioned`, `generated_summary` (a title containing "earnings call insights").
   - Sets `content_status`.
   - HTML is turned into text with BeautifulSoup for SA and the FT last-resort path. Typed JSON blocks go through `typed_blocks` for bbg, wsj and barrons.
   - **No model call anywhere in this chain.**
2. **In-flight -> `publication_article`** (`catalog.store`, `:61-83`):
   - Keeps the 14 `ARTICLE_FIELDS` and adds `schema_version`, `record_type`, `article_key`.
   - **Drops** `security_key`, `ticker`, `company`, `issues`, `review_status`, `raw_bytes`, `raw_ext`.
   - Canonicalizes `url`.
   - Moves the security fields into the separate link record.
3. **Dedupe:**
   - In-job: by `article_id` and `body_sha256` (`worker.py:139-141`).
   - Cross-job: by the local SQLite `article_objects` / `article_aliases` (`catalog.py:99-109`). The **desktop SQLite file is the dedupe authority** (plan 09-21 `:290-292`).
   - Harvest mode would add a bucket check (`worker.py:142-146`), but it is unwired.
4. **Pool -> served feed item** (`pool_reader.window_read`, `:461-550`):
   - Link + body -> `{publisher, published_at(=published), article_key, url, title, published_date(UTC), fetched_at, first_discovered_at, security_key, key_form, words, body_sha256, content_status}`.
   - **`text` and `body_blocks` are NOT carried to the page.**
   - Dedupe on `article_key` within one identity.
   - Sort newest-first.
5. **Pool -> chatter score** (`chatter_axis.compute_chatter_axis`, `:538-667`):
   - Builds a per-day article histogram over a 30-day window for each universe identity.
   - Drops names with a zero window total (`NO_SIGNAL_IN_WINDOW`).
   - Scores TRENDING = count on the as-of day and BREAKOUT = % jump vs the baseline (`movement_gate.py`).
   - Min-max normalizes to 0-100, takes TOP_N=10 and writes a generation plus pointer.
   - It is a **pure count. No sentiment and no model.**

---

## 5. Component map

Every route below is served by `lib/research/api/scoped_amgt.py` (route table `:3991-4011`) and
called from `portal/src/api/endpoints/amgt-lead-panel.ts`.

| Component | Fields read | Server side | Portal side |
|---|---|---|---|
| **Lead Panel: ranked list (Trending/Breakout x Chatter)** | DynamoDB generation rows: `rank`, `score`, `raw_chatter_count`, `ticker`, `security_key`, `axis`; pointer: `generation_id`, `coverage_vintage`, `payload_hash`, `state`, `row_count` | `read_rankings` `scoped_amgt.py:574-638` (`GET /lead-panel/rankings/{movement}/{subject}`) | `amgt-lead-panel.ts:63-69`; `hooks/useLeadPanelApi.ts:47`; `components/RankedList.tsx:103-113` (`chatter {score}/100 ({raw_chatter_count} mentions)`); `GenerationCaption.tsx:40` |
| **Lead Panel: Security overlay chatter tile** | the TRENDING_CHATTER point row: `rank`, `score` | `read_security_overlay` `:1870-1951` (`chatter` = `:1947`) via `read_point_record` `:646` | `components/SecurityOverlay.tsx:120-131` |
| **Lead Panel / page header: news feed** ("News -- newest first") | feed `items[]`: `title`, `url`, `publisher`, `published_at`, `article_key`; plus `coverage_status`, `store_item_count`, `window`, `reason`, `social.status` | `read_feed` `:3021-3048` <- `read_coverage_set` `:2193-2304` <- `pool_reader.coverage_items`. Travels on the overlay payload (`:1944`). | `components/HeaderBrief.tsx:84-110`, `:131` |
| Coverage route (retired tab) | same block as the feed | `GET /security/{k}/coverage` `:3873-3874` | client `amgt-lead-panel.ts:144`; hook `useLeadPanelApi.ts:135-138`. **No page component calls `useCoverageSet`**; only the harnesses mock it. |
| **Thesis** | **NONE** from publications | `read_thesis_bundle` `:1984-2043` reads `drafting/v1/<key>.json`. The live BA drafting object is filing-sourced (`accession`/`form` keys) with **0 evidence records**. No code path from `publications/v1` or the silver articles into drafting (Grep of `lib/research` for `publications/v1`, `pool_reader`: only `pool_reader.py`, `scoped_amgt.py`, `chatter_axis.py`, `crosswalk.py`, `build_universe.py`). `drafting/producer.py:53-63` could draft from coverage-item titles, but it is a fixture producer and is not fed by the pool. | none |
| **Exec Mgmt** | NONE | none | none |
| **Peers** | NONE | none | none |
| **Model** | NONE | none | none |

The page never receives article `text`, `body_blocks`, `words` or `expected_words`. The feed shows
headline + link + publisher + timestamp only.

---

## 6. Gaps and hazards

**H1. The new grammar cannot land FT, WSJ or Barron's bronze, and even SA/Bloomberg is unwired.**
- `raw_bytes` is set only on the SA and Bloomberg paths (`publishers.py:217-221, 244-249`).
- `HarvestUploader` is not reachable from the CLI (`__main__.py:74, 81-85`), and there is no `harvest_grammar` config key.
- Live: 0 publisher-article bronze and 0 silver for all five. The chatter Lambda IAM already grants `{barrons,wsj,ft,seeking-alpha}/harvest/silver/` (`chatter-axis-schedule.tf:67-70`), but **not `bloomberg/harvest/silver/`**, and `pool_reader` reads **only** `publications/v1` + `publication-links/v1` (`pool_reader.py:73-74`). So even once silver lands, nothing on the page reads it.

**H2. Keying: the link carries the harvester key, not the canonical key.**
- The link `security_key` is `BA`/`COST`/`HD` (pilots, `config.json:15-19`) or `security-<sha256(folder)[:16]>` (`__main__.py:29`).
- It is bridged to `BA_US_Equity` only by the crosswalk's `association_keys` (`crosswalk.py:114-133, 437, 569, 888-894`).
- A name the crosswalk does not map reads NEVER_HELD/IDENTITY-ONLY, not an error.
- No composite FIGI anywhere on this channel. Since today's Andrew-direct (@6f1a72e4be) adopts composite FIGI for research, the link key and the crosswalk will need a FIGI association form.
- **The dedupe authority is a desktop SQLite file** (plan 09-21 `:290-292`), so a second machine would re-pull everything.

**H3. Relevance is weak.** A single case-insensitive name mention anywhere in the body links the
article (`publishers.py:99-105`). 4 of 5 sampled links are incidental mentions (s.1). The chatter
axis counts them as full signal, and the header shows them as the company's news.

**H4. Chatter signal is effectively zero, and the rows have gone static.**
- The 2026-09-21 and 09-22 TRENDING generations have the **identical `payload_hash`** `d09ee37a...` and 2 rows (BA_US_Equity window 1, HD_US_Equity window 2), both `score 0`, `raw_chatter_count 0`.
- BREAKOUT is EMPTY: 189 of 191 names have no signal.
- The pool has held only 7 links since 2026-09-15, so as the 30-day window slides past 2026-08-22..09-03, TRENDING will go EMPTY with no new uploads.
- The Lambda comment still claims "~34 tickers" and a DynamoDB articles GSI (`chatter-axis-schedule.tf:142-153`). That is stale prose; the code reads the pool.
- The universe vintage is frozen at `universe/v1/2026-09-16.json`.

**H5. Upload state is inconsistent.** Locally there are 83 bodies and 84 links with 167 outbox rows
`pending` and **0 `uploaded`**, while S3 holds 7 + 7 dated 2026-09-15. Either the uploads ran from
another runtime root or the outbox was rebuilt. UNKNOWN which. So ~76 validated local bodies and
~77 links have never reached the pool.

**H6. Non-English articles.**
- Discovery searches the **English company name** and the relevance regex matches that English name (`publishers.py:101-103, 227, 256, 322`). Bloomberg pins `languagePreference=en` (`contracts.json:74`). So foreign-language coverage of non-US names (Keyence, SAP, BABA local press) is structurally not collected.
- No record carries a language field. SA's `locale` and `availableTranslations` exist in bronze and are dropped.
- No translation step exists for articles. The PRD's `C-FILINGS-TRANSLATION` (`AMGT_RESAPP_PRD.md:789-804`) covers filings only.
- Non-ASCII typography (curly quotes) in bodies is preserved (12-35 non-ASCII chars per sampled body).

**H7. Paywall and licensing.**
- The canonical record has no paywall or licence field. Paywall state is used only as a **gate** (`unlocked`) and then discarded.
- SA hard-codes `unlocked=True` even though bronze shows `isMpwLocked: true` on the sampled article.
- The PRD records the vendor-terms question on programmatic access as **NOT READ and Andrew's** (`C-SA-UNMEASURED`, `AMGT_RESAPP_PRD.md:1221-1234`), and paywalled sources are "not thereby ratified for production" (`:1216-1219`). These are full subscriber bodies stored in an Opal bucket, which is a licensing exposure, not an engineering one.
- The page shows only the title and link; bodies are not served.

**H8. Raw bytes are not retained on the legacy path.** Only `response_sha256` is stored, the hash
of bytes nobody kept (inventory 09-18 `:676`). A re-parse needs a re-fetch.

**H9. Not in the pool at all:**
- Vendor ticker tags (SA `primaryTickers` / `secondaryTickers` tag ids).
- Author.
- Summary bullets.
- Comment and like counts. So "most-discussed" is stated as ABSENT (`scoped_amgt.py:3038`), and the feed has no discussion ordering.

**H10. Mixed `published` offsets** (`Z`, `.002Z`, `-04:00`) are normalized to UTC only at
`pool_reader.parse_stamp` (`:395-426`). The day bucket is a UTC date, so an evening-ET SA article
lands on the next UTC day.

---

## SUMMARY

1. **Channel.** One local, signed-in-browser harvester (`lib/opal_data_harvest`) covers SA, FT, WSJ, Bloomberg.com and Barron's. It discovers by English company-name search (SA alone by symbol) and links an article to a security when the name appears once anywhere in the title or body. Its Windows task is **Disabled** with no trigger, and uploads are manual.
2. **Live pool.** `publications/v1` has 7 bodies and `publication-links/v1` has 7 links (BA 2, COST 2, HD 3; last written 2026-09-15). Locally there are 83 bodies and 84 links with 167 outbox rows pending and 0 marked uploaded.
3. **New grammar.** `{barrons,wsj,ft,bloomberg}/harvest/{bronze,silver}/article` hold 0 objects. The 6 SA `bronze/article` objects came from the SA REST channel, with the `sha256("sa:"+id)` hash confirmed. `HarvestUploader` is not wired to the CLI, and FT/WSJ/Barron's never set `raw_bytes`, so they could never land bronze.
4. **Article record.** 18 fields, schema-locked: `article_key`, `publisher`, `article_id`, `url`, `title`, `published`, `fetched_at`, `body_blocks`, full `text`, `words`, `expected_words`, hashes, `transport`, `content_status`. There is no language, ticker tag, author, excerpt, paywall or licence field.
5. **Link record.** `security_key` (the harvester key `BA` or `security-<16hex>`), `company`, `ticker`, `article_key`, `publisher`, `first_discovered_at`. It bridges to `BA_US_Equity` only through the crosswalk `association_keys`, and there is no FIGI.
6. **Chatter axis.** Lambda `amgt-resapp-chatter-axis`, daily at 10:00 UTC. It counts pool articles per day, with no model and no sentiment, and writes `opal-harvest-security-metrics`. 2026-09-22: TRENDING has 2 rows, both score 0, with a payload_hash identical to 09-21. BREAKOUT is EMPTY with 189 of 191 names having no signal.
7. **Components.** The Lead Panel reads the chatter rows (`RankedList`, `SecurityOverlay`), and the page-header news feed (`HeaderBrief`) shows title, url, publisher and published_at through `pool_reader`. Thesis, Exec Mgmt, Peers and Model read **no** news fields. Article text never reaches the page.
8. **Biggest hazards.**
   - Relevance is weak: 4 of 5 sampled links are one incidental mention.
   - Non-English coverage is structurally absent (English name search, `languagePreference=en`, no language field).
   - Paywall flags are dropped (SA hard-codes unlocked), and the vendor terms are unread and Andrew's to decide.
   - The dedupe authority is a desktop SQLite file.
9. **Corrections to prior inventories.** Record types are `publication_article` / `security_article`, not `publication_body` / `publication_link`. Bronze is possible for SA and Bloomberg only, not all five.
