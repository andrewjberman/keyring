# IRPT_YCDGEN task order -- `YCD-r-5` -- ROUND 5 (ENRICHMENT): THE RUNNER'S 12-REQUEST PLAN, THE REQUEST HASH, AND THE LOOKUP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R5.md</decomp_doc>
<owned_cells>YCD-r-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 5** cuts the Overview to a 12-request plan (Andrew's bar: the report in one sitting), feeds the held-data elements from data Opal already holds, wires the six risk statistics, keys the change flag on the request, and closes the two maps' residuals. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-5 decomposition)

### `YCD-r-5` -- the runner's 12-request plan, the request hash, and the lookup (E1 runner half, E4 build; FWD-6, FWD-2)
- `runner.py`: 5.1's print and refusal; 5.4's `request_sha256` and the flag rule (with `keeper.py` if the flag is computed there).
- `lookup.py` (new): 5.4's one-command lookup.
- Tests:
  - the PLAN line;
  - a 13-request plan refuses before the lease;
  - a changed parameter under one call name reads `request_changed`, not `true`;
  - an unchanged request with a changed answer reads `true`;
  - the lookup prints a kept record from a fake store.

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

### 4.1 The call budget (built by YCD-r-4)

- `runner.run(..., budget=None)`. `budget` is `{"requests_per_window": N, "window_seconds": W}`; N is 1-6 and W is a positive
  int.
- With a budget, the planned requests are split into windows of at most N. After each window the runner releases the lease
  (`transport.close()`), waits W seconds through the session's wait (counted in `opal_waiting_ms`), and acquires a fresh lease
  for the next window. It never sends an (N+1)th request inside one window.
- Without a budget, a plan of more than 6 requests REFUSES before any lease (`BUDGET_REQUIRED:<n> requests`). Six or fewer run
  as today.
- CLI: `--requests-per-window N --window-seconds W`.
- A STOP inside any window ends the whole run (the C-SESSION stop rules hold per window).

### 5.1 The 12-request plan (YCD-r-5 runner half; YCD-p-5 map half)

- `MAX_RUN_REQUESTS = 12` (2 windows of 6; CTO round-4 ruling 1).
- Before the first call (and before the lease), `runner.main` prints one line: `PLAN requests=<n> windows=<w>
  per_window=<N> window_seconds=<W>`. With no budget, `windows=1` and `per_window=6`.
- A plan over 12 requests REFUSES before the lease, with `PLAN_OVER_BUDGET:<n> requests (max 12)`. It refuses with or without
  `--requests-per-window`.
- The Overview map (`deliverables/maps/overview_map.json`) keeps only the calls an element reads. With Y-5's 99 holdings it
  plans to at most 12 requests, counting `YCD-p-5`'s benchmark call.
- An element whose call is not in the map reads NOT_AVAILABLE, with reason `OUTSIDE_TIME_BUDGET`. Its line reads "Not
  available: outside the run's time budget."
- No answer kept from an earlier run stands in for a call in this run.

### 5.4 The request hash and the lookup (YCD-r-5)

- Each kept call records `request_sha256`: the sha256 of the canonical JSON of `{method, path, params}` after templating.
- `changed_since_previous` compares against the previous run's kept call with the same name AND the same `request_sha256`:
  - same request: `true` or `false` as before;
  - no previous call with that name: `no_previous`;
  - a previous call with the name but a different request: `request_changed` (never `true`).
- A previous run record without `request_sha256` reads `no_previous`.
- `research/lookup.py` (new): `python lookup.py --firm <f> --request <REQ> --call <name>` prints the call's kept record for an
  analyst. That is its status, shape, sha256, request_sha256, changed_since_previous and kept_at, plus a one-line summary of
  the answer's kind (identifiers, data or document) and size. It reads through the keeper's store and prints no figure value
  from a client file.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `runner.py` at the base (round 4 merged): `split_windows(planned, budget=None)` with at most 6 a window (`BUDGET_REQUIRED:<n> requests` with no budget over 6, `BUDGET_INVALID`); `run(..., budget=None)`; CLI `--requests-per-window` and `--window-seconds`; `main` plans and splits before the lease. Keep every existing test passing (test_runner.py: 50 at the base; test_keeper.py: 11).
- The flag today: `runner._previous_hashes(previous)` maps call NAME to sha256 (runner.py:155-158) and `keeper.keep(..., previous_sha256=None, kept_at=None)` sets `changed_since_previous` to no_previous / true / false (keeper.py:121-139). Row S7 (REMEDIATION_v4): runs F and G sent one call name with zoom=5y then zoom=max, and G read `true` -- a changed REQUEST read as a changed answer. Contract 5.4 is the remedy.
- The lookup reads what the runner wrote: `keeper.KeptStore` (`kept_location`) and `runner.RunStore` (`run_location`). Its tests use the fake stores test_runner.py already builds; no AWS in a test.

## 4. SURFACES AND BOUNDS

You READ (never edit): `infra/aws/lambda/investor-reporting/` outside your `<paths>`, `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions, the maps you do not own). NEVER: a YCharts call (or any vendor call), an S3 or DynamoDB write, a deploy, a Terraform command, a portal change, a cookie, token or session value in any file, a figure value from a client file or a vendor answer in any committed file (C-FIRM), and none of another cell's files. Read-only AWS reads your order names use the main tree's shim `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws`, into your OS temp directory only, deleted when done. Tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W<slot>-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/runner.py
infra/aws/lambda/investor-reporting/ycharts/research/keeper.py
infra/aws/lambda/investor-reporting/ycharts/research/lookup.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_keeper.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_lookup.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the PLAN line prints before the lease and a 13-request plan refuses PLAN_OVER_BUDGET before the lease (tests -k plan_budget in test_runner.py, >= 2) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/r-5.AC1.py`)
- **AC2** -- a changed parameter under one call name reads request_changed, never true, and an unchanged request with a changed answer reads true (tests -k request_hash in test_runner.py, >= 2) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/r-5.AC2.py`)
- **AC3** -- the lookup prints one kept call's record from a fake store (tests -k lookup in test_lookup.py, >= 1) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/r-5.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-r-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/r-5.AC1.py</invocation><expect>r-5.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-r-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/r-5.AC2.py</invocation><expect>r-5.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-r-5"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/checks/r-5.AC3.py</invocation><expect>r-5.AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-r-5.runner-plan-budget-request-hash-lookup.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-r-5.runner-plan-budget-request-hash-lookup`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 5 cut from the CTO's round-4 analysis @a1b47e6b3f sections 2-3 (E1-E6) and REMEDIATION_v4 (W3-S6, S7) with W4-S4; decomposition round 5 v1.0 (`IRPT_YCDGEN_DECOMP_R5.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~1`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: r-5.AC1 FAIL as expected; r-5.AC2 FAIL as expected; r-5.AC3 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~11:5xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @beb0e52cfb (code) and, re-landed by a fresh slot-~1 worker after the issuer widened the sparse worktree to every mission home, @bcb83344c1 (proof and row W1-S2); merged 84a7af1854. r-5.AC1 PASS (2), r-5.AC2 PASS (3), r-5.AC3 PASS (2) on the merged tree; research suite 116 passed. Row W1-S2 ACCEPTED (lookup takes --region, default us-east-1, through runner.research_s3). STATUS NOTE (2.0.0_SA_COO~Y, 2026-10-07): the flip to 'complete' is NOT recorded here: the TO issuance gate refuses it because the instance's artifact-resolution check reports runner.py, keeper.py, lookup.py and their tests as PENDING-THIS-COMMIT yet older than the instance's commit bcb83344c1; the order stays 'issued' until the instance is re-landed or the CTO rules.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>5</round>
<slot>~1</slot>
<fabric>laptop</fabric>
