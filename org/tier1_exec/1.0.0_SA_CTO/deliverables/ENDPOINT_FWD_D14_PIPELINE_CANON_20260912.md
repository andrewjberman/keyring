# ENDPOINT (step 2, `/endpoint --forward`) -- D14, the pipeline canon

**v2 of this endpoint, cut 2026-09-12 from brief v2.** v1 was cut from brief v1 @`2659d45788`.

> **NOT YET LANDED IN A PRD.** No project exists and no PRD exists, so this block is emitted ready
> to paste. Its home is the D14 PRD under a section titled exactly `ENDPOINT (step 2, /endpoint
> --forward)`, because step 10 reads it back to answer *"does the PRD name this outcome?"*

**Cut by:** `1.0.0_SA_CTO` (L2). **From:** `docs/briefs/d14-pipeline-canon-brief-20260912.md`
@`2663f120be`, 18,455 bytes as the record stores it, author `4.0.0_SA_CRO~D`, mode NEW (greenfield).
**Andrew has NOT read either version of the brief.** His 2026-09-03 word is that he confirms the
CTO's DONE WHEN from this pass; if he amends the brief, this endpoint re-cuts from the amendment.

---

## AMENDMENT RECORD -- WHAT MOVED FROM v1, AND ONE CORRECTION

`4.0.0_SA_CRO~D` reported brief v2 with this headline: *"Part I -- the six outcomes -- is UNCHANGED,
and that is a finding: the seven artifacts were built against v1's outcomes and none moved."*
The brief's own Part I heading reads `THE OUTCOME TERRITORY (unchanged from v1)`.

**I measured it before re-cutting, and it is not unchanged.**

```
  INSTRUMENT   git show <ref>:<brief> at both vintages, sections sliced on the PART headings,
               sha256 + unified diff. Line endings are the record's, not the worktree's.
  PART I       v1 5,026 bytes  ->  v2 3,592 bytes     DIFFERS
  PART III     compression only                        UNCHANGED IN SUBSTANCE
  CONTROL      Part IV differs -- the slicer can see a change when there is one.
```

**The headline is right about the SET and wrong about the CONTENT.** There are still six outcomes,
in the same order, over the same territory -- nothing was added, retired or renumbered, and on that
the CRO's finding stands. But two of the six changed in a way that is not compression, and both
changes are in the part a grade is read from.

**Both are the same move: a value added to an enumeration. An enumeration is a schema (Rule 24),
and a new value is a new world the acceptance line has to survive.**

| outcome | v1 | v2 | what it does to my v1 cut |
|---|---|---|---|
| O3 | CONFORMS / CONTRADICTS / OUT OF PLANE (3) | + **DERIVED FROM another project's row** (4) | FWD-3's ACCEPT had two branches and the new value is a third it does not cover |
| O6 | CONFORMANT / MIGRATE / RETIRE / DECLARED EXCEPTION (4) | + **AWAITING a named word** (5) | FWD-6 could be graded met while nothing was decided |

**Neither is hypothetical, and that is why they are worth a re-cut rather than a note:**

- **O3's fourth value is already in use.** Brief finding IV.12: `IRPT_FNTEND`'s four graded surfaces
  are DERIVED from `IRPT_BCKEND`'s rows. One of the two paused projects this outcome exists to
  unblock cannot point at a line in its own report, because its answer is in a sibling's.
- **O6's fifth value covers a ninth of the ledger.** Brief finding IV.13, counting
  `06_CONFORMANCE_LEDGER.md` s.7: 27 CONFORMANT / 14 MIGRATE-home / 6 MIGRATE-format /
  3 MIGRATE-grammar / 13 RETIRE / **9 AWAITING a word** -- 72 dispositions, 9 of them undecided.
  My v1 bar was *"every part carries its decision"*, and `AWAITING` is a value that satisfies that
  sentence while deciding nothing. **A bar a pending item passes is a bar that passes vacuously**,
  which is the failure class this estate has already named twice this week.

**FWD-1, FWD-2, FWD-4 and FWD-5 are carried forward UNCHANGED and are reproduced verbatim.**
FWD-3 and FWD-6 keep their ids and their outcome statements; only their acceptance lines are
re-tested, per the rule that an ACCEPT is re-tested and never inherited. **No id is renumbered,
reused or retired**, and nothing in a PRD or a graded row cites these ids yet.

---

## THE SIX OUTCOMES

```
  FWD-1  A seat handed a pipeline it has never seen can say whether it follows the
         rules, and which rule decided it, from one document
         DONE WHEN  EXERCISED -- two people have actually judged the same pipeline
                    against it and compared answers
         ACCEPT     two people who have never worked together each judge the same
                    pipeline from the one document and give the same answer,
                    including which rule decided it -- where today two people
                    reading different documents reach different answers
         SOURCE     brief v2 Part I O1; bar Part III O1
         STATUS     unchanged from v1

  FWD-2  Andrew settles, in one sitting, which parts of the estate are organised by
         firm and which by product
         DONE WHEN  EXERCISED -- he has actually gone through the list and decided
         ACCEPT     he works down the whole list in one sitting; every case has
                    enough beside it to decide on without going and looking
                    something up; the ones he has already decided are already
                    filled in
         SOURCE     brief v2 Part I O2; bar Part III O2
         STATUS     unchanged from v1

  FWD-3  The person running a paused project can see exactly what the new rules
         contradict in their plan, and start again on the strength of it
         DONE WHEN  EXERCISED -- an owner has actually read theirs and resumed
         ACCEPT     the person running a paused project can point at what ended the
                    pause -- either nothing in their plan conflicts, or here is the
                    list of things to change, or here is the other project whose
                    answer decides theirs, and here is that answer and what it
                    settled for them -- where today the pause has no per-project
                    condition for ending at all
         SOURCE     brief v2 Part I O3; bar Part III O3; finding IV.12
         STATUS     AMENDED at v2 -- third branch added; outcome and id unchanged

  FWD-4  Anyone who needs a firm's name looks it up instead of deciding what to
         call it
         DONE WHEN  EXERCISED -- a real piece of work has taken a name from it
         ACCEPT     two people doing the same job, on different days, use the same
                    name for the same firm -- where today the same firm is called
                    four different things in four places
         SOURCE     brief v2 Part I O4; bar Part III O4
         STATUS     unchanged from v1

  FWD-5  Taking on a new firm is one checklist run end to end, with no step where
         somebody has to invent an answer
         DONE WHEN  EXERCISED -- a firm has actually been taken on this way and its
                    people can see their dashboard
         ACCEPT     someone follows the checklist from start to finish, the new
                    firm's people see their dashboard at the end, and nowhere in it
                    did anyone have to make a judgement call the rules should
                    already have made -- where today every firm has been a one-off
         SOURCE     brief v2 Part I O5; bar Part III O5; Andrew, "we're going to have
                    the same pattern over and over again as we take on more and
                    more firms"
         STATUS     unchanged from v1

  FWD-6  Every part of the estate has a decision recorded against it -- leave it,
         move it, retire it, or allow it as a stated exception
         DONE WHEN  APPLIED -- every part carries either a decision or the name of
                    the person it is waiting on, and the two can be told apart on
                    sight
         ACCEPT     someone starting a cleanup reads what to do with each part from
                    the list instead of going and measuring everything again; the
                    parts nobody has decided yet are counted and say who has to
                    decide them, so the list can never read as finished while part
                    of it is not; and anything allowed as an exception can later be
                    checked to see whether the reason still holds
         SOURCE     brief v2 Part I O6; bar Part III O6; finding IV.13
         STATUS     AMENDED at v2 -- the undecided case is now named and counted
                    rather than passing silently; outcome and id unchanged
```

---

## TWO THINGS FOR ANDREW BEFORE THIS IS RATIFIED -- BOTH STILL OPEN AT v2

### 1. FWD-6's BAR REACHES INTO A SIBLING PROJECT, SO I CUT THE BAR LOWER THAN THE BRIEF WROTE IT

The brief's Part III bar for O6 is *"a migration project starts from the ledger's rows rather than
from a fresh census."* Part II says **migrations are SEPARATE PROJECTS, one per pipeline family.**
So that bar cannot be graded inside D14 -- it is met, or not, by a project D14 does not own and may
not exist for months.

**I cut FWD-6 at `APPLIED`** rather than at the `EXERCISED` the brief's bar implies. **This is me
lowering a bar the brief set, and it is the kind of move that should never pass silently**, so it is
stated here rather than absorbed. If Andrew wants the higher bar, FWD-6 becomes ungradeable until a
migration project runs, and D14 cannot close on its own.

**v2 does not move this.** I diffed Part III and re-read Part I's O6: the migration project is still
inside the outcome's territory and migrations are still separate projects. The question is unchanged
and is still his.

### 2. THE SIX MAKE THE CANON READABLE AND DISPOSITIONED. NONE MAKES IT ENFORCED.

FWD-1 is *a seat can ANSWER from one document*. FWD-6 is *every part carries a DECISION*. Neither
says anything mechanically REFUSES a tree that departs from the canon.

**This fabric measured the cost of that distinction four times in one day** -- a battery pinned
failing for hours, an obligation routed into it unrun, a preflight blind to the change it was named
to grade, and an integrity check whose arming was optional to the very party it checks. **A canon
that is only readable is a canon that is optional**, and the evidence is that the estate's rules were
already law and were unenforced, which is finding IV.1 of the brief itself.

**I HAVE NOT ADDED A SEVENTH OUTCOME.** Step 2 cuts from the brief and nowhere else, and inventing
scope at L2 is exactly the guess this phase exists to prevent. **The question is Andrew's:** is
enforcement deliberately out of D14's territory -- a later project, or a property of the spine D14
owns -- or is it a gap in Part I? One line settles it, and it is cheaper now than after a
decomposition.

⛔ **ANSWERED 2026-09-13 -- BY ANDREW'S OWN COMMISSION, NOT BY THIS SEAT. CLOSED AS AN OPEN CALL.** At ~03:2xZ he
approved "all recs" on a card set whose item 4 commissioned TWO Platform Logic briefs, the second being *"the
EXECUTABLE-LAYER brief -- key/name builders off the identity spine, a flagger at safe-commit/safe-apply"* (relayed
`4.0.0_SA_CRO~D` 96332). That brief landed @`fd579d3caf`: its O4 REFUSES a change the builder would not have produced,
and its O6 refuses a clean-up left half-done. **So enforcement is INSIDE D14, delivered as a sibling brief rather
than as a seventh outcome here** -- which is why this endpoint still carries six. Its endpoint is
`ENDPOINT_FWD_D14_EXECUTABLE_LAYER_20260913.md`. **The FWD-6 bar question above remains open**, and tonight it has
company: the naming endpoint's FWD-6 carries the same shape -- a bar met only by a project that does not exist yet.

---

## PROVENANCE

**READ:** `docs/briefs/d14-pipeline-canon-brief-20260912.md` at BOTH vintages, @`2659d45788` and
@`2663f120be`, from the record via `git show` rather than the worktree -- the worktree renders this
file with the other line endings and reports 23,327 bytes for v1 where the record holds 23,097, so a
byte figure quoted off disk is a different measurement from a byte figure quoted off a commit.
Sections sliced on the eight top-level headings (denominator printed: 8 in each vintage). Part I and
Part III diffed line by line; Part IV read whole for findings IV.11, IV.12 and IV.13 (denominator
printed: 3 findings present under Part IV in v2).

**CONTROL:** the Part IV slice differs between the two vintages, so the slicing instrument can see a
change when one exists. Without that arm, a "Part III is unchanged" reading and a broken slicer are
the same output.

**NOT READ, deliberately:** the task-order register, `query_project`, any project JSON, the directive
register. Phase 0 reads the brief and nothing else -- a step-2 endpoint assembled from the register
returns an empty set and calls it an endpoint.

**NOT READ and load-bearing:** brief v2's Part V dependencies and Part VII disclaimers, and findings
IV.1 through IV.10, were not re-read at v2; IV.1 is quoted above from the v1 read. The outcomes are
cut from Parts I and III, which is where the skill says to cut from.

**NOT CLAIMED:** that these are the outcomes Andrew wants. That is his confirmation, per his
2026-09-03 word, and it is the next step. **Also not claimed:** that the seven reference artifacts
in `infra/logic/` are unaffected. They were built against v1's O3 and O6 enumerations; whether the
two added values reach them is `4.0.0_SA_CRO~D`'s read of its own artifacts, not mine, and I have
told it what I measured rather than telling it what to do about it.
