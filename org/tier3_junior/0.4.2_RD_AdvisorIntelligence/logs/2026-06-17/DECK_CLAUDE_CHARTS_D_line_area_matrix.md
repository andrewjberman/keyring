# DECK_CLAUDE.CHARTS-D — Line / area + matrix (heatmap / treemap) chart archetypes

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**agent:** 0.4.2_RD_AdvisorIntelligence~D
**window:** since the FANOUT-D RAVC close (e9aaa0451 / RE-close 233305Z) -> this log. CHARTS-D GO @ 005149Z.

## What was asked

Andrew-direct chart fan-out GO. TO `DECK_CLAUDE.CHARTS-D.line-area-matrix-charts.md`. Port the
portal's line/area + matrix charts into the new Charts family. NOTE: base RD reorganized the engine
into `engine/archetypes/<family>/` packages during the FANOUT-D integration -- my compare/flow/list
moved there; I now own `engine/archetypes/charts/series.py` EXCLUSIVELY (line/area/heatmap/treemap).

## What shipped — commit `734167835` (series.py + showcase, +210/-9, ~D author, DECK lane)

4 chart archetypes (Charts family now 7 incl. peer ~A composition):
- **chart-line-timeseries** -- native LINE_MARKERS, multi-series macro indicators (A1 via _native).
- **chart-area-stacked** (PRIORITY, the MP "surface") -- native AREA_STACKED allocation trend.
- **chart-heatmap** -- SHAPE-BUILT correlation matrix on the A1 diverging scale navy(+)/coolgrey(0)/
  purple(-). No red/green in the bible, so intensity comes from `_alpha()` (injects `<a:alpha>`; the
  srgbClr stays NAVY/PURPLE so the A1 lint passes). Uniform cell grid -> D3-safe.
- **chart-treemap** -- SHAPE-BUILT, EQUAL-WIDTH columns so rect AREA is EXACTLY proportional to weight
  (height = weight*scale, area = cw*height) AND D3-safe -- the key insight from stat-stacked: equal
  column width means any two cells that coincidentally share top+height also share width, so D3's
  "row of unequal widths" can never fire. (The first cut used a binary slice-and-dice treemap -> D3
  failed because a vertical split makes two full-height columns of unequal width; column-packing fixed it.)

Called `_native.opal_chart` (did not edit _native / compose.py / registry.py / peer submodules). F2:
every fn plots ONLY supplied data.

## Verification

- **Showcase** `dev/scripts/showcase_charts_series.py` -- REAL Opal data (macro series, MP allocation
  surface, a 6x6 correlation matrix using real Correlation-page asset labels, real sleeve weights) ->
  **GATE PASS: 0 lint + full coverage** (5sl, 4/4). Native-chart text lives in the chart XML (not slide
  text), so coverage tokens for line/area come from the captions/eyebrow.
- **COM visual-QA** -- rendered all 5 slides + READ every one. Two fixes from the QA: heatmap negative
  value labels wrapped ("-" on its own line) -> switched to no-wrap C.text; treemap had a ~5% area drift
  from the cosmetic per-cell gap -> removed it so area is EXACTLY proportional (cells touch, ramp separates).
- **/seams completion gate (Andrew-direct, REQUIRED)** -- ran the 3-axis pass on each of the 4 charts,
  ground-truthed against the BUILT pptx (python-pptx read-back), NOT self-report. **ALL 4 SOUND on all
  3 axes.** Report on the record: `seams_charts_series.md` (this dir). Key SEMANTIC evidence:
  line series == supplied verbatim; area stacked sum == 100.0 every year; heatmap 28 NAVY == count(v>=0)
  + 8 PURPLE == count(v<0) with alpha=14+86|v| monotonic; treemap height/weight ratio == 0.097 constant.
- **Lint** -- trimmed unused imports; `ruff --extend-select FA` = All checks passed; py_compile OK.

## MCP traffic

2 handled: CHARTS-D GO received (base RD) + ACK sent. RAVC2 completion report (with /seams verdicts) to
base RD CC 2.0.0_SA_COO follows this log.

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-* | N/A -- standalone deck tooling (TO mandate); gate = /seams 3-axis + design_lint + COM-QA. |
| design_lint (Deck.finalize) | PASS -- 0 violations (A1 incl. alpha-cells; D3 via equal-width columns/uniform grid) |
| /seams (4 charts x 3 axes) | PASS -- all SOUND; verdicts ground-truthed vs the built pptx (seams_charts_series.md) |
| python-pptx read-back | PASS -- series/sums/cell-colors/rect-areas all match expected |
| COM visual-QA | PASS -- every slide read; 2 fixes (heatmap label-wrap, treemap exact-area) |
| ruff 0.15.11 / py_compile | PASS -- All checks passed (FA + default, py39) |

What worked: the D3 reasoning from reading stat_stacked (equal-width columns) -- it turned a D3-fragile
treemap into a D3-safe-by-construction one; the python-pptx read-back gave HARD numbers for the SEMANTIC
seam (not eyeballing). What failed: nothing blocking (the binary-split treemap D3 failure was caught by
the gate and rebuilt). Gap found: none new.

## Current State (zero-context handoff)

- CLOUD HEAD includes `734167835` (series.py + showcase). Local only -- RD cannot push; base RD integrates.
- `engine/archetypes/charts/series.py` registers chart-line-timeseries / chart-area-stacked / chart-heatmap
  / chart-treemap (`python -m engine.compose --catalog` -> Charts family). Calls `_native.opal_chart` for
  the native two; shape-builds the matrix two with `_alpha()` + C primitives.
- Nothing blocked. `.comp-graph/.agent_context` TO_ID=DECK_CLAUDE.CHARTS-D... Broker IDLE after RAVC2.
  Persistent inbox Monitor `b5oe7bxoo` armed.

## Next Steps

- RAVC2 close: await validation from base RD [`0.4.2_RD_AdvisorIntelligence`] (combined-deck integration)
  / CC [`2.0.0_SA_COO`]. React to any revise on the 4 charts.
- No self-owned follow-on.
