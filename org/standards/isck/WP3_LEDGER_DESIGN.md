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
only). Battery size, derived: 24 reject + 24 accept on rows 1/3–12 (with row 5's five axes
expanded) + 18 + 18 on row 2 + 6 resolve-if-present = **90 arms** — the number a runner must print
beside its colour.

**Completion evidence (memo §8):** WP-3 completes on this battery passing from a clean clone of
the pinned commit, not on code delivery. ⛔ **INSTRUCTION, not description (R3-DT-7, `0.4.0_DT_
ClientPlatform~X`): the first draft of this table named 23 reject arms and ONE accept arm beneath a
sentence claiming both directions — a battery built from it could only ever say NO, and §7 makes
this table the battery's source. Every row now names its sibling accept arm(s); the battery is NOT
complete until every id in both columns exists and the runner prints the 90-arm denominator.**

## 4. DERIVATION RULES (one per derivable axis; the projection is a pure fold over events)

- `entity.current_status`: `provisional` at mint unless the receipt is `checked_unique` (→ `active`);
  `contested` iff an opened `contest_event` (target entity) has no resolved partner OR an upheld
  resolution's `consequence_refs` do not yet exist; `retired` iff a `retirement` relation exists OR the
  entity occupies the ceasing endpoint of a directional relation (§3.12 table); else `active`.
- `entity_binding.status`: `open` iff no close event and no `valid_to`; `closed` iff a close event;
  `disputed` iff an open contest with `target_kind: binding` names it (the R2-2 carrier for the one
  deferred ARM-1 value — it closes here).
- `identity_relation.verification_standing` and `bridge_assertion.verification_standing`: the head
  of the assertion chain (`superseded_by` links); a `contradicted` assertion is left only by a new
  assertion superseding it.
- `materializer.current_status`: `superseded` iff a `materializer_version` with `supersedes` points
  past the current; `retired` by decommission event; `unknown` iff zero observations.
- `bridge_assertion.registry_standing`: ADJUDICATION-CARRIED — authored; the ledger stores it and
  refuses a change without an `adjudicated_by` (the event vocabulary is a later candidate).

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

design attacked-dry → engine chosen by ONE stated criterion (Rule-26 locality of the store) →
battery written FIRST from §3 (both arms per row) → ledger code until the battery passes from a
clean clone → `wp3_certification_receipt` set on the frozen bundle (NOT a new candidate_id: the
contract did not change) → the live vertical slice (charter exit condition 3) begins.
