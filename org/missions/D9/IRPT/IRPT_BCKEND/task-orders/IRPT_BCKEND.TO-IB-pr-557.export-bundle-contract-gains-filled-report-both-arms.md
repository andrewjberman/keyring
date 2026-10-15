# TO IRPT_BCKEND.TO-IB-pr-557 -- BUILD the ExportBundle contract's filled_report source kind: both schema copies byte-equal, one minor revision step, both arms tested (serve-path pair, round 3)

<to_id>IRPT_BCKEND.TO-IB-pr-557</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~401</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-3 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_PS_ROUND_3_20261015.md` (msg 8058, @a4718eab10; the CVO's L10 slug ADJUDICATION_v102) | **Decomp cell:** `IB-pr-557` (decomposition section 196) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-401`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~401 <0.9.0_WK_IRPT_BCKEND~401@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch401/`).

**Cell `IB-pr-557` (inlined).** Round 2's export slice (`IB-pr-555`, record `deliverables/0.9.0_WK_IRPT_BCKEND~399/IB200-3_record.json`, row `IRPT_BCKEND-D2-W399-S1`) found that the PACKAGED `ExportBundle` contract refuses a bundle that carries a `filled_report` item: its `authorized_report_revisions` items are `additionalProperties: false` and admit no `filled_report_source` property, so `bundle.validate` refuses the frozen filled bundle. The CTO ruled (round 3): the contract gains `filled_report` as an allowed source kind for NEW bundles, the contract's revision moves by a MINOR step, nothing that serves today changes, and the test pins BOTH arms. READ FIRST: `export/bundle.py` (`_CONTRACT_FILE`, `validate`), `retained_export.py` (the `filled_report` branch IB-pr-555 built: the exact shape of a frozen `filled_report` item: its key, VersionId, sha256 and size), the two schema copies and `export/tests/test_packaged_contracts_match_docs.py` (the packaged copy is byte-equal to the docs copy; one test per file), and the existing valid bundle fixture `portal/src/pages/InvestorReporting/fixtures/wire/ExportBundle.valid.json` (read only).

**Change (JSON only; no Python product file):** in BOTH `docs/contracts/investor-reporting/v1/ExportBundle.schema.json` and `infra/aws/lambda/investor-reporting/_contracts/ExportBundle.schema.json` (keep them BYTE-EQUAL, LF-normalised): add the `filled_report_source` property (an object whose required fields are exactly those the IB-pr-555 freeze writes for a filled item) to the `authorized_report_revisions` item schema, with a `description` that cites THIS signed pair (packet sha256 `7daa29f0fe10e0a7bda3eb2c12f1eee3bb4ca43ecc7361fbdf1327ded864abac`, hop 4) and invents no quotation of the PRD (the header says the file is generated from the PRD CONTRACTS row and a fabricated quoted source is refused by a battery: if a test or gate in the repository refuses the new description or the revision step for that reason, record a BLOCKING row naming the gate and stop); change nothing else; set `x-contract-revision` one MINOR step up (the base reads `1.1`, so `1.2`). Existing bundles (no `filled_report_source`) must still validate byte-for-byte as before.

**Write the tests** `infra/aws/lambda/investor-reporting/export/tests/test_export_bundle_filled_report_contract.py` (at least 6 tests; synthetic ids and hashes only; validate with the same jsonschema call `bundle.validate` uses against the PACKAGED schema file): ARM 1, a new bundle with a well-formed `filled_report_source` item validates; the same item without its sha256 (or VersionId) is refused; an unknown extra property is still refused; ARM 2, the existing valid fixture and a PATH A and a PATH B shaped bundle (copy their shapes from the existing export tests) validate UNCHANGED; the packaged and docs copies are byte-equal (LF-normalised). Name the arms in the record.

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~401/IB201-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the product paths you changed, sorted; deliverables and the channel excluded],"arms_tested":["new_bundle_validates","old_bundle_validates_unchanged"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own run serving the BASE schema (git show of the base commit), 1 or more>,"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2) is data, not a marker block:** the check serves the BASE bytes of BOTH schema copies in memory (it patches `open` and `Path.read_text/read_bytes` for those two paths) and runs YOUR new test file; it must then FAIL on ASSERTIONS (the arm-1 tests), not on an error. So read the schema in your tests through `open`, `json.load(open(...))` or `Path.read_text` of the packaged path, never from a copy you embed in the test.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB201-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**AMENDMENT 1 (the issuer, 2026-10-15 ~06:1xZ, on your row `IRPT_BCKEND-D2-W401-S1`; my defect, the cell text missed the top-level `oneOf`):** the CTO's ruling is that a NEW bundle carrying `filled_report` VALIDATES, and your finding is that the top-level `oneOf` has no branch for a frozen filled bundle (no retained-report ref, no `narrative_state`). The grant is therefore widened by exactly ONE additive change: add ONE NEW top-level `oneOf` branch that admits a bundle whose report source is the `filled_report_source` item(s) and nothing else of the existing branches' shape (read how the existing branches are written and mirror their style; the new branch must not make any bundle that was refused before validate unless it carries a well-formed `filled_report_source`). Every EXISTING branch stays byte-for-byte as it is, so every existing bundle validates unchanged (arm 2 proves it with the existing fixtures). The same revision step (1.1 to 1.2) covers it: an added branch is backward compatible. Your inherited state: your three commits stay (the build, the criteria output, the instance); finish the build, re-run the three criteria and replace the criteria output and the instance. The four failing tests in `_contracts/tests/test_seam_paired.py` (your row S2) fail at base too: leave them, they are not in the check's regression set.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB201-1-AC1" cell_refs="IB-pr-557"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py" . IB201-1-AC1</invocation><expect>IB201-1-AC1 PASS</expect></criterion>
<criterion id="IB201-1-AC2" cell_refs="IB-pr-557"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py" . IB201-1-AC2</invocation><expect>IB201-1-AC2 PASS</expect></criterion>
<criterion id="IB201-1-AC3" cell_refs="IB-pr-557"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py" . IB201-1-AC3</invocation><expect>IB201-1-AC3 PASS</expect></criterion>

<expected_criteria>IB201-1-AC1, IB201-1-AC2, IB201-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 6) and the existing contract and export tests pass; AC2 with the BASE bytes of both schema copies served in memory the new tests FAIL on assertions; AC3 the record: the worker's own paths exactly as recorded and inside the grant (both schema copies and the new test), the two copies byte-equal after line-ending normalisation, `x-contract-revision` one minor step up, `filled_report` in the new schema and not in the base one, both arms named, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent;** no AWS call is needed (all storage and scope are stubs).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a gate or battery in the repository that refuses the new property or the revision step (record it); a change to any EXISTING schema property or any EXISTING oneOf branch (only the new item property, ONE new top-level oneOf branch and the revision may be added); a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W401-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~401/
docs/contracts/investor-reporting/v1/ExportBundle.schema.json
infra/aws/lambda/investor-reporting/_contracts/ExportBundle.schema.json
infra/aws/lambda/investor-reporting/export/tests/test_export_bundle_filled_report_contract.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 196 (round 3, workstream ~PS), cell `IB-pr-557`.
<owned_cells>IB-pr-557</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB201-1-AC1, IB201-1-AC2, IB201-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~401/IRPT_BCKEND.TO-IB-pr-557.export-bundle-contract-gains-filled-report-both-arms.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits two JSON schema copies and writes tests and one record; nothing is deployed, so no served bundle is validated differently and no served byte moves; the packaged copy reaches the export lambda only at a later deploy under the signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB201-1 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; seven negatives on this cell, each failing its own arm: too few tests, a weak test file, a stray path, the two copies differing, a two-step revision, no new kind, one arm only.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~401` (worktree `C:/dev/wk-IRPT_BCKEND-401`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is two schema copies and a test in the repository; no deploy).
</preflight>
