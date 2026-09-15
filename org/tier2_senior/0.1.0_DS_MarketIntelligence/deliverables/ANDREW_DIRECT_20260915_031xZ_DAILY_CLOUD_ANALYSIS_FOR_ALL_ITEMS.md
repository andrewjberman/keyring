# ANDREW-DIRECT 2026-09-15 ~03:1xZ (2026-09-14 ~11:1x PM ET) -- "We should have analysis for all items that appear in the Daily Cloud"

**Channel:** direct, at the `0.1.0_DS_MarketIntelligence` terminal (Claude Code session
`d2a7b357-7407-41d6-ad83-043404c6b0c6`); received between 03:05Z and 03:20Z (bounded by this
seat's 03:04:31Z ls-remote read and its Monitor's 03:20Z expiry notice).
**Recorded by:** `0.1.0_DS_MarketIntelligence`, same turn, per `org/XXX.md` "Andrew-direct
instructions -- RECORD + BROADCAST".

---

## Verbatim

> I need you to look into why we surface the following in the Daily Cloud drilldown modal: ukraine train strike
> 10 articles [middle dot] 7-day rolling window
>
> [close glyph]
> Score
> -0.607
> Outlook
> Bearish
> [refresh glyph]
> Sentiment is evolving quickly
> Sentiment is evolving quickly -- the full AI read lands on the next scan refresh. Check back shortly.. We should have analysis for all items that appear in the Daily Cloud.

Three UI glyphs from the pasted modal are rendered as bracketed names to keep this file ASCII.
Every word is his, unedited, including the double period.

---

## Scope, as stated -- NOT adjudicated here

- An INVESTIGATION ask: "look into why we surface" the pending card for a Daily Cloud keyword.
- An OUTCOME statement: "We should have analysis for all items that appear in the Daily Cloud."

This record does not widen or narrow either. It gates no seat.

## Bearing on a prior ruling -- surfaced, not adjudicated

The pending card on evening keywords is produced by the GPT-cost gate recorded as *"gate
keyword-intelligence-generator to MORNING run only (Andrew 2026-06-11)"* (`903fbe9a8d`;
`infra/aws/lambda/news_trending_analysis/lambda_function.py:1584-1612`). Meeting the outcome above
requires lifting or changing that gate. That trade-off is his; this seat has put it to him with the
measured cost, and acts only on his answer.

## Measured at record time

- The Daily Cloud renders the first 20 keywords of
  `s3://opal-data-portal-v2/json/sentiment/keyword-sentiments.json`
  (`portal/src/components/market-performance/TopicCloud.tsx:135`, `.slice(0, 20)`).
- `news-trending-analysis` rewrites that file at BOTH daily runs (11:16Z and 21:16Z; bucket versions
  read). It invokes `keyword-intelligence-generator` only on the morning run -- its own live log,
  2026-09-13 and 2026-09-14 21:16Z: *"SKIP: keyword-intelligence-generator not invoked (evening run
  hour=21 >= cutoff 17 UTC) -- morning-only per GPT cost policy"*.
- 2026-09-14: the morning file's first 20 equal that day's 20 cached analyses (20 of 20). The evening
  run re-clustered and relabelled; only 7 of the evening's 20 visible keywords had any cached analysis
  in the proxy's 8-day lookback, so 13 of 20 served the pending card until the next morning run.
  "ukraine train strike" is one of them: 0 rows ever in `opal-keyword-intelligence` (the morning label
  for that cluster was "russia-ukraine conflict").
- The card itself is `_evolving_keyword_card`
  (`infra/aws/lambda/portal_data_proxy/lambda_function.py:1401-1437`, returned at `:1675` on every
  cache miss), introduced `09f361593c` (2026-06-10).
