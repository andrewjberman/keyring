# IRPT_YCDGEN task order -- `YCD-r-4` -- ROUND 4 (ENRICHMENT): THE RUNNER'S CALL BUDGET, AND THE KEEPER'S POINT-OBJECT RULE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md</decomp_doc>
<owned_cells>YCD-r-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, trigger or EventBridge rule is added or read; the project runs on demand only (PRD C-SCOPE)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE nothing is returned at the cut; the issuer's evidence context is this order's check files
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- YCharts direct-API generation, Opal-branded: every YCharts answer of a research run kept in the client firm's store with no secret in it, each report element traced to the answer it comes from, and Opal's own script making the report in Opal's branding. **Round 4** gives the runner a per-window call budget (the firewall challenges the 7th request of any run), finds which held-data figures Opal already holds, adds six risk statistics, and fixes the two maps' missing rows. No worker calls YCharts, writes the store, deploys or grants: the issuer makes every live call at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-3 decomposition)

### `YCD-r-4` -- the runner's call budget, and the keeper's point-object rule (E1 build, E3; FWD-1, FWD-2, FWD-6)
- `ycharts/research/runner.py`: contract 4.1.
- `ycharts/research/keeper.py`: the series rule (3.3) also reads DATA when `series[].data` is a list of point OBJECTS (dicts
  whose values include numbers), the live shape. Pin it with a fixture built from the round-2 kept scatter answer's TYPE
  SKELETON (keys and value types, no value).
- Tests: a 12-request plan runs as 2 windows of 6 with a release and a fresh lease between; a 7th request is never sent in a
  window; no budget with more than 6 requests refuses before the lease; a stop in window 2 ends the run; the point-object
  scatter skeleton labels DATA.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined verbatim from the decompositions)

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

### 3.3 The keeper's series rule (C-KEEP; built by YCD-r-3)

`shape` is `DATA` when a JSON answer holds a `series` key whose value is a list of objects, any of which carries a list
of numbers or of `[number, number]` pairs (YCharts' scatter answer, `data.series`). It is added to the existing DATA keys,
and no other label changes.

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

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- `runner.py` at the base: `plan_calls(map_doc, security_id, window=None, holdings=None)` (expand calls, 3.1); `run(*, session, store, runs, firm, request_id, portfolio_security_id, map_doc, clock, previous=None, window=None, min_gap_s=0, stops=None, holdings=None)`; the lease is `session.acquire(request_budget=REQUEST_BUDGET, ttl=TTL)` and `transport.close()` releases it; `_Clocks` counts `transport.wait` time into `opal_waiting_ms`. Keep every existing test passing (test_runner.py: 34 at the base).
- Measured (row S6): the firewall challenges the 7th request of a run, at ~1.5 s, 8 s and 2 s spacing, on three different calls. The window length is unmeasured; the issuer measures it at close and passes it as --window-seconds.
- `keeper.py`: the shape rule (3.3) reads DATA for `series` lists of numbers or [number, number] pairs. The live round-2 scatter answer is `{"data": {"series": [{..., "data": [ {"x": <number>, "y": <number>, "name": <string>, ...}, ...]}], ...}, "params": {...}}` (point OBJECTS); it still labels IDENTIFIERS (row S4). Write the fixture as that type skeleton with made-up numbers, no client value.

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

- **AC1** -- the budget: windows of at most N with a release and fresh lease between, never an (N+1)th request in a window, a plan over 6 with no budget refuses before the lease, a stop in a later window ends the run (tests -k 'budget or window', >= 3) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/r-4.AC1.py`)
- **AC2** -- the point-object scatter skeleton labels DATA (tests -k point in test_keeper.py, >= 1) (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/r-4.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-r-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/r-4.AC1.py</invocation><expect>r-4.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-r-4"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/checks/r-4.AC2.py</invocation><expect>r-4.AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-r-4.runner-call-budget-and-point-objects.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-r-4.runner-call-budget-and-point-objects`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 4 cut from the CTO's round-3 analysis @033795b666 sections 2-3 (E1-E6); decomposition round 4 v1.0 (`IRPT_YCDGEN_DECOMP_R4.md`); PRD v0.1 @8b364d6d94; Andrew's egress word @ce20ca6854 (the issuer's live calls only). Chain `~1`. Risk WORLD: the gate's floor for infra paths. Checks dry-run at the base: r-4.AC1 FAIL as expected; r-4.AC2 FAIL as expected.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~05:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @7f0d395090, merged 0a439396d1; r-4.AC1 PASS (16), r-4.AC2 PASS (2) on the merged tree; research suite 104 passed after all four merges. Issuer ruling on the two choices the worker named: `record["lease"]` holds the first window's fence, and the window wait is counted in the next window's first call's `waited_ms` -- both ACCEPTED (the record schema and the clock sum hold). Live: the merged runner ran windows 1-2 of the round-4 close (no budget path; 6, 6, 6, 1 and 1 requests a run, no challenge).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>4</round>
<slot>~1</slot>
<fabric>laptop</fabric>
