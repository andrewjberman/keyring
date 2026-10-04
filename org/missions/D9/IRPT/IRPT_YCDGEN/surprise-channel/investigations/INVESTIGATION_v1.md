# IRPT_YCDGEN -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

Worker rows are `IRPT_YCDGEN-W<n>-S<k>`; append-only; gate `.tools/surprise-row-gate.py`.

## IRPT_YCDGEN-W3-S1 -- the laptop has no bundled Chromium; Edge's close() hangs 20-90 s after the PDF is written

```json
[
  {
    "id": "IRPT_YCDGEN-W3-S1",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
    "surfaced_at": "2026-10-04T01:45:00Z",
    "one_line": "YCD-l-1 render_pdf.cjs: no playwright-bundled Chromium is installed, so it launches the msedge channel (bundled as fallback), and browser.close() takes 20-90 s on this laptop, so the close is bounded at 3 s and the process exits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "YCD-l-1: render_pdf.cjs loads playwright-core from portal/node_modules, launches chromium headless, sets the HTML and prints to PDF.",
    "world_is": "C:/Users/AndrewBerman/AppData/Local/ms-playwright holds only an MCP msedge profile dir (no chromium-<rev> build), so a bundled launch fails; msedge (channel) launches in about 1 s, prints in about 0.1 s, but await browser.close() took 21.8 s (measured with a timing script) and 93 s in a second run. A first test run took 85 s; with the bounded close it is 7 s. The issuer's host run therefore needs Edge or Chrome installed (IRPT_CHROMIUM_CHANNEL overrides the channel); the PDF is already on disk before the close.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node timing script under .runtime of the worker worktree: launch 1164 ms, pdf 1278 ms, close 21789 ms (msedge channel)",
        "infra/aws/lambda/investor-reporting/ycharts/research/render_pdf.cjs: Promise.race of browser.close() against a 3000 ms timer, then process.exit(0)",
        "pytest tests/test_layout_overview.py: 6 passed in 85.04s before the change, 6 passed in 7.17s after"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

## IRPT_YCDGEN-W2-S1 -- the gateway client the order names does not carry `/securities/securities_info`

```json
{
  "id": "IRPT_YCDGEN-W2-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-04T01:43Z",
  "one_line": "TO-YCD-m-1 names the gateway client as the home of the five estate-called data endpoints including /securities/securities_info; the client carries four of them and no securities_info method. The call lives in the Lambda's ycharts/generate/recipe.py as COMPARISON_IDENTITY_ROUTE. The map still lists it as portfolio_info, sourced from the Lambda route.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order lists the endpoints the estate already calls as those of infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py: general_data.json, fund_data.json, /indices/table_data, scatter_plot_data.json and /securities/securities_info.",
  "world_is": "client.py defines indices_table_data, general_data, fund_data, scatter_plot_data, search and freshness_probe, and no securities_info method; /securities/securities_info is read by the Lambda (ycharts/generate/recipe.py COMPARISON_IDENTITY_ROUTE, and the session tests). The map's portfolio_info call is therefore backed by the Lambda route, not the gateway client.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py@ad781b948a: def lines are indices_table_data, general_data, fund_data, scatter_plot_data, search, freshness_probe; no securities_info.",
      "infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:412@ad781b948a: COMPARISON_IDENTITY_ROUTE = \"/securities/securities_info\"."
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_YCDGEN-W2-S2 -- the retained PDF carries no template id; "Overview" is read from page 1's title and the page count

```json
{
  "id": "IRPT_YCDGEN-W2-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-04T01:43Z",
  "one_line": "The order says page 1's title and the template's report type identify an Overview. The PDF's own metadata names no template (Title empty, Creator wkhtmltopdf), so the map's template_id 14141822 is carried from the CRO research (an Overview of 23 pages), matched here on page 1 title 'Portfolio Overview' and 23 pages. The PDF is 23 pages, not the 4 of the contract's example.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A retained Overview among Cottonwood's ORIGINAL_VENDOR_PDF objects is identified by page 1's title and the template's report type (aggregate_security_overview, template 14141822).",
  "world_is": "Read in memory from opal-data-irpt irpt/cottonwood/state/vendor_documents/ART-ac668d3baaab.../6e753361...pdf (582,765 bytes, listed 2026-09-27): page 1 title 'Portfolio Overview', 23 pages, producer wkhtmltopdf; no template id or report type field is readable in the file. The 23-page count matches docs/research/investor_reporting_ycharts_variants_20260911/README.md (Overview, template 14141822, 23 pages). The other objects were listed by size only; none was opened.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3api list-objects-v2 opal-data-irpt irpt/cottonwood/state/vendor_documents/ read-only on 2026-10-04: 12 objects; one 582,765-byte object read with get-object into the OS temp dir (outside the repo) and removed after the map was built.",
      "docs/research/investor_reporting_ycharts_variants_20260911/README.md@ad781b948a: Overview, template 14141822, 23 pages, portrait."
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_YCDGEN-W2-S3 -- no estate document names the table_data column ids or the portfolio response shape; the map's table_data and scatter sources are inferred from printed labels, and holdings rows cannot be templated

```json
{
  "id": "IRPT_YCDGEN-W2-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~2",
  "surfaced_at": "2026-10-04T01:43Z",
  "one_line": "The order has each element sourced from an estate-called endpoint and the 2026-09 field scrape. The scrape is of a Comparison report and names printed fields, not API columns; the estate's own use shows only the column names ytd_total_return, price and pe_ratio and the level/price/total_return series. So 176 of the 249 elements carry a table_data or scatter source whose column id (or metric) is inferred from the printed label and unmeasured for a P:<id> portfolio, 8 more rest on the level series or securities_info, and 65 are BUILDER_ONLY, including every per-holding table (the three permitted placeholders cannot carry holding ids). Each is claim inferred; the live run measures them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Each element's source is a data endpoint and field chosen from the endpoints the estate already calls and the 2026-09 field scrape, or BUILDER_ONLY when no data endpoint carries it.",
  "world_is": "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json holds sections, printed field names and units for a Comparison report; it carries no endpoint, calc or column id. The gateway reads table_data by calc_name (integration.py _parse_table) and the estate documents only ytd_total_return, price and pe_ratio as columns. Whether /indices/table_data answers for a P:<id> typed portfolio, and under which calc names, is unmeasured at the cut. The map therefore names columns by the printed label (for example asset_allocation_cash, std_dev_5y) as inferred, uses the level series for the cumulative, annual and drawdown elements, and marks per-holding and look-through-holdings rows BUILDER_ONLY.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json@ad781b948a: top-level keys _meta, entities, sections, field_catalog, distinct_field_names, feasibility_read_PROPOSAL; sections carry field names and units only.",
      "infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py:74-98@ad781b948a: _parse_table matches datum calc_name; _parse_series reads chart_data[0][0].raw_data (fund_data) or chart_data[0].raw_data (general_data).",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json: 249 elements, 12 calls; 65 elements BUILDER_ONLY, the rest sourced to a listed call."
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```
