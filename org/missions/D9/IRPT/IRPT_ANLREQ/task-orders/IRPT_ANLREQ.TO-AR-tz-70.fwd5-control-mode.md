# TO-AR-tz-70 -- FWD-5 driver: a POSITIVE CONTROL mode (AR-tz-70, round 60, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-70</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~272</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-70` (`decompositions/IRPT_ANLREQ_DECOMP_R60_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the driver, its tests and the mint helper are merged)

---

## WORKER FACE

### THE CELL

`AR-tz-70`: "the cross-firm driver can run the SAME GET list as an identity ENTITLED to the ticket, and read every answer as ALLOWED or DENIED." The driver `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` (merged, AR-tz-67/68) signs in as a firm-B principal and expects every call on another firm's ticket to be REFUSED. The CTO's binding condition (msg 9804, 2026-10-16): the same run carries a POSITIVE CONTROL, the same GET list issued by an identity entitled to that ticket (no new grant), which must read ALLOWED, so that every firm-B REFUSED is shown to be the fence and not a broken route; all-refused without the control grades nothing.

**What to do (in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`).**
1. Add the flag `--control`. With `--control` and a valid `--go` the driver runs the SAME non-excluded routes, in the same order, with the same required arguments (`--base --email --ticket --firm-a --firm-b --request-id --job-id --out`; here `--email` is the entitled identity, `--firm-a` its own firm label, `--firm-b` the ticket's owner firm) and the same guard, sign-in, redirect handling and `EXCLUDED` rows. Without `--go` it prints the plan (the plan text gains one line describing the control mode) and exits 0 with no request sent. Without `--control` the behavior is byte for byte unchanged.
2. Control verdicts, a closed set: `ALLOWED` (a 2xx answer; for the route `ticket-list` additionally the JSON object carries a `tickets` list that CONTAINS the ticket id, case-insensitive, else DENIED), `DENIED` (401, 403 or 404, or a 2xx `ticket-list` that does not carry the ticket id), `UNREACHED` (3xx, 400, 405, 5xx, a dropped connection, a call the guard refused, a route with no GET shape, a missing id), `EXCLUDED` (the two excluded rows, never sent). No marker scan in control mode (an entitled identity may see the ticket id).
3. Control exit code: 0 when `ticket-read` AND `ticket-list` are both `ALLOWED`; 1 when either of them is `DENIED` (the control is broken, so the fence cannot be shown); 2 when either is `UNREACHED`, when no session was established, or when a required id is missing (checked before sign-in, zero requests). The other made routes (`form-as-filled`, `original-upload`, `opal-report`, `report-pdf`, `commentary-pdf`) are REPORTED with their verdict and do not change the exit (the ticket may carry no package, so an owner's 404 is a true answer).
4. The report is `fwd5_control_report.json` in `--out` (never the run report's name), schema `fwd5_control_report/1`, the same fields as the run report plus `"mode": "control"`, per call the route, method, status, verdict, body length and reason, the principal as a digest. It never holds a body, a cookie, a token, a password or an address. The password comes from stdin as one JSON object exactly as the run does.
5. Extend `selftest()` by at least four checks of the control classifier and exit code (keep every existing check). Put the new tests in the NEW file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py` (its own file; do not edit the two existing test files), reusing the style of the existing offline tests (a local fake HTTP server on 127.0.0.1; import the driver by inserting the driver's folder on `sys.path`). Name them `test_fwd5_control_<what>`. At least 8: all-allowed exits 0; `ticket-list` without the ticket id is DENIED and exits 1; `ticket-read` 403 exits 1; `ticket-read` dropped exits 2; package routes answering 404 are reported DENIED and the exit stays 0; the report is `fwd5_control_report.json` with `mode` control and holds no body, cookie, token, password or address; `--control` without `--go` sends nothing; a missing `--firm-b` or id exits 2 before any request.

Standard library and pytest only. No AWS, no network beyond the local fake, no secret, no run. Use plain names.

### ACCEPTANCE

<criterion id="AR70-tz-AC1" cell_refs="AR-tz-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 8 --prefix=test_fwd5_control_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR70-tz-AC2" cell_refs="AR-tz-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 21 --prefix=test_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR70-tz-AC3" cell_refs="AR-tz-70"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py --selftest</invocation><expect>FWD5-SELFTEST-OK</expect></criterion>
`AR70-tz-AC1` -- the new control tests pass, at least 8. Dry-run at box/dell2 6ef50aec55: FAIL as expected (the file does not exist). `AR70-tz-AC2` -- the two existing test files still pass, 21 functions in all (the unchanged-behavior control; 21 test functions): PASS at base as expected. `AR70-tz-AC3` -- the driver's own selftest still prints `FWD5-SELFTEST-OK` with the added checks: PASS at base as expected.

<expected_criteria>AR70-tz-AC1,AR70-tz-AC2,AR70-tz-AC3</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` and the new test file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py` only (plus this order's file, your deliverables folder, the surprise channel). The two existing test files and the mint helper are not touched.
- **No AWS, no network beyond the local fake, no run, no mint, no deploy.** Run mode behavior is unchanged.
- **Refusal clause.** If the file at your base already has a `--control` flag, say so in a surprise row and make no edit to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`; still add the tests.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_TX.md</decomp_doc> (round 60, workstream ~TX), cell `AR-tz-70`.
<owned_cells>AR-tz-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR70-tz-AC1, AR70-tz-AC2, AR70-tz-AC3. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/IRPT_ANLREQ.TO-AR-tz-70.fwd5-control-mode.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR70-tz-AC1,AR70-tz-AC2,AR70-tz-AC3` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the diff size of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` (lines added and removed), the counts passed for the three criteria, the printed `--plan` line for the control mode, the exit codes of the all-allowed, the missing-ticket-in-list and the dropped-ticket-read cases, the check lines, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new mode of a driver nobody has run, plus tests; no edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission changes in this cell.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: letting the control mode reuse the REFUSED/LEAK verdicts (a 2xx in control mode is the PASS, not a LEAK); scanning markers in control mode (the entitled identity may see the ticket id); requiring the package routes to be ALLOWED (the ticket has no package); a ticket-list 2xx that does not carry the ticket id read as ALLOWED; writing the control report under the run report's name; changing the behavior of the run mode.
</preflight>

- Cut on the CTO's binding condition (msg 9804): the FWD-5 live run carries a positive control; the control principal is an identity entitled to the ticket (the staff path, no new grant), minted by the same mint helper. Risk LOCAL: a driver mode and tests in deliverables folders, nothing run.
- Base: `AR70-tz-AC1` FAIL, `AR70-tz-AC2` PASS, `AR70-tz-AC3` PASS, as expected at box/dell2 6ef50aec55.
