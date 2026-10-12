# IRPT_BCKEND PRD v0.47 -- ratified-text review (CONTRACTS: a day with no inputs stops only itself and the day after)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @2f003943f0
(ADDENDUM v0.47). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 6248. **Prior:** v0.46 SIGNED with this point open.
**Verdict: SIGNED. The point on v0.46 is closed. One note for the build.**

## The repair

Read as a diff against v0.46: answers 3 and 5 are replaced.

- A day's claim rows are written whenever that day's own inputs are present, whatever the prior day holds. No claim row is an input
  to another claim.
- The table stores claims only. Whether an account-day is served is derived at read from today's row and the PRIOR TRADING DAY's,
  by the calendar. One missing day costs two days, not every day after.
- A missed day is re-opened by the scheduled run inside seven trading days, and after that by the same producer run for a named
  day, on demand, writing that day's rows once.
- The proof gains the day after, and the day after that, and the re-opening.

All three things this seat asked for are there. Storing nothing derived is the better design: nothing stored goes stale when a
late day lands.

## The module, printed

This seat printed `date_basis_grading.py` lines 303 to 334. The CTO's reading is right: `serving_rule` takes `days`, "the ordered
graded days", and judges each day against `days[i - 1]`. Given a list with day D missing, it takes D-1 as D+1's prior, which the
contract now forbids.

## The note: the module's own rule and the contract now differ in one word

The contract says the prior TRADING day. The module's docstring and loop say the prior GRADED day. A builder who reaches for the
module's `serving_rule` with the list of days that have rows gets the behaviour the contract forbids, and its counts will look
right on any run with no gap. Two ways to keep them one rule: pass the calendar's trading days as `days`, so a day with no row
simply fails the membership test the loop already makes; or change the module and its docstring. Either way the build's cell
should say which, and the proof's gap case is what tells them apart, so it must be run through the same function the reader uses.
