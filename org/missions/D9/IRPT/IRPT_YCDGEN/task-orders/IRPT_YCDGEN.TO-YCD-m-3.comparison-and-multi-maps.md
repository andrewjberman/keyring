# IRPT_YCDGEN task order -- `YCD-m-3` -- ROUND 3 (ENRICHMENT): THE COMPARISON AND MULTI MAPS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md</decomp_doc>
<owned_cells>YCD-m-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~4</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 3** builds the Overview's held-data (167) and other-endpoint (7) elements on round 2's coverage table, fixes the keeper's series rule, and maps the Comparison and Multi reports. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-m-3` -- the Comparison and Multi maps (E6; FWD-3, FWD-4)
- By the method of m-1/m-2 (`map_pdf.py`, as is; read-only) over Cottonwood's retained certified PDFs:
  - **Multi:** Y-3's REQ-329a56182b2668d44a28c8d7.
  - **Comparison:** REQ-e4b7f5ab... or REQ-7ea49c2d....

  Locate each through its request's job checkpoint, as `live_walk/case_trace.py` does, read into OS temp only.
- Write `deliverables/maps/comparison_map.json` and `deliverables/maps/multi_map.json` (C-MAP shape, `report_type`
  `COMPARISON` / `MULTI`). Each element is sourced to an Overview call or computed method where the same figure exists
  there, else to a candidate endpoint (`claim` `inferred`), else `BUILDER_ONLY`. These are maps only; no layout this round.

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

- The method is m-1/m-2's: `ycharts/research/map_pdf.py` (pdfplumber words, tables, embedded images and vector-drawn chart regions) gives the element skeleton per page; you READ it and run it, you do not edit it. The Overview map (`deliverables/maps/overview_map.json`, 253 elements) and its coverage table (`overview_coverage.json`) show the sourcing style.
- The retained certified PDFs (ORIGINAL_VENDOR_PDF family) of three READY Cottonwood requests: Multi `REQ-329a56182b2668d44a28c8d7` (ULT + IWM); Comparison `REQ-e4b7f5aba7fb218c37f28002` and `REQ-7ea49c2d9b27957d0ea8888f`. Locate each PDF read-only through the request's rows, as `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py` does (it re-hashes the retained PDF by the version its checkpoint names), into OS temp only; delete them when done. Use the Comparison request whose PDF is a Comparison (variant 2, one comparison key); say which in `source_pdf`.
- Each map: `schema` `irpt-ycdgen-map-v1`, `report_type` `COMPARISON` or `MULTI`, `template_id` (from the PDF or the request's recipe), `source_pdf` `{bucket, artifact_prefix, pages}`, `calls` (reuse the Overview map's call names where the same data serves), `elements` (every number, table and chart, labels only). No figure value enters git (C-FIRM).

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/comparison_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- both maps present with schema, report type and source_pdf, and every page of each source PDF holds at least one element (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/m-3.AC1.py`)
- **AC2** (judgment) -- every number, table and chart on each source PDF is listed as an element, and no figure value is in either file (graded by 3.0.0_SA_CVO against the PDFs)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-m-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/m-3.AC1.py</invocation><expect>m-3.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-m-3" judgment="true"/>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~4/IRPT_YCDGEN.TO-YCD-m-3.comparison-and-multi-maps.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-m-3.comparison-and-multi-maps`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 3 cut from the CTO's round-2 analysis section 2 (E1-E6); decomposition round 3 v1.0 (`IRPT_YCDGEN_DECOMP_R3.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~4`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: m-3.AC1 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~01:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~4 @9c4d183fd6, merged 04c20019c8; m-3.AC1 PASS (Comparison 32/32 pages from REQ-7ea49c2d, Multi 34/34 from REQ-329a5618). AC2 (every figure listed; no figure value) is the CVO's. Rows W4-S1..S4 noted: landscape page footers kept as BUILDER_ONLY text; the C-MAP extension for second/third securities (column_sources, key_index, comparison_* calls) accepted for round 4's layouts; REQ-e4b7f5ab is not Comparison evidence (no key printed).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>3</round>
<slot>~4</slot>
<fabric>laptop</fabric>
