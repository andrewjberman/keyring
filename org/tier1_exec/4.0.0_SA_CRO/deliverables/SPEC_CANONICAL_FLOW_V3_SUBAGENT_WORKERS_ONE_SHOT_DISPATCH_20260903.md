# SPEC: CANONICAL FLOW v3 -- subagent workers, one-shot dispatch, single router

**Author:** `4.0.0_SA_CRO`. **On Andrew's word**, CRO terminal 2026-09-03 ~19:2xZ: *"I want to move forward
to an implementation spec, it doesnt have to be perfect, but it should take the concepts we were discussing
before about where the problems were, and instead reformat it around the solutions we're describing here."*
**Status:** IMPLEMENTATION SPEC, first cut. Not the spine. Amending
`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` is `1.0.0_SA_CTO`'s act as scribe; section 9 is that input.
**Supersedes as the working document:** the problems brief
`docs/briefs/canonical-flow-l6-l10-mechanism-gaps-20260903.md` @`6a1d845ecb` -- every problem there maps
to a section here (section 10).
**Measured basis:** two live subagent probes at ~19:0xZ (a Fable 5.1 general-purpose subagent; a Sonnet 5
subagent with worktree isolation), the broker's live-agent list at 19:0xZ, the Win32 process table.

**Governing principle, Andrew verbatim:** *"We want to move as quickly as possible first and accurately
second... clever parallelization, specifically non-overlapping parallelization."*

---

## 1. The shape

Three tracks that never wait on each other and share only FILES, never messages.

```
  L1-L4  CRO brief -> CTO endpoint/register/PRD          (unchanged; "works perfectly")
  L5     COO decomp + battery                            (unchanged; "no problem there")
         |
         v
  L6     COO cuts EVERY task order for EVERY cell, ONE issuance   <-- one-shot
         |
         +------------------------------+------------------------------+
         |                              |                              |
  TRACK A (COO)                  TRACK B (CVO)                  TRACK C (CTO)
  spawns N worker SUBAGENTS      arms surprise-watch            IDLE. Waits for the slug.
  hands each its TO queue        reads rows as they land
  merges worktrees as TOs close  investigates DEEP (comp-*,
  hands next TO on completion      graph, analysis)
  never messages a worker        compiles remediations
  never messages the CVO         never messages anyone
         |                              |
         v                              v
  every TO terminal  +  every row dispositioned      <-- existing L10 precondition gate
                                        |
                                        v
  L10    CVO issues ONE slug  ------->  CTO                 <-- single router, always CTO
                                        |
                        +---------------+---------------+
                        |                               |
             every FWD covered                  FWD not covered
                        |                               |
             ROUND-N ANALYSIS -> COO            PRD ADDENDUM (rare)
             (expectations vs delivered,        bumps prd_version,
              + the remediations file)          then round-N as left
                        |
                        v
             COO recuts/adds TOs, ONE issuance, repeat from L6
                        |
                        v
             CTO: all FWDs REALIZED -> CLOSED.  Done.
```

**What is gone:** the three-way L10 route (`SPEC_ERROR`->L6 / `DECOMP_INVALIDATING`->L5 /
`SCOPE_CHANGE`->L2). Andrew: *"the idea of L10 maybe going to CTO in some cases, COO in other cases, etc is
not smart."* The CTO is the only router. Whether a recut is an L5 re-decomposition or an L6 re-issue is the
COO's internal call and no longer a route token.

**What is gone:** worker seats as broker-registered processes. Workers are subagents of the COO.

**What is gone:** rounds as small circles. One issuance covers the decomposition; a "round" is one full
drain of it.

---

## 2. The seats

| seat | limbs | what it holds | what it never does |
|---|---|---|---|
| `1.0.0_SA_CTO` | L2-L4; L10 router + closer | the PRD, the FWDs, the round-N analysis, the CLOSED stamp | touch a task order; talk to a worker; talk mid-round |
| `2.0.0_SA_COO` (one per project: base, ~A, ~B) | L5-L6; owns Track A | the decomposition, every TO, the worker subagents, their worktrees, the merge | talk to the CVO mid-round; talk to a worker except by handing it a TO |
| `3.0.0_SA_CVO` (one, across projects, until volume says otherwise) | L8-L9; owns Track B | the surprise channel, the deep tooling, the remediations file, the slug | talk to anyone until the slug; talk to a worker ever |
| worker subagent `0.9.0_WK_<CODE>~<n>` | L7 | its TO queue, its worktree, comp-find/comp-read | talk to anyone; verify beyond the TO's bar; spawn |
| `0.0.0_AB_MSTR` | none | push windows | any of the above |

**Three simultaneous projects = one CTO, three COOs, one CVO.** Andrew's topology, verbatim: *"we just spawned
a CTO, a COO per project (therefore Base, ~A and ~B for three simultaneous projects), and either one CVO or
CVO per project."* This spec starts at one CVO: `surprise-watch.sh` already streams both channel roots, and
the CVO's work is read-and-compile, which parallelizes across projects inside one seat. Split to one per
project only when a measured backlog on the channel says so.

---

## 3. HOW WORKERS ARE FED -- the crux

Andrew: *"if these Task Orders really have immaculate context from the decomp and battery, and we feed the
agents those, and also arm them with comp-find/comp-read, I feel like they should be good to go off that
basis alone... they dont need a lot of functions/noise/context."*

### 3.1 The task order IS the context

A worker subagent starts with **fresh context** (measured: it sees its prompt, CLAUDE.md and MEMORY.md, and
nothing of the parent's conversation). That is the feature. Everything a worker needs is IN the task order,
and a task order that is not sufficient on its own is a defective task order, refused at L6, never patched
by a message.

The TO carries, as today plus tightened:
- `<decomp_ref>` + `<owned_cells>` -- the cells, **with their cell text inlined**, not just the ids. A worker
  does not open the decomposition to find out what its cell says.
- `<preflight>` -- the battery's three dispositions **with their findings inlined** where they touch the
  owned cells. A worker does not re-run comp-schedule / comp-iam / comp-adversary; it reads what the COO ran.
- `<proof_of_spec>` -- the criteria, each with **the exact invocation that proves it** where the COO can
  name one. The worker's verification is running that invocation and recording the output. Nothing deeper.
- `<paths>` -- every file the worker will read or write, absolute-from-root. A worker does not search for
  where things are; it navigates to where the TO says they are and uses comp-find/comp-read only to
  UNDERSTAND what it finds there.
- `<issued_to>` -- the worker serial (3.3).

### 3.2 The worker's tool kit -- minimal by construction

Mechanism: a defined agent type at `.claude/agents/worker.md` (harness-native; the frontmatter fixes model,
tools, reasoning). Measured: a general-purpose subagent gets 143 tools including every MCP server. **The
worker type gets these and only these:**

```
  Bash        -- for comp-find, comp-read, safe-commit.sh, and the TO's own proof invocations
  Read, Edit, Write, Glob, Grep
  ToolSearch  -- NOT granted; nothing deferred is reachable
```

**Not granted, deliberately:** `mcp__opal-agent-comms__*` (no register, no send, no inbox -- the worker
cannot talk and cannot be talked to; "no talking" is structural, not a rule), `Agent` (no nesting), `Monitor`,
`SendMessage`, every gateway/playwright/Lusha tool, `Skill`. A worker that needs a capability outside this
list has a TO that is asking it to do something outside L7, and that is a surprise row, not a tool request.

**Model:** the worker type defaults to the cheaper model (measured: `model: sonnet` override works under a
Fable parent). The COO overrides per TO when a cell's `<preflight>` marks it hard.

### 3.3 Identity -- the one real friction, and its answer

Measured: a subagent **inherits the parent's `OPAL_AGENT_SERIAL`** and git identity. Left alone, every worker
commit, telemetry row and lane check resolves to the COO, and the spine's L6 gate refuses a Tier-0/1 in
`<issued_to>`.

**Convention:** worker serial `0.9.0_WK_<CODE>~<n>` -- e.g. `0.9.0_WK_NFRA_COMPEFFICACY~1`. Measured against
the guards' shared `TIER01_RE`: reads as **Tier-2**, so `<issued_to>` passes, `cvo_send_guard` treats it as a
worker, lane checks resolve it as a worker. The COO sets it in the worker's prompt as an instruction to
export `OPAL_AGENT_SERIAL` in every Bash call and to commit via `safe-commit.sh --author "<serial> <<serial>@opal.agent>"`.
No new broker registration -- the serial exists on commits and telemetry only, which is exactly as much
identity as a worker needs. `~<n>` is the worker's slot in the fan-out, reused across TOs it drains.

### 3.4 Isolation -- the dirty tree, answered

Measured: `isolation: "worktree"` gives the worker its own checkout under `.claude/worktrees/`, own branch,
**1 `git status` entry against 191 in main**. A crashed worker leaves nothing in the shared tree.

**Rule:** every worker runs in a worktree. The COO merges a worker's branch into `CLOUD` when the TO's
proof-of-spec instance is valid (existing `proof-of-spec-check.py`), pull-merge never rebase (existing NEVER
rule), and removes the worktree. **Measured caveat:** the harness did NOT auto-reap the probe's worktree
though it was unchanged; the COO's merge step removes it explicitly (`git worktree remove` + branch delete)
and does not rely on auto-clean.

### 3.5 The worker's verification bar -- cursory by design

Andrew: *"I don't think they need to be operating from a position of trying to 'verify' what they're doing
outside of a relatively cursory basis. The CVO is the one that can really go deep."*

The worker proves each `<proof_of_spec>` criterion by running the invocation the TO names and recording the
output. It re-grounds the TO's premises against live state on its first act (existing L7 clause) and no
further. It does not run comp-adversary, does not read the graph, does not census. **Ambiguity is not the
worker's to resolve** -- a premise that does not hold, a path that is not where the TO says, a result the
invocation does not produce: one surprise row (`spec_asserts` / `world_is`), keep working on the next
criterion or the next TO, report to the COO at the end. The depth lives on Track B.

### 3.6 Feeding cadence -- drain, do not respawn

Measured: a subagent is continuable via `SendMessage` with its context intact. The COO hands a worker its
NEXT task order that way when its current one is terminal. No respawn, no re-reading of CLAUDE.md, no cold
start. A worker holds a QUEUE (its share of the one-shot issuance) and drains it. Andrew's stall -- *"they do
their one task, and if they hit a surprise, then they kind of just have to send it up the chain and stop"* --
cannot occur: the surprise is a row and the next TO is already in hand.

---

## 4. DISPATCH -- one shot, sized fan-out

### 4.1 One issuance covers every cell

The COO cuts a task order for **every cell** of the decomposition in **one commit** and dispatches the set in
one act. Andrew: *"I think we one shot all TOs right out the gate."* No cell is left for "the next round";
the next round exists only if the CTO's round-N analysis sends work back (section 6).

**Mechanical carrier (new, small):** `to-pipeline-gate.py` gains a coverage limb -- a tree dispatch commit
under a project at `dep_stage: DECOMP` is refused unless the union of `<owned_cells>` across the staged task
orders equals the decomposition's cell set. The cell ids are already parsed at the cut (the S5 fix
@`7b649df39d` resolves `cell_refs` against the decomposition); coverage is one set comparison on data the
gate already holds. This is the fail-closed form of "frontload."

### 4.2 The fan-out rule -- N is derived, stated, and capped

Andrew: *"not spreading task orders over too many agents (need a mechanism for how this is decided)."*
Measured today: **14 worker lanes live for two classes, all reading READY -- idle -- at 129 processes.**

**N = the number of dependency-independent chains in the decomposition's edge set, capped by a budget the
COO states in the dispatch record.** The decomposition already carries dependency edges keyed to observed
completion (spine L5); a chain is a maximal path through them; two TOs on one chain cannot run concurrently
and belong to one worker's queue; two chains can and may get two workers. The cap is written in the dispatch
commit message as data (`fanout: N of M chains, cap K, reason: <one line>`), so the number is auditable
rather than a norm. Default cap: **8**, below the harness's own workflow guideline of 15 and far below what
this box has been asked to carry. A COO that wants more states why in the same line.

Subagents cost API calls, not processes (measured: no new claude.exe, no MCP spawn, no watcher). So the cap
is about the COO's context budget and the merge rate, not the machine -- which is why 8 is a starting cap
and not a hardware constant.

### 4.3 The dispatch act

One commit: every TO + the `fanout:` line. Then, per worker slot `~1..~N`: `Agent(subagent_type:"worker",
isolation:"worktree", prompt: <TO #1 of that slot's queue, verbatim, plus the identity export line>)`.
No GO message on the broker -- the spawn IS the GO, and there is no inbox to deliver to. The `dep_stage`
flip to `EXECUTING` happens **in the dispatch commit** by the COO, not afterwards by the row owner
(problem #1 in section 10 -- the guards arm with the act).

---

## 5. THE PARALLEL TRACKS -- non-overlapping by construction

| | Track A -- COO | Track B -- CVO | Track C -- CTO |
|---|---|---|---|
| reads | worker final reports; proof-of-spec instances at HEAD | investigation rows as they land (`surprise-watch.sh` stream) | nothing until the slug |
| writes | merges; the next TO to a drained worker; `dep_stage` | remediation rows; the slug | nothing until the slug |
| tools | the harness Agent/SendMessage primitives; the gates | **all of it** -- comp-find/read/blast/trace/adversary, the graph, atom-decomp on a row that needs it | none |
| depth | shallow; keeps the drain moving | deep; "only on problems that actually appear ambiguous do we ramp the analysis" | n/a |
| messages sent | zero | zero | zero |
| ends when | every TO terminal, every worktree merged | every row dispositioned; slug written | -- |

**The tracks share files, not messages.** Track A writes deliverables and status flips; Track B reads the
channel those produce. The existing `cvo_send_guard` stays and is SIMPLIFIED: the CVO's only admitted send,
at any `dep_stage`, is the slug to `1.0.0_SA_CTO`. That closes the `ROUND_CLOSE` hole (problem #2) by
removing the stage condition rather than adding a stage.

**Track B's one surviving hazard -- silence.** A dead `surprise-watch` and a quiet channel look identical
(problem #4). Cheapest carrier: the CVO's heartbeat summary carries the channel watermark (`rows seen: N,
undispositioned: M, watch pid: P, banner: parent-tied`), which the COO reads once at "all TOs terminal" before
waiting on the slug. If the watermark is behind the channel's row count, the COO tells the CTO -- not the
CVO -- and the CTO re-arms. One read, no monitor, no cron.

---

## 6. THE CLOSE -- single router

### 6.1 The slug goes to the CTO. Always.

Precondition unchanged: every TO terminal with a valid proof-of-spec, every investigation row dispositioned
(existing `surprise-row-gate.py` L10 limb, HEAD-blob reads, fail-closed). Then the CVO writes
`surprise-channel/remediations/REMEDIATION_v<N>.md` -- the ONE artifact for the round -- and its only
message of the round: the slug's path and vintage, to `1.0.0_SA_CTO`.

### 6.2 The CTO's read -- FWD coverage first, then round-N

Andrew: *"CTO assesses whether PRD FWDs are adequately covered, if they didnt cover it well enough they add
addendum to PRD (feel like this should never really happen) and much more likely they just have some kind of
Round (N) analysis off the basis of expectations which gets handed back to COO with the Remediations file."*

1. **Coverage read.** For each `FWD-<n>` in the PRD header: do the proof-of-spec instances at HEAD, taken
   together, reach its `DONE WHEN`? This is the existing `COMPLETION_GRADES` read, one verdict per outcome,
   against the exercised artifact, never the report.
2. **If an FWD is structurally uncovered** -- no cell ever served it -- the CTO writes a **PRD addendum**
   (bumps `prd_version`; the existing `prd-header-notify` delivers it to the COO). Rare by design: an
   uncovered FWD means L5 missed it, and the L5 decomposition is over the manifest the CTO wrote.
3. **Otherwise, the round-N analysis:** `ledger/ROUND_ANALYSIS.round<N>.md` -- per FWD, expectation vs.
   delivered, what the remediations file says about it, and what the CTO wants in the next drain. Handed to
   the COO **with the remediations file**. One message, two artifacts.

### 6.3 The COO's recut

The COO reads both, adds or recuts task orders as its own judgment dictates (re-decompose a cell, re-issue a
TO, add cells for the addendum), and issues them as **one shot again** (4.1 -- coverage of the affected
cells). Repeat from Track A. The three route tokens are retired; the COO's internal choice between an L5
and an L6 act is its own and is recorded in the dispatch commit, not routed.

### 6.4 CLOSED

When every FWD grades `REALIZED`, the CTO stamps `CLOSED`. The existing R6 gate stands as-is
(`missions-tree-index.py:412-489`): both close documents present, same round, exactly the header's outcomes,
every grade `REALIZED`, seats pinned, observed state not below the card. The COO's `COMPLETION_REPORT` is now
simply the final drain record (which cells, which proofs) and the CTO's `COMPLETION_GRADES` is the last
round-N analysis with every row `REALIZED`. Nothing new to build at the close; it was the best-gated rung
already.

---

## 7. MIDSTREAM -- one seat's truth-gathering

Andrew: *"there needs to be kind of like a truth-gathering phase when a project is being started
midstream... a flexible, robust, not overfit strategy."*

Under this design the only seat with state worth recovering per project is **the COO**. Workers are
subagents -- they die with it and their work is either merged (durable, at HEAD) or in a worktree branch
(durable, isolated, unmerged). The CVO's state is the channel file plus a watermark. The CTO's state is the
PRD.

**The COO's restart is three reads, not a procedure:**

1. **Which TOs are terminal** -- from the proof-of-spec instances at HEAD, never from `<status>` (the stalest
   carrier in its own document). A TO whose instance is absent or invalid is not terminal, whatever its
   status field says.
2. **Which worktree branches exist** -- `git worktree list` + `git branch --list 'worktree-*'`. Each is a
   worker that died mid-TO. If its proof-of-spec instance is valid, merge it; else discard the branch and
   re-dispatch the TO. Nothing floating in main.
3. **Which rows are undispositioned** -- the existing gate's census, run read-only.

Then re-dispatch the non-terminal TOs to fresh worker slots (4.3). The CVO re-arms `surprise-watch` from
its watermark. The CTO does nothing. **Not overfit:** three reads on three durable artifacts, each already
gated for validity; no state machine, no checkpoint file, no new format.

The shared-tree residue Andrew described (191 entries today) is the pre-v3 world: broker-registered worker
processes writing directly into the one checkout. Under 3.4 the class does not recur for L7 work.

---

## 8. GATING -- what refuses, and what stops needing to

**Kept, unchanged:** `to-pipeline-gate.py` (L6 shape, preflight, tier of `<issued_to>`, terminal-flip needs
a valid proof); `to-proof-of-spec-check.sh`; `proof-of-spec-check.py`; `surprise-row-gate.py` (rows, L10
precondition); `missions-tree-check.sh`; R6.

**Added (small):**
- L6 coverage limb (4.1): one set comparison, data the gate already holds.
- `dep_stage` flip in the dispatch commit (4.3): the gate reads the flip in the same staged set it grades.

**Simplified:**
- `cvo_send_guard.py`: drop the stage condition; the CVO's only admitted send is to the CTO. The generalized
  Tier-0/1 act guard (LD-0529) stays for the remaining broker-registered seats.
- `.git/hooks/pre-commit` sentinels: retarget the three fail-closed regexes from `task_orders/` and the flat
  `org/surprise_channel/` to the tree paths (`task-orders/`, `surprise-channel/`). Hygiene; five minutes.

**Made structural (no gate needed):**
- No talking: the worker type has no send tool.
- Fan-out: a stated number in the dispatch commit, not a norm.
- No worker noise: the worker type has no gateway, no browser, no skills, no nesting.

**Not built:** any approval gate, any monitor, any cron. Andrew's standing constraint.

---

## 9. WHAT CHANGES IN THE SPINE -- input to `1.0.0_SA_CTO`

Clause-level, so the scribe can take it whole:

| limb | today | v3 |
|---|---|---|
| L6 Output | "parallelism is more instances, never more projects on one instance"; "Task orders are small circles that close" | one issuance covers every cell of the decomposition; fan-out N derived from dependency chains, capped, stated in the dispatch record; a worker holds a queue |
| L6 Handoff | `EXECUTING` "flipped by the row owner on the first task order" | flipped by the COO in the dispatch commit |
| L6 Tool | `send_message` to the exact serial | `Agent(subagent_type: worker, isolation: worktree)`; the spawn is the GO |
| L7 Owner | "the Tier-2 worker named in `<issued_to>`" | a worker subagent of the issuing COO, serial `0.9.0_WK_<CODE>~<n>`, tool kit per 3.2, worktree per 3.4, verification bar per 3.5 |
| L7 Surprise | unchanged | unchanged (row is the carrier; keep working) |
| L8 Gate | CVO to Tier-2 refused while `EXECUTING` | CVO's only admitted send, at any stage, is the slug to the CTO |
| L9 | unchanged | unchanged; explicit that deep tooling lives here |
| L10 Routes | `SPEC_ERROR`->L6, `DECOMP_INVALIDATING`->L5, `SCOPE_CHANGE`->L2, stamped by CVO | the slug to the CTO; CTO writes a PRD addendum (uncovered FWD) or a round-N analysis; both go to the COO with the remediations file; the COO recuts in one shot |
| L10 Close | COO report + CTO grades, R6 | unchanged |
| (new) Midstream | absent | section 7 |
| Section 2 table | L7 "Tier-2 workers / the L6 gate refuses a Tier-0 or Tier-1 `<issued_to>`" | L7 "worker subagents of the COO / the worker agent type has no send tool" |

---

## 10. PROBLEM -> SOLUTION

From the brief @`6a1d845ecb`, flat list:

| # | problem | dissolved or addressed by |
|---|---|---|
| 1 | `dep_stage` armed by a different seat, after dispatch | 4.3 -- flipped in the dispatch commit; and workers have no broker path, so the arming window guards nothing for L7 |
| 2 | send guard dark at `ROUND_CLOSE` | 5 / 8 -- stage condition removed; CVO's only send is to the CTO |
| 3 | fail-closed sentinels blind to tree paths | 8 -- retarget; hygiene |
| 4 | L8/L9 silent stall | 5 -- watermark in the CVO heartbeat, one COO read at drain-end, escalation to the CTO |
| 5 | L10 precondition over a stale index | unchanged and still unconfirmed; the one open read (`_index_paths`) carried forward |
| 6 | worker under-calls significance | 3.5 -- the worker no longer judges; every non-match is a row; the CVO grades all of them |
| 7 | applied-state of a guard illegible | partially: fewer guards; the dispatch commit carries `fanout:` and the flip as data. The general problem stands. |
| 8 | piecemeal dispatch | 4.1 -- one shot, coverage-gated |
| 9 | fan-out past the machine | 4.2 -- derived N, stated cap; and subagents cost no processes |
| 10 | worker stalls on a surprise | 3.6 -- queue drain via SendMessage; the row never stops the worker |
| 11 | managers message constantly | 3.2 + 5 -- workers cannot; the tracks share files; the CVO has one send per round |
| 12 | no midstream restart | 7 |

---

## 11. WHAT THIS SPEC DOES NOT DECIDE

- **The worker serial convention** (3.3) is proposed and measured against the guard regex; not ratified.
- **One CVO vs one per project** -- start at one; the split trigger is a measured channel backlog, not stated.
- **The fan-out default cap of 8** is a starting number, not a measured optimum. It is stated so it can be
  wrong in a specific direction.
- **Whether Track A uses the harness `Workflow` tool** (deterministic `parallel()`/`pipeline()`, opt-in) or
  hand-rolled `Agent` calls. Workflow gives the fan-out and the merge order as code; it also requires an
  explicit opt-in per run. Start hand-rolled; move to Workflow when the drain logic is stable enough to
  freeze.
- **The exact worker tool list** (3.2) -- the principle is fixed (navigate + edit + commit + prove, nothing
  else); the list may need `PowerShell` on this box.
- **The stall carrier** (5) is the cheapest thing that works; it is one field in a heartbeat, and it may be
  wrong.
- **Nothing here was exercised end to end.** The subagent facts are measured on two probes; the flow is not.

---

## 12. BUILD ORDER -- rough, per "it doesn't have to be perfect"

1. `.claude/agents/worker.md` -- the worker type: tools, model, the identity-export instruction. Half a day.
   Test: spawn one against an existing terminal TO in a worktree; it commits under `0.9.0_WK_*`, the lane
   gates admit it, telemetry lands under its serial.
2. The COO's dispatch protocol as a skill (`/dispatch`): read decomp -> chains -> N -> cut all -> `fanout:`
   line -> flip -> spawn N -> drain loop via SendMessage -> merge on valid proof -> remove worktree.
3. `to-pipeline-gate.py` coverage limb; `cvo_send_guard.py` simplification; sentinel retarget.
4. The CTO's round-N artifact (`ledger/ROUND_ANALYSIS.round<N>.md`) and the addendum path.
5. Spine amendment v3.0 by the CTO from section 9.
6. Run **one** project through it -- a small one -- with the step logs Andrew already asked for (record
   @`bcc26d2691`), so the four-quadrant read grades v3 against v2 on the same instrument.

---

## 13. LEVERS READ FROM ONE THREAD OF THE ROUND 1-6 ARTIFACTS

Andrew, CRO terminal ~20:1xZ: *"it really does seem like the game is effectively context compilation,
deconstructing from a lossy qualitative broad outcomes, and narrowing down more and more granular into the
structural truth and nodes... how much more effective could the TOs be, and how much more effective can the
validator be?"* One full thread read: decomp v0.2.7 -> TO-CE-T-2 -> its proof instance -> INVESTIGATION_v1
(33 rows) -> REMEDIATION_v1 (3 graduated) -> STEP_LOG_COMPILED.round1 -> comp-adversary's declaration on the
TO. Every claim below names its specimen.

**The principle the thread shows:** signal is highest at the two ENDS of the chain -- the decomp cell when
clean, a real surprise row (S13, S17) -- and lowest in the MIDDLE, which is exactly what crosses the worker
boundary. The TO and the proof instance are where provenance, authority chains and self-report accumulate.
**Provenance travels in the record; only the spec travels to the worker.** This section refines 3.1.

### L-1. The TO has two faces; the worker sees one

TO-CE-T-2: 89 lines. Signal -- THE CELL, SURFACES, BOUNDS, six criteria -- about 30. The rest: a 15-line
`<status>` of POST-HOC prose (push state, prior history, the round's authority chain) sitting FIRST in the
file; Rule 27 seating; preflight narrative; the compiler-tools mandate; the report clause. A fresh-context
subagent reads all of it before the first act. **The worker face** (cell text, paths absolute-from-root,
bounds, criteria per L-2) is the subagent's prompt; **the record face** (status, authority, preflight,
provenance) stays in the file for the gates and is never sent.

### L-2. One clause per criterion, invocation and expectation inlined

T2-AC3 conjoins five clauses. T9-AC2 is the failure: the worker self-graded PASS having met "only 2 of 4
ways"; `proof-of-spec-check.py` passed it (rc 0 -- by its own words it "does not grade a criterion's truth");
the CVO's L9 read caught it (S13). **Mechanical criteria** carry `invocation` + `expect` (a pattern the
observed output must match); the worker runs and records; the checker greps -- PASS becomes
machine-decidable. **Judgment criteria** ("stated honestly", "owner named") carry `judgment: true`, are not
self-graded, and go only to the CVO. A compound criterion is refused at the cut.

### L-3. Split the surprise channel

INVESTIGATION_v1: 33 rows, 1,065 lines; roughly half are the CVO's own L10 stamps, scoped corrections and
narrative, in the same JSON array as worker surprises; the markdown has collapsed (one bold line at :219 with
846 lines beneath it). Workers append to `investigations/`; the CVO's adjudications go to their own file
(`adjudications/`, or a section of the remediation file). L8 intake then reads worker rows only, and the
CVO's narrative stops inflating the L10 precondition's census. The `adjudicates` carrier already exists; the
split is a file boundary.

### L-4. comp-adversary's neighborhood should be the decomposition, not the filesystem

On TO-CE-T-2 its "uncited neighborhood" is `org/mcp/broker.db-shm`, `agent-spawn-audit.log`,
`.last-stimulus-scan` -- directory siblings of one cited path. The tool declares it: *"graph expansion not
wired -- neighborhood = directory siblings only."* The right neighborhood for a task order is its cell's
`depends_on` chain, those cells' proof instances, and the PRD rows it cites -- a graph the decomposition
already carries. Its `T11 admissibility method` slot reads *"ships when CRO's method ratifies"*: that slot is
this seat's, unfilled, named here as owed.

### L-5. Freeze the decomposition at the cut

v0.1.2 -> v0.2.7 in one day; a tool row's "status now / evidence now" column is now a 400-character running
ledger. Under one-shot dispatch (4.1) the rectangle has no reason to version mid-round. History lives in the
proof instances and the CTO's round-N analysis (6.2); the source grain stays clean for the next cut.

### L-6. The acceptance test for v3 already exists

STEP_LOG_COMPILED.round1: 63 rows; per limb L2 2, L3 1, L4 4, L5 3, L6 5, L7 3, L8 3, L9 4, L10 3, **X 35**.
Fifty-six percent of every seat's acts in round 1 were outside the limbs -- startup, push windows, law
broadcasts, holds, relays. Andrew's messaging observation, measured on the loop's own instrument. Step 6 of
section 12 compiles the same log on a v3 run; **X's share is the verdict.**

### On the validator

It works. S13 caught a self-graded PASS that the spec's bar reads as FAIL; S17 caught a PRD row carrying
`claim=measured` on a subset claim the world contradicts (158 of 2,302 sampled, 38.6% / 58.2%, rc-coded).
Both came from the CVO reading a proof against the spec. The lever is not depth -- it is L-2 and L-3, which
cut what the CVO reads so its depth lands where the ambiguity is.

**Push state of this file:** LOCAL on commit; origin UNREAD by this seat; the integrator owns the window.
