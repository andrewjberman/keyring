# CTO round analysis -- IRPT_DASHBD workstream B-IN, round 132

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-19 ~14:0xZ. **Slug:** `3.0.0_SA_CVO~IRPT` msg 10702,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v154.md` (C-S97, @b48dfc10d2).
**Drain-end packet:** `2.0.0_SA_COO~I2` msg 10693,
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND132_BIN_DRAIN_END_20261019.md` (@bddaac50dd).

## What the round proved

DB-i-19 drained, and DBI132-1-AC1 PASSES on the merged tree. On the Scope feed's first landed silver day (2026-10-16), the
wrapper's 795 PRESENT plus 68 ABSENT (39 / 17 / 12) equals the feed manifest's 863 accounts, with 0 unaccounted. The CVO
re-read it independently and matches v81. It was one snapshot read; nothing was written or deployed.

## What the round did not prove (limits, not passes)

- **(a) The boundary measure pairs calendar days.** `run_scope_feed_real.py:66-67` pairs day d with d + 1. Every
  Friday-to-Monday and pre-holiday boundary, about one in five, is never measured.
- **(b) The chain check needs a 238-day window.** `MIN_WINDOW_DAYS = 238` (`:45`). On the daily chain alone that is
  2027-06-10. The issuer's "three landed days" plan cannot reach it.
- **(c)** The null-start count differs from v81: 39 against 40.

## Rulings

1. **(a) The boundary pairs on the next TRADING day**, from `lib/trading_calendar.py` (CLAUDE.md: never judge a series
   gap without the trading calendar). A weekend or holiday is not a missing boundary.
2. **(b) The chain check is reached by the history backfill, not by waiting.** It is gated on IB-pn-5: the bronze-writer
   fix (my ruling @2f780e14a6), its ADDENDUM 5 pair, then the backfill run. Its earliest date is "the day after the
   backfill lands", stated as that dependency, never as 2027-06-10.
3. **(c)** The 39-against-40 difference is settled by the S60 membership read. Counts and hashed ids only.

## ENRICHMENT LIST for round 133 (the COO cuts it in one issuance)

| # | cell | risk | gate |
|---|---|---|---|
| E1 | The boundary measure pairs each landed day with its next trading day (`lib/trading_calendar.py`), with a test that a Friday pairs with the Monday and a holiday-eve with the next open day | LOCAL | none |
| E2 | The S60 membership read: which account moves between 39 and 40 null-start, by hashed id | LOCAL (read) | none |
| E3 | Re-run the wrapper on the first two landed trading days (10-16 and 10-19) with E1 in place; the boundary measure must report its pair count | LOCAL (read) | E1 merged |
| E4 | The chain check on the backfilled window | WORLD read | IB-pn-5 backfill landed |

**Close state:** round 132 MAY-CLOSE stands. E1 to E3 are cut now; E4 is carried as gated. There is no PRD addendum: no
FWD went unserved. The chain's FWD stays open on its dependency.
