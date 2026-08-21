# S5 -- COMPONENT 10 SPEC HALF: the profile algebra + the mutation-capability gateway (schema/law, PROPOSED 0.1.2)
**THIS DOCUMENT IS A SPECIFICATION, NOT AN ACTIVATION. Activation of the gateway on ANY real mutation class is a SEPARATE, WORDED
act (Andrew's, per the no-gates-without-his-word law); no reader may cite this document as authority to switch anything on.**
(CTO arch gate 63767, 2026-08-20 2117Z: PASS-AS-SPEC, build staged; all four design calls upheld; precondition-token leg to be staged
EARLY as its own small build on a NAMED, BOUNDED write class -- exercised there first, never as a global write gate.)
**Seat:** 4.0.0_SA_CRO (base, spec owner) · **TO:** NFRA_EPISTEMY.SPINE S5 · **Date:** 2026-08-20 ~2115Z · **Status:** PROPOSED;
**BUILD STAGED** (component-10 build is OUTSIDE this spec -- it follows component 4 (lease service) and CTO's arch gate on this spec;
the gateway is an EXTERNAL broker/action gateway, never the acting agent's own process).
**Source of record cited, never re-declared:** `docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md` sec.2.6 (Mutation_Capability,
six-element admission, three gates, profile compilation, derived purpose) + sec.2.3 (Knowledge_Basis) + sec.2.5 (Eligibility) + sec.2.9
(harm_model@v -- CITED AS A STAMP ONLY; rider a: sec.2.9 is NOT buildable spec, and nothing here builds against it). Exchange records:
Response II sec.2.1 (elements A-F), Response III sec.1.1/1.4/4 (typed rejections, four-state lease, purpose-typed thresholds, derived
purpose, the DISCRIMINATE matrix), Response IV sec.1.1/1.2 (five axes, CONTAIN with expiry + exit disposition).

## 0. The object in one paragraph
A **Mutation_Capability** is a gateway-MINTED, proof-carrying, short-lived authorization to perform ONE mutation class on ONE declared
target set under ONE compiled **Gate_Profile**. The agent never mints it; the agent presents a six-element bundle; the gateway COMPILES
the profile from the bundle's purpose tuple, CHECKS the bundle against the profile at three typed gates, and either MINTS (with an
expiry and a live precondition token) or REJECTS with a TYPED rejection that names the gate and the reason. The capability is consumed
at act time by the same gateway, which re-compares the precondition token; a changed world expires the capability. Nothing in this
spec is a per-instance judgment call: every admission check below is mechanically checkable from the bundle, the registry, and a live
read -- the semantic judgments live upstream, in the Causal_Assessment_Object (S6) and its attestations.

## 1. Schema (compact; field -> source -> produce-time honesty; the S6 absence-semantics model applies to every nullable)
| Field | Source | Honesty |
|---|---|---|
| `capability_id`, `minted_at`, `expires_at` | gateway | always populated (gateway-side) |
| `purpose` = {`epistemic_intent`, `operational_objective`, `transition_form`, `exposure_class`, `evidence_output_class`} | five axes (sec.2.6; values sec.2 below) -- DECLARED by the presenter | required; the DERIVED purpose is a separate field below |
| `purpose_derived` = {same five fields} + `derivation_ref` | gateway: derived from the production-influence closure (component 7) over the target set -- "what production process reads what this act writes" | if the reader population is NOT ENUMERABLE (a plane the census cannot see), `purpose_derived.exposure_class` = null with ABSENCE SEMANTIC: UNDERIVABLE -> admission FAILS TOWARD THE HIGHER BAR (typed rejection `PURPOSE_UNDERIVABLE`); never a silent STERILE |
| `risk_class_ref` | harm_model@v stamp (sec.2.9 basis -- cited, not built) | nullable: null = NO RATIFIED HARM MODEL at mint vintage -> the profile compiles at the MOST restrictive threshold row and says so (`profile.basis_note`) |
| `causal_assessment_ref` | S6 object id | required for any non-NONE epistemic intent; for `NONE` (e.g. MAINTAIN under standing policy) null with semantic: NO CLAIM ASSERTED |
| `evidence_vector_ref`, `attestation_refs[]` | elements A, B | nullable per S6 rules; an unattested instrument on a load-bearing datum is `EPISTEMIC_INADMISSIBLE` at the epistemic gate, never silently accepted |
| `authority_ref` + `authority_scope` {mutation_class, target_predicate, actor} | element C (ratified policy object or explicit principal word, with scope) | required; scope check as strict as provenance check |
| `policy_epoch` | the current ratified epoch at mint | required; a STALE epoch at act time is `AUTHORITY_EPOCH_STALE` (the external gateway rejects; a stale agent may read/analyze, never commit/certify/deny/gate) |
| `knowledge_basis_digest` | sec.2.3 | required (digest of the five pinned versions; a null member inside is carried per S6) |
| `harm_model_version` | sec.2.9 stamp | nullable (see risk_class_ref) |
| `precondition_token` {target_state_digest, read_at, read_window_seconds} (0.1.2: unit on the name, per the C10-PRECOND build) | element D, LIVE read inside the declared window, ATOMICALLY BOUND (git ref / TF state serial / conditional-write where the store provides it; named GAP where it does not, e.g. plain S3 put) | required; a token older than its window at act time = `PRECONDITION_CHANGED`; a target class with NO token mechanism is admissible ONLY at `exposure_class = STERILE` |
| `transition_manifest_hash`, `rollback_manifest_hash`, `verification_manifest_hash` | elements E, F + sec.2.7 | required for any non-STERILE exposure; STERILE may carry null rollback with semantic: NOTHING-TO-REVERSE-BY-CONSTRUCTION, which the derived exposure must corroborate |
| `containment` {`expiry`, `exit_disposition`} | Response IV sec.1.2 | REQUIRED iff `operational_objective = CONTAIN`; null otherwise. A CONTAIN without expiry is a policy nobody ratified -> `PROFILE_UNSATISFIABLE` at compile |
| `discriminate_matrix_ref` | Response III sec.4.4 | REQUIRED iff `epistemic_intent = DISCRIMINATE`: the pre-registered result matrix, checked TOTAL / REFUTABLE / SEPARATING at mint (COMPLETED is an act-time/close-time check) |
| `output_quarantine` | derived from `evidence_output_class` | DIAGNOSTIC products: may support a causal claim; may NOT verify production state, satisfy a completion obligation, be served, or authorize mutation; any status upgrade keeps immutable links to the full experiment bundle (no status-token laundering) |

## 2. The enumerations (Rule-24 record, per axis; token census sec.5)
| Axis | Declared layer | Values | (i) MECE / CE vs layer | (ii) grain | (iii) intent | (iv) stability |
|---|---|---|---|---|---|---|
| `epistemic_intent` | what the act is FOR, epistemically | DISCRIMINATE · APPLY_SUPPORTED_CLAIM · NONE | exclusive; CE closed by NONE (acts with no claim) -- hunted: "confirm" is APPLY_SUPPORTED_CLAIM with a higher-rung assessment, not a value | one act | one | stable |
| `operational_objective` | what the act does to the world's state | REMEDIATE · CONTAIN · MAINTAIN · RESTORE | exclusive; hunted: "migrate" is a transition FORM not an objective (it lives on the next axis) -- the flattening GPT caught in the 4-row enum | one act | one | CONTAIN carries expiry+exit by construction |
| `transition_form` | the shape of the state change | MUTATE_IN_PLACE · MIGRATE · ROLLBACK · REPLACE | exclusive by form; hunted: "port-over" = MIGRATE (ratified doctrine: build-correctly-and-port) | one act | one | stable |
| `exposure_class` | who can be affected | STERILE · BOUNDED_PRODUCTION · FULL_PRODUCTION | exclusive, ordered; CE by derivation -- an UNDERIVABLE exposure is not a 4th value, it is a null with the UNDERIVABLE semantic + a typed rejection (the NOT_EXERCISABLE lesson: never add-a-value to absorb an instrument failure) | target set | one | moves only when the reader census moves |
| `evidence_output_class` | what the products may become | DIAGNOSTIC · TEMPORARY_OPERATIONAL · CANONICAL_PRODUCTION | exclusive; quarantine rules bind per value | products | one | stable |
| rejection = (`gate`, `reason`) TWO-FIELD | gate ∈ {COMPILATION, EPISTEMIC, AUTHORITY, TRANSACTION}; reason typed PER GATE: COMPILATION {PROFILE_UNSATISFIABLE, BUNDLE_MALFORMED}; EPISTEMIC {EPISTEMIC_INADMISSIBLE, MATRIX_NONSEPARATING, PURPOSE_ESCALATED_BY_REACHABILITY, PURPOSE_UNDERIVABLE}; AUTHORITY {AUTHORITY_SCOPE_MISS, AUTHORITY_EPOCH_STALE}; TRANSACTION {PRECONDITION_CHANGED, LEASE_NOT_VALID} | two fields because one flat enum would mix WHERE it failed with WHY (the RCG v2 split); each reason belongs to exactly one gate; CE per gate hunted against the bundle elements A-F: A,B -> EPISTEMIC; C -> AUTHORITY; D,E,F -> TRANSACTION; profile -> COMPILATION. 0.1.2 (C10-PRECOND proposal weighed): a MALFORMED/ABSENT-FIELD element (e.g. a token with a null window/digest/read_at) is a BUNDLE-SHAPE defect whose remedy is fix-the-caller -- it is rejected at COMPILATION as BUNDLE_MALFORMED (any element), NEVER as a TRANSACTION reason: PRECONDITION_CHANGED stays reserved for the world-moved / read-too-old cases (expired window, 412s). Shape failures have ONE home so each gate keeps one intent | one admission attempt | one (teach, not merely block) | a new reason is added UNDER its gate, never as a new gate |
| `lease_state` (four-state, Response III sec.1.4) | validity of a support member at evaluation | VALID · INVALID · UNKNOWN · EXPIRED | exclusive + exhaustive by the transition table: changed digest -> INVALID; unreadable member -> UNKNOWN; expired attestation -> UNKNOWN; horizon passed -> EXPIRED; only a current attested comparison -> VALID; **failure to re-evaluate NEVER preserves VALID** | one member | one | the estate's generated_at/last_review split is the two-clock instance |
| `containment.exit_disposition` | how a CONTAIN ends | LIFT · CONVERT_TO_RATIFIED_POLICY · ESCALATE | exclusive + exhaustive over the ways a temporary deny may end; CONVERT walks the full authority gate | one containment | one | stable |
Deliberately NOT minted here: `Risk_Class` values (the harm model's, sec.2.9 -- not buildable; carried as a ref), and the four
policy ARCHETYPES (REMEDIATE/DISCRIMINATE/MIGRATE/ROLLBACK rows of Response III sec.4.1) -- they persist as NAMED QUERIES over the
tuple space, never as an enum (the recall-vs-truth split).

## 3. The profile algebra (deterministic; the one algorithm)
Input: the purpose tuple T = (ei, oo, tf, ec, eoc) + `risk_class_ref` (or null) + the registry's per-axis CONSTRAINT CONTRIBUTIONS
(each axis VALUE contributes a triple: requirements R_v (elements that must clear, with threshold rows), prohibitions P_v (things the
act may not do), permissions M_v (relaxations it may use)).
1. `Gate_Profile(T)` = ( ∪ R_v , ∪ P_v , ∩ M_v , pointwise-max over thresholds ) across the five values -- requirements and prohibitions
   UNION (the strictest axis wins), permissions INTERSECT (a relaxation holds only if every axis grants it), thresholds take the
   POINTWISE MAX per evidence axis (never a scalar height -- Response III sec.4.1).
2. SATISFIABILITY: if ∪R ∩ ∪P ≠ ∅ (a requirement the tuple also prohibits, e.g. STERILE + CANONICAL_PRODUCTION, or CONTAIN without
   expiry) -> `PROFILE_UNSATISFIABLE` with the contradicting pair printed. Contradiction is DETECTED, never reconciled into a softer
   profile (manufactured coherence is the failure).
3. DERIVED PURPOSE: T_derived from the production-influence closure over the target set; admission evaluates `T_effective` = the
   axis-wise STRICTER of (declared, derived) -- declared ∧ derived, derived wins on conflict; a declared STERILE whose targets have a
   production reader is `PURPOSE_ESCALATED_BY_REACHABILITY` (re-evaluated at the REMEDIATE/MIGRATE bar, not denied outright); an
   unenumerable reader population is `PURPOSE_UNDERIVABLE` (fail toward the higher bar).
4. The three gates, in order, each with its typed rejection: EPISTEMIC (A, B, and for DISCRIMINATE the matrix's TOTAL/REFUTABLE/
   SEPARATING) -> AUTHORITY (C + epoch) -> TRANSACTION (D token atomically bound; E reversibility contract opened before the first
   irreversible act, or explicit irreversibility acknowledgment escalated to the authority tier; F pre-registered verification;
   lease states of every support member VALID). First failing gate names the rejection; later gates are NOT evaluated (a bundle that
   fails epistemically gets no authority verdict to misread as "nearly admitted").
5. MINT: capability with `expires_at` = min(profile horizon, token window end, containment expiry if any); the act consumes it at
   the same gateway with a fresh token compare AND a fresh policy_epoch compare -- A CAPABILITY VALID AT MINT AND STALE AT ACT MUST FAIL,
   never pass (else the gate is a stale attestation); a consumed capability cannot be re-presented (single use).
6. The acceptance ceiling (sec.2.8): no accumulation of proofs converts an irreversible FULL_PRODUCTION act into evidence-authorized
   -- the profile's `required_authority_class` carries WHICH word (this estate's ratified instance: the principal for irreversible
   full-production acts); proofs earn the card, the word takes the risk.

## 4. Estate correspondence (what already runs, so the build re-uses rather than re-invents -- Build Ladder rung 2)
Epistemic gate = the certification-owner-withholds-GO law (human-enforced today); authority gate = enumeration-based owned-paths +
lane refusals typed distinct from gate failures; transaction gate = safe-commit lock (token: remote ref; rejected push = token
mismatch; rebase banned), safe-apply/HALTGT, the deploy-completion ledger (element E's embryo), TF plan staleness against state
serial (partial token); the NAKED layer = plain S3 put (no token, last-writer-wins -> conditional-write where provided, named gap
otherwise). Purpose quarantine = the ad-hoc-QA carve-out (ad-hoc artifacts are never production evidence) -- DISCRIMINATE × STERILE ×
DIAGNOSTIC avant la lettre. Derived purpose = the consumer edges of the dependency graph (component 7's closure).

## 5. Token census (word-boundary, RUN at authoring 2026-08-20 ~2118Z over SYSTEM_DEFINITIONS / rule bank / canonical,
counts defs/bank/canon; any occupied token classified REUSED-same-sense / PROSE-ONLY / COLLISION -- a collision is renamed before
this spec leaves PROPOSED). RESULT: all 21 NEW tokens 0/0/0. Reused-set hits: REPLACE 0/1/0 (rule bank :451, English verb in a
prose string -- PROSE-ONLY, no axis occupancy), VALID 0/1/0 (:454, prose), EXPIRED 0/1/0 (:500, "an expired declaration must
stop concealing" -- same sense as the lease state, compatible), NONE 1/1/0 (prose); every other reused token 0/0/0 in the canon
files (their ratification lives in the exchange records and the S6 schema, cited). NO COLLISION.
New: Mutation_Capability · Gate_Profile · Epistemic_Intent · Operational_Objective · Transition_Form · Exposure_Class ·
Evidence_Output_Class · APPLY_SUPPORTED_CLAIM · BOUNDED_PRODUCTION · TEMPORARY_OPERATIONAL · CANONICAL_PRODUCTION ·
PROFILE_UNSATISFIABLE · BUNDLE_MALFORMED (0.1.2; census 0/0/0 canon trio) · PURPOSE_ESCALATED_BY_REACHABILITY · PURPOSE_UNDERIVABLE · MATRIX_NONSEPARATING · AUTHORITY_EPOCH_STALE ·
LEASE_NOT_VALID · CONVERT_TO_RATIFIED_POLICY · EPISTEMIC_INADMISSIBLE · AUTHORITY_SCOPE_MISS · PRECONDITION_CHANGED.
Reused (ratified or exchange-ratified, same sense): DISCRIMINATE / REMEDIATE / CONTAIN / MAINTAIN / RESTORE / MIGRATE / ROLLBACK /
REPLACE / MUTATE_IN_PLACE / STERILE / FULL_PRODUCTION / DIAGNOSTIC / VALID / INVALID / UNKNOWN / EXPIRED / LIFT / ESCALATE / NONE.

## 6. What this spec does NOT do
Does not build the gateway (staged; component 10 build after component 4); does not enumerate Risk_Class (sec.2.9 not buildable);
does not define the harm algebra; does not grant any agent the power to mint (gateway-only by construction); does not create a
new approval gate on any live work (NEVER: no gates without Andrew's word -- this is a SPEC of a mechanism the PRD ratified for
build-staging; its activation on any real mutation class is a separate, worded act). CTO arch gate next; exercised leg = the first
compiled profile over a real bundle when component 10 builds.
