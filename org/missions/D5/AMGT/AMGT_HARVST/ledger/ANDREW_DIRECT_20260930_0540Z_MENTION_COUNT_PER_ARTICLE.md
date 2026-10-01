# ANDREW-DIRECT 2026-09-30 ~05:40Z -- a mention count per article, shown wherever articles are displayed

**Received by:** `2.0.0_SA_COO~H` at its terminal, in this session.
**Routed to:** `2.0.0_SA_COO~D` (frontend, DSGN_AMGTV1). Andrew picks up with that seat directly.

## Andrew's words, verbatim

> "Thats ok if its just one off mentions, but there should be a mentions counter wherever articles are displayed so that
> its clear at quick glance."

> "you dont need to worry about the frontend, just make sure that its documented per article, COO~D will take care of it,
> just get it handled on backend if not handled already and then issue an mcp on the subject to them, and I will pick up
> with them from there on the subject"

The context was HVST-o-5's Lenovo backfill: 22 new articles (bbg 11, wsj 11), some of them broad pieces that name Lenovo
once.

## Backend state -- measured 2026-09-30 ~05:4xZ, CLOUD `aa587798c4`

**The field exists per (article, company).**
- Gold `article_security_mention.mention_count`: the times the company is named in the article's text.
- Its siblings are `mention_in_title`, `mention_in_lead`, `signal_tier`, `co_mention_count` and `is_roundup`.
- Builder: `lib/research/harvest/publication_gold.mention_rows`.

**It is populated on every served row.** Measured on the served snapshot (`_latest_gold_snapshot_rows`):

| measure | value |
|---|---|
| served rows | 304, over 115 articles |
| `mention_count` null | 0 |
| distribution | 1: 97, 2: 63, 3: 31, 4: 30, 5: 23, 6-13: 60 |

**It is served per article on the article list the backend exposes.**
- Route: `GET /api/scoped/amgt/security/{key}/timeline/day` (`lib/research/harvest/timeline_api.py`).
- `ARTICLE_FIELDS` (:124-127) = `article_key`, `headline`, `publisher`, `signal_tier`, **`mention_count`**, `mention_in_title`,
  `mention_in_lead`, `published_utc`, `published_precision`.
- `_serve_article_row` (:144-) carries `mention_count` as the stored integer.
- The list is sorted by tier, then `mention_count` descending.
- The events route is UNMOUNTED (HELD), so no other served article list exists today.

**Gap:** an article in silver but not yet in the mention gold snapshot has no count. That covers the 22 new Lenovo
articles from HVST-o-5.
- They gain a count at the next `build_mention` rebuild, a served act under a never-widen pair.
- It is carried into HARVST's round-25 packet as a round-26 item.
- No backend code change is needed for the field itself.

## Relay

This record, plus one MCP message to `2.0.0_SA_COO~D` citing it. No gate is added and no other seat is bound; the scope is
Andrew's words above.
