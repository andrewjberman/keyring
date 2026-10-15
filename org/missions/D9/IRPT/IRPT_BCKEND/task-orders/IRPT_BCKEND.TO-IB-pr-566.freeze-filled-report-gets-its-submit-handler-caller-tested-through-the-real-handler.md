# TO IRPT_BCKEND.TO-IB-pr-566 -- BUILD the production caller of freeze_filled_report: the export submit path (PATH C) freezes the server-pinned filled report and serves it from the frozen row; tested through the real handler

<to_id>IRPT_BCKEND.TO-IB-pr-566</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~410</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-5 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_PO5_PS5_PY3_20261015.md` (@25f361860e, msg 8183), ~PS item 1 (W407-S1) | **Decomp cell:** `IB-pr-566` (decomposition section 203) | **outcome_ref:** FWD-2

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-410`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~410 <0.9.0_WK_IRPT_BCKEND~410@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.** Python: ASCII only in product code and logs; tests use synthetic ids and bytes.

**Client data rule:** counts, dates, hashes, commit ids, field names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch410/`).

**Cell `IB-pr-566` (inlined) -- W407-S1: `freeze_filled_report` gets its production caller.** Today `freeze_filled_report(body, permitted_account_ids, reader)` in `infra/aws/lambda/investor-reporting/export/retained_export.py` (server-pins the filled report, IB-pr-563) has NO production caller: the export submit path handles a retained report (PATH A) and a platinum series (PATH B) only. Ruling (CTO, call f50a): the export submit handler calls it, the server pins, and a test drives the REAL handler, not the function alone. PATH C = a body whose `filled_report_source` is a dict (`is_filled_report(body)`); the client id is the only input from the wire (`entry.py` `_page_pins_dropped` already drops page-sent pins at the call site).

**READ FIRST (named files only):** `infra/aws/lambda/investor-reporting/export/entry.py` (`submit_export`, near line 360, and where `ports` are composed, near line 405 where `platinum_series` is installed), `infra/aws/lambda/investor-reporting/export/submit_async.py` (`accept`, near line 113: PATH B freezes with `freeze_platinum`, builds the grant with `platinum_grant`, rides the frozen item on the marked event as `pinned_series`; `run`, the async leg), `infra/aws/lambda/investor-reporting/export/submit_service.py` (`serve_submit` and `_serve_platinum`, near lines 60 to 175: the PATH B twin that builds the bundle from the FROZEN row and never re-reads the current object), `infra/aws/lambda/investor-reporting/export/retained_export.py` (`freeze_filled_report`, `filled_row`, `read_pinned_filled`, `platinum_grant`, `platinum_print_query`, `FilledReportNotCovered`, `FilledReportUnavailable`, `FilledReportSourceRefused`), `infra/aws/lambda/investor-reporting/export/bundle.py` (the filled_report pin shape, lines 91 to 170) and the tests `infra/aws/lambda/investor-reporting/export/tests/test_export_path_b_route.py` (how PATH B is driven through the real handler with stub ports: mirror it), `test_filled_report_server_pin.py`, `test_filled_report_source.py`, `test_filled_report_freeze_scope.py`.

**Change (all new logic inside `# BEGIN FILLED-REPORT-F` ... `# END FILLED-REPORT-F` lines):** (1) in `submit_async.accept`, a PATH C branch before the PATH A resolve: when `_retained.is_filled_report(body)`, call `_retained.freeze_filled_report(body, permitted, ports["filled_reader"])` (the port is `ports["filled_reader"]`, signature `reader(client_id, version_id=None)` returning a dict with `key`, `version_id` and `body` bytes, as `freeze_filled_report` and its tests already use it; the installed reader is the next cell's), take the grant for the covered accounts the freeze returns (add a `filled_grant` in `retained_export.py` modelled on `platinum_grant` if the existing grant helpers cannot take a filled row; say which in the notes), write the BUILDING pointer, and ride the FROZEN row on the marked event (as `pinned_series` rides; call it `pinned_filled`); (2) in `submit_service`, the async leg serves PATH C from that frozen row only (`_serve_filled`, the twin of `_serve_platinum`): bundle from `report_revisions=[row]`, the grant written and read back, the print query, the status `QUEUED`; a filled report has no series: its status `business_date` is the document's own as-of date when it carries one, else null (say which in the notes); (3) a missing `ports["filled_reader"]` refuses as `FilledReportUnavailable` through the same public refusal class the other source refusals use, never a KeyError; (4) PATH A and PATH B behaviour is unchanged. Keep module-level code outside the blocks.

**Write the tests** `infra/aws/lambda/investor-reporting/export/tests/test_filled_report_submit_handler.py` (at least 6 tests; stubs; synthetic ids and bytes; drive `entry.submit_export` the way `test_export_path_b_route.py` drives PATH B): `test_submit_filled_report_through_handler_queues` (a PATH C body reaches QUEUED; the frozen bundle carries the SERVER's pin of the current object), `test_forged_pin_ignored_through_handler` (a body carrying a client-chosen version_id, sha256 and size is frozen with the server's values), `test_uncovered_account_refused_through_handler` (a document naming an account outside scope is refused OBJECT_NOT_COVERED with no pointer, no event and no bundle), `test_no_filled_reader_refused_unavailable`, and at least two more (an overwritten object after submit still yields the pinned bytes in the async leg; PATH B body is unchanged by the branch).


**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB207-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~410/IB207-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["submit_filled_report_through_handler_queues","forged_pin_ignored_through_handler","uncovered_account_refused_through_handler","no_filled_reader_refused_unavailable"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where the seam is"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit. Name the tests exactly as listed (the check reads the names; each name is the tail of a `def test_..` function).

**The difference control (criterion 2).** The check removes every `FILLED-REPORT-F` block IN MEMORY from the product files `submit_async.py`, `submit_service.py` and `retained_export.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error. All new logic therefore sits between `# BEGIN FILLED-REPORT-F` and `# END FILLED-REPORT-F` lines; module-level code outside the blocks must leave every module importable with the blocks gone; reference the new names only inside test functions.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB207-1-AC1" cell_refs="IB-pr-566"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py" . IB207-1-AC1</invocation><expect>IB207-1-AC1 PASS</expect></criterion>
<criterion id="IB207-1-AC2" cell_refs="IB-pr-566"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py" . IB207-1-AC2</invocation><expect>IB207-1-AC2 PASS</expect></criterion>
<criterion id="IB207-1-AC3" cell_refs="IB-pr-566"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py" . IB207-1-AC3</invocation><expect>IB207-1-AC3 PASS</expect></criterion>

<expected_criteria>IB207-1-AC1, IB207-1-AC2, IB207-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 6) and the existing filled-report and export tests pass; AC2 with the FILLED-REPORT-F blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a need to edit a file outside the paths block (record which and why; the issuer amends); a typed object address in product code (an address is `lib/opal_naming.py` `address()` output, and a builder REFUSAL is a missing registry row to record, never a hand-typed workaround); a change in PATH A or PATH B behaviour; a client identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W410-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
infra/aws/lambda/investor-reporting/export/submit_async.py
infra/aws/lambda/investor-reporting/export/submit_service.py
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/handler.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_submit_handler.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_server_pin.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_source.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_freeze_scope.py
infra/aws/lambda/investor-reporting/export/tests/test_export_bundle_filled_report_contract.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~410/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 203 (round 5, workstream ~PS), cell `IB-pr-566`.
<owned_cells>IB-pr-566</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB207-1-AC1, IB207-1-AC2, IB207-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~410/IRPT_BCKEND.TO-IB-pr-566.freeze-filled-report-gets-its-submit-handler-caller-tested-through-the-real-handler.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files in the export package and writes tests and one record; nothing is deployed, so no served byte moves; the deploy legs wait on 49 Financial gold for the first cloud write (B-49F round-120 analysis @5e358b0a8f).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p207_cells.py IB207-1 dry-run at base on dell2 2026-10-15 ~08:1xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; eight negatives on this cell, each failing its own arm: no marker block, a marker removal that breaks import, a weak test file, too few tests, a stray path, no submit or handler change, a missing named test, a typed object address.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~410` (worktree `C:/dev/wk-IRPT_BCKEND-410`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is repository edits and tests; no deploy).
</preflight>
