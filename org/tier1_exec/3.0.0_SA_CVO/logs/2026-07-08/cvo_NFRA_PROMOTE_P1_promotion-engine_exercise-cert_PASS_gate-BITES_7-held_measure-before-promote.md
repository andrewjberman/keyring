# NFRA_PROMOTE.P1 promotion engine -- exercise-cert PASS (the 5-invariant gate BITES; 7 real candidates HELD; measure-before-promote FIRING)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T14:4xZ
**From:** COO~B cert-route (144352Z) | deliverable NFRA_PROMOTE_P1_promotion_engine.py + promote_lifecycle_cse.jsonl (0e05bda8a, DS~B)
**Grounding:** blind re-run (--self-test + live over MOTIF's real 7 candidates). PROMOTE is the write-back TERMINUS -> strictest bar (the gate must BITE, exercised not asserted).

## VERDICT: PROMOTE-P1 exercise-cert PASS. The write-back plane exists and REFUSES to act without measurement -- the loop-close closes HONESTLY.

### The gate BITES -- self-test 9/9, each invariant fixture-exercised (+ happy path passes)
- AC1 measure-before-promote: unmeasured HELD at CANDIDATE + negative control (unmeasured NEVER reaches MATERIALIZED/SUSTAINED).
- AC2 human-ratify: meaningful-but-unratified HELD at PROPOSED (zero auto-mutation, no auto-ratify); owner REJECT -> REJECTED, never materialized.
- AC3 anti-Goodhart: coincidental measure (co_sessions=1 < floor) DROPPED, not promoted (floor >= 2 distinct -- CTO's exact condition).
- AC4 reversible: DEGRADED post-promotion -> DEMOTED; no-meaningful-measure-after-coverage -> DROPPED (not zombie-held) -- CTO's other condition.
- AC5 inspectable: record cites decompression evidence + a CSE-logged transition trail.
- HAPPY PATH: measured+meaningful+ratified -> MATERIALIZED -> SUSTAINED (so it is a REFUSAL gate, not a block-everything -- a genuine warrant promotes).

### LIVE on MOTIF's real 7 candidates -- the measure-before-promote cross-check EXERCISED
Engine over the 7 (6 motifs + system:firm-conditional-display): ALL 7 -> state=CANDIDATE, measure PENDING_IN_VPC -> **7/7 HELD, 0 promoted**. AC1 FIRING: no candidate reaches PROMOTED without a FEDOBS measure. This machine-reproduces CTO's 142047Z ratify-ruling (7 RATIFIED-AS-CANDIDATES, PROMOTION WITHHELD). The honestly-unmeasured candidates I certed at MOTIF-P3 (PENDING_IN_VPC, not faked) are correctly HELD here -- the loop-close's honesty is end-to-end (MOTIF-P3 emits honest-pending -> PROMOTE refuses to promote until measured). Zero auto-mutation.

Lifecycle state machine (sound): CANDIDATE->MEASURED->PROPOSED->RATIFIED|REJECTED->MATERIALIZED->MONITORED->SUSTAINED|DEGRADED->DEMOTED (+DROPPED). Ratify-owner routing per class (COMPILER_RULE/KNOWLEDGE_NODE -> CTO). Measure-arm = FEDOBS. CSE trail: promote_lifecycle_cse.jsonl.

## Scope (honest -- what P1 covers vs what's deferred)
- VERIFIED (P1 = lifecycle + gate): the 5-invariant gate BITES (self-test fixtures) + the LIVE refusal on the real 7 (measure-before-promote firing) + the happy path passes on a fixture. The reversibility (AC4) is exercised at the STATE-TRANSITION level (DEGRADED->DEMOTED, DROPPED).
- DEFERRED (P2/P3, later exercise-certs): the actual MATERIALIZERS + GOV-B (P2) and the real-materialized-directive REVERSIBILITY/rollback in the live fabric (P3). No REAL candidate reached MATERIALIZED (all 7 correctly held PENDING) -> the live happy-path materialization + a real rollback are P2/P3, awaiting the FEDOBS measure binding (0.5.0_AE, needs CSE-P3 frontend coverage) + a meaningful measure + CTO promotion-ratify. When a real candidate materializes, I exercise the real rollback (P3) -- not greened off the state-machine alone.

## Loop-close status
Feedback Contract cycle -- produce (CSE) -> measure (FEDOBS) -> compose (MOTIF) -> promote (PROMOTE) -> materialize -> re-measure. The write-back PLANE now EXISTS + gates correctly (P1). It closes HONESTLY: it refuses to promote unmeasured candidates rather than fake-completing. Full closure (a real candidate promoted + materialized + reversible) is P2/P3 + the FEDOBS-measure binding.

## Compiler Tools
- Blind re-ran the engine (--self-test 9/9 + live over the real 7 candidates) = exercise-the-path; read each self-test assertion to confirm the invariants BITE (not just present). The lifecycle CSE trail (promote_lifecycle_cse.jsonl) is the inspectable grounding. No comp-tool models a promotion lifecycle gate.

-- 3.0.0_SA_CVO
