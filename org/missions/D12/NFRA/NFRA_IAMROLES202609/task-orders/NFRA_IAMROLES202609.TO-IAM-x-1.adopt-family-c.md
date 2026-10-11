# NFRA_IAMROLES202609.TO-IAM-x-1 -- ADOPT Family C (rows 6 and 14) into Terraform: survey with a gate dry-grade, pairs, one apply per module

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R7.md</decomp_doc>
<owned_cells>IAM-x-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-4 enrichment; the round-6 analysis calls this E1)

```
IAM-x-1. ACT: adopt row 6 `lambda-ec2-runtime-monitor-role` and row 14 `sentiment_query_api-role` (Family C, the last two
ADOPT rows) into Terraform under ROUND_ANALYSIS.round6.md @2f49aa235b E1 and ADOPTION_PLAN_TEN.md @59112aafed Family C.
The owner of record is 0.7.0_AE_CloudOps~Z; you, 0.7.0_AE_CloudOps~IR, execute. Same shape as round 6's w-orders.

ROLES: row 6 `lambda-ec2-runtime-monitor-role` (IN USE: last used 2026-10-11T04:21Z) -> a NEW file in
       infra/aws/terraform/shared-infra/ (round-5 home ruling); row 14 `sentiment_query_api-role` (an UNDERSCORE in the
       name; last used 2026-01-02) -> the module YOU name in the survey, from where its consumers are declared.

THE OMISSION RULE, binding: each `aws_iam_role` block carries name, path, description (omit if the live role has none),
assume_role_policy, max_session_duration (as live) and NOTHING about policies. `inline_policy` and `managed_policy_arns`
are ABSENT. Read each role's trust LIVE; never copy a sibling's.

PHASE A -- no apply, no AWS write:
  1. Read each role live (get-role, list-role-policies, list-attached-role-policies, list-role-tags). Write row 6's
     declaration as `infra/aws/terraform/shared-infra/zz_adopt_family_c_row6.tf.proposed`, and row 14's as
     `org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/zz_adopt_family_c_row14.tf.draft`
     (its module is not granted until the issuer amends it in). One aws_iam_role + one import block per role, labels
     namespaced to the role name.
  2. In YOUR OWN worktree, copy each into its module under a `.tf` name, run `safe-apply`'s PLAN only, and record in
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/PLAN_SURVEY_family_c.md, one line
     each per module, exactly:
       PLAN: <module>: <the plan summary line, verbatim>
       DEFAULT_TAGS: <module>: <the provider default_tags keys>
       AUTH_KEY_COLLISION: <module>: <safe-apply's KEY COLLISION line verbatim, or "none">
       STATE_KEY: <module>: <the backend state key the resources land in>
       NAMING: <module>: <the gate's verdict on the staged rename, verbatim>
     plus each role's live tags, row 14's home module with its reason, and the negative control (the plan with the
     file held out). NAMING is graded WITHOUT committing: stage the rename and run
     `python .tools/naming-gate.py --diff <the staged diff file>` (row Z-S35's safe probe). If either name is refused
     on a limb the placement override does not reach, write it in the survey and STOP before any import.
     Remove the `.tf` copies, then commit only the `.tf.proposed`, the `.tf.draft` and the survey.
  3. STOP. Report the survey's lines to 2.0.0_SA_COO~ZI. The pair(s)
     ledger/NEVER_WIDEN_ROUND7_X-1_{COO,CTO}_HALF.md are written against your survey.

PHASE B -- only on the issuer's GO, after both halves are SIGNED and row 14's module is amended into <paths>:
  4. Read .open_deploys/ for the module, then open a deploy-ledger entry `iamroles-r7-family-c-<module>` per module.
  5. Rename to `.tf` and COMMIT the declaration on your worktree branch BEFORE any import (A4-r6, row Z-S27). Use the
     placement override only if the gate still refuses an adopted name; take no author override. Then `safe-apply`
     with `-target=` on the adopted aws_iam_role resource ONLY, and drain the branch into box/sitez in the same session.
     After the drain, run the untargeted module plan in the shared tree and record that it reads 0 to destroy.
     Apply only a targeted plan equal to the pair's: 1 to import, 0 to add, 0 to destroy per module, and only the
     tags_all update the pair names. Anything else: stop, file a row, do not apply.
  6. Re-plan after each apply and record in
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/POST_APPLY_family_c.md, one line
     per module, exactly:
       POST-APPLY-PLAN: <module>: 0 to add, 0 to change, 0 to destroy
     Verify LIVE after each apply: the role's trust principal, its inline and attached policy counts unchanged, and its
     tags equal to the module's default_tags. Then close each ledger entry.
```

## DEPENDENCIES

See DECOMP_R7 section 4. PHASE B waits on the pair(s) and on the amendment that admits row 14's module.

## BOUNDS

```
THE OMISSION RULE (above). NO PERMISSION MOVES: policies, trust and usage untouched (C-TWO-REMEDIES).
PHASE A applies nothing and writes nothing to AWS. PHASE B applies only the plan the pair signed.
safe-apply only (NEVER-9); the deploy ledger opens first and closes last (NEVER-2).
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/shared-infra/zz_adopt_family_c_row6.tf.proposed
infra/aws/terraform/shared-infra/zz_adopt_family_c_row6.tf
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-x-1.adopt-family-c.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-x-1).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-x-1"><invocation>bash -c "n=\$(ls infra/aws/terraform/*/zz_adopt_family_c_row*.tf 2>&1 | grep -c '\.tf\$'); echo files=\$n; cat infra/aws/terraform/*/zz_adopt_family_c_row*.tf | grep -c -E '^[[:space:]]*(inline_policy|managed_policy_arns)'"</invocation><expect>`files=2` followed by `0` -- both declarations exist under their .tf names and neither sets inline_policy or managed_policy_arns; files=0 or 1 means PHASE B has not landed for every module</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-x-1"><invocation>grep -c -E '^POST-APPLY-PLAN: .+: 0 to add, 0 to change, 0 to destroy$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/POST_APPLY_family_c.md</invocation><expect>exactly 2 -- each module plans clean after its apply; fewer is a finding recorded in that file</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-x-1"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r7-family-c') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r7-family-c* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=2` -- two ledger entries whose own Status line reads CLOSED (a file merely existing does not count; it is written at OPEN time)</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-x-1" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did each apply
  move custody without moving a permission or row 6's in-use trust, and did the survey name every tag and the naming
  verdict before the pair was signed?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>7</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-x-1</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 7) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-6 slug (msg 33175, REMEDIATION_v6.Z.md @bd4025ade2) -> `ROUND_ANALYSIS.round6.md` @2f49aa235b E1 -> L5 round-7 decomp -> this issuance.
**Risk WORLD:** a Terraform import of existing IAM roles, two phases, PHASE B under its own never-widen pair per module.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 120`, BUDGET REACHED, 1 of 6 carriers, C1=23 (7 gates POSITIVE), C2=23 PARTIAL (0 of 23 scanned), rc=3; PARTIAL_OR_BLIND, not read as clean; the assignee reads .open_deploys/ for each module before its ledger opens.
comp-iam: RUN -- `bash .tools/comp-iam stats`: 219 IAM roles parsed / 196 services / 175 Lambda services; neither role is declared at the cut (Grep of name= over infra/aws/terraform/*.tf at 04:0xZ finds only the six declared rows).
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 4 of 4 (omission rule, A4-r6 order, smartx -target bound, live-read positive control; DECOMP_R7 section 2).
</preflight>

**Preflight disposition:** checks dry-run at the base before the cut: AC1 base FAIL as expected (`files=0`); AC2 base FAIL as expected (file absent); AC3 base FAIL as expected (`open=0 closed=0`).
