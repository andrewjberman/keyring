# TO-IB-yr-612 -- every unclaimed changed member of irpt-ycharts-generate gets an owner

<to_id>IRPT_BCKEND.TO-IB-yr-612</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~150</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-612` (`decompositions/IRPT_BCKEND_DECOMP_R61_Y.md`)

---

## WORKER FACE

### THE CELL

The Lambda `irpt-ycharts-generate` is packaged from `infra/aws/lambda/investor-reporting/ycharts/generate/`. A census of its
next build against the live function found 19 members that differ from live. 4 of them are owned by orders that changed them.
**15 are owned by nobody:** the 14 files under `fixtures/har/` (`FIXTURE_MANIFEST.json`, `collection.json`, `create_201.json`,
`create_422_fee.json`, `dashboard.json`, `decision_branches.json`, `generate_201.json`, `generate_404_minimal.json`, `report.pdf`,
`status_drifted.json`, `status_ok.json`, `templates.json`, `upload_ok.json`, `validate_200.json`) and the top-level `templates.json`.

**Your cell: write one owner table for those 15**, at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~150/MEMBER_OWNERS.json`. It is a JSON list with one object
per member and these keys:
- `member`: the path relative to `ycharts/generate/`, for example `fixtures/har/report.pdf`;
- `evidence_commit`: the newest commit that changed that file (`git log -1 --format=%H -- <repo path>`);
- `owner_lane`: the lane in `.owned-paths.yaml` that grants that repo path. Resolve it by reading the YAML's `paths` map, not
  by guessing from names;
- `owner_serials`: that lane's `permitted_agents`;
- `disposition`: `KEEP`, or `REMOVE` when the member should not ship in the Lambda package at all. Test fixtures are a
  candidate: say so only when the packaging rule (`files[]` of the `irpt-ycharts-generate` row in
  `infra/aws/lambda/ci/lambda-source-map.json`) shows the file is packaged and no runtime import reads it;
- `reason`: one sentence.

Change no product file. This cell writes one table and moves no bytes.

**Why:** the CTO's round analysis @e363a194ed item E-Y2 (row S337): every changed member needs an owner before that function's
next release.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y61-2-AC1" cell_refs="IB-yr-612"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/R61_checks/check_612_member_owners.py</invocation><expect>PASS: 15 of 15 members owned</expect></criterion>

<criterion id="Y61-2-AC2" cell_refs="IB-yr-612"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/R61_checks/check_612_member_owners.py --file org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/R61_checks/planted_bad_owners.json</invocation><expect>FAIL: 3 problem(s) across 1 row(s)</expect></criterion>

<expected_criteria>Y61-2-AC1,Y61-2-AC2</expected_criteria>

**Issuer's base run at dell2 CLOUD cc788ffd58:** AC1 FAIL as expected (the table is absent). AC2 prints `FAIL: 3 problem(s)
across 1 row(s)` as expected (the control): the planted lane, the planted commit and the short member set are all refused. It must
stay that way.

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; the cell writes one JSON table.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant.
comp-adversary: RUN -- `comp-adversary compose` on check_612_member_owners.py: 5 complement sources run, 0 deferred, 4 declared-excluded (v1 contract); the declaration is not a clean bill.
comp-blast: DECLARED-NOT-APPLICABLE -- no product file, no served path; the table moves ownership records only.
lane: the <paths> block IS the grant. Every path is under the worker's own deliverables, this order's file, or the append-only channel (lane ANY).
</preflight>

## BOUNDS

- **Grant.** The `<paths>` block and this order's file. The check scripts are READ-ONLY.
- **No AWS call, no deploy, no network call.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do
  not weaken the check. A member whose path no lane grants is a ROW (`owner_lane` cannot be invented), not a guess.
- **Row ids** are `IRPT_BCKEND-W150-S<k>`, appended with a `## <ID> -- <one line>` heading. Re-read the channel immediately
  before writing. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~150" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~150@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~150 <0.9.0_WK_IRPT_BCKEND~150@opal.agent>" -F <msgfile> -- <paths>`
  (dell2 has no git committer identity). Do NOT pre-`git add`. Write the message file with the Write tool. Verify with
  `git status --porcelain <path>` (empty).
- **Search discipline:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.
- **ASCII only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~150/MEMBER_OWNERS.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~150/IRPT_BCKEND.TO-IB-yr-612.ycharts-generate-member-owners.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-612.ycharts-generate-member-owners.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R61_Y.md</decomp_doc> round 61, workstream ~Y, cell `IB-yr-612`.
<owned_cells>IB-yr-612</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y61-2-AC1, Y61-2-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~150/IRPT_BCKEND.TO-IB-yr-612.ycharts-generate-member-owners.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y61-2-AC1,Y61-2-AC2` BEFORE the flip to complete. Copy the shape
from `deliverables/0.9.0_WK_IRPT_BCKEND~94/IRPT_BCKEND.TO-IB-yr-291.receipt-carries-vendor-endpoint-ledger.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the table's KEEP and REMOVE counts, each lane named, and the commit
hash.
