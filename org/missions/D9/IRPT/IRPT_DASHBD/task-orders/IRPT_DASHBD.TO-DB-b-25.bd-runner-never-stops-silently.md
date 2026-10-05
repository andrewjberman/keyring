# TO IRPT_DASHBD.TO-DB-b-25 -- the concurrent BD runner never stops silently: retry a failed bearer mint once, abort on a worker crash, and report complete only when the queue is empty

<to_id>IRPT_DASHBD.TO-DB-b-25</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~11</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer, inside its own decomposition, on relaunch 2's silent stop (ledger
irpt-dashbd-e3-bd-population-pull-20261004, log ~10:4xZ) under CTO batches 249, 250 and 258 | **Decomp cell:** `DB-b-25` (decomposition
section 16) | **outcome_ref:** P-5 (FWD-8) | **depends_on:** DB-b-22 (merged).

THIS CELL MAKES NO VENDOR CALL. The issuer runs the pull.

---

## WORKER FACE

**What happened.** Relaunch 2 of `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~8/bd_population_concurrent_e3.py`
ended about 10:27Z. Its record read `complete: true, aborted: null`, yet 2,384 accounts were never requested and 6 in-flight calls were
lost. Its stderr shows `http.client.RemoteDisconnected` (a `ConnectionResetError`) escaping a worker thread. The bearer mint
(`Bearer._mint`, about :97, called from `current()` and `remint_after_401()`) is OUTSIDE `_attempts`' transport except, so a vendor
disconnect during a mint kills that worker thread silently. Once all 6 died, `go()` joined them and wrote a "complete" record.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-11`; run everything from its root. Edit only the runner and its tests
in the `~8` folder.

1. **Mint retry.** A transport error (`urllib.error.URLError`, `OSError` (which covers ConnectionResetError and
   RemoteDisconnected) or `TimeoutError`) raised by the mint is retried ONCE after a short backoff, under the same coordinator
   lock, so there is never a second concurrent mint. If the retry also fails, the run ABORTS with the reason
   `mint failed twice: <ExceptionType>`. Never print a token or a session value.
2. **Worker crash.** An unexpected exception in a worker thread must not vanish. Catch it at the top of `_worker`; record the
   in-flight account as `STOPPED`, class `worker-crash: <ExceptionType>`; and abort the run with that reason. Remaining workers
   stop at their next loop check, as they already do on abort.
3. **Complete means done.** The snapshot's `complete` is true only when `go()` returned with the queue empty, nothing in flight and
   no abort. Otherwise it is false and `aborted` names why. The end-of-run denominators line must not show an unexplained `other`.
4. **Tests,** added to `.../~8/tests/test_bd_population_concurrent_e3.py` with test names containing `mint`, `crash` and
   `complete`:
   - a stub mint raising `ConnectionResetError` once is retried and the run lands everything;
   - one raising twice aborts with the mint reason;
   - a stub `_request` raising an unexpected exception that `_attempts` does not handle makes the run abort, with the account
     recorded `STOPPED`;
   - a run left with a non-empty queue reports `complete: false`.

   The existing tests keep passing.

<criterion id="DB16-1-AC1" cell_refs="DB-b-25"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r16/p16_runner_resilience.py" . DB16-1-AC1</invocation><expect>DB16-1-AC1 PASS</expect></criterion>
`DB16-1-AC1` -- the runner tests pass, with new tests naming mint, crash and complete. Base: FAIL.

<criterion id="DB16-1-AC2" cell_refs="DB-b-25"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r16/p16_runner_resilience.py" . DB16-1-AC2</invocation><expect>DB16-1-AC2 PASS</expect></criterion>
`DB16-1-AC2` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>DB16-1-AC1,DB16-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. NO vendor call, no token mint, no `run` or `sweep`. Tests are offline with stubs.
- **Refusal clause.** A change to the ruled pace, the ramp, the retry budget per call or the abort set of batches 249/250 is out
  of scope: file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~8/bd_population_concurrent_e3.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~8/tests/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~11/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-25.bd-runner-never-stops-silently.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 16 (round 16, workstream B), cell `DB-b-25`.
<owned_cells>DB-b-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB16-1-AC1, DB16-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~11/IRPT_DASHBD.TO-DB-b-25.bd-runner-never-stops-silently.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB16-1-AC1,DB16-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the new test names, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a deliverables runner and its tests; 0 served bytes move; no vendor call in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB16-1-AC1 base FAIL (no mint/crash/complete tests), DB16-1-AC2 base PASS (guard), dry-run at base e8564f6a18 2026-10-05 ~10:5xZ.
lane: the <paths> block IS the grant.
</preflight>
