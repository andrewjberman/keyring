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
| 1 LAW-1 derivation-freedom (audit incomplete) | mint-receipt authentication: every `entity` must be preceded by a `mint_receipt` from a registered minting authority in its epoch, and the entity's mint facts must EQUAL the receipt's (§3 row 6) |
| 3 referential resolution | every STRICT reference in §2d RESOLVES to a stored record or the write is REJECTED |
| 5 serial uniqueness beyond a batch | global uniqueness across batches AND fabrics (the `provisional` reconciliation path stays: two fabrics may each mint; the ledger records both and the `canonicalized_as` relation, never a rewrite) |
| 6 LAW-3 append-only (no plane) | no delete, no in-place semantic mutation: a write that carries an existing primary id with different bytes is REJECTED; "close" is an event |
| 11 cross-record promises | `superseded_by` freezes standing; upheld contests need a consequence on the same target dated after; resolved needs an opened — **each a REJECTED-WRITE rule (§3 row 13), never a projection state** (R3-CRO-25 / R3-CVO-9) |
| 12 canonicalization / cross-batch provenance | the frontier normalizer (per `normalization_version`); run↔surface↔frontier joins across the whole store |

## 2. AUTHORITATIVE vs DERIVED — the object model (memo §8, made concrete)

| object class | AUTHORITATIVE records (append-only; the truth) | DERIVED read model (recomputable; never written by a client) |
|---|---|---|
| Entity identity | `entity` · `mint_receipt` · `identity_relation` (incl. `retirement`) · `contest_event` (target_kind entity) | current entity standing; canonical serial for any serial (alias resolution) |
| Bindings | `entity_binding` rows (each an assertion of an interval) · binding open/close EVENTS · `contest_event` (target_kind binding) | current bindings by identity space + substrate key; binding history per entity |
| State | `state_observation` (incl. `observed_absent`, `partial`) | latest admissible state per (serial, space, fabric, method) |
| Materializers | `materializer` · `materializer_version` · `materialization_run` (+ run receipts) | current version (HEAD, §4); lifecycle standing; consumers |
| Provenance | `source_frontier` (+ entries) | resolved consumed-state vector per run; frontier identity |
| Surfaces | `surface_version` (+ publication receipt fields) | current authority version per logical surface (HEAD, §4); current physical projections |
| Coherence | `coherence_evaluation` | current alignment status per (target_policy, fabric) |
| Migration | `migration_receipt` | vintage of any rewritten value (the manifest lookup, RA-4) |

**`status_basis` rule (R2-2 §2), made consistent with the FROZEN machine contract (R3-CRO-26,
`4.0.0_SA_CRO~X`):** the frozen `+38` schema requires `status_basis` on the five status-bearing
records with each axis value `const: authored`, and `+38` is immutable. So **authoritative records
stay `authored` — always.** What the ledger adds is (a) a DERIVATION RULE per derivable axis (§4) and
(b) the REJECTED WRITE: an authored value on a derivable axis that disagrees with the fold over the
admitted records is refused (§3 row 5) — LAW 3's enforcement plane arriving without a byte of the
contract changing. The DERIVED value lives in a **PROJECTION object**, which is NOT a contract
record: it has no `record_type` in the frozen catalog, is never admitted as a write (a projection
submitted as a batch member is REJECTED — `L-05-projection-submitted-as-record-rejected`), and
carries `{axis, value, basis: [admitted record ids], derived_at_commit_seq}` so the `why` surface
(§5.4) can show it. Controls: `L-05-frozen-authored-record-validates` (a `+38`-valid record whose
authored value agrees with the fold is ACCEPTED unchanged) and
`L-05-projection-not-mistakable-for-record` (a projection fails `+38` validation by construction).
`bridge_assertion.registry_standing` stays ADJUDICATION-CARRIED (`authored`, no fold) until an
adjudication-event vocabulary exists (declared, not absorbed). The earlier sentence here — "`derived`
becomes LEGAL and REQUIRED for ledger-resident records" — was a contract change dressed as a ledger
rule and is withdrawn.

## 2b. WHAT THE FROZEN CONTRACT CANNOT CARRY — routed to a NEW CANDIDATE, never a mutation of +38
(R3-CRO-19 / R3-CVO-6, the design attack's central result)

The frozen catalog has 14 record types. Five facts this design must derive or enforce have NO
append-only carrier in it:

| transition | what the frozen contract offers | why it cannot work append-only | carrier required (new candidate) |
|---|---|---|---|
| supersession of an assertion (`identity_relation`, `bridge_assertion`) | `superseded_by` on the OLD record | setting it after the old record exists is an in-place mutation (responsibility 3 rejects; LAW 3); setting it at creation requires a forward reference to a record that does not yet exist (responsibility 2 rejects) | **backward link:** `supersedes` on the NEW assertion (already the shape on `materializer_version.supersedes`); `superseded_by` becomes derived, never written |
| binding close (and open as an event) | `entity_binding.valid_to` + `status` on the row | a close is a mutation of the open row, or a second row with no link to the first | **`binding_event`** `{opened \| closed}` with `binding_id`, `occurred_at`, `actor`, `evidence_refs` — or `lifecycle_event` generalizing `contest_event` |
| materializer decommission | nothing (`retired` is authored) | no event to fold over | **`lifecycle_event` `materializer_decommissioned`** with `materializer_serial`, `occurred_at`, `actor`, `evidence_refs` |
| mint-authority registration + epoch (R3-CRO-30; the R3-CRO-19 residual) | nothing — `minting_authority` is a `nonempty` string on `entity` and `mint_receipt`; row 6's in/out-of-epoch arms had no source of truth and replay could not reconstruct which epoch applied | an external registry is not in the replay set and not anchored by `commit_seq` | **`authority_epoch_event`** `{opened \| closed}` with `authority_id` (= the `minting_authority` string), `occurred_at`, `actor`, `evidence_refs` — a TOTAL state machine per `authority_id` (start CLOSED; `opened` only from CLOSED, `closed` only from OPEN; ordered by `(occurred_at, commit_seq, event id)`); an epoch is the interval between an `opened` and its `closed`; reopening legal; mint authorization is evaluated at the mint batch's own `commit_seq` and is never re-opened by a backfilled event (row 6, R3-CRO-34) |
| materializer process-level supersession (R3-CVO-6 residual limb, replay 20260828T043700Z) | `superseded_by_version` on the OLD `materializer` | the same shape as `superseded_by`: set after the successor version exists it is an in-place mutation of the old record; set at creation it is a forward reference to a version that does not yet exist | **`lifecycle_event` `materializer_superseded`** with `materializer_serial`, `superseding_version_id` (a `matv:` of ANOTHER materializer), `occurred_at`, `actor`, `evidence_refs`; `superseded_by_version` becomes derived, never written (REFUSED after creation, row 3) |
| correction of an EVENT (R3-CVO-12, adjudicated 20260828T050018Z, ledger row 13; closed over ALL THREE carriers by R4-CRO-2) | `contest_event.target_kind` is `entity \| binding` only — no contest can name an event, so a mis-typed `materializer_superseded`, a wrong-but-well-shaped binding close, or a wrong epoch event is irreversible | a terminal, uncorrectable record forces a rewrite on the first typo — the append-only premise fails at every event carrier | **`contest_event.target_kind` widened to `entity \| binding \| lifecycle_event \| binding_event \| authority_epoch_event`** with `target_event_id` (STRICT, exactly-one with the entity/binding target fields, the kind's prefix); `consequence_refs[]` union = `rel \| bind \| bev \| ctev \| lce \| aep`; an `upheld` event contest names exactly ONE replacement (schema `maxItems 1`, the kind's prefix) of the same `event_kind` + the same CARRIER KEY (`materializer_serial` \| `binding_id` \| `authority_id`), new id, validates independently; **VOIDED events advance no machine and feed no fold** — round-4 ITEM 8 |

**Two typing gaps ride the same candidate (R3-CRO-22 / R3-CRO-25):** `contest_event.consequence_refs`
(items) and `migration_receipt.migrated_record_ref` are `nonempty` free strings in `+38` although
the ledger must RESOLVE them (§2d, §3 row 13). Until typed, the ledger applies a PARSE-THEN-RESOLVE
policy to them (§2d); the new candidate types them as record-id unions.

**Ruling (C5's last sentence, applied):** these are CONTRACT defects surfaced by the enforcement
design. They land as **`v0.3-candidate`** — a NATIVE label in a new family (`v0.3-candidate+N`,
`supersedes_bundle_id` → the frozen `+38`; never a second alias on a `v0.2-candidate+N` record —
CVO~X 20260828T043852Z, ledger row 12), attacked (one bounded round on the five carriers + the two
typings + the lifecycle-event contest target + their folds — eight items), then frozen — BEFORE any
ledger code. The frozen
`+38` is not touched; `superseded_by` and `materializer.superseded_by_version` stay in it as fields
the ledger REFUSES to accept on a write after creation (§3 responsibility 3) and populates only as
derived projections. WP-3's §7 sequence
gains this step first. Until the new candidate is frozen, §4's folds for those axes are DECLARED,
not buildable.

## 2c. ADMISSION MODEL — atomic batches, final-state validation (R3-CRO-18 / R3-CVO-7: the mint bootstrap deadlock)

A ledger WRITE is a **batch** (one or more records) admitted ATOMICALLY: every reference in the
batch must resolve against **(store ∪ batch)** at the batch's FINAL state, and the whole batch is
rejected if any does. Ordering inside a batch is irrelevant; there is no "receipt-first vs
entity-first" — the bootstrap pair `{mint_receipt, entity}` is one batch whose two references
resolve against each other. **Primary-id fields are NOT reference fields** (§2d excludes them by
construction; stated so nobody re-adds them). A batch containing an `entity` with no `mint_receipt`
in (store ∪ batch) is REJECTED (responsibility 6); a batch containing a receipt whose `entity_serial`
never appears is REJECTED (responsibility 2, final state). Tests:
`L-06-bootstrap-pair-accepted`, `L-06-orphan-entity-rejected`, `L-02-forward-ref-within-batch-accepted`,
`L-02-unresolved-at-final-state-rejected` (either ordering).

## 2d. THE TYPED REFERENCE TABLE — every reference field in `+38`, its target class, its policy (R3-CRO-22)

Derived MECHANICALLY from the frozen schema at dcbe214a44: a property is a reference iff its type is
`$ref ent_serial` / `$ref mat_serial` or a `pattern` beginning with a record-id prefix (`ent: mat:
matv: run: sf: sv: bind: ct: ctev: rel: br: obs: mr: mig: ce:`), excluding each record's own primary
id. Every other `$ref` in the schema targets a non-record def (`iso_ts`, `sha256`, `ulid`,
`nonempty`, `evidence_refs`, `claim_origin`, `referent_scope`, `registry_standing`,
`verification_standing`) — the census is closed over the schema, not over suffix spelling. **The
earlier row-2 enumeration (18 + 6) was written from memory and omitted four of these; this table
replaces it.**

**Policy values (one axis: what the ledger does with the value):** **STRICT** — must resolve in
(store ∪ batch) at final state to a record of the named class, or the batch is REJECTED; every STRICT
row has BOTH arms `L-02-unresolved-<record>.<field>` / `L-02-resolved-<record>.<field>`.
**STRICT-CONDITIONAL** — STRICT when the stated condition holds, otherwise the field is a mint
(uniqueness under row 13). **PARSE-STRICT** — a `nonempty` string in `+38`; a value that PARSES as a
record id (any prefix above) is STRICT; a value that does not is REJECTED where the responsibility
requires a record (row 13 consequences) and stored OPAQUE otherwise (migration); typed in
`v0.3-candidate`. **EXTERNAL** — an opaque reference to something outside the ledger (evidence
locations, substrate keys, published locations); never resolved; listed so the exclusion is visible.

| record | field | target class | policy | required in +38 |
|---|---|---|---|---|
| `bridge_assertion` | `subject_entity_serial` | `entity` | STRICT | yes |
| `bridge_assertion` | `object_entity_serial` | `entity` | STRICT | yes |
| `bridge_assertion` | `superseded_by` | `bridge_assertion` | STRICT (and REFUSED on any write after creation — row 3; derived only, §2b) | no |
| `coherence_evaluation` | `target_source_frontier` | `source_frontier` | STRICT | no |
| `contest_event` | `contest_id` | `contest_event[event_kind=opened]` with equal `contest_id` | STRICT-CONDITIONAL (`event_kind=resolved`); on `opened` it is a mint (row 13 uniqueness) | yes |
| `contest_event` | `surviving_contest_id` | `contest_event[event_kind=opened]` | STRICT | no (`outcome=merged` requires it) |
| `contest_event` | `target_entity_serial` | `entity` | STRICT | conditional (`target_kind=entity`) |
| `contest_event` | `target_binding_id` | `entity_binding` | STRICT | conditional (`target_kind=binding`) |
| `contest_event` | `target_event_id` (v0.3, item 8) | `lifecycle_event` \| `binding_event` \| `authority_epoch_event` (by `target_kind`; the kind's prefix) | STRICT | conditional (`target_kind` ∈ the three event kinds) — not in `+38`; listed so the round-4 arms `L-02-unresolved/resolved-contest_event.target_event_id` exist from the first draft |
| `contest_event` | `consequence_refs[]` | `identity_relation` \| `binding_event` (v0.3) \| `contest_event` \| `entity_binding` \| `lifecycle_event` (v0.3, item 8 — R3-CVO-13: the ONE authoritative union; the schema pattern is `rel\|bind\|bev\|ctev\|lce`) | PARSE-STRICT (row 13: each item MUST parse and resolve) | conditional (`outcome=upheld`) |
| `entity` | `canonicalized_as` | `entity` | STRICT | no |
| `entity_binding` | `entity_serial` | `entity` | STRICT | yes |
| `identity_relation` | `subject_serial` | `entity` | STRICT | yes |
| `identity_relation` | `object_serial` | `entity` | STRICT | no |
| `identity_relation` | `superseded_by` | `identity_relation` | STRICT (REFUSED after creation — row 3; derived only) | no |
| `materialization_run` | `materializer_serial` | `materializer` | STRICT | yes |
| `materialization_run` | `materializer_version_id` | `materializer_version` | STRICT | yes |
| `materialization_run` | `source_frontier_id` | `source_frontier` | STRICT | yes |
| `materialization_run` | `output_surface_version_ids[]` | `surface_version` | STRICT (each item) | items when present |
| `materializer` | `superseded_by_version` | `materializer_version` | STRICT | no (`current_status=superseded` requires it) |
| `materializer_version` | `materializer_serial` | `materializer` | STRICT | yes |
| `materializer_version` | `supersedes` | `materializer_version` | STRICT | no |
| `migration_receipt` | `migrated_record_ref` | any record class | PARSE-STRICT (parses → must resolve; else stored OPAQUE with `L-02-opaque-migration-ref-accepted`) | yes |
| `mint_receipt` | `entity_serial` | `entity` | STRICT (final state; the bootstrap pair, §2c) | yes |
| `source_frontier` | `entries[].source_serial` | `entity` | STRICT (each entry) | entry-required |
| `state_observation` | `entity_serial` | `entity` | STRICT | yes |
| `surface_version` | `logical_surface_serial` | `entity` | STRICT | yes |
| `surface_version` | `physical_instance_serial` | `entity` | STRICT | no |
| `surface_version` | `producing_run_id` | `materialization_run` | STRICT | yes |
| `surface_version` | `source_frontier_id` | `source_frontier` | STRICT | yes |

**Denominator: 29 reference rows in `+38`** — 26 STRICT + 1 STRICT-CONDITIONAL + 2 PARSE-STRICT — of
which 27 are typed by pattern and 2 (`consequence_refs[]`, `migrated_record_ref`) are free strings the
ledger parses; **+1 row declared for `v0.3` (`target_event_id`), so row 2's template expands over 30**. **There is no "resolve-if-present" class**: a present reference resolves or the
batch is rejected. `state_observation.producer_serial` is `nonempty` in `+38` and names a PRODUCER,
not a ledger record — EXTERNAL, RULED (CVO~X 20260828T043852Z, ledger row 11): a producer may be a
probe, a validator invocation or a human seat; it is NOT typed in `v0.3-candidate`; a future join
adds an explicit `producer_kind` + typed `producer_ref` in a later candidate rather than overloading
this field.

**EXTERNAL (21, never resolved):** `evidence_refs` on `entity`, `entity_binding`,
`state_observation`, `identity_relation`, `materializer`, `coherence_evaluation`, `bridge_assertion`,
`mint_receipt`, `contest_event`, `migration_receipt`; `surface_version.promotion_evidence_refs`,
`surface_version.published_ref`; `entity_binding.native_key`,
`state_observation.source_native_key`, `state_observation.producer_serial`;
`coherence_evaluation.subject_ref` / `target_ref` / `resolved_target_ref`;
`bridge_assertion.held_on` / `store_owner`; `migration_receipt.migration_map`;
`source_frontier.entries[].authority_ref`.

## 2e. ADMISSION ORDER AND THE REPLAY ANCHOR (R3-CRO-23)

Records carry EVENT time (`occurred_at` / `asserted_at` / `minted_at` / `published_at`); nothing in
`+38` carries INGESTION order, and append-only permits a later batch to carry an earlier-dated record
(backfill). Two replays that disagree on whether to include it are both "as of" the same anchor
unless the anchor names an ingestion point. So the ledger assigns, per admitted batch, a
**`commit_seq`** — a strictly increasing integer in the ENVELOPE of the store (never a field of a
record; the frozen bytes are untouched) — and every record is stored with the `commit_seq` of the
batch that admitted it.

**Anchor binding (total, deterministic):**

| anchor | binds to | replay set |
|---|---|---|
| `as_of publication P` | `commit_seq(P)` — the batch that admitted the `surface_version` with `publication_state=published` | every record with `commit_seq ≤ commit_seq(P)` |
| `as_of frontier F` | `commit_seq(F)` — the batch that admitted the `source_frontier` | every record with `commit_seq ≤ commit_seq(F)` |
| `as_of commit_seq N` | N | every record with `commit_seq ≤ N` (the primitive the two above reduce to) |

**Event-time policy inside the set:** folds (§4) order the replay SET by event time; a backfilled
earlier-dated record is EXCLUDED from any anchor admitted before it and INCLUDED — at its event-time
position — in any anchor admitted after it. The `replay` surface (§5.6) returns the anchor's
`commit_seq` beside the estate so a reader can see which backfills it could not know about.
Records outside the source vector are cut by the same `commit_seq` (there is no anchor without a
cutoff). Tests: `L-12-backfill-before-anchor-excluded`, `L-12-backfill-after-anchor-included-at-event-time`,
`L-12-anchor-commit-seq-printed` (accept), plus row 12's existing arms.

## 3. THE THIRTEEN ENFORCEMENT RESPONSIBILITIES (memo §8 + R3-CRO-25 / R3-CVO-9, each with its rejection and its test)

| # | responsibility | REJECT when | REJECT arm ids | ACCEPT arm ids (the sibling that proves the reject is not "reject everything") |
|---|---|---|---|---|
| 1 | global serial uniqueness across batches + fabrics | a mint for a serial already minted (any fabric) — the second fabric's serial must be `provisional` and reconciled by relation | `L-01-dup-serial-cross-batch`, `L-01-dup-serial-cross-fabric` | `L-01-distinct-serials-accepted`, `L-01-provisional-pair-reconciled-accepted` |
| 2 | referential integrity for every reference in §2d | any STRICT / STRICT-CONDITIONAL / parsed PARSE-STRICT reference that does not resolve in (store ∪ batch) at final state | `L-02-unresolved-<record>.<field>` × 30 (the rows of §2d, incl. the v0.3 `target_event_id`) | `L-02-resolved-<record>.<field>-accepted` × 30, plus `L-02-opaque-migration-ref-accepted` (every accept id carries the `accepted` token — `2.0.0_SA_COO~X` 77377 residual) |
| 3 | append-only retention | delete; or a write with an existing primary id and different bytes; or `superseded_by` / `materializer.superseded_by_version` populated on any write after creation | `L-03-delete`, `L-03-inplace-mutation`, `L-03-superseded-by-written`, `L-03-superseded-by-version-written` | `L-03-append-accepted`, `L-03-idempotent-rewrite-accepted` (same id, same bytes) |
| 4 | binding open/close by event, never mutation — a MACHINE per `binding_id` over EFFECTIVE events (R4-CRO-3) | a binding row whose `valid_to` changed in place; a close with no event; a SECOND effective `opened` for one `binding_id`; a SECOND effective `closed`; an `opened` ordered after a `closed` on the same id (the forbidden re-open — re-opening is a NEW `binding_id`); order `(occurred_at, commit_seq, id)`; a voided event is not counted | `L-04-close-by-mutation`, `L-04-close-without-event`, `L-04-second-open-rejected`, `L-04-second-close-rejected`, `L-04-open-after-close-rejected` | `L-04-close-event-accepted`, `L-04-open-accepted`, `L-04-reopen-as-new-binding-accepted`, `L-04-voided-close-then-replacement-accepted` |
| 5 | event→status projection with exact `status_basis` (authoritative records stay `authored`; §2) | an authored status on a derivable axis that disagrees with the fold; a projection submitted as a record | `L-05-entity.current_status-authored-vs-derived`, `L-05-entity_binding.status-…`, `L-05-identity_relation.verification_standing-…`, `L-05-materializer.current_status-…`, `L-05-bridge_assertion.verification_standing-…` (the five DERIVABLE-AT-WP-3 axes; `bridge_assertion.registry_standing` is ADJUDICATION-CARRIED and has no fold — declared, not tested), `L-05-projection-submitted-as-record-rejected` | `L-05-<axis>-authored-agrees-accepted` × 5 (the same five axes), `L-05-frozen-authored-record-validates`, `L-05-projection-not-mistakable-for-record` |
| 6 | mint-receipt authentication + authority epoch + mint-fact equality (R3-CRO-27; the epoch's SOURCE OF TRUTH is the `authority_epoch_event` carrier of §2b — R3-CRO-30 — so the epoch arms are DECLARED until `v0.3-candidate` freezes) | an `entity` with no preceding `mint_receipt`; a receipt whose `minting_authority` is not OPEN at `minted_at` in the epoch state machine **as of the mint batch's own `commit_seq`** (authorization is an ADMISSION-TIME fact, R3-CRO-34: a later-admitted backfilled `closed` never re-opens an admitted mint's verdict — the mint's admission is replayable at its own anchor, §2e; the history question "which authorities were open at t" is a different query and is answered by event time); an epoch event that is not a legal transition of the TOTAL machine (start state CLOSED; `opened` legal only from CLOSED, `closed` only from OPEN; events ordered by `(occurred_at, commit_seq, event id)`, so a same-timestamp `opened` + `closed` order by admission then id — deterministic); `entity.minted_at ≠ receipt.minted_at`; `entity.minting_authority ≠ receipt.minting_authority`; a SECOND receipt for one `entity_serial` ; an epoch event whose `actor` is not one of the ROOT families (`0.0.0_AB_MSTR` / `1.0.0_SA_CTO`, pinned in the schema — R4-CRO-6); an epoch event whose `actor` string differs from the AUTHENTICATED submitting principal (the spoof: a trusted-looking string from another writer — `actor` is authored data, so the ledger binds it to the seat that submitted the batch BEFORE applying the family predicate; CVO~X 054009Z); a voided epoch event is not a transition | `L-06-entity-without-receipt`, `L-06-authority-unregistered`, `L-06-authority-closed-before-mint`, `L-06-overlapping-epoch-rejected` (second `opened` from OPEN), `L-06-close-without-open-rejected`, `L-06-duplicate-close-rejected`, `L-06-unauthorized-epoch-transition-rejected`, `L-06-epoch-actor-spoof-rejected`, `L-06-minted-at-mismatch`, `L-06-authority-mismatch`, `L-06-second-receipt-for-serial` | `L-06-receipted-mint-accepted`, `L-06-authority-in-epoch-accepted`, `L-06-reopened-authority-accepted` (closed then opened again: two intervals, no overlap), `L-06-same-time-open-close-ordered-accepted`, `L-06-backfilled-close-leaves-admitted-mint-accepted`, `L-06-mstr-genesis-open-accepted`, `L-06-cto-close-reopen-as-authenticated-writer-accepted`, `L-06-mint-facts-equal-accepted` |
| 7 | relation direction rules + cycle AND fork rejection on EVERY chain (R3-CRO-24; R3-CVO-8 residual: the `supersedes` chains too) | a canonicalization/succession/replacement/merge cycle; a direction row not in §3.12; a second assertion `supersedes`-targeting the same prior; a second `materializer_version` `supersedes`-targeting the same prior version; a CYCLE in an assertion `supersedes` chain or a `materializer_version.supersedes` chain (the atomic batch `{A supersedes B, B supersedes A}` resolves every reference, forks nothing, and has ZERO heads — cycle detection runs on (store ∪ batch) at final state, §2c) ; a SECOND ROOT — a `materializer_version` with `supersedes` absent when a version for that `materializer_serial` already exists in (store ∪ batch) (R3-CRO-29: two roots resolve everything, fork nothing, and are both heads); a `supersedes` whose target belongs to a DIFFERENT `materializer_serial` (lineage contamination); a `supersedes` whose target is not that materializer's current head; a SECOND effective decommission of one materializer, or ANY effective lifecycle event ordered after its decommission (R4-CRO-4: decommission is TERMINAL; `superseded → decommissioned` is LEGAL; a voided event advances nothing and its upheld replacement takes its position); a SECOND EFFECTIVE `materializer_superseded` event for one `materializer_serial` in (store ∪ batch) — EFFECTIVE = admitted and not VOIDED; VOIDED derives ONLY from an admitted `upheld` lifecycle-event contest (round-4 item 8) whose consequence is exactly one REPLACEMENT event of the same `event_kind` and `materializer_serial` with a new event id that validates independently; the replacement is admitted only as that consequence; `opened` / `dismissed` / `merged` contests void nothing; two effective successors — including a same-batch race — are rejected at final state (R3-CVO-11 + R3-CVO-12 conditions 3–6) | `L-07-cycle-canonicalize`, `L-07-cycle-merge`, `L-07-unknown-kind`, `L-07-branching-supersession-rejected`, `L-07-fork-materializer-version-rejected`, `L-07-cycle-assertion-supersedes-rejected`, `L-07-cycle-version-supersedes-rejected`, `L-07-second-root-rejected`, `L-07-cross-materializer-supersedes-rejected`, `L-07-second-process-supersession-rejected`, `L-07-two-effective-successors-same-batch-rejected`, `L-07-replacement-without-upheld-contest-rejected`, `L-07-second-decommission-rejected`, `L-07-transition-after-decommission-rejected` | `L-07-acyclic-chain-accepted`, `L-07-retirement-accepted`, `L-07-linear-version-chain-accepted`, `L-07-linear-assertion-chain-in-one-batch-accepted`, `L-07-single-root-accepted`, `L-07-single-process-supersession-accepted`, `L-07-voided-then-replacement-accepted`, `L-07-superseded-then-decommissioned-accepted` |
| 8 | frontier coordinate uniqueness + temporal consistency | two entries normalizing to one canonical key with different versions (the NORMALIZER, per `normalization_version`); an observation after the consuming run's start | `L-08-normalized-collision` (the case the contract's shape check cannot see), `L-08-observed-after-start` | `L-08-distinct-normalized-keys-accepted`, `L-08-observed-before-start-accepted` |
| 9 | run / frontier / materializer-version / surface consistency | surface not in run outputs; frontier disagreement; version not the run's | `L-09-membership`, `L-09-frontier-disagree`, `L-09-version-disagree` | `L-09-consistent-triple-accepted` |
| 10 | admissible publication | `published` from a non-succeeded run; before completion; without a promoter | `L-10-publish-from-failed`, `L-10-publish-before-complete`, `L-10-no-promoter` | `L-10-publish-after-succeeded-accepted`, `L-10-unpublished-accepted` |
| 11 | current read projections — single-valued HEADs (R3-CRO-24) | a projection that cannot show its `status_basis` records; a HEAD query that would return two values (impossible after row 7 + the §4 head rules — the arm proves it) | `L-11-projection-without-basis`, `L-11-two-heads` | `L-11-projection-with-basis-accepted`, `L-11-tied-publication-head-deterministic`, `L-11-same-batch-tie-broken-by-id` (R3-CVO-10) |
| 12 | historical replay (anchored by `commit_seq`, §2e) | a replay as of an anchor that differs from the state recorded at that `commit_seq` | `L-12-replay-frontier`, `L-12-replay-publication`, `L-12-backfill-before-anchor-excluded` | `L-12-replay-matches-recorded-accepted`, `L-12-backfill-after-anchor-included-at-event-time`, `L-12-anchor-commit-seq-printed` |
| 13 | cross-record contest integrity (the three limit-11 promises as REJECTED WRITES) | a `resolved` event whose `contest_id` has no admitted `opened` event; a second `opened` for one `contest_id`; a `resolved` whose typed target differs from its `opened`; an `upheld` resolution any of whose `consequence_refs` does not parse, does not resolve, targets a different typed target, or is dated at/before the opening's `occurred_at`; a `merged` whose `surviving_contest_id` is not an admitted `opened`; a SECOND `resolved` for one `contest_id` (two admitted resolutions with different outcomes would make the fold ambiguous — R3-CVO-9 residual); a `merged` whose `surviving_contest_id` equals its own `contest_id`; a `merged` whose survivor is not OPEN at the merge (its own `resolved` already admitted), or has a different `target_kind` / target id, or whose merge edge closes a CYCLE in the merge graph over (store ∪ batch) (R3-CRO-35: survivor continuity — the contest that absorbs another must be a live contest on the same typed target, and A→B, B→A leaves no survivor); an `upheld` contest on an EVENT (v0.3, item 8 — `lifecycle_event` / `binding_event` / `authority_epoch_event`) whose `consequence_refs` is not EXACTLY ONE replacement event of the same `event_kind` and the same carrier key (`materializer_serial` / `binding_id` / `authority_id`), or whose replacement's id already exists; a `resolved` not ordered AFTER its `opened` (same `contest_id`), or an `opened` on an event not ordered AFTER that event — order `(occurred_at, commit_seq, id)`, a same-instant pair decided by the id (R4-CRO-5) | `L-13-event-upheld-without-single-replacement-rejected`, `L-13-event-replacement-kind-or-key-differs-rejected`, `L-13-resolved-before-opened-rejected`, `L-13-opened-before-target-event-rejected`, `L-13-resolved-without-opened`, `L-13-duplicate-opened`, `L-13-duplicate-resolved`, `L-13-resolved-target-differs`, `L-13-consequence-unparsable`, `L-13-consequence-unresolved`, `L-13-consequence-wrong-target`, `L-13-consequence-predates-opening`, `L-13-merged-into-unopened`, `L-13-merged-into-self`, `L-13-merged-into-resolved-rejected`, `L-13-merged-cross-target-rejected`, `L-13-merge-cycle-rejected` | `L-13-opened-then-resolved-accepted`, `L-13-upheld-with-later-same-target-consequence-accepted`, `L-13-merged-into-open-same-target-accepted`, `L-13-dismissed-accepted`, `L-13-event-upheld-with-single-replacement-accepted`, `L-13-same-instant-pair-ordered-by-id-accepted` |

**Battery size is DERIVED, never typed (R3-CRO-21 / R3-DT-8 — the one typed number whose whole job
was to be checked was wrong twice).** The runner prints the denominator by COUNTING the ids it ran;
a reader reproduces it from this table by the predicate `0.4.0_DT_ClientPlatform~X` and
`4.0.0_SA_CRO~X` converged on: every backtick-quoted token beginning `L-` in §3 is one arm, a `× N`
template expands to N arms per column, a token cited twice is one arm. The per-row vector for this
revision is printed in the commit message that lands it, cited by hash — if the vector and the
table disagree, the table wins and the vector is the stale one.

**Completion evidence (memo §8):** WP-3 completes on this battery passing from a clean clone of
the pinned commit, not on code delivery. ⛔ **INSTRUCTION, not description (R3-DT-7, `0.4.0_DT_
ClientPlatform~X`): the first draft of this table named 23 reject arms and ONE accept arm beneath a
sentence claiming both directions — a battery built from it could only ever say NO, and §7 makes
this table the battery's source. Every row now names its sibling accept arm(s); the battery is NOT
complete until every id in both columns exists and the runner prints the denominator it counted.**

## 4. DERIVATION RULES — DECISION TABLES (R3-CRO-20 / R3-CVO-8: a fold is a FUNCTION — exactly one value for every reachable record set)

**Event-order rule, once:** every fold consumes the axis's records in the replay set (§2e) ordered
by `(occurred_at | asserted_at | minted_at, commit_seq, primary_id)`; a record written LATER but
dated EARLIER is folded at its date (append-only, replayable — responsibility 12). **Precedence is
top-down: the FIRST row whose condition holds wins; the last row is the total-coverage default.**
Each table has a pairwise-overlap control (`L-05-<axis>-overlap-<a>-<b>`) proving the precedence
picks one value, and a no-condition control proving the default fires. **Folds consume only
ADMITTED record sets** — row 13 has already refused a resolved-without-opened, a wrong-target or a
pre-dated consequence, so no fold below has a branch for them (R3-CVO-9's "projection folds only
admitted event sets").

**`entity.current_status`** (records: `mint_receipt`, `identity_relation`, `contest_event[target_kind=entity]`)

| # | condition (evaluated in order) | value |
|---|---|---|
| 1 | a `retirement` relation with this subject exists, OR the entity occupies the CEASING endpoint of a directional relation (§3.12 table) | `retired` |
| 2 | an admitted `opened` contest targeting this entity has no `resolved` partner | `contested` |
| 3 | its `mint_receipt.collision_preflight == deferred_to_reconciliation` AND no `canonicalized_as`/`merged_into` relation has resolved it | `provisional` |
| 4 | (default) | `active` |

A contest opened against a RETIRED entity is admitted (append-only) and never changes the value
(row 1 outranks row 2) — the contest's own record carries it. Overlap controls: retired×contested,
contested×provisional, provisional×retired; default control: one receipted `checked_unique` mint,
no relations, no contests → `active`.

**`entity_binding.status`** (records: `binding_event` — NEW CANDIDATE, §2b; `contest_event[target_kind=binding]`)

| # | condition | value |
|---|---|---|
| 1 | an EFFECTIVE (admitted, not voided) `closed` binding_event exists for this `binding_id` — at most one can (row 4's machine) | `closed` |
| 2 | an admitted `opened` contest targeting this binding has no resolved partner | `disputed` |
| 3 | (default: an effective `opened` event, or the row itself with `valid_to: null`) | `open` |

A contest on a closed binding leaves it `closed` (row 1 outranks row 2); a contest on the CLOSE
EVENT itself (item 8) that is upheld voids that close, and the fold then reads the replacement or,
absent one effective close, `open`. **Buildable only after the new candidate carries
`binding_event`** (§2b); until then this axis is authored.

**`identity_relation.verification_standing` / `bridge_assertion.verification_standing`**
(records: the assertion chain via the BACKWARD `supersedes` link — NEW CANDIDATE, §2b)

| # | condition | value |
|---|---|---|
| 1 | this assertion is `supersedes`-targeted by a later assertion | (not current — the HEAD's value is the projection; the old record keeps its own authored standing, never rewritten) |
| 2 | the chain head's authored standing | that value (`unverified` \| `corroborated` \| `contradicted`) |

Single-valued by construction: exactly one head per chain (a second assertion superseding the same
target is REJECTED — row 7, `L-07-branching-supersession-rejected`). **Buildable only after the new
candidate** (§2b).

**`materializer.current_status`** (records: `materializer_version`, `lifecycle_event[materializer_decommissioned | materializer_superseded]` — NEW CANDIDATE for both events, §2b)

| # | condition | value |
|---|---|---|
| 1 | a `materializer_decommissioned` event exists | `retired` |
| 2 | an EFFECTIVE (admitted, not VOIDED) `materializer_superseded` event exists whose `superseding_version_id` resolves to a version of ANOTHER materializer — the projection's basis cites the effective event, and when a voided predecessor exists, the upheld contest and the replacement too; a voided event contributes nothing (R3-CVO-6 residual: the frozen `superseded_by_version` on the OLD record was the same forbidden shape as `superseded_by`; derived from the event, REFUSED on a write — row 3; R3-CVO-12 condition 6) | `superseded` |
| 3 | at least one `materializer_version` for this serial exists | `active` |
| 4 | (default: zero versions) | `unknown` |

Overlap controls: retired×superseded, superseded×active; default control: zero versions → `unknown`.
**Buildable only after the new candidate carries both events**; until then rows 1–2 are authored.

**`bridge_assertion.registry_standing`**: ADJUDICATION-CARRIED — authored; the ledger stores it and
REFUSES a change without `adjudicated_by` (the adjudication-event vocabulary is a later candidate).
Declared, not folded; no table.

**HEAD selection — the two singular projections §2 promises (R3-CRO-24):**

*current version of a `materializer`*: the `materializer_version` chain is LINEAR by row 7 (a fork
is rejected at write); the head is the unique version no other version `supersedes`. A materializer
with zero versions has no head (`failure_state: no_versions`, never an empty string). Control:
`L-11-two-heads` is UNREACHABLE after row 7 — the arm submits the fork and asserts the REJECT fired
at write, not at read.

*current authority version of a logical surface*: among admitted `surface_version` records with this
`logical_surface_serial` and `publication_state=published`, order by `(published_at DESC,
commit_seq DESC, surface_version_id DESC)` and take the first. `commit_seq` is total ACROSS batches
but every member of one atomic batch shares it (R3-CVO-10), so the tertiary key is the primary id
— unique by row 1/row 3, lexically total — and a tie on `published_at` (two publications in one
second, two records with one `published_ref` and different content, or two published versions of
one surface in ONE batch) is broken deterministically; the projection reports `tie_broken_by:
commit_seq | surface_version_id` beside the value (`L-11-tied-publication-head-deterministic`,
`L-11-same-batch-tie-broken-by-id`). Zero published versions → `failure_state:
none_published`. A second published version at the same `published_ref` is a rebuild in place and is
ADMITTED (append-only); the earlier one is history, visible through `replay`.

## 5. THE SIX MINIMUM QUERY SURFACES (memo §8) — each with its evidence shape

1. `resolve(raw_ref) -> {candidates: [serial…], evidence, failure_state}` — zero, one, or many
   canonical serials for a substrate reference, never a silent one.
2. `binding_history(serial) -> [interval + basis + disputes]` — renames and disputed intervals intact.
3. `surface_provenance(surface_version_id) -> {frontier, materializer bundle, run receipt}`.
4. `why(record, axis) -> [status_basis records]` — the admitted records that produce a projected
   value (the projection object of §2).
5. `coherence(physical_pin, target) -> {availability, integrity, currency, provenance, fabric_validity}`
   — five separate axes, never collapsed (§3.14).
6. `replay(as_of: frontier | publication | commit_seq) -> {estate, anchor_commit_seq}` — from
   append-only records, cut by `commit_seq` (§2e).

## 6. WHAT IS DELIBERATELY OPEN (memo §12; not decided here)

- Persistence engine (SQLite/DuckDB file · Iceberg table under Nessie · a JSONL log + index). The
  battery is engine-agnostic by construction: every test is a write-then-query. `commit_seq` is a
  requirement ON the engine (a monotone batch counter), not a choice of engine.
- API form (library · CLI · service). The six surfaces are the contract; the transport is not.
- Round-3 attackers may attack the design's ADMISSIBILITY (a responsibility the thirteen miss; a
  derivation rule that can return two answers; a query surface whose evidence shape lies) — never
  the engine choice.

## 7. LANDING SEQUENCE

design attacked-dry → **`v0.3-candidate`: the five carriers + two typings + the lifecycle-event contest target of §2b (eight items) land in the
contract as a NEW candidate_id in a native family (`bundle_identity.py` family rule amended:
`v0.3-candidate+N`, `supersedes_bundle_id` → +38), attacked in one bounded round (round 4:
`ROUND3_CHARTER.md` addendum, `R4-<seat>-<n>` ids, `round: 4` rows in the continued register,
`BOUNDARY_ROUND4.md`), frozen** → engine chosen by ONE
stated criterion (Rule-26 locality of the store) → battery written FIRST from §3 (both arms per
row; the manifest is the denominator) → ledger code until the battery passes from a clean clone →
**`wp3_certification_receipt` recorded on the frozen label through the REGISTRY-SIDE receipt
carrier** (R3-CRO-28 / R3-CRO-31 / R3-CRO-33: `bundle_identity.py --receipt <kind> --value
<receipt commit> <commit>` appends the receipt to the label's `BUNDLE_LABELS.json` entry — keyed by
the immutable `candidate_id` + `contract_bundle_id`, refused unless the label is frozen, idempotent
on the same value, REFUSED on a conflicting second value — and the VALUE is a commit that must
CONTAIN a STRUCTURED RECEIPT at `org/standards/isck/receipts/<kind>.json` with `kind`,
`candidate_id`, `contract_bundle_id`, `manifest_path`, `manifest_digest`, `result`, `evidence_digest`,
`run_commit`: the validator reads it from the object database at that commit and REFUSES unless
`kind` matches, `candidate_id` + `contract_bundle_id` equal the label's, `sha256(git show
<commit>:<manifest_path>)` equals `manifest_digest`, `result == PASS` and both digests are sha256
strings — an existing commit with no receipt, a receipt of another kind, another bundle, or a FAIL
result writes NOTHING; `derive()` exposes the accepted receipt while the bundle's member bytes and
id are untouched; NOT a new candidate_id because no member byte changed) → the live vertical slice
(charter exit condition 3) begins, its receipt landing by the same carrier.
