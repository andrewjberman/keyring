# /drive tick 5 — site-Z D-family scope — 2.0.0_SA_COO~Z — 2026-08-20 15:11Z (cron ebf739a0, the 15:06 fire)

**Authority/carrier:** Andrew-direct @2b3b2eaeaa; XXX.md COO row @e2c8e55dab. Scope: D6/D7/D8/D9 (SITEZ rows; LD-0428).

## Measurements (denominators printed)
- `get_live_agents` 15:11Z: MSTR~Z, DE~Z, OpalETL~Z, CTO~Z, COO~Z LIVE; BG broker-aged (event-driven; watcher live by process) → 6 watchers; CVO~Z gone. Census 6/6 by process; inbox top-level empty.
- Telemetry 19,402 rows; since the tick-4 marker (15:04:06Z): DE~Z 9, COO~Z 2, MSTR~Z 1, OpalETL~Z 0 (last 15:02:47Z), CTO~Z 0 (last 15:02:43Z), BG 0 (last 14:49Z), CVO~Z 0 (reaped). Commits since tick: COO~Z 1 (tick-4 log). Portal DEV: none.
- `deploy_ledger check --red`: only the out-of-scope HELD-STALE freshguard gate; 3/3 sentinels.
- D8 proof rows D8-5/D8-6: UNCOMPUTABLE-BY-CONSTRUCTION still (DE~Z act 1 ~28 min in, 9 work-calls this tick — MOVING).

## Classification + action
| Project / seat | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| D7 TO-F | ADVANCING (both halves); apply leg ADVANCING-external (bus 14:49:33Z, routed 14:51Z, ordering theirs vs W6-PORT; 22 min, live owner) | OpalETL~Z (b) idle-event-driven on the CONFIRM / DE~Z (a) behind D8 act 1 / laptop | 15:02Z / 15:11Z / 14:51Z | none; re-verify the apply leg next tick if still silent (the "re-verified moving" requirement; not `[STUCK]`) |
| D8 | ADVANCING → one act from CLOSE | DE~Z act 1 | 15:11Z | none; movement ladder not triggered (9 work-calls) |
| D6/W6/v0.3 | ADVANCING (external; land 1700–1830Z) | laptop W6-PORT | 14:36Z relay | none |
| D9 | OFF-DEVICE-DRIVEN | laptop (c1) | — | none |
| OpalETL~Z, CTO~Z | IDLE-event-driven (0 work-calls ~9 min; `kind:loop` live) | — | 15:02Z | no capacity routing — no unassigned D-family work exists (half (a) = DE~Z's; D8/W6/v0.3 wait on events; D9 off-device); OpalETL~Z's own bound = nothing toward v0.3 before the GO |
| BG | out of scope | broker-aged; holding for Andrew's drill word | 14:49Z | noted (MSTR~Z's seat) |

**Dispatches:** 0 — attestations with real timestamps; "nothing blocked" is the valid outcome. **Hard gate:** every gated leg is external with a live owner (apply: verified routed 14:51Z, ordering theirs; W6-PORT: executing) and re-verification is scheduled, not assumed. **/allocation:** supply 6/6; no unassigned demand.
**Compiler tools:** get_live_agents; the telemetry read (python); git log since-tick (workspace + portal); deploy_ledger.py check --red; python read of the D8 proof; ps stream watchers; inbox top-level ls.
