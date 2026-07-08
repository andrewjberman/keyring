# LOOP-CLOSE terminus/acceptance cert -- FULL PASS (CSE-emit fix VERIFIED on the real path) -- the SEMCTL federated learning loop is CLOSED on real data

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T15:3xZ
**From:** DS~B fix + re-materialize (c61f3b11c) | supersedes the CONDITIONAL PASS (0b0299159) -- the one held condition is now CLOSED.
**Grounding:** git spot-check of the co_session shas + EXERCISED self-test (7/7 incl the new durable-CSE checks) + the REAL MATERIALIZED CSE now in the trail + source-confirmed shared write-point. Verify-don't-trust, exercised.

## VERDICT: FULL PASS. The SEMCTL federated learning loop is CLOSED clean on real data -- first real promotion end-to-end (observe -> measure -> validate -> promote -> materialize), with an inspectable write-back CSE trail. Honesty held at every gate.

The CONDITIONAL PASS's single held condition (R4/AC5 durable CSE emission) is now VERIFIED FIXED. All three acceptance parts + human-ratify hold:

### (i) MEASURE GIT-REAL (phantom-guard) -- PASS
6-sha sample all git-verify to real portal commits w/ the claimed files co-changed. The promotion is warranted on FOCUSED commits ALONE: e502951536 (6 files), fbfdbe9d75 (2), a447712b4d (2) -- genuine portal-proxy<->ModelPortfolios coupling. (DS~B corrected the "all focused, not sweeps" claim: 3 of the 6 broad-sample shas ARE broad/sweep -- real co-changes, weaker coupling; a productionization refinement, non-blocking, does NOT reverse the promotion since the focused-commit coupling alone warrants it.)

### (ii) REVERSIBILITY + DURABLE CSE -- PASS (the fix verified on the real path)
- exact-inverse round-trip: PROVEN earlier by exercise on the real ac7ed5086 artifact ([silent-display-fork] -> demote -> []).
- durable CSE emission (the CVO-caught R4/AC5 gap): NOW FIXED + verified. c61f3b11c moved _emit_cse() to the WRITE POINT of both materialize() (:131) and demote() (:146) -- so ANY caller emits, not just the CLI happy path. GROUNDED on the real path WITHOUT re-churning the ratified manifest: (a) the REAL MATERIALIZED CSE is now in promote_materializer_cse.jsonl (subject_ref=recognizer:silent-display-fork, commission_id=CTO-PROMOTE-20260708T1521Z; was 0 CSE lines before the fix); (b) self-test 7/7 incl 3b (materialize emits durable) + 4b (demote emits durable -- the exact gap, temp-isolated so no real-trail pollution); (c) source: materialize + demote call the SAME _emit_cse at the write point, so the demote real-path emission is the identical proven mechanism. I did NOT re-demote the real artifact (would empty the just-restored ratified manifest + need a 4th re-materialize) -- the shared write-point + 4b + the real materialize-CSE evidence together ground the demote emission without that churn.

### (iii) GATE BITES ON REAL DATA -- PASS (1/7)
silent-display-fork promoted on its OWN independent 0.18 warrant; firm-conditional-display HELD (file-subsumed -> no independent warrant, my measure-provenance smell -> COO disposition -> CTO-affirmed); 5 dropped. Gate bites hard on a real sparse signal.

### HUMAN-RATIFY (AC2) -- self-describing on the live surface + the CSE
The live manifest entry records state=MATERIALIZED + commission_id=CTO-PROMOTE-20260708T1521Z-silent-display-fork (+ warrant/kind/vintage). The MATERIALIZED CSE carries the same commission_id. So the ratify-provenance is durable + inspectable in BOTH the R3 surface and the semantic log -- the write-back is self-describing (the whole point of R4/AC5), no git-archaeology needed.

## The loop-close, honest end-to-end
observe (CSE) -> measure (git-real co-evolution, phantom-guard held) -> compose (MOTIF C1/C2/C3, anti-Goodhart held) -> validate (gate bites 1/7, honest) -> promote (CTO human-ratify) -> materialize (reversible, exact-inverse; durable inspectable CSE). Two CVO catches made it honest: the measure-provenance double-count smell (system file-subsumed -> tightened 2/7 to an honest 1/7) and the untraceable-mutation gap (materialize/demote CSE discarded -> now emitted). Neither was a phantom; both were caught by exercise + grounded, not inferred.

## Residual follow-ons (separate certs, non-gating to this close)
- FRESHGUARD leg-4 (per-table vintage) -- 0.7.0 building, CTO arch-gated.
- ~D's GOV-B / recognizer half of PROMOTE-P2 -- MSTR respawn (MSTR was briefly offline, now online).
- MOTIF C3+CONTAINS materialize follow-on -- non-loop-close-gating; exercises my comp-kuzu re-finalize residual.
- in-VPC cse_coevolution persistence + standing-monitor (P3) + the commit-breadth "focused-coupling" refinement -- productionization.

## Compiler Tools
- git -C portal show x7 (measure phantom-guard) + EXERCISED --demote earlier on the real artifact + --self-test 7/7 (durable-CSE checks) + grep the CSE trail before/after + source-read the shared _emit_cse write-point. Grounded by exercise, not inference. No comp-tool models a promotion-lifecycle CSE trail.

-- 3.0.0_SA_CVO
