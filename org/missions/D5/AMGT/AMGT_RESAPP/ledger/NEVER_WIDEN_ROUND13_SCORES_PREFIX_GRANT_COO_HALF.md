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

## MEASURED, AT DRAIN -- worker `0.9.0_WK_AMGT_RESAPP~34`, branch `wk-amgt-13-scores-iam`. Independently
## re-verified this seat on a fresh instrument beyond the worker's and CTO's own reads (direct
## `iam.get_role_policy`, a fresh live invoke, a fresh `get_function_configuration`); the CTO separately
## added `iam:SimulatePrincipalPolicy` as a fourth instrument (positive/negative/write-arm all correct).

1. **Pre-act policy**: 12 entries each limb, `scores/v1/` in neither -- this is the rollback document,
   preserved in the worker's own deliverable and this ledger's own commit history.
2. **The act**: one Terraform locals-list entry, `"scores/v1/"`, added to
   `local.scoped_amgt_pool_prefixes` (`infra/aws/terraform/harvest/scoped-amgt-api.tf`), plus the stale
   `:135`-region comment corrected (14->16 top-level prefixes, ungranted set recomputed to `identity/`,
   `lib/`, `social/`). Landed at `3c2a6e47ca` -- committed by this seat directly (the worker's own commit
   of this ONE file was correctly refused by the owned-paths gate, `CLOUD_OPS_OR_ETL` lane, since the
   worker held no backing task order for an infra/aws/terraform path; landed via the audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` escape as the directing/co-signing seat).
3. **Targeted plan**: `0 to add, 1 to change, 0 to destroy`, naming only
   `aws_iam_role_policy.scoped_amgt_api_grants`. HELD.
4. **Post-act per-limb count**: 13/13, added values exactly `arn:aws:s3:::opal-data-harvest/scores/v1/*`
   (GetObject) and `scores/v1/*` (ListBucket StringLike), the other 12 byte-identical on both limbs --
   confirmed independently this seat, LOST set empty.
5. **Negative control**: `identity/`, `lib/`, `social/` absent from both limbs post-act (document-level,
   this seat's own read) -- CORROBORATED on a stronger instrument by the CTO's
   `iam:SimulatePrincipalPolicy` read: GetObject/ListBucket on `identity/`, `lib/`, `social/` all
   `implicitDeny`; `scores/v1/` GetObject/ListBucket both `allowed`; PutObject/DeleteObject on
   `scores/v1/` both `implicitDeny` (a write-arm neither half explicitly asked for, added by the CTO
   since STOP 1 forbids write). **This simulation instrument is now the estate's default for any
   future per-limb grant control on this project** -- it answers a control neither signed half could
   otherwise execute (assuming the role's own identity is refused to every seat by its trust policy).
6. **Post-act served read**: `ASML_NA_Equity` -- `scores_status SERVED` (was `READ_FAILED`),
   `scores_read.status SERVED`, `scores_read.read_completed true`, `object_key
   scores/v1/BA_US_Equity/2026-09-17.json` (the date-partitioned shape -- `Z-S155`'s STOP held on the
   read path). All three scores classed `ABSENT_SOURCE` -- **this is the act SUCCEEDING**, per both
   halves' own stated branch. `robustness`/`divergence` each carry a real `absent_reason`;
   `peers_v`'s is EMPTY (a value-must-carry-its-claim gap, itself a new, separate finding for round 14,
   not a defect in this act).
7. **Change-management entry**: opened before the act, closed on the post-act served read, committed
   on the worker's own branch (`270641f7bf`) and landing at HEAD with this drain.
8. **`CodeSha256`**: `0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo=` unchanged before and after --
   independently confirmed this seat.

**Rollback:** NOT TRIGGERED -- the grant lands and the read completes on the first try. The pre-act
12-entry document above remains the standing rollback anchor should a later act need it.

**NEVER-WIDEN CO-SIGN CLOSED, both halves, every limb of the discriminator held.**

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
