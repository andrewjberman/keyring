# IRPT_YCDGEN task order -- `YCD-r-1` -- ROUND 1 (THE THREAD): THE RUNNER INSIDE THE SERVED LEASE, AND THE RUN RECORD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP.md</decomp_doc>
<owned_cells>YCD-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 1** builds the thread: one Cottonwood Overview end to end. Nothing in this round calls YCharts or writes the store from a worker; the issuer makes the one live run at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `YCD-r-1` -- the runner inside the served lease, and the run record (S03, S05, S06; FWD-1, FWD-6)
- `ycharts/research/runner.py`:
  - `run(*, session, store, runs, firm, request_id, portfolio_security_id, map_doc, clock, previous=None) -> dict` where
    `session` is a `ResidentSession`-shaped object (`acquire(request_budget=..., ttl=...)` returning an
    `OperationTransport`), `store` a `KeptStore`, `runs` a writer of run.json (same builder, table `ycharts_runs`, object
    `run.json`).
  - It acquires the lease through `session.acquire(...)`, issues each of `map_doc["calls"]` in order through the transport's
    `request(path_with_query)`, keeps each answer through the keeper, and closes the transport (which releases the lease) in
    a `finally`.
  - **Clocks:** the transport's `wait` hook is wrapped so time spent waiting for `next_allowed_at` adds to
    `opal_waiting_ms`; each request's own duration adds to `ycharts_working_ms`.
  - **Stop, never storm:** a reply that `transport.decision` classifies as `WAF_REFRESH_REQUIRED`, `BROWSER_CHALLENGE` or
    `BACKOFF`, or any refusal from the lease, ends the run at once with `status` `STOPPED` and the reason; the lease is
    released; no call is retried.
  - `previous`: the previous run.json for the same portfolio, if any, gives each call's previous sha256.
  - A command-line entry (`python runner.py --firm ... --request ... --portfolio ... --map <path>`) for the issuer's host run;
    it composes the real `ResidentSession` from the environment the resident uses and prints only store keys and counts.
- Tests (`tests/test_runner.py`) with the REAL `operation_lease.OperationLease` and `OperationTransport` over an in-memory
  DynamoDB double (as `ycharts/session/tests/test_resident_session.py:18-34`) and a scripted transport: the lease is held
  during the calls and released after (also after a failure); spacing waits land in `opal_waiting_ms`; every call is kept
  and listed in run.json, valid against 2.2; a challenge on call 2 of 3 stops with STOPPED, two calls issued, lease released.

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

- This order follows `YCD-k-1` in the same worktree and slot: use `keeper.py` as built there.
- `ycharts/session/operation_lease.py`: `OperationLease(store, *, provider, account_id, clock)` (`:46`), `SPACING = 2.0`, `MAX_TTL = 900.0`, `ATTEMPTS = 3` (`:42-44`); `acquire(holder, *, session_fence, ttl)` (`:97`, refuses OPERATION_BUSY), `renew`, `reserve(token, *, hard_deadline)` (`:148`; refuses OPERATION_SPACING while `next_allowed_at > now`, then sets it to now + 2.0), `complete`, `release` (`:176`). `OperationTransport(broker, transport, *, lease, holder, ttl, invoke, clock, wait, request_budget)` (`:193`, acquires in its constructor); `request(path, method='GET', payload=None, content_type=None)` (`:242`) waits out the spacing through `wait`, reserves, invokes, completes; `close()` (`:292`) releases.
- `ycharts/session/resident_session.py`: `DynamoOperationStore(client, *, table)` (`:22`, key `{tenant: _opal, job: <key>}`); `ResidentSession(*, secrets_client, dynamo_client, jobs_table, enrolled_user_id, clock=time.time, wait=time.sleep)` (`:93`, provider `ycharts`, account `str(enrolled_user_id)`); `acquire(*, request_budget=60, ttl=120)` (`:115`) returns an `OperationTransport` over `Transport(secret_id='ycharts/session/current')`. It imports `broker`, `transport`, `deadline_transport` as top-level modules: put `ycharts/session` and `ycharts/generate` on `sys.path`.
- `ycharts/generate/transport.py`: `Transport.request(...)` returns `(record, body)` with record `{method, path, status, content_type, bytes, set_cookie_count, waf_action, login_destination, final_url_path, body_complete}` (`:508-512`); `decision(reply, operation)` (`:160`) gives WAF_REFRESH_REQUIRED on a challenge, captcha or block waf_action, BROWSER_CHALLENGE on 202/403/405 with `awswaf` in the body, BACKOFF on 429. `ReplayTransport` (`:540`) is a test double.
- In-memory DynamoDB double: `ycharts/session/tests/test_resident_session.py:18-34`; the `operation_lease` tests load the module once through importlib (`test_operation_lease.py:15-23`) -- reuse the same module object.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD and this decomposition). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, and none of another cell's files. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (create it if absent: a `#` title, then one `## <ROW-ID> -- <title>` section with a fenced json row per surprise), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/runner.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/fixtures_runner/
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the runner tests pass: lease held then released (also on failure), waits in opal_waiting_ms, every call kept and listed, a challenge stops with STOPPED (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/checks/r-1.AC1.py`)
- **AC2** -- seam probe: the tests drive the served operation_lease module, not a stand-in (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/checks/r-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-r-1"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/checks/r-1.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-r-1"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round1/checks/r-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-r-1.runner-in-lease-run-record.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-r-1.runner-in-lease-run-record`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** PRD v0.1 @8b364d6d94 (RATIFIED; CTO 104764); decomposition round 1 v1.0 (`IRPT_YCDGEN_DECOMP.md`); Andrew-direct order @ee801b0505 and egress/subscription word @ce20ca6854; endpoint confirmed ("all approved", CTO 104738). Chain `~1`. Risk WORLD: the floor the gate infers for infra paths (spine v3.19 L6). Checks dry-run at base CLOUD d2a93927af: r-1.AC1 FAIL (absent) as expected; r-1.AC2 FAIL (absent) as expected.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>1</round>
<slot>~1</slot>
<fabric>laptop</fabric>
