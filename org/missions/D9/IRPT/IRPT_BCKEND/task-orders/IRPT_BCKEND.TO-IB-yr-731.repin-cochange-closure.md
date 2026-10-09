# TO-IB-yr-731 -- irpt-ycharts-generate's staged rows ship no commit split (release 5 repair 2, row D2-S18)

<to_id>IRPT_BCKEND.TO-IB-yr-731</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~222</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `IB-yr-731` (`decompositions/IRPT_BCKEND_DECOMP_R73_Y.md`)

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/ci/lambda-source-map.json` describes how each Lambda is packaged. In the row `"irpt-ycharts-generate"`,
`staged_from` lists files copied in at a fixed git `pin` with their `sha256`. Release 5 rolled back because one commit shipped
SPLIT. Rider `f60e6f1d2a` changed `reports/retention.py` and its callers `composition.py` / `repository.py`. The callers are pinned at
`2f3ee8c15b`, but `retention.py` is still at `3f29017cfc`, so `RetentionPolicy.reference()` got 4 arguments against 3.

**Your cell: move exactly these three rows to pin `2f3ee8c15ba67a88041d179290539778a04d29cb`.**

| packaged_as | repo_path |
|---|---|
| `retention.py` | `infra/aws/lambda/investor-reporting/reports/retention.py` |
| `infra/logic/registry/reporting_policies.json` | `infra/logic/registry/reporting_policies.json` |
| `contracts/ExportBundle.schema.json` | `docs/contracts/investor-reporting/v1/ExportBundle.schema.json` |

- Set each row's `pin` to that full sha and its `sha256` to the hex sha256 of the blob at the pin
  (`git show 2f3ee8c15b:<repo_path>`, as bytes), in the same formats the other rows use.
- Change nothing else. Edit in place, byte-preserving, so the JSON still parses.

### ACCEPTANCE (run from your worktree root, after your commit)

<criterion id="Y73-1-AC1" cell_refs="IB-yr-731"><invocation>python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD</invocation><expect>changed_members=6</expect></criterion>

<criterion id="Y73-1-AC2" cell_refs="IB-yr-731"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r73/cochange_closure.py irpt-ycharts-generate</invocation><expect>cochange_closure PASS</expect></criterion>

<criterion id="Y73-1-AC3" cell_refs="IB-yr-731"><invocation>bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh</invocation><expect>symbol_closure PASS</expect></criterion>

<expected_criteria>Y73-1-AC1,Y73-1-AC2,Y73-1-AC3</expected_criteria>

- AC1 must name exactly `composition.py`, `custody_submission.py`, `repository.py`, `retention.py`,
  `infra/logic/registry/reporting_policies.json` and `contracts/ExportBundle.schema.json`. Any other member is a ROW, not a pass.
- AC2 must print `split=0`.
- AC3 runs BUILD_ONLY and must stay `missing=0`.

**Issuer's base run at box/dell2 HEAD 93e31749b4:**
- AC1: `changed_members=3`.
- AC2: `split=3` (retention.py, reporting_policies.json, ExportBundle.schema.json), FAIL.
- AC3: PASS.

## BOUNDS

- **Grant.** The `<paths>` block and this order's file. BUILD_ONLY only; no deploy, no upload, no AWS writes, no downloads or
  installs.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken the check.
- **Rows** are `IRPT_BCKEND-D2-W222-S<k>`. Re-read the channel, then append only your own block. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~222" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~222@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~222 <0.9.0_WK_IRPT_BCKEND~222@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool. Do not pre-`git add`. Use ASCII only and native Grep/Glob/Read.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~222/IRPT_BCKEND.TO-IB-yr-731.repin-cochange-closure.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-yr-731.repin-cochange-closure.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R73_Y.md</decomp_doc> round 73, workstream ~Y, cell `IB-yr-731`.
<owned_cells>IB-yr-731</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y73-1-AC1, Y73-1-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~222/IRPT_BCKEND.TO-IB-yr-731.repin-cochange-closure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y73-1-AC1,Y73-1-AC2` BEFORE the flip to complete. Shape:
`deliverables/0.9.0_WK_IRPT_BCKEND~155/IRPT_BCKEND.TO-IB-yr-641.repin-x1-staged-rows.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):**
- each criterion's output lines, including the six `changed` lines, the split count and the symbol-closure counts;
- the three rows' pins and sha256 values;
- the diff summary;
- the commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, role or grant changes; the census and BUILD_ONLY only read AWS and build locally.
comp-adversary: RUN -- AC2 at base FAILs on the exact S18 defect plus 2 more splits (split=3); AC3 is the symbol-closure control.
comp-blast: RUN (by reading) -- three staged rows of one function; riders named in the decomposition (~G2 x3, ~Y x1, ~M2 x2, ~P x2) for the release-5b pair; no deployed byte moves.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
