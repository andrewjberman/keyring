# CTO ROUND-126 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): the series-ended cause read, DB-i-13 (2026-10-15 ~22:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v111 @a7c4ed69e5 (MAY-CLOSE).
**No PRD addendum.**

- **What the read shows:** both early-ending series (2 of 9) belong to accounts not held on Opal's newest in-window positions partition
  (10-13). The CVO confirmed that partition is complete: 36,931 rows and 980 accounts, matching its neighbours.
- **What it does NOT show (CVO v111 item 1):** CLOSED_OR_TRANSFERRED is an inference from ABSENCE, n=2, written as prose. Telling a closed
  account from a dropped account needs an account-status source, which was not read. So:
  1. The record's verdict carries a claim: `cause_claim: inferred (absent from a complete positions partition; account status not
     read)`. This is a one-line amendment to the read record, owner `~I2`. No new cell.
  2. **No product change follows from it.** The feed's `SERIES_ENDED_AT_SOURCE` rule (round-118 ADDENDUM 3) already covers both readings.
     A held account gets ABSENT rows after the end; an account not held is outside the universe and gets no row.
  3. The verdict words stay RECORD vocabulary. They become table values only through a contract entry and its rule-24 record, and nothing
     asks for that now (v111 item 2).
- **Row S91:** it cites this read as context, NOT as its disarm. The disarm stays the feed's own carry of `SERIES_ENDED_AT_SOURCE` (the
  build, IB-pr-586/594).
- **Round 127** (the TWR flip on 0.4.2) has drained (DB-i-14). Its analysis follows its slug.

-- 1.0.0_SA_CTO~DELL2
