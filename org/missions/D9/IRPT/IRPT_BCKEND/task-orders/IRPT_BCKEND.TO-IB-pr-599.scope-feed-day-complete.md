# TO IRPT_BCKEND.TO-IB-pr-599 -- The Scope account feed writes a day's keys ONLY when the day is complete (CTO msg 8536, item 4)

<to_id>IRPT_BCKEND.TO-IB-pr-599</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~436</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round analysis msg 8536 (item 4: write a day's key only when the day is complete, with a test) | **Decomp cell:** `IB-pr-599` (decomposition section 225) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-436`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~436 <0.9.0_WK_IRPT_BCKEND~436@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/inf/manual_api/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-599` (inlined).** The Scope account feed `data/inf/manual_api/pull_inflection_scope_account_returns.py` (IB-pr-586, amended by IB-pr-594) calls Orion once per household and today writes every day's bronze and silver keys from the households that answered, even when some household failed (`run`, inside the block `SCOPE-FEED-B`, the loop over `days` after the line `CALLS: ...`). A day written from a partial answer is read by every consumer as a complete day: its missing accounts look like accounts without a return. The CTO's round analysis (msg 8536, item 4) orders the rule: **a day's key pair is written ONLY when the day is complete.** LOCAL, offline, with tests.

**READ FIRST (named files only):** `data/inf/manual_api/pull_inflection_scope_account_returns.py` (whole; `run` near line 693, `write_day` near 443, `load_universe`), its tests `data/inf/manual_api/test_pull_inflection_scope_account_returns.py` and `data/inf/manual_api/test_scope_feed_daily_factor.py` (read how a fake transport and fake S3 are built there).

**Rule.** A day D is COMPLETE when every household that appears in `universe_by_day[D]` (before any `--max-households` cap) has outcome `OK` (an HTTP 200 body with no ambiguous account group). For a day that is not complete write NEITHER its bronze key NOR its silver key; for a complete day write both exactly as today. A day is judged on its own universe: a household with no account on day D does not block D. After the loop print one line `DAYS: complete=<n> skipped=<m>` and, per skipped day, `SKIPPED: <day> households_failed=<comma list of the household tokens that blocked it>` (tokens, never raw ids). The exit code is 0 when no day was skipped and 1 when any day was skipped. A 429 that persists still raises `_Stopped` before any write, unchanged. The bronze envelope of a complete day stays as it is. A rerun after a failed day recomputes the window from the newest landed day (IB-pr-594), so the skipped day is written by the rerun with no new code; the test proves it.

**Change.** All new logic inside `# BEGIN SCOPE-FEED-C` ... `# END SCOPE-FEED-C` lines placed INSIDE the `SCOPE-FEED-B` region (a new `_complete_days(days, universe_by_day, ok_hh)` helper and the edit `run` needs); the module must still import with the SCOPE-FEED-C blocks removed, and with them removed the old behaviour (partial days written) stands unchanged (the difference control). The two existing test files may change ONLY the assertions that assert a partial day is written after a failed household; say which in the record.

**Write the tests** `data/inf/manual_api/test_scope_feed_day_complete.py` (at least 7 tests; synthetic ids, a fake transport and S3, no network): `test_day_with_a_failed_household_writes_no_key`, `test_complete_day_writes_both_keys`, `test_failed_households_are_named_in_the_output_and_the_exit_is_nonzero`, `test_rerun_after_a_failed_day_writes_the_day`, `test_from_date_window_writes_only_complete_days`, `test_a_throttle_stop_writes_no_key_for_the_day`, `test_existing_behaviours_unchanged`. `from_date_window_writes_only_complete_days`: a three-day `--from-date` window in which one household fails writes no key for the days that household's accounts appear in and both keys for the other days. `existing_behaviours_unchanged`: a run with every household OK writes the same key set and bytes as before this cell.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~436/IB231-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["day_with_a_failed_household_writes_no_key","complete_day_writes_both_keys","failed_households_are_named_in_the_output_and_the_exit_is_nonzero","rerun_after_a_failed_day_writes_the_day","from_date_window_writes_only_complete_days","a_throttle_stop_writes_no_key_for_the_day","existing_behaviours_unchanged"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `SCOPE-FEED-C` block IN MEMORY from the feed script and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB231-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB231-1-AC1" cell_refs="IB-pr-599"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r231/p231_cells.py" . IB231-1-AC1</invocation><expect>IB231-1-AC1 PASS</expect></criterion>
<criterion id="IB231-1-AC2" cell_refs="IB-pr-599"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r231/p231_cells.py" . IB231-1-AC2</invocation><expect>IB231-1-AC2 PASS</expect></criterion>
<criterion id="IB231-1-AC3" cell_refs="IB-pr-599"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r231/p231_cells.py" . IB231-1-AC3</invocation><expect>IB231-1-AC3 PASS</expect></criterion>

<expected_criteria>IB231-1-AC1, IB231-1-AC2, IB231-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 7) and the existing tests named in the paths block pass; AC2 with the SCOPE-FEED-C blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the feed script, the tests named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W436-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/inf/manual_api/pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_day_complete.py
data/inf/manual_api/test_pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_daily_factor.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-599.scope-feed-day-complete.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~436/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 225 (round 3, workstream ~PN), cell `IB-pr-599`.
<owned_cells>IB-pr-599</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB231-1-AC1, IB231-1-AC2, IB231-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~436/IRPT_BCKEND.TO-IB-pr-599.scope-feed-day-complete.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository script and its tests; nothing is deployed, run against Orion or S3, so no served byte moves; the apply of the feed (IB-pr-596) carries the changed script.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p231_cells.py IB231-1 dry-run at base on dell2 2026-10-15 ~18:4xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp roots the run created itself: all three PASS; negatives each failing its own arm (0 unexpected).
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~436` (worktree `C:/dev/wk-IRPT_BCKEND-436`). Class LOCAL.
</preflight>
