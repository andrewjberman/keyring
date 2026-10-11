# IRPT_BCKEND PRD v0.44 -- ratified-text review (CONTRACTS: the repeated-share rule's window is fixed)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @84fec7b9b4
(ADDENDUM v0.44; the CTO's message cites c525adc7e2, the PRD file's last commit is 84fec7b9b4). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 5895.
**Prior:** v0.43 SIGNED with the window as its open note.
**Verdict: SIGNED. The note on v0.43 is closed. One point for the producer's design, not a condition.**

## The note is closed

v0.43's "over the days of the grading run" is replaced: the window is the 40 trading days ending at the graded day, by the trading
calendar; fewer than 20 compared days in it gives no grade. A security-day's grade now depends on that day and the 40 before it,
and on nothing else.

This seat ran the module's tests: 54 passed. Among them are the three that carry the claim: the same security-day gets the same
grade whatever the length of the series; every day of a year of bars reproduces; later bars change nothing. Read by name, not
line by line.

## The three points the CTO asked to have attacked

1. **40, and the floor of 20, are chosen on one table.** Said so in the text, with the table: the set the rule takes stops growing
   from 40. For a rule that can only remove a grade, a stated choice with its table is enough. It would not be enough for a rule
   that admits.
2. **14 securities, seven of them on part of the run, with nothing measured against their moved bars.** The text says exactly that,
   and says the rule cannot tell a stale feed from a fund that does not move. A day it takes is blank. This is the design's
   standing limit, stated.
3. **The cost: 287 account-days and 2 accounts.** Stated, with the rule-off reproduction beside it. Not re-run by this seat.

The distribution v0.43 owed is given, and the text draws the right conclusion from it itself: the threshold sits where few
securities lie, 4 between four and six tenths.

## One point for the producer's design

The floor means a security has no grade from the second witness until its window holds 20 compared days. Two consequences the
next cell should carry, since it designs where the module is called:

- the reader must be given bars reaching 40 trading days before the first day it grades, or the first weeks of every run are blank
  for a reason that has nothing to do with the security;
- a security newly held, or newly listed, is blank for about its first month on this witness. That is the safe direction, and it
  should be visible as its own count, apart from the securities the rule takes for repeating.

## The sign-off instrument

The CTO reports the tool fixed at site Z (@41b9fa7e01) and not yet on dell2. This review, like the last four, was asked for by message.
