# TO IRPT_BCKEND.TO-IB-pr-563 -- BUILD the server-side pin of the filled report at submit (CTO ruling on call f50a): freeze_filled_report reads the current object's VersionId, sha256 and size and the submit handler calls it; a forged client pin is ignored (serve-path pair, round 4)

<to_id>IRPT_BCKEND.TO-IB-pr-563</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~407</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_PS_ROUND_4_20261015.md` (msg 8138, @ac865e2d91) and his ruling on call f50a (msg 8104) | **Decomp cell:** `IB-pr-563` (decomposition section 200) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-407`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~407 <0.9.0_WK_IRPT_BCKEND~407@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch407/`).

**Cell `IB-pr-563` (inlined).** The CTO ruled on call f50a (msg 8104; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_F50A_FILLED_REPORT_EXPORT_PIN_SERVER_SIDE_20261015.md`): the SERVER pins the filled report at submit (the signed packet wins). Today `freeze_filled_report(body, permitted_account_ids, reader)` in `infra/aws/lambda/investor-reporting/export/retained_export.py` (near line 408) freezes a pin the CALLER sent in the body (`filled_report_source`: key, VersionId, sha256, size). The ruling: `freeze_filled_report` READS THE CURRENT OBJECT'S VersionId, sha256 and size itself (the object at the naming builder's platinum address for client=<id>, through the same injected reader the freeze uses) and the submit handler calls it, so the client id is the only input from the wire; page-sent pin fields are IGNORED. No route change; neither half of the signed pair re-opens. READ FIRST: `retained_export.py` (`freeze_filled_report`, `platinum_row`, `freeze_platinum`, the `_Store`-style reader the tests use), `export/entry.py` (`submit_export` near line 347) and `export/handler.py` (`submit_export` near line 208, the nested `submit` near line 370): find the one place the submit path freezes sources and call the server-side pin there; `export/tests/test_filled_report_source.py` and `test_filled_report_freeze_scope.py` (their calls pass a client pin: update them to the new shape, they are in your grant), and the shared named-account reader `_scope/filled_named_accounts.py` (the freeze already scopes on it).

**Change (all new logic inside `# BEGIN FILLED-REPORT-E` ... `# END FILLED-REPORT-E` lines in `retained_export.py` and in the submit call site):** (1) the server-side read of the current object's VersionId, sha256 and size (and the scope check on the document it reads, unchanged in behaviour); (2) the submit handler calls it with the client id from the wire and puts the PINNED values in the frozen bundle; (3) any `version_id`, `sha256` or `size` the page sent is dropped before the freeze and never trusted (an unexpected pin field is ignored, not an error, unless the repository's wire contract already refuses unknown members: then it is refused with the same class as other unknown members; say which in the notes); (4) a missing object is refused as the freeze already refuses a missing source. Existing behaviour for PATH A and PATH B is unchanged. Keep module-level code outside the blocks so removing them leaves every module importable.

**Write the tests** `infra/aws/lambda/investor-reporting/export/tests/test_filled_report_server_pin.py` (at least 6 tests; stubs; synthetic ids and bytes): `test_overwritten_version_still_exports_pinned_bytes` (submit pins version V1; the object is then overwritten with V2; exporting the frozen bundle reads the pinned VersionId and yields the V1 bytes), `test_forged_client_pin_ignored` (a body that carries a client-chosen version_id, sha256 and size is frozen with the SERVER's values, never the forged ones), the pin carries VersionId, sha256 and size of the current object, a missing object is refused, a document naming an account outside scope is still refused, PATH B is unchanged. Name the two tests exactly as above (the check reads the names).

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~407/IB204-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[the product paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["overwritten_version_still_exports_pinned_bytes","forged_client_pin_ignored"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where the submit call site is"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2).** The check removes every FILLED-REPORT-E block IN MEMORY from `retained_export.py` and `export/entry.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB204-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB204-2-AC1" cell_refs="IB-pr-563"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py" . IB204-2-AC1</invocation><expect>IB204-2-AC1 PASS</expect></criterion>
<criterion id="IB204-2-AC2" cell_refs="IB-pr-563"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py" . IB204-2-AC2</invocation><expect>IB204-2-AC2 PASS</expect></criterion>
<criterion id="IB204-2-AC3" cell_refs="IB-pr-563"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py" . IB204-2-AC3</invocation><expect>IB204-2-AC3 PASS</expect></criterion>

<expected_criteria>IB204-2-AC1, IB204-2-AC2, IB204-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 6) and the existing export tests pass; AC2 with every FILLED-REPORT-E block removed in memory the new tests FAIL on assertions; AC3 the record: the worker's own paths exactly as recorded and inside the grant (retained_export.py, a submit call site, the new test), the two named tests present and listed (an overwritten version still exports the pinned bytes; a forged client pin is ignored), no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a change in PATH A or PATH B behaviour; a route or wire-contract change beyond ignoring page-sent pin fields; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W407-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~407/
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/handler.py
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_server_pin.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_source.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_freeze_scope.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 200 (round 4, workstream ~PS), cell `IB-pr-563`.
<owned_cells>IB-pr-563</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB204-2-AC1, IB204-2-AC2, IB204-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~407/IRPT_BCKEND.TO-IB-pr-563.server-pins-the-filled-report-at-submit.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files in the export package and writes tests and one record; nothing is deployed, so no served byte moves; the deploy legs wait on 49 Financial gold for one date (CTO msg 7995) and on the source-map cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched; the ruling changes the export wire to send the client id only, which is the portal cell's.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB204-2 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; seven negatives on this cell, each failing its own arm: no marker block, a marker removal that breaks import, a weak test file, a stray path, no submit call site changed, a missing named test, a typed object address.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~407` (worktree `C:/dev/wk-IRPT_BCKEND-407`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is repository edits and tests; no deploy).
</preflight>
