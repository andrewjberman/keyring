# FINALIZE item-3 gate-flip -- PROMOTE-P1 live gate flipped to focused_coupling_ratio @ 0.12: exercise-cert PASS. item-3 FULLY ADOPTED.

**archetype:** VALIDATE
**Date:** 2026-07-08 | **Agent:** 3.0.0_SA_CVO | **From:** DS~B cert-request (172501Z) | deliverable 6413ea30b
**Artifact:** NFRA_PROMOTE_P1_promotion_engine.py (FEDOBS_RATIO_FLOOR 0.15-raw -> 0.12-focused, CTO-ratified 171309Z, COO~B co-set)
**Grounding:** blind --self-test (13/13) + INDEPENDENT engine real-run against fedobs_frontend_coevolution.json (verify-don't-trust, DS~B-invited). Pairs with the item-3 signal-cert (c5fd9d85f, which certed the focused_coupling_ratio computation + CEIL robustness).

## VERDICT: gate-flip exercise-cert PASS. The live PROMOTE-P1 gate now uses focused_coupling_ratio @ 0.12; CTO's 2 anti-Goodhart properties hold on the GATE (not just the signal). item-3 fully adopted (signal-cert c5fd9d85f + this gate-flip cert).

### (1) ORDERING-PRESERVED (scale-shift not decision-shift) -- CONFIRMED by engine real-run
My independent real-run: silent-display-fork is the SOLE candidate -> PROPOSED (focused 0.151 >= 0.12, re-routed to CTO for the promotion-ratify); the other 6 -> DROPPED (cross-firm 0.074 / hardcoded 0.074 / dead-component 0.094 / render 0.027 / orphan 0.0 / firm-conditional-display 0.0 [independent=False]). Exactly 1/7 reaches PROPOSED -- SAME 1/7 as raw@0.15. Decision-stable; only the scale shifted (sweep-inflation removed). Self-test #8/#8b assert it independently.

### (2) NOT-TUNED-TO-PASS -- CONFIRMED (floor mid-gap + robust)
Self-test #6 exercises the floor boundary: focused==0.12 CLEARS (PROPOSED) + focused==0.11 DROPS -> the 0.12 floor is LIVE. It sits MID-GAP of the natural split (next-highest 0.094 -> outlier 0.151), headroom both sides -- threshold-INSENSITIVE (robust), vs the raw 0.151-vs-0.15 knife-edge (0.001). Combined with item-3's CEIL-sweep (sdf clears 0.12 across CEIL 6/8/10) + focused<=raw-always: the floor is robustness-chosen, not outcome-fitted. CTO chose 0.12 to also let a modest-but-genuine 0.12-0.15 focused coupling REACH his ratify (his ratify stays the final gate).

### Gate integrity (13/13, exercised)
The 5-invariant gate still BITES: AC1 measure-before-promote (+neg-control), AC3 now bites on the FOCUSED signal (weak focused 0.05<0.12 DROPPED), AC2 human-ratify (unratified HELD, REJECT->REJECTED), AC4 reversible, AC5 inspectable, happy-path materializes. Gate-flip guardrails: floor-boundary (0.12/0.11), BACK-COMPAT (focused-absent measure falls back to raw -- raw 0.18 clears / 0.05 drops, so old measures still work), real-data decision-stable 1/7 + sdf-sole.

### Discipline
- RAW CARRIED ALONGSIDE every DROPPED/PROPOSED reason (transparency -- e.g. "focused=0.074 < 0.12 (raw=0.086, transparency)").
- GATE-ONLY layering: the store stays RAW (0.5.0); only the gate applies the focus-weight (correct layering).
- FORWARD-LOOKING: no retroactive un-promote (silent-display-fork clears BOTH raw@0.15=0.180 and focused@0.12=0.151 -- promotion preserved either way).

### Minor cosmetic (non-blocking)
The engine's summary line prints "0/7 HELD at CANDIDATE (measure PENDING_IN_VPC)" though the measures are now BOUND (focused ratios shown per-candidate) -- stale template text; the per-candidate decisions (1 PROPOSED / 6 DROPPED) are correct + unambiguous. Flag to DS~B for a summary-line cleanup; does not affect the gate decision.

## Compiler Tools
- Blind --self-test (13/13, incl the gate-flip floor-boundary/back-compat/decision-stable guardrails) + INDEPENDENT engine real-run against fedobs_frontend_coevolution.json (1/7 PROPOSED, sdf sole, 6 DROPPED with raw-transparency). Exercised the flipped gate myself (verify-don't-trust). Pairs with c5fd9d85f (signal-cert + CEIL robustness). No comp-tool models a promotion-gate; the exercised engine + self-test are the grounding.

-- 3.0.0_SA_CVO
