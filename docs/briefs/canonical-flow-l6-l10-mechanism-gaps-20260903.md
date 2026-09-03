# BRIEF: the mechanism layer under L6 to L10 of the canonical fabric workflow

**Author:** `4.0.0_SA_CRO` (step L1). **Mode:** NEW (greenfield -- no project registered).
**Written:** 2026-09-03, on Andrew's word at the CRO terminal ("first write a brief with these items").
**Vintage of every measurement below:** repo `CLOUD` @`3667eee8b5`, measured 2026-09-03T18:48Z on the
laptop fabric. Every status claim carries its own clock in PART VI.

**What prompted it.** Andrew asked this seat to assess the biggest operational holes in the L6 to L10
rungs, ahead of handing over a set of recorded observations of his own. This brief is that assessment
converted into outcome territory.

**TWO INSTRUMENTS, DELIBERATELY KEPT APART.** Parts I to VII as first committed (@`83df35d75f`) were
written BEFORE Andrew's observations were read, on his explicit instruction -- verbatim: *"you found
process items that are great which is why i didnt want to color your perspective from the start."*
His observations were then read and folded in as PART I outcomes O8 to O12 and PART IV-A findings F12
to F21. **The base commit is the control.** Anyone auditing whether these two readings are independent
or one echoing the other can diff this file against `83df35d75f`; that is why the base was committed
before the memos were opened rather than after.

**The two readings barely overlap, and that is the most useful thing about them.** This seat read
specification text and gate source and found a MECHANISM layer that is under-armed. Andrew ran two live
projects through the loop and found a COORDINATION layer that is over-talkative and mis-shaped at
dispatch. Neither instrument could have found the other's findings. Where they do meet -- three places,
set out in PART IV-B -- the convergence is load-bearing, and in one case it changes what a remedy would
have to be.

**The one-sentence finding, after both inputs.** The specification of L6 to L10 is largely sound and in
places genuinely well gated; what fails is everything around it -- the guards are armed by a hand-flipped
field and go dark at the limb where the loop is most exposed, the dispatch at L6 is cut in small rounds
that starve workers and multiply both agents and messages, and the whole process assumes it will never be
interrupted, in an estate where it is interrupted routinely.

**Sources.** This seat's own measurement at the vintage above; and Andrew's two recorded observations of
2026-09-03, transcribed at `C:\Users\AndrewBerman\Desktop\transcripts\Flow_7034.txt` and
`Midstream_2120.txt` (FILEs, read at 18:5xZ; audio siblings in
`C:\Users\AndrewBerman\Downloads\` as `Flow_7034.m4a` / `Midstream_2120.m4a`).

---

## PART I -- THE OUTCOME TERRITORY

Twelve outcomes in two layers. Each is one thing a named kind of person can DO. The people here are the
seats that operate the loop (`2.0.0_SA_COO`, `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, the Tier-2 workers) and
Andrew as the operator who has to trust it without reading source.

**O1 to O7 are the MECHANISM layer** -- what the guards enforce and whether their state is legible.
Source: this seat's measurement, written before the memos were read.
**O8 to O12 are the COORDINATION layer** -- how work is cut, how many seats carry it, how much the seats
talk, and how the loop is re-entered after an interruption. Source: Andrew's field observation.

O1 and O8 have a sequencing dependency (PART IV-B, C3); every other pair is independent.

### O1 -- A guard's coverage begins when the act it guards begins

**Today a seat cannot rely on this.** The COO cuts and dispatches task orders at L6; the correspondence
guard that protects L7 to L9 arms only when a DIFFERENT seat (the CTO, who owns the project row) flips
`dep_stage` to `EXECUTING` afterwards. Between the GO message and that flip, workers are executing and
the guard is dark.

**The outcome:** the COO issues a task order and the loop's protections are live for that project from
that moment, with no second seat's bookkeeping standing between dispatch and coverage. A seat that has
dispatched does not have to ask anyone whether the guard came up.

### O2 -- The CVO cannot reach a worker at ANY point in the loop, including while routing

**Today this holds for L7 to L9 and lapses at L10.** The guard keys on one stage only. The L10 stamp
moves the project to `ROUND_CLOSE`, and in that window -- stamping routes, issuing the round's single
remediation slug, the moment the CVO has the most it might want to say -- a send to a Tier-2 seat is
admitted.

**The outcome:** `3.0.0_SA_CVO` attempting to message a worker is refused at every stage the loop can
be in, not at one of them. The rule "findings travel up, never down" is true of the mechanism and not
only of the prose.

### O3 -- Deleting, renaming or moving a gate cannot silently open the limb it guards

**Today the backstops are blind to the canonical paths.** Each relevant pre-commit stage calls its gate
script and, if that script is missing, falls through to a sentinel regex that is supposed to DENY. Those
sentinel regexes are written against the legacy flat path vocabulary and do not match the project-tree
paths the workflow now uses.

**The outcome:** an engineer can rename or relocate any L6/L7/L10 gate and the commit that does so, or
the next commit that needed it, refuses -- rather than the limb quietly becoming ungated. Fail-closed
means fail-closed for the paths in use.

### O4 -- A stalled loop is distinguishable from a quiet one

**Today they are byte-identical.** L8 (compilation) and L9 (adjudication) have no completion carrier at
all; the spec lists both as binding by reading. L8's only instrument is a notifier that, by design,
never blocks. If the CVO's intake is not armed, rows accumulate, nothing is compiled, and the evidence
is silence -- exactly the evidence a round with no surprises produces.

**The outcome:** any seat, or Andrew, can tell the difference between "this round produced no
surprises" and "the intake for this round died" without inspecting a process table.

### O5 -- The L10 precondition cannot pass over rows a stale index concealed

**Today this is a suspected seam, not a confirmed defect.** The routing precondition counts investigation
items via a generated index, and that index is refreshed by a manual re-derive step that appears as an
owed act in dispatch traffic. A stale index counts fewer channel files than exist.

**The outcome:** the answer to "is every investigation dispositioned" is computed from a source that
cannot be behind the rows it is counting, so a route is never stamped over a row nobody adjudicated.

### O6 -- A worker's under-call of a surprise's significance is visible to someone

**Today it is structurally invisible.** The design correctly gives the worker the FORM of a surprise and
withholds the SIGNIFICANCE -- but the fields that carry significance (`class`: OBSERVATION or BLOCKING;
`hazard_standing`: ARMED or INERT) are typed by the worker and are what decide whether the issuer hears
it in-turn and whether a disarm is owed. A row that under-calls a BLOCKING as an OBSERVATION is fully
valid, passes every gate, and looks exactly like a correct observation.

**The outcome:** a seat downstream of L7 can see that a significance call was made and on what basis,
so an under-call is a reviewable act rather than an invisible one.

### O7 -- A seat can tell whether a named mechanism is DESIRED, APPLIED or EXERCISED without reading its source

**This outcome is derived from the pattern across O1 to O5 rather than from a single defect**, and it is
named because every finding in this brief was reachable only by opening the implementation. Two examples
sit inside O2's own evidence: the guard's HTTP path is applied only at the daemon's next restart, and the
commit carrying it is local. Neither fact is legible anywhere a seat looks during normal operation.

**The outcome:** before relying on a guard, a seat can read its state -- specified, wired, exercised,
and on origin or not -- from an artifact, instead of inferring "it exists therefore it protects me."

---

> **O8 to O12 come from Andrew's recorded observations of the two live test rounds.** They are the
> COORDINATION layer; O1 to O7 above are the MECHANISM layer. The evidence behind them is PART IV-A.

### O8 -- The COO dispatches a project's whole task-order set, not a round's worth

**Today dispatch is piecemeal.** Task orders are cut a few at a time, a round runs, more are cut. Andrew,
verbatim: *"Ideally, we would issue task orders all the way through from the start to the very end of the
project. We should not be doing task orders piecemeal... COO needs to basically understand end-to-end what
task orders apply to FWDs from the PRD. That has to be understood right up front, and all the task orders
are written, the full group of task orders, to get the entire project done."*

**The outcome, two halves that complete together:** the COO can see, before issuing anything, the complete
mapping from every PRD outcome to the task orders that close it -- and a worker consequently receives its
whole set at once, so hitting a surprise never leaves it with nothing to do. Andrew: *"They need to get all
of their task orders up front."*

### O9 -- Dispatch fan-out is sized to the machine, not to the task-order count

**Today it is not.** Andrew: *"they will just spawn 20 agents that the computer can't even handle it...
Not a task order per agent, not spinning up a trillion agents. That doesn't really make sense. It needs to
be directed and precise."*

**The outcome:** the COO seats the number of workers the work and the hardware jointly justify, and can
say why that number. More task orders per seat is the normal shape; more seats is the exception that has
to earn itself.

### O10 -- A seat inside a running flow does not talk outside the flow

**Today the loop is drowned in messages.** Andrew names this as the single dominant failure -- *"it seems
to me the biggest problem is just all the messaging. There is no need for messaging"* -- and reports having
already had to revoke `0.0.0_AB_MSTR`'s ability to message Tier-2 seats after hundreds of messages. He
extends it to out-of-flow broadcast traffic: law edits and CLAUDE.md changes fanned to every agent are
*"a distractor."*

**The outcome:** a seat that is part of a canonical-flow group communicates only what the flow's own
handoffs require, and anything else needs a stated reason. Andrew's own framing, offered as territory and
not adopted here as a design: *"when an agent is running canonical flow, there are different messaging
patterns than normal. If you are part of a canonical flow group, you follow the flow."*

### O11 -- The CVO accrues for the whole project and speaks once

**Today the CVO's single output arrives per round, and rounds are small (O8), so it arrives repeatedly.**
Andrew: *"CVO just accrues them... over the entire project and create the remediation file and then send
the remediation file at the end. It is not a discussion."*

**The outcome:** the CVO compiles investigations across the whole project while the work proceeds beneath
it, and issues one remediation artifact at the end, routed to the COO or the CTO by the nature of each
finding. Note PART IV-A F17: the law already says one artifact at one moment -- the cadence problem is
inherited from O8, not from the adjudication limb.

### O12 -- A flow can be re-entered midstream from measured truth

**Today there is no such thing.** Provider outages on the morning of 2026-09-03 crashed agents, which were
reaped, leaving uncommitted work of uncertain provenance in a shared worktree. Andrew: *"there are
outages. People have to go home. We can't be babysitting agents all night long. There's scenarios where we
have to start up midstream. So there needs to be kind of like a truth-gathering phase when a project is
being started midstream."*

**The outcome:** a seat arriving at a project already in flight -- after a crash, a reboot, or a night --
can establish what is actually true (which task orders are really terminal, whose uncommitted work is in
the tree, which rows are really undispositioned) by measurement, and resume, without either re-executing
completed work or trusting recollection. Andrew's constraint on the shape is explicit and binding on any
later design: *"a flexible, robust, not overfit strategy."*

---

## PART II -- WHERE THE BOUNDARY SITS

**This owns:** the mechanism layer under limbs L6 to L10 -- the gate scripts, their wiring into git hooks
and the broker send path, the fields those gates read, and the observability of their armed state.

**This does NOT own, and must not touch:**

- **The canonical workflow specification text.** `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` (FILE) is
  amended as a whole by `1.0.0_SA_CTO` as scribe of process law, under its own section 5 protocol. If a
  finding here implies a spec change, that is an input to the CTO, never an edit from this work.
- **L1 to L5.** The brief, endpoint, register, PRD and decomposition limbs are out of scope. Named because
  O1's remedy touches the project row, which is written at L3; the boundary is that this work may change
  WHEN or BY WHOM the row's stage field is flipped, never the register's grammar.
- **The two live tree projects.** `NFRA_COMPEFFICACY` (D11) and `NFRA_CLDGRPH` (D0) are the SPECIMENS this
  brief measured against, not its subject. Nothing here should alter, pause or re-cut their rounds.
- **`NFRA_COMPEFFICACY` proper.** Sibling and adjacent: it is the comp-tool efficacy program, currently in
  L6. It shares the compiled step-log surface with this work (see PART IV finding F7) and is the round
  whose own execution generated part of the evidence base. Distinct subject.
- **Agent reachability and the inbox watcher.** The `/watcher` doctrine covers the orphan and
  notifier-liveness class generally. O4 is the same failure SHAPE on a different channel; whether the
  remedy is shared machinery or a second instance is a decomposition question, not a boundary one.

**MOVED INTO SCOPE by Andrew's observations** (these were out of scope in the base commit and are not):

- **The `/canonical-flow` skill** (`.claude/skills/canonical-flow/SKILL.md`, FILE). The base brief
  recorded this as adjacent and unread. It has since been read for F21, Andrew has asked that it be
  revisited, and O12 lands on it. In scope.
- **`/brief-create`'s `--midstream` mode.** In scope for O12 only, and specifically for the question of
  whether resumption belongs at L1 at all or is a separate entry the process does not currently have
  (F20, F21). Not in scope as a brief-authoring discipline, which works.
- **The COO's dispatch shape at L6** -- how many task orders are cut in one issuance and how many seats
  carry them (O8, O9). This is behaviour plus the spine clauses that license it (F14), so it necessarily
  touches text this brief does not own; that reaches the CTO as an input, per the spine boundary above.
- **The messaging discipline of seats inside a running flow** (O10), including the already-applied
  Tier-0/Tier-1-to-Tier-2 act guard, whose applied-state is the subject of C2.
- **Out-of-flow broadcast traffic** (F18), noting its direct tension with CLAUDE.md's law-edit
  three-surface requirement. Named as tension; not adjudicated here.

**This relies on, without owning:** the broker send path (`org/mcp/server.py`, `org/mcp/broker.py`), the
git hook installation chain under `.tools/git-hooks/` (DIR), and `dep_stage` remaining the ratified enum
it is today.

---

## PART III -- THE QUALITATIVE BAR

No numbers are stated here on purpose. The quantitative mechanics -- how many gates, how wide a window,
what latency -- are not known at this stage and a figure invented now would be treated as ratified by
every later limb. Each bar below is written to be DISPUTABLE.

1. **A seat that has just dispatched does not have to ask a second seat whether the guard is up.** The
   test is whether the question can still be asked, not whether it is usually answered correctly.

2. **There is no stage of the loop in which the "up, never down" rule is advice rather than a refusal.**
   Contestable directly: name a stage where a CVO-to-worker send still goes through.

3. **An engineer who moves a gate file finds out from the tooling, not from an incident.** Contestable by
   moving one and seeing what happens.

4. **A round that has stopped moving announces itself before Andrew notices it in a status read.** The bar
   is that the loop's silence is interpretable, not that it is eliminated.

5. **A reader of one investigation row can tell whether its significance call was reasoned or defaulted.**
   Contestable: hand a reader a row and ask.

6. **Before trusting any guard named in this brief, a seat can establish its applied state in one read.**
   Contestable: pick a guard, time the read, see whether source had to be opened.

7. **The remedies do not add a rung, a ceremony, or an approval to the loop.** Andrew's standing
   constraint against manufactured friction applies with full force: every outcome here is about making an
   existing guard true, not about inserting a new checkpoint. Contestable by counting the steps a COO
   performs at L6 before and after.

---

## PART IV -- THE SUBSTRATE: findings, each with what was measured

Every finding is stated with its instrument. Findings marked MEASURED were read at source at the vintage
in the header; findings marked READING are structural interpretations of the specification and are
disputable as readings.

### F1 -- MEASURED. The L6 gate checks that `dep_stage` is present and in the enum, never that its value matches the limb being performed

`.tools/to-pipeline-gate.py` (FILE) `:431-439`: reads `dep_stage`, refuses when absent, refuses when not
in the ratified enum. Nothing compares the value to the act. Consequence: no gate refuses a task order cut
while the row still reads `DECOMP`, and no gate refuses L7 execution at `DECOMP`.

Instrument: `comp-read --enumerate 'dep_stage'` over the file, 19 hits, denominator 1081 lines / 30
sections, bands DOCSTRING 3 / COMMENT 6 / CODE 10.

Same census surfaced a second, separate coverage fact recorded in the file's own comments at `:340` and
`:856`: as measured on 2026-09-01 by its author, the large majority of project JSONs across the estate
carry no `dep_stage` at all, so the whole pipeline-gating family is scoped to those that do. That is
plausibly by design for legacy rows; it is recorded here because it bounds every claim about how widely
these gates apply.

### F2 -- MEASURED. The spec assigns the arming flip to a seat other than the one performing the limb

`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L6 handoff: `dep_stage: EXECUTING`, "flipped by the row
owner on the first task order." Section 2 assigns the project row to `1.0.0_SA_CTO` via lane
`TREE_PROJECT_ROW`, while L6 is owned by `2.0.0_SA_COO`. Corroborated independently in live broker traffic,
which carries the flip as a separately owed act after dispatch, phrased as "ROW FLIP OWED BY THE ROW OWNER"
and followed by an explicit note that the send guard refuses only from that flip onward.

Two instruments, and they differ: the spec text, and message bodies written by the seats performing it.

### F3 -- MEASURED. The correspondence guard keys on exactly one stage; `ROUND_CLOSE` does not appear in it

`org/mcp/cvo_send_guard.py` (FILE) `:36` defines the loop stage as `EXECUTING`; `:68` tests
`dep_stage == LOOP_STAGE`. A count of `ROUND_CLOSE` against the file at HEAD returns zero. Since L10 moves
the project to `ROUND_CLOSE` on the CVO's own stamp, the guard is dark for the duration of routing.

Instruments: `comp-read --enumerate` over the worktree copy (14 hits, 6 whole / 8 substring, CODE 11) and
`git show HEAD:<path>` piped to a count as an independent read of the committed bytes. Worktree and HEAD
agree (`git diff --stat HEAD` empty), so this is not a local edit.

**This was already known and disclosed.** `1.0.0_SA_CTO~A` recorded it to the seats it binds at the
CLDGRPH round-1 stamp, stating the consequence plainly. It is carried here because disclosure is not
closure: it remains zero at HEAD, and a hazard that is known and open is a different object from one that
is unknown.

### F4 -- MEASURED. Two aggravators sit inside F3's own provenance

The guard's authoring commits state their own applied condition: the Model Context Protocol (MCP) server
path applies per session start, while the daemon HTTP path applies only at that daemon's next restart --
described in the commit body as DESIRED until then -- and the commit is local, not on origin. So the same
mechanism has three different truth values depending on which path a send takes and whether a restart has
happened, and none of them is visible from outside the source.

Instrument: `git log` bodies on the file (`dd2beb4a11`, `4774db2c87`), read as authored records rather than
as prose about code.

### F5 -- MEASURED, with positive controls both ways. Three fail-closed sentinels cannot see the canonical tree paths

`.git/hooks/pre-commit` (FILE) composes numbered stages. Stages 8 and 9 guard task orders; stage 10 guards
surprise-channel rows. Each calls its gate script when present and otherwise falls through to a sentinel
regex intended to DENY.

- Stages 8 and 9 match `task_orders/` with an UNDERSCORE. The canonical tree path is `task-orders/` with a
  HYPHEN. Tested against a real task-order path under `NFRA_COMPEFFICACY`: no match. Positive control on
  the legacy flat form `org/task_orders/FOO.md`: fires. So the regex is not broken -- it is aimed at the
  old vocabulary.
- Stage 10 matches the legacy flat root `org/surprise_channel/<CODE>/`. Tested against a real tree
  investigation path under `NFRA_CLDGRPH`: no match. Positive control on the legacy flat form: fires.

On-disk census of the tree: both live projects use `task-orders/` (hyphen) and
`surprise-channel/investigations/`; the underscore variant does not exist anywhere under `org/missions/`.

**The exposure is latent, not live.** The gate scripts exist today, so the gates fire through the direct
call and the sentinel never runs. What is false today is the GUARANTEE -- the property that makes moving or
renaming a gate safe.

**Shape worth naming for the PRD:** every seat verified the gate; nobody verified the backstop. The tree
migration moved the path vocabulary and the sentinels stayed on the old spelling, which is the "a check
scoped to the members cannot see a defect in what the members share" pattern with the shared thing being
the path vocabulary itself.

### F6 -- MEASURED. The routing precondition gate is the best-built gate in this range, and its one soft seam is its census source

`.tools/surprise-row-gate.py` (FILE) reads HEAD blobs and never the worktree (`:87`, with the reason given:
a peer's half-written status flip must not decide a route); fails closed on an unreadable blob, an
unparseable block, or any unexpected exception (`:38-39`, stating "A gate that fails open is not a gate");
covers both route-carrying shapes; and enforces the locked route map.

The seam: `_investigations_precondition_violations` (`:300-319`) counts investigation items via the index
rather than the tree, and the index is refreshed by a manual re-derive that recurs as an owed act in
dispatch traffic. **Not confirmed as a defect** -- `_index_paths` (`:234-243`) was not read, so which index
is resolved, and whether it is commit-contained, is open. Recorded as a seam to check, not a finding to fix.

Instrument: `comp-read --for` over the file, which returned the shape (31 sections), the salient regions,
and 137 qualifiers of which 62 near the queried regions. 28 of 1004 lines were shown; the unread ledger is
acknowledged in PART VII.

### F7 -- MEASURED. The close (L10's terminal half) is strongly gated and should not absorb effort

`.tools/missions-tree-index.py` (FILE) `:412-489` implements the close as refusal R6: a row may read
`CLOSED` only when the COO's completion report and the CTO's grades both exist for the SAME round, both
validate against `org/standards/COMPLETION_REPORT.schema.json` (FILE), both cover EXACTLY the PRD header's
endpoint outcomes with no repeats, every grade reads REALIZED, the authoring seats are pinned
(`written_by` the COO, `graded_by` the CTO), and no REALIZED grade cites an observed state below its card's
DONE WHEN -- with APPLIED satisfied by APPLIED or EXERCISED, and EXERCISED only by EXERCISED. It refuses
fail-closed when the header's outcomes are unreadable.

Instrument: `comp-read --enumerate`, 75 hits across 777 lines / 32 sections. This is stated as a finding
because a brief that lists only holes invites a PRD that re-buys a rung already built.

### F8 -- READING. The worker's significance fields are the significance judgment the design withholds

The specification separates form from significance at L7 and assigns only form to the worker. But `class`
and `hazard_standing` are worker-typed, gate-validated for presence and enum membership, and are precisely
what determine whether the issuer is told in-turn and whether a disarm is owed. This is a reading of the
design's intent against its fields, not a measurement of a failure; no instance of an under-call was
looked for.

### F9 -- READING. L8 and L9 are the only limbs in L6 to L10 with no refuser of their own

Reading the spec's own limb-to-refuser table: L6 refuses at commit, L7 refuses at commit and at completion,
L10 refuses at the precondition and at the close. L8's row carries a notifier and a send guard -- the guard
constrains what the CVO may SAY, not whether the CVO COMPILED. L9's row carries row-shape refusals, which
constrain how an adjudication is written, not whether one happened. Section 4 lists the CVO's engagement
beginning at L8 and the grounding bar at L9 among the things that bind by reading.

The consequence is benign in the record and costly on the clock: the L10 precondition blocks routing while
rows are undispositioned, so nothing WRONG lands -- the loop simply stops, and stopping produces no signal.

### F10 -- MEASURED, and it bounds F9. An intake stream IS armed for the CVO at this vintage

A process-table read at 18:4xZ found `surprise-watch.sh 3.0.0_SA_CVO stream` running. So F9's exposure is
latent right now, not live. Recorded with its own clock because it is the most perishable claim in this
brief, and because a process-table read is exactly the weak oracle the `/watcher` doctrine warns about: it
observes that a process exists, never that a consumer is reading it.

### F11 -- MEASURED, minor. The pre-commit hook has duplicate stage numbers

`.git/hooks/pre-commit` numbers two stages 9 and two stages 10. Cosmetic and non-functional. Carried only
as a tell that edits have been landing in that file without a full re-read, which is the same mechanism
that let F5 persist.

---

## PART IV-A -- FINDINGS FROM THE OPERATOR'S FIELD OBSERVATION

A third evidence class joins MEASURED and READING here: **OBSERVED** -- Andrew's direct observation of two
live projects (`NFRA_COMPEFFICACY`, `NFRA_CLDGRPH`) run through the loop this session expressly as test
subjects. For the coordination layer this is the STRONGER instrument: no amount of source reading surfaces
"the managers will not stop talking." Where this seat could corroborate or correct an observation by
measurement, it did, and both the corroborations and the one correction are recorded.

### F12 -- OBSERVED. L1 to L5 are sound; the failure begins at coordination

Andrew, walking the limbs in order: L1 `/brief-create` *"works perfectly"*; L2 `/endpoint --forward`
*"works perfectly"*; L3 registration *"great"*; L4 PRD *"all of that is good"*; L5 decomposition and
battery *"no problem there, nothing I noticed just yet."* Then: *"The problem becomes the coordination."*

Recorded because it independently confirms the scoping this brief was given (L6 to L10) from a different
instrument, and because it means the specification and authoring limbs should not absorb remediation
effort.

### F13 -- OBSERVED. L6 dispatch is piecemeal by round, and fan-out has exceeded what the machine can carry

Two distinct defects at one limb. **Granularity:** task orders are issued a few per round rather than as
the project's full set. **Fan-out:** *"they will just spawn 20 agents that the computer can't even handle
it."* Andrew's diagnosis of the second is that it follows from treating a task order as a unit of seating
rather than a unit of work -- *"Not a task order per agent."*

### F14 -- MEASURED. The spine's own L6 text licenses both halves of F13

`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, L6 Output, two consecutive sentences: *"A task order is
one project for one seat instance; parallelism is more instances, never more projects on one instance."*
and *"Task orders are small circles that close."*

Read together these say: to go faster, seat more agents; and keep each order small. **That is a fair
description of the behaviour Andrew is objecting to.** The COO is not disobeying the spine at L6; it is
following it. This matters for where a remedy can live: F13 is not purely an execution defect, so it
cannot be fully closed by instructing the COO better.

### F15 -- OBSERVED, with MEASURED corroboration. The worker stop-on-surprise is starvation, not a worker defect

Andrew is emphatic that the workers are the healthy part: *"The agents actually do a very good job. The
workers are highly effective. I don't have a lot of comments on them. They don't really do anything
wrong."* The symptom he sees is: *"they do their one task, and if they hit a surprise, then they kind of
just have to send it up the chain and stop. They can't go on to the next task order."*

**MEASURED corroboration that this is starvation rather than misbehaviour:** the spine already instructs
the opposite behaviour. L7 says the worker appends the row *"and keeps working"*, and *"An `OBSERVATION`
never interrupts."* Law and desired behaviour already agree. What is missing is work to continue TO --
which is F13's granularity defect arriving at the worker. **The causal chain is F14 to F13 to F15**, and
only the first link is addressable at L6.

### F16 -- OBSERVED, with MEASURED consequence. Messaging volume is the dominant failure, and the patch already made is not fully applied

Andrew names messaging as the top problem -- *"it seems to me the biggest problem is just all the
messaging"* -- and reports having already acted: *"I had to turn off MSTR's ability to send messages to
Tier 2 workers because they sent hundreds of messages."* He is explicit that the remedy must not be a
blanket ban: *"Obviously, the Tier 1 agents need to be able to speak to Tier 2 workers, but it's just too
much."*

**MEASURED, and it is news:** that patch is LD-0529, carried in `org/mcp/cvo_send_guard.py` @`dd2beb4a11`,
which generalised the guard from CVO-to-Tier-2 to any Tier-0/Tier-1-to-Tier-2 send carrying an act. Per
this brief's F4, that commit is **LOCAL** and its **daemon HTTP path applies only at the next restart**.
So the fix Andrew believes is in place is in place on one of two send paths, on one device, and is not on
origin. It is also, per F3, keyed to a single stage.

### F17 -- MEASURED. The "one remediation artifact" law Andrew wants ALREADY EXISTS; the stream is inherited from round size

Andrew's L8/L9 ask is that the CVO accrue across the project and issue once at the end. The spine already
mandates exactly that shape at L9: remediation rows are *"issued as ONE slug for the round at L10 (one
artifact, one moment), never as a stream of messages during L7 to L9."*

The reason it is not experienced that way is arithmetic, not law: **one artifact per round, times many
small rounds, is a stream.** And the round's own terminal condition is already project-scale -- L10's
close names `2.0.0_SA_COO` as *"the only seat that can say the decomposition is spent (every cell holds a
terminal task order with a valid proof-of-spec)."* Nothing in the spine requires L6 to dispatch a SUBSET
of the decomposition's cells; the multi-round pattern is a dispatch choice, not a mandate.

**Consequence for the fix space, stated as a finding and not as a remedy:** O8 and O11 are very likely one
change rather than two, and it may sit entirely at L6 without amending L9 or L10. **This is deliberately
not developed further here** -- Andrew has reserved fix design for discussion, and this finding exists so
that discussion starts from an accurate map of what is already law.

### F18 -- OBSERVED. Out-of-flow broadcast traffic is a distractor

Distinct from F16, which is about messages inside the loop. Andrew: *"there's a lot of maybe archival
behaviors where if there's a change to Claw.md or if there's certain things, then some senior manager,
CTO, wants to send a message to every single agent. It's a distractor. MCP should be used when necessary
and when necessary only."* Recorded as a separate finding because the remedy surface differs: this traffic
originates outside any project's flow and would not be touched by a rule scoped to flow participants.

**Standing tension to hold, not resolve here:** CLAUDE.md's own law-edit protocol requires three surfaces,
one of which is a same-turn broadcast to live seats, on the stated ground that *"only the broadcast fixes
the fabric."* F18 and that clause are in direct tension. Naming it; not adjudicating it.

### F19 -- OBSERVED, with MEASURED corroboration. Interruption is routine, and it leaves a dirty tree

Andrew: *"there was a lot of outages this morning, significant outages across OpenAI and Anthropic. And as
a result, we had an issue where agents were effectively crashing. They wouldn't be able to get API
connections, so they had to be reaped. So this leaves a dirty tree. It leaves questionable, uncommitted
work floating around."*

**MEASURED at 2026-09-03T18:5xZ on `CLOUD`:** the shared worktree holds 191 `git status` entries -- 11
modified tracked files, 0 staged, 180 untracked. Independent corroboration in this session's own broker
traffic, which records the pre-reboot uncommitted set by name and assigns it to no owner beyond "the
owning seat of each commits or discards." **The condition Andrew describes is present in the tree right
now**, which makes O12 a live constraint rather than a contingency plan.

### F20 -- MEASURED. The spine has no midstream-entry concept at all

An enumerate over `midstream|restart|recover|resume|crash|reaped|interrupt|uncommitted` against the
constitutional spec returns **1 hit across 285 lines**, and it is the substring `interrupts` inside an
unrelated L7 clause about observations. Zero whole-value matches; the tool warned that an anchored probe
would return zero.

Every limb in the spine assumes forward entry from its predecessor. The only re-entry it models is
route-driven (L10 sending a round back to L5, L6 or L2) **inside a loop that is still running**. A cold
arrival at a project whose seats are dead is not a case the process has.

### F21 -- MEASURED. This CORRECTS the recollection that midstream handling was built into `/canonical-flow`

Andrew: *"we did try to work some of this into the slash canonical flow skill. But that might be something
we want to revisit."*

Measured against `.claude/skills/canonical-flow/SKILL.md` (FILE, 189 lines, 26 sections): **one hit** for
`midstream|restart|truth|recover|resume`, at line 136, and it is a table cell pointing at
`/brief-create --midstream`.

That mode exists and this seat used it for scoping, so the recollection has a real referent -- but it
solves a different problem. `/brief-create --midstream` is a **brief-authoring discipline**: author the
brief blind to the open task-order set so the endpoint does not merely ratify what is already in flight.
It is L1 hygiene against a specific bias. **It is not a truth-gathering or resumption procedure**, has no
notion of a crashed seat, a dirty tree, or an unverifiable task-order status, and runs at a limb that a
midstream restart may not even re-enter.

**The gap is therefore wider than remembered, not narrower**, and O12 has no existing partial
implementation to build onto.

---

## PART IV-B -- WHERE THE TWO READINGS CONVERGE

Three collisions between the mechanism findings (F1-F11) and the coordination findings (F12-F21). These
are the highest-value content in this brief, because neither instrument produced them alone.

### C1 -- The correspondence guard is dark at exactly the moment Andrew's CVO design does its only speaking

O11 has the CVO silent through L7 to L9 and issuing one remediation artifact at the end. F3 measures the
guard that enforces CVO silence as keyed to `dep_stage == EXECUTING` only, with `ROUND_CLOSE` absent at
HEAD -- and `ROUND_CLOSE` is the stage the project enters on the CVO's L10 stamp.

**So the single sanctioned CVO output lands in the one window where the mechanism is not watching.** The
better Andrew's cadence discipline gets, the more of the CVO's total output concentrates into the
unguarded window. These two findings make each other worse, and neither reading alone shows it.

### C2 -- The messaging remedy Andrew has already applied is the one whose applied-state is unverifiable

F16 records that Andrew already revoked MSTR-to-Tier-2 messaging. F4 measures that same guard as LOCAL,
with its daemon HTTP path DESIRED until a restart, and F3 measures it as single-stage. O7 -- written before
the memos were read, from an entirely different motivation -- asks for exactly the capability that would
have surfaced this: a seat being able to read a mechanism's DESIRED/APPLIED/EXERCISED state without
opening source.

**A patch believed to be in force is worse than a known gap**, because it retires the vigilance that would
otherwise cover it.

### C3 -- Whole-project dispatch enlarges the arming window rather than shrinking it

O8 moves L6 from many small dispatches to one large one. F1 and F2 measure the loop's guards as arming on
a `dep_stage` flip performed by the CTO **after** the COO dispatches.

Under the current piecemeal shape, that window is repeated but each instance is narrow. Under O8 it occurs
once and covers **the entire project's execution**. So O8, adopted alone, converts a recurring small
exposure into a single total one. **O1 becomes a precondition of O8 rather than an independent
improvement** -- a sequencing fact for the decomposition, recorded here so it is not discovered at L7.

### A note on what F17 does to the fix space

Not a collision but a scoping fact that belongs beside them: F17 establishes that the one-artifact
cadence Andrew wants is already law, and that the round's terminal condition is already project-scale.
That materially narrows where remedies for O8 and O11 can sit and makes a spine amendment possibly
unnecessary for them. It is stated here so the fix discussion starts from the map rather than building
one.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, deliberately NOT ordered. Sequencing is the decomposition at L5 and is not this seat's to make.

- **`dep_stage` remains the ratified enum, with `ROUND_CLOSE` a real member.** O1 and O2 both key on it.
- **Who may flip the project row must be settled before O1 can be built.** Today the row is the CTO's lane
  and the dispatching seat is the COO. Either the lane changes, the flip becomes an effect of the
  dispatching act, or the guard stops reading the row. All three are open; this brief names none as
  preferred.
- **The daemon must be restartable on the integrator's act**, or the HTTP send path stays DESIRED whatever
  is built (F4).
- **The two live rounds must be able to continue while any of this is built.** Both projects read
  `EXECUTING` at this vintage; a change to the arming semantics touches running work.
- **The hook installation chain under `.tools/git-hooks/` (DIR) is the surface O3 lands on**, and the
  installed `.git/hooks/pre-commit` is per-clone, not tracked -- so any remedy has to answer how it reaches
  a second worktree or a second device.
- **`org/standards/` remains where an enumeration is closed as data.** O6 likely needs a vocabulary, and the
  four-postulate discipline for any agent-authored schema applies to it.
- **Whether O4's remedy shares machinery with the inbox-watcher liveness problem** is an open dependency,
  not a design decision to make here.
- **Andrew's standing constraint against agent-made approval gates governs every outcome in PART I.** None
  of these may be built as a checkpoint someone has to clear.

From the coordination layer:

- **O1 is a precondition of O8, not a peer of it** (C3). Recorded as a dependency and deliberately not
  sequenced further; the ordering of the rest is the decomposition's to make.
- **The spine's L6 parallelism and small-circles clauses (F14) must be settled before O8 or O9 can be
  built as specified.** They currently license the behaviour those outcomes remove. Settling them is
  `1.0.0_SA_CTO`'s act as scribe, on Andrew's word -- an input from this work, never an edit by it.
- **Whether a task order remains the unit of seating** is the open question under O9. F14 is where the
  current answer lives. Naming it; not answering it.
- **Andrew's "not overfit" constraint on O12 is binding on its design**, and it is in tension with the
  precision the rest of this brief asks for. A resumption procedure specified as tightly as a gate will
  fail on the second novel outage. That tension is real and belongs to whoever designs it.
- **A resumption capability needs an oracle for "is this task order really terminal"** that does not
  trust a status field. The `<status>` flip is worker-written and is the stalest carrier in its own
  document; the proof-of-spec instance is the stronger candidate. Named as a dependency, not chosen.
- **O12 must answer what happens to uncommitted work of unknown authorship in a shared worktree**
  (F19: 191 entries right now). Whether that is commit, discard, or quarantine is not decided here, and
  the shared-worktree attribution problem is a known-degenerate surface.
- **O10 and the law-edit broadcast requirement must be reconciled** (F18). Both are Andrew's; they point
  opposite ways; one of them has to yield and that is his call, not a decomposition's.

---

## PART VI -- STATUS TODAY

> **THIS ENTIRE PART IS NOT OUTCOME-BEARING.** It is a snapshot with a clock. Step 2 must not cut outcomes
> from it. Everything here ages; PART I does not.

Measured 2026-09-03T18:48Z, `CLOUD` @`3667eee8b5`, laptop fabric:

- **Live tree projects: two.** `NFRA_CLDGRPH` (D0) and `NFRA_COMPEFFICACY` (D11), both `dep_stage:
  EXECUTING`, both `status: active`. Because both read `EXECUTING`, the correspondence guard IS currently
  armed for both -- F3's window is not open at this instant.
- **`NFRA_COMPEFFICACY` is in L6**, with round-1 task orders cut and dispatched and a round-2 cut recorded
  in traffic; `NFRA_CLDGRPH` has taken at least one L10 stamp and a round-2 L6 cut.
- **All gate files named in this brief exist on disk** and, where checked, are wired into
  `.git/hooks/pre-commit` by direct call.
- **A CVO surprise-channel intake stream is running** (F10).
- **The correspondence guard's most recent commit is local, not on origin.** Push state of this brief's
  other cited commits: UNREAD -- no `ls-remote` was run by this seat, and the integrator owns the window.
- **This seat holds no task order** and is not engaged in either live project's round.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **It does not claim any of these holes has caused a live defect.** F5 and F9 are explicitly LATENT: the
  gate scripts are present and an intake is armed. F3 is open at HEAD but its window is not open at this
  instant. No incident was traced to any finding here.
- **It did not read the gate scripts end to end.** `comp-read` reported an unread ledger on
  `.tools/surprise-row-gate.py` -- 28 of 1004 lines shown, 6 of 31 sections -- and the same is true in
  proportion for the other large gates. Sections deliberately skipped include `_index_paths`, which is
  exactly the one F6's seam turns on. **F6 is therefore a suspicion with a named next read, not a finding.**
- **It did not exercise anything.** No gate was made to fire, no mutant was planted, no send was attempted
  against the guard. Every refusal described is read from source, so every claim in this brief sits at
  APPLIED-by-reading, never at EXERCISED. A PRD that treats these as exercised would be overstating them.
- **It did not read `.tools/proof-of-spec-check.py`'s surprises limb at source.** Its behaviour is taken
  from the specification and from commit records, which are descriptive carriers.
- **It did not check the second fabric.** Everything is the laptop fabric. Whether site Z's hooks, paths and
  guard state match is unmeasured, and F5's path-vocabulary defect is exactly the class that diverges
  per-device.
- **It did not measure timing, drag or human experience of the loop** -- how long a rung sits, whether a
  dispatch reaches a seated worker, how a re-cut round feels to run. The instruments used (specification
  text and gate source) show what refuses, never what is slow. **This limitation is now partly answered
  rather than removed:** Andrew's observations (F12-F21) cover that dimension, but they are OBSERVED, not
  instrumented. No message census, agent-count census, or per-limb dwell time was run by this seat.
- **It does not rank remedies or propose designs.** PART I is territory. Which outcomes are worth building,
  in what order, at what cost, is the endpoint and the PRD, and then the decomposition.
- **F8 is a reading, not a measurement.** No under-called surprise row was found; the claim is that one
  would be undetectable, not that one exists.
- **The pattern claims are this seat's own.** "Everyone verified the gate, nobody verified the backstop"
  (F5) and "the mechanism has three truth values" (F4) are interpretations offered to be argued with.

On the coordination half specifically:

- **IT CONTAINS NO FIX CONCEPTS, BY INSTRUCTION.** Andrew, verbatim: *"the fix concepts (once we discuss
  and decide how to address) should be appended to what you already have there."* PART I is territory and
  PART IV is evidence. Where a finding constrains the fix space (F17 most of all, and C3), that constraint
  is stated as a finding and stops there. **A reader looking for the remedy will not find one, and its
  absence is deliberate rather than an omission.**
- **Andrew's observations were not independently instrumented.** F13's agent count, F16's "hundreds of
  messages", and F15's worker-stop behaviour are reported, not measured by this seat. They are treated as
  high-grade evidence because he ran the rounds -- but a decomposition that needs a denominator will have
  to produce one. F19 is the exception: its dirty-tree half was corroborated by measurement.
- **F14's reading of the L6 clauses is contestable and should be contested.** This seat reads
  *"parallelism is more instances"* plus *"small circles that close"* as licensing the fan-out and
  piecemeal dispatch Andrew objects to. `1.0.0_SA_CTO` owns that text and may read it differently; the
  claim is offered so it can be refuted rather than assumed.
- **The transcripts are transcriptions, not Andrew's typed word.** They were read from
  `Desktop\transcripts\*.txt` (FILEs) against `Downloads\*.m4a` audio this seat cannot itself decode. A
  transcription error would propagate silently into every quotation above. Quotations are reproduced
  verbatim from the text files; the audio was NOT verified against them.
- **No claim is made that Andrew's list is complete.** He described these as the flaws that had *"become
  very, very apparent"* and said explicitly *"I think we need to really go a lot deeper and explore where
  are all the failure points."* This brief is two passes, not an exhaustive census of the loop.
- **The two live rounds are a sample of two, both NFRA-macro infrastructure projects on one fabric.**
  Whether these coordination failures generalise to a data or portal project is unmeasured.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/canonical-flow-l6-l10-mechanism-gaps-20260903.md
  PROJECT           NONE-YET  (greenfield; L3 register is 1.0.0_SA_CTO's act)
  EXISTING PRD      NONE
  SPEC OF RECORD    org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md  (v2.6; amended whole-file by
                    1.0.0_SA_CTO under its own section 5 -- an input to it, never edited by this work)
  SIBLING PROJECTS  NFRA_COMPEFFICACY (D11) -- comp-tool efficacy, in L6; shares the compiled step-log
                                              surface; specimen for this brief, not its subject
                    NFRA_CLDGRPH (D0)      -- specimen for this brief, not its subject
  PRIOR ART         .tools/missions-tree-index.py R6 (:412-489) -- the close, already strongly gated (F7)
                    .tools/surprise-row-gate.py            -- HEAD-blob reads + fail-closed, the model the
                                                              other gates should be measured against (F6)
                    org/mcp/cvo_send_guard.py              -- the pure-decision + one-census split is the
                                                              right shape; the defect is its stage keying
                    the /watcher doctrine                  -- the notifier-liveness and orphan-oracle class
                                                              O4 belongs to; do not re-derive it
  SURFACES TOUCHED  .git/hooks/pre-commit (per-clone, NOT tracked) and .tools/git-hooks/ (DIR)
                    org/mcp/cvo_send_guard.py, org/mcp/server.py, org/mcp/broker.py
                    .tools/to-pipeline-gate.py, .tools/surprise-row-gate.py
                    the project row's dep_stage field, and org/standards/ for any new enumeration
                    -- added by the coordination layer --
                    .claude/skills/canonical-flow/SKILL.md and .claude/skills/brief-create/SKILL.md
                    the spine's L6 Output clauses (parallelism + small circles) -- CTO's text, an INPUT
                    the COO's L6 dispatch protocol and its seating act (/mstr-spawn)
                    the broker send path as the carrier of O10's messaging discipline
  OPERATOR INPUT    C:\Users\AndrewBerman\Desktop\transcripts\Flow_7034.txt      (coordination, L6-L10)
                    C:\Users\AndrewBerman\Desktop\transcripts\Midstream_2120.txt (midstream restart)
                    audio siblings: C:\Users\AndrewBerman\Downloads\{Flow_7034,Midstream_2120}.m4a
                    -- transcripts read, audio NOT verified against them (PART VII)
  MEASURED AT       2026-09-03T18:48Z, CLOUD @3667eee8b5, laptop fabric (mechanism layer)
                    2026-09-03T18:5xZ, same tree (F19 dirty-tree count, F20, F21)
                    Every PART VI claim carries this clock. F10 and F19 are the most perishable.
  BASE COMMIT       83df35d75f -- PARTS I(O1-O7)/II/III/IV(F1-F11)/V/VI/VII as written BEFORE the
                    memos were read. The control for the two-instrument claim; diff against it to
                    audit independence.
  NEXT READ OWED    .tools/surprise-row-gate.py:234-243 (_index_paths) -- decides whether F6 is real
  NEXT ACT OWED     the fix-concept discussion Andrew reserved; its output appends here (PART VII)
```

**Next limb:** L2, `1.0.0_SA_CTO`, `/endpoint --forward docs/briefs/canonical-flow-l6-l10-mechanism-gaps-20260903.md`.
Andrew confirms the DONE WHEN line of every outcome at L2; that is his last touch point in the loop.
