# TO IRPT_BCKEND.TO-IB-pr-508 -- the runner jsonschema tolerance test's import order is repaired so the three builder suites run together (row D2-W356-S3; CTO round-175 analysis section 2)

<to_id>IRPT_BCKEND.TO-IB-pr-508</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~360</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>175</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-175 ANALYSIS (msg 6829) section 2 (row D2-W356-S3) and section 3 item 2 | **Decomp cell:** `IB-pr-508` (decomposition section 167) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-508` (inlined):** `data/assets/scripts/gold/investor_reporting/tests/test_runner_jsonschema_tolerance.py` cannot be collected at all, alone or with other suites: at lines about 40 to 46 it REMOVES the repository's `.tools` directory from `sys.path` (so collection of other test modules does not see `.tools` first), and then, at line 46, imports `safe_deploy_core`, which lives only in `.tools`: `ModuleNotFoundError: No module named 'safe_deploy_core'`. Measured at base: `python -m pytest <that file> -q` reads `1 error`; the combined run with `test_holdings_49f.py` (22 pass alone) and `test_holdings_inf.py` (14 pass alone) stops at collection, rc 2. **Repair the import order in that ONE file** so it collects and passes alone and with the other two, without leaving `.tools` on `sys.path` for later modules (the file's comment says why it removes it: row W42-S3). A minimal shape: import `safe_deploy_core` BEFORE the lines that remove `.tools` from the path (so the import happens while `.tools` is present), or load it by `importlib` from its file path inside the function that needs it (`_runtime_py_members`), leaving the path untouched. Choose the smaller edit. BUILD ONLY: no AWS call, no deploy; the test reads the deploy guard's bundle declaration only.

**Do:**
1. Read the file (head and the helper `_runtime_py_members`) and the guard's `find_bundle("investor_reporting")`; make the smallest edit that makes the file collectable and passing; change no assertion and no other file. `git rev-parse HEAD` before your first edit is `base_commit` (state it).
2. Run the file alone, then the three suites together, then `test_holdings_49f.py` and `test_holdings_inf.py` each alone; report counts.
3. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~360/IB175-2_import_order.json`: `{"base_commit":"<40-hex>","edit":"one sentence on what moved","alone":{"passed":N},"together":{"passed":N},"sys_path_has_tools_after_import":false}`; the last field is the result of a one-line check you run: after importing the test module, `.tools` is NOT on `sys.path`.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB175-2-AC1" cell_refs="IB-pr-508"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py" . IB175-2-AC1</invocation><expect>IB175-2-AC1 PASS</expect></criterion>
<criterion id="IB175-2-AC2" cell_refs="IB-pr-508"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py" . IB175-2-AC2</invocation><expect>IB175-2-AC2 PASS</expect></criterion>
<criterion id="IB175-2-AC3" cell_refs="IB-pr-508"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py" . IB175-2-AC3</invocation><expect>IB175-2-AC3 PASS</expect></criterion>

<expected_criteria>IB175-2-AC1, IB175-2-AC2, IB175-2-AC3</expected_criteria>

What the checks grade: AC1 the tolerance test collects and passes alone (1 or more passed, no error); AC2 the three suites pass together (37 or more passed, rc 0); AC3 `git diff --numstat <base_commit> HEAD -- data/assets/scripts/gold/investor_reporting/` names exactly that one test file and at most 12 changed lines. Do not edit the checks. Do NOT run the whole `tests/` folder (one test in it makes live read-only AWS calls).

## BOUNDS

- **Grant:** the `paths` block and nothing else. Edit exactly the one test file; no other test, no product code, no deploy, no AWS call.
- **Refusal clause:** STOP, file a row, change nothing more, if the repair needs a change to any file other than that test, or if making it collect changes a test outcome other than turning the collection error into passes (name what).
- **Row ids** are `IRPT_BCKEND-D2-W360-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
data/assets/scripts/gold/investor_reporting/tests/test_runner_jsonschema_tolerance.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~360/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-508.tolerance-test-import-order-repair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 167 (round 175, workstream ~P), cell `IB-pr-508`.
<owned_cells>IB-pr-508</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB175-2-AC1, IB175-2-AC2, IB175-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~360/IRPT_BCKEND.TO-IB-pr-508.tolerance-test-import-order-repair.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one gold-runner test file; nothing is deployed from this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p175_cells.py dry-run at base on dell2 2026-10-13 ~07:0xZ: IB175-2 AC1 FAIL (0 passed, 1 error), AC2 FAIL (rc 2, collection error), AC3 FAIL (no record). Measured at base: test_holdings_49f.py 22 passed, test_holdings_inf.py 14 passed.
lane: the paths block IS the grant; worker slot ~360 of IRPT_BCKEND. Class LOCAL.
</preflight>
