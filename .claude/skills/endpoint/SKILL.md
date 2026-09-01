---
name: endpoint
description: Project the TERMINAL STATE of one or more directives -- "if every active task order completes as written, what do we actually HAVE?" -- then reorient it to the endpoint Andrew actually wants. Answers the one question no other skill answers: not what stage we are at (/exec-sum), not what is on the register (/directives-check), not which gates are armed (/comp-schedule), not which TOs are open (/to-check), but whether THE WORK IN FLIGHT ADDS UP TO SOMETHING WORTH HAVING. Phase 1 PROJECTS the endpoint as numbered capability outcomes, each tagged DESIRED/APPLIED/EXERCISED and carrying its acceptance test, plus an explicit UNCOVERED partition for endpoint-necessary work that NO task order covers. Phase 2 takes Andrew's desired endpoint, computes the DELTA, and emits a dispatch-ready restructuring package -- TOs to CUT / AMEND / RETIRE -- handed to 2.0.0_SA_COO to sequence and dispatch. It never dispatches itself. Invoke as `/endpoint D2`, `/endpoint D2 D8`, `/endpoint ADVI_PERFRP`. Andrew-commissioned 2026-09-01 at the CTO terminal.
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

Phase 2 normally follows Phase 1 in the same conversation: Andrew reacts to the projection,
states the endpoint he wants, and the skill continues. `--reorient` exists for a later session.

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
