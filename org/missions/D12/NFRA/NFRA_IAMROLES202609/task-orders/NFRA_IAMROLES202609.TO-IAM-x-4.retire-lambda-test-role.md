# NFRA_IAMROLES202609.TO-IAM-x-4 -- RETIRE row 7 `lambda-test-role`: own recreation record, detach, delete, NoSuchEntity read back

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R7.md</decomp_doc>
<owned_cells>IAM-x-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (round-6 analysis E3, unconditional by Addendum 2)

```
IAM-x-4. ACT: delete IAM role `lambda-test-role` (row 7, RETIRE) under 1.0.0_SA_CTO~Z's ruling
org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IAMROLES_ROW7_LAMBDA_TEST_ROLE_DELETE_20261011_Z.md @5af6d5e23e,
which adopts laptop 1.0.0_SA_CTO's YES (@106f60a7c8) and its terms. Why it is recoverable: never assumed (RoleLastUsed
null), trust lambda.amazonaws.com only, 1 AWS-managed attachment (AWSLambdaBasicExecutionRole), 0 inline, 0 functions on
it, 0 documents account-wide naming role/lambda-test-role.

STEPS, IN THIS ORDER (the ruling's terms, plus step 0):
  0. RE-READ AND RECORD, before touching anything. Re-read the five facts above live; if ANY differs (a use, a function,
     an inline policy, a reference), STOP and file a row -- nothing is deleted. Then write the site-Z recreation record
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/retire_row7/RECREATE_lambda-test-role.md
     from the live reads: the exact `get-role` JSON (path, description, max session, the assume-role policy document
     verbatim) and every attached policy ARN, beside the exact `aws iam create-role` + `attach-role-policy` commands that
     rebuild it. (The laptop's record is not in this clone; the rollback must not depend on it.) Commit it.
  1. Open a NEVER-2 deploy-ledger entry `iamroles-r7-retire-row7` whose rollback leg is the create-role + attach commands
     in that record.
  2. Detach the managed policy (aws iam detach-role-policy).
  3. Delete the role (aws iam delete-role).
  4. Read back: `aws iam get-role --role-name lambda-test-role` returns NoSuchEntity, beside a positive control: the
     same call on an existing role (e.g. opal-smartx-lambda-role) returns the role. Record both outputs verbatim in
     .../round7/retire_row7/RETIRE_READBACK.md, then close the ledger entry.
  5. Leave the GOVERNANCE_DISPOSITION row to the issuer; report the read-back to 2.0.0_SA_COO~ZI.
```

## DEPENDENCIES

None. A separate workstream of round 7 (DECOMP_R7 section 8); it shares no module or file with x-1, x-2 or x-3.

## BOUNDS

```
ONE ROLE: lambda-test-role only. Step 0's STOP is binding: any changed fact means nothing is deleted.
The NEVER-2 entry opens before step 2 and closes after step 4; the rollback is create-role from the site-Z record.
No other role, policy or tag is touched. G-21: no alert, monitor or schedule.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/retire_row7/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-x-4.retire-lambda-test-role.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-x-4).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-x-4"><invocation>grep -c -E 'aws iam (create-role|attach-role-policy) ' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/retire_row7/RECREATE_lambda-test-role.md</invocation><expect>2 or more -- the site-Z recreation record carries the rebuild commands (create-role and each attach)</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-x-4"><invocation>bash -c ".tools/aws iam get-role --role-name lambda-test-role 2>&1 | grep -c NoSuchEntity"</invocation><expect>exactly `1` -- the role is gone, read live (a positive control on an existing role is in RETIRE_READBACK.md)</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-x-4"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r7-retire-row7') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r7-retire-row7* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=1` -- the NEVER-2 entry's own Status line reads CLOSED</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-x-4" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): were the five
  facts re-read live before the delete, and does the site-Z record rebuild the role exactly as it was?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>7</round>
<workstream>RETIRE_ROW7</workstream>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-x-4</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 7, Addendum 2) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** `ROUND_ANALYSIS.round6.md` E3 + Addendum 2 -> CTO ruling @5af6d5e23e (adopting laptop @106f60a7c8; msgs 33193 / 33195, exit (b)) -> DECOMP_R7 section 8 -> this issuance.
**Risk WORLD:** a delete of one IAM role, recoverable from the site-Z record; the CTO ruling is the sign-off on its blast radius.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 120` at the round-7 cut: BUDGET REACHED, 1 of 6 carriers, C2 PARTIAL, rc=3; PARTIAL_OR_BLIND; the assignee reads .open_deploys/ before its entry opens.
comp-iam: RUN -- `bash .tools/comp-iam stats`: 219 IAM roles parsed; live get-role lambda-test-role at 04:5xZ: created 2026-02-19, RoleLastUsed None, RoleId AROAUR7FNW6PKHOVBXCS4.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (nothing pins the role, per the CTO's five reads; the laptop recreation record is NOT in this clone, so step 0 writes a site-Z record).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (record absent); AC2 base FAIL as expected (`0`: the role exists); AC3 base FAIL as expected (`open=0 closed=0`).
