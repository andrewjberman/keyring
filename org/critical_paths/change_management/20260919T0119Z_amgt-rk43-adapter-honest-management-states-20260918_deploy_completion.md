# Deploy Completion Record
**Date opened:** 2026-09-19T01:19:53.361680+00:00
**Status:** OPEN
**Deploy:** AMGT-rk-43 adapter: honest management states (ceo_profile_reading fields, zero-officer ABSENT arm)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~45
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served over 13 GET routes LOST=[] GAINED=[] |  | OPEN |

## Log

- 20260919T011953Z OPENED by 0.9.0_WK_AMGT_RESAPP~45 with 1 leg(s)
- PRE-ACT MEASUREMENTS (fresh, this worker, immediately before build):
  - Never-widen pair on file for AMGT-rk-43: COO half
    `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_COO_HALVES.md`
    sha256 `a41ead71ea87a409b19cbacbd0567eff47e68a93a5ecb4ec7327c11786e8d923`; CTO half
    `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_CTO_HALVES.md`
    sha256 `0e702e1f923fea87306693770cff2caf7434e717be30b419d301e6bcb2902f7d`. Both carry an
    `AMGT-rk-43` section (COO half signs SIGNED; CTO half signs SIGNED per its own `AMGT-rk-43`
    section text "SIGNED").
  - Adapter single-writer queue check (issuer rule): `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ
    -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api
    infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` printed NOTHING (worktree not behind
    the shared branch on adapter-touching paths) -- checked twice, once at spawn and once immediately
    before this build, both empty.
  - Pre-act live Lambda `opal-amgt-scoped-api` (`get-function-configuration`): `CodeSha256`
    `0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo=`, `LastModified` 2026-09-18T00:59:50.000+0000,
    `CodeSize` 786895.
  - Pre-act artifact `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
    `VersionId` (head-object, fresh): `sGCyeje9jhn9jzu86QcORUXKQnVfFNpu`.
  - Bucket versioning on `opal-313476888478-lambda-artifacts` (get-bucket-versioning, fresh):
    `Enabled` -- matches the issuer's ~22:4xZ measurement; proceeding.
  - ROLLBACK MECHANISM (recorded before acting, per the issuer rule and CTO msg 23830): restore the
    pre-act bytes as the current artifact version via `aws s3api copy-object --bucket
    opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --copy-source
    "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=sGCyeje9jhn9jzu86QcORUXKQnVfFNpu"`,
    then the same targeted `safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this` (the
    module resolves the CURRENT version and is never edited), then `get-function-configuration` must
    print `CodeSha256` `0l7f4YGikexrP7INF7q8r5k11+0J0BBxpJ6sYqP8Uyo=` again. Not exercised unless
    rolling back.
