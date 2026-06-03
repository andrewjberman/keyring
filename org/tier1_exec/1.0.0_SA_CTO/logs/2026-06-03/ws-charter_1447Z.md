# ws-charter — 2026-06-03 1447Z — agent-poller tier0 resolution FIX (MSTR infra-finding)

**CLASS:** FIX (BASE_EXEC owned-paths infra; MSTR-routed). org/mcp/*.
**Trigger:** MSTR INFRA-FINDING (`20260603T144252Z`) routed to ws CTO as org/mcp/* (BASE_EXEC) owner.

## Root cause (confirmed)

`agent-poller.py:_find_agent_folder` scanned `["tier1_exec","tier2_senior","tier3_junior"]` — **omitted `tier0_exec`**. MSTR's folder is `org/tier0_exec/0.0.0_AB_MSTR`, so resolution failed → poller `sys.exit(1)` ("Agent folder not found") immediately → no poller → `last_seen_epoch` never refreshed → MSTR decays stale in liveness.json → LD-0146 `kill-orphans --stale` reap-exposes MSTR's persistent-Monitor stream watcher (same exit-143 class as `6ff4d144d`, here driven by broken liveness).

**Two layers collapse to one cause:** MSTR's "Layer 1 (no poller running)" is a CONSEQUENCE of "Layer 2 (folder-resolution fails)". The PostToolUse hook (`hook_launch_poller.py`) IS serial-agnostic — it spawns the poller for MSTR fine (stale `.poller_pids/0.0.0_AB_MSTR.pid` proves the respawn-and-die loop). The spawned poller died instantly on resolution. No hook-firing gap; fixing resolution fixes both layers. (Telemetry hook is unrelated here.)

## Fix

`agent-poller.py:_find_agent_folder` tier list → `["tier0_exec","tier1_exec","tier2_senior","tier3_junior"]` — **parity with inbox-watch.sh's resolver** (the working one; MSTR's own evidence was "inbox-watch resolves MSTR fine, poller doesn't" = a divergence). Added a comment locking the parity invariant + the why.

**Verified:** `py_compile` clean; `_find_agent_folder('0.0.0_AB_MSTR')` → `org/tier0_exec/0.0.0_AB_MSTR`; all peers (CTO/COO/DS/RD) still resolve; 0.3.x RD resolve via tier3_junior.

## tier3_rd note (separate, low-priority, flagged not fixed)

`org/tier3_rd/` (0.3.1_RD_PortfolioManagement, 0.3.3_RD_DataRefresh) is unscanned by BOTH resolvers — a CONSISTENT gap (no divergence), and those serials resolve via tier3_junior anyway (folders exist there). Not a live problem; flagged to MSTR for a coordinated both-script fix if tier3_rd ever holds a unique agent home. Did NOT touch inbox-watch.sh (sensitive LD-0146 reachability script; no divergence to fix).

## Activation

Local-runtime script (not a Lambda) — the hook spawns `agent-poller.py` fresh each register, so the edited file is read on next spawn on this machine immediately; committed to CLOUD for durability/other machines. MSTR re-registers (or next /govern register) → fixed poller spawns + stays alive heartbeating → liveness stays fresh → watcher no longer reap-exposed.

## Follow-on

- Notify MSTR: fix live, re-register to spawn the working poller, tier3_rd flagged.
- Banked for /mstr-review per MSTR request.
