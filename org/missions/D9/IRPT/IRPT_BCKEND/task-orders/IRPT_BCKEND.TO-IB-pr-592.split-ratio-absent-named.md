# TO IRPT_BCKEND.TO-IB-pr-592 -- The served manifest NAMES each ratio-absent split security by security and day (CTO half of the 49 Financial split pair, condition 3): the ratio_absent list in the frame attrs and the run manifest, grading unchanged

<to_id>IRPT_BCKEND.TO-IB-pr-592</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~432</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO half of the 49 Financial split pair (@ab04a4b5a2, condition 3: the manifest names the ratio-absent days by security and day) | **Decomp cell:** `IB-pr-592` (decomposition section 220) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-432`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~432 <0.9.0_WK_IRPT_BCKEND~432@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-592` (inlined).** The CTO signed the 49 Financial split pair (half @ab04a4b5a2) on the condition (its item 3) that **the 13 ratio-absent security-days stay ungraded AND "the served manifest names them by security and day. They are never silent."** The build of IB-pr-578 and 583 records only COUNTS in the run manifest's `split_adjust` block (`securities_ratio_absent`, `days_ratio_absent`, `unkeyed_split_rows`, `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` near lines 880 to 905: `_split_attrs` and `_split_adjust_manifest`). That does not meet the condition. This cell adds the NAMES, LOCAL, offline, with tests. Grading is NOT changed.

**READ FIRST (named files only):** `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (the `SPLIT-ADJUST-A` and `SPLIT-ADJUST-B` blocks: `measure_split_ratios` (returns a result per split security: status, ratio, accounts_used), `_split_ratios_for_day`, `_split_attrs`, `_split_adjust_manifest`, the `_frame_for` block that sets `frame.attrs["split_adjust"]`, and where the manifest is built from the frames), and the tests `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py` and `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_unkeyed.py` (how a day is driven offline: mirror it in YOUR new test file; never edit them).

**Change** (all new logic inside `# BEGIN SPLIT-ADJUST-C` ... `# END SPLIT-ADJUST-C` lines; the module must import with the blocks removed): (1) `_split_attrs` also carries `ratio_absent`: a list, one entry per split security of the day whose status is `SPLIT_RATIO_ABSENT`, `{"day": "<the day>", "security": "<the security key as the producer keys it: the entry's identifier chain value>", "accounts_used": <n>}`; (2) a day with `unkeyed_split_rows` above zero also contributes ONE entry `{"day": "<the day>", "security": null, "accounts_used": 0, "reason": "UNKEYED_SPLIT_ROW", "unkeyed_split_rows": <n>}`; (3) the run manifest's `split_adjust` block gains `ratio_absent`: the entries of every day of the run, sorted by day then security (a null security sorts last), and nothing else in the block changes (every existing key keeps its name and meaning). A run with no ratio-absent security produces `ratio_absent: []`. The list holds NO account identifier and no quantity or value.

**Write the tests** `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_ratio_absent_named.py` (at least 8 tests; synthetic securities, accounts and values; mirror `test_split_adjust.py`): `test_manifest_names_each_ratio_absent_security_by_day`, `test_ratio_absent_entry_carries_day_security_and_accounts_used`, `test_no_ratio_absent_leaves_the_manifest_list_empty`, `test_list_is_sorted_by_day_then_security`, `test_unkeyed_rows_are_listed_by_day_without_a_security`, `test_existing_manifest_keys_unchanged`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~432/IB225-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["manifest_names_each_ratio_absent_security_by_day","ratio_absent_entry_carries_day_security_and_accounts_used","no_ratio_absent_leaves_the_manifest_list_empty","list_is_sorted_by_day_then_security","unkeyed_rows_are_listed_by_day_without_a_security","existing_manifest_keys_unchanged"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `SPLIT-ADJUST-C` block IN MEMORY from `holdings_performance.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB225-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB225-1-AC1" cell_refs="IB-pr-592"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r225/p225_cells.py" . IB225-1-AC1</invocation><expect>IB225-1-AC1 PASS</expect></criterion>
<criterion id="IB225-1-AC2" cell_refs="IB-pr-592"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r225/p225_cells.py" . IB225-1-AC2</invocation><expect>IB225-1-AC2 PASS</expect></criterion>
<criterion id="IB225-1-AC3" cell_refs="IB-pr-592"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r225/p225_cells.py" . IB225-1-AC3</invocation><expect>IB225-1-AC3 PASS</expect></criterion>

<expected_criteria>IB225-1-AC1, IB225-1-AC2, IB225-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 8) and the existing tests named in the paths block pass; AC2 with the SPLIT-ADJUST-C blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the producer file and the tests named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W432-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_ratio_absent_named.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_unkeyed.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_performance.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-592.split-ratio-absent-named.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~432/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 220 (round 1, workstream ~PM), cell `IB-pr-592`.
<owned_cells>IB-pr-592</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB225-1-AC1, IB225-1-AC2, IB225-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~432/IRPT_BCKEND.TO-IB-pr-592.split-ratio-absent-named.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file and adds tests in the repository; nothing is deployed or run against a served prefix, so no served byte moves; the release is the split pair's Act 1 and carries a rebuilt candidate (the digest in the pair changes and its COO half is re-issued).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p225_cells.py IB225-1 dry-run at base on dell2 2026-10-15 ~17:0xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~432` (worktree `C:/dev/wk-IRPT_BCKEND-432`). Class LOCAL.
</preflight>
