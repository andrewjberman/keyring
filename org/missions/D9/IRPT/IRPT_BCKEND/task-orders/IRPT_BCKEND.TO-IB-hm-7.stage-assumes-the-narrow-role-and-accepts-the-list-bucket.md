# TO IRPT_BCKEND.TO-IB-hm-7 -- BUILD two changes to the HMAC list stage of the directory runner: (a) it ASSUMES the narrow role (fixed session name `hmac-list-stage`) for its secret read and its put (CTO ruling B, msg 10234), (b) its destination bucket is the one the URI names (the globgrph folder), refused only when it would land inside a directory prefix of the firm's own bucket (CTO ruling msg 10203)

<to_id>IRPT_BCKEND.TO-IB-hm-7</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~451</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-7` (decomposition section 245) | **outcome_ref:** FWD-21 | **Ordered by:** the CTO's rulings: msg 10203 (the list is written to ONE key per firm in the globgrph folder, `address()` output) and msg 10234 (B: a narrow role holding `secretsmanager:GetSecretValue` on the one secret and `s3:PutObject` on the three firm keys, trusted by the host's role only; the host profile gains only `sts:AssumeRole` on that role ARN; CloudTrail attribution by a fixed session name `hmac-list-stage`). It builds on the stage IB-hm-2 landed (`emit_hmac_list` in `directory_runner.py`, graded by the issuer).

---

## WORKER FACE

**Cell `IB-hm-7` (inlined).** `data/assets/scripts/gold/investor_reporting/directory_runner.py` holds `emit_hmac_list` (the LAST stage of `run_firm`, after `land()`, inside a catch-all) with its helpers `hmac_list_forms`, `_parse_hmac_uri` and `_hmac_key_bytes`. Two things in it must change, and nothing else:

**(a) Assume the narrow role.** Add an optional runner argument `--hmac-role-arn <arn>` (parser in `main`, passed down through `run_firm` as `hmac_role_arn`, exactly as `--hmac-secret-id` and `--hmac-list-uri` already are). When it is given, `emit_hmac_list` calls `sts.assume_role(RoleArn=<arn>, RoleSessionName="hmac-list-stage")` ONCE and builds BOTH the Secrets Manager client (for `get_secret_value`) and the S3 client (for the single `put_object`) from the temporary credentials the call returns (`AccessKeyId`, `SecretAccessKey`, `SessionToken`); the string `hmac-list-stage` is a module constant (upper-case name) and the ONLY session name; no role session is created when the argument is absent (the ambient session is used, as today). The `sts` client is injectable like the other two (`sts_client=None` means `boto3` at call time). Nothing from the assumed credentials is printed or returned. A failure of `assume_role` is an ordinary exception of the stage: the existing catch-all in `run_firm` reports its class name and nothing else.

**(b) The destination bucket.** Today `_parse_hmac_uri(uri, firm_bucket)` REFUSES any URI whose bucket is not the firm's bucket. The ruling puts the list in the globgrph folder, so the bucket is whatever the URI names. The refusals that remain: not an `s3://` address; an empty key or a key ending in `/`; and **only when the URI's bucket IS the firm's own bucket**, a key that starts with `PROD_PREFIX` or `QA_PREFIX` (the directory prefixes), so the stage still cannot overwrite a directory object. Record the reason in the docstring.

**Six new tests** (added to the EXISTING file `data/assets/scripts/gold/investor_reporting/tests/test_directory_hmac_list.py`; the names are fixed; stub boto3 and STS, no AWS call, invented values only): `test_the_stage_assumes_the_named_role_with_the_fixed_session_name` (the stub STS records `RoleArn` and `RoleSessionName`), `test_the_assumed_credentials_are_used_for_the_secret_and_the_put` (the stub factory for the secrets and S3 clients receives the three credential fields from the stub STS result), `test_without_a_role_arn_the_ambient_session_is_used` (STS is never called), `test_a_uri_in_another_bucket_is_accepted`, `test_a_uri_inside_a_directory_prefix_of_the_firm_bucket_is_refused`, `test_the_session_name_is_the_fixed_literal` (the module constant equals `hmac-list-stage` and the string appears nowhere else as a session name). All ten existing tests must still pass (change an existing test only where it asserted the old firm-bucket refusal, and say which in the notes).

**Do, in this order:**
1. Read `directory_runner.py` from the `HMAC LIST` header comment, `_entry`, `hmac_list_forms`, `_parse_hmac_uri`, `_hmac_key_bytes`, `emit_hmac_list`, `run_firm` and `main`; read the existing test file for the stub style. Record the test-folder counts at base: `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q --color=no` (the folder is red at base for reasons that are not yours; record passed, failed, error counts and keep the failing set identical).
2. Make the two changes and add the six tests. Run the whole test file, then the folder: the failing and error sets must equal base, and the passed count rises by six.
3. Run the three criteria below from the repository root, each under `timeout 300`; AC3 reads `HEAD~1..HEAD`, so run it AFTER your one commit. Record each output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~451/IBhm7_criteria_output.txt`; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBhm7_notes.md` (the changes in a paragraph, the before and after counts).
4. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~451 <0.9.0_WK_IRPT_BCKEND~451@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool; the issuer, not you, amends or flips afterwards): the runner, the test file, your deliverables folder, and any surprise row. Do not push. Report once, under 150 words.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBHM7-AC1" cell_refs="IB-hm-7"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r250/p250_cells.py" . IBHM7-AC1</invocation><expect>IBHM7-AC1 PASS</expect></criterion>
<criterion id="IBHM7-AC2" cell_refs="IB-hm-7"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r250/p250_cells.py" . IBHM7-AC2</invocation><expect>IBHM7-AC2 PASS</expect></criterion>
<criterion id="IBHM7-AC3" cell_refs="IB-hm-7"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r250/p250_cells.py" . IBHM7-AC3</invocation><expect>IBHM7-AC3 PASS</expect></criterion>

<expected_criteria>IBHM7-AC1, IBHM7-AC2, IBHM7-AC3</expected_criteria>

What the checks grade: AC1 the six named tests exist and pass (the check runs pytest on the whole test file); AC2 by AST, `emit_hmac_list` calls `assume_role` with the keyword `RoleSessionName` set to the fixed literal `hmac-list-stage` (or an upper-case module constant) and that literal is in the runner, and `run_firm` still calls `land()` before the stage; AC3 your ONE commit touches only the runner, the test file and this order's paths. The convention of the assumed session, and whether the credentials really reach both clients, are the issuer's read at the drain. Do not edit the checks.

## BOUNDS

- **Grant:** edit `directory_runner.py`; add tests to `tests/test_directory_hmac_list.py`; write `deliverables/0.9.0_WK_IRPT_BCKEND~451/`; the surprise channel for rows. **NO AWS call of any kind; NO change to `refresh.py`, Terraform, the registry or any other file; NO real id, ARN or key material (invent obviously fake ARNs); NO push.**
- **Refusal clause:** STOP and report, writing nothing further, if the stage cannot take the assumed credentials into both clients without a change outside the one file. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~451/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-7.stage-assumes-the-narrow-role-and-accepts-the-list-bucket.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 245 (round 9, workstream ~PM), cell `IB-hm-7`.
<owned_cells>IB-hm-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM7-AC1, IBHM7-AC2, IBHM7-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~451/IRPT_BCKEND.TO-IB-hm-7.stage-assumes-the-narrow-role-and-accepts-the-list-bucket.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a source and test edit in a worktree; nothing is deployed, no AWS call; the new argument is inert until a later cell passes it.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed by this order (the narrow role is created by a later Terraform cell).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p250_cells.py IBHM7 dry-run at base on dell2 2026-10-17 ~04:2xZ: AC1, AC2, AC3 FAIL. Positive control (control250.py) over synthetic git repos each with a base commit and ONE worker commit: the three positives PASS and each of 10 negatives (a test name missing, a named test failing, no test file, no assume_role call, a wrong session name, the keyword missing, the stage before land(), the runner or the tests not in the commit, another file touched) fails its own arm (0 unexpected). NOT measured by me: that the assumed credentials reach both clients (the issuer reads the diff), the destination rule's correctness beyond the two named tests, anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~451`. Class LOCAL.
</preflight>
