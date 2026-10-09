# TO IRPT_BCKEND.TO-IB-pr-411 -- persist_inputs.report_index carries the stored custody report's sha256 (W64-S1); contract updated

<to_id>IRPT_BCKEND.TO-IB-pr-411</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~274</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>112</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** IRPT_DASHBD ADDENDUM 12 item 3 (@77e60c3d2b; CTO msg 3370), row IRPT_DASHBD W64-S1 | **Decomp cell:** `IB-pr-411` (decomposition section 105) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** IRPT_DASHBD's custody-statement runner keeps a dormant "verify persisted sha256" limb until IRPT serves the stored report's
sha256 (W64-S1). The persist response already returns it (`export/custody_persist.py`, the final `return {..., "sha256": ref["sha256"]}`).
The read does not. `OwnedAnalysisReader._custody_report_index` in `infra/aws/lambda/investor-reporting/ops/owned_report.py` returns
`{report_id, revision, retention_ref}`, and the stored index row's `ref` holds the object's `sha256`. Root:
`C:/dev/wk-irpt-bckend-274/infra/aws/lambda/investor-reporting/`.

**Build:**
- `_custody_report_index` returns `{report_id, revision, retention_ref, sha256}`, where `sha256` is the index row's `ref["sha256"]`.
- A row whose `ref.sha256` is not 64 lowercase hex is refused, never served blank (e.g. `RequestReadRefused("PERSIST_REPORT_SHA256")`).
- Nothing else in the read changes.

**Tests** in `ops/tests/` (names contain `report_index_sha256`, at least 2):
- a persisted report's `report_index.sha256` equals the stored ref's sha256;
- a row with a missing or malformed sha256 is refused.
The existing `persist_inputs` tests still pass.

**Contract:** in `docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json`, the `persist_inputs.report_index` object (non-null
branch) adds a required `sha256` with pattern `^[0-9a-f]{64}$`, and `additionalProperties` stays false. Update the `persist_inputs` fixtures
and tests in `infra/aws/lambda/investor-reporting/_contracts/` to match, so they still pass. A fixture with no sha256 is now refused.

**Release:** none in this cell. This rides IB-pr-405's narrow irpt-status release, which comes after IRPT_ANLREQ release 1 (CTO
ADDENDUM 17).

<criterion id="IB112-1-AC1" cell_refs="IB-pr-411"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r112/p112_cells.py" . IB112-1-AC1</invocation><expect>IB112-1-AC1 PASS</expect></criterion>
<criterion id="IB112-1-AC2" cell_refs="IB-pr-411"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r112/p112_cells.py" . IB112-1-AC2</invocation><expect>IB112-1-AC2 PASS</expect></criterion>
<criterion id="IB112-1-AC3" cell_refs="IB-pr-411"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r112/p112_cells.py" . IB112-1-AC3</invocation><expect>IB112-1-AC3 PASS</expect></criterion>

<expected_criteria>IB112-1-AC1, IB112-1-AC2, IB112-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests and contract; no upload, apply or deploy.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W274-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~274" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~274@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~274 <0.9.0_WK_IRPT_BCKEND~274@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/tests/
infra/aws/lambda/investor-reporting/_contracts/
docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~274/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-411.report-index-sha256.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 105 (round 112, workstream ~P), cell `IB-pr-411`.
<owned_cells>IB-pr-411</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB112-1-AC1, IB112-1-AC2, IB112-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~274/IRPT_BCKEND.TO-IB-pr-411.report-index-sha256.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the change, the test names, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one owned read's report_index gains sha256 (opt-in persist_inputs member); contract updated; no release in this cell (rides IB-pr-405's narrow irpt-status release).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p112_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~13:5xZ: AC1 FAIL (0 selected), AC2 PASS (control), AC3 FAIL (no sha256 in report_index); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (IRPT_DASHBD ADDENDUM 12 item 3 places it with ~P2).
</preflight>
