# TO IRPT_BCKEND.TO-IB-pr-553 -- BUILD hop 2's publisher plumbing for the filled report: the object name, report_address() from the naming builder, the registry family row, a validating put and a default-OFF pass (serve-path pair, build slice a)

<to_id>IRPT_BCKEND.TO-IB-pr-553</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~397</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 7995 (CTO half of the serve-path pair signed @82183fcfaf; the document's source ruled; build slices may start now) and the packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (sha256 `7daa29f0fe10e0a7bda3eb2c12f1eee3bb4ca43ecc7361fbdf1327ded864abac`) | **Decomp cell:** `IB-pr-553` (decomposition section 194) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-397`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~397 <0.9.0_WK_IRPT_BCKEND~397@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch397/`).

**Cell `IB-pr-553` (inlined).** The CTO signed the CTO half of the serve-path pair (msg 7995) and ruled the document's source: gold is parquet (built by `2.0.0_SA_COO~D2` as the table `filled_report_values`), and THIS seat's publisher reads that gold and composes the platinum JSON. **This cell builds the publisher's PLUMBING for hop 2 only; it does not compose from gold (the gold table does not exist yet), and the scheduled pass ships OFF.** READ FIRST: the packet `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (sections 1, 2, 4, 9) and the design record `deliverables/0.9.0_WK_IRPT_BCKEND~395/IB199-3_serve_path_design.json` (hop 2), then `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` (SUMMARY_OBJECT near line 251, `summary_address` near line 313, `build_client_summary`), `handler.py` (the summary put near lines 192 and 371-372), `infra/logic/registry/reporting_policies.json` (the CLIENT_SUMMARY family near line 51) and the existing tests in `reporting-publish/tests/`. The document is contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` 0.5.1, key `document`: exactly two top-level keys `household` and `values`; `household` = {household_ref, as_of, first_data_date, accounts}; each account entry = {account_id, last4, first_data_date, window_status in MEASURED/NOT_SPANNED/BREAK}; `values` = an object keyed by member id whose entries are a number, a text, `{"absent": "<reason in words>"}`, `{"by_row": {...}}` or a list of series (read the contract's `document` block for the full rule).

**Build, in `publisher.py` (all new logic inside the BEGIN/END blocks):** (1) `FILLED_REPORT_OBJECT = "filled_report.json"` beside SUMMARY_OBJECT; (2) `report_address(firm, client_id, naming=None)` beside `summary_address`: the same client-id admissibility refusal, and the address is `naming.address("irpt", firm, TIER_PLATINUM, TABLE_PLATINUM, "client=%s" % cid, FILLED_REPORT_OBJECT)` ONLY, never a typed key; (3) `validate_filled_report(document)`: raise `PublishRefused` unless the document has exactly the keys `household` and `values`, the four household fields, well-formed account entries, and every `values` entry one of the allowed forms (an absent form carries a non-empty reason string); (4) `publish_filled_report(firm, client_id, document, put, naming=None)`: validate, address by `report_address`, `put(address, json bytes with sorted keys and compact separators)`, return the address. **In `handler.py`:** a filled-report pass that is OFF unless the environment switch `FILLED_REPORT_PASS` is exactly `1`; when on, per client it calls a reader `read_filled_report_gold(firm, client_id)` that today raises `NotYetAvailable` (a small exception class you add: the gold table is `2.0.0_SA_COO~D2`'s) and the pass records the client as not available and writes nothing. **In `reporting_policies.json`:** one new family row for the filled-report object, copying the shape of the CLIENT_SUMMARY family (the family set is closed, so a row is needed). Existing behaviour is unchanged: the existing publisher tests must still pass.

**Write the tests** `infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py` (at least 8 tests; synthetic ids only): the address equals the builder's output for client=<id> and never differs by hand; an inadmissible client id is refused; an extra top-level key is refused; a missing household field is refused; an absent form with an empty reason is refused; a valid document is put once with sorted compact JSON; the put receives the builder's address; the default pass is OFF (no put, no reader call) and with the switch on the reader's `NotYetAvailable` leaves nothing written.

**Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~397/IB200-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[every product path you changed, sorted, repo-relative; deliverables and the channel excluded],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"default_off":true,"address_example":"<the naming builder's output for ('irpt','49financial','platinum','reporting','client=PLACEHOLDER','filled_report.json'), copied from running it>","notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2).** Wrap the NEW product logic of this cell in `# BEGIN FILLED-REPORT-A` ... `# END FILLED-REPORT-A` comment lines in the file(s) named below (one or more blocks per file; the whole new function bodies and the new branches). The check removes every such block IN MEMORY and runs YOUR new test file: it must then FAIL on ASSERTIONS (a failed test), not on an import or collection error. So write the blocks so that, with them removed, the module still imports (no module-level statement may use a name defined only inside a block), and write the new tests so that they reference the new names only INSIDE test functions. A test file that still passes with the blocks removed is the defect the control exists to catch.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB200-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB200-1-AC1" cell_refs="IB-pr-553"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-1-AC1</invocation><expect>IB200-1-AC1 PASS</expect></criterion>
<criterion id="IB200-1-AC2" cell_refs="IB-pr-553"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-1-AC2</invocation><expect>IB200-1-AC2 PASS</expect></criterion>
<criterion id="IB200-1-AC3" cell_refs="IB-pr-553"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-1-AC3</invocation><expect>IB200-1-AC3 PASS</expect></criterion>

<expected_criteria>IB200-1-AC1, IB200-1-AC2, IB200-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 8) and the existing publisher tests pass; AC2 with every FILLED-REPORT-A block removed in memory from publisher.py the new tests FAIL on assertions (not on an import error); AC3 the record: the worker's own product paths exactly as recorded, all inside the grant, publisher.py, the registry file and the new test among them, no typed object address in a product file, `default_off` true, `address_example` equal to the naming builder's output, the registry row present, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product files and tests named in the paths block and your records, nothing else. **Nothing is deployed, invoked, written to AWS or the served prefixes, signed or sent;** no AWS call is needed (all storage and scope are stubs).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS, invokes or sends; a change that breaks an existing publisher test and cannot be made additive; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W397-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~397/
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/logic/registry/reporting_policies.json
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 194 (round 2, workstream ~PS), cell `IB-pr-553`.
<owned_cells>IB-pr-553</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB200-1-AC1, IB200-1-AC2, IB200-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~397/IRPT_BCKEND.TO-IB-pr-553.hop-2-filled-report-publisher-plumbing.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits repository files and writes tests and one record; nothing is deployed, so no served byte moves; the pair this slice belongs to is signed (both halves, packet 7daa29f0fe10) and its deploy legs wait on the gold table and a later order.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched by this slice.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB200-1 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; ten negatives on this cell, each failing its own arm: a failing test, too few tests, no marker block, a marker removal that breaks import, a weak test file, a stray path, a record that disagrees with the commits, a typed address, a wrong address example, a pass not off.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~397` (worktree `C:/dev/wk-IRPT_BCKEND-397`). Class WORLD by the path floor (the spine v3.19 gate infers WORLD from an infrastructure path; the work is code and tests in the repository; no deploy).
</preflight>
