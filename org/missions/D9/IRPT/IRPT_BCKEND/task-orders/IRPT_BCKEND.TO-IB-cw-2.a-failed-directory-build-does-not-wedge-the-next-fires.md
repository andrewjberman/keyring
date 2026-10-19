# TO IRPT_BCKEND.TO-IB-cw-2 -- BUILD (no deploy): a failed directory build must not block every later fire: the failure manifest records the failed command's id and status; the NEXT fire treats a reported failed command as terminal and re-dispatches ONCE for its own fire date; an in-flight command still blocks; the Success path stays byte-equal (CTO ruling on row D2-S239, msg 10699, part (b))

<to_id>IRPT_BCKEND.TO-IB-cw-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~457</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-cw-2` (decomposition section 251) | **outcome_ref:** FWD-7 (the directory is READY at all 3 firms) | **Ordered by:** the CTO's ruling `deliverables/1.0.0_SA_CTO~DELL2/RULING_D2_S239_COTTONWOOD_DIRECTORY_WEDGE_20261019.md` part (b) and the row `IRPT_BCKEND-D2-S239`. **This order edits source and tests in your worktree. It deploys nothing: the Lambda release is a later order under its own never-widen pair, applied outside the 11:30Z to 14:15Z band.**

---

## WORKER FACE

**Cell `IB-cw-2` (inlined).** The defect, measured: `infra/aws/lambda/investor-reporting/directory/refresh.py`, `SsmBuildDispatcher.__call__` lines about 843 to 853 read the last dispatched command's status and, when it is neither in flight nor `Success`, `raise DispatchError("BUILD_ENDED_UNSUCCESSFUL", status)` and never re-dispatch. The failure manifest `refresh_firm` writes (lines about 1007 to 1029, `failure = {"build_error", "build_dispatch_failure", "build_dispatch_half", "build_command_status"}`) carries NO command id, and `_last_dispatched` (lines about 294 to 319) finds only `REFRESH_DISPATCHED` records. So every later fire walks back to the same old `REFRESH_DISPATCHED` record, reads the same failed command, and raises again: Cottonwood has been stuck on its 2026-10-14 command for three fires. **The contract (the CTO's, not yours to change):**
1. **The failure record carries the failed command's id and status.** When `__call__` raises for a previous command that ended unsuccessfully, the manifest that fire writes (a `REFRESH_FAILED` record) records that command's id and its status (for example `failed_command_id` and the existing `build_command_status`). It still carries NO error text (the existing rule: the exception TYPE is recorded, never its text).
2. **The NEXT fire treats that command as terminal.** A previous command whose failure an earlier fire has ALREADY REPORTED (a `REFRESH_FAILED` manifest, dated after the `REFRESH_DISPATCHED` record that named it, records that same command id) is terminal: the fire does NOT raise on it, it re-dispatches the build ONCE for its own fire date. The first fire that merely OBSERVES a failure still reports it (records the id and status) and does not dispatch in the same breath.
3. **Never a loop within a fire.** One fire sends at most one build per firm. A re-dispatched build that fails again is reported by the NEXT fire, which records its id; the fire after that re-dispatches.
4. **An in-flight command still blocks, exactly as today** (`Pending`, `InProgress`, `Delayed`: the fire returns without dispatching).
5. **The Success path is byte-equal to today.** For a previous command that ended `Success` (and for the in-flight path) the dispatcher's result and the SSM calls are identical to the base `refresh.py`.
Keep the change minimal and local to `refresh.py`: reuse the existing helpers; add the smallest code that meets 1 to 5; do not restructure the walk, do not change `last_manifest`, do not touch any other file than the new test file. No non-ASCII anywhere (CLAUDE.md).

**Six new tests** in a NEW file `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_failed_command_redispatch.py` (names fixed; invented ids and dates only; no AWS call; reuse the `FakeS3` and `FakeSSM` style of `tests/test_refresh_manifest_dispatch_date.py`):
- `test_a_failed_previous_command_is_reported_with_its_id_and_status`
- `test_the_failure_record_carries_no_error_text`
- `test_an_unreported_failed_command_is_reported_and_not_redispatched` (zero `send_command` calls)
- `test_a_reported_failed_command_is_terminal_and_the_fire_redispatches_exactly_once` (exactly one `send_command`; the manifest that fire writes is `REFRESH_DISPATCHED` for its own fire date with the NEW command id)
- `test_an_in_flight_command_returns_without_dispatch` (zero `send_command` calls)
- `test_a_fire_never_dispatches_twice`
Drive the real `lambda_handler` / `refresh_firm` / `SsmBuildDispatcher` with fake S3 and SSM clients (the handler's `client=` argument injects S3), over two or three consecutive fire dates, so the test sees the manifests the first fire wrote and the second fire reads.

**Do, in this order:**
1. Read `refresh.py` lines 205 to 330 (the walk and `_last_dispatched`), 563 to 612 (the constants), 729 to 960 (`SsmBuildDispatcher`), 1007 to 1030 (the failure manifest) and 1211 to 1340 (`lambda_handler`), and the fake-client style of `tests/test_refresh_manifest_dispatch_date.py`. Run `python -m pytest infra/aws/lambda/investor-reporting/directory/tests -q --color=no -p no:cacheprovider --continue-on-collection-errors` once and record passed, failed and error counts (the folder is red at base for reasons that are not yours; the failing and error sets must be identical after).
2. Implement and test. Run the three criteria below from the repository root under `timeout 300` (AC3 reads `HEAD~1..HEAD`: run it AFTER your one commit). Record AC1 and AC2 output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~457/IBcw2_criteria_output.txt` BEFORE the commit; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBcw2_notes.md` (the change in a paragraph, how fires 1 and 2 behave, the before and after test counts).
3. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~457 <0.9.0_WK_IRPT_BCKEND~457@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): `refresh.py`, the new test file, your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words, with AC3's result.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBCW2-AC1" cell_refs="IB-cw-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r256/p256_cells.py" . IBCW2-AC1</invocation><expect>IBCW2-AC1 PASS</expect></criterion>
<criterion id="IBCW2-AC2" cell_refs="IB-cw-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r256/p256_cells.py" . IBCW2-AC2</invocation><expect>IBCW2-AC2 PASS</expect></criterion>
<criterion id="IBCW2-AC3" cell_refs="IB-cw-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r256/p256_cells.py" . IBCW2-AC3</invocation><expect>IBCW2-AC3 PASS</expect></criterion>

<expected_criteria>IBCW2-AC1, IBCW2-AC2, IBCW2-AC3</expected_criteria>

What the checks grade: AC1 the six named tests exist and all pass; AC2 a differential, run by the check itself over a fixture, that a `Success` previous command and an in-flight previous command give byte-identical results and the same SSM calls from the BASE `refresh.py` (HEAD~1) and your new one, and that `refresh.py` actually changed; AC3 that your ONE commit touches only `refresh.py`, the new test file and this order's paths. The no-regression read of the whole folder is the issuer's. Do not edit the checks.

## BOUNDS

- **Grant:** edit `infra/aws/lambda/investor-reporting/directory/refresh.py`; add `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_failed_command_redispatch.py`; write `deliverables/0.9.0_WK_IRPT_BCKEND~457/`; the surprise channel for rows. **NO AWS call; NO change to any other source file, Terraform or registry; NO real command id, bucket or client identifier (invent fakes); NO deploy; NO push.**
- **Refusal clause:** STOP and report, writing nothing further, if the contract cannot be met without changing a file outside the two, or if the Success path cannot stay byte-equal. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
infra/aws/lambda/investor-reporting/directory/refresh.py
infra/aws/lambda/investor-reporting/directory/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~457/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-cw-2.a-failed-directory-build-does-not-wedge-the-next-fires.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 251 (round 14, workstream ~PM), cell `IB-cw-2`.
<owned_cells>IB-cw-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBCW2-AC1, IBCW2-AC2, IBCW2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~457/IRPT_BCKEND.TO-IB-cw-2.a-failed-directory-build-does-not-wedge-the-next-fires.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a Lambda source and test edit in a worktree; nothing is deployed and no AWS call is made. The release is a separate order under a never-widen pair (CTO ruling part (b)): one Lambda function (`irpt-directory-refresh`), a new zip version through Terraform, outside the 11:30Z to 14:15Z band.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p256_cells.py IBCW2 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no tests; the refresh.py is unchanged so the differential refuses). Positive control (control256.py) over synthetic git repos each with the REAL base refresh.py and expiry.py and ONE worker commit: the three positives PASS (a harmless addition leaves the Success and in-flight paths identical); each negative (a test name missing, a named test failing, no test file, the Success path's trail text changed, the in-flight status no longer blocking, refresh.py unchanged, refresh.py or the tests not in the commit, another file touched) plus the empty repo fails its own arm, 0 unexpected. NOT measured by me: the implementation, that fires 1 and 2 behave as the contract says on a real manifest history (the six tests drive it with fakes; the release order reads it live), anything deployed.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~457`. Class WORLD (the gate's floor for an infra/aws/lambda path; the act is a source and test edit in a worktree and deploys nothing).
</preflight>
