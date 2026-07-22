# Convergence pass on the frozen re-stage + Andrew Jul6/7 variance -- 3.0.0_SA_CVO

**Date:** 2026-07-22 (delta 05:23Z -> 05:44Z; supersedes the prior log's now-stale ETag)
**Task Order:** ad-hoc (main CVO -- MDPF re-flip)
**Status:** milestone (convergence pass CLOSED; holding for DT marker-consumer)
**archetype:** VALIDATE

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| python (Layer-3 gate --selftest 7/7 + live) | PASS | E5 by_model absence-agreement added + mutant-proven; full gate PASS on c27e1f37 |
| aws s3 (eclipse/orion partitions + parquet) | PASS | Andrew Jul6/7: source totalValue stable, 65 IWM modelId flips localized |
| ruff / safe-commit | PASS | 656a38dd6, 88851665d ruff-clean, gate-clean |

**What worked:** reading eclipse parquet + modelId diff nailed the Jul6/7 mechanism; E5 absence limb closes the class E1 is blind to. **Gap found:** my prior verdict was on a superseded ETag (ebe4e111) -- DS re-staged twice more; always re-pin the vintage.

## Work Completed (delta since 0523Z)

1. **DS re-staged twice more** (partial-row fix, then the by_model absent-as-zero / A2 $107.2M false-dip fix) -> new FROZEN set. My ebe4e111 verdict superseded; re-verified on the frozen set.
2. **Andrew-direct: inflection Jul6/7 AUA variance** -> the "bounce" is a LEGACY date-mislabel of a REAL one-time 07-10 Eclipse modelId reclassification (65 IWM portfolios, ~$11.8M non-model->model, custody flat, permanent); the revamp dates it correctly + renders smooth. Not real AUM, not a revamp bug; residual IWM->Opal remap = a business question to DS. Committed 88851665d; answered Andrew; CTO accepted.
3. **E5 by_model absence-agreement limb** added to Layer-3 (independent of DS clause iv): sum(by_model model) None IFF model_aua None, exact absence limb + rounding-tol value limb; mutant-proven. @656a38dd6.
4. **Convergence pass on frozen c27e1f37** = PASS: E1 0/421, E3 49F-only, all-or-nothing 0 partial, E5 1281/1281 agree, 6 honest-None lineage-verified. A2 dip independently confirmed GONE (07-13/14/15 = None, no collapse).

## Blockers

None on me. Re-publish waits on DT's marker-consumer (their inflection Class-1 exemption, in flight).

## Current State

> Handoff for a zero-context reader.

Main CVO up (watcher bvwun8x6h, zero crons). **MDPF re-flip: my CVO legs GREEN on the FROZEN set** -- new frozen ETags **49f aa5c5b85 / inflection cec5a0d6 / global c27e1f37 / A1 529b7c21 / A2 f2c03476 / A4 8a195549** (SUPERSEDES ebe4e111 from the prior log). Andrew's B/EXCLUDE basis + all-None honest-None + the inflection_non_model_aua audit field all hold. My Layer-3 gate (@656a38dd6, mutant-proof 7/7: E1 + E3-49F-only + all-or-nothing + E5-by_model-absence) PASSES; marker lineage-verify ALL OK (source-based, vintage-independent); A2 false-dip fixed. Router still ROLLED BACK (staging only, live serve = legacy). RV-0054 post-re-land.

## Next Steps

1. **[3.0.0_SA_CVO] RE-VERIFY DT's gate on marker-consumer land** (event-driven) -> full 3-gate battery green.
2. **[1.0.0_SA_CTO] gate the data** on full-battery-green -> FE-first re-land + fresh co-sign.
3. **[0.4.0_DS_ClientPlatform] confirm the IWM->Opal 07-10 modelId remap is intended** (non-blocking business residual).
4. **[3.0.0_SA_CVO] N=3 continued-verification** post-re-land; then RV-0054.
