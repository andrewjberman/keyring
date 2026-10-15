# TO IRPT_BCKEND.TO-IB-pr-554 -- BUILD hop 3: the /report route, a NEW named-account reader, the all-accounts scope refusal and the route declaration (serve-path pair, build slice b)

<to_id>IRPT_BCKEND.TO-IB-pr-554</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~398</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 7995 (CTO half of the serve-path pair signed @82183fcfaf; the document's source ruled; build slices may start now) and the packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (sha256 `7daa29f0fe10e0a7bda3eb2c12f1eee3bb4ca43ecc7361fbdf1327ded864abac`) | **Decomp cell:** `IB-pr-554` (decomposition section 194) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-398`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~398 <0.9.0_WK_IRPT_BCKEND~398@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch398/`).

**Cell `IB-pr-554` (inlined).** Hop 3 of the filled-report serve path (CTO half signed, msg 7995): a NEW route `GET /api/scoped/investor-reporting/reporting/client/{client_id}/report` on the reporting-read lambda that returns the platinum filled report with NO re-shaping and REFUSES unless the viewer's scope covers EVERY account the document names. READ FIRST: the packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (sections 1, 3, 4, 9) and the design record `deliverables/0.9.0_WK_IRPT_BCKEND~395/IB199-3_serve_path_design.json` (hop 3), then `infra/aws/lambda/investor-reporting/reporting/entry.py` (SUMMARY_ROUTE_KEY near line 92, the summary object near line 93, `_summary_named_accounts` near line 317, `serve_summary` near line 332 with its `_check_covered` loop near line 344, the ROUTES map near line 373), `infra/aws/terraform/investor-reporting/reporting-read/api.tf` (the summary route near line 34) and `locals.tf` (near line 75), and the existing tests `reporting/tests/test_reporting_summary.py` and `test_reporting_entry.py` (the summary's tests are your model: stubs for storage and scope, no AWS). The document shape is contract 0.5.1 (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, block `document`): `household.accounts[]` entries carry `account_id`; `values` members of account grain hold `{"by_row": {"<account_id>": figure}}`.

**Build, in `entry.py` (all new logic inside the BEGIN/END blocks):** (1) a route key for the new route beside SUMMARY_ROUTE_KEY and one new key in ROUTES; (2) a NEW reader `_filled_named_accounts(document)` returning every account id the document names: each `household.accounts[].account_id` and every account key of each `values` member's `by_row` map that is keyed by an account (the summary's reader cannot be reused: the filled document nests its accounts and carries no top-level firm or client_id); (3) a new operation `serve_filled_report` modeled on `serve_summary`: the object read is the one at the platinum filled-report address for client=<id> built by the SAME naming builder call the summary uses, with the object name `filled_report.json` (declare the name in this file; do not type a key); a missing object is NOT_READY; an object of another firm is refused; every named account must pass the same `_check_covered` the summary uses, and ANY uncovered account refuses the whole request with `OBJECT_NOT_COVERED` and NO bytes (the scope-check loop is the block the difference control removes); a client id in the request is a claim, never a grant; the body returned is the stored document unchanged. **In `api.tf`:** exactly ONE new `aws_apigatewayv2_route` resource for the new route beside the summary route, on the same integration and authorizer; **in `locals.tf`:** the route-key local if the summary route has one (copy the pattern). No IAM change is needed (packet section 4); do not add one. Existing behaviour is unchanged: the existing tests must still pass.

**Write the tests** `infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_filled_report.py` (at least 10 tests; stubs; synthetic ids): full coverage is served byte-for-byte; and tests whose function NAMES contain these words (the check reads the names): `uncovered_viewer` (a viewer covering fewer accounts than the document names is refused OBJECT_NOT_COVERED with no bytes), `client_id_is_claim` (a client id in the request never grants access), `nested_accounts_named` (accounts named only inside a `by_row` map and inside `household.accounts` are both checked), `other_firm` (a document of another firm is refused); also a missing object is NOT_READY, and the route key is in ROUTES.

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~398/IB200-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[every product path you changed, sorted; deliverables and the channel excluded],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"negative_tests":["uncovered_viewer","client_id_is_claim","nested_accounts_named","other_firm"],"notes":["what each fact rests on and what was not read; say whether terraform validate could be run"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2).** Wrap the NEW product logic of this cell in `# BEGIN FILLED-REPORT-B` ... `# END FILLED-REPORT-B` comment lines in the file(s) named below (one or more blocks per file; the whole new function bodies and the new branches). The check removes every such block IN MEMORY and runs YOUR new test file: it must then FAIL on ASSERTIONS (a failed test), not on an import or collection error. So write the blocks so that, with them removed, the module still imports (no module-level statement may use a name defined only inside a block), and write the new tests so that they reference the new names only INSIDE test functions. A test file that still passes with the blocks removed is the defect the control exists to catch.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB200-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**AMENDMENT 1 (the issuer, 2026-10-15 ~04:2xZ, on your row `IRPT_BCKEND-D2-W398-S1`; my defect, the grant omitted a pinning test):** `infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_entry.py` line 74 (`test_one_route_and_function_name`) pins `entry.ROUTES` to EXACTLY two keys, so the new third key makes it fail. That file is now IN your grant: update ONLY that pin so ROUTES equals the two existing keys plus the new report route key (keep every other assertion in the file as it is), and say in the record's notes that you did. Your inherited state: your two commits on this branch (the row and the failed criteria output) stay; proceed with the build from the start of the face.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB200-2-AC1" cell_refs="IB-pr-554"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-2-AC1</invocation><expect>IB200-2-AC1 PASS</expect></criterion>
<criterion id="IB200-2-AC2" cell_refs="IB-pr-554"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-2-AC2</invocation><expect>IB200-2-AC2 PASS</expect></criterion>
<criterion id="IB200-2-AC3" cell_refs="IB-pr-554"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-2-AC3</invocation><expect>IB200-2-AC3 PASS</expect></criterion>

<expected_criteria>IB200-2-AC1, IB200-2-AC2, IB200-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 10) and the existing entry and summary tests pass; AC2 with every FILLED-REPORT-B block removed in memory from entry.py the new tests FAIL on assertions (the uncovered-viewer refusal is gone); AC3 the record: the worker's own product paths exactly as recorded and inside the grant (entry.py, api.tf and the new test among them), no typed object address, the four negative tests listed and present by name in the test file, the route template in entry.py and in api.tf, exactly one new aws_apigatewayv2_route resource, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent;** no AWS call is needed (all storage and scope are stubs). The Terraform edit is a repository file only: no `terraform plan`, `apply` or `safe-apply` is run.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a Terraform plan or apply; a change to an existing route or an IAM statement; a change that breaks an existing entry or summary test and cannot be made additive; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W398-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_entry.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~398/
infra/aws/lambda/investor-reporting/reporting/entry.py
infra/aws/terraform/investor-reporting/reporting-read/api.tf
infra/aws/terraform/investor-reporting/reporting-read/locals.tf
infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_filled_report.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 194 (round 2, workstream ~PS), cell `IB-pr-554`.
<owned_cells>IB-pr-554</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB200-2-AC1, IB200-2-AC2, IB200-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~398/IRPT_BCKEND.TO-IB-pr-554.hop-3-report-route-scope-check-and-declaration.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files (a lambda module and a Terraform declaration) and writes tests and one record; nothing is deployed or applied, so no route exists and no served byte moves; the deploy is a later WORLD act under the signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed or added (packet section 4: the invoke grant and the platinum read grant already cover the new path).
comp-routes: RUN -- the order DECLARES one new GET route in a repository Terraform file and in the lambda's ROUTES map; nothing is applied; the existing summary and account routes are untouched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB200-2 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; ten negatives on this cell, each failing its own arm: a failing test, too few tests, no marker block, a marker removal that breaks import, a weak test file, a stray path, a record that disagrees with the commits, a missing negative test by name, two new route resources, a missing route template.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~398` (worktree `C:/dev/wk-IRPT_BCKEND-398`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is code, tests and a Terraform declaration in the repository; no deploy, no apply).
</preflight>
