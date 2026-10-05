# IRPT_YCDGEN task order -- `YCD-c-2` -- ROUND 2 (ENRICHMENT): THE COVERAGE TABLE FOR THE 176 UNANSWERED ELEMENTS, AND THE PROBE MAP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R2.md</decomp_doc>
<owned_cells>YCD-c-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 2** enriches round 1's live thread (one Cottonwood Overview, run `YCD-R1-20261004T1944Z`: 2 of 12 calls answered with data; 176 of 249 elements have no answer). No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-2 decomposition)

### `YCD-c-2` -- the coverage table for the 176 unanswered elements, and the probe map (E3; FWD-3, FWD-1 depth)
- Inputs, read-only: the map; run 3's kept answers (`s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/
  request=YCD-R1-20261004T1944Z/`, six objects, read with the laptop's credentials into OS temp, never into the repo); the
  HAR request shapes file the issuer extracted (method, path and parameter NAMES only); the estate's YCharts clients
  (the gateway's `client.py`, `ycharts-market-data-pull/ycharts_client.py`); the security-level data Opal already reads
  (the served generate path's `securities_info`, `general_data`, `fund_data` uses).
- Output: 2.7's two files. No figure value enters git (C-FIRM): classes, reasons, endpoint paths and field paths only.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

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

### 2.7 The coverage table and the probe map (cell YCD-c-2)

- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json`:
  `{"schema": "irpt-ycdgen-coverage-v1", "run": "YCD-R1-20261004T1944Z", "elements": [{"id": "p2.e05", "class":
  "HELD_DATA | OTHER_ENDPOINT | BUILDER_ONLY", "reason": "one line", "via": {...}}]}`.
  - `HELD_DATA`: computable from security-level answers weighted by the portfolio's holdings, which Opal holds (the
    frozen upload); `via` names the security-level endpoint and field, and the weighting.
  - `OTHER_ENDPOINT`: a YCharts endpoint that answers for a model portfolio; `via` names the probe call (by `name` in the
    probe map).
  - `BUILDER_ONLY`: neither; `reason` says why.

  Exactly one class per element, for exactly the 176 element ids run 3 left with no answer.
- `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/coverage_probe_map.json`: the C-MAP shape (2.3) holding `calls`
  only (and `elements: []`): one candidate call per OTHER_ENDPOINT route, each GET or the one admitted read-only POST, with
  the same placeholders. It is what the issuer runs live at close.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- The 176 element ids are the list `IDS` inside the check `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/c-2.AC1.py`: every element of the map whose call run 3 did not answer with a 2xx (steps 03-06 answered 400/404; steps 07-12 were never called after the firewall stop at step 7).
- Run 3's six kept answers (read-only, laptop credentials, into OS temp only): `.tools/aws s3 cp s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R1-20261004T1944Z/ <OS temp>/kept --recursive`. Statuses: 01 securities_info 200; 02 fund_data level series 200; 03 scatter_plot_data POST 400 (`Invalid x axis metric: standard_deviation_5y, Invalid y axis metric: annualized_total_return_5y`); 04 table_data 400; 05 and 06 table_data 404 (`indices=P:<id>` does not serve a model portfolio). Client data: read field NAMES and shapes only.
- The HAR request shapes (method, path, parameter NAMES only; no value, cookie or header), extracted by the issuer: `C:/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/b55fbe94-a2b0-45e3-adad-582b87cc1103/scratchpad/har_request_shapes.json`. It lists, among others, `/calculations/all_calc_menu*.json` (YCharts' calc ids), `/dashboard/fund_chart_module_data/{n}`, `/dashboard/scatter_plot_module_data/{n}`, `/model_portfolios/transition_analysis/list`.
- The estate's YCharts clients: `infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py`, `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`; the served generate path (`ycharts/generate/`) and its HAR fixtures (`ycharts/generate/fixtures/har/`) show the model-portfolio routes YCharts' own app calls.
- HELD_DATA means the element can be computed from SECURITY-level answers (for example table_data with real tickers) weighted by the portfolio's holdings in the frozen upload (the normalized portfolio's rows: identifier and quantity). State the endpoint, field and weighting in `via`.
- The probe map is planned by `runner.plan_calls`: GET, or a POST only to `/charts/scatter_plot_data.json`; placeholders `{security_id}`, `{start}`, `{end}`.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD and the decompositions). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k), never an edit outside them.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/coverage_probe_map.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the coverage table classifies exactly the 176 ids, one class each from HELD_DATA / OTHER_ENDPOINT / BUILDER_ONLY with a reason, every OTHER_ENDPOINT naming a probe call (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/c-2.AC1.py`)
- **AC2** -- the probe map plans through runner.plan_calls without a refusal (GET or the admitted POST) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/c-2.AC2.py`)
- **AC3** (judgment) -- no figure value from a client file or vendor answer is in either file (C-FIRM), graded by 3.0.0_SA_CVO

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-c-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/c-2.AC1.py</invocation><expect>c-2.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-c-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/c-2.AC2.py</invocation><expect>c-2.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-c-2" judgment="true"/>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-c-2.coverage-table-and-probe-map.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-c-2.coverage-table-and-probe-map`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 2 cut from the CTO's round-1 analysis @34daa80ad5 section 2 (E1-E5); decomposition round 2 v1.0 (`IRPT_YCDGEN_DECOMP_R2.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~3`. Risk WORLD: the gate's floor for infra paths and the class of vendor-facing work. Checks dry-run at the base: c-2.AC1 FAIL as expected; c-2.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-04 ~22:5xZ):** worker 0.9.0_WK_IRPT_YCDGEN~3 @c41213cc7f, merged 14254f9b70; c-2.AC1 PASS (176/176: 167 HELD_DATA, 7 OTHER_ENDPOINT, 2 BUILDER_ONLY), c-2.AC2 PASS (2 probe calls) on the merged tree; AC3 (C-FIRM) is the CVO's. Rows W3-S2, W3-S3 (their surfaced_at reads 2026-10-05T00:30Z; the worker reports the true time as ~2026-10-04T22:52Z). The issuer's close runs the probe map live.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>2</round>
<slot>~3</slot>
<fabric>laptop</fabric>
