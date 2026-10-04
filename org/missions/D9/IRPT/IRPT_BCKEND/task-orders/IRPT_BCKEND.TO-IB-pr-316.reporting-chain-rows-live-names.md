# TO IRPT_BCKEND.TO-IB-pr-316 -- the source map keys the 49F reporting chain by its live names and records them (S322, S178)

<to_id>IRPT_BCKEND.TO-IB-pr-316</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~119</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND ANALYSIS rounds 42-46 item E2 (msg 104972), on E1's LIVE list
(S178's remainder) and row S322 | **Decomp cell:** `IB-pr-316` (decomposition section 42) | **outcome_ref:** FWD-8 (the served 49F
reporting chain) | **depends_on:** none. WORLD is the source map's gate floor; this is a record only.

---

## WORKER FACE

**What is wrong.** `infra/aws/lambda/ci/lambda-source-map.json` has rows keyed `irpt-reporting-gold-lambda`,
`irpt-reporting-publish-lambda` and `irpt-reporting-read-lambda`, which name no live function. The live 49 Financial reporting
functions are builder-named:

| function | live CodeSha256 | role |
|---|---|---|
| irpt-49f-reporting-gold-lambda | Mex71Y5g.. | irpt-49f-reporting-gold-role |
| irpt-49f-reporting-publish-lambda | AH5r60vp.. | irpt-49f-reporting-publish-role |
| irpt-49f-reporting-read-lambda | Wzf2qS5P.. | irpt-49f-reporting-read-role |

The naming limb admits builder-minted names in the source map (CVO ruling @7b38f056ca, gate @1c3fc41a4d and @7de9db9085).

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-119`. Run everything from its root.

**What you do:**
1. **Re-key each stale row** to its live name, with a small Python script that preserves the file's JSON formatting and line endings:
   - `irpt-reporting-gold-lambda` becomes `irpt-49f-reporting-gold-lambda`; same for publish and read.
   - Set each row's `iam_role` to the live role.
   - If a row's `tf_resource` / `tf_file` do not resolve to the module that declares the live function (find it under
     `infra/aws/terraform/investor-reporting/`), correct them to the declaring module.
   Commit with safe-commit. The naming limb must read PASS; if it refuses, stop and file a row.
2. **Record each function**, one recorder run each, with a timeout of at least 900 s. Read the live hash, then run:
   `bash infra/aws/lambda/ci/record-terraform-deploy.sh investor-reporting --function <fn> --code-sha256 <hash> --author "0.9.0_WK_IRPT_BCKEND~119 <0.9.0_WK_IRPT_BCKEND~119@opal.agent>"`
   Its "Resolved deployment set" names exactly that function, with no `HALF-LANDED`. Nothing is left staged afterwards.
   - **If the recorder refuses** because the row's pipeline or tf address does not resolve: stop, file a row, and do not hand-edit
     `deployed_code_sha256`.

<criterion id="IB48-2-AC1" cell_refs="IB-pr-316"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r48/p48_e2_cells.py" . IB48-2-AC1</invocation><expect>IB48-2-AC1 PASS</expect></criterion>
`IB48-2-AC1` -- the three live-named rows equal live code and role; the three stale keys are gone. Base: FAIL.

<criterion id="IB48-2-AC2" cell_refs="IB-pr-316"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r48/p48_e2_cells.py" . IB48-2-AC2</invocation><expect>IB48-2-AC2 PASS</expect></criterion>
`IB48-2-AC2` -- a GUARD: no other row changes against base 123258bd51 (irpt-ycharts-generate excepted), and comp-lambdamap adds no
finding. Base: PASS.

<expected_criteria>IB48-2-AC1,IB48-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only.
- **Refusal clause.** A `--all` run, a run without `--function`, or a hand edit of a deploy-record field is a defect: stop and
  file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/CHANGELOG.json
infra/aws/lambda/ci/source-map-reconcile-audit.jsonl
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~119/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-316.reporting-chain-rows-live-names.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 42 (round 48, workstream ~P), cell `IB-pr-316`.
<owned_cells>IB-pr-316</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB48-2-AC1, IB48-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~119/IRPT_BCKEND.TO-IB-pr-316.reporting-chain-rows-live-names.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB48-2-AC1,IB48-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the naming limb's line, each recorder run's resolved-set and reconcile
lines, each criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- lambda-source-map.json: three stale rows re-keyed to the live 49F reporting functions and recorded; a record only, 0 served bytes move.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB48-2-AC1 base FAIL, IB48-2-AC2 base PASS (14 of 14), dry-run at base 123258bd51 2026-10-04 ~23:5xZ.
lane: the <paths> block IS the grant.
</preflight>
