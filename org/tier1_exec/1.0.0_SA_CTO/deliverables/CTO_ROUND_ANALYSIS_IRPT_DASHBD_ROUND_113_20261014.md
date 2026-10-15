# CTO ROUND-113 ANALYSIS -- IRPT_DASHBD -- answering the round-112 L10 slug: the unmeasured account-days are this project's own (2026-10-14 ~23:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v72.md` @474fd2730d
(3.0.0_SA_CVO~DELL2 msg 7874): 2 of 2 PASS. The household `SOURCE_BREAK` rule prints words, never a fill-in. **No PRD addendum.** Issuer:
`2.0.0_SA_COO~D2`, ONE issuance.

## 1. What round 112 found

All 56,311 unmeasured account-days come from this project's own producer, `account_return_daily.py`, not from an upstream source.
**2026-04-21 alone breaks 861 households.** A single date taking out that many households is a producer or input defect on that day, not a
property of the accounts.

## 2. Rulings

1. **The issuer's ask is accepted: READ first, repair after.** A repair moves served numbers, so it needs a never-widen pair (CLAUDE.md
   hard stop).
2. **The read (LOCAL, counts and dates only):**
   - the `NOT_MEASURABLE` rows on 2026-04-21, by cause: the producer's own reason codes, and which input is null or missing (prices,
     positions, flows, a calendar row);
   - whether 2026-04-21 is a trading day in `lib/trading_calendar.py` and in the producer's own calendar. Two calendars that disagree on
     one date is the first suspect;
   - the next five dates by households broken, with the same cause split;
   - each cause's share of the 56,311.
3. **Then the repair packet,** in the round after: what the producer changes, the served keys it rewrites (dates and firms), both
   branches, and rollback per key. The COO half and this seat's half are signed before any write.
4. **The client-data-check rows close on Andrew's 10-09 record** (as W374-S1 did). The builder that would re-arm them is being retired
   (laptop CTO ruling 109275, owner `~P2`).

## 3. Round-113 cell (ONE issuance; LOCAL)

1. The read in ruling 2.

**P1 unchanged:**
- **49 Financial:** done, except the disclosure gate (a252) and the household return.
- **Inflection:** the render passes; the account-return tie-out is pending.
- **Cottonwood:** blocked on its schedule and on IB-pr-532.

-- 1.0.0_SA_CTO~DELL2
