# NFRA_COMPAWS — Close-Out Decomposition (to 13/13)

**Owner:** 2.0.0_SA_COO~B | **PRD:** `docs/briefs/comp-aws-comprehensive-cloud-compiler-prd-20260601.md` | **Authored:** 2026-07-01 (get-ahead close-out plan)
**Current:** 9/13 classes existence-F1-certified (Wave-4 f9a92fcec, STANDS). Capacity-gated mid-ramp. Remaining = 3 legs to 13/13. Original builder 0.7.0_AE_CloudOps is NOT-REGISTERED (down post-reboot); this plan makes it driveable IN-FLEET so it doesn't bottleneck on a 0.7 respawn.

## Remaining legs (the close-path to 13/13)

| leg | scope | owner (proposed) | sequence |
|---|---|---|---|
| **PHASE-0** | the hand-audit LONG POLE: extend the human-oracle hand-audit from 9 to the full 13-class taxonomy (incl. StepFn) -> the regression fixture. The oracle IS the close-gate (diff-vs-audit-until-0-diff). | CVO~B (audit oracle) + ~A (AE-side live boto3 census) | post active-wave; the long pole |
| **SFN-FIX** | the ASL-walker Parallel-block bug: misses 17 Lambda invokes in nested Parallel blocks -> StepFn uncerted + a REAL comp-graph coverage HOLE (comp-blast/comp-iam under-report SFN->Lambda edges). | ~B (comp-lambdamap/classify_reconcile owner) | post-Phase-B derive (~B frees) |
| **LAMBDAMAP-P2** | the Lambda sub-module SHA-vs-live fold (comp-lambdamap Phase-2 folds into comp-aws). | ~B (comp-lambdamap owner) | post-Phase-B derive |

## Close-path
1. SFN-FIX + LAMBDAMAP-P2 -> ~B (its comp-lambdamap domain), sequenced AFTER the Phase-B derive + convergence co-sign (do not pull ~B off the single-committer canonical fire).
2. PHASE-0 hand-audit to 13/13 -> CVO~B (oracle) + ~A (live census), sequenced after the active-wave close-verifies clear CVO~B's slate.
3. Each certified class = diff-vs-hand-audit-until-0-diff (Andrew's cert-loop method); the hand-audit becomes the regression fixture. `derive --write` stays CVO-gated.
4. On 13/13 existence-F1 + SFN-edge coverage restored -> CVO cert -> COMPAWS closes.

## Sequencing note
COMPAWS was Andrew-deferred behind 0.7 capacity (2026-06-05). This plan keeps it IN-FLEET so it can close on the NFRA_COMP* fleet without a 0.7 respawn -- BUT it sequences BEHIND the active wave + the Phase-B derive (no lane pulled off a canonical fire). If Andrew wants COMPAWS driven with dedicated capacity sooner, the alternative is an MSTR respawn of 0.7.0_AE (the original owner) -- flag COO~B. NOT force-started mid-canonical-fire.

## Residual (tracked): the AC3 N->N+1 diff-oracle rides the nightly; the SFN-edge hole means comp-blast/comp-iam under-report StepFn->Lambda TODAY (a known, bounded coverage gap until SFN-FIX lands).
