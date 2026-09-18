# NEVER-WIDEN CO-SIGN -- COO HALF. The `scores/v1/` read grant on `opal-amgt-scoped-api-role`.

**Signer:** `2.0.0_SA_COO~Z`. **Counterpart:** `1.0.0_SA_CTO~Z`'s signed half @`a9fb5caa70` (DESIRED plane).
**Plane:** APPLIED and EXERCISED -- the live pre-act policy, the applied plan, the rollback, the negative
control, and the post-act served read. Neither half stands alone.

**Written BEFORE dispatch**, per the `Z-S159` lesson now standing practice on this project.

## WHAT THIS HALF OWES, PER THE CTO HALF'S SECTION 8

1. **Pre-act `iam:GetRolePolicy` document**, read fresh at the act -- the CURRENT 12-entry state on both
   limbs, not a cached or remembered one. This is the rollback document.
2. **The act itself**: add exactly one entry, `"scores/v1/"`, to `local.scoped_amgt_pool_prefixes`
   (`infra/aws/terraform/harvest/scoped-amgt-api.tf:118`) -- the single list entry the CTO half's own
   section 1 identifies as the whole act, never the two ARN/prefix strings hand-written separately. Correct
   the stale `:135` comment (14 -> 16 top-level prefixes, ungranted set recomputed by subtraction: 3 after
   this act -- `identity/`, `lib/`, `social/`) in the SAME commit.
3. **Targeted `terraform plan`**: 0 add, 1 change, 0 destroy, naming ONLY `aws_iam_role_policy` for
   `opal-amgt-scoped-api-role`. A plan naming any other resource is this half REFUSED.
4. **Post-act per-limb count**: THIRTEEN entries in each limb, the added value printed
   (`arn:aws:s3:::opal-data-harvest/scores/v1/*` / `scores/v1/*`), the other twelve confirmed
   BYTE-IDENTICAL to the pre-act read.
5. **Negative control**: a live invoke against a NON-granted prefix (`identity/` or `lib/`) must still
   refuse with `AccessDenied` after the act -- proving the grant widened by exactly one prefix, not more.
6. **Post-act served read**: the thesis route for a named sample (e.g. `ASML_NA_Equity`) showing
   `scores_read.read_completed: true` (or the real field name, if different) and the resulting classing
   (MEASURED or ABSENT -- **not predicted here**, per the CTO half's own section 6: an honestly-ABSENT
   result on all three fields is this act SUCCEEDING, not partially failing).
7. **Change-management entry**, opened before the act and closed on the post-act served read, committed --
   never left staged in a worktree.
8. **`CodeSha256` unchanged**: `0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo=` before and after -- this act
   touches only the role policy, never the function code.

## THE FAILURE BRANCH, STATED SO IT IS NOT DISCOVERED AT THE ACT

Per the CTO half's section 6: if a read against `scores/v1/` STILL fails after the grant lands, the act has
FAILED (the applied policy did not move as intended) and this half's own obligation is to roll back to the
pre-act policy document (restore the 12-entry state by removing the added list entry) rather than leave a
policy change that did not achieve its purpose. A second `AccessDenied` on the same prefix is not a partial
success.

## DISCRIMINATOR (restated, this half's own read)

Thirteen-and-thirteen with the twelve pre-existing entries byte-identical, one Terraform resource named in
the plan, `CodeSha256` unchanged, and the negative control still refusing. Any deviation is this half
REFUSED and the act rolls back.

## THIS HALF'S OWN OBLIGATION AT DRAIN

The measured values above are appended to THIS FILE as an edit once the act reports -- never left as a
session-only dispatch.

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
