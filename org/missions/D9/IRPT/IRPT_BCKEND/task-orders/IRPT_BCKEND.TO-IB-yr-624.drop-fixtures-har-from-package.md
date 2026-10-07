# TO-IB-yr-624 -- irpt-ycharts-generate's package drops the 14 fixtures/har members

<to_id>IRPT_BCKEND.TO-IB-yr-624</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~151</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-624` (`decompositions/IRPT_BCKEND_DECOMP_R62_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` has one row per Lambda. The row `irpt-ycharts-generate` has a `files` list (114
entries) that the builder zips from `infra/aws/lambda/investor-reporting/ycharts/generate/`. Fourteen entries are test fixtures
that no runtime code reads: `fixtures/har/FIXTURE_MANIFEST.json`, `collection.json`, `create_201.json`, `create_422_fee.json`,
`dashboard.json`, `decision_branches.json`, `generate_201.json`, `generate_404_minimal.json`, `report.pdf`, `status_drifted.json`,
`status_ok.json`, `templates.json`, `upload_ok.json` and `validate_200.json` (all under `fixtures/har/`).

**Your cell: remove exactly those 14 entries from that row's `files` list.**
- Keep the top-level `templates.json`; it is a different file and runtime code reads it.
- Change nothing else in the row and no other row.
- Keep the file's formatting: an edit of the 14 lines only, no re-serialization of the whole JSON.
- Delete no fixture file and change no test.

**Why:** the CTO's round-61 analysis @aae1ed7781 item E-Y4. The round-61 owner table found them packaged and test-only.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y62-4-AC1" cell_refs="IB-yr-624"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/R62_checks/check_624_fixtures_dropped.py --trace</invocation><expect>PASS: 0 runtime readers of fixtures across 184 packaged text members</expect></criterion>

<criterion id="Y62-4-AC2" cell_refs="IB-yr-624"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/R62_checks/check_624_fixtures_dropped.py --package --base df522860d7</invocation><expect>PASS: files[] carries 0 fixtures/har members (100 members); 0 test or fixture files changed</expect></criterion>

<criterion id="Y62-4-AC3" cell_refs="IB-yr-624"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/R62_checks/check_624_fixtures_dropped.py --trace --plant</invocation><expect>FAIL: 1 runtime reader(s) of fixtures across 185 packaged text members</expect></criterion>

<expected_criteria>Y62-4-AC1,Y62-4-AC2,Y62-4-AC3</expected_criteria>

**Issuer's base run at dell2 CLOUD df522860d7:**
- AC1: PASS, 0 readers across 184 text members, and the same after your change (the trace never counts fixtures/har members).
  The issuer simulated the change on a copy and read 184 / 100 / 185 for AC1-AC3.
- AC2: FAIL as expected (14 fixtures/har members packaged, 0 test or fixture files changed).
- AC3: the control, FAIL as expected: 1 reader across 185 members, before and after your change.

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- a 14-line deletion from a package list, graded by a trace whose control is planted; the check script was base-run on all three modes above.
comp-blast: RUN (by reading) -- the row's files[] feeds build-and-upload.sh and release-census.py for this one function only; no other row and no deployed byte moves. The next build of irpt-ycharts-generate ships 14 fewer members, under that release's own halves.
lane: the <paths> block IS the grant (worker_grant, task-order-paths). lambda-source-map.json is also in lane IRPT_COMPLETION_SOURCE_MAP, which permits 2.0.0_SA_COO~Y2, the drain's merge author.
</preflight>

## BOUNDS

- **Grant.** The `<paths>` block and this order's file. The check script is READ-ONLY.
- **No AWS call, no build, no upload, no deploy, no network call.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do
  not weaken the check.
- **Row ids** are `IRPT_BCKEND-W151-S<k>`, appended with a `## <ID> -- <one line>` heading. Re-read the channel immediately
  before writing. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~151" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~151@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~151 <0.9.0_WK_IRPT_BCKEND~151@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. Verify with `git status --porcelain <path>` (empty).
- **Search discipline:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.
- **ASCII only.**

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~151/IRPT_BCKEND.TO-IB-yr-624.drop-fixtures-har-from-package.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-624.drop-fixtures-har-from-package.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R62_Y.md</decomp_doc> round 62, workstream ~Y, cell `IB-yr-624`.
<owned_cells>IB-yr-624</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y62-4-AC1, Y62-4-AC2, Y62-4-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~151/IRPT_BCKEND.TO-IB-yr-624.drop-fixtures-har-from-package.proof_of_spec.json`,
validated with your worktree's own `python .tools/proof-of-spec-check.py <instance> Y62-4-AC1,Y62-4-AC2,Y62-4-AC3` BEFORE the
flip to complete. Copy the shape from
`deliverables/0.9.0_WK_IRPT_BCKEND~150/IRPT_BCKEND.TO-IB-yr-612.ycharts-generate-member-owners.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the `files` count before and after, the diff summary, and the commit
hash.
