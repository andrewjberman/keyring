# NFRA_IAMROLES202609.TO-IAM-x-2 -- NARROW the dead grants (Z-S23 opal-smartx-lambda-role, Z-S32 codebuild-semantic-clustering-role): survey, pairs, one apply per module

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R7.md</decomp_doc>
<owned_cells>IAM-x-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-4 enrichment; the round-6 analysis calls this E2)

```
IAM-x-2. ACT: remove the inline-policy statements that grant only on resources that do not exist, on two roles, under
ROUND_ANALYSIS.round6.md @2f49aa235b E2. WHY: an S3 bucket name is global, so an Allow on a bucket that does not exist
grants access to whoever creates that name later. Removing a dead statement is a NARROWING, a WORLD act under its own pair.

TARGETS (as surfaced; re-read every one LIVE, never trust these lines):
  Z-S23  opal-smartx-lambda-role (module smartx-pipeline, which carries three pre-existing Lambda drifts, row Z-S21):
         inline `opal-smartx-s3-access` names opal-data-smartx and opal-code-smartx (NoSuchBucket at the 10-09 read);
         inline `opal-smartx-secrets` names arn:aws:secretsmanager:us-east-2:313476888478:secret:opal/smartx/config-*
         (the only such secret is in us-east-1). `opal-smartx-logs` is NOT a target.
  Z-S32  codebuild-semantic-clustering-role (module news-pipeline; IN USE, last used 2026-09-11):
         inline `CodeBuildSemanticClusteringPolicy` names a bucket read as NoSuchBucket (1.0.0_SA_CTO~Z, w-3 CTO half).

  A2-r7 (issuer, 2026-10-11 ~05:5xZ, on 1.0.0_SA_CTO~Z's observation in msg 33206 at the x-1 CTO half @1e7ff2decd):
         sentiment_query_api-role (row 14, module market-overview): inline `DynamoDBAccess` names a us-east-2 table
         that does not exist. It is a THIRD target, under the same rule, read live in its own region. Its file is
         `infra/aws/terraform/market-overview/zz_narrow_row14.tf(.proposed)`. In market-overview, this narrowing's
         apply serializes behind IAM-x-1's row-14 adoption on `.open_deploys/` (adoption first), and it stays
         -target only: the module would otherwise recreate the deleted bucket market_data_v2.

RULE OF REMOVAL: a statement is removed only if EVERY resource it names is read live as non-existent. Every other
statement stays byte-identical. Nothing is added; no trust and no tag changes. The aws_iam_role blocks keep the omission
rule (they never set inline_policy or managed_policy_arns); an inline policy is managed ONLY as its own
aws_iam_role_policy resource.

PHASE A -- no apply, no AWS write:
  1. For each target policy: get-role-policy, then read EVERY resource ARN in it live (s3api head-bucket /
     get-bucket-location; secretsmanager describe-secret in the ARN's own region). Beside the dead ones, read ONE
     resource that does exist with the same call as a positive control, because a failed read returns a value too.
     Write org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/NARROW_SURVEY.md with one
     line per removed ARN, exactly:
       REMOVED: <arn> LIVE-READ: <NoSuchBucket | ResourceNotFoundException | the exact error code>
     at least one line, exactly:
       CONTROL: <existing arn> FOUND
     and per policy a verdict: NARROW (some statements stay) or DELETE (every statement is dead).
  2. Declare each target policy as an aws_iam_role_policy with an import block, AS LIVE, in
     `infra/aws/terraform/smartx-pipeline/zz_narrow_z_s23.tf.proposed` and
     `infra/aws/terraform/news-pipeline/zz_narrow_z_s32.tf.proposed`. In YOUR OWN worktree plan each under a `.tf` name
     (PLAN only), with `-target` in smartx-pipeline. Record in NARROW_SURVEY.md, per module, the PLAN line (expect
     imports and 0 changes, which proves the as-live declaration), the narrowed document's diff, and the plan the
     narrowing would produce. For a DELETE policy, propose the Terraform-native route (for example import, then remove,
     as two applies under one ledger). Grade the staged files with `python .tools/naming-gate.py --diff <staged diff>`,
     WITHOUT committing. Remove the `.tf` copies; commit only the `.tf.proposed` files and the survey.
  3. STOP. Report to 2.0.0_SA_COO~ZI. The pair(s) ledger/NEVER_WIDEN_ROUND7_X-2_{COO,CTO}_HALF.md are written against
     your survey and name, per module, exactly which statements leave and that nothing else moves.

AMENDMENT A3-r7 (issuer, 2026-10-11 ~06:5xZ, on NARROW_SURVEY.md @6b0ba5dac4, msg 33223) -- THIS GOVERNS PHASE B:
  - TARGETS 1 + 2 (opal-smartx-s3-access, opal-smartx-secrets on the ORPHAN opal-smartx-lambda-role): DELETE through the
    IAM API, not Terraform: `aws iam delete-role-policy` for each, under ONE NEVER-2 entry `iamroles-r7-narrow-smartx`
    whose rollback leg is `aws iam put-role-policy` with each policy's as-live document, saved first to
    .../round7/ROLLBACK_smartx_<policy>.json from get-role-policy. Remove the inert zz_narrow_z_s23.tf.proposed in
    the same commit; it is never applied. The x-4 ruling took the same route. It avoids the two-apply
    import-then-remove, and the canon collision smartx-s3-access / opal-smartx-s3-access disappears, because the
    colliding name never enters the module. smartx-pipeline is NOT applied.
  - TARGET 3 (CodeBuildSemanticClusteringPolicy, news-pipeline): the rule of removal is extended to RESOURCE GRAIN for
    this target. From statement `S3Access`, remove ONLY `arn:aws:s3:::codebuild-semantic-clustering-artifacts/*`
    (read 404). `opal-data-news-v2/*`, the statement's actions and the other three statements stay byte-identical.
    This is the cell's own WHY at its sharpest: a global bucket name with read+write on an IN-USE role. Terraform:
    import, then the one-element Resource edit, -target only, in the A4-r6 order.
  - TARGET 4 (DynamoDBAccess on sentiment_query_api-role, market-overview): HELD. Nothing is applied. Wrong-region,
    not dead; no squatting hazard; the role's only data grant. DELETE vs REPOINT is a product call (a repoint is a
    widening), carried to 1.0.0_SA_CTO~Z in the round's L10 slug. Remove the inert zz_narrow_row14.tf.proposed.
  - The pair(s) are written per act: smartx (2 policy deletes) and news-pipeline (1 Resource element).
PHASE B -- only on the issuer's GO, after both halves are SIGNED:
  4. Read .open_deploys/ for the module, then open a deploy-ledger entry `iamroles-r7-narrow-<module>` per module.
  5. Commit the declaration on your worktree branch BEFORE any import (A4-r6, row Z-S27); then `safe-apply` with
     `-target=` on the declared aws_iam_role_policy resource(s) ONLY; then drain the same session; then record that the
     untargeted shared-tree plan reads 0 to destroy (smartx-pipeline's three Z-S21 drifts stay as before).
  6. Record in org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/POST_APPLY_narrow.md,
     one line per module, exactly:
       POST-APPLY-PLAN: <module>: 0 to add, 0 to change, 0 to destroy
     Verify LIVE: each REMOVED arn is gone from the role's policies, every other statement is unchanged, and trust and
     tags are unchanged. Then close each ledger entry.
```

## DEPENDENCIES

See DECOMP_R7 section 4. PHASE B waits on the pair(s). If row 14 (IAM-x-1) is homed in news-pipeline, the two applies
there serialize on `.open_deploys/`.

## BOUNDS

```
RULE OF REMOVAL (above): only all-dead statements leave; nothing is added; trust and tags do not move.
THE OMISSION RULE on aws_iam_role blocks stands; inline policies only as aws_iam_role_policy resources.
smartx-pipeline: -target ONLY (row Z-S21). safe-apply only (NEVER-9); the ledger opens first and closes last (NEVER-2).
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/smartx-pipeline/zz_narrow_z_s23.tf.proposed
infra/aws/terraform/smartx-pipeline/zz_narrow_z_s23.tf
infra/aws/terraform/news-pipeline/zz_narrow_z_s32.tf.proposed
infra/aws/terraform/news-pipeline/zz_narrow_z_s32.tf
infra/aws/terraform/market-overview/zz_narrow_row14.tf.proposed
infra/aws/terraform/market-overview/zz_narrow_row14.tf
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-x-2.narrow-the-dead-grants.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-x-2).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-x-2"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/NARROW_SURVEY.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo removed=\$(grep -c '^REMOVED: ' \$f) dead=\$(grep -c -E '^REMOVED: .+ LIVE-READ: [A-Za-z]+\$' \$f) control=\$(grep -c -E '^CONTROL: .+ FOUND\$' \$f)"</invocation><expect>`removed=N dead=N control=M` with N at least 3 and equal in both places, and M at least 1 -- every removed ARN carries a live non-existence read, beside at least one positive control</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-x-2"><invocation>grep -c -E '^POST-APPLY-PLAN: .+: 0 to add, 0 to change, 0 to destroy$' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/POST_APPLY_narrow.md</invocation><expect>exactly 1 -- news-pipeline plans clean after its one-element narrowing (A3-r7: smartx deletes go through the IAM API with no plan; market-overview is held); fewer is a finding recorded in that file</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-x-2"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r7-narrow') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r7-narrow* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=2` -- two ledger entries (smartx IAM-API deletes, news-pipeline apply; A3-r7) whose own Status line reads CLOSED</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-x-2" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did each removed
  statement name only non-existent resources, read live against a positive control, and is every remaining statement,
  the trust and the tags byte-identical to before?

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
<to_id>NFRA_IAMROLES202609.TO-IAM-x-2</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 7) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-6 slug (msg 33175, REMEDIATION_v6.Z.md @bd4025ade2) -> `ROUND_ANALYSIS.round6.md` @2f49aa235b E2 -> L5 round-7 decomp -> this issuance.
**Risk WORLD:** a permission narrowing on two live roles, two phases, PHASE B under its own never-widen pair per module.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 120`, BUDGET REACHED, 1 of 6 carriers, C1=23 (7 gates POSITIVE), C2=23 PARTIAL (0 of 23 scanned), rc=3; PARTIAL_OR_BLIND, not read as clean; the assignee reads .open_deploys/ for each module before its ledger opens.
comp-iam: RUN -- `bash .tools/comp-iam stats`: 219 IAM roles parsed / 196 services / 175 Lambda services; live list-role-policies: codebuild-semantic-clustering-role carries CodeBuildSemanticClusteringPolicy (1); opal-smartx-lambda-role carries 3 (round-6 close read).
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 4 of 4 (omission rule, A4-r6 order, smartx -target bound, live-read positive control; DECOMP_R7 section 2).
</preflight>

**Preflight disposition:** checks dry-run at the base before the cut: AC1 base FAIL as expected (`MISSING:` the survey); AC2 base FAIL as expected (file absent); AC3 base FAIL as expected (`open=0 closed=0`).
