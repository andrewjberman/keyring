# TO IRPT_BCKEND.TO-IB-pr-582 -- The source receipts record the absent_at_source exemption's evidence reads: after the gate, re-take the receipts when the provider read anything and carry them into _source_objects and the revision digest

<to_id>IRPT_BCKEND.TO-IB-pr-582</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~424</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PK</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8359 item 4 (CVO v120; row W420-S1) | **Decomp cell:** `IB-pr-582` (decomposition section 215) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-424`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~424 <0.9.0_WK_IRPT_BCKEND~424@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Cell `IB-pr-582` (inlined).** IB-pr-577 (merged @95ca50c91e) wires the `absent_at_source` evidence readers into `run_firm`. `run_firm` freezes the source receipts BEFORE the gate (near the line `receipts = inputs.receipts()` and the `snapshot["_source_objects"] = receipts` assignment, with the `irpt-source-objects` entry of `snapshot["source_set_revision"]` carrying `digest(canonical_bytes(receipts))`). The evidence reads happen inside the gate (the provider), after that freeze, so the prior-day objects the exemption reads are NOT in the receipts and NOT in the revision digest (your colleague's row W420-S1). The CTO ruled (msg 8359 item 4): the receipts record the exemption's evidence reads. This cell makes that so, LOCAL, offline, with tests.

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`run_firm` near lines 3188 to 3420: the receipts freeze, the gate call, the `ABSENT-AT-SOURCE-B` blocks, `_absent_provider`, `_absent_scope_listing`, `land`), `data/assets/scripts/gold/investor_reporting/source_inputs.py` (`VersionedInputs`: what `receipts()` returns, whether it accumulates every read including later ones, and how a read is keyed with its version id), `infra/aws/lambda/investor-reporting/holdings/publication.py` (how `source_objects` and `source_set_revision` are published), and the tests `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py` and `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py` (the `fire` harness and the `_Inputs` stub: extend the stub in YOUR new test file, never edit the existing ones).

**Change (all new logic inside `# BEGIN ABSENT-AT-SOURCE-C` ... `# END ABSENT-AT-SOURCE-C` lines in `holdings_snapshot.py`; the module must stay importable with the blocks removed):** after the gate and the listing, and ONLY when the evidence provider was called (`absent_captured` is not empty), take `inputs.receipts()` again; if it holds receipts the first freeze did not, replace `snapshot["_source_objects"]` with the new list and replace the `irpt-source-objects` row of `snapshot["source_set_revision"]` with one whose revision is the digest of the new list (same `source` name, same position, same `completion_date`). A run in which the provider was not called, or in which it read nothing new, leaves `_source_objects` and the revision row byte-identical. The recorded evidence keys carry their pinned version ids as every other receipt does. If `VersionedInputs.receipts()` does not accumulate later reads, or the stub in a test cannot show it, STOP with a row naming what you found (the issuer amends the grant).

**Write the tests** `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_receipts.py` (at least 8 tests; synthetic ids and keys; the harness of `test_holdings_publish_gate.py`): `test_evidence_reads_are_recorded_in_the_source_objects`, `test_source_set_revision_digest_covers_the_evidence_reads`, `test_no_evidence_read_leaves_source_objects_unchanged`, `test_recorded_evidence_keys_carry_the_pinned_version_ids`, `test_refused_run_publishes_nothing_extra`, `test_second_fire_records_its_own_evidence_reads`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~424/IB219-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["evidence_reads_are_recorded_in_the_source_objects","source_set_revision_digest_covers_the_evidence_reads","no_evidence_read_leaves_source_objects_unchanged","recorded_evidence_keys_carry_the_pinned_version_ids","refused_run_publishes_nothing_extra","second_fire_records_its_own_evidence_reads"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `ABSENT-AT-SOURCE-C` block IN MEMORY from the product file and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB219-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB219-1-AC1" cell_refs="IB-pr-582"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py" . IB219-1-AC1</invocation><expect>IB219-1-AC1 PASS</expect></criterion>
<criterion id="IB219-1-AC2" cell_refs="IB-pr-582"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py" . IB219-1-AC2</invocation><expect>IB219-1-AC2 PASS</expect></criterion>
<criterion id="IB219-1-AC3" cell_refs="IB-pr-582"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py" . IB219-1-AC3</invocation><expect>IB219-1-AC3 PASS</expect></criterion>

<expected_criteria>IB219-1-AC1, IB219-1-AC2, IB219-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 8) and the existing tests named in the paths block pass; AC2 with the ABSENT-AT-SOURCE-C blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the files named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W424-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_receipts.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-582.receipts-evidence.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~424/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 215 (round 1, workstream ~PK), cell `IB-pr-582`.
<owned_cells>IB-pr-582</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB219-1-AC1, IB219-1-AC2, IB219-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~424/IRPT_BCKEND.TO-IB-pr-582.receipts-evidence.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file and adds tests in the repository; nothing is deployed or run against a served prefix, so no served byte moves; the release is a later act under the never-widen pairs.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p219_cells.py IB219-1 dry-run at base on dell2 2026-10-15 ~15:0xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~424` (worktree `C:/dev/wk-IRPT_BCKEND-424`). Class LOCAL.
</preflight>
