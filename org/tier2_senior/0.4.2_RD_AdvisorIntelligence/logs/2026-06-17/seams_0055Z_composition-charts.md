# SEAM: composition chart archetype fn  ->  rendered native editable chart   (scale: MICRO x3)
**archetype:** VALIDATE

DECK_CLAUDE.CHARTS-A Andrew-direct /seams completion gate. Three chart archetypes in
`engine/archetypes/charts/composition.py`, each its own seam (archetype fn -> the chart it emits
into the .pptx). Ground truth = the rendered/saved artifact `output/Opal_Charts_Composition_Showcase.pptx`
(the served artifact for this deck-tooling class) -- chart XML + embedded workbook + COM render, not source.

## Seam definition
- **Side A:** `chart_donut` / `chart_pie` / `chart_donut_center` (composition.py), each taking a real
  data payload `segments: N x (label, value)` (F2 -- supplied data only).
- **Side B:** the native python-pptx chart written into the slide (`ppt/charts/chartN.xml` + embedded
  `ppt/embeddings/Microsoft_Excel_SheetN.xlsx`), styled by the shared `_native.opal_chart` (A1 + Lato).
- **Boundary:** `_native.opal_chart(s, "doughnut"/"pie", categories, [(name, values)])` + my post-config
  (legend, center label, point recolor for the selected-segment variant).
- **Expected contract:** the chart TYPE matches the archetype name; it plots EXACTLY the supplied
  values (no fabrication/scaling); slices are Opal A1; the chart is genuinely editable; the catalog
  claim is true to the impl.

## Axis verdicts -- per archetype

### chart-donut (MP allocation donut)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL  | PASS | showcase finalize() GATE PASS (generates); COM-rendered slide 2 read -- ring + legend + center "$2.5B / TOTAL AUA" all present, no render error. |
| DECLARATIVE | PASS | catalog: `chart-donut -> archetypes.charts.chart_donut`, takes "segments: N x (label, value $M)"; `ppt/charts/chart1.xml` is a `doughnutChart` (TYPE matches name); embedded `Microsoft_Excel_Sheet1.xlsx` present -> editable. |
| SEMANTIC    | PASS | chart1.xml numeric cache == supplied [180,420,760,540,310,290] EXACTLY (vals_match=True); rendered shares 7/17/30/22/12/12% sum 100, Intermediate Term largest wedge; center total $2.5B = sum; legend swatches color-match slice colors (OPAL_SERIES order); all fills A1. |

### chart-pie (AdvisorIntelligence distribution)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL  | PASS | GATE PASS; COM-rendered slide 3 -- pie + category/% labels outside + note caption, no error. |
| DECLARATIVE | PASS | catalog: `chart-pie -> archetypes.charts.chart_pie`; `chart2.xml` is a `pieChart` (TYPE matches); `Microsoft_Excel_Sheet2.xlsx` embedded -> editable. |
| SEMANTIC    | PASS | chart2.xml cache == [720,540,410,380,260,190] EXACTLY; rendered 29/22/16/15/10/8% sum 100, Northeast largest; per-slice category+% labels correct + legible (charcoal on white); A1 palette. |

### chart-donut-center (MP selected-segment donut)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL  | PASS | GATE PASS; COM-rendered slide 4 -- donut, Intermediate Term highlighted purple, center "30% / INTERMEDIATE TERM", legend; no error. |
| DECLARATIVE | PASS | catalog: `chart-donut-center -> archetypes.charts.chart_donut_center`, takes "...; highlight idx"; `chart3.xml` doughnutChart; `Microsoft_Excel_Sheet3.xlsx` embedded -> editable. |
| SEMANTIC    | PASS | chart3.xml cache == [180,420,760,540,310,290] EXACTLY; highlight=2 -> Intermediate Term slice recolored PURPLE (single accent), others muted blue ramp; center share 30% = 760/2500; legend swatches match the recolored slices; A1 palette. |

## Knowledge-parity delta
BELIEVED (catalog/TO): three native editable composition charts whose type matches the name and that
plot only supplied data. TRUE (artifact ground truth): confirmed -- 3 chart parts (doughnut/pie/doughnut)
+ 3 embedded workbooks; embedded values byte-equal the supplied payloads; A1 series. No drift; no record
correction needed. Note: the chart category/value text lives in chart XML (not slide text frames), so the
finalize() fidelity-coverage check is satisfied via the eyebrow title + legend + center text (by design).

## Verdict
**SOUND** (all 3 axes PASS) for chart-donut, chart-pie, chart-donut-center.

## Residual / unknowns
- Editability proven structurally (chart part + embedded workbook present) + by construction (python-pptx
  add_chart embeds the data); NOT exercised by a literal human double-click in this session (would require
  interactive PowerPoint) -- structural evidence is decisive for this artifact class.
- /seams grounded on the local rendered artifact (correct ground truth here -- there is no deployed/served
  cloud surface for the deck composer; the .pptx IS the product).

## Compiler Tools
| Tool | Why / result |
|---|---|
| comp-surface-check | auto-run by safe-commit at commit; PASS (0 critical surfaces). |
| (comp-* otherwise N/A) | standalone deck tooling -- the mandated validation is /seams 3-axis + design_lint [AUTO] gate (0 violations) + COM visual-QA + the chart-XML value-equality check above. |
