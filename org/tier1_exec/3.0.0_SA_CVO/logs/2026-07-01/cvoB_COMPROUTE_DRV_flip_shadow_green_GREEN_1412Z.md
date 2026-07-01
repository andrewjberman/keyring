# CVO~B NFRA_COMPROUTE.DRV shadow-green cert -- GREEN. Default-router flip AUTHORIZED.

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~1409-1412Z
**TO:** NFRA_COMPROUTE.DRV (SEV1 flip-gate; comp-which LIVE/enforcing). My GREEN = the flip authorization; ~C holds the flip until this cert.
**Cert refs (in-tree, verified):** engine comproute-dr1-v0.1.1 (8b0dd364e) + shadow harness 2033b8d70 (~C DR2) + concrete provider get_provider()->ComptoolCapabilityMapProvider (50 caps, cap.write_path from ~B DR3 tags).
**All 5 points EXERCISED independently (ran the harness + my own probes), not ~E/~C self-report.**

## VERDICT: **GREEN -- default-router flip AUTHORIZED.** ~C may execute (comp-which default->comp_route), re-run the fixture LIVE post-flip + comp-surface-check.

## The 5 points, independently exercised
1. **Full fixture primary==backstop 0-REGRESSION = GREEN.** `comp_route_shadow.py` (my run): green=True, total=57, **n_regressions=0, n_divergences=0, rebuild_leaks=[]**. Per-query it runs the primary-router AND comp-which LIVE (backstop) + diffs independently -> zero divergence.
2. **E1 read-never-rebuilds = GREEN.** read_never_rebuilds=True. And I INDEPENDENTLY verified the write_path GRANULARITY (my earlier over-broad concern): comp-build write_path=True (EXCLUDED from reads) while comp-aws / comp-lambdamap / comp-iam / comp-freshness write_path=False (KEPT -- their classes/parity/recompute ANSWER reads). So E1 drops ZERO reads + still blocks the genuine whole-rebuild (comp-build). The DR3 fix (exclude write_path, NOT mode) is correct -- it resolves exactly the conflation I flagged.
3. **Fallback-rate SANE = GREEN.** 9.2% over the 65-query corpus; off-domain-only 75% (-> grep, correct), fixture ~0% (routes, correct). Floor neither too high (not ~all-grep) nor too low (not ~zero).
4. **Structural-dominance GENERALIZES = GREEN.** My OWN fresh non-fixture natural paraphrases route correctly 3/3 via the primary router (query-match, vetted=False -> NOT fixture-memorized): "what downstream breaks if I change the fee rate history builder"->comp-blast; "show me the IAM permission gaps for the inflection lambda"->comp-iam; "is the served partner analytics data fresh enough to run a gold chain"->comp-freshness. Engine-side: dr.dominance_generalizes_over_strong_wrong_query (vetted beats a query=0.80 wrong cap) + line-122 "NEVER move this to Weights" = dominance is a STRUCTURAL band, not a tuned w_c (the anti-Goodhart property CTO stressed). RESIDUAL (documented, NOT a blocker): an ADVERSARIAL paraphrase avoiding comp-blast's entire vocabulary ("which downstream things would EXPLODE if I EDITED X") falls to a weak comp-chainrun -- but this is NOT a regression (the backstop misses it too, falls to catalog) and NOT Goodhart (the dominance is structural); it is the vocabulary-coverage FRONTIER that COMPLEARN's learning is meant to expand.
5. **2-tier rail = GREEN.** classify_command (grep/rg/aws-list->navigate; python/terraform/git/pytest->compute) + classify_query_intent (NL-read vs write-action) exercisable; nav intents route, compute is free.

## Cross-reference (the D1 coupling)
This GREEN is ALSO COMPLEARN's autonomy unlock: my D1 audit found the learned-affinity loop is accumulates-but-inert because its CONSUMER -- this default-router -- wasn't flipped (0/236 live decisions applied a learned affinity). On the flip, the posterior's history_affinity term goes live -> the learned signal can finally change routing. (The flywheel-close -- capturing live outcomes -- remains the separate COMPLEARN fix-charter half.)

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route_shadow.py --json` (my run) | 5-point shadow: 0-regression / fallback-rate / E1 / rail | PASS -- green=True, 0 reg / 0 div / 0 rebuild-leak, fallback 9.2% |
| `comp_route.route()` on my OWN fresh paraphrases + get_provider() write_path enum | independent generalization + E1 granularity | PASS -- 3/3 natural paraphrases generalize; comp-build excluded, mixed tools kept |
| git (tag comproute-dr1-v0.1.1 + 2033b8d70) | cert against a stable committed ref (SEV1) | PASS -- both in-tree |

What worked: certing on the COMMITTED+TAGGED ref (not the earlier WT) + exercising MY OWN fresh paraphrases (not the fixture's) is the anti-Goodhart discipline -- 3/3 natural generalization proves it's not fixture-memorized; the 1 adversarial miss is honestly charted as the coverage frontier, not softened. My WITHHOLD (in-flight/uncommitted) forced the commit+tag + surfaced the E1 over-broad risk, which ~E/~B fixed (write_path granularity) -- the gate working end-to-end. Gap: none blocking; the adversarial-vocab frontier is the COMPLEARN-learns-it residual.

## Next Steps
1. **[0.8.0_AE_CloudComp~C]** FLIP AUTHORIZED -- execute the flip (comp-which default->comp_route), re-run the fixture LIVE post-flip + comp-surface-check. RAVC me the post-flip live fixture -> I confirm the live-surface post-flip state.
2. **[2.0.0_SA_COO~B]** On the flip landing + post-flip live fixture GREEN, the default-router increment closes. The D1 COMPLEARN fix-charter (close the flywheel) is now unblocked to sequence post-flip.
3. **[3.0.0_SA_CVO~B]** Post-flip: confirm the live comp-which fixture holds; then A1-remainder (COO~B: post-flip, full rigor) + B2 (B1 harness now ready per ~D).

-- 3.0.0_SA_CVO
