# NFRA_EPISTEMY — SPINE LEDGER (S1 harm-surface tracker · S2 schema-act index)
**Seat:** 4.0.0_SA_CRO (base) · **TO:** NFRA_EPISTEMY.SPINE @bf88ff55c6 · **Opened:** 2026-08-20 ~2030Z
**Spec of record:** docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md
This ledger is the spine's running record — appended at every schema act and every review milestone.
Rider (a) binds: nothing in S1 is buildable spec.

## S1 — the four harm surfaces (PRD §4b), tracked as OPEN REQUIREMENTS

| # | Surface | Status | Owner-or-deferral | Condition that would close it |
|---|---|---|---|---|
| 1 | Harm normal form (dimensions / effect maps / composition / interaction / observation / recovery capacity separated) | OPEN | DEFERRED — base holds the spec question; no build seat until the whole-system review returns | A Rule-24-recorded normal form with per-surface closure certificates, reviewed by the exchange counterparty, ratified by Andrew |
| 2 | Generated applicability compiler + proof-bearing exclusions | OPEN | DEFERRED — depends on #1 | APPLICABLE/INAPPLICABLE(leased proof)/UNKNOWN compiled per dimension from the basis, never selected; mutant-challenged |
| 3 | Composition + interaction algebra (per-surface closure, algebra-mutants) | OPEN | DEFERRED — depends on #1; the deterministic precondition-invalidation layer is the first stage (Response IX §2.1) | The algebra GENERATED from declared semantics; the algebra-mutant battery alters results in the expected direction; the A+B counterexample caught mechanically |
| 4 | Recovery-reachability instrument (path witnesses, support closure, independence cuts, exercised-witness floor) | OPEN | DEFERRED — depends on #1–#3; the floor (Response IX §2.2) is policy-ready now | Proof-carrying Recovery_Reachability_Certificate returning a path witness; never-exercised paths carried ASSUMED and priced; churn-indexed re-exercise (the open question to the counterparty) |

Re-stated at each program review. A lane TO citing §2.9 as buildable spec is a finding at my gate.

## S2 — executed schema-act index (every act carrying its four-postulate record + token census)

| Date/Z | Act | Record | Gate |
|---|---|---|---|
| 08-20 ~1340 | Lifecycle_Stage value enum (v3.11) + the ACTIVE health-clause amendment | ANDREW_DIRECT_20260820_LIFECYCLE_STAGE_VALUE_ENUM_RATIFIED.md; CVO~Z proposal §2.3/§2.4; CVO cert @8252e2378b | Andrew word; CVO exit-bar |
| 08-20 ~1414 | `observability` C3.ii vertical mint (roster 29→30) | ANDREW_DIRECT_20260820_OBSERVABILITY_VERTICAL_MINT.md; CVO cert @2d7ff49e58 | Andrew word; CVO cert |
| 08-20 ~1315 | Rule 24 WIDENED to all schema enumeration (law) | ANDREW_DIRECT_20260820_RULE24_BINDS_ALL_SCHEMA_ENUMERATION.md @1ab080d864 | Andrew word |
| 08-20 ~1456 | Rule 24 SCOPED to outcome arrays/predicates, CE against declared layer (law) | ANDREW_DIRECT_20260820_SCOPE_OUTCOME_ARRAYS_MECE_LAYER_COVERAGE.md | Andrew word |
| 08-20 | ~B census verdict array split (3 axes) + GOVERNED_DUAL_CARRIER class | census @bc03be2524 / @6b48695dfa rule_24_record | base ruling |
| 08-20 | ~A atom_layer0 package records (11) incl. splitter results, stage states, seam axes, grammar | rule24/SCHEMA_ENUMERATION_RECORDS.json @462ac78311 → @47e3a54027 | base validation |
| 08-20 | ~C disposition schema record (roadmap) + ALREADY_RESOLVED_SINCE_CENSUS + matrix type-shapes (RESOLVES-BY-RULING, INHERITANCE, SELF-DECLARED) | rule24/DISPOSITION_SCHEMA_RECORD.json @167a763aa4; batch-1 bundles | base batch gate |
| 08-20 ~1945 | Rarity coordinates: BOTH populations (per-firm + estate-wide) — ruled, rider spec pending | ANDREW_DIRECT_20260820_RARITY_DENOMINATOR_AND_DEVICE_AXIS.md | Andrew word |
| 08-20 ~2050 | registry_vintage optional slot on atomicity_certificate + R24-AL0-012 (4.0.0_SA_CRO~A) -- LANDED; validator took +1 required record only, NOT vintage-aware -> pre-12 bundles red at HEAD; vintage-aware law RULED (63721->~A 2051Z), amendment rides ~A next commit; Runs 1-22 stand valid at their vintage | @45a2892ed2 | base ruling; CTO gate on the validator amendment |
| 08-20 ~2050 | Observation_Record schema act (C1-ENVELOPE, 4.0.0_SA_CRO~A): 4 stage axes {acquisition, transport, enumeration, parse} + substantive {KNOWN, UNKNOWN}, construction rule KNOWN only on all-green; token census at 16a15842e2 | @45a2892ed2 (25 files; schemas/observation_record.schema.json + rule24/OBSERVATION_RECORD_SCHEMA_ENUMERATION.json) -- BASE-VERIFIED by exercise 2056Z: run_acceptance rc=0 (8/8 mutants, STABLE, 6/6 wrappers), validate_envelope PASS absent+known, manifest 17/17 on disk. ONE Rule-24 finding routed as amendment: `plane` is a free string carrying `DESIRED_REPOSITORY` = plane x substrate fused in one token (24(iii)); ask = ratified plane enum + separate `substrate` field | base VERIFIED 2056Z -> CTO GATED 2100Z (63743) at 45a2892ed2 WITH THE AMENDMENT AS A BINDING BIND-TIME CONDITION: no consumer may parse/branch/key on `plane` until the ratified-enum + `substrate` split lands (ratified-by-usage guard); amendment wants a NAMED landing (~A next commit) |
| 08-20 ~2034 | Causal_Assessment_Object schema 0.1.0 (S6) + Rule-24 record: six declared axes, interim_status declared over the MANIFEST (CTO 63664), 6 new tokens census-RUN 0/0/0 | NFRA_EPISTEMY/S6_CAUSAL_ASSESSMENT_OBJECT.schema.json + _RULE24_RECORD.md @16a15842e2 | CTO gate 63695 PASS-TO-EXERCISE (2042Z) APPLIED -> 0.1.1 @85f64c7142 (status cut; 11 declared absence semantics; result_status read-only-by-construction); CTO 63743: 0.1.1 ACCEPTED, the absence-semantics table named THE MODEL for every component schema act ("a nullable field with no declared absence semantic is a hole; one that names what its absence DISQUALIFIES is a control"); exercised leg = ~C Phase-1 instance + CVO verify |
| 08-20 ~2100 | C2 rarity-coordinate rider SPEC (rides R1; BOTH populations per Andrew 1945Z; 3 enums Rule-24-recorded; census run, all new tokens 0/0/0, `recurrence` reused) | C2_RARITY_COORDINATE_RIDER_SPEC_20260820.md @cc3defbef2 | base -> COO routes the R1 owner act (0.8.0 candidate) |
| 08-20 ~2118 | S5 profile algebra + mutation-capability gateway SPEC (component-10 spec half; BUILD STAGED): five purpose axes, two-field typed rejection (gate x reason), four-state lease, CONTAIN expiry+exit, DISCRIMINATE matrix, compilation = union/intersect/pointwise-max -> satisfiability, derived purpose wins, acceptance ceiling; Rule-24 per axis; census RUN 21 new tokens 0/0/0 no collision | NFRA_EPISTEMY/S5_PROFILE_ALGEBRA_AND_MUTATION_GATEWAY_SPEC_20260820.md @f99f9efec2 | base -> CTO arch gate (requested ~2122Z) |

## S3–S7 — status at open
S3 certs: the FIRST envelope-backed observations exist (C1 evidence/, 6 observation records incl. 3 honest ABSENT->UNKNOWN); no Discrimination_Certificate yet. S4: DISCHARGED 2038Z -- three lane TOs relayed/delivered ~2026Z;
agent-side acks landed ~A 203151Z (C1-ENVELOPE, "GO triggered", S0 ground-read started) and ~B 203255Z
(C7-CLOSURE, GO triggered, execution held by the TO's own clause until Pass 3 completes); both returned
to COO same turn; zero scope questions at either lane. S6: AUTHORED @16a15842e2 (row above), CTO gate
requested. S5: next base act after the rarity rider. S7: proof at the envelope-cert milestone.
