# Security Analysis: bubble collage and FinBERT sentiment for the news scanner -- findings and specs (DRAFT)

**Author:** the sentiment fork of `4.0.0_SA_CRO~Z`. **Date:** 2026-10-02 ~17:5xZ.
**Ask:** Andrew-direct ~17:3xZ, items N7, N8 and N10
(`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261002_173xZ_SECURITY_ANALYSIS_UIUX_WALK_BRIEFS_TO_CTO_Z.md`).
- **Routing:** this draft goes to `1.0.0_SA_CTO~Z` first. The backend spec is for `2.0.0_SA_COO~H` (AMGT_HARVST), and the
  frontend contract is for `2.0.0_SA_COO~D`.
- **Method:** code at HEAD (workspace CLOUD, portal DEV `a730d8ce`), and one read-only S3 read of the three newest HARVST gold
  snapshots (17:5xZ).
- **Not done:** no vendor call, no model download, no Lambda invoke, no write.

**Reading of "the current news scanner" (inferred):** the Lead Panel's Chatter face (`ChatterBubbles`, articles collected per
covered name) together with the per-security timeline's article rows (`TimelinePanel`). Both are fed by HARVST gold. The
estate's other "news scanner" is the Market Overview news pipeline (Topic Cloud). It is a separate corpus, and it is where
FinBERT lives today.

---

## 1. Topic Cloud (Market Overview)

| Question | Answer | Evidence | Tag |
|---|---|---|---|
| Components | `SentimentGauge` reads `keyword-sentiments.json` and renders `TopicCloud`. A click opens `KeywordSentimentModal`. | `portal/src/components/market-performance/SentimentGauge.tsx:15-16`, `:131`, `:352` | measured |
| Layout | **It is a word cloud, not circles.** It uses `@visx/wordcloud` (d3-cloud underneath) with an archimedean spiral, the random seed fixed at 0.5, and no rotation. The spiral places the largest word first at the centre, and smaller words land further out, which is the "centred on the largest, smaller outward" look Andrew names. Font size is linear in the value, and the top 20 keywords are shown. | `TopicCloud.tsx:11-12`, `:139`, `:160-171`, `:187-198` | measured |
| Colorway | `getSentimentColor(s)` clamps s to [-0.5, +0.5]. It interpolates RGB stops: RED `#f5365c` at or below -0.30; RED to ORANGE `#f97316` from -0.30 to -0.05; ORANGE to YELLOW `#eab308` from -0.05 to 0; YELLOW to LIME `#84cc16` from 0 to +0.05; LIME to GREEN `#2dce89` from +0.05 to +0.20; GREEN at or above +0.20. The yellow neutral family is Andrew-direct (2026-09-14). | `TopicCloud.tsx:44-90`, comment at `:47-49` | measured |
| Copies of the colorway | **Three private copies.** `KeywordSentimentModal.tsx:40-66` has the same ramp and adds null mapped to slate `#94a3b8` ("No Data"). `ExecutiveSummary.tsx:693-697` is a different 3-step version (+/-0.05, using the success, danger and warning tokens). Labels are a fourth set of cut points (`KeywordSentimentModal.tsx:68-75`: +/-0.05, +/-0.15). | the files named | measured |
| Tooltip | A solid indigo tooltip with white ink. It shows the word, the mention count, a sentiment swatch and the signed score. | `TopicCloud.tsx:242-260` | measured |
| Analysis modal | `KeywordSentimentModal`: a fixed overlay at z-100 with blur, a 720px card, a header and close control, then loading, error and data states. The data state lists articles, each with its signed FinBERT score in the colorway. | `KeywordSentimentModal.tsx:116-200`, `:284-287`, `:533-545` | measured |
| Chart library | `recharts` ^3.7.0 (installed 3.7.0), `@visx/wordcloud` and `@visx/text` 3.12.0, with `d3-cloud` 1.2.7 brought in transitively. **There is no apexcharts.** `d3-hierarchy`, `d3-force` and `@visx/hierarchy` are **absent** from `node_modules`. | `portal/package.json:27-28`, `:42`; a node_modules read | measured |

## 2. FinBERT in the estate

| Question | Answer | Evidence | Tag |
|---|---|---|---|
| The scorer | Lambda `opal-news-ai-sentiment`: a container image `finbert-lambda:latest` (CI-managed), 3008 MB, 900 s timeout, no trigger of its own ("invoked by other Lambdas"). The model is ProsusAI FinBERT, a tone classifier. The handler source is not in the repo, because the image is built by CI. | `infra/aws/terraform/news-pipeline/lambdas.tf:246-268`; `NEWS_SCANNER_DEEP_DIVE_20260916.md` F10 | measured (the TF); the model id is inferred from the deep dive |
| The orchestrator | Lambda `finbert-batch-processor`, run by two EventBridge rules (`cron(10 2,4,12,14,16,17,18,20,21,22,23 * * ? *)` and `cron(55 0,13,20 * * ? *)`, 14 runs a day). It reads DynamoDB `opal-news-articles` rows from the last 7 days that lack `sentiment_finbert`, invokes the scorer with `"title. summary"`, and writes back. | `infra/aws/lambda/finbert_batch_processor/lambda_function.py:18-21`, `:30-70`, `:130-159`; `finbert-batch.tf:47-92` | measured (code); applied state not read |
| Score shape | The scorer returns `{sentiment: positive\|negative\|neutral, confidence, scores}`. The stored fields are `sentiment_finbert` = +confidence, -confidence, or **0.0 for neutral**; `sentiment_finbert_label`; and `sentiment_finbert_confidence`. The signed score runs from -1 to +1. | `lambda_function.py:77-106`, `:153-157` | measured |
| What it scores | News-pipeline articles (RSS: Seeking Alpha, Yahoo Finance, The Verge, and others), at article grain. **Not HARVST articles.** | deep dive section 1; the table name | measured |
| How Topic Cloud reads it | The chain runs L2 trending, then KIG, then `opal-data-portal-v2/json/sentiment/keyword-sentiments.json`: a per-keyword mean, then TopicCloud. The modal reads article `sentiment_finbert`. | deep dive lines 41-77; `portal-proxy.ts:549`, `:579` | measured (doc + types) |
| **Andrew's standing rule on neutral** | 2026-09-16: *"0 means finbert has no confidence, no confidence articles should not be pulling everything in to 0, we grade what actually gets scored ... use finbert when there is a score and gpt 4o when there isn't ... finbert not being sure is not a vote"*. The GPT gap-fill (`sentiment_gpt`) exists in the news Lambdas' code (`news_trending_analysis`, `keyword_drilldown_generator`). | deep dive section 6 (lines 359-366); a grep hit on `sentiment_gpt` | measured (the word + code); its deployed state is NOT established |

## 3. The news scanner on Security Analysis

| Question | Answer | Evidence | Tag |
|---|---|---|---|
| Chatter face | `ChatterBubbles`. It draws one circle per security on a **fixed 4-column grid in served order** (`COLUMNS=4`, `CELL_W=160`, `MAX_RADIUS=40`). Area is proportional to the month's `collected`, with one shared `k`. Every bubble has one fill, `PALETTE.blue500`; **there is no sentiment colour.** The hover is the native `<title>`. Month cursor: "Earlier month" and "Later month" over the served months. | `portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx:55-59`, `:113-127`, `:144-159`, `:180-196` | measured |
| Its route | `GET /api/scoped/amgt/lead-panel/timeseries/collected/chatter` leads to `lib/research/api/monthly_chatter.read_monthly_chatter()`. Per covered name and per **calendar month**, it serves the summed `chatter_daily.articles_total` and per-publisher counts from `article_security_mention`. It reads only `security_key, day, articles_total` and `article_key, security_key, publisher, published_utc`. | `scoped_amgt.py:4903-4917`; `monthly_chatter.py:1-38`; `amgt-lead-panel.ts:96-100` | measured |
| Timeline | `TimelinePanel` serves day bars, the event list (`lead_headline -- span, n articles`) and the selected-day article rows (`headline ?? '[no headline]'`). There is no sentiment anywhere. The routes are `.../security/<key>/timeline` (`from` and `to` pass through) and `.../timeline/day/<date>`. | `TimelinePanel.tsx:87`, `:99`, `:353-367`, `:575-597`; `scoped_amgt.py` `_serve_timeline` (`query.get("from")`, `query.get("to")`); `timeline_api.py:262-276` | measured |
| **HARVST gold sentiment today** | **None.** `GOLD_MENTION_SCHEMA` (26 fields, title and `published_precision` since @b7e88285ac, HVST-aj-7, 14:17Z today), `GOLD_DAILY_SCHEMA` and `GOLD_EVENT_SCHEMA` carry no sentiment, label or confidence field. | `publication_gold.py:64-90`, `:382-420`, `:1078-1092` | measured |
| Text available to score | Silver `article` carries `title` and `text_blocks` (the mention matcher uses the first 3 blocks as the "lead"). | `publication_gold.py:179-191`; `silver_from_bronze.py:134` | measured |
| What is missing to colour a bubble or an article | (a) a FinBERT score per HARVST article; (b) the score carried to the mention rows and aggregated per (security, window); (c) the served fields on the chatter and timeline payloads; (d) the colorway shared in the portal. | the above | inferred |

## 4. The period (month and earlier month, against rolling 30, 90 and 365 days)

| Question | Answer | Evidence | Tag |
|---|---|---|---|
| What the cursor is bound to | The served `months` list. `stepMonth` is client-side, and a step makes no request. The route aggregates by calendar month only and takes **no window parameter**. | `ChatterBubbles.tsx:37-42`; `monthly_chatter.py:1-12`; `scoped_amgt.py:4904-4917` | measured |
| What the timeline accepts | The per-security `/timeline` already takes `from` and `to`. A rolling window there is **frontend-only**. | `timeline_api.py:262-276`; `_serve_timeline` | measured |
| Gold depth, read 17:5xZ | `chatter_daily` newest `part-20261002T170716Z`: 58,300 rows, **day 2026-01-01 to 2026-10-02** (275 days), 212 securities, 6,155 non-zero security-days. `article_security_mention` `part-20261002T165144Z`: 23,691 rows, `published_utc` from 2013-07-30 to 2026-10-02. `chatter_event` `part-20260930T001658Z`: **8 rows**, first_day from 2026-02-12 to 2026-09-14, and the snapshot is 2 days older than daily. | a read-only S3 GET of the newest keys from `monthly_chatter._newest_snapshot_key` | measured |
| Coverage | **30 and 90 days: covered. 365 days: NOT covered.** Daily is dense only from 2026-01-01, so a 365-day window today holds 275 served days. Either `chatter_daily` is backfilled to 2025-10-02, or the 365 view states its true start ("since 1 January 2026"). `chatter_daily` already stores `trailing_7d_sum` and `trailing_30d_sum` (`publication_gold.py:396-397`). | the above | measured |

**Outside this fork's scope, for the parent:** `chatter_event`, the only "what happened at a spike" layer that exists today,
holds 8 events estate-wide, and its newest snapshot is from 09-30. Item N4 (the spike annotation layer) cannot rest on it as
built.

---

## 5. BACKEND SPEC for `2.0.0_SA_COO~H` (AMGT_HARVST)

Build ladder: the estate already has the scorer, so **reuse `opal-news-ai-sentiment`**. Write no new model host and download
no model. Invoking an Opal-owned Lambda is not vendor egress.

| # | Act | What | Acceptance (testable) |
|---|---|---|---|
| H1 | **Score HARVST articles** | A HARVST gold builder step (beside `build_mention`, `publication_gold.py:1031`) scores each newest silver article not yet scored at its current `record_hash`. Text: `title + ". " + first lead block(s)`, truncated to 500 characters, mirroring the news pipeline's `"title. summary[:500]"`. It invokes `opal-news-ai-sentiment` with `{"text": ...}` and maps the result exactly as the batch processor does (+conf, -conf, 0.0 for neutral). | A planted article with a known text gets the expected label and sign. A second run with no silver change makes 0 invocations. A re-silvered article (new `record_hash`) is re-scored once. |
| H2 | **Carry the score in gold** | A new gold table `article_sentiment` at article grain, OR fields on the mention rows. Recommended: the table, keyed `(article_key, record_hash)`, with `sentiment_score` (float, -1..+1), `sentiment_label` (positive\|negative\|neutral), `sentiment_confidence`, `model` (the image digest), `text_basis` and `scored_at`. `build_mention` then joins `sentiment_score`, `sentiment_label` and `sentiment_confidence` onto each mention row, as it now carries `title`. **No colour, no "bullish" word and no display text in gold** (rule 17b; the colour is the portal's). | Each mention row's sentiment equals its article's row at the same `record_hash`. 0 rows carry a colour or a display label. |
| H3 | **Aggregate under Andrew's neutral rule** | Per (security, day) in `chatter_daily`: `sentiment_mean` = the mean of **non-neutral** scores only ("finbert not being sure is not a vote"); `sentiment_voters` = the count of non-neutral; `sentiment_scored` = the count scored. `articles_total` is untouched. The three denominators are stored side by side, never one number (deep dive F2). | Over a planted day of 3 positive, 1 negative and 4 neutral articles, the mean is over 4 voters, voters=4, scored=8 and articles_total=8. A day with 0 voters stores `sentiment_mean` null, not 0. |
| H4 | **Serve it** | `monthly_chatter` adds per month (or per window, see H5) `sentiment_mean`, `sentiment_voters` and `sentiment_scored`. The timeline series adds the day's three fields. The day rows add each article's `sentiment_score` and `sentiment_label`. | The served JSON carries the fields. A month or day with 0 voters serves null plus a plain reason. **This moves served output: a never-widen pair (CTO + COO) before the deploy.** |
| H5 | **Rolling windows** | `collected/chatter` accepts `?days=30\|90\|365`. The sums run over `chatter_daily` days in (as_of - N, as_of]. The response states `window_start_served` (the real first day served) beside the asked window. The calendar-month form stays the default until the frontend switches. | `days=30` equals the sum of the last 30 daily rows for 3 sampled names. `days=365` today serves `window_start_served = 2026-01-01` and says so. |
| H6 | **History, optional** | Backfill `chatter_daily` (and scoring) to 2025-10-02 so 365 days is whole, or record that 365 days means "since 1 January 2026". | One of the two is ruled and recorded. |

**Reserved and open for this spec:**
- **The GPT gap-fill for neutral-only articles** is Andrew's 2026-09-16 rule for the news pipeline. Carrying it to HARVST is
  OpenAI egress. OpenAI is not on `org/ref/VENDOR_EGRESS_WHITELIST.yaml`, so it needs his word.
- **Rule 30 (LGIC):** a new gold table name and address are builder output (`lib/opal_naming.py`). Whether HARVST, an existing
  pipeline, takes them now is the CTO's call.
- **H1's invoke permission:** the HARVST builder's execution role needs `lambda:InvokeFunction` on `opal-news-ai-sentiment`
  (the pattern is `news-pipeline/iam.tf:293-296`). Which role runs the HARVST gold build was NOT established here.

## 6. FRONTEND CONTRACT for `2.0.0_SA_COO~D` (DSGN_AMGTV1)

| # | What | Reads | Acceptance |
|---|---|---|---|
| F1 | **Bubble collage.** Replace the 4-column grid with a deterministic spiral pack: sort by size, place the largest at the centre, then place each next bubble at the first non-overlapping point along an archimedean spiral. This is the same placement rule `@visx/wordcloud` uses for Topic Cloud. About 40 lines as a small util; **no new dependency** (`d3-hierarchy` and `d3-force` are absent). Labels sit inside large bubbles and appear on hover for small ones. | `collected` per name for the window | Every served name with a count gets one bubble. There are 0 overlaps. The same payload gives the same layout. The whole set fits one panel with no vertical scroll at 1280px for up to 60 names. |
| F2 | **Colour by sentiment.** Extract `getSentimentColor` from `TopicCloud.tsx:44-90` into one shared module (null maps to slate `#94a3b8`, as in `KeywordSentimentModal.tsx:41`) and use it in TopicCloud, the modal and the bubbles. Retire the `ExecutiveSummary.tsx:693` 3-step copy, or rule it as different on purpose. | `sentiment_mean` (null means no voters) | One colour function in `src/`. A bubble with null sentiment is slate and its hover says "no scored articles". |
| F3 | **Hover tooltip** in the Topic Cloud tooltip look (indigo, white ink, swatch). | name, `collected`, `sentiment_mean`, `sentiment_voters` of `sentiment_scored` | The tooltip prints the voters denominator beside the mean. |
| F4 | **Click opens a modal** in the `KeywordSentimentModal` shell pattern: the name's articles in the window, each with its signed score in the colorway. | the day and window article rows with `sentiment_score` | It opens and closes with Escape and on overlay click. Articles are sorted newest first. |
| F5 | **Period control:** three presets, 30d, 90d and 365d, replacing "Earlier month"/"Later month". | `?days=` (H5); the timeline's `from`/`to` | Each preset makes one request. The 365 preset prints `window_start_served` when it is later than as_of - 365. |

**Could not establish:** the deployed state of the GPT gap-fill code; the `opal-news-ai-sentiment` handler source and its exact
model revision; the HARVST gold builder's execution role; the scorer's throughput per invocation (needed to size the one-time
backfill of about 8,700 articles).
