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
- **Tool:** `/endpoint --forward <brief>`. Andrew confirms the `DONE WHEN` line of every outcome here; it is his last
  touch point, and after L2 no limb waits on him. The same skill re-enters here from an L10 `SCOPE_CHANGE`, where the
  CTO adjudicates: it runs `/open-calls --adjudicate` on the subject, rules on the recommendations itself, records the
  ruling, appends the new outcomes at the next unused ids, re-issues the PRD, and the loop runs forward from L4.
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
  as reviewers of this limb; every worker as a correspondent. The CVO's findings travel UP the loop to `2.0.0_SA_COO`
  (or to `1.0.0_SA_CTO` for a scope change) and never DOWN to a worker: a worker hears from the CVO only through a
  task order or an operating note issued by the COO. A row's `disarm_owner` names who disarms, never whom the CVO
  may message; a disarm request travels through the COO.
- **Input:** new investigation rows on either channel root. **Output:** the compiled channel, append-only during the round.
- **Tool:** `org/surprise_channel/surprise-watch.sh <serial> stream` (a read-only watermark on both roots, one line
  per new row, at-least-once) is the CVO's intake; `comp-surprise` is the rollup over both roots.
- **Gate:** `org/mcp/cvo_send_guard.py`, on the broker's send path, refuses a message from the CVO to any Tier-2
  serial while a tree project reads `dep_stage: EXECUTING`; the whole send is refused and nothing is written. The
  watcher notifies and never blocks.
- **Handoff:** every row to L9.

### L9 — Adjudication

- **Owner:** `3.0.0_SA_CVO`. **Not engaged:** every other seat.
- **Input:** the investigation rows. **Output:** a `disposition` on every row (`UNDER_INVESTIGATION`, `GRADUATED`,
  `DISMISSED_WITH_REASON`, `DECOMP_INVALIDATING`) and, for graduated rows, remediation rows at
  `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/remediations/REMEDIATION_v<N>.md`, issued as ONE slug for the
  round at L10 (one artifact, one moment), never as a stream of messages during L7 to L9. Graduation is a grounding bar:
  a row graduates when its mechanism is attributed, its denominators carried and its remedy holder named; severity
  decides where it lands, grounding decides whether it graduates. A `DECOMP_INVALIDATING` row reopens L5 for the
  current round at once; it never also takes a forward route.
- **Tool:** the surprise-channel protocol and its row schemas at `org/surprise_channel/schemas/`.
- **Gate:** `.tools/surprise-row-gate.py` refuses a new remediation row without its required fields, off its enums,
  or a graduated row without grounded evidence. Lane `TREE_CVO` admits only the CVO to `remediations/`.
- **Handoff:** the remediation rows, to L10.

### L10 — Routing

- **Owner:** `3.0.0_SA_CVO` stamps the route; the route owner acts. **Not engaged:** every worker.
- **Precondition:** every task order under the project is terminal, each finished with a valid proof-of-spec instance
  whose `surprises` entries resolve to rows, and every investigation row is dispositioned.
- **The loop:** the round's findings re-enter at the limb the route names and run forward again through L10; a
  remediation pass is an L5 re-decomposition or an L6 re-dispatch by the COO, cut as fresh task orders and remediated
  runs in the order their dependencies dictate, to the relevant workers or to newly seated ones, never a conversation
  between the CVO and a worker. Looping in order is the point of the process.
- **Input:** the remediation rows. **Output:** on each row a `route` and its `loop_target`, locked:
  `SPEC_ERROR` to L6 (owner `2.0.0_SA_COO`, re-cuts the task order), `DECOMP_INVALIDATING` to L5 (owner
  `2.0.0_SA_COO`, re-decomposes), `SCOPE_CHANGE` to L2 (owner `1.0.0_SA_CTO`, re-enters the endpoint; the row names
  the contradicted `FWD-<n>`, or names a proposed outcome with `outcome_ref` null). A graduated row whose remedy was
  executed inside the round by its owner, its remediation `REMEDIATED` and, if it was armed, its hazard `DISARMED`,
  carries no route and re-enters nowhere; the gate admits that row and no other route-less one. The three routes answer
  one question about this project's own chain: what the remedy needs that does not exist yet. A finding whose remedy lies
  outside that chain is not routed and no route targets another project: the row's `disarm_owner` fixes it in place
  when the fix lies inside that owner's lane, or the row is `DISMISSED_WITH_REASON` naming the brief or record that
  opens the owning surface's own project at L1; one project's loop never writes into another's. A round whose
  remediation doc graduates zero rows proceeds to the next L6 dispatches, or, when the decomposition is spent, opens
  the close.
- **The close:** two reads on two axes. `2.0.0_SA_COO`, the only seat that can say the decomposition is spent (every
  cell holds a terminal task order with a valid proof-of-spec), writes `ledger/COMPLETION_REPORT.round<N>.json`: one
  row per outcome in the PRD header, the cells that served it, each cell's proof-of-spec, and the claim `COVERED` or
  `UNCOVERED`, both denominators printed, so an outcome no cell ever served shows in the COO's own report.
  `1.0.0_SA_CTO` reads the exercised artifact each outcome's `DONE WHEN` names, never the report, and writes
  `ledger/COMPLETION_GRADES.round<N>.json`: one verdict per outcome, `REALIZED`, `NOT_REALIZED` or `NOT_EVALUATED`,
  the artifact and its vintage cited, the observed state matching the card's state, and the artifacts covering every
  limb of the card's acceptance clause; a control window that makes a limb true by construction is not evidence for
  it, and a limb no artifact covers grades `NOT_EVALUATED`. `CLOSED` follows mechanically when every grade reads
  `REALIZED` and no grade cites a state below its card. A `NOT_REALIZED` re-enters at L5 as a decomposition gap or at L2 as a `SCOPE_CHANGE`;
  a grade in question on receipt is adjudicated by the CTO as at L2. An outcome whose `DONE WHEN` is an act after the
  work is met by a closing-pass task order whose specification is that act. Then the registry bookkeeping: terminal
  status, completion date, registry row. Contract: `org/standards/COMPLETION_REPORT.schema.json`.
- **Tool:** the remediation row; `.tools/prd-header-notify.py kind:route` delivers a new route row to its owner and
  re-offers until READ.
- **Gate:** `.tools/surprise-row-gate.py` refuses a route-carrying row (a remediation row with a `route`, or an
  investigation row whose `disposition` is `DECOMP_INVALIDATING`) while any task order under the project is not
  terminal or any investigation item under it is not dispositioned, a route and target off the locked map, and a
  `SCOPE_CHANGE` without its kind and outcome reference. An existing item is dispositioned by a new investigation row
  that names it in `adjudicates`; the channel stays append-only. `.tools/missions-tree-index.py check` refuses a
  `CLOSED` row unless the completion report and the grades exist for the same round, cover exactly the header's
  outcomes, and every grade reads `REALIZED`.
- **Handoff:** the stamped row to the route owner and to no one else; `dep_stage: ROUND_CLOSE` on the CVO's stamp,
  then `CLOSED` on the CTO's grades, both flipped by the row owner.

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
| L8–L10 | `3.0.0_SA_CVO` | lane `TREE_CVO` on `remediations/`; `investigations/` and `cards/` admit every seat | binds by reading; the CVO's messages go to the COO or the CTO, never to a worker |
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
| L8 compilation | `3.0.0_SA_CVO` | `EXECUTING` | at send: `org/mcp/cvo_send_guard.py` | — | `surprise-watch.sh` to the CVO |
| L9 adjudication | `3.0.0_SA_CVO` | `EXECUTING` | `surprise-row-gate.py` (rows), lane `TREE_CVO` | — | — |
| L10 routing | `3.0.0_SA_CVO` stamps; owner acts; at the close `2.0.0_SA_COO` reports, `1.0.0_SA_CTO` grades | `ROUND_CLOSE`, `CLOSED` | `surprise-row-gate.py` (precondition, locked map); `missions-tree-index.py check` (the `CLOSED` flip) | — | `prd-header-notify.py kind:route` to the owner |

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
| 2.1 | 2026-09-03 | `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_L7_L10_LOOP_CVO_RELAYS_TO_COO_NEVER_CONVERSES_WITH_WORKERS.md` @10a4beaffb; `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_ALL_TOS_PROOF_OF_SPEC_BEFORE_LOOPBACK_CVO_REMEDIATION_SLUG_AT_L10.md` @de2d6d643c | the L7 to L10 loop: the CVO's findings travel up to the COO (or the CTO for a scope change) and never down to a worker; remediations are one slug at L10; every task order finishes with its valid proof-of-spec before any loop-back; the pass re-enters at L5 or L6 as fresh and remediated task orders in dependency order; the L10 handoff is to the route owner only |
| 2.2 | 2026-09-03 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_045xZ_RECS_APPROVED_CVO_SEND_REFUSED_L7_L9_GATE_III_INVESTIGATIONS_LIMB.md` | two refusers for clauses that bound by reading: the L8 send guard on the broker path (CVO to a Tier-2 serial refused while a tree project is executing) and the second limb of the L10 gate (no route while an investigation item is undispositioned; both route shapes; the `adjudicates` carrier) |
| 2.3 | 2026-09-03 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md` | the close: the COO's completion report and the CTO's grades, two reads on two axes, the `CLOSED` flip mechanical on the grades (`missions-tree-index.py` R6, `COMPLETION_REPORT.schema.json`); autonomy after L2 -- Andrew confirms the `DONE WHEN` lines at L2 and no limb waits on him after; `SCOPE_CHANGE` and a questioned grade are adjudicated by the CTO (`/open-calls --adjudicate`) and the loop runs forward from L4 |
| 2.4 | 2026-09-03 | `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` @f9ca7a9309 -- the in-place disarm of NFRA_CLDGRPH round 1's first finding, whose remedy lay in another surface's document; the question relayed by the run's L2 owner to the scribe | the routes are about this project's own chain; an outside remedy is a disarm in place within the owner's lane or a `DISMISSED_WITH_REASON` naming the brief that opens the owning surface's own project at L1; no route targets another project |
| 2.5 | 2026-09-03 | `org/standards/COMPLETION_REPORT.schema.json` (the grader's bar in the contract) | the close's grading bars stated in the process rather than in messages: a `REALIZED` grade cites artifacts covering every limb of the card's acceptance clause and a vacuous control window is not evidence; the observed state never sits below the card's state (mechanical in the tree check) |
| 2.6 | 2026-09-03 | `.tools/surprise-row-gate.py` (the gate-model fork between the two fabrics' CTOs, ruled at the base) | a graduated row whose remedy was executed inside the round (`REMEDIATED`, and `DISARMED` if armed) carries no route and re-enters nowhere; every other route-less remediation row is refused |
