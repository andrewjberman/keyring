# TO IRPT_BCKEND.TO-IB-pr-412 -- publish the custody-report-read and custody-report-persist response contracts (red-list entries owned by ~P2); routes.json keeps response_schema null

<to_id>IRPT_BCKEND.TO-IB-pr-412</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~275</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>113</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ADDENDUM 18/19 (the red `_contracts` list is ~P2's); red list `0.9.0_WK_IRPT_BCKEND~271/IB109-1_contracts_red_list.json`, the NAMED entries for IB-pr-355 and IB-pr-373 | **Decomp cell:** `IB-pr-412` (decomposition section 106) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** Two of the red `_contracts` tests are ~P2's:
- `test_seam_paired.py::test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[custody-report-read]` (IB-pr-355);
- the same test with `[custody-report-persist]` (IB-pr-373).

Both are red because `docs/contracts/investor-reporting/v1/responses/<operation>.response.schema.json` does not exist. The test reads that
file BY OPERATION NAME (`response_contract()` in `_contracts/tests/test_seam_paired.py`). The routes.json rows declare `response_schema: null`
on purpose (row W167-S1, `60f7d8f4c8`: the portal wire generator skips only an explicit null), and that stays. Root: `C:/dev/wk-irpt-bckend-275/`.

**Build:**
- **Author** `docs/contracts/investor-reporting/v1/responses/custody-report-read.response.schema.json` and
  `.../custody-report-persist.response.schema.json`, modelled on the existing `responses/*.response.schema.json` files. Each must pass every
  assertion in `test_seam_paired.py`:
  - a valid Draft 2020-12 schema;
  - `operation` const = the operation;
  - `contract_version` const = the module's `CONTRACT_VERSION`;
  - `additionalProperties: false`;
  - `contract_version`, `operation` and `firm_id` required;
  - `data` required;
  - every `data` `$ref` resolving to a published document schema.
- **Describe what the SHIPPED handlers return.** Persist: `export/custody_persist.py` returns `{report_kind, report_id, revision, sha256}`.
  Read: the custody-report read's response, from its handler. Never invent a member.
- **Add the good and bad fixtures** the control test needs for each operation, in the form the test reads.
- **Do NOT change routes.json.** Both rows keep `response_schema: null`.
- **Do NOT touch** `analysis-request-original` (IRPT_ANLREQ's) or the route-census test. They stay red until their owner acts, and your
  check excuses exactly those two.

<criterion id="IB113-1-AC1" cell_refs="IB-pr-412"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r113/p113_cells.py" . IB113-1-AC1</invocation><expect>IB113-1-AC1 PASS</expect></criterion>
<criterion id="IB113-1-AC2" cell_refs="IB-pr-412"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r113/p113_cells.py" . IB113-1-AC2</invocation><expect>IB113-1-AC2 PASS</expect></criterion>
<criterion id="IB113-1-AC3" cell_refs="IB-pr-412"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r113/p113_cells.py" . IB113-1-AC3</invocation><expect>IB113-1-AC3 PASS</expect></criterion>

<expected_criteria>IB113-1-AC1, IB113-1-AC2, IB113-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Contract documents, fixtures and tests only; no code, no deploy.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W275-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~275" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~275@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~275 <0.9.0_WK_IRPT_BCKEND~275@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
docs/contracts/investor-reporting/v1/responses/custody-report-read.response.schema.json
docs/contracts/investor-reporting/v1/responses/custody-report-persist.response.schema.json
infra/aws/lambda/investor-reporting/_contracts/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~275/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-412.custody-response-contracts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 106 (round 113, workstream ~P), cell `IB-pr-412`.
<owned_cells>IB-pr-412</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB113-1-AC1, IB113-1-AC2, IB113-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~275/IRPT_BCKEND.TO-IB-pr-412.custody-response-contracts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the two schemas' members, the fixtures added, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- two new response-contract documents and their fixtures; routes.json untouched (response_schema stays null, so the portal wire generator is unchanged); no code, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p113_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~14:1xZ: AC1 FAIL (2 custody controls red), AC2 FAIL (red beyond the two not owned), AC3 PASS (control); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO ADDENDUM 18: one owner).
</preflight>
