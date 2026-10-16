# TO IRPT_BCKEND.TO-IB-pn-1 -- The Scope account feed script runs in the runner's flat layout (row IRPT_BCKEND-D2-S221)

<to_id>IRPT_BCKEND.TO-IB-pn-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~480</issued_to>
<issued_by>2.0.0_SA_COO~N2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** IB2's first-run read of IB-pr-596 (msg 9366) and row `IRPT_BCKEND-D2-S221` | **Decomp cell:** `IB-pn-1` (`IRPT_BCKEND_DECOMP_R4_N.md`) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-480`, cut from the current branch by the issuer (sparse: `data/inf/manual_api/`, `data/inf/scripts/gold/`, `data/inf/scripts/silver/`, `data/inf/scripts/bronze/`, `lib/`, `.tools/` and the project folder are present; if a test import fails for a missing directory, run `git sparse-checkout add <that directory>` locally and never commit it). Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~480 <0.9.0_WK_IRPT_BCKEND~480@opal.agent>" -F <msgfile> -- <explicit paths>` (message file written by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit (the runner runs Python 3.9, so no `X | Y` type unions and no `match`). No typed bucket name, `s3://` address or key prefix in a product file.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array. Row ids are `IRPT_BCKEND-D2-W480-S<k>` (start at 1); `surfaced_at` = `date -u +%FT%TZ` at filing.

**Cell `IB-pn-1` (inlined).** The Scope account feed `data/inf/manual_api/pull_inflection_scope_account_returns.py` is run on the chain's runner as `/tmp/orion_gold_scripts/pull_inflection_scope_account_returns.py`: the runner flattens every script of the S3 prefixes `code/gold/`, `code/manual_api/`, `code/silver/` and `code/bronze/` by basename into that one directory (`data/inf/scripts/gold/orion-gold-dispatch.sh`, `sync_scripts()`, lines 533-546). Its first scheduled run died at import: line 34, `_REPO_LIB = _HERE.parents[2] / "lib"`, raised `IndexError: 2` because `/tmp/orion_gold_scripts` has only two ancestors. A second statement assumes the repository layout too: line 71, `BUILDER_PATH = _HERE.parent / "scripts" / "gold" / "INF_B_00.canonical_holdings.py"`, names a directory that does not exist on the runner, where `INF_B_00.canonical_holdings.py` sits beside the script. Make the script run in BOTH layouts (the repository and the runner's flat directory), and change nothing else.

**The change (the minimum):**
1. `_REPO_LIB` is `_HERE.parents[2] / "lib"` when `len(_HERE.parents) > 2`, else `None`. The two places that insert it into `sys.path` (inside `_calendar` and `_builder`, near lines 384 and 395) skip the insert when it is `None`; `_calendar` still imports `trading_calendar` from the script's own directory first.
2. `BUILDER_PATH` is `_HERE / "INF_B_00.canonical_holdings.py"` when that file exists, else the repository path it names today.
3. Nothing else in the script changes: the request bodies, the `SCOPE-FEED-A/B/C` blocks, the exit codes, the day-complete rule and the daily factor stay byte for byte. Mark your edit with comments containing `RUNNER-LAYOUT`.

**READ FIRST (named files only):** the feed script (whole), its three test files `data/inf/manual_api/test_pull_inflection_scope_account_returns.py`, `data/inf/manual_api/test_scope_feed_daily_factor.py`, `data/inf/manual_api/test_scope_feed_day_complete.py` (how a fake transport and fake S3 are built), and the check `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r1/pn1_cells.py` (read it; do not edit it; it builds the flat layout from the four code folders and runs your script in it).

**Write the tests** `data/inf/manual_api/test_scope_feed_runner_layout.py` (at least 4 tests; no network; synthetic values): `test_module_executes_when_its_file_has_two_ancestors` (execute the script source with `__file__` set to `/orion_gold_scripts/pull_inflection_scope_account_returns.py` and the flat directory on `sys.path`, as the check does), `test_repo_lib_is_none_without_a_third_ancestor`, `test_source_prefixes_reads_the_builder_beside_the_script` (a temp flat directory holding the script, `INF_B_00.canonical_holdings.py` and the modules it imports, copied from the repository), `test_source_prefixes_falls_back_to_the_repository_path` (the repository layout still resolves). Each test builds its temp directories itself and cleans up.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~480/IBN1-1_record.json`: `{"base_commit":"<40hex, git rev-parse HEAD at your start>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"tests_total":<n>,"tests_passed":<n>,"notes":["what each fact rests on and what you did not read; the sparse directories you added"],"aws_writes_made":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~480/IBN1-1_criteria_output.txt`, write the proof instance named under proof_of_spec (it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R4_N.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`) and validate it with `python .tools/proof-of-spec-check.py <instance>`. Commit with explicit paths (script, tests, record and criteria output first; then set the instance's artifact rows to that commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IBN1-1-AC1" cell_refs="IB-pn-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r1/pn1_cells.py" . IBN1-AC1</invocation><expect>IBN1-AC1 PASS</expect></criterion>
<criterion id="IBN1-1-AC2" cell_refs="IB-pn-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r1/pn1_cells.py" . IBN1-AC2</invocation><expect>IBN1-AC2 PASS</expect></criterion>
<criterion id="IBN1-1-AC3" cell_refs="IB-pn-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r1/pn1_cells.py" . IBN1-AC3</invocation><expect>IBN1-AC3 PASS</expect></criterion>

<expected_criteria>IBN1-1-AC1, IBN1-1-AC2, IBN1-1-AC3</expected_criteria>

What the checks grade: AC1 the script source executes at module level with its file two directories below the root; AC2 in the flat layout `source_prefixes()` returns the bucket and the two prefixes; AC3 the new tests (at least 4) and the three existing feed test files pass and your record names only paths inside the grant. AC1 and AC2 fail at the base (the difference control); do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and a scratch directory outside the repository. LOCAL build: you write the feed script, the new test file and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check. If AC2 still fails after the two changes because the flat layout lacks a module that `INF_B_00.canonical_holdings.py` imports, that is a finding about the deployed code folders, not yours to fix: file a BLOCKING row naming the module and stop.

<paths>
data/inf/manual_api/pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_runner_layout.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pn-1.scope-feed-runner-layout.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~480/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R4_N.md</decomp_doc> round 4, workstream ~PN, cell `IB-pn-1`.
<owned_cells>IB-pn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBN1-1-AC1, IBN1-1-AC2, IBN1-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~480/IRPT_BCKEND.TO-IB-pn-1.scope-feed-runner-layout.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository script and adds one test file; nothing is deployed or run against Orion or S3, so no served byte moves. The runner's copy of the script changes only at a later WORLD apply under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- pn1_cells.py dry-run at base on dell2 2026-10-16 ~13:5xZ: AC1 FAIL (IndexError: 2), AC2 FAIL (FileNotFoundError on the sibling scripts/gold path), AC3 FAIL (new test file absent). Positive control: the two-change fix applied in a temp copy of the four code folders: AC1 PASS, AC2 PASS.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~480` (worktree `C:/dev/wk-IRPT_BCKEND-480`). Class LOCAL.
authority: workstream ~PN is this seat's under the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1; write surface `data/inf/manual_api/` is named there. IB-pr-596 stays issued by `2.0.0_SA_COO~P2`.
</preflight>
