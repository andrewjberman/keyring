# NFRA_IAMROLES202609.TO-IAM-r-5 -- THE TWO PRODUCTION SERVING-PATH ROLES: declared, and adoption PROVED SAFE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md</decomp_doc>
<owned_cells>IAM-r-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~6</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; acceptance property 1)

```
IAM-r-5. ACT: write Terraform declarations for the two PRODUCTION SERVING-PATH roles --
portal-auth-lambda-role and opal-data-refresh-lambda-role -- and PROVE, before anything is applied,
that adopting them would destroy nothing.

⛔⛔ READ THIS PARAGRAPH FIRST. THE ISSUER HAS ALREADY MADE THIS CALL SO YOU NEVER FACE A CHOICE
BETWEEN CAUSING AN OUTAGE AND STOPPING.

  THIS CELL IS AN ADOPTION, NOT A CREATION. Both roles EXIST AND SERVE PRODUCTION TRAFFIC RIGHT NOW.
  Nothing here creates them, and nothing here may destroy or replace them.

  THIS CELL DOES NOT APPLY AND DOES NOT MUTATE TERRAFORM STATE. No `terraform apply`, no
  `safe-apply`, no `terraform import` that writes state, no `aws iam` call that changes anything.
  The deliverable is A DECLARATION plus A PLAN THAT PROVES ADOPTION IS SAFE.

  WHY THE BAR IS THE PLAN AND NOT THE APPLY, measured at this round's cut and not inherited:
  `infra/aws/terraform/data-refresh/main.tf` carries ZERO `resource "aws_iam_role"` blocks and FOUR
  `resource "aws_iam_role_policy"` blocks that attach inline policies to opal-data-refresh-lambda-role
  BY NAME STRING, plus hardcoded role ARNs. So TERRAFORM ALREADY MANAGES POLICIES ON A ROLE IT DOES
  NOT OWN. A plan that destroyed or replaced that role would ORPHAN FOUR LIVE POLICY ATTACHMENTS on a
  production serving path -- which is precisely the outage `C-NO-ACCESSDENIED` forbids this project
  from causing. The plan is the instrument that tells you whether that is a risk. Run it; do not
  outrun it.

  ⛔ A PLAN SHOWING **destroy** OR **replace** ON EITHER ROLE IS A HARD STOP: file a BLOCKING surprise
  row with the plan output quoted, and STOP ON THAT CRITERION. Do not "fix" it by applying anyway,
  and do not adjust the declaration until the plan is quiet if you do not understand WHY it was
  noisy -- a plan made quiet by guessing is worth less than a noisy one you understood.

THE TWO ROLES ARE IN DIFFERENT STATES AND THE DECLARATIONS DIFFER ACCORDINGLY:
  portal-auth-lambda-role         ZERO hits in infra/aws/terraform -- absent outright.
  opal-data-refresh-lambda-role   NINE hits, all references, none a declaration (above).

THE SHAPE IS CLOSED AT THE CUT: a deliverable at
    .../deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md
carrying, per role: the live role as read from AWS (trust policy, attached and inline policies), the
proposed `resource "aws_iam_role"` declaration, the PLAN OUTPUT VERBATIM, and an explicit line
stating whether the plan destroys or replaces anything. The declarations themselves go in the
Terraform module as commented-out or `.tf.proposed` text -- NOT as live `.tf` that a peer's apply
could pick up. ⛔ DO NOT LEAVE AN ACTIVE .tf FILE THAT ANOTHER SEAT'S APPLY WOULD EXECUTE.
```

## DEPENDENCIES

This cell depends on **IAM-r-3**, keyed to OBSERVED COMPLETION -- it establishes that these two are
genuinely in the undeclared set. ⛔ **IF `IAM-r-3` FOUND EITHER ROLE IS ALREADY DECLARED SOMEWHERE,
THAT ROLE DROPS OUT OF THIS CELL** and the finding is recorded instead. This round has already found
one member misfiled; do not adopt something that is already in code.

## BOUNDS -- what this cell may not cross

```
⛔ C-NO-ACCESSDENIED (D5): the project must not cause the outage it exists to prevent. These are
PRODUCTION SERVING-PATH roles. Everything below follows from that.

⛔ NO APPLY, NO STATE MUTATION, NO AWS WRITE. Reads of live AWS state are expected and fine
(`aws iam get-role`, `list-role-policies`, `list-attached-role-policies`). Anything that changes
AWS or Terraform state is out of this cell.

⛔ THE PLAN IS THE DELIVERABLE'S EVIDENCE AND ITS OUTPUT IS QUOTED VERBATIM. A summary of a plan is
not a plan. If the plan cannot be produced at all -- no backend access, a locked state, a version
that lacks the mechanism -- that is a BLOCKING row naming what stopped it, not a substitute.

⛔ IF ANY WORLD-CHANGING ACT NEVERTHELESS BECOMES NECESSARY, NEVER-2 BINDS AND ITS ORDERING IS NOT
NEGOTIABLE: open the change-management entry BEFORE the act, ACT, then CLOSE AND COMMIT the entry AND
the sentinel BEFORE taking the grading reads -- because a worker can die at any instruction boundary
and only what is committed or true in the world survives. `safe-apply`, never bare `terraform apply`.
⚠ THOSE PATHS ARE GRANTED SO NEVER-2 IS SATISFIABLE, NOT AS PERMISSION TO ACT. This order does not
authorise an apply.

⛔ comp-blast IS OWED AT THIS CELL. The L5 battery declared it not-applicable for the round as a whole
and deferred it here, because this is the cell that changes Terraform custody. Run it against the
candidate change and cite it.

⛔ C-TWO-REMEDIES: this is the GOVERNANCE axis. Declaring a role is not narrowing it. Do not adjust
any permission, and do not recommend a narrowing -- if you notice one, that is a surprise ROW.

DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED).
C-ANALYZER-PRICED-FIRST + G-25: no AWS Access Analyzer.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
THE ROUND-2 CUT'S OWN MEASUREMENT, and it is the reason this cell is shaped as a proof rather than a
change:
  opal-data-refresh-lambda-role  9 hits in infra/aws/terraform, NONE a declaration.
                                 data-refresh/main.tf: 0 aws_iam_role blocks, 4 aws_iam_role_policy
                                 blocks (data_refresh_sscn_s3, data_refresh_cloudfront_read,
                                 data_refresh_time_machine_invoke,
                                 portal_time_machine_invoke_downstream), plus role_arn strings at
                                 main.tf:38,124 and qa-scratch-instance.tf:19. Its own comment at
                                 :53 says "attached to the PRE-EXISTING ... role".
  portal-auth-lambda-role        0 hits.

comp-iam (round-2 battery, RUN): 195 TF roles / 188 services / 1084 ops / 304 gaps; wafv2:UNMODELED
and UNMAPPED-METHOD -- 304 is a FLOOR on the DESIRED plane. ⛔ AND ITS TWO REUSE NOTEs BEAR DIRECTLY
ON THIS CELL: TF role labels `orchestrator` and `scheduler` were each reused across three modules and
SILENTLY MIS-LINKED their inline policies before a fix. If your declaration reuses a label that
already exists in another module, you can reproduce that class. Namespace the resource label.

comp-schedule (round-2 battery, RUN to completion): GATES ARMED 25. C2, the deploy-ledger carrier,
reads 6 -- other projects' open entries, none of them this project's and none of them yours to close.
G-17, G-21 and G-23 bind this cell.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-5.production-roles-declared-and-adoption-proved-safe.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/data-refresh/
infra/aws/terraform/
</paths>

`change_management/`, `.open_deploys/` and `ledger/` are granted so NEVER-2 is SATISFIABLE if a deploy
is ever opened here -- they are NOT permission to open one and this order does not authorise an apply.
`infra/aws/terraform/` is granted for READING; `infra/aws/terraform/data-refresh/` is the one module
you may write a proposed declaration into, and it must not be live `.tf` a peer's apply would execute.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W6-S<k>`, `"fabric": "site-z"`. A BLOCKING row is read by the COO in your final report; an OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-r-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md && grep -c -E 'portal-auth-lambda-role|opal-data-refresh-lambda-role' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md</invocation><expect>a count of 2 or greater -- both roles are addressed by name, neither silently dropped; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-r-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md && grep -c -i -E 'resource "aws_iam_role"' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md</invocation><expect>a count of 2 or greater -- a proposed declaration exists for each role, which is what "brought into code" means; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-r-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md && grep -c -i -E 'will be destroyed|must be replaced|forces replacement' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md</invocation><expect>a count of 0, printed -- the quoted plan output contains no destroy and no replacement on either production role, which is the whole safety bar; a nonzero count means the plan was destructive and the cell must have STOPPED with a BLOCKING row rather than recorded it as a pass</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-r-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md && grep -c -i -E 'comp-blast' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md</invocation><expect>a count of 1 or greater -- the comp-blast lens the L5 battery deferred to this exact cell was run and cited; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-r-5"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md && grep -c -i -E 'terraform apply|safe-apply|terraform import|put-role-policy|delete-role|APPLIED-TO-PRODUCTION' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/ADOPTION_PLAN.md</invocation><expect>a count of 0, printed -- nothing was applied and no state was mutated; the cell proved adoption safe and stopped there, which is what C-NO-ACCESSDENIED requires of it</expect></criterion>
  <criterion id="AC6" cell_refs="IAM-r-5" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): both roles addressed
- **AC2** (mechanical): a real declaration exists per role -- the deliverable of "bring them into code"
- **AC3** (mechanical, NEGATIVE and the safety bar): the plan destroys and replaces nothing. A destructive plan is a STOP, never a recorded pass
- **AC4** (mechanical): the comp-blast lens deferred to this cell was run
- **AC5** (mechanical, NEGATIVE): nothing was applied and no state mutated
- **AC6** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): would an engineer reading this deliverable be willing to run the adoption on a production serving path -- is the plan understood rather than merely quiet, and does the declaration match the live role closely enough that adoption is a bookkeeping act rather than a change? A plan can be quiet because nothing is wrong or because the declaration is too vague to disagree with anything, and only a reader can tell those apart.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- bound every AWS read and scope every Terraform read to one module.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L6, round 2) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @076f37eeb2
**Authority chain:** round-1 slug @fd7a0b3e91 -> `ROUND_ANALYSIS.round1.md` @b647fd4f63 section 4, which re-scopes these two as "NOT an ownership question ... the answer is almost certainly BRING THEM INTO TERRAFORM, which is WORK and is cuttable now" -> L5 round-2 decomp @fde51f6e6a sections 1a and 2c -> this issuance.
**Chain:** the measurement chain, position 3 of 3 (IAM-r-2 -> IAM-r-3 -> IAM-r-5).
**ISSUER'S RECORDED SPECIFICATION CALL, flagged for the CVO at L9 -- THE SECOND OF THIS PROJECT AND THE SAME SHAPE AS THE FIRST:** the analysis authorises bringing these roles into Terraform as work. This order cuts the WORK as *declaration plus a plan proving adoption destroys nothing*, and puts the APPLY out of the cell. Reasoning: both roles serve production; one has four live policy attachments hanging off it by name, so a destroy/replace would orphan them; and `C-NO-ACCESSDENIED` forbids this project causing the outage it exists to prevent. Where an authorisation and a bound conflict, the bound wins and the cell stops at the last provably safe step. If the CVO grades this too conservative, the remedy is a round-3 cell that applies under a change-management entry with the plan already in hand -- which is strictly cheaper and safer than the reverse mistake. This is the same call this issuer made on the round-1 pre-flight cell, made the same way, and recorded rather than left implicit.
**Provenance:** the policy-attached-but-undeclared state is this round's own pre-cut measurement, at decomposition section 1a and channel row Z-S8.
<preflight>
comp-schedule: RUN to completion, 5 of 5 carriers, 14.5 s, rc=0. C1=23 C2=6 C3=12 C4=20 C5=335. GATES ARMED 25; G-17, G-21 and G-23 bind this cell. C2's six deploy-ledger entries belong to other projects and none is this cell's to close.
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; BLIND on wafv2 (UNMODELED) and UNMAPPED-METHOD. Its two reuse NOTEs are inlined because a new declaration reusing an existing module label can reproduce exactly the silent mis-link they describe.
comp-find --corpus aws: RUN -- 219 nodes, LIVE-no-DECLARED=16, vintage 2026-09-10 12:21:58 UTC.
comp-blast: DECLARED-NOT-APPLICABLE at L5 for the round as a whole and EXPLICITLY DEFERRED TO THIS CELL; it is OWED here and AC4 grades it.
comp-adversary: RUN on the round-2 decomposition; its declaration records that this lane has NOT inspected either production role's live policy -- this cell does that.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-2 vintage. comp-blast is the one non-core lens owed here. comp-routes, comp-cache, comp-transform and comp-pipescript are DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, data prop or gold script.
