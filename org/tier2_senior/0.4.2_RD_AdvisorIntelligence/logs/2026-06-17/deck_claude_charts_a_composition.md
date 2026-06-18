# 0.4.2_RD_AdvisorIntelligence~A — DECK_CLAUDE.CHARTS-A: composition charts (donut / pie)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-06-17  **Driver:** Andrew-direct chart fan-out via base RD (0.4.2_RD_AdvisorIntelligence).
TO: `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/DECK_CLAUDE.CHARTS-A.composition-charts.md`.

## Objective
Port the portal's composition charts into the new Charts family as REAL, EDITABLE, on-brand native
python-pptx charts. Own `engine/archetypes/charts/composition.py` exclusively; call the shared
`_native.opal_chart` (do not edit it / compose.py / registry.py / sibling submodules). Andrew-direct
gate: /seams (mechanical/declarative/semantic) PASS per chart archetype.

## Work Completed
- Built 3 archetypes in `composition.py`, all native via `_native.opal_chart` (A1 palette + Lato + chrome
  applied by the helper), each taking a real data payload (F2):
  - **chart-donut** -- MP allocation doughnut: clean ring + a color-matched manual legend (swatch + value +
    share) + a center TOTAL label in the donut hole. Square chart frame so the hole center is deterministic.
  - **chart-pie** -- composition pie: per-slice category + percentage labels (OUTSIDE_END), optional note caption.
  - **chart-donut-center** -- the MP selected-segment variant: one segment recolored PURPLE (single accent),
    the rest a muted blue ramp, center label = the selected segment + its share.
- Grounded the data shapes in the portal sources: the canonical MP model lineup from `ModelPortfolios.tsx` +
  `modelPortfolioColors.ts` (Ultra-Short / Short / Intermediate / Long / Ultra-Long Term + Non-Model;
  50/50 blends folded per the FE), and the AdvisorIntelligence DistributionTab Top-N+Other shape.
- Showcase `dev/scripts/showcase_charts_composition.py` with real Opal-shaped data -> **GATE PASS: 4 slides,
  0 lint, 3/3 coverage**. (Chart category/value text lives in chart XML, not slide text frames, so coverage
  is carried by the eyebrow title + legend + center text -- by design.)

## Validation (the product)
- **/seams 3-axis PASS on all 3 archetypes** -- full report: `seams_0055Z_composition-charts.md`. MECHANICAL
  (generates + COM-renders), DECLARATIVE (registered + catalog claim true + chart TYPE matches name + editable),
  SEMANTIC (chart XML embedded values byte-equal the supplied payloads; rendered proportions correct;
  legend swatches color-match slices; A1 palette). Verdict SOUND x3.
- **COM visual-QA** -- rendered all 4 slides, read each: donut/pie segments Opal-colored + legible, center
  labels correct, no clutter, no white-on-white.
- **Editable** -- 3 native chart parts (chart1/3 doughnut, chart2 pie) + 3 embedded workbooks
  (Microsoft_Excel_SheetN.xlsx) -> double-click in PowerPoint surfaces the data grid.

## Compiler Tools
| Tool | Result |
|---|---|
| comp-surface-check | auto-run by safe-commit; PASS (0 critical surfaces). |

Justification: standalone deck tooling -- the mandated validation is the /seams 3-axis pass + design_lint
[AUTO] gate (0 violations, incl. the chart-series A1 check) + COM visual-QA + the chart-XML value-equality
check. py_compile clean; ruff (--extend-select FA) 0 violations on both .py (no E701/F401 -> no bypass).

## Current State (handoff)
- Committed on the DECK lane (~A author): `engine/archetypes/charts/composition.py` +
  `dev/scripts/showcase_charts_composition.py` + this log + the seam report + TO->complete.
- Scoped to MY submodule only -- `_native.py` / compose.py / registry.py / sibling chart submodules
  (bar/scatter/series, owned by ~C/~B/~D) untouched. The whole Charts family is filling concurrently.
- Decks on disk: `deck_generation/output/Opal_Charts_Composition_Showcase.pptx` (+ PNGs under output/qa_charts).
- RD cannot push; base RD / DT carries push + the combined Charts showcase integration.

## MCP / Blockers
GO ACK'd; RAVC2 (with the /seams verdicts) sent to base RD (0.4.2_RD_AdvisorIntelligence) CC 2.0.0_SA_COO
on completion. No blockers. Persistent Monitor `buhz8mnxu` armed; broker WORKING throughout.
