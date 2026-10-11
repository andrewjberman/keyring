# NFRA_IAMROLES202609.TO-IAM-x-3 -- READ-ONLY: smartx-pipeline's three Lambda drifts and three null outputs, one evidence table (row Z-S21)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R7.md</decomp_doc>
<owned_cells>IAM-x-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (round-6 analysis Addendum 1, item E4)

```
IAM-x-3. READ-ONLY. NOTHING IS APPLIED, DEPLOYED OR REVERTED.
An untargeted plan of infra/aws/terraform/smartx-pipeline moves three aws_lambda_function resources and nulls three
outputs (row Z-S21, measured by you in round 6's PHASE A):
  assets_daily_pull  s3_object_version XmkW9C_XX1J_6sREU2VZ2naPbfmRQa7O -> QNIiMQgfRzxG_KrI_6mVxJDjJbZFOnsd
  jwt_refresher      s3_object_version lRZrP4cIcsSbeYBd8SIB6_W8No75LiDw -> HAmOeAkTP0mT6304E9OvUVTpk_GhC8hh
  rest_pull          s3_object_version Way7ManCnOWA8bAdT8YIAzZ0ncPu4ino -> g_1WqvOSlrPbM1uf8nFcy0uG9SB4xXwb, plus a new source_code_hash
  outputs autostart_lambda_arn, autostart_role_arn, eventbridge_rule_arn -> null
No project owns smartx-pipeline. 1.0.0_SA_CTO~Z rules the deploy-or-revert act on YOUR table.

STEPS:
  1. Re-run the untargeted plan in the shared tree (PLAN only, -lock=false) and confirm the same set, or record what changed.
  2. For each of the three functions, read LIVE (aws lambda get-function-configuration: CodeSha256, LastModified,
     CodeSize; get-function for the code location) and read the repo (git log on the function's source path and on
     the .tf that names its package). Name the commit that moved the planned package / object version.
  3. For each, decide, from that evidence, whether the PLANNED code ever ran live: compare the live CodeSha256 and
     LastModified with the commit date and with the plan's source_code_hash where one exists.
  4. For each output, read the cause of its null (the resource it reads, and whether that resource exists in state).
  5. Write org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_drift/SMARTX_DRIFT_TABLE.md
     with one line per function, exactly:
       DRIFT: <function>: commit=<sha> ran_live=<yes|no> rec=<DEPLOY|REVERT|HOLD>: <one-line reason>
     and one line per output, exactly:
       OUTPUT: <name>: cause=<one line>
     then the evidence beside each, each read verbatim with its command.
  6. STOP and report to 2.0.0_SA_COO~ZI.
```

## DEPENDENCIES

None. It runs in parallel with IAM-x-1 and IAM-x-2 (DECOMP_R7 section 7).

## BOUNDS

```
READ-ONLY: no apply, no deploy, no revert, no tag, no state edit; terraform plan -lock=false only.
Never type a Lambda update by hand (CLAUDE.md: aws lambda update-function-code is Terraform only).
G-21: no alert, monitor or schedule.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_drift/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-x-3.smartx-drift-table.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-x-3).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-x-3"><invocation>grep -c -E '^DRIFT: (assets_daily_pull|jwt_refresher|rest_pull): commit=[0-9a-f]{7,40} ran_live=(yes|no) rec=(DEPLOY|REVERT|HOLD): .+$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_drift/SMARTX_DRIFT_TABLE.md</invocation><expect>exactly 3 -- one complete row per drifted function, each naming a commit, a live-ran verdict and a recommendation</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-x-3"><invocation>grep -c -E '^OUTPUT: (autostart_lambda_arn|autostart_role_arn|eventbridge_rule_arn): cause=.+$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_drift/SMARTX_DRIFT_TABLE.md</invocation><expect>exactly 3 -- each null output has a named cause</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-x-3"><invocation>bash -c "ls -a org/critical_paths/.open_deploys/ | grep -c 'smartx'"</invocation><expect>`0` -- the cell opened no deploy ledger on smartx, because it applied nothing</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-x-3" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): does each
  recommendation follow from evidence read live, and would the CTO rule the act from this table alone?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>7</round>
<workstream>SMARTX_DRIFT</workstream>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-x-3</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 7, Addendum 1) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** `ROUND_ANALYSIS.round6.md` Addendum 1 @48153f21bc (E4; msg 33186) -> DECOMP_R7 section 7 -> this issuance.
**Risk LOCAL:** read-only; nothing in the world moves.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 120` at the round-7 cut: BUDGET REACHED, 1 of 6 carriers, C2 PARTIAL, rc=3; PARTIAL_OR_BLIND; this cell opens no ledger.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell reads Lambda code versions and outputs, not IAM permissions.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (the three drifts and null outputs as measured in Z-S21 at 097d3bcc3e; the read-only bound).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (file absent); AC2 base FAIL as expected (file absent); AC3 base reads `0` (no smartx ledger open; it stays a guard).
