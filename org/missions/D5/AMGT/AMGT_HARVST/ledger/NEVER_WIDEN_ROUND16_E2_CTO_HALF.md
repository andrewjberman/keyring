# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 16, `HVST-e-2` (rebuild mention and daily with one-span-one-count) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~11:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round16/NEVER_WIDEN_HALF_COO_E2.md` @`604165a591` (msg 26577, READ-acked). Rule at
`5f25e64267` (the `e-1` drain, an ancestor of HEAD, verified). Ruling implemented: `ROUND_ANALYSIS.round15.md` @`ce26d1244b`, as
corrected by COO~H msg 26565 (the double count does move tier C, because tier C is `mention_count >= 2`).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT
- **Mention -- this seat's own in-memory rebuild** (`mention_rows` over 120 silver articles and 191 securities, against the newest
  served part): 275 -> 275; **added 0, removed 0**. Changed fields: `mention_count` 14 rows, `signal_tier` 8. **Moved rows by security:
  AMZN 8, UPS 2, DAL 1, FDX 1, GOOGL 1, GOOG 1 (14 over 6). Tier moves: all C -> D -- AMZN 2, UPS 2, DAL 1, FDX 1, GOOGL 1, GOOG 1
  (8).** No title, lead or A/B move. This equals the COO half s.4.1.
- **Events -- the same rebuild:** `event_rows` over the new mention rows keeps **8 of 8** served events (id and lead unmoved), 0 new,
  0 lost. This equals s.4.3; no event put is needed.
- **Daily -- the COO's `span_attribution.py 2026-09-29`, run by this seat:** 51,952 -> 51,952; SPAN cells AMZN 41, DAL 65, GOOGL 29,
  GOOG 29, UPS 24, FDX 24 (**212**); **DRIFT 0 cells** on all 19 columns; extension rows 0 at the 09-29 as-of; events from the new
  mention equal row by row, True. This equals s.4.2.

## 2. CONDITIONS
1. `--as-of` is 2026-09-29 (0 extension rows) or 2026-09-30 (191 extension rows, nothing else). Any other date is outside both halves.
2. No event put under this half. If the post-put event read is unequal, that is a BLOCKING row, and the remedy is its own pair.
3. The 8 C -> D rows are the intended effect: a mention counted once is below tier C's threshold of two. The judgment criterion
   reads the 09-06 crash report (count 10 -> 8, still tier A) and one C -> D co-mention article, as the round-15 ruling specified.

## 3. ROLLBACK
Forward-only, as the COO half s.5 states. Nothing is deleted.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
