# IRPT_BCKEND PRD v0.46 -- ratified-text review (CONTRACTS: C-DBPRODUCER, the date-basis producer)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @3f577ef37f
(ADDENDUM v0.46). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6244. **Prior:** v0.45 SIGNED.
**Verdict: SIGNED. One point that the text must settle before the build's cell is cut, and one smaller.**

Nothing is served by this addendum. It is a contract for a build, and the build waits on three reads.

## What is right

- **The bars come from a landed, scheduled source, and the landed prices store is refused as that source.** It covers 0 of the 85
  graded days and nothing writes it. There is a second reason, measured today in another project and reproduced by this seat:
  that store's close for funds whose price was not replaced is about three quarters of the traded price going back. A close like
  that dates nothing. The refusal stands on either ground.
- **The claim has its own table,** written once per account-day, never back into a landed partition.
- **A blank day is a row.** "Not yet graded" is no row; "graded and not served" is a row. A reader cannot confuse them.
- **A pass stopped partway writes no day as complete,** and the grading step then writes no claim for that day.
- **No new vocabulary;** the source declaration does not change until claim rows exist for 20 consecutive trading days.
- **Row W313-S3 is named and not papered over:** a served reader that chains across a day it did not measure and still says
  measured, for two other firms. Left unchanged here for a stated reason, and read first.

## The point: one day with no inputs must not stop every day after it

Three sentences of the contract, read together:

- answer 4: each run grades the days of the last 7 trading days whose inputs are all present; a day whose inputs never arrive stays
  without rows;
- answer 5: the prior day's claim is read from the claim table; no row for the prior day means the day is not graded;
- answer 3: "not graded" is no row.

Take a day D whose bars or holdings never land. D has no rows. Day D+1 has its inputs, but its prior day has no row, so it is not
graded: no row. Then D+2, for the same reason. Read literally, one missing day leaves every later day without a row, and after
seven trading days D is outside the catch-up window and is never looked at again. The table would stop, silently, and "nothing
alerts" is the contract's own sentence.

This seat does not think that is what is meant. The module's serving rule needs a good claim today and the prior day, which
suggests D+1 should be written as a ROW that is not served, so the chain restarts at D+2. But the text does not say so, and a
builder will have to choose. The proof as written would not catch the wrong choice: it withholds one day's bars and checks that
day has no rows; it does not look at the day after.

What the text needs, in a sentence each:
1. what day D+1 WRITES when day D has no row: a row with a not-served claim and its reason, or nothing;
2. what happens to a day that leaves the 7-day window with no rows: it stays empty for ever, or a stated act re-opens it;
3. the proof gains the day after the withheld day.

## The smaller point: a read on demand in place of an alert

"Nothing alerts" is right under the standing rule against new monitors. A gap nobody can see is still a gap. The contract file
the build's first cell writes should name the one read a seat makes to see it: per day of the last N trading days, the count of
accounts with a claim row beside the count with a holdings row.

## The sign-off instrument

The fixed tool flagged this half's text as changed since signed, before this review.
