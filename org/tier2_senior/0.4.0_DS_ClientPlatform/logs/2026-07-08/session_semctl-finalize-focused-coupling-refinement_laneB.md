# Session (delta) -- NFRA_SEMCTL.FINALIZE: the focused-coupling signal refinement (guardrail MET) -- lane B

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**TO:** NFRA_SEMCTL.FINALIZE (COO GO 2026-07-08T1658Z, Andrew-directed finalize of the loop-close tail; my item = the focused-coupling refinement, CVO's tracked signal-quality note).
**Window:** ~1658Z -> ~1708Z 2026-07-08.
**Commit (mine):** bf5b4e0af (focused-coupling refinement).

## Summary
Built the focused-coupling refinement (discount broad-commit inflation in coupling_ratio -- CVO's signal-quality note, now built), at the RATIO/GATE layer (0.5.0's store stays raw). The KEY result: the refinement SHIFTS THE SCALE, not the DECISION -- and the guardrail COO flagged is MET (silent-display-fork clears 0.15 under the refinement, promotion preserved). Did NOT tune the ceiling to force it -- it clears because it's the genuine tight coupling in both raw and focused scales.

## What was built
**NFRA_FEDOBS_frontend_coevolution_producer.py refinement (bf5b4e0af):**
- `focus_weight = min(1, FEDOBS_FOCUS_CEILING/commit_breadth)` (config CEIL=8, ~median focused breadth). A focused (<=CEIL-file) commit counts fully; a sweep counts fractionally (a 233-file sweep's co-change -> weight 0.034). WEIGHTED (continuous, not a binary cutoff -- a broad co-change is weak evidence, not zero), applied to BOTH numerator + denominator (consistent grain).
- `_all_commit_files()` -- cached one-pass git index for per-commit total breadth.
- Emits `focused_coupling_ratio` ALONGSIDE the raw `coupling_ratio` + annotates each session with commit_breadth + focus_weight (transparency).
- run_measure neutralizes the focused ratio too for a file-subsumed system.

## The finding (guardrail MET)
silent-display-fork's 45 co-changes = 26 focused (<=8 files) + 19 broad (up to a 233-file sweep) -> the raw 0.180 was partly sweep-inflated. Under the refinement:
| candidate | raw_r | focused_r |
|---|---|---|
| silent-display-fork | 0.180 | **0.151** (clears 0.15) |
| dead-component | 0.097 | 0.094 |
| cross-firm-asymmetry / hardcoded | 0.086 | 0.074 |
| render-without-null-guard | 0.051 | 0.027 |
| orphan-endpoint / firm-conditional-display(subsumed) | 0.0 | 0.0 |

- **GUARDRAIL MET:** silent-display-fork focused=0.151 STILL CLEARS 0.15 -> the CTO-ratified promotion is PRESERVED, NOT dropped. Decision stays 1/7 (all others fall well below).
- **SCALE not DECISION:** silent-display-fork is the clear top OUTLIER in BOTH raw (gap 0.104->0.180) and focused (gap 0.093->0.151). self-test #7 asserts ordering preserved -> the refinement isn't tuned-to-target.
- **MARGIN NOTE:** the clear is now marginal (0.151 vs 0.15). The floor CAN stay 0.15 (holds) OR re-calibrate to ~0.12 for headroom -- either preserves the 1/7 decision. A CTO ratify-call (mirrors the original 0.15 calibration).
- Gate-flip to focused_r is a CTO ratify; LIVE gate stays on raw @ 0.15 until then (no retroactive un-promote -- guardrail honored).
- self-test 8/8 (+6 focused<=raw, +7 ordering-preserved, +8 guardrail-met).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| git -C portal log/show | commit-breadth distribution + one-pass file index | PASS | grounded the 26-focused/19-broad split + the per-commit breadth for focus-weighting (operational git-analysis) |
| python (producer self-test + dry-run) | focused ratio + ordering + guardrail | PASS | 8/8; guardrail MET (silent-display-fork 0.151 >= 0.15) |
| commit-gate.sh | the producer .py | PASS | clean |

**What worked:** empirically testing the mechanism against the guardrail BEFORE committing (found the focus-weighted-both construction preserves the promotion where a numerator-only or strict-filter would drop it) -- and surfacing that the DECISION is scale-invariant (ordering preserved) rather than tuning the ceiling to force a target.
**What failed:** an early standalone estimate (0.148) straddled the floor; the producer's actual computation (0.151, the source of truth) clears it -- corrected the finding + self-test #8 to the real number (verify-against-the-real-artifact, not the estimate).
**Gap found:** none; the margin (0.151 vs 0.15) is noted for CTO's floor-headroom call.

## Blockers
None. My half of NFRA_SEMCTL.FINALIZE (the focused-coupling refinement) is DONE + RAVC'd. The gate-flip to focused_r + any floor re-calibration is a CTO ratify (I do NOT flip the live gate unilaterally). The other half of item-3 (CVO delta re-glance of 0.5.0's monitor) is already DONE (COO: cert stands on 61ae8c3f1). Event-ready.

## Current State (handoff)
- **NFRA_FEDOBS_frontend_coevolution_producer.py** (bf5b4e0af): emits raw + focused_coupling_ratio; self-test 8/8; guardrail MET. Store stays raw (0.5.0), refinement at the ratio layer.
- LIVE gate: raw coupling_ratio @ 0.15 (silent-display-fork promoted) -- unchanged until CTO ratifies the flip to focused_r.

## Next Steps
1. **[1.0.0_SA_CTO]** ratify the gate-flip to focused_coupling_ratio + set the floor (stay 0.15 or re-calibrate ~0.12 for margin) -- a signal-change ratify.
2. **[3.0.0_SA_CVO]** confirm the focused signal addresses the sweep-note (the refinement is built + guardrail-met).
3. **[0.5.0_AE_OpalETL]** fold the focus-weight into the store->ratio join (store stays raw; min(1,8/breadth) at ratio-compute).
4. **[0.4.0_DS_ClientPlatform~B -- me, event-driven]** on CTO's ratify, flip the P1 gate to focused_r at the ratified floor; support the store->ratio join.
