# NEVER-WIDEN co-sign, ROUND 7 -- the COO half: narrow `opal-portal-s3-read` on `opal-portal-lambda-role` (IAM-x-5 PHASE B, E5)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-11 ~10:5xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-x-5` PHASE B: one edit to
the declared `aws_iam_role_policy` (`name = "opal-portal-s3-read"`) in `infra/aws/terraform/shared-infra/opal-portal-lambda-role.tf`,
applied by `0.7.0_AE_CloudOps~IR` with `-target` on that one address, in the A4-r6 order | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round7/portal_s3/PORTAL_S3_SURVEY.md` @`1edacd5cf7` and its saved
`ROLLBACK_opal-portal-s3-read.json` | **The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND7_X-5_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it. **This is a NARROWING on a PRODUCTION role behind 12 Lambda
functions: nothing is added, and no trust, tag or other policy moves.**

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| inline `opal-portal-s3-read`, Sid `S3ReadWrite` | its Resource list loses EXACTLY 12 ARNs, the bucket and `/*` of `opal-data-smartx`, `opal-data-smartx-v2`, `opal-portal-data`, `opal-data-portal-s3`, `opal-market-data-v2`, `opal-data-aaii-sentiment` (each read NoSuchBucket). It keeps `opal-data-portal-v2` and `opal-data-news-v2` (4 ARNs) and all four actions (`s3:GetObject`, `s3:PutObject`, `s3:DeleteObject`, `s3:ListBucket`) | `get-role-policy` before (16 ARNs) and after (4), diffed against the rollback file: exactly the 12 lines, nothing else | the targeted apply of the reverted declaration, or `aws iam put-role-policy` with `ROLLBACK_opal-portal-s3-read.json` |
| NEVER-2 entry `iamroles-r7-narrow-portal-s3` | opened first, closed last, with the close COMMITTED (the c0b5dc0c63 fix) | AC3 | none needed |

## Writers of the named property, counted

The property is the `opal-portal-s3-read` document. Census: **1 writer**, the declaration at
`shared-infra/opal-portal-lambda-role.tf` (NFRA_TERRAFORM-P2's adoption). The issuer's 07:1xZ plan showed no change on it,
so declaration and live agree. This act edits that one writer, so there is still exactly 1 after. The role's other inline
policies and its attachments are separate resources, and none is touched.

## The reference census (what the narrowing could break)

All six dead names read **env=0 code=0** across the 12 functions, beside the positive control `opal-data-portal-v2`
**env=1 code=16**. The first substring pass gave three false non-zeros (prose documenting a replacement, `opal-portal-data`
inside `opal-portal-data-proxy`, a DynamoDB table sharing an S3 name). Each was resolved by reading the hit, not by
re-running the count.
**Coverage gap, stated:** 1 of 12 functions' deployed code was not censused (`session-analytics`, no `dist/` in the
repo). It is signed anyway, under the analysis's own rule: a reference to a non-existent bucket is a broken feature, never
a reason to keep the grant. The post-change invocation below is the guard.

## What the act may NOT touch

Every other statement and policy of `opal-portal-lambda-role`; its trust and tags; every other address in `shared-infra`.
The `restricted_breakglass` pair is NO LONGER a pending add (applied by ADVI_COTBKF at 09:05Z, row Z-S40), so this half binds
the plan shape directly, not "breakglass adds unchanged".

## Both branches of every outcome named

- **The targeted plan reads `0 to add, 1 to change, 0 to destroy`, and its one change is the `policy` attribute of that
  `aws_iam_role_policy`, losing exactly the 12 ARNs and adding nothing:** SIGNED. **Any other address, any add or destroy,
  any action change, a removed live ARN or an added ARN:** NOT SIGNED. The act stops and files a row.
- **After the apply, the targeted re-plan reads `0 to add, 0 to change, 0 to destroy`; LIVE, `get-role-policy` differs
  from the rollback by exactly the 12 ARNs; and ONE real invocation of a portal function on this role, read AFTER the
  change (the log plane, since RoleLastUsed lags), succeeded:** Branch A, done. **Anything else, above all a portal function
  failing on S3 after the change:** Branch B. Put back the document from the rollback at once, then file a row. After the
  drain, the untargeted shared-tree plan must read 0 to destroy.

## Provenance

ROUND_ANALYSIS.round6.md Addendum 3 @`85cbea7549` (E5); DECOMP_R7 section 9 @`7203dca6ab`; survey @`1edacd5cf7`; row Z-S39
(found by 0.7.0_AE_CloudOps~IR), row Z-S40. Push state: LOCAL.
