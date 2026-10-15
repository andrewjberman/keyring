# TO IRPT_BCKEND.TO-IB-pr-558 -- BUILD the export freeze on the route's ONE named-account reader (a shared module), with its own negative test: a document naming one account outside scope is refused at the freeze (serve-path pair, round 3)

<to_id>IRPT_BCKEND.TO-IB-pr-558</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~402</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_PS_ROUND_3_20261015.md` (msg 8058, @a4718eab10; the CVO's L10 slug ADJUDICATION_v102) | **Decomp cell:** `IB-pr-558` (decomposition section 196) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-402`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~402 <0.9.0_WK_IRPT_BCKEND~402@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch402/`).

**Cell `IB-pr-558` (inlined).** The signed pair's scope rule names EVERY account the filled document names (`household.accounts` plus the account-keyed `by_row` keys). Round 2 built that reader INSIDE `reporting/entry.py` for the route (`_filled_named_accounts` and `_by_row_keys`); the export freeze built in `IB-pr-555` gates on `household.accounts` only (row `IRPT_BCKEND-D2-W399-S2`). The CTO ruled (round 3): the export freeze uses the SAME reader as the route, so the rule is written ONCE, and the export path gets its own negative test; a freeze that scopes narrower than the route is a widening. READ FIRST: `reporting/entry.py` (`_by_row_keys`, `_filled_named_accounts`, `serve_filled_report`; they use `_ids.is_issued`), `reporting/tests/test_reporting_filled_report.py` (its tests exercise the reader through the route), `export/retained_export.py` and `export/bundle.py` (the `filled_report` freeze built in IB-pr-555 and where it scopes), `export/tests/test_filled_report_source.py`, and how the export package finds shared code (`retained_export.py` already puts the sibling `_scope`, `_ids`, `_authz`, `_keys` directories of `infra/aws/lambda/investor-reporting/` on `sys.path`; `entry.py` does the same).

**Change:** (1) NEW module `infra/aws/lambda/investor-reporting/_scope/filled_named_accounts.py` that defines `filled_named_accounts(document, is_issued_account)` (the reader moved verbatim in behaviour: every `household.accounts[].account_id`, each `by_row` key that `is_issued_account` accepts, a raw or malformed key returns None so the request is refused, an asset-class key names no account, a document with no account named raises the same refusal the route raised); the module is imported by NAME with `import filled_named_accounts as _fna` and called as `_fna.filled_named_accounts(...)` INSIDE function bodies (no `from ... import` of the function and no module-level use), so that removing the marked blocks leaves every module importable. (2) `reporting/entry.py` imports the module and its `serve_filled_report` calls the shared reader (pass `_ids.is_issued` as the predicate, keep every behaviour and every message); the inline `_filled_named_accounts` and `_by_row_keys` are DELETED from entry.py (the reader is defined exactly once). (3) The export freeze (`retained_export.py`, or `bundle.py` where the freeze scopes) calls the SAME shared reader on the filled document and refuses the freeze when any named account is outside the viewer's permitted set, with the same refusal class the freeze already uses. Existing behaviour is unchanged; update the existing tests only where they reached the moved private names (`test_reporting_filled_report.py`, `test_filled_report_source.py` are in your grant).

**The difference control (criterion 2).** Wrap the NEW logic in `# BEGIN FILLED-REPORT-D` ... `# END FILLED-REPORT-D` lines in the shared module (the function body) and in `retained_export.py` (the freeze's scope call). The check removes every such block IN MEMORY and runs YOUR new test file `infra/aws/lambda/investor-reporting/export/tests/test_filled_report_freeze_scope.py`: it must then FAIL on ASSERTIONS, not on an import or collection error (so keep the module-level code outside the blocks, as above, and reference new names only inside test functions).

**Write the tests** `infra/aws/lambda/investor-reporting/export/tests/test_filled_report_freeze_scope.py` (at least 6 tests; stubs; synthetic ids): a document whose account-keyed `by_row` names ONE account outside the viewer's scope is refused at the freeze (name the test `test_export_freeze_refuses_uncovered_account`), a document naming only covered accounts freezes, an asset-class `by_row` key names no account, a raw or malformed key refuses, `household.accounts` alone out of scope refuses, and the freeze and the route give the SAME answer for the same document and the same scope (call both on one fixture).

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~402/IB201-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[the product paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["export_freeze_refuses_uncovered_account"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; say whether the export package build includes the _scope directory"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB201-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB201-2-AC1" cell_refs="IB-pr-558"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py" . IB201-2-AC1</invocation><expect>IB201-2-AC1 PASS</expect></criterion>
<criterion id="IB201-2-AC2" cell_refs="IB-pr-558"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py" . IB201-2-AC2</invocation><expect>IB201-2-AC2 PASS</expect></criterion>
<criterion id="IB201-2-AC3" cell_refs="IB-pr-558"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py" . IB201-2-AC3</invocation><expect>IB201-2-AC3 PASS</expect></criterion>

<expected_criteria>IB201-2-AC1, IB201-2-AC2, IB201-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 6) and the existing route, entry and export tests pass; AC2 with every FILLED-REPORT-D block removed in memory from the shared module and the freeze the new tests FAIL on assertions; AC3 the record: the worker's own paths exactly as recorded and inside the grant, the reader `def filled_named_accounts(` defined exactly once and in the shared module, imported by entry.py and by the export freeze, the inline copy gone from entry.py, the negative test `export_freeze_refuses_uncovered_account` listed and present by name, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent;** no AWS call is needed (all storage and scope are stubs).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a change in the route's behaviour or messages; a freeze that scopes narrower than the route; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W402-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~402/
infra/aws/lambda/investor-reporting/_scope/filled_named_accounts.py
infra/aws/lambda/investor-reporting/reporting/entry.py
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_freeze_scope.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_source.py
infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_filled_report.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 196 (round 3, workstream ~PS), cell `IB-pr-558`.
<owned_cells>IB-pr-558</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB201-2-AC1, IB201-2-AC2, IB201-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~402/IRPT_BCKEND.TO-IB-pr-558.export-freeze-on-the-shared-named-account-reader.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files in two lambda packages and a shared module and writes tests and one record; nothing is deployed, so no served byte moves; the deploy legs wait on 49 Financial gold for one date (CTO msg 7995).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched or added; the existing filled-report route keeps its behaviour.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB201-2 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; eight negatives on this cell, each failing its own arm: a weak test file, no marker block, a stray path, the inline copy staying in entry.py, no entry import, no freeze import, a second definition of the reader, no negative test by name.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~402` (worktree `C:/dev/wk-IRPT_BCKEND-402`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is repository edits and tests; no deploy).
</preflight>
