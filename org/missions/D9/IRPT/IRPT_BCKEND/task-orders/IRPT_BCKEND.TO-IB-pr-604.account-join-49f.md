# TO IRPT_BCKEND.TO-IB-pr-604 -- Fix the 49 Financial account join: the account the candidate drops although the source reports it with positions is kept; the guard unchanged (CTO ruling @334382c7f4 item 1, msg 8527; IB-pr-602's finding)

<to_id>IRPT_BCKEND.TO-IB-pr-604</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~440</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round analysis msg 8527 item 1 and ADDENDUM 1 @334382c7f4 (cut the join cell only for what still trips: one account, cause join, on the transplant tree) | **Decomp cell:** `IB-pr-604` (decomposition section 229) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-440`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~440 <0.9.0_WK_IRPT_BCKEND~440@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/ data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-604` (inlined).** IB-pr-602 (record `deliverables/0.9.0_WK_IRPT_BCKEND~437/IB233-1_49f_transplant_reread.json`, merged @98bfeea0f2) re-measured 49 Financial on the TRANSPLANT tree (pin 1 plus the exemption): `classified_security_lost` no longer trips (0 of 1,839), but `account_lost` still trips on ONE of 7,640 served accounts: the source still reports it WITH positions (class `in_source_with_positions`, cause `join`, the exemption cannot clear it) and our candidate drops it. The CTO's ruling (@334382c7f4 item 1, msg 8527): **fix the join, not the guard**: find the key the candidate drops the account on (a type, a padding or a firm-scope key) and fix it, with a test that has that account's shape using SYNTHETIC ids; the guard's threshold is unchanged. Two held rows ride in the same cell: W426-S2 (a false-fail on a closed account) becomes a NEGATIVE test, and W426-S3 (the build module prints tickers to the console) becomes one line: the build prints counts only. LOCAL, code and tests, nothing run against AWS writes.

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`build_snapshot`, the account and position joins, the scope account ids, `evaluate_publish_gate` near line 3076 for the `account_lost` branch, `closed_account_ids`), the driver of IB-pr-602 `deliverables/0.9.0_WK_IRPT_BCKEND~437/IB233-1_49f_transplant_reread_harness.py` (it builds the 49 Financial candidate once and classifies the lost accounts; reuse its set-up lines in a COPY under your own deliverables folder, do not edit it), and the existing tests `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py`, `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py`, `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py`.

**Do:**
1. **Find the drop, in process, READ ONLY.** Run your copy of the driver so that it builds the candidate and prints, for the ONE lost account of class `in_source_with_positions`, NOT its id but WHICH STAGE of the build loses it (the first stage where it is present in the source rows and absent from the output) and which KEY it differs on from the rows that survive (its type, its padding or case, or its firm-scope key), as a category and a length only. Record the stage name and the key category in the record's notes. Ids, tickers and values go nowhere: no tracked file, no log.
2. **Fix the join** inside `# BEGIN ACCOUNT-JOIN-A` ... `# END ACCOUNT-JOIN-A` lines in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the module must import with the blocks removed, and with them removed the old behaviour stands: the difference control). The fix is a normalization of that key at the join (or the narrowest correction the stage allows); it does not touch `evaluate_publish_gate`'s thresholds or conditions, and it must not change any other account's rows (the test proves it on a synthetic set). Do NOT touch the `ABSENT-AT-SOURCE` or `SPLIT-ADJUST` blocks, and leave the one-date bypass alone.
3. **The console line (W426-S3):** where the build module prints a security identifier or an account identifier to the console, print the count instead; a test proves the printed output of a build over a synthetic set holds no identifier.
4. **Write the tests** `data/assets/scripts/gold/investor_reporting/tests/test_account_join.py` (at least 6 tests; synthetic ids; no AWS, no network): `test_account_dropped_on_the_join_key_is_kept`, `test_closed_account_absent_from_source_is_not_a_false_fail`, `test_other_accounts_are_unchanged`, `test_the_guard_threshold_is_unchanged`, `test_the_build_prints_counts_only`. `account_dropped_on_the_join_key_is_kept`: a synthetic source set where one account carries the key shape you found (a type, padding, case or scope-key difference) and positions above zero; before the fix it is dropped, after it is kept. `closed_account_absent_from_source_is_not_a_false_fail`: a synthetic account the directory closes and the source no longer reports is not counted lost and does not trip `account_lost`. `other_accounts_are_unchanged`: every other synthetic account's rows are byte-equal with and without the fix. `the_guard_threshold_is_unchanged`: the gate still refuses a synthetic lost account that is neither closed nor exempted, exactly as at the base.
5. If you cannot find the stage or the key, STOP on that part, file a row with what you ruled out (stage names only), and write what you have; the check then fails honestly; never estimate and never loosen the guard.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~440/IB235-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["account_dropped_on_the_join_key_is_kept","closed_account_absent_from_source_is_not_a_false_fail","other_accounts_are_unchanged","the_guard_threshold_is_unchanged","the_build_prints_counts_only"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `ACCOUNT-JOIN-A` block IN MEMORY from `holdings_snapshot.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB235-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB235-1-AC1" cell_refs="IB-pr-604"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py" . IB235-1-AC1</invocation><expect>IB235-1-AC1 PASS</expect></criterion>
<criterion id="IB235-1-AC2" cell_refs="IB-pr-604"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py" . IB235-1-AC2</invocation><expect>IB235-1-AC2 PASS</expect></criterion>
<criterion id="IB235-1-AC3" cell_refs="IB-pr-604"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py" . IB235-1-AC3</invocation><expect>IB235-1-AC3 PASS</expect></criterion>

<expected_criteria>IB235-1-AC1, IB235-1-AC2, IB235-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 6) and the existing tests named in the paths block pass; AC2 with the ACCOUNT-JOIN-A blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write `holdings_snapshot.py`, the tests named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W440-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_account_join.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-604.account-join-49f.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~440/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 229 (round 3, workstream ~PL), cell `IB-pr-604`.
<owned_cells>IB-pr-604</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB235-1-AC1, IB235-1-AC2, IB235-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~440/IRPT_BCKEND.TO-IB-pr-604.account-join-49f.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository module and its tests; nothing is deployed, minted or written to AWS; the join fix reaches a served byte only through a later holdings release (the exemption pair's transplant candidate is rebuilt with this commit added, a separate read cell).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p235_cells.py IB235-1 dry-run at base on dell2 2026-10-15 ~20:0xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; the negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~440` (worktree `C:/dev/wk-IRPT_BCKEND-440`). Class LOCAL.
</preflight>
