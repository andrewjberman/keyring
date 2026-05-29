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

### UPDATE (same tick) — DS~B slice landed within minutes; query WIRED + VERIFIED

DS~B published both per-firm distribution artifacts to my exact key (json/mdpf/{firmId}/account-distribution.json) minutes after coordination. Verified from S3 (D1 method):
- EXISTS ✓ both; FRESH ✓ (generated 21:08Z); SCALED ✓ (49F 6,838 accts/$1.38B; Inflection 400 accts/$96.6M); shape field-match ✓ (full AccountDistribution: total + by_model{canonical: DistributionStats incl histogram{21 bins/20 counts}+percentiles}).
- by_model CANONICAL display names: 49F 5 (no SMA — distribution source = model_portfolio_accounts/SmartX, no 49F SMA accounts), Inflection 7 (incl 2 blends).
- Extra top-level fields firm_id/firm_name/source = harmless (structural typing; no slimming).

NO code change needed — the 5e88321d scaffold was already correct. Query wired + verified SAME tick.
Handed RD~B the confirmed hook + flagged the 49F 5-vs-7 (distribution vs AUA) model-set divergence. RAVC2'd COO. ACK'd DS~B (PASS).

DE work on all 3 MDPF defects now done: D1 (pre-publish-resolved), D2 (RD~B lane), D3 (both partitions data-wired: left AUA from perFirmMdpfData, right bell-curve from getAccountDistributionByFirm). Remaining = RD~B render + /frontend-dev visual smoke.

Commits this tick: portal/DEV 5e88321d.
