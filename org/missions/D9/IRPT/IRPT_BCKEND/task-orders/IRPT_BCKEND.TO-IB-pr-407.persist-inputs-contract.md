# TO IRPT_BCKEND.TO-IB-pr-407 -- publish IB-pr-405's include=persist_inputs: the read route's routes.json entry and its response schema

<to_id>IRPT_BCKEND.TO-IB-pr-407</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~270</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>108</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 17 (msg 3220; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_75_76_P_64_Y_20261008.md`), row D2-W268-S3 | **Decomp cell:** `IB-pr-407` (decomposition section 101) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** IB-pr-405 (drained @6f51e09a79) added an opt-in `include=persist_inputs` to `GET
/api/scoped/investor-reporting/analysis/requests/{requestId}` (operation `analysis-request-read`, irpt-status). The response then gains a
`persist_inputs` object with exactly four members: `artifact_id`, `composition_sha256`, `retention_policy`, and `report_index` (an object
`{report_id, revision, retention_ref}` or `null`). See `infra/aws/lambda/investor-reporting/ops/owned_report.py` `persist_inputs` and
`ops/tests/test_persist_inputs.py`. The contract does not publish this yet (row W268-S3). Root: `C:/dev/wk-irpt-bckend-270/`.

**Build:**
- **`docs/contracts/investor-reporting/v1/routes.json`:** in the `analysis-request-read` row's `query.include` text, add `persist_inputs` to the
  allowed names and say what it adds. Change nothing else in that file.
- **The row's response schema** (`docs/contracts/investor-reporting/v1/responses/analysis-request-read.response.schema.json`, or the schema
  it `$ref`s, e.g. `OwnedAnalysisRequest.schema.json`): declare an optional `persist_inputs` property with exactly those four members
  and `additionalProperties: false`.
  - `artifact_id` matches `^ART-[0-9a-f]{64}$`.
  - `composition_sha256` matches `^[0-9a-f]{64}$`.
  - `retention_policy` is a string.
  - `report_index` is that object or `null`.
- **Fixtures and tests** in `infra/aws/lambda/investor-reporting/_contracts/` (names contain `persist_inputs`, at least 2):
  - a response carrying a valid `persist_inputs` conforms;
  - one with an extra or a missing member does not.
  If the schema is mirrored under `_contracts/`, keep the two byte-identical.

<criterion id="IB108-1-AC1" cell_refs="IB-pr-407"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r108/p108_cells.py" . IB108-1-AC1</invocation><expect>IB108-1-AC1 PASS</expect></criterion>
<criterion id="IB108-1-AC2" cell_refs="IB-pr-407"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r108/p108_cells.py" . IB108-1-AC2</invocation><expect>IB108-1-AC2 PASS</expect></criterion>
<criterion id="IB108-1-AC3" cell_refs="IB-pr-407"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r108/p108_cells.py" . IB108-1-AC3</invocation><expect>IB108-1-AC3 PASS</expect></criterion>

<expected_criteria>IB108-1-AC1, IB108-1-AC2, IB108-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Contract files and tests only; no code, no deploy.
- **Pre-existing failures:** 9 `_contracts` tests already fail at HEAD and are not this cell's (row D2-S46). Do not fix or weaken
  them, and report them unchanged.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W270-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~270" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~270@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~270 <0.9.0_WK_IRPT_BCKEND~270@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
docs/contracts/investor-reporting/v1/routes.json
docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json
docs/contracts/investor-reporting/v1/responses/analysis-request-read.response.schema.json
infra/aws/lambda/investor-reporting/_contracts/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~270/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-407.persist-inputs-contract.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 101 (round 108, workstream ~P), cell `IB-pr-407`.
<owned_cells>IB-pr-407</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB108-1-AC1, IB108-1-AC2, IB108-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~270/IRPT_BCKEND.TO-IB-pr-407.persist-inputs-contract.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the files changed, the test names, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- contract documents and contract tests for one existing route's opt-in member; no code, no function, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route added or removed; one route's declared query and response gain an optional member.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p108_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~11:5xZ: AC1 FAIL (0 selected), AC2 PASS (control, 20 passed), AC3 FAIL (query names no persist_inputs); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO ADDENDUM 17).
</preflight>
