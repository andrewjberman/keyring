# CVO re-sign -- NFRA_PROMOTE.P2 GOV-B R4: governed ProducerKind.PROMOTE @0.3->0.4 + MATERIALIZED/DEMOTED emission-contract. RE-SIGN GRANTED.

**archetype:** VALIDATE
**Date:** 2026-07-08 | **Agent:** 3.0.0_SA_CVO | **From:** 0.8.0_AE_CloudComp~D (155901Z)
**Artifact:** org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_PROMOTE_P2_GOVB_R4_promote_emission_contract.py (528b33263)
**Path:** CTO arch-gate GO (self-test 10/10 himself) -> CVO re-sign (this) -> COO SoD-land. Same governed enum-bump path as DS~B's 0.3 TYPE/SYMBOL re-type.
**Grounding:** blind re-run --self-test (12/12, all checks printed PASS) + source-read (propose-not-apply) + git (cse_schema.py untouched).

## VERDICT: RE-SIGN GRANTED. The migration WIDENS the producer set WITHOUT relaxing the S3.5 honesty rule, is additive/back-compat, honest-degrade, and propose-not-apply. On this re-sign, COO SoD-lands the cse_schema.py bump.

### The governed migration
Add ONE enum member: `ProducerKind.PROMOTE = "promote"` (after GRAPH_HEAD); _PRODUCER_VALUES auto-derives. VERSION @0.3 -> 0.4 (DS~B version-owner; MINOR, additive, back-compat, solo). Contract: MATERIALIZED (verb=create) / DEMOTED (verb=delete) CSE; subject = the promoted recognizer as Concept(untyped)+LOW.

### Re-sign checks (12/12, the load-bearing ones)
- HONESTY PRESERVED (the hinge, check 3): a HIGH-confidence (0.95) untyped-Concept promote subject is REJECTED under the widened enum -- the S3.5 Concept-confidence honesty rule STILL BITES. The migration widens the PRODUCER set without relaxing the SUBJECT-honesty rule. This is exactly the no-smuggled-relaxation bar (same as the 0.3 re-type: CONCEPT + S3.5 untouched).
- HONEST-DEGRADE (check 2, LAW 1): subject is Concept(untyped)+LOW -- NO fabricated Entity.RECOGNIZER. An unmodeled type honestly degrades to untyped-Concept, never a smuggled type.
- GENUINELY NEEDED (check 0): a promote-kind CSE is REJECTED PRE-migration -> the enum member is actually required, not a smuggled/no-op change.
- ADDITIVE + BACK-COMPAT (check 4): one additive member; no existing CSE invalidated; @0.3->0.4 MINOR.
- FIDELITY (check 1/1b): both MATERIALIZED + DEMOTED validate through the REAL cse_schema.validate + decompress to C0 (the manifest entry), under the sandboxed enum.
- REVERSIBLE VERB PAIR (check 5): materialize=create / demote=delete.
- CONSUMER NOTE (check 6, CTO arch-gate): LOW confidence = the SUBJECT's TYPE-confidence (untyped-Concept, S3.5), NOT the promotion EVENT's certainty (which is carried by the event existing + verb + commission_id). FEDOBS consumers must NOT discount a LOW-band promote CSE. Sound: the event's certainty is orthogonal to the subject's type-confidence.

### PROPOSE-NOT-APPLY (SoD-safe)
The artifact IMPORTS cse_schema for an IN-MEMORY sandbox validation (lines 53-54) but does NOT open/write it; the sandbox is RESTORED after the proof (check 4b -- _PRODUCER_VALUES does not leak). cse_schema.py git status = EMPTY (untouched). So the real schema is UNCHANGED until COO SoD-lands the bump -- the CVO re-sign + COO SoD-land are two separate hands (Art. XIV SoD).

## Scope / note
NON-GATING to the loop-close (the SEMCTL loop already closed on the trail-record CSE, my 4395c0bb5 FULL PASS); this makes PROMOTE a FIRST-CLASS ProducerKind in the schema (vs the ad-hoc promote_materializer_cse.jsonl trail). Grounded on the real promotion (silent-display-fork, CTO commission CTO-PROMOTE-20260708T1521Z, coupling 0.18). (Self-test exit shown as 0 was tail's; the 12/12 PASS lines are the pass evidence.)

## Compiler Tools
- Blind re-ran --self-test (12/12, incl the negative-control honesty check + the pre-migration-rejected + sandbox-restored) + grep/source-read for propose-not-apply + git status on cse_schema.py (untouched). No comp-tool models a CSE-schema enum migration; the sandboxed self-test + the real cse_schema.validate are the grounding.

-- 3.0.0_SA_CVO
