# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 38

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T01:15:01Z**
Tick 37's log is `@2e76c3941a`. **Four acts: an Andrew-direct answered, a tool defect repaired
against the estate rather than against its own case, two rows this seat owed disarmed on measured
conditions, and a first-time finding on POSN.**

---

## 1. ANDREW-DIRECT, ACTION REQUESTED -- ANSWERED

His words, relayed verbatim: *"have them report exactly what was done on their box so i can have an
/exec-sum that shows the fwds for their respective two projects RESAPP and ASTTAX"*

**`ctoZ_ANDREW_FWD_REPORT_RESAPP_ASTTAX_20260913T0105Z.md` @`d5bbfb18ba`** (PUBLISHED), handed to
`0.0.0_AB_MSTR~Z` to carry. All 21 outcomes enumerated -- text in his terms, its BAR, its grade,
what was actually built, what it waits on. Plain language; no order ids, serials, hashes or tool
names; FWD ids kept, which is the one exception he asked for by name.

⭐ **THE COLUMN THIS SEAT ADDED BEYOND THE FOUR ASKED FOR, AND THE REPORT TURNS ON IT: each
outcome's BAR.** Without it "NOT REALIZED" reads as failure fifteen times. With it he sees that
**14 of RESAPP's 15 have a bar of *someone has actually done this*** -- and no amount of code
closes those. Across both projects **19 of 21 close only when a person uses the thing**, and the
thing is not in front of a person: RESAPP because publishing is frozen, ASTTAX because one decision
is pending. **The building is not the bottleneck; access is.** The two exceptions are named rather
than buried (RESAPP `FWD-9` needs only the page served; ASTTAX `FWD-4` needs only a scope decision).

**Two corrections made before sending, both from re-measuring rather than re-reading:** the draft
said RESAPP's work was all finished, which stopped being true when round 8 was cut minutes earlier
(43 of 46 finished, 3 running); and the opening line carried the combined 21-outcome figure against
RESAPP alone.

## 2. THE POSN FINDING -- TWO OUTCOMES WITH NO WORK CUT IN THREE ROUNDS

`FWD-4` (each class one colour) and `FWD-6` (the two screens agree) are **named by zero cut
orders**, measured over 15 order files against the 6-outcome denominator. Both were in the round-1
plan (`AT1-s-6`, `AT1-s-7`); neither cell was ever issued, and the round-2 and round-3 plans re-cut
around the classification defect without carrying them. Recorded as **NEVER GRADED**, per the
relay's explicit instruction not to infer a grade.

⛔ **AND IT IS RECONCILED IN THE REPORT WITH `4.0.0_SA_CRO~Z`'s CONTRIBUTION, WHICH WILL BE IN THE
SAME DOCUMENT.** That seat measured the PLANS against the outcomes and correctly found 6 of 6
covered. This seat measured the WORK ACTUALLY CUT and found 4 of 6. **Both numbers are right; the
gap between them is the finding**, and the body says so in one sentence so he does not derive it.
Two right numbers that look contradictory cost a reader more than one wrong number.

Nothing needs deciding tonight: POSN's L10 either puts them back into the work or records them out
of scope, and out-of-scope is a scope decision that goes to him.

## 3. THE TOOL REPAIR -- AND TWO WRONG FIXES BEFORE THE RIGHT ONE

**`.tools/to-check.py` @`5661885`** (PUBLISHED; lane ANY under `.tools/**`, NOT a LOOP_MECHANISM
file; commit-gate clean; `_extract_tag` untouched so the blast radius is the status field alone).

The defect: an unpaired backticked mention in the WORKER FACE (*"flip this file's `<status>` to
`complete`"*) opened a match that the record element's own closing tag then closed, so the
classifier graded prose -- first token a backtick, matching no word set, falling through to ACTIVE.

⭐ **TWO WRONG FIXES WERE WRITTEN FIRST AND BOTH PASSED THE CASE THAT MOTIVATED THEM:**

| attempt | what it did to the estate |
|---|---|
| "a status is a single bare token" | skipped legitimate PROSE statuses (SPRING-CLEAN closures) and, in a SET file of six orders, took a later order's status -- **six closed projects reopened** |
| "the non-nesting pair" | broke the MIRROR shape, where an element's content legitimately holds a backticked mention -- **130 active orders became 144** |

**What caught both: a same-instant A/B against HEAD's own copy over the WHOLE ESTATE, with the
prediction stated first.** The fix that held masks inline code spans to LOCATE the element, then
slices the value from the ORIGINAL text.
```
PREDICTION  exactly one project moves; the project SET is unchanged
RESULT      set identical (49 both sides); AMGT_RESAPP 9 ACTIVE -> 3 ACTIVE
            totals 130 -> 124, and 130 - 124 = 6, the six round-7 orders wrongly ACTIVE
```
⚠ **AND THE FIRST A/B WAS ITSELF BROKEN**, disclosed because it is the cheaper lesson: HEAD's copy
was extracted to the scratchpad, where `WORKSPACE = __file__.parent.parent` resolves outside the
repo, and it censused NOTHING -- returning a clean `0 active TOs, 0 projects` that reads exactly
like a real answer. The positive control (both versions must see a non-empty corpus) caught it.

## 4. `Z-S36` AND `Z-S42` DISARMED -- `Z-S50` @`950801db26`

Both on their own literal conditions, each with a control that fires:
```
Z-S36   to-check AMGT_RESAPP = 3   gate = 3 of 46    EQUAL
        CONTROL POSN_ASTTAX  = 4   gate = 4 of 15    EQUAL   (not both reading zero)
Z-S42   register D5 = 3            gate SUM = 3      EQUAL
        CONTROL  D4 = 6            gate SUM = 6      EQUAL
```
**What changed in the world, not just in the tool:** the register's D5 line read six open orders
against a true zero for most of tonight and now reads three against three -- a seat resolving scope
from the register gets the right number for the first time since round 7 began.
⛔ **NOT CLAIMED: that the two instruments share a DOMAIN.** `to-check` reads the FILESYSTEM; the
gate reads `git ls-files`. They diverge for any window in which orders exist on disk uncommitted --
legitimate, not this defect, and a future reader should check tracked-versus-disk before calling it
a bug.

## 5. ROUND 8 IS CUT, AND IT IS THE ANALYSIS'S RECUT INPUT

`2.0.0_SA_COO~ZZZ` cut, issued and spawned round 8 in the tick the L10 analysis landed: **three
cells at the consumer boundary** -- the consumer join, the incomplete read at the chart, and the
control shown to fire. Those are `C-S99`, `C-S98` and the owed `W11-S5` mutant: **the three inputs
this seat's round-7 analysis named, in the order it named them.** The L10 chain worked end to end.

## 6. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED · NO PITCH (unchanged; CVO-confirmed at tick 31)
  CARRIED   portal DEV push (its cost is now stated to Andrew in his own report) ·
            LIMB 6 widening · Bright Data proxy
  NOT-MINE  POSN round-3 four-of-fifteen · the half-hash mechanical-change carve-out (both MSTR's)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  3 OPEN of 46 -- round 8 running
  POSN_ASTTAX  active/EXECUTING  REACHABLE  4 OPEN of 15 -- round 4 not cut; L10 held
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
**Nothing in scope is blocked on this seat.** Both remedies the round-7 slug assigned here are now
discharged.

**Push state:** `origin/SITEZ 75348a0900` (ls-remote). `5661885` (the tool fix) and `d5bbfb18ba`
(Andrew's report) are **PUBLISHED**; `950801db26` (`Z-S50`) is LOCAL. Negative control `83cc87f29d`
reads NOT an ancestor. `HEAD:portal e85f6eb84f`, unmoved. No TO cut, no dispatch, no apply, no
merge, no promote.

## POSTSCRIPT -- WHY THIS LOG'S COMMIT IS LATER THAN ITS STAMP

Written at 01:15:01Z and committed at ~01:19Z. `safe-commit` REFUSED the first attempt, correctly:
`2.0.0_SA_COO~ZZZ` had an open merge draining worker `~14`'s `rg-3`, and the gate's own text is
*"wait for the merge to finish (a drain closes in its own time), then re-run"*. A merge state this
seat did not create is a peer's work in progress; it was identified by author and left alone. The
drain landed at `1dea673348` and this committed immediately after.
⚠ **The body above is the state AT ITS STAMP and is not rewritten:** it says AMGT 3 OPEN of 46,
which was true at 01:15Z. `rg-3` drained in the gap, so the live count is 2 of 46. A log records
its tick; the movement cursor comes from the COMMIT, never from the stamp or the filename.

## Compiler Tools

A same-instant A/B runner -- HEAD's copy of the tool extracted INTO `.tools/` so its
`__file__`-derived workspace resolves, both versions run back to back, per-project map diffed, with
a positive control that both see a non-empty corpus and a stated prediction · `_open_tos_for_project`
with `ZZZZ_NOSUCH` · `directives-check --json` for membership and its `open_tos` as the disarm
subject · a python `FWD-<n>` census over both projects' order files against each PRD header's
declared array · the decomp cell tables read for the plan-plane count · `git ls-files` /
`ls-tree` for tracked-versus-disk · `git merge-base --is-ancestor` against a fresh `ls-remote` with
`83cc87f29d` as the negative control · `commit-gate.sh` on the `.py` edit · `git show HEAD:<path>`
as the post-commit oracle with a `Z-S99` negative control · `safe-commit.sh -F`, every message file
written by a non-shell writer and checked ASCII-only.
