# TO IRPT_DASHBD.TO-DB-b-22 -- the ONE Black Diamond pull's concurrent completion: one coordinator, one shared bearer, 2 then 6 workers, one retry per call (E3, batches 249 and 250)

<to_id>IRPT_DASHBD.TO-DB-b-22</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~8</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 249 (msg 105079: concurrent workers on ONE shared
bearer) and batch 250 (msg 105082: one retry per call; a twice-failed account is recorded, not fatal) | **Decomp cell:** `DB-b-22`
(decomposition section 14) | **outcome_ref:** P-5 (FWD-8's population tie-out) | **depends_on:** DB-b-21 (merged).

THIS CELL MAKES NO VENDOR CALL. The issuer runs the completion.

---

## WORKER FACE

**What exists.** Two scripts in this repo make up the ONE pull:
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/bd_population_pull_e3.py`, the pull (plan of 5,252 requests,
  `_address`, `TRANSIENT_HTTP`, `PLAN_NAME`);
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~7/bd_population_complete_e3.py`, its sequential completion
  (`load_b20`, `list_landed`, `derive_plan`, `print_denominators`, `_canon`, `_status_of`, `run_complement`, `main`).

The sequential completion works but is vendor-latency bound (about 12 s per call). It made 127 calls and landed 125, then
aborted on a second transport error (`URLError`) because its retry budget was one per RUN. 144 responses have landed under
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<bd_internal_id>.json`.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-8`. Run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~8/`.

**What you build**, in your folder:
1. **`bd_population_concurrent_e3.py`.** It imports the two scripts' functions by path (as `~7` imports `~6`); do not copy them.
   Three modes:
   - **`plan`** stays OFFLINE under DRY_RUN=1, with S3 list reads only. It writes `BD_POPULATION_CONCURRENT_PLAN_E3.json`: every
     field of `~7`'s completion plan (`requests_planned`, `landed`, `landed_accounts`, `complement`, `complement_accounts`,
     `vendor_calls: 0`, `dry_run`) plus a `ruling` object holding exactly these values:
     - `ruling_ids` `["1.0.0_SA_CTO RULINGS batch 249", "1.0.0_SA_CTO RULINGS batch 250"]`;
     - `workers_start` 2, `workers_max` 6, `ramp_after_s` 600, `aggregate_rps` 2;
     - `retries_per_call` 1, `consecutive_failures_abort` 3, `failed_cap` 105 (2% of 5,252);
     - `mint_interval_s` 120 and `fresh_mint_s` 30.

     It prints both denominators (planned = landed + complement).
   - **`run --go`** (LIVE; the issuer runs it, never you). It refuses unless `--go` is given, the plan exists and is re-derived
     identically (`_canon`), and the `ruling` object is present. Then:
     - **One coordinator owns the shared bearer.** It mints through the same 49F sign-in path (`h.get_clientview_token(
       h.load_bd_session())`), one mint at a time under a lock, never one per worker. It re-mints when the bearer is
       `mint_interval_s` old, or early when a call gets 401 on a bearer older than `fresh_mint_s`. That call then takes its one retry.
     - **Workers** are threads that take accounts from ONE queue holding the complement only, so each account is requested once.
       The aggregate pace is at most `aggregate_rps` across all workers (one shared rate limiter).
     - **Ramp:** start `workers_start`. After `ramp_after_s` with no 401 and no 429, raise to `workers_max`.
     - **429** halves the active workers (minimum 1), and its retry waits for its backoff (`Retry-After`, else 30 s).
     - **Retry:** one retry per CALL for a transport error, a 5xx or a 429. A call that fails twice is recorded `FAILED` with its
       response class (`transport`, `5xx`, `429`), and the run continues.
     - **Abort the whole run** on any of these: 3 consecutive failed calls across workers; a 401 on a bearer younger than
       `fresh_mint_s`; any other 4xx; a landing failure; or `FAILED` above `failed_cap`.
     - Each 200 lands at `~6`'s `_address(on, "20261004", bd)`.
     - It writes `BD_POPULATION_CONCURRENT_E3.json`, with per-call records (account, worker, bearer generation, status, class,
       retried, landed). It checkpoints the file every 50 calls and in a `finally`, so an abort always leaves a record. An earlier
       record is renamed with a timestamp, never overwritten.
     - It prints both denominators at start and end. It never logs a credential, a bearer or a response body.
   - **`sweep --go`** (LIVE; the issuer's). It reads the last run record's `FAILED` set and refuses unless the set is at most
     `failed_cap` and every class is transport, 5xx or 429. It prints the set, requests each account once under the same
     coordinator rules, and prints the residue.
2. **`tests/test_bd_population_concurrent_e3.py`**: at least 8 pytest tests, all offline (stub boto3, the helpers and time):
   - the shared bearer is minted by the coordinator alone (mint count with 6 workers is far below the call count);
   - the ramp goes from 2 to 6 only after `ramp_after_s` with no 401 or 429;
   - a 429 halves the workers and is retried once after its backoff;
   - a call failing twice is recorded FAILED and the run continues;
   - 3 consecutive failures abort;
   - FAILED above `failed_cap` aborts;
   - a 401 within `fresh_mint_s` of a mint stops the run, and a 401 on an older bearer re-mints and retries;
   - a landed account is never requested, and no account is requested twice across workers;
   - `run` and `sweep` refuse without `--go`, and both denominators are printed.

   The words `shared bearer`, `ramp`, `429`, `FAILED`, `sweep`, `consecutive`, `--go` and `denominators` appear in the file.
3. **Run `plan` once**, then commit the script, the tests and the plan.

<criterion id="DB14-1-AC1" cell_refs="DB-b-22"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r14/p14_concurrent_completion.py" . DB14-1-AC1</invocation><expect>DB14-1-AC1 PASS</expect></criterion>
`DB14-1-AC1` -- the concurrent-completion tests pass, at least 8, naming the eight words. Base: FAIL.

<criterion id="DB14-1-AC2" cell_refs="DB-b-22"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r14/p14_concurrent_completion.py" . DB14-1-AC2</invocation><expect>DB14-1-AC2 PASS</expect></criterion>
`DB14-1-AC2` -- the offline plan is the run's whole input: it reconciles (planned 5252 = landed + complement, landed at least 144,
no overlap), and its `ruling` carries the batch 249/250 values. Base: FAIL.

<criterion id="DB14-1-AC3" cell_refs="DB-b-22"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r14/p14_concurrent_completion.py" . DB14-1-AC3</invocation><expect>DB14-1-AC3 PASS</expect></criterion>
`DB14-1-AC3` -- a GUARD: your commits touch only IRPT_DASHBD paths. Base: PASS.

<expected_criteria>DB14-1-AC1,DB14-1-AC2,DB14-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads and lists only. NO Black Diamond call, no token mint, no `run`, no `sweep`.
- **Refusal clause.** Any vendor call, a `run` or `sweep`, or a credential written anywhere is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~8/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-22.bd-population-concurrent-completion.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 14 (round 14, workstream B), cell `DB-b-22`.
<owned_cells>DB-b-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB14-1-AC1, DB14-1-AC2, DB14-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~8/IRPT_DASHBD.TO-DB-b-22.bd-population-concurrent-completion.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB14-1-AC1,DB14-1-AC2,DB14-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the plan's denominators, each criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a script, tests and an offline plan under a deliverables folder; 0 served bytes move; no vendor call in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB14-1-AC1 base FAIL (no tests), DB14-1-AC2 base FAIL (no plan), DB14-1-AC3 base PASS (guard), dry-run at base 0b6a5aff58 2026-10-05 ~01:5xZ.
lane: the <paths> block IS the grant.
</preflight>
