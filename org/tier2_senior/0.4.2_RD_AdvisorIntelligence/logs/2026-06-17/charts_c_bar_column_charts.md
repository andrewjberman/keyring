# 0.4.2_RD_AdvisorIntelligence~C — DECK_CLAUDE.CHARTS-C: bar / column chart archetypes

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-06-17/18  **Driver:** Andrew-direct chart fan-out GO (base RD dispatch, CC COO). TO: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/DECK_CLAUDE.CHARTS-C.bar-column-charts.md`. Lane ~C. Follows FANOUT-C (statcards+stat); engine was restructured to `engine/archetypes/<family>/` packages between the two (my arch_statcards/arch_stat migrated to `archetypes/statcards|stat/` intact).

## Objective
Port the portal's **bar / column** charts into the new Charts family. Own `engine/archetypes/charts/bar.py` exclusively; native charts via the base-owned `_native.opal_chart` (call, don't edit); the waterfall is SHAPE-BUILT. Real Opal data (F2). Close with **/seams per chart** (Andrew-direct gate).

## Work Completed (IMPLEMENT) — engine/archetypes/charts/bar.py
- **chart-column-cme** — CME 10-yr expected return + volatility per asset class. Native grouped columns (return navy / vol purple, both % on a shared axis). The TO's sanctioned "(or a paired line)" form -- a true column+line combo needs combo support in the base-owned `_native`, out of my lane.
- **chart-bar-diverging** — FactorTilts signed exposures about a zero baseline. Two-series **STACKED** bar: Overweight(+) navy / Underweight(-) purple (series-level A1 via `_color_series`). `invert_if_negative=False` so negatives keep purple (default invert rendered them white); `category_axis.tick_label_position=LOW` so factor labels clear the negative bars.
- **chart-column** — clean single-series native column (Valuation Fwd P/E), navy + data labels.
- **chart-waterfall** — Attribution contribution bridge, **SHAPE-BUILT** (python-pptx has no waterfall): floating C.osh rectangles, start/total anchors (navy / med-blue), up=navy / down=purple deltas, cool-grey connectors at each running level + a baseline. Cumulates 6.50 + 1.10 + 1.30 - 0.40 = 8.50.
- showcase `dev/scripts/showcase_charts_bar.py` — 1 slide/chart, real Opal data shapes (CME return/vol, the 6 factor tilts, Fwd P/E, attribution bridge).

## VALIDATE — gate + /seams (Andrew-direct completion gate) + COM-QA
**finalize() [AUTO] lint + coverage:** 0 violations, 4/4 coverage, 5 slides. `--catalog` shows the 4 under `Charts`. ds-commit-gate clean (py_compile + AST + ruff py39, no E701).

**/seams 3-axis per chart (render-grounded), all PASS:**
| chart | MECHANICAL | DECLARATIVE | SEMANTIC (render-grounded) |
|---|---|---|---|
| chart-column-cme | renders (7 classes x 2 series) | registered, COLUMN_CLUSTERED, claim true | navy=return/purple=vol; every height matches supplied value incl. Cash 3.6>1.0 |
| chart-bar-diverging | renders | registered, BAR_STACKED, claim true | +navy-right / -purple-left; all 6 signs+magnitudes match; zero baseline |
| chart-column | renders | registered, COLUMN_CLUSTERED, claim true | Fwd P/E heights descend 19.5->11.8 matching data |
| chart-waterfall | renders | registered, shape-built, claim true | cumulates start->total exactly (8.50); down-delta purple; connectors at correct levels |

**COM visual-QA** of all 5 slides, clean after **2 fixes on the diverging bar**: (1) negatives rendered hollow/white (PowerPoint `invertIfNegative` default) -> switched to two-series stacked + `invert_if_negative=False` so negatives render purple; (2) factor labels overlapped the purple bars at the zero line -> `tick_label_position=LOW`. Re-rendered clean. Other 3 charts clean first pass.

## Files Modified / Current State (handoff)
Committed `11358e779` (DECK lane, ~C author), pushed origin/CLOUD. See commit message for per-file detail.
- `deck_generation/engine/archetypes/charts/bar.py` — 4 chart fns + register (Charts family).
- `deck_generation/dev/scripts/showcase_charts_bar.py` — new.
- TO flipped `<status>complete</status>`.
- Owned ONLY `bar.py` + showcase. `_native.py` / `compose.py` / `registry.py` / sibling chart submodules untouched (called `opal_chart`, did not edit it). QA PNGs `deck_generation/output/qa_charts_bar/` (gitignored).

## Next Steps
- [0.4.2_RD_AdvisorIntelligence] base RD integrates; Andrew per-chart keep/kill/revise.
- A true CME **column+line combo** (vol as a line on a secondary axis) is a `_native.opal_chart` enhancement (base-owned) — flagged for base RD if the grouped-column form isn't preferred.
- Charts family now has composition (RD~A) + bar/column (RD~C) live; scatter (RD~B) + line/area+matrix (RD~D) per the port-map remain.

## MCP / Blockers
Inbound: 1 GO (base RD, CHARTS-C) acted on. No blockers. Broker status WORKING throughout; persistent Monitor `bzb0io1z3` armed at load.
