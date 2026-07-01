# Deploy-Completion Ledger — MDPF WS-E swap (CUSTODY_SOURCE basis switch) DORMANT deploy

**Status:** CLOSED (2026-07-01T22:00Z — dormant deploy VERIFIED; my WS-E pre-flip leg DONE) | **Opened:** 2026-07-01T21:52Z (deploy-START) | **Owner:** 0.4.0_DS_ClientPlatform~A | **Authorized:** CTO arch-gate PATH-A CONFIRMED (1.0.0_SA_CTO 2026-07-01) + 0.5.0 design handoff + Andrew basis-switch ruling | **Priority:** P1 (MDPF served aggregate-AUA frozen since 06-25; this is the fix at the root) | **Window:** co-activation-gated
**Class:** served-data pipeline CODE change — NO-HALF-DEPLOYS gate binds; DORMANT (CUSTODY_SOURCE=bd = zero behavior change) so the deploy itself carries zero served-value delta; the value-changing flip is a SEPARATE gated step.

## Why
WS-E `build_mdpf_wse_49f_non_model_aua.py` computed `partner_custody_total` from `bd/silver/allocations` restricted to Schwab via the `bd/silver/FEES` crosswalk; the fees crosswalk froze 06-25 → served 49F custody (and the aggregate AUA) froze 6 days. Andrew ruled a Schwab-native straight-RPS assets-only basis. This deploy lands the swap CODE dormant behind `CUSTODY_SOURCE` so the cutover is a single SSM flip co-activated with 0.5.0's trigger re-point (`mdpf-pipeline-v1.3.0`, also dormant).

## Change
- Commit `49af9819b` on origin/CLOUD (pushed). Deltas 1/2/4 + delta-3 (PATH A no-op) + fail-closed seam. Output schema `COLS_NON_MODEL_AUA` UNCHANGED.
- Deploy target: `s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` (the mdpf-daily-runner s3-syncs `code/scripts/` per CLAUDE.md Rule 12; dispatch runs it with the trigger-stamped `CUSTODY_SOURCE` env).
- Pre-deploy baseline (old v0.9): ETag `93d7873ca1f1370b51bff24de9f2be34`, LastModified 2026-05-20, 25,915B.

## Legs
| # | Leg | Status |
|---|---|---|
| 1 | Code: deltas 1/2/4 + delta-3 PATH-A seam + fail-closed | **DONE** (commit 49af9819b) |
| 2 | Gate: py_compile + ruff 0.15.11 py39 + ds-commit-gate | **DONE** (all clean) |
| 3 | Test schwab branch (dry-run 06-24): custody $1,591,210,618.75, non_model $180,524,950.02, coherence gate PASS, rc=0 | **DONE** |
| 4 | Test bd branch to completion (dry-run) unchanged — the DORMANT live path | **DONE** (cert cross-check PASS to the cent; custody $1,658,320,156.02; non_model $247,634,487.29; rc=0 — unchanged) |
| 5 | Deploy: `aws s3 cp` local → mdpf code prefix (AES256) | **DONE** (22:00Z) |
| 6 | Verify deployed: new ETag != old + re-pull md5 == local | **DONE** (ETag `0e30e4b422fb5e2ab61facbb8e6f00e4` == local md5, 41,774B; old was `93d7873…`) |

## Close (2026-07-01T22:00Z)
All 6 legs DONE. Code `49af9819b` deployed to `s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wse_49f_non_model_aua.py`, artifact byte-verified == local (ETag==md5). DORMANT: `/mdpf/custody_source`=bd → bd branch runs on tonight's nightly = zero behavior change (bd branch regression confirmed unchanged). My WS-E leg of the 3 pre-flip legs (WS-E swap dormant + 0.5.0 leg-2 sanity gate + 0.5.0 RPS backfill) is DONE. RAVC 0.5.0 + COO at close. The FLIP (SSM bd→schwab) + CVO post-flip parity are the SEPARATE co-activation flow (COO never-widen sign-off), NOT this ledger. No half-state.

## Rollback
Dormant = no served change to undo. If leg 4 (bd regression) fails → abort the cp, no deploy. If a post-deploy issue → re-cp the old v0.9 (ETag `93d7873…`) OR the flip stays at bd (both bases available behind the flag).
