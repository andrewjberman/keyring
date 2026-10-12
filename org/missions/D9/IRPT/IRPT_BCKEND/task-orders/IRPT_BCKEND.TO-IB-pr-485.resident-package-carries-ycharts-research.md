# TO IRPT_BCKEND.TO-IB-pr-485 -- BUILD ONLY: `ycharts/research` rides the resident package, proven by a test that resolves every import `build_resident_runtime` makes on BOTH binding branches

<to_id>IRPT_BCKEND.TO-IB-pr-485</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~340</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>167</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6517 (PRD ADDENDUM v0.51 section 2 item 4; ROUND-166 ANALYSIS section 3a, ruling on row D2-W333-S1) | **Decomp cell:** `IB-pr-485` (decomposition section 159) | **outcome_ref:** FWD-8

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-340/` (bash `/c/dev/wk-irpt-bckend-340`). Work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call, nothing built into a deployable package and uploaded, no host touched, no Lambda invoked. The package is staged only into a temp directory inside a test and removed after.

**Why.** `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` stages `DIRS` (about lines 37-38: `_scope, _ids, _keys, _authz, _contracts, intake, ops, reports, ycharts/generate, ycharts/session, ycharts/extract`) and not `ycharts/research`. `reports/resident_installed.py` lists `commentary_ready_queue_url` as an OPTIONAL binding (about line 50) and `build_resident_runtime` (about lines 345-346) imports
`opal_packager` (`ycharts/research/opal_packager.py`) when the bindings carry it. A module the runtime imports on any binding branch is part of the package; otherwise switching the binding on fails at import, on the host, not at build. The CTO ruled: YES, `ycharts/research` rides the resident package (analysis section 3a). The live host's bindings are READ in another order (to the cloud-ops seat); you do not touch the host.

**Build.**
1. Add `ycharts/research` to `DIRS` in `build_resident_package.py`. Read what else the builder does per directory first (the per-directory tracked-file listing, any exclusions such as tests, and the manifest it writes) and keep the new directory consistent with how `ycharts/generate` is handled; state any difference in the record.
2. A test that STAGES the package (call the builder's staging function(s) into a temp directory without uploading anything; read how `reports/tests/test_resident_packager_binding.py` and the other tests in `reports/tests/` drive `build_resident_runtime`) and resolves EVERY import `build_resident_runtime` makes, on BOTH branches: (a) bindings WITHOUT `commentary_ready_queue_url`; (b) bindings WITH it. Resolution means: with only the staged tree on `sys.path` (run it in a subprocess so the repo's own tree is not importable), `build_resident_runtime` is called with fake clients as the existing tests do, and both branches construct without an `ImportError`.
   Difference control: run branch (b) against the package staged from the BASE `DIRS` (a copy of the builder at `base_commit`) and show it fails with an `ImportError` naming `opal_packager`.

**Tests (the build's own):** `infra/aws/lambda/investor-reporting/reports/tests/test_resident_package_imports.py`, at least THREE tests: the staged package contains `ycharts/research/opal_packager.py`; branch (a) resolves; branch (b) resolves; plus the difference control as a test or in the record. The reports folder reads `202 passed` at base; after, no failure and at least 202 passed.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~340/IB167-5_resident_dirs_record.json`: `{base_commit, files_changed, dirs_before:[...], dirs_after:[...], per_directory_handling_difference_in_words, imports_resolved_both_branches:true, difference_control:{branch_b_on_base_dirs:"ImportError opal_packager"}, hash_pins:[every place in the repo that pins a hash of a file you changed, with what you did about it],
host_reach (the resident package is installed on the host only in a resident release under its own never-widen pair; say which file the host pins), suites:{reports_before, reports_after}, request_sent:false, deployed:false}`.

<criterion id="IB167-5-AC1" cell_refs="IB-pr-485"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-5-AC1</invocation><expect>IB167-5-AC1 PASS</expect></criterion>
<criterion id="IB167-5-AC2" cell_refs="IB-pr-485"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-5-AC2</invocation><expect>IB167-5-AC2 PASS</expect></criterion>
<criterion id="IB167-5-AC3" cell_refs="IB-pr-485"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-5-AC3</invocation><expect>IB167-5-AC3 PASS</expect></criterion>

<expected_criteria>IB167-5-AC1, IB167-5-AC2, IB167-5-AC3</expected_criteria>

What the checks grade: AC1 your new test file exists and at least 3 tests pass; AC2 the regression guard (it PASSes at base BY DESIGN): the reports folder reads at least 202 passed and 0 failed; AC3 the record: `ycharts/research` in `dirs_after` and not in `dirs_before`, `imports_resolved_both_branches` true, the builder names `ycharts/research`, `request_sent` and `deployed` false, and nothing outside `reports/`, your deliverables, rows and order changed.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. The packager (`opal_packager.py`), the accessor and the host are not yours.
- **Refusal clause:** if staging the package needs a write outside a temp directory, or branch (b) cannot be made to fail on the base `DIRS`, STOP, file a row and report; do not weaken a test. Never weaken a check; do not edit `p167_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W340-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~340" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~340@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~340 <0.9.0_WK_IRPT_BCKEND~340@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/reports/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~340/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-485.resident-package-carries-ycharts-research.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 159 (round 167, workstream ~P), cell `IB-pr-485`.
<owned_cells>IB-pr-485</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB167-5-AC1, IB167-5-AC2, IB167-5-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~340/IRPT_BCKEND.TO-IB-pr-485.resident-package-carries-ycharts-research.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; `DIRS` before and after; how the builder handles the new directory against `ycharts/generate`; the three-plus tests and the difference control; the reports folder's last line before and after; the hash pins found and what you did; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell adds one directory to a package builder's list and a test in the repo; no package is built for a host, uploaded or installed.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p167_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~20:4xZ: IB167-5 AC1 FAIL (the new test is absent), AC2 PASS (the regression guard: reports 202 passed), AC3 FAIL (no record); commit-gate clean. The issuer read the DIRS list (build_resident_package.py lines 37-38) and the optional binding comment in resident_installed.py; the CTO read the runtime's import at lines 345-346.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
