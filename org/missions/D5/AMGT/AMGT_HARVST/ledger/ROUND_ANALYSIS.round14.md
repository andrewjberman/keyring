# AMGT_HARVST -- ROUND 14 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~08:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26499, READ-acked, subject *"L10 SLUG AMGT_HARVST round 14
@365f6f47aa"*, citing `surprise-channel/adjudications/ADJUDICATION_v22.md`. Issuer packet
`round14/ROUND14_DRAIN_END_PACKET.md` @`f9f4378a8c`.

**Round 14 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

The held-out read ran: 130 rows over 50 securities, the five tuned securities excluded. **It forms 0 events**, so it gives no
precision grade, and round 13's 7 of 7 stays IN-SAMPLE. The CVO found one real burst the rule declined: **AMZN's fatal Miami
cargo-jet crash**, a story over several days, each article tier B, and "the rule never forms a story without a tier-A article".

## 2. THE CVO'S DECISION -- "measure why the lead misses" -- MEASURED BY THIS SEAT, AND THE PREMISE IS WRONG

Read on the served gold `article_security_mention` (263 rows), joined by `article_key` to the silver articles (120):

- **The articles are NOT headline-only.** All 120 carry body blocks. The five crash articles have 7-29 blocks and 256-1,019 words,
  all `live` / `complete_candidate`.
- **The LEAD hits and the TITLE misses.** "Amazon Cargo Plane Overshoots Runway in Miami, Killing Five" (bbg, 09-06): AMZN row
  `mention_in_title False`, `mention_in_lead True`, tier B. "NTSB Says Amazon Cargo Jet Hit Van ..." (09-07): title False, lead
  False, tier C (first mention at block 3). "Amazon Jet Tried to Abort Landing ..." (09-10) and the wsj and barrons pieces carry
  no AMZN title hit either.
- **Cause: AMZN's alias set is `['Amazon.com', 'Amazon.com Inc']`.** A headline says "Amazon", and the word-bounded matcher
  never finds "Amazon.com" in it. `universe_securities.securities_from_universe` builds aliases from the name plus
  `suffix_forms` (corporate suffixes such as "Inc"), and nothing strips a `.com` tail. The body says "Amazon.com Inc.", so
  the lead hits; the headline never does. **Tier A is unreachable for Amazon on any headline that uses its common name**, at
  any burst size.

So the gate to open is the ALIAS set, not the tier rule. The tier rule (title AND lead) stays as written.

## 3. RULINGS

1. **The alias floor adds the common name a registered name implies -- RULED, cell 1.** At minimum a `.com` tail is stripped
   (`Amazon.com` -> `Amazon`), and the cell first censuses the whole universe for other non-suffix tails that headlines drop,
   printing its denominator (names scanned, aliases added per rule). The existing `_usable_alias` guard still applies. The
   rebuild of `article_security_mention` and the events moves served gold, so it goes under a never-widen pair. The pair
   names every security whose rows move, and **reads a sample of the new matches for false hits** (a bare common name is
   looser than a registered one). Expected, and to be MEASURED at the pair, not assumed: the AMZN crash articles gain title
   hits, reach tier A, and form an event. That is the first held-out event and the first multi-day one. Its JUDGMENT (L9)
   is the round-13 question: one story, its own company, and a lead that names it.
2. **`Z-W40-S1` (name detection strips a single-story security's own recurring words)** travels with cell 1, as the CVO
   specified. The new "Amazon" alias is exactly such a word, so the cell reads the row first, and its criteria show that
   the AMZN burst is not lost to that strip.
3. **The burst-shape census stays as round 14 defined it** (>= 5 articles over >= 2 days). A 5-article multi-day AMZN event,
   if cell 1 forms one, is the first exercise of that shape. If it forms with fewer articles, the shape stays UNEXERCISED and
   says so.

## 4. FWD GRADES

`FWD-6` and `FWD-5`: NOT REALIZED, served half met, page half held by Andrew's *"lets hold on pushes and merges for now"*
(~20:3xZ 09-28, to `0.0.0_AB_MSTR~Z`). The others stand as `ROUND_ANALYSIS.round13.md` left them.

## 5. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 15 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Common-name aliases, then rebuild mentions and events** (rulings 1-2) | universe census of non-suffix tails with a denominator; `.com` at minimum; rebuild under a never-widen pair naming every moved security, with a false-hit sample read; JUDGMENT on every new event; `Z-W40-S1` read first |

**Fan-out:** 1 cell. **NOT cells:** the event route (`Z-W39-S1`, still not wanted); the portal push (Andrew's hold); the Seeking
Alpha 402 (the account holder's).

## 6. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- Read the Seeking Alpha subscription state (`Z-W37-S4`, HTTP 402) [entitlement].
- Lift *"lets hold on pushes and merges for now"* for the timeline panel push [a hold set by name].

## Compiler Tools
This seat's read of `publication_gold._iter_latest_articles()` (120 articles; body presence per publisher: barrons 15/15, bbg 19/19,
ft 14/14, sa 46/46, wsj 26/26) and `_latest_gold_snapshot_rows("article_security_mention")` (263 rows), joined on `article_key`,
printing tier, title/lead flags, first mention block and match forms for every row on the crash articles.
