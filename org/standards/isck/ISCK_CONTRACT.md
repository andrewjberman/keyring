# ISCK CONTRACT v0 — the Issue 3A Identity-State Contract (DRAFT)

**Authority:** Andrew ruling 2026-08-27 (ISCK adoption) —
`org/tier1_exec/1.0.0_SA_CTO/deliverables/D11_ISCK_RULING_20260827/RULING.md` @d869c9ffe0.
**Author:** `1.0.0_SA_CTO~X` · **Status: v0 DRAFT — NOT FROZEN, NOT RATIFIED.** This package is the
WP-2 starting draft; it closes only after adversarial schema validation by the fabric (the same
process that reworked the L0 contract seven times). Nothing populates production records against v0
until that pass lands and the version is pinned.
**Machine contract:** `ISCK_CONTRACT.v0.schema.json` (JSON Schema Draft 2020-12, one `$defs` entry
per record type). **Validator + mutant battery:** `validate_isck.py` (run it; PASS is printed with
its own denominator).

---

## 1. THE FIVE LAWS (from the ruling, stated as constraints a validator can hold)

1. **MINT, NEVER DERIVE.** An enduring mutable entity's serial is opaque and minted once. It is
   never computed from a path, ARN, anchor, parse, list position, or any substrate key. (Schema:
   serial patterns are `ent:`/`mat:` + 26-char ULID; nothing else validates.)
2. **HASH AT THE CORRECT GRAIN.** Hashes identify immutable things only: observations, versions,
   execution bundles, receipts. A fingerprint NEVER appears without `fingerprint_method` +
   `normalization_version` (the CRLF/LF law, now mechanical).
3. **A RENAME IS A BINDING EVENT; A CHANGE IS AN OBSERVATION; NEITHER TOUCHES THE SERIAL.**
   Bindings carry validity intervals and close rather than mutate. Succession/reconciliation
   relations are append-only.
4. **RULE 26 IS METADATA.** Every observation, run, and physical instance carries `fabric_id`
   (+ `device_id` where device-local). Logical surfaces and physical instances are SEPARATE
   entities joined by `instance_of` relations.
5. **PROVENANCE IS A FRONTIER, NOT A HEAD.** Every run consumes a `source_frontier` (a vector of
   source versions); every surface version pins the frontier and the materializer version that
   produced it. Coherence is evaluated multi-axis against a DECLARED target policy, emitted as an
   immutable record.

## 2. RECORD CATALOG (10 types)

| record | identity mechanism | what it is |
|---|---|---|
| `entity` | minted `ent:<ulid26>` | durable identity for any addressable entity class |
| `entity_binding` | minted `bind:<ulid26>` | temporal source-native reference to an entity |
| `state_observation` | `obs:<ulid26>` or `sha256:<hex64>` (immutable — content-addressing legal) | one measurement of entity state |
| `identity_relation` | minted `rel:<ulid26>` | append-only succession/alias/merge/split/instance link |
| `materializer` | minted `mat:<ulid26>` | durable logical identity of a transformation process |
| `materializer_version` | `matv:<ulid26>` + `bundle_digest` | immutable execution bundle |
| `materialization_run` | `run:<ulid26>` | one execution, one fabric, one frontier |
| `source_frontier` | `sf:<ulid26>` | immutable vector of source versions a run consumed |
| `surface_version` | `sv:<ulid26>` + `content_digest` | immutable output version of a logical surface |
| `coherence_evaluation` | `ce:<ulid26>` | immutable multi-axis alignment assessment (3B's record) |

## 3. ENUMS — each with its Rule 24 four-postulate record

Format per enum: **domain** (what population the values partition) · **MECE** (uncovered-member
hunt result) · **grain** · **intent** · **state-coherence** (which values one remedy does NOT move).

- **`identity_scope`** `logical | fabric_instance | device_instance | run_occurrence` — domain: the
  scope at which an entity's identity is claimed unique. MECE over declared scopes; hunted member:
  *account-scoped cloud identity* — folded into `logical` (the account is part of the native key,
  not the scope). Grain: entity. Intent: one axis, where-does-this-identity-live. State: not a
  state axis (structural classification; no remedy moves values).
- **`claim_origin`** `producer_declared | independently_observed | rule_derived | model_inferred |
  human_adjudicated` — domain: how an assertion entered the record. MECE: the store-declared member
  that broke `measured|inferred` is `producer_declared`; hunted residual: *imported-from-legacy-
  record* — classed `rule_derived` (the rule being the migration map, which must be cited in
  evidence). Grain: assertion. Intent: origin only — NOT quality (that is `verification_standing`;
  splitting these two axes is the whole point). State: origin is immutable; no remedy moves it.
- **`verification_standing`** `unverified | corroborated | contradicted | superseded` — domain:
  epistemic standing of an assertion. State-coherence: `unverified→corroborated` moves by RUNNING A
  CHECK; `contradicted` moves only by ADJUDICATION; `superseded` moves by a NEW assertion — three
  different acts, named per Rule 24(iv).
- **`registry_standing`** `candidate | admitted | held | rejected | retired` — domain: lifecycle
  position in an admitting registry (bridges first). Parse-generated rows may be `candidate`,
  NEVER `admitted` without evidence — the constraint that keeps a heuristic from becoming
  structural truth.
- **`observation_failure_state`** `observed | partial | substrate_unavailable | instrument_error |
  not_applicable` — domain: what the instrument could see. **`substrate_unavailable` is DISTINCT
  from an absent value** — the two-state collapse that defeated `nerves_resolve` is inexpressible
  here by construction. State: `substrate_unavailable` is moved by repairing SUBSTRATE (owner: the
  store), `instrument_error` by repairing the INSTRUMENT (owner: the tool) — different owners,
  named.
- **`relation_type`** `candidate_equivalence | canonicalized_as | merged_into | split_from |
  successor_of | replaces | instance_of` — domain: identity-level links. Succession
  interpretations (birth/retire/continue/split/merge/reorganize) are DERIVED from predecessor/
  successor cardinality per the ruling — deliberately NOT an enum here, so ambiguity cannot be
  forced at write time. Ambiguous continuity = an OPEN `candidate_equivalence`, a held state.
- **`entity_status`** `candidate | active | retired | held` — `candidate` is a cross-fabric mint
  awaiting reconciliation (minting-policy draft, §5).
- **`binding_status`** `open | closed | disputed`.
- **`target_policy`** `latest_authority | declared_release | as_of_frontier | historical_replay` —
  domain: what a coherence evaluation compares against. Kills the false-stale class: "behind" is
  only reportable relative to a DECLARED target.
- **Coherence axes** (each its own enum, deliberately NOT collapsed — different owners, different
  remedies): `availability` `available|partial|unavailable` · `integrity`
  `verified|mismatch|unverified` · `currency` `at_target|behind_target|ahead_of_target|unknown` ·
  `provenance` `complete|incomplete|unresolved` · `fabric_validity`
  `valid_for_fabric|foreign_fabric|unknown`.
- **`bundle_completeness`** `complete | partial_legacy` — a legacy pin (e.g. WP-0's blob-grain
  producer) may not reconstruct a full bundle; `partial_legacy` REQUIRES `absent_components[]` so
  honesty is mechanical, not prose (the F-2 lesson: "REQUIRED when..." never lives in a
  description string again).
- **`entity_class` and `identity_space`** are REGISTERED VOCABULARIES, not closed enums at v0 —
  initial members below; additions arrive with a four-postulate record per Rule 24 or they are not
  additions. Initial `entity_class`: `file, symbol, arn_resource, chain_motif, store, graph_surface,
  materializer, discovered_system, physical_instance, runtime_family, runtime_occurrence, part`.
  Initial `identity_space`: `git, aws_arn, iceberg_table, nessie_ref, s3_key, local_path,
  kuzu_internal, dynamo_key, logical_name`.

## 4. CONDITIONAL REQUIREMENTS (the consuming half — enforced in schema, not prose)

- `failure_state = observed` → `fingerprint`, `fingerprint_method`, `normalization_version` all
  REQUIRED. Any other failure_state → fingerprint MUST BE ABSENT (a value from a failed instrument
  is a verdict from a bare except).
- `fabric_scope = device_local` (binding) → `fabric_id` REQUIRED.
- `bundle_completeness = partial_legacy` → `absent_components[]` REQUIRED, minItems 1.
- `random_seeds` is either a non-empty array or the literal `"not_applicable"` — never absent, so
  deterministic and unrecorded are distinguishable.
- `source_frontier.entries` minItems 1 — an empty frontier is not a frontier.

## 5. MINTING AUTHORITY (RATIFIED — Andrew-direct 2026-08-27 ~18:4xZ, "Recs approved")

Primary minting on the LAPTOP fabric (substrate majority + integrator residence). Any other fabric
mints with `entity_status: candidate`; reconciliation is non-destructive via `candidate_equivalence`
→ (`canonicalized_as` | `merged_into`) — historical observations are NEVER rewritten or deleted.
ULID generation gives collision-safety without coordination; the status field, not the id shape,
carries candidacy.

## 6. WHAT v0 DOES NOT DO (named, so silence is not read as coverage)

- No storage/transport decision (file layout, ledger home, query surface) — WP-3's work.
- No bridge-assertion record — the L3 scaffold's cells adopt these primitives at population time;
  `BRIDGE_ASSERTION` composes `claim_origin` × `verification_standing` × `registry_standing` and is
  drafted with the L3 registry, not here.
- No continuity-policy CONTENT — the policy REGISTRY (per entity_class) is referenced by id
  (`identity_policy`); policies themselves are authored per class with their own evidence.
- The Rule 24 records above are AUTHOR-side; the adversarial pass hunts what I missed.
- ⛔ **THE SCHEMA CANNOT ENFORCE LAW 1'S "NEVER DERIVED" — FOUND BY THE MUTANT BATTERY'S OWN FIRST
  RUN.** A 26-char hex string fits inside the Crockford alphabet, so a hash-derived value of the
  right LENGTH passes the serial shape check. The regex enforces SHAPE (paths, ARNs, full digests
  all reject); derivation-freedom is a MINTING-PROCESS property, held by the minting authority and
  its audit — not by any validator. A reviewer who reads "pattern-checked" as "mint-verified" is
  reading the instrument, not the law.
