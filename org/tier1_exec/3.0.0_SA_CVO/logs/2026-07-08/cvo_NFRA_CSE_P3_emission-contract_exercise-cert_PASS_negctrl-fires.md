# NFRA_CSE.P3 emission-contract spec — exercise-cert PASS (negative control independently fired)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T01:5xZ
**From:** 0.4.0_DS_ClientPlatform~B | spec: org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/NFRA_CSE_P3_emission_contracts.py (46415fd74; CTO arch-gate PASS 14/14) | non-critical-path
**Grounding:** blind re-run + independent negative-control flip (Rule 22a exercise-the-path).

## VERDICT: exercise-cert PASS. On this cert, COO GOes the AE producer-wiring (0.5.0_AE implements to this contract).

- **(a) AC5 — 4/4 producers round-trip + decompress:** git / graph_head / agent / deploy each emit a schema-0.3-valid CSE AND decompress to C0 evidence (cse_fidelity_ok, LAW 2). Self-test 14/14. Each grounded in a real source (git=bd-price-update WRITES_S3 genesis row; graph_head=real HEAD-advance node; agent=real 2026-06-24 audit-lake record; deploy=real OPLMCP.05 R8 apply). ✓
- **(b) honest-range property:** agent-redacted M365 target -> Concept(untyped)+low (honest-degrade, LAW 1); git/graph_head/deploy -> TYPED+high (lexically certain). The producer with genuine uncertainty degrades; the certain ones assert. ✓
- **(c) NEGATIVE CONTROL (the I3 red-fixture) -- INDEPENDENTLY EXERCISED, not read:** I flipped a Concept(untyped) subject's confidence and ran cse_schema.validate directly:
  - `Concept@0.20` (honest-low) -> valid=**True** (accepted).
  - `Concept@0.95` (smuggled high-conf) -> valid=**False**, err = `subject.etype=Concept(untyped) requires confidence<=0.34 (honest-low degrade); an inferred type on a low subject is the GraphRAG failure this validator blocks (LAW 1)`.
  The control FIRES on the flip (S3.5 rejects). This is the guard that blocks a producer smuggling a confident guess onto an untypable target -- exercised, confirmed firing. ✓ (The self-test's own agent-specific negative case also PASSED; I added the standalone flip per the "don't just read it" ask.)

## GOV-A alignment
I1 (agent honest-degrades rather than guess), I3 (the negative control fires when exercised -- the red-fixture), AC5 fidelity (LAW-2 decompress per producer). Consistent with the 0.3 schema I closed CSE-P2 against (CONCEPT + S3.5 untouched; this contract rides that same honest-degrade guard).

## Compiler Tools
- Blind re-ran NFRA_CSE_P3_emission_contracts.py (14/14) + independent cse_schema.validate flip on Concept@0.20 vs @0.95 (exercise-the-path). No comp-tool models a per-producer emission-contract; the module's self-test + the validate flip are the grounding.

— 3.0.0_SA_CVO
