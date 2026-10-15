# TO IRPT_BCKEND.TO-IB-pr-555 -- BUILD hop 4: the filled_report export source kind, additive only, pinned by VersionId and sha256 (serve-path pair, build slice c)

<to_id>IRPT_BCKEND.TO-IB-pr-555</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~399</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 7995 (CTO half of the serve-path pair signed @82183fcfaf; the document's source ruled; build slices may start now) and the packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (sha256 `7daa29f0fe10e0a7bda3eb2c12f1eee3bb4ca43ecc7361fbdf1327ded864abac`) | **Decomp cell:** `IB-pr-555` (decomposition section 194) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-399`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~399 <0.9.0_WK_IRPT_BCKEND~399@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch399/`).

**Cell `IB-pr-555` (inlined).** Hop 4 of the filled-report serve path (CTO half signed, msg 7995): a `filled_report` source kind for the export, ADDITIVE ONLY. READ FIRST: the packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (sections 1, 4, 5, 9) and the design record `deliverables/0.9.0_WK_IRPT_BCKEND~395/IB199-3_serve_path_design.json` (hop 4), then `infra/aws/lambda/investor-reporting/export/bundle.py` (the platinum test near line 111 and the performance_source pins near line 191) and `retained_export.py` (`platinum_row` near line 267 and `freeze_platinum` near line 279), and the existing tests `export/tests/test_export_path_b.py`, `test_retained_export.py`, `test_bundle_report_ref.py` (your models and your regressions). The export freezes PATH A (a retained report by revision ref) and PATH B (a platinum performance series pinned by VersionId and sha256 at submit) today; the filled report is a NEW source kind: the submit pins the filled-report object (the platinum object `filled_report.json` for client=<id>, whose address comes from the naming builder, never typed) by its VersionId and sha256 and freezes it into the bundle the way PATH B freezes the platinum series.

**Build, in `bundle.py` and `retained_export.py` (all new logic inside the BEGIN/END blocks):** a branch for source kind `filled_report` in the body validation (an unknown or malformed pin is refused) and in the freeze (the frozen entry records the key, VersionId, sha256 and the byte count, and a pin whose sha256 does not match the object's bytes is refused). **ADDITIVE ONLY:** PATH A, PATH B and every existing source kind behave exactly as before; at most SIX existing lines may be removed or rewritten in total across the two files (an `if` becoming an `if/elif` is the expected case), and the record states the exact removed-line count. Existing behaviour is unchanged: the existing tests must still pass.

**Write the tests** `infra/aws/lambda/investor-reporting/export/tests/test_filled_report_source.py` (at least 8 tests; stubs; synthetic ids and bytes): a valid `filled_report` pin is frozen with VersionId, sha256 and size; a pin with a wrong sha256 is refused; a pin missing its VersionId is refused; an unknown source kind is still refused; a PATH B body is frozen exactly as before; a bundle with a `filled_report` entry round-trips through the same freeze and read helpers the retained export uses; and no existing kind's output changes (compare against a PATH A and a PATH B fixture).

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~399/IB200-3_record.json`: `{"base_commit":"<40hex>","changed_paths":[every product path you changed, sorted; deliverables and the channel excluded],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"existing_kinds_untouched":true,"removed_lines":<the number of lines your diff removes from bundle.py and retained_export.py, 0 to 6>,"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2).** Wrap the NEW product logic of this cell in `# BEGIN FILLED-REPORT-C` ... `# END FILLED-REPORT-C` comment lines in the file(s) named below (one or more blocks per file; the whole new function bodies and the new branches). The check removes every such block IN MEMORY and runs YOUR new test file: it must then FAIL on ASSERTIONS (a failed test), not on an import or collection error. So write the blocks so that, with them removed, the module still imports (no module-level statement may use a name defined only inside a block), and write the new tests so that they reference the new names only INSIDE test functions. A test file that still passes with the blocks removed is the defect the control exists to catch.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB200-3_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB200-3-AC1" cell_refs="IB-pr-555"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-3-AC1</invocation><expect>IB200-3-AC1 PASS</expect></criterion>
<criterion id="IB200-3-AC2" cell_refs="IB-pr-555"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-3-AC2</invocation><expect>IB200-3-AC2 PASS</expect></criterion>
<criterion id="IB200-3-AC3" cell_refs="IB-pr-555"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-3-AC3</invocation><expect>IB200-3-AC3 PASS</expect></criterion>

<expected_criteria>IB200-3-AC1, IB200-3-AC2, IB200-3-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 8) and the existing export tests pass; AC2 with every FILLED-REPORT-C block removed in memory from bundle.py and retained_export.py the new tests FAIL on assertions; AC3 the record: the worker's own product paths exactly as recorded and inside the grant (both export files and the new test among them), no typed object address, `existing_kinds_untouched` true, `removed_lines` equal to the diff's removed lines and at most 6, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent;** no AWS call is needed (all storage and scope are stubs).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a change to PATH A or PATH B behaviour; more than six removed lines; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W399-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~399/
infra/aws/lambda/investor-reporting/export/bundle.py
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_source.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 194 (round 2, workstream ~PS), cell `IB-pr-555`.
<owned_cells>IB-pr-555</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB200-3-AC1, IB200-3-AC2, IB200-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~399/IRPT_BCKEND.TO-IB-pr-555.hop-4-filled-report-export-source-kind.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files and writes tests and one record; nothing is deployed, so no bundle carries the new kind and no served byte moves; the deploy is a later act under the signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched by this slice.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB200-3 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; eight negatives on this cell, each failing its own arm: a failing test, too few tests, no marker block, a marker removal that breaks import, a weak test file, a stray path, a record that disagrees with the commits, a removed-line count that disagrees with the diff.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~399` (worktree `C:/dev/wk-IRPT_BCKEND-399`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is code and tests in the repository; no deploy).
</preflight>
