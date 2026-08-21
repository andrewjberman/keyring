# NFRA_EPISTEMY Component 2: instrument-attestation harness

This package implements the `Discrimination_Certificate` described by the shared source of
record, `docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md` section 2.2. It is a
schema-act proposal routed through 4.0.0_SA_CRO Base and the 1.0.0_SA_CTO architecture gate;
the package does not claim independent ownership of the shared object.

One certificate is local to one instrument version, plane, searched population, and denominator
grain. It becomes VALID only after an isolated positive control and a generated known negative
actually discriminate, the shared dependency intersection is named, and at least one observed
crossing lies beyond the target population's failure domain.

The outcome axis is `VALID | INVALID | UNKNOWN | EXPIRED`. A known construction defect is
INVALID. A changed invalidation coordinate is EXPIRED. An unavailable required current coordinate
is UNKNOWN. Only a current and fully demonstrated certificate is VALID. Failure to re-attest never
preserves validity.

There are no nullable certificate fields. Missing evidence is a schema error; unavailable
reevaluation state is the explicit UNKNOWN terminal. This satisfies the S6 absence-semantics law
without using null as an untyped hole.

The implementation wraps but does not edit `comp-find`, `comp-estate`, or `census_substrate`.
Each positive and generated-negative acquisition emits a C1 Observation_Record. An observation
under a VALID certificate carries its non-null `discrimination_certificate_ref`; the same
observation without attestation retains null. Plane is consumed only as the ratified
`DESIRED | APPLIED | EXERCISED` enum beside the separate substrate field, discharged at
`6f944857c4`.

Components 3 and 4, cloud writes, shared-engine edits, enforcement, and the PRD section 2.9 harm
surfaces are outside this component.
