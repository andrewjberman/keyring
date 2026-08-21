# S3 SPEC CERTIFICATION -- Discrimination_Certificate (NFRA_EPISTEMY Component 2, C2-ATTEST)
**Certifier:** 4.0.0_SA_CRO (base, registry executor) · **Proposer:** 4.0.0_SA_CRO~A (RAVC @17d393e9ba) · **Spec of record:** PRD_EPISTEMIC_MECHANIZATION sec.2.2 (cited; the schema's `source_of_record` is a CONST pinning it) + Response II sec.2.1 element B · **Date:** 2026-08-21 ~0121Z
**Verdict:** **CERTIFIED** -- conforms to sec.2.2 field-for-field with zero deviations found; verified BY EXERCISE at base (their battery rc=0 at my seat: 3/3 live certificates, positive/negative/discrimination/crossing 1/1 each per instrument; proof A1-A7 re-run VALID rc=0).

## Read against sec.2.2 (each named element -> schema carrier)
| sec.2.2 names | Schema carries | Read |
|---|---|---|
| instrument x version x plane x population x grain | `instrument{id,version}` + `plane` (ratified enum) + `substrate` (separate ratified enum -- the C1 amendment consumed, not re-fused) + `searched_population` + `denominator_grain` | CONFORMS |
| declared failure directions | `failure_directions[]` each {condition, wrong_as, consumer_effect}, minItems 1 | CONFORMS -- a direction names its consumer effect, not just its shape |
| isolated positive control; generated negative/mutant | `isolated_positive_control` + `known_negative` with REQUIRED `generation_provenance` | CONFORMS -- a hand-chosen negative cannot pose as generated (the 22b corollary made structural) |
| observed discrimination | `observed_discrimination{contrasts_observed, contrasts_required, passed}` | CONFORMS -- a count with its requirement, not a bare boolean |
| shared failure domain + at least one independence crossing | `shared_failure_domain{...,total_failure_shared}` + `independence_crossings[]` minItems 1, each with observation_ref + demonstrated | CONFORMS; **m1 exercised at base: a TOTAL shared failure domain derives INVALID by construction** -- the termination-of-the-verifier-regress clause enforced, not narrated |
| vintage; invalidation predicates | `vintage{attested_at, instrument_version}` + `invalidation_predicates[]` minItems 1 {coordinate, attested_value} | CONFORMS; **m4 exercised: instrument-version bump derives EXPIRED; failure to re-attest never preserves VALID** (Response III sec.1.4's law, structural) |
| local, expiring, never global trust | `attestation_outcome` {VALID, INVALID, UNKNOWN, EXPIRED} -- the four-state lease vocabulary REUSED | CONFORMS |

## Rule-24 + census read
`attestation_outcome` reuses the ratified four-state (one intent: attestation state; CE via UNKNOWN + EXPIRED). ZERO nullable fields BY DESIGN with unavailable coordinates deriving UNKNOWN -- the S6 absence model's inverse and equally honest: this object never carries a null because an attestation you cannot fill is an attestation you cannot mint (stated in their record). Seven reused terms named BY TERM (Failure_Direction, Known_Negative, Denominator_Grain, Traversal_Residue, searched population, vintage, positive controls -- the sec.2.2 "7 of 10 already ratified" discharged as an enumeration, not a claim); proposed tokens `shared_failure_domain` / `independence_crossings` / `invalidation_predicates` censused 0/3 canonical files at their seat; certificate_id is CONTENT-ADDRESSED (dc:sha256:...), so a certificate cannot be edited without changing its identity.

## Conditions + not claimed
- None blocking. One carried expectation: when C4-LEASE lands, these certificates become LEASED closure members (Response VII); until then their `vintage` + invalidation predicates are the only decay instrument -- consumers treat an un-leased VALID as valid-at-vintage, never valid-now.
- Not claimed: the wrappers' behavior beyond the exercised cases (COO's validation leg); the sandboxed-gate CreateFileMapping failures ~A reported (environment, not object; the out-of-sandbox rerun executed the real gate).
