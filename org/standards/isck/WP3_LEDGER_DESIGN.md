# WP-3 — THE IDENTITY LEDGER: ENFORCEMENT PLANE FOR THE ISCK (DESIGN, for adversarial attack)

**Author:** `1.0.0_SA_CTO~X` · **Authority:** `3.0.0_SA_CVO~X` C5 verdict (self-drive D11 tick 12,
20260828T040820Z, ledger row 10): *"Land WP3_LEDGER_DESIGN.md before code, then attack-dry with
CVO/CRO/DT."* · **Status: DESIGN DRAFT — binds nothing until attacked-dry and landed as code.**
**Inputs:** the GPT memorandum §5, §8, §9, §10, §12 (`…/D11_GPT_ISCK_STATUS_ASSESSMENT_20260828/`);
`R2_2_DERIVED_STATUS_DESIGN.md` §2 (status_basis, the two axis classes) and its landing;
`ISCK_CONTRACT.md` §6 (every declared limit that says "WP-3"); `BOUNDARY_ROUND3.md` §5.
**Contract it implements:** the FROZEN schema-only candidate `v0.2-candidate+38` at dcbe214a44
(`BUNDLE_IDENTITY.json`). ⛔ **The ledger IMPLEMENTS the pinned model; it does not revise it.** A
defect in the contract found while building is a finding routed to a NEW candidate_id, never a
ledger-side workaround (C5 verdict, last sentence).

---

## 0. THE ONE SENTENCE

**Records are the truth; the ledger is the place that refuses a record which contradicts the
records before it — and the place that answers "what is current" only by deriving it.**

## 1. WHAT THE CONTRACT CANNOT DO ALONE (the limits this design closes — cite, do not restate)

| `ISCK_CONTRACT.md` §6 limit | what the ledger adds |
|---|---|
| 1 LAW-1 derivation-freedom (audit incomplete) | mint-receipt authentication: every `entity` must be preceded by a `mint_receipt` from a registered minting authority in its epoch (§3) |
| 3 referential resolution | every `*_serial` / `*_id` / frontier entry / surface pin / run / materializer version RESOLVES to a stored record or the write is REJECTED |
| 5 serial uniqueness beyond a batch | global uniqueness across batches AND fabrics (the `provisional` reconciliation path stays: two fabrics may each mint; the ledger records both and the `canonicalized_as` relation, never a rewrite) |
| 6 LAW-3 append-only (no plane) | no delete, no in-place semantic mutation: a write that carries an existing primary id with different bytes is REJECTED; "close" is an event |
| 11 cross-record promises | `superseded_by` freezes standing; upheld contests need a consequence on the same target dated after; resolved needs an opened |
| 12 canonicalization / cross-batch provenance | the frontier normalizer (per `normalization_version`); run↔surface↔frontier joins across the whole store |

## 2. AUTHORITATIVE vs DERIVED — the object model (memo §8, made concrete)

| object class | AUTHORITATIVE records (append-only; the truth) | DERIVED read model (recomputable; never written by a client) |
|---|---|---|
| Entity identity | `entity` · `mint_receipt` · `identity_relation` (incl. `retirement`) · `contest_event` (target_kind entity) | current entity standing; canonical serial for any serial (alias resolution) |
| Bindings | `entity_binding` rows (each an assertion of an interval) · binding open/close EVENTS · `contest_event` (target_kind binding) | current bindings by identity space + substrate key; binding history per entity |
| State | `state_observation` (incl. `observed_absent`, `partial`) | latest admissible state per (serial, space, fabric, method) |
| Materializers | `materializer` · `materializer_version` · `materialization_run` (+ run receipts) | current version; lifecycle standing; consumers |
| Provenance | `source_frontier` (+ entries) | resolved consumed-state vector per run; frontier identity |
| Surfaces | `surface_version` (+ publication receipt fields) | current authority version per logical surface; current physical projections |
| Coherence | `coherence_evaluation` | current alignment status per (target_policy, fabric) |
| Migration | `migration_receipt` | vintage of any rewritten value (the manifest lookup, RA-4) |

**`status_basis` rule (R2-2 §2, now enforceable):** for each of the six axes on the five
status-bearing records, the ledger holds a DERIVATION RULE (§4). At WP-3 landing `derived` becomes
LEGAL and REQUIRED for ledger-resident records on the five DERIVABLE-AT-WP-3 axes; a write whose
authored status disagrees with the derivation is a **REJECTED WRITE** — LAW 3's enforcement plane
arriving. `bridge_assertion.registry_standing` stays ADJUDICATION-CARRIED (`authored`) until an
adjudication-event vocabulary exists (declared, not absorbed).

## 2b. WHAT THE FROZEN CONTRACT CANNOT CARRY — routed to a NEW CANDIDATE, never a mutation of +38
(R3-CRO-19 / R3-CVO-6, the design attack's central result)

The frozen catalog has 14 record types. Three transitions this design must derive have NO
append-only carrier in it:

| transition | what the frozen contract offers | why it cannot work append-only | carrier required (new candidate) |
|---|---|---|---|
| supersession of an assertion (`identity_relation`, `bridge_assertion`) | `superseded_by` on the OLD record | setting it after the old record exists is an in-place mutation (responsibility 3 rejects; LAW 3); setting it at creation requires a forward reference to a record that does not yet exist (responsibility 2 rejects) | **backward link:** `supersedes` on the NEW assertion (already the shape on `materializer_version.supersedes`); `superseded_by` becomes derived, never written |
| binding close (and open as an event) | `entity_binding.valid_to` + `status` on the row | a close is a mutation of the open row, or a second row with no link to the first | **`binding_event`** `{opened \| closed}` with `binding_id`, `occurred_at`, `actor`, `evidence_refs` — or `lifecycle_event` generalizing `contest_event` |
| materializer decommission | nothing (`retired` is authored) | no event to fold over | **`lifecycle_event` `materializer_decommissioned`** with `materializer_serial`, `occurred_at`, `actor`, `evidence_refs` |

**Ruling (C5's last sentence, applied):** these are CONTRACT defects surfaced by the enforcement
design. They land as **`v0.3-candidate`** — a new `candidate_id`, attacked (one bounded round on the
three carriers + their folds), then frozen — BEFORE any ledger code. The frozen `+38` is not touched;
`superseded_by` stays in it as a field the ledger REFUSES to accept on a write after creation
(§3 responsibility 3) and populates only as a derived projection. WP-3's §7 sequence gains this
step first. Until the new candidate is frozen, §4's folds for those axes are DECLARED, not buildable.

## 2c. ADMISSION MODEL — atomic batches, final-state validation (R3-CRO-18 / R3-CVO-7: the mint bootstrap deadlock)

A ledger WRITE is a **batch** (one or more records) admitted ATOMICALLY: every reference in the
batch must resolve against **(store ∪ batch)** at the batch's FINAL state, and the whole batch is
rejected if any does. Ordering inside a batch is irrelevant; there is no "receipt-first vs
entity-first" — the bootstrap pair `{mint_receipt, entity}` is one batch whose two references
resolve against each other. **Primary-id fields are NOT reference fields** (row 2's enumeration
already excludes them; stated so nobody re-adds them). A batch containing an `entity` with no
`mint_receipt` in (store ∪ batch) is REJECTED (responsibility 6); a batch containing a receipt whose
`entity_serial` never appears is REJECTED (responsibility 2, final state). Tests:
`L-06-bootstrap-pair-accepted`, `L-06-orphan-entity-rejected`, `L-02-forward-ref-within-batch-accepted`,
`L-02-unresolved-at-final-state-rejected` (either ordering).

## 3. THE TWELVE ENFORCEMENT RESPONSIBILITIES (memo §8, each with its rejection and its test)

| # | responsibility | REJECT when | REJECT arm ids | ACCEPT arm ids (the sibling that proves the reject is not "reject everything") |
|---|---|---|---|---|
| 1 | global serial uniqueness across batches + fabrics | a mint for a serial already minted (any fabric) — the second fabric's serial must be `provisional` and reconciled by relation | `L-01-dup-serial-cross-batch`, `L-01-dup-serial-cross-fabric` | `L-01-distinct-serials-accepted`, `L-01-provisional-pair-reconciled-accepted` |
| 2 | referential integrity for every reference field | any reference that does not resolve in the store | `L-02-unresolved-<field>` × the 18 reference fields enumerated below | `L-02-resolved-<field>` × the same 18 (a resolving reference is accepted) |
| 3 | append-only retention | delete; or a write with an existing primary id and different bytes | `L-03-delete`, `L-03-inplace-mutation` | `L-03-append-accepted`, `L-03-idempotent-rewrite-accepted` (same id, same bytes) |
| 4 | binding open/close by event, never mutation | a binding row whose `valid_to` changed in place; a close with no event | `L-04-close-by-mutation`, `L-04-close-without-event` | `L-04-close-event-accepted`, `L-04-open-accepted` |
| 5 | event→status projection with exact `status_basis` | an authored status on a derivable axis that disagrees with the fold | `L-05-entity.current_status-authored-vs-derived`, `L-05-entity_binding.status-…`, `L-05-identity_relation.verification_standing-…`, `L-05-materializer.current_status-…`, `L-05-bridge_assertion.verification_standing-…` (the five DERIVABLE-AT-WP-3 axes; `bridge_assertion.registry_standing` is ADJUDICATION-CARRIED and has no fold — declared, not tested) | `L-05-<axis>-derived-agrees-accepted` × the same five |
| 6 | mint-receipt authentication + authority epoch | an `entity` with no preceding `mint_receipt`; a receipt from an authority outside its epoch | `L-06-entity-without-receipt`, `L-06-authority-out-of-epoch` | `L-06-receipted-mint-accepted`, `L-06-authority-in-epoch-accepted` |
| 7 | relation direction rules + cycle rejection | a canonicalization/succession/replacement/merge cycle; a direction row not in §3.12 | `L-07-cycle-canonicalize`, `L-07-cycle-merge`, `L-07-unknown-kind` | `L-07-acyclic-chain-accepted`, `L-07-retirement-accepted` |
| 8 | frontier coordinate uniqueness + temporal consistency | two entries normalizing to one canonical key with different versions (the NORMALIZER, per `normalization_version`); an observation after the consuming run's start | `L-08-normalized-collision` (the case the contract's shape check cannot see), `L-08-observed-after-start` | `L-08-distinct-normalized-keys-accepted`, `L-08-observed-before-start-accepted` |
| 9 | run / frontier / materializer-version / surface consistency | surface not in run outputs; frontier disagreement; version not the run's | `L-09-membership`, `L-09-frontier-disagree`, `L-09-version-disagree` | `L-09-consistent-triple-accepted` |
| 10 | admissible publication | `published` from a non-succeeded run; before completion; without a promoter | `L-10-publish-from-failed`, `L-10-publish-before-complete`, `L-10-no-promoter` | `L-10-publish-after-succeeded-accepted`, `L-10-unpublished-accepted` |
| 11 | current read projections | a projection that cannot show its `status_basis` records | `L-11-projection-without-basis` | `L-11-projection-with-basis-accepted` |
| 12 | historical replay | a replay as of frontier F or publication P that differs from the state recorded then | `L-12-replay-frontier`, `L-12-replay-publication` | `L-12-replay-matches-recorded-accepted` |

**Row 2's denominator, enumerated from the frozen schema (so "N reference fields" is never quoted
as a guess):** `entity.canonicalized_as` · `entity_binding.entity_serial` ·
`state_observation.entity_serial` · `identity_relation.subject_serial` ·
`identity_relation.object_serial` · `identity_relation.superseded_by` ·
`bridge_assertion.subject_entity_serial` · `bridge_assertion.object_entity_serial` ·
`bridge_assertion.superseded_by` · `mint_receipt.entity_serial` ·
`materializer_version.materializer_serial` · `materializer_version.supersedes` ·
`materialization_run.materializer_serial` · `materialization_run.materializer_version_id` ·
`materialization_run.source_frontier_id` · `materialization_run.output_surface_version_ids[]` ·
`surface_version.producing_run_id` · `surface_version.source_frontier_id` — **18** (plus
`contest_event.target_entity_serial` / `target_binding_id` / `surviving_contest_id`,
`coherence_evaluation.target_source_frontier`, `migration_receipt.migrated_record_ref` and
`source_frontier.entries[].source_serial`, which are reference-SHAPED but resolve to records the
ledger may not hold yet — **6 declared as "resolve-if-present"**, tested by `L-02-resolved-<field>`
only). Battery size, PARSED per row (R3-CRO-21 — my first sentence here typed "24 + 24 = 48" on
rows 1/3–12; the table itself reads 2R+2A · 2+2 · 2+2 · 5+5 · 2+2 · 3+2 · 3+1 · 3+2 · 1+1 · 2+1 = **27
reject + 22 accept = 49**) + row 2's 18 + 18 + 6 resolve-if-present = 42 → **91 arms**. The runner
prints this number by COUNTING the ids it ran, never by reading this sentence; if the two disagree the
sentence is the stale one.

**Completion evidence (memo §8):** WP-3 completes on this battery passing from a clean clone of
the pinned commit, not on code delivery. ⛔ **INSTRUCTION, not description (R3-DT-7, `0.4.0_DT_
ClientPlatform~X`): the first draft of this table named 23 reject arms and ONE accept arm beneath a
sentence claiming both directions — a battery built from it could only ever say NO, and §7 makes
this table the battery's source. Every row now names its sibling accept arm(s); the battery is NOT
complete until every id in both columns exists and the runner prints the 90-arm denominator.**

## 4. DERIVATION RULES — DECISION TABLES (R3-CRO-20 / R3-CVO-8: a fold is a FUNCTION — exactly one value for every reachable record set)

**Event-order rule, once:** every fold consumes the axis's records ordered by
`(occurred_at | asserted_at | minted_at, primary_id)`; a record written LATER but dated EARLIER is
folded at its date (append-only, replayable — responsibility 12). **Precedence is top-down: the
FIRST row whose condition holds wins; the last row is the total-coverage default.** Each table
has a pairwise-overlap control (`L-05-<axis>-overlap-<a>-<b>`) proving the precedence picks one
value, and a no-condition control proving the default fires.

**`entity.current_status`** (records: `mint_receipt`, `identity_relation`, `contest_event[target_kind=entity]`)

| # | condition (evaluated in order) | value |
|---|---|---|
| 1 | a `retirement` relation with this subject exists, OR the entity occupies the CEASING endpoint of a directional relation (§3.12 table) | `retired` |
| 2 | an opened contest targeting this entity has no `resolved` partner, OR its `upheld` resolution's `consequence_refs` do not all resolve | `contested` |
| 3 | its `mint_receipt.collision_preflight == deferred_to_reconciliation` AND no `canonicalized_as`/`merged_into` relation has resolved it | `provisional` |
| 4 | (default) | `active` |

A contest opened against a RETIRED entity is admitted (append-only) and never changes the value
(row 1 outranks row 2) — the contest's own record carries it. Overlap controls: retired×contested,
contested×provisional, provisional×retired; default control: one receipted `checked_unique` mint,
no relations, no contests → `active`.

**`entity_binding.status`** (records: `binding_event` — NEW CANDIDATE, §2b; `contest_event[target_kind=binding]`)

| # | condition | value |
|---|---|---|
| 1 | a `closed` binding_event exists for this `binding_id` | `closed` |
| 2 | an opened contest targeting this binding has no resolved partner | `disputed` |
| 3 | (default: an `opened` event, or the row itself with `valid_to: null`) | `open` |

A contest on a closed binding leaves it `closed` (row 1 outranks row 2). **Buildable only after the
new candidate carries `binding_event`** (§2b); until then this axis is authored.

**`identity_relation.verification_standing` / `bridge_assertion.verification_standing`**
(records: the assertion chain via the BACKWARD `supersedes` link — NEW CANDIDATE, §2b)

| # | condition | value |
|---|---|---|
| 1 | this assertion is `supersedes`-targeted by a later assertion | (not current — the HEAD's value is the projection; the old record keeps its own authored standing, never rewritten) |
| 2 | the chain head's authored standing | that value (`unverified` \| `corroborated` \| `contradicted`) |

Single-valued by construction: exactly one head per chain (a second assertion superseding the same
target is REJECTED — responsibility 7's cycle/branch rule extended to chains; test
`L-07-branching-supersession-rejected`). **Buildable only after the new candidate** (§2b).

**`materializer.current_status`** (records: `materializer_version`, `lifecycle_event[materializer_decommissioned]` — NEW CANDIDATE for the event)

| # | condition | value |
|---|---|---|
| 1 | a `materializer_decommissioned` event exists | `retired` |
| 2 | `materializer.superseded_by_version` resolves to a version of ANOTHER materializer (the frozen field is the carrier for process-level supersession; "points past the current" was circular and is gone) | `superseded` |
| 3 | at least one `materializer_version` for this serial exists | `active` |
| 4 | (default: zero versions) | `unknown` |

Overlap controls: retired×superseded, superseded×active; default control: zero versions → `unknown`.

**`bridge_assertion.registry_standing`**: ADJUDICATION-CARRIED — authored; the ledger stores it and
REFUSES a change without `adjudicated_by` (the adjudication-event vocabulary is a later candidate).
Declared, not folded; no table.

## 5. THE SIX MINIMUM QUERY SURFACES (memo §8) — each with its evidence shape

1. `resolve(raw_ref) -> {candidates: [serial…], evidence, failure_state}` — zero, one, or many
   canonical serials for a substrate reference, never a silent one.
2. `binding_history(serial) -> [interval + basis + disputes]` — renames and disputed intervals intact.
3. `surface_provenance(surface_version_id) -> {frontier, materializer bundle, run receipt}`.
4. `why(record, axis) -> [status_basis records]` — the records that produce a projected value.
5. `coherence(physical_pin, target) -> {availability, integrity, currency, provenance, fabric_validity}`
   — five separate axes, never collapsed (§3.14).
6. `replay(as_of: frontier | publication) -> the estate as of that point` — from append-only records.

## 6. WHAT IS DELIBERATELY OPEN (memo §12; not decided here)

- Persistence engine (SQLite/DuckDB file · Iceberg table under Nessie · a JSONL log + index). The
  battery is engine-agnostic by construction: every test is a write-then-query.
- API form (library · CLI · service). The six surfaces are the contract; the transport is not.
- Round-3 attackers may attack the design's ADMISSIBILITY (a responsibility the twelve miss; a
  derivation rule that can return two answers; a query surface whose evidence shape lies) — never
  the engine choice.

## 7. LANDING SEQUENCE

design attacked-dry → **`v0.3-candidate`: the three carriers of §2b land in the contract as a NEW
candidate_id, attacked in one bounded round, frozen** → engine chosen by ONE stated criterion (Rule-26 locality of the store) →
battery written FIRST from §3 (both arms per row) → ledger code until the battery passes from a
clean clone → `wp3_certification_receipt` set on the frozen bundle (NOT a new candidate_id: the
contract did not change) → the live vertical slice (charter exit condition 3) begins.
