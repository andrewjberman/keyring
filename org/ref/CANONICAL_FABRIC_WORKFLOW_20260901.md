# THE CANONICAL FABRIC WORKFLOW

**Status:** constitutional. This document is the one specification of how the Opal fabric takes a topic from a brief
to a closed project. There is one process, the ten limbs L1 to L10, and every document, gate, skill and record that
touches the process resolves to this file. Amendment is by whole-file version under the protocol in section 5; the
authorizing records are named only in the changelog (section 6).

**Vocabulary.** A **limb** is one of the ten numbered hops; "step" is an accepted synonym. A **seat** is an agent
serial. **Owner** means the only seat that performs the limb; **not engaged** means no other seat reviews, grades,
certifies, or acts on that limb's artifact while the limb is open. A **gate** refuses at commit or at completion; a
**notifier** delivers and never blocks; **binds by reading** means the sentence has no mechanical carrier. The
register's `dep_stage` enum (`REGISTERED`, `PRD`, `DECOMP`, `EXECUTING`, `ROUND_CLOSE`, `CLOSED`) is data; its limb
mapping is in section 3. Route tokens are `SPEC_ERROR`, `DECOMP_INVALIDATING`, `SCOPE_CHANGE`.

**Project tree.** Every project lives at `org/missions/D<n>/<MACRO>/<CODE>/` with the subfolders `brief/`, `prd/`,
`decompositions/`, `task-orders/`, `deliverables/<serial>/`, `surprise-channel/investigations/`,
`surprise-channel/remediations/`, `ledger/`, `cards/`. The row is `project.json`; the flat index entry
`org/projects/<CODE>.json` is generated from it and carries `home`. The grammar is `org/standards/PROJECT_TREE.contract.json`.

---

## 1. The ten limbs

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
- **Tool:** `/endpoint --forward <brief>`. The same skill re-enters here from an L10 `SCOPE_CHANGE`.
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
  decide-first question into L5. Any substantive edit bumps `prd_version`.
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
  catalog. No cell is owned by a Tier-0 or Tier-1 seat.
- **Tool:** `/atom-decomp` (`projects/ATOM_DECOMP`), the lenses.
- **Gate:** lane `TREE_COO` refuses any other author's write to `decompositions/`. The decomposition is consumed at L6
  through `<decomp_ref>`; a defective decomposition surfaces at L7 as a `DECOMP_INVALIDATING` row and routes back here.
- **Handoff:** `dep_stage: DECOMP`.

### L6 — Task orders

- **Owner:** `2.0.0_SA_COO`. **Not engaged:** `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`.
- **Input:** the decomposition. **Output:** `org/missions/D<n>/<MACRO>/<CODE>/task-orders/<CODE>.TO-<id>.<slug>.md`,
  each carrying `<decomp_ref>` with a delimited `<owned_cells>` list, `<preflight>` with the three mandatory
  dispositions, `<proof_of_spec>` with the criterion ids the assignee will prove, `<issued_to>` naming one Tier-2
  seat, and a GO message to that exact serial in the same window. A task order is one project for one seat instance;
  parallelism is more instances, never more projects on one instance. A dark seat class is seated by a spawn, which is
  the COO's act. Task orders are small circles that close.
- **Tool:** the task-order protocol, `send_message` to the exact serial.
- **Gate:** at commit, `.tools/git-hooks/to-proof-of-spec-check.sh` refuses a new task order without `<proof_of_spec>`
  or without `<decomp_ref>`; `.tools/to-pipeline-gate.py` refuses a new task order whose project row is absent, whose
  `dep_stage` or `fabric` is off its enum, whose preflight is incomplete, whose PRD fails L2 or L4's conditions above,
  whose row and folder disagree, or whose `<issued_to>` names a Tier-0 or Tier-1 seat; an override is written to
  `org/to-pipeline-override-audit.log`. Lane `TREE_COO` refuses any other author's issuance.
- **Handoff:** `dep_stage: EXECUTING`, flipped by the row owner on the first task order.

### L7 — Execution

- **Owner:** the Tier-2 worker named in `<issued_to>`. **Not engaged:** every Tier-0 and Tier-1 seat as a worker.
- **Input:** the task order and its cited decomposition cells. **Output:** the deliverables and the proof-of-spec
  instance at `org/missions/D<n>/<MACRO>/<CODE>/deliverables/<serial>/<TO>.proof_of_spec.json`, one acceptance row per
  criterion with its invocation and output evidence, and the task order's own `<status>` flip, committed by the
  worker. The specification is frozen for the round; the worker's first act is to re-ground the task order's premises
  against live state; status moves with the act, by the actor, in the same commit; a precondition that becomes
  unreachable is declared so on the record.
- **Surprise:** when the worker had to do something the task order did not say, or could not do something it said,
  the worker appends one row to `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v<N>.md`
  (`org/surprise_channel/<CODE>/INVESTIGATION_v<N>.md` on a project without a tree home; site Z writes
  `INVESTIGATION_v<N>.Z.md`) carrying `spec_asserts`, `world_is`, `class` (`OBSERVATION` or `BLOCKING`),
  `hazard_standing` (`ARMED` or `INERT`, with `disarm_owner` when armed), and keeps working. The row is the carrier; a
  message is never the carrier. The worker judges the form of a surprise, never its significance. An `OBSERVATION`
  never interrupts; a `BLOCKING` row also goes to the issuer in the same turn; an `ARMED` row is disarmed in the same
  turn by its named owner, and disarmed is not remediated.
- **Gate:** `.tools/surprise-row-gate.py` at commit refuses a new investigation row without both halves, off its
  enums, or off its project. `.tools/proof-of-spec-check.py` at completion refuses an instance that fails its schema,
  whose cells and criteria do not align in both directions, whose artifact rows do not resolve at their pins, or whose
  `surprises` entries do not each open with a row id present in the project's investigation file; the L6 gate refuses
  a terminal `<status>` flip without a valid instance. Lanes admit the worker on `deliverables/<serial>/`,
  `task-orders/` for its own status flip, `surprise-channel/investigations/`, and `cards/`.
- **Handoff:** the investigation rows, to L8.

### L8 — Compilation

- **Owner:** `3.0.0_SA_CVO`, whose engagement with the project begins here. **Not engaged:** the owners of L1 to L7
  as reviewers of this limb.
- **Input:** new investigation rows on either channel root. **Output:** the compiled channel, append-only during the round.
- **Tool:** `org/surprise_channel/surprise-watch.sh <serial> stream` (a read-only watermark on both roots, one line
  per new row, at-least-once) is the CVO's intake; `comp-surprise` is the rollup over both roots.
- **Gate:** none; the watcher notifies and never blocks.
- **Handoff:** every row to L9.

### L9 — Adjudication

- **Owner:** `3.0.0_SA_CVO`. **Not engaged:** every other seat.
- **Input:** the investigation rows. **Output:** a `disposition` on every row (`UNDER_INVESTIGATION`, `GRADUATED`,
  `DISMISSED_WITH_REASON`, `DECOMP_INVALIDATING`) and, for graduated rows, a remediation row at
  `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/remediations/REMEDIATION_v<N>.md`. Graduation is a grounding bar:
  a row graduates when its mechanism is attributed, its denominators carried and its remedy holder named; severity
  decides where it lands, grounding decides whether it graduates. A `DECOMP_INVALIDATING` row reopens L5 for the
  current round at once; it never also takes a forward route.
- **Tool:** the surprise-channel protocol and its row schemas at `org/surprise_channel/schemas/`.
- **Gate:** `.tools/surprise-row-gate.py` refuses a new remediation row without its required fields, off its enums,
  or a graduated row without grounded evidence. Lane `TREE_CVO` admits only the CVO to `remediations/`.
- **Handoff:** the remediation rows, to L10.

### L10 — Routing

- **Owner:** `3.0.0_SA_CVO` stamps the route; the route owner acts. **Not engaged:** every worker.
- **Precondition:** every task order under the project is terminal and every investigation row is dispositioned.
- **Input:** the remediation rows. **Output:** on each row a `route` and its `loop_target`, locked:
  `SPEC_ERROR` to L6 (owner `2.0.0_SA_COO`, re-cuts the task order), `DECOMP_INVALIDATING` to L5 (owner
  `2.0.0_SA_COO`, re-decomposes), `SCOPE_CHANGE` to L2 (owner `1.0.0_SA_CTO`, re-enters the endpoint; the row names
  the contradicted `FWD-<n>`, or names a proposed outcome with `outcome_ref` null). A round whose remediation doc
  graduates zero rows proceeds to the next L6 dispatches; a project closes on a zero-graduation round by the two-part
  atomic close.
- **Tool:** the remediation row; `.tools/prd-header-notify.py kind:route` delivers a new route row to its owner and
  re-offers until READ.
- **Gate:** `.tools/surprise-row-gate.py` refuses a route row while any task order under the project is not terminal,
  a route and target off the locked map, and a `SCOPE_CHANGE` without its kind and outcome reference. The dispositioned
  half of the precondition binds by reading.
- **Handoff:** `dep_stage: ROUND_CLOSE`, then `CLOSED` on the closing round, flipped by the row owner on the CVO's stamp.

### Cross-cutting — the integrator

`0.0.0_AB_MSTR` holds the directive register, opens and closes the push windows on the shared branch, and seats
classes on request. It works no limb and holds no task order. Whether a commit is on origin is a measured property
of every done test, read by `ls-remote`, never a cell of a decomposition.

---

## 2. Role exclusivity — the guard on each half

| limb | owner only | writes refused by | engagement by message |
|---|---|---|---|
| L1 | `4.0.0_SA_CRO` | none (the brief's shape is refused at L6) | binds by reading |
| L2–L4 | `1.0.0_SA_CTO` | lane `ANY_CTO` on `prd/`; lane `TREE_PROJECT_ROW` on the row | binds by reading |
| L5–L6 | `2.0.0_SA_COO` | lane `TREE_COO` on `decompositions/`, and on `task-orders/` for issuance | binds by reading |
| L7 | Tier-2 workers | the L6 gate refuses a Tier-0 or Tier-1 `<issued_to>` | not applicable |
| L8–L10 | `3.0.0_SA_CVO` | lane `TREE_CVO` on `remediations/`; `investigations/` and `cards/` admit every seat | binds by reading |
| integrator | `0.0.0_AB_MSTR` | the pre-push deploy gate on deploy scope | binds by reading |

---

## 3. Limb, owner, `dep_stage`, refuser

| limb | owner | `dep_stage` after the limb | refuses at commit | refuses at completion | notifies |
|---|---|---|---|---|---|
| L1 brief | `4.0.0_SA_CRO` | none | — | — | — |
| L2 endpoint | `1.0.0_SA_CTO` | none | — | — | — |
| L3 register | `1.0.0_SA_CTO` | `REGISTERED` | `missions-tree-check.sh` | — | — |
| L4 PRD | `1.0.0_SA_CTO` | `PRD` | lane `ANY_CTO` | — | `prd-header-notify.py` to the COO |
| L5 decomposition | `2.0.0_SA_COO` | `DECOMP` | lane `TREE_COO` | — | — |
| L6 task orders | `2.0.0_SA_COO` | `EXECUTING` | `to-proof-of-spec-check.sh`, `to-pipeline-gate.py`, lane `TREE_COO` | — | — |
| L7 execution | Tier-2 worker | `EXECUTING` | `surprise-row-gate.py` (rows) | `proof-of-spec-check.py`; the terminal-flip limb of `to-pipeline-gate.py` | — |
| L8 compilation | `3.0.0_SA_CVO` | `EXECUTING` | — | — | `surprise-watch.sh` to the CVO |
| L9 adjudication | `3.0.0_SA_CVO` | `EXECUTING` | `surprise-row-gate.py` (rows), lane `TREE_CVO` | — | — |
| L10 routing | `3.0.0_SA_CVO` stamps; owner acts | `ROUND_CLOSE`, `CLOSED` | `surprise-row-gate.py` (precondition, locked map) | — | `prd-header-notify.py kind:route` to the owner |

Every notification and every acknowledgement is read on the broker's delivery ledger: sent, emitted and read are
three states, and only an agent's own acknowledgement is read.

---

## 4. What binds by reading

The citable brief and the qualitative outcomes at L1 and L2; the arc and defined outcome of the PRD; the choice to
use the decomposition method's validator at L5; the worker's significance judgment at L7, which is deliberately not
the worker's; the CVO's engagement beginning at L8; the grounding bar at L9; the dispositioned half of the L10
precondition; role exclusivity against engagement by message at every limb; the integrator-only push. Everything
else in section 3 refuses.

---

## 5. Amendment protocol

This file is amended as a whole, by `1.0.0_SA_CTO` as the scribe of process law, on Andrew's word or on a routed
L10 finding. Each amendment is a new version with one changelog line naming the record that authorized it. No
in-place markers, no partial-clause patches, no quotations, no dates or hashes in the body. Independent review of
an amendment is the CVO's constitutional review role and is not an engagement with any limb. A document that
describes this process in a second shape is retired to a redirect the day it is found.

---

## 6. Changelog

| version | date | authorizing record | summary |
|---|---|---|---|
| 1.0 | 2026-09-01 | `org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` | first text of the ten steps and the surprise flow |
| 2.0 | 2026-09-03 | state of record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_024xZ_CANONICAL_WORKFLOW_L1_L10_STATE_OF_RECORD.md` @716a9bc7ce (LD-0521); brief `org/tier0_exec/0.0.0_AB_MSTR/deliverables/BRIEF_20260903_CANONICAL_FABRIC_WORKFLOW_SPEC_TEN_LIMBS_ONE_PROCESS.md` @ba9add4200; water test `workflows/atom_decomposition/runs/canonical-fabric-workflow-spec/20260903T0305Z/` | constitutional form; ten limbs with one owner each and the not-engaged set; the project tree homes; the surprise row as the only carrier; the L6 refusal of Tier-0/1 seating and the L10 precondition gate; the proof-of-spec surprises limb; worker commits its own status; the earlier second description of the process retired to a redirect |
