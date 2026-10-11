# IRPT_BCKEND PRD v0.39 -- ratified-text review (ADDENDUM v0.39, the types the second witness may grade)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @90bfa5fc4f.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 5452. **Prior reviews:** v0.37 (REFUSED), v0.38 (SIGNED).
**Verdict: SIGNED, with two points the sizing cell must carry. Neither is a ground to refuse.**

## What this seat checked against the record

The record is not on the trunk. This seat read it at the branch commit the addendum cites
(`git show bfc0645151:deliverables/0.9.0_WK_IRPT_BCKEND~299/IB138-2_TYPE_OVERLAP_AND_FUND_CHECK_READ.md`, 92 lines).

| the addendum | the record, printed |
|---|---|
| seven admitted pairs with their counts | Table 1, lines 17, 20, 21, 23, 24, 26, 27: each count as the addendum gives it, each with 0 in the one-day-off column |
| `Inst`: 2 one-day-off of 1,474; `Not Available`: 3 of 8,596; 5 of 64,536 | lines 22, 25 and 28: as given |
| the cash pair has 0 days on which the close moved | line 16: as given |
| the untyped (141) and MIXED (54) columns are empty | lines 18 and 19: as given |
| 6,149 priced fund trades: same day 4,490, next day 0, prior 28, more than one 1,102, none 245, no bar 284 | line 58: as given, on the trade date at a relative tolerance of 1e-4 |

The test the addendum applies is the one this seat named at v0.38, and it is applied both ways: seven pairs pass it, and two fund
pairs with a non-empty column are kept out "on the smallness of the number" being no argument. The untyped and the mixed are kept out
though their columns are empty, because the finding has no class to travel on. A security with no bar is graded by nobody. Each of
those fails closed. `EXCHANGE_TRADED` is withdrawn for the source's own strings, so no token is invented.

The addendum also says nothing is cut before the record is on the trunk with its numbers unchanged. That is the right guard for a
text signed against an unmerged record, and this half is signed on that sentence.

## Point 1: "next day only 0" is true at one tolerance, and the record prints another

The addendum says of the fund trades "NEXT day only 0 ... and there are none". The record's Table 2 has four rows. On the trade
date at a relative 1e-4, the tolerance the witness rule uses, next-day-only is 0. On the trade date to the cent, it is 3 (line 59).

The 1e-4 row is the right one to cite, because it is the rule's own tolerance. But the text states "none" without saying at what
tolerance, and its own principle is that a small number in that column is still a number. Table 2 admits nothing by itself, so this
does not change what is admitted. The sizing cell prints both rows and says what the 3 are.

## Point 2: three of the admitted pairs rest on few securities

`RIC/BDC / Inv` is admitted on 2 securities and 83 moved days; `Retirement` on 4 and 107; `A` on 6 and 407. The test this seat named
did not set a floor, and the column is empty, so they pass it. But a date label is a property of how the reader serves a ticker, and
the admitted pair then carries the finding to every fund of that share class the first witness does not hold. The fund-trade table
is the evidence that reaches those funds directly. The sizing cell prints, for each admitted fund pair, how many of the 6,149 trades
and how many funds fall in it. A pair with no trade evidence of its own is named.

## What this seat read

The addendum in full (the PRD from its v0.39 heading); the record at the branch commit, its two tables, its five one-day-off rows
(lines 42 to 46) and its control line. Not run: the read itself.
