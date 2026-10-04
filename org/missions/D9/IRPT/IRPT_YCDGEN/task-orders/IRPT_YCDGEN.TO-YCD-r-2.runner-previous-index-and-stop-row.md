# IRPT_YCDGEN task order -- `YCD-r-2` -- ROUND 2 (ENRICHMENT): THE RUNNER'S PREVIOUS-RUN LOOKUP AND ITS STOP ROW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R2.md</decomp_doc>
<owned_cells>YCD-r-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 2** enriches round 1's live thread (one Cottonwood Overview, run `YCD-R1-20261004T1944Z`: 2 of 12 calls answered with data; 176 of 249 elements have no answer). No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-2 decomposition)

### `YCD-r-2` -- the runner's previous-run lookup and its stop row (E4, E5; FWD-2, C-SESSION)
- `ycharts/research/runner.py`:
  - `RunIndex(s3_client)` with `get(firm)` and `put(firm, doc)` at 2.5's key.
  - `main()` reads the index BEFORE the lease (2.5 refusal; `--bootstrap-index` writes an empty one), passes the
    previous run.json for the portfolio (via `RunStore.get`) to `run()`, and after the run writes the portfolio's entry
    when at least one call was kept.
  - `run()` on a STOP writes 2.6's stop row through a `stops` writer (same S3 client), after the lease is released.
- `ycharts/research/file_stop_row.py`, as in 2.6.
- Tests (in `tests/test_runner.py`, plus `tests/test_file_stop_row.py`):
  - a run-2-then-run-3 case reads `changed_since_previous` `false` for an unchanged answer and `true` for a changed one,
    and `no_previous` only for a portfolio absent from the index;
  - a missing index refuses before any lease, and `--bootstrap-index` writes an empty index;
  - a WAF-challenged call writes a stop row whose `world_is` names the step and decision, and the lease is released;
  - `file_stop_row.py` prints a section the surprise-row gate's schema admits.

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

### 2.5 The previous-run index (FWD-2; cell YCD-r-2)

- Key: `address('irpt', firm, 'state', 'ycharts_runs', 'index=latest', object='latest_by_portfolio.json')`, i.e.
  `s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/index=latest/latest_by_portfolio.json` for Cottonwood.
  It sits inside the research principal's Put/Get grant (`ycharts_runs/*`); no list grant exists or is added.
- Body: `{"schema": "irpt-ycdgen-run-index-v1", "firm": "...", "portfolios": {"P:123": {"request_id": "...",
  "run_key": "...", "at": "..."}}}`.
- Without a list grant, a missing key reads AccessDenied, the same as a real permission failure. So a missing or
  unreadable index REFUSES before the lease (`RUN_REFUSED:PREVIOUS_INDEX_UNREADABLE`), unless the CLI is given
  `--bootstrap-index`; that flag writes an empty index and is used once per firm by the issuer.
- After a run that kept at least one call, the runner writes the index entry for its portfolio (read, modify, write).
  Runs are serialized by the lease, so the read-modify-write cannot race.
- `changed_since_previous` is `no_previous` only when the index has no entry for the portfolio.

### 2.6 The stop row (C-SESSION; cell YCD-r-2)

- On any STOP (a STOP_DECISIONS reply, a lease refusal, a lease-release failure), the runner writes
  `address('irpt', firm, 'state', 'ycharts_runs', 'request=' + request_id, object='stop_row.json')` beside run.json. It
  is a surprise-row-shaped object WITHOUT an `id`: `project`, `fabric` (`laptop`), `surfaced_by` (the runner's
  `--surfaced-by`, default `2.0.0_SA_COO~Y`), `surfaced_at`, `one_line`, `class` `OBSERVATION`, `hazard_standing`
  `INERT`, `grounding` (status GROUNDED; evidence = the run key and the stop reason), `disposition`
  `UNDER_INVESTIGATION`, `spec_asserts` (the C-SESSION sentence), `world_is` (the step, call name, HTTP status and
  decision).
- `ycharts/research/file_stop_row.py <stop_row.json> <row-id>` prints the channel section (`## <id> -- <title>` and a fenced
  json row with the id set) for the issuer to append and commit. The issuer files it; the runner never writes git.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `ycharts/research/runner.py` at the base: `run(*, session, store, runs, firm, request_id, portfolio_security_id, map_doc, clock, previous=None, window=None, min_gap_s=0)`; `STOP_DECISIONS`; `RunStore(s3).put/get`; `run_location(firm, request_id)`; `research_s3(boto3, region, firm, request_id)` (the firm's research principal); `_compose(bindings_path, firm, request_id)`; `main()` with `--previous-request` (read by `RunStore.get`). Keep every existing test passing.
- `ycharts/research/keeper.py`: `_naming()` returns `lib/opal_naming.py`, whose `address(system, firm, tier, table, partition, object=...)` is the builder; `_canonical(obj)` gives canonical JSON bytes; `kept_object(..., previous_sha256=...)` computes `changed_since_previous`.
- `tests/test_runner.py` has `World` (a real OperationLease over an in-memory DynamoDB double, `FakeS3`) and `valid_run_record`. The run record's key set is fixed (2.2); the stop row is a SEPARATE object.
- A filed surprise row carries `id`, `project`, `fabric`, `surfaced_by`, `surfaced_at`, `one_line`, `class`, `hazard_standing`, `grounding` (`status`, `evidence` list), `disposition`, `spec_asserts`, `world_is`; read rows in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` for the exact shape.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD and the decompositions). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/runner.py
infra/aws/lambda/investor-reporting/ycharts/research/file_stop_row.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_file_stop_row.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the previous-run index: run 2 then run 3 reads false/true per call, no_previous only off the index, a missing index refuses before the lease, --bootstrap-index writes an empty one (tests -k 'previous or index', >= 3) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/r-2.AC1.py`)
- **AC2** -- the stop row: a challenged call writes stop_row.json naming the step and decision with the lease released; file_stop_row.py prints a channel section (tests -k stop_row, and test_file_stop_row.py) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/r-2.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-r-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/r-2.AC1.py</invocation><expect>r-2.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-r-2"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/r-2.AC2.py</invocation><expect>r-2.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-r-2.runner-previous-index-and-stop-row.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-r-2.runner-previous-index-and-stop-row`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 2 cut from the CTO's round-1 analysis @34daa80ad5 section 2 (E1-E5); decomposition round 2 v1.0 (`IRPT_YCDGEN_DECOMP_R2.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~1`. Risk WORLD: the gate's floor for infra paths and the class of vendor-facing work. Checks dry-run at the base: r-2.AC1 FAIL as expected; r-2.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-04 ~22:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @fd43467321, merged 988a62c350; r-2.AC1 PASS (6 tests), r-2.AC2 PASS (4 + 4); research suite 51 passed on the merged tree. Issuer note: per 2.5 a STOPPED run with kept calls replaces the portfolio's index entry, so a call absent from it reads no_previous on the next run (accepted as written; carried to the round close).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>laptop</fabric>
