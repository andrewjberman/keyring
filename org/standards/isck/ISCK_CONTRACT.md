# ISCK CONTRACT v0.1 — the Issue 3A Identity-State Contract (DRAFT, boundary revision)

**Authority:** Andrew ruling 2026-08-27 (ISCK adoption; PRD ratified; minting + retention ratified) —
`org/tier1_exec/1.0.0_SA_CTO/deliverables/D11_ISCK_RULING_20260827/RULING.md`.
**Author:** `1.0.0_SA_CTO~X` · **Status: v0.1 DRAFT — NOT FROZEN.** v0.1 is the ROUND-1 BOUNDARY
revision of the adversarial pass (seats: `2.0.0_SA_COO~X`, `0.4.0_DT_ClientPlatform~X`,
`3.0.0_SA_CVO~X`; findings F1–F7, DT-1–8, CV-1–6, all upheld — see §7 changelog and
`BOUNDARY_ROUND1.md`). Round 2 attacks v0.1. Nothing populates production records until the pass
closes and the version is pinned.
**Machine contract:** `ISCK_CONTRACT.v0.schema.json` ($id `...:v0.1`). **Validator + battery:**
`validate_isck.py` (axis arm + fixtures + mutants with EXPECTED-REASON assertions + semantic checks
+ gutted-schema meta-control). **Vocabulary registries:** `vocab/*.json` (warn-gated at v0.1).
**Coverage probes:** `isck_coverage_probes.py` (DT~X) · `check_postulate_labels.py`,
`check_enum_collisions.py`, `check_mutant_isolation.py` (COO~X).

---

## 1. THE FIVE LAWS (constraints a validator can hold, with their enforcement plane named)

1. **MINT, NEVER DERIVE.** An enduring mutable entity's serial is opaque, minted once, never
   computed from a path, ARN, anchor, parse, or position. Serial patterns enforce SHAPE ONLY —
   see §6 limit 1. **The minting act lowercases the ULID before prefixing** (CV/F6): a serial is
   born lowercase or it was not minted by the authority.
2. **HASH AT THE CORRECT GRAIN, AND THE THREE FIELDS TRAVEL AS A GROUP.** Hashes identify immutable
   things only. `fingerprint`, `fingerprint_method`, `normalization_version` are COUPLED by
   `dependentRequired` in every direction (DT-1/DT-5): a fingerprint never travels without its
   method + normalization, and method/normalization never travel without their fingerprint — on
   EVERY failure_state, not an enumerated subset.
3. **A RENAME IS A BINDING EVENT; NEITHER RENAME NOR STATE CHANGE TOUCHES THE SERIAL.** Bindings
   carry validity intervals; `closed` requires a close instant (DT-4). ⛔ **APPEND-ONLY HAS NO
   ENFORCEMENT PLANE AT v0.1** (CV-2): the validator is stateless and cannot see mutation — see §6
   limit 6. Succession/reconciliation relations carry warrant conditionals (F5).
4. **RULE 26 IS METADATA, AND LOCATION IS TWO FAMILIES, NOT ONE FIELD** (R2-1, the convergent
   round-2 finding — GPT + CRO~X gap 1, independent instruments). **EXECUTION family**:
   `observed_on_fabric` / `executed_on_fabric` / `built_on_fabric` / `evaluated_on_fabric`
   (+ optional `*_device`) — where the act happened; always concrete, always legal to state.
   **REFERENT family**: `referent_scope` (`fabric_invariant | fabric_local | device_local`,
   `fabric_local` NEW) + `referent_fabric_id` / `referent_device_id` — what locality the
   REFERENCED STATE claims; constrained TWO-DIRECTIONALLY BY THE IDIOM (every require arm ships
   with its forbid mirror — the DT-R2-1 family rule): invariant forbids both keys, fabric_local
   requires the fabric and forbids the device, device_local requires both. A run is an EVENT at a
   location and carries execution only — its inputs carry their own scopes, and reconciling the
   two is 3B's fabric_validity axis. The old single `fabric_id` could not say "observed on the
   laptop, about a fabric-invariant referent" without lying in one direction (the round-1
   invariant fixtures did exactly that — the positive battery enshrined the contradiction, both
   reviews' words).
5. **PROVENANCE IS A FRONTIER; COHERENCE VERDICTS CARRY THEIR WARRANT.** Every run consumes a
   `source_frontier`; every surface version pins frontier + materializer version. A coherence
   evaluation asserting `verified`/`mismatch`/a currency verdict REQUIRES evidence; `mismatch`
   REQUIRES its delta (CV-3). `unknown`/`unverified` stay free OF REQUIRED WARRANTS — the remedy
   that moves `verified` must not punish honesty about not knowing. Free of warrants is not free
   of contradiction: a `delta_summary` PRESUPPOSES a comparison and `unverified` asserts none ran,
   so it is FORBIDDEN there (ARM-4 CUT #4; the F5 shape — a value with nothing behind it).

## 2. RECORD CATALOG (17 types — 11 at v0.1; +`bridge_assertion` R2-8, +`mint_receipt` R2-7; +`contest_event`, +`migration_receipt` at the R2-2 landing; +`lifecycle_event`, +`binding_event`, +`authority_epoch_event` at the round-4 / `v0.3-candidate` landing)

**ROUND 4 — `v0.3-candidate` (ROUND3_CHARTER.md §11, eight items; `WP3_LEDGER_DESIGN.md` §2b):**
the frozen `+38` could not carry five facts append-only and left two references untyped; the
enforcement design routed them here rather than working around them. **`lifecycle_event`**
(`lce:<ulid26>`; §3.27 — `materializer_decommissioned` | `materializer_superseded`, the latter
with `superseding_version_id` naming a version of ANOTHER materializer; one EFFECTIVE supersession
per materializer, ledger-enforced) · **`binding_event`** (`bev:<ulid26>`; §3.28 — `opened` |
`closed` on a `binding_id`: a close is an EVENT, never a mutation of the row) ·
**`authority_epoch_event`** (`aep:<ulid26>`; §3.29 — `opened` | `closed` per `authority_id`, a
TOTAL state machine; the source of truth §5's audit lacked) · **`supersedes`** (backward) on
`identity_relation` and `bridge_assertion` — the new head names its predecessor; `superseded_by`
stays in the catalog as a field the ledger REFUSES on any write after creation and populates only
as a derived projection (likewise `materializer.superseded_by_version`) · **`contest_event.target_kind`
widened to `lifecycle_event`** with `target_event_id` (§3.20; the correction path for a mis-typed
process supersession — an `upheld` contest names exactly ONE replacement of the same kind and
serial, R3-CVO-12) · **`consequence_refs[]` TYPED** as a record-id union (`rel` | `bind` | `bev` |
`ctev` | `lce`) · **`migrated_record_ref` TYPED** over the whole catalog's id prefixes.

`entity` · `entity_binding` · `state_observation` · `identity_relation` · `materializer` ·
`materializer_version` · `materialization_run` · `source_frontier` · `surface_version` ·
`coherence_evaluation` · **`contest_event` (R2-2 3b/RA-1 — contests are their own record with a
TYPED target, an `opened`/`resolved` pair keyed by `contest_id`; §3.19–3.21; id space
`ctev:<ulid26>`, contest id `ct:<ulid26>`)** · **`migration_receipt` (R2-2 3a / CRO input 5 /
AT-1 — the append-only carrier of every vocabulary rewrite; §3.23; id space `mig:<ulid26>`)** ·
**`bridge_assertion` (R2-8 — the first load-bearing consumer, landed
per the ruled either-in-this-boundary-or-freeze-together condition).** Identity mechanisms per the
ratified table (minted serials for enduring mutables; content-addressing legal for immutable
observations/versions/receipts). `bridge_assertion` id space: `br:<ulid26>`. **`mint_receipt` (R2-7, 12th type)** — LAW 1's
compensating control DEFINED: every mint emits a receipt carrying `serial_form:
ulid26_lowercase_v1` (F6's normalization as a const a consumer can reject on),
`collision_preflight` (`checked_unique -> evidence_refs REQUIRED` | `deferred_to_reconciliation`
— the ratified cross-fabric provisional path), authority + fabric (execution family). ⚠ HONESTY
CLAUSE: the record type exists and validates; ENFORCEMENT that every mint actually emits one is
the ledger's (WP-3) — sec 5/sec 6 limit 1 wording updated to "control DEFINED, enforcement
deferred", which is a smaller hole than "control undescribed".

**CV-1's CARRIED REQUIREMENT IS LANDED, not carried:** `registry_standing = admitted ->
evidence_refs` is a schema arm with its mutant — a parse-generated candidate structurally cannot
reach `admitted` without evidence. The record also lands, AT BIRTH rather than by retrofit: F1's
held-names-its-item (`held -> held_on`), F2's value-carries-its-owner (`inadmissible ->
store_owner`), the rejection warrant (`rejected -> adjudicated_by`) with its candidate forbid
mirror, DT-R2-2's shared-enum propagation (three claim_origin values -> evidence on THIS consumer
too), the verification warrant set, CVO-75229 condition 3's schema-expressible half (a
symbol-plane bridge REQUIRES firm_scope), `declared_cardinality`
(`function|cover|partial_function|unknown` — DEC-02's evidence field), and the self-bridge
semantic arm. UNREACHED VALUES, deliberate and adjudicated at the ARM-4 pre-landing run:
`retired` (terminal, no obligations), `producer_declared` (needs no external warrant by
definition), `human_adjudicated` (traced by the CVO rubric per the standing carry, not by schema),
`unverified` (the honest free cell). **Every ARM-1 candidate at the round-2 boundary (13 values
across 9 fields) is disposed by id in `ARM1_ADJUDICATION.md`** — 2 CUT (§3.5 `open`, §3.6
`partial`), 1 DEFERRED BY LANDED DESIGN (§3.5 `disputed`), 10 NO with the citation each rests on.

## 3. ENUM RECORDS — full five-label form (F3), with CONDITIONAL-ARM TABLES where arms exist (CV-6)

Per CV-6 (adopted into the CVO certification bar): a four-postulate record for a conditional-bearing
enum carries a **CONDITIONAL-ARM TABLE** — per arm, the moving remedy and its OWNER — and the
battery holds one negative mutant per then-arm plus positive coverage per accepting branch.
**Postulate (iv) binds CONDITIONAL COVERAGE, not only value lists** (DT-1's generalization): the
uncovered-member hunt runs on the set of values each conditional reaches, not only on the domain.

### 3.1 `claim_origin` — `producer_declared | independently_observed | rule_derived | model_inferred | human_adjudicated`
DOMAIN: how an assertion entered the record. MECE: hunted members — store-declared →
`producer_declared`; legacy-import → `rule_derived` (migration map cited in evidence). GRAIN:
assertion. INTENT: origin only — never quality (that is verification_standing; the split is the
point). STATE-COHERENCE: origin is immutable; no remedy moves it.
ARM TABLE: `independently_observed -> evidence_refs required` (owner: the asserting seat; remedy:
supply the observation refs or do not claim independence). **R2-3: this arm now binds EVERY
consumer of the enum** -- identity_relation AND entity_binding (`binding_basis`); an arm that binds
one consumer of a shared enum and not another is the obligation-propagation gap COO~X named at
76588.

### 3.2 `verification_standing` — `unverified | corroborated | contradicted` (R2-2 LANDED: `superseded` LEFT the axis)
DOMAIN: epistemic standing of an assertion — the PURE epistemic axis. MECE over check-states; hunted
members: partially-checked → stays `unverified` (a partial check that upgrades standing is the F5
defect); superseded → NOT A VALUE: supersession is TEMPORAL and is carried by `superseded_by`
PRESENCE on the old record (CVR2-2's laundering cell: as a value, `contradicted -> superseded`
erased the contradiction from the current-value view; as a field, `contradicted` + `superseded_by`
is EXPRESSIBLE and the epistemic history survives the temporal event). GRAIN: assertion.
INTENT: one axis — has a check run and what did it say. STATE-COHERENCE: `unverified→corroborated`
moves by RUNNING A CHECK (asserting seat); `contradicted` is ENTERED on evidence (checker) and
LEFT only by SUPERSESSION — a NEW assertion carrying its own standing, evidence and `asserted_by`,
with `superseded_by` set on the old one; the contradicted record itself never changes (R2-2's
append-only path; DT-R2-6: the field form made candidate x contradicted uninhabitable on
bridge_assertion, and `4.0.0_SA_CRO~X` caught that the first re-recording cited `contest_resolved`,
whose targets are entities/bindings, never assertions — an impossible carrier). Under R2-2 this
axis is DERIVABLE-AT-WP-3 on both consumers (fold over the assertion chain; `status_basis`
declares it `authored` until then, §3.22).
ARM TABLE (F5): `corroborated|contradicted -> evidence_refs required` (owner: checker).
REMOVED at the R2-2 landing (checklist b): `superseded -> superseded_by required` on BOTH
consumers — the value is gone; the field stays; `superseded_by present -> no further standing
changes on THIS record` is DECLARED UNENFORCED pre-WP-3 (§6 limit 11). The identity_relation
`adjudicated_by` forbid arm SHRANK from {unverified, corroborated, superseded} to {unverified,
corroborated} with an explicit post-reduction mutant (`relation.corroborated-with-adjudicator`,
COO~X 77156's named trap). RETIRED (DT-R2-6, both consumers at once per DT-R2-2's shared-enum
rule): `contradicted -> adjudicated_by` — who overturned a contradiction is the `asserted_by` of
the superseding assertion, carried on the append-only path, not a field on the record it
overturns. ⛔ Evidence INDEPENDENCE is not schema-checkable — §6 limit 2.

### 3.3 `registry_standing` — `candidate | admitted | held | rejected | retired | inadmissible`
DOMAIN: lifecycle position in an admitting registry (bridges first). MECE: `inadmissible` ADDED at
the boundary (F2) — the structurally-ineligible relation (CVO-75229 condition-4 named gap) was
received by no value; a deliberate DEVIATION from the ruled five, recorded with this rationale.
GRAIN: registry row. INTENT: admission lifecycle — NOT epistemic quality (verification_standing)
and NOT origin (claim_origin). STATE-COHERENCE: per value -- `candidate` moves by evidence +
adjudication (registry); **`held` = ELIGIBLE, adjudication PAUSED on a NAMED item — owner: the
admitting registry; exits: admitted | rejected when the named item resolves; a held row with no
named item is malformed** (F1); `rejected` moves only by new evidence (re-candidacy); `retired`
moves nothing — terminal for a once-admitted row; **`inadmissible` — owner: the STORE OWNER, remedy:
store-side change; terminal for the registry, a NAMED GAP deliverable for the store** (different
remedy owner than `rejected`, which is why it cannot share a value). Parse-generated rows enter as
`candidate` and NEVER reach `admitted` without evidence (consuming half lands with BRIDGE_ASSERTION
— §2 carried requirement).

### 3.4 `entity.current_status` — `provisional | active | retired | contested`
DOMAIN: identity lifecycle of a minted serial. RENAMED at the boundary (F4): `candidate→provisional`
(cross-fabric mint awaiting reconciliation), `held→contested` (identity under adjudication) — the
two DIFFERENT-MEANING collisions with registry_standing eliminated; `retired` KEPT deliberately
(same sense both enums, and the ruled succession table's own word: 1→0 = Retirement). MECE: hunted
member — merged-away → `retired` + `canonicalized_as` set. GRAIN: entity. INTENT: identity
lifecycle. STATE-COHERENCE: `provisional` moves by reconciliation (minting authority);
`contested` moves by adjudication (named adjudicator); `retired` terminal; `active` degrades only
via succession relations.
ARM TABLE (batch 2; CRO~X synchronization finding): `contested -> adjudicated_by REQUIRED` (owner:
the adjudicator; the record carries WHO is adjudicating, and SHOULD carry `evidence_refs` for the
contest basis — evidence is recommended, not arm-required, because a contest can open before its
evidence is assembled and forcing it would manufacture prose). Cross-field semantic arm:
`canonicalized_as` set -> status must be `retired | contested` (a canonicalized entity is never
active/provisional).

### 3.5 `entity_binding.status` — `open | closed | disputed`
DOMAIN: whether a source-native reference currently denotes the entity. MECE: hunted member —
never-valid (a binding minted in error) → `closed` with `valid_to = valid_from` and evidence.
GRAIN: binding row. INTENT: interval state. STATE-COHERENCE: `open→closed` moves by the observed
rebind/disappearance (observer); `disputed` moves by adjudication; `disputed` MAY carry
`valid_to: null` (still open, contested) — deliberately unconstrained (DT-4 carve-out).
ARM TABLE: `closed -> valid_to nonempty` (DT-4; owner: the closer — a close without an instant is
the mutation LAW 3 forbids wearing the close's label) · `open -> valid_to null` (ARM-1 cut 1,
`ARM1_ADJUDICATION.md`; owner: the writer — an open binding carrying an end instant is a closed
binding wearing open's label, the mirror of DT-4; `disputed` deliberately unconstrained, its
overlay dissolves into the typed contest record at the R2-2 landing).

### 3.6 `observation_failure_state` — `observed | observed_absent | partial | substrate_unavailable | instrument_error | not_applicable`
DOMAIN: what the instrument could see. MECE — `observed_absent` ADDED at R2-5 (the GPT review's
item): a SUCCESSFUL observation whose finding is ABSENCE, distinct by construction from
`substrate_unavailable` (could not look) and from `not_applicable` (no question) — the
nerves_resolve two-state collapse closed on its THIRD face; a resolver's honest "I looked and it
is not there" finally has a first-class cell. GRAIN: observation. INTENT: instrument
outcome. STATE-COHERENCE: `substrate_unavailable` moved by repairing SUBSTRATE (store owner);
`instrument_error` by repairing the INSTRUMENT (tool owner); `partial` by widening the observation
(observer); `observed_absent` moved only by the referent APPEARING (a NEW observation — the record
itself is terminal, LAW 3); different owners, named.
ARM TABLE (DT-1 closed the `partial` hole): `observed -> all three fingerprint fields required`
(owner: observer) · `substrate_unavailable|instrument_error|not_applicable -> ALL THREE fingerprint
fields FORBIDDEN` (DT-5 — a failed instrument may not carry a value OR the metadata claiming a
method ran) · `partial -> fingerprint OPTIONAL but the three-field coupling binds via
dependentRequired` (partial legitimately fingerprints what it could see — WITH its method and
normalization, per the CRLF law) **+ `evidence_refs` REQUIRED** (ARM-1 cut 2,
`ARM1_ADJUDICATION.md`; owner: observer — a partial observation names what it could NOT see;
partial-without-warrant is indistinguishable from `observed` with a field missing, the same
unfalsifiable cell `observed_absent` was given a warrant for) · `observed_absent -> fingerprint triple FORBIDDEN (nothing to
hash) + evidence_refs REQUIRED` (owner: observer — an absence claim carries the warrant of WHERE
it looked, because absence-without-warrant is exactly the unfalsifiable cell every census defect
this directive found has hidden in).

### 3.7 `referent_scope` — `fabric_invariant | fabric_local | device_local` (R2-1; supersedes `fabric_scope`)
DOMAIN: the locality the REFERENCED STATE claims (never where the act ran — that is the execution
family). MECE: `fabric_local` ADDED (GPT review) — the round-1 hunted member
"fabric-scoped-but-multi-device" now has its cell instead of an out-of-scope note. GRAIN:
referent, per record (entity_binding + state_observation + **every `source_frontier` entry** —
round 3 R3-CRO-6: a consumed device-local source that cannot name its device is the Rule-26 hole at
the frontier grain; runs carry NO referent scope — an event has a location, not a locality claim).
INTENT: Rule 26 locality of the referent, one axis.
STATE-COHERENCE: structural classification, no remedy axis.
ARM TABLE (two-directional BY IDIOM): `fabric_invariant -> referent_fabric_id AND
referent_device_id FORBIDDEN` · `fabric_local -> referent_fabric_id REQUIRED, referent_device_id
FORBIDDEN` · `device_local -> both REQUIRED` (owner: the writer; a scope claim carries exactly the
keys its locality needs, no more).

### 3.8 `materializer.current_status` — `active | superseded | retired | unknown`
DOMAIN: standing of a logical process identity. MECE: `unknown` is the honest cell (L0's own
`materializer_standing` lesson — `historical_in_use` maps to `active` + a consumer relation, not a
status; the consumer relation is WP-3's). GRAIN: materializer. INTENT: process lifecycle.
STATE-COHERENCE: `unknown` moves by READING THE CODE (any seat); `superseded` by a successor version
landing (owner); `retired` by decommission (owner) — named per L0's postulate-(iv) critique.
ARM TABLE (R2-3, COO~X 76588): `superseded -> superseded_by_version REQUIRED` (matv id, new field)
— the 3.16 allowlist admits the `superseded` collision as SAME SENSE, and same sense carries the
same obligation: a superseded thing names its successor, in every enum that says the word.

### 3.9 `run_status` — `running | succeeded | failed | partial`
DOMAIN: outcome of one execution. MECE: hunted member — cancelled → `failed` with evidence at v0.1
(declared, not silently folded). GRAIN: run. INTENT: execution outcome. STATE-COHERENCE: `running`
moves by the execution completing (executor); `succeeded`/`failed` are terminal for the run record
(a re-run is a NEW run, never a mutation — LAW 3); `partial` moves only by a successor run.
ARM TABLE (CV-4): `running -> completed_at null` · `succeeded|failed|partial -> completed_at
required` (terminal states carry their instant). ⛔ EMISSION POSITION, declared (DT run-status set):
a `failed` run MAY declare outputs (partial emission is real) and a `succeeded` run MAY declare none
(a verified no-op is real) — DELIBERATELY unconstrained; a consumer needing emission guarantees
reads the run receipt, not the status.

### 3.10 `bundle_completeness` — `complete | partial` (R2-2 LANDED: `partial_legacy` RETIRED, 3d split)
DOMAIN: DEGREE of pin completeness of a materializer version's execution bundle — degree ONLY.
MECE: complete | partial spans the degree axis; the CAUSE of partiality (legacy or otherwise) is
NOT a value here (CVR2-2's intent fusion, Rule 24(iii)): the WHAT lives on `absent_components[]`
+ `evidence_refs`; the legacy WHY is PROVENANCE, an event-layer fact carried by the
`migration_receipt` that rewrote `partial_legacy -> partial` (source value preserved verbatim
there — AT-6's "cause preserved" has its slot, and it is not on this record by design). GRAIN:
version. INTENT: pin completeness (degree). STATE-COHERENCE: `partial` moves by reconstructing
the absent components (owner: the pinning seat) — or never, honestly.
ARM TABLE: `complete -> all six bundle digests required` · `partial -> absent_components
required, minItems 1` (honesty is a conditional, not prose) · FORBID `absent_components` on
`complete` (ARM-4 cut 3). Positive coverage: BOTH arms carry fixtures (DT-6 closed the
complete-arm zero-coverage hole); the rewrite carries fixture `migration_receipt`.

### 3.11 `identity_scope` — `logical | fabric_instance | device_instance | run_occurrence`
DOMAIN: the scope at which an identity claims uniqueness. MECE: account-scoped → `logical` (the
account lives in the native key). GRAIN: entity. INTENT: identity locality. STATE: structural, no
remedy axis.

### 3.12 `relation_type` — `candidate_equivalence | canonicalized_as | merged_into | split_from | successor_of | replaces | instance_of | retirement` (R2-2 LANDED: `retirement` ADDED, direction table CLOSED)
DOMAIN: identity-level links. MECE: over declared link kinds — hunted members: fabric INSTANCE_ON
(memoranda vocabulary) folds into `instance_of` (the record's fabric lives on the instance entity,
not the relation); ambiguous continuity is an OPEN `candidate_equivalence`, not a missing value;
ceased-with-no-successor (CRO input 4 / CVO AT-4) → `retirement`, a ONE-endpoint terminal event —
`object_serial` FORBIDDEN for that kind and REQUIRED for every other (two-directional; the
retirement REASON lives on this event's `evidence_refs`, never as prose on the entity — 3e —
**and the schema now says so: `retirement -> evidence_refs REQUIRED`** (round-3 REWORK-1,
`4.0.0_SA_CRO~X` at bf6fbe53d9: a `producer_declared` retirement with no evidence validated while
this sentence said both paths carry evidence — the sentence was prose; mutant
`relation.retirement-without-evidence`).
**DIRECTION TABLE (RA-3, RA-5 — CLOSED over the vocabulary; a new kind lands WITH its row or it
does not land):** which party CEASES per kind —
| kind | ceases | why |
|---|---|---|
| `merged_into` | SUBJECT | A merged into B retires A |
| `replaces` | OBJECT | A replaces B retires B |
| `successor_of` | OBJECT | A successor-of B retires B |
| `canonicalized_as` | SUBJECT | the contract's own semantic arm (§3.4: canonicalized_as set -> retired\|contested): after adjudication the subject RETIRES into the canonical target, its serial persisting as a resolvable alias (non-destruction law), never as an active identity — RA-5 overturned the draft's NEITHER |
| `retirement` | SUBJECT | the one-endpoint terminal event |
| `split_from` · `instance_of` · `candidate_equivalence` | NEITHER | topology, not succession |
`retired` (entity) derives from `retirement` OR from occupying the ruled CEASING endpoint of a
directional relation; both paths carry `evidence_refs` (DERIVABLE-AT-WP-3; `authored` until then).
Succession INTERPRETATIONS are DERIVED from predecessor/successor cardinality (ruled) — deliberately not an enum, so ambiguity cannot be forced at write time;
ambiguous continuity = an open `candidate_equivalence`. GRAIN: serial-pair. INTENT: identity
topology. STATE-COHERENCE: relations are append-only; `superseded_by` is the only forward pointer.
⛔ SELF-LOOPS are rejected by the validator's SEMANTIC arm (DT-2b): a 1→1 self-merge would be READ
AS A CONTINUATION by the ruling's own cardinality derivation — a lying record the architecture
itself would interpret; the schema cannot compare two fields, the validator can and does.

### 3.13 `target_policy` — `latest_authority | declared_release | as_of_frontier | historical_replay` (round 3, R3-CRO-11: `latest_authority` RESOLVES)
ARM TABLE (two-directional, added R3-CRO-11): `latest_authority -> resolved_target_ref +
resolved_target_version REQUIRED` (the head the evaluation actually compared against — a verdict
against "latest" with no resolved head is not reproducible) · `declared_release | as_of_frontier |
historical_replay -> both FORBIDDEN` (the target IS the ref; a resolution field on a pinned target
is a second carrier that drifts). Mutants `coherence.latest-without-resolved-head`,
`coherence.declared-release-with-resolved-head`; fixture `coherence_evaluation_latest`.
DOMAIN: what a coherence evaluation compares against. MECE over target choices; kills the
false-stale class ("behind" exists only relative to a DECLARED target). GRAIN: evaluation. INTENT:
comparison frame. STATE: structural.

### 3.14 The five coherence axes (per-axis enums, deliberately not collapsed — different owners/remedies)
`availability` `available|partial|unavailable` (remedy: restore access — owner: surface holder) ·
`integrity` `verified|mismatch|unverified` (remedy: run the check — checker; `mismatch` moves by
re-materialization — producer) · `currency` `at_target|behind_target|ahead_of_target|unknown`
(remedy: rebuild against target — producer; `unknown` by resolving the target — evaluator) ·
`provenance` `complete|incomplete|unresolved` (remedy: recover the frontier — producer) ·
`fabric_validity` `valid_for_fabric|foreign_fabric|unknown` (remedy: re-derive on the owning fabric
— Rule 26). ARM TABLE (CV-3): `integrity verified|mismatch -> evidence_refs required` · `mismatch
-> delta_summary required` · `currency at_target|behind_target|ahead_of_target -> evidence_refs
required`. `unknown`/`unverified` FREE OF REQUIRED WARRANTS by design — no arm may DEMAND evidence
or a delta from a seat that has not checked. FORBID (ARM-4 CUT #4): `integrity verified|unverified
-> delta_summary forbidden` — a delta is the product of the check; `verified` denies a delta and
`unverified` denies the check (its remedy column: "run the check").

### 3.15 Registered vocabularies — `entity_class`, `identity_space`, `identity_policy` (DT-3)
NOT closed enums. ⛔ OPENNESS IS DECLARED (it was previously only implied): the schema accepts any
non-empty string; membership is checked against `vocab/entity_classes.json`,
`vocab/identity_spaces.json`, `vocab/identity_policies.json` — **WARN at v0.1, not reject**, so a
typo is VISIBLE without closing the domain. An ADDITION is a registry-file commit carrying its
four-postulate record — the Rule 24 gate now has a diffable mechanical half. `identity_policy`
joined this remedy at CV-2 (a reference field with no referent artifact is "a value needs a whole
PATH, not a slot").


### 3.16 Cross-enum token collisions — the ALLOWED list and its gate (F4 + COO~X probe 2)
The collision census runs over ALL 18 enum domains (3 hoisted + 15 inline — round 1's census of 10
had the WRONG DENOMINATOR, found by its own author's tool). A collision passes ONLY via the
ALLOWED list with a stated same-sense reason. ALLOWED at v0.1: `retired` (same sense, ruled at F4);
`partial` (same sense — "some, not all, of the expected whole" — applied to instrument/run/surface;
the REMEDIES differ per §3.6/3.9/3.14 arm tables, which is where the difference belongs);
`unknown`, `active`, `complete`, `unverified` (same epistemic/lifecycle sense per
pair — `unknown`'s entry now spans THREE domains with declared_cardinality added, same sense in
all; **`superseded` LEFT the list at the R2-2 landing: it now lives in ONE domain only
(`materializer.current_status`), so it no longer collides — the census reads 6 collisions, 6
allowed, down from 7; `partial` gained `bundle_completeness` as a fourth same-sense domain when
`partial_legacy` retired; **`opened`, `closed` ADDED at round 4 / `v0.3-candidate`: the same
event-pair sense — the two halves of an interval's life — in `contest_event.event_kind`
(`opened | resolved`, one shared token), `binding_event.event_kind` and
`authority_epoch_event.event_kind` (`opened | closed`); the REMEDIES differ per §3.19/3.28/3.29
owner rows, which is where the difference belongs;** remedy divergence lives in each enum's state-coherence record — and per CVR2-2, `unknown`'s
entry carries a grain note: same sense, DIFFERENT grain-legitimacy — observer-state is coherent at
observer grain (coherence axes) and mixed at subject grain (materializer status); the subject-grain
use dissolves under R2-2's derived-status work). ELIMINATED rather than
allowed: `candidate`, `held` (different meanings — renamed out at F4). The gate REFUSES any new
collision not on the list.

### 3.17 `declared_cardinality` — `function | cover | partial_function | unknown`
DOMAIN: the cardinality shape a bridge CLAIMS for its relation (one-to-one-parent vs overlapping
vs partial vs undetermined). MECE: hunted member — many-to-many → this is TWO bridges (one per
direction), declared rather than absorbed; `unknown` is the honest undetermined cell. GRAIN:
bridge assertion. INTENT: one axis — claimed relation shape (never VERIFIED shape: that is
`observed_cardinality`, a free measurement field beside it, and the pair is deliberately
typed-beside-measured with the CLAIM constrained and the OBSERVATION free). STATE-COHERENCE:
`unknown` moves by MEASURING (the asserting seat); a declared shape moves only by a SUPERSEDING
assertion (append-only, LAW 3); no single remedy moves all four — named. ⛔ FEEDS DEC-02: the
function-vs-cover census over admitted bridges is the evidence the 540 decision waits on.
NOTE (CVO~X certification finding, the record's own provenance): this enum was BORN WITHOUT this
record and invisible to the gates — the labels gate's denominator was a maintained count, stale
the moment the enum landed. The structural remedy (gates derive enum censuses FROM THE SCHEMA) is
routed to the gate owner; this record closes the instance.

### 3.18 `mint_receipt.collision_preflight` — `checked_unique | deferred_to_reconciliation`
DOMAIN: what the minting authority did about serial collision at mint time. MECE: hunted member —
checked-and-FOUND-colliding → not a receipt state; a collision aborts the mint (no receipt exists
for an unminted serial); declared rather than absorbed. GRAIN: one mint. INTENT: one axis —
preflight disposition. STATE-COHERENCE: `deferred_to_reconciliation` moves by the reconciliation
running (minting authority of the primary fabric); `checked_unique` is terminal for the receipt
(append-only). ARM TABLE: `checked_unique -> evidence_refs REQUIRED` (owner: the minting seat —
a uniqueness claim carries its scan) · `deferred` needs no warrant (the deferral IS the honest
state, and the reconciliation record carries its own). Born WITH this record — the
declared_cardinality lesson (CVO~X's CV-1 finding) applied at the next enum's birth.

### 3.19 `contest_event.event_kind` — `opened | resolved` (R2-2 LANDED, 3b)
DOMAIN: the two events of a contest's life; a contest is an EVENT PAIR keyed by `contest_id`, never
a lifecycle value that displaces the interval truth (3b). MECE: hunted member — withdrawn → a
`resolved` with `outcome: dismissed` (the opener's withdrawal is a dismissal on the record, not a
third kind); re-opened → a NEW `contest_id` (append-only; a contest is never re-mutated). GRAIN:
one event. INTENT: one axis — which half of the pair. STATE-COHERENCE: `opened` is terminal for
its record; the contest MOVES by a `resolved` event with the same `contest_id` (owner: the
adjudicator) — the projection rule is a pure fold (contested/disputed iff an opened id has no
resolved partner; `upheld` keeps the subject contested until its `consequence_refs` EXIST).
ARM TABLE (two-directional): `opened -> basis + evidence_refs REQUIRED; outcome, adjudicated_by,
consequence_refs, surviving_contest_id FORBIDDEN` (owner: the opener; `surviving_contest_id` added
to this table at R3-CVO-3 — the schema forbade it from REWORK-2, the table had not said so) ·
`resolved -> outcome + adjudicated_by REQUIRED`
(owner: the adjudicator; `basis` may be restated — harmless surplus, class A).

### 3.20 `contest_event.target_kind` — `entity | binding | lifecycle_event | binding_event | authority_epoch_event` (R2-2 LANDED, RA-1; `lifecycle_event` ADDED round 4 item 8, R3-CVO-12; `binding_event`, `authority_epoch_event` ADDED at round 4's second pin, R4-CRO-2)
DOMAIN: what a contest is ABOUT. MECE: the two mutable identity carriers, plus EVERY event carrier
the round introduced — each is terminal and authoritative, and a mis-typed event on any of them
would force a rewrite, the one thing the ledger never does (R4-CRO-2 closed the doctrine over all
three; a carrier that could not be contested was the hunted member); an assertion is NEVER a target
(assertions are left by supersession on their own chain — §3.2, `supersedes` since round 4); a
surface contest → out of scope at v0.3 (declared, not absorbed). GRAIN: one event. INTENT: one
axis — target type. STATE-COHERENCE: structural; no remedy moves it.
ARM TABLE (five-directional, exactly-one target field): `entity -> target_entity_serial REQUIRED;
target_binding_id, target_event_id FORBIDDEN` · `binding -> target_binding_id REQUIRED;
target_entity_serial, target_event_id FORBIDDEN` · `lifecycle_event | binding_event |
authority_epoch_event -> target_event_id REQUIRED with the kind's prefix (`lce:` | `bev:` | `aep:`);
target_entity_serial, target_binding_id FORBIDDEN` (owner: the writer — the identity_relation
grain is a serial PAIR and cannot name a binding or an event, which is why contests are their own
record shape). An `upheld` contest on an event names exactly ONE replacement (schema: `maxItems 1`,
the kind's prefix) of the same `event_kind` and the same CARRIER KEY — `materializer_serial` |
`binding_id` | `authority_id` — with a NEW id (validator semantic arm, batch-scope; ledger rows
4/6/7/13 beyond it); VOIDED is derived only from that, and a voided event advances no machine and
feeds no fold. CHRONOLOGY (R4-CRO-5): `opened` < `resolved` for one `contest_id`, and the target
event < the `opened` that challenges it, in the order `(occurred_at, commit_seq, id)` — a same-instant
pair is decided by the id, deterministically.

### 3.21 `contest_event.outcome` — `upheld | dismissed | merged` (R2-2 LANDED, RA-2)
DOMAIN: how a contest resolved. MECE: the challenge stood (`upheld`), fell (`dismissed`), or was
absorbed into another contest (`merged` — the survivor named by the typed `surviving_contest_id`
field, NEVER in `consequence_refs`; R3-CVO-3 caught this sentence still carrying the pre-REWORK-2
form beside a schema that forbids it). GRAIN:
one resolution. INTENT: one axis — verdict. STATE-COHERENCE: terminal for the event; `upheld`
moves the SUBJECT only when its referenced consequence exists (owner: whoever cuts the
consequence event — canonicalized_as / merged_into / binding close-rebind).
ARM TABLE (two-directional per value — round-3 REWORK-2, `4.0.0_SA_CRO~X` at bf6fbe53d9: the
first table omitted `merged` while the schema required an UNTYPED consequence for it, so a
survivor could be `not-a-contest-id`): `upheld -> consequence_refs REQUIRED, surviving_contest_id
FORBIDDEN` (RA-2: an upheld challenge without its consequence is a promise, and a projection that
clears on a promise re-opens the laundering cell at the contest door) · `merged ->
surviving_contest_id REQUIRED (typed `ct:<ulid26>`), consequence_refs FORBIDDEN` (the survivor
carries the consequences; a merge names exactly one surviving contest) · `dismissed -> BOTH
FORBIDDEN` (a dismissed challenge has no consequence and no survivor to name) · `opened ->
surviving_contest_id FORBIDDEN` (with the other resolution fields, §3.19). Mutants:
`contest.merged-without-survivor`, `contest.merged-with-consequence`,
`contest.upheld-with-survivor`, `contest.survivor-not-a-contest-id`. ⛔ DECLARED LIMIT (§6 limit 11): that the consequence is an event on the SAME
typed target dated AFTER the opening is a LEDGER check, not a schema arm.

### 3.22 `status_basis` — `authored | derived` (R2-2 LANDED, sec 2 / AT-2 / RA-4 / CRO input 2)
DOMAIN: the basis of ONE projected status axis on ONE record — a FIELD-SCOPED, EXACT-KEY map
(`additionalProperties: false`, every axis key REQUIRED) on the five status-bearing records / six
axes: `entity.current_status` · `entity_binding.status` · `identity_relation.verification_standing`
· `materializer.current_status` · `bridge_assertion.verification_standing` AND
`bridge_assertion.registry_standing`. MECE: a status is either a CLAIM by its author or a
DERIVATION from the event layer; hunted member — MIGRATED is `authored` + a `migration_receipt`
ref in `evidence_refs`, no third value (the receipt is the discriminator). GRAIN: one axis on one
record. INTENT: one axis — provenance of the projection. STATE-COHERENCE: `authored -> derived`
moves ONLY when WP-3's derivation rule for that axis lands as code (owner: the ledger) — ⛔
`derived` is ILLEGAL pre-WP-3 and the schema says so (`const: authored` per key): a one-value enum
by construction (AT-2), whose live bit is VINTAGE — and vintage is NOT inferred from absence
(RA-4): post-landing a record WITHOUT the map is INVALID, and a pre-landing record is one the
MIGRATION MANIFEST enumerates (`migration/R2_2_MIGRATION_MANIFEST.json`, cut at this landing:
0 production records, 1 fixture rewrite). Two declared axis classes (AT-5): five DERIVABLE-AT-WP-3;
`bridge_assertion.registry_standing` ADJUDICATION-CARRIED (moves only on an adjudication event
carrying `adjudicated_by`; permanent-authored until that event vocabulary lands, declared).
ARM TABLE: the map is REQUIRED on all five records (mutant `entity.no-status-basis`), exact-keyed
(`bridge.status-basis-partial-map`, `binding.status-basis-extra-key`), authored-only
(`entity.status-basis-derived`).

### 3.23 `migration_receipt.recoverability` — `recovered | floor` (R2-2 LANDED, 3a / CRO input 5 / AT-1)
DOMAIN: what a vocabulary rewrite could recover. MECE: the pre-rewrite meaning was recoverable and
the target carries it (`recovered`), or it was not and the target is the declared honest floor
(`floor` — e.g. `superseded -> unverified + superseded_by`). GRAIN: one rewrite of one field on one
record. INTENT: one axis — recoverability. STATE-COHERENCE: append-only, terminal; a second
migration is a second receipt. The receipt preserves `source_value`, `target_value`, the map and
its evidence — a migration that erases what a value used to say is the laundering defect performed
by the remedy (CRO input 5); and the rewrite IS a status change in a kernel whose thesis is
a-change-is-an-observation, so a rewritten standing carries `claim_origin: rule_derived` with the
map in `evidence_refs` (AT-1), making a migrated value DISCRIMINABLE from a virgin one. ARM TABLE:
no conditional — every field REQUIRED (`evidence_refs` included: mutant `mig.missing-evidence`).

### 3.24 `source_frontier.completeness` — `complete | partial` (round 3, R3-CRO-8)
DOMAIN: whether the frontier accounts for every source the run EXPECTED. MECE: a frontier either
carries every expected coordinate (`complete`) or fewer (`partial`); the denominator is
`expected_count` (REQUIRED on both values — a partial frontier that cannot say how partial is the
adjective this record exists to retire). Hunted member — "unknown expectation" → the writer names
the count it ran with; a run with no expectation is a run with no frontier. GRAIN: one frontier.
INTENT: one axis — accounting completeness (never data quality). STATE-COHERENCE: `partial ->
complete` moves by a NEW frontier (append-only; LAW 5) when the absent source appears — owner: the
frontier writer (the run's executor). ARM TABLE: none conditional (`expected_count` unconditional);
SEMANTIC, BOTH DIRECTIONS (R3-CVO-4 caught the first cut constraining `complete` only — `partial`
was a costume state): every frontier REQUIRES `expected_count >= len(entries)`
(`sem.frontier-overfull-denominator`) · `complete` REQUIRES `expected_count == len(entries)` AND no
`unavailable` entry (`sem.frontier-complete-count-mismatch`, `sem.frontier-complete-with-unavailable`)
· `partial` REQUIRES something to be missing: `expected_count > len(entries)` OR at least one
`unavailable` entry (`sem.frontier-partial-costume`); positive controls: `source_frontier_partial`
(absent by unavailability), `source_frontier_partial_short` (absent by count).

### 3.25 `source_frontier.entries.availability` — `available | unavailable` (round 3, R3-CRO-8; the entry-level field `availability` — named without `[]` because the labels gate's header regex `[a-z_.]+` cannot see brackets, which made this record INVISIBLE to the gate at c3ead58283 while the commit body claimed "23 of 23": the gate's blind spot and the typed number, both on the record)
DOMAIN: whether the source at this coordinate could be read when the frontier was compiled. MECE:
read (`available`, carries `source_version`) or not (`unavailable`, PRESENT with its
`absence_evidence` — the source does not disappear from the vector, R2-5's rule at the frontier
grain). Hunted member — partially readable → `available` with the partial version named; the
degree lives on the observation, not here. GRAIN: one entry. INTENT: one axis — readability at
compile time. STATE-COHERENCE: `unavailable -> available` moves by a NEW frontier (owner: the
writer). ARM TABLE (two-directional, entry-level — invisible to ARM 1/4, which read record-level
arms only; declared): `unavailable -> absence_evidence REQUIRED` · `available -> absence_evidence
FORBIDDEN`. Entry locality (R3-CRO-6): every entry carries `referent_scope` with the §3.7
two-directional fabric/device arms — a device-local path with no device key is unrepresentable.

### 3.26 `surface_version.publication_state` — `unpublished | published` (round 3, R3-CRO-10)
DOMAIN: whether this immutable surface has been PROMOTED to an authority ref. MECE: a surface is
built (always) and either promoted or not; `published_ref` alone was a bare string that could be
set on a failed run's output (CRO's exhibit). Hunted member — "promoted then withdrawn" → a NEW
surface_version or a retirement on the authority, never a mutation (LAW 3). GRAIN: one surface
version. INTENT: one axis — promotion state. STATE-COHERENCE: `unpublished -> published` moves by
the PROMOTER (owner: the authority holder, e.g. the deploy lane) with a receipt. ARM TABLE
(two-directional): `published -> published_ref (nonempty) + published_at + promoted_by +
promotion_evidence_refs REQUIRED` · `unpublished -> published_ref REQUIRED AND null, the three
FORBIDDEN` (R3-CVO-5: the first cut pinned `published_ref` to null only IF PRESENT, so the declared
null carrier could vanish; mutant `surface.unpublished-without-published-ref`).
SEMANTIC (batch): a published surface's producing run must be `succeeded` and `published_at >=
run.completed_at` (`sem.published-from-failed-run`, `sem.published-before-run-completed`).
Failed-with-outputs stays legal (§3.9); what is guarded is PROMOTION.

### 3.27 `lifecycle_event.event_kind` — `materializer_decommissioned | materializer_superseded` (round 4 items 3 + 4, R3-CRO-19 / R3-CVO-6)
DOMAIN: the two process-level transitions of a materializer that `+38` could only AUTHOR (§3.8
`retired`, `superseded` were authored values with no event to fold over). MECE: hunted members —
a version succession is NOT a lifecycle event (it is `materializer_version.supersedes`, same
materializer); a re-activation after decommission → a NEW materializer serial (append-only; a
decommission is terminal); a correction of a wrong event → a `contest_event` on it (§3.20), never a
second event. GRAIN: one event. INTENT: one axis — which transition. STATE-COHERENCE: each event
is terminal for its record; the materializer's `current_status` is a FOLD over its effective
events (`WP3_LEDGER_DESIGN.md` §4) — `retired` outranks `superseded`; the remedy for a wrong
event is the contest (owner: the adjudicator), for a wrong fold the ledger (owner: WP-3). **THE
MACHINE (R4-CRO-4), over EFFECTIVE events per `materializer_serial`:** at most ONE decommission;
NO effective transition ordered after it (decommission is TERMINAL); `superseded ->
decommissioned` is LEGAL; a voided event advances nothing and its upheld replacement takes its
position. Validator semantic arm in-batch (`_materializer_machine_errors`), ledger row 7 beyond.
ARM TABLE (two-directional): `materializer_superseded -> superseding_version_id REQUIRED` (a
`matv:` of ANOTHER materializer — same-materializer is rejected by the validator semantic arm
in-batch and by the ledger beyond) · `materializer_decommissioned -> superseding_version_id
FORBIDDEN` (owner: the writer). `evidence_refs` REQUIRED on both (an event with no warrant is an
opinion).

### 3.28 `binding_event.event_kind` — `opened | closed` (round 4 item 2, R3-CRO-19 / R3-CVO-6)
DOMAIN: the two halves of a binding interval's life, carried as EVENTS so a close never mutates
the `entity_binding` row (LAW 3). MECE: hunted members — disputed is NOT an event kind (it is a
contest on the binding, §3.20); re-opened → a NEW `binding_id` (the interval is a new assertion).
GRAIN: one event. INTENT: one axis — which half. STATE-COHERENCE: `entity_binding.status` is a
FOLD (`closed` iff a `closed` event exists for the id; `disputed` iff an open contest; else
`open`) — the row's authored `status` / `valid_to` must AGREE with the fold or the write is
rejected (WP3 row 5; owner: the writer for the row, the ledger for the fold). `opened` and
`closed` share the token sense of §3.29 (ALLOWED, §3.16). `evidence_refs` REQUIRED. **THE
MACHINE (R4-CRO-3), over EFFECTIVE events per `binding_id`:** the `entity_binding` ROW is the
initial open fact; an `opened` event is legal at most ONCE; a `closed` at most ONCE; no `opened`
ordered after a `closed` (the forbidden re-open on the same id — re-opening is a NEW
`binding_id`). A wrong event is corrected by a contest on it (§3.20), never by a second event;
its replacement carries the same `binding_id`. Validator semantic arm in-batch
(`_binding_machine_errors`), ledger row 4 beyond.

### 3.29 `authority_epoch_event.event_kind` — `opened | closed` (round 4 item 5, R3-CRO-30 / R3-CRO-34)
DOMAIN: the two transitions of a minting authority's epoch — the source of truth §5's audit and
§6 limit 1 lacked. MECE: hunted members — revoked IS `closed` (a revocation is a close with its
evidence); suspended → `closed` then `opened` (two intervals; reopening is legal); a rename of an
authority → a new `authority_id` (the id is the `minting_authority` string, verbatim). GRAIN: one
event. INTENT: one axis — which transition. STATE-COHERENCE: a TOTAL machine per `authority_id`
— start CLOSED; `opened` legal only from CLOSED, `closed` only from OPEN; ordered by
`(occurred_at, commit_seq, event id)`; mint AUTHORIZATION is evaluated at the mint batch's own
`commit_seq` and never re-opened by a backfilled event (WP3 row 6; owner: the ledger; the writer
owns the event's warrant). `evidence_refs` REQUIRED. **THE TRUST ROOT (R4-CRO-6, adjudicated
`3.0.0_SA_CVO~X` 20260828T054009Z): who may open or close an epoch is pinned IN THIS CONTRACT at
seat-FAMILY grain — `actor` matches `^(0\.0\.0_AB_MSTR|1\.0\.0_SA_CTO)(~[A-Z])?$` (the registry
owner and the contract author; a root rotation is a contract amendment = a new candidate_id with
`supersedes_bundle_id`, replayable through `BUNDLE_LABELS.json`, no new bundle member). That
regex is the STRUCTURAL half only — `actor` is authored data and a spoofed root string passes it;
the ledger binds `actor` EXACTLY to the AUTHENTICATED submitting principal and only then applies
the family predicate (WP3 row 6: `L-06-unauthorized-epoch-transition-rejected` and
`L-06-epoch-actor-spoof-rejected`; the accepts are the MSTR genesis-open and a CTO close /
re-open with actor == the authenticated writer). Declared here, enforced by the ledger; §6.** A
wrong epoch event is corrected by a contest on it (§3.20); its replacement carries the same
`authority_id`.

## 4. CONDITIONAL REQUIREMENTS (the consuming half — all mechanical)

The full set now spans: three-field fingerprint coupling (every direction, every failure_state) ·
hard-failure forbids all three fingerprint fields · observed requires all three · fabric_scope
arms on three record types (require AND forbid directions) · closed→valid_to ·
warrant conditionals on identity_relation (evidence/adjudicator/successor) · run terminal/running
completed_at arms · bundle_completeness both arms · coherence evidence/delta arms ·
`evidence_refs` minItems 1 ON THE $def (CV-5 — present means non-empty, no future conditional can
forget it) · `random_seeds` = non-empty list or literal `"not_applicable"` · frontier minItems 1 ·
iso_ts range-checked fields (CV-4; calendar validity beyond ranges: validator semantic arm, §6) ·
**R2-2:** `status_basis` exact-key maps REQUIRED on five records (`const: authored`) · contest
target-kind arms (both directions) + event-kind arms + outcome arms · `retirement` object_serial
forbid / other-kind require · `open -> valid_to null` + `partial -> evidence_refs` (ARM-1) ·
**round 4 / `v0.3-candidate`:** contest target-kind arms THREE-directional (exactly-one target
field, §3.20) · `lifecycle_event` kind arms (`materializer_superseded -> superseding_version_id`
require / `materializer_decommissioned` forbid, §3.27) · `evidence_refs` REQUIRED on all three
event records · `consequence_refs[]` items pattern-typed (record-id union, minItems 1) ·
`migrated_record_ref` pattern-typed over the catalog · `supersedes` pattern-typed per assertion
record (`rel:` / `br:`) · **round 4, second pin:** contest target arms FIVE-directional with a
per-kind `target_event_id` prefix (§3.20) · `upheld` on an event → `consequence_refs` exactly one,
the kind's prefix · `migrated_record_ref` also admits `sha256:<64hex>` (the two content-addressed
primary ids, R4-CRO-1) · `authority_epoch_event.actor` pattern = the root families (§3.29) ·
validator semantic machines: binding (§3.28), materializer lifecycle (§3.27), contest chronology
(§3.20), replacement same-carrier-key — all over EFFECTIVE (non-voided) events.

## 5. MINTING AUTHORITY (RATIFIED — Andrew-direct 2026-08-27 ~18:4xZ, "Recs approved")

Primary minting on the LAPTOP fabric. Other fabrics mint `entity.current_status: provisional`;
reconciliation is non-destructive via `candidate_equivalence` → (`canonicalized_as` | `merged_into`)
— historical observations NEVER rewritten. ULID per serial; **the minting act LOWERCASES the ULID
before prefixing** (F6) — a serial is born lowercase or it was not minted by the authority.
⛔ **LAW 1's COMPENSATING CONTROL: DEFINED at R2-7, ENFORCEMENT DEFERRED TO WP-3** (upgrading
CV-2's entry-5 finding from "undescribed"): the `mint_receipt` record type exists with its
serial-form const and collision-preflight arms; what WP-3's ledger adds is the guarantee that
every mint EMITS one. Until then a mint without a receipt is a process violation a certification
names, not a schema rejection.

## 6. DECLARED LIMITS — what v0.1 CANNOT enforce, so silence is never read as coverage

Classified per DT-2's taxonomy (genuinely-inexpressible vs deferred vs process-note):

1. **LAW-1 derivation-freedom — INEXPRESSIBLE** (confirmed by execution, CV-2/P2): the serial regex
   enforces shape; a derived value of the right length and alphabet passes. Control: the minting
   authority's audit — itself INCOMPLETE until WP-3 (§5).
2. **Evidence INDEPENDENCE — inexpressible in the SCHEMA, PARTIALLY MECHANICAL in the VALIDATOR**
   (RECLASSIFIED at round 2, CVR2-1 — the original "inexpressible" classification was wrong within
   this section's own taxonomy): the SYNTACTIC-IDENTITY subcase (evidence_refs that are entirely
   the record's own id / subject / source coordinates) is rejected by the semantic arm with
   both-direction mutants. ⛔ THE RESIDUAL IS STATED so the mechanical half is not read as the
   whole: an ALIASED or MIRRORED self-citation (same substrate under a different name) passes the
   syntactic check — semantic independence (does ref X genuinely support claim Y from a different
   substrate) remains the verifying seat's Rule 22 duty, un-mechanizable here.
3. **REFERENTIAL RESOLUTION — INEXPRESSIBLE at instance grain** (DT-2a): every `*_serial`/`*_id` is
   shape-checked, never resolved; a surface_version may cite three nonexistent records and
   validate. Resolution needs the ledger (WP-3).
4. **FIELD-PAIR COMPARISON — inexpressible in the SCHEMA, PARTIALLY MECHANICAL in the VALIDATOR**
   (DT-2b): self-loops, self-canonicalization, self-supersession, interval order, run time order
   are rejected by `validate_isck.py`'s SEMANTIC arm (batch or single-record where computable).
   The schema half is declared; the validator half is enforced and mutant-covered.
5. **SERIAL UNIQUENESS — batch-scope mechanical, ledger-scope deferred** (DT-2d): the semantic arm
   rejects duplicate serials within one validated batch; cross-batch uniqueness needs WP-3.
6. **LAW-3 APPEND-ONLY / CLOSE-NOT-MUTATE — NO ENFORCEMENT PLANE AT v0.1** (CV-2): the validator is
   stateless; a mutated record re-validates identically. The plane that could see mutation is the
   ledger (WP-3). ⛔ No v0.1-based certification can certify LAW 3; certification scopes name the
   exclusion.
7. **iso_ts CALENDAR VALIDITY** (CV-4): ranges are pattern-checked (month 01-12, day 01-31, time
   ranges); Feb-30-class dates pass the pattern and are rejected by the validator semantic arm.
8. **Vocabulary membership — WARN-not-reject at v0.1** (DT-3, deliberate): openness declared in
   §3.15; the gate hardens only by ruling.
9. **Run emission — DELIBERATELY UNCONSTRAINED** (§3.9): failed-with-outputs and
   succeeded-with-none are legal; the receipt carries emission truth.
10. **Rule 24 records are AUTHOR-side until certified** — PROCESS NOTE, not a limit (CV-2 entry-4
    reclassification): the adversarial pass + CVO certification are the check.
11. **R2-2's CROSS-RECORD PROMISES — NO ENFORCEMENT PLANE pre-WP-3, DECLARED (AT-1, RA-2 carry):**
    (i) `superseded_by present -> no further standing changes on THIS record` — a stateless
    validator cannot see a cross-version write; (ii) an `upheld` contest's `consequence_refs` must
    name an event on the SAME typed target dated AFTER the opening — referential + temporal, ledger
    grain (limit 3's class); (iii) a `resolved` event's `contest_id` must match an `opened` one —
    batch-scope at best. All three become REJECTED-WRITE rules when the ledger lands; until then a
    certification touching them names the exclusion. **Round 4 / `v0.3-candidate`:** (i) is now
    carried the other way round — the NEW assertion's `supersedes` (backward, resolvable at
    creation) is the authored fact and `superseded_by` is ledger-derived; (ii)/(iii) gain their
    carriers' typing (`consequence_refs[]` record-id union; `contest_id` semantics unchanged) and a
    third target kind (`lifecycle_event`, §3.20) whose upheld consequence is ONE replacement of the
    same kind + serial (validator semantic arm in-batch). The ledger-scope halves are `WP3_LEDGER_DESIGN.md`
    rows 7 and 13 — still declared here, not enforced by this validator.
12. **FRONTIER CANONICALIZATION — declared, PARTIALLY MECHANICAL (round 3, R3-CRO-5):** the writer
    supplies `canonical_key` under the frontier's `normalization_version`; the validator rejects an
    OBVIOUSLY non-canonical key (dot-segments, empty segments, trailing slash) and two entries
    sharing a `canonical_key` with different `source_version`. It CANNOT prove two syntactically
    different keys are the same source (that needs the normalizer itself, WP-3) — a mis-canonicalized
    key that happens to be well-formed passes. **Cross-batch provenance (R3-CRO-7/9/10)** — frontier
    observed-before-run-start, run<->surface membership + frontier identity, publication only from a
    succeeded run and after it completed — is enforced WITHIN A BATCH by `_batch_provenance_errors`
    and is ledger-scope beyond it (limit 3's class).

## 7. CHANGELOG v0 → v0.1 (finding → fix; full tally in BOUNDARY_ROUND1.md)

F1 held-undefined → §3.3/3.4 records with owners+exits · F2 uncovered member → `inadmissible` ·
F3 thin records → §3 full five-label form, 16 records · F4 + probe-2 collisions → renames
(`provisional`/`contested`) + §3.16 gate + ALLOWED list · F5 warrant-free standing → §3.2 arms in
schema · F6 case trap → §5 lowercase line · F7 battery drift-blindness → expected-reason
assertions + gutted-schema meta-control · DT-1 partial hole → global dependentRequired coupling ·
DT-2 undeclared inexpressibles → §6 items 3-5 + validator semantic arm · DT-3 vocab consuming half
→ `vocab/` registries + warn gate · DT-4 closed-no-close → binding arm · DT-5 metadata-without-
fingerprint → symmetric coupling + forbid-all-three arm · DT-6 complete-arm zero coverage → 11th
fixture · DT-7 invariant-with-fabric → forbid arm · DT-8 three models of locality → shared
`fabric_scope` on three records · CV-1 → §2 carried requirement · CV-2 → §5 control-incomplete +
§6 items 6/10 + identity_policy into §3.15 · CV-3 → coherence warrant arms · CV-4 → iso_ts ranges +
terminal-completed_at arm · CV-5 → minItems on the $def · CV-6 → arm tables throughout §3.

**v0.2-candidate, post-round-2-boundary (2026-08-28):** ARM-1 adjudication (`ARM1_ADJUDICATION.md`,
13 of 13 candidates disposed) → §3.5 `open -> valid_to null` arm + mutant `binding.open-with-valid_to`
· §3.6 `partial -> evidence_refs REQUIRED` arm + mutant `observation.partial-no-warrant` + 15th
fixture `state_observation_partial` · the new require-only arm is ruled class A in
`ARM4_ADJUDICATION.md` (26 of 26). Schema `$id` stays `v0.1` until the bundle-identity record
(Round 3 target) mints the candidate identifier — the label/bundle split is deliberate, not drift.

**R2-2 LANDED (2026-08-28, one commit; design @7c093caff5 attacked-dry; gate = COO~X census
77156; cut authorized by CVO~X's C2 verdict after ARM-1 @9869831971) — checklist (a)–(h):**
(a) `superseded` leaves `verification_standing` (§3.2, 3-value); `migration_receipt` record type
(§3.23) + `migration/R2_2_MIGRATION_MANIFEST.json` (0 production records, 1 fixture rewrite) ·
(b) both `superseded -> superseded_by` REQUIRE arms REMOVED; the identity_relation enum-set forbid
SHRANK with an explicit mutant (`relation.corroborated-with-adjudicator`); ARM-4 class-D rows
CLOSED · (c) `contest_event` record, typed target, total vocabulary (§3.19–3.21; 8 mutants) · (d)
`retirement` relation kind, `object_serial` forbidden for it / required otherwise (§3.12) · (e)
direction table CLOSED into §3.12 · (f) `status_basis` exact-key maps REQUIRED on five records /
six axes, `const: authored` (§3.22; 4 mutants) · (g) `partial_legacy -> partial` (§3.10) with its
receipt as fixture `migration_receipt` · (h) COO~X 77156 cited as the pre-landing gate that was
MET. Battery at the landing: 18 fixtures · 83 reason-asserted mutants (8 of them contest_event —
the commit body's "9" was a typed number, corrected by `3.0.0_SA_CVO~X`'s derivation) · 20 enum
records · collisions 6/6 allowed · ARM 4 21 live require-only, 0 NEW · ARM 3 103 of 103 inhabitable
(`4.0.0_SA_CRO~X` at the pin; the landing log's "96" was a pre-landing tree figure). §6 limit 11
declares the three cross-record promises the ledger must enforce.

**Round-3 REWORK at bf6fbe53d9 (`4.0.0_SA_CRO~X`, 20260828T024424Z; landed as the first round-3
commit):** REWORK-1 `retirement -> evidence_refs REQUIRED` (§3.12; the reason sentence was prose) ·
REWORK-2 `merged -> surviving_contest_id` typed `ct:` REQUIRED + `consequence_refs` FORBIDDEN;
`upheld` forbids the survivor; `dismissed` forbids both (§3.21 arm table re-recorded — it had
omitted `merged`). Register: `ROUND3_FINDING_REGISTER.json` R3-CRO-1..4, R3-CVO-1.

**SCHEMA-ONLY FREEZE — `v0.2-candidate+38` FROZEN (C4, `3.0.0_SA_CVO~X` 20260828T040820Z):**
`bundle_identity.py dcbe214a44 --freeze --boundary <BOUNDARY_ROUND3.md commit>` records
`frozen_at` + the round-3 boundary in `BUNDLE_LABELS.json`; `BUNDLE_IDENTITY.json` reads
`status: frozen`, `freeze_scope: schema-only`. **The three operational receipts stay null BY
DEFINITION** — that is "not operationally certified", not a contradiction (the record's earlier
comment said otherwise and was corrected in the same change). **The frozen label is immutable:**
any byte change on the package path derives a NEW `candidate_id`; the contract is never mutated
under `+38`. The freeze lifts ONLY WP-3 implementation start (`WP3_LEDGER_DESIGN.md`, design-first,
C5); production population and the 56 L3 cells stay HELD.

**ROUND 3 CLOSED — `BOUNDARY_ROUND3.md`, 2026-08-28 04:0xZ, boundary pin dcbe214a44 =
`v0.2-candidate+38` (`bundle:sha256:617fd9a1…`, `BUNDLE_LABELS.json`).** 30 findings registered
(`ROUND3_FINDING_REGISTER.json`), 21 FIXED, 7 AMENDED-RECORD, 2 REFUTED by named rule — one of them the
pre-declared planted claim (R3-CTO-2), refuted by the EXPECTED rule (CVR2-1) by two attackers
independently; specificity MEASURED, the margin (one first pass UPHELD on an instrument misuse, now
R3-CRO-16) on the record. Both attackers DRY. Gates at the pin: six of six exit 0 | 1 open (the class-D
`disputed` projection). **The contract is ELIGIBLE FOR CANDIDATE FREEZE** (memo §10 candidate-freeze
column met); **NOT operationally certified** — WP-3 ledger, live vertical slice, historical replay
remain. Later-round landings after the REWORK 5–11 entry below: R3-CVO-4/5 @ab052139a8 (partial
frontier both directions; unpublished requires the null carrier) · R3-CRO-16 @393c248a09 (validator
fails fast on a non-list) · consume-gate resolution arc @9b27b8c41e → f98f2d020b → 74671f0911 →
ea64a64850 (DT~X) · labels gate census @e54c9a0b9e (COO~X) · runner `ISCK_REPO_ROOT` @454781703a.

**Round-3 REWORK 5–11 (`4.0.0_SA_CRO~X` at 36a5514df8; landed as one commit):** `source_frontier`
gains `normalization_version`, `completeness` (§3.24) + `expected_count`; every entry gains
`canonical_key`, `availability` (§3.25) + `absence_evidence`, and `referent_scope` with the §3.7
fabric/device arms; the validator's coordinate key reads only schema-reachable fields (it read a
dead `fabric_id`); semantic: non-canonical keys, same-key-two-versions, complete-count mismatch,
complete-with-unavailable · `surface_version` gains `publication_state` (§3.26) with the
publication receipt fields · `coherence_evaluation` gains `resolved_target_ref/version` on
`latest_authority` (§3.13) · batch provenance: frontier observed-after-run-start, surface not in
run outputs, surface/run frontier disagreement, published-from-failed-run,
published-before-completion (`_batch_provenance_errors`; §6 limit 12). Battery: 21 fixtures ·
99 mutants · 20 semantic · 23 enum records. ARM 3 prints two OPEN companion repairs
(`latest_authority`, `published`) until `0.4.0_DT_ClientPlatform~X`'s next consume-gate commit
carries them (the probe module was under DT~X's announced lock at this landing — declared, not
hidden).

## 8. CHANGELOG `v0.2-candidate+38` → `v0.3-candidate` (ROUND 4 — chartered `ROUND3_CHARTER.md` §11 on `3.0.0_SA_CVO~X` 20260828T043852Z, self-drive D11 ledger row 12)

**Why:** the WP-3 enforcement design (`WP3_LEDGER_DESIGN.md`, attacked to its second quiet pin
30d9186e3b by CRO~X / CVO~X / DT~X) found five facts the frozen `+38` cannot carry append-only and
two references it left untyped (§2b there; R3-CRO-19, R3-CVO-6, R3-CRO-22, R3-CRO-30, R3-CVO-12).
Per C5's last sentence they land as a NEW candidate in a NEW family — `+38` is untouched.
**What (eight items):** (1) `supersedes` on `identity_relation` + `bridge_assertion` (§2; the head
names its predecessor) · (2) `binding_event` (§3.28) · (3)+(4) `lifecycle_event` (§3.27) · (5)
`authority_epoch_event` (§3.29) · (6) `consequence_refs[]` typed (§4) · (7) `migrated_record_ref`
typed (§4) · (8) `contest_event.target_kind` + `lifecycle_event` with `target_event_id` (§3.20).
**Identity:** `bundle_identity.py`'s family rule (ledger row 12) — a bundle whose schema blob
differs from the frozen `+38` schema derives `v0.3-candidate+N` (N = package-path commits since the
round-3 boundary) with `supersedes_bundle_id` → the `+38` bundle; a bound bundle keeps its label.
**Battery at the opening commit:** fixtures, mutants and semantic arms per the self-test's printed
denominators (never typed here); §3.16 ALLOWED gains `opened`, `closed`. **Round 4 rules:** §11 of
the charter — `R4-<seat>-<n>` ids, `round: 4` rows in `ROUND3_FINDING_REGISTER.json`, PINNED
declarations, the quiet pin. **Exit:** `BOUNDARY_ROUND4.md` + `--freeze` on the native label;
ledger code only after that AND the design's dry.
