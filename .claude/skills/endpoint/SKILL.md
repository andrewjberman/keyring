---
name: endpoint
description: Project the TERMINAL STATE of one or more directives -- "if every active task order completes as written, what do we actually HAVE?" -- then reorient it to the endpoint Andrew actually wants. Answers the one question no other skill answers: not what stage we are at (/exec-sum), not what is on the register (/directives-check), not which gates are armed (/comp-schedule), not which TOs are open (/to-check), but whether THE WORK IN FLIGHT ADDS UP TO SOMETHING WORTH HAVING. Phase 1 PROJECTS the endpoint as numbered capability outcomes, each tagged DESIRED/APPLIED/EXERCISED and carrying its acceptance test, plus an explicit UNCOVERED partition for endpoint-necessary work that NO task order covers. Phase 2 takes Andrew's desired endpoint, computes the DELTA, and emits a dispatch-ready restructuring package -- TOs to CUT / AMEND / RETIRE -- handed to 2.0.0_SA_COO to sequence and dispatch. It never dispatches itself. PHASE 0 (`--forward`) runs EARLIER than both -- at pipeline step 2, BEFORE the PRD and before any task order exists -- reading the step-1 CRO brief instead of the register and emitting the QUALITATIVE endpoint that gets written into the PRD, so step 10 can answer "does the PRD name this outcome?" without it collapsing into the spec-error route. Invoke as `/endpoint D2`, `/endpoint D2 D8`, `/endpoint ADVI_PERFRP`, `/endpoint --forward <topic|brief-path>`. Andrew-commissioned 2026-09-01 at the CTO terminal; Phase 0 added same day per SPEC_CANONICAL_LOOP_INCORPORATION_20260901 s.1.2.
---

# /endpoint -- the terminal-state projector

**The question:** *if every active task order completes exactly as written, what do we have --
and is that the thing we want?*

Every other status lens reads the PRESENT. This one reads the FUTURE IMPLIED BY THE PRESENT, and
then lets Andrew move it.

| Skill | Question |
|---|---|
| `/exec-sum` | what stage are we at NOW |
| `/registry-check` | what projects exist; what/where/why |
| `/directives-check` | what is on the register; is membership clean |
| `/comp-schedule` | which gates are still ARMED |
| `/to-check` | which task orders are OPEN |
| **`/endpoint`** | **what do we HAVE when they all finish -- and is that what we want** |

## Invocation

| Form | Behavior |
|---|---|
| `/endpoint D2` | Phase 1 only: project one directive's terminal state. |
| `/endpoint D2 D8` | Phase 1 across several directives, with a CROSS partition (what they share, what collides). |
| `/endpoint ADVI_PERFRP` | Project-scoped rather than directive-scoped. |
| `/endpoint D2 --reorient` | Re-enter Phase 2 against a projection already rendered this session. |
| `/endpoint D2 --uncovered` | The UNCOVERED partition alone -- the fastest read of "what is nobody doing". |
| **`/endpoint --forward <topic\|brief-path>`** | **PHASE 0.** Runs at pipeline STEP 2, BEFORE the PRD exists and before any TO. Reads the CRO brief, not the register. See PHASE 0. |

Phase 2 normally follows Phase 1 in the same conversation: Andrew reacts to the projection,
states the endpoint he wants, and the skill continues. `--reorient` exists for a later session.

---

# PHASE 0 -- FORWARD (pipeline STEP 2, before the PRD)

**Commissioned by `SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` §1.2 under Andrew-direct
2026-09-01 (`/open-calls`, "All recs approved" + *"get it done and spec whatever needs to be spec'd"*).**

**The ask it serves, Andrew's words:** *"before even writing the PRD, we need to define where we
need to go."*

⛔ **WHY PHASES 1 AND 2 CANNOT SERVE IT.** Phase 1 asks *"if every active TO completes as written,
what do we have?"* — **it reads TASK ORDERS IN FLIGHT.** At step 2 there are no task orders and
there is not yet a project. **A skill that enumerates the register returns an empty set and calls it
an endpoint.** Phase 0 reads the BRIEF instead, and reads nothing else.

⛔ **WHY THIS IS THE KEYSTONE, NOT A NICE-TO-HAVE.** Step 10's routing fork has three limbs, and the
third — SCOPE CHANGE — is decided by *"does the PRD name this OUTCOME?"*
>> **With no named endpoint that question has NO ANSWER, and the scope-change route SILENTLY
   COLLAPSES INTO THE SPEC-ERROR ROUTE.** Every misrouted scope change then lands on COO as a TO
   amendment instead of on CTO as a PRD revision. **The loop degrades quietly rather than failing
   loudly**, which is the worst available failure mode. <<

## Step F0 -- RE-ENTRY: when the CTO's L10 coverage read finds an outcome no cell served

⛔ **THIS IS NOT THE GREENFIELD PATH AND MUST NOT REFUSE THE CALLER.** Under spine v3.0 no row routes
here and no route token exists: the CTO's OWN coverage read at L10 (per `FWD-<n>`, against the proof-of-spec
instances at HEAD, on receipt of the CVO's slug) finds an outcome no cell served, or a grade the artifact
cannot settle, and the CTO re-enters **here** itself -- the PRD-addendum path. That arrival has an EXISTING
PRD, EXISTING outcomes and NO new brief, so the F1 refusal (*no brief, no phase*) would turn the CTO's own
correctly-measured gap into a dead end at the wrong seat.

**WHAT ARRIVES** (the CTO's own L10 read; the slug `REMEDIATION_v<N>.md` and the rows it graduated are the
evidence, never a routed instruction):

```
  coverage      FWD-n UNCOVERED (no cell served it) | IN QUESTION (the artifact cannot settle the grade)
  slug          surprise-channel/remediations/REMEDIATION_v<N>.md @vintage   <- the CVO's one artifact
  id            {PROJECT}-S{n}        <- each graduated row chains back to the investigation item, which carries:
     spec_asserts   what the TO SAID
     world_is       what the world TURNED OUT TO BE
```

>> **`spec_asserts` + `world_is` ARE THE PAYLOAD.** The pair is the whole argument that an outcome
   was wrong: what we believed, and what reality did instead. Everything else is addressing. <<

**HOW TO RE-ENTER — the brief is NOT re-read and NOT re-run:**

1. **Read the named outcome only.** `outcome_ref` points at one `FWD-n`. **Do not re-derive the
   list** — a scope change contests ONE outcome, and re-running Phase 0 over the whole endpoint
   silently re-litigates outcomes nobody questioned.
2. **Decide which of three things happened**, and say which:
   - **the outcome was WRONG** → amend it in place, id unchanged.
   - **the outcome was RIGHT and INCOMPLETE** → **add a new `FWD-n` at the next unused number.**
     The contested one stays as it is.
   - **the outcome is OBSOLETE** → retire it; **its number stays vacant forever** (see the id
     contract above), because rows already cite it.
3. **`ACCEPT` is re-tested, not inherited.** If `world_is` contradicted the outcome, the acceptance
   line that let it read as met is the thing that failed. Rewrite it — **in plain English, no
   technical language**, per F3.
4. **The PRD edit is CTO's, same turn.** Nothing routes onward until the ENDPOINT section reflects
   the change, because step 10 will read it back on the next round.

⛔ **AND THE ONE THING RE-ENTRY MUST NEVER DO: silently shrink the endpoint.** Retiring the
contested outcome is always the cheapest way to make a scope change go away, **and the seat doing
the retiring is the seat the finding was against.** A retirement here states, in one line, what
capability the project is no longer promising — **if that sentence is uncomfortable to write, the
outcome was not obsolete.**

⚠ **WHAT I DO NOT HOLD:** whether a scope change may arrive against an outcome that was never
ratified by Andrew (emitted, never approved). The gate cannot tell. **Treat it as a normal re-entry
and say on the record that the outcome was unratified** — do not use it as grounds to discard.

## Step F1 -- Read the BRIEF. Refuse without one.

The input is the step-1 CRO brief (`docs/briefs/**`) or a topic naming one. Print the path, its
`generated` line if it carries one, and its byte size.

⛔ **NO BRIEF, NO PHASE 0 — ON THE GREENFIELD PATH ONLY.** ⚠ **An L10 re-entry from the CTO's own coverage read has
no brief BY DESIGN and this refusal MUST NOT fire on it -- see Step F0, which runs first.** Applying
F1 to a re-entry turns a correctly-routed finding into a dead end. On the greenfield path:
print `UNMEASURABLE: no brief at <path>; step 1 has not produced one`
and stop. **Do not synthesise an endpoint from the topic string** — an endpoint invented from a
title is exactly the guess this phase exists to prevent, and it would then be written into a PRD and
read back at step 10 as though someone had decided it.

⛔ **DO NOT READ THE TO REGISTER IN THIS PHASE, even if the project already exists.** If TOs are in
flight, the caller wanted Phase 1. Reading both silently blends *what we intend* with *what is
already moving*, and the blend is unrecoverable downstream because nothing marks which is which.

## Step F2 -- Emit numbered CAPABILITY OUTCOMES, same shape as Step 3

Identical unit and format to Phase 1 (see Step 3), so a step-10 reader does not need a second
grammar:

**ONE BLANK LINE BETWEEN OUTCOMES, always** — a wall of them is unreadable and the reader is
deciding, not skimming.

⛔ **`FWD-n` IDS ARE PERMANENT AND NEVER REUSED. THIS IS A CONTRACT, NOT A CONVENTION.**
Once an outcome lands in a PRD its id is fixed for the life of the project.
- A new outcome takes the **next unused number**, never a freed one.
- A retired outcome **leaves its number vacant** — the gap is the record that it existed.
- **Never renumber to close a gap.** Renumbering silently re-points every citation ever made to the
  old id, and nothing announces it.
>> **WHY IT IS A CONTRACT: the CTO's round-N analysis and any PRD addendum cite `FWD-<n>` back into this
   list, and a graduated row may name the outcome it contradicts.** An analysis row saying *"the world
   contradicted FWD-3"* is worthless if FWD-3 later means a different outcome. **A drifting id turns a
   grounded finding into a wrong one, and the finding still looks grounded.** <<
Agreed with `3.0.0_SA_CVO` 2026-09-01 as the precondition for `outcome_ref` on the remediation schema; the
route tokens that field once rode with were retired at spine v3.0, and the permanence contract stands on its
own.

```
  FWD-3  Advisors can see per-client performance without opening Black Diamond
         DONE WHEN  EXERCISED -- an advisor has actually read one
         ACCEPT     a named advisor reads a figure here they would otherwise
                    have gone to Black Diamond for
         SOURCE     brief s.4, "the parity oracle is BD and never a dependency"

  FWD-4  Since-inception figures are trustworthy across the 2024 seam
         DONE WHEN  APPLIED -- the labelled tier is in place
         ACCEPT     the seam is visible in the figure, never silently spanned
         SOURCE     brief s.5
```

⛔ **THE TAG MEANS SOMETHING DIFFERENT HERE, AND THE DIFFERENCE IS THE WHOLE VALUE.** In Phase 1 the
tag is the outcome's **CURRENT** state. At step 2 nothing is built, so a current-state tag would read
`DESIRED` on every row and **a field with one value carries no information.**
>> **In Phase 0 the field names the BAR — the state the outcome must reach before it counts as
   delivered. Label it `DONE WHEN`, and gloss the value inline so the card needs no legend.** <<

**The question it actually asks, and it is worth asking per outcome:**
**is this real when the thing is BUILT, or only when it has RUN and someone READ the result?**

⛔ **`DESIRED` IS NOT A VALID BAR.** An outcome that counts as delivered when someone merely intends
it is not an outcome. The honest range is **`APPLIED` or `EXERCISED`** — the field is binary in
practice, and "tagged with three values" obscured that.

⚠ **HISTORY, so nobody re-derives it:** the commissioning spec said "tagged DESIRED/APPLIED/
EXERCISED" and did not say tagged with *what*. This seat first labelled the field `REACH`; **Andrew
read it and had to ask what it meant, which is the label failing its own disputability test.**
Renamed `DONE WHEN` on his word, 2026-09-01.

## Step F3 -- KEEP IT QUALITATIVE. This is a ratified constraint, not a licence to be vague.

**Andrew, verbatim:** *"This does not have to be a deliverable contract. It can be qualitative
because we will not know enough about the quantitative mechanics at this point."*

⛔ **DO NOT FORCE A CONTRACT. Forcing one is what makes the endpoint a guess wearing a schema.** A
number invented at step 2 is not rigour — it is a fabrication that every later stage will treat as
ratified because it is sitting in a PRD.

**Qualitative is not vague.** The test: an ACCEPT line is good if a competent reader could later
DISPUTE whether it was met. *"Advisors find it useful"* fails — nobody can contest it. *"An advisor
reads a figure here they would otherwise have gone to BD for"* passes — it names who, what, and the
alternative it displaces, and it can be argued about without a single number.

⛔ **AND THE ACCEPT LINE CARRIES NO TECHNICAL LANGUAGE. EVER.** Andrew-direct 2026-09-01: *"the
'Accept' description never has technical language, always should be very understandable in plain
English."*

**No serials, no file paths, no table or column names, no key names, no tool names, no fabric jargon
(`face`, `cell`, `leaf`, `emit`, `partition`, `grain`, `served`).** Those belong in the PRD's own
sections and in the decomp — never in the line that says what counts as done.

```
  FAILS   perfrp_performance_relationship emits at L3 grain with a non-null
          content_hash on the served leaf
  PASSES  an advisor can see a client's return for a period they choose, and
          it matches what the account statements add up to
```

>> **THE REASON IS NOT STYLE.** An ACCEPT line written in system vocabulary can only be judged by
   someone who knows the system — **so it silently becomes a check the BUILDER grades, which is
   exactly the self-attestation the whole loop exists to avoid.** A line in plain English can be
   graded by the person the outcome is FOR. **Write it so Andrew, or an advisor, could tell you
   whether it happened.** <<

## Step F4 -- Write it INTO the PRD as a NAMED SECTION

The output's home is the PRD, under a section titled **`ENDPOINT (step 2, /endpoint --forward)`** —
because step 10 reads it back to answer *"does the PRD name this outcome?"*

- **PRD exists:** insert or replace that section. Never edit any other section of someone's PRD.
- **PRD does not exist yet** (the normal case — this runs BEFORE the PRD): emit the block ready to
  paste and print the exact path and section title it belongs under. **Say plainly that it is NOT
  YET LANDED**, because an endpoint that lives only in a terminal is the carrier problem this whole
  spec exists to close.

## Step F5 -- Provenance, mandatory

Same rule as Step 7: brief path + vintage, every outcome traced to a brief line, and an explicit
`NOT READ:` line naming what was deliberately not consulted (the register, the TOs, the project
JSON). **A phase defined by what it refuses to read must say what it refused.**

---

# PHASE 1 -- PROJECT

## Step 0 -- Declare the domain BEFORE enumerating

⛔ **This step is the whole skill and it is the one that will get skipped.**

Write down, in one line each, what the directive is FOR -- the capabilities that would make it
DONE -- **before** looking at a single task order. This is the DECLARED DOMAIN of TAXONOMY LAW
postulate (i), and it is the only thing an enumeration can be MECE *against*.

>> **Enumerate the domain from the directive's PRD and stance cell, never from the TO list.**
   A domain derived from the TOs is not a domain, it is a restatement -- and it makes the
   UNCOVERED partition of Step 4 structurally empty. <<

## Step 1 -- Enumerate members MECHANICALLY, print denominators

Compose existing engines. **Do not build a new one** (CLAUDE.md build ladder rungs 1-2).

```
python .tools/directives-check.py --code <Dn> --json     # member projects + open-TO count
```
then per member project, the broker's project store:
```
query_project("<PROJECT_CODE>")                          # TOs with per-TO status
```

Print: how many member projects, how many ACTIVE, how many open TOs, per project.
**A count without its denominator is not a count.**

⚠ **INSTRUMENT DEFECT, MEASURED 2026-09-01:** `python .tools/to-check.py --all --project <CODE>`
**ignores the `--project` filter** -- three different D8 projects returned byte-identical tails.
Do not use it for per-project TO counts. `query_project` is the sound instrument. If `to-check`
is ever fixed, the tell that it is working is that two different projects return DIFFERENT rows.

## Step 2 -- Read each open TO for its DELIVERABLE, not its title

`comp-read <to-file> --for "what state of the world does this TO leave behind when complete"`.

A TO title names a task. The endpoint needs the STATE the task leaves. `comp-read` hands over the
qualifiers, contradictions and line 1 that a grep of the same file structurally cannot.

## Step 3 -- Render the projection as numbered CAPABILITY outcomes

**Ratified format, Andrew-direct 2026-09-01: the unit is a CAPABILITY, tagged with its state,
with the artifact assertion demoted to the acceptance line.**

```
  D2-5  Advisors see BD-parity performance for all 5,309 accounts
        STATE:   DESIRED  (census ARMED, UNFIRED)
        OWNER:   ADVI_BDPARITY  /  0.4.0_DS_ClientPlatform~Y
        ACCEPT:  5,309 cells emitted; every non-EXACT cell explained or accepted;
                 re-derived on a SECOND instrument
        BLOCKS:  W2 release (2.0.0_SA_COO)
```

⛔ **EVERY OUTCOME CARRIES A STATE TAG. THIS IS NOT DECORATION.**

| Tag | Means |
|---|---|
| `DESIRED` | someone intends it; nothing is applied |
| `APPLIED` | the change is landed but has never run against reality |
| `EXERCISED` | it has run, and the result was READ |

>> **"All TOs complete" projects DESIRED, never EXERCISED.** A TO's stated deliverable is a
   DESCRIPTION, and a description is never a state (CLAUDE.md rule 22, STATE axis). An endpoint
   rendered without state tags is a fiction that reads exactly like a plan. <<

## Step 4 -- ⛔ THE UNCOVERED PARTITION -- the step that justifies the skill

Walk the Step-0 domain against the Step-1..3 outcomes and name every domain member **no active
task order covers.**

>> **A DENOMINATOR OVER THE TASK ORDERS THAT EXIST CANNOT DISCLOSE WORK NOBODY CUT A TO FOR.**
   Enumerating the TO store makes never-written work invisible BY CONSTRUCTION, and the
   projection then reads CLEAN precisely where the estate is emptiest. <<

**SPECIMEN, measured at commission time 2026-09-01 -- the case that produced this skill:**
`AUTH_SELFHEAL` carried a LANDED stage-3 atom-decomp @`3a8bfec867` -- **10 cells, UNCERTIFIED** --
and **ONE** open task order across the whole of D8 (`AUTH_SELFHEAL.TO-A1.cookie-riding-consumer-
inventory.md`, at `0.6.2_AE_PartnerETL`). A TO-sum projection of D8 would have reported the
endpoint as *"we get a consumer inventory"* and would have been structurally unable to say that
this is a fraction of the decomposed work. D2 at the same instant: 8 active projects, 22 open TOs.
**The asymmetry is the finding, and only Step 4 can see it.**

Each uncovered member renders with WHY it is uncovered -- these want different remedies:

| Class | Meaning |
|---|---|
| `NO-DECOMP` | project registered, nothing decomposed yet |
| `DECOMP-UNCUT` | decomp landed, TOs never cut from it (the D8 specimen) |
| `OUT-OF-SCOPE` | deliberately excluded -- cite the ruling |
| `UNOWNED` | needed, decomposed, no seat holds it |
| `OFF-DEVICE` | covered, but on a fabric this device cannot see (Step 5) |

## Step 5 -- Device coverage, stated not assumed

Directives carry a PLACEMENT. **D2 is LAPTOP; D8 is SITEZ.** A run spanning both is reading TO
stores it may not fully see from the device it runs on.

State per directive: `COVERAGE: this device` or `COVERAGE: PARTIAL -- <Dn> is placed <DEVICE>;
N project(s) not readable from here`. **Never silently project over TOs you cannot read** -- an
unreadable TO store and an empty one render identically, and the empty one is the flattering read.

## Step 6 -- ⛔ THE SHARED-DEPENDENCY PASS (CLAUDE.md rule 22)

**A projection assembled per-project CANNOT see a defect in what the projects SHARE.** Every
per-project arm passes while a shared upstream is broken.

Ask what the member projects have in COMMON -- a substrate, an emitter, a served key space, a
schedule, one gate -- and check THAT on its own. Then re-read the member population UNSCOPED once.

D2's active projects read a common performance-reporting substrate; that substrate is a
single point of endpoint failure that no per-project outcome row will ever show.

## Step 7 -- Provenance line, mandatory

Close Phase 1 with what was READ, not what was recalled:

```
GROUNDED ON: directives-check.py --code D2 --json @<commit>; query_project x N;
             comp-read on N TO files; comp-schedule --drift
NOT READ:    <anything load-bearing that was skipped>
```

⛔ **NEVER project from recollection.** The hand-authored predecessor of this skill
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/D2_D8_EXPECTATIONS_AND_OUTCOMES_LOCK_20260901.md`)
carries its own correction: *"10 OF 11 IS WRONG AND I BROADCAST IT THREE TIMES."* A remembered
denominator was broadcast three times before anyone censused it. That is the cost of skipping
Step 1, and it is why Step 7 is not optional.

---

# PHASE 2 -- REORIENT

Phase 1 ends by putting the projection to Andrew and asking the only question that matters:
**"is this the endpoint you want?"**

## Step 8 -- Capture the DESIRED endpoint verbatim

Andrew's statement of the wanted end state is recorded VERBATIM before any interpretation.
Relay, never adjudicate wider OR narrower (CLAUDE.md section 2). If a wider reading seems
plausible, ASK -- do not build on the wider one.

## Step 9 -- The DELTA table

Set-difference the projected endpoint against the desired endpoint. Four cells, and the last two
are the ones people skip:

| Cell | Meaning | Remedy shape |
|---|---|---|
| `KEEP` | projected, wanted | leave the TO alone |
| `GAP` | wanted, not projected | CUT a TO (or fill an UNCOVERED member) |
| `SURPLUS` | projected, NOT wanted | RETIRE / descope -- this is where capacity comes back |
| `MISALIGNED` | both, different grain or state | AMEND the TO |

⛔ **SURPLUS IS THE HALF THAT PAYS FOR THE REST.** A reorientation that only ADDS work is not a
reorientation, it is a wish. Name what stops.

## Step 9a -- ⛔ THE REACHABILITY PASS: which KEEP items the fabric cannot finish by working

**Added 2026-09-01 after the first live run, where this produced the single most valuable line in
the output and no earlier step would have surfaced it.**

Walk the KEEP set and mark every item whose completion requires an act **NO SEAT CAN PERFORM** --
a sovereign word, a vendor-egress grant, an external ingestion, another party's release. Then
count them.

>> **A DELTA TABLE MADE ONLY OF WORK IS A LIE OF OMISSION WHEN THE BLOCKER IS NOT WORK.** Every
   KEEP row looks equally actionable, so a plan reads as reachable while some of its rows are
   waiting on a sentence nobody has said. **The count of unreachable-by-working rows belongs in
   the package's headline, not its footnotes.** <<

**SPECIMEN, first run:** Andrew ruled "everything on D2" = the 22 open task orders. SIX of those
22 sat behind two acts no seat could perform -- one un-given per-use vendor-egress word (5 chained
TOs) and one unnamed activation signal. **The restructuring package could not reach the endpoint it
was written for, and only this pass says so.**

Render as: `REACHABLE BY WORKING: N of M. BLOCKED ON AN ACT NOBODY IN THE FABRIC CAN PERFORM: K --
<who owes each>.` Hand the K-list to whoever owes it **in the same turn** as the package.

## Step 9b -- ⛔ ASK THE STAGED SEAT WHETHER THE ACT WILL ACTUALLY WORK

**Added 2026-09-01, same run, ~10 minutes after Step 9a. This one cost a sovereign word.**

For every K-list item you are about to put to Andrew as a decision, **message the seat holding the
staged act and ask whether it expects the act to SUCCEED** -- before you write the option text.

>> **THE REGISTRY RECORD SAYS AN ACT IS AWAITING A WORD. IT DOES NOT SAY WHETHER THE ACT WILL WORK.**
   Only the seat holding it knows that, and its prediction lives in ITS session, not in the record
   the decision-maker reads. A record that says *"held pending Andrew's ruling"* reads identically
   whether the act is a sure thing or a foregone failure. <<

**SPECIMEN, first run, measured:** this skill's Phase 2 put the Cottonwood one-shot re-run to Andrew
as a Recommended carve-out, built from `MDPF_HEALGAP`'s registry line *"Today's hole stays open until
Andrew rules on the one-shot re-run."* **The executing seat had already recorded a falsifiable
prediction (msg 90345) that a re-fire would fail identically.** Andrew spent a per-use vendor-egress
word; the run fired at 02:49:51Z and failed byte-identically to a run 3.4 h earlier -- same strategy,
same `roster 15 / observed 14`, hole still open, verified against a positive control. **The blocking
condition was vendor-side and unchanged. Nothing our side did could have moved it.**

⛔ **A SOVEREIGN WORD IS A FINITE RESOURCE AND THIS SKILL IS AN INSTRUMENT FOR SPENDING IT.** An
option rendered as *Recommended* carries this seat's endorsement into a decision the reader cannot
re-derive. **Never mark an act Recommended on the strength of a record alone when a seat is holding
that act and can be asked.** One message beforehand is the entire cost.

**And when the answer is "it will fail": say so IN THE OPTION TEXT.** The option Andrew ratified
correctly said the hole does not self-heal; it did not say the re-run was predicted to fail. Both
were true and only one was disclosed.

### 9b-ii -- THE EXECUTOR'S HALF. Without it this rule just moves the failure one step.

**Contributed by `0.6.2_AE_PartnerETL` (msg 90597) against its own act, and adopted verbatim in
substance: *"the option-text rule catches the asker; that one catches the executor. Both seats need
a clause or the next instance just moves one step."***

⛔ **A seat holding a staged act that is about to spend a sovereign per-use word STATES ITS EXPECTED
OUTCOME BEFORE IT FIRES -- and if it expects failure, it says so BEFORE, not in the report.**

The asker's clause above fails whenever the asker does not think to ask. The executor is the only
party who always holds the prediction, so the executor's clause is the one that cannot be routed
around.

⚠ **AND THE SHARPER SELF-FINDING FROM THAT SEAT, which neither clause above would have caught:**
it justified firing as *"the run was the only test of my own prediction."* **It was not a test.** A
FAILURE was consistent with the predicted cause AND with every other unchanged blocker; only a
SUCCESS would have discriminated, and its own diagnosis said success required a vendor-side change
it had no evidence had occurred. **A low-information act dressed in the language of an experiment.**
Before spending a word to "test" something, ask which outcome would actually distinguish anything --
if only one branch is informative and you have evidence it will not occur, the act is a repetition,
not an experiment.

## Step 10 -- Emit the dispatch-ready package. DO NOT DISPATCH.

**Andrew-direct 2026-09-01, and 00:1xZ 2026-09-01 before it: this seat RULES; `2.0.0_SA_COO`
decomposes, sequences and dispatches.** `/endpoint` stops at the package.

```
ENDPOINT RESTRUCTURING -- <Dn ...>  -> 2.0.0_SA_COO to sequence + dispatch
  DESIRED ENDPOINT (Andrew, verbatim): "..."
  CUT     N TO(s):    <outcome> -> <project> -> <suggested seat, or UNOWNED>
  AMEND   N TO(s):    <to-file> -> <what changes and why>
  RETIRE  N TO(s):    <to-file> -> <the SURPLUS ruling that retires it>
  SEQUENCING INPUT (not a ruling): <ordering constraints this seat observed>
  UNRESOLVED: <what Phase 2 could not settle, and who owns each>
```

⛔ **NEVER implement an approval gate here.** An agent-made gate is invisible to Andrew.
Proposing a sequence is legal; installing a stop is not.

---

# THE FIVE HAZARDS -- run this checklist before rendering ANY projection

1. **UNCOVERED** -- did Step 4 actually run against a Step-0 domain built independently of the TO list?
2. **STATE** -- does every outcome carry DESIRED / APPLIED / EXERCISED?
3. **SHARED DEPENDENCY** -- did Step 6 check what the members share, and re-read unscoped once?
4. **DEVICE** -- is coverage stated per directive rather than assumed?
5. **PROVENANCE** -- is the Step-7 line present, with NOT READ populated honestly?

**A projection missing any of the five is a plan, not a projection. Say which one is missing
rather than rendering as though it is complete.**

---

# COST AND NON-APPLICATION

**COST:** one `directives-check --json`, one `query_project` per member project, one `comp-read`
per open TO, one `comp-schedule --drift`. For D2 at commission time that is 1 + 10 + 22 + 1 = 34
reads. **This is not a cheap skill and it is not meant to be run often** -- it is a re-planning
instrument, not a status lens. For "what is happening right now", run `/exec-sum`; it is a
fraction of the cost and answers a different question.

**NON-APPLICATION:**
- **A single project with a live, correct decomp.** If the TOs already cover a decomposed domain,
  Phase 1 restates the decomp at a cost of ~30 reads and tells you nothing. Read the decomp.
- **Mid-round, on a FROZEN spec.** Rule 27 freezes the spec mid-round; `/endpoint` proposes
  restructuring, which is off-spec by construction. Between rounds, or on Andrew's word.
- **As a status report.** It answers a counterfactual, not a state. Anything that renders
  `EXERCISED` is a claim about the present and must be measured, not projected.
- **Where the directive has no PRD and no stance cell.** Step 0 has nothing to build a domain
  from, so Step 4 cannot fire, so the skill degrades to `/to-check` with extra steps. Say so and
  stop.
