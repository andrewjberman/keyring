# TO-AR-tz-68 -- FWD-5 driver amendment: a run that can exit 0, and the ids it needs (AR-tz-68, round 53, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-68</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~232</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>53</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-68` (`decompositions/IRPT_ANLREQ_DECOMP_R53_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (the driver is merged)

---

## WORKER FACE

### THE CELL

`AR-tz-68`: "a run that can exit 0, and the ids it needs." Round 52 built the FWD-5 driver (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`, merged; READ it and its tests `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py`). Its worker filed two blockers for the later WORLD run, ruled here by the issuer:

1. **The meeting row and the commentary-draft row are EXCLUDED, not UNREACHED.** The DONE WHEN (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` lines 65 to 68) is "tries the ticket and each package file". A POST of a meeting is a WRITE attempt on another firm's ticket and is outside it (its scope refusal is proved offline by `infra/aws/lambda/ticket_center/tests/test_cross_firm_meeting_scope.py`). The commentary draft has no GET route; it rides the ticket read's body, which the LEAK check already inspects. So in the plan and the report both rows carry the closed verdict `EXCLUDED` with their reason, and they count in NEITHER the `UNREACHED` exit (2) NOR the pass: the exit code is decided only over the calls that ARE made (ticket read, ticket list, form-as-filled, original upload, Opal report, report PDF, commentary PDF).
2. **The ids the package routes need are run inputs.** The package routes take a request id, a job id and the other firm's id, which a refused ticket read cannot supply. They are CLI inputs `--firm-b <id> --request-id <id> --job-id <id>`, REQUIRED for a run (a missing one exits 2 before any request), printed in `--plan` and in the usage text, and sourced in the run packet from the ticket that the FWD-1 run files. Today's CLI names none of them (worker row S5).

**What to build.** Edit `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py` for both rulings (the closed verdict set becomes REFUSED, LEAK, UNREACHED, EXCLUDED; the report and the plan print EXCLUDED rows with a one-line reason; the exit code over made calls is 0 only when every made call is REFUSED and no LEAK, 1 on any LEAK, 2 on any made call that was UNREACHED or on a missing required id). Add the new test file `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py` with at least 6 tests named `test_fwd5_driver_<what>` against the fake server: all made calls refused plus both excluded rows gives exit 0 and a report holding EXCLUDED twice; one UNREACHED made call gives exit 2; a LEAK gives exit 1 even with excluded rows; each missing id gives exit 2 with zero requests sent; the plan lists the three ids; the excluded rows are never sent (zero requests for the meeting path). Keep every test of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py` green (edit `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py` only where a test asserted the old UNREACHED meeting behaviour, and say which in your report). Standard library and pytest only; no secret, no real name.

### ACCEPTANCE

<criterion id="AR68-tz-AC1" cell_refs="AR-tz-68"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py tests 6 --prefix=test_fwd5_driver_ org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/fwd5_driver/test_fwd5_driver_exit_semantics.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py</invocation><expect>R46-TESTS-OK</expect></criterion>
`AR68-tz-AC1` -- the new test file exists, every test function is named `test_fwd5_driver_*`, the tests of both files pass and at least 6 pass. Dry-run at box/dell2 4e7c72d5a8: `R46-TESTS-FAIL absent: ...` -- FAIL as expected.

<expected_criteria>AR68-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py`, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py` (edit only as stated), the new test file in your deliverables folder `0.9.0_WK_IRPT_ANLREQ~232/`, the surprise channel, this order's file. The two edited files belong to the round-52 worker's deliverables folder: they are named here and in `<paths>`, which is your grant.
- **No network beyond the local fake server, no AWS, no sign-in, no mint, no run.**
- **Refusal clause.** If something here contradicts what the code does, build for the code, file a surprise row and say so.
- **No alarms, monitors or notifications.**

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/fwd5_driver.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~231/fwd5_driver/test_fwd5_driver_offline.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your own deliverables folder `0.9.0_WK_IRPT_ANLREQ~232/` is granted by the tree convention). Everything else you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R53_TX.md</decomp_doc> (round 53, workstream ~TX), cell `AR-tz-68`.
<owned_cells>AR-tz-68</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR68-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~232/IRPT_ANLREQ.TO-AR-tz-68.fwd5-driver-exit-semantics.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR68-tz-AC1` BEFORE the flip. Commit the files first, then pin.
</proof_of_spec>

**REPORT:** the files edited, the count passed, which old test (if any) you changed, the exit code table you built, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- files in deliverables folders; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies. Traps named for the worker: an EXCLUDED row that silently turns a failure into a pass (the exit code is decided only over calls that are made, and a made call that is unreached is still exit 2); a missing id that still sends a request; printing an id that is a secret (ids are not, but no token or address); changing the old tests to hide a regression.
</preflight>

- Disposes of the issuer-owned rows W231-S1 and S2 (BLOCKING for the later run). Risk LOCAL: deliverables only.
- Base: `AR68-tz-AC1` FAIL as expected (`R46-TESTS-FAIL absent`) at box/dell2 4e7c72d5a8.
