# AMGT_RESAPP -- the SA corpus: how stale, and is it queryable by ticker?

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | Option 1 of the `/next-calls` set.
**Purpose:** settle whether "the SA corpus already in S3, read as history" is a viable v1 news
source. **Answer: it is stale by five months AND it is not ticker-queryable. Both halves fail.**

---

## 1. THE CORRECTION THIS FORCES -- I was wrong earlier today

> ⛔ **`AMGT_RESAPP_PRE_BRIEF_NOTES_20260910.md` s3.5 and `AMGT_RESAPP_SA_ONESHOT_PROBE_20260910.md`
> both state that SA articles ARE ticker-tagged. THAT IS FALSE OF THE LANDED CORPUS.**
>
> **How I got it wrong:** I read `data/seeking-alpha/scripts/edge_scraper_enhanced.py:293-338`,
> saw it build a validated per-article `tickers` array, and wrote down a property of the ARTIFACT
> on the strength of the PRODUCER'S CODE. That is the exact failure CLAUDE.md names -- *never trust
> a producer's self-report, verify against the SERVED artifact* -- and I cited a line number, which
> made a code-reading look like a measurement.
>
> **The discriminator I skipped:** the Edge scraper is the LOCAL/EC2 path. The corpus in S3 was
> produced by the **deployed Lambdas**, and `enumerate 'tickers'` returns **0 hits across
> `seeking-alpha-analysis-scraper` (401 lines) and 0 across `seeking-alpha-news-scraper` (296
> lines)**. The deployed path never had ticker extraction at all.

## 2. STALENESS -- and the grain trap inside it

| Measure | Value |
|---|---|
| Objects under `s3://opal-data-news-av/seeking-alpha/` | **10,245** (11.6 MB), paginator drained |
| Article objects | **7,785** (5,286 news + 2,499 analysis) |
| **Object WRITE times** | 2026-02-18 -> **2026-07-30** |
| **ARTICLE dates (the content)** | 2025-12 -> **2026-04** |
| Distinct day-partitions | **72** |

```
2025-12     19
2026-01  1,027  #################
2026-02  2,655  ############################################
2026-03  2,535  ##########################################
2026-04  1,549  #########################
```

⚠ **WRITE TIME IS NOT CONTENT DATE, and reading the wrong one understates the staleness by three
months.** The newest OBJECT was written 2026-07-30, which looks like ~6 weeks old. The newest
ARTICLE is from **2026-04** -- the later writes were backfill of older content. **The corpus is
~5 months stale, not ~6 weeks.** Anyone quoting a freshness number here must say which clock.

## 3. TICKER QUERYABILITY -- 0.0%, with a printed denominator

Random sample, **n=200 of a 7,785 population**, seed 11:

| Outcome | n | % |
|---|---|---|
| `news`: **no `tickers` field at all** | 153 | 76.5% |
| `analysis`: **no `tickers` field at all** | 30 | 15.0% |
| `analysis`: field present but **EMPTY** | 17 | 8.5% |
| **field populated** | **0** | **0.0%** |

**Zero of two hundred.** Not "sparse" -- absent. And the DynamoDB side cannot rescue it:
`opal-news-articles` (~342,625 items) is keyed **`(article_date, url_hash)`** and
`seeking-alpha-article-urls` (~50,648 items) is keyed **`(run_date, article_id)`**. **Both are
partitioned by DATE. Neither can be queried by ticker without a GSI or a full scan.**

## 4. WHAT THIS CHANGES

**The "free v1 news option" is withdrawn.** The earlier reasoning was: SA corpus is landed and
ticker-tagged, so mentions-by-ticker works today at zero cost. **Both premises are false.**

Corrected state of the three sources:

| Source | Ticker-queryable? | Fresh? | Cost to make usable |
|---|---|---|---|
| SA corpus in S3 | **NO -- 0/200** | **NO -- stops 2026-04** | entity extraction + a re-scrape |
| SA fresh (one-shot) | n/a | would be | credential + the consolidation (Option 2) |
| RSS/NewsAPI corpus | **NO** -- topic-level `affected_tickers` only | yes (if that scanner still runs -- unverified) | entity extraction |

> **THE LOAD-BEARING CONCLUSION FOR THE BRIEF:** *"scan our news database for mentions of the
> stock"* requires **an entity-extraction / ticker-resolution leg no matter which corpus is chosen.**
> It is not an optional enrichment and it is not avoidable by picking the other source. It is a
> certain v1 work item and should be sized as one.

### 4a. ANDREW-DIRECT 2026-09-10 -- THE DESIGN, and my recommendation above is WITHDRAWN

> **VERBATIM:** *"no it doesnt, we'd need to redesign that aspect, it would probably be crawling or
> oneshotting this: https://seekingalpha.com/symbol/{ALL CAPS TICKER}"*

~~**A silver lining worth stating:** the articles carry `title`, `body`, `url`, `publish_date`,
`author`, `topics`, so the text needed to extract tickers is present and a backfill over the 7,785
landed articles would produce a ticker-indexed historical corpus.~~ **WITHDRAWN.**

**WHY HE IS RIGHT, stated as the principle so it generalises:** an entity-extraction backfill
**INFERS** which ticker an article is about, from prose. The SA **symbol page is SA's own
AUTHORITATIVE INDEX** of that association -- Seeking Alpha already knows which articles belong to a
ticker, and publishes it. **Do not reconstruct by inference an index the source already publishes.**
My proposal would have spent a backfill to produce a fuzzier answer than a single fetch gives.

**It also inverts the direction of the query, which is the deeper point:**

```
  my proposal :  7,785 articles  --extract-->  tickers      (articles -> tickers, inferential, N-pass)
  the design  :  ticker  --fetch-->  https://seekingalpha.com/symbol/{TICKER}  (ticker -> articles,
                                                                authoritative, 1 fetch per name)
```

**THE DESIGN: crawl or one-shot `https://seekingalpha.com/symbol/{ALL CAPS TICKER}` per name.**
This is the same target the Option 3 probe tried and could not reach on the dead credential, so it
is unblocked by the Bright Data consolidation and nothing else.

> ⚠ **AN IDENTITY PROBLEM THIS EXPOSES, flagged not solved: the SA symbol is not the Bloomberg
> ticker, and the 89-name universe is heavily ex-US.** `SAP GY Equity` -> `SAP`, but
> `Copa CPA` -> `CPA`, `Koninklijke KPN NA` -> an ADR symbol, `Hon Hai 2317 TT` and
> `Mitsubishi UFJ 8306 JP` have no obvious SA symbol at all. **A ticker-mapping layer sits between
> the coverage list and this fetch**, and its coverage over the 89 is unmeasured. That mapping --
> not the fetch -- is the real work item, and it should be sized before the news leg is scoped.

**=> The landed 7,785-article corpus is therefore NOT the v1 news source in any form.** It is
historical, stale at 2026-04, unindexed by ticker, and superseded as a design by the symbol-page
fetch. It should be treated as an archive, not a feed.

## 5. NOT MEASURED

- Whether the **RSS/NewsAPI scanner is still running** (its README is ~10 months stale and cites a
  path from the other device). If it is live, it is the only FRESH news source in the estate.
- Whether `opal-news-articles`' 342,625 items include the SA articles or are RSS-only.
- Whether any GSI exists on either table (I read key schemas, not indexes).
