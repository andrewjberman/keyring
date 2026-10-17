# TO IRPT_BCKEND.TO-IB-pn-3 -- Every boto3 client of the Scope account feed names its region (IB2 msg 10539: NoRegionError on the runner)

<to_id>IRPT_BCKEND.TO-IB-pn-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~481</issued_to>
<issued_by>2.0.0_SA_COO~N2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `0.7.0_AE_CloudOps~IB2` msg 10539 (the first scheduled chain after the corrected apply) | **Decomp cell:** `IB-pn-3` (`IRPT_BCKEND_DECOMP_R5_N.md`) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-481`, cut from the current branch by the issuer (sparse: `data/inf/manual_api/`, `data/inf/scripts/gold/`, `data/inf/scripts/silver/`, `data/inf/scripts/bronze/`, `lib/`, `.tools/` and the project folder are present; if a test import fails for a missing directory, run `git sparse-checkout add <that directory>` locally and never commit it). Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~481 <0.9.0_WK_IRPT_BCKEND~481@opal.agent>" -F <msgfile> -- <explicit paths>` (message file written by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit (the runner runs Python 3.9, so no `X | Y` type unions and no `match`). No typed bucket name, `s3://` address or key prefix in a product file.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array. Row ids are `IRPT_BCKEND-D2-W481-S<k>` (start at 1); `surfaced_at` = `date -u +%FT%TZ` at filing.

**Cell `IB-pn-3` (inlined).** The Scope account feed `data/inf/manual_api/pull_inflection_scope_account_returns.py` runs on the chain's runner as `/tmp/orion_gold_scripts/pull_inflection_scope_account_returns.py`. Its second scheduled run (the 11:33Z chain on 2026-10-17) exited 1 after 1.6 s: `botocore.exceptions.NoRegionError` at line 327, `boto3.client("secretsmanager")` inside `session_token()`. The runner sets no default AWS region, so a client built without `region_name` cannot resolve one. The feed's other client, line 579, already names `region_name="us-east-1"`, as does every client in `data/inf/manual_api/jwt_freshness.py`. No Orion request was made. The step has now failed at import, then at its first client, and has never reached Orion: this cell must also prove, in the repository, that nothing else in the step's own path depends on the runner's environment.

**The change (the minimum):**
1. Line 327 becomes `boto3.client("secretsmanager", region_name="us-east-1")`, with a comment containing `RUNNER-REGION`.
2. Nothing else in the script changes unless your end-to-end test (below) finds another runner-only failure inside the script; fix that too, mark it `RUNNER-REGION` or `RUNNER-ENV`, and say so in the record. A failure whose fix lies outside the paths block is a BLOCKING row, not yours to fix.

**READ FIRST (named files only):** the feed script (whole), its four test files `data/inf/manual_api/test_pull_inflection_scope_account_returns.py`, `data/inf/manual_api/test_scope_feed_daily_factor.py`, `data/inf/manual_api/test_scope_feed_day_complete.py`, `data/inf/manual_api/test_scope_feed_runner_layout.py` (how the fake transport and fake S3 are built, and how the flat layout is built), `data/inf/manual_api/jwt_freshness.py` (how it names the region), and the check `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r3/pn_region_cells.py` (read it; do not edit it).

**Write the tests** `data/inf/manual_api/test_scope_feed_region.py` (at least 3 tests; no network; synthetic values; each builds and removes its own temp directories):
1. `test_every_boto3_construction_names_region_name`: parse the feed script with `ast`; every `boto3.client`, `boto3.resource` and `boto3.Session` call carries a `region_name` keyword.
2. `test_a_client_without_a_region_fails_in_the_scrubbed_environment_and_with_one_builds` (the control): in a subprocess with every `AWS_*` variable removed, `AWS_CONFIG_FILE` and `AWS_SHARED_CREDENTIALS_FILE` pointing at missing files and fake keys set, `boto3.client("secretsmanager")` raises `NoRegionError`, and `boto3.client("secretsmanager", region_name="us-east-1")` builds.
3. `test_run_end_to_end_in_the_flat_layout_under_the_scrubbed_environment`: copy the feed script, `INF_B_00.canonical_holdings.py` and every module the existing tests' flat-layout helper copies into a temp directory laid out as the runner's flat directory (script beside its dependencies, two ancestors is not required here), remove the `AWS_*` variables as in test 2, replace `botocore.client.BaseClient._make_api_call` for `secretsmanager` with a fake that returns a session token whose expiry is an hour ahead, and run the script's own `run` for ONE synthetic household with the existing fake transport and fake S3 helpers. It must reach an Orion request through the fake transport and write the day's two keys through the fake S3, with exit 0. If a runner-only difference stops it, that is the finding: fix it inside the script if it is a one-line environment assumption, else file a BLOCKING row naming it.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/IBN3-1_record.json`: `{"base_commit":"<40hex, git rev-parse HEAD at your start>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"tests_total":<n>,"tests_passed":<n>,"notes":["what each fact rests on and what you did not read; the sparse directories you added; whether test 3 found any further runner-only difference"],"aws_writes_made":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/IBN3-1_criteria_output.txt`, write the proof instance named under proof_of_spec (it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R5_N.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`) and validate it with `python .tools/proof-of-spec-check.py <instance>`. Commit with explicit paths (script, tests, record and criteria output first; then set the instance's artifact rows to that commit and commit the instance alone in a second commit, flipping the order `complete` only when every criterion passes). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IBN3-1-AC1" cell_refs="IB-pn-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r3/pn_region_cells.py" . IBN3-AC1</invocation><expect>IBN3-AC1 PASS</expect></criterion>
<criterion id="IBN3-1-AC2" cell_refs="IB-pn-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r3/pn_region_cells.py" . IBN3-AC2</invocation><expect>IBN3-AC2 PASS</expect></criterion>
<criterion id="IBN3-1-AC3" cell_refs="IB-pn-3"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r3/pn_region_cells.py" . IBN3-AC3</invocation><expect>IBN3-AC3 PASS</expect></criterion>

<expected_criteria>IBN3-1-AC1, IBN3-1-AC2, IBN3-1-AC3</expected_criteria>

What the checks grade: AC1 `session_token()` builds its real boto3 client in the flat layout with no region available and returns (no network); AC2 every boto3 construction in the script names `region_name`; AC3 the new tests (at least 3, including the end-to-end one) and the feed's five existing test files pass and your record names only paths inside the grant. AC1 and AC2 fail at the base (the difference control); do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and a scratch directory outside the repository. LOCAL build: you write the feed script, the new test file and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.

<paths>
data/inf/manual_api/pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_region.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pn-3.scope-feed-region.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R5_N.md</decomp_doc> round 5, workstream ~PN, cell `IB-pn-3`.
<owned_cells>IB-pn-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBN3-1-AC1, IBN3-1-AC2, IBN3-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/IRPT_BCKEND.TO-IB-pn-3.scope-feed-region.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository script (one argument on one client) and adds one test file; nothing is deployed or run against Orion or S3, so no served byte moves. The runner's copy changes only at a later WORLD apply under its own addendum.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- pn_region_cells.py dry-run at base on dell2 2026-10-17 ~12:3xZ: AC1 FAIL (botocore NoRegionError, the production error), AC2 FAIL (line 327 boto3.client has no region_name), AC3 FAIL (new test file absent). Positive control: the one-token fix applied in a temp copy of the four code folders: AC1 PASS, AC2 PASS.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~481` (worktree `C:/dev/wk-IRPT_BCKEND-481`). Class LOCAL.
authority: workstream ~PN is this seat's under the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1; write surface `data/inf/manual_api/` is named there.
</preflight>
