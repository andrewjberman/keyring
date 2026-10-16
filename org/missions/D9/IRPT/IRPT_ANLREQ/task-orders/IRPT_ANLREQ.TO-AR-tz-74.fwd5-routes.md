# TO-AR-tz-74 -- FWD-5 driver: the five more read routes, the no-selection call, and a served body is ALLOWED in the control (AR-tz-74, round 64, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-74</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~277</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-74` (`decompositions/IRPT_ANLREQ_DECOMP_R64_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the driver, its control mode and its envelope grading are merged)

---

## WORKER FACE

### THE CELL

`AR-tz-74`: "the cross-firm driver DRIVES every read route that reads the same request, job, report or package, plus one call with no selected_tenant, and reads a served body as ALLOWED in the control." The CVO's grade of FWD-5 (`ADJUDICATION_v26`, 2026-10-16) is FAIL (unproven, no leak found) because five report-side read routes on the same request or job and the no-`selected_tenant` shape were never driven; the CTO (msg 10010) ordered a third live sitting that DRIVES them, and the CTO's earlier enrichment (msg 9955) says a 2xx JSON with no `ok` key in the control is a served body, ALLOWED.

**What to do (in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`).**
1. Add SIX routes to `ROUTES`, in this order, after `commentary-pdf` and before the two EXCLUDED rows are unchanged (keep the EXCLUDED rows where they are; the made-call order is what matters). All are GET, and each name is exactly as written: `request-read` = `/api/scoped/investor-reporting/analysis/requests/{request_id}?selected_tenant={firm_b}`; `request-history` = `/api/scoped/investor-reporting/analysis/requests?selected_tenant={firm_b}` (needs nothing); `job-status` = `/api/scoped/investor-reporting/status/{job_id}?selected_tenant={firm_b}`; `narrative` = `/api/scoped/investor-reporting/narrative/{request_id}?selected_tenant={firm_b}` (the request id stands in for the report id: the firm fence refuses before any id is read; say so in the route's plan text); `export-receipt` = `/api/scoped/investor-reporting/export/{request_id}?selected_tenant={firm_b}` (same stand-in); `request-read-no-selection` = `/api/scoped/investor-reporting/analysis/requests/{request_id}` with NO `selected_tenant` at all. Extend the guard's GET allow-list with exactly those path shapes (`/analysis/requests`, `/analysis/requests/<seg>`, `/status/<seg>`, `/narrative/<seg>`, `/export/<seg>`, all under `/api/scoped/investor-reporting`; NOT `/export/<seg>/download`, NOT the bare `/status`). The run now makes 13 calls and has 15 rows (13 made, the 2 EXCLUDED unchanged).
2. Envelope grading (already in the driver for routes under `/api/scoped/investor-reporting/`) applies to the six new routes, with these changes to BOTH modes:
   - RUN mode, a 2xx JSON object WITHOUT an `ok` key on a report-side route is a SERVED BODY: `LEAK` (a firm-B principal received content). A 2xx that is not a JSON object stays `UNREACHED`. `ok` true stays `LEAK`; `ok` false with `FIRM_BINDING` or `NOT_AUTHORIZED` stays `REFUSED`; any other `ok` false stays `UNREACHED` EXCEPT on the route `request-read-no-selection`.
   - RUN mode, route `request-read-no-selection` only (without `selected_tenant` the caller's own firm anchors the bucket, so the right answer is absence, not the fence): `ok` false with ANY code other than `CONTRACT_VERSION` and `?` -> `REFUSED` with the reason "no selection: refused by <code> in the caller's own tenant"; `ok` false with `CONTRACT_VERSION` or `?` -> `UNREACHED`; `ok` true or a served body -> `LEAK`.
   - CONTROL mode: a 2xx JSON object WITHOUT an `ok` key is a served body -> `ALLOWED`; `ok` true -> `ALLOWED`; `ok` false with `CONTRACT_VERSION` or `?` -> `UNREACHED`; any other `ok` false -> `DENIED` (the code is kept in the row). The control exit rule is unchanged (0 only when `ticket-read` and `ticket-list` are both ALLOWED).
3. Every report row keeps the same keys (`code` as before). Exit codes of run mode are unchanged. Extend `selftest()` by at least four checks (keep every existing one).
4. Tests: the NEW file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py`, tests named `test_fwd5_routes_<what>` (a local fake HTTP server on 127.0.0.1, in the style of the existing offline tests; import the driver by inserting its folder on `sys.path`). At least 12: the run makes 13 calls and writes 15 rows; each of the six new routes sends the right path (the fake records paths) and `request-read-no-selection` carries no `selected_tenant`; the guard refuses `/export/<seg>/download` and the bare `/status`; run mode FIRM_BINDING on all six new routes exits 0 (the no-selection route REFUSED by `NOT_FOUND` too); a served body (2xx JSON, no `ok`) on a new report-side route in run mode is LEAK and exits 1; the no-selection route answering `CONTRACT_VERSION` is UNREACHED and exits 2; the no-selection route answering `ok` true is LEAK; control mode: a served body is ALLOWED, `ok` true is ALLOWED, `NOT_FOUND` is DENIED (and the exit stays 0 when `ticket-read` and `ticket-list` are ALLOWED), `CONTRACT_VERSION` is UNREACHED; the report holds no body. The four existing driver test files MAY be edited ONLY where a test asserts the old route count (7 made, 9 rows) or the old grading of a 2xx JSON without `ok` on a report-side route; keep each test's intent, update the number or the fake answer, and list every edited test by name in a surprise row. Keep every other existing test as it is.

Standard library and pytest only. No AWS, no network beyond the local fake, no secret, no run. Use plain names.

### ACCEPTANCE

<criterion id="AR74-tz-AC1" cell_refs="AR-tz-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 12 --prefix=test_fwd5_routes_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR74-tz-AC2" cell_refs="AR-tz-74"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 52 --prefix=test_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR74-tz-AC3" cell_refs="AR-tz-74"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py --selftest</invocation><expect>FWD5-SELFTEST-OK</expect></criterion>
`AR74-tz-AC1` -- the new route tests pass, at least 12. Dry-run at box/dell2 BASE: FAIL as expected (the file does not exist). `AR74-tz-AC2` -- the four existing driver test files still pass, 52 functions in all (the unchanged-behavior control; 13 + 8 + 14 + 17): PASS at base as expected. `AR74-tz-AC3` -- the driver's own selftest still prints `FWD5-SELFTEST-OK` with the added checks: PASS at base as expected.

<expected_criteria>AR74-tz-AC1,AR74-tz-AC2,AR74-tz-AC3</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`, the new test file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py`, and the four existing driver test files ONLY for the edits described in item 4 (plus this order's file, your deliverables folder, the surprise channel). The mint helper and `served.py` are not touched.
- **No AWS, no network beyond the local fake, no run, no mint, no deploy.** The ticket-service routes and the exit rules are unchanged.
- **Refusal clause.** If the file at your base already has a route named `request-read`, say so in a surprise row and make no edit to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`; still add the tests.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/fwd5_driver/test_fwd5_driver_routes.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R64_TX.md</decomp_doc> (round 64, workstream ~TX), cell `AR-tz-74`.
<owned_cells>AR-tz-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR74-tz-AC1, AR74-tz-AC2, AR74-tz-AC3. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~277/IRPT_ANLREQ.TO-AR-tz-74.fwd5-routes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR74-tz-AC1,AR74-tz-AC2,AR74-tz-AC3` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the diff size of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` (lines added and removed), the counts passed for the three criteria, the names of every edited existing test, the exit codes of the all-FIRM_BINDING run, the served-body run and the no-selection CONTRACT_VERSION run, the check lines, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- six read routes and two grading rules in a driver, plus tests; no edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission changes in this cell.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: grading a served body to the firm-B principal as UNREACHED (it is content for another firm: LEAK); grading the no-selection route REFUSED only on a fence code (the right refusal there is absence in the caller's own tenant); letting the no-selection route carry a selected_tenant; allowing the download or the bare status shape in the guard; changing the exit rules; editing an existing test beyond the route count and the no-ok grading.
</preflight>

- Cut on the CVO's grade (`org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v26.md`, FWD-5 FAIL unproven) and the CTO's msg 10010: a third sitting drives (a) the packaged ticket's files, (b) the five read routes on the same request and job, (c) one call with no selected_tenant. Risk LOCAL: a driver rule and tests in deliverables folders, nothing run.
- Base: `AR74-tz-AC1` FAIL, `AR74-tz-AC2` PASS, `AR74-tz-AC3` PASS, as expected at box/dell2 BASE.
