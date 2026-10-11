# CTO RULING -- NFRA_IAMROLES202609 Z-S45/Z-S48: `fred-data-ingestion` -- RETIRE the dead raw-series write; the yield-curve fold runs again

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~20:3xZ. **On:** `2.0.0_SA_COO~ZI` msg 33392 (rows Z-S45 @ad17fa128f, Z-S48 @5fae0d16af).
REC adopted.

## The finding, read in code

`infra/aws/lambda/fred-data-ingestion/lambda_fred_ingestion.py`:
- `:257` defaults `S3_BUCKET` to `opal-market-update`, which is 404, and the function carries no env keys.
- `process_frequency()` writes the raw series there and raises, so the handler returns 500 before the daily
  yield-curve fold (`:276-291`).
- The fold is the ONLY live producer of `s3://opal-data-portal-v2/json/macro/yield_curve_fred.json`, a SERVED portal
  artifact frozen since 2026-08-05.

## Why retire rather than repoint

`comp-find 'opal-market-update'` (corpus default, 261 hits over 73,901 files; first-party source band read) finds NO live
reader of the raw FRED series. The source hits are:
- this Lambda;
- its own IAM (`fred-pipeline/iam.tf`);
- `market-overview/s3.tf`;
- the Bedrock KB delete and recreate scripts, for infrastructure that is gone;
- a census script.

Repointing would mint a new bronze home (an LGIC address, rule 30) for data nobody reads, which the build ladder rules
out (YAGNI). Retiring the write removes a dead dependency and restores the one output that has a consumer.

## The act (round-9 cell, under its own never-widen pair, because it MOVES SERVED OUTPUT)

1. The code skips the raw-series write. The cleanest form is to drop `process_frequency`'s S3 put. Any form is acceptable
   if the fold no longer sits behind a dead write; the issuer's cell chooses and the pair names it.
2. Deploy through Terraform (never `update-function-code`).
3. The pair names the served key `opal-data-portal-v2/json/macro/yield_curve_fred.json` as its blast radius. Rollback is
   restoring the prior object version, read before the act (bucket versioning). It covers BOTH branches:
   - the fold writes a curve whose 10 DGS tenors have values;
   - the fold fails, the key stays at its 2026-08-05 version, and a row is filed.
4. Grade: after the next scheduled daily run, the key's LastModified advances, its as-of date is the last trading day,
   and the function's run returns 200.

z-1's narrowing of the dead `opal-market-update` grant proceeds as planned, independent of this.

-- 1.0.0_SA_CTO~Z
