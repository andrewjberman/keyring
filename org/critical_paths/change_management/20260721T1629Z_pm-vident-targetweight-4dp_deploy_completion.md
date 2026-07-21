# Deploy-completion ledger: pm-vident-targetweight-4dp

- **Opened:** 2026-07-21T16:29Z by 0.3.0_DT_TradingOperations (Andrew-direct "you can drive it"; Yang-directed 2026-07-21)
- **Scope:** Round Vident-model **TargetWeight to 4 decimals (1bp)** in every emitted file. Applied at EMISSION only; true (unrounded) weights still drive the oversubscribed/sum-to-1 guards and the persisted `model_securities` record. CASHTARGET residual derived from the ROUNDED weights so each emitted column still sums to exactly 1.0000 (overshoot on a near-fully-invested model shaves the largest weight; cash never negative).
- **Surfaces (5 emit points across 3 lambdas + portal):**
  1. `opal-portfolio-excel-generator` — `generate_vident_model_csv` (Submit `tradeCsvUrl` download) + `generate_vident_excel` (submit Excel). TF: portfolio-management.
  2. `trade-workflow-handler` — `_generate_model_excel` (EXECUTE-time Excel emailed to Vident). TF: trade-pipeline.
  3. `trade-dashboard-api` — `_generate_model_excel` (in-app view; byte-identical copy). TF: trade-pipeline.
  4. Portal `TradeTab.tsx` `handleExportCsv` — the Export-button CSV (client-side twin). Portal DEV->PROD.
- **NOT changed:** stored `model_securities` record stays full-precision (durable true source; execute Excel rounds at emission).

## Pre-deploy verification (proven before any apply)
- py_compile: all 3 lambdas PASS. ruff 0.15.11: PASS. Portal `tsc -b --noEmit`: 0 errors.
- Behavior test (REAL generators, `scratchpad/test_4dp_rounding.py`): CSV + Excel emit <=4dp TargetWeights AND column sums to **exactly 1.000000000000**; helper overshoot-shave keeps cash>=0; exact-1 case emits no cash row. ALL PASS.
- Frontend/backend parity (node): `handleExportCsv` core produces byte-identical output to the backend (cash 0.4186, same sample rows 0.0314/0.0272/0.0162/0.0467/0.0141). ALL PASS.

## Legs
1. [x] Code committed `c8a87691a` (CLOUD, Andrew-authorized lane override) + source-map `bb4aaf3a1`
2. [x] Artifacts built+uploaded+read-back-verified x3: opal-portfolio-excel-generator `cub1v/Dlut...`, trade-workflow-handler `QRhdxXf4...`, trade-dashboard-api `TJ/P4Nf...`
3. [x] safe-apply portfolio-management -> Apply complete 0/1/0; 0-diff; live CodeSha256==`cub1v/Dlut...` (Active/Successful)
4. [x] safe-apply trade-pipeline -> Apply complete 0/2/0; 0-diff; live CodeSha256 both match (workflow-handler `QRhdxXf4...`, dashboard-api `TJ/P4Nf...`)
5. [x] record-terraform-deploy + tags portfolio-management-v2.4.1 + trade-pipeline-v1.20.1 + push --follow-tags (`eba42d8b7`)
6. [x] Portal /prod-deploy -> PROD `99fed48f` (tag portal-v2.1.140, peel-verified) pushed; parity gate empty (only TradeTab.tsx); CI run 29850995452 **conclusion: success**; main tree back on DEV `2c802d13` (Rule 19 held); workspace submodule pointer bumped
7. [x] Behavioral verification: DEPLOYED-code == TESTED-code -- backend live CodeSha256 == artifact sha on all 3 lambdas; portal CI success + tag peels to PROD head. TESTED-code EXERCISED: behavior test (real generators) CSV+Excel emit <=4dp & column sums to exactly 1.0000; node parity byte-identical frontend<->backend. (Prod lambda NOT invoked -- has DynamoDB/autosave side effects; sha-match + local-exercise is the side-effect-free sound proof.) Notified Yang/Andrew/COO.

## Status: CLOSED 2026-07-21 (7/7 legs; backend 3 lambdas + portal all deployed+verified)
