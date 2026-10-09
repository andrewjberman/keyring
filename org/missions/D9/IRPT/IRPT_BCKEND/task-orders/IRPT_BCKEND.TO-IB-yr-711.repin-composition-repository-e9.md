# TO-IB-yr-711 -- irpt-ycharts-generate's staged composition.py and repository.py carry E9 (E11 repair)

<to_id>IRPT_BCKEND.TO-IB-yr-711</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~221</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-711` (`decompositions/IRPT_BCKEND_DECOMP_R71_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` describes how each Lambda is packaged. In the row `"irpt-ycharts-generate"`, the
`staged_from` list names files copied in from other repo paths, each at a fixed git `pin` with its `sha256`.

Two of those rows are pinned at `3f29017cfc`, which is older than E9, the change that added `CUSTODY_POLICY_REVISION` and per-family
policy revisions:

| packaged_as | repo_path |
|---|---|
| `composition.py` | `infra/aws/lambda/investor-reporting/reports/composition.py` |
| `repository.py` | `infra/aws/lambda/investor-reporting/reports/repository.py` |

Because of that, the packaged `custody_submission.py` cannot import `CUSTODY_POLICY_REVISION`, and release 4 rolled back.

**Your cell: move exactly those two rows to pin `605c4cd4aceded875fe4c7164fa1494385b08a96`.**
- Set each row's `pin` to that full 40-character sha, in the same form the other rows use.
- Set each row's `sha256` to the hex sha256 of the blob at that pin (`git show 605c4cd4ac:<repo_path>`, hashed as bytes), in the same
  format the other rows use.
- Change nothing else: no other row and no other field. Edit the values in place; do not re-serialize the JSON. It must still parse.
  Keep its line endings byte for byte.

### ACCEPTANCE (run from your worktree root, after your commit)

<criterion id="Y71-1-AC1" cell_refs="IB-yr-711"><invocation>python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD</invocation><expect>changed_members=3</expect></criterion>

<criterion id="Y71-1-AC2" cell_refs="IB-yr-711"><invocation>bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh</invocation><expect>symbol_closure PASS</expect></criterion>

<expected_criteria>Y71-1-AC1,Y71-1-AC2</expected_criteria>

- AC1 must name exactly `custody_submission.py`, `composition.py` and `repository.py`. Any other changed member is a ROW, not a pass.
- AC2 runs BUILD_ONLY (it never uploads) and parses the built zip. It must print `missing=0` and `symbol_closure PASS`, and its build
  line must still read `OK: import-closure`.

**Issuer's base run at box/dell2 HEAD 605c4cd4ac:**
- AC1: `changed_members=1` (custody_submission.py).
- AC2: `MISSING custody_submission.py:15 imports CUSTODY_POLICY_REVISION from composition`, `modules=62 pairs=273 missing=1`,
  `symbol_closure FAIL`.

## BOUNDS

- **Grant.** The `<paths>` block and this order's file. BUILD_ONLY only; no deploy, no upload, no AWS writes, no downloads or
  installs.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken the check.
- **Rows** are `IRPT_BCKEND-D2-W221-S<k>`. Re-read the channel, then append only your own block. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~221" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~221@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~221 <0.9.0_WK_IRPT_BCKEND~221@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool. Do not pre-`git add`. Use ASCII only and native Grep/Glob/Read.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~221/IRPT_BCKEND.TO-IB-yr-711.repin-composition-repository-e9.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-711.repin-composition-repository-e9.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R71_Y.md</decomp_doc> round 71, workstream ~Y, cell `IB-yr-711`.
<owned_cells>IB-yr-711</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y71-1-AC1, Y71-1-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~221/IRPT_BCKEND.TO-IB-yr-711.repin-composition-repository-e9.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y71-1-AC1,Y71-1-AC2` BEFORE the flip to complete. Shape:
`deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):**
- each criterion's output lines, including the three `changed` lines and the closure counts;
- the two rows' pins and sha256 values;
- the diff summary;
- the commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, role or grant changes; the census and BUILD_ONLY only read AWS and build locally.
comp-adversary: RUN -- AC2 at base FAILs on the exact defect (1 missing of 273 pairs); it is a real negative control, not a self-report.
comp-blast: RUN (by reading) -- two staged rows of one function; commits to those files since 3f29017cfc are E9 (2aa217ec58) plus riders f60e6f1d2a (~G2) and b13bab7495 (~P), named for the release-5 pair; no deployed byte moves.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
