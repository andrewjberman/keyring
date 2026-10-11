# NEVER-WIDEN co-sign, ROUND 4 -- the COO half: act 3c, THE EXEC-SUMMARY GENERATOR'S FENCE ROW at `opal-data-49financial`

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~16:0xZ | **Act covered:** act 3c, a prerequisite of act 4b |
**Read against:** `ROUND_ANALYSIS.round3.md` ADDENDA 10 and 11 (CTO msgs 3922 and 3927), the act 3b pair (applied,
`FB-f-14` @0acccf7d8e), `NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md` (amended), cells `FB-g-23` (@51891d2693), `FB-g-27`
(the row) and `FB-g-28` (the identity policy) | **The other half:** `1.0.0_SA_CTO~DELL1`,
`ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_CTO_HALF.md`. No act begins until both halves are files at HEAD, the CTO half
reads SIGNED, `FB-g-27` is merged and graded, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius below, and ONLY it. It is inert before act 4b: nobody writes or reads the exec-summary's
keys at the canonical home until 4b moves its mode, so this act sits outside the one-day window.

## What the act MAY touch (the whole permitted set)

ONE `PutBucketPolicy` on `opal-data-49financial` through `infra/aws/terraform/shared-infra/s3-49financial.tf`, generated from ONE
new registry row (`exemptions.json`, `FB-g-27`). Principal `exec-summary-generator-role`; prefix the one directory
`advi/49financial/platinum/advisors/` (the module's `class_prefix` of the legacy class `platinum/advisors/`):

| side | what is added | carrier |
|---|---|---|
| Deny (the fence) | the role is exempt for `s3:GetObject`, `s3:ListBucket` and `s3:PutObject` under that directory ONLY; any other action or key stays denied to it (three generated Deny statements) | the scoped row |
| Allow (bucket policy, read-only) | `s3:GetObject` on `advi/49financial/platinum/advisors/*`; `s3:ListBucket` on the bucket, bounded to that directory | the module's `fence_scoped_allow_statements`, from the same row |
| Put (identity side, NOT this act) | `s3:PutObject` on `advi/49financial/platinum/advisors/*/exec_summary.json` | `FB-g-28`, the exec-summary root's own policy, its own scoped apply |

No `PutObjectAcl`, no Delete, no bucket-wide or `s3:*` row. `s3:PutObject` is exempted at the fence for the WHOLE directory
(the grammar's grain is a prefix), and is Allowed only identity-side for the one file name `exec_summary.json`: the effective
write reach is the identity policy's, and the fence exemption alone grants nothing.

**Writers counted (N rules read).** The property is who may enter the bucket and with what. LIVE: 1 writer of the bucket policy
(`aws_s3_bucket_policy.opal_data_49financial`), 1 generator (`module.opal_name`, from `exemptions.json`), 0 hand statements.
DECLARED: the same; 9 + 1 = 10 scoped rows (3b's nine and the generator's). N printed: 1 writer, 1 generator, 1 registry file.
The `advisors/` directory's WRITERS at the canonical home are separate (the 4b/4c half's census): `D_04` and
`exec-summary-generator`, N = 2.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the plan names exactly one resource (`aws_s3_bucket_policy.opal_data_49financial`), in place,
  statements 29 to 34 (three Deny and two Allow added; the blanket Deny's exemption list gains one principal); the applied
  `get-bucket-policy` equals the registry's render (`r4_act3b.py` arm L1); an IAM evaluation of `s3:GetObject` on a sample object
  of the directory with the live policy reads `allowed`; `s3:PutObject` on the sample `exec_summary.json` reads `allowed` only
  AFTER `FB-g-28` is applied (before it, the identity side is absent: `implicitDeny` is the expected read, and is stated, not a
  defect); a non-admitted role reads `implicitDeny`; a post-apply plan reads No changes.
- **Branch B -- NOT SIGNED, the act stops and rolls back:** the plan names a second resource; the rendered policy differs from
  the registry by a statement; the applied policy removes an existing Allow or Deny of 3b; any admitted principal of 3b now
  evaluates `implicitDeny`/`explicitDeny` on its granted object; `AccessDenied` on `PutBucketPolicy` for the actor (a ROUTE to
  `0.7.0_AE_CloudOps~FBL`, not a failure). Rollback: the prior policy (printed before the apply) put back the same hour; the
  row stays at HEAD as the record.

## What this half does not know (stated)

- Whether an organization SCP denies the role on this bucket (the evaluation cannot see one; act 4b's first real invocation
  reads it).
- Whether the exec-summary reads any key of this directory other than `<id>/summary.json`-class siblings it needs
  (`platinum/leaderboards/` is a class the registry does not place: the seam keeps it on the pipeline bucket; read from
  `served_seam.py`, which 4b's own half re-reads).
- The shared-infra root's plan state (standing drift): a root that cannot plan scoped is a BLOCKING row.

## Provenance

`ROUND_ANALYSIS.round3.md` ADDENDA 10 and 11; `r4_exec.py` (the check for `FB-g-27`); `r4_act3b.py` for the live read. Push
state: LOCAL.
