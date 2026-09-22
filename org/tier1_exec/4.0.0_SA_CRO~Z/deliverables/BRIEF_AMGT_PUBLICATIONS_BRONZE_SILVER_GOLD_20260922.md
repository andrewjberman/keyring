# BRIEF -- the publication channels: retrieval, structure, and the bronze / silver / gold strategy for the Chatter axis

**From** `4.0.0_SA_CRO~Z`, 2026-09-22 ~14:xxZ, on Andrew's words at this terminal (record
`ANDREW_DIRECT_20260922_AMGT_PUBLICATION_RETRIEVAL_STRUCTURE_BRIEF.md`). **To** Andrew, and `1.0.0_SA_CTO~Z` for the
L2+ route. **Status:** research and a plan. No vendor call, no pull, no code, no cut. Every number below was measured
this session and carries its denominator; every design item is marked as a recommendation.

---

## 0. The answer in one screen

1. **Where we are.** Round 27 closed 2 of 2. Round 28 is issued (`0ed364cff0`): six code-only cells, wave 0 of the
   Lenovo trial (language detection, FIGI identity fields, fiscal-year join, Lusha domain fallback, SA identity by
   company name, currency labels), all `pending`. Publications for Lenovo are trial stage 9, ONE run, not cut yet.
2. **The field map is organised BY CHANNEL** (five dictionaries, A to E) with a component cross-table in the main
   file. Per FIELD, the component it feeds is not recorded. **Recommend:** one `feeds` column on every field row, and a
   component index generated from it, so both views come from one record (s.2).
3. **Retrieval is the real problem, and it is measured, not guessed.** Only Seeking Alpha is queried by symbol. FT,
   WSJ, Barron's and Bloomberg.com are queried by English company name, and an article is linked on ONE word-bounded
   name mention anywhere. Over the 84 links on this desktop: **19 of 84 mention the company exactly once; 38 of 84
   never name it in the title.** The chatter axis counts all 84 as equal signal. **Recommend:** keep the mention as the
   FLOOR (his tolerance), and GRADE strength above it in gold rather than filtering at retrieval (s.3).
4. **Structure: clean JSON is real for 3 of 5 publishers and structured-in-HTML for 2.** SA, Bloomberg and Barron's
   return native JSON; WSJ and FT return JSON embedded in an HTML page. The in-flight parse is clean on 7 of 7 live
   bodies (0 markup). **Not verified:** FT, WSJ and Barron's bronze, because their bytes are never retained (s.4).
5. **Timestamps:** three clocks exist and are kept apart today (published, fetched, first-discovered). `published`
   arrives in two forms (64 `Z`, 20 with an offset, of 84). Silver normalises to UTC and keeps the offset (s.4.2).
6. **Bronze** = the vendor's bytes per article, one object per fetch, under `article_hash`. Already ruled and built
   (rk-85), OFF until the move. Gap: the silver writer is fed from the NORMALISED record (18 fields), not the vendor
   payload, so SA's `locale`, paywall flags, ticker tags and sentiment are lost before silver. **Recommend** silver be
   built from bronze (s.5).
7. **Gold = three tables** (s.6): `article_security_mention` (the dissect-anywhere grain, one row per article x
   security, with the strength fields he named: headline, lead, count, density, co-mentions), `chatter_daily` (the
   Chatter axis base, one row per security x UTC day, with trailing windows and a breakout ratio that matches the
   ratified price rule), and `chatter_event` (the event spine: clustered strong-signal days). The timeline graph reads
   `chatter_daily`; a click on any point reads `article_security_mention`.
8. **Calls for Andrew** (s.8): the signal-tier weights; whether a single passing mention counts in the axis at all or
   only in the event spine; the non-English press question for HK/JP names; the publisher-terms question the PRD
   already marks as his.

---

## 1. Where rounds 27/28 and the Lenovo trial stand (measured at HEAD `6acadc3dd2`)

| item | state |
|---|---|
| round 27 | CLOSED: rk-105 (filing-attempt skip-held) and rk-106 (roster domain diagnosis) terminal, 9/0/0; one graduated defect C-S386 rides the next code cell (`ROUND_ANALYSIS.round27.md`) |
| PRD | v0.22 ADMITTED (both halves signed; brief half by this seat @`96cc4dae9d`); section 12 is the Lenovo trial |
| round 28 | ISSUED @`0ed364cff0`: rk-107 language detector (Latin alphabets), rk-108 FIGI family on identity, rk-109 fiscal-year join, rk-110 Lusha verified-domain fallback, rk-111 SA identity by `companyName`, rk-112 currency labels. All six `<status>pending`, all code-only |
| Lenovo | `992_HK_Equity`, 18 objects in the bucket (peers 5, model blocks 3, bronze 2, raw 2, scores 2, packs, posture, filings, filing_attempt); stage 9 (publications, one run) and stage 10 (social) not cut |
| publications channel today | Windows task DISABLED; uploads manual; S3 holds 7 bodies + 7 links (last 2026-09-15); this desktop holds **83 bodies, 84 links, 167 outbox rows pending, 0 uploaded** |

**For Lenovo specifically:** SA reaches it only through the ADR line (`LNVGY`, OTC); the four name-search publishers
will search "Lenovo" in English; Hong Kong and Chinese-language press is not collected by anything (field map H6).

---

## 2. How the collected fields are organised today, and the recommendation

**Today:** `prd/FIELDMAP_20260922.md` plus five channel files (A publications/news, B Seeking Alpha/peers, C
filings/IR/translation, D Bloomberg/model, E people/SERP/social). Each channel file has a field dictionary per layer
(bronze, served, silver, DynamoDB) with type, shape and meaning, and a "Component map" section listing which routes and
portal components read the channel. The main file's s.1 is a component-to-channel table. **So the organising axis is
CHANNEL; component is a summary, and a field row does not say which component it feeds.**

**Recommendation** (both his cases from one record):
- keep the channel files as the source of truth, each opening with a one-paragraph description of the channel (vendor,
  mechanism, cadence, cost, key) -- file A already does this;
- add one column to every field row: `feeds` = `Lead Panel | Thesis | Exec Mgmt | Peers | Model | none`, with the
  served route beside it;
- generate the component view from those rows (one table per component: channel, layer, field, route), with a
  one-paragraph description of the component at its head;
- a field whose `feeds` is `none` is the honest "stored, not shown" list, which the map today carries only as prose.

---

## 3. Aspect 1, RETRIEVAL

### 3.1 What each channel does today (`lib/opal_data_harvest/publishers.py` @`6acadc3dd2`, `contracts.json`)

| publisher | discovery call | keyed by | time bound | relevance test |
|---|---|---|---|---|
| sa | `/api/v3/symbols/{symbol}/news?filter[since]=0&filter[until]=0&include=author,primaryTickers,sentiments` | **symbol** | `filter[since]/[until]` exist (unused, both 0) | name mention |
| bbg | `nemo-next/api/search/query?query="<company>"`, 3 pages | quoted company name | none on search; a symbol `news(s, symbol, name)` call with `targetDate` exists in `bloomberg_rest_fetch.py:119-123` and is UNUSED by the harvester | name mention |
| ft | `ft.com/search?q=<company>` | company name | none measured | name mention |
| wsj | `wsj.com/search?query=<company>` -> `__NEXT_DATA__` searchResults | company name | none measured | name mention |
| barrons | `barrons.com/search?query=<company>` -> `searchData.articles` | company name | none measured | name mention |

The relevance test (`publishers.py:99-105`): any alias, word-bounded, case-insensitive, anywhere in `title + text`.
It is a GATE (`company_not_mentioned` rejects), never a grade.

### 3.2 The signal, measured on this desktop's 84 links (3 securities x 5 publishers, 83 bodies)

| measure | result |
|---|---|
| company named in the TITLE | **46 of 84** (barrons 4/15, bbg 10/19, ft 8/15, sa 13/20, wsj 11/15) |
| named in the first 3 blocks | 60 of 84 |
| named in the first block | 50 of 84 |
| mention count exactly 1 | **19 of 84** |
| mention count 2-4 | 28 of 84 |
| mention count 5 or more | 37 of 84 |
| median share of blocks that mention it | 0.24 |
| `published` range | 2022-06-08 to 2026-09-14 (a search returns history, not just the latest) |

The 7 objects in S3 tell the same story at small scale: 2 of 7 (both Boeing) are ABOUT the company (24 and 30
mentions, named in the title); the other 5 mention it 2 to 7 times, 4 of them not in the title (a Williams-Sonoma
tariff story, a Vanguard piece, a YouTube/Amazon story, an S&P earnings roundup, an FT macro piece).

**So the low signal is not noise from bad matching; it is the shape of a name search.** A search returns everything
that mentions the name, and the pipeline keeps everything that mentions the name. His tolerance ("not phased if the
articles are low signal as long as the security is mentioned") means the FLOOR is right. What is missing is the
GRADE above the floor, and that belongs in gold, not in the fetch.

### 3.3 The refined mechanism (recommendation)

1. **Prefer the symbol-keyed listing wherever a publisher has one.** SA already does. Bloomberg's client has a
   symbol `news()` call with a date bound that the harvester never uses; test it in the Lenovo run (one call). A
   symbol listing carries the vendor's OWN relevance judgment (SA's `primaryTickers` tag; measured on a BABA news
   item: tag `137271` = `BABA`, `Alibaba Group Holding Limited`), which becomes a gold feature, not a gate.
2. **Keep the name search for FT, WSJ and Barron's**, with two additions: search the legal short name AND the
   ticker-in-quotes form, and stop paging at a per-(security, publisher) WATERMARK = the newest `published` already in
   silver, so a re-run costs one page. SA's `filter[since]` and Bloomberg's `targetDate` are the same watermark
   expressed natively.
3. **Keep the mention floor exactly as it is.** Do not raise it. Raising it discards the 19 single-mention articles
   he said he is fine keeping, and they are the raw material of the event spine's co-mention feature.
4. **Every retrieval decision becomes a silver field, never a dropped flag:** which rung found the article (symbol
   listing / name search / ticker search), the search rank, the vendor tag, the paywall state, the language. Today
   all of these are read in flight and discarded (field map s.3.1).
5. **Dedupe stays the bucket's** (`article_hash` = `sha256(<publisher>:<id>)`, ruled and built in rk-85). A watermark
   miss can never re-fetch a known article.

---

## 4. Aspect 2, STRUCTURE

### 4.1 Clean JSON per channel: verified where the bytes exist

| publisher | transport | body source | clean JSON? | bronze retained today? |
|---|---|---|---|---|
| sa | `json` | listing item; body is HTML INSIDE the JSON (`attributes.content`), parsed to blocks with BeautifulSoup | **yes** (native JSON), body needs one HTML-to-blocks step | yes (SA REST channel: 6 objects; the browser channel's SA bronze is the listing item) |
| bbg | `json` | `story.body.content` typed blocks | **yes** | possible (code passes `raw_bytes`), 0 objects landed |
| barrons | `json` | `/articles/api/articles/{slug}` -> `body` typed blocks | **yes** | **no** -- `raw_bytes` never set (`publishers.py:371-374`) |
| wsj | `http_embedded_json` | `__NEXT_DATA__.props.pageProps.articleData.flattenedBody` | **structured, inside HTML**; the article JSON API is `unresolved` (`contracts.json`) | **no** |
| ft | `http_jsonld` (+ `http_html_last_resort`) | JSON-LD `NewsArticle.articleBody`, a plain string split on blank lines | **structured, inside HTML**; `api.ft.com` is disallowed (403) | **no** |

The parse output is clean: 7 of 7 live bodies pass the markup/code regex, carry 12-27 blocks and 337-949 words.
**What is NOT verified is the bronze for three publishers**, because their bytes are never kept: a re-parse needs a
re-fetch (field map H1, H8). **Recommendation:** bronze for WSJ and FT is the HTML page as received (form (a),
`.html`), for Barron's the JSON response; the JSON-in-HTML extraction is a SILVER step, replayable from bronze. This
is what "know what we're getting" costs: three publishers currently give us nothing to know.

### 4.2 Organisation by timestamp

Three clocks exist and are already kept apart at the reader boundary (`pool_reader.py`):

| clock | field | meaning | today's form |
|---|---|---|---|
| publication | `published` | when the publisher says it ran; the ONLY day-bucketing clock | mixed: 64 `Z`, 20 with an offset (of 84); parsed to UTC at read time only |
| retrieval | `fetched_at` | when we fetched it | tz-aware |
| association | `first_discovered_at` | when a security's job first found it | tz-aware |

**Recommendation for silver:** `published_utc` (timestamp, UTC), `published_offset_min` (the offset the publisher
sent, so local-time analysis is possible later), `published_date_utc` (the bucket key), `published_precision`
(`second | minute | date` -- Bloomberg sends `12:00:00.000Z` on some stories, which looks like a date-only value
promoted to noon). The day bucket is UTC everywhere; a US-evening article lands on the next UTC day, and the offset
column lets a consumer re-bucket by exchange day if a later analysis wants it. Sorting, windows and joins all run on
`published_utc`; `fetched_at` is never substituted (already a rule, `pool_reader.py`).

---

## 5. Bronze and silver, per channel

**Bronze (built, rk-85; off until the move).** `{source}/harvest/bronze/article/article_hash=<sha256(pub:id)>/<stamp>.<ext>`
for `seeking-alpha`, `bloomberg`, `barrons`, `wsj`, `ft`; `received-form` in object metadata; the bytes as received.
Add: the LISTING page as bronze too (`.../bronze/search/...` or `.../bronze/news_listing/...`, form (c), keyed by the
query hash and date), because the listing is where rank, vendor tags and the watermark live.

**Silver, one `article` table per source, and one `listing_hit` table.** The rk-85 writer shapes the silver row from
the normalised 18-field record. **That is a fidelity loss against C-SILVER-PARQUET's "every vendor field kept"**:
measured on SA bronze, `locale`, `isPaywalled/isLockedPro/isMpwLocked`, `primaryTickers`, `secondaryTickers`,
`sentiments`, `themes`, `summary`, `commentCount`, `likesCount` are all present in bronze and absent from the record
(field map s.3.1). **Recommend the silver row be built FROM BRONZE**, with:

| column group | columns |
|---|---|
| identity | `article_key`, `publisher`, `article_id`, `url` (canonical), `bronze_key`, `fetched_at`, `record_hash` |
| text | `title`, `body_blocks` (list<string>), `text`, `words`, `expected_words`, `body_sha256`, `transport`, `content_status` |
| time | `published_utc`, `published_offset_min`, `published_date_utc`, `published_precision`, `last_modified_utc` (SA) |
| vendor-native, typed as delivered | `language` (SA `locale`; null elsewhere), `paywall_flags` (struct), `vendor_ticker_tags` (list<struct{tag_id, symbol, company}>, from `included`), `vendor_sentiment` (list), `themes` (list<string>), `summary_bullets` (list<string>), `comment_count`, `like_count`, `author_ids` (ids only, never names), `section`/`subtype` |
| retrieval provenance | `retrieval_rung` (`symbol_listing | name_search | ticker_search`), `search_query`, `search_rank`, `search_page` |

Typing is standard (string, int, bool, timestamp, list, struct); nothing is filtered or summarised. The link (which
security an article is about) is NOT silver: it is Opal's judgment, so it is gold (already ruled, rk-85 ruling 4).

---

## 6. Gold: the three tables, and the derived metrics

All three are `amgt/harvest/gold/...` parquet, `date=` partitioned, one row per entity per generation (R11), built
from silver only, and re-buildable from silver at any time.

### 6.1 `article_security_mention` -- one row per (article, security). The dissect-anywhere grain.

| metric | definition | why |
|---|---|---|
| `mention_count` | word-bounded matches of the name/aliases/ticker in `text` | "how much the security is mentioned" |
| `mention_in_title` | bool | "is it mentioned in headline?" |
| `mention_in_lead` | any match in the first 3 blocks | the journalistic lead is where the subject sits |
| `first_mention_block`, `first_mention_pos` | block index; character offset / text length | how far in the name first appears |
| `blocks_hit`, `blocks_total`, `mention_density` | blocks with a match / all blocks | 0.24 median today; an ABOUT-the-company story runs 0.5+ |
| `match_forms` | which alias forms hit (legal name, short name, ticker) | ticker-only hits are weaker |
| `vendor_tagged_primary` / `_secondary` | SA `primaryTickers` / `secondaryTickers` includes this security | the vendor's own judgment |
| `co_mentioned_securities`, `co_mention_count` | other UNIVERSE names matched in the same article | a roundup ("all 12 S&P reporters") mentions many; a story about one names few |
| `is_roundup` | `co_mention_count >= 5` (threshold is a call) | the S&P scoreboard case |
| `signal_tier` | **A** title + lead; **B** lead or density >= 0.3; **C** 2+ mentions elsewhere; **D** single passing mention | the categorisation he asked for |
| `signal_weight` | A 1.0, B 0.6, C 0.3, D 0.1 (**defaults, his call**) | one number for the axis |
| time | `published_utc`, `published_date_utc`, `fetched_at`, `first_discovered_at`, `lag_hours` = fetched minus published | latency of our coverage |
| lineage | `article_key`, `security_key`, `composite_figi` (when the crosswalk carries it), `publisher`, `retrieval_rung`, `language` | joins |

On the 84 measured links the tiers would split roughly A 46, B/C 19-28, D 19 -- the axis today weights all 84 at 1.0.

### 6.2 `chatter_daily` -- one row per (security, `published_date_utc`). The Chatter axis base.

| metric | definition |
|---|---|
| `articles_total`, `articles_tier_a..d` | counts by tier |
| `mention_score` | sum of `signal_weight` over the day's articles |
| `publishers_distinct`, `publisher_mix` | breadth: one outlet or five |
| `mention_count_total` | sum of `mention_count` |
| `trailing_7d`, `trailing_30d` | rolling sums of `mention_score` (dense: an empty day is a zero, as `chatter_axis.dense_series` already insists) |
| `baseline_30d_mean`, `baseline_30d_sd` | over the prior 30 days, excluding the day |
| `breakout_ratio` | `mention_score / baseline_30d_mean` | the same shape as the RATIFIED price rule (+5% over the trailing 30-day mean, Andrew 09-18 card B); the chatter floor is a call |
| `z_score` | `(mention_score - baseline_mean) / sd` | for ranking across companies of different base volume |
| `first_published_utc`, `last_published_utc`, `coverage_lag_hours_median` | when the day's news actually ran |
| `data_status` | `COMPLETE | PARTIAL | DENIED` from the reader's four failure states, so a quiet day is never a broken read |

The existing Lambda's TRENDING (count on the day) and BREAKOUT (jump versus baseline) map onto `mention_score` and
`breakout_ratio` directly; the DynamoDB rows become a projection of this table instead of a separate count.

### 6.3 `chatter_event` -- the company-specific event spine.

An EVENT is a cluster: consecutive UTC days for one security where `articles_tier_a + articles_tier_b >= 2` from
`publishers_distinct >= 2`, merged across gaps of at most 1 day (thresholds are a call). Columns: `event_key`
(`sha256(security_key + start_date + first article_key)`), `event_start_utc`, `event_end_utc`, `peak_date`,
`peak_mention_score`, `articles_total`, `publishers`, `lead_headline` (the earliest tier-A title), `lead_article_key`,
`co_mentioned_securities` (the union), `event_status` (`OPEN | CLOSED`). This is the spine later joins hang on:
filings (an 8-K or annual report date inside the window), price moves (`chatter_daily` next to the price axis), and
management changes (an officer named in the lead headline).

### 6.4 Why this serves the timeline graph he described

`chatter_daily` is the series (one point per day per company, dense). Any point dissects into
`article_security_mention` rows for that day, sorted by tier then `published_utc`. Any run of points dissects into a
`chatter_event`. Nothing on the page needs the body text; the graph needs only the three gold tables.

---

## 7. What changes where, and when

| step | change | owner | when |
|---|---|---|---|
| 1 | field map: `feeds` column + generated component index | `1.0.0_SA_CTO~Z` (map author) | next map revision |
| 2 | bronze for WSJ/FT (HTML page) and Barron's (JSON); listing pages as bronze | rk-85's writer, `publishers.py` (`raw_bytes` on 3 more paths) | with the publications move (M4) |
| 3 | silver `article` from bronze, widened per s.5; `listing_hit` | `harvest_grammar.article_silver_row` | same cell |
| 4 | retrieval: Bloomberg symbol `news()` trial, watermark paging, provenance fields | harvester | the Lenovo run (stage 9) is the first test: one run, caps as ruled |
| 5 | gold tables 6.1-6.3 | a new gold producer; the chatter Lambda reads `chatter_daily` | after the Lenovo run lands silver |
| 6 | the page: RankedList/SecurityOverlay/HeaderBrief read the gold projection | portal + `scoped_amgt.py` | after 5 |

The Lenovo trial is the right first test: one security, five publishers, caps stated, and the 83 local bodies are a
ready-made second sample for the tier thresholds once uploaded (they are stuck behind the outbox, field map H5).

---

## 8. Calls for Andrew, each with a recommendation

| # | call | recommendation |
|---|---|---|
| 1 | tier weights A/B/C/D | 1.0 / 0.6 / 0.3 / 0.1 to start; re-fit after Lenovo plus the 83 |
| 2 | does a tier-D single passing mention count in the axis? | yes at 0.1, so the floor he set stays visible; it counts fully in `co_mention` and the event spine's context, never as an event trigger |
| 3 | roundup threshold | `co_mention_count >= 5` |
| 4 | event thresholds | 2+ tier-A/B articles from 2+ publishers, gap of at most 1 day |
| 5 | non-English press for HK/JP names (Lenovo is the first case) | out of the trial; state it as UNRESOLVED-BY-DESIGN in the trial report, and decide after the report |
| 6 | publisher terms on stored subscriber bodies | already his in the PRD (`C-SA-UNMEASURED`); this brief adds nothing to it, and stores nothing new |
| 7 | silver from bronze (widened) versus silver from the normalised record (rk-85 as built) | from bronze; the vendor fields he wants for gold (tags, language, paywall) exist only there |

---

## 9. What this brief does not claim

It ran no vendor call and no pull; the retrieval rungs in s.3.3 are proposals, and Bloomberg's symbol `news()`
endpoint is measured to EXIST in the client, not to work live. The 84-link sample is three US pilots on five
publishers; Lenovo's shape (ADR line on SA, English-only name search) will differ, and the trial is what measures it.
The tier weights, roundup and event thresholds are defaults for his ruling, not findings. Nothing here changes the
ratified contracts; where it disagrees with rk-85's silver shape it says so and leaves the change to the L4.
