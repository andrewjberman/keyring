# TO-AR-tz-76 -- FWD-5 driver: REAL report and export ids, and GET tickets/metrics (AR-tz-76, round 66, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-76</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~279</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>66</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-76` (`decompositions/IRPT_ANLREQ_DECOMP_R66_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the driver and its route set are merged)

---

## WORKER FACE

### THE CELL

`AR-tz-76`: "the cross-firm driver drives `narrative` and `export-receipt` with REAL ids, no stand-ins, and drives `GET tickets/metrics`." The CVO's grade of FWD-5 (`ADJUDICATION_v27`) stays FAIL (unproven) until a fourth sitting shows working controls with REAL ids on `request-history`, `narrative` and the no-selection call, and drives `GET /api/scoped/tickets/metrics`; the CTO (msg 10104) put those three gaps into sitting 4's scope. The merged driver puts the REQUEST id where the narrative's report id and the export receipt's export id belong (a stand-in), so the control read FIRM_BINDING on `narrative` and NOT_FOUND on `export-receipt` in sitting 3, which grades nothing.

**What to do (in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`).**
1. Add the flags `--report-id` and `--export-id` (both optional at parse time). The route `narrative` uses `/api/scoped/investor-reporting/narrative/{report_id}?selected_tenant={firm_b}` and needs `report_id`; the route `export-receipt` uses `/api/scoped/investor-reporting/export/{export_id}?selected_tenant={firm_b}` and needs `export_id`. A run without the value for one of them makes that route `UNREACHED` with the existing reason "no value supplied for report_id" (or export_id): the run then exits 2, which is the point (a sitting must supply real ids). Remove the stand-in wording from the two routes' plan text and say instead that the value comes from the flag. The ids are NOT markers (do not add them to the LEAK marker scan).
2. Add ONE route `tickets-metrics`, GET `/api/scoped/tickets/metrics`, a ticket-service route that needs nothing. It sits right after `ticket-list` in `ROUTES`. Extend the guard's GET allow-list with exactly `/api/scoped/tickets/metrics` (nothing else under `/api/scoped/tickets/`). It is graded like the other ticket-service routes: in run mode a 2xx is a `LEAK` (a firm-B principal received the ticket metrics) and 401/403/404 is `REFUSED`; in control mode a 2xx is `ALLOWED`, 401/403/404 `DENIED`. The run now makes 14 calls and has 16 rows (14 made, the 2 EXCLUDED unchanged).
3. Everything else is unchanged: exit codes, the envelope grading, the report's keys, the control exit rule. Extend `selftest()` by at least three checks (keep every existing one).
4. Tests: the NEW file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~279/fwd5_driver/test_fwd5_driver_real_ids.py`, tests named `test_fwd5_real_<what>` (a local fake HTTP server on 127.0.0.1, in the style of the existing offline tests; import the driver by inserting its folder on `sys.path`). At least 10: the run makes 14 calls and writes 16 rows; `narrative` sends the `--report-id` value and `export-receipt` the `--export-id` value in the path (the fake records paths); a run without `--report-id` leaves `narrative` UNREACHED and exits 2; a run without `--export-id` leaves `export-receipt` UNREACHED and exits 2; `tickets-metrics` sends `/api/scoped/tickets/metrics` and carries no `selected_tenant`; a 403 on it is REFUSED, a 200 on it is LEAK and exits 1 in run mode; in control mode a 200 is ALLOWED and a 403 DENIED; the guard refuses `/api/scoped/tickets/metrics/anything` and `/api/scoped/tickets/claim`; the report holds no body. The five existing driver test files (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py` to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py` in the acceptance below) MAY be edited ONLY where a test asserts the old call count (13 made, 15 rows) or runs the full route set without the two new flags and expects exit 0 (pass `--report-id` and `--export-id` there); keep each test's intent and list every edited test by name in a surprise row. Keep every other existing test as it is.

Standard library and pytest only. No AWS, no network beyond the local fake, no secret, no run. Use plain names.

### ACCEPTANCE

<criterion id="AR76-tz-AC1" cell_refs="AR-tz-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 10 --prefix=test_fwd5_real_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~279/fwd5_driver/test_fwd5_driver_real_ids.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR76-tz-AC2" cell_refs="AR-tz-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 70 --prefix=test_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR76-tz-AC3" cell_refs="AR-tz-76"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py --selftest</invocation><expect>FWD5-SELFTEST-OK</expect></criterion>
`AR76-tz-AC1` -- the new real-id tests pass, at least 10. Dry-run at box/dell2 BASE: FAIL as expected (the file does not exist). `AR76-tz-AC2` -- the five existing driver test files still pass, 70 functions in all (the unchanged-behavior control; 13 + 8 + 14 + 17 + 18): PASS at base as expected. `AR76-tz-AC3` -- the driver's own selftest still prints `FWD5-SELFTEST-OK` with the added checks: PASS at base as expected.

<expected_criteria>AR76-tz-AC1,AR76-tz-AC2,AR76-tz-AC3</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`, the new test file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~279/fwd5_driver/test_fwd5_driver_real_ids.py`, and the five existing driver test files ONLY for the edits described in item 4 (plus this order's file, your deliverables folder, the surprise channel). The mint helper and `served.py` are not touched.
- **No AWS, no network beyond the local fake, no run, no mint, no deploy.** No write route is added: the write routes are outside FWD-5's DONE WHEN (CTO msg 10104).
- **Refusal clause.** If the file at your base already has a route named `tickets-metrics`, say so in a surprise row and make no edit to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`; still add the tests.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~279/fwd5_driver/test_fwd5_driver_real_ids.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R66_TX.md</decomp_doc> (round 66, workstream ~TX), cell `AR-tz-76`.
<owned_cells>AR-tz-76</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR76-tz-AC1, AR76-tz-AC2, AR76-tz-AC3. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~279/IRPT_ANLREQ.TO-AR-tz-76.fwd5-real-ids.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR76-tz-AC1,AR76-tz-AC2,AR76-tz-AC3` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the diff size of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` (lines added and removed), the counts passed for the three criteria, the names of every edited existing test, the exit codes of a run without `--report-id`, a run with a 200 on `tickets-metrics` and an all-refused 14-call run, the check lines, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two input flags and one read route in a driver, plus tests; no edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission changes in this cell.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: keeping the request id as a silent default for the report or export id (a stand-in is the defect); adding the real ids to the LEAK marker scan; allowing any other path under /api/scoped/tickets/ in the guard; grading a 200 on tickets-metrics REFUSED in run mode; changing exit rules or the envelope grading; editing an existing test beyond the call count and the missing-flags runs.
</preflight>

- Cut on the CVO's ADJUDICATION_v27 and the CTO's msg 10104: sitting 4 needs working controls with REAL ids (no stand-ins) on narrative and export-receipt, and GET tickets/metrics driven. Risk LOCAL: a driver input and a route with tests in deliverables folders, nothing run.
- Base: `AR76-tz-AC1` FAIL, `AR76-tz-AC2` PASS, `AR76-tz-AC3` PASS, as expected at box/dell2 BASE.
