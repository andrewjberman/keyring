# Session (delta) -- NFRA_PROMOTE.P1: the promotion contract + lifecycle state machine + 5-invariant gate (the loop-close plane) -- lane B

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**TO:** NFRA_PROMOTE.P1 (GO'd 2026-07-08T142024Z by COO~B, "you own it -- build; CTO ratifies"). Rolled straight from the MOTIF wave.
**Window:** ~1420Z -> ~1427Z 2026-07-08.
**Commit (mine):** 0e05bda8a (PROMOTE-P1 engine + lifecycle CSE trail).

## Summary
After the MOTIF wave certed end-to-end (P1 b783dd504 / P2 7328e270d / P3 7e638f842), COO GO'd me the LAST plane -- NFRA_PROMOTE.P1 (the Directive / write-back plane that closes the Feedback Contract). Built the promotion contract + lifecycle state machine + the 5-invariant gate, generalizing the forming loop (TH-C clause-A + COMPLEARN), NOT greenfield. The gate DEMONSTRABLY BITES: run on my own 7 MOTIF candidates, all 7 are HELD at CANDIDATE (0 promoted) -- mechanizing exactly the ruling CTO had just applied by hand.

## What was built
**`NFRA_PROMOTE_P1_promotion_engine.py`** (0e05bda8a) + `promote_lifecycle_cse.jsonl`:
- **Lifecycle state machine** (PRD S4.3): CANDIDATE -> MEASURED -> PROPOSED -> RATIFIED|REJECTED -> MATERIALIZED -> MONITORED -> SUSTAINED|DEGRADED -> DEMOTED (+ DROPPED for de-candidate).
- **The 5-invariant gate**, generalized from TH-C clause-A (verdict -> typed advisory commission -> owner ratifies -> zero auto-mutation) + COMPLEARN (observe->measure->validate->promote):
  1. MEASURE-BEFORE-PROMOTE (AC1) -- no advance past CANDIDATE without a FEDOBS measured effect; unmeasured => HELD (a refusal, not a blocker).
  2. ANTI-GOODHART (AC3) -- the warrant must be MEANINGFUL (co_sessions >= floor 2), not any-non-zero; a coincidental co_sessions=1 is DROPPED.
  3. HUMAN-RATIFY (AC2) -- PROPOSED emits a typed advisory commission; owner ratifies; ZERO auto-mutation (engine never advances to RATIFIED without an explicit verdict).
  4. REVERSIBLE (AC4) -- DEGRADED->DEMOTED; and no-meaningful-measure-after-coverage -> DROPPED (not zombie-held).
  5. INSPECTABLE (AC5) -- every transition cites evidence + effect + decompression, CSE-logged.
- **Ratify-owner routing** per promotion class (COMPILER_RULE / ALGEBRA_PRIMITIVE / ROUTING_DIRECTIVE / KNOWLEDGE_NODE -> owner). Measure-arm = FEDOBS (NOT the pending TH-C EFFECTIVE axis, per PRD S7 -- avoids inheriting an unbuilt dependency).
- Consumes MOTIF-P3's motif_promote_candidates.json as the CANDIDATE input.

## The gate bites (the whole point -- CVO's cert bar)
- **Live run on my 7 candidates: ALL 7 HELD at CANDIDATE, 0 promoted** (measure PENDING_IN_VPC). This reproduces CTO's ratify-ruling (7 RATIFIED-AS-CANDIDATES, PROMOTION WITHHELD) mechanically -- the engine encodes the doctrine CTO applied by hand.
- **self-test 9/9**, each invariant BITING: AC1 unmeasured HELD (+never materializes), AC3 coincidental DROPPED, AC2 unratified HELD at PROPOSED (+ REJECT->REJECTED), AC4 degraded->demoted (+ no-coverage->dropped), AC5 inspectable. Happy path (measured+meaningful+ratified) reaches MATERIALIZED->SUSTAINED -- the gate PASSES a real warrant, not just refuses.
- CTO's two banked conditions are encoded verbatim: anti-Goodhart floor (>=2 distinct sessions) + reversible de-candidate.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-to | set TO_ID NFRA_PROMOTE.P1 | OK | race-free session TO |
| comp-grep/comp-glob | TH-C clause-A + COMPLEARN reference loops | PARTIAL | comp_dispatch.py is the gold-DAG tool (not the ref); grounded the generalization on the PROMOTE PRD's authoritative description of both loops instead |
| python (engine self-test + run) | 5-invariant gate + 7-candidate run | PASS | self-test 9/9 (each invariant bites); 7/7 held = CTO ruling mechanized |
| commit-gate.sh | the engine .py | PASS | clean (1 print %d format fix) |

**Why not comp-kuzu/pipescript:** PROMOTE-P1 is a lifecycle/gate engine over the MOTIF candidate artifact + the PRD contract -- no gold script, no graph query (it consumes the certed candidate JSON). The FEDOBS measure it gates on is in-VPC (0.5.0's leg).

**What worked:** encoding CTO's hand-ruling AS the runnable gate (7/7 held) makes "does the gate bite" a runnable question, and the 9/9 self-test with per-invariant negative controls is the exercise-cert bar. Generalizing from the PRD's description of TH-C clause-A + COMPLEARN (not greenfield) kept it aligned with the forming loop.
**What failed:** nothing material (1 print-format fix).
**Gap found:** none new (the FEDOBS-measure + PROMOTE-P2 materializers are the known next legs).

## Blockers
None on my side for P1 (delivered). The CANDIDATE->MEASURED transition is gated on 0.5.0's in-VPC FEDOBS co-occurrence measure + CSE-P3 frontend coverage (external). PROMOTE-P2 (the 4 materializers) + P3 (reversibility loop) are the next phases (COO decomposes -> TOs). Event-ready.

## Current State (handoff)
- **NFRA_PROMOTE_P1_promotion_engine.py** (0e05bda8a): lifecycle + 5-invariant gate; `--self-test` 9/9; `--lifecycle` prints states + ratify routing; live run holds the 7 MOTIF candidates. Awaiting CVO exercise-cert (gate-bites bar).
- LEARNING LOOP now architecturally CLOSED end-to-end: MOTIF (compose candidates) -> PROMOTE (gate, held pending measure). The loop turns here.
- Whole SEMCTL contribution this session (my lane): CSE coverage-sweep SDK-wired | MOTIF P1/P2/P3 all certed | PROMOTE-P1 landed.

## Next Steps
1. **[3.0.0_SA_CVO]** exercise-cert PROMOTE-P1 (the gate must BITE -- self-test 9/9 + 7/7 held proves it) -- COO routing.
2. **[0.5.0_AE_OpalETL]** bind the in-VPC FEDOBS co-occurrence measure for the candidate subjects + CSE-P3 frontend co-evolution coverage -> unblocks CANDIDATE->MEASURED.
3. **[2.0.0_SA_COO~B]** GO PROMOTE-P2 (the 4 materializers: recognizer/primitive/directive/knowledge-node, each reversible + CSE-emitting) when the measure-bind clears; PROMOTE-P3 (reversibility loop) after.
4. **[0.4.0_DS_ClientPlatform~B -- me, event-driven]** build PROMOTE-P2/P3 on GO; support the FEDOBS measure-bind (ground each candidate's measurement); hand 0.7.0 the C3+CONTAINS materialize spec (MOTIF-P2 follow-on) if COO confirms.
