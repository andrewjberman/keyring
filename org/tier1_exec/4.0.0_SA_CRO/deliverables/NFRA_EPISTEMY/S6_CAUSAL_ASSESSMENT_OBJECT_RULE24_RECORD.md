# S6 — Causal_Assessment_Object schema 0.1.0: Rule-24 record + token census (PROPOSED)
**Seat:** 4.0.0_SA_CRO (base, registry executor) · **TO:** NFRA_EPISTEMY.SPINE S6 · **Date:** 2026-08-20 ~2035Z
**Source of record:** PRD_EPISTEMIC_MECHANIZATION §2.4/§2.5 (cite-not-copy: the schema CITES those sections; a
field change routes through base, never in-lane). **Exerciser:** 4.0.0_SA_CRO~C (C9-RIDE, Phase 1 at the
Batch-2 boundary). **Gate:** 1.0.0_SA_CTO arch gate. Status PROPOSED; widened only by naming act.

## Axes declared (one intent + one grain each; the object is a RECORD, its enums are SEPARATE AXES, never one
flattened "result")

| Axis | Declared layer (grain) | Values | (i) MECE / CE-against-layer | (ii) grain | (iii) intent | (iv) stability |
|---|---|---|---|---|---|---|
| `result_status` | claim-strength rungs of ONE assessment | INFERRED · EXPERIMENTALLY_CONSISTENT · DISCRIMINATED_WITHIN · INTERVENTION_SUPPORTED · SOURCE_OR_GRAPH_CONFIRMED · CONTRADICTED · UNKNOWN | exclusive by rung; CE closed by UNKNOWN (instrument/none) + CONTRADICTED (refuted) — hunted: "withdrawn" = UNKNOWN w/ invalidation predicate, not a rung | one (claim) | one (how strong) | moves under evidence arrival; UNKNOWN moves under instrument repair — named, acceptable (state axis: evidence-sufficiency) |
| `exclusions[].reason_class` | why a space member is absent from tested_set | RULED_OUT_BY_EVIDENCE · NOT_ADDRESSABLE_BY_EXPERIMENT · DEFERRED · OUTSIDE_CLAIM_SCOPE | exclusive; CE over the reasons an experiment omits a member — hunted: "omitted by error" is not a value by design (it is the attack the printed complement exposes) | one (member) | one (exclusion cause) | only RULED_OUT moves a member out of live_candidates; the other three keep it in known_residual — the asymmetry is the design, stated |
| `evidence_vector[].axis` | evidence-rail kinds | TEMPORAL · DEPENDENCY · CO_CHANGE · RUNTIME_TRACE · SUBSTRATE_DRIFT · RECENCY_HEAT · TOPOLOGICAL · DECLARED_RATIONALE · INTERVENTION | not strictly exclusive by nature (rails overlap) — declared as a COVER, not a partition, per the original exchange's own caveat; CE hunted: instrument-trust is NOT an axis here (it is the attestation ref per datum) | one (datum) | one (evidence kind) | all move under observation |
| `evidence_vector[].basis` | grounding ladder | desired · applied · exercised | ratified estate vocabulary REUSED, not re-coined | — | — | — |
| `candidate_relation.relation_kind` | hypothesis relation shape | CONTRIBUTED_TO · NECESSARY_FOR · SUFFICIENT_FOR · CORRELATED_UNDER_POLICY | exclusive by logical form; CE hunted: "prevented" = CONTRIBUTED_TO with negated effect_ref, stated | one | one | n/a (declarative) |
| `interim_status.value` (pre-envelope) | **MANIFEST SUBJECT** at one vintage (NOT the run set — CTO 63664: else the absence member becomes unreachable in the record) | DERIVED_FROM_BUNDLE · ACQUISITION_FAILED_NO_BUNDLE | disjoint + exhaustive OVER THE MANIFEST (bundle exists / does not) — the bundle-branch's detail derives from stage_states+terminal; the absence branch is populated by predicate over the manifest, denominator = manifest's | one (manifest subject) | one (was an assessment acquirable) | the one member that does NOT move under run repair is ACQUISITION_FAILED (moves only when a bundle appears) — named |

## Token-hygiene census (word-boundary, canon surfaces at HEAD)
New tokens: `Causal_Assessment_Object` 0 · `ACQUISITION_FAILED_NO_BUNDLE` 0 · `DERIVED_FROM_BUNDLE` 0 ·
`CORRELATED_UNDER_POLICY` 0 · `EXPERIMENTALLY_CONSISTENT` 0 · `INTERVENTION_SUPPORTED` 0 (all unoccupied
across SYSTEM_DEFINITIONS / rule bank / canonical — measured at authoring). Reused (same sense, ratified):
`desired/applied/exercised`, `DISCRIMINATED_WITHIN` (exchange ladder), `RULED_OUT_BY_EVIDENCE`,
`NOT_ADDRESSABLE_BY_EXPERIMENT`, `known_residual` (PRD §2.4 vocabulary). Deliberately EXCLUDED from
`result_status`: `root cause` / `proven` / `confirmed` bare (reserved words, legal only on source-confirmed
claims — the ladder's final rung carries them by name).

## What this record does NOT claim
Not ratified; not wired to any gateway; no consumer yet besides ~C's exercise. The Eligibility_Evaluation,
Discrimination_Certificate, and Observation_Record are SEPARATE objects (PRD §2.5/§2.2/§2.1) referenced by id —
this record does not re-declare their fields. Recovery/reachability edges, when the object grows them, cite
Response IX's exercised-witness floor (rider d).
