# IRPT_YCDGEN task order -- `YCD-m-1` -- ROUND 1 (THE THREAD): THE OVERVIEW ELEMENT MAP FROM A RETAINED CERTIFIED OVERVIEW PDF

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP.md</decomp_doc>
<owned_cells>YCD-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 1** builds the thread: one Cottonwood Overview end to end. Nothing in this round calls YCharts or writes the store from a worker; the issuer makes the one live run at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `YCD-m-1` -- the Overview element map from a retained certified Overview PDF (S04; FWD-1, FWD-3)
- Find a retained Overview among Cottonwood's ORIGINAL_VENDOR_PDF objects (bucket `opal-data-irpt`, prefix
  `irpt/cottonwood/state/vendor_documents/`), READ-ONLY, in memory: page 1's title and the template's report type
  (`aggregate_security_overview`, template 14141822) identify it. No object is written and no PDF is saved to disk in the repo.
- `ycharts/research/map_pdf.py`: lists every number, table and chart on each page (pdfplumber words, tables and image or
  vector-chart regions) with its printed label, as the element skeleton.
- The map file (2.3): for each element, the YCharts DATA endpoint and field that supplies it, chosen from the endpoints the
  estate already calls (the gateway's `infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py`: `/charts/general_data.json`,
  `/charts/fund_data.json`, `/indices/table_data`, `/charts/scatter_plot_data.json`, `/securities/securities_info`) and the
  2026-09 field scrape `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`; or `BUILDER_ONLY` when no
  data endpoint carries it. Every source is `claim: "inferred"` until the live run measures it.
- `calls` lists each data call the elements need, deduplicated, with its params template.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decomposition)

## 2. CONTRACTS THE CELLS SHARE (fixed for round 1)

### 2.1 The kept object (C-KEEP) -- written by the keeper, one per call

Key: `address('irpt', firm, 'state', 'ycharts_responses', 'request=' + request_id, object='step=%02d_%s.json' % (step, name))`.

```json
{
 "schema": "irpt-ycdgen-kept-v1",
 "request_id": "REQ-...", "firm": "cottonwood", "step": 1, "name": "snake_case_call_name",
 "call": {"method": "GET", "path": "/charts/general_data.json", "query": {"securities": "id:P:123,include:true,,"},
          "body_keys": []},
 "response": {"status": 200, "content_type": "application/json", "bytes": 1234, "sha256": "<hex of the kept body bytes>",
              "body_json": {}, "body_b64": null},
 "shape": "IDENTIFIERS | DATA | DOCUMENT",
 "changed_since_previous": "true | false | no_previous",
 "kept_at": "2026-10-04T00:00:00Z"
}
```

- **Scrub:** any key (at any depth, in `query`, `body_json` or a header-like map) matching
  `(?i)cookie|token|csrf|session|password|secret|authorization|api[_-]?key|credential` has its value replaced by
  `"<scrubbed>"`; any string value carrying `ycsessionid=`, `csrftoken=`, `aws-waf-token=` or `cf_clearance=` is replaced
  the same way. `sha256` is of the SCRUBBED body bytes, so a rotated cookie never reads as a changed answer.
- **Shape** (one axis: what the call gave back): `DOCUMENT` when the content type is `application/pdf` or `application/zip`
  or the body starts with `%PDF`; else, for JSON, `DATA` when it holds a key `raw_data`, `calc_raw_value` or `chart_data`, or
  any list of two or more numbers (or of `[number, number]` pairs); else `IDENTIFIERS`.
- `changed_since_previous` compares `sha256` with the same call name's sha256 in the previous run for the same portfolio;
  the caller passes that previous sha256 (or none).

### 2.2 The run record (C-RUN) -- `ycharts_runs/request=<REQ>/run.json`

```json
{
 "schema": "irpt-ycdgen-run-v1",
 "request_id": "REQ-...", "firm": "cottonwood", "report_type": "OVERVIEW", "template_id": "14141822",
 "portfolio": {"security_id": "P:123"}, "window": {"start": null, "end": null},
 "lease": {"fence": 7, "session_fence": 25},
 "calls": [{"step": 1, "name": "...", "key": "irpt/cottonwood/state/ycharts_responses/...", "shape": "DATA",
            "sha256": "...", "changed_since_previous": "no_previous", "status": 200,
            "started_at": "...", "ycharts_ms": 812, "waited_ms": 2000}],
 "elements": [{"id": "p1.e03", "source": {"call": "...", "field": "$.chart_data[0][0].raw_data"}},
              {"id": "p2.e01", "source": "NOT_AVAILABLE", "reason": "BUILDER_ONLY"}],
 "clocks": {"ycharts_working_ms": 0, "opal_waiting_ms": 0, "opal_building_ms": null},
 "report": null,
 "status": "COMPLETE | STOPPED", "stop_reason": null
}
```

- **Three clocks (FWD-6):** `ycharts_working_ms` sums each call's request-sent-to-last-byte time; `opal_waiting_ms` sums the
  time held by the lease's spacing (`next_allowed_at`), the lease queue or a poll interval; `opal_building_ms` is the
  layout's. The runner writes the record with `opal_building_ms: null` and `report: null`; the layout fills both and
  rewrites the same key.
- `elements` copies the map's element ids and sources (the trace from each element to its call and field).

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

- Retained YCharts PDFs for Cottonwood (READ-ONLY, measured at the cut): bucket `opal-data-irpt`, prefix `irpt/cottonwood/state/vendor_documents/`, 12 objects (2026-09-27 to 2026-10-03). The ~580 KB ones are likely Overviews; 827-937 KB are likely Comparison or Multi. List with `.tools/aws s3api list-objects-v2 --bucket opal-data-irpt --prefix irpt/cottonwood/state/vendor_documents/`, read with `get-object` into your OS temp dir (OUTSIDE the repo) and delete it when done. Page 1's title and report type (`aggregate_security_overview`, template 14141822) identify an Overview.
- Local libraries: pdfplumber 0.11.9, pypdf 6.12.2, PyMuPDF (fitz) 1.27.1.
- YCharts DATA endpoints the estate already calls (`infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py`): GET `/charts/general_data.json` (`securities=id:<sym>,include:true,,`, `metrics=id:<m>,include:true,,`, `xAxis=time`, optional `startDate`/`endDate`; reads `chart_data[0].raw_data`); GET `/charts/fund_data.json` (`calcs=id:<calc>,include:true,,`, `securities=...`, `zoom=max`, `maxPoints=100000`, `partner=basic_2000`; reads `chart_data[0][0].raw_data`); GET `/indices/table_data` (`indices`, `columns`; reads `indicesData[].data[].calc_name` and `calc_raw_value`); POST `/charts/scatter_plot_data.json` (`xAxisMetric`, `yAxisMetric`); GET `/securities/securities_info?securities=`. The 2026-09 field scrape of a YCharts report: `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`. The CRO's research: `docs/research/investor_reporting_ycharts_cloud_20260911/README.md` and `docs/research/investor_reporting_ycharts_variants_20260911/`.
- A portfolio's typed id is `P:<model_portfolio_id>`; the map's params use the `{security_id}` placeholder for it.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD and this decomposition). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, and none of another cell's files. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (create it if absent: a `#` title, then one `## <ROW-ID> -- <title>` section with a fenced json row per surprise), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/map_pdf.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_map_pdf.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the map validates against contract 2.3: every page has elements, every source names a listed call or BUILDER_ONLY, and no figure-shaped string is in the file (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/checks/m-1.AC1.py`)
- **AC2** (judgment) -- every number, table and chart on the source Overview PDF is listed as an element (graded by 3.0.0_SA_CVO against the PDF)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-m-1"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/checks/m-1.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-m-1" judgment="true"/>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-m-1.overview-element-map.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-m-1.overview-element-map`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** PRD v0.1 @8b364d6d94 (RATIFIED; CTO 104764); decomposition round 1 v1.0 (`IRPT_YCDGEN_DECOMP.md`); Andrew-direct order @ee801b0505 and egress/subscription word @ce20ca6854; endpoint confirmed ("all approved", CTO 104738). Chain `~2`. Risk WORLD: the floor the gate infers for infra paths (spine v3.19 L6). Checks dry-run at base CLOUD d2a93927af: m-1.AC1 FAIL (absent) as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>1</round>
<slot>~2</slot>
<fabric>laptop</fabric>
