# IRPT_BCKEND PRD v0.40 -- ratified-text review (CONTRACTS: the unmoved-bar guard on the second witness)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @6d12b3dd65
(ADDENDUM v0.40, from line 976). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 5625. **Prior:** v0.39 SIGNED.
**Verdict: SIGNED. Two notes, neither a condition.**

## The rule

The second witness gives no grade for a security on a day its own bar equals its bar for the prior trading day. A security-day no
witness grades is ungradeable. The first witness is unchanged.

It can only remove grades. A day it removes is blank, never served on a wrong basis. That is the safe direction, and it is aimed at
the one failure the record has shown: a carried-forward bar that a prior-close mark would equal.

## The figures, checked against the record

This seat read `deliverables/0.9.0_WK_IRPT_BCKEND~303/IB142-1_UNMOVED_BAR_GUARD_READ.md` whole and set each figure of the addendum
beside it. All match: blank 51.753 percent (50.305 without), never served 357, 552 account-days no longer freed, 1,135 of 64,536
overlap security-days not graded of which 1,071 had read equal; with the institutional class 46.298 percent and 283; six of its 71
outside securities un-graded on more than half their days, 79 of 85 at worst. The corrected sentence is right by the record's
Table 1: the five days sit in `Inst` (2) and `RIC/BDC / Not Available` (3), none in an admitted type.

The figures are the worker's; this seat re-ran nothing.

## What is right in the text beyond the rule

- **The admission test is read with the guard off.** Under the guard the one-day-off column is empty for every type by arithmetic,
  so it can no longer tell types apart. Saying so in the contract stops a later reader from admitting a type on an empty column.
- **The institutional class stays out.** A reader that repeats its bar on most days for a fund that prices daily is not carrying
  that fund. Removing the repeated days leaves the days it moves, and nothing measured says what those are.

## Two notes

1. **The text does not say what happens when the reader has no bar for the prior trading day** (the first day of a window, or a
   gap). A bar carried across a gap would equal the bar two days back and pass. The safe reading is no grade, and the earlier
   sizing already counted such rows as having no bar. One sentence would close it.
2. **The guard catches a repeated bar. It does not catch a bar that is a day late and still moves.** With the guard off the overlap
   shows 5 one-day-off days in 64,536 and all five are repeats, so no late-and-moving series was seen where both witnesses can be
   compared. Outside the overlap, where the second witness grades alone, nothing can be compared by construction. That limit is
   v0.39's and is unchanged.

## The sign-off instrument, again

`prd-signoff.py status` read this half SIGNED and current before this review: the addendum sits below the hashed sections. The
review happened because the CTO asked by message. Row IRPT_BCKEND-D2-S83 stands.
