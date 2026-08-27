# ISCK ROUND-2 CHARTER — synthesis of the two external reviews (Andrew-supplied)

**Authority:** Andrew-direct at the `1.0.0_SA_CTO~X` terminal, 2026-08-27 ~19:4xZ — two inputs
supplied and ordered synthesized ("Yes let's synthesize that with the 4.0.0_SA_CRO~X feedback"):
1. **The GPT review** (relayed by Andrew): architecture APPROVED — *"Preserve the five-law
   structure, ten-record kernel, three-axis assertion model, provenance frontier, non-destructive
   reconciliation, and separated coherence axes. Do not freeze v0.1 yet."*
2. **The `4.0.0_SA_CRO~X` review** (Andrew-driven Codex seat, fourth instrument, fresh eyes;
   commission recorded @f789d08341): six material gaps + an exit-gate recommendation — *"excellent
   architecture, excellent first adversarial round... but not yet internally self-consistent enough
   to become the foundation it is meant to be."*

Plus the two probe-acceptance measurements (COO~X @a6704d677c: labels 9/13 risen-not-closed,
collisions PASS/F4 CLOSED, isolation 33/36 REGRESSED) — which independently corroborate CRO~X gap 5.

**Round 2's theme, both reviews in one sentence: TEMPORAL AND CROSS-RECORD SEMANTICS, not further
enum polishing.** DT~X's registered prediction is CONFIRMED early by CRO~X gap 3: entity and
materializer — two of the four unconditioned record types — carry current defects, not fixture debt.

---

## PRESERVED INVARIANTS (attack implementations, not these)

Five laws · ten-record kernel · three-axis assertion model (claim_origin ×
verification_standing × registry_standing) · source-frontier provenance · non-destructive
reconciliation · separated coherence axes. **v0.1 is NOT frozen and nothing populates.**

## THE WORKSTREAMS (owner: the pass; integrator: `1.0.0_SA_CTO~X`)

**R2-1 FABRIC SEMANTICS — the convergent headline (GPT + CRO~X gap 1, independent instruments).**
LAW 4 currently contradicts its own schema: state_observation/materialization_run REQUIRE
`fabric_id` unconditionally while their `fabric_invariant` arms forbid only `device_id` — both
invariant fixtures validate carrying `fabric_id: laptop`, so **the positive battery enshrines the
contradiction**. Remedy direction (both reviews agree): TWO fields — where the observation/run
OCCURRED (execution location, always known, always carried) vs which locality the REFERENCED STATE
claims (`fabric_invariant | fabric_local | device_local` — `fabric_local` is NEW, GPT's addition).
One overloaded `fabric_id` cannot express both truths.

**R2-2 APPEND-ONLY SEMANTICS + DERIVED STATUS (GPT).** Resolve how bindings and lifecycle statuses
change under an append-only ledger; make every `current_status` field an EXPLICITLY DERIVED
PROJECTION over the relation/event history (the two-clocks law applied to the contract's own
fields). Connects to §6 limit 6 (LAW-3 has no enforcement plane until the ledger).

**R2-3 WARRANT COMPLETION (GPT + CRO~X gaps 2–3).** (a) claim_origin arms EVERYWHERE the shared
enum is consumed — `entity_binding.binding_basis = independently_observed` currently validates with
no evidence AND IS THE POSITIVE FIXTURE; (b) lifecycle warrants — `contested` with no adjudicator
and `superseded` with no successor both validate today; (c) ALL affirmative coherence verdicts
require warrants + **RESOLVED comparators** (a target named but never resolved is a verdict about
nothing).

**R2-4 SPLIT REMAINING MIXED TEMPORAL/EPISTEMIC AXES (GPT).** Sweep every enum for values mixing
when-it-happened with how-well-we-know; split where found.

**R2-5 OBSERVATION OF ABSENCE (GPT).** Represent a SUCCESSFUL observation that the referent is
ABSENT — distinct from `substrate_unavailable` (could not look) and `not_applicable`. The
nerves_resolve lesson one level down: absence-as-a-finding needs a first-class cell.

**R2-6 FRONTIER COHERENCE (CRO~X gap 4).** A frontier carrying the same source coordinate twice
with different versions validates today. Semantic uniqueness key — candidate
`(source_serial, identity_space, authority_ref, fabric_id)` — plus a conflicting-version mutant.

**R2-7 MINT RECEIPT (GPT).** Define the mint-receipt record BEFORE operational certification —
closes §5's named-incomplete compensating control on LAW 1.

**R2-8 BRIDGE_ASSERTION (GPT).** Either the record lands in the round-2 boundary or its companion
schema freezes simultaneously with ISCK — it is the FIRST LOAD-BEARING CONSUMER, and CV-1's carried
requirement (`admitted -> evidence_refs`) binds it.

**R2-9 BATTERY MATURATION (CRO~X gap 5 + COO~X acceptance numbers).** Committed probes are part of
the package: **every declared gate passes FROM A CLEAN CLONE.** Work the measured findings: labels
9/13 (four records missing postulate labels — `registry_standing` missing state-coherence is the
THIRD occurrence of that one axis being the under-recorded one; pattern flagged); isolation 33/36
(three non-isolating mutants — diagnose redundant-enforcement vs real); coverage (4 record types
structurally unexamined, 6 candidate gaps); inhabitability (7 values without companion repairs).
**Per-rule ABLATION controls, not only one gutted-schema test** (CRO~X): delete each rule in a
copy, assert its mutants flip. Denominator settled: §3 holds 13 ENUM records + 3 non-enum
subsections — gates run against 13.

**R2-10 VERSION IDENTITY (CRO~X gap 6 — fixed for round 1 in the same commit as this charter).**
"v0.1" briefly named two byte-distinct contracts (21d6fc7325 then 55b82489df). BOUNDARY_ROUND1.md
now pins attacked-input commit, boundary-output commit, post-boundary amendments, and the final
schema digest. STANDING RULE: every boundary names all four, forever — the identity ambiguity ISCK
exists to kill does not get to live in ISCK's own version history.

## THE EXIT GATE (operational-use gate; distinct from schema freeze — GPT's distinction, adopted)

**SCHEMA FREEZE ≠ LEDGER-BACKED PRODUCTION CERTIFICATION.** Round 2 exits when:
1. R2-1 through R2-10 are resolved or explicitly carried with owners;
2. every declared gate passes via `run_gates.sh <tip>` — an ATOMIC GIT-ARCHIVE EXTRACT of the
   cited commit (DT-R2-3: a live working tree is not atomic; a gate run during any landing samples
   a torn state and fakes either colour) — AND, at exit time, that cited tip is ON ORIGIN, so the
   extract reproduces from a true clone (COO~X: the file-copy and git-clone readings of
   "clean clone" disagree whenever commits are local; the exit gate takes the stricter one, and
   the integration window is therefore part of the exit path);
3. **the VERTICAL-SLICE END-TO-END BATTERY passes** (GPT, the operational gate): one flow covering
   minting → binding → RENAME (serial survives) → state observation → DUPLICATE PROVISIONAL
   RECONCILIATION (non-destructive) → materialization from a source frontier → NESSIE AUTHORITY
   ADVANCEMENT (projection reports behind its declared target) → KUZU DISLOCATION DETECTION →
   HISTORY PRESERVATION (nothing rewritten).
Passing that slice — not any review's approval — is the gate for operational use.

## POST-ROUND-2 INTEGRATION TARGET (CRO~X, recorded for WP-3)

Integrate ISCK into the scratchpad realization by converting current semantic slugs into native
bindings while RETAINING existing digest identities for immutable generations, commits, and
receipts — the migration is a REBIND, not a re-mint, which is the contract eating its own cooking.

## PROCESS NOTES BINDING THIS ROUND

Round 2 is NON-BLIND (declared at the round-1 boundary); agreement is shared-context convergence.
`4.0.0_SA_CRO~X` enters as a live, Andrew-driven fourth instrument (MSTR disposition update
76568; the 18:43–19:34Z superseded window still voids anything dated inside it). Dispositions go
seat-direct; the tally lands at the round-2 boundary with its four version pins.

— synthesized and recorded by `1.0.0_SA_CTO~X`, 2026-08-27, on Andrew's word; both source reviews
quoted from his relay at this terminal.
