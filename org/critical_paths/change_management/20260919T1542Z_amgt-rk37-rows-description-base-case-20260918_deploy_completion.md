# Deploy Completion Record
**Date opened:** 2026-09-19T15:42:33.451586+00:00
**Status:** OPEN
**Deploy:** AMGT-rk-37: five sheet-row fields + CIE_DES/CIE_DES_BULK pulled; description order and describes-the-business test; Base case served, Upside/Downside ABSENT by ruling; co-signed rk-37 pair
**Authored by:** 0.9.0_WK_AMGT_RESAPP~39
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer fields + reader + cases + tests committed | commit hash |  | OPEN |
| L2 | activation | module.scoped_amgt_api.aws_lambda_function.this redeployed | TF apply 0 destroy + 0-diff replan + deployed CodeSha256 == uploaded sha |  | OPEN |
| L3 | verify | 13 of 13 GET routes 200 pre/post, LOST=[] GAINED=[]; AC4; the 12 drafted names' description status listed pre/post | census + AC4 output |  | OPEN |

## Pre-act record (measured fresh by this worker before any live act; never inherited from rk-36)

- Never-widen pair, `AMGT-rk-37` sections read at this worktree's HEAD: COO half sha256
  `594ba746e3ad48dad4252b45864ddc21596c4deb80fa031c078e8dbd3fc715c5`, CTO half sha256
  `db0e1bbaffeef4414c215d0a5ea3ed1ba6b16b12b2564007346d90ba68994757`. Both carry a signed
  `AMGT-rk-37` section (COO half :104-124; CTO half signature block, "WITHHOLDING LIFTED --
  SIGNED" against the `541d395e0d` re-cut).
- `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
  -> EMPTY (this worktree is not behind SITEZ on the adapter/deploy surfaces).
- Bucket versioning on `opal-313476888478-lambda-artifacts` re-measured: `{"Status": "Enabled"}`.
- Pre-act `CodeSha256` (opal-amgt-scoped-api): `7lAqBNEGJWmYGt87UpxFYobyA6jevkFxM5yoIIjB+WY=`
  (`LastModified` 2026-09-19T13:46:07Z -- rk-36's post-deploy value, MEASURED FRESH by this
  worker, not copied from rk-36's record).
- Pre-act artifact `VersionId` (research/opal-amgt-scoped-api.zip):
  `6Kr.kKS6nCiPwLaCJkz1vMLnexahBGcg` -- the rollback target if this act needs reverting.
- Pre-deploy 13-route census: 13 of 13 200 (see L3 leg for the full table).
- Pre-deploy check_face_len: BA_US_Equity 179, HD_US_Equity 199 (thesis route, independent read).
- Pre-deploy description status on the 12 drafted names (overlay route, live Lambda): all 12
  SERVED via `D-1 drafting/v1 company_description sentence 1` (the unconditional pass-through
  this cell replaces) -- ASML_NA_Equity, BABA_US_Equity, BA_US_Equity, COST_US_Equity,
  HAL_US_Equity, HD_US_Equity, INTU_US_Equity, KMB_US_Equity, NU_US_Equity, PBR_US_Equity,
  SAP_GY_Equity, VLO_US_Equity.

## Log

- 20260919T154233Z OPENED by 0.9.0_WK_AMGT_RESAPP~39 with 3 leg(s)
