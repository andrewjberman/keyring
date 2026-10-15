# TO IRPT_BCKEND.TO-IB-pr-594 -- The Scope account feed stores the DAILY FACTOR only, admits SERIES_ENDED_AT_SOURCE and walks calendar days with a scheduled window from the newest landed day (CTO msg 8484, round-118 ADDENDUM 3)

<to_id>IRPT_BCKEND.TO-IB-pr-594</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~433</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8484 (round-118 ADDENDUM 3: store the daily factor only; SERIES_ENDED_AT_SOURCE admitted, for the scheduled feed too; chain calendar days) on B-IN's round-122 probe | **Decomp cell:** `IB-pr-594` (decomposition section 221) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-433`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~433 <0.9.0_WK_IRPT_BCKEND~433@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/inf/manual_api/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-594` (inlined).** IB-pr-586 (merged @7b150e672a) built the Orion Scope account feed `data/inf/manual_api/pull_inflection_scope_account_returns.py`. B-IN's history probe (`2.0.0_SA_COO~I2`, packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND122_BIN_DRAIN_END_20261015.md`) and the CTO's ruling (msg 8484, round-118 ADDENDUM 3) fix four things the build must do, LOCAL, offline, with tests: (1) **store the DAILY FACTOR only**: Orion's series points are calendar-day and contiguous from each account's start; the chained factors equal Orion's period return up to a year, and Orion annualizes its summary over a year, so a stored summary is wrong: the silver row's value column is the point's daily `factor`, and the summary `performance` is never stored; (2) **`SERIES_ENDED_AT_SOURCE` is admitted**: an account whose series ends before the window's end gets, for each day after its last point, an `ABSENT` row with that reason class (claim `measured`: this call observed it), never a zero and never a fill; (3) **calendar days, weekends included**: the rows chain by calendar day; (4) the scheduled run (no `--from-date`) takes a calendar-day window from the day AFTER the newest landed silver partition through the pull date, capped at 10 calendar days back (so a Monday run also carries the weekend); when nothing has landed the window is the pull date alone.

**READ FIRST (named files only):** `data/inf/manual_api/pull_inflection_scope_account_returns.py` (whole: `daily_points` near line 236, `classify` near 251 which today stores `return_value = performance / 100`, the window and universe code, the `--from-date` path, the write path), its test `data/inf/manual_api/test_pull_inflection_scope_account_returns.py` (19 tests), the probe record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~308/` (find the record there by name; counts only; it shows the series shape: names `factor`, `performance`, `startDate`, `endDate`) and `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/ORION_PAIR_B_ADDENDUM_1_SCOPE_ACCOUNT_FEED.md` (sections 2 and 3).

**Change** (all new logic inside `# BEGIN SCOPE-FEED-B` ... `# END SCOPE-FEED-B` lines; the module must import with the blocks removed; the existing coverage rule, reason classes `NO_GROUP`, `GROUP_NO_SERIES`, `NO_START_DATE_AT_SOURCE`, the fee basis and the write path stay): (1) the silver value column `return_value` becomes `daily_factor` = the point's `factor` as a float (null on an ABSENT row); the column `return_value` and any summary are gone from the silver schema and from the bronze envelope's row summaries; update ONLY the assertions of the existing feed test that name `return_value` (that one rename is the only edit allowed there). (2) After the last point of an account's series, each later day of the window gets an `ABSENT` row, reason `SERIES_ENDED_AT_SOURCE`, claim `measured`, cause null. A group with no series at all stays `GROUP_NO_SERIES`. (3) A non-trading calendar day takes its universe from the previous trading day's held accounts. (4) The scheduled window as stated above (list the silver prefix's `date=` partitions the way the script already lists or heads keys; refuse with a message on a listing error: no silent single day).

**AMENDMENT 1 (issuer ruling on your row W433-S1).** The calendar-day chain applies to the `--from-date` (backfill) path TOO: CTO msg 8484 item 4 and pair (b) addendum 2 section 2 item 4 chain CALENDAR days, weekends included, for the one-time history run as for the scheduled one (B-IN's probe: the series are calendar-day and contiguous from each account's start). That supersedes my AMENDMENT 1 of IB-pr-586 (its sentence "a day that is not a trading day writes nothing"). So `--from-date` emits one row per account per CALENDAR day of the window (a non-trading day takes its universe from the previous trading day's held accounts; a day with no series point for an account whose series has ended is `SERIES_ENDED_AT_SOURCE`). The existing test that pins trading-day rows for `--from-date` is the ONE other assertion you may change in `test_pull_inflection_scope_account_returns.py` (to calendar-day rows); add the named test `test_from_date_window_emits_calendar_days_including_weekends`. Rows W433-S2 (the cap is 10 calendar days back from the pull date, 11 days inclusive) and S3 (a Monday run pulls Friday; the weekend arrives with Tuesday's pull date) are accepted as built.

**Write the tests** `data/inf/manual_api/test_scope_feed_daily_factor.py` (at least 12 tests; synthetic ids and a fake transport/S3, no network): `test_daily_factor_is_the_point_factor_and_the_return_column_is_gone`, `test_the_summary_performance_is_never_stored`, `test_series_ended_at_source_marks_days_after_the_last_point_absent`, `test_series_end_reason_claim_is_measured`, `test_calendar_days_include_weekends_in_the_window_and_the_rows`, `test_scheduled_window_starts_after_the_newest_landed_day_and_is_capped`, `test_first_run_window_is_the_pull_date_only`, `test_factor_chains_to_the_period_return_in_a_fixture`, `test_existing_reason_classes_unchanged`, `test_from_date_window_emits_calendar_days_including_weekends`. `factor_chains_to_the_period_return_in_a_fixture`: a fixture series of daily factors whose product equals the fixture's period return.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~433/IB227-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["daily_factor_is_the_point_factor_and_the_return_column_is_gone","the_summary_performance_is_never_stored","series_ended_at_source_marks_days_after_the_last_point_absent","series_end_reason_claim_is_measured","calendar_days_include_weekends_in_the_window_and_the_rows","scheduled_window_starts_after_the_newest_landed_day_and_is_capped","first_run_window_is_the_pull_date_only","factor_chains_to_the_period_return_in_a_fixture","existing_reason_classes_unchanged","from_date_window_emits_calendar_days_including_weekends"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `SCOPE-FEED-B` block IN MEMORY from the feed script and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB227-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB227-1-AC1" cell_refs="IB-pr-594"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r227/p227_cells.py" . IB227-1-AC1</invocation><expect>IB227-1-AC1 PASS</expect></criterion>
<criterion id="IB227-1-AC2" cell_refs="IB-pr-594"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r227/p227_cells.py" . IB227-1-AC2</invocation><expect>IB227-1-AC2 PASS</expect></criterion>
<criterion id="IB227-1-AC3" cell_refs="IB-pr-594"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r227/p227_cells.py" . IB227-1-AC3</invocation><expect>IB227-1-AC3 PASS</expect></criterion>

<expected_criteria>IB227-1-AC1, IB227-1-AC2, IB227-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 12) and the existing tests named in the paths block pass; AC2 with the SCOPE-FEED-B blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the feed script and the tests named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W433-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/inf/manual_api/pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_daily_factor.py
data/inf/manual_api/test_pull_inflection_scope_account_returns.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-594.scope-feed-daily-factor.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~433/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 221 (round 2, workstream ~PN), cell `IB-pr-594`.
<owned_cells>IB-pr-594</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB227-1-AC1, IB227-1-AC2, IB227-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~433/IRPT_BCKEND.TO-IB-pr-594.scope-feed-daily-factor.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository script and its tests; nothing is deployed, run against Orion or S3, so no served byte moves; the apply of the feed (CloudOps, after this merges) carries the changed script.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p227_cells.py IB227-1 dry-run at base on dell2 2026-10-15 ~17:4xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~433` (worktree `C:/dev/wk-IRPT_BCKEND-433`). Class LOCAL.
</preflight>
