# TO IRPT_BCKEND.TO-IB-pr-604 -- ADDENDUM 1 of the holdings exemption: an account the candidate day's SmartX map shows, absent from both custody tables, is exempted with the evidence `smartx_map_present` named in the manifest; the two-consecutive-day threshold and the 95 percent floor unchanged (CTO ADDENDUM 1 @9fef489152, msg 8644). RE-CUT of the join-fix order, whose premise failed (rows W440-S1 to S3).

<to_id>IRPT_BCKEND.TO-IB-pr-604</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~441</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ADDENDUM 1 to the round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_LANES_PJ4_PJ5_PM1_PN2_PN3_PO8_20261015.md` (@9fef489152, msg 8644: item 1 rule change as its own addendum pair, item 4 "IB-pr-604's order is re-cut as that build") | **Decomp cell:** `IB-pr-604` (decomposition section 229, re-cut in section 231) | **outcome_ref:** FWD-21

**RE-CUT (issuer, 2026-10-15 ~21:1xZ).** The order first read "fix the 49 Financial account join". Worker `~440` measured that no join key is wrong (candidate-day custody holds 0 balance and 0 position rows for the one lost account under every key form; the prior day held 1 and 13; the candidate day's SmartX map holds 1 row) and stopped (rows `IRPT_BCKEND-D2-W440-S1` to `S3`, drained @6c58d386ab). The CTO ruled the treatment (msg 8644). The cell, the criterion ids and the check file name stay; the cell text, the test file, the marker (`ABSENT-AT-SOURCE-D`), the record slot (`~441`) and the named tests change. The candidate-bundle rebuild with this commit added is a LATER read cell (it needs this commit), then the addendum pair packet.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-441`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~441 <0.9.0_WK_IRPT_BCKEND~441@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/ data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`, `infra/logic/registry`, `org/standards`; the file `data/firm_registry.json` is needed by the registry lookup).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use (`holdings_49f.SOURCE_BUCKET`, `holdings_49f.SMARTX_PREFIX`).

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-604` (inlined).** The absent_at_source exemption (`ABSENT-AT-SOURCE-A`, `-B`, `-C` in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`) exempts a lost account only when the source shows it with NO positions in BOTH custody tables (`positions` and `balance`) on the candidate day AND the prior trading day, every one of those four partitions at least 95 percent complete (`absent_at_source_exempt`; `ABSENT_AT_SOURCE_FLOOR_PERCENT`). For 49 Financial the one remaining lost account is absent on the candidate day and present on the prior day, so it is not eligible today, by design; the CTO ruled (msg 8644): **an account the candidate day's SmartX map shows, and that is absent from both custody tables on the candidate day and the prior day, is exempt-eligible, and the manifest names the SmartX presence as the evidence.** A SmartX row shows the account exists; the exemption never lists it as `closed`. The two-consecutive-day threshold (one absent day is NOT eligible) and the 95 percent floor are NOT changed; (c) "emit it listed outside the exemption" is refused (two rules for one state). LOCAL, code and tests, nothing run against AWS.

What this cell builds, and only this:
1. **The SmartX evidence read (49 Financial's reader only).** Where `_absent_evidence` (or the function that calls it) builds the evidence for the 49 Financial builder, also read the SmartX account map partition the BUILD read: the key is `holdings_49f.SMARTX_PREFIX + "fact_allocation_account_map/date=<overlay_date>/data.parquet"` in `holdings_49f.SOURCE_BUCKET`, the partition `holdings_49f.load_49f_sources` picks with `_latest_date_partition(..., as_of=...)` for the same cutoff, read through the same `VersionedInputs` object so the pinned bytes are the ones the build read. Reduce it to the SET of served account ids it shows (any row of the map counts, whatever its allocation status), keyed EXACTLY as the served account id of the same account is formed (`opaque_id("account", long_id, ...)`; read `holdings_49f._smartx_overlay` and `holdings_49f.build_49f_actual` for how the builder joins `account_number` (padded to 10 by `_pad10`) to the custody account text, and use the same form: a test proves a synthetic map id and a synthetic custody id of the same account give the same served id). Keep the set in the evidence under a new key, `smartx_map_ids`. A firm whose builder has no SmartX reader (Cottonwood, Inflection) gets no new key. Any missing, empty or unreadable map leaves `smartx_map_ids` ABSENT from the evidence and decides nothing else: the exemption decision never depends on SmartX.
2. **The evidence in the manifest.** `absent_at_source_record` writes each exempted account's entry; when the account's served id is in `smartx_map_ids`, the entry gains the key `"evidence": "smartx_map_present"`; otherwise the entry is byte-identical to the one the base code writes (no key, not null). Thread the set to the entry through the gate's `listed` details or the captured evidence the listing already uses (read `_absent_provider`, `_absent_scope_listing`, `absent_at_source_exempt` and `evaluate_publish_gate`); do not change `absent_at_source_exempt`'s decision.
3. **What does NOT change:** `absent_at_source_exempt`'s decision for every input (a test compares it with and without the new key on the same evidence); `ABSENT_AT_SOURCE_FLOOR_PERCENT`; the two-day threshold; the gate's other conditions; `publication.py` (it passes the manifest list through untouched; do not edit it); the CUSIP lines; the one-date bypass; Cottonwood's and Inflection's manifest bytes; the listing node (a zero-value ACCOUNT node, the not-reported words).

**Marking the change.** Every added or changed span of `holdings_snapshot.py` sits between a line `# BEGIN ABSENT-AT-SOURCE-D` and a line `# END ABSENT-AT-SOURCE-D` (they may sit INSIDE the existing `-A`, `-B` or `-C` blocks, on their own lines). With every D span removed the file must import and be the old file (the difference control). Add no line outside a D span. (The candidate rebuild applies exactly these spans onto the transplanted 49 Financial file, so keep each span small and self-contained.)

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`absent_at_source_exempt`, `absent_at_source_record`, `_absent_evidence`, `_absent_spec_49f`, `source_evidence_for`, `_absent_provider`, `_absent_scope_listing`, `evaluate_publish_gate` near line 3312, `run_firm`), `data/assets/scripts/gold/investor_reporting/holdings_49f.py` (`load_49f_sources`, `_smartx_overlay`, `build_49f_actual`, `SMARTX_PREFIX`, `SOURCE_BUCKET`, `_text`), and the existing tests `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py`, `test_absent_at_source_wiring.py`, `test_absent_at_source_receipts.py`, `test_holdings_publish_gate.py` (copy their fixture style: synthetic frames, no AWS).

**Do:**
1. Write the D spans as above.
2. **Write the tests** `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py` (at least 8 tests; synthetic ids; no AWS, no network). These eight names are required, each a test function; reference the new names only INSIDE test functions (never at import time), so that with the D spans removed the file still collects and fails on assertions:
   - `test_smartx_present_account_absent_two_days_is_exempt_with_evidence`: a lost synthetic account in the SmartX set, with no positions in both tables on both days, partitions complete: exempt, and its manifest entry carries `"evidence": "smartx_map_present"` and the base fields unchanged.
   - `test_account_absent_one_day_is_not_exempt_even_with_a_smartx_row`: absent on the candidate day, positions on the prior day, in the SmartX set: NOT exempt (the gate still raises `account_lost`); no manifest entry.
   - `test_account_with_positions_on_either_day_is_not_exempt_with_a_smartx_row`: positions on the candidate day only, and on the prior day only: each NOT exempt.
   - `test_account_not_in_smartx_is_exempt_without_an_evidence_key`: absent two days, not in the set: exempt exactly as at the base; its entry has no `evidence` key at all.
   - `test_a_failed_or_empty_smartx_read_changes_no_decision_and_adds_no_evidence`: a map that is missing, empty, or raises: the exemption decision equals the base decision on the same custody evidence, and no entry carries `evidence`.
   - `test_a_firm_with_no_smartx_reader_has_a_byte_unchanged_manifest`: the Cottonwood-shaped path (the COT builder): the manifest `absent_at_source` bytes are equal to what the removed-D base code writes for the same input (compute the base arm in the test by calling `absent_at_source_record` on an entry set with no SmartX key).
   - `test_the_evidence_id_form_matches_the_custody_id_form`: a synthetic SmartX `account_number` and a synthetic custody `account_id` of the same account (the padding the builder uses) give the same served id.
   - `test_the_floor_and_the_two_day_threshold_are_unchanged`: `ABSENT_AT_SOURCE_FLOOR_PERCENT` equals 95, a partition at 94 percent of the prior day's count never exempts, and `absent_at_source_exempt` returns the same `(exempt, details)` for the same evidence with and without a `smartx_map_ids` key.
3. If you cannot find where the SmartX partition the build read can be re-read through `VersionedInputs`, or the id form, STOP on that part, file a row with what you ruled out (names only), and write what you have; the check then fails honestly; never estimate and never loosen a threshold.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~441/IB235-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["account_absent_one_day_is_not_exempt_even_with_a_smartx_row","account_with_positions_on_either_day_is_not_exempt_with_a_smartx_row","a_failed_or_empty_smartx_read_changes_no_decision_and_adds_no_evidence","the_floor_and_the_two_day_threshold_are_unchanged"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is (file, function, D span count); the sparse directories you added; the first absent day the evidence gave in your fixture"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters. Name the eight test names in your final message, with the count of D spans.

**The difference control (criterion 2).** The check removes every `ABSENT-AT-SOURCE-D` span IN MEMORY from `holdings_snapshot.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB235-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product file, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB235-1-AC1" cell_refs="IB-pr-604"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py" . IB235-1-AC1</invocation><expect>IB235-1-AC1 PASS</expect></criterion>
<criterion id="IB235-1-AC2" cell_refs="IB-pr-604"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py" . IB235-1-AC2</invocation><expect>IB235-1-AC2 PASS</expect></criterion>
<criterion id="IB235-1-AC3" cell_refs="IB-pr-604"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py" . IB235-1-AC3</invocation><expect>IB235-1-AC3 PASS</expect></criterion>

<expected_criteria>IB235-1-AC1, IB235-1-AC2, IB235-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 8) and the existing publish-gate, exemption, wiring, receipts and bypass tests pass; AC2 with the ABSENT-AT-SOURCE-D spans removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write `holdings_snapshot.py`, the test file named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file; a need to change `absent_at_source_exempt`'s decision, the 95 percent floor or the two-day threshold (the CTO ruled them unchanged). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W441-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_smartx_evidence.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_receipts.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-604.account-join-49f.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~441/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 229 (round 3, workstream ~PL), cell `IB-pr-604`, re-cut in section 231.
<owned_cells>IB-pr-604</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB235-1-AC1, IB235-1-AC2, IB235-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~441/IRPT_BCKEND.TO-IB-pr-604.account-join-49f.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository module and its tests; nothing is deployed, minted or written to AWS; the change reaches a served byte only through the 49 Financial addendum candidate (a later read cell) and the addendum pair's apply, and it changes only a manifest entry's evidence key (no gate decision).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p235_cells.py IB235-1 dry-run at base on dell2 2026-10-15 ~21:1xZ after the re-cut: AC1, AC2, AC3 FAIL (no work, no record). Positive control (control235.py) in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; the negatives each fail their own arm; 0 unexpected.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~441` (worktree `C:/dev/wk-IRPT_BCKEND-441`). Class LOCAL.
</preflight>
