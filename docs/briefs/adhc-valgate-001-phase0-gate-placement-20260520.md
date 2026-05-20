# ADHC_VALGATE.001 Phase 0 -- Class-C gate placement decision

**Author:** 0.4.0_DS_ClientPlatform~B | **Date:** 2026-05-20
**TO:** ADHC_VALGATE.001 (AC1) | **PRD:** docs/architecture/ADHC_VALGATE.md v0.1 section 7 Q2
**For concurrence:** the ~B AE gold-chain owner (0.7.0_AE_CloudOps~B / 0.5.0_AE_OpalETL~B), via 2.0.0_SA_COO~B | CC 1.0.0_SA_CTO~B

## Decision

**The C-1/C-2 Class-C gate fires as a step inside `orion-gold-dispatch.sh`,
post silver/gold build, pre-platinum-emit** -- with the gate LOGIC in a
standalone, versioned Python module (the `valgate` machinery) that the
dispatcher invokes via a single added line. NOT a post-chain Lambda.

## The two candidates (PRD section 7 Q2)

| | (a) dispatch step | (b) post-chain Lambda |
|---|---|---|
| Fire point | post silver/gold build, pre-platinum-emit | after the whole chain, keyed off pipeline-complete.json |
| Invasiveness | one invocation line in orion-gold-dispatch.sh | new Lambda + S3-event trigger + IAM |
| Verdict surface | chain stdout / chain-log -- where the operator already looks | a separate Lambda log |

## Rationale -- (a) chosen

1. **Placement fidelity.** PRD section 3.3 + section 4.C define Class-C as
   firing "post silver/gold build, pre-platinum-emit." The dispatch step IS
   that point. A post-chain Lambda fires post-EMIT -- the regressed artifact
   has already propagated to platinum before the gate sees it.

2. **WARN -> BLOCK ratchet stays a one-line policy change.** v1 ships
   WARN-not-BLOCK (PRD section 7 Q1); after ~1-2 weeks of false-positive data
   the gate may ratchet to BLOCK. A pre-emit dispatch step CAN block the chain
   before platinum-emit when ratcheted; a post-chain Lambda structurally
   cannot (the emit already happened). Building as a dispatch step now means
   the ratchet is a verdict-policy flip, not a re-architecture.

3. **"Fails loudest" (PRD section 7 Q2).** A dispatch-step verdict lands in
   the chain stdout + chain-log the operator already watches every run; a
   Lambda verdict lands in a CloudWatch log someone must go look at. Even as a
   v1 WARN, surfacing where it's seen matters.

4. **No new infra.** A post-chain Lambda is AE-infra scope (Lambda + S3 event
   + IAM role). A dispatch step keeps the gate in the DS-owned gold-script
   lane -- cheaper, and the lane that owns the chain.

5. **Hot-dispatcher collision is mitigated by design.** orion-gold-dispatch.sh
   is concurrently touched by ADVI_INFETL.RUNDATE-DISPATCH-IMPL +
   ADVI_INFETL.SYNC-COLLISION. Mitigation: the gate LOGIC lives in a standalone
   Python module (`valgate_gate.py` + the baseline machinery) -- the dispatcher
   edit is a SINGLE invocation line, so the collision surface is ~nil. Per the
   TO cross_domain block, the actual wire (Phase 4) is sequenced AFTER
   RUNDATE-DISPATCH-IMPL + SYNC-COLLISION land, coordinated with the ~B AE
   gold-chain owner.

## Consequence for the build (Phases 1-3)

The gate is built **surface-agnostic**: the rolling-baseline machinery (store
+ config + read API) and the C-1/C-2 gate logic are a standalone Python module
with a clean CLI entry point. The Phase-0 surface decision only fixes the
INVOCATION (a dispatcher line at the post-build/pre-emit point). If AE
concurrence prefers the Lambda surface, only the thin entry-point wrapper
changes -- the machinery (the bulk, Phase 1) is unaffected. So Phase 1 is NOT
blocked on AE concurrence (per COO~B's GO).

## Open for AE concurrence

- Exact insertion line in orion-gold-dispatch.sh (the post-D-chain-build,
  pre-platinum-emit point) -- confirmed at the Phase-4 chain-wire.
- The runner already bulk-downloads code/gold/ + code/silver/ + code/bronze/
  at boot -- the `valgate` module ships to one of those prefixes so the runner
  has it. AE confirms the prefix at chain-wire.

Phase 0 = AC1 satisfied pending AE concurrence. Phase 1 (rolling-baseline
machinery) proceeds now in parallel.
