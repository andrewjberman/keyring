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
1. [ ] Code committed (CLOUD) + source-map committed
2. [ ] Artifacts built+uploaded (build-and-upload, content-sha256 read-back verified) x3
3. [ ] safe-apply portfolio-management -> 0-diff; live CodeSha256 == artifact sha
4. [ ] safe-apply trade-pipeline (workflow-handler + dashboard-api) -> 0-diff; live CodeSha256 == artifact sha
5. [ ] record-terraform-deploy + tags (portfolio-management, trade-pipeline) + push --follow-tags
6. [ ] Portal /prod-deploy -> tag + CI SUCCESS + workspace submodule pointer updated
7. [ ] Behavioral verification (served: export produces 4dp, column sums to 1) + notify Yang/Andrew/DS

## Status: OPEN
