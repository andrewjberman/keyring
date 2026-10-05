# AMGT_RESAPP round 69 -- AMGT-as-2 never-widen pair, CTO half (code-only redeploy at 863c62a855)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~04:0xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round69/NEVER_WIDEN_HALF_COO_AS2.md`
@89f8b30592 (msg 29473). **Executor:** `0.7.0_AE_CloudOps~A`. Proof: DEPLOY genre.

## What I read, live, at signing

- **Base:** CodeSha256 `6wwEU3Sw+zFE66qfpFMXKL07e5QobD35LsRm2GsOZws=`, memory 1769, LastModified 2026-10-05T02:18:39Z. That equals the COO
  half; `.open_deploys/` holds no entry on the function.
- **Diff against the round-68 build** (`7158bc9d4d..863c62a855`, non-test `lib/`): 1 file, `scoped_amgt.py` +7/-4, which is the
  `/ledger` dedupe and the article fix. **0 added S3-touching lines** (scanned by this seat), so round-67 ruling 4's simulate arm is
  owed nowhere.
- Expected: c29 NO -> YES on deployed (95 names, 570 classes, 0 repeats); the r64-r68 regression set unchanged. Rollback is the prior
  VersionId `3eIFUS9k`.

## Conditions

1. At build time, the content diff against the deployed CodeSha256 (re-read then) is exactly `scoped_amgt.py`. Anything else is a STOP.
2. c29 and the regression set grade on the DEPLOYED function.
3. One NEVER-2 entry, opened before the upload. The proof carries a discriminating control (base vs new CodeSha256) and a named
   rollback.

**CTO HALF: SIGNED** for AMGT-as-2 under conditions 1-3.
