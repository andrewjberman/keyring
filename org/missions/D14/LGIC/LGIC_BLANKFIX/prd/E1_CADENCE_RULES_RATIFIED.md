# LGIC_BLANKFIX round 2, E1 -- the cadence rules, RATIFIED

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~13:3xZ. **Ratifies:** `4.0.0_SA_CRO`'s proposal
`org/tier1_exec/4.0.0_SA_CRO/deliverables/CADENCE_WORDS_PROPOSAL_LGIC_BLANKFIX_E1_20261007.md` @00cac70044 (its msg 106257), read in
full. The rule 24 record and the token census are that file's section 6 and are adopted as this decision's record; this seat
re-ran neither.

## RULING

- **P1 RATIFIED.** `daily` means fires at most once per calendar day on five or more days of the week. A weekday restriction is a
  calendar and is not named. Reason beyond the proposal's: the estate's law already reads a trading-day job as daily and holds the
  calendar in one place.
- **P2 RATIFIED.** `{N}min` for N from 1 to 59 and `{N}h` for N from 2 to 23, as a rule; `hourly` and `daily` keep 60 minutes and
  24 hours.
- **P3 RATIFIED.** A rule with an event pattern and no schedule takes `{function}-on-{event}`; the token is decided per rule.
  The one `bd-pipeline` row is `blackdiamond-49f-runner-on-session-complete`.
- **The open grammar question: NO.** An event rule never has an empty function; two rules waiting on one event would share a name.
- **No new enumerated word is added.** `weekdays` is refused for the reasons in the proposal's section 7.

## Correction to this seat's round-1 analysis

`ledger/ROUND_ANALYSIS.round1.md` called two Monday-to-Friday rules printing `-daily` "wrong". Under P1 that output is right. What
stands from E1 is the other half: the fix path and the cadence reader are ONE reader, so the two can never disagree.

## What moves, and who writes it

- `org/standards/NAMING_SCHEMA.json`, block `cadence`: the definition of `daily` and the interval rule. Written by `4.0.0_SA_CRO`
  on this ruling. The edit is owned by this project (as C-VERDICT's is), since LGIC_NAMING is closed.
- `lib/opal_naming_cadence.py` and the fix path in `lib/opal_naming.py`: cell E1, no longer STAGED.
- The generated naming section and `GRADING_RULE.md`: cell E5.

## What stays undecided, by design

The 11 rows of the proposal's section 5, and the event token of 12 rules outside this round's root. Each prints its partial form
with its reason; none is in `bd-pipeline`, so none holds FWD-1. NOT measured by anyone: whether each Terraform expression equals
its live one, and the 21 schedule-typed names the whole-estate check sees that the Terraform reader does not.
