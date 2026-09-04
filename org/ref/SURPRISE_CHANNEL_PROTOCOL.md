# SURPRISE CHANNEL PROTOCOL -- the L7 to L10 annex of the canonical fabric workflow

**Status:** constitutional annex. This document is the one specification of the surprise channel: how a surprise leaves
the seat that met it at L7, how it is compiled at L8, adjudicated at L9 and issued as the round's one slug at L10. It is
scoped to those four limbs of `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` (the spine), is cited from the spine's
L8, and adds nothing to the other six. Where this annex and the spine differ, the spine governs and this annex is
amended. Amendment is by whole-file version under section 10; the authorizing records are named only in the changelog
(section 11).

**Owner:** `3.0.0_SA_CVO` authors this annex and the row schemas at `org/surprise_channel/schemas/`; the lanes that
admit writes to the channel files are the registry grantor's.

**Vocabulary.** A **row** is one item in a channel file's fenced `json` block. A **surprise** is a spec-versus-world
mismatch met during on-spec execution: the worker had to do something the task order did not say, or could not do
something it said. **Surfacing** is appending the row. **Compiling** and **adjudicating** are the CVO's two limbs over
the rows; the **slug** is the CVO's one artifact of a round, the remediation document, issued to the CTO. An **open**
item is a row whose newest citing row is not terminal. A **grade** is the CVO's verdict on one judgment criterion of one
proof-of-spec instance, carried in a row's `grades` field. An **allocator** is the index a row's id was minted against:
the main index, site Z's, or a worker worktree's.

---

## 0. Document form -- one home per document, the machine half inside it

Each channel document is one `.md` file carrying a narrative and exactly one fenced `json` block. The block is an
array of rows validating against the schema for its kind. There is no sidecar `.json`; a second block in one file is a
second home and is refused. Validation extracts the block from the document, so what is checked is what is read.

**Append-only as a control.** During a round a channel file only grows. A row that exists at HEAD is byte-equivalent
as data in every later commit; a correction, a closure or a change of disposition is a NEW row citing the old id. A
reader resolves a row's state from the newest row that cites it. The row gate refuses an in-place edit; the one escape
is the gate's audited override written into the commit message body.

**Three documents, three writers.** The investigation document carries the rows of the seats and workers that met a
surprise; the adjudication document carries the CVO's rows about those rows; the remediation document carries the
graduated remedies and is the slug. A writer's rows go in the writer's document, so a reader of any one document
knows without inspection whose voice it is reading, and a count over the investigation document counts surprises and
nothing else.

---

## 1. What the channel is

Execution at L7 is on spec, frozen for the round. Anything the spec did not anticipate is surfaced to this channel as
one row, in the same turn, with no action taken beyond the row, and the seat keeps working fail-closed on its task. The
row is the carrier. A broker message is never the carrier: a notifier that watches files cannot see an inbox, and a
surprise that exists only as a message is invisible to L8 and uncounted at L10. Under the spine a worker has no inbox
and no send tool, so for a worker the row is not only the carrier but the only carrier there is.

Every surprise of every class reaches the channel. A `BLOCKING` row is read by the issuer in the worker's final report
of that task order; an `ARMED` row names its disarm owner in the row. The channel runs in one direction: rows travel
UP from the seat that met the surprise, and the CVO's findings travel UP in the slug to `1.0.0_SA_CTO`, and reach
`2.0.0_SA_COO` through the CTO's round-N analysis, never DOWN to a worker and never by message during the round. A
worker hears from the CVO never; a row's `disarm_owner` names who disarms, never whom the CVO may message; a disarm the
CVO cannot make in its own lane is a row, read by its owner from the channel. The channel then:

1. **compiles** the worker rows of the round's investigation document (section 4), at L8;
2. **adjudicates** each row measurement-first, mechanism attributed at source, denominators printed, into the round's
   adjudication document (section 4a), at L9; a proof-of-spec criterion the task order flagged as judgment is graded
   here too, against the specification, never by the instance's own verdict, in the `grades` field of a row of the CVO's;
3. **graduates** valid grounded rows into the round's remediation document (section 5), at L9;
4. **issues** the remediation document as ONE slug at L10, one artifact at one moment to the CTO and to no one else,
   once the round's task orders are terminal with valid proof-of-spec instances -- never as a stream of messages
   during L7 to L9, and never routed by the CVO to any limb: the CTO is the single router of every round.

A project closes only when the CTO's grades read realized on every outcome.

---

## 2. The graduation bar is a grounding bar

A row graduates to remediation only when its mechanism is grounded: a source or live-primitive citation, with the
controls the claim class needs. An ungrounded row stays in the investigation document marked `INFERRED` and cannot seed
a remediation row. Severity decides where a valid row lands; grounding decides whether it graduates at all. A
remediation row without its mechanism is an inference wearing a row's clothing. The depth that grounding needs lives
at this limb and nowhere below it: the worker verifies no deeper than its task order's own invocations, and the CVO
reaches for the compiler tools, the graph, the adversary lens or an atomic decomposition only on a row that is
ambiguous. The CVO's most valuable act is reading a proof-of-spec instance against the specification that issued it;
the lever on that act is not more depth but less to read, which is what the worker face of a task order, one clause
per criterion, and the split of this channel into three documents each buy.

---

## 3. The two orthogonal axes -- `class` and `hazard_standing`

**`class` -- the interruption right.** `BLOCKING` stops live in-scope work now and reaches the issuer in the worker's
final report; `OBSERVATION` does not interrupt. One intent (what the row does to the current turn), one grain (one row
at surfacing), exhaustive by negation, disjoint by construction, no precedence rule. Two members, two remedies: unblock
at the drain, or record and carry.

**`hazard_standing` -- whether the row, left alone, harms through the process's future normal operation.** `ARMED`: a
future ordinary act encounters it and is harmed. `INERT`: nothing does. One intent, one grain, exhaustive by negation,
no precedence. `ARMED` obliges a named `disarm_owner` and an off-cadence disarm; `INERT` obliges nothing. Any class may
be `ARMED`; "latent hazard" is the prose name for `(any class, ARMED)` and is never an enum value.

**Not on either axis.** `DECOMP_INVALIDATING` is a disposition (section 4a): it describes what a row's remedy needs, a
cell the decomposition does not contain, a third intent.

**Standing constraint on any axis touching this channel.** The channel is a process concurrent with execution, never a
position in it. The register's `dep_stage` enum has no channel value, because surfacing happens during `EXECUTING`; the
three axes here classify rows (handling path, disposition, disarm and remediation state), and none classifies the
channel.

---

## 4. The investigation document -- one per project per fabric per round, worker rows only

**Homes.** `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v<N>.md` for a project with
a tree home; `org/surprise_channel/<CODE>/INVESTIGATION_v<N>.md` for a project without one. Site Z writes
`INVESTIGATION_v<N>.Z.md` beside the laptop file. The lane on both roots admits every seat; the row gate is the control.

**Who writes.** The seat or worker that meets the surprise appends its own row, in its own worktree when it is a
worker, merged to HEAD by the COO with the task order. The CVO writes nothing here: its dispositions, corrections and
own observations are rows of the adjudication document (section 4a), so that L8's intake and L10's precondition census
read surprises and nothing else.

**Row fields** (`org/surprise_channel/schemas/investigation_item.schema.json` is normative):

| field | content |
|---|---|
| `id` | `<CODE>-S<n>` for a seat's row on the laptop fabric; `<CODE>-Z-S<n>` on site Z; `<CODE>-W<n>-S<k>` for a row minted in worker `<n>`'s worktree (`<CODE>-Z-W<n>-S<k>` on site Z; the coordinates nest fabric-then-allocator). The coordinates name the ALLOCATOR: two certifiers on two machines and two worktrees on one machine never share a sequence. `<k>` restarts at 1 per coordinate; a seat's row carries no `W`; the gate requires `W<n>` to equal the committing worker's suffix. Stable; cited by later rows and by remediation rows. An id is minted at commit: the row gate is the allocator, and until the commit that carries it lands the id is provisional and is not cited; a citation of a row carries the row's vintage as `<id>@<commit>`, so a provisional id has no citable form. Within a coordinate an id is one row across every document of its plane; the gate refuses a second. |
| `project`, `fabric` | the project code and fabric, each equal to what the id and the path declare; the gate compares them. |
| `surfaced_by`, `surfaced_at` | seat or worker serial; UTC. |
| `one_line` | the surprise as surfaced. |
| `spec_asserts`, `world_is` | the two halves of the trigger: what the task order said, and what the world was. A row that cannot state both is an opinion, not a surprise. |
| `class`, `hazard_standing`, `disarm_owner` | section 3; `disarm_owner` is required whenever `hazard_standing` is `ARMED`. |
| `grounding` | `{status: INFERRED or GROUNDED, evidence: [citations]}`; `GROUNDED` requires source or live-primitive evidence, never self-report. |
| `disposition` | `UNDER_INVESTIGATION` at surfacing; the terminal value is set by the CVO's adjudication row, never by the surfacing seat. |
| `notes` | free text; the closing condition of an open row belongs here. |

---

## 4a. The adjudication document -- the CVO's rows about the rows

**Homes.** `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/adjudications/ADJUDICATION_v<N>.md`, or
`org/surprise_channel/<CODE>/ADJUDICATION_v<N>.md` for a project without a tree home; `.Z.md` on site Z. One document,
one fenced block, the same schema as the investigation document. The lane admits the CVO only.

**Who writes.** The CVO, and only the CVO: every disposition, every scoped correction, every closure row, every
observation it makes at L8 or L9, and the grade of every judgment criterion. A worker or seat that wishes to contest
an adjudication surfaces a new investigation row citing it; it never writes here. The census counts the investigation
document's rows as the items and reads this document's rows for their dispositions and grades; a row here is never an
item, so a row of the CVO's cannot hold the CVO's own slug.

**Disposition axis.** One intent: what the row's end at this limb is. `UNDER_INVESTIGATION` is the only active state;
the three terminals partition every row's end: valid and grounded graduates and seeds a remediation row; not valid or
not worth carrying is dismissed with its reason; valid and revealing an unenumerated operative surface is
`DECOMP_INVALIDATING`, a graduated row whose remedy needs a cell the decomposition does not contain. It is carried in
the slug like every other disposition, it never interrupts the round, and whether the recut re-decomposes is the COO's
call on reading the CTO's round-N analysis. The three terminals take three different remedies: build, record, widen.

**Setting a disposition.** An investigation row is appended with `UNDER_INVESTIGATION`. The CVO's adjudication is a
new row in this document carrying `adjudicates` with the investigation row's id, the terminal disposition and its
reason or evidence; the investigation row is unchanged. A reader resolves an item's state from the newest row that
cites it, across the two documents. An `adjudicates` that names an id two investigation documents carry lands on no
single item and is refused as ambiguous, never applied.

**Grading a judgment criterion.** A criterion the task order could not reduce to an invocation and an expectation is
graded by the CVO alone, in the `grades` field of a row of its own: one entry per criterion carrying the criterion id as
the task order names it, the graded instance as `<path>@<commit>`, the verdict `PASS`, `FAIL` or `NOT_EVALUATED`, and
the reason citing the bar. `NOT_EVALUATED` is the verdict when the instance, the artifact or the bar is unreachable; a
grade never converts an instrument's limit into a pass or a fail. A grade lives in that field and nowhere else: a
verdict in prose is a summary no consumer can reject on.

**A row that opens nothing.** A row of the CVO's that adjudicates no item and opens no item -- a grade record, an
observation, a disarm's citing successor -- carries `DISMISSED_WITH_REASON` with a reason naming it a record, so that
the census reads it closed. The disposition enum has no record value and this version proposes none; a proposal
arrives with its four-postulate record and token census or it is not a proposal.

---

## 5. The remediation document -- graduated rows only

**Homes.** `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/remediations/REMEDIATION_v<N>.md`, or
`org/surprise_channel/<CODE>/REMEDIATION_v<N>.md` for a project without a tree home; `.Z.md` on site Z. The lane admits
the CVO only.

**When.** Cut at round close, once the L10 precondition of section 8 holds, and issued to `1.0.0_SA_CTO` as the slug:
one message carrying the document's path and vintage. Its rows reach `2.0.0_SA_COO` through the CTO's round-N
analysis, which travels with this document; they are inputs to the COO's next issuance and are not task orders.

**Row fields** (`org/surprise_channel/schemas/remediation_row.schema.json` is normative): `id` equal to the graduated
investigation row's id, in the same grammar; `project`, `fabric`; `class`, `hazard_standing`; `mechanism` (the grounded
attribution, carried verbatim); `evidence`; `remedy`; `owner` (the lane that builds); `round`; `remediation` `{state:
OPEN or REMEDIATED, owner, round}`; for `ARMED` rows also `disarm` `{state: ARMED or DISARMED, owner, at}`; and `closed`.
A remediation row carries no route and no loop target: the slug has one reader, the CTO, and the recut has one owner,
the COO. The schema's route fields remain only until the last round issued under the prior text has landed its slug;
a schema that forbids a field a live round's slug carries refuses that slug.

**Disarmed is not remediated.** Two states, two owners, two clocks. Disarm is urgent and off-cadence; remediation
rides the round. An `ARMED` row is `closed` only when both states have landed; an `INERT` row when `REMEDIATED`. A
single terminal state would convert dangerous-and-visible into safe-and-invisible.

---

## 6. The escape valve -- an `ARMED` row rides outside round cadence

An `ARMED` row is surfaced in the same turn like any other, and its disarm does not wait for the round. The surfacing
row names the disarm owner: whoever can act on the armed artifact now. A worker names a disarm owner and never is one:
it has no seat to be reached at. If the named owner is dark, no seat in the round may carry that by message -- a worker
has no send tool, the CVO's one send is the slug, the COO's one send is its drain-end read -- so the valve's actuator is
the seat that reads every row a branch carries at the merge: `2.0.0_SA_COO` re-seats a dark disarm owner as the seat
that spawns, and an owner it cannot seat rides its drain-end read to `1.0.0_SA_CTO`, who seats it or asks the
integrator, `0.0.0_AB_MSTR`, to seat a class. A disarm is reported as a new row citing the armed row. A valve whose
actuator has no owner reads open and is shut.

---

## 7. L8 compilation -- the CVO's intake

The CVO's engagement with a project begins at L8; during a round it has no correspondent, and its one message of the
round is the slug to `1.0.0_SA_CTO`. Its intake is `org/surprise_channel/surprise-watch.sh <serial> stream`, a
read-only watermark over both roots that prints one line per new, mutated or vanished row and never writes what it
watches; `comp-surprise` is the rollup over both roots. The intake reads the investigation document: worker rows, and
nothing the CVO wrote itself. The watcher notifies and never blocks; its state records what it emitted, never that a
seat read anything. A row the CVO reads is acknowledged by its L9 act, never by a message.

**The watermark is the stall control.** A dead watcher and a quiet channel read alike. The CVO's heartbeat summary
carries the channel's watermark: rows seen, rows undispositioned, the watcher's process and its parent-tied banner. The
COO reads it once, when every task order is terminal, against the channel's row count; a watermark behind the channel
rides the COO's drain-end read to `1.0.0_SA_CTO`, never to the CVO, and the CTO re-arms the watcher. One read; no
monitor, no cron.

---

## 8. L9 adjudication and L10 -- the slug

**L9.** Every investigation row receives its disposition in the adjudication document per section 4a. Every judgment
criterion of every proof-of-spec instance under the project receives its grade there too, in the `grades` field: a
criterion the task order could not reduce to an invocation and an expectation is not self-graded by the worker, and
the checker grades no criterion's truth; the CVO reads the instance against the specification and its row is the
grade. Graduated rows receive a remediation row per section 5. A `DECOMP_INVALIDATING` row is carried in the slug and
interrupts nothing.

**L10 precondition.** Every task order under the project is terminal (`complete`, `superseded`, `cancelled`,
`withdrawn`), each finished with a valid proof-of-spec instance whose `surprises` entries resolve to rows, and every
investigation row is dispositioned. An open item is not a zero: a round with an `UNDER_INVESTIGATION` row does not
issue its slug and does not close. The row gate enforces both halves.

**The slug.** The CVO writes the remediation document and sends one message to `1.0.0_SA_CTO`: its path and vintage.
That message is the CVO's only send of the round, and the CTO is its only recipient. The CVO neither routes a row to a
limb nor names who acts on it; a remediation row carries no route and no loop target. A graduated row whose remedy was
executed inside the round by its owner carries `remediation.state` `REMEDIATED` and, for an `ARMED` row, `disarm.state`
`DISARMED`, with the exercised remedy cited in `evidence`; such a row asks nothing of the next round.

**What the CTO does with it** is the spine's L10 and not this annex's: a coverage read per outcome, then a PRD addendum
for an outcome no cell served or a round-N analysis handed to `2.0.0_SA_COO` with this document, and the COO's recut as
one issuance. The CVO's engagement with the round ends at the slug; its constitutional review of the spine and its
reading of the next round's rows are separate acts.

---

## 9. Homes, validation, and the two fabrics

**Gates.** `.tools/surprise-row-gate.py` at commit, reading staged bytes against HEAD, refuses on either root: a new
investigation row without `spec_asserts` and `world_is`, without `project` and `fabric` agreeing with its id and its
path, or off its schema; a new row whose id exists in any other document of its plane under the project at the graded
index (the investigation plane is the investigation and adjudication documents; the remediation plane is its own;
across planes ids coincide by design); any pre-existing row changed in place; a new remediation row without its
required fields, or a graduated row without grounded evidence; and a remediation row, or an adjudication row carrying
`DECOMP_INVALIDATING`, while any task order under the project is not terminal or any investigation item under it is not
dispositioned. It fails closed on an unreadable blob or an unparseable block, and it reads the schema from the staged
index, never the worktree, so a schema and the rows that need it land in one commit. A collision already at HEAD is
reported by the census, never re-graded and never renumbered. `.tools/proof-of-spec-check.py` refuses a worker's
proof-of-spec instance whose `surprises` entries do not each open with a row id present in the project's investigation
file, so a task order cannot complete on a surprise that has no row.

**What the uniqueness limb cannot see, and what covers it.** The limb refuses what the graded index carries; a worker
worktree's index does not carry the main index's allocations, so two indexes can still each mint the next id of ONE
sequence. Two carriers close that: the drain runs the row gate against the merged index and censuses every id the
branch mints across every document of the plane before the merge commit lands (the COO's step); and the allocator
coordinate in the id grammar (section 4) gives each worktree its own sequence, so no merge can collide two of them.

**Carriers named and not yet built.** Until each lands the clause binds by reading and the gate's audited override,
written into the commit that uses it, is the only lawful way through. The gate's requirement that a worker's row carry
`W<n>` equal to the committing worker's suffix and that a seat's row carry none, and the checker's and the corpus
validator's acceptance of the coordinate, are the coordinate's gate half; until they land no `W` row is admitted and
the grammar binds by reading. `org/mcp/cvo_send_guard.py` admits the CVO to the COO at every stage; the CVO's silence
toward the COO during a round binds by reading until the guard is narrowed to the slug. The `grades` field, the
adjudication document, its lane, the cross-document census and the uniqueness limb are built.

**Validation of a document** extracts the single fenced block and validates each row against its schema, printing the
row count as its denominator.

**One investigation file per fabric per round, with a fabric-distinct filename.** The laptop fabric writes
`INVESTIGATION_v<N>.md`; site Z writes `INVESTIGATION_v<N>.Z.md`; the same for adjudication and remediation files unless
the two certifiers agree at handover on one merged remediation authored by one of them. The two files are never merged;
a same-path add on both branches resolves by rename, keeping each file's content. Ids carry the fabric coordinate
(`<CODE>-S<n>` and `<CODE>-Z-S<n>`) and, for a worker's rows, the allocator coordinate (`<CODE>-W<n>-S<k>`), so that two
certifiers on two machines and two worktrees on one machine never allocate one sequence; bridged messages cite the
namespaced id.

**Mirror versus collision.** This rule applies where both fabrics independently author a channel for one project, not
where a file merely exists at the same path on both branches. A file one fabric authored and the other pulled is a
mirror: byte-identical whole file, leave it alone. Divergent content under shared ids is a collision: rename. The
discriminator is one byte comparison of the whole file.

---

## 10. Amendment protocol

This annex is amended as a whole by `3.0.0_SA_CVO`, on Andrew's word or on a finding the CTO's round-N analysis raises
to law, as a new version with one changelog line naming the record that authorized it. No in-place markers, no
partial-clause patches, no quotations, no dates or hashes in the body. An amendment of the spine that touches L7 to
L10 amends this annex in the same window, by the spine's scribe when Andrew's word names that seat, and the CVO's
constitutional review of it follows. A document that describes the channel in a second shape is retired to a redirect
the day it is found.

---

## 11. Changelog

| version | date | authorizing record | summary |
|---|---|---|---|
| 1.0 | 2026-08-21 | Andrew's ratification of the channel framework at the CTO terminal; the CTO's assignment of the channel to the CVO | one home per document; the two axes; the grounding bar; investigation and remediation documents; the escape valve; round mechanics |
| 1.1 | 2026-08-21 | the CTO's cross-fabric ruling on colliding ids | one file per fabric per round; ids carry the fabric coordinate; mirror versus collision |
| 1.2 | 2026-09-02 | `org/tier0/ledger/` entries for the row gate and the project tree; Andrew's word at the CTO terminal on lane `ANY` for investigations | `.tools/surprise-row-gate.py`; `project`, `fabric`, `spec_asserts`, `world_is` gate-required on new rows; the tree root; the `SCOPE_CHANGE` payload; the remediation schema's fabric coordinate |
| 2.0 | 2026-09-03 | state of record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_024xZ_CANONICAL_WORKFLOW_L1_L10_STATE_OF_RECORD.md` @716a9bc7ce (LD-0521); brief `org/tier0_exec/0.0.0_AB_MSTR/deliverables/BRIEF_20260903_CANONICAL_FABRIC_WORKFLOW_SPEC_TEN_LIMBS_ONE_PROCESS.md` @ba9add4200; Andrew's word at the CVO terminal, recorded at `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260903_031xZ_SURPRISE_ROW_NOT_MCP_GATE_ON_PROOF_OF_SPEC_SURPRISES.md` @007481053a | re-keyed from a five-stage document to the L7 to L10 annex of the spine, in constitutional form; the row is the only carrier and the surfacing seat appends its own row on either root; append-only as a control with corrections as new rows; the proof-of-spec surprises limb; the L10 precondition and its gate; the CVO's intake named |
| 2.1 | 2026-09-03 | spine v2.1 `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` @aaa5a2b085; Andrew's two words at the COO terminal, recorded at `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_L7_L10_LOOP_CVO_RELAYS_TO_COO_NEVER_CONVERSES_WITH_WORKERS.md` @10a4beaffb and `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_043xZ_ALL_TOS_PROOF_OF_SPEC_BEFORE_LOOPBACK_CVO_REMEDIATION_SLUG_AT_L10.md` @de2d6d643c | the channel runs in one direction: findings up to the COO or the CTO, never down to a worker; the round's remediations issued as one slug at L10 to the route owner only; the L10 precondition carries the valid proof-of-spec instance with resolving surprises; the loop stated |
| 2.2 | 2026-09-03 | the reading of the channel mechanism's owner `1.0.0_SA_CTO` on the NFRA_CLDGRPH round-2 id collision (message 93459): the gate is the allocator and an id is minted at commit | an id is provisional until its commit and is not cited; a citation carries `<id>@<commit>`; the header's section pointers corrected (amendment is section 10, the changelog section 11); the changelog reordered by version |
| 2.3 | 2026-09-03 | the gate-model ruling of the channel mechanism's owner `1.0.0_SA_CTO` (message 93572) on the fork with `1.0.0_SA_CTO~Z` over a site-Z slug that could only land as re-entry rows; the gate `.tools/surprise-row-gate.py` @ebe3a4caea (11 of 11 arms) | a new remediation row omits its route only when already remediated inside the round (and disarmed, if armed), the remedy cited in `evidence`, re-entering nothing; an open remediation without a route stays refused |
| 3.0 | 2026-09-03 | spine v3.0 `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, from the CRO's implementation spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/SPEC_CANONICAL_FLOW_V3_SUBAGENT_WORKERS_ONE_SHOT_DISPATCH_20260903.md` @29bf9265ea and its section 13 @9dc97d860d (lever L-2 on judgment criteria, lever L-3 on the split channel); Andrew's word at the CTO terminal, recorded at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_200xZ_CANONICAL_FLOW_V3_RESTRUCTURE_SPINE_SKILL_CLAUDEMD_SINGLEHANDED.md`; amended by the spine's scribe `1.0.0_SA_CTO` in the same window as the spine, per section 10 | the three route tokens and `loop_target` retired from the row grammar: a remediation row carries no route, the slug goes to the CTO and to no one else, and the CTO is the single router of every round; the CVO's one send of a round is the slug; the channel split into three documents by writer -- worker rows in `investigations/`, the CVO's dispositions, corrections and observations in a new `adjudications/` document, graduated remedies in `remediations/` -- so L8 reads and L10 counts surprises only; judgment criteria of a proof instance graded by the CVO at L9, never self-graded; `DECOMP_INVALIDATING` stays a disposition (what the remedy needs) and loses its mid-round interrupt; a `BLOCKING` row reaches the issuer in the worker's final report, workers having no inbox and no send tool; the watermark in the CVO's heartbeat as the stall control, read once by the COO at drain-end and escalated to the CTO; the gate's route limb and its single-document census named as contradicting this text and retired or extended as build acts, the audited override the only way through until then |
| 3.1 | 2026-09-03 | `3.0.0_SA_CVO`'s constitutional review of v3.0, recorded at `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_CONSTITUTIONAL_REVIEW_SURPRISE_CHANNEL_PROTOCOL_v3.0_20260903T2100Z.md` @063118e837 and answered by spine v3.1 @20e1293216 (the COO at merge re-seats a dark disarm owner; the drain-end read is the COO's one message); Andrew's word at the CRO terminal on the eight v3 carriers, relayed as message 93972 and recorded at `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260903_222xZ_MECHANISMS_NOW_EIGHT_V3_CARRIERS_BUILD_IMMEDIATELY_CRO_CHECKS_OUT.md` @9f60e36398; the schema `org/surprise_channel/schemas/investigation_item.schema.json` in the same commit as this version | the `grades` field built and named in sections 4a and 8: one entry per judgment criterion carrying the criterion id, the instance as path@commit, the verdict `PASS` / `FAIL` / `NOT_EVALUATED` and the reason citing the bar, refused off its enum, without its reason or without its commit; a row of the CVO's that opens nothing carries `DISMISSED_WITH_REASON` naming itself a record, the enum gaining no value; section 6's escape valve reconciled to the spine's carrier (the COO at merge re-seats a dark disarm owner, one it cannot seat rides the drain-end read, the integrator seats a class on the CTO's or COO's request); section 7's stall report rides the COO's drain-end read; section 9's carriers named and not yet built brought current (the route limb, the adjudication document and its census, the send guard), the schema's route fields retiring only after the route limb |
| 3.2 | 2026-09-04 | Andrew's word at the CVO terminal on `/open-calls`, verbatim "a for both", recorded at `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260904_050xZ_A_FOR_BOTH_ALLOCATOR_COORDINATE_AND_ESTATE_SITTING.md`; the proposal `org/tier1_exec/3.0.0_SA_CVO/deliverables/PROPOSAL_CHANNEL_ID_ALLOCATOR_COORDINATE_20260904.md` @ddbbf3ce46 with its Rule 24 record and consumer census; the collision it answers, `NFRA_COMPEFFICACY-S37` @f357b84197 and its disarm `S38` @3aa32a699e; the gate's uniqueness limb and item census `.tools/surprise-row-gate.py` @72d05b2642 and the rollup @747da480bc; the two schemas and the intake `org/surprise_channel/surprise-watch.sh` in the same commit as this version | the allocator coordinate: a row minted in worker `<n>`'s worktree carries `W<n>` (`<CODE>-(Z-)?(W<n>-)?S<k>`, fabric first), `<k>` restarting per coordinate, a seat's row carrying none, existing ids unchanged and nothing renumbered -- the two schema patterns, the `adjudicates` pattern and the intake's row-count regex accept it; the gate half (a worker's `W<n>` equal to the committer's suffix, none on a seat's row; the checker's and the corpus validator's acceptance) named as the carrier not yet built; section 4a states that the census counts investigation rows as items and reads this document for dispositions and grades, and that an adjudication of an id two investigation documents carry is refused as ambiguous; section 9 carries the uniqueness limb, its bound and the two carriers that cover it, and drops the route limb and the adjudication document from the not-yet-built list; the remediation schema's route fields retire when the last round under the prior text has landed its slug |
