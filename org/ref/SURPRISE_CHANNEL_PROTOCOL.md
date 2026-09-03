# SURPRISE CHANNEL PROTOCOL -- the L7 to L10 annex of the canonical fabric workflow

**Status:** constitutional annex. This document is the one specification of the surprise channel: how a surprise leaves
the seat that met it at L7, how it is compiled at L8, adjudicated at L9 and routed at L10. It is scoped to those four
limbs of `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` (the spine), is cited from the spine's L8, and adds nothing to
the other six. Where this annex and the spine differ, the spine governs and this annex is amended. Amendment is by
whole-file version under section 9; the authorizing records are named only in the changelog (section 10).

**Owner:** `3.0.0_SA_CVO` authors this annex and the two row schemas at `org/surprise_channel/schemas/`; the lanes
that admit writes to the channel files are the registry grantor's.

**Vocabulary.** A **row** is one item in a channel file's fenced `json` block. A **surprise** is a spec-versus-world
mismatch met during on-spec execution: the worker had to do something the task order did not say, or could not do
something it said. **Surfacing** is appending the row. **Compiling**, **adjudicating** and **routing** are the CVO's
three limbs over the rows. An **open** item is a row whose newest citing row is not terminal.

---

## 0. Document form -- one home per document, the machine half inside it

Each channel document is one `.md` file carrying a narrative and exactly one fenced `json` block. The block is an
array of rows validating against the schema for its kind. There is no sidecar `.json`; a second block in one file is a
second home and is refused. Validation extracts the block from the document, so what is checked is what is read.

**Append-only as a control.** During a round a channel file only grows. A row that exists at HEAD is byte-equivalent
as data in every later commit; a correction, a closure or a change of disposition is a NEW row citing the old id. A
reader resolves a row's state from the newest row that cites it. The row gate refuses an in-place edit; the one escape
is the gate's audited override written into the commit message body.

---

## 1. What the channel is

Execution at L7 is on spec, frozen for the round. Anything the spec did not anticipate is surfaced to this channel as
one row, in the same turn, with no action taken beyond the row, and the seat keeps working fail-closed on its task. The
row is the carrier. A broker message is never the carrier: a notifier that watches files cannot see an inbox, and a
surprise that exists only as a message is invisible to L8 and uncounted at L10.

Every surprise of every class reaches the channel. A `BLOCKING` row also goes to the issuer in the same turn; an
`ARMED` row names its disarm owner in the row. The channel runs in one direction: rows travel UP from the seat that
met the surprise, and the CVO's findings travel UP to `2.0.0_SA_COO` (or to `1.0.0_SA_CTO` for a scope change), never
DOWN to a worker. A worker hears from the CVO only through a task order or an operating note issued by the COO; a
row's `disarm_owner` names who disarms, never whom the CVO may message; a disarm request travels through the COO.
The channel then:

1. **compiles** the rows into the round's investigation document (section 4), at L8;
2. **adjudicates** each row measurement-first, mechanism attributed at source, denominators printed, at L9;
3. **graduates** valid grounded rows into the round's remediation document (section 5), at L9;
4. **routes** each graduated row to the limb that owns its remedy, at L10, once the round's task orders are terminal
   with valid proof-of-spec instances -- the remediations of a round are issued as ONE slug at L10, one artifact at
   one moment to the route owner, never as a stream of messages during L7 to L9.

A project closes only on a zero-graduation round.

---

## 2. The graduation bar is a grounding bar

A row graduates to remediation only when its mechanism is grounded: a source or live-primitive citation, with the
controls the claim class needs. An ungrounded row stays in the investigation document marked `INFERRED` and cannot seed
a remediation row. Severity decides where a valid row lands; grounding decides whether it graduates at all. A
remediation row without its mechanism is an inference wearing a row's clothing.

---

## 3. The two orthogonal axes -- `class` and `hazard_standing`

**`class` -- the interruption right.** `BLOCKING` stops live in-scope work now and goes to the issuer; `OBSERVATION`
does not interrupt. One intent (what the row does to the current turn), one grain (one row at surfacing), exhaustive by
negation, disjoint by construction, no precedence rule. Two members, two remedies: unblock now, or record and route.

**`hazard_standing` -- whether the row, left alone, harms through the process's future normal operation.** `ARMED`: a
future ordinary act encounters it and is harmed. `INERT`: nothing does. One intent, one grain, exhaustive by negation,
no precedence. `ARMED` obliges a named `disarm_owner` and an off-cadence disarm; `INERT` obliges nothing. Any class may
be `ARMED`; "latent hazard" is the prose name for `(any class, ARMED)` and is never an enum value.

**Not on either axis.** `DECOMP_INVALIDATING` is a disposition (section 4): it describes a row's scope effect on L5, a
third intent.

**Standing constraint on any axis touching this channel.** The channel is a process concurrent with execution, never a
position in it. The register's `dep_stage` enum has no channel value, because surfacing happens during `EXECUTING`; the
three axes here classify rows (handling path, disposition, disarm and remediation state), and none classifies the
channel.

---

## 4. The investigation document -- one per project per fabric per round

**Homes.** `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v<N>.md` for a project with
a tree home; `org/surprise_channel/<CODE>/INVESTIGATION_v<N>.md` for a project without one. Site Z writes
`INVESTIGATION_v<N>.Z.md` beside the laptop file. The lane on both roots admits every seat; the row gate is the control.

**Who writes.** The seat that meets the surprise appends its own row. The CVO appends its own rows for what it observes
at L8 and L9, and appends the closure and correction rows of section 0.

**Row fields** (`org/surprise_channel/schemas/investigation_item.schema.json` is normative):

| field | content |
|---|---|
| `id` | `<CODE>-S<n>` on the laptop fabric; `<CODE>-Z-S<n>` on site Z. Stable; cited by later rows and by remediation rows. |
| `project`, `fabric` | the project code and fabric, each equal to what the id and the path declare; the gate compares them. |
| `surfaced_by`, `surfaced_at` | seat serial; UTC. |
| `one_line` | the surprise as surfaced. |
| `spec_asserts`, `world_is` | the two halves of the trigger: what the task order said, and what the world was. A row that cannot state both is an opinion, not a surprise. |
| `class`, `hazard_standing`, `disarm_owner` | section 3; `disarm_owner` is required whenever `hazard_standing` is `ARMED`. |
| `grounding` | `{status: INFERRED or GROUNDED, evidence: [citations]}`; `GROUNDED` requires source or live-primitive evidence, never self-report. |
| `disposition` | `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON`, `DECOMP_INVALIDATING`; `dismissal_reason` is required with a dismissal. |
| `notes` | free text; the closing condition of an open row belongs here. |

**Disposition axis.** One intent: where the row goes next. `UNDER_INVESTIGATION` is the only active state; the three
terminals partition every row's end at this limb: valid and grounded graduates and seeds a remediation row; not valid
or not worth carrying is dismissed with its reason; valid and revealing an unenumerated operative surface is
`DECOMP_INVALIDATING`, which routes backward to L5 first, reopens the current round's scope, and never also takes a
forward route. The three terminals take three different remedies: build, record, reopen.

**Setting a disposition.** A row is appended with `UNDER_INVESTIGATION`. The CVO's adjudication is a new row citing the
old id and carrying the terminal disposition and its reason or evidence; the original row is unchanged.

---

## 5. The remediation document -- graduated rows only

**Homes.** `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/remediations/REMEDIATION_v<N>.md`, or
`org/surprise_channel/<CODE>/REMEDIATION_v<N>.md` for a project without a tree home; `.Z.md` on site Z. The lane admits
the CVO only.

**When.** Cut at round close and handed to the issuer at completion of the round's task orders. Its rows re-enter at
L5 as the next round's decomposition inputs; they are not task orders.

**Row fields** (`org/surprise_channel/schemas/remediation_row.schema.json` is normative): `id` equal to the graduated
investigation row's id; `project`, `fabric`; `class`, `hazard_standing`; `mechanism` (the grounded attribution, carried
verbatim); `evidence`; `remedy`; `owner` (the lane that builds); `round`; `remediation` `{state: OPEN or REMEDIATED,
owner, round}`; for `ARMED` rows also `disarm` `{state: ARMED or DISARMED, owner, at}`; `closed`; and the routing
fields of section 8.

**Disarmed is not remediated.** Two states, two owners, two clocks. Disarm is urgent and off-cadence; remediation
rides the round. An `ARMED` row is `closed` only when both states have landed; an `INERT` row when `REMEDIATED`. A
single terminal state would convert dangerous-and-visible into safe-and-invisible.

---

## 6. The escape valve -- an `ARMED` row rides outside round cadence

An `ARMED` row is surfaced in the same turn like any other, and its disarm does not wait for the round. The surfacing
row names the disarm owner: whoever can act on the armed artifact now. If that seat is dark, the row escalates in the
same turn to the integrator, `0.0.0_AB_MSTR`, which seats a class on request. A disarm is reported as a new row citing
the armed row. A valve whose actuator has no owner reads open and is shut.

---

## 7. L8 compilation -- the CVO's intake

The CVO's engagement with a project begins at L8; its correspondents are the COO and, for a scope change, the CTO,
and no worker. Its intake is `org/surprise_channel/surprise-watch.sh <serial> stream`,
a read-only watermark over both roots that prints one line per new, mutated or vanished row and never writes what it
watches; `comp-surprise` is the rollup over both roots. The watcher notifies and never blocks; its state records what it
emitted, never that a seat read anything. A row the CVO reads is acknowledged by its L9 act, never by a message.

---

## 8. L9 adjudication and L10 routing

**L9.** Every row receives its disposition per section 4. Graduated rows receive a remediation row per section 5. A
`DECOMP_INVALIDATING` row reopens L5 for the current round at once.

**L10 precondition.** Every task order under the project is terminal (`complete`, `superseded`, `cancelled`,
`withdrawn`), each finished with a valid proof-of-spec instance whose `surprises` entries resolve to rows, and every
investigation row is dispositioned. An open item is not a zero: a round with an `UNDER_INVESTIGATION` row does not
route and does not close. The row gate enforces the task-order half and the proof-of-spec checker its surprises
clause; the dispositioned half binds by reading.

**The loop.** The round's findings re-enter at the limb the route names and run forward again through L10. A
remediation pass is an L5 re-decomposition or an L6 re-dispatch by the COO, cut as fresh task orders and remediated
runs in the order their dependencies dictate, to the relevant workers or to newly seated ones. Looping in order is
the point; the CVO never shortens it by writing to a worker.

**Routing fields on a remediation row.** `route` is the decision: what does the remedy need that does not exist yet?
`SPEC_ERROR`, a cell the decomposition already contains; `DECOMP_INVALIDATING`, a cell it does not; `SCOPE_CHANGE`, an
outcome the PRD does not name. `loop_target` is derived from `route` and stored so a reader of one row can act:
`SPEC_ERROR` to 6, `DECOMP_INVALIDATING` to 5, `SCOPE_CHANGE` to 2; the gate refuses any pair off that map. A
`SCOPE_CHANGE` row carries `scope_change_kind` (`CONTRADICTS_NAMED_OUTCOME` with a real `outcome_ref`, or
`REQUIRES_UNNAMED_OUTCOME` with `outcome_ref` null and a `proposed_outcome`); the filer never allocates an outcome id.

**Who acts.** The CVO stamps the route; the route owner acts: `2.0.0_SA_COO` for 6 and 5, `1.0.0_SA_CTO` for 2. The
stamped rows go to the route owner and to no one else. The
notifier `.tools/prd-header-notify.py kind:route` delivers a new route row to its owner and re-offers until read. A
round whose remediation document graduates zero rows proceeds to the next L6 dispatches; a project closes on a
zero-graduation round.

---

## 9. Homes, validation, and the two fabrics

**Gates.** `.tools/surprise-row-gate.py` at commit, reading staged bytes against HEAD, refuses on either root: a new
investigation row without `spec_asserts` and `world_is`, without `project` and `fabric` agreeing with its id and its
path, or off its schema; any pre-existing row changed in place; a new remediation row without its required fields, a
graduated row without grounded evidence, a `route` and `loop_target` off the locked map, a `SCOPE_CHANGE` without its
kind and outcome reference, or a route row while any task order under the project is not terminal. It fails closed on
an unreadable blob or an unparseable block. `.tools/proof-of-spec-check.py` refuses a worker's proof-of-spec instance
whose `surprises` entries do not each open with a row id present in the project's investigation file, so a task order
cannot complete on a surprise that has no row.

**Validation of a document** extracts the single fenced block and validates each row against its schema, printing the
row count as its denominator.

**One investigation file per fabric per round, with a fabric-distinct filename.** The laptop fabric writes
`INVESTIGATION_v<N>.md`; site Z writes `INVESTIGATION_v<N>.Z.md`; the same for remediation files unless the two
certifiers agree at handover on one merged remediation authored by one of them. The two files are never merged; a
same-path add on both branches resolves by rename, keeping each file's content. Ids carry the fabric coordinate
(`<CODE>-S<n>` and `<CODE>-Z-S<n>`) so that two certifiers on two machines never allocate one sequence; bridged messages
cite the namespaced id.

**Mirror versus collision.** This rule applies where both fabrics independently author a channel for one project, not
where a file merely exists at the same path on both branches. A file one fabric authored and the other pulled is a
mirror: byte-identical whole file, leave it alone. Divergent content under shared ids is a collision: rename. The
discriminator is one byte comparison of the whole file.

---

## 10. Amendment protocol

This annex is amended as a whole by `3.0.0_SA_CVO`, on Andrew's word or on a routed L10 finding, as a new version with
one changelog line naming the record that authorized it. No in-place markers, no partial-clause patches, no quotations,
no dates or hashes in the body. An amendment of the spine that touches L7 to L10 amends this annex in the same
window. A document that describes the channel in a second shape is retired to a redirect the day it is found.

---

## 11. Changelog

| version | date | authorizing record | summary |
|---|---|---|---|
| 1.0 | 2026-08-21 | Andrew's ratification of the channel framework at the CTO terminal; the CTO's assignment of the channel to the CVO | one home per document; the two axes; the grounding bar; investigation and remediation documents; the escape valve; round mechanics |
| 1.1 | 2026-08-21 | the CTO's cross-fabric ruling on colliding ids | one file per fabric per round; ids carry the fabric coordinate; mirror versus collision |
| 1.2 | 2026-09-02 | `org/tier0/ledger/` entries for the row gate and the project tree; Andrew's word at the CTO terminal on lane `ANY` for investigations | `.tools/surprise-row-gate.py`; `project`, `fabric`, `spec_asserts`, `world_is` gate-required on new rows; the tree root; the `SCOPE_CHANGE` payload; the remediation schema's fabric coordinate |
| 2.1 | 2026-09-03 | spine v2.1 `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` @aaa5a2b085; Andrew's two words at the COO terminal, recorded at `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_L7_L10_LOOP_CVO_RELAYS_TO_COO_NEVER_CONVERSES_WITH_WORKERS.md` @10a4beaffb and `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_ALL_TOS_PROOF_OF_SPEC_BEFORE_LOOPBACK_CVO_REMEDIATION_SLUG_AT_L10.md` @de2d6d643c | the channel runs in one direction: findings up to the COO or the CTO, never down to a worker; the round's remediations issued as one slug at L10 to the route owner only; the L10 precondition carries the valid proof-of-spec instance with resolving surprises; the loop stated |
| 2.0 | 2026-09-03 | state of record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_024xZ_CANONICAL_WORKFLOW_L1_L10_STATE_OF_RECORD.md` @716a9bc7ce (LD-0521); brief `org/tier0_exec/0.0.0_AB_MSTR/deliverables/BRIEF_20260903_CANONICAL_FABRIC_WORKFLOW_SPEC_TEN_LIMBS_ONE_PROCESS.md` @ba9add4200; Andrew's word at the CVO terminal, recorded at `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260903_031xZ_SURPRISE_ROW_NOT_MCP_GATE_ON_PROOF_OF_SPEC_SURPRISES.md` @007481053a | re-keyed from a five-stage document to the L7 to L10 annex of the spine, in constitutional form; the row is the only carrier and the surfacing seat appends its own row on either root; append-only as a control with corrections as new rows; the proof-of-spec surprises limb; the L10 precondition and its gate; the CVO's intake named |
