# work 1741Z — 0.4.0_DS_ClientPlatform~C — stale ADVI queue reconcile (COO-directed)

**Tick:** /work 2026-06-01 ~1741Z. **Trigger:** COO 174640Z (b) RECONCILE the 7 stale 5/28 ADVI TOs (verify-and-close, NOT blind-resume; surface only genuinely-open).

## Done this tick
Verified each of the 7 stale (5/28) ADVI TOs against current state via git evidence; flipped + inline `reconcile_2026_06_01` verdict; committed `1bc4f1f24` (pushed). **list_task_orders pending = 0** (queue noise cleared).

| TO | Verdict | Evidence |
|---|---|---|
| ADVI_INFDEMO.F4 cost-basis-anchor | DONE (in_progress->complete) | verify-channel PASS-mechanical, ship-gate (a)-(d) met (a8be3399e/b570b342a) |
| ADVI_INFDEMO.F11 fee-sliced-flows | SUPERSEDED (dispatched->superseded) | fee-split+canonical-NNA shipped via ADVI_INFMVP.F4/F5 (f5ac50af1/bcc29881c) + F11-B leg-1 LIVE (982394f01) |
| ADVI_INFDEMO.F11-followonB daily-fee-substreams | DONE leg-1 (pending->complete) | shipped 982394f01; leg-2 deferred |
| ADVI_INFDEMO.F4-followon per-year-attribution | PARKED (pending->parked) | post-demo tail; ADVI_INFMVP shipped+smoke-passed; per-year=graceful-hide. **Borderline-open — surfaced to COO** |
| ADVI_DEMOV1.003 registration (~C) | SUPERSEDED | ADVI_DEMOV1 CLOSED COMPLETE via .010-.012 (767c113ab) |
| ADVI_DEMOV1.004 pii-leak-scan (~C) | SUPERSEDED | leak-scan PASSED Fire-7 R5 leak=0 (9e52c86c9); project closed |
| ADVI_DEMOV1.006 mechanism-change (~D) | DONE (~D lane) | Path B shipped by ~D Phases 1-3 (115af15f8/50176a86e); COO-flagged stale (19fdf2155) |

ZERO genuinely-open. Only F4-followon (PARKED) surfaced as borderline (closeable unless Andrew wants per-year display refined).

## Commits
- `1bc4f1f24` (7-TO reconcile) — pushed origin/CLOUD.

## RAVC2
- COO 175136Z (verdicts + capacity flag) + CTO 175148Z (CC, F4/F11 were CTO-issued).

## Capacity / next
- FIND_INSURE active work fully closed (only Andrew universe-A/B remains). Reconcile quick -> flagged COO I have CAPACITY; accepted the MDPF Item-3 (12/27 standalone) parallelization offer — awaiting the Item-3 TO/scope dispatch (won't touch DS~B's TO-1a/1b).
