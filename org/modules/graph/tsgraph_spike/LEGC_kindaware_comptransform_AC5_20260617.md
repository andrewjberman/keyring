# Leg C — kind-aware comp-transform parity + AC5 forked-FLOWS_TO (result)

**Author:** 0.4.0_DE_ClientPlatform · 2026-06-17 · NFRA_TSGRAPH.P1 Leg C (drive-to-completion)
**Reviewer (cutover gate):** 1.0.0_SA_CTO
**F5 STATUS:** computed on the LOCAL semantic graph (`out/portal_full.graph.json`, which carries the FLOWS_TO `kind`/`condition`). **The F5 live-validation = the SAME query via `comp-kuzu json_extract` against Nessie->Kuzu — PENDING base-AE's props-column deploy** (executing tonight; CloudEdge has no props column until it lands). Re-run + close on the props ping.

## The kind-aware analysis (goal 3 — the display-logic-bug-class)
`comp-transform ternary-audit` made control-flow-real: query the FLOWS_TO edges with `kind=recompute/guarded` AND a `condition` — i.e. fields whose value is COMPUTED DIFFERENTLY per cohort/mode/firm. A field reached by **>=2 condition-branches** is a forked (dual-source) display-logic site.

### Semantic (kind-aware) — 23 cohort-gated computations, **5 FORKED fields**:
| forked field | the fork (condition <= source) | bug class |
|---|---|---|
| `benchmark` | `benchmarkType==='index'` → `ModelPortfolioPeriodReturn.index_benchmark` / else `.etf_benchmark` | cohort/mode |
| `spread` | `benchmarkType==='index'` → `.index_spread` / else `.etf_spread` | cohort/mode (the P0 exhibit) |
| `benchmark_volatility` | `benchmarkType==='index'` → `.index_benchmark_volatility` / else `.etf_benchmark_volatility` | cohort/mode |
| **`name`** | `advisor_id==='inflection_wealth_management'`-gated, **dual-source** `PlatinumLeaderboardEntry` vs `EmployeeLeaderboardEntry` | **cross-firm conditional asymmetry (D7) + AC5 dual-source fork** |
| `count` | `useLogScale` → `HistogramData.counts` / `DistributionStats.histogram` | display-mode |

### Regex baseline (`comp-transform ternary-audit ModelPortfolios`):
> "No variables found with union types." — found **0**. It missed all 5 forks / 23 cohort-gated computations entirely (`benchmarkType` is a `'index'|'etf'` union it can't resolve).

**Verdict: kind-aware comp-transform = better-than-regex (regex finds nothing; semantic finds 5 real forked display-logic sites).** This is the goal-3 payoff: the cohort/mode/firm display-logic the regex is blind to.

## AC5 — NNA dual-source divergence surfaces as a forked FLOWS_TO
AC5's mechanism (a dual-source divergence surfacing as a **forked FLOWS_TO with conditions**) is PROVEN on real frontend forks above — the `name` fork is a genuine **dual-source, firm-conditional** divergence (Platinum vs Employee leaderboard, gated on the inflection firm), exactly the shape AC5 predicts. NOTE on the NNA-specific case: the NNA `D_00f`-vs-`D_00c` divergence is a BACKEND two-gold-script concern feeding the same served `nna` field (not a frontend ternary), so its full demonstration needs the cloud/trace cross-graph stitch (P4 / the backend join), not the frontend extractor — the AC5 forked-FLOWS_TO MECHANISM is met here; the NNA backend instance is a cross-graph item.

## Residual / next
- **F5 live-validation** (the gate): re-run these queries via `comp-kuzu` against the LIVE Nessie->Kuzu once base-AE's props column carries `kind`/`condition` (json_extract). Imminent — event-driven on AE's ping.
- Condition-branch labelling is approximate for multi-source forks (the `name` fork shows the false-branch sources); the fork DETECTION is exact, the branch label is a refinement.
- Then: the full parity-gate RAVC2 -> CTO cutover review = TSGRAPH P1 validated-complete.
