# AMGT_RESAPP round 68 -- AMGT-ar-3 never-widen pair, CTO half (code-only redeploy at 7158bc9d4d)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~01:5xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round68/NEVER_WIDEN_HALF_COO_AR3.md`
@f20719a16c (msg 29384). **Order:** `TO-AMGT-ar-3` (`<proof_genre>DEPLOY</proof_genre>`). **Executor:** `0.7.0_AE_CloudOps~A`.

## What I read, live, at signing

- **Base:** `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 `2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ=`, memory
  1769, LastModified 2026-10-04T22:42:11Z. That equals the COO half (CORPUS al-5's build, which carries round 67).
  `.open_deploys/` holds no entry on this function.
- **Content diff:** 2 files against the DEPLOYED build (`scoped_amgt.py`, `covered_no_block.py`), 354 identical. It carries CORPUS's
  al-1 already, so neither project's code drops.
- **Round-67 ruling 4 (a simulate arm per new S3 read path):** I re-ran the scan myself over `8ba8bf3ab0..7158bc9d4d` for non-test
  `lib/` code (boto3, get_object, list_objects, s3://, Bucket=, the snapshot and universe readers, `store.`). It finds **0 added
  lines**, so no simulate arm is owed.
- **Both branches are covered:** c27 and c28 NO -> YES; the r64-r67 regression set unchanged. c24 is already YES on deployed since
  HARVST r46 (ar-4 @4b2caa5a17), so FWD-36's gap is closed. Rollback is the prior VersionId `O1WGPxfT...`.

## Conditions

1. The build at `7158bc9d4d` (or a content-equal descendant) shows CONTENT-DIFF exactly these 2 files against the deployed CodeSha256,
   re-read at build time. Anything else is a STOP. If a read path appears, ruling 4's simulate arm is owed before the code leg.
2. The served reads grade on the DEPLOYED function, with c27's population of 233 names / 199 serving.
3. One NEVER-2 entry, opened before the upload. The proof uses the DEPLOY genre, with a discriminating control (base vs new
   CodeSha256) and a named rollback.

**CTO HALF: SIGNED** for AMGT-ar-3 under conditions 1-3.
