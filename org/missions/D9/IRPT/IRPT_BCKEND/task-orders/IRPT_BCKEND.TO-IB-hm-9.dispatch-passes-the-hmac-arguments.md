# TO IRPT_BCKEND.TO-IB-hm-9 -- BUILD the dispatch half of the per-firm HMAC list: `refresh.py` hands the runner's three HMAC arguments (`--hmac-secret-id`, `--hmac-role-arn`, `--hmac-list-uri`) to each firm's build, from the Lambda's environment, validated, and only when all three are configured (CTO rulings msg 10203 and 10234)

<to_id>IRPT_BCKEND.TO-IB-hm-9</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~453</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-9` (decomposition section 246) | **outcome_ref:** FWD-21 | **Ordered by:** the CTO's rulings: msg 10203 (the step is in the runner, one key per firm), msg 10234 (B: a narrow role the stage assumes), and the builder outputs recorded in `deliverables/2.0.0_SA_COO~P2/IB-hm-3_BUILDER_OUTPUTS_FOR_THE_HMAC_LIST_20261017.md` (the three per-firm list URIs, the role name, the secret name `irpt/hmac-list/key`). It builds on the runner arguments IB-hm-2 and IB-hm-7 landed (`--hmac-secret-id`, `--hmac-list-uri`, `--hmac-role-arn` in `data/assets/scripts/gold/investor_reporting/directory_runner.py`).

---

## WORKER FACE

**Cell `IB-hm-9` (inlined).** `infra/aws/lambda/investor-reporting/directory/refresh.py` dispatches one SSM command per firm to the runner host. `runner_script(firm_id, business_date, bundle_uri, run_stamp, work_root=...)` (line 634) returns the shell; its build line is `python3 $R/directory_runner.py --firms %s --upload 2>&1`. The class `SsmBuildDispatcher` builds that script at about line 803 and, for a firm with a source principal in the Lambda's `IRPT_DIRECTORY_SOURCE_ROLE_MAP`, prepends an `export IRPT_SOURCE_READ_ROLE_ARN='...'` line; `_firm_source_roles_from_env()` (line 1388) is the model for reading and VALIDATING an environment value that is written into a shell line (a value that is not made of the allowed characters is DROPPED, never quoted around). **You add the same kind of path for the HMAC arguments:**
1. **Three environment variables** read by new module-level helpers (names fixed): `IRPT_HMAC_SECRET_ID` (the secret id string), `IRPT_HMAC_ROLE_ARN` (an IAM role ARN) and `IRPT_HMAC_LIST_URI_MAP` (a JSON object `{firm_id: "s3://bucket/key"}`). A helper `_hmac_args_for(firm_id)` returns the list of CLI tokens `["--hmac-secret-id", <id>, "--hmac-role-arn", <arn>, "--hmac-list-uri", <uri>]` for that firm, or `[]` unless ALL THREE are present and valid for that firm. Validation (a value that fails is DROPPED and the firm builds as today, no hmac arguments): the secret id matches `^[A-Za-z0-9/_+=.@-]{1,512}$`; the role ARN starts `arn:aws:iam::`, contains `:role/` and uses only the characters `_ARN_CHARS` already allows; the URI matches `^s3://[a-z0-9][a-z0-9.-]{2,62}/[A-Za-z0-9/_.=+@-]+$`, has no `..` and does not end in `/`.
2. **The dispatch.** `runner_script` gains an optional keyword `hmac_args=None` (a list of tokens) and, when given and non-empty, appends them to the build line, each token shell-quoted by `shlex.quote`; with `hmac_args` absent or empty the returned script is BYTE-IDENTICAL to today's (a test proves it). `SsmBuildDispatcher` passes `_hmac_args_for(firm_id)` and appends one trail line `hmac list stage armed for the <firm_id> build` (the firm id only; no value) when it passes any.
3. **No literal in the source.** `refresh.py` must contain no string constant that holds a secret id, a role ARN, a bucket name or an `s3://` address for this feature: every value comes from the environment (the Terraform cell sets it). The check greps the AST for such constants.

**Six new tests** in a new file `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_hmac_args.py` (names fixed; invented values only; no AWS call): `test_all_three_values_yield_the_six_tokens_for_a_firm`, `test_a_missing_value_yields_no_tokens`, `test_a_firm_absent_from_the_uri_map_yields_no_tokens`, `test_an_unsafe_value_is_dropped_never_quoted_around` (a value with a quote, a semicolon or a space in each of the three), `test_the_script_without_hmac_args_is_byte_identical_to_the_old_script` (compare with the script from a call that passes no `hmac_args`, AND assert the build line is exactly `python3 $R/directory_runner.py --firms <firm> --upload 2>&1`), `test_the_dispatcher_passes_the_tokens_into_the_script_and_trails_the_firm_id_only` (stub SSM; no value appears in the trail).

**Do, in this order:**
1. Read `refresh.py` lines 600 to 720, 780 to 830 and 1380 to 1401, the existing refresh tests for the stub style (`tests/test_refresh_manifest_dispatch_date.py` has `FakeS3`/`FakeSSM`), and run `python -m pytest infra/aws/lambda/investor-reporting/directory/tests -q --color=no -p no:cacheprovider --continue-on-collection-errors` once; record passed, failed, error counts (the folder may be red at base for reasons that are not yours; the failing and error sets must be identical after).
2. Implement and test. Run the three criteria below from the repository root, each under `timeout 300` (AC3 reads `HEAD~1..HEAD`: run it AFTER your one commit). Record AC1 and AC2 output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~453/IBhm9_criteria_output.txt` BEFORE the commit; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBhm9_notes.md` (the change in a paragraph, before and after counts).
3. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~453 <0.9.0_WK_IRPT_BCKEND~453@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): `refresh.py`, the new test file, your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words, with AC3's result.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBHM9-AC1" cell_refs="IB-hm-9"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r252/p252_cells.py" . IBHM9-AC1</invocation><expect>IBHM9-AC1 PASS</expect></criterion>
<criterion id="IBHM9-AC2" cell_refs="IB-hm-9"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r252/p252_cells.py" . IBHM9-AC2</invocation><expect>IBHM9-AC2 PASS</expect></criterion>
<criterion id="IBHM9-AC3" cell_refs="IB-hm-9"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r252/p252_cells.py" . IBHM9-AC3</invocation><expect>IBHM9-AC3 PASS</expect></criterion>

<expected_criteria>IBHM9-AC1, IBHM9-AC2, IBHM9-AC3</expected_criteria>

What the checks grade: AC1 the six named tests exist and pass (the check runs pytest on the new file); AC2 by AST, `runner_script` takes `hmac_args`, the module defines `_hmac_args_for`, and no string constant of `refresh.py` holds `secretsmanager`, `globgrph`, `opal-data-assets` or an `s3://` address; AC3 your ONE commit touches only `refresh.py`, the new test file and this order's paths. The no-regression read of the existing folder is the issuer's. Do not edit the checks.

## BOUNDS

- **Grant:** edit `infra/aws/lambda/investor-reporting/directory/refresh.py`; add `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_hmac_args.py`; write `deliverables/0.9.0_WK_IRPT_BCKEND~453/`; the surprise channel for rows. **NO AWS call; NO change to any other source file, Terraform or registry; NO real secret id, ARN, bucket or key (invent fakes in tests); NO push.**
- **Refusal clause:** STOP and report, writing nothing further, if the dispatch cannot take the tokens without changing a file outside the two; or if the script without hmac arguments cannot stay byte-identical. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
infra/aws/lambda/investor-reporting/directory/refresh.py
infra/aws/lambda/investor-reporting/directory/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~453/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-9.dispatch-passes-the-hmac-arguments.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 246 (round 10, workstream ~PM), cell `IB-hm-9`.
<owned_cells>IB-hm-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM9-AC1, IBHM9-AC2, IBHM9-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~453/IRPT_BCKEND.TO-IB-hm-9.dispatch-passes-the-hmac-arguments.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a Lambda source and test edit in a worktree; nothing is deployed and no AWS call is made; the new path is inert until the Terraform cell sets the three environment variables and a later pair authorises the apply.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p252_cells.py IBHM9 dry-run at base on dell2 2026-10-17 ~05:2xZ: AC1, AC2, AC3 FAIL. Positive control (control252.py) over synthetic git repos each with a base commit and ONE worker commit: the three positives PASS and each negative (a test name missing, a named test failing, no test file, runner_script without hmac_args, no _hmac_args_for, a string constant naming secretsmanager or globgrph or opal-data-assets or an s3 address, refresh.py or the tests not in the commit, another file touched) fails its own arm. NOT measured by me: the validation regexes' sufficiency (the tests and the issuer's read), the dispatch behaviour on a real host, anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~453`. Class WORLD (the gate's floor for an infra/aws/lambda path; the act is a source and test edit in a worktree and deploys nothing).
</preflight>
