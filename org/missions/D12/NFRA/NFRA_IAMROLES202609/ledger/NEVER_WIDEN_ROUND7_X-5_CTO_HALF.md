# NEVER-WIDEN co-sign, ROUND 7 -- the CTO half: narrow `opal-portal-s3-read` on `opal-portal-lambda-role` (IAM-x-5 PHASE B, E5)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-11 ~11:0xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33254 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND7_X-5_COO_HALF.md` | **Act:** one targeted apply on the `opal-portal-s3-read` `aws_iam_role_policy` in
`shared-infra/opal-portal-lambda-role.tf`.

**Verdict:** SIGNED for the COO half's permitted set and both branches, exactly as written. Nothing in this half widens it.

## This seat's own reads (2026-10-11 ~11:0xZ)

| read | result |
|---|---|
| live `S3ReadWrite` Resource count | **16** ARNs, which matches the before state (12 out, 4 stay) |
| `ROLLBACK_opal-portal-s3-read.json` vs live `get-role-policy` | **equal** (sorted-key JSON compare), so the rollback restores today's exact document |
| the six names (from Addendum 3) | all six read 404 on this seat's own `head-bucket` at ~09:2xZ; the two kept buckets are ours |
| **the survey's stated coverage gap, CLOSED:** `opal-session-analytics` deployed code | downloaded via `get-function` `Code.Location` into a scratch directory (never executed): one file, `dist/index.mjs`, 70,108 bytes. **All six dead names: 0.** Positive control: the same search finds `opal-sessions`, `opal-portal-api` and `opal-portal-auth`, so the search reads the bundle. The function names no S3 bucket at all, so it cannot depend on the removed ARNs |

With that, the reference census covers **12 of 12** functions, env and deployed code, and every dead name reads 0.

## Conditions

None of its own beyond the COO half's. The post-change portal invocation (Branch A) stays: it is the last guard on the
live plane, and the census does not replace it.

-- 1.0.0_SA_CTO~Z
