# NFRA_PROMOTE.P2 DS-materializers -- exercise-cert PASS (proposes-not-applies + reversible round-trip + gated); DS half of P2

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T14:5xZ
**From:** COO~B cert-route (145004Z) | deliverable NFRA_PROMOTE_P2_materializers.py (6577989fa, DS~B)
**Grounding:** blind re-run (--self-test 15/15) + source-read of the materialization contract (auto_mutation + demote inverse). Write-back plane -> strictest bar.

## VERDICT: PROMOTE-P2 DS-materializers exercise-cert PASS (machinery + gate). LIVE real-materialization + real-rollback deferred to the acceptance-run/P3.

3 materializers, each wired to the P1 lifecycle: ALGEBRA_PRIMITIVE -> governed CSE schema migration; ROUTING_DIRECTIVE -> router explicit heuristic; KNOWLEDGE_NODE -> graph named-capability node. Self-test 15/15 (3 x {produces / auto_mutation-False / reversible-round-trip / CSE} + 2 neg-controls + serializable).

### The 3 hard properties -- exercised
1. **ZERO AUTO-MUTATION (the write-back honesty)**: source :66 `auto_mutation: bool = False # ALWAYS False -- proposes, never writes the substrate`; self-test 1a/2a/3a confirm auto_mutation is False for all 3. The "materialization" is a PROPOSAL/handoff artifact, NOT an auto-applied change -- the live fabric is NEVER auto-mutated; the real apply is a separate human/explicit step. This is the strictest + correct write-back safety: the terminus proposes, it does not silently write.
2. **REVERSIBLE (exact-inverse round-trip)**: source :64 `demote: dict # the exact inverse (reversibility, invariant #4)`; :150 `demote(m, reason)` applies `m.demote` + emits a demote CSE. Self-test 1b/2b/3b: demotion INVERTS the apply + round-trips. Fixture-exercised (the machinery reverses).
3. **GATED-ON-RATIFIED (anti-auto-mutation gate bites)**: neg-controls -- an unratified/unmeasured promotion is REJECTED (no materialization); an anti-Goodhart-DROPPED candidate is NOT materializable. The gate bites on the materializer, not just the P1 lifecycle.
4. INSPECTABLE (invariant #5): every materialize + demote emits a CSE; the materialization is a serializable handoff artifact.

## Scope (honest -- what P2-DS certs vs what's deferred)
- VERIFIED: the materializer MACHINERY + the gate + the reversibility ROUND-TRIP on a fixture + zero-auto-mutation (proposes-not-applies). 15/15, source-confirmed.
- DEFERRED (acceptance-run / P3): the LIVE materialization of a REAL ratified candidate (a proposed materialization actually applied) + the REAL rollback of that applied artifact. These await the FEDOBS measure-bind (0.5.0) + a meaningful measure + CTO promotion-ratify -- no real candidate is measured yet (all 7 HELD PENDING at P1). My P3 bar stands: I exercise the REAL rollback on a real APPLIED materialization (not the fixture round-trip) + the 2-part producer acceptance (git-grounded real signal + gate-bites-on-real).
- SEPARATE (not this cert): ~D's GOV-B / recognizer-materializer half of P2 -- comes when ~D spawns; my GOV-B bar (I1/I3 on the producer) is locked.

## Loop-close note
Because auto_mutation=False (proposes-not-applies), the write-back terminus NEVER auto-mutates the fabric -- it emits a proposal + a human applies. That means "loop closed" = a real candidate PROPOSES a materialization on real measurement + a human applies + it's reversible -- not an autonomous self-modification. The honesty + safety are structural: the loop cannot silently rewrite the estate.

## Compiler Tools
- Blind re-ran --self-test (15/15) + source-read the materialization dataclass (auto_mutation False, demote exact-inverse) = the machinery + hard-property verification. No comp-tool models "does this materializer auto-mutate / reverse"; the self-test + source are the grounding (Rule 22 mechanism-read for the auto_mutation/inverse claim).

-- 3.0.0_SA_CVO
