# AMGT_HARVST ROUND 41 -- L8 COMPILE + L9 JUDGMENT -- FWD-16 tone is the scorer's own output on all 31,042 gold rows; FWD-6's 507 events are real stories (78 of them one company's story under two listings); L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-03 ~23:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round41/ROUND41_DRAIN_END_PACKET.md` @`94c659696c` (3,864 B, read to EOF), msg 29065.
**Authority:** Andrew-direct ~20:3xZ, "yes to all recommendations" (`ANDREW_DIRECT_20261003_20xxZ_YES_TO_ALL_SEVEN_OPEN_CALL_RECS.md`
@`9fe6e6f111`). Its card 2 is "HARVST: run FinBERT scoring over the stored articles, and the event rebuild", with "a served gold move
takes its never-widen pair". FT collection and STOP_FT are not covered and are unchanged; 0 collectors ran.
**Orders:** three issuer direct acts, an-1 to an-3, all done. Both gold moves carry a signed pair (COO `72f2c9be42` / CTO `8e0fed682a`).

## 1. FWD-16 -- is the gold tone the scorer's own output? YES, on every row

This seat read S3 `opal-data-harvest` itself:
- **The scorer's store.** `amgt/harvest/gold/article_sentiment/` holds 5 parts and 13,235 rows: **13,224 scored texts** keyed by
  `text_sha256`, plus 11 unscorable markers ("no title and no text_blocks"). Scorer `opal-news-ai-sentiment`.
- **Served gold.** `article_security_mention/date=2026-10-03/part-20261003T222707Z.parquet` holds **31,042 rows**: positive 12,117,
  negative 10,034, neutral 8,891. `sentiment_scorer` is `opal-news-ai-sentiment` on 31,042 of 31,042.
- **The join.** Every gold row's `sentiment_content_key` was looked up in the store: **31,042 match label and score, 0 mismatch, 0 key
  absent, 0 null tone.** The tone on gold is the scorer's own record, carried and not re-derived.
- **Plausibility, 8 random headlines.** 7 read right, e.g. "Micron's stellar results provide lift across semiconductor sector" +0.95,
  "'Crisis of Confidence' Grips Indonesia Stocks After MSCI Warning" -0.92, "Goldman Sachs top 30 mutual fund overweight holdings"
  neutral. 1 is debatable: "Notable analyst calls this week: Pfizer, AMD and Intel among top picks" scores -0.52. That is FinBERT's
  own call and is carried as served.

**Grade: FWD-16 PASS in gold.** It is not yet served to the page: RESAPP's chatter route serves `tone` null with a reason until its next
deploy, and FWD-17 (window tone) was not built this round.

## 2. FWD-6 -- are 507 events a faithful set of news stories? YES, with one counting caveat

`chatter_event/date=2026-10-03/part-20261003T230450Z.parquet`: **507 events over 68 securities.**
- **The rule holds on every event.** `publishers_distinct` min 2 (median 2, max 4); `tier_a` min 2; `articles_total` min 2, median
  3, max 31; `days_span` 1-13. 0 events have fewer than 2 publishers, and the packet reports headline null 0.
- **10 sampled events read as real company stories:** "Emirates NBD Said to Be in Talks to Buy HSBC's Turkey Unit"; "Netflix has cash
  to raise bid for Warner Bros. in fight against Paramount"; "Unilever Seeks Buyers for Iconic British Mustard Brand Colman's"; "Roche
  Backs Full-Year View as First-Half Sales Rise"; "Spotify Users Climb; Third Quarter Forecast Misses Estimates".
- **The counting caveat.** 89 events share their lead headline and first day with another security:
  - **78 are one company's story under two listings:** BP/ LN + BP US 33; HSBA LN + HSBC US 14; ASML NA + ASML US 13; ULVR LN + UL US
    9; ROG SW + RHHBY US 8; ICICIBC IN + IBN US 1.
  - **11 are genuine stories about two companies** (Hon Hai + Nvidia, JD + Amazon, Visa + Mastercard ...).

  On each listing's own page the event is correct. As a count of distinct stories, 507 is per listing: about 429 distinct company
  stories. `composite_figi` is null on these rows, so nothing groups the listings.
- **The 2-publisher rule's other face** (packet section 3): AMD and VLO serve 0 events because their tier-A coverage comes from one
  publisher (sa: 45 and 37). That is the rule's answer, not a gap.

**Grade: FWD-6 PASS** on the served events, with the per-listing count named.

## 3. Note on scope

an-2's rebuild re-derived gold from current silver, so mention grew 23,691 -> 31,042 (sa +7,043, bbg +308). These are silver rows from
backfills that had already finished: the ~17:3xZ record reads "every backfill finished (sa 89/89 at 2026-10-03 04:46Z)", and 0
collectors ran this round. The pair signed it knowingly, within card 2's "a served gold move takes its
never-widen pair". Recorded so the growth is not read as new collection.

## 4. L10 PRECONDITION

All three acts are done. No rows were filed this round, and none is open BLOCKING or ARMED for HARVST (ARMED 0 since v51). The two
judgment limbs are graded above. **MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S71",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T23:37:00Z",
    "one_line": "Round 41 L9: FWD-16 PASS in gold -- all 31,042 gold mention rows carry tone equal to the scorer's own article_sentiment record for their content key (13,224 scored texts; 0 mismatch, 0 absent, 0 null), scorer opal-news-ai-sentiment on every row; FWD-6 PASS -- 507 served events over 68 securities, every one with >= 2 publishers and >= 2 tier-A articles, sampled stories read as real news; 78 events are one company's story under two listings (BP, HSBC, ASML, Unilever, Roche, ICICI), so 507 counts per listing (~429 distinct company stories).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest amgt/harvest/gold/article_sentiment/ (5 parts, 13,235 rows; 13,224 text_sha256 keys, 11 unscorable).",
        "amgt/harvest/gold/article_security_mention/date=2026-10-03/part-20261003T222707Z.parquet: 31,042 rows; labels 12,117 / 10,034 / 8,891; join to the store by sentiment_content_key = text_sha256: 31,042 match.",
        "amgt/harvest/gold/chatter_event/date=2026-10-03/part-20261003T230450Z.parquet: 507 events, 68 securities; publishers_distinct min 2; 89 lead-headline+first-day pairs shared across securities, 78 of them dual listings of one company.",
        "ANDREW_DIRECT_20261003_20xxZ_YES_TO_ALL_SEVEN_OPEN_CALL_RECS.md @9fe6e6f111 card 2."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The round's two judgment limbs read PASS on the served artifacts; no act is owed for them.",
    "spec_asserts": "FWD-16: the tone on gold is the scorer's output; FWD-6: bursts of real coverage appear as marked events with a headline.",
    "world_is": "Both true on the served artifacts; the event count is per listing.",
    "notes": "FOR THE CTO: grade FWD-16 (gold) and FWD-6 on this read; see Z-C-S72 for the per-listing count."
  },
  {
    "id": "AMGT_HARVST-Z-C-S72",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T23:37:00Z",
    "one_line": "Enrichment: one company's story is served as an event under each of its listings (78 of 507 events: BP/ LN + BP US 33, HSBA LN + HSBC US 14, ASML NA + ASML US 13, ULVR LN + UL US 9, ROG SW + RHHBY US 8, ICICIBC IN + IBN US 1) and composite_figi is null on these rows, so no field groups the listings; correct per page, but any cross-security count (events, chatter) double-counts these companies.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "chatter_event part-20261003T230450Z: (lead_headline, first_day) groups with >1 security_key, by pair: 33, 14, 13, 9, 8, 1 (dual listings) + 11 multi-company.",
        "composite_figi None on the dual-listed rows read."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A cross-security count counts each company once.",
    "world_is": "Six dual-listed companies count twice.",
    "notes": "A company-level key (e.g. a populated composite_figi or an issuer id) would let any aggregate collapse listings; per-security pages are unaffected."
  }
]
```

-- 3.0.0_SA_CVO~Z
