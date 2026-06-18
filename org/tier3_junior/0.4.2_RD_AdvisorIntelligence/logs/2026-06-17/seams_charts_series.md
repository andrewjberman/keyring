# SEAM: chart data payload -> rendered chart (DECK_CLAUDE.CHARTS-D, series.py x4)   (scale: MICRO x4)

**archetype:** VALIDATE
**agent:** 0.4.2_RD_AdvisorIntelligence~D

Andrew-direct completion gate (per TO CHARTS-D): /seams each of the 4 chart archetypes on all 3
axes. Ground truth = the BUILT artifact `output/Opal_Charts_Series_Showcase.pptx` (read back via
python-pptx) + the deployed code + the COM render -- never source self-report alone.

## Seam definition (per chart)
- **Side A** = the data payload passed to the archetype fn (categories/series, labels/matrix, weights).
- **Side B** = the rendered chart on the slide (native pptx chart graphicframe, or shape-built rects).
- **Boundary** = the fn signature `archetypes.charts.<func>(s, ...)` -> shapes added to slide `s`.
- **Contract** = registry row (catalog) + docstring + DESIGN_BIBLE (A1 only, F2 data-only).

## Axis verdicts

### chart-line-timeseries  (native LINE_MARKERS)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | built pptx slide 2 `has_chart=True`; opal_chart -> add_chart fired |
| DECLARATIVE | PASS | catalog row method=`archetypes.charts.chart_line_timeseries` family=Charts; rendered type = LINE_MARKERS (65) matches "multi-series line" claim |
| SEMANTIC | PASS | read-back series == supplied verbatim: GDP `[2.0,2.1,4.9,3.4,1.4,3.0,2.8,2.3]`, +3 series exact. F2 holds (plots only supplied). COM render: GDP peaks 3Q23 / troughs 1Q24, tracks values |

### chart-area-stacked  (native AREA_STACKED, the MP surface)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | slide 3 `has_chart=True`; type AREA_STACKED (76) |
| DECLARATIVE | PASS | catalog row + docstring "stacked-area allocation surface"; rendered type matches |
| SEMANTIC | PASS | **stacked sum per category == 100.0 for all 5 years** (read-back: 2021..2025 each = 100.0). COM render: flat 100 top, equity/fixed/alt/cash bands. F2 holds |

### chart-heatmap  (SHAPE-BUILT, A1 diverging)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | slide 4 has 36 cell rects + 5 legend swatches (41 filled) |
| DECLARATIVE | PASS | catalog "A1 diverging navy(+)/coolgrey(0)/purple(-)"; built fills are ONLY navy/purple srgbClr (A1) + alpha -- no red/green (bible-compliant) |
| SEMANTIC | PASS | **sign-correct + monotonic**: 28 NAVY cells == count(v>=0)=28; 8 PURPLE == count(v<0)=8. alpha = 14+86\|v\| (NAVY 22.6..100.0 = \|v\| 0.10..1.0; PURPLE 18.3..31.2 = \|v\| 0.05..0.20) -- opacity rises monotonically with \|correlation\|. Diagonal v=1 -> alpha 100 (darkest). F2: plots supplied matrix only |

### chart-treemap  (SHAPE-BUILT, area proportional)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | slide 5 has 6 cell rects |
| DECLARATIVE | PASS | catalog "rect area proportional to weight"; equal-width columns (D3-safe by construction, like stat-stacked) |
| SEMANTIC | PASS | **area EXACTLY proportional to weight**: all 6 rects share width 5.94in; height/weight ratio = 0.097 CONSTANT across all 6 (weights 30/24/16/12/10/8 -> heights 2.91/2.328/1.552/1.164/0.97/0.776). area = cw*height => area ratio == weight ratio exactly. Strictly monotonic (bigger weight = bigger tile). F2: only supplied weights |

## Knowledge-parity delta
None. What we BELIEVED (catalog rows + docstrings) == what is TRUE in the built artifact, on every
axis, for all 4 charts. The A1-only diverging claim, the F2 data-only claim, the "area proportional"
claim, and the chart-type claims were each ground-truth-verified against the rendered pptx, not just
asserted. No record needed correction.

## Verdict
**All 4 charts SOUND (all 3 axes PASS).** chart-line-timeseries / chart-area-stacked /
chart-heatmap / chart-treemap.

## Residual / unknowns
- Native charts are EDITABLE (double-click -> data grid) -- confirmed by construction (opal_chart ->
  add_chart with CategoryChartData); not separately exercised by an in-PowerPoint edit.
- `_native.opal_chart` A1 series styling is base-RD-owned (called, not edited); its OPAL_SERIES order
  puts purple as series-2 (area Fixed-Income band) -- a house choice, not in my lane.
- SEMANTIC verified on the showcase's representative Opal data; the fns plot whatever is supplied (F2),
  so a real-deck payload carries its own correctness.

## Compiler Tools
| Tool | Result |
|------|--------|
| comp-* | N/A -- standalone deck tooling (TO mandate). Gate = /seams 3-axis + design_lint + COM-QA. |
| design_lint (Deck.finalize) | PASS -- 0 violations (A1 incl. the alpha-cells, D1/D2/D3 incl. the equal-width-column D3-safety) |
| python-pptx read-back (ground truth) | PASS -- series/sums/cell-colors/rect-areas all match expected |
| COM visual-QA (render_png.ps1 + read) | PASS -- every slide read; 1 heatmap label-wrap fix + treemap made exact-area |
| ruff/py_compile | PASS -- All checks passed (FA + default, py39) |
