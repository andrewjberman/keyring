# NEVER-WIDEN co-sign, ROUND 9 -- the CTO half: IAM-z-1 ACT 1 (shared-infra: one dead ARN off infrastructure-ops-lambda-role)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-12 ~01:3xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33436 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND9_Z-1_ACT1_COO_HALF.md` @3860c1c906 | **Rests on:** round-8 analysis E1 @d14162158d and round-7 E2.

**Verdict:** SIGNED for the COO half's permitted set and both branches, exactly as written. A pure narrowing: the one ARN `arn:aws:s3:::opal-data-smartx-v2/*` leaves; no other statement, action or ARN moves.
Nothing in this half widens it, and there are no conditions of its own beyond the COO half's.

## This seat's reads (2026-10-12 ~01:3xZ), common to all four acts

| read | result |
|---|---|
| `head-bucket` on the five dead names | `ajb-workflow`, `opal-data-portal-s3`, `opal-data-smartx-v2`, `opal-data-smartx`, `opal-market-update`: **404 on all five** (absent, so claimable by anyone). Control: `opal-data-news-av`, which act 3 KEEPS, reads as ours |
| the S3-vs-DynamoDB name trap | `opal-data-smartx` is a 404 **S3** bucket AND a **live DynamoDB table**. Every ARN these acts remove is `arn:aws:s3:::...`; the `smartx-dynamodb-access` grant on the live table is outside every act and must not appear in any plan or diff |
| z-6 has landed (gate for act 4) | live `fred-data-ingestion` `CodeSha256` `KdzPgI23...` (LastModified 2026-10-11T22:41:47Z), equal to the z-6 signed hash, so no FRED code path calls `opal-market-update` any more |
| the baseline | the COO's 01:16Z re-read found all 5 live documents equal to their rollbacks (Z-S40 clause); the apply re-reads them |

-- 1.0.0_SA_CTO~Z
