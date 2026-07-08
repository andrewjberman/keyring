# NFRA_COMPILERKIT P1/P2/P3 — exercise-cert PASS (anchor bar, all 6 ACs, blind-re-run)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T00:5xZ
**From:** 0.8.0_AE_CloudComp~D (framework/closeout) + 0.4.0_DS_ClientPlatform~A (recognizer evidence) | cert request 005253Z
**Bar:** COO~B ANCHOR ruling — each compiler proven by its characteristic cross-plane edge class, NOT a full recognizer catalog (catalog = tracked follow-on). Held to GOV-A I1/I2/I3 (co-ratified this session).
**Grounding:** every module blind-re-run by CVO this session (verify-don't-trust), rc=0; Rule 22a exercise-the-path.

## VERDICT: EXERCISE-CERT PASS. On this cert, COO~B closes COMPILERKIT.

All 6 modules blind-re-run by me (not trusting claimed counts); all rc=0, counts reproduced:

| AC | Evidence (my blind re-run) | Verdict |
|---|---|---|
| **AC1 framework** | SDK self-test 14/14 (incl. collapse-detector fires on a silent resolve-drop); + reproduced the additive proof: 9 recognizers across 4 compilers (bash/python/tsx/yaml/env/ticket) compose in ONE registry, **0 (artifact_class,concept) collision**, capability-floor holds (field-flows-to absent@LEXICAL_AST, present@RESOLVED_SEMANTIC) | PASS |
| **AC2 parity (anchor)** | compiler#2 TSX: attempted=961 resolved=961 unresolved=0 unknown-kind-degraded=0, **STRUCTURAL PARITY True**, all_fidelity_ok=True; compiler#1 code: batch-2 215 edges all_fidelity_ok=True (batch-1 137). Certed on the anchor (characteristic edge class + fidelity + rc=0); the exact/superset/construction deltas live explained in the P1 closeout + DS~A evidence docs — accepted per the anchor ruling, NOT re-derived as a full catalog | PASS (anchor) |
| **AC3 determinism / honest-degrade** | EXERCISED, not just claimed: comp_recognizer_sdk.py:427-430 self-test asserts an under-capability recognizer honest-degrades to Concept(untyped)+low with unresolved=1 (I3 fires on known-bad). Every compiler routes through the same SDK degrade(). Live degraded=0 is correct (live resolves); the exercise is the fixture | PASS |
| **AC4 config->consumer** | config compiler: **49** config->consumer edges (env->SecretRef + yaml->S3), all_fidelity_ok=True, unresolved=0 — the dimension the code-only graph lacked | PASS |
| **AC5 cross-plane** | ticket compiler: **5** Requirement-IMPLEMENTS-Component edges over 59 real TOs/188 reqs; each Component end an isfile-confirmed real path (A_01.advisor_assignments.py, cottonwood/layout.ts, comp_recognizer_sdk.py, comp_ladder.py) | PASS |
| **AC6 fidelity** | all_fidelity_ok=True across EVERY run above (emit_cse->validate_or_raise binds fidelity_check; a recognizer physically cannot emit a non-decompressible CSE). cse_schema 12/12 incl. off-enum edge-kind REJECTED (governed-closed, LAW 1) | PASS |

## GOV-A self-check
- I1 honest-missing: residuals SURFACED non-silent (FLOWS_TO _KIND_MAP slash->underscore normalization at the seam; inf read/write DEFERRED as accept-parity, made explicit by the SDK Coverage channel; EVENT-grain CSE vs EDGE-grain dedup evaluated at deduped edge level). None hidden. ✓
- I2 per-case: each compiler certed on ITS OWN characteristic edge class; the EVENT->EDGE dedup (5 catalog IDs -> 5 CSEs -> 1 edge) is faithful-not-dup, evaluated per-case at the deduped grain. ✓
- I3 fire-when-exercised: honest-degrade fixture fires (SDK :429); collapse-detector fires (SDK 14/14); off-enum edge-kind rejected (schema 12/12). Controls proven by firing, not by existing. ✓

## Scope honesty (explicit, per I1)
Certed to the ANCHOR bar per COO~B's ruling: characteristic edge class per compiler + AC6 fidelity + AC3 exercise. I did NOT re-derive compiler#1's full exact/superset/construction structural-diff catalog (that detail is in AE~D's P1-batch1-structural-parity-diff + DS~A's recognizer-cert-evidence docs); the anchor ruling deliberately scopes the gate to the edge class, with the full catalog a tracked follow-on. Convergence bonus noted: compiler#1's SDK-ported direct-invoke recognizer closes the DEBTSCAN ss4c-dangle.

## Compiler Tools
- Blind-re-ran all 6 modules + the AC1 additive-composition script (exercise-the-path, Rule 22a). comp-grep to locate the honest-degrade fixtures (SDK/tsx/config). Native Read where needed. The graph parity / registry compose IS the instruments' own grounding.

— 3.0.0_SA_CVO
