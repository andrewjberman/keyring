# ANDREW-DIRECT 2026-09-16 ~01:0xZ -- POSN_AGGFIX: mark complete NOW and close it in the registries

**Received at:** the `2.0.0_SA_COO~Z` terminal, 2026-09-16 ~01:0xZ (Andrew, direct, in session).
**Recorded by:** `2.0.0_SA_COO~Z`. **Broadcast:** `1.0.0_SA_CTO~Z`, `3.0.0_SA_CVO~Z`, `0.0.0_AB_MSTR~Z`, same turn.

## THE WORD, VERBATIM AND ENTIRE

> "AGGFIX is basically done, I'm having CTO~Z run the final /prod-deploy and i want it marked complete now, please wrap it up and mark closed in the various registries."

**NOT ADJUDICATED WIDER OR NARROWER.** It names POSN_AGGFIX, it names the CTO~Z promote as already in hand, and it
orders the close. It says nothing about any other project, and this seat does not extend it to one.

## WHAT THE CLOSE MECHANICALLY REQUIRES, MEASURED RATHER THAN ASSUMED

`.tools/missions-tree-index.py` rule R6 (`close_violations`, `:438-492` @`9998f2a760`) refuses a `dep_stage: CLOSED`
row unless BOTH close documents exist for the same round, their fwd ids equal the PRD header's `endpoint_outcomes`
exactly, and every grade reads `REALIZED` at a `state_observed` no lower than the card's `done_when_state`.

**The schema splits the close across two seats by construction** (`org/standards/COMPLETION_REPORT.schema.json`):
`written_by` must match the COO serial pattern and `graded_by` must match the CTO serial pattern. So the COO cannot
write the grades and the CTO cannot write the report. This is not a gate anyone invented tonight and it is not this
seat holding Andrew's instruction up -- it is the L10 close as ratified (Andrew-direct 2026-09-03 ~05:2xZ,
"at least two agents have a chance of assessing the true finished status").

## WHAT THIS SEAT DID ON HIS WORD, THIS TURN

1. **`ledger/COMPLETION_REPORT.round1.json`** -- written, the COO's half. 8 outcomes (the PRD header's exact set),
   all `claim: COVERED`, **all 17 of 17 decomposition cells cited**, every cell carrying its terminal task order and
   that order's proof-of-spec at a commit pin. Schema: 0 violations. R6 with this report and the grades absent:
   exactly ONE violation, and it names the grades.
2. **Routed the grades to `1.0.0_SA_CTO~Z`** -- the one remaining artifact, with the R6 contract and the 8 rows it
   must carry, so that seat can land it beside the promote it is already running.
3. **The `dep_stage` flip is PREPARED, NOT LANDED**, and the reason is stated plainly below.

## WHY THE FLIP IS NOT IN THIS COMMIT

Flipping `dep_stage` to `CLOSED` before the grades exist does not mark the project complete -- it puts
`missions-tree-index.py check` into a REFUSING state for the whole tree (18 projects, 367 index rows), which every
other seat runs. That would convert "marked complete" into "the registry is broken for everyone", which is not what
he asked for and is strictly harder to undo than waiting for one file. Baseline before this commit: **0 violations.**
The flip lands in its own commit the moment the grades do, and this seat is not waiting on anything else to do it.

## REGISTER CARRIERS -- WHAT ACTUALLY CARRIES THE STATUS, MEASURED

`org/missions/DIRECTIVES.yaml:84` carries POSN_AGGFIX as a **bare member name** in its `projects:` list, with **no
status token**. The `POSN_AGGFIX[active]` that `directives-check` renders is DERIVED from `project.json`. So the
close needs **no DIRECTIVES.yaml edit**, and the Rule 27 question of who owns that carrier does not arise here.
The carriers that do move: `project.json` (`status`, `dep_stage`) and the generated flat index row, re-derived by
`missions-tree-index.py derive --write`.

## STATE AT RECORD TIME

Round 1 is L7-TERMINAL: 7 of 7 task orders `complete`, 7 of 7 proof instances VALID under
`.tools/proof-of-spec-check.py`, `dep_stage: ROUND_CLOSE` @`1750364833`. The edge gate is live
(auth-validator-edge v20 on 25 of 25 associations of EVTSA9VEHNZVH); the producer is deployed and its served result
read twice on different instruments. `1.0.0_SA_CTO~Z` opened the portal DEV to PROD freeze window at 01:05:21Z
(msg 23316, payload 7 files / 379 insertions to `be8cf218`); this seat holds every portal/DEV push per that ask and
has none to hold.

## THE ONE THING THIS CLOSE DOES NOT CARRY, STATED SO NOBODY INFERS IT DID

Round 1 never ran L8 compile, L9 adjudication or an L10 slug at `3.0.0_SA_CVO~Z`. The 28-row surprise channel has
**no CVO watermark**, and all 28 rows sit at disposition `UNDER_INVESTIGATION`. The close Andrew ordered is the R6
close on the endpoint outcomes, which is a different question from the channel's adjudication. Those rows do not
block the close and are not silently discharged by it; they remain owed and are named in the broadcast to
`3.0.0_SA_CVO~Z` so that seat is not left working a round it believes is open.

**Push state: LOCAL** (site-Z push hold, LD-0522).
