# IRPT_YCDGEN task order -- `YCD-r-3` -- ROUND 3 (ENRICHMENT): THE RUNNER'S HOLDINGS AND EXPAND CALLS, AND THE KEEPER'S SERIES RULE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md</decomp_doc>
<owned_cells>YCD-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 3** builds the Overview's held-data (167) and other-endpoint (7) elements on round 2's coverage table, fixes the keeper's series rule, and maps the Comparison and Multi reports. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-r-3` -- the runner's holdings and expand calls, and the keeper's series rule (E1 data side, E3, W3-S3; FWD-1, FWD-2, FWD-3)
- `ycharts/research/runner.py`: contracts 3.1 and 3.2. `plan_calls(..., holdings=None)` expands; `main --holdings-from`
  reads the frozen input with the host role's clients (`_compose` returns them beside the research S3 client); `run()`
  takes `holdings` and writes the `holdings` block and schema v2.
- `ycharts/research/keeper.py`: contract 3.3.
- Tests: expand planning (chunking, item format, order, kept names `__cNN`, refusal without holdings); the holdings read
  over fake clients shaped like the served rows (a corrected row reads its corrected ticker); run.json v2 keeps every v1
  key; the scatter-shaped answer labels DATA.

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

### 3.1 The expand call (C-MAP v2; built by YCD-r-3, used by YCD-w-3)

A map call may carry:

```json
"expand": {"over": "holdings", "param": "indices", "chunk": 20, "item": "{ticker}", "join": ","}
```

- `param` names the one param the runner fills with the chunk. `item` is `{ticker}` or `id:{ticker},include:true,,`.
  `chunk` is 1-50.
- The runner issues one request per chunk of the holdings' tickers, in the holdings' order. Each answer is kept under the
  name `<call name>__c<kk>` (kk = 01, 02, ...), with one step per chunk, continuing the run's step numbers.
- Every other param is filled as today: `{security_id}`, `{start}`, `{end}`.
- `runner.plan_calls(map_doc, security_id, window, holdings=None)` plans the expanded requests. An `expand` call with no
  holdings given REFUSES before any lease (`EXPAND_REQUIRES_HOLDINGS:<name>`).

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

### 3.3 The keeper's series rule (C-KEEP; built by YCD-r-3)

`shape` is `DATA` when a JSON answer holds a `series` key whose value is a list of objects, any of which carries a list
of numbers or of `[number, number]` pairs (YCharts' scatter answer, `data.series`). It is added to the existing DATA keys,
and no other label changes.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `runner.py` at the base: `plan_calls(map_doc, portfolio_security_id, window=None)`; `run(*, session, store, runs, firm, request_id, portfolio_security_id, map_doc, clock, previous=None, window=None, min_gap_s=0, stops=None)`; `RunIndex`, `RunStore`, `research_s3(...)`, `_compose(bindings_path, firm, request_id)`; `main()` with `--bootstrap-index`, `--previous-request`, `--min-gap-s`. `READ_ONLY_POSTS` admits one POST. Keep every existing test passing (tests/test_runner.py, 25 tests at the base).
- `keeper.py`: `_shape(...)` (or the function that sets `shape`) uses DATA keys `raw_data`, `calc_raw_value`, `chart_data` and numeric lists. Round 2's live scatter answer has `{"data": {"series": [...], ...}, "params": {...}}` and was labelled IDENTIFIERS.
- The served request reads: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/case_trace.py` reads the `irpt-requests` row (consistent GetItem) and the composition object by the version the row names. Mirror its key and field names; your tests use fakes shaped like those rows, never live AWS.
- The Y-5 request whose frozen input the close run will read: `REQ-a618aa83407689bc95193a01` (tenant `cottonwood`); its document's rows carry `security_id` (the resolved symbol, e.g. SGOV where the user corrected TIMXX) and `original.quantity.value`; `basis` is `USD`.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/runner.py
infra/aws/lambda/investor-reporting/ycharts/research/keeper.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_keeper.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- expand planning and the holdings read: chunking, item format, order, kept names __cNN, refusal without holdings, a corrected row's ticker, run.json v2 keeps every v1 key (tests -k 'expand or holdings', >= 3) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/r-3.AC1.py`)
- **AC2** -- the keeper labels a series-shaped answer DATA (tests -k series in test_keeper.py, >= 1) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/r-3.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-r-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/r-3.AC1.py</invocation><expect>r-3.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-r-3"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/checks/r-3.AC2.py</invocation><expect>r-3.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-r-3.runner-holdings-expand-and-series-shape.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-r-3.runner-holdings-expand-and-series-shape`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 3 cut from the CTO's round-2 analysis section 2 (E1-E6); decomposition round 3 v1.0 (`IRPT_YCDGEN_DECOMP_R3.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~1`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: r-3.AC1 FAIL as expected; r-3.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~01:1xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @5a982069a6, merged dd418f6555; r-3.AC1 PASS (8), r-3.AC2 PASS (2) on the merged tree. **Issuer ruling on row W1-S1:** run.json is v2 with `holdings` only when the run is given holdings, v1 unchanged otherwise -- accepted as built (v1's exact key pin stays valid; the layout reads v1 as no holdings).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>3</round>
<slot>~1</slot>
<fabric>laptop</fabric>
