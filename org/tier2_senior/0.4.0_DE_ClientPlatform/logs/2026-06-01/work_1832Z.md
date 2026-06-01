# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1832Z (Inflection 5/18-step scope-probe)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE

## Dispatch
CTO [CONFIRM] accepted TO-1a 49F PASS + confirmed global residual = intentionally Inflection-gated. New light scope-probe (read-only, coordinate DS~B): is Inflection's 5/18 step the SAME BD->Schwab class as 49F, or a distinct legitimate Inflection event? -> arms Andrew re-derive-Inflection-vs-accept.

## FINDING 1 (the ask) — Inflection 5/18 step is DISTINCT from 49F's class
Inflection per-firm + source partitions:
- 5/15: model=0, non_model=203.8M, sma=0, custody=203.8M (methodology_version v0_8_ruling2).
- 5/18: model=93.6M, non_model=106.1M, sma=0, custody=199.7M (v0_9_1).
- Same v0_8->v0_9 methodology FLIP as 49F, BUT different economics: custody TOTAL ~continuous (-$4.1M, normal market move); model BROKE OUT from 0 (0->$93.6M) so non_model dropped correspondingly (-$97.7M). NO SMA. Total PRESERVED.
=> Inflection's step = a MODEL-BREAKOUT re-decomposition (models not decomposed pre-5/18, broken out at v0.9 cutover), total-continuous. NOT 49F's BD->Schwab custody-TOTAL re-measurement (-$156M real). So Inflection does NOT need a 49F-style Schwab custody re-derive (its total is already continuous). The visible non_model-band step (-$97.7M) is the legitimate model breakout — addressable by display-treatment or back-decomposing pre-5/18 inflection models, NOT a custody re-derive.

## FINDING 2 (coherence, beyond the ask) — global aggregate NOT recomputed from re-derived 49F pre-5/18
- 5/18: GLOBAL non_model 389.6M == 49F-rederived(283.5M)+INF(106.1M) EXACTLY (residual 0). Coherent post-cutover.
- 5/15: GLOBAL non_model 659.4M != 49F-rederived(274.8M)+INF(203.8M)=478.6M -> residual $180.75M = EXACTLY old-49F(455.5M) minus rederived-49F(274.8M).
=> Global's aggregate{} for the re-derived 1/16-5/17 range still carries OLD-49F (BD-basis), while the 49F per-firm SLICE shows re-derived (Schwab). Global is INCOHERENT with the re-derived 49F slice pre-5/18 + still seams. A re-aggregation gap, distinct from Inflection. Closing global's seam needs BOTH (a) re-aggregate global from the re-derived 49F partitions + (b) the Inflection disposition.

## Commits
- CLOUD `<pending>` — this log

## Comms
- RAVC2 (classification DISTINCT + global-coherence finding) -> CTO; CC COO + DS~B + CVO.
- (self-caught + fixed a bare-& watcher mis-launch this tick; relaunched tracked bqgz3j215.)

## Next
- [CTO/Andrew] Inflection = accept (total-continuous) or back-decompose-models-for-display (NOT custody re-derive); + global re-aggregation gap disposition.
- [DS~B] methodology confirm on the Inflection model-breakout + the global re-aggregation.
- Held: AC6 ADD-DAYS re-verify; pre-1/16 §4; Andrew visuals; FE-slim de-conflict. /work cron live.
