# TO IRPT_BCKEND.TO-IB-pr-609 -- Every exempted account carries exactly one of three SmartX evidence values: `smartx_map_present`, `smartx_map_absent` (the map was obtained and does not show the account), or `unread` with a reason category; the decision, the floor and the threshold unchanged (CTO half of exemption ADDENDUM 1, revision note, msg 8774)

<to_id>IRPT_BCKEND.TO-IB-pr-609</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~445</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO half of the exemption ADDENDUM 1, `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_HOLDINGS_EXEMPTION_PAIR_ADDENDUM_1_CTO_HALF.md`, revision note (msg 8774): "A missing key reads the same as 'not checked', so every exempted account carries evidence = smartx_map_present | smartx_map_absent | unread (with a reason category)." | **Decomp cell:** `IB-pr-609` (decomposition section 235) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-445`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~445 <0.9.0_WK_IRPT_BCKEND~445@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/ data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`, `infra/logic/registry`, `org/standards`; the file `data/firm_registry.json` is needed by the registry lookup).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-609` (inlined).** HEAD's `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` carries three `ABSENT-AT-SOURCE-D` spans (IB-pr-604, IB-pr-607). For the 49 Financial reader, the evidence read sets `smartx_map_ids` when the SmartX account map was obtained and `smartx_map_unread` (a reason category) when it was not. The listing hook in `_absent_scope_listing` writes `"evidence": "smartx_map_present"` when the exempted account is in `smartx_map_ids`, and `"evidence": "unread"` with `"evidence_reason"` when `smartx_map_unread` is set; **when the map WAS obtained and the account is not in it, it writes NO key.** The CTO ruled that a missing key reads the same as "not checked": **that third case must write `"evidence": "smartx_map_absent"`**, so every exempted account of the 49 Financial reader carries exactly one of the three values. The SmartX read stays evidence and never a gate: no decision, node, floor or threshold depends on it; no permission change rides. LOCAL, code and tests, nothing run against AWS.

What this cell changes, and only this (inside `ABSENT-AT-SOURCE-D` spans; with every D span removed the file must import and equal `holdings_snapshot.py` as it stood at commit `e2700915d2`, before IB-pr-604):
1. **The listing hook:** for each exempted account of an evidence that carries `smartx_map_ids` or `smartx_map_unread` (i.e. the 49 Financial reader ran): if the id is in `smartx_map_ids` write `smartx_map_present`; else if `smartx_map_unread` is set write `unread` and `evidence_reason` (unchanged); else (the map was obtained and does not show the account) write `"evidence": "smartx_map_absent"` and NO `evidence_reason`. A firm whose builder has no SmartX reader (Cottonwood, Inflection) carries neither `smartx_map_ids` nor `smartx_map_unread`: its entries stay byte-identical to the base code's and get NO evidence key.
2. Keep each span small and self-contained (a later cell re-applies the spans onto the transplanted 49 Financial file).
3. **What does NOT change:** `absent_at_source_exempt`'s decision for every input; `ABSENT_AT_SOURCE_FLOOR_PERCENT`; the two-day threshold; the gate's conditions; `publication.py`; the CUSIP lines; the one-date bypass; the node set; the reason categories and their producers; the `smartx_map_present` and `unread` behaviours.

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the three D spans, `_absent_provider`, `_absent_scope_listing`), and the existing tests `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py` (its fixtures stay), `test_absent_at_source_exemption.py`, `test_absent_at_source_wiring.py`, `test_absent_at_source_receipts.py`, `test_holdings_publish_gate.py`.

**Do:**
1. Edit the D span of the listing hook as above.
2. **Edit the tests** in `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py` (at least 12 tests in all; synthetic ids; no AWS, no network; no assertion of any OTHER file is edited). The test `test_account_not_in_smartx_is_exempt_without_an_evidence_key` encodes the OLD behaviour: replace it with the two tests below and keep the other tests under their names, with their bodies unchanged except where an assertion pins "no evidence key" for a SUCCESSFUL read (update only that assertion to the new value). Reference the new names only INSIDE test functions, so that with the D spans removed the file still collects and fails on assertions:
   - `test_an_account_the_obtained_map_does_not_show_gets_evidence_smartx_map_absent`: a SUCCESSFUL read of a map that does not show the exempted account: the entry carries `"evidence": "smartx_map_absent"`, carries no `evidence_reason`, and the exemption decision equals the base decision.
   - `test_every_exempted_account_carries_exactly_one_of_the_three_evidence_values`: with a map that shows one exempted account and not another, and again with a failed read, every exempted entry's `evidence` is exactly one of `smartx_map_present`, `smartx_map_absent`, `unread`, and an `evidence_reason` appears if and only if the value is `unread`.
   Also confirm the Cottonwood-shaped test (`test_a_firm_with_no_smartx_reader_has_a_byte_unchanged_manifest`) still passes unchanged: the other firms get no evidence key.
3. In `test_absent_at_source_wiring.py`, the entry of `test_published_manifest_carries_absent_at_source_never_closed` already reads `unread` (the fixture writes no map): if an existing wiring assertion fails because of your change, STOP and file a row.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~445/IB240-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":[the eleven test names the check lists as required, exactly as the check's list holds them],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is (file, function, D span count); the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters. The eleven required names are: `smartx_present_account_absent_two_days_is_exempt_with_evidence`, `account_absent_one_day_is_not_exempt_even_with_a_smartx_row`, `account_with_positions_on_either_day_is_not_exempt_with_a_smartx_row`, `an_account_the_obtained_map_does_not_show_gets_evidence_smartx_map_absent`, `a_failed_smartx_read_gives_evidence_unread_with_a_reason_and_changes_no_decision`, `a_missing_or_empty_map_gives_evidence_unread_with_a_reason`, `the_unread_reason_is_a_category_with_no_identifier`, `every_exempted_account_carries_exactly_one_of_the_three_evidence_values`, `a_firm_with_no_smartx_reader_has_a_byte_unchanged_manifest`, `the_evidence_id_form_matches_the_custody_id_form`, `the_floor_and_the_two_day_threshold_are_unchanged`. Name the test count and the D span count in your final message.

**The difference control (criterion 2).** The check requires the two new tests to exist, then removes every `ABSENT-AT-SOURCE-D` span IN MEMORY from `holdings_snapshot.py` and runs YOUR test file: it must then FAIL on ASSERTIONS, not on an import or collection error.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB240-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product file, tests, record first; then the criteria output; then the instance alone). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB240-1-AC1" cell_refs="IB-pr-609"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r240/p240_cells.py" . IB240-1-AC1</invocation><expect>IB240-1-AC1 PASS</expect></criterion>
<criterion id="IB240-1-AC2" cell_refs="IB-pr-609"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r240/p240_cells.py" . IB240-1-AC2</invocation><expect>IB240-1-AC2 PASS</expect></criterion>
<criterion id="IB240-1-AC3" cell_refs="IB-pr-609"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r240/p240_cells.py" . IB240-1-AC3</invocation><expect>IB240-1-AC3 PASS</expect></criterion>

<expected_criteria>IB240-1-AC1, IB240-1-AC2, IB240-1-AC3</expected_criteria>

What the checks grade: AC1 the test file (at least 12 tests) and the existing publish-gate, exemption, wiring, receipts and bypass tests pass; AC2 the two new tests exist and, with the ABSENT-AT-SOURCE-D spans removed, the test file fails on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the eleven named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write `holdings_snapshot.py`, the test file named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test outside the one test replaced above stays green and no other existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test (other than the one replaced above) that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file; a need to change `absent_at_source_exempt`'s decision, the floor or the threshold, or to make any decision depend on the SmartX read. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W445-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_receipts.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-609.smartx-evidence-absent.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~445/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 235 (round 7, workstream ~PL), cell `IB-pr-609`.
<owned_cells>IB-pr-609</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB240-1-AC1, IB240-1-AC2, IB240-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~445/IRPT_BCKEND.TO-IB-pr-609.smartx-evidence-absent.proof_of_spec.json`.
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
comp-adversary: RUN -- p240_cells.py IB240-1 dry-run at base on dell2 2026-10-16 ~00:1xZ: AC1, AC2, AC3 FAIL (the two new tests do not exist; AC2 refuses to grade without them). Positive control (control240.py) in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; the negatives each fail their own arm; 0 unexpected.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~445` (worktree `C:/dev/wk-IRPT_BCKEND-445`). Class LOCAL.
</preflight>
