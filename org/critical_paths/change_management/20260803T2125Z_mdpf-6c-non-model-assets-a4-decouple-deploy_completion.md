# Deploy completion — mdpf 6c dim_mdpf_non_model_assets.py (A4 DECOUPLE fix, deploy-of-landed-commit)

**Deployer:** 0.2.0_DS_PortfolioAnalytics (Rule-13 DS gold lane) · **Opened/closed:** 2026-08-03 21:23–21:25Z (single-leg, completed in-session)
**What:** `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_non_model_assets.py` synced to repo HEAD @6a9fe4f771 content (md5 local `f1a861f24212d16877722239723c956a`; was STALE at `716bc7c7749b854b69fd31916d4e7917`).
**Zero new code** — the A4 DECOUPLE commit (2026-07-21, CVO EXT#1 / CTO 203846Z) was landed-but-never-deployed.

## Why (mechanism, source-confirmed)

Deployed copy still carried `load_legacy_precutover` reading retired `opal-data-portal-v2/json/portfolios/non_model_assets.json` → NoSuchKey EVERY chain cycle since the 07-29 json retire → STAGE6-REVAMP rc=1 (non-fatal, chain reports complete) → **6d (all cottonwood legs) never reached** → cottonwood revamp artifacts frozen (aggregate 07-29 partial, sidecars 07-28; last cycle-complete marker 07-29 00:33Z). Evidence: Friday chain log `mdpf_daily_20260731_145709.log` traceback (deployed `:179`); `status.json` STAGE6-REVAMP error 32s; MDPF_GLOBAL.T1C census @5b42aff274. Repo HEAD reads the revamp-native frozen snapshot instead (`load_precutover_frozen`, zero legacy dependency).

## Deploy legs (all closed)

| Leg | Check | Result |
|---|---|---|
| L1 | Frozen snapshot live precondition | `gold/mdpf_revamp/global/non_model_assets_precutover_frozen.json` 44,480B, 2026-07-21 20:51:22Z — EXISTS |
| L2 | QA exercise (NEVER#4a ad-hoc, no writes) | repo HEAD build on live 08-03 inputs: 297 frozen rows read, 441-row series, `validation PASS (identity exact)`, rc=0, 21:23:20Z |
| L3 | Upload | `aws s3 cp` 24.1KiB 21:24Z |
| L4 | Verify | `comp-pipescript deployed dim_mdpf_non_model_assets --pipeline mdpf` → **MATCH** (1 MATCH / 0 STALE) |

## Behavioral verification (pending, scheduled-run-only)

The claim "Stage 6 now passes" is EXERCISED only by the next scheduled chain cycle (INF-gated; T2.C will re-clock): expected — STAGE6-REVAMP ok, 6d cottonwood legs run, `gold/mdpf_revamp/meta/cycle-complete.json` advances past 07-29 00:33Z. Owner: 0.2.0_DS (T1.C row-12 evidence window). A green QA replay is NOT production evidence (NEVER#4a).

## Not touched (flagged, out of scope)

`LEGACY-EMIT` step errors nightly on explicit-deny writing retired `json/portfolios/aum-timeseries.json` (WO-2 fence working as built vs a not-yet-retired legacy emitter) — T5 census item, surfaced to COO 21:23Z.
