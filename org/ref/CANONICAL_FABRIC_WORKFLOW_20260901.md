# THE CANONICAL FABRIC WORKFLOW

**Status:** constitutional. This document is the one specification of how the Opal fabric takes a topic from a brief
to a closed project. There is one process, the ten limbs L1 to L10, and every document, gate, skill and record that
touches the process resolves to this file. Amendment is by whole-file version under the protocol in section 5; the
authorizing records are named only in the changelog (section 6).

**Vocabulary.** A **limb** is one of the ten numbered hops; "step" is an accepted synonym. A **seat** is an agent
serial registered on the broker. A **worker** is a subagent of the COO that issued its task order: it has a serial for
commits and no telemetry, and no seat, no inbox and no send tool. **Owner** means the only seat that performs the limb;
**not engaged** means no other seat reviews, grades, certifies, or acts on that limb's artifact while the limb is open.
An **issuance** is the one commit that cuts a task order for every cell of a decomposition; a **round** is one drain of
an issuance. A task order has a **worker face**, the part a worker is given and the whole of its context, and a
**record face**, the part the gates read and a worker never sees. A **track** is one of the three concurrent lines of
work inside a round, the COO's, the CVO's and the CTO's; tracks share files and never messages. The **slug** is the
CVO's one artifact of a round; the **round-N analysis** and the **PRD addendum** are the CTO's two possible answers
to it. The **thread** is one named person's one journey through a product at coarse resolution, run LIVE through
every real hop from the screen to the data and back, and proven by one trace artifact that records each hop's
request and response and ends in the rendered result; a thread with any hop fed by a fixture is not done. For a
product with a frontend, **live** means the real backend, real data and real login, with the frontend running locally
or on DEV; a PROD release is an enrichment item, not part of the thread. For a pipeline, the person is the consumer
of the served output. For a backend or infrastructure product, live is defined at L2. An
**enrichment round** is any round after the first: it adds the capabilities the CTO's round-N analysis names in its
enrichment list, with the thread kept working. A **gate** refuses at commit or at completion; a **notifier** delivers and never blocks; **binds by reading**
means the sentence has no mechanical carrier. The register's `dep_stage` enum (`REGISTERED`, `PRD`, `DECOMP`,
`EXECUTING`, `ROUND_CLOSE`, `CLOSED`) is data; its limb mapping is in section 3.

**Project tree.** Every project lives at `org/missions/D<n>/<MACRO>/<CODE>/` with the subfolders `brief/`, `prd/`,
`decompositions/`, `task-orders/`, `deliverables/<serial>/`, `surprise-channel/investigations/`,
`surprise-channel/adjudications/`, `surprise-channel/remediations/`, `ledger/`, `cards/`. The row is `project.json`;
the flat index entry `org/projects/<CODE>.json` is generated from it and carries `home`. The grammar is
`org/standards/PROJECT_TREE.contract.json`.

---

## 1. The ten limbs

**The shape of a round.** L1 to L5 run once, in order, each handing its artifact to the next. **Round 1 builds the
thread, the whole journey end to end at coarse resolution, rough and incomplete but working; every later round is an
enrichment round.** The product is known to work from the first round, and each later round adds to something that
already runs, instead of proving components one at a time and joining them last. L6 cuts every task
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
  L1 brief -> L2 endpoint -> L3 register -> L4 PRD -> L4-R sign-off gate -> L5 decomposition + battery (frozen at the cut)
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
  are the two other admitted shapes), every line citable. A brief for a product or pipeline names its candidate
  thread: which person, which journey, at coarse grain, so L2 has something to cut the first outcome from.
- **Tool:** `/brief-create`.
- **Gate:** none at L1. The brief's path shape is refused at L6 by the PRD header pattern if it is none of the three.
- **Handoff:** the brief's path and vintage, `<path>@<commit>`, become the PRD header's `brief_ref`.

### L2 — Endpoint

- **Owner:** `1.0.0_SA_CTO`. **Not engaged:** `2.0.0_SA_COO`, `3.0.0_SA_CVO`, every worker.
- **Input:** the brief. **Output:** numbered qualitative outcomes `FWD-1..n`, each citing a brief line, carrying no
  numbers, each disputable; ids are permanent and never reused.
- **THE THREAD IS THE FIRST OUTCOME.** For a product or a pipeline, `FWD-1` is the thread, its `DONE WHEN` reading
  `EXERCISED -- one live trace ending in the rendered result`; every other outcome is cut as before and is served by
  the enrichment rounds. The seam between any two components lies inside the thread by construction, so it always has
  an owner. For a pipeline with no product surface the thread is source to served artifact, and its person is the
  consumer of that artifact. COST: one outcome. For a backend or infrastructure product the thread is one named
  consumer's one real use of the mechanism -- the real tool at HEAD from an ordinary seat shell, or the deployed
  component, over real inputs, through the entry the consumer uses -- ending in the consumer's observed result,
  recorded as one trace; the result may land on one machine's working branch or in a QA location, and shared-branch
  availability and production scheduling are enrichment items. NON-APPLICATION: a pure governance project, which has
  no mechanism anyone invokes.
- ⛔ **NO FWD IS A WAIT.** Every outcome is PROVABLE BY AN ACT A SEAT CAN TAKE ON DEMAND. An outcome whose only proof is an event nobody
  controls -- a failure, a rare condition, a calendar -- is written WRONG, and the remedy is not patience: it is re-cut so its MECHANISM is
  DRIVEN DELIBERATELY, with the organic case kept as the negative arm. **THE ACT MAY BE A DRIVEN RUN OR A READ OF EXISTING HISTORY** -- driving is
  one form of proof and reading a record that already exists is another; what is forbidden is WAITING FOR AN EVENT. An outcome whose
  property is the ABSENCE of something (that nobody triggered it, that no hand enforced it) cannot be driven at all and is proven by the
  history read, not by qualification. An outcome is SUPERSEDED only when no such act exists; where the substance is provable and only the
  WORDING names a calendar, the remedy is to re-point the `DONE WHEN` at the on-demand read, KEEPING THE ID. Where a wait is genuinely essential it is EXPRESSLY QUALIFIED on the
  outcome, carrying its reason and Andrew's word, and it is the exception that names itself; the default is not a wait. An outcome already
  written as a wait is SUPERSEDED at the next unused id, its text kept verbatim with the reason beside it, never edited away.
  Andrew-direct 2026-09-10 ~03:0xZ: *"no FWD is ever a 'wait' unless explicitly advised otherwise ... our goal with projects and task
  orders is not to sit on them for weeks, it is to sprint, execute, validate, and close"*. This is the L2 half of his ~21:4xZ
  manual-trigger word (which binds the ACCEPT at L4/L6): the accept rule is the cure, this is the prevention. **Measured the same night:**
  `ETFS_GUARDRAIL` FWD-7 sat NOT_EVALUATED as "a real terminal failure, rare by design" while the terminal send guard read a key the
  renderer never writes and COULD NOT FIRE AT ALL -- the wait would have been permanent and nothing would ever have said so.
- **Tool:** `/endpoint --forward <brief>`. Andrew confirms the `DONE WHEN` line of every outcome here; it is his last
  touch point, and after L2 no limb waits on him. The same skill re-enters here from the CTO's own L10 read, when the
  coverage read finds an outcome no cell served or a grade the artifact cannot settle: the CTO adjudicates by running
  `/open-calls --adjudicate` on the subject, rules on the recommendations itself, records the ruling, appends the new
  outcomes at the next unused ids, re-issues the PRD as an addendum, and the loop runs forward from L4.
- **Gate:** none at L2. At L6 the L6 gate refuses a task order whose PRD does not define every listed outcome in its
  endpoint section, and every defined outcome not listed in the header.
- **Handoff:** the outcomes land inside the PRD as its endpoint section.

### L3 — Register

- **Owner:** `1.0.0_SA_CTO`. **Not engaged:** `2.0.0_SA_COO`, `3.0.0_SA_CVO`, every worker. `0.0.0_AB_MSTR` is NOT
  ENGAGED AT L3 EITHER: it retains write access to `DIRECTIVES.yaml` and `MACROS.yaml` as an integrator fallback and
  gates neither; the CTO writes all four carriers — tree row, generated index, members line, macro enum — in one commit
  (Andrew-direct 2026-09-10 ~20:1xZ; LD-0542).
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
  defined outcome, the surface manifest, one row per engine, and for a product or pipeline two further sections: the
  **THREAD**, the hop list of the first outcome written `N. A -> B`, one line per hop, and the **ENRICHMENT BACKLOG**,
  everything off the thread, ordered, one line each. Both sit in the brief half of the sign-off below. **One product
  is one project; its first outcome is one journey; it is never split into a frontend project and a backend
  project.** Where such a split already exists, the two PRDs name one project as the owner of each seam hop until the
  product is re-registered as one project (a closer's hand-back does this). Every specification decision is closed in the PRD;
  a decision that is an enumeration is closed as data in `org/standards/` and cited; a PRD carries no open
  decide-first question into L5. Any substantive edit bumps `prd_version`; a PRD addendum from L10 is such an edit,
  by the same owner, and re-enters L5 through the same notifier as a first PRD.
- **Tool:** the PRD authoring protocol and the template it names.
- **Gate:** lane `ANY_CTO` refuses any other author's write to `prd/`. At L6 the L6 gate refuses a task order whose
  PRD lacks the header, fails its schema, disagrees with the row on identity, lacks the endpoint section, or lacks the
  surface manifest.
- **Notifier:** `.tools/prd-header-notify.py` (post-commit) delivers each HALF of a new or bumped PRD that is not
  already signed at its current bytes to the reviewer ROUTED for it (L4-R below), and delivers to `2.0.0_SA_COO`
  ONLY once both halves are SIGNED; it re-offers until READ, nudges an overdue half with the CTO copied, and
  re-routes an overdue brief half to a live COO. The handoff to L5 is the COO notification, never a dispatch.
- **Handoff:** `dep_stage: PRD` **and** both halves SIGNED at the PRD's current bytes (`python .tools/prd-signoff.py
  status <CODE>` reads ADMITTED).

### L4-R — The PRD sign-off gate (v3.15)

- **Owner:** two HALVES, one reviewer each. `3.0.0_SA_CVO` signs the RATIFIED-TEXT half (the ENDPOINT and CONTRACTS
  sections) -- always, nobody substitutes. `4.0.0_SA_CRO` signs the BRIEF half (every other section); when no CRO
  session is live, or the CRO is overdue, a live `2.0.0_SA_COO` instance that is NOT this project's round holder
  signs in its stead and the file records `substitute_for`. **Not engaged:** `1.0.0_SA_CTO` (the author; it cannot
  sign), the COO lane that will decompose this PRD (it cannot sign the brief half it decomposes), every worker.
  Andrew-direct 2026-09-10 ~21:2xZ: *"CRO and CVO should have to sign off on PRD before COO gets it"*; 2026-09-11
  ~05:3xZ: *"CVO should always be included. If CRO is not online, can do COO in their stead."*
- **Binding:** both halves bind to the HASH of the ENDPOINT section alone at HEAD (`half_hash`), never to
  `prd_version` and never to any other section. A wording change anywhere else re-opens nothing and withholds no
  delivery; only an ENDPOINT change re-signs. **The brief half is admitted without a signature when the brief was
  written by a `4.0.0_SA_CRO` serial** (the brief's authoring commit, read by the lib), so on such a project the one
  reviewer is the CVO. Sign-off files written before this binding carried their half's own sections; they are read
  against the ENDPOINT hash from now on, so a file whose ENDPOINT is unchanged stays SIGNED.
- **Trigger:** the L4 notifier, on every new or bumped header, for each half still owed at the current bytes; the
  message names the half, the review it asks for, the stamp command and the window.
- **Input:** the PRD at HEAD; the brief at the pin `brief_ref` names; the endpoint at the pins the ENDPOINT section
  cites; the counterpart PRD where the project has one.
- **The RATIFIED-TEXT half** (`3.0.0_SA_CVO`): every DONE WHEN, ACCEPT and PROOF in the ENDPOINT section is verbatim
  from the ratified pins; every operative constraint is present; no annotation, history or seat name is inside the
  SECTION (heading to next heading -- the gate's own `_top_section`); the CONTRACTS section agrees with the
  counterpart PRD.
- **The BRIEF half** (`4.0.0_SA_CRO`, or the substitute): every entry of the BRIEF COVERAGE map (and any supplement
  map) carries its section's CONTENT into the consuming cell -- fields, units, paths, guards, proof gaps -- not a
  pointer; the heading denominator matches the brief at the named pin; cell rows name the right counterpart cells.
  Corrections return BY PINNED LINE in the review record.
- **The stamp:** `python .tools/prd-signoff.py sign|refuse <CODE> --half brief|ratified-text --review <path>@<pin>
  [--reason "..."] [--for <primary>]`. It writes `org/missions/D<n>/<MACRO>/<CODE>/prd/signoff/<serial>.json` in lane
  `TREE_PRD_SIGNOFF` -- `{prd, prd_version, prd_pin, half, half_hash, verdict, review_ref, signed_by, signed_at
  [, substitute_for, reason]}` -- bound to HEAD's bytes (it refuses an uncommitted PRD edit), commits it through
  `safe-commit` under the signer's serial, and prints the gate's verdict. A REFUSED verdict carries the pinned
  review and one-line reason and lands the same way; the CTO answers a REFUSED with a bump that touches only what
  the review named. `python .tools/prd-signoff.py status [<CODE>]` is the one read of what is owed and by whom;
  nobody asks a seat what it is doing.
- **Window and escalation, automatic:** a half is OVERDUE `REVIEW_WINDOW_MINUTES` (60) after its delivery. The
  notifier (commit-driven, so it runs on every seat's commit) then re-sends the half as an OVERDUE nudge to the
  routed reviewer with `1.0.0_SA_CTO` copied; after two windows a brief half still owed is offered to a live COO
  instead; the ratified-text half is only ever re-asked of the CVO. READ is not SIGNED: a read ack retires the
  delivery row, never the half.
- **Gate, two carriers, both mechanical, ONE rule** (`.tools/prd_signoff_lib.py`, called by both and by the stamp):
  (1) the notifier withholds the COO delivery until both halves are SIGNED at the current bytes and releases it on
  the sign-off commit; (2) `.tools/to-pipeline-gate.py` LIMB 6 refuses a task order whose PRD has a half MISSING,
  STALE, REFUSED, NOT-PERMITTED or unreadable, naming the half. Separation of duties: `prd/**` is lane `ANY_CTO`,
  `prd/signoff/**` is lane `TREE_PRD_SIGNOFF`; the author and the round-holding COO lane are refused by the lib.
- **Multi-round (L10 -> L4):** an addendum is a bump and re-enters here only when it changes the ENDPOINT section;
  the notifier then asks the CVO, and the brief half's owner unless the CRO wrote the brief.
- **Vintage:** a PRD last committed before the L4-R law commit (`f8337502a9`) is grandfathered until its next
  `prd_version` bump (v3.13 non-retroactivity), and `status` says so.
- **Cost:** two reads per changed half, on the critical path by design; a half's re-review is scoped to its delta.
- **Non-application:** a header-only bump or any edit outside the ENDPOINT section re-opens nothing.

### L5 — Decomposition and battery

- **Owner:** `2.0.0_SA_COO`. **Not engaged:** `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, every worker. No seat
  certifies the decomposition before L6; the COO may run the sealed-mutant harness as a self-check that no seat waits on.
- **Input:** the PRD's thread and surface manifest. **Output:** `org/missions/D<n>/<MACRO>/<CODE>/decompositions/<CODE>_DECOMP.md`:
  the rectangle of THIS ROUND. Round 1's rectangle is over the thread's hops, one cell per adapter to build or repair,
  so the first issuance builds the journey and not a layer of it; an enrichment round's rectangle is over the
  enrichment list the round-N analysis names, and over the manifest's surfaces where an item spans them. A project
  with no thread (L2's non-application) keeps the rectangle over the manifest's surfaces. The decomposition carries
  every cell with a status from a vocabulary that has a
  not-evaluated value, cell ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md`, the Rule 24 four-postulate record,
  a placement axis (which fabric executes each cell), dependency edges keyed to observed completion, and a battery
  disposition per lens: the mandatory core `comp-schedule`, `comp-iam`, `comp-adversary`, each `RUN` with a
  denominator or blindness statement or `DECLARED-NOT-APPLICABLE` with a reason, plus any lens of the admitted
  catalog. On round 1 of a threaded project every lens defaults to `DECLARED-NOT-APPLICABLE` with the reason "thread
  round; the lens runs on the enrichment round that touches its surface", except `comp-iam`, which is `RUN` whenever
  the thread touches IAM. A lens whose neighborhood is not the cell's dependency chain, its dependencies' proof instances and the
  PRD rows it cites, but the filesystem around a cited path, states that blindness in its disposition. No cell is
  owned by a seat; every cell is served by a worker at L7. The dependency edges are the input L6 derives its fan-out
  from: a maximal path through them is a chain, and two cells on one chain never run at once. **Cells are cut by write
  set:** each cell owns files no other cell of the round writes. A one-line hookup in a shared file (a mount, an
  import, a route entry, a registry line) belongs to no cell; the COO adds every hookup at the merge. An edge is a
  real data dependency, one cell consuming another's output, never file contention. A batch cell that touches many
  cells' files runs last in its round or folds into the merge. The decomposition is
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
  writes, absolute from the root, its written files disjoint from every other cell's of the round; and `<proof_of_spec>` with one clause per criterion: a mechanical criterion carries
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
  line. Two task orders on one chain belong to one worker's queue; two chains may take two workers. The issuance
  covers every cell of THIS ROUND's decomposition: round 1's decomposition is the thread, and every later round's is
  the enrichment list the CTO's round-N analysis names.
- **Tool:** the task-order protocol; then, per worker slot, the harness's subagent call with the worker agent type and
  a HAND-CUT worktree off CLOUD (`git worktree add -b wk-<code>-<round>-<n> /c/tmp/<slot> CLOUD`, its path in the prompt;
  never the harness's own isolation option, which bases on origin/main with no `org/` or `.tools/`), its prompt the worker face of the slot's first task order verbatim plus the identity line of
  L7. The spawn is the GO; no broker message carries it and no inbox receives it.
- **Gate:** at commit, `.tools/git-hooks/to-proof-of-spec-check.sh` refuses a new task order without `<proof_of_spec>`
  or without `<decomp_ref>`; `.tools/to-pipeline-gate.py` refuses a new task order whose project row is absent, whose
  `dep_stage` or `fabric` is off its enum, whose preflight is incomplete, whose PRD fails L2 or L4's conditions above,
  whose row and folder disagree, whose `<issued_to>` names a Tier-0 or Tier-1 seat, whose criteria are not one
  clause each (a compound criterion, or a mechanical criterion without exactly one invocation and one expectation),
  whose issuance leaves a cell of the decomposition unowned, which is issued to a worker without a `<paths>`
  block, or whose `<risk>` is absent, off its enum, or below the floor its `<paths>` and invocations imply; an
  override is written to `org/to-pipeline-override-audit.log`. Lane `TREE_COO` refuses any other
  author's issuance; lane `TREE_PROJECT_ROW` admits the COO to the row for the `EXECUTING` flip.
- **Handoff:** `dep_stage: EXECUTING`, flipped by the COO in the issuance commit, so the guards that key on the stage
  arm with the act that starts it.
- **THE RISK CLASS DECIDES THE CHECKING.** Every task order carries `<risk>`, one of three values:
  - `LOCAL` -- code, tests or records, including a portal change that lands on DEV only; nothing served moves.
  - `SERVED` -- a PROD promotion or a served data path.
  - `WORLD` -- a deploy, a delete, a grant, a key, or a claim to Andrew.

  The L6 gate infers a floor from the order's `<paths>` and invocations (an infrastructure path or a deploy verb is
  `WORLD`) and refuses a declared class below it. The class decides which limbs engage:
  - `LOCAL`: the worker's proof, the checker's match, and the COO's one real run of the outcome at close (L7, the
    drain). No CVO grade and no CTO exercised read.
  - `SERVED`: adds the CVO's grade of its judgment criteria, on the real run's artifact, never on static markup.
  - `WORLD`: adds the CTO's exercised read and the change-management entry.

  A FAST mode lease never lowers a class.
- **THE DIRECT-ACT PATH.** A unit of work that is one cell, of a declared small size (about 300 product lines or
  fewer) and `LOCAL`, runs no L2, no L4-R and no L8 to L10:
  - the COO writes one order carrying `<direct_act>true</direct_act>`;
  - a worker executes it and it drains;
  - the COO's one real run of the outcome is its close.
- **THE ISSUER RULES INSIDE ITS OWN DECOMPOSITION.** The COO amends its own orders' criteria, re-points a path and
  grants a path mid-round, and names in the amendment commit the gate limb that graded it or that none did; the
  decomposition stays frozen. The CTO rules only on an ENDPOINT change and on `SERVED` or `WORLD` work.
- **CHECKS ARE FILES, DRY-RUN AT THE BASE.** Each mechanical criterion's invocation is a small test or script file
  the issuer writes and runs once against the base before the cut: a build check fails there and a bound or control
  check passes there. One line per check in the issuance commit records the base run. A check that does neither is
  recut before the spawn.
- **THE FACE CARRIES THE CELL, NOT THE RULES.** The standing worker rules are the worker agent type's definition,
  never restated on a face. `<worker_class>` names the agent type the spawn uses: `worker`, or `worker-light` for a
  cell of about 100 product lines or fewer and for the batch repair cell.
- **THE VERIFICATION DIET -- A TASK ORDER IS MOSTLY THE BUILD.** A build task order carries at most THREE mechanical
  criteria: the built behaviour; the hop's seam probe against its REAL neighbour where that neighbour is reachable, a
  fixture only where it is not; and at most one further criterion the cell genuinely needs. A fourth carries a
  one-line reason on the face. A difference-control arm (below) is part of the criterion it controls and is not
  counted as a separate check. Repo-wide
  hygiene -- typecheck, lint, the full suite, `py_compile` -- is never a criterion on an order: the COO runs it once per
  merge at the drain, beside `safe-merge.sh`'s row gate, and re-runs the live thread trace once per round there. A
  judgment criterion appears only where the outcome needs judgment, a user-facing reading or a design-conformance
  grade, and is not a default slot on every face. An instrument, record or style repair is one cell per round, never
  a round of its own (L10). The refusal clause, the difference control and the proof-of-spec instance below are kept
  unchanged: the diet removes volume, not those controls. This is a rule of the cut, carried by the task-order
  protocol and `/dispatch`; no gate counts criteria. COST: none -- a smaller face. NON-APPLICATION: a task order whose
  whole subject is a control, where its difference arm is the build.
- ⛔ **A SEAM PROVED TO DELIVER ITS INPUT IS NOT A SEAM PROVED TO HAVE AN EFFECT. A criterion NAMES THE OUTCOME, never only the
  MECHANISM.** "The value reaches the function" and "the value changes what the function decides" are DIFFERENT CLAIMS, and an
  arm that proves the first reads exactly like an arm that proves the second. Every criterion asserting a control, a fence, a
  flag or a threshold states WHAT MUST DIFFER when it is engaged, and proves that difference against the SAME run with the
  control disengaged -- the arm's own positive control, in one harness. MEASURED 2026-09-10, `ETFS_GUARDRAIL` W4-S6: a forcing
  spec was proved to REACH the classifier and the schedule proved unable to reach it -- both true, both still true -- and the
  ladder then RE-CLASSIFIED from real S3 and discarded it entirely, so the run PUBLISHED where the outcome required a refusal.
  The cut had specified a MECHANISM and never an OUTCOME. Third instance from one seat's cuts in one night (W4-S4, W4-S5, W4-S6).
  ⛔ **A POSITIVE CONTROL IS NOT A DIFFERENCE CONTROL AND DOES NOT DISCHARGE THIS.** A probe that fires so a zero is not a
  dead instrument bounds UNDER-FIRING only; it never shows what CHANGES when the control is engaged. Measured on the first
  audit run against this clause (`2.0.0_SA_COO~A`, its OWN just-drained round): 6 of 20 criteria carry a control arm and
  only **2 of 16 mechanical criteria carry THIS shape** -- the other four are positive controls. **The adoption cost is
  therefore real, not bookkeeping**, and a seat reporting conformance states which of the two it counted.
  COST: one extra arm, run in the same harness with the flag flipped. NON-APPLICATION: a criterion whose subject IS the
  delivery (a transport, a grant, a route), where arrival is the outcome; and **A CENSUS, where the outcome IS THE COUNT
  and the DENOMINATOR is the discipline** -- `2.0.0_SA_COO~A`'s argument, adopted in its terms: an arm reading 55 of 55
  families each with a reason, or facts-per-key with its zero printed, is not proving a control works and owes no flipped
  twin.
  ⛔ **AND IT DOES NOT BIND RETROACTIVELY.** A round is graded against the law in force AT ITS CUT (the v3.0 transition
  rule: an open round finishes under its cut task orders). A criterion that predates the clause is not a defect and is
  never re-cut for it; where an audit shows which criteria carry the arm, **the L9 and L10 grade WITH that audit in hand
  and RECORD THE BOUNDARY IN THE GRADE** rather than re-opening. A round's CLAIM can be sound on paired evidence held
  elsewhere in the same order while the CRITERION does not itself carry it -- that distinction is stated in the grade, and
  stating it is what makes it weighable.
- ⛔ **THE REFUSAL CLAUSE -- A CRITERION IS SHAPED SO THAT REFUSING IT IS CHEAPER THAN RESCUING IT, AND THE FACE SAYS SO.**
  Every face instructs its assignee to REFUSE a criterion it cannot satisfy as written and to report the refusal with its
  measurement, never to repair the criterion, widen it, or satisfy it by a route the cut did not name. **A worker that edits
  the issuance half so its own proof validates certifies an alignment the cut never declared**, which is why the refusal is an
  instruction and not a permission. **This is the only control that has ever caught a defect in a cut on this estate**, and the
  cut's author is structurally unable to be that control: an issuer checking its own criteria is reading them to agree with them.
  MEASURED 2026-09-10, one night, four seats, every instance surfaced by the assignee and none by the author: `2.0.0_SA_COO`
  three ticks running (W2-S2; W1-S30/S31; W5-S1/S3), each an expectation named without reading the code path that would have to
  produce it; `2.0.0_SA_COO~A` four (a validator path and a card-schema version that do not exist, a premise labelled MEASURED
  that came from a contract document rather than a run, a count carried from an earlier vintage, a comparator force-fitted into
  a population it sits outside); a worker that REFUSED TO FIRE rather than spend its order's one permitted run, whose two
  measurements showed the run could not have recorded its own forcing and WOULD have published served keys and mailed a
  recipient a standing Andrew-direct protects; and a worker that held its own face in its grant and refused to add the criterion
  tags that would have let it close. COST: none -- the clause is text on a face. NON-APPLICATION: none at L6.
  ⛔ **AND THE GAP THIS CLAUSE DOES NOT CLOSE, named because it is where the same defects keep landing unseen: AN ACCEPTANCE
  CRITERION HAS NO ASSIGNEE.** An `ACCEPT` at L4 and a `DONE WHEN` at L2 are read next by the GRADER, who reads them to apply
  them rather than to refuse them, so the refusal path that catches a task order's defects does not exist for the artifact that
  decides whether the task order's work COUNTS. `1.0.0_SA_CTO` committed three instances of the same hand-scoped-domain family
  in one night and TWO WERE IN ACCEPTS -- one would have graded an outcome REALIZED on a live violation, and one scoped an
  estate-wide gate's acceptance to a single project. Until a mechanism exists, the L10 reads every ACCEPT it grades against
  ONCE MORE UNSCOPED before the grade, and prints the denominator it used.

### L7 — Execution

- **Owner:** the worker named in `<issued_to>`, a subagent of the COO that issued the task order. **Not engaged:** every
  seat; a worker is not a seat and no seat is a worker.
- **The worker.** It starts with fresh context: the worker face of its task order, the standing law, and nothing else.
  It runs as the worker agent type, whose tools are the shell, the file tools and the search tools and nothing else:
  no broker tool, so it cannot register, send or receive; no subagent tool, so it cannot nest; no skill, gateway or
  browser tool. Its model and effort are declared by its agent type's own definition (`.claude/agents/worker.md`, or
  `.claude/agents/worker-light.md` when the face's `<worker_class>` names it), never chosen per task order and never
  passed as a per-spawn override. It exports its serial in every shell call and commits under it through `safe-commit.sh`
  with that serial as author; the serial reads as Tier-2 to every guard and is registered nowhere. Its write surface
  is its task order: no lane enumerates a worker, and the lane resolver admits it to exactly the paths its order
  names in `<paths>` while that order is non-terminal at HEAD, to `deliverables/<serial>/` by convention, and to
  nothing else; a path it needs that the order does not name is a `BLOCKING` row, never an override. It runs in its
  own worktree on its own branch, so a crashed worker leaves nothing in the shared tree; its first act is to read
  that the worktree carries the tree the order names, and one that does not is a `BLOCKING` row and a stop, never a
  reconstruction. Every invocation it runs is bounded, and a timeout is the recorded output. A capability it lacks
  that a task order needs is a surprise row, never a tool request.
- **A worker can die at ANY instruction boundary, so the ONLY residue it cannot take with it is what is COMMITTED or what
  is TRUE IN THE WORLD.** Two consequences, both procedure and neither judgement. (1) **ORDERING on any act that changes the
  world** (a deploy, an image act, a served write): open the change-management entry, ACT, then CLOSE THE ENTRY AND COMMIT IT
  BEFORE taking the reads that grade the act -- a death after the act and before the commit leaves the world changed and the
  record silent, which is the expensive shape. (2) **THE ISSUER'S OBLIGATION on a mid-act death:** one sweep of the ARTIFACT
  PLANE with a DIFFERENT instrument than the dead seat's, taken BEFORE any decision to finish or roll back -- an entry a dead
  worker left CLOSED is a self-report exactly as an entry a dead device left OPEN is (CLAUDE.md NEVER-2, read in both
  directions). The reads that remain after such a death are MEASUREMENT on a plane that already exists: the issuer takes them
  at its own seat under the dead-seat residue rule and the CVO validates whoever took them; the order does not wait for the
  slot to come back. Measured instance: NFRA_CLDGRPH round 6, row W2-S67/S95 -- a worker died on an API rate limit seconds
  after a seven-family digest re-pin; the issuer read all seven families live with `describe-task-definition` (7 of 7 on the
  new digest, 0 of 7 on any tag) and no rollback was owed.
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
  `INVESTIGATION_v<N>.Z.md`) with the id `<CODE>-W<n>-S<k>`, `n` the worker's slot and `k` the next unused number
  within that coordinate, so two worktrees never allocate one sequence; carrying `spec_asserts`, `world_is`,
  `class` (`OBSERVATION` or `BLOCKING`),
  `hazard_standing` (`ARMED` or `INERT`, with `disarm_owner` when armed), and keeps working on the next criterion or
  the next task order in its queue. The row is the carrier; a message is never the carrier. The worker judges the
  form of a surprise, never its significance: a premise that does not hold, a path that is not where the task order
  says, a result the invocation does not produce, each is one row. An `OBSERVATION` never interrupts; a `BLOCKING`
  row is read by the COO in the worker's final report of that task order; an `ARMED` row is disarmed in the same turn
  by its named owner, and disarmed is not remediated.
- **The drain.** When a task order is terminal the COO reads the worker's final report and the proof-of-spec instance,
  merges the worker's branch into the working branch when the instance is valid, pull-merge never rebase, through
  `.tools/safe-merge.sh`, which grades the merged index with the row gate and censuses every id the branch mints
  before the merge lands and aborts the merge on a refusal, removes the worktree and its branch explicitly, and hands the worker its next task order by continuing the same subagent with
  its context intact; no respawn, no cold start. At each merge the COO reads every row the branch carries: an `ARMED`
  row whose `disarm_owner` is dark is the COO's to re-seat, since the COO is the seat that spawns, and one it cannot
  seat rides the COO's drain-end read to the CTO. A worker with an empty queue ends. A worker that dies mid-task-order
  leaves a branch; the COO merges it if its instance is valid and otherwise discards it and re-dispatches the task
  order to a fresh slot. The COO merges per chain end, carrying the orders' status closes in the same merge, and adds
  every shared-file hookup the round's reports name in one commit before the one real run. A
  checker the round needs is merge tooling or rides the one repair cell, never a wave the product waits on.
- **The one real run at close.** At the round's last merge the COO runs each outcome the round served once, for real:
  the running page with real or served data, looked at, or the real entry point for a backend or pipeline outcome.
  The artifact is committed under the COO's deliverables folder. It is the close record of every `LOCAL` cell and
  the artifact the CVO grades `SERVED` judgment criteria on. It replaces every seat-to-seat re-read of the same
  check: the checker's match is the verdict on a mechanical criterion, and nobody re-runs it.
- **Gate:** `.tools/surprise-row-gate.py` at commit refuses a new investigation row without both halves, off its
  enums, off its project, whose id is off the grammar or already carried by another document of the plane, or off
  its coordinate: a worker's row carries its own slot's `W<n>` and a seat's row carries none.
  `.tools/proof-of-spec-check.py` at completion refuses an instance that fails its schema, whose cells and criteria
  do not align in both directions, whose artifact rows do not resolve at their pins, whose `surprises` entries do
  not each open with a row id present in the project's investigation file, whose recorded output does not match
  the criterion's expectation, or which carries a verdict on a judgment criterion; the L6 gate refuses a terminal
  `<status>` flip without a valid instance. The lane resolver admits the worker to its order's `<paths>` and to
  `deliverables/<serial>/`; `task-orders/` admits every seat for the status flip; the override-audit log is one
  file at the main worktree root, written from every worktree. The worker's toolkit is the worker agent type's
  frontmatter. A worker writes no telemetry: the compiled step log reads L7 from its commits under its serial, its
  proof-of-spec instance and its final report.
- **Handoff:** the investigation rows, to L8; the merged branch, to HEAD.

### L8 — Compilation

- **Owner:** `3.0.0_SA_CVO`, whose engagement with the project begins here, in a round carrying a `SERVED` or `WORLD`
  cell. In a round of `LOCAL` cells only, the CVO is not engaged. The COO's drain-end message then carries the
  real-run record and the round's `BLOCKING` and `ARMED` rows to the CTO, and stands in for the slug. **Not engaged:**
  the owners of L1 to L7 as reviewers of this limb; every worker, which has no inbox. The CVO sends nothing to anyone during a round; its
  findings travel up in the slug at L10, to the CTO and to no one else, and reach the COO through the CTO's round-N
  analysis. The one exception is the law's own carrier: an Andrew-direct spoken at the CVO's terminal is recorded
  verbatim and broadcast the same turn, as every seat's law requires, and that broadcast is a relay of his word, not
  an engagement with a limb. A worker never hears from the CVO. A row's `disarm_owner` names who disarms, never whom the CVO may
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
- **Gate:** `org/mcp/cvo_send_guard.py`, on the broker's send path, refuses a message from the CVO to any recipient
  but the CTO, at every stage; the whole send is refused and nothing is written. It admits one other class by its
  shape: a send whose subject opens with the Andrew-direct marker and whose body names the record's path under the
  CVO's own deliverables home -- the marker alone or the path alone still refuses. The watcher notifies and never
  blocks.
- **Handoff:** every row to L9.

### L9 — Adjudication

- **Owner:** `3.0.0_SA_CVO`. **Not engaged:** every other seat.
- **Input:** the investigation rows and every proof-of-spec instance under the project. **Output:** in the CVO's own
  document, `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/adjudications/ADJUDICATION_v<N>.md`, a `disposition` on
  every `BLOCKING` or `ARMED` investigation row (`UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON`,
  `DECOMP_INVALIDATING`), each a new row naming the item it adjudicates, together with the CVO's corrections and its
  own observations, so that the investigation document carries worker rows only. An `OBSERVATION` row that is not
  armed is NOTED at the round's close and needs no disposition; the CVO may still graduate one. The output also
  carries the grade of every judgment criterion of a `SERVED` or `WORLD` cell, graded on the COO's real-run artifact
  and read against the specification that issued it; the worker records without a verdict. The CVO does not re-read
  a mechanical criterion: the checker's match is its verdict. For graduated rows, the output adds remediation rows at
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
  or a graduated row without grounded evidence, and a new row in the adjudication document off the CVO's coordinate
  `<CODE>-C-S<k>`. Lane `TREE_CVO` admits only the CVO to `remediations/` and to `adjudications/`. The census counts
  the investigation document's rows as the items and reads the adjudication document for their dispositions; an
  adjudication that names an id two investigation documents carry lands on no item and is refused.
- **Handoff:** the remediation rows, to L10.

### L10 — The slug, the CTO's read, the recut, the close

- **Owner:** `3.0.0_SA_CVO` issues the slug; `1.0.0_SA_CTO` routes, always; `2.0.0_SA_COO` recuts. **Not engaged:**
  every worker; `3.0.0_SA_CVO` after the slug; `2.0.0_SA_COO` until the round-N analysis reaches it.
- **Precondition:** every task order of the round is terminal, each finished with a valid proof-of-spec instance
  whose `surprises` entries resolve to rows, and every `BLOCKING` or `ARMED` investigation row is dispositioned. An
  `OBSERVATION` row that is not armed counts against nothing. An order of a later round never holds an earlier
  round's slug.
- **The slug.** The CVO writes the round's remediation document, the one artifact of the round, and sends its only
  message of the round: the slug's path and vintage, to `1.0.0_SA_CTO`. There is no route token and no route owner;
  the CTO is the single router of every round.
- **The CTO's read.** First coverage: for each outcome in the PRD header, do the proof-of-spec instances at HEAD,
  taken together, reach its `DONE WHEN`. This is the same read as the close's grades, one verdict per outcome. For a
  `LOCAL` or `SERVED` outcome it reads the COO's real-run record; for a `WORLD` outcome it reads the exercised
  artifact itself; it never reads a report. Then one of two answers. An outcome no cell ever served takes a PRD
  addendum: the CTO bumps `prd_version`, the L4 notifier delivers the header to the two reviewers and, once both re-sign (L4-R), to the COO, and the loop runs forward from
  L4; this is rare by design, because an uncovered outcome means L5 missed it and the decomposition is over the thread
  and the manifest the CTO wrote. Otherwise the CTO writes `ledger/ROUND_ANALYSIS.round<N>.md`: per outcome, the expectation against
  what was delivered, what the remediations file says about it, what the adjudications say of each judgment criterion,
  and what the next drain should carry; and hands it to the COO with the remediations file, one message, two artifacts.
  The analysis ends in an **ENRICHMENT LIST for round N+1**: the capabilities that round adds, taken from the PRD's
  enrichment backlog (the next firm, the next window, the second screen, export), one item per cell, ordered by what a
  user gains, each keeping the thread working. Remediations ride in the same issuance under two rules: a remediation
  that breaks the thread goes first, and every remediation that concerns only a verification instrument, a record or a
  style residual is batched into ONE cell for the round, never a round of its own. Andrew may re-order or replace the
  list at any time by his word; no limb waits on him. A round whose every outcome grades `REALIZED` is closed, not
  enriched.
- **The recut.** The COO reads both, decomposes the enrichment list as the round's rectangle, and adds or recuts task
  orders as its own judgment dictates, a re-decomposed cell, a re-issued task order, new cells for an addendum, and issues them as one issuance again under L6, covering every
  affected cell; the choice between a re-decomposition and a re-issue is the COO's and is recorded in the issuance
  commit, never routed. The round runs again from the three tracks. A finding whose remedy lies outside this project's
  chain is not recut and no analysis targets another project: the row's `disarm_owner` fixes it in place when the fix
  lies inside that owner's lane, or the row is `DISMISSED_WITH_REASON` naming the brief or record that opens the owning
  surface's own project at L1; one project's loop never writes into another's.
- **The close:** two reads on two axes. `2.0.0_SA_COO`, the only seat that can say the decomposition is spent (every
  cell holds a terminal task order with a valid proof-of-spec), writes `ledger/COMPLETION_REPORT.round<N>.json`: one
  row per outcome in the PRD header, the cells that served it, each cell's proof-of-spec, and the claim `COVERED` or
  `UNCOVERED`, both denominators printed, so an outcome no cell ever served shows in the COO's own report; it is the
  final drain record. `1.0.0_SA_CTO` writes the grades from the COO's real-run record for a `LOCAL` or `SERVED`
  outcome, and from its own read of the exercised artifact each `WORLD` outcome's `DONE WHEN` names, never from the
  report, in `ledger/COMPLETION_GRADES.round<N>.json`: one verdict per outcome, `REALIZED`, `NOT_REALIZED` or
  `NOT_EVALUATED`, the artifact and its vintage cited, the observed state matching the card's state, and the artifacts
  covering every limb of the card's acceptance clause; a control window that makes a limb true by construction is not
  evidence for it, and a limb no artifact covers grades `NOT_EVALUATED`; it is the last round-N analysis. `CLOSED`
  follows mechanically when every grade reads `REALIZED` and no grade cites a state below its card. A `NOT_REALIZED`
  is the CTO's own round-N analysis for the next drain, or a PRD addendum where the outcome itself is wrong; a grade
  in question on receipt is adjudicated by the CTO as at L2. An outcome whose `DONE WHEN` is an act after the work is
  met by a closing-pass task order whose specification is that act. Then the registry bookkeeping: terminal status,
  completion date, registry row. Contract: `org/standards/COMPLETION_REPORT.schema.json`.
- **Tool:** the remediation document; `.tools/prd-header-notify.py` delivers an addendum's bumped header to the reviewers and, once both re-sign (L4-R), to the COO, and
  re-offers until READ; the round-N analysis travels by one message from the CTO to the COO.
- **Gate:** `.tools/surprise-row-gate.py` refuses a remediation row while any task order of the slug's round is not
  terminal, or any `BLOCKING` or `ARMED` investigation item is not dispositioned. The items are the investigation
  document's rows; the CVO's own rows and unarmed `OBSERVATION` rows never count against the slug. It counts the
  round's orders, never the project's, so a round N+1 issuance cut before round N's slug does not hold round N. An existing item is dispositioned by a new
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

### Closer — a product in flight, on Andrew's word

- **When:** a product whose components exist but on which no journey works end to end. A read-only trace needs no
  word from Andrew and any Tier-1 seat may run one; the CTO may propose a closer when a project shows two or more
  rounds and no live journey; Andrew's word gates only the build: the contract, the mandates and the implementing and
  reviewing seats. A closer is scheduled in sequence like any project, and its Codex COO seats count toward the
  laptop's three-COO limit. It runs in place of L5 to L9 for the named journeys; L1 to L4 are not re-run, and the
  project's PRD and channel stay where they are. NON-APPLICATION: greenfield work, where round 1 already builds the
  thread; a single-surface fix; and a pure governance project.
- **State of the project while it runs:** the CTO records the contract's path on each affected project row as
  `closer_contract`, in the contract's commit, and `/canonical-drive` skips a project whose row carries it; rounds
  already cut are not re-opened. The field is removed at hand-back.
- **Four artifacts, one owner each.** (1) A **trace brief** per product surface, by `4.0.0_SA_CRO` or any Tier-1 seat:
  the current state read from the DEPLOYED bytes, an adapter map, and a numbered hop walk, each hop graded `WORKS`,
  `INCOMPLETE`, `MISSING` or `MISMATCHED` and ending in the change that closes it; any new address or name in it is
  the naming builder's output. (2) A **contract** of at most two pages, by `1.0.0_SA_CTO`: the outcome journeys; the
  operating mode, implement directly with no task orders and no recut for an in-scope fix; the table of one writer
  per shared surface, which is also the path grant and lands in the same commit; the shared semantic contracts, which
  double as acceptance ids; a breaking change settled by one exchange between peers and then the CTO's ruling. (3) A
  one-page **mandate** per implementing seat, by the CTO: its first act, its acceptance ids, its write surface. (4)
  **Execution and review**: each implementing seat, a `2.0.0_SA_COO` instance, implements directly and publishes
  pinned candidates; a `3.0.0_SA_CVO` instance per implementing seat grades each pinned candidate `PASS`, `FAIL` or
  `NOT_EVALUATED`, and offline success is never called a deployed end-to-end pass; a Codex CVO grades on a live trace,
  the deployed bytes or a test run and never on a comp-tool read; the CTO integrates and rules. The
  COO implementing directly, rather than through workers, is the one departure from L7, and Andrew's word naming the
  product is its authority.
- **Three rules.** **LIVE FIRST:** the first milestone is the live thread through the shared first hop (the
  authentication, scope and bootstrap every screen crosses), owned by one seat and proven live before any offline
  closure counts toward an acceptance id; offline closures are allowed and grade nothing until then. **FILES OVER
  MAIL:** each seat keeps one fixed-shape STATUS file overwritten in place (pins, write claims, next proof,
  dependencies with owner, limits) and an INTERFACES file holding only the current schema and example, superseded text
  moved to a history file; a message between peers carries an interface published, a blocker or a review handoff and
  nothing else, never an acknowledgement, though an acknowledgement Andrew or `0.0.0_AB_MSTR` asks for is sent; the
  CTO's rulings append to one rulings file and go out as one message per batch. **NO
  SIDE-QUESTS:** a naming, registry or storage-policy question that is not on the thread is parked with an owner and
  the condition that un-parks it, never run as a review chain inside the sprint.
- **Hand-back:** once the thread and the named journeys pass live, the product becomes one project, its thread the
  first outcome and its other journeys the enrichment backlog; any frontend and backend projects it was split into
  close as superseded; and the remaining work returns to canonical enrichment rounds under L10, or to the close.
- **Tool:** `/closer`, in both runtimes; its templates are the four artifacts.
- **FAST MODE -- one seat, one project, Andrew present.** Two settings on every project decide how its work runs,
  independently of each other:
  - **presence**, the mode lease, decides pace and reviewer;
  - **risk and size**, `<risk>` plus the direct-act floor (L6), decide how much checking the work gets.

  The mode lease:
  - It is FAST while Andrew is at the computer and FULL, the default, otherwise.
  - It is a device-local marker armed by `/drive-mode` (`.tools/drive-mode.py`): two hours by default, extended while
    his presence stamp is under thirty minutes old.
  - It fails closed to FULL: absent, expired or unreadable reads FULL, so a forgotten FAST never runs overnight.
  - Every arm, end and lapse is one line of the committed drive-mode log.
  - It names one seat and one surface. The only refusal the lease adds is at arm: a surface another live lease or
    another project's open order already drives. Andrew resolves it with a hold on the other, or a narrower surface.
  - The project's seat runs ONE loop, and each tick reads the lease: FULL runs `/canonical-drive`, FAST runs
    `/closer-drive`.

  While FAST:
  - The seat builds each item itself: no task orders, no decomposition, no subagents, no surprise rows for in-scope
    work. STATUS.md, overwritten in place, is the record.
  - Per item: its own test, typecheck and lint on the touched package, and one real run looked at.
  - The seat lands on portal DEV itself, with CI running and no CTO go-ahead or integrator push; the push gate admits
    the lease's seat to DEV only, and PROD stays gated.
  - The CVO grades each landed pin after the fact. A FAIL becomes the next item, and nothing waits on it.
  - The seat raises no CTO ruling inside the lease's surface.
  - The comp-tool search rail stands down for the seat for the lease's life.
  - Messages are an interface published, a blocker or a review handoff, and nothing else.

  Never relaxed: the commit gate, the seat's own worktree, no rebase on a shared branch, the never-widen sign-off, the
  deploy ledger, `safe-apply`, vendor egress on Andrew's per-use word, PROD promotion, destructive-act confirmation,
  the cross-firm guard, the naming builder for any new address or name, and secrets. **A FAST lease never lowers a
  `<risk>` class:** a deploy inside it is still `WORLD`.

  Boundaries:
  - **FULL -> FAST:** the COO cuts nothing new, lets each worker finish the order in hand or flips it superseded
    with its cell moved to the next-list, and writes STATUS.md from the open cells and the enrichment backlog.
  - **FAST -> FULL:** the seat commits what builds and pins any unfinished edit on its branch. The next round is then
    cut straight from STATUS.md's next-list with no CTO round-N analysis for that one cut. The analysis resumes at
    that round's L10, and the CVO's next slug carries one section on the FAST interval.
  - `closer_contract` stays the multi-seat rescue on Andrew's word. Both it and a FAST lease make `/canonical-drive`
    stand aside.

### Cross-cutting — the integrator

`0.0.0_AB_MSTR` retains write access to the directive register WITHOUT holding a gate over it, opens and closes the push windows on the shared branch, and seats
classes on request. It works no limb, holds no task order and spawns no worker. Whether a commit is on origin is a
measured property of every done test, read by `ls-remote`, never a cell of a decomposition.

---

## 2. Role exclusivity — the guard on each half

| limb | owner only | writes refused by | engagement by message |
|---|---|---|---|
| L1 | `4.0.0_SA_CRO` | none (the brief's shape is refused at L6) | binds by reading |
| L2–L4 | `1.0.0_SA_CTO` | lane `ANY_CTO` on `prd/`; lane `TREE_PROJECT_ROW` on the row | binds by reading |
| L5–L6, the drain | `2.0.0_SA_COO` | lane `TREE_COO` on `decompositions/`, and on `task-orders/` for issuance | binds by reading; the COO's one message of a round is the drain-end read to the CTO |
| L7 | worker subagents of the COO | the L6 gate refuses a Tier-0 or Tier-1 `<issued_to>` and a worker order without `<paths>`; the lane resolver admits a worker to its order's `<paths>` only; the worker agent type has no send tool | not applicable: a worker cannot be messaged and cannot message |
| L8–L9, the slug | `3.0.0_SA_CVO` | lane `TREE_CVO` on `remediations/` and `adjudications/`; `investigations/` and `cards/` admit every seat | the CVO's one message of a round is the slug to the CTO; the same-turn broadcast of an Andrew-direct at its terminal is the law's carrier, not a message of the round |
| L10 read, close | `1.0.0_SA_CTO` | lane `TREE_LEDGER` on `ledger/`; lane `ANY_CTO` on `prd/` | the CTO's one message of a round is the round-N analysis to the COO |
| integrator | `0.0.0_AB_MSTR` | the pre-push deploy gate on deploy scope | binds by reading |
| closer (on Andrew's word) | trace brief `4.0.0_SA_CRO` or a Tier-1 seat; contract, mandates and rulings `1.0.0_SA_CTO`; implementation `2.0.0_SA_COO` instances; review `3.0.0_SA_CVO` instances | the path grant the contract's writer table lands in its own commit | binds by reading; messages carry an interface published, a blocker or a review handoff, never an acknowledgement |

Three simultaneous projects are one CTO, one COO per project (the base and its lanes), and one CVO across them until a
measured channel backlog says otherwise.

---

## 3. Limb, owner, `dep_stage`, refuser

| limb | owner | `dep_stage` after the limb | refuses at commit | refuses at completion | notifies |
|---|---|---|---|---|---|
| L1 brief | `4.0.0_SA_CRO` | none | — | — | — |
| L2 endpoint | `1.0.0_SA_CTO` | none | — | — | — |
| L3 register | `1.0.0_SA_CTO` | `REGISTERED` | `missions-tree-check.sh` | — | — |
| L4 PRD | `1.0.0_SA_CTO` | `PRD` | lane `ANY_CTO` | — | `prd-header-notify.py` to the routed reviewer of each half still owed, on every bump |
| L4-R sign-off | `3.0.0_SA_CVO` (ratified-text half, always); `4.0.0_SA_CRO` (brief half) or a live `2.0.0_SA_COO` not holding the round in its stead | `PRD` | lane `TREE_PRD_SIGNOFF` (the CTO and the round-holding COO lane are REFUSED); the stamp is `prd-signoff.py` | `to-pipeline-gate.py` LIMB 6 refuses a TO against a PRD with a half not SIGNED at its current bytes | `prd-header-notify.py` withholds the COO delivery until both halves SIGNED, nudges an overdue half (CTO copied), re-routes an overdue brief half, releases on the sign-off commit |
| L5 decomposition | `2.0.0_SA_COO` | `DECOMP` | lane `TREE_COO` | — | — |
| L6 issuance | `2.0.0_SA_COO` | `EXECUTING` | `to-proof-of-spec-check.sh`, `to-pipeline-gate.py` (coverage, criterion grammar, the worker's `<paths>`, `<risk>` and its floor), lane `TREE_COO` | — | — |
| L7 execution | a worker subagent | `EXECUTING` | `surprise-row-gate.py` (rows: halves, uniqueness, coordinate); `owned-paths-validate.py` (the order's `<paths>`); at the drain, `safe-merge.sh` (the row gate on the merged index) | `proof-of-spec-check.py` (the expectation match); the terminal-flip limb of `to-pipeline-gate.py` | — |
| L8 compilation | `3.0.0_SA_CVO` | `EXECUTING` | at send: `org/mcp/cvo_send_guard.py` (the CVO to the CTO only) | — | `surprise-watch.sh` to the CVO |
| L9 adjudication | `3.0.0_SA_CVO` | `EXECUTING` | `surprise-row-gate.py` (rows; the `C-` coordinate), lane `TREE_CVO` | — | — |
| L10 slug, read, recut, close | `3.0.0_SA_CVO` issues the slug; `1.0.0_SA_CTO` reads and routes; `2.0.0_SA_COO` recuts; at the close `2.0.0_SA_COO` reports, `1.0.0_SA_CTO` grades | `ROUND_CLOSE`, `CLOSED` | `surprise-row-gate.py` (the precondition over the round's orders and its `BLOCKING` or `ARMED` worker rows); `missions-tree-index.py check` (the `CLOSED` flip) | — | `prd-header-notify.py` (an addendum's header) to the COO |
| FAST mode (on the lease) | the lease's seat builds; Andrew reviews live; `3.0.0_SA_CVO` grades pins after the fact | unchanged | `drive-mode.py arm` (a surface another driver holds); `never-rules-gate.sh` (portal DEV push admitted to the lease's seat only) | — | — |

Every notification and every acknowledgement is read on the broker's delivery ledger: sent, emitted and read are
three states, and only an agent's own acknowledgement is read. A worker is on no ledger and in no telemetry stream;
its completion is its proof-of-spec instance at HEAD and its acts are its commits.

---

## 4. What binds by reading

The citable brief and the qualitative outcomes at L1 and L2; the arc and defined outcome of the PRD; the choice to
use the decomposition method's validator at L5; the worker's significance judgment at L7, which is deliberately not
the worker's; the CVO's engagement beginning at L8; the grounding bar at L9; the dispositioned half of the L10
precondition; role exclusivity against engagement by message at every limb; the integrator-only push. Everything
else in section 3 refuses.

The eight carriers the third version named are built, checked out and refuse, and so is the drain's refuser on the
merged index; section 3 names each. One clause still names a carrier that does not exist, and binds by reading
until it does; where a live gate contradicts this text the gate's own audited override is the only lawful way
through, written into the commit that uses it.

- **The step log reads L7 from git.** A worker's acts leave no telemetry row; the compiled step log that grades an
  amendment (section 5) reads a worker's limb from its commits under its serial, its proof-of-spec instance and its
  final report. Until the compiler reads git, a worker's share of acts outside the limbs binds by reading.

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
| 3.2 | 2026-09-04 | Andrew's word at the CRO terminal on the eight carriers (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/` @9f60e36398, message 93970) and their builds: the L6 coverage limb, criterion grammar, the checker's expectation match and judgment refusal, the row gate's route retirement and adjudication census @b4299fa5aa; the send guard @85bb815ad0; the sentinels @01b41e4f0b; the row lane and the `adjudications/` lane @7668568ed6 (LD-0534); the worker agent type @4df363de8f, @324fa75544, @d57b4c2523; the rollup @747da480bc; the adjudication document exercised @b50a124783; v3's first drain and its five gaps (`3.0.0_SA_CVO` 94007, 94010; `4.0.0_SA_CRO` 94014): the uniqueness limb and the item census @72d05b2642, the drain's union gate as procedure @e6351512fe; Andrew's word at the CTO terminal, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260904_0458Z_RECS_APPROVED_WORKER_LANE_IS_THE_TASK_ORDER_AND_ROW_ID_ALLOCATOR_COORDINATE.md` @9ef9a40aae (the same word at the CVO's @92af61a111 and the COO's @febe803b27): the task order as the worker's grant (`worker_grant` stanza @e08447ff7d, LD-0534 Amendment 1; the resolver's fifth clause and the L6 `<paths>` refusal @6efb43b9d0; `/dispatch` @788e3a7888, @febe803b27) and the allocator coordinate (annex v3.2/v3.3 and the schema half @4d65d9b496, @e3e999c139; the gate half @6efb43b9d0); the one audit log @6bfaa233ed; `4.0.0_SA_CRO`'s check-outs of all eight (94025, 94074) | every carrier of section 4 at v3.0 is built and refuses, and section 3 names each; a worker's write surface is exactly its order's `<paths>` while the order is non-terminal at HEAD, no lane enumerates a worker, and an order issued to a worker without `<paths>` is refused at the cut; a worker's first act is the worktree premise and every invocation is bounded; the row id carries an allocator coordinate, `W<n>` for a worker's slot and `C-` for the CVO's adjudication rows, uniqueness by full id across the plane's documents, and an adjudication that lands on no single item refused; the census counts worker rows as the items and never the CVO's; the CVO's send guard admits the CTO alone at every stage; the override-audit log is one file at the main worktree root; a worker writes no telemetry and the step log reads L7 from git; section 4 now holds two clauses, the drain's gate on the merged index and the step log's L7 read |
| 3.3 | 2026-09-04 | `2.0.0_SA_COO`'s surface (message 94085) that `.tools/safe-merge.sh` @2187fac0f9 and the drain step re-pointed at it @f414b18822 are ancestors of the 3.2 commit @743d282408, which called the refuser unbuilt; the refuser's own report of its unexercised collision arm (94078) | section 4's drain clause names the refuser that exists and the arm it still owes: a real collision at a merged index aborting the merge; the L7 refuser cell of section 3 names `safe-merge.sh` at the drain |
| 3.4 | 2026-09-04 | `4.0.0_SA_CRO`'s check-out of the drain refuser's deciding arm (message 94094): a real cross-document collision at the merged index did not land, rc 1, but by the pre-commit hook and not by the script -- `safe-merge.sh` calls the row gate with no paths, grades nothing, and exits with the merge open; the green arm merges correctly | section 4's drain clause states the exercised state: the script's own abort has not passed, the hook is what refuses today, the merge is left open, and the clause leaves this section when the script grades the merged index's changed paths and the arm passes at check-out |
| 3.5 | 2026-09-04 | `2.0.0_SA_COO`'s fix of the drain refuser @747a0b23c3 (the gate fed the merged index's staged paths; an empty set refused; the merge aborted on refusal; two regression arms) and `4.0.0_SA_CRO`'s check-out of its deciding arm on its own instrument (message 94105): the collision refused by the script's own grade and aborted with no merge left open, the non-colliding branch merged | the drain clause leaves section 4: the L7 drain merges through `safe-merge.sh`, which grades the merged index and aborts on a refusal; section 4 holds one clause, the step log's L7 read from git |
| 3.6 | 2026-09-04 | `3.0.0_SA_CVO`'s constitutional review of v3.2-v3.5 (message 94134, record `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_CONSTITUTIONAL_REVIEW_SPINE_v3.2-v3.5_20260904T0740Z.md` @5c965cfcdb; ACCEPT all four; finding F1: the narrowed L8 guard and the same-turn broadcast law contradicted at the CVO's terminal); the gate's owner's ruling and build, `org/mcp/cvo_send_guard.py` with both callers @8623a92a70 | L8's silence and its guard take one exception, the law's own carrier: the CVO's same-turn broadcast of an Andrew-direct record, admitted by its marker and the record's path under the CVO's own home, either alone still refused; section 2 says the broadcast is not a message of the round |
| 3.7 | 2026-09-09 | Andrew-direct ~21:5xZ at the `2.0.0_SA_COO~A` terminal (workers on Opus at high effort; "I'm ok with enumerating opus for worker agents"), the agent definition edit `.claude/agents/worker.md` @65d7815288 and its broadcast (message 94731); `1.0.0_SA_CTO` moves the two spine clauses the edit contradicted | L7: the worker's model is Opus at high effort by the agent type's definition, never per task order and never a per-spawn override (was "the cheaper one unless the preflight marks the cell hard"); L6 tool clause: the spawn uses a hand-cut worktree off CLOUD with its path in the prompt, never the harness's isolation option (which bases on origin/main with no `org/` or `.tools/` -- the trap the first exercised spawn hit for 51 minutes). No step, owner or gate changes. |
| 3.8 | 2026-09-10 | `1.0.0_SA_CTO`'s NFRA_COMPEFFICACY round-7 L10 ruling R-8 (slug `3.0.0_SA_CVO` 94834, row S40), with its two siblings of the same night (`NFRA_OUTSET`-S29, `ETFS_GUARDRAIL` W2-S7) | L6 cut discipline gains one clause: **an accept that names an INSTRUMENT names its COVERAGE fact, an accept that names a HARNESS names its GRAIN flag (which vintage it scores), and an accept that compares a STORED BASELINE names the ENVIRONMENT the baseline was captured in** (the tree, the ranker mode, the rendering of every hashed asset). Measured cause: three criteria in one night could neither pass nor fail, and a fourth read a FALSE RED because its baseline was captured in a linked worktree whose CRLF-rendered model asset silently put the ranker in lexical fallback. No step, owner or gate changes. |
| 3.9 | 2026-09-10 | `2.0.0_SA_COO~A`'s row NFRA_CLDGRPH-S95 (message 94841), taken by `1.0.0_SA_CTO` at 94844 | L7 gains the worker-death clause: a worker can die at any instruction boundary, so a world-changing act ORDERS itself open-entry / act / close-and-COMMIT-the-entry / then read, and the ISSUER's obligation on a mid-act death is one artifact-plane sweep with a DIFFERENT instrument than the dead seat's BEFORE deciding to finish or roll back (an entry a dead worker left CLOSED is a self-report, the mirror of NEVER-2's open-entry clause); the remaining reads are measurement the issuer may take at its own seat with the CVO validating. No step, owner or gate changes. |
| 3.10 | 2026-09-10 | Andrew-direct ~03:0xZ at the `1.0.0_SA_CTO` terminal (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_030xZ_NO_FWD_IS_A_WAIT.md`) | L2 gains **NO FWD IS A WAIT**: every outcome provable by an act a seat can take on demand; one whose only proof is an event nobody controls is re-cut so its mechanism is driven deliberately, the organic case kept as the negative arm; an essential wait is expressly qualified with its reason and his word; an outcome already written as a wait is SUPERSEDED at the next unused id with its text kept. The L2 half of the ~21:4xZ manual-trigger rule that binds accepts at L4/L6. No step, owner or gate changes. |
| 3.11 | 2026-09-10 | four seats converging in one night, none of it previously written: `2.0.0_SA_COO` 94998 and 95007, `2.0.0_SA_COO~A` 95015, and two worker refusals (EG-s-21 not fired; EG-s-22's assignee refusing to tag its own face). Recorded by `1.0.0_SA_CTO` at `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_20260910T054xZ_THE_REFUSAL_CLAUSE.md` | L6 gains **THE REFUSAL CLAUSE**: a criterion is shaped so refusing it is cheaper than rescuing it and the face says so; the assignee refuses and reports with its measurement, never repairs, widens or re-routes; a worker editing the issuance half so its own proof validates certifies an alignment the cut never declared. It is the only control that has caught a defect in a cut on this estate, and the cut's author cannot be that control. The clause also NAMES ITS OWN GAP -- an acceptance criterion has no assignee, so the refusal path does not protect the artifact that decides whether work counts -- and binds the L10 to re-read every ACCEPT once more UNSCOPED, with the denominator printed, until a mechanism exists. No step, owner or gate changes. |
| 3.12 | 2026-09-10 | `0.9.0_WK_ETFS_GUARDRAIL~4`'s third refusal to fire and `2.0.0_SA_COO`'s 95058, ruled by `1.0.0_SA_CTO` at R-EG-6 | L6 gains **A SEAM PROVED TO DELIVER ITS INPUT IS NOT A SEAM PROVED TO HAVE AN EFFECT**: a criterion names the OUTCOME, never only the mechanism, and proves what must DIFFER when the control is engaged against the same run with it disengaged. Found when a forcing spec proved to reach the classifier was then discarded by a re-classification, publishing where a refusal was required. No step, owner or gate changes. |
| 3.13 | 2026-09-10 | `2.0.0_SA_COO~A`'s audit of its OWN just-drained round against v3.12 (95066), an hour after the clause landed and the round closed | v3.12 gains three qualifiers, all from that audit: a POSITIVE control is not a DIFFERENCE control and does not discharge the clause (measured 2 of 16 mechanical criteria carry the real shape, not the 6 of 20 a loose count gives, so the adoption cost is real); a CENSUS is a NON-APPLICATION because its outcome IS its count; and the clause DOES NOT BIND RETROACTIVELY -- a round is graded against the law in force at its cut, the L9 and L10 grade with any audit in hand and RECORD THE BOUNDARY IN THE GRADE, and no drained round is re-cut for a later law. No step, owner or gate changes. |
| 3.14 | 2026-09-10 | Andrew-direct ~21:2xZ at the `1.0.0_SA_CTO` terminal, VERBATIM *"I dont want to ask shit this should be entirely automatic and gated, CRO and CVO should have to sign off on PRD before COO gets it"* (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_212xZ_PRD_SIGNOFF_IS_A_GATE_CRO_AND_CVO_BEFORE_COO.md`); measured cause: `3.0.0_SA_CVO` d0e72ccd56 and `4.0.0_SA_CRO` e975e96fc0 / 637b2f8178 on the two IRPT PRDs, thirteen corrections in three unrequested passes | L4 gains **THE PRD SIGN-OFF GATE (L4-R)**: the brief's author signs the coverage map for CONTENT carriage, the verifier signs the ENDPOINT section against the ratified pins and the CONTRACTS section against the counterpart; both sign-offs are files in the reviewers' own lane `TREE_PRD_SIGNOFF`, version-bound to the PRD; `prd-header-notify.py` withholds the COO delivery until both exist and `to-pipeline-gate.py` LIMB 6 refuses a task order from an unsigned PRD. The CTO cannot sign its own document. Two mechanical carriers, one new lane, no new owner; non-retroactive for rounds already cut. |
| 3.15 | 2026-09-11 | Andrew-direct ~05:2xZ-05:3xZ at the `1.0.0_SA_CTO` terminal: "look critically at the sign-off process ... it is very loose right now and unclear. I want to tighten it up. How do we move the gating process along naturally so i dont have to be buzzing around asking agents what theyre doing?"; "CVO should always be included. If CRO is not online, can do COO in their stead"; "make sure the spine operation works properly, that the scripts work properly and the agents know how to use them to do their stamp. make sure there are clear expectations here". Measured: thirteen PRD versions in one night, the brief half re-signed three times unchanged; the notifier never triggered on a sign-off commit (fixed 973ad3770f); the reviewers were nudged by Andrew by hand | L4-R tightened: TWO HALVES bound to their bytes (`half_hash`), not to `prd_version`; ONE rule in `.tools/prd_signoff_lib.py` called by the gate, the notifier and the new stamp `.tools/prd-signoff.py` (`sign` / `refuse` / `status`); reviewers ROUTED per half (CVO always; CRO or a live COO not holding the round in its stead); a 60-minute window with automatic OVERDUE nudges (CTO copied) and re-routing; the addendum path re-opens only the half it changed; the vintage boundary (`f8337502a9`) in code; reviewer expectations stated. No new owner. |
| 3.16 | 2026-09-23 | Andrew-direct at the `1.0.0_SA_CTO~C` terminal (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260923_CANONICAL_FLOW_OPS_AND_CLOSER_FLOW.md` @c564b6262a): *"we need to focus on one round bringing a product or pipeline to MVP status ... subsequent rounds are all about enrichment"* and the closer flow formalised lightly; the brief he commissioned, `org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF_CANONICAL_FLOW_SPEED_CLOSER_FLOW_SKILLS_PARITY_20260923.md` @ea031c3987 (R1-R4). Measured cause: IRPT_FNTEND 15 rounds and IRPT_BCKEND 18 rounds with zero journeys end to end and zero outcomes REALIZED, both PRDs leaving the frontend/backend seam jointly unowned; the frontend BUILD share of criteria falling from 68% in round 1 to 0% by round 15; the closer run reaching code in under an hour and then both live contacts failing on the shared first hop after about 8.5 hours offline | **THE THREAD FIRST**: a product's `FWD-1` is one live journey end to end on the deployed stack; the PRD gains THREAD and ENRICHMENT BACKLOG sections (brief half); a new product is one journey in one project; round 1's rectangle is over the thread's hops, with the battery defaulting to not-applicable except `comp-iam`. **ENRICHMENT ROUNDS**: the round-N analysis ends in an enrichment list for round N+1; remediations ride along, thread-breaking first and instrument/record/style repairs batched into one cell; the L6 sentence that made every later round a repair loop is replaced by one that covers THIS round's decomposition. **THE VERIFICATION DIET**: at most three mechanical criteria per build task order; repo-wide hygiene and the thread trace run at the drain; judgment only where needed; by prompting, no gate. **CLOSER**: a subsection beside Midstream for a product in flight on Andrew's word, its four artifacts, LIVE FIRST, FILES OVER MAIL and NO SIDE-QUESTS, and its hand-back to enrichment rounds; `/closer` is its instrument. Non-retroactive: a round already cut finishes under its cut task orders. No new gate or owner. |
| 3.17 | 2026-09-23 | Andrew-direct ~16:3xZ at the `4.0.0_SA_CRO` terminal answering seven open calls on the v3.16 brief and text, VERBATIM *"1.) Hold is off. 2.) Yes. 3.) Yes. 4.) Rec approved. 5.) That does apply for projects that have a frontend but needs to be considered in the event it's purely a backend/infrastructure product (e.g. NFRA_GLOBGRPH, NFRA_COMPEFFICACY, LGIC_NAMING, LGIC_LGCTFM, etc.). 6.) Yes. 7.) Yes."* (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_163xZ_HOLD_OFF_AND_CLOSER_OPEN_CALLS_RULINGS.md` @7303be1bbb), relayed to `1.0.0_SA_CTO~C` as message 99672 with the six non-sovereign fixes of the same `/open-calls` output | **LIVE** defined for a product with a frontend: the real backend, real data and real login, the frontend local or on DEV, a PROD release an enrichment item; for a purely backend or infrastructure product it is OPEN, and such a product stays outside the thread clause until defined. **L4** reworded: one product is one project, its first outcome one journey, never a frontend/backend split. **CLOSER**: a read-only trace needs no word from Andrew; the CTO may propose a closer at two or more rounds with no live journey; Andrew's word gates only the build; a closer is sequenced like any project and its Codex COO seats count toward the three-COO limit; the row carries `closer_contract` while it runs and `/canonical-drive` skips it; a Codex CVO grades on a live trace, deployed bytes or a test run, never a comp-tool read; the no-acknowledgement rule covers peer traffic only; at hand-back the product becomes one project and its split projects close as superseded. **DIET**: a difference-control arm is part of its criterion, not a fourth check. **PIPELINE THREAD**: its person is the consumer of the served output. No new gate or owner. |
| 3.18 | 2026-09-23 | Andrew-direct ~17:0xZ at the `4.0.0_SA_CRO` terminal, VERBATIM *"Your rec is approved on call 5b. I will handle MSTR"* (addendum to `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_163xZ_HOLD_OFF_AND_CLOSER_OPEN_CALLS_RULINGS.md` @c4ec953322), approving `org/tier1_exec/4.0.0_SA_CRO/deliverables/PROPOSAL_THREAD_FOR_BACKEND_AND_INFRASTRUCTURE_PRODUCTS_20260923.md` @2dd215da34, relayed to `1.0.0_SA_CTO~C` as message 99684 | **THE BACKEND/INFRASTRUCTURE THREAD** (call 5's open half): one named consumer's one real use of the mechanism -- the real tool at HEAD from an ordinary seat shell or the deployed component, over real inputs, through the consumer's real entry -- ending in the consumer's observed result as one trace; the result may land on one machine's working branch or in a QA location, and shared-branch availability and production scheduling are enrichment items. L2's non-application narrows to a pure governance project, and so does the Closer's. Transition: `LGIC_NAMING` is `CLOSED` and not reopened; `NFRA_COMPEFFICACY` and `LGIC_LGCTFM` apply it from their next issuance. Served-output writes still carry the never-widen sign-off; no gate is lifted. No new gate or owner. |
| 3.19 | 2026-09-24 | Andrew-direct ~15:3xZ at the `4.0.0_SA_CRO~A` terminal approving report 2's seven recs and C1-C9 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_153xZ_REPORT2_ALL_SEVEN_RECS_APPROVED.md`, report `org/tier1_exec/4.0.0_SA_CRO/deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`); Andrew-direct ~15:4xZ there approving the joint model and sending reports 2 and 3 to the CTO for immediate implementation (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_154xZ_REPORT3_REFINEMENTS_APPROVED_BOTH_REPORTS_TO_CTO.md`, report 3 `docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md` Waves 1-3) | **FAST MODE AND THE RISK CLASS, ONE RULE:** presence (the mode lease) decides pace and reviewer, `<risk>` plus the direct-act floor decide checking; the Closer subsection carries FAST mode (the lease, the one refusal at arm, `/closer-drive`, the DEV landing, after-the-fact CVO grading, the rail stood down, the never-relaxed list, both boundaries); L6 gains `<risk>` (`LOCAL` / `SERVED` / `WORLD`, a floor inferred from paths and invocations), the direct-act path, issuer rulings inside its own decomposition, checks as files dry-run at the base, and `<worker_class>`; L7 names no model and adds the per-chain merge and the COO's one real run of each outcome at close, which replaces every seat-to-seat re-read; L8-L9 engage the CVO on `SERVED` / `WORLD` rounds only and disposition `BLOCKING` / `ARMED` rows only; L10's precondition and refuser count the slug's round, never the project, and the CTO's exercised read is kept for `WORLD` outcomes; L4-R binds both halves to the ENDPOINT hash alone and admits the brief half when the CRO wrote the brief. Law-locked edits (CLAUDE.md, org/XXX.md), the memory cap and the byte budgets are not in this version. |
| 3.20 | 2026-09-24 | Andrew-direct ~17:0xZ at the `4.0.0_SA_CRO~A` terminal, VERBATIM "Yes, i like that item 1, send it" (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_170xZ_C10_CUT_TASK_ORDERS_BY_WRITE_SET.md`; report 2 section 13, C10) | **CELLS ARE CUT BY WRITE SET:** L5 -- each cell owns files no other cell of the round writes, a one-line hookup in a shared file belongs to no cell, an edge is a real data dependency and never file contention, a batch cell touching many cells' files runs last or folds into the merge; L6 -- a cell's written `<paths>` are disjoint from every other cell's of the round; L7 -- the COO adds every hookup the round's reports name in one commit at the merge, before the one real run. The `fanout:` line and the cap of eight are unchanged. |
