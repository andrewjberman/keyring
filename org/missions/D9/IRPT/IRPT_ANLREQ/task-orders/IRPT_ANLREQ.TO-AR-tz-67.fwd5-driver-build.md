# TO-AR-tz-67 -- FWD-5 build: the driver that signs in as a second-firm principal and tries the ticket and each package file (AR-tz-67, round 52, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-67</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~231</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>52</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-67` (`decompositions/IRPT_ANLREQ_DECOMP_R52_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the mint helper `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py` is merged)

---

## WORKER FACE

### THE CELL

`AR-tz-67`: "the FWD-5 driver." FWD-5's DONE WHEN (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` lines 65 to 68) is a seat-driven exercise: a sign-in at another firm tries the ticket and each package file and is refused every time, repeatable on demand. Round 46 built the scoped second-firm mint helper (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~219/fwd5_driver/fwd5_mint.py`, READ it: `mint --email --firm --allowed-firm-ids`, `remove --email`, stdin-only password). This cell builds the DRIVER, BUILD ONLY and OFFLINE: the run is a later WORLD act by the applier under a pair, after `2.0.0_SA_COO~V2`'s release, and you do not run it.

**What to build** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` (Python, standard library only; model the sign-in and the route guard on `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`, which you READ for how the real sign-in form and cookies or bearer work on DEV; the portal's own API routes for a ticket and its package files are listed in the front-door record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~212/FWD5_FRONT_DOOR_AND_PORTAL_MAP.md` and the ticket-service fence map `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~210/FWD5_TICKET_SERVICE_FENCE_MAP.md`, READ both):

1. `python fwd5_driver.py --plan` prints the plan (the routes it will call, in order) and exits 0 with no network. `--selftest` runs offline (no network, no AWS, no browser). `--base <url> --email <addr> --ticket <ticket id of ANOTHER firm> --firm-a <the principal's firm> --out <dir> --go IRPT_ANLREQ.TO-RUN-FWD5.<id>` is the run; without a `--go` matching `^IRPT_ANLREQ\.TO-RUN-FWD5\.\S+$` it prints the plan and exits 0.
2. The password is read from stdin as one JSON object `{"password": "..."}`, exactly as the mint helper reads it; it is never printed, logged or written, and neither is any cookie, token or address (print only the digest of an address if one must be named).
3. The run signs in as the scoped principal, then for the named ticket of another firm calls, in order: the ticket read; the ticket list (the other firm's ticket must be absent from the principal's list); each package-file route the record lists (original upload, the form as filled, the Opal report, the report PDF, the commentary draft, the commentary PDF) by the ticket's `report_ref` and package pointers; and the meeting route. Expectation per call: the response is a REFUSAL (a 403 or the service's 404 for out of scope) and the body carries nothing of the ticket (no title, no firm name, no file bytes); any 2xx with a body, or any body that names the other firm or holds file bytes, is a LEAK. The driver exits 0 only when EVERY call was refused and no LEAK was seen; it exits 1 on any leak and 2 on any call it could not make (an unreached route is not a pass).
4. A route allow-list guard: the driver may only issue GET to the listed ticket routes and POST to the sign-in routes; any other request is refused before it is sent (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_driver.mjs`'s POST_ALLOWED pattern).
5. The out directory receives one JSON report with, per call: the route name, the status code, a closed verdict (`REFUSED`, `LEAK`, `UNREACHED`) and the body length only (never the body).

**Offline tests** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py` (stdlib and pytest; every test named `test_fwd5_driver_<what>`; use an in-process fake HTTP server on a free local port or an injected transport; synthetic names only): all-refused gives exit 0 and a report with only `REFUSED`; one 200 with a body gives exit 1 and a `LEAK`; a call that fails to connect gives exit 2 and `UNREACHED`; a refused body that contains the other firm's name is a LEAK; the guard refuses a PUT or a POST to a ticket route before sending (the fake server sees zero such requests); the report holds no body, cookie, token or password (grep the written file for the planted values); `--plan` and a `--go` that does not match print the plan and send nothing (zero requests to the fake server); stdin password never appears in stdout. At least 8 tests.

### ACCEPTANCE

<criterion id="AR67-tz-AC1" cell_refs="AR-tz-67"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 8 --prefix=test_fwd5_driver_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR67-tz-AC1` -- the test file exists, every test function is named `test_fwd5_driver_*`, the tests pass and at least 8 pass. Dry-run at box/dell2 ac2ce8a2d7: `R46-TESTS-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR67-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/` (your deliverables folder, granted by the tree convention) and the surprise channel, this order's file. No source file, no other test.
- **No network beyond a local fake server in tests, no AWS, no secret, no mint, no run.** You do not sign in anywhere real.
- **Refusal clause.** If a route in the record cannot be located in the portal or the ticket service in your cone, list it in the plan as `UNREAD` with the reason and file an OBSERVATION row; do not invent a route. If a folder is outside your cone, file a `BLOCKING` row naming it.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder `0.9.0_WK_IRPT_ANLREQ~231/` is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R52_TX.md</decomp_doc> (round 52, workstream ~TX), cell `AR-tz-67`.
<owned_cells>AR-tz-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR67-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/IRPT_ANLREQ.TO-AR-tz-67.fwd5-driver-build.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR67-tz-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the files, the count passed, the routes in the plan (and any `UNREAD`), the guard's refusals, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- new files in a deliverables folder; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the later run is a separate WORLD act.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: a driver that exits 0 when a route was never reached; treating a 2xx with an empty body as a refusal; printing or writing a cookie, token, address or body; a guard that checks the method but not the path; inventing a route the record does not list.
</preflight>

- Cut on the CTO's Move 2 (msg 8742) "FWD-5's cross-firm tests", the seat-driven exercise being the DONE WHEN. The run (mint on DEV, drive, remove) follows V2's release (target Oct 20) as a WORLD act through `0.7.0_AE_CloudOps~AQ2` under a pair. Risk LOCAL: new files in a deliverables folder, nothing run.
- Base: `AR67-tz-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 ac2ce8a2d7.
