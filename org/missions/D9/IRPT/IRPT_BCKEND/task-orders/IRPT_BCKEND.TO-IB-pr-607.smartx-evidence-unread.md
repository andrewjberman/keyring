# TO IRPT_BCKEND.TO-IB-pr-607 -- The SmartX evidence is never omitted silently: a failed or refused SmartX read gives an exempted account the evidence `unread` with a reason category; the decision, the floor and the threshold unchanged (CTO half of exemption ADDENDUM 1, msg 8719 condition 2)

<to_id>IRPT_BCKEND.TO-IB-pr-607</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~443</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO half of the exemption ADDENDUM 1, `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_HOLDINGS_EXEMPTION_PAIR_ADDENDUM_1_CTO_HALF.md`, condition 2 (msg 8719): "if the SmartX account-map read fails or is refused at run time ... the account's `evidence` key reads `unread`, with the reason, and is never omitted silently" | **Decomp cell:** `IB-pr-607` (decomposition section 233) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-443`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~443 <0.9.0_WK_IRPT_BCKEND~443@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/ data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`, `infra/logic/registry`, `org/standards`; the file `data/firm_registry.json` is needed by the registry lookup).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-607` (inlined).** IB-pr-604 (merged @f888350689; commit `0a745b842b` is the worker's change) added three `ABSENT-AT-SOURCE-D` spans to `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: `_absent_smartx_map_ids` and `_absent_add_smartx_evidence` (the 49 Financial reader's SmartX read, which today returns nothing and adds NO key when the map partition is missing, empty, lacks `account_number`, or the read raises), the provider hook in `_absent_provider`, and the listing hook in `_absent_scope_listing` (which writes `"evidence": "smartx_map_present"` into an exempted account's entry when the account is in `smartx_map_ids`). The CTO half of the addendum (signed, condition 2) forbids the silent omission: **a SmartX read that fails or is refused at run time leaves the exemption decision exactly as it is, and each exempted account's manifest entry carries `"evidence": "unread"` and `"evidence_reason": "<category>"`.** The SmartX read stays evidence and never a gate: no decision, node, floor or threshold depends on it; no permission change rides. LOCAL, code and tests, nothing run against AWS.

What this cell changes, and only this (all inside `ABSENT-AT-SOURCE-D` spans; with every D span removed the file must import and equal `holdings_snapshot.py` as it stood at commit `e2700915d2`, before IB-pr-604):
1. **Record the failure, never a silent skip.** When `_absent_add_smartx_evidence` runs for the 49 Financial reader and does NOT obtain a map, it sets `evidence["smartx_map_unread"]` to one reason CATEGORY string from exactly this set: `no_overlay_clock` (the snapshot carries no `overlay_as_of`), `partition_missing_or_empty` (the partition is absent or empty), `no_account_number_column`, or `read_error:<ExceptionClassName>` (the read raised: the exception CLASS NAME only, matching `[A-Za-z0-9_]+`; never the message, never an id, never a key). A successful read sets `smartx_map_ids` as today and never `smartx_map_unread`. Do not change which firms run the reader: a firm whose builder has no SmartX reader (Cottonwood, Inflection) still gets NO new key and its manifest stays byte-identical.
2. **The entry.** In the listing hook, for each exempted account: if its id is in `smartx_map_ids`, `"evidence": "smartx_map_present"` as today; else if the evidence carries `smartx_map_unread`, `"evidence": "unread"` and `"evidence_reason": <that category>`; else (the read succeeded and does not show the account) NO evidence key, as today.
3. **What does NOT change:** `absent_at_source_exempt`'s decision for every input; `ABSENT_AT_SOURCE_FLOOR_PERCENT`; the two-day threshold; the gate's conditions; `publication.py`; the CUSIP lines; the one-date bypass; the node set; Cottonwood's and Inflection's manifest bytes; the `smartx_map_present` behaviour.

**Marking.** Every added or changed span sits between a line `# BEGIN ABSENT-AT-SOURCE-D` and a line `# END ABSENT-AT-SOURCE-D`. Keep each span small and self-contained (a later cell re-applies the spans onto the transplanted 49 Financial file).

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the three D spans, `_absent_provider`, `_absent_scope_listing`), and the existing tests `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py` (IB-pr-604's; its fixtures stay), `test_absent_at_source_exemption.py`, `test_absent_at_source_wiring.py`, `test_absent_at_source_receipts.py`, `test_holdings_publish_gate.py`.

**Do:**
1. Edit the D spans as above.
2. **Edit the tests** in `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py` (at least 11 tests in all; synthetic ids; no AWS, no network; no assertion of any OTHER file is edited). The test `test_a_failed_or_empty_smartx_read_changes_no_decision_and_adds_no_evidence` encodes the OLD behaviour: replace it with the three tests below (its fixtures, the missing/empty/raising map arms, are reused) and keep the other eight of IB-pr-604's tests under their names unchanged. Reference the new names only INSIDE test functions, so that with the D spans removed the file still collects and fails on assertions:
   - `test_a_failed_smartx_read_gives_evidence_unread_with_a_reason_and_changes_no_decision`: a map read that raises (use two exception classes, one a stand-in for a refused grant): the exemption decision equals the base decision on the same custody evidence, the node set is unchanged, and each exempted account's entry carries `"evidence": "unread"` and `"evidence_reason": "read_error:<the class name>"`.
   - `test_a_missing_or_empty_map_gives_evidence_unread_with_a_reason`: a missing partition and an empty one each give `unread` with `partition_missing_or_empty`; a map frame without `account_number` gives `no_account_number_column`; a snapshot without `overlay_as_of` gives `no_overlay_clock`; in every arm the decision is the base decision.
   - `test_the_unread_reason_is_a_category_with_no_identifier`: every `evidence_reason` produced in the arms above matches `^(no_overlay_clock|partition_missing_or_empty|no_account_number_column|read_error:[A-Za-z0-9_]+)$`, and an exception whose MESSAGE holds a synthetic account id leaves that id out of the entry (the whole manifest list serialised holds no synthetic id other than the entry's own `account_id`).
   Also confirm, in the existing `test_account_not_in_smartx_is_exempt_without_an_evidence_key`, that a SUCCESSFUL read that does not show the account still adds no key.
   **AMENDMENT 1 (issuer, 2026-10-15 ~22:5xZ, on your row W443-S1): the wiring test's expected entry changes.** `test_absent_at_source_wiring.py::test_published_manifest_carries_absent_at_source_never_closed` runs 49 Financial's `run_firm` on a fixture that writes NO SmartX map, so the reader finds a missing partition: under the CTO's condition the entry MUST read `"evidence": "unread"` and `"evidence_reason": "partition_missing_or_empty"`. That ONE test's expected dict gains exactly those two keys (nothing else in it, and no other assertion of that file or of any other existing test changes); the `"closed" not in` assertion stays. This is the only existing assertion this order may edit besides the replaced test. The category `partition_missing_or_empty` also covers a partition whose rows hold no usable account number (your row W443-S2): keep that, and say so in a comment on the category.
3. If you cannot find where a refused read surfaces (it must reach `_absent_add_smartx_evidence` as an exception from the read), STOP on that part, file a row with what you ruled out, and write what you have; never loosen a threshold.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~443/IB238-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":[the ten test names the check lists as required, exactly as the check's list holds them],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is (file, function, D span count); the sparse directories you added; the reason categories your code can produce"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters. The ten required names are: `smartx_present_account_absent_two_days_is_exempt_with_evidence`, `account_absent_one_day_is_not_exempt_even_with_a_smartx_row`, `account_with_positions_on_either_day_is_not_exempt_with_a_smartx_row`, `account_not_in_smartx_is_exempt_without_an_evidence_key`, `a_failed_smartx_read_gives_evidence_unread_with_a_reason_and_changes_no_decision`, `a_missing_or_empty_map_gives_evidence_unread_with_a_reason`, `the_unread_reason_is_a_category_with_no_identifier`, `a_firm_with_no_smartx_reader_has_a_byte_unchanged_manifest`, `the_evidence_id_form_matches_the_custody_id_form`, `the_floor_and_the_two_day_threshold_are_unchanged`. Name the test count and the D span count in your final message.

**The difference control (criterion 2).** The check requires the three new `unread` tests to exist, then removes every `ABSENT-AT-SOURCE-D` span IN MEMORY from `holdings_snapshot.py` and runs YOUR test file: it must then FAIL on ASSERTIONS, not on an import or collection error.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB238-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product file, tests, record and criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB238-1-AC1" cell_refs="IB-pr-607"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r238/p238_cells.py" . IB238-1-AC1</invocation><expect>IB238-1-AC1 PASS</expect></criterion>
<criterion id="IB238-1-AC2" cell_refs="IB-pr-607"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r238/p238_cells.py" . IB238-1-AC2</invocation><expect>IB238-1-AC2 PASS</expect></criterion>
<criterion id="IB238-1-AC3" cell_refs="IB-pr-607"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r238/p238_cells.py" . IB238-1-AC3</invocation><expect>IB238-1-AC3 PASS</expect></criterion>

<expected_criteria>IB238-1-AC1, IB238-1-AC2, IB238-1-AC3</expected_criteria>

What the checks grade: AC1 the test file (at least 11 tests) and the existing publish-gate, exemption, wiring, receipts and bypass tests pass; AC2 the three `unread` tests exist and, with the ABSENT-AT-SOURCE-D spans removed, the test file fails on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the ten named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write `holdings_snapshot.py`, the test file named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test outside the one test replaced above and the one wiring-test dict of AMENDMENT 1 stays green and no other existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test (other than the one replaced above and the one wiring-test dict of AMENDMENT 1) that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file; a need to change `absent_at_source_exempt`'s decision, the floor or the threshold, or to make any decision depend on the SmartX read. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W443-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_receipts.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-607.smartx-evidence-unread.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~443/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 233 (round 5, workstream ~PL), cell `IB-pr-607`.
<owned_cells>IB-pr-607</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB238-1-AC1, IB238-1-AC2, IB238-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~443/IRPT_BCKEND.TO-IB-pr-607.smartx-evidence-unread.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository module and its test file; nothing is deployed, minted or written to AWS; the change reaches a served byte only through the addendum candidate (a later read cell) and its apply, and it changes only the manifest entry's evidence keys (no gate decision, no node).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the CTO half forbids an IAM change riding here.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p238_cells.py IB238-1 dry-run at base on dell2 2026-10-15 ~22:5xZ: AC1, AC2, AC3 FAIL (the unread tests do not exist; AC2 refuses to grade without them). Positive control (control238.py) in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; the negatives each fail their own arm; 0 unexpected.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~443` (worktree `C:/dev/wk-IRPT_BCKEND-443`). Class LOCAL.
</preflight>
