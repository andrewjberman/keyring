# IRPT_YCDGEN task order -- `YCD-m-2` -- ROUND 2 (ENRICHMENT): THE MAP'S FOUR VECTOR-DRAWN CHARTS AND TWO SMALL GAPS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R2.md</decomp_doc>
<owned_cells>YCD-m-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 2** enriches round 1's live thread (one Cottonwood Overview, run `YCD-R1-20261004T1944Z`: 2 of 12 calls answered with data; 176 of 249 elements have no answer). No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-2 decomposition)

### `YCD-m-2` -- the map's four vector-drawn charts and two small gaps (E2; FWD-3, m-1.AC2)
- `ycharts/research/map_pdf.py`: detect a chart drawn as vector shapes (pdfplumber `rects`, `curves`, `lines` clustered into
  one region), not only an embedded image, and give it the nearest printed title as its label.
- Re-run on the same retained source Overview (the 23-page PDF of row W2-S2, read from S3 into OS temp only, never into
  the repo), then update `overview_map.json`:
  - add the four charts: p3 Stock Style Exposure, p3 Market Classification, p3 Region, p5 Stock Sector Exposure. Each
    gets the next unused element id on its page; existing ids never renumber;
  - p14.e03 lists all six of its columns;
  - p13.e04 regains its dropped header word.
- A test on a small synthetic PDF (made in the test with reportlab or pypdf drawing ops, if available, or a fixture
  under `tests/fixtures/`) has one chart drawn only as rectangles, and it is detected with its title.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

### 2.3 The element map (C-MAP) -- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`

```json
{
 "schema": "irpt-ycdgen-map-v1", "report_type": "OVERVIEW", "template_id": "14141822",
 "source_pdf": {"bucket": "opal-data-irpt", "artifact_prefix": "ART-<first 12 hex>", "pages": 4},
 "calls": [{"name": "snake_case", "method": "GET", "path": "/charts/general_data.json",
            "params": {"securities": "id:{security_id},include:true,,", "metrics": "id:total_return,include:true,,"}}],
 "elements": [{"id": "p1.e01", "page": 1, "kind": "number | table | chart | text", "label": "printed label text",
               "source": {"call": "snake_case", "field": "JSONPath into the kept body_json"},
               "claim": "inferred | measured", "note": "one line"},
              {"id": "p3.e04", "page": 3, "kind": "chart", "label": "...", "source": "BUILDER_ONLY",
               "claim": "inferred", "note": "computed only inside YCharts' report builder"}]
}
```

- Labels are printed label text only. **No figure value from the PDF enters git** (C-FIRM): no number read from a figure's
  position, no dollar amount, no percentage value.
- `params` placeholders: `{security_id}` (the portfolio's typed id), `{start}`, `{end}`.

### 2.4 Module home and run environment

- Package: `infra/aws/lambda/investor-reporting/ycharts/research/` (new): `keeper.py`, `runner.py`, `layout_overview.py`,
  `render_pdf.cjs`, `map_pdf.py`, and `tests/`. Tests follow the sibling layout: beside the code, no `conftest.py`, paths
  inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`).
- The runner imports the served session modules as top-level modules, so it puts `ycharts/session` and `ycharts/generate`
  on `sys.path` (`resident_session.py` imports `broker`, `transport`, `deadline_transport`).

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `ycharts/research/map_pdf.py` (pdfplumber) builds the element skeleton from words, tables and embedded images; charts drawn only as vector shapes were missed (m-1.AC2 FAIL, graded by 3.0.0_SA_CVO).
- The source PDF, read-only, into OS temp only (never the repo): `.tools/aws s3 cp s3://opal-data-irpt/irpt/cottonwood/state/vendor_documents/ART-ac668d3baaab005af9de6af46e40bbe80be2fdf0c95693d27b9c9ea05990437b/6e75336144a4a5908a4e9c5bba451c300cc8843bc12268ce26d6e7708fa158b8.pdf <OS temp>/overview.pdf` (582,765 bytes, 23 pages). Delete it when done. It is client data: print labels and coordinates only, never a figure.
- Base map facts: p3 has one chart (`p3.e02` Market Capitalization chart), p5 one (`p5.e17` Bond Sector Exposure chart); `p13.e04` is 'Expense Ratios, Sales Charges & Standardized Yields: data rows'; `p14.e03` is 'Performance Calculation Settings: {portfolio_name}'. Round-1 ids and sources never renumber or move (check m-2.AC3); only p13.e04 and p14.e03 may change.
- A new chart element: `kind` `chart`, `label` the nearest printed title, `source` the endpoint and field that would supply it or `BUILDER_ONLY`, `claim` `inferred`.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD and the decompositions). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the map carries chart elements for p3 Stock Style Exposure, p3 Market Classification, p3 Region and p5 Stock Sector Exposure (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/m-2.AC1.py`)
- **AC2** -- vector-chart detection is tested (tests -k vector in test_map_pdf.py, >= 1) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/m-2.AC2.py`)
- **AC3** -- control: every round-1 element id keeps its source, except p13.e04 and p14.e03 (PASS at the base and after) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/m-2.AC3.py`)
- **AC4** (judgment) -- every number, table and chart on the source Overview PDF is listed as an element (m-1.AC2 re-graded by 3.0.0_SA_CVO against the PDF)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-m-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/m-2.AC1.py</invocation><expect>m-2.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-m-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/m-2.AC2.py</invocation><expect>m-2.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-m-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/m-2.AC3.py</invocation><expect>m-2.AC3 RESULT: PASS</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-m-2" judgment="true"/>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-m-2.map-vector-charts-and-gaps.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-m-2.map-vector-charts-and-gaps`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 2 cut from the CTO's round-1 analysis @34daa80ad5 section 2 (E1-E5); decomposition round 2 v1.0 (`IRPT_YCDGEN_DECOMP_R2.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~2`. Risk WORLD: the gate's floor for infra paths and the class of vendor-facing work. Checks dry-run at the base: m-2.AC1 FAIL as expected; m-2.AC2 FAIL as expected; m-2.AC3 PASS (control) as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-04 ~23:0xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 @9880d0fb36, merged 9cfc9da211; m-2.AC1 PASS (4 of 4 charts: p3.e24-e26, p5.e34), m-2.AC2 PASS (4 vector tests), m-2.AC3 PASS (249 of 249 round-1 sources kept) on the merged tree; research suite 56 passed. AC4 (m-1.AC2 re-grade) is the CVO's.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>2</round>
<slot>~2</slot>
<fabric>laptop</fabric>
