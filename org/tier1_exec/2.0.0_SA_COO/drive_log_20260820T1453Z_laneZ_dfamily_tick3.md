# /drive tick 3 — site-Z D-family scope — 2.0.0_SA_COO~Z — 2026-08-20 14:53Z (cron ebf739a0, the 14:46 fire)

**Authority/carrier:** Andrew-direct @2b3b2eaeaa; XXX.md COO row @e2c8e55dab. Scope: D6/D7/D8/D9 (= the SITEZ rows of DIRECTIVES.yaml:20; LD-0428 @bb5b6bc7e2 read — a ~Z seat works only these).

## Measurements (denominators printed)
- `get_live_agents` 14:53Z: MSTR~Z, DE~Z (pid 31384), OpalETL~Z, CTO~Z, COO~Z LIVE; BG STALE-by-broker (218s) but watcher live = by process; CVO~Z gone (reaped). **6/6; six stream watchers; zero ghosts.**
- Telemetry 19,330 rows; since the tick-2 marker (14:42:36Z): DE~Z 24, OpalETL~Z 24, COO~Z 17, MSTR~Z 15, CTO~Z 13, BG 2, CVO~Z 0 (reaped). Commits since tick: COO~Z 3 (TO-F pending flip @562a74f4f7; v0.3 V03-4 fold @43a17864a8; tick-2 log), OpalETL~Z 3 (@8efa0cd890 half-b log; @b52d015d58 leg-3 Rule-24 fold; +1), base-MSTR import 2, Andrew 1, 0.8.0_AE 1 (laptop imports). Portal DEV: no new commit (DE~Z's act 1 is an exercise + proof flip, not a build).
- `deploy_ledger check --red`: only the out-of-scope HELD-STALE freshguard gate; 3/3 sentinels.
- D8 proof instance: D8-5/D8-6 still UNCOMPUTABLE-BY-CONSTRUCTION at this read (DE~Z act 1 in flight, 11 min).
- Broker summaries: OpalETL~Z + CTO~Z refreshed to WORKING (the tick-2 `[SYNC]` landed); DE~Z still "startup" (24 work-calls say otherwise — the board reads telemetry, not the line).

## Classification + action
| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| D7 TO-F | ADVANCING (both halves) | OpalETL~Z (b) committed @4bede18189, apply REQUESTED via MSTR~Z ferry ~14:47Z; DE~Z (a) behind D8 act 1 | 14:53Z / 14:53Z | **verification ask to MSTR~Z**: is the 5-item apply request on the bus + how did the laptop sequence it (the D7 critical path now) — not `[STUCK]` (6 min) |
| D8 | ADVANCING → one act from CLOSE | DE~Z act 1 (live halves) | 14:53Z | none; CTO~Z declares CLOSED on the flipped rows; I validate |
| D6/W6/v0.3 | ADVANCING (external, verified 14:36Z; land 1700–1830Z) | laptop W6-PORT | — | none; v0.3 GO + W6 flip at the landing |
| D9 | OFF-DEVICE-DRIVEN | laptop (c1) | — | none |
| BG | out of scope | holding for Andrew's word on the dead-seat spawn drill (MSTR~Z's thread) | — | noted only |

**Dispatches:** 1 (the MSTR~Z verification ask + board). **Hard gate:** every D-family item is attested MOVING with real timestamps; the one external leg (laptop apply) is verified-moving by the ask, not assumed; "nothing blocked" is the valid outcome. **/allocation:** supply 6/6, every completing worker alive and producing; no supply act.
**Compiler tools:** get_live_agents; the telemetry read (python); git log since-tick (workspace + portal submodule); deploy_ledger.py check --red; ps stream watchers; python read of the D8 proof instance.
