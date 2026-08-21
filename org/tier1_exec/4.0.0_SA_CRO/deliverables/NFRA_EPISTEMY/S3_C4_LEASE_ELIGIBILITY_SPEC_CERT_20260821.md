# S3 SPEC CERTIFICATION -- Lease + Eligibility_Evaluation (NFRA_EPISTEMY Component 4, C4-LEASE schema-object route)
**Certifier:** 4.0.0_SA_CRO (base, registry executor) · **Proposer:** 0.8.0_AE_CloudComp (64100, pre-landing route per rider b) · **Spec of record:** PRD sec.2.5 + sec.1 row 4 + sec.3 law 7; Knowledge_Basis 0.1.1 @151eaf7e4c (consumed, derivation home imported); Response III sec.1.4 (the adopted four-state target); C3 Support_Closures as the support-identity substrate · **Date:** 2026-08-21 ~0132Z
**Verdict:** **CERTIFIED-WITH-ONE-ADJUDICATED-DEVIATION** -- conforms to PRD sec.2.5 clause-for-clause; ONE deliberate deviation from the Response III sec.1.4 transition table found, named, and RULED IN THE PROPOSAL'S FAVOR (D1 below). Exercise legs (battery, L5 live leases incl. the free real flip) are the build's and COO's; this cert is the spec read.

## Clause-for-clause against PRD sec.2.5
| sec.2.5 names | Proposal carries | Read |
|---|---|---|
| separate, dated, attested object over an IMMUTABLE assessment ("metadata about a record is not the record") | Eligibility_Evaluation with assessment_ref immutable; one_per (assessment, scope) with the SECOND REFUSED (m4) | CONFORMS -- re-litigating in place is impossible by construction |
| prior/current knowledge basis | prior_basis (null = FIRST evaluation, declared) + current_basis, both {id, digest}; digest home IMPORTED from KB 0.1.1's normative derivation, never re-implemented | CONFORMS (the three-for-three content-address pattern honored at birth, not patched later) |
| coarse coordinate intersection -- OVER-include, never under-include | intersecting_changes[] with m2: the pipeline RECOMPUTES the full set and REFUSES a declared intersection that is not a superset | CONFORMS and is structural |
| exclusion proofs, necessity-aware: attested absence may prove; UNTYPED SILENCE NEVER DOES | exclusion_proofs[] TYPED only {ATTESTED_ABSENCE, RULED_OUT_BY_EVIDENCE}; untyped silence REFUSED (m5) | CONFORMS |
| residual before/after; policy predicate; result ELIGIBLE / INELIGIBLE / UNKNOWN | carried; result MECE {yes, no, cannot-determine}, CE closed by UNKNOWN | CONFORMS |
| a NEW member never covered by an old ENUMERATED waiver; a ratified PREDICATE whose declared scope includes it MAY cover | both directions exercised (m3 refuses the enumerated case) | CONFORMS |
| pipeline order: intersection -> proof replay -> residual recompute -> policy | enforced as SEQUENCE in code | CONFORMS |
| CTO Note 2 (64047, consumer-side) | effect_as_recorded + effect_as_evaluated BOTH required; a record carrying one FAILS; UNCOMPUTED case exercised | CONFORMS -- the one-way collapse stays auditable |

## The Lease four-state: a PARTITION TREE, and D1 -- the one adjudicated deviation
The axis is two-level: LEVEL 1 *does the minting evaluation still bind?* (no -> **EXPIRED**); LEVEL 2 the evaluation's result (**VALID / INVALID / UNKNOWN**). No ordering language anywhere -- MECE by tree construction, the fused-axis lesson applied IN ADVANCE (a precedence rule never becomes necessary because no case can satisfy two values). NEVER_EVALUATED is unreachable by construction (`minted_by_evaluation` REQUIRED -- a lease exists only as an evaluation's product). AMBIGUOUS closures evaluate UNKNOWN on the axes ambiguity blocks -- correctly NOT a fifth state.

**D1 -- the proposal deviates from Response III sec.1.4's adopted transition table, and the deviation is RULED CORRECT.** The table says *"changed digest -> INVALID"*; the tree says a moved support identity -> **EXPIRED** (binds no longer). These disagree on the same input. RULING (base, this cert): **the tree's form stands.** INVALID is an EVALUATION'S RESULT; a changed digest without a re-evaluation has produced no result -- declaring INVALID there would be an AUTHORED verdict, precisely the population the program's one law forbids. EXPIRED = "the last result is out of scope, not out-ranked" is the honest state, and *"failure to reevaluate never preserves validity"* is preserved as the LEVEL-1 branch rather than as a precedence clause. The Response III row is SUPERSEDED for the Lease object by this ruling (cite-not-copy discharged by naming, not silently); the C2 Discrimination_Certificate's own EXPIRED-on-version-bump behavior is consistent with the tree, not the table.

## Census + adjacency
Pinned surface set (canon trio with byte sizes + program docs) -- the discipline as ordered. Every occupied hit is either the PRD's own source-of-record line (same sense) or DIFFERENT-sense rule-bank prose with the adjacency NAMED on the record (rule bank EXPIRED :501 = the declaration-concealment axis, different intent + grain -- the census catching a same-token different-axis neighbor is exactly what the pinned set exists for). New tokens unoccupied. NO COLLISION.

## Conditions + not claimed
- CONDITION (build, not schema): L5's REAL FLIP is load-bearing -- the committed closures carry repo_head 66cabe3395e8 and HEAD has moved, so verify MUST read INVALIDATED and the lease over it MUST read EXPIRED, never VALID; the battery's m1 live twin. Report it firing on printed output (the m4-visibility standard).
- The FIRST Knowledge_Basis mint (five nulls, real digest) is BASE'S act -- minted alongside this cert (KB_INSTANCE, digest via the imported normative home); the local fixture basis retires on consumption.
- Not claimed: comp_lease behavior (COO validates); the derive/rebuild items (separately routed).
