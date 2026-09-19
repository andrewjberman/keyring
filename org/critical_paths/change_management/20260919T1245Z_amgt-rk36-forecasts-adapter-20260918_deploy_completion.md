# Deploy Completion Record
**Date opened:** 2026-09-19T12:45:14.563041+00:00
**Status:** OPEN
**Deploy:** AMGT-rk-36: forecasts FY1-FY3 (BEST_ + SA fallback) on the model block; read_model serves forecast_*; co-signed rk-36 pair
**Authored by:** 0.9.0_WK_AMGT_RESAPP~39
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer + fallback module + scopes + adapter committed | commit hash |  | OPEN |
| L2 | activation | module.scoped_amgt_api.aws_lambda_function.this redeployed | TF apply 0 destroy + 0-diff replan + deployed CodeSha256 == uploaded sha |  | OPEN |
| L3 | verify | 13 of 13 GET routes 200 pre/post, LOST=[] GAINED=[]; AC5 | census + AC5 output |  | OPEN |

## Log

- 20260919T124514Z OPENED by 0.9.0_WK_AMGT_RESAPP~39 with 3 leg(s)
- 20260919T1246Z PRE-ACT READS (fresh, this worker, before any live act): never-widen pair sha256 --
  COO half `594ba746e3ad48dad4252b45864ddc21596c4deb80fa031c078e8dbd3fc715c5` (NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md),
  CTO half `db0e1bbaffeef4414c215d0a5ea3ed1ba6b16b12b2564007346d90ba68994757` (NEVER_WIDEN_ROUND14_CHAIN_M_CTO_HALVES.md);
  both files carry an `AMGT-rk-36` section, CTO half re-signed (WITHHOLDING LIFTED -- SIGNED) at `541d395e0d`. Lambda
  `opal-amgt-scoped-api` PRE-ACT `get-function-configuration` CodeSha256 = `3TXiCLy8w3Le2z9hiKzW3eqqhKQT4ALaKGCeCECv3rM=`
  (LastModified 2026-09-19T09:12:44Z), matching the issuer's own 09:12Z measurement. Artifact
  `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` CURRENT VersionId (pre-act) =
  `gg65p2Qo.KibhsWzkZmsvaSdavPreFoF` (LastModified 2026-09-19T08:53:44Z) -- THE ROLLBACK TARGET if this act must be
  undone. Bucket versioning RE-MEASURED `get-bucket-versioning` -> `Enabled` (matches both signed halves' 2026-09-18
  ~22:4xZ/~23:2xZ reads). Bloomberg `bloomberg_health` -> `ok: True` before the pull. Adapter single-writer queue:
  no other round-14 adapter cell holds this worktree; the pre-build stale-bytes check (`git log
  $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api
  infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`) will be re-run and pasted here immediately before the
  build, per the order.
