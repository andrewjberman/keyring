# TO IRPT_BCKEND.TO-IB-pr-562 -- BUILD the lambda source-map entries for the shared named-account reader in EVERY importing function, with a build-only import test per function (serve-path pair, round 4; row D2-W402-S3)

<to_id>IRPT_BCKEND.TO-IB-pr-562</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~406</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_PS_ROUND_4_20261015.md` (msg 8138, @ac865e2d91) and his ruling on call f50a (msg 8104) | **Decomp cell:** `IB-pr-562` (decomposition section 200) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-406`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~406 <0.9.0_WK_IRPT_BCKEND~406@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch406/`).

**Cell `IB-pr-562` (inlined).** Round 3 built the shared named-account reader `infra/aws/lambda/investor-reporting/_scope/filled_named_accounts.py` (cell `IB-pr-558`, row `IRPT_BCKEND-D2-W402-S3`, ARMED): `reporting/entry.py` (the filled-report route) and the export freeze (`export/retained_export.py`) import it BY NAME, but `infra/aws/lambda/ci/lambda-source-map.json` is explicit per file and lists no entry for it, so a deploy of any function that packages an importing module would omit the file and fail on import. The CTO ruled (round 4, item 1): add source-map `staged_from` entries for the shared file in EVERY importing function, plus a BUILD_ONLY import test per function. READ FIRST: the map's entries for `irpt-49f-reporting-read-lambda`, `irpt-ycharts-generate` and `irpt-export-render` (and any other function whose entry mentions `reporting/entry.py`, `export/retained_export.py` or `export/bundle.py`: COMPUTE that set from the map; the check computes the same), how an existing `_scope/*.py` file is recorded in `staged_from` (`repo_path`, `pin`, `packaged_as`, `sha256`) and in `files`, `infra/aws/lambda/ci/build-and-upload.sh` (its BUILD_ONLY mode) and `infra/aws/lambda/ci/tests/test_build_only.sh`.

**Change (the map only; no Python product file):** for each importing function add EXACTLY ONE `staged_from` entry `{"repo_path":"infra/aws/lambda/investor-reporting/_scope/filled_named_accounts.py","pin":"<a 40-hex commit that holds the file at its current bytes: git log -1 --format=%H -- the file>","packaged_as":"filled_named_accounts.py","sha256":"<64 hex: the sha256 of the file's bytes at that pin (git show of the pin)>"}` and add `"filled_named_accounts.py"` to that function's `files` list. Change nothing else in the map (not `artifact_sha256`, not any deploy record, not any other function). Keep the file's existing line endings and key order.

**BUILD_ONLY import test, per function:** for each importing function run the repository's build-only mode locally (no upload, no AWS write; read `build-and-upload.sh` for the exact invocation and what it needs) and import the entry module from the built tree under `python -I`; record `{"function":"<name>","result":"PASS"}` (or FAIL with the reason in notes; a FAIL is a BLOCKING row, not a pass). If the build-only mode needs AWS credentials or network beyond reads, record that as a row and do the import check on the staged tree the build step produces.

**Write the test** `infra/aws/lambda/ci/tests/test_source_map_filled_named_accounts.py` (python, at least 4 tests; read the map with `Path.read_text` or `open`): for every function whose entry mentions one of the importing modules (computed from the map), the entry exists exactly once with the right `packaged_as`, a 40-hex pin that holds the file (`git show`) with the sha256 equal to the file's sha256 at that pin, and `files` names it; no function that does not package an importing module carries the entry; the entry's pin is reachable from HEAD.

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~406/IB204-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the product paths you changed, sorted],"build_only_imports":[{"function":"<name>","result":"PASS"},...one per importing function],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own run serving the BASE map bytes (git show of the base commit), 1 or more>,"notes":["what each fact rests on and what was not read; the build-only invocation you used"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2) is data:** the check serves the BASE bytes of the source map in memory (it patches `open` and `Path.read_text/read_bytes` for that path) and runs YOUR new test; it must then FAIL on ASSERTIONS. Read the map in the test through `open` or `Path.read_text` of its repository path, never from an embedded copy.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB204-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB204-1-AC1" cell_refs="IB-pr-562"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py" . IB204-1-AC1</invocation><expect>IB204-1-AC1 PASS</expect></criterion>
<criterion id="IB204-1-AC2" cell_refs="IB-pr-562"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py" . IB204-1-AC2</invocation><expect>IB204-1-AC2 PASS</expect></criterion>
<criterion id="IB204-1-AC3" cell_refs="IB-pr-562"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py" . IB204-1-AC3</invocation><expect>IB204-1-AC3 PASS</expect></criterion>

<expected_criteria>IB204-1-AC1, IB204-1-AC2, IB204-1-AC3</expected_criteria>

What the checks grade: AC1 the new test (at least 4) passes; AC2 with the BASE source-map bytes served in memory the new test FAILS on assertions; AC3 the record: the worker's own paths exactly as recorded and inside the grant (the map and the new test only), every function the check computes as importing has exactly one entry with packaged_as, a 40-hex pin that holds the file, a sha256 equal to the file's at that pin (recomputed by the check) and the file named in `files`, a PASS build-only import recorded for each of those functions, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent.** The build-only mode is run locally without upload; no `terraform plan` or `apply` is run.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, uploads, invokes or sends; a change to any map field other than the new entries and the files lists; a build-only import that fails (a BLOCKING row); a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W406-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~406/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/tests/test_source_map_filled_named_accounts.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 200 (round 4, workstream ~PS), cell `IB-pr-562`.
<owned_cells>IB-pr-562</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB204-1-AC1, IB204-1-AC2, IB204-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~406/IRPT_BCKEND.TO-IB-pr-562.source-map-stages-the-shared-reader-in-every-importing-function.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits the lambda source map (a JSON record) and writes a test and one record; nothing is built for upload or deployed, so no served byte moves; the map is read by the build and by the deploy census, and the new entries make a later deploy of the route or the export include the shared file.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB204-1 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; ten negatives on this cell, each failing its own arm: too few tests, a weak test file, a stray path, a missing entry in one function, a wrong sha256, a pin that does not hold the file, the files list missing the file, a failing build-only import, a missing build-only import, plus the clean positives.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~406` (worktree `C:/dev/wk-IRPT_BCKEND-406`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is a JSON record and a test in the repository; no deploy).
</preflight>
