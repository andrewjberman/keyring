# IRPT_YCDGEN -- round 1 L8/L9 adjudication (the first compile of the project's channel)

<sweep_watermark>2026-10-04T18:45:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-04 ~20:3xZ (DRAFT). L8 inputs: `surprise-channel/investigations/INVESTIGATION_v1.md` at
CLOUD HEAD (5 rows); the issuer's round-1 drain-end record, drain commit `c1d672f636` (2.0.0_SA_COO~Y: all 4 orders
terminal and merged; 7 mechanical checks PASS on the merged tree; m-1.AC2 a judgment criterion for this seat) and
`org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md` section "IRPT_YCDGEN"; the close record under
`deliverables/2.0.0_SA_COO~Y/close/` (three host runs, two never-widen packets, the before- and after-reads) with
commits `8daaf100b2`, `9a01678592`, `b9f350b215`, `f9f0d95cad` and `9abe43df79`; CTO RULINGS batches 237 and 239; the
ledgers irpt-ycdgen-grant-20261004 and irpt-ycdgen-principal-20261004; and this seat's own reads for this compile (code
and git at CLOUD HEAD 96f17cdbe9; the research suite, 37 passed; read-only AWS: the Cottonwood research tables listed,
`run.json` of YCD-R1-20261004T1944Z read without any figure value, and the retained Overview's head-object and its
prefix listed; no YCharts call). 5 items compiled, all surfaced at or before the watermark. The 4 task orders are
complete at HEAD. 3 are dismissed by the 3 rows below (W3-S1, W2-S1, W2-S2); 2 graduate in
`remediations/REMEDIATION_v1.md`: S1 REMEDIATED and closed, W2-S3 OPEN. ARMED: 1 before (S1, BLOCKING); it arrives
DISARMED (2.0.0_SA_COO~Y, 2026-10-04T19:22:34Z, the after-read of the principal's apply); 0 stay ARMED. Outside this
compile: IRPT_YCDGEN-S2, the issuer's disarm record of S1 (surfaced 19:55Z, after the watermark, uncommitted at this
read), is the next compile's; the WAF challenge that stopped close runs 2 and 3 at step 7 carries no row at this read.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S1",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "W3-S1: the laptop has no bundled Chromium and Edge's close() hangs after the PDF is written; the cell bounded the close at 3 s, and the build has since rendered the close run's report.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W3-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "render_pdf.cjs launches the msedge channel by default, falls back to a bundled Chromium, and races browser.close() against a 3000 ms timer before process.exit(0) (:32-54). The build runs on the laptop, not the resident host: layout_overview.py reads the brand assets from the laptop's main tree (:10-11), render_pdf.cjs resolves playwright-core from portal/node_modules (:15-25), and the host script runs only the runner (ycdgen_close_host_r3.sh:45-49). l-1.AC2 passed on real Chromium at the drain; the research suite passes at CLOUD HEAD; and close run 3's report was built and rendered (run.json clocks.opal_building_ms 9500, report pages 39).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W3-S1",
        "infra/aws/lambda/investor-reporting/ycharts/research/render_pdf.cjs:32-54 at CLOUD HEAD 96f17cdbe9 (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py:7-11 and :274-286 (render through render_pdf.cjs, timeout 100 s) at CLOUD HEAD 96f17cdbe9 (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "drain c1d672f636 (2.0.0_SA_COO~Y): 'l-1.AC1 PASS (6), l-1.AC2 PASS (real Chromium, 2 pages)'",
        "python -m pytest -q tests in ycharts/research at CLOUD HEAD 96f17cdbe9: 37 passed in 10.19 s, no cache written (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R1-20261004T1944Z/run.json: report.pages 39, clocks.opal_building_ms 9500; overview.pdf 256,141 bytes at ycharts_opal_reports/request=YCD-R1-20261004T1944Z/ written 19:55:55Z (s3api list-objects-v2, this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An environment fact handled inside the cell's grant: the bounded close is in code, and the render path has produced the close run's report on the machine where the build runs."
  },
  {
    "id": "IRPT_YCDGEN-C-S2",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "W2-S1: the order named the gateway client as the home of all five estate-called endpoints, but /securities/securities_info is the Lambda recipe's route; the map sources it there and the live run answered on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "client.py at CLOUD HEAD defines freshness_probe, indices_table_data, general_data, fund_data, scatter_plot_data and search (:117-169) and no securities_info; recipe.py:412 reads COMPARISON_IDENTITY_ROUTE = \"/securities/securities_info\". The PRD names the gateway integration as prior art, read and not imported across the host boundary (IRPT_YCDGEN_PRD.md:175), so the order's list was a pointer, not the call path. The map's call portfolio_info is GET /securities/securities_info (overview_map.json calls[0]); close run 3's step 1 answered 200 with shape IDENTIFIERS, as run 2's did.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W2-S1",
        "infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py:117-169 and infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:412 at CLOUD HEAD 96f17cdbe9 (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md:175 (engines row: the gateway integration is prior art, 'read, not imported across the host boundary')",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json calls[0]: portfolio_info GET /securities/securities_info (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "9abe43df79 (close run 2): '01 securities_info: 200 IDENTIFIERS'; s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R1-20261004T1944Z/run.json calls[0]: portfolio_info status 200, shape IDENTIFIERS (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A wording slip in the order's list of homes; the map names the route the estate actually calls, and the live run answered on it. No cell, outcome or code is affected."
  },
  {
    "id": "IRPT_YCDGEN-C-S3",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:33:00Z",
    "one_line": "W2-S2: the retained Overview PDF names no template, so the worker identified it by page 1's title and its 23 pages, which agree with the CRO's measured variant; the identification is recorded in the map.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W2-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "head-object on the retained object ART-ac668d3baaab.../6e75336144a4... (582,765 bytes, 2026-09-27T16:22:24Z) returns no user metadata, so the store's object carries no template id either. The map records its source as bucket opal-data-irpt, artifact_prefix ART-ac668d3baaab, 23 pages (overview_map.json source_pdf) with template_id 14141822; the CRO research lists the Overview as template 14141822, 23 pages, portrait. The prefix now holds 14 objects (12 at the worker's read; two added 2026-10-04 02:27Z and 03:16Z). Whether the map lists every element on that PDF is m-1.AC2, this seat's judgment criterion, graded on its own and not by this row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W2-S2",
        "s3api head-object opal-data-irpt irpt/cottonwood/state/vendor_documents/ART-ac668d3baaab.../6e75336144a4...: ContentType application/pdf, ContentLength 582765, Metadata {} (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "s3api list-objects-v2 opal-data-irpt irpt/cottonwood/state/vendor_documents/: 14 objects, keys and sizes only, none opened (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json: template_id 14141822, report_type OVERVIEW, source_pdf {bucket opal-data-irpt, artifact_prefix ART-ac668d3baaab, pages 23} (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
        "docs/research/investor_reporting_ycharts_variants_20260911/README.md:15: Overview, template 14141822, 23 pages, portrait",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-m-1.overview-element-map.md:141, :145: AC2 is a judgment criterion graded by 3.0.0_SA_CVO against the PDF"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A recorded identification method on two features that agree with the CRO's measured variant; the map carries element ids and sources only, so no figure depends on it. The map's completeness is graded at m-1.AC2."
  }
]
```
