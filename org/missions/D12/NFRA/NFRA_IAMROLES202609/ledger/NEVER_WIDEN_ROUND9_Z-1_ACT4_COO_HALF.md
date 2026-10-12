# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: IAM-z-1 ACT 4 (IAM-API delete-role-policy S3Access on FredIngestionLambdaRole)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-12 ~01:2xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-1` PHASE B, ACT 4,
by `0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-narrow-dead-fred-s3access` | **Read against:** `deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/NARROW_DEAD_SURVEY.md` @`aacd0c491f` (section 4) |
**The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND9_Z-1_ACT4_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## Baseline, re-read by this signer at 01:16Z (Z-S40)

The live `FredIngestionLambdaRole/S3Access` (1 statement: `opal-market-update` and `/*`, Put+Get+ListBucket) EQUALS `ROLLBACK_FredIngestionLambdaRole_S3Access.json`. The apply re-reads this baseline. If the document has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

One `aws iam delete-role-policy --role-name FredIngestionLambdaRole --policy-name S3Access`.
- Both of its ARNs are the 404 bucket, so narrowing would leave it empty: the act deletes it.
- The policy is not Terraform-declared (survey section 4).

Rollback: put-role-policy S3Access with the rollback document.

## What the act may NOT touch

`yield-curve-artifact-write` and `fred-ingestion-secrets-read` (both live, TF-declared, and used by the fold that z-6 restored); `SecretsManagerAccess` (row Z-S49, not this act); the managed `AWSLambdaBasicExecutionRole`.

## Both branches

**Sequencing, signed:** this act runs after z-6, which is COMPLETE @4729bf8ba0. The running code has put_object=0, so nothing on the role calls `opal-market-update` and the delete has no failure mode.
- **The delete lands.** Afterwards `list-role-policies` no longer lists S3Access and still lists the other three, and the next daily fire (23:00Z) still reads `FRED-RUN statusCode=200 yield_curve_success=true`. Done.
- **That fire fails after the delete:** restore S3Access from the rollback document, then file a row.

## Provenance

DECOMP_R9 @`ef498be99f`; ROUND_ANALYSIS.round8.md @`d14162158d` E1; survey @`aacd0c491f`; rows Z-S45, Z-S46, Z-S51. Push state: LOCAL.
