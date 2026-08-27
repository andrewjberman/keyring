# ANDREW RULING 2026-08-27 — ISSUE 3 ADOPTED: THE IDENTITY-STATE COHERENCE KERNEL (ISCK)

**Received:** 2026-08-27, Andrew-direct at the `1.0.0_SA_CTO~X` terminal, following the issue-1/2/3
design discussion of the same day. **Carriers:** Andrew's message (operative summary, quoted verbatim
below) plus two supporting memoranda delivered as files and copied into this directory:

- `D11_Identity_State_Coherence_Kernel_20260827.docx` (the D11 kernel synthesis)
- `C3MATERIALIZE_Identity_State_Coherence_Kernel.docx` (the implementation memorandum)

Both were read in full at this seat before this record was written. The memoranda were shaped with
GPT assistance on Andrew's instruction; the RULING authority is Andrew's word at this terminal.

---

## THE OPERATIVE RULING (Andrew's message, verbatim)

> Adopt Issue 3 as the Identity-State Coherence Kernel under D11. Resolve the design fork in favor
> of opaque minted entity and materializer serials; temporal substrate bindings; versioned
> fingerprints with method and normalization; and append-only succession and reconciliation
> relations. Hashes may identify immutable observations, versions, and receipts, but must not
> identify enduring mutable entities.
>
> Issue 3A defines the shared contract before the L3 bridge cells are populated. Issue 1 implements
> entity resolution, grain, bindings, and succession over that contract. Issue 2 implements the
> materializer census, logical materializer identities, implementation versions, declared opinions,
> and run provenance over the same contract. Issue 3B then evaluates coherence between source
> frontiers, canonical Iceberg/Nessie graph versions, Kuzu projection pins, materializer versions,
> and fabric locality.
>
> The L0 part registry becomes a typed projection of the general identity ledger, not a separate
> identity system. Device-local physical artifacts receive instance identities related to logical
> surfaces; they are not automatically treated as one physical entity across fabrics. The graph
> membership model must be cover-capable, while fusion signatures remain matching evidence rather
> than identity.
>
> In parallel with the contract work, pin the existing C2/C3 evidence and its producer into
> immutable, digest-addressed storage. After 3A lands, migrate L0, register Nessie authority
> surfaces, repair resolver failure states, and populate the first evidence-backed symbol-to-file
> bridge. That bridge supports the first decisive structure-plus-behavior fusion experiment.
>
> The underlying architecture then becomes mechanically clear: The spine establishes who or what
> persists. The materializer topology establishes which process transformed which source frontier
> into which version. The coherence kernel proves that every published and projected graph surface
> is traceable to those identities, states, processes, authorities, and fabrics.

## WHAT THIS RESOLVES (from the memoranda's own decision registers)

| decision | standing |
|---|---|
| Universal identity mechanism | **RESOLVED: opaque minted serials.** Source keys are temporal bindings; hashes are state/version/receipt evidence, never enduring-mutable-entity identity |
| Universal entity grain | **RESOLVED: none.** Canonical grain remains `(PLANE, ENTITY)` |
| Logical vs physical surface | **RESOLVED: separate identities** linked by INSTANCE_OF/INSTANCE_ON; Rule 26 becomes enforceable metadata (fabric/device on every observation, run, instance) |
| C0 meaning | **RESOLVED: the observation-to-identity boundary** — entity claims + binding claims + state observations; NOT persistent identity itself |
| System membership persistence | **RESOLVED: cover-capable.** Algorithmic exclusivity optional; the 540 cross-domain memberships become a REQUIRED REGRESSION COHORT |
| Fused position as identity | **RESOLVED: no.** Recognition/continuity evidence only; L4 identity is a minted serial + succession graph (predecessor/successor cardinality derives birth/retire/split/merge; ambiguity is a held state) |
| Bridge basis taxonomy | **RESOLVED directionally:** split into claim origin (PRODUCER_DECLARED/INDEPENDENTLY_OBSERVED/RULE_DERIVED/MODEL_INFERRED/HUMAN_ADJUDICATED) x verification (UNVERIFIED/CORROBORATED/CONTRADICTED/SUPERSEDED) x registry standing (CANDIDATE/ADMITTED/HELD/REJECTED/RETIRED). Supersedes the two-value `measured|inferred` in the L3 conditions — the store-declared uncovered member is now covered |
| Bridge population sequencing | **RESOLVED: after 3A.** The held L3 decomp @187528c95d remains a released-inert scaffold; NO cell is populated against free-text or parsed keys |
| Materializer identity | **RESOLVED:** MATERIALIZER serial (logical, durable) / MATERIALIZER_VERSION (immutable bundle: source tree + dependency lock + configuration + declared opinions + normalizers + runtime contract) / MATERIALIZATION_RUN (one execution, one fabric, one source frontier, immutable receipt). "One canonical materializer per layer" = one semantic identity + contract per layer, NOT one physical script |
| Provenance unit | **RESOLVED: SOURCE FRONTIER** (vector of source versions), never one scalar head. Frontier-vs-materializer split attributes any delta to source change or process change |
| Coherence semantics | **RESOLVED:** multi-axis evaluation (availability/integrity/currency/provenance/fabric-validity) against a DECLARED TARGET POLICY (LATEST_AUTHORITY/DECLARED_RELEASE/AS_OF_FRONTIER/HISTORICAL_REPLAY), emitted as an immutable timestamped record — never one mutable status field |
| Resolver failure semantics | **RESOLVED:** RESOLVED/AMBIGUOUS/GENUINELY_UNADDRESSED/SUBSTRATE_UNAVAILABLE/NOT_APPLICABLE — the two-state collapse in nerves_resolve is to be repaired |
| Monitoring mode | on-demand / at-build-time by default, per the standing moratorium — continuous watching only on Andrew's explicit word |

## WHAT REMAINS OPEN AT ANDREW (memoranda Appendix B.1, carried, not decided here)

1. Explicit PRD ratification (and whether the earlier D11 arc word already constituted it).
2. Product semantics of the 540 cross-domain memberships (persistence stays cover-capable regardless).
3. Canonical identity-minting authority + cross-fabric collision/reconciliation policy approval.
4. Retention/storage policy for immutable evidence bundles and run receipts.

## EFFECTS ON STANDING DECISIONS AND HOLDS AT THIS SEAT

- **DEC-02** (cover vs partition): the PERSISTENCE half is ruled (cover-capable). The product half
  (what the 540 mean) stays open at Andrew. The 540 regression-cohort requirement binds every
  clustering/materializer experiment from now on.
- **CVO 75229 condition 2** named `basis (measured|inferred)`: superseded by the three-axis taxonomy
  above by Andrew's ruling. `3.0.0_SA_CVO~X` certification rubric for any L3 decomp updates
  accordingly; the other three conditions stand unchanged.
- **PRD L4 language** "identity = position in the fused space": to be AMENDED before ratification —
  fused position is recognition evidence; identity is the minted serial. Amendment landed same
  commit as this record.
- **The L3 bridge decomp @187528c95d:** stays inert until 3A lands; then its 56 bridge cells are
  populated in 3A serials under candidate->admitted lifecycle, never from parses.

## EXECUTION SEQUENCE ADOPTED (WP-0..WP-8, from the implementation memorandum)

WP-0 evidence preservation (immediate, parallel) -> WP-1 PRD amend+ratify -> WP-2 Issue 3A contract
package (ENTITY, ENTITY_BINDING, STATE_OBSERVATION, IDENTITY_RELATION, MATERIALIZER,
MATERIALIZER_VERSION, MATERIALIZATION_RUN, SOURCE_FRONTIER, SURFACE_VERSION) under adversarial
schema validation -> WP-3 L0 + materializer migration (serials on all 42 parts; plural materializer
relations; Nessie _refs/_objs registered; grains/keys/failure_modes populated) -> WP-4 resolver
repair -> WP-5 symbol->file bridge slice -> WP-6 decisive two-view fusion experiment at file carrier
grain -> WP-7 Issue 3B coherence evaluator -> WP-8 L4 succession.

Acceptance is by the falsification battery (file-rename, Kuzu-rebuild, Nessie-advance,
same-frontier reproduction, wrong-fabric refusal, duplicate-mint reconciliation, parse-only-bridge
rejection, 540-cohort accounting, ambiguous-succession hold — full table in the memoranda).

— recorded by `1.0.0_SA_CTO~X`, 2026-08-27
