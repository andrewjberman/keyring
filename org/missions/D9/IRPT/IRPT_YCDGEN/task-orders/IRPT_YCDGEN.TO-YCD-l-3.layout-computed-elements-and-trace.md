# IRPT_YCDGEN task order -- `YCD-l-3` -- ROUND 3 (ENRICHMENT): THE LAYOUT COMPUTES THE HELD-DATA AND OWN-SERIES ELEMENTS, WITH THE TRACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md</decomp_doc>
<owned_cells>YCD-l-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 3** builds the Overview's held-data (167) and other-endpoint (7) elements on round 2's coverage table, fixes the keeper's series rule, and maps the Comparison and Multi reports. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-l-3` -- the layout computes the held-data and own-series elements, with the trace (E1 build side; FWD-1, FWD-3)
- `ycharts/research/layout_overview.py`: the 3.4 methods and statistics over kept answers, including the chunked
  `__cNN` names and run.json's `holdings`; the 3.5 trace written into the finished run.json; the page prints each value or
  the not-available line with its reason.
- Tests on fixtures: each METHOD on a small hand-checked case; sleeve renormalization; coverage below 0.95 gives
  NOT_AVAILABLE with its reason; the trace lists the kept keys used.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

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

### 3.2 The holdings (C-RUN v2; built by YCD-r-3, read by YCD-l-3)

- `runner.main --holdings-from <REQ-id>` reads the frozen input of that served request, read-only, with the HOST role's S3
  and DynamoDB clients (the research principal cannot read `opal-data-irpt`).
  - The `irpt-requests` row gives the request's composition reference, and the composition's `resolved.document.rows` gives
    each row. Follow `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py` for the reads.
  - A row's ticker is its resolved symbol (`security_id`, which carries the user's correction, e.g. SGOV for TIMXX); its
    amount is `original.quantity.value`; `basis` is the document's `basis`.
- run.json gains `"holdings": {"source_request": "REQ-...", "basis": "USD", "rows": [{"ticker": "AAPL", "amount": "123.45"}]}`,
  and `schema` becomes `irpt-ycdgen-run-v2`; every v1 key is kept.
- The amounts are client figures. They live only in the firm's store, never in git or a log line.

### 3.4 Computed element sources (C-MAP v2; written by YCD-w-3, computed by YCD-l-3)

A map element's `source` may be:

```json
{"computed": "<METHOD>", "call": "<call name>", "columns": ["calc ids"], "field": "<JSONPath per security>",
 "sleeve": "stock | bond | null", "statistic": "<series statistic id or null>"}
```

METHOD is one of:
- `WEIGHTED_MEAN`: `sum_i w_i * v_i` over holdings with an answer.
- `WEIGHTED_MEAN_SLEEVE`: the same, with `w_i` scaled by holding i's sleeve share (its `asset_allocation_stock` or
  `asset_allocation_bond` answer) and renormalized to 1.
- `HARMONIC_WEIGHTED_MEAN`: `1 / sum_i (w_i / v_i)`.
- `SUM`: `sum_i v_i`.
- `BUY_AND_HOLD`: the portfolio value path `V(t) = sum_i amount_i * series_i(t) / series_i(t0)`, then `statistic`.
- `OWN_SERIES`: `statistic` over the portfolio's own kept level series (step `portfolio_level_series`).

Weights: `w_i = amount_i / sum(amount)` for basis `USD`; `w_i = amount_i` for a weight basis.

Statistic ids (series methods): `total_return_<1m|3m|ytd|1y|3y|5y|10y|15y>`, `annualized_return_<3y|5y|10y|15y>`,
`std_dev_<1y|3y|5y|10y|15y>` (annualized from monthly returns), `max_drawdown_<1y|3y|5y|10y|all>`, `cumulative_series`.

The coverage table gains class `OWN_SERIES` (row W3-S2): an element computable from the portfolio's own kept level
series. Its `via` names the statistic.

### 3.5 The computed trace (C-RUN v2; written by YCD-l-3)

When the layout finishes, each computed element's entry in run.json's `elements` carries:

```json
"computed": {"method": "...", "inputs": ["kept keys"], "coverage": 0.0-1.0, "status": "VALUE | NOT_AVAILABLE", "reason": null}
```

- `coverage` is the weight share of holdings with an answer.
- Below 0.95 the element is NOT_AVAILABLE with reason `COVERAGE_BELOW_0.95` (issuer ruling). A missing input gives
  `INPUT_MISSING:<call>`.
- The page prints the value, or the not-available line with its reason. Never an approximation (C-BUILDERONLY).

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `layout_overview.py` at the base: `load_kept(dir)` keys kept objects by call `name` (a chunked call's kept names are `<call>__c01`, `__c02`, ...: gather them by prefix); `element_value(element, kept_by_name)` returns `value`, `builder_only`, `not_answered` (no 2xx answer kept) or `unread`; `build(run_doc, kept_by_name, map_doc, brand)`; `finish(run_doc, pdf, built_ms)`. Keep every existing test passing (tests/test_layout_overview.py).
- A `/indices/table_data` answer: `{"indicesData": [{"id": "AAPL", "data": [{"calc_name": "...", "calc_raw_value": 1.23}]}]}` (the gateway reads it by calc_name: `infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py:74-98`). A `/charts/fund_data.json` answer with several securities: `chart_data` is a list per security, each `[[{"raw_data": [[ts_ms, value], ...]}]]` (series per security in request order).
- Your tests use small fixtures (3 holdings, hand-checked numbers you write), never a client figure.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- each 3.4 METHOD computes a hand-checked value on fixtures, sleeve renormalization included (tests -k computed, >= 4) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/l-3.AC1.py`)
- **AC2** -- coverage below 0.95 reads NOT_AVAILABLE with its reason, and the finished run.json carries the 3.5 trace with the kept keys used (tests -k 'coverage_below or computed_trace', >= 2) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/l-3.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-l-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/l-3.AC1.py</invocation><expect>l-3.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-l-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/l-3.AC2.py</invocation><expect>l-3.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-l-3.layout-computed-elements-and-trace.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-l-3.layout-computed-elements-and-trace`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 3 cut from the CTO's round-2 analysis section 2 (E1-E6); decomposition round 3 v1.0 (`IRPT_YCDGEN_DECOMP_R3.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~3`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: l-3.AC1 FAIL as expected; l-3.AC2 FAIL as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>3</round>
<slot>~3</slot>
<fabric>laptop</fabric>
