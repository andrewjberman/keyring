# NFRA_IAMROLES202609.TO-IAM-x-6 -- DEPLOY smartx-pipeline's three drifted Lambda versions and the ratified output nulls (row Z-S21, E4 act)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R7.md</decomp_doc>
<owned_cells>IAM-x-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (E4's act, ruled by 1.0.0_SA_CTO~Z)

```
IAM-x-6. ACT: ONE apply of infra/aws/terraform/smartx-pipeline under
org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IAMROLES_E4_SMARTX_DRIFT_DEPLOY_ALL_20261011_Z.md @20c0a85d55 (on your
table SMARTX_DRIFT_TABLE.md @c951e42cae). DEPLOY all three: assets_daily_pull and jwt_refresher are byte-identical
re-uploads; rest_pull's only change is docstring line 3 of smartx_jwt_reader.py (data/orion -> data/inf), committed source
46d0b98aef. The three null outputs (autostart_lambda_arn, autostart_role_arn, eventbridge_rule_arn) ride the apply: their
removal was Andrew-ratified (a3b36fd877 / @874b52729c).

PHASE A -- read-only:
  1. Plan the module UNTARGETED at HEAD (PLAN only, -lock=false), save it with -out, and grade it from show -json. Write
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_deploy/SMARTX_DEPLOY_SURVEY.md
     with, exactly:
       PLAN: smartx-pipeline: <the plan summary line, verbatim>
     plus, per function, the before and after s3_object_version (and rest_pull's source_code_hash), each function's live
     CodeSha256 now, and every other address in the plan (expected: none besides the three outputs).
  2. STOP and report. The pair ledger/NEVER_WIDEN_ROUND7_X-6_{COO,CTO}_HALF.md is written against your survey.

PHASE B -- only on the issuer's GO, after both halves are SIGNED:
  3. Read .open_deploys/ for smartx-pipeline; open a NEVER-2 entry `iamroles-r7-smartx-deploy` naming the three functions.
     Its rollback leg per function is a Terraform update back to the prior object version (pin the data source's
     version_id to the old version, then apply). NEVER aws lambda update-function-code.
  4. safe-apply the SAVED plan only if it still equals the survey's (0 to add, 3 to change, 0 to destroy, plus the three
     output nulls); anything else stops the act.
  5. After the apply: live CodeSha256 for all three equals the plan's after-value; read ONE scheduled invocation of
     smartx-rest-pull on the log plane and record its RequestId and outcome; re-plan the module. Record in
     .../smartx_deploy/POST_APPLY_smartx.md, exactly:
       POST-APPLY-PLAN: smartx-pipeline: 0 to add, 0 to change, 0 to destroy
       INVOKE: smartx-rest-pull: <RequestId> <SUCCEEDED|FAILED>
     Then close the entry, with the close COMMITTED.
```

## DEPENDENCIES

None. A separate workstream of round 7, `SMARTX_DEPLOY` (DECOMP_R7 section 10). No other round-7 order touches
smartx-pipeline (x-2's smartx deletes went through the IAM API).

## BOUNDS

```
The plan is exactly the survey's: three aws_lambda_function updates and the three ratified output nulls. NOTHING else:
no add, no destroy, no IAM, no other address. safe-apply only (NEVER-9); the NEVER-2 entry opens first and closes last;
a Lambda code change goes through Terraform only. G-21: no alert, monitor or schedule.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_deploy/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-x-6.smartx-drift-deploy.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-x-6).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-x-6"><invocation>grep -c -E '^POST-APPLY-PLAN: smartx-pipeline: 0 to add, 0 to change, 0 to destroy$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_deploy/POST_APPLY_smartx.md</invocation><expect>exactly 1 -- the module plans clean after the apply, so the drift is gone</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-x-6"><invocation>grep -c -E '^INVOKE: smartx-rest-pull: [0-9a-f-]{36} SUCCEEDED$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_deploy/POST_APPLY_smartx.md</invocation><expect>exactly 1 -- a real scheduled invocation of the redeployed rest_pull succeeded, read on the log plane</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-x-6"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r7-smartx-deploy') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r7-smartx-deploy* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=1` -- the NEVER-2 entry's own Status line reads CLOSED</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-x-6" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did live
  CodeSha256 match the plan for all three, and did the apply move nothing but the ruled drift?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>complete</status>
<round>7</round>
<workstream>SMARTX_DEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-x-6</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 7) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** IAM-x-3 table @c951e42cae -> CTO ruling @20c0a85d55 (msg 33261) -> DECOMP_R7 section 10 -> this issuance.
**Risk WORLD:** three Lambda code-version moves on a pipeline no project owns, under a NEVER-2 entry and a never-widen pair.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 120` at the round-7 cut: BUDGET REACHED, 1 of 6 carriers, C2 PARTIAL, rc=3; PARTIAL_OR_BLIND; the assignee reads .open_deploys/ for smartx-pipeline before its entry opens (none open at 11:3xZ).
comp-iam: DECLARED-NOT-APPLICABLE -- the act moves Lambda code versions; no IAM resource is in the plan (the survey proves it).
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (the three moves as the CTO's artifact diff read them; the outputs' ratified removal).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (file absent); AC2 base FAIL as expected (file absent); AC3 base FAIL as expected (`open=0 closed=0`).
