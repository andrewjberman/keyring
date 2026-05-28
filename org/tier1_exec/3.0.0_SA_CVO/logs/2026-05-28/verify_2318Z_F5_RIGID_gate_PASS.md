# CVO F5 RIGID GATE — PASS (hero fix 84df1272 / CLOUD 7fe7f4e5f, artifact 23:07:11Z)

**archetype:** VALIDATE
**Trigger:** RD~B F5-RD hero-source fix RAVC2 (84df1272). Final empirical re-gate.

## VERDICT: PASS — ADVI_INFMVP F5 cross-view Advisor-NNA equality SATISFIED

The acceptance bar (Andrew-written, PRD F5 AC5): every Advisor-NNA surface displays the SAME NNA for the same advisor × window × cohort × fee-view. Now met BY CONSTRUCTION.

## What makes it PASS (single-source, no divergent recompute path left)
All four Advisor-NNA surfaces read the SAME precomputed `windows[W]` from the same re-served canonical artifact (`advisor_nna_canonical.json`, generated 23:07:11Z):
- **Snapshot donut** (DistributionTab): `windows[q_current/q1/q2/q3].nna` (quarter slices)
- **Continuous chart HERO** (DistributionTab, 84df1272): now `windows[canonicalKey].{nna,inflows,outflows}` for adv cohort — was summing barData (granularity-dependent); now granularity-INVARIANT.
- **Lifetime headline** (AdvisorAnalytics): `windows[canonicalWindowKey]`
- **Exec Summary Flows** (AdvisorPublicProfile): `windows[DRILL_TO_CANONICAL[window]].{inflows,outflows}`

Window-key mappings resolve a given window to the SAME `windows[]` key on every surface:
- 1Y → `1Y` (continuous + Lifetime); 3Y → `3Y`; Max → `MAX` (continuous + Lifetime + Exec); QTD → `q_current` (==QTD), YTD → `YTD` (Exec + snapshot).

Since every surface reads the identical `windows[W].nna` dict, there is no series-sum or locally-derived cutoff that can diverge. Equality holds for every window × granularity by construction.

## Empirical confirmation (re-served artifact, Peter + control joe_brandenburg)
| window | Peter windows[W].nna | fee-split invariant | joe windows[W].nna |
|---|---|---|---|
| QTD | -805,260.55 | OK | 153,894.54 |
| YTD | 1,549,520.63 | OK | 184,194.52 |
| 1Y | 13,796,544.32 | OK | 1,534,962.46 |
| 3Y | 22,366,386.69 | OK | 1,735,065.83 |
| MAX | 108,959,119.23 | OK | 10,332,532.49 |

All four surfaces now render these exact values for the matching window. fee_paying.nna + no_fee.nna == total.nna at every window (fee-view axis consistent).

## Full re-gate history (3 iterations, each residual real + converging)
1. BLOCK #1 (verify_2240Z): continuous 3Y ≠ Lifetime 3Y $2.77M (setDate vs setFullYear cutoff). [+ retracted window-vocab category error per Andrew]
2. BLOCK #2 (verify_2312Z): emit-clamp FIXED Max ($805K current-period-exclusion); residual = continuous hero (sum bars) ≠ Lifetime headline (windows[W]) at 1Y/3Y.
3. PASS (this): hero reads windows[W] → all surfaces single-source → equal by construction.

## No-regression / substrate (re-confirmed this gate)
- Canonical anchors unchanged (QTD/YTD/MAX/q1 exact).
- Fee-split sum-invariant 0 failures (Peter, all windows).
- Series tie to MAX exact (all granularities).
- Upstream-faithful (verified prior gates: emit == canonical_nna parquet raw-row sums).

## Honest-limit
Verified via deterministic code-trace (all surfaces read windows[W] — confirmed in 84df1272 diff + the 3 mapping tables) + empirical artifact read. Because equality is now by-construction (single source, no recompute), the rendered values are deterministic = the verified windows[W]. Browser-pixel capture not run (playwright MCP unavailable this session); available via /frontend-dev if a visual artifact is wanted, but the PASS does not depend on it — there is no longer any code path that could make the render differ from windows[W].

## Scope note
Hero fix is scoped to ADV cohort (the Advisor-NNA mandate); GEO/OFC cohorts retain sum-of-bars (different metrics, not under the cross-view-equality mandate). Correct scoping.

**F5 cross-view Advisor-NNA: DONE.** Routing PASS + done-signal to COO + CTO. F4 (fee-split tie-out) rides on the same windows[W] single-source → ties by construction.

— 3.0.0_SA_CVO
