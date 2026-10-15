# TO IRPT_BCKEND.TO-IB-pr-583 -- A split row with no key at all makes the day SPLIT_RATIO_ABSENT and is counted, never skipped silently: the unkeyed split rows in the frame attrs and the run manifest

<to_id>IRPT_BCKEND.TO-IB-pr-583</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~425</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PK</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8359 item 3 (CVO v120; row W421-S2) | **Decomp cell:** `IB-pr-583` (decomposition section 215) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-425`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~425 <0.9.0_WK_IRPT_BCKEND~425@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Cell `IB-pr-583` (inlined).** IB-pr-578 (merged @07f60f52f3) split-adjusts the 49 Financial holdings price return in `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`. A split row of the day's transactions is keyed by the entry's `identifier_columns` chain (cusip, then ticker_symbol). The CTO ruled (msg 8359 item 3, from row W421-S2): a blank cusip falls back to the security's other key; if NONE exists, the day is `SPLIT_RATIO_ABSENT` and it never skips silently. Today `_split_ratios_for_day` drops a split row whose chain is empty (`secs = sorted({s for s in split_sec if s})`): such a row is skipped without a trace. This cell closes that, LOCAL, offline, with tests.

**READ FIRST (named files only):** `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (the `SPLIT-ADJUST-A` blocks: `_split_ratios_for_day`, `measure_split_ratios`, `_split_attrs`, `_split_adjust_manifest`, the `_frame_for` block that reads the day's transactions and sets `frame.attrs`, `SPLIT_REASONS`, `identifier()`), `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (the first entry's `split_adjust` and `identifier_columns`) and `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py` (how a day is driven offline: mirror it in YOUR new test file, never edit the existing tests).

**Change (all new logic inside `# BEGIN SPLIT-ADJUST-B` ... `# END SPLIT-ADJUST-B` lines; the module must stay importable with the blocks removed):** (1) the key of a split row is the FIRST non-empty value of the entry's `identifier_columns` chain (already so; keep it, and add a test that a blank cusip with a ticker matches by ticker). (2) A split row on the day whose chain is EMPTY (no key at all) is counted as an `unkeyed_split_rows` for that day. (3) When `unkeyed_split_rows` is above zero the day carries `split_ratio_absent_day = True` in `frame.attrs["split_adjust"]` and `unkeyed_split_rows = n`; the keyed securities of the day are adjusted exactly as today (an unkeyed row never adjusts any security, and never changes a keyed security's ratio). (4) The run manifest's `split_adjust` block gains `days_ratio_absent` (the number of days with `unkeyed_split_rows` above zero) and `unkeyed_split_rows` (summed over days), and its `reason_codes` text for `SPLIT_RATIO_ABSENT` says that a split row with no key makes the day ratio-absent. A run in which no day has an unkeyed row produces the same manifest values as today for every existing key, and two new keys at zero. Grading is NOT changed by this cell (no account status moves because of an unkeyed row): the count is the visibility the CTO asked for, and the served effect is the CTO's to rule from the DELTA.

**Write the tests** `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_unkeyed.py` (at least 9 tests; synthetic cusips, tickers, accounts and values, tiny frames): `test_unkeyed_split_row_marks_the_day_ratio_absent_and_counts`, `test_blank_cusip_falls_back_to_ticker`, `test_no_key_at_all_never_skips_silently`, `test_keyed_rows_unchanged_when_no_unkeyed_row`, `test_manifest_counts_unkeyed_split_rows`, `test_unkeyed_row_does_not_adjust_a_keyed_security`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~425/IB219-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["unkeyed_split_row_marks_the_day_ratio_absent_and_counts","blank_cusip_falls_back_to_ticker","no_key_at_all_never_skips_silently","keyed_rows_unchanged_when_no_unkeyed_row","manifest_counts_unkeyed_split_rows","unkeyed_row_does_not_adjust_a_keyed_security"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `SPLIT-ADJUST-B` block IN MEMORY from the product file and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB219-2_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB219-2-AC1" cell_refs="IB-pr-583"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py" . IB219-2-AC1</invocation><expect>IB219-2-AC1 PASS</expect></criterion>
<criterion id="IB219-2-AC2" cell_refs="IB-pr-583"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py" . IB219-2-AC2</invocation><expect>IB219-2-AC2 PASS</expect></criterion>
<criterion id="IB219-2-AC3" cell_refs="IB-pr-583"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py" . IB219-2-AC3</invocation><expect>IB219-2-AC3 PASS</expect></criterion>

<expected_criteria>IB219-2-AC1, IB219-2-AC2, IB219-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 9) and the existing tests named in the paths block pass; AC2 with the SPLIT-ADJUST-B blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the files named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W425-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_unkeyed.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_performance.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-583.split-unkeyed.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~425/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 215 (round 1, workstream ~PK), cell `IB-pr-583`.
<owned_cells>IB-pr-583</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB219-2-AC1, IB219-2-AC2, IB219-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~425/IRPT_BCKEND.TO-IB-pr-583.split-unkeyed.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file and adds tests in the repository; nothing is deployed or run against a served prefix, so no served byte moves; the release is a later act under the never-widen pairs.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p219_cells.py IB219-2 dry-run at base on dell2 2026-10-15 ~15:0xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~425` (worktree `C:/dev/wk-IRPT_BCKEND-425`). Class LOCAL.
</preflight>
