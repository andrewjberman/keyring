# /drive tick 10 — site-Z D-family scope — 2.0.0_SA_COO~Z — 2026-08-20 16:21Z (cron ebf739a0; census tick at the swap event)

**Authority/carrier:** Andrew-direct @2b3b2eaeaa; XXX.md COO row @e2c8e55dab. Scope: D6/D7/D8/D9 (SITEZ rows; LD-0428).

## Census at the event (the swap DE~Z → CVO~Z)
- **CVO~Z LIVE** PID 38360, summary = re-seat at the V03 landing, second-read scope verbatim, startup protocol in progress; its stream watcher present (pid 1433797). Its 1 work-row since tick + 0.1m age = starting up, not parked.
- **DE~Z watcher child REAPED**: stream-watcher census = exactly 6 (COO~Z, CVO~Z, OpalETL~Z, CTO~Z, MSTR~Z, BG) — one per consuming seat, ZERO duplicates, ZERO DE~Z stream = the orphan-thief hazard absent at the moment of the swap.
- **DE~Z session still broker-registered** (PID 31384, summary STANDING DOWN, 96s) — mid-swap transient; MSTR~Z's reap completes it. WATCH ITEM for tick 11: if DE~Z still registered next tick, ask MSTR~Z to deregister (7 registered vs 6-seat ceiling is a bookkeeping artifact only while transient).
- BG broker-STALE (556s) with 9.5m telemetry age = the event-driven idle posture, healthy.

## Measurements (denominators printed)
- Marker frame 16:14:04Z (decoded). Telemetry 20,069 rows; since tick: COO~Z 16, CTO~Z 13, MSTR~Z 11, OpalETL~Z 5, DE~Z 4, CVO~Z 1, BG 0 (idle). Commits since: @33024cb134 (V03 accepted-pre-port + re-cert delta) · @3fcb378ef0 (my addendum 10).
- W5-V03 `pending` — the ONE remaining open D-family TO; close = laptop port landing (@0ebb5c71 ferried, rollback pinned) → CVO~Z second read → CTO~Z on-instance confirm. Outside COO power at every leg, each verified moving this tick (port on the laptop's cadence; CVO~Z seated for the read; CTO~Z live).
- `deploy_ledger check --red`: 3/3 sentinels; only the out-of-scope external/sovereign gates.

## Classification + action
| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| D6: W5-V03 | ADVANCING-EXTERNAL (port ferried; second-read seat LIVE; confirm staged at CTO~Z) | MSTR~Z/laptop → CVO~Z → CTO~Z | 16:2xZ | none; 2-step project close STAGED at my seat for the CLOSED word |
| D6 (rest) / D7 / D8 | COMPLETE / ruler-held residuals | — | — | none |
| D9 | OFF-DEVICE-DRIVEN | laptop (c1) | — | none |

**Dispatches:** 0 — the census WAS this tick's event-act; every remaining leg is externally held and moving. **Hard gate:** census executed at the event as committed (2520); no COO-resolvable gate unresolved. **/allocation:** supply = 6 working seats + 1 departing (transient); the V03 second-read worker is ALIVE and seated — the exact condition the swap existed to produce.
**Compiler tools:** get_live_agents; telemetry read (python, denominator 20,069, frame printed); ps stream-watcher census (grep -v grep); git log since-marker; deploy_ledger.py check --red; W5-V03 status grep.
