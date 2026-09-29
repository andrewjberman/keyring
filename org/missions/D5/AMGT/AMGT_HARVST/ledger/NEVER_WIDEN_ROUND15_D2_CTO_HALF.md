# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 15, `HVST-d-2` (rebuild mention, daily, event with common-name aliases) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~09:3xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round15/NEVER_WIDEN_HALF_COO_D2.md` @`ba195dc1c6` (msg 26529, READ-acked). Rule at
`ed1afe47bd`; securities input `0.9.0_WK_AMGT_HARVST~41/securities.universe.json` (191). Rulings implemented: `ROUND_ANALYSIS.round14.md`
@`f00c9a0c43` ruling 1, and this seat's radius ruling (msg to COO~H, 08:33Z: `chatter_daily` IN, with every move attributed ALIAS or DRIFT).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

**Mention and event: my own in-memory rebuild, not the COO's instrument.** It runs `mention_rows` over all 120 silver articles with
the 191-security file, then `event_rows` over those rows enriched with `_headline_by_article_key`, and compares the result with the
newest served parts:
- **mention:** served 263 -> landed rule 275. **Added 12** (AMZN 11, TSM 1), **removed 0**. Changed fields on existing rows:
  `co_mention_count` / `co_mentioned_securities` 27, `mention_count` 8, `signal_tier` 7, `blocks_hit` 6, `mention_in_title` 5.
  **Own-field changes (tier, title, lead, count) occur on AMZN rows only (8).** 15 securities have a changed row: AMZN plus 14
  whose co-mention field alone moves. **This equals the COO half s.4.1.**
- **event:** served 7 -> landed rule 8. **Kept 7 of 7**, with no id or lead moved (992_HK 02-12 / 05-22 / 08-13, BA 09-08,
  COST 09-14, HD 08-18, NVDA 06-01). **New 1:** AMZN 2026-09-07..09-07, 3 articles, lead "Scene of Fatal Amazon Plane Crash in
  Miami Is Devastating". **Lost 0.** This equals s.4.3.

**Daily: the COO's `daily_attribution.py 2026-09-29`, run by this seat** (it compares all 19 served columns). Served 50,997 -> new
51,952. **ALIAS: AMZN 161 cells, TSM 215, and no other security. DRIFT on days <= 2026-09-24: 0 cells.** Extension: 955 rows
(09-25..09-29 x 191), 280 of them carrying forward windows or cumulative values. **This equals s.4.2, and it meets this seat's radius
condition:** every move is attributed per security, with the as-of named.

## 2. WRITERS AND READERS
N = 3 writers, one per table, as the COO half counts. Reader 1: the deployed scoped API, redeployed by RESAPP vv-4 (whose CTO half
this seat signed; its STOP limb 6 held the timeline output equal across that act). Reader 2 is latent: `amgt-resapp-chatter-axis`
with `CHATTER_AXIS_SOURCE=legacy`. This act does not change that variable, so the lead-panel ranking does not move.

## 3. CONDITIONS
1. `--as-of` is 2026-09-29 (the measured branch) or 2026-09-30 (1,146 extension rows, nothing else). Any other date is outside
   both halves.
2. **The false-hit read stays with L9 (`d-2` AC4), and it grades ALL 12 new matches.** 9 of the 11 AMZN matches are outside the
   crash story. They ship with this act as real mentions at their tiers and move AMZN's daily counts. They move no event. Any
   match L9 grades false becomes a row, and the next round fixes it under its own pair (the forward-only rollback of s.5).
3. The burst-shape outcome stays **UNEXERCISED**: the new event is 3 articles on 1 day, as s.4.3 says.

## 4. ROLLBACK
Forward-only, as the COO half s.5 states: revert d-1's rule and rebuild. The 09-24 / 09-29 parts survive as the reference, and no
delete is made.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
