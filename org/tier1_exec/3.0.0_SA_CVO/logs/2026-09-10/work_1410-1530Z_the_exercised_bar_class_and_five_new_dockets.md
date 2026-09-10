# 3.0.0_SA_CVO~Z -- work log 2026-09-10 14:10Z-15:30Z: the EXERCISED-bar finding, eight grades re-graded, and five new dockets cleared as they arrived

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

**Seat:** `3.0.0_SA_CVO~Z`, site Z, branch SITEZ. **Prior log:** `work_1145-1410Z_*` (this lane, this session).
**Loops:** zero crons; `/watcher` Monitor `bpo6oiomw` live. **Push state:** measured by ancestry against
`origin/SITEZ` -- the five commits through `055209ef7d` are ON ORIGIN; `8e472f2881`, `9e0e4e2af8` and
`27981a401e` were LOCAL at last read.

## Summary

Six commits. The window's substance is one finding that re-graded eight outcomes across a sibling project,
and then five separate dockets adjudicated as peers filed them. **All three projects end at 0 open.**

## 1. The EXERCISED-bar finding -- `Z-S19` @7577025b1e, `C-S14` @c72897a805

`1.0.0_SA_CTO~Z`'s L4 addendum held that no grader could have caught the specimen problem because "the
question was ABSENT FROM THE SPEC". It was not. `ROUND_ANALYSIS.round2.md:29-40` carries each outcome's
DONE WHEN beside its verdict: **eight of the eleven REALIZED grades sit on an `EXERCISED` bar.**

FWD-1 spells it out -- *"it has run on real trading mornings ... INCLUDING AT LEAST ONE MORNING WHERE THE
VERDICT WAS 'NOTHING'"*. That clause needs the verdict to DIFFER ACROSS MORNINGS, and a hard-coded
`ROW_FACTS` literal produces an identical verdict every morning BY CONSTRUCTION. It does not turn on what
"run" means, which is what made it decisive.

**UPHELD WITHOUT AMENDMENT @b75e35f36e. Eight grades REALIZED -> APPLIED. The project's true state is 3
REALIZED of 12, not the 11 of 12 that had reached Andrew.** Both artifacts edited in place.

The discrimination that made the row fit to file cut against my own case: `COMPLETION_REPORT.round3.json`
claims **COVERED**, not REALIZED -- a COO coverage claim, not a grade. I read the completion report first
and had to correct that conflation before filing, or a correct finding would have landed on an innocent lane.

**Filing shape, which the ruling seat named as the right one:** a ROW so it does not live only in an inbox,
PLUS a send because the addendum was mid-issue. A finding that arrives only as a message dies with the
inbox; one that arrives only as a row misses a cut already in flight.

## 2. Five dockets cleared as they arrived

| row | finding |
|---|---|
| `C-S7` `Z-S10` | `proof-of-spec-check.py` resolves against the tree the SCRIPT lives in; the refusal NAMES THE WORKER |
| `C-S8` `Z-S11` | two IAM-r-6 bars CANNOT FAIL; one `-i` flag is the whole distance between "measured 0" and "reads 3" |
| `C-S9` `Z-W6-S2/3/4` | a SET whose label asserts what one member lacks; a CRITERION scoring the TOOL's vocabulary; a WRITE SURFACE that is the wrong custody home |
| `C-S39` `Z-S172` | FWD-19's DONE WHEN carries the same unsatisfiable clause I voided in S1-AC4 -- caught BEFORE the grade |
| `C-S10` `Z-W5-S1/2` | second independent arrival at C-S8's defect, supplying the grading instrument; and independent confirmation of C-S9's "five, not four" |

**`C-S39` is the one that matters most, because it is the first time this class PREVENTED a wrong grade
rather than corrected one.** `2.0.0_SA_COO~Z` took the sibling project's re-grade as a CLASS and ran it
against its own PRD -- explicitly *not* by re-reading its own artifacts, which would not have surfaced it.
I added one step the row did not claim: `comp-read --enumerate 'refused or challenged'` returns 2 hits, and
**`:219` is the OUTCOME'S OWN HEADLINE**, not a second mention of the bar. Amending the DONE WHEN alone
leaves FWD-19's *name* asserting a behaviour its own constraints forbid.

And the adjudicative consequence, stated so the L4 decision is framed: if clause 1 stands, FWD-19 cannot
reach REALIZED -- the honest grade is APPLIED. **Doing nothing is not one of the available routes.**

## 3. Two corrections against myself

- **My S1-AC4 void stopped one level short.** C-S37 voided it as the criterion's defect. The census reads
  'refused or challenged' 2x in the PRD and 2x in the order, and 'refusal or challenge' 0x in the PRD and 3x
  in the order -- **the criterion was FAITHFUL to its spec.** Z-S169 called it the issuer's defect, the
  issuer accepted that, and both of us were one level short. Voiding it is what removed the pressure to look
  upward.
- **C-S6's "FOUR inline policies" was `main.tf`-scoped and I did not say so.** Module-wide it is FIVE
  (`main.tf` 4 + `qa-scratch-instance.tf` 1). The finding HOLDS at the right denominator -- an exhaustive
  sweep of the module's only two .tf files returns `aws_iam_role` declarations 0 and 0. `Z-W5-S2` reached
  FIVE independently at 14:05Z on a different instrument, and added a THIRD count: round 1 recorded THREE.
  **One state, counted 3, 4 and 5 by three cells, and I produced the 4.**

## 4. Blockers met and cleared -- both correct refusals, no override taken

- **INDEX-DRIFT.** A stale `dep_stage` on `org/projects/NFRA_REPORT.json` (index `ROUND_CLOSE` vs tree
  `EXECUTING`) refused commits on an **unrelated project**. Not my lane, no override exists ("never bypass").
  Routed; it cleared at 14:40:53Z when `2.0.0_SA_COO~ZZ` cut round 4 -- the act I predicted would reconcile it.
- **A FOREIGN MERGE**, twice, from worker drains. `safe-commit` refuses correctly during a merge and there is
  deliberately no override. Held rows were backed up outside the repo each time and landed after.

⛔ **A structural note the CTO seat has taken as a gate-design item:** the blocker prevented filing the
surprise row that would record the blocker. Every durable carrier in the channel lives under `org/missions/`,
so a gate refusing all of `org/missions/` **refuses its own incident record**.

## 5. Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| surprise-row-gate.py | imported throughout | PASS | the gate's own builder as the instrument |
| comp-read --enumerate | CLAUDE.md, the OPSEC PRD, two .tf files | PASS | every zero paired with a positive control in the same run |
| comp-find | locating orders, PRDs | PASS | found `task-orders/` (hyphen), not the assumed `task_orders/` |
| safe-commit.sh | 6 commits | PASS | **zero overrides this window** |
| git (ls-tree, show, merge-base) | cut-vintage reads, push state | PASS | ancestry, never a tip hash |

**What worked:** treating every refusal as a measurement. Three refusals this window (corpus, register,
merge) and all three were CORRECT; none needed an override, and locating each one produced a finding.

**What failed:** I reported a commit as landed when `safe-commit`'s tail had printed a reminder block rather
than its verdict. The repository said otherwise -- `git status` showed the file still modified. **A tool's
stdout is the tool describing itself; git log is the repository answering.** Caught before it reached a
message.

**Gap found:** my blocker message went to three recipients and the lane guard REFUSED it, writing nothing
for anyone. I hold a banked note reading "CVO~Z reports to CTO~Z, never MSTR" and addressed the register
holder anyway, because the gate's remedy line named that lane. **A guard caught what a banked lesson should
have.**

## 6. The pattern this window measured

Four seats reached parts of one defect without coordinating -- the issuing lane against its own frozen
issuance, a worker from its pre-edit baseline, this seat at the cut vintage, and a second worker converging
with this seat on a policy count. **None found it by re-reading a deliverable.** Every one found it by
RUNNING AN INVOCATION AND COMPARING THE NUMBER TO WHAT THE DOCUMENT CLAIMED -- the one act a green proof
instance never performs on itself.

## Blockers

None at this lane. All CVO limbs on all three projects are DISCHARGED.

## Current State

- **NFRA_OPSEC202609:** 179 items, **0 open**, 115 GRADUATED. Round-3 L9 discharged. NO SLUG CUTTABLE --
  `TO-OP3-S-2` staged on an SNS confirmation only Andrew can action, ~68h left at the CTO's 14:14Z read.
- **NFRA_REPORT:** 31 items, **0 open**. Round 4 cut @20327a663f into four cells; `RP-s-23` is the deploy
  cell whose one deployment exercises all eight re-graded outcomes at once.
- **NFRA_IAMROLES202609:** 28 items, **0 open**, 25 GRADUATED.
- **A standing commitment:** `Z-S11`'s disarm is MINE and deliberately left ARMED -- at IAM-r-6's L9, AC1 and
  AC3 are NOT credited, and AC1 is graded from the case-SENSITIVE per-token census `Z-W5-S1` supplied, never
  from AC1's own case-insensitive count. NOT CREDITED IS NOT GRADED FAIL.
- 35 commits this session. Inbox acked through msg 20968. Watcher `bpo6oiomw` live; zero crons.

## Next Steps

- [`2.0.0_SA_COO~Z`] `TO-OP3-S-2` is the only thing between round 3 and a slug, and its input is a mailbox.
- [`1.0.0_SA_CTO~Z`] FWD-19's clause 1 -- amend, read as satisfied by a different mechanism, or grade FWD-19
  APPLIED; whichever route, the headline at `:219` must travel with the bar at `:221`. Also the
  graduated-to-remediation join (9 ARMED items measured earlier), and the proof-of-spec schema question from
  `Z-W6-S3`.
- [`2.0.0_SA_COO~ZI`] the criterion-cutting pattern (`Z-W5-S1`), now at two instances in one round.
- [`3.0.0_SA_CVO~Z`] L9 on IAM-r-6 when it drains; the OPSEC round-3 slug the moment `TO-OP3-S-2` goes
  terminal. Nothing before that.
