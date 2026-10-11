# TO TCKT_VNEXT.TO-R2-ts1 -- by default no ticket_center test can reach a real SES send or a real users-table read

<to_id>TCKT_VNEXT.TO-R2-ts1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~10</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (test files under `infra/`); nothing is applied | **Decomp cell:** `R2-ts-1`
(`decompositions/TCKT_VNEXT_DECOMP_R2.md`) | **outcome_ref:** FWD-1 (hygiene) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~10`. Your worktree is `C:/tmp/tckt-r2-10` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~10 <0.9.0_WK_TCKT_VNEXT~10@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### WHY

Two rows are open against the tests in `infra/aws/lambda/ticket_center/tests/`:
- the tests call the handler's create, submit and claim paths, which reach the real SES client through `_ses_client()`
  (`infra/aws/lambda/ticket_center/lambda_function.py:250-258`, the module global `_ses`) unless a test stubs it. On a box whose AWS
  user may send, a test run would send real mail;
- `_directory_snapshot` (`lambda_function.py`, near `:379-440`) and the profile-scope lookup read the live `opal-users-v2` table
  whenever the box holds AWS credentials and a test did not fake them.
Today this is held off only by procedure (tests are run with invalid AWS keys). This cell makes it structural.

### THE CELL `R2-ts-1`

1. New file `infra/aws/lambda/ticket_center/tests/conftest.py` with ONE autouse, function-scoped fixture that, before every test in
   this directory:
   - installs a guard as the handler module's SES client (the module global `_ses`, and `_ses_client` if needed), whose
     `send_raw_email` and `send_email` raise `AssertionError("real SES send reached from a test")`;
   - installs a guard on the handler's users-table read path (whatever object `_directory_snapshot` and the profile-scope lookup
     query; read the code and guard the narrowest shared object), which raises
     `AssertionError("real users-table read reached from a test")` on `query`, `get_item` and `scan`;
   - restores the previous objects after the test.
   The fixture must NOT override a stub a test installs for itself: the existing tests set `mod._ses`, `mod._table`,
   `mod._directory_snapshot` and similar in their own `setUp` or body, and those assignments happen after an autouse fixture runs, so
   they win. Verify that by running the directory.
   The handler module is imported by the existing tests under the name they already use; import it the same way they do (read
   `test_analysis_request.py` and `test_client_notify.py` for the import and the `sys.path` handling) so the fixture patches the
   SAME module object.
2. New file `infra/aws/lambda/ticket_center/tests/test_no_real_aws.py` with EXACTLY these names:
   - `test_ses_send_is_guarded_by_default`: with no stub installed by the test, calling the module's SES client `send_raw_email`
     raises `AssertionError`;
   - `test_users_table_read_is_guarded_by_default`: with no fake installed by the test, the users-table read path raises
     `AssertionError`;
   - `test_a_test_can_still_install_its_own_stub`: a test that assigns its own SES stub gets its stub called, not the guard.
3. **You edit NO existing test file and NO product file.** If an existing test now fails because it reached the guard, that test was
   reaching real AWS: do NOT edit it and do NOT weaken the guard to let it through. File one row naming the test and the call it
   reached, and make the guard's failure for that path a `pytest.skip` ONLY if there is no other way to keep `tc-regress` green; say
   so in your report. (At the base the directory passes with 147 tests under invalid credentials, so most paths are already faked.)

### ACCEPTANCE

<criterion id="R2-ts1-AC1" cell_refs="R2-ts-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py ts-guard</invocation><expect>TS-GUARD-OK</expect></criterion>
`R2-ts1-AC1`: the three tests exist and pass.

<criterion id="R2-ts1-AC2" cell_refs="R2-ts-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py tc-regress</invocation><expect>TC-REGRESS-OK</expect></criterion>
`R2-ts1-AC2`: the whole `ticket_center/tests` directory passes (at least 147 passed, 0 failed, 0 errors).

<expected_criteria>R2-ts1-AC1 R2-ts1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent) as expected; AC2 OK (passed=147) as expected.

## BOUNDS

- **Grant:** the `<paths>` block, your deliverables folder
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~10/`, and this order's file (status flip only).
- Make no AWS call. Do not touch `lambda_function.py`, any existing test file, or `tests/test_report_ref_shape.py` (another worker's
  cell this round).
- No non-ASCII. A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W10-S<k>`, its own fenced block at the end of the
  investigation file, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Never weaken a test.

<paths>
infra/aws/lambda/ticket_center/tests/conftest.py
infra/aws/lambda/ticket_center/tests/test_no_real_aws.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_CHECKS/r2_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R2.md</decomp_doc> (round 2), cell `R2-ts-1`.
<owned_cells>R2-ts-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-ts1-AC1 R2-ts1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~10/TCKT_VNEXT.TO-R2-ts1.tests-cannot-reach-real-ses-or-users-table.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R2-ts1-AC1 R2-ts1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, the object you guarded for the users-table read and why, any test that
reached the guard, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (test files only).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arm is the third test (a test's own stub still wins) and the no-weakening rule in step 3.
</preflight>

Source: CTO round-2 analysis @bbba700c22 section 4 item 5; rows TCKT_VNEXT-D2-W1-S4 (ARMED, disarmed by procedure) and D2-W7-S1.
