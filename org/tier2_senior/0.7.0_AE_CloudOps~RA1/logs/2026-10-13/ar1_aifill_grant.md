# 0.7.0_AE_CloudOps~RA1 -- 2026-10-13 -- AMGT_RESAPP AMGT-ar-1: the adapter role reads the AI-fill prefix; one list entry, one targeted apply, check YES 7 of 7

**Date:** 2026-10-13 ET (GO 00:35Z, msg 5310; apply 00:38:18Z-00:39:53Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-ar-1.the-adapter-role-reads-the-ai-fill-prefix
**Status:** APPLIED AND VERIFIED; AC1 and AC2 PASS; ledger CLOSED 7 of 7

## Objective

Step 1 of the FWD-41 never-widen pair: add `amgt/harvest/gold/ai_fill/` to `local.scoped_amgt_pool_prefixes` so the inline policy `opal-amgt-scoped-api-grants` grants `s3:GetObject`
and `s3:ListBucket` on it. Additive on an empty prefix. The function's code is untouched.

## The act
**archetype:** DEPLOY

1. Printed the constant (`amgt/harvest/gold/ai_fill/`); `check_ar1_grant.py` before: NO (4 of 7), 7 statements, 34 resources, sha16 `77c69f8359764942`, the half's values.
2. Opened the 7-leg ledger entry, then added the one entry (+6 lines with its comment) to `scoped-amgt-api.tf`.
3. Targeted plan of `aws_iam_role_policy.scoped_amgt_api_grants`, graded from its JSON: 1 update; Resource 34 -> 35 (the `ai_fill/*` ARN only); Condition 34 -> 35 (`ai_fill/*` only).
4. Targeted `safe-apply` of the saved plan: 0 added, 1 changed, 0 destroyed. Check after: YES (7 of 7); sha16 `77c69f8359764942` -> `b50b9248dbcc7d02`.
5. AC2: 2 names captured, non-200 none.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L7, close | PASS | opened before the edit |
| check_ar1_grant.py | before and after | NO 4/7 -> YES 7/7 | |
| terraform plan -target, show -json, safe-apply.sh | one resource | PASS | 1 change |
| check_ar3_aifill_served.py capture | 2 names | PASS | |

**What worked:** grading the plan from its JSON per statement before the apply; the check's own stripped-entry control.
**What failed:** nothing in the act. The order lacks `<proof_genre>DEPLOY</proof_genre>` (the same defect as bk-2), so the checker will read INVALID on that one violation until the issuer adds it.
**Gap found:** none in the world.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Computed the post sha16 with the check's own `canon_sha16` form | the order asks for pre and post printed; the check prints only the control |
| Skipped record-terraform-deploy.sh | no Lambda code or source-map entry moved |

## Files Modified

- `infra/aws/terraform/harvest/scoped-amgt-api.tf` (+6)
- `org/critical_paths/change_management/20261014T0037Z_amgt-resapp-r104-ar1-aifill-grant-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the proof instance
- local only, uncommitted: `.scratch_ar1/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R2]` Add `<proof_genre>DEPLOY</proof_genre>` to the order, flip its status, and send the GO for AMGT-ar-3 when bk-2, ar-1 and the AMD store are in.
2. `[box-sync / MSTR]` Integrate the local commits.
