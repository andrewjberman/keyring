# TO IRPT_BCKEND.TO-IB-pr-493 -- each 49 Financial ACCOUNT node carries an additive `account_id` member, the directory's id (rows DSGN_IRPTV1-D2-W69-S1, D2-W72-S2)

<to_id>IRPT_BCKEND.TO-IB-pr-493</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~344</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>170</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's rulings in the DSGN_IRPTV1 ROUND-32 ANALYSIS section 2a and ROUND-33 ANALYSIS section 1, and the CTO ROUND-170 ANALYSIS section 4 (msg 6739) | **Decomp cell:** `IB-pr-493` (decomposition section 162) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-493` (inlined):** the live 49 Financial holdings builder mints each ACCOUNT node's id from the Schwab custody key (`holdings_49f.py:339`, `hs.opaque_id("account", firm_id, raw_account)` over `dim_balance.account_id`), while the directory's account ids come from `dim_account` (`directory_runner.py`, `acct_row`: the raw key is the zero-padded 10-digit account id). The page therefore has no account id on a node and must guess. Add an ADDITIVE `account_id` member on each 49F ACCOUNT node: the DIRECTORY's opaque id of that account. **BUILD ONLY: no deploy, no AWS call, no run of the live builder.**

**Edit ONLY these files (paths in your worktree):**
1. `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: `_node` (:560) gains an OPTIONAL keyword `account_id=None`; the member `account_id` is written only when it is not None (every existing caller unchanged).
2. `data/assets/scripts/gold/investor_reporting/holdings_49f.py`: in `build_49f_actual` (:286), where the ACCOUNT node is made (:347), pass `account_id=` the directory's id when it can be established, else omit it. Establish it from what the builder already holds: `dir_ids` (:320, the landed directory's set of opaque account ids, or None when no directory has landed). Candidates for the account's directory id are `hs.opaque_id("account", firm_id, raw_account)` and `hs.opaque_id("account", firm_id, hs._pad10(raw_account))` (read `directory_runner.py:592` and `holdings_snapshot._pad10` to confirm how the two key spaces relate); the member is the candidate that IS in `dir_ids`. If `dir_ids` is None, or no candidate is in it, the member is OMITTED for that node and the census (the builder's returned census dict) counts it under a new key `account_id_member_omitted`; a candidate that differs from the node id is counted under `account_id_differs_from_node_id`. Never invent an id; never read `dim_account` here (the builder does not today; stay with `dir_ids`).
3. THE CONTRACT: `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` and its two byte-identical copies `infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json` and `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`: the node `properties` gain `account_id` (type string, description: the directory's opaque account id for an ACCOUNT node, additive, optional) and the three files stay BYTE-IDENTICAL; `additionalProperties:false` stays.
4. `infra/aws/lambda/investor-reporting/_contracts/fixtures/HoldingsSnapshot.valid.json`: its ACCOUNT node (`N-1`) carries `account_id` (a synthetic opaque string); it still validates; `HoldingsSnapshot.invalid.json` is NOT edited and must still fail.
5. `infra/aws/lambda/investor-reporting/_ids/raw_keys.json`: the 49F account entry names that the live builder's node id is built from the Schwab `dim_balance.account_id` and that the node's `account_id` member is the directory's id (state the rule in one sentence; keep the file valid JSON).
6. ONE new test file `data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f_account_id.py` with at least THREE arms on the existing synthetic fixtures of `tests/test_holdings_49f.py` (read how it stubs `_directory_account_ids`): the member equals the directory's id when a candidate is in `dir_ids`; it is omitted and counted when `dir_ids` is None; it is omitted and counted when no candidate is in `dir_ids`; and every other member of the node is unchanged.

**Hazard to file as a row, not to fix:** the two Lambdas `irpt-holdings` and `irpt-ycharts-generate` STAGE `docs/contracts/.../HoldingsSnapshot.schema.json` and pin its sha256 in `infra/aws/lambda/ci/lambda-source-map.json`; editing the docs copy leaves those pins stale. Do NOT edit `lambda-source-map.json`; file ONE row stating which functions and pins (their names and the line numbers), class BLOCKING, hazard standing INERT (nothing is deployed from this order).

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB170-2-AC1" cell_refs="IB-pr-493"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-2-AC1</invocation><expect>IB170-2-AC1 PASS</expect></criterion>
<criterion id="IB170-2-AC2" cell_refs="IB-pr-493"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-2-AC2</invocation><expect>IB170-2-AC2 PASS</expect></criterion>
<criterion id="IB170-2-AC3" cell_refs="IB-pr-493"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-2-AC3</invocation><expect>IB170-2-AC3 PASS</expect></criterion>

<expected_criteria>IB170-2-AC1, IB170-2-AC2, IB170-2-AC3</expected_criteria>

What the checks grade: AC1 `hs._node(..., account_id="x")` carries the member and `hs._node(...)` without it does not, and your new test file passes (3 or more); AC2 the three schema copies are byte-identical, name `account_id` as a string on a node, the valid fixture's ACCOUNT node carries it and validates, the invalid fixture still fails, and `raw_keys.json` names it; AC3 the 22 existing builder tests and the existing contract tests still pass. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and nothing else. No deploy, no AWS call, no run of the live builder, no `lambda-source-map.json` edit, no edit of `HoldingsSnapshot.invalid.json` or of an existing test.
- **Refusal clause:** STOP, file a row, change nothing more, if the directory's id cannot be established from `dir_ids` and the two candidates without reading `dim_account` or another source, or if making the member additive would require a change to the schema beyond adding the property (say what).
- **Row ids** are `IRPT_BCKEND-D2-W344-S<k>` (the next free `k`).
- **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/holdings_49f.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f_account_id.py
infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/HoldingsSnapshot.valid.json
infra/aws/lambda/investor-reporting/_ids/raw_keys.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~344/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-493.account-node-carries-the-directory-account-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 162 (round 170, workstream ~P), cell `IB-pr-493`.
<owned_cells>IB-pr-493</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB170-2-AC1, IB170-2-AC2, IB170-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~344/IRPT_BCKEND.TO-IB-pr-493.account-node-carries-the-directory-account-id.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- BUILD ONLY. The files are gold-runner code (an SSM host bundle, in no Lambda's members), a contract in three byte-identical copies (staged by `irpt-holdings` and `irpt-ycharts-generate`, which pin the docs copy's sha256: a stale-pin hazard the worker files as a row), a fixture and `raw_keys.json`; nothing is deployed from this order. The APPLY of the member (a served contract change) is a later order under a never-widen pair, which re-pins those functions first.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p170_cells.py dry-run at base on dell2 2026-10-13 ~02:2xZ: IB170-2 AC1 FAIL (`_node` has no `account_id` keyword), AC2 FAIL (the schema names no `account_id`), AC3 PASS (a bound: 22 builder tests and 24 contract tests pass). The cut ran no builder and no positive control for AC2.
lane: the paths block IS the grant; worker slot ~344 of IRPT_BCKEND. Class WORLD (the `infra/` floor).
</preflight>
