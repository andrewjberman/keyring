# TO IRPT_ANLREQ.TO-AR-y-320.release29b-build-ticket-service -- BUILD the opal-ticket-api package for the owner check (AR-y-316) and compare it with the live package; read the Terraform source change that must ride with it

<to_id>IRPT_ANLREQ.TO-AR-y-320</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~130</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZH</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the infrastructure `<paths>` imply; the worker builds only: nothing is uploaded, applied or invoked)
**Decomp cell:** `AR-y-320` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (hop 1, the filing) | **depends_on:** `AR-y-316` (merged `49f70cd078`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~130`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-130` (branch `wk-IRPT_ANLREQ-130`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~130 <0.9.0_WK_IRPT_ANLREQ~130@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W130-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call EXCEPT the read-only AWS reads the steps name (`get-function`, `get-function-configuration`, `list-object-versions`, `head-object`, a download of the live zip or of a version of the artifact key, through the `.tools/aws` shim), and a `git fetch` of remote-tracking refs; no push, no deploy, no upload, no apply, no invoke, no Terraform plan or apply. No non-ASCII in what you add. Scratch outside the product tree (you may not delete recursively; say where it is).
- **THE BUILD GUARD (a past incident: row D2-S69):** every build is `BUILD_ONLY=1`, and before the first build at a base commit you run `git show <commit>:infra/aws/lambda/ci/build-and-upload.sh | grep -c BUILD_ONLY`: it must print at least 1 (the trunk builder prints 8). At a commit older than the guard the script UPLOADS. Print the count in your record. Your run must never reach `aws s3 cp`. The script writes ONE fixed temp path per function: use a PRIVATE `TMPDIR` (a new empty folder outside the repository) for every build and copy the zip out at once. Stage every artifact under `C:/dev/irpt-release-r29b/` (create it; it is outside the repository); never delete anything you did not make.

### THE CELL (`AR-y-320`, inlined) -- BUILD ONLY. Nothing is uploaded, applied, deployed or invoked.

*The ticket service's SUBMIT-FORM owner check (`AR-y-316`, merged `49f70cd078`, row W101-S3) is source only. This cell builds the package that carries it: `opal-ticket-api` (`infra/aws/lambda/ticket_center`) gets `lambda_function.py` from the trunk. It must NOT be released without its IAM statement: the check reads `irpt-requests` and FAILS CLOSED with a 503 when the read is denied, so a release without the grant would refuse every client filing. The Terraform source change that carries the grant and the environment variable is in `infra/aws/terraform/ticket-center/main.tf` (the data source `irpt_requests`, the statement `IrptRequestsInputOwnerRead`, and `IRPT_REQUESTS_TABLE` in the Lambda environment). Live now (release 28, 2026-10-14T01:58:04Z): CodeSha256 `C/Rt/FnSqOj7SnZC1GeoEilj8jbCKdvAUHnxYrnNZNM=`, 34057 bytes, one member `lambda_function.py` sha256 `cfa99176f89f7cdb32c3e171bdfdf930a605ee51fd3e590b1a55e878073d4d70`, S3 object `ticket-center/opal-ticket-api.zip` VersionId `7vn6xyMOZjpSaKwiT73UaNfXj6mNSljr` (the rollback target). The Lambda is released by Terraform (`s3_object_version`), never by a code update call, and the applier does that, not you.*

Read first: the release-28 build record of YOUR package `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~115/r30/OPAL_TICKET_API_BUILD.json` (the base, the recorded inputs, the build command, the guard counts and the control that reproduced the package that was live), the applier's closing report `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r28/A_AFTER_R28a.txt` (what is live now, with the VersionId), and the worker 126 record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~126/r40/` (or its deliverable folder) for the owner check itself. The release moves ONLY `lambda_function.py`; if the comparison with the live package shows ANY other differing member, STOP the build, file a BLOCKING row naming it, and record what you have.

1. **The live read.** `.tools/aws lambda get-function --function-name opal-ticket-api --query Configuration.CodeSha256 --output text` and `Code.Location`; download the zip into a NEW EMPTY folder under your `.scratch/r40/` (write the URL to a file and read it from Python run with `-I`), check its sha256 base64 equals the CodeSha256, and take `member_manifest` (member name -> sha256). `list-object-versions` for the artifact key `ticket-center/opal-ticket-api.zip` in bucket `opal-313476888478-lambda-artifacts` (prefix exact; print the latest VersionId and the version count as the denominator; read the listing as a whole JSON, NOT through a paged `--query length()`): the latest VersionId is the rollback target. Print each next to the values above; a difference is a finding (someone released since): say what changed and carry on only if the change is already on the trunk.
2. **The no-move control.** Reproduce the live package: the base and any diff the release-28 build used are in the record named above (its `no_move_control` and `release_input`). Rebuild the live package in a throwaway worktree OUTSIDE the product tree at that base (guard count printed): `TMPDIR=<private> BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh ticket-center opal-ticket-api` (use `git -c core.longpaths=true worktree add --detach`). Its CodeSha256 must equal the live one and `differs_from_live` must be `[]`. If the live package cannot be reproduced, name the members that differ and STOP with a BLOCKING row.
3. **The release input.** Check out the trunk HEAD in a throwaway worktree (state its full sha; it must contain `49f70cd078`). The only packaged member expected to differ is `lambda_function.py`. Make any change ONLY in a second throwaway worktree (never the trunk's map or recipe); save `git diff` of anything you edit there (the map, a builder) as `r40/<name>.diff` in your deliverable folder and print its `git hash-object`. Every moved member's new bytes must equal the trunk HEAD's blob (print both sha256).
4. **Build the release.** `BUILD_ONLY=1`, same command, private TMPDIR. Stage the zip as `C:/dev/irpt-release-r29b/opal-ticket-api-r29b.zip`. Record `artifact` {`path`, `sha256` (hex of the zip), `bytes`, `code_sha256_base64` (the digest the script prints)}.
5. **Compare with the LIVE package, member by member.** `delta_vs_live` = members whose sha256 differ; `only_in_live`; `only_in_release`. EXPECTED: EXACTLY `["lambda_function.py"]`, equal to the trunk HEAD's blob. Anything else: BLOCKING row, do not widen.
6. **Tests.** Run, from the build's source tree, `infra/aws/lambda/ticket_center/tests/` whole (report `passed`, `failed`, `skipped`, `denominator`; the expected figure from worker 126's record is 300 passed) and name the new file `test_submit_input_owner.py`'s count (21).
7. **The Terraform source, READ ONLY.** From the trunk HEAD, print `git diff <the release-28 applier's close commit or the base of step 2> <trunk HEAD> -- infra/aws/terraform/ticket-center/main.tf` and record in `terraform_note`: (a) every resource the next scoped plan would change besides the Lambda's code attributes (the new `data.aws_dynamodb_table.irpt_requests`, the policy `opal_ticket_api_ddb` statement `IrptRequestsInputOwnerRead`, the environment variable `IRPT_REQUESTS_TABLE`), by name, (b) which Terraform root and which `-target` list a plan must use to carry the policy and the Lambda together, and the ORDER the pair must state (the grant BEFORE the code, because the check fails closed), (c) anything in the diff that is NOT these three (say what; the pair must name it). You do not run Terraform.
8. **Write `r40/OPAL_TICKET_API_BUILD.json`** (the record the checker reads; the checker `y320-build` is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py`): `live_read`, `guard_counts`, `no_move_control` {`code_sha256`, `differs_from_live`}, `release_input`, `artifact`, `delta_vs_live`, `only_in_live`, `only_in_release`, `rollback` (the S3 latest VersionId and sha256 of the key), `tests` {`passed`, `failed`, `skipped`, `denominator`, `named_tests`}, `terraform_note`, `claim`, `not_read`.
9. **In your report:** the live read in one line, the control (equal or not), the delta (members), the artifact path and sha256, the tests, the three Terraform items.

### ACCEPTANCE

<criterion id="AR320-y-AC1" cell_refs="AR-y-320"><invocation>python C:/dev/wk-irpt-anlreq-130/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y320-build --root C:/dev/wk-irpt-anlreq-130</invocation><expect>Y320-BUILD-OK</expect></criterion>
`AR320-y-AC1`: the record carries the live read, a no-move control equal to the live CodeSha256, a staged release zip whose sha256 the checker recomputes, a delta against the live package of exactly lambda_function.py, passing tests, and the rollback VersionId.

<criterion id="AR320-y-AC2J" cell_refs="AR-y-320" judgment="true"/>
`AR320-y-AC2J` (judgment, graded at L9, never by you): the live package was read from AWS in this run and not taken from a record, the guard count was printed before each build, both builds were BUILD_ONLY with a private TMPDIR, the delta is exactly the one member, the Terraform note names every resource a plan would change and the grant-before-code order, and nothing was uploaded or applied.

<expected_criteria>AR320-y-AC1 AR320-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~130/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-320</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~130/IRPT_ANLREQ.TO-AR-y-320.release29b-build-ticket-service.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-320`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR320-y-AC1,AR320-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package zip staged outside the product tree, throwaway worktrees outside the repository, and read-only live AWS reads (get-function, list-object-versions, a download of the live zip); nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no change; step 7 only READS the Terraform source diff.
comp-adversary: RUN -- by reading the release-28 record of this package and rows W115-S1, W116-S1 and D2-S69 against the cell; the lens: a control that reproduces a stale package instead of the one live now, a build at a commit without the guard that uploads, a member that moves that no cell changed, a code release described without the grant it needs (the check fails closed). The order requires the live read in the run, the guard count before each build, the whole-package comparison and a Terraform note that names the grant-before-code order. NOT seen: the live role policy, the live table.
</preflight>

---

## RECORD FACE

- Cut on the merged owner check `AR-y-316` (`49f70cd078`) after the CTO's rulings msgs 7620 and 7633, workstream `ZH` of round 40. The release pair (the issuer's, after this cell) names the one widening (the `irpt-requests` read grant: `dynamodb:GetItem`, the three firms, the owner attributes) and the order grant-then-code. Base: `AR320-y-AC1` FAIL as expected (no record).
