# /drive tick 4 — site-Z D-family scope — 2.0.0_SA_COO~Z — 2026-08-20 15:03Z (cron ebf739a0, the 14:56 fire)

**Authority/carrier:** Andrew-direct @2b3b2eaeaa; XXX.md COO row @e2c8e55dab. Scope: D6/D7/D8/D9 (SITEZ rows; LD-0428).

## Measurements (denominators printed)
- `get_live_agents` 15:03Z: MSTR~Z, DE~Z, OpalETL~Z, CTO~Z, COO~Z LIVE; BG aged off the broker (event-driven Teams loop, telemetry last 14:49Z) but its stream watcher is live by process → 6 watchers; CVO~Z gone (reaped). Census by process 6/6; no ghosts.
- Telemetry 19,386 rows; since the tick-3 marker (14:54:34Z): DE~Z 13, OpalETL~Z 13, COO~Z 7, CTO~Z 4, MSTR~Z 2, BG 0, CVO~Z 0 (reaped). Commits since tick: OpalETL~Z 1 (@2e7fae20d3 the Rule-24 matrix table), COO~Z 1 (tick-3 log). Portal DEV: no new commit (DE~Z's act 1 is an exercise; its `ui-smoke` extension is a tool edit).
- `deploy_ledger check --red`: only the out-of-scope HELD-STALE freshguard gate; 3/3 sentinels.
- D8 proof rows D8-5/D8-6: still UNCOMPUTABLE-BY-CONSTRUCTION (DE~Z act 1 in flight ~20 min).
- Broker summaries now accurate at DE~Z (detailed WORKING), OpalETL~Z (WORKING, apply-confirm wait), CTO~Z (ruler/router frame).

## Classification + action
| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| D7 TO-F | ADVANCING (both halves; apply leg ADVANCING-external — on the bus 14:49:33Z, routed 14:51Z, sequencing theirs) | OpalETL~Z (b) / DE~Z (a) / laptop apply | 15:02Z / 15:03Z / 14:51Z | none; re-verify the apply leg at the next tick only if still silent (~12 min old now) |
| D8 | ADVANCING → one act from CLOSE | DE~Z act 1 | 15:03Z | none; CTO~Z declares on the flipped rows; I validate |
| D6/W6/v0.3 | ADVANCING (external, land 1700–1830Z) | laptop W6-PORT | 14:36Z relay | none |
| D9 | OFF-DEVICE-DRIVEN | laptop (c1) | — | none |
| BG | out of scope | broker-unregistered, watcher live; holding for Andrew's drill word | — | noted (MSTR~Z's seat) |

**Dispatches:** 0 — per-project attestation with real timestamps is this tick's output ("nothing blocked" is the valid outcome; no receipt-ack noise manufactured). **Hard gate:** every gated leg is external with a live owner and verified moving (apply: bus 14:49Z/routed 14:51Z; W6-PORT: executing 14:36Z); nothing COO-resolvable is unresolved. **/allocation:** supply 6/6; every completing worker alive and producing.
**Compiler tools:** get_live_agents; the telemetry read (python); git log since-tick (workspace + portal); deploy_ledger.py check --red; python read of the D8 proof; ps stream watchers.
