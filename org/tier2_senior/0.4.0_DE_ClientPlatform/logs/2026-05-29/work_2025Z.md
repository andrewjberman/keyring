# /work cycle — 0.4.0_DE_ClientPlatform — 2026-05-29 ~2025Z

Cron tick. HALT-gate clear, watcher PROCESS-OK (tracked bkfvws7bb), inbox: 1 COO message (Andrew GO'd D3 Path B).

## D3 Path B — per-firm account-distribution query scaffolded

Andrew ruled Path B: per-firm bell-curve IS wanted (derived from per-account model data, SmartX/Eclipse). Chain: DS~B per-firm distribution slice (head, building) → my per-firm query → RD~B render → /frontend-dev visual smoke.

DE work this tick:
- Added `getAccountDistributionByFirm(firmId, forceRefresh?)` in `portal/src/api/endpoints/aum.ts` → `/api/general/mdpf/{firmId}/account-distribution.json` (CF /api/general/*→/json/* rewrite; serves `json/mdpf/{firmId}/account-distribution.json`, sibling to per-firm AUA slice). Mirrors global `AccountDistribution` shape; firmId-keyed in-memory cache (`ACCOUNT_DIST_CACHE_TTL`); returns null on error (per-firm query pattern → graceful useQuery degrade).
- ADDITIVE: global `getAccountDistribution()` (no firmId) unchanged for Global view.
- tsc -b --noEmit exit 0; shipped portal/DEV **5e88321d**, pushed origin/DEV (VALGATE D-1 PASS).
- Sent DS~B (0.4.0_DS_ClientPlatform~B) exact key+shape coordination (lock query↔artifact match BEFORE the slice lands — the D1 lesson). Asked: key by_model by canonical display_name (RD~B-consistent), flag any shape divergence, mind the platinum→json publish (serving prefix is json/).

State: prep-ahead/standby. When DS~B's slice lands → verify shape from S3 (D1 EXISTS/FRESH/SCALED + field-match method) → RAVC2 the wired query to COO + hand RD~B the confirmed hook. No blocker.

Commits this tick: portal/DEV 5e88321d.
