# /drive tick 8 — site-Z D-family scope — 2.0.0_SA_COO~Z — 2026-08-20 16:01Z (cron ebf739a0; FIRST tick on the ~Z marker per the tick-7 correction)

**Authority/carrier:** Andrew-direct @2b3b2eaeaa; XXX.md COO row @e2c8e55dab. Scope: D6/D7/D8/D9 (SITEZ rows; LD-0428).

## Measurements (denominators printed)
- Marker frame: `~Z` file, 15:50:12Z (decoded + printed before use — the tick-7 lesson). Counts below span 11 minutes and are magnitude-plausible.
- `get_live_agents` 16:01Z: MSTR~Z, DE~Z, OpalETL~Z, CTO~Z, COO~Z — 5 broker-live. **BG absent from the broker but telemetry FRESH (16:01:00Z, 6 rows since tick)** — the event-driven seat aged off registration, process alive; MSTR~Z's seat, noted not acted. CVO~Z reaped (0 since tick, expected).
- Telemetry 19,915 rows; since 15:50:12Z: OpalETL~Z 21, MSTR~Z 19, COO~Z 19, CTO~Z 15, DE~Z 11, BG 6 — every live seat producing.
- Commits since marker: TO-F flip **@42f789623c** (MSTR lane; portal gitlink → @483b896c same commit) + endings fix @251b454dbe · acceptances @486b18154d (TO-F 12/12) + @9912a960d5 (W6-T1 accepted-pending-live-positive) · my @a29bb7edd2 (record COMPLETE-ACCEPTED) + @91cd28257e (addendum 9) · MSTR~Z handoff save @305d2e4023 (1555Z, clean-restart prep).
- TO statuses: TO-F **complete** · TO-AC pending (dry-run-only BY RULING) · W5-V03 pending (owner WORKING Phase-1 census, 21 rows/1.5m age) · W6-T1 pending (accepted-pending-live-positive).
- `deploy_ledger check --red`: 3/3 sentinels; only the three out-of-scope external/sovereign HELD-STALE gates (24h nudge cadence, suppressed).

## Classification + action
| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| D7 TO-F | **COMPLETE** (accepted @486b18154d; flipped @42f789623c; record current @a29bb7edd2) | — | 15:5xZ | row closed |
| D7 TO-AC | pending, dry-run-only BY RULING (CTO~Z READ-principal gate) — ruler-held, re-verified | OpalETL~Z | 15:59Z | none |
| D7 TAC rows | at COO~Z hold by design (schedule lands via OpalETL~Z after its queue) | me | — | held; sequenced behind V03 |
| D6: W6-T1 F8 | ACCEPTED-PENDING-LIVE-POSITIVE — close rides MSTR~Z's BG relaunch (handoff saved 1555Z; successor's 08-21 acceptance morning named) — outside COO power, verified moving | MSTR~Z | 15:55Z | none; I validate at the CLOSED upgrade |
| D6: W5-V03 | ADVANCING — owner on Phase-1 consumer census NOW (21 work rows since 15:50) | OpalETL~Z | 15:59Z | none; I validate V03-1..8 on arrival |
| D8 | COMPLETE | — | — | closed |
| D9 | OFF-DEVICE-DRIVEN | laptop (c1) | — | none |

**Dispatches:** 0 — the program's only open builder (OpalETL~Z) is actively producing; DE~Z is IDLE with both acts closed and no unrouted program work (new routing = CTO~Z's); BG's broker-absence is a registration TTL with fresh telemetry, MSTR~Z's seat. "Nothing blocked" is the valid outcome. **Hard gate:** no COO-resolvable gate unresolved (TO-AC = ruling; F8 close = MSTR~Z relaunch, moving; ledger reds = external/sovereign, out of scope). **/allocation:** supply 5 broker-live + BG process-alive; every completing worker producing.
**Compiler tools:** get_live_agents; telemetry read (python, denominator 19,915, frame printed); git log since-marker (workspace + portal); deploy_ledger.py check --red; grep on the four TO status lines.
