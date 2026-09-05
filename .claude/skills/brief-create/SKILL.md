---
name: brief-create
description: Write the L1 BRIEF that starts the canonical loop, from a plain-English prompt: `/brief-create {what to look into}`; `--midstream` for a project already in flight (authored blind to the open task-order set). Its consumer is `/endpoint --forward` at L2, which cuts outcomes from it, so the brief must be citable and outcome-shaped. Self-contained. 4.0.0_SA_CRO.
---

# /brief-create — step 1 of the canonical fabric loop

**Andrew-direct, 2026-09-01, VERBATIM:** *"creating a skill called /brief-create for CRO and we make
a version where default is new, and youd write `/brief-create {A user-written prompt detailing what I
want them to look into and spec out}`. That skill would hold all the relevant information one would
need to create a perfectly formatted brief with all necessary refs and associated for your /endpoint
run and PRD creation."*

**Self-contained by design.** Andrew: *"it effectively is completely contained end to end in one
process, doesn't need references really, the various skills/gates/scripts/etc contain all relevant
instruction."* Everything needed is below. `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` exists to
**memorialise** the loop, not to be consulted mid-task.

## Invocation

| Form | Behavior |
|---|---|
| `/brief-create {prompt}` | **DEFAULT: NEW.** Greenfield — nothing is built yet. |
| `/brief-create --midstream {project} {prompt}` | The project is already in flight. See MODE: MIDSTREAM. |

---

## ⛔ THE ONE THING THAT DETERMINES WHETHER THIS BRIEF IS USABLE

**Your consumer is `/endpoint --forward` at step 2. It cuts numbered capability outcomes out of this
brief and prints a `SOURCE:` line citing your section.**

>> **A CLAIM WITH NO CITABLE SECTION CANNOT BECOME AN OUTCOME.** It does not degrade gracefully — it
   vanishes. Number your sections and keep one idea per numbered thing. <<

**And write outcomes as things a PERSON CAN DO, never as things a system emits.**

```
  FAILS    the projection tier persists per-relationship returns at L3 grain
  PASSES   an advisor answers "how did this household do, and why" in one place
```
The first cannot be graded by the person the work is for. The second can.

---

## THE STRUCTURE

Proven on `docs/briefs/advi-perfrp-merge-forward-brief-20260901.md`. **Use these parts; they exist
because each one prevents a specific failure.**

### PART 0 — How the constraint was honoured, and WHERE IT BENT
Only for `--midstream`, and it goes FIRST. See that mode below.

### PART I — THE OUTCOME TERRITORY
Numbered `O1..On`. **Each is one thing a named kind of person can DO.** This is the part step 2 cuts
from; everything else exists to support or bound it.
- Give each its own heading so it can be cited.
- **If two outcomes always complete together, they are ONE outcome.** Expect roughly 5–12. Beyond
  that you are decomposing, which is COO's job at step 5, not yours.

### PART II — WHERE THE BOUNDARY SITS
What this owns versus what it merely relies on, with sibling projects **named**. ⛔ **A boundary left
implicit is re-litigated in every decomp** — this section prevents more downstream thrash than any
other.

### PART III — THE QUALITATIVE BAR
**Andrew, verbatim:** *"This does not have to be a deliverable contract. It can be qualitative
because we will not know enough about the quantitative mechanics at this point."*
⛔ **DO NOT INVENT NUMBERS.** A number fabricated at step 1 is treated as ratified by every later
stage because it is sitting in a document.
**Qualitative is not vague — the test is DISPUTABILITY.** *"Advisors find it useful"* fails; nobody
can contest it. *"An advisor reads a figure here they would otherwise have opened Black Diamond for"*
passes: who, what, and the alternative it displaces, with no number in it.

### PART IV — THE SUBSTRATE: is this in a canonical pattern?
Findings about what already exists and whether it fits the estate's normal shape. **State each as a
FINDING with what you measured**, not as an opinion. This is where prior art gets surfaced so the
PRD does not re-buy it.

### PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW
Dependencies and preconditions, named and NOT sequenced. **Sequencing is step 5.** Naming a
dependency here is help; ordering it here is a decomp you are not authorised to make.

### PART VI — STATUS, MARKED NOT-OUTCOME-BEARING
What is true today, measured, with its clock. ⛔ **Label the whole part NOT OUTCOME-BEARING** so step
2 does not cut outcomes from a status snapshot. Status ages; outcomes do not.

### PART VII — WHAT THIS BRIEF DOES NOT CLAIM
What you did not check, could not measure, or deliberately left open. **A brief without this part
reads as more complete than it is**, and the reader cannot tell the difference.

---

## MODE: MIDSTREAM

For a project already in flight — the merge-forward case, where work exists but has lost its frame.

⛔ **AUTHOR IT BLIND TO THE CURRENT TASK-ORDER SET.**
>> **A brief written while looking at what is open will describe an endpoint that RATIFIES what is
   open — and the output is the same thrash with a fresh label and a ceremony attached.** <<

**Do not read** the project's task orders, or its `phase` / `blocking` fields. Those are the branch;
this brief is the base.
**Do read** the existing PRD's purpose and acceptance sections, whatever grounded it originally, and
**the served reality** — what a user can actually see today. Reality is admissible; the branch is not.

**PART 0 IS MANDATORY IN THIS MODE:** state how you honoured the blind constraint **and where it
bent.** It will bend somewhere. ⛔ **A midstream brief claiming perfect blindness is less trustworthy
than one that names the leak**, because the leak is where a ratifying outcome would enter.

**"Unchanged" is a valid finding.** If the endpoint has not moved, say so — that tells Andrew the
failure was in DECOMPOSITION, not DIRECTION, and it is one of the most useful things this brief can
return. Do not manufacture novelty to look useful.

---

## REFS TO CARRY, so the PRD does not re-derive them

Every brief ends with the pointers its consumers need — **the "necessary refs and associated"**:

```
  BRIEF PATH        docs/briefs/{name}-{YYYYMMDD}.md
  PROJECT           {CODE} if one exists, or NONE-YET
  EXISTING PRD      path, or NONE
  SIBLING PROJECTS  the ones named in Part II
  PRIOR ART         what Part IV found already built
  MEASURED AT       UTC clock for every status claim in Part VI
```

## WHAT THIS SKILL DOES NOT DO

- **It does not decompose.** No cells, no task orders, no sequencing. Step 5, and not yours.
- **It does not write the endpoint.** Step 2 cuts outcomes from this; you supply the territory.
- **It does not gate anything.** The loop's only gate is step 6, task-order issuance.
- **It does not dispatch.**

## WHAT HAPPENS NEXT, so you know who reads this

```
  step 2   1.0.0_SA_CTO   /endpoint --forward {your brief}   -> capability outcomes, cited to you
  step 3   1.0.0_SA_CTO   register + fabric key
  step 4   1.0.0_SA_CTO   the PRD -- a project ARC with the endpoint inside it
  step 5   2.0.0_SA_COO   decomp
```
