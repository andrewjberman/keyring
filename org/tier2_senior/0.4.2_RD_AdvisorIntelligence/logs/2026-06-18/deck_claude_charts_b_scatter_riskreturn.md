# 0.4.2_RD_AdvisorIntelligence~B — DECK_CLAUDE.CHARTS-B: scatter / risk-return + Peers (Yang) chart archetypes

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, TRACE

**Date:** 2026-06-18  **Driver:** GO from 0.4.2_RD_AdvisorIntelligence (base, deck-system owner) — Andrew-direct chart fan-out. TO: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/DECK_CLAUDE.CHARTS-B.scatter-riskreturn-charts.md`.

## Objective
Port the portal's scatter / risk-return charts into the new `Charts` archetype family. I own
`engine/archetypes/charts/scatter.py` exclusively (call `_native`, do not edit). Three named priorities incl.
the Peers chart (a direct request from Yang). Close with `/seams` per chart (Andrew-direct gate) + COM QA.

## Work Completed (IMPLEMENT)

### Ported the portal sources first (TRACE)
Read `ReturnVolatilityScatter.tsx` (x=vol, y=return; circle=model, diamond=benchmark; benchmark shares the
model color), `RollingSharpeChart.tsx` (model+benchmark lines over time, 1.0 reference), `PeersTab.tsx`
`QuartileChart` (percentiles PERFORMANCE-ranked: p5=top return, p95=bottom; 4 quartile bands p95->p5), plus
`_native.py` (opal_chart/opal_scatter) + `stat_stacked` (the shape-built pattern) + the port-map.

### 3 chart archetypes in `engine/archetypes/charts/scatter.py`
- **chart-scatter-riskreturn** — native XY (x=vol, y=return) via `_native.opal_scatter`; circle=model,
  diamond=benchmark, disconnected A1-colored markers. Delegates fully to `_native` (one styling source).
- **chart-line-rolling** — native line over time (`opal_chart` line_smooth); ONE parameterized archetype for
  Rolling Sharpe / Capture / Drawdown + an optional flat reference series (1.0 for Sharpe, 100 for Capture).
- **chart-quartile-peers** (Yang) — SHAPE-BUILT box-plot per period: a p25-p75 two-tone IQR box split at the
  median (upper med-blue, lower muted) + a white median rule + navy whiskers/caps to p5/p95 + model (purple
  circle) and benchmark (navy diamond) markers; shared Y scale across periods; compact legend.
register() each, `family="Charts"`, method `archetypes.charts.<func>`.

### Showcase + gate (VALIDATE)
`dev/scripts/showcase_charts_scatter.py` — 3 chart slides with representative risk-consistent Opal data (5
models UST->LTA, rolling-Sharpe series, INT peer quartiles across 1M/QTD/YTD/1Y/SI). **GATE PASS 0 lint +
full coverage**. ruff 0.15.11 (--extend-select FA) clean on both files.

### /seams completion gate (Andrew-direct) — all 3 SOUND
Report: `logs/2026-06-18/seams_0110Z_charts_b_scatter_line_peers.md`. Each archetype PASS on MECHANICAL +
DECLARATIVE + SEMANTIC, render-grounded against the COM-rendered PPTX. **Peers (Yang) SEMANTIC = PASS**: box
spans p25-p75, median + whiskers placed right, model circle above benchmark diamond in all 5 periods.

### COM visual-QA — read every slide
Rendered to PNG via PowerPoint COM across iterations; read all 4 slides each pass. Caught + resolved two
defects (both in base-owned files, confirmed by base RD): (1) scatter rendered with a connecting line
(`_native._color_series` set the XY series line) — base RD fixed `opal_scatter` (bcf700d17), I delegate;
(2) a 5x D3 false-positive on the box-plot (D3 rowed decorative marks) — base RD fixed design_lint
(00ec056cb: row only min(w,h)>=0.5 containers). Per base RD directive I did NOT dodge — restored the proper
2-tone colored box. Final render: all 4 slides clean.

## Compiler Tools
No comp-* tools run. Justification: standalone `deck_generation` chart tooling — no data-pipeline, cloud/infra,
or frontend change (`<compiler_tools_mandate>` N/A). Mandated validation = the `/seams` 3-axis pass per chart
+ `design_lint` [AUTO] gate (0 lint) + PowerPoint-COM visual-QA (read every slide). py_compile + ruff clean.

## Current State (handoff)
- Committed `5a3e69179` (scatter.py + showcase_charts_scatter.py) under ~B author line; pushed to CLOUD.
- `python -m engine.compose --catalog` -> Charts family includes chart-scatter-riskreturn / chart-line-rolling
  / chart-quartile-peers (alongside the RD~A composition + RD~C bar charts already built).
- HEAD includes base RD's two fixes: 00ec056cb (D3) + bcf700d17 (opal_scatter). My scatter.py delegates to the
  fixed `_native.opal_scatter`; my box-plot uses the proper colored build.
- Showcase artifact: `output/Opal_Charts_Scatter_Showcase.pptx` (4 slides).

## Next Steps
- [0.4.2_RD_AdvisorIntelligence] Integrate the Charts module into the combined showcase. chart-bubble (optional)
  deferred — not built (3 priorities + Yang delivered).
- [Andrew / Yang] Review the Peers quartile chart (slide 4 of the charts showcase) — Yang's requested chart.

## MCP / Blockers
1 inbound GO (CHARTS-B) + 3 base-RD coordination notes (D3-unblock, opal_scatter-fix, Peers-quartile-correct)
handled. No blockers. Broker status WORKING; persistent Monitor `buzjqy12e` armed. RAVC2 to base RD CC
2.0.0_SA_COO with the /seams verdicts.
