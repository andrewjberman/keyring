# TO-AR-tz-72 -- FWD-5 driver: send the contract version and grade the report-side routes by the envelope (AR-tz-72, round 62, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-72</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~275</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-72` (`decompositions/IRPT_ANLREQ_DECOMP_R62_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the driver and its control mode are merged)

---

## WORKER FACE

### THE CELL

`AR-tz-72`: "the cross-firm driver grades the report-side routes by the ENVELOPE, with the contract version sent." The live sitting of 2026-10-16 read HTTP 200 on four report-side routes (`original-upload`, `opal-report`, `report-pdf`, `commentary-pdf`) for BOTH the firm-B principal and the entitled control. The CTO traced it (row `IRPT_ANLREQ-D2-S157`): the function `infra/aws/lambda/investor-reporting/_authz/served.py` refuses a request that does not carry the header `X-Contract-Version: v1` BEFORE any firm or record read (lines 1198-1202) and answers HTTP 200 with a REFUSAL ENVELOPE: a JSON object `{"ok": false, "contract_version": "v1", "operation": ..., "status": {..., "public_reason_code": "<CODE>", ...}}` (read `refuse()` at line 453 and `status_envelope()` at line 339 of that file). The driver sent no such header and graded any 2xx a LEAK (run) or ALLOWED (control), so both verdicts on those four routes were false. A fence refusal is `FIRM_BINDING` (or `NOT_AUTHORIZED`); a `CONTRACT_VERSION` refusal says nothing about the fence.

**What to do (in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`).**
1. Send the header `X-Contract-Version: v1` on EVERY GET the driver makes (run mode and control mode). The sign-in POST is unchanged.
2. For the routes whose path starts with `/api/scoped/investor-reporting/` (the four report-side routes), grade a 2xx answer by its JSON envelope instead of by the status alone. Parse the body as a JSON object; `ok` must be a boolean; the reason code is `status.public_reason_code` when it is a string matching `^[A-Z][A-Z0-9_]{2,40}$`, else the code is `?`. The body is read and dropped; only `ok` and the code are kept.
   - RUN mode: `ok` true -> `LEAK`; `ok` false and code in {`FIRM_BINDING`, `NOT_AUTHORIZED`} -> `REFUSED`; `ok` false with ANY OTHER code (including `CONTRACT_VERSION` and `?`) -> `UNREACHED` with the reason "refused by <code>, not by the firm fence"; a 2xx that is not a JSON object or has no boolean `ok` -> `UNREACHED`.
   - CONTROL mode: `ok` true -> `ALLOWED`; `ok` false with code `CONTRACT_VERSION` or `?` -> `UNREACHED`; `ok` false with any other code -> `DENIED` (the reason names the code); not a JSON object or no boolean `ok` -> `UNREACHED`.
   - Non-2xx answers on these routes keep today's grading. The ticket-service routes (`/api/scoped/tickets...`) are graded exactly as today. The marker scan stays as it is in run mode and is applied to the body BEFORE the envelope grading (a marker in any body is a LEAK).
3. Each report row gains the key `code`: the reason code (string) for a report-side route that was graded by its envelope, else the empty string. Nothing else is added to a row; the report still never holds a body, a cookie, a token, a password or an address (a reason code is a closed-vocabulary word, not a body).
4. Exit codes and the control exit rule are unchanged. Extend `selftest()` by at least four checks of the envelope grading (keep every existing check).
5. Tests: the NEW file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py`, tests named `test_fwd5_envelope_<what>` (a local fake HTTP server on 127.0.0.1, in the style of the existing offline tests; import the driver by inserting its folder on `sys.path`). At least 10: every GET carries `X-Contract-Version: v1` (the fake records headers); run mode `ok` true on a report-side route is LEAK and exits 1; `FIRM_BINDING` is REFUSED; `NOT_AUTHORIZED` is REFUSED; `CONTRACT_VERSION` is UNREACHED and exits 2; another code is UNREACHED; a 2xx non-JSON body is UNREACHED; a non-boolean `ok` is UNREACHED; control mode `ok` true is ALLOWED, `FIRM_BINDING` is DENIED, `CONTRACT_VERSION` is UNREACHED; a ticket route 200 is still LEAK in run mode; the report rows carry `code` and no body. The three existing driver test files MAY be edited ONLY where a test asserted the old whole-2xx grading of a report-side route; keep each such test's intent, change its fake answer to a refusal or success ENVELOPE, and list every edited test by name in a surprise row. Keep every other existing test as it is.

Standard library and pytest only. No AWS, no network beyond the local fake, no secret, no run. Use plain names.

### ACCEPTANCE

<criterion id="AR72-tz-AC1" cell_refs="AR-tz-72"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 10 --prefix=test_fwd5_envelope_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR72-tz-AC2" cell_refs="AR-tz-72"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 35 --prefix=test_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py</invocation><expect>R46-TESTS-OK</expect></criterion>
<criterion id="AR72-tz-AC3" cell_refs="AR-tz-72"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py --selftest</invocation><expect>FWD5-SELFTEST-OK</expect></criterion>
`AR72-tz-AC1` -- the new envelope tests pass, at least 10. Dry-run at box/dell2 BASE: FAIL as expected (the file does not exist). `AR72-tz-AC2` -- the three existing driver test files still pass, 35 functions in all (the unchanged-behavior control; 21 + 14): PASS at base as expected. `AR72-tz-AC3` -- the driver's own selftest still prints `FWD5-SELFTEST-OK` with the added checks: PASS at base as expected.

<expected_criteria>AR72-tz-AC1,AR72-tz-AC2,AR72-tz-AC3</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`, the new test file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py`, and the three existing driver test files ONLY for the edits described in item 5 (plus this order's file, your deliverables folder, the surprise channel). The mint helper and `served.py` are not touched.
- **No AWS, no network beyond the local fake, no run, no mint, no deploy.** The ticket-route grading and the exit rules are unchanged.
- **Refusal clause.** If the file at your base already sends `X-Contract-Version`, say so in a surprise row and make no edit to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`; still add the tests.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/fwd5_driver/test_fwd5_driver_envelope.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~272/fwd5_driver/test_fwd5_driver_control.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R62_TX.md</decomp_doc> (round 62, workstream ~TX), cell `AR-tz-72`.
<owned_cells>AR-tz-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR72-tz-AC1, AR72-tz-AC2, AR72-tz-AC3. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~275/IRPT_ANLREQ.TO-AR-tz-72.fwd5-envelope-grading.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR72-tz-AC1,AR72-tz-AC2,AR72-tz-AC3` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the diff size of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` (lines added and removed), the counts passed for the three criteria, the names of every edited existing test, the exit codes of the `CONTRACT_VERSION` case (run mode) and the `FIRM_BINDING` case (run mode), the check lines, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a request header and a grading rule in a driver nobody has run successfully, plus tests; no edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission changes in this cell.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: grading a CONTRACT_VERSION refusal as REFUSED (it says nothing about the firm fence: it is UNREACHED); grading any `ok` false as the fence (only FIRM_BINDING and NOT_AUTHORIZED are); sending the header only on report-side routes; echoing the body or the reason text into the report (only the closed-vocabulary code); changing the ticket-service grading or the exit rules; editing an existing test beyond the report-side whole-2xx assertions.
</preflight>

- Cut on the CTO's ruling msg 9907 (row S157): the live sitting's four 200s were CONTRACT_VERSION refusals for both identities; the next sitting needs a driver that sends the header and grades by the envelope, with the control reading ok true. Risk LOCAL: a driver rule and tests in deliverables folders, nothing run.
- Base: `AR72-tz-AC1` FAIL, `AR72-tz-AC2` PASS, `AR72-tz-AC3` PASS, as expected at box/dell2 BASE.
