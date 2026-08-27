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
   REQUIRES its delta (CV-3). `unknown`/`unverified` stay free — the remedy that moves `verified`
   must not punish honesty about not knowing.

## 2. RECORD CATALOG (10 types — unchanged roster, see schema for the field law)

`entity` · `entity_binding` · `state_observation` · `identity_relation` · `materializer` ·
`materializer_version` · `materialization_run` · `source_frontier` · `surface_version` ·
`coherence_evaluation`. Identity mechanisms per the ratified table (minted serials for enduring
mutables; content-addressing legal for immutable observations/versions/receipts).

⛔ **CARRIED REQUIREMENT for the future BRIDGE_ASSERTION record (CV-1, binding on its author):**
`registry_standing = admitted -> evidence_refs minItems 1`, or the three-axis split is WEAKER than
the old basis bar in exactly the cell that matters. §3's "candidate never admitted without
evidence" gets its consuming half the day the record exists. `3.0.0_SA_CVO~X`'s L3 certification
bar reads for that conditional's existence.

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

### 3.2 `verification_standing` — `unverified | corroborated | contradicted | superseded`
DOMAIN: epistemic standing of an assertion. MECE over check-states; hunted member: partially-checked
→ stays `unverified` (a partial check that upgrades standing is the F5 defect). GRAIN: assertion.
INTENT: one axis — has a check run and what did it say. STATE-COHERENCE: `unverified→corroborated`
moves by RUNNING A CHECK (asserting seat); `contradicted` moves only by ADJUDICATION (adjudicator);
`superseded` moves by a NEW assertion (any seat) — three acts, three owners.
ARM TABLE (F5): `corroborated|contradicted -> evidence_refs required` (owner: checker) ·
`contradicted -> adjudicated_by required` (owner: adjudicator) · `superseded -> superseded_by
required` (owner: superseding author). ⛔ Evidence INDEPENDENCE is not schema-checkable — §6 limit 2.

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
the mutation LAW 3 forbids wearing the close's label).

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
normalization, per the CRLF law) · `observed_absent -> fingerprint triple FORBIDDEN (nothing to
hash) + evidence_refs REQUIRED` (owner: observer — an absence claim carries the warrant of WHERE
it looked, because absence-without-warrant is exactly the unfalsifiable cell every census defect
this directive found has hidden in).

### 3.7 `referent_scope` — `fabric_invariant | fabric_local | device_local` (R2-1; supersedes `fabric_scope`)
DOMAIN: the locality the REFERENCED STATE claims (never where the act ran — that is the execution
family). MECE: `fabric_local` ADDED (GPT review) — the round-1 hunted member
"fabric-scoped-but-multi-device" now has its cell instead of an out-of-scope note. GRAIN:
referent, per record (entity_binding + state_observation; runs carry NO referent scope — an event
has a location, not a locality claim). INTENT: Rule 26 locality of the referent, one axis.
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

### 3.10 `bundle_completeness` — `complete | partial_legacy`
DOMAIN: whether a materializer version's execution bundle is fully pinned. MECE: over the declared
pin-completeness domain — with the CVR2-2 finding CARRIED OPENLY: a future partial-NOT-legacy
bundle has no honest home in this two-value domain (intent-fusion of degree with cause); the R2-2
design doc resolves it (complete|partial + cause-in-evidence) rather than this record absorbing it
silently. GRAIN: version. INTENT: pin completeness. STATE-COHERENCE: `partial_legacy` moves by reconstructing the absent components
(owner: the pinning seat) — or never, honestly.
ARM TABLE: `complete -> all six bundle digests required` · `partial_legacy -> absent_components
required, minItems 1` (honesty is a conditional, not prose). Positive coverage: BOTH arms carry
fixtures (DT-6 closed the complete-arm zero-coverage hole).

### 3.11 `identity_scope` — `logical | fabric_instance | device_instance | run_occurrence`
DOMAIN: the scope at which an identity claims uniqueness. MECE: account-scoped → `logical` (the
account lives in the native key). GRAIN: entity. INTENT: identity locality. STATE: structural, no
remedy axis.

### 3.12 `relation_type` — `candidate_equivalence | canonicalized_as | merged_into | split_from | successor_of | replaces | instance_of`
DOMAIN: identity-level links. MECE: over declared link kinds — hunted members: fabric INSTANCE_ON
(memoranda vocabulary) folds into `instance_of` (the record's fabric lives on the instance entity,
not the relation); ambiguous continuity is an OPEN `candidate_equivalence`, not a missing value.
Succession INTERPRETATIONS are DERIVED from predecessor/successor cardinality (ruled) — deliberately not an enum, so ambiguity cannot be forced at write time;
ambiguous continuity = an open `candidate_equivalence`. GRAIN: serial-pair. INTENT: identity
topology. STATE-COHERENCE: relations are append-only; `superseded_by` is the only forward pointer.
⛔ SELF-LOOPS are rejected by the validator's SEMANTIC arm (DT-2b): a 1→1 self-merge would be READ
AS A CONTINUATION by the ruling's own cardinality derivation — a lying record the architecture
itself would interpret; the schema cannot compare two fields, the validator can and does.

### 3.13 `target_policy` — `latest_authority | declared_release | as_of_frontier | historical_replay`
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
required`. `unknown`/`unverified` FREE by design.

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
`unknown`, `active`, `superseded`, `complete`, `unverified` (same epistemic/lifecycle sense per
pair; remedy divergence lives in each enum's state-coherence record — and per CVR2-2, `unknown`'s
entry carries a grain note: same sense, DIFFERENT grain-legitimacy — observer-state is coherent at
observer grain (coherence axes) and mixed at subject grain (materializer status); the subject-grain
use dissolves under R2-2's derived-status work). ELIMINATED rather than
allowed: `candidate`, `held` (different meanings — renamed out at F4). The gate REFUSES any new
collision not on the list.

## 4. CONDITIONAL REQUIREMENTS (the consuming half — all mechanical)

The full set now spans: three-field fingerprint coupling (every direction, every failure_state) ·
hard-failure forbids all three fingerprint fields · observed requires all three · fabric_scope
arms on three record types (require AND forbid directions) · closed→valid_to ·
warrant conditionals on identity_relation (evidence/adjudicator/successor) · run terminal/running
completed_at arms · bundle_completeness both arms · coherence evidence/delta arms ·
`evidence_refs` minItems 1 ON THE $def (CV-5 — present means non-empty, no future conditional can
forget it) · `random_seeds` = non-empty list or literal `"not_applicable"` · frontier minItems 1 ·
iso_ts range-checked fields (CV-4; calendar validity beyond ranges: validator semantic arm, §6).

## 5. MINTING AUTHORITY (RATIFIED — Andrew-direct 2026-08-27 ~18:4xZ, "Recs approved")

Primary minting on the LAPTOP fabric. Other fabrics mint `entity.current_status: provisional`;
reconciliation is non-destructive via `candidate_equivalence` → (`canonicalized_as` | `merged_into`)
— historical observations NEVER rewritten. ULID per serial; **the minting act LOWERCASES the ULID
before prefixing** (F6) — a serial is born lowercase or it was not minted by the authority.
⛔ **THE COMPENSATING CONTROL FOR LAW 1 IS INCOMPLETE AT v0.1** (CV-2, entry-5 finding): "the
minting authority and its audit" names no mint-audit artifact, receipt record, or audit owner. The
MINT RECEIPT lands with WP-3 (the ledger); until then LAW 1's enforcement is the minting seat's
discipline, and every certification scope must say so.

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
