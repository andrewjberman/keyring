# TO IRPT_BCKEND.TO-IB-pr-567 -- BUILD the installed filled reader and the render-side read of a pinned filled report through the shared named-account reader; one pinned filled report rendered from a fixture

<to_id>IRPT_BCKEND.TO-IB-pr-567</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~411</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-5 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_PO5_PS5_PY3_20261015.md` (@25f361860e, msg 8183), ~PS item 2 (W407-S2) | **Decomp cell:** `IB-pr-567` (decomposition section 203) | **outcome_ref:** FWD-2

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-411`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~411 <0.9.0_WK_IRPT_BCKEND~411@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.** Python: ASCII only in product code and logs; tests use synthetic ids and bytes.

**Client data rule:** counts, dates, hashes, commit ids, field names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch411/`).

**Cell `IB-pr-567` (inlined) -- W407-S2: the export render installs the filled reader.** `freeze_filled_report` reads the filled report through an injected `ports["filled_reader"]` (`reader(client_id, version_id=None)` returning `{key, version_id, body}`), and no installed composition supplies it: a submit with a filled source is refused as unavailable today. Ruling (CTO round-5 analysis, ~PS item 2): `irpt-export-render`'s filled-source branch reads the PINNED object through the shared named-account reader, and a test renders one pinned filled report from a fixture. The submit-path caller is the sibling cell `IB-pr-566` (it owns `submit_async.py`, `submit_service.py` and `retained_export.py`; do NOT edit them).

**READ FIRST (named files only):** `infra/aws/lambda/investor-reporting/export/entry.py` (where `ports` are composed, near line 405: `platinum_series` is installed by `retained.installed_platinum_reader(ports, TENANT)`), `infra/aws/lambda/investor-reporting/export/retained_export.py` (`installed_platinum_reader`, `platinum_reader`, `read_pinned_filled` and `FilledReportUnavailable`: the reader contract the filled reader must meet), `infra/aws/lambda/investor-reporting/export/render.py`, `infra/aws/lambda/investor-reporting/export/dispatch.py`, `infra/aws/lambda/investor-reporting/export/download.py`, `infra/aws/lambda/investor-reporting/export/package.py`, `infra/aws/lambda/investor-reporting/export/handler.py` (how a bundle's `authorized_report_revisions` become a render package: find the one place a revision carrying `filled_report_source` would be read), `infra/aws/lambda/investor-reporting/export/bundle.py` (the pin shape, lines 91 to 170), `infra/aws/lambda/investor-reporting/_scope/filled_named_accounts.py` (the shared reader), `lib/opal_naming.py` (`address()`) and `infra/logic/registry/` (names only, to find whether the filled report object has an address row) and the 49 Financial hop-1 producer for the filled report values (Glob `data/assets/scripts/gold/irpt_reporting/` for the name `filled_report_values`; read how its output key is built).

**Change (all new logic inside `# BEGIN FILLED-REPORT-G` ... `# END FILLED-REPORT-G` lines):** (1) a NEW module `infra/aws/lambda/investor-reporting/export/filled_reader_installed.py` with `installed_filled_reader(ports, tenant)` returning `reader(client_id, version_id=None)`: with a `version_id` it reads THAT version only (S3 `VersionId`), without one it reads the current object; it returns `{key, version_id, body}` and raises nothing it does not name; the object address comes from `lib/opal_naming.address()` for the filled report, never typed (if the builder refuses because the registry has no row for it, that is a missing registry row: file a BLOCKING row naming the missing row and STOP; do not edit the registry); (2) `entry.py` installs it as `ports["filled_reader"]` when the port is absent, as `platinum_series` is installed; (3) the render side: where a bundle revision carries `filled_report_source`, the render reads the pinned bytes with `read_pinned_filled(reader, pin)` (the one read the freeze also uses) and takes the named accounts from the shared reader `filled_named_accounts`, and never reads the current object for a pin; (4) a pin whose bytes no longer hash to the pinned sha256 or whose version is gone is refused (`FilledReportUnavailable`), never rendered. (5) **AMENDMENT 1 (issuer, on your rows W411-S2 and S4): ONE implementation, not two.** `IB-pr-566` is merged on box/dell2 (@2cb9105a27) and its submit legs read the pinned bytes through `retained_export.filled_render_read(reader, item)` and take the covered accounts from `retained_export.filled_covered_accounts(data, permitted_account_ids)`. Make `render.filled_render_package` CALL those two (read-only use of `retained_export.py`, which you do not edit) and delete the parallel logic, so the named-account logic exists once; keep your tests, now through the shared functions. (6) **AMENDMENT 1: the new module must be packaged.** `infra/aws/lambda/ci/lambda-source-map.json` lists the export function's modules by name in its `files` array; `filled_reader_installed.py` is not in the `files` list of `irpt-export-render`, so a deploy would omit it. Add exactly that one name to that function's `files` list (nothing else in the map) and write `infra/aws/lambda/ci/tests/test_source_map_filled_reader_installed.py` (at least 2 tests, reading the map with `open` or `Path.read_text`: the module is named exactly once in `irpt-export-render`'s `files`, and the module file exists in its `source_dir`). Your rows W411-S1 (the export role's read of the filled object) and S3 (lib/ in the package: `lib/opal_naming.py` is already in that `files` list) stay as recorded for the deploy legs. If the render seam is not in `render.py`, `dispatch.py`, `download.py`, `package.py` or `handler.py`, STOP and file a row naming the file (the issuer amends the grant). PATH A and PATH B behaviour is unchanged.

**Write the tests** `infra/aws/lambda/investor-reporting/export/tests/test_filled_report_installed_reader_render.py` (at least 5 tests; a stub S3 with versions; synthetic ids and bytes): `test_installed_reader_reads_pinned_version` (a pin reads its VersionId even after the object is overwritten), `test_render_pinned_filled_report_from_fixture` (one pinned filled report rendered from a fixture: the render package carries the pinned bytes' sha256 and the named accounts), `test_installed_reader_never_reads_current_object_for_a_pin`, and at least two more (a tampered or missing pinned version is refused; `entry` installs the port when absent and leaves a supplied one alone).


**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB207-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~411/IB207-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["installed_reader_reads_pinned_version","render_pinned_filled_report_from_fixture","installed_reader_never_reads_current_object_for_a_pin"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where the seam is"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit. Name the tests exactly as listed (the check reads the names; each name is the tail of a `def test_..` function).

**The difference control (criterion 2).** The check removes every `FILLED-REPORT-G` block IN MEMORY from the product files `entry.py`, `filled_reader_installed.py`, `render.py`, `download.py` and `dispatch.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error. All new logic therefore sits between `# BEGIN FILLED-REPORT-G` and `# END FILLED-REPORT-G` lines; module-level code outside the blocks must leave every module importable with the blocks gone; reference the new names only inside test functions.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB207-2-AC1" cell_refs="IB-pr-567"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py" . IB207-2-AC1</invocation><expect>IB207-2-AC1 PASS</expect></criterion>
<criterion id="IB207-2-AC2" cell_refs="IB-pr-567"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py" . IB207-2-AC2</invocation><expect>IB207-2-AC2 PASS</expect></criterion>
<criterion id="IB207-2-AC3" cell_refs="IB-pr-567"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py" . IB207-2-AC3</invocation><expect>IB207-2-AC3 PASS</expect></criterion>

<expected_criteria>IB207-2-AC1, IB207-2-AC2, IB207-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 5) and the existing filled-report and export tests pass; AC2 with the FILLED-REPORT-G blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a need to edit a file outside the paths block (record which and why; the issuer amends); a typed object address in product code (an address is `lib/opal_naming.py` `address()` output, and a builder REFUSAL is a missing registry row to record, never a hand-typed workaround); a change in PATH A or PATH B behaviour; a client identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W411-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
infra/aws/lambda/investor-reporting/export/entry.py
infra/aws/lambda/investor-reporting/export/filled_reader_installed.py
infra/aws/lambda/investor-reporting/export/render.py
infra/aws/lambda/investor-reporting/export/download.py
infra/aws/lambda/investor-reporting/export/dispatch.py
infra/aws/lambda/investor-reporting/export/package.py
infra/aws/lambda/investor-reporting/export/handler.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_installed_reader_render.py
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/tests/test_source_map_filled_reader_installed.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~411/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 203 (round 5, workstream ~PS), cell `IB-pr-567`.
<owned_cells>IB-pr-567</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB207-2-AC1, IB207-2-AC2, IB207-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~411/IRPT_BCKEND.TO-IB-pr-567.export-render-installs-the-filled-reader-and-renders-one-pinned-filled-report-from-a-fixture.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files in the export package (one new module) and writes tests and one record; nothing is deployed, so no served byte moves; the deploy legs wait on 49 Financial gold for the first cloud write and on the source-map staging already landed (IB-pr-562).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p207_cells.py IB207-2 dry-run at base on dell2 2026-10-15 ~08:1xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; eight negatives on this cell, each failing its own arm: no marker block, a marker removal that breaks import, a weak test file, too few tests, a stray path, no submit or handler change, a missing named test, a typed object address.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~411` (worktree `C:/dev/wk-IRPT_BCKEND-411`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is repository edits and tests; no deploy).
</preflight>
