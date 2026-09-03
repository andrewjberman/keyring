# BRIEF: the mechanism layer under L6 to L10 of the canonical fabric workflow

**Author:** `4.0.0_SA_CRO` (step L1). **Mode:** NEW (greenfield -- no project registered).
**Written:** 2026-09-03, on Andrew's word at the CRO terminal ("first write a brief with these items").
**Vintage of every measurement below:** repo `CLOUD` @`3667eee8b5`, measured 2026-09-03T18:48Z on the
laptop fabric. Every status claim carries its own clock in PART VI.

**What prompted it.** Andrew asked this seat to assess the biggest operational holes in the L6 to L10
rungs, ahead of handing over a set of recorded observations of his own. This brief is that assessment
converted into outcome territory. It is deliberately written BEFORE his observations land, so that his
and this seat's readings can be compared as two instruments rather than one echoing the other.

**The one-sentence finding.** L6 to L10 are well specified and, in several places, genuinely well
gated -- but the guards that enforce the specification are armed by a hand-flipped field, go dark at
the limb where the loop is most exposed, and are backed by fail-closed sentinels that cannot see the
paths the workflow actually uses. The specification is not the weak layer. The mechanism under it is.

---

## PART I -- THE OUTCOME TERRITORY

Seven outcomes. Each is one thing a named kind of person can DO. The people here are the seats that
operate the loop (`2.0.0_SA_COO`, `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, the Tier-2 workers) and Andrew as
the operator who has to trust it without reading source.

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
- **The `/canonical-flow` skill document.** Adjacent surface, separately owned; not read for this brief.

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
  text and gate source) show what refuses, never what is slow. Andrew's recorded observations are expected
  to land here, and this brief should be read as deliberately blind to that dimension.
- **It does not rank remedies or propose designs.** PART I is territory. Which outcomes are worth building,
  in what order, at what cost, is the endpoint and the PRD, and then the decomposition.
- **F8 is a reading, not a measurement.** No under-called surprise row was found; the claim is that one
  would be undetectable, not that one exists.
- **The pattern claims are this seat's own.** "Everyone verified the gate, nobody verified the backstop"
  (F5) and "the mechanism has three truth values" (F4) are interpretations offered to be argued with.

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
  MEASURED AT       2026-09-03T18:48Z, CLOUD @3667eee8b5, laptop fabric.
                    Every PART VI claim carries this clock. F10 is the most perishable.
  NEXT READ OWED    .tools/surprise-row-gate.py:234-243 (_index_paths) -- decides whether F6 is real
```

**Next limb:** L2, `1.0.0_SA_CTO`, `/endpoint --forward docs/briefs/canonical-flow-l6-l10-mechanism-gaps-20260903.md`.
Andrew confirms the DONE WHEN line of every outcome at L2; that is his last touch point in the loop.
