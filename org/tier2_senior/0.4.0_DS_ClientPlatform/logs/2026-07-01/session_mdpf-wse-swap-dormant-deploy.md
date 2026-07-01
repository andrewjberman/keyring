# MDPF WS-E swap (CUSTODY_SOURCE basis switch) — DS~A impl + dormant deploy

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DEPLOY, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~A | **Date:** 2026-07-01 | **Window:** ~21:10Z–22:05Z
**Project:** MDPF_ASSETS (WS-E) / MDPF basis-switch (P1 pace-setter) | **RAVC:** 2.0.0_SA_COO

## Summary
Implemented Andrew's Schwab-native straight-RPS assets-only custody basis switch in the WS-E
feeder `build_mdpf_wse_49f_non_model_aua.py` (I am its author), gated behind a `CUSTODY_SOURCE`
flag, and dormant-deployed it (bd default = zero change). Forced a grounding that CORRECTED the
arch-gated design: delta-3 (custodian-scope) was falsified against live data and ruled a no-op.

## What I did (deltas)
- **D1 schwab branch:** `partner_custody_total = sum(market_value)` over `schwab/silver/rps/
  date=YYYYMMDD` (assets-only), Schwab-scoped by construction — dropped the `bd/silver/fees`
  crosswalk + `bd/silver/allocations` read + `gold/aua_certification` cross-check (the frozen-
  fees dependency that caused the 6-day served freeze). `bd` branch unchanged (default).
- **D2 CUSTODY_SOURCE:** `os.environ.get("CUSTODY_SOURCE","bd")` on the dispatch path (the
  trigger stamps it); SSM `/mdpf/custody_source` direct-read only on ad-hoc/off-dispatch runs.
- **D4 assets-only:** exclude `ticker=='CASH'` (1 row, ~$17K); bank-sweep already excluded
  upstream (silver drops zero-qty sweep); MM fund positions (SNVXX/SWVXX) kept.
- **D3 DROPPED (PATH A no-op):** see Findings.
- **Fail-closed seam (kept):** custodian-scope AUTO-ENGAGES if the WS-B custodian col ever
  populates; hard residual fail-close (rc=1, no write) on `non_model<0`, `non_model>custody`,
  or schwab `non_model` outside the sane band [$50M,$500M].

## Findings (grounded, drove the design correction)
1. **Delta-3 mechanism FALSIFIED (source+live confirmed).** The WS-B `model_aua_positions`
   custodian column EXISTS in schema (feeder L74) but is HARDCODED `None` (`wsb_49f_smartx_
   model_aua.py` L169, "not exposed on the SmartX allocation row") — 100% None across all 6
   live partitions 06-24..06-29. Plus the WS-B account_id keyspace (SmartX allocationId UUIDs)
   does NOT overlap RPS (10-digit Schwab numerics) → no DS-side scope path. So `filter
   custodian=='Schwab'` would zero both legs → non_model ≈ whole custody. Raised to 0.5.0+CTO
   (Rule 22: schema-has-column != column-populated; ground the VALUE not the shape).
2. **Magnitude disambiguator → PATH A.** `non_model = RPS(Schwab) − model(all) − sma(all)` =
   +$180.5M/+$186.5M/+$203.3M (06-24/06-25/06-30), positive/stable. Structural clincher: the
   accepted v0.9 basis ALREADY subtracts model(all)/sma(all) from a Schwab-restricted custody
   base → model/sma already the Schwab universe → delta-3 is a no-op. CTO ruled PATH A
   OPERATIVE; 0.5.0 retracted the "$156M held-away in model/sma" premise (unsourceable).
3. **Cash rule LOCKED (consistency is load-bearing):** exclude `ticker=='CASH'` → 06-24 custody
   = $1,591,210,618.75 (== 0.5.0 design $1.591B to the cent). Identical across WS-E + 0.5.0
   leg-2 gate + CVO parity (CVO verifies served==RPS-sum to the cent, so a $17K divergence
   between call-sites would false-fail parity).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-which` | RPS silver schema/partitions; cash-convention search | ROUTED | pointed to comp-pipescript io / pipescript --resource; used converter source + live parquet for the authoritative schema |
| `comp-pipescript io` | build_mdpf_wse_49f_non_model_aua.py | PARTIAL | dynamic f-string keys → no auto I/O map (expected); confirmed consumer = WS-A aggregator; schema unchanged |
| `comp-pipescript deployed` | build_mdpf_wse_49f_non_model_aua.py | N/A-for-mdpf | checks opal-data-bd/code only; mdpf deploy-verify has no comp-tool → rail-checked raw head-object |
| `pipescript --resource` | schwab/silver/rps | NO-THREAD | not a named thread; grounded via the RPS silver converter source + live parquet instead |

**What worked:** comp-which routed correctly; the RPS silver converter (`convert_schwab_rps_to_
parquet.py`) gave the authoritative output schema/path; live-parquet probes grounded every
number to the cent. **What failed:** nothing blocking. **Gap found:** no comp-tool verifies
`opal-data-mdpf/code/` deploy state (comp-pipescript deployed is hardcoded to opal-data-bd/code)
— used a rail-checked `aws s3api head-object` (ETag==local-md5). Candidate comp-freshness/
comp-pipescript extension to cover the mdpf code prefix.

## Verification (3 paths, all green)
- schwab explicit-flag (rps=wsb=06-24): custody $1,591,210,618.75, non_model $180,524,950.02,
  coherence gate PASS, rc=0.
- bd branch regression (to completion): cert cross-check PASS to the cent, custody
  $1,658,320,156.02, non_model $247,634,487.29, rc=0 — UNCHANGED.
- schwab env-path (dispatch-faithful: `CUSTODY_SOURCE=schwab` env, only `--date`, default
  dates): custody $1,608,080,123.25 (rps 06-30 default), roll-forward offset handled,
  non_model $197,394,454.52, gate PASS, rc=0.
- Gates: `py_compile` OK; `ruff 0.15.11 --target-version py39` clean; `ds-commit-gate.sh` clean.

## Deployment Sequence
1. Commit `49af9819b` (safe-commit, author 0.4.0_DS_ClientPlatform~A) → push origin/CLOUD.
2. Deploy-completion ledger OPENED: `org/critical_paths/change_management/20260701T2152Z_mdpf-
   wse-swap-dormant-deploy_deploy_completion.md`.
3. `aws s3 cp` → `s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wse_49f_non_model_aua.py`
   (--sse AES256). Rule 13 (DS owns gold-script commit→QA-deploy incl aws s3 cp).
4. Verify: deployed ETag `0e30e4b422fb5e2ab61facbb8e6f00e4` == local md5, 41,774B, 21:59:53Z
   (old v0.9 was `93d7873…`, 25,915B). Byte-identical.
5. Ledger CLOSED (commit `bf1a9fcca`) → push. RAVC 0.5.0 + COO.

## Blockers
NONE. My WS-E leg is DONE (dormant-deployed + verified). The FLIP is gated on 0.5.0's leg-2
Schwab-native sanity gate + RPS-source backfill + COO's never-widen window — genuine external
gates in other lanes, not a stall.

## Current State
- Code: `data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py` @ `49af9819b` on
  origin/CLOUD. New functions: `resolve_custody_source`, `_latest_rps_partition`,
  `compute_partner_custody_total_schwab`; `load_wsb_model_aua(custody_source=)` +
  `build_non_model_aua(custody_source=)` gated; main() branches on CUSTODY_SOURCE. Output schema
  `COLS_NON_MODEL_AUA` UNCHANGED. Constants: `RPS_SILVER_PREFIX`, `RPS_CASH_TICKERS={"CASH"}`,
  `SSM_CUSTODY_PARAM`, `SCHWAB_NON_MODEL_SANE=(50M,500M)`.
- Deployed: `s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wse_49f_non_model_aua.py`
  (ETag `0e30e4b4…`). DORMANT: `/mdpf/custody_source`=bd → bd branch → zero behavior change.
- Ledger CLOSED (bf1a9fcca). 0.5.0 trigger (`mdpf-pipeline-v1.3.0`) already dormant.

## Next Steps
- [0.5.0_AE_OpalETL] Land leg-2 Schwab-native sanity gate (custody band set on the CASH-excluded
  rule = $1,591,210,618.75 for 06-24) + the RPS-source backfill → then 2 of 3 pre-flip legs done.
- [2.0.0_SA_COO] Convene the never-widen sign-off (CTO + CVO co-sign) once all 3 pre-flip legs
  land → single SSM flip `/mdpf/custody_source` bd→schwab co-activates WS-E + trigger atomically.
- [3.0.0_SA_CVO] Post-flip parity on the FIRST nightly: served == straight-RPS-sum (CASH-excluded,
  to the cent), coherent residual (non_model non-negative + in-band); MDPF un-freezes.
- [0.4.0_DS_ClientPlatform~A] Hold for the co-activation window; the deployed schwab branch
  serves correctly the moment the flag flips. Re-baseline of the ~422-pt history (design §4) is
  Andrew-pending (accept-the-step vs recompute) — NOT authorized; do not run backfill ad-hoc.
