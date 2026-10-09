# NFRA_IAMROLES202609.TO-IAM-w-1 -- ADOPT Family B (row 9, SmartX) into smartx-pipeline: survey, pair, apply

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R6.md</decomp_doc>
<owned_cells>IAM-w-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-4; the round-5 analysis calls this E1)

```
IAM-w-1. ACT: adopt row 9 `opal-smartx-lambda-role` (Family B, SmartX) into Terraform under the CTO's ruling (ROUND_ANALYSIS.round5.md @f77e32d7c3 E1) and
ADOPTION_PLAN_TEN.md @59112aafed (your own plan, Family B). You are owner of record (ruling @fa8ec0e726).

FWD-4, verbatim: "Every role is either in code or has a named owner and a reason". This order moves 1 role(s)
from "named owner" to "in code".

ROLES: `opal-smartx-lambda-role` (3 inline policies: opal-smartx-logs, opal-smartx-s3-access, opal-smartx-secrets)
MODULE(S): `infra/aws/terraform/smartx-pipeline/`

THE OMISSION RULE, binding: each `aws_iam_role` block carries name, path, description, assume_role_policy,
max_session_duration (as live) and NOTHING about policies. `inline_policy` and `managed_policy_arns` are ABSENT.
Setting either makes it authoritative and the next run detaches every live policy it does not list.
Three inline policies make the omission rule matter most here.

PHASE A -- no apply:
  1. Read each role live (get-role, list-role-policies, list-attached-role-policies, list-role-tags) and write the
     declaration as `infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf.proposed`: one aws_iam_role + one import block per role, labels namespaced to the role name
     (round 2's candidate infra/aws/terraform/data-refresh/zz_adoption_candidate.tf.proposed is the shape).
  2. In YOUR OWN worktree, copy each file to a `.tf` name and run `safe-apply`'s PLAN only (no apply). Record in
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/round6/PLAN_SURVEY_family_b.md, one line each per module, exactly:
       PLAN: <module>: <the plan summary line, verbatim>
       DEFAULT_TAGS: <module>: <the provider default_tags keys>
       AUTH_KEY_COLLISION: <module>: <safe-apply's KEY COLLISION line verbatim, or "none">
       STATE_KEY: <module>: <the backend state key the resources land in>
     plus each role's live tags. Remove the `.tf` copy; commit only the `.tf.proposed` file(s) and the survey.
  3. STOP. Report the survey's lines to 2.0.0_SA_COO~ZI. The never-widen pair
     ledger/NEVER_WIDEN_ROUND6_W-1_{COO,CTO}_HALF.md is written against your survey.

PHASE B -- only on the issuer's GO, after both halves are SIGNED:
  4. Open a deploy-ledger entry named `iamroles-r6-family-b` (one per module) in org/critical_paths/change_management/
     with its .open_deploys/ marker.
  5. Rename each `.tf.proposed` to `.tf` and `safe-apply`. Apply only a plan that equals the survey's (N to import,
     0 to add, 0 to destroy, plus only the tag updates the pair names). Anything else: stop, file a row, do not apply.
  6. Run the plan again after the apply and record in org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/round6/POST_APPLY_family_b.md, one line per module, exactly:
       POST-APPLY-PLAN: <module>: 0 to add, 0 to change, 0 to destroy
     (or the real line if it differs, which is a finding). Then close each ledger entry.
```

## DEPENDENCIES

See DECOMP_R6 section 4. PHASE B waits on both never-widen halves.

## BOUNDS

```
THE OMISSION RULE (above). NO PERMISSION MOVES: the role's policies, trust and usage are untouched (C-TWO-REMEDIES).
PHASE A applies nothing. PHASE B applies only the plan the pair signed.
safe-apply only (NEVER-9); the deploy ledger opens first and closes last (NEVER-2).
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf.proposed
infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/round6/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-w-1.adopt-family-b-smartx.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-w-1).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-w-1"><invocation>grep -c -E '^[[:space:]]*(inline_policy|managed_policy_arns)' infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf</invocation><expect>exactly `0` -- the declaration exists under its .tf name and sets neither inline_policy nor managed_policy_arns; a "No such file" error means PHASE B has not landed</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-w-1"><invocation>grep -c -E '^POST-APPLY-PLAN: .+: 0 to add, 0 to change, 0 to destroy$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~Z/round6/POST_APPLY_family_b.md</invocation><expect>exactly 1 -- each module plans clean after its apply, so the declaration matches live; fewer is a finding recorded in that file</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-w-1"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r6-family-b') closed=\$(ls org/critical_paths/change_management/ | grep -c 'iamroles-r6-family-b')"</invocation><expect>`open=0` and `closed=` 1 or greater -- each module's ledger entry opened and closed</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-w-1" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did the apply move
  custody without moving a permission, and did the survey name every tag the apply wrote before the pair was signed?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>6</round>
<slot>0.7.0_AE_CloudOps~Z</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-w-1</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 6) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-5 slug @f022594845 -> `ROUND_ANALYSIS.round5.md` @f77e32d7c3 E1 -> L5 round-6 decomp -> this issuance.
**Risk WORLD:** a Terraform import of existing IAM roles, two phases, PHASE B under its own never-widen pair.
<preflight>
comp-schedule: RUN at round 5 -- `python .tools/comp-schedule --budget 220`, BUDGET REACHED, 1 of 6 carriers, C1=23, C2=22 PARTIAL, rc=3; PARTIAL_OR_BLIND, not read as clean; the assignee reads .open_deploys/ for its module before any ledger opens.
comp-iam: RUN -- `bash .tools/comp-iam stats`: 214 IAM roles parsed / 196 services / 1154 operations; none of this order's roles is declared at the cut (ADOPTION_PLAN_TEN section 0).
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 3 of 3 (omission rule, default_tags hazard, row 2 ECS trust; DECOMP_R6 section 2).
</preflight>

**Preflight disposition:** checks dry-run at the base `6e61646e81`: AC1 base: FAIL as expected (file absent); AC2 base: FAIL as expected (file absent); AC3 base: FAIL as expected (`open=0 closed=0`).
