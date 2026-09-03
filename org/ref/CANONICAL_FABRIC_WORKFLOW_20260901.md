# THE CANONICAL FABRIC WORKFLOW

**Status:** constitutional. This document is the one specification of how the Opal fabric takes a topic from a brief
to a closed project. There is one process, the ten limbs L1 to L10, and every document, gate, skill and record that
touches the process resolves to this file. Amendment is by whole-file version under the protocol in section 5; the
authorizing records are named only in the changelog (section 6).

**Vocabulary.** A **limb** is one of the ten numbered hops; "step" is an accepted synonym. A **seat** is an agent
serial registered on the broker. A **worker** is a subagent of the COO that issued its task order: it has a serial for
commits and telemetry and no seat, no inbox and no send tool. **Owner** means the only seat that performs the limb;
**not engaged** means no other seat reviews, grades, certifies, or acts on that limb's artifact while the limb is open.
An **issuance** is the one commit that cuts a task order for every cell of a decomposition; a **round** is one drain of
an issuance. A task order has a **worker face**, the part a worker is given and the whole of its context, and a
**record face**, the part the gates read and a worker never sees. A **track** is one of the three concurrent lines of
work inside a round, the COO's, the CVO's and the CTO's; tracks share files and never messages. The **slug** is the
CVO's one artifact of a round; the **round-N analysis** and the **PRD addendum** are the CTO's two possible answers
to it. A **gate** refuses at commit or at completion; a **notifier** delivers and never blocks; **binds by reading**
means the sentence has no mechanical carrier. The register's `dep_stage` enum (`REGISTERED`, `PRD`, `DECOMP`,
`EXECUTING`, `ROUND_CLOSE`, `CLOSED`) is data; its limb mapping is in section 3.

**Project tree.** Every project lives at `org/missions/D<n>/<MACRO>/<CODE>/` with the subfolders `brief/`, `prd/`,
`decompositions/`, `task-orders/`, `deliverables/<serial>/`, `surprise-channel/investigations/`,
`surprise-channel/adjudications/`, `surprise-channel/remediations/`, `ledger/`, `cards/`. The row is `project.json`;
the flat index entry `org/projects/<CODE>.json` is generated from it and carries `home`. The grammar is
`org/standards/PROJECT_TREE.contract.json`.

---

## 1. The ten limbs

**The shape of a round.** L1 to L5 run once, in order, each handing its artifact to the next. L6 cuts every task
order of the decomposition in one issuance. Three tracks then run at once and share only files: the COO spawns the
workers, feeds each its queue, merges each finished task order and sends nothing until its drain-end read; the CVO
reads the surprise channel as rows land, investigates as deeply as a row needs, compiles the round's remediations
and never messages anyone until the slug; the CTO waits. When every task order is terminal and every row
dispositioned, the CVO issues the slug to the CTO, always to the CTO. The CTO reads coverage of the endpoint's
outcomes: an outcome no cell served takes a PRD addendum; otherwise the round-N analysis goes to the COO with the
remediations file, and the COO recuts in one issuance. When every outcome grades realized the CTO stamps the close.
Signal is highest at the two ends of that chain, a clean cell and a real surprise row, and lowest in the middle,
which is exactly what crosses the worker boundary; so provenance travels in the record and only the specification
travels to the worker.

```
  L1 brief -> L2 endpoint -> L3 register -> L4 PRD -> L5 decomposition + battery (frozen at the cut)
                                                           |
                                                           v
  L6  one issuance: a task order for every cell; fan-out N derived, stated, capped
                                                           |
            +----------------------------------------------+----------------------------------------------+
            |                                              |                                              |
   TRACK A  the COO                             TRACK B  the CVO                                TRACK C  the CTO
   spawns N workers, hands each its queue       reads worker rows as they land, investigates     waits for the slug
   merges as task orders close, hands the next  deep, adjudicates in its own document,
   reads ARMED rows at each merge               compiles the remediations; sends nothing
   sends nothing until the drain-end read       until the slug
            |                                              |
            v                                              v
   every task order terminal          +          every row dispositioned                 <- the L10 precondition
   (the COO's one message: the                             |
    drain-end read, to the CTO)                            v
  L10 the CVO's one slug -> the CTO, always
            |
            +-- an outcome no cell served ------> PRD addendum (rare) -> L4 forward
            |
            +-- otherwise ----------------------> round-N analysis + remediations -> the COO recuts, one issuance, from L6
            |
            +-- every outcome realized ---------> CLOSED
```

### L1 — Brief

- **Owner:** `4.0.0_SA_CRO`. **Not engaged:** every other seat.
- **Input:** the topic, discussed with Andrew. **Output:** the brief at `org/missions/D<n>/<MACRO>/<CODE>/brief/<slug>.md`
  (`docs/briefs/<slug>.md` and a sovereign-word record `org/tier<n>_<tier>/<serial>/deliverables/ANDREW_DIRECT_<slug>.md`
  are the two other admitted shapes), every line citable.
- **Tool:** `/brief-create`.
- **Gate:** none at L1. The brief's path shape is refused at L6 by the PRD header pattern if it is none of the three.
- **Handoff:** the brief's path and vintage, `<path>@<commit>`, become the PRD header's `brief_ref`.

### L2 — Endpoint

- **Owner:** `1.0.0_SA_CTO`. **Not engaged:** `2.0.0_SA_COO`, `3.0.0_SA_CVO`, every worker.
- **Input:** the brief. **Output:** numbered qualitative outcomes `FWD-1..n`, each citing a brief line, carrying no
  numbers, each disputable; ids are permanent and never reused.
- **Tool:** `/endpoint --forward <brief>`. Andrew confirms the `DONE WHEN` line of every outcome here; it is his last
  touch point, and after L2 no limb waits on him. The same skill re-enters here from the CTO's own L10 read, when the
  coverage read finds an outcome no cell served or a grade the artifact cannot settle: the CTO adjudicates by running
  `/open-calls --adjudicate` on the subject, rules on the recommendations itself, records the ruling, appends the new
  outcomes at the next unused ids, re-issues the PRD as an addendum, and the loop runs forward from L4.
- **Gate:** none at L2. At L6 the L6 gate refuses a task order whose PRD does not define every listed outcome in its
  endpoint section, and every defined outcome not listed in the header.
- **Handoff:** the outcomes land inside the PRD as its endpoint section.

### L3 — Register

- **Owner:** `1.0.0_SA_CTO`. **Not engaged:** `2.0.0_SA_COO`, `3.0.0_SA_CVO`, every worker. `0.0.0_AB_MSTR` holds the
  directive register the row must appear in.
- **Input:** the endpoint. **Output:** `org/missions/D<n>/<MACRO>/<CODE>/project.json` with `project_code`,
  `macro_code`, `directive`, `fabric` (`laptop` or `site-z`), `dep_stage`, `status`; the generated
  `org/projects/<CODE>.json`; the project listed under `directives.D<n>.members.projects` in `org/missions/DIRECTIVES.yaml`;
  the macro present and ratified under `directives.D<n>.macros` in `org/missions/MACROS.yaml`.
- **Tool:** `.tools/missions-tree-index.py derive --write` (the index), `check` (the validator).
- **Gate:** `.tools/git-hooks/missions-tree-check.sh` at commit refuses R1 (folder grammar), R2 (macro not ratified),
  R3 (a hand-written flat twin), R4 (row and folder disagree), R5 (absent from the directive register), `ROW-*`
  (a required field missing or off its enum) and `INDEX-*` (index missing, drifted, orphaned); it fails closed when
  the validator cannot run.
- **Handoff:** `dep_stage: REGISTERED`; the row is the identity every later gate compares the PRD against.

### L4 — PRD

- **Owner:** `1.0.0_SA_CTO`. **Not engaged:** `2.0.0_SA_COO`, `3.0.0_SA_CVO`, every worker.
- **Input:** the brief and the endpoint. **Output:** `org/missions/D<n>/<MACRO>/<CODE>/prd/<CODE>_PRD.md`: the
  fenced PRD_HEADER json block first (`org/standards/PRD_HEADER.schema.json`: `project`, `directive`, `fabric`,
  `prd_version`, `step`, `brief_ref`, `endpoint_outcomes`, `status`), the endpoint section, the project arc with its
  defined outcome, and the surface manifest, one row per engine. Every specification decision is closed in the PRD;
  a decision that is an enumeration is closed as data in `org/standards/` and cited; a PRD carries no open
  decide-first question into L5. Any substantive edit bumps `prd_version`; a PRD addendum from L10 is such an edit,
  by the same owner, and re-enters L5 through the same notifier as a first PRD.
- **Tool:** the PRD authoring protocol and the template it names.
- **Gate:** lane `ANY_CTO` refuses any other author's write to `prd/`. At L6 the L6 gate refuses a task order whose
  PRD lacks the header, fails its schema, disagrees with the row on identity, lacks the endpoint section, or lacks the
  surface manifest.
- **Notifier:** `.tools/prd-header-notify.py` (post-commit) delivers a new or bumped header to `2.0.0_SA_COO` and
  re-offers until READ. The handoff to L5 is that notification, never a dispatch.
- **Handoff:** `dep_stage: PRD`.

### L5 — Decomposition and battery

- **Owner:** `2.0.0_SA_COO`. **Not engaged:** `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, every worker. No seat
  certifies the decomposition before L6; the COO may run the sealed-mutant harness as a self-check that no seat waits on.
- **Input:** the PRD's surface manifest. **Output:** `org/missions/D<n>/<MACRO>/<CODE>/decompositions/<CODE>_DECOMP.md`:
  the rectangle over the manifest's surfaces, every cell carrying a status from a vocabulary that has a
  not-evaluated value, cell ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md`, the Rule 24 four-postulate record,
  a placement axis (which fabric executes each cell), dependency edges keyed to observed completion, and a battery
  disposition per lens: the mandatory core `comp-schedule`, `comp-iam`, `comp-adversary`, each `RUN` with a
  denominator or blindness statement or `DECLARED-NOT-APPLICABLE` with a reason, plus any lens of the admitted
  catalog. A lens whose neighborhood is not the cell's dependency chain, its dependencies' proof instances and the
  PRD rows it cites, but the filesystem around a cited path, states that blindness in its disposition. No cell is
  owned by a seat; every cell is served by a worker at L7. The dependency edges are the input L6 derives its fan-out
  from: a maximal path through them is a chain, and two cells on one chain never run at once. The decomposition is
  frozen at the cut: it does not version during a round; a cell's history lives in the proof-of-spec instances and
  in the round-N analysis, and the next cut starts from a clean rectangle.
- **Tool:** `/atom-decomp` (`projects/ATOM_DECOMP`), the lenses.
- **Gate:** lane `TREE_COO` refuses any other author's write to `decompositions/`. The decomposition is consumed at L6
  through `<decomp_ref>`; a defective decomposition surfaces at L7 as a row, reaches the CTO in the slug, and comes
  back to the COO in the round-N analysis; the recut is the COO's own re-decomposition.
- **Handoff:** `dep_stage: DECOMP`.

### L6 — Task orders

- **Owner:** `2.0.0_SA_COO`. **Not engaged:** `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`.
- **Input:** the decomposition. **Output:** one issuance, a single commit, carrying a task order for every cell of the
  decomposition at `org/missions/D<n>/<MACRO>/<CODE>/task-orders/<CODE>.TO-<id>.<slug>.md`. Each task order carries
  two faces in one file. The worker face is what the worker is given and is the whole of its context; a task order
  whose worker face is not sufficient on its own is defective at L6, never patched by a message. It carries
  `<decomp_ref>` with a delimited `<owned_cells>` list and the text of every owned cell inlined; the surfaces and the
  bounds; the battery's findings inlined where they touch the owned cells; `<paths>`, every file the worker reads or
  writes, absolute from the root; and `<proof_of_spec>` with one clause per criterion: a mechanical criterion carries
  its invocation and its expectation, the pattern the observed output must match, so that its pass is decided by a
  match and not by the worker; a judgment criterion is flagged as such, is never self-graded, and is graded by the
  CVO at L9; a criterion that conjoins clauses is refused at the cut. The record face, the status, the seating, the
  preflight's disposition narrative, the authority chain and the provenance, stays in the file for the gates and
  never travels to the worker. `<issued_to>` names the worker serial `0.9.0_WK_<CODE>~<n>`, where `~<n>` is the
  worker's slot in the fan-out and is reused across the task orders that slot drains. A task order is one project for
  one worker; a worker holds a queue, its share of the issuance, and drains it. The dispatch record is the issuance
  commit's message: it carries the fan-out as data, `fanout: N of M chains, cap K, reason: <one line>`, where M is
  the number of dependency-independent chains in the decomposition's edge set, N is the number of workers spawned,
  and K is the cap the COO states; the default cap is eight, and a larger cap is stated with its reason in the same
  line. Two task orders on one chain belong to one worker's queue; two chains may take two workers. No cell is left
  for a later round; a later round exists only when the CTO's round-N analysis sends work back.
- **Tool:** the task-order protocol; then, per worker slot, the harness's subagent call with the worker agent type and
  worktree isolation, its prompt the worker face of the slot's first task order verbatim plus the identity line of
  L7. The spawn is the GO; no broker message carries it and no inbox receives it.
- **Gate:** at commit, `.tools/git-hooks/to-proof-of-spec-check.sh` refuses a new task order without `<proof_of_spec>`
  or without `<decomp_ref>`; `.tools/to-pipeline-gate.py` refuses a new task order whose project row is absent, whose
  `dep_stage` or `fabric` is off its enum, whose preflight is incomplete, whose PRD fails L2 or L4's conditions above,
  whose row and folder disagree, or whose `<issued_to>` names a Tier-0 or Tier-1 seat; an override is written to
  `org/to-pipeline-override-audit.log`. Lane `TREE_COO` refuses any other author's issuance. The coverage of every
  cell by the issuance, and the refusal of a compound criterion or of a mechanical criterion without its invocation
  and expectation, bind by reading (section 4).
- **Handoff:** `dep_stage: EXECUTING`, flipped by the COO in the issuance commit, so the guards that key on the stage
  arm with the act that starts it (section 4 on the row lane).

### L7 — Execution

- **Owner:** the worker named in `<issued_to>`, a subagent of the COO that issued the task order. **Not engaged:** every
  seat; a worker is not a seat and no seat is a worker.
- **The worker.** It starts with fresh context: the worker face of its task order, the standing law, and nothing else.
  It runs as the worker agent type, whose tools are the shell, the file tools and the search tools and nothing else:
  no broker tool, so it cannot register, send or receive; no subagent tool, so it cannot nest; no skill, gateway or
  browser tool. Its model is the cheaper one unless the task order's preflight marks the cell hard and the COO
  overrides per task order. It exports its serial in every shell call and commits under it through `safe-commit.sh`
  with that serial as author; the serial reads as Tier-2 to every guard and is registered nowhere. It runs in its own
  worktree on its own branch, so a crashed worker leaves nothing in the shared tree. A capability it lacks that a task
  order needs is a surprise row, never a tool request.
- **Input:** the worker face of the task order. **Output:** the deliverables and the proof-of-spec instance at
  `org/missions/D<n>/<MACRO>/<CODE>/deliverables/<serial>/<TO>.proof_of_spec.json`, one acceptance row per criterion
  carrying the invocation the task order named and the output it produced, and for a judgment criterion the output
  alone with no verdict; and the task order's own `<status>` flip, committed by the worker on its branch. The
  specification is frozen for the round; the worker's first act is to re-ground the task order's premises against
  live state, and it verifies no deeper than running each mechanical criterion's invocation and recording what it
  printed: the match against the expectation is the checker's, the grade of a judgment criterion is the CVO's, and
  the worker runs no adversary lens, reads no graph and censuses nothing. Status moves with the act, by the actor,
  in the same commit; a precondition that becomes unreachable is declared so on the record.
- **Surprise:** when the worker had to do something the task order did not say, or could not do something it said,
  the worker appends one row to `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v<N>.md`
  (`org/surprise_channel/<CODE>/INVESTIGATION_v<N>.md` on a project without a tree home; site Z writes
  `INVESTIGATION_v<N>.Z.md`) carrying `spec_asserts`, `world_is`, `class` (`OBSERVATION` or `BLOCKING`),
  `hazard_standing` (`ARMED` or `INERT`, with `disarm_owner` when armed), and keeps working on the next criterion or
  the next task order in its queue. The row is the carrier; a message is never the carrier. The worker judges the
  form of a surprise, never its significance: a premise that does not hold, a path that is not where the task order
  says, a result the invocation does not produce, each is one row. An `OBSERVATION` never interrupts; a `BLOCKING`
  row is read by the COO in the worker's final report of that task order; an `ARMED` row is disarmed in the same turn
  by its named owner, and disarmed is not remediated.
- **The drain.** When a task order is terminal the COO reads the worker's final report and the proof-of-spec instance,
  merges the worker's branch into the working branch when the instance is valid, pull-merge never rebase, removes the
  worktree and its branch explicitly, and hands the worker its next task order by continuing the same subagent with
  its context intact; no respawn, no cold start. At each merge the COO reads every row the branch carries: an `ARMED`
  row whose `disarm_owner` is dark is the COO's to re-seat, since the COO is the seat that spawns, and one it cannot
  seat rides the COO's drain-end read to the CTO. A worker with an empty queue ends. A worker that dies mid-task-order
  leaves a branch; the COO merges it if its instance is valid and otherwise discards it and re-dispatches the task
  order to a fresh slot.
- **Gate:** `.tools/surprise-row-gate.py` at commit refuses a new investigation row without both halves, off its
  enums, or off its project. `.tools/proof-of-spec-check.py` at completion refuses an instance that fails its schema,
  whose cells and criteria do not align in both directions, whose artifact rows do not resolve at their pins, or whose
  `surprises` entries do not each open with a row id present in the project's investigation file; the L6 gate refuses
  a terminal `<status>` flip without a valid instance. Lanes admit the worker on `deliverables/<serial>/`,
  `task-orders/` for its own status flip, `surprise-channel/investigations/`, and `cards/`. The worker's toolkit is the
  worker agent type's frontmatter, and the checker's match of an output against its expectation is the checker's
  limb; until each exists it binds by reading (section 4).
- **Handoff:** the investigation rows, to L8; the merged branch, to HEAD.

### L8 — Compilation

- **Owner:** `3.0.0_SA_CVO`, whose engagement with the project begins here. **Not engaged:** the owners of L1 to L7
  as reviewers of this limb; every worker, which has no inbox. The CVO sends nothing to anyone during a round; its
  findings travel up in the slug at L10, to the CTO and to no one else, and reach the COO through the CTO's round-N
  analysis. A worker never hears from the CVO. A row's `disarm_owner` names who disarms, never whom the CVO may
  message; a disarm the CVO cannot make in its own lane is a row, read by its owner from the channel.
- **Input:** new investigation rows on either channel root, the workers' rows and no others. **Output:** the compiled
  channel, append-only during the round, and the CVO's heartbeat summary carrying the channel's watermark: rows seen,
  rows undispositioned, the watcher's process and its parent-tied banner.
- **Tool:** `org/surprise_channel/surprise-watch.sh <serial> stream` (a read-only watermark on both roots, one line
  per new row, at-least-once) is the CVO's intake; `comp-surprise` is the rollup over both roots. The depth lives here:
  comp-find, comp-read, the graph, the adversary lens, an atomic decomposition of a row that needs one; only a row
  that is ambiguous draws that depth, and the worker face, the one-clause criterion and the split channel exist so
  that what the CVO reads is short and its depth lands where the ambiguity is.
- **Stall.** A dead watcher and a quiet channel read alike. When every task order is terminal the COO reads the CVO's
  watermark once against the channel's row count; if the watermark is behind, the COO tells the CTO, not the CVO, and
  the CTO re-arms the watcher. That drain-end read is the COO's one message of a round: the watermark, and any armed
  row whose disarm owner the COO could not seat. One read, no monitor, no cron.
- **Gate:** `org/mcp/cvo_send_guard.py`, on the broker's send path, refuses a message from the CVO to any Tier-2
  serial while a tree project reads `dep_stage: EXECUTING`; the whole send is refused and nothing is written. The
  watcher notifies and never blocks. The CVO's single admitted send of a round, the slug to the CTO, binds by reading
  until the guard is narrowed to it (section 4).
- **Handoff:** every row to L9.

### L9 — Adjudication

- **Owner:** `3.0.0_SA_CVO`. **Not engaged:** every other seat.
- **Input:** the investigation rows and every proof-of-spec instance under the project. **Output:** in the CVO's own
  document, `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/adjudications/ADJUDICATION_v<N>.md`, a `disposition` on
  every investigation row (`UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON`, `DECOMP_INVALIDATING`), each
  a new row naming the item it adjudicates, together with the CVO's corrections and its own observations, so that the
  investigation document carries worker rows only; the grade of every judgment criterion, read against the
  specification that issued it, since the checker grades no criterion's truth and the worker records without a
  verdict; and, for graduated rows, remediation rows at
  `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/remediations/REMEDIATION_v<N>.md`, issued as ONE slug for the
  round at L10 (one artifact, one moment), never as a stream of messages during L7 to L9. Graduation is a grounding bar:
  a row graduates when its mechanism is attributed, its denominators carried and its remedy holder named; severity
  decides where it lands, grounding decides whether it graduates. `DECOMP_INVALIDATING` names a row whose remedy needs
  a cell the decomposition does not contain; it is carried in the slug like every disposition, it never interrupts the
  round, and the re-decomposition it implies is the COO's call at the recut. A remediation row carries no route: the
  slug's reader is always the CTO and the recut is always the COO's. A graduated row whose remedy was executed inside
  the round by its owner carries `REMEDIATED` and, if it was armed, `DISARMED`, and re-enters nowhere.
- **Tool:** the surprise-channel protocol and its row schemas at `org/surprise_channel/schemas/`.
- **Gate:** `.tools/surprise-row-gate.py` refuses a new remediation row without its required fields, off its enums,
  or a graduated row without grounded evidence. Lane `TREE_CVO` admits only the CVO to `remediations/` and to
  `adjudications/`. The gate's route limb, which refuses an open remediation row that carries no route, and its
  census, which reads the investigation document alone, each contradict this text and are retired or extended as a
  build act; until then a slug lands only by the gate's audited override and the CVO's rows sit in the investigation
  document (section 4).
- **Handoff:** the remediation rows, to L10.

### L10 — The slug, the CTO's read, the recut, the close

- **Owner:** `3.0.0_SA_CVO` issues the slug; `1.0.0_SA_CTO` routes, always; `2.0.0_SA_COO` recuts. **Not engaged:**
  every worker; `3.0.0_SA_CVO` after the slug; `2.0.0_SA_COO` until the round-N analysis reaches it.
- **Precondition:** every task order under the project is terminal, each finished with a valid proof-of-spec instance
  whose `surprises` entries resolve to rows, and every investigation row is dispositioned.
- **The slug.** The CVO writes the round's remediation document, the one artifact of the round, and sends its only
  message of the round: the slug's path and vintage, to `1.0.0_SA_CTO`. There is no route token and no route owner;
  the CTO is the single router of every round.
- **The CTO's read.** First coverage: for each outcome in the PRD header, do the proof-of-spec instances at HEAD,
  taken together, reach its `DONE WHEN`; this is the same read as the close's grades, one verdict per outcome, against
  the exercised artifact, never the report. Then one of two answers. An outcome no cell ever served takes a PRD
  addendum: the CTO bumps `prd_version`, the L4 notifier delivers the header to the COO, and the loop runs forward from
  L4; this is rare by design, because an uncovered outcome means L5 missed it and the decomposition is over the manifest
  the CTO wrote. Otherwise the CTO writes `ledger/ROUND_ANALYSIS.round<N>.md`: per outcome, the expectation against
  what was delivered, what the remediations file says about it, what the adjudications say of each judgment criterion,
  and what the next drain should carry; and hands it to the COO with the remediations file, one message, two artifacts.
- **The recut.** The COO reads both, adds or recuts task orders as its own judgment dictates, a re-decomposed cell, a
  re-issued task order, new cells for an addendum, and issues them as one issuance again under L6, covering every
  affected cell; the choice between a re-decomposition and a re-issue is the COO's and is recorded in the issuance
  commit, never routed. The round runs again from the three tracks. A finding whose remedy lies outside this project's
  chain is not recut and no analysis targets another project: the row's `disarm_owner` fixes it in place when the fix
  lies inside that owner's lane, or the row is `DISMISSED_WITH_REASON` naming the brief or record that opens the owning
  surface's own project at L1; one project's loop never writes into another's.
- **The close:** two reads on two axes. `2.0.0_SA_COO`, the only seat that can say the decomposition is spent (every
  cell holds a terminal task order with a valid proof-of-spec), writes `ledger/COMPLETION_REPORT.round<N>.json`: one
  row per outcome in the PRD header, the cells that served it, each cell's proof-of-spec, and the claim `COVERED` or
  `UNCOVERED`, both denominators printed, so an outcome no cell ever served shows in the COO's own report; it is the
  final drain record. `1.0.0_SA_CTO` reads the exercised artifact each outcome's `DONE WHEN` names, never the report,
  and writes `ledger/COMPLETION_GRADES.round<N>.json`: one verdict per outcome, `REALIZED`, `NOT_REALIZED` or
  `NOT_EVALUATED`, the artifact and its vintage cited, the observed state matching the card's state, and the artifacts
  covering every limb of the card's acceptance clause; a control window that makes a limb true by construction is not
  evidence for it, and a limb no artifact covers grades `NOT_EVALUATED`; it is the last round-N analysis. `CLOSED`
  follows mechanically when every grade reads `REALIZED` and no grade cites a state below its card. A `NOT_REALIZED`
  is the CTO's own round-N analysis for the next drain, or a PRD addendum where the outcome itself is wrong; a grade
  in question on receipt is adjudicated by the CTO as at L2. An outcome whose `DONE WHEN` is an act after the work is
  met by a closing-pass task order whose specification is that act. Then the registry bookkeeping: terminal status,
  completion date, registry row. Contract: `org/standards/COMPLETION_REPORT.schema.json`.
- **Tool:** the remediation document; `.tools/prd-header-notify.py` delivers an addendum's bumped header to the COO and
  re-offers until READ; the round-N analysis travels by one message from the CTO to the COO.
- **Gate:** `.tools/surprise-row-gate.py` refuses a remediation row while any task order under the project is not
  terminal or any investigation item under it is not dispositioned. An existing item is dispositioned by a new
  adjudication row that names it in `adjudicates`; the channel stays append-only. `.tools/missions-tree-index.py check`
  refuses a `CLOSED` row unless the completion report and the grades exist for the same round, cover exactly the
  header's outcomes, and every grade reads `REALIZED`.
- **Handoff:** the slug to the CTO and to no one else; the round-N analysis to the COO and to no one else;
  `dep_stage: ROUND_CLOSE` on the CTO's receipt of the slug, then `CLOSED` on the CTO's grades, both flipped by the
  row owner.

### Midstream — one seat's truth-gathering

A project picked up mid-round, after a restart, a dead session or a handoff, has one seat with state worth recovering:
the COO. Workers are subagents and die with it; their work is either merged at HEAD or on a worktree branch, and both
are durable. The CVO's state is the channel files and its watermark. The CTO's state is the PRD. The COO's restart is
three reads on three gated artifacts, not a procedure: which task orders are terminal, from the proof-of-spec
instances at HEAD and never from a `<status>` field, so an instance absent or invalid is not terminal whatever the
field says; which worktree branches exist, each a worker that died mid-task-order, merged if its instance is valid
and otherwise discarded and re-dispatched; which rows are undispositioned, from the row gate's census run read-only.
A round that was issued to seats rather than workers has a fourth read, the uncommitted and untracked edits under the
project's paths that a dead seat left in the shared tree; those are finished or discarded by the COO, one commit per
task order, with the CVO validating each against the task order's criteria, and no seat checks out or cleans another's
unfinished edit. Then the COO re-dispatches the non-terminal task orders to fresh slots under L6, the CVO re-arms its
watcher from its watermark, and the CTO does nothing. `/canonical-flow` is the instrument of this read for every seat.

### Cross-cutting — the integrator

`0.0.0_AB_MSTR` holds the directive register, opens and closes the push windows on the shared branch, and seats
classes on request. It works no limb, holds no task order and spawns no worker. Whether a commit is on origin is a
measured property of every done test, read by `ls-remote`, never a cell of a decomposition.

---

## 2. Role exclusivity — the guard on each half

| limb | owner only | writes refused by | engagement by message |
|---|---|---|---|
| L1 | `4.0.0_SA_CRO` | none (the brief's shape is refused at L6) | binds by reading |
| L2–L4 | `1.0.0_SA_CTO` | lane `ANY_CTO` on `prd/`; lane `TREE_PROJECT_ROW` on the row | binds by reading |
| L5–L6, the drain | `2.0.0_SA_COO` | lane `TREE_COO` on `decompositions/`, and on `task-orders/` for issuance | binds by reading; the COO's one message of a round is the drain-end read to the CTO |
| L7 | worker subagents of the COO | the L6 gate refuses a Tier-0 or Tier-1 `<issued_to>`; the worker agent type has no send tool | not applicable: a worker cannot be messaged and cannot message |
| L8–L9, the slug | `3.0.0_SA_CVO` | lane `TREE_CVO` on `remediations/` and `adjudications/`; `investigations/` and `cards/` admit every seat | the CVO's one message of a round is the slug to the CTO |
| L10 read, close | `1.0.0_SA_CTO` | lane `TREE_LEDGER` on `ledger/`; lane `ANY_CTO` on `prd/` | the CTO's one message of a round is the round-N analysis to the COO |
| integrator | `0.0.0_AB_MSTR` | the pre-push deploy gate on deploy scope | binds by reading |

Three simultaneous projects are one CTO, one COO per project (the base and its lanes), and one CVO across them until a
measured channel backlog says otherwise.

---

## 3. Limb, owner, `dep_stage`, refuser

| limb | owner | `dep_stage` after the limb | refuses at commit | refuses at completion | notifies |
|---|---|---|---|---|---|
| L1 brief | `4.0.0_SA_CRO` | none | — | — | — |
| L2 endpoint | `1.0.0_SA_CTO` | none | — | — | — |
| L3 register | `1.0.0_SA_CTO` | `REGISTERED` | `missions-tree-check.sh` | — | — |
| L4 PRD | `1.0.0_SA_CTO` | `PRD` | lane `ANY_CTO` | — | `prd-header-notify.py` to the COO |
| L5 decomposition | `2.0.0_SA_COO` | `DECOMP` | lane `TREE_COO` | — | — |
| L6 issuance | `2.0.0_SA_COO` | `EXECUTING` | `to-proof-of-spec-check.sh`, `to-pipeline-gate.py`, lane `TREE_COO` | — | — |
| L7 execution | a worker subagent | `EXECUTING` | `surprise-row-gate.py` (rows) | `proof-of-spec-check.py`; the terminal-flip limb of `to-pipeline-gate.py` | — |
| L8 compilation | `3.0.0_SA_CVO` | `EXECUTING` | at send: `org/mcp/cvo_send_guard.py` | — | `surprise-watch.sh` to the CVO |
| L9 adjudication | `3.0.0_SA_CVO` | `EXECUTING` | `surprise-row-gate.py` (rows), lane `TREE_CVO` | — | — |
| L10 slug, read, recut, close | `3.0.0_SA_CVO` issues the slug; `1.0.0_SA_CTO` reads and routes; `2.0.0_SA_COO` recuts; at the close `2.0.0_SA_COO` reports, `1.0.0_SA_CTO` grades | `ROUND_CLOSE`, `CLOSED` | `surprise-row-gate.py` (precondition); `missions-tree-index.py check` (the `CLOSED` flip) | — | `prd-header-notify.py` (an addendum's header) to the COO |

Every notification and every acknowledgement is read on the broker's delivery ledger: sent, emitted and read are
three states, and only an agent's own acknowledgement is read. A worker is on no ledger; its completion is its
proof-of-spec instance at HEAD.

---

## 4. What binds by reading

The citable brief and the qualitative outcomes at L1 and L2; the arc and defined outcome of the PRD; the choice to
use the decomposition method's validator at L5; the worker's significance judgment at L7, which is deliberately not
the worker's; the CVO's engagement beginning at L8; the grounding bar at L9; the dispositioned half of the L10
precondition; role exclusivity against engagement by message at every limb; the integrator-only push. Everything
else in section 3 refuses.

Eight clauses of this text name a carrier that is not yet built or that a live mechanism contradicts. Each is a build
act named in the authorizing record of the version that introduced it; until it lands the clause binds by reading,
and where a live gate contradicts it the gate's own audited override is the only lawful way through, written into the
commit that uses it.

- **The issuance covers every cell.** The L6 gate's coverage limb, one set comparison of the union of `<owned_cells>`
  across the staged task orders against the decomposition's cell set, does not exist; the coverage binds by reading.
- **The COO flips `EXECUTING` in the issuance commit.** The row lane admits only the CTO to `project.json`; until the
  registry grantor widens that lane to the COO for this act, the issuance commit that carries the flip is refused, and
  the CTO flips the row in the same window.
- **The worker's toolkit.** The worker agent type at `.claude/agents/worker.md` fixes the toolkit and the model; until
  its first exercised spawn commits under a worker serial through the lane gates, its silence binds by reading.
- **One clause per criterion.** The proof-of-spec instance carries a criterion's invocation, output and denominator
  and no expectation pattern or judgment flag; the checker grades no criterion's truth. The expectation match at the
  checker, the judgment flag on the criterion, and the L6 refusal of a compound criterion or of a mechanical criterion
  without its invocation and expectation are build acts; until they land, a worker's pass is self-graded as before and
  the CVO's L9 read of the instance against the specification is the only grade.
- **The adjudication document.** The tree contract has no `adjudications/` folder, the row gate's census reads the
  investigation document alone, and `adjudicates` resolves within one document; until the folder, the census and the
  cross-document resolution land, the CVO's rows sit in the investigation document as before.
- **A remediation row carries no route.** The row gate's route limb refuses an open remediation row without one; a
  slug lands through the gate's audited override until the limb is retired.
- **The CVO's single send.** The send guard admits the CVO to the COO at every stage; the CVO's silence toward the COO
  during a round binds by reading until the guard is narrowed to the slug.
- **The fail-closed sentinels.** The pre-commit sentinels match the flat channel and task-order paths, not the tree's.

---

## 5. Amendment protocol

This file is amended as a whole, by `1.0.0_SA_CTO` as the scribe of process law, on Andrew's word or on a finding the
CTO's round-N analysis raises to law. Each amendment is a new version with one changelog line naming the record that
authorized it. No in-place markers, no partial-clause patches, no quotations, no dates or hashes in the body.
Independent review of an amendment is the CVO's constitutional review role and is not an engagement with any limb.
A document that describes this process in a second shape is retired to a redirect the day it is found. A round open
at the moment of an amendment finishes under the task orders already cut, because the specification is frozen for a
round; the next issuance is under the amended text. An amendment of the round's mechanics is graded on the compiled
step log of the first project run under it: the share of every seat's acts that fall outside the ten limbs is the
verdict, read against the last round under the prior text on the same instrument.

---

## 6. Changelog

| version | date | authorizing record | summary |
|---|---|---|---|
| 1.0 | 2026-09-01 | `org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` | first text of the ten steps and the surprise flow |
| 2.0 | 2026-09-03 | state of record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_024xZ_CANONICAL_WORKFLOW_L1_L10_STATE_OF_RECORD.md` @716a9bc7ce (LD-0521); brief `org/tier0_exec/0.0.0_AB_MSTR/deliverables/BRIEF_20260903_CANONICAL_FABRIC_WORKFLOW_SPEC_TEN_LIMBS_ONE_PROCESS.md` @ba9add4200; water test `workflows/atom_decomposition/runs/canonical-fabric-workflow-spec/20260903T0305Z/` | constitutional form; ten limbs with one owner each and the not-engaged set; the project tree homes; the surprise row as the only carrier; the L6 refusal of Tier-0/1 seating and the L10 precondition gate; the proof-of-spec surprises limb; worker commits its own status; the earlier second description of the process retired to a redirect |
| 2.1 | 2026-09-03 | `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_L7_L10_LOOP_CVO_RELAYS_TO_COO_NEVER_CONVERSES_WITH_WORKERS.md` @10a4beaffb; `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_ALL_TOS_PROOF_OF_SPEC_BEFORE_LOOPBACK_CVO_REMEDIATION_SLUG_AT_L10.md` @de2d6d643c | the L7 to L10 loop: the CVO's findings travel up to the COO (or the CTO for a scope change) and never down to a worker; remediations are one slug at L10; every task order finishes with its valid proof-of-spec before any loop-back; the pass re-enters at L5 or L6 as fresh and remediated task orders in dependency order; the L10 handoff is to the route owner only |
| 2.2 | 2026-09-03 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_045xZ_RECS_APPROVED_CVO_SEND_REFUSED_L7_L9_GATE_III_INVESTIGATIONS_LIMB.md` | two refusers for clauses that bound by reading: the L8 send guard on the broker path (CVO to a Tier-2 serial refused while a tree project is executing) and the second limb of the L10 gate (no route while an investigation item is undispositioned; both route shapes; the `adjudicates` carrier) |
| 2.3 | 2026-09-03 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md` | the close: the COO's completion report and the CTO's grades, two reads on two axes, the `CLOSED` flip mechanical on the grades (`missions-tree-index.py` R6, `COMPLETION_REPORT.schema.json`); autonomy after L2 -- Andrew confirms the `DONE WHEN` lines at L2 and no limb waits on him after; `SCOPE_CHANGE` and a questioned grade are adjudicated by the CTO (`/open-calls --adjudicate`) and the loop runs forward from L4 |
| 2.4 | 2026-09-03 | `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` @f9ca7a9309 -- the in-place disarm of NFRA_CLDGRPH round 1's first finding, whose remedy lay in another surface's document; the question relayed by the run's L2 owner to the scribe | the routes are about this project's own chain; an outside remedy is a disarm in place within the owner's lane or a `DISMISSED_WITH_REASON` naming the brief that opens the owning surface's own project at L1; no route targets another project |
| 2.5 | 2026-09-03 | `org/standards/COMPLETION_REPORT.schema.json` (the grader's bar in the contract) | the close's grading bars stated in the process rather than in messages: a `REALIZED` grade cites artifacts covering every limb of the card's acceptance clause and a vacuous control window is not evidence; the observed state never sits below the card's state (mechanical in the tree check) |
| 2.6 | 2026-09-03 | `.tools/surprise-row-gate.py` (the gate-model fork between the two fabrics' CTOs, ruled at the base) | a graduated row whose remedy was executed inside the round (`REMEDIATED`, and `DISARMED` if armed) carries no route and re-enters nowhere; every other route-less remediation row is refused |
| 3.0 | 2026-09-03 | implementation spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/SPEC_CANONICAL_FLOW_V3_SUBAGENT_WORKERS_ONE_SHOT_DISPATCH_20260903.md` @29bf9265ea (sections 3 to 9, on Andrew's word at the CRO terminal) and its section 13 @9dc97d860d (six levers read from one thread of NFRA_COMPEFFICACY's round 1-6 artifacts, on Andrew's question at the CRO terminal); Andrew's word at the CTO terminal, recorded at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_200xZ_CANONICAL_FLOW_V3_RESTRUCTURE_SPINE_SKILL_CLAUDEMD_SINGLEHANDED.md`; Andrew's word at the MSTR terminal on the outage remediation (LD-0532, `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_200xZ_OUTAGE_REMEDIATION_CTO_CANONICAL_FLOW_COO_CVO_CLEANUP_RUN.md` @c44bd68273); the problems brief `docs/briefs/canonical-flow-l6-l10-mechanism-gaps-20260903.md` @6a1d845ecb that the spec answers | L6 is one issuance covering every cell, fan-out derived from the decomposition's chains and stated as data in the issuance commit with a default cap of eight; a task order has a worker face and a record face and only the worker face travels; one clause per criterion, a mechanical criterion carrying its invocation and expectation, a judgment criterion flagged and graded only by the CVO, a compound criterion refused; the decomposition frozen at the cut; workers are subagents of the COO, serial `0.9.0_WK_<CODE>~<n>`, a minimal toolkit with no send tool, one worktree each, a cursory verification bar, a queue drained by continuation; the spawn is the GO and no broker message carries it; three tracks share files and never messages, the CVO's one send is the slug to the CTO, the CTO's one send is the round-N analysis to the COO; the surprise channel split by writer into investigations, adjudications and remediations so L8 reads and L10 counts worker rows only; the three route tokens are retired and the CTO is the single router, answering the slug with a PRD addendum for an outcome no cell served or a round-N analysis the COO recuts in one issuance; the stall read by watermark at drain-end; the midstream restart as three reads, four for a round issued to seats, with a dead seat's unfinished edits finished or discarded by the COO under the CVO's validation; the close unchanged; eight clauses named in section 4 as binding by reading until their carriers land, four of them contradicted by a live gate or lane; the transition rule that an open round finishes under its cut task orders; an amendment of the round's mechanics graded on the compiled step log's share of acts outside the limbs |
| 3.1 | 2026-09-03 | `3.0.0_SA_CVO`'s constitutional review of the annex at v3.0 (message 93939), which accepted the annex and upheld the adjudication document, and raised two findings for the scribe; the worker agent type landed at `.claude/agents/worker.md` | an `ARMED` row whose disarm owner is dark has a carrier: the COO reads every row a branch carries at the merge, re-seats a dark owner as the seat that spawns, and carries one it cannot seat in its drain-end read; the drain-end read is named as the COO's one message of a round, the watermark and any owner it could not seat, so section 2 and L8 agree; the worker-toolkit clause of section 4 now names its carrier and binds by reading only until the first exercised spawn |
