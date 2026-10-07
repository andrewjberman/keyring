# AMGT_HARVST -- ROUND 48 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~07:0xZ

**Input:** CVO slug msg 29934, `surprise-channel/adjudications/ADJUDICATION_v60.md` @66ebf41775 (52 lines, read in full;
precondition MET; ARMED 0). Packet: `round48/ROUND48_DRAIN_END_PACKET.md` @a5f52a22b4.

## 1. WHAT THE ROUND DELIVERED

- **au-1:** the driver catches its upload timeout and writes the stop status and SUMMARY. PASS.
- **au-2:** `listing_empty_200` on a covered name is recorded as `soft_block`. PASS; the issuer's mutant fails as it should.
- **au-3, gold rebuild #6:** PASS (CTO half @0b26f965af). Mention part `part-20261006T060121Z` has 33,665 rows, with a `url` on 31,919:
  barrons, bbg and sa complete; ft 30 of 930; wsj 34 of 880. The 1,746 ft/wsj rows without one have no stored link. The order was
  stored links only.
- **The collection run:** every leg is still STOPPED (sa 9, barrons 130, bbg 104, wsj 154, ft 0 of 191). The declared set is EMPTY.

**Round 48 is CLOSED.**

## 2. THE BOARD (denominator 17)

Unchanged: **8 REALIZED** (FWD-2, 4, 5, 6, 8, 12, 16, 17). **9 NOT REALIZED as a qualified wait** on Andrew's presence (FWD-1, 3, 7, 9,
10, 11, 13, 14, 15): his hand-solve of each blocked leg's challenge, and the SA account answering 200 (AMENDMENT 2 @69ce080222).

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **RESAPP FWD-4's links for ft and wsj** ("an item followed out to its original"). Only 30 of 930 ft and 34 of 880 wsj items have a stored link | **A round-49 cell, measured before it is built, with NO publisher fetch.**<br>- First census the stored ft and wsj silver records: does each carry an identifier from which the publisher's own canonical article address is CONSTRUCTED, with no request made?<br>- **Where it does,** construct the url from the stored id, and prove it against the 64 items whose stored url already exists: they must be byte-equal.<br>- **Where it does not,** the item shows a plain "no link was stored for this article" and never a guessed or dead link.<br>- No ft.com or wsj.com host is contacted. Andrew's FT hold stands. |
| 2 | **The collection outcomes** | Unchanged (AMENDMENT 2). The round cuts no collection cell. A leg resumes from its own checkpoint as the issuer's act, once Andrew hand-solves it. |

## 4. ENRICHMENT LIST (round 49, ONE issuance by `2.0.0_SA_COO~H`)

1. **The ft/wsj link census, then the construction where stored ids allow it** (ruling 1). Any served gold write goes under a pair.
2. **The resume, when Andrew is present:** the issuer's act, not a cell. The per-leg report at the drain is read against the round-47
   card-5 rule (95% of the run universe).

## 5. ACTS FOR ANDREW (cited)

- **Hand-solve the barrons, wsj and bbg challenges while present** (collection-run condition 3).
- **The Seeking Alpha account:** its account endpoint answers HTTP 402 (his account).
- **The ft leg:** "Dont attempt FT until I return" (his hold, quoted).
