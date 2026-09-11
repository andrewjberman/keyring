# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 23

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-11T21:10Z**
Short by intent: tick 22's log (`@9f68a8507a`) covers ticks 19-22. This records one external event
and two law edits.

## 1. LEG 1 LANDED -- and it verified the gate fix against a real act

`0.0.0_AB_MSTR~Z` @21632: merge `cefc55b6c7`, parents `932d83eb17` + `aa484f6b62`, **212 laptop
commits** now in this tree. Its report of the gate: *"surprise-row-gate PASSED under
`1.0.0_SA_CTO~Z`'s @dc8444a93b -- 87 carried IRPT rows exempt, 0 refused."*

⭐ **87 PREDICTED, 87 MEASURED, BY A DIFFERENT SEAT ON A DIFFERENT INSTRUMENT.** Before the merge this
seat simulated it by standing `origin/CLOUD` in for `MERGE_HEAD` and predicted exactly 87 rows carried
and exempt across 4 IRPT channel files. That is **corroboration rather than repetition** -- the first
time tonight a prediction of mine was checked against a real act instead of against my own re-run.
⚠ The 87-vs-100 gap stays unreconciled ON PURPOSE: 87 is ROWS, 100 was VIOLATIONS, one row can violate
on both limbs. Different denominators in kind; not a discrepancy.

**STATE IS LEG-OUTSTANDING, NOT PARITY** (leg 2 is the laptop MSTR's, that box in managed winddown).
This seat's `@49ddcc481d` and both PRD amendments rode that push and are ON ORIGIN.

## 2. TWO LAW EDITS TO `org/XXX.md` -- the file this loop re-arms from

**`@537fbff93a`** -- this seat's row now carries `[FABRIC: SITE-Z -- arm ONLY on site z]`. The union
merge left `:324` (laptop) and `:325` (site-z) both opening with the base serial `1.0.0_SA_CTO`, with
the fabric recoverable only from prose mid-sentence.
⭐ **BUT THE GUARD WAS MEASURED, NOT ASSUMED, AND IT HOLDS** -- step 0.2 refuses a cross-fabric arm:
laptop row **3 of 3** laptop, this row **2 of 2** site-z, **12 of 12** tree `project.json` carry
`fabric`. So the hazard `0.0.0_AB_MSTR~Z` warned every seat about is a READING hazard, not an
unguarded one. Told it so: an unnecessary worry propagates as fast as a real one.

**`@7f73b6d40e`** -- the substantive one. Found by `2.0.0_SA_COO~Z` (21639), routed by
`0.0.0_AB_MSTR~Z` (21640), **in the opposite direction from the one expected: not a wrong row, a
MISSING LIVE one.**
⛔ **Step 1b-F recorded ANDREW-DIRECT arms while claiming "every one is listed" -- a Rule 24 MECE
failure in the single source of truth for what runs unattended.** A loop can also be armed by a seat
CHOOSING to accept a recommendation, which is what Andrew's ~15:4xZ and ~20:0xZ words invited ("I
recommend", twice). Those arms are legitimately armed and were legitimately absent.
VERIFIED AT SOURCE BEFORE EDITING STARTUP LAW, all three:
```
only POSN mention in XXX.md  -> this seat's own :325 row. No COO~Z /drive row. Loop IS running.
NFRA_OPSEC202609             -> status=active dep_stage=CLOSED  (= that arm's own stop condition)
:326                         -> "so every one is listed."
```
Rule now enumerates by SUBTRACTION from "every loop running unattended on this device": **DIRECTED**
(an Andrew-direct word, quoted) vs **CHOSEN** (a seat accepting a recommendation).
⭐ **A CHOSEN ARM IS NOT A LESSER ARM** -- a different fact about a different authority; collapsing
them makes the table less trustworthy while looking more complete.
⛔ **AND A SEAT MAY NOT AUTHOR ITS OWN CHOSEN ROW.** `2.0.0_SA_COO~Z` declined to, rather than "dress
a recommendation I chose to accept in the authority of an Andrew-direct arm record". That judgment is
right, is now written into the rule, and is why this edit was the CTO's. Its POSN row is landed here
naming it as the chooser and citing 21613. Its spent OPSEC row is KEPT and marked, not deleted.
⚠ Written in because it confused two seats tonight: **A ROW IS NOT PROOF THE LOOP IS RUNNING.** It
records an AUTHORIZATION; liveness is `CronList` at the seat.

## 3. THE WATCH ITEM THIS LOG WAS GOING TO RAISE CLOSED WHILE IT WAS BEING WRITTEN

Mid-tick, both projects were WITHHELD on the SAME seat's brief re-sign (`4.0.0_SA_CRO~Z`, its 6th and
7th), and this section was drafted to flag that one seat's queue had become the single largest thing
standing between this scope and forward motion -- with the note that the L4-R law itself permits a
live COO to sign the brief half in the CRO's stead if it did not clear.
**It cleared. Measured at 21:19Z, both halves SIGNED and current on both projects:**
```
AMGT_RESAPP  v0.5 @932d83eb17   ratified SIGNED current · brief SIGNED current  -> ADMITTED
POSN_ASTTAX  v0.5 @49ddcc481d   ratified SIGNED current · brief SIGNED current  -> ADMITTED
```
⭐ Recorded rather than deleted, because the near-miss is the useful part: **folding seven amendments
into ONE commit per PRD is what made this two reviews instead of nine**, and the queue still came
within minutes of being the binding constraint. The L4-R gate did exactly its job at both ends --
WITHHELD the moment the bytes moved, ADMITTED the moment they were re-signed.

## 4. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 1 RESERVED (proxy vendor, CARRIED; pitched tick 22)
  -- unchanged this tick; 3.0.0_SA_CVO~Z acked and has begun AMGT round-5 L9.
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 in scope)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  ADMITTED
  POSN_ASTTAX  active/EXECUTING  REACHABLE  ADMITTED
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
Both projects are now unblocked at L4-R. Forward motion sits with `2.0.0_SA_COO~Z` (POSN round-3
re-decomposition + ONE issuance) and `3.0.0_SA_CVO~Z` (AMGT round-5 L9 dispositions, 51 rows).

**Push state:** LOCAL (`537fbff93a`, `7f73b6d40e`, this log). `0.0.0_AB_MSTR~Z` pushes origin/SITEZ.

## Compiler Tools

`prd-signoff.py status` · `safe-commit.sh` · per-project `project.json` fabric census (12 of 12) ·
the integrator's `ls-remote` read · `get_live_agents`.
