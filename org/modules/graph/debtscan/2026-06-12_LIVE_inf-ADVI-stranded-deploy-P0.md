# DEBTSCAN LIVE FINDING — inf-ADVI 4-layer stranded-deploy P0 (2026-06-12)
## First wild catch of the 2a (stranded-deploy) + census class

**Family:** 2a reachability/stranded-deploy + 2d compositional (the class DEBTSCAN was built to catch)
**Severity:** SEV1 (live served-data staleness; Andrew-timed P0)
**Status:** **CLOSED 2026-06-12T22:53Z** — P0 recovered + R4 served-verified end-to-end.
**Triage:** REAL — Andrew-detected 20:37Z (inf ADVI $202M vs Orion $204.6M); recovered 20:44-21:26Z; **R4 served-verify CONFIRMED 22:49-22:53Z: ADVI total_aua = $204,596,210 EXACT Orion match (platinum) + MP aggregate cross-page consistent to the dollar + model_aua exact-match eclipse E_00 + reconciliation sentinel to the dollar ($1,798,043,903). Brief 17dff6ed3.**
**Provenance:** DS recovery report a3f53eeb7 (R5) + CTO root-cause trace; this is the operational LEDGER of the live instance + the structural-TO decomposition.

---

## Root cause — ONE 06-11 cutover bundle stranded across 4 layers

The v2-transactions cutover (06-11 ~12:08-16:08Z uploads) left the deploy inconsistent across layers, each independently breaking a pipeline leg:

| Layer | Defect | Class |
|---|---|---|
| L1 | EC2 bronze-runner syncs code/bronze-runner/ but the 8-dim orchestrator went to code/bronze/ (wrong prefix) → ran the May-8 7-dim orchestrator (no transactions) | stranded-deploy (MDPF_COUNTS) |
| L2 | inf-api-txn defaults date=now-1d; processed 06-11; 06-12 quorum sat 8/9 | half-cutover quorum-lag |
| L3 | code/silver uploads collided with stale May code/gold twins → sync_scripts() FATAL killed the 13:00Z chain (silent: on-instance, lock-held, no log/CW/SNS) | basename-collision + silent-FATAL |
| L4 | Eclipse runs as gold-chain post-sentinel; gold never ran (L3) → MP model leg froze 06-11 | cascade |

**Detection was HUMAN** (Andrew noticed stale ADVI) — the guard's FATAL is invisible. That is the core DEBTSCAN lesson: a fail-closed guard that's SILENT defeats its own purpose.

---

## Structural follow-up decomposition (8 candidates → TO status)

| # | Follow-up | TO | Status |
|---|---|---|---|
| a | Collapse code/bronze vs code/bronze-runner dual prefix | BRONZE-FIX #1 | AE 0.6 building |
| b | _BRONZE_COMPLETE required-dim set (silent-partial) | BRONZE-FIX #2 | authored/queued |
| c | Extend comp-pipescript deployed to bronze-runner prefixes | TOOL-03 | **LANDED b2ff049ce** (hand-diff retired; silent argparse-no-op closed) |
| d | MDPF source-data vintage stamping (F1-provenance) | BRONZE-FIX #4 | **LANDED 24753c70e** (replay reproduces P0 sig) |
| e | inf-api-txn D-1 default vs same-day quorum (complete v2 cutover OR move default) | BRONZE-FIX #6 (NEW) | authoring (DS lane) |
| f | Collision-guard FATAL loud channel (CW/SNS + lock-holder liveness) | BRONZE-FIX #7 (NEW) | **authored this entry** (DS lane) — the silent-outage fix |
| g | On-instance bootstrap-baked scripts refresh path (S3 doesn't propagate to running instances) | BRONZE-FIX #8 (NEW) | candidate (AE lane) |
| h | Gold-runner auto-shutdown arms on ANY completion w/o checking other running chains (21:27Z near-miss) | BRONZE-FIX #9 (NEW) | **authored this entry** (AE lane) — the near-miss fix |
| — | Deploy-completion ledger + RED COO alarm (the meta-catch) | BRONZE-FIX #5 | dispatched (AE 0.7 lead) |

Plus the 9 manual_api DRIFT rows (TOOL-03 finding) = a possible additional stranded-deploy under investigation (AE 0.6).

---

## DEBTSCAN significance

This is the FIRST live-wild instance of the exact class DEBTSCAN was chartered to catch (the 2a stranded-deploy + census family). DEBTSCAN's tooling (TOOL-01/02/03) + the structural contracts (#1-#9) directly close every layer: c was unverifiable until TOOL-03; the whole class was invisible until the completion-ledger (#5) + FATAL-loud-channel (#7). The precision-gate machinery proved its value on day-1 in the lab; tonight proved it in production.

**COO filing 2026-06-12T21:31Z** (recovery R5 a3f53eeb7 landed). R4 served-verify (platinum ~$204.6M) pending chain ~23:08Z — will append on confirm.

**COO CLOSE 2026-06-12T23:03Z** — R4 served-verify CONFIRMED end-to-end (brief 17dff6ed3): ADVI $204,596,210 EXACT Orion match + MP cross-page consistent to the dollar + model_aua exact-match eclipse E_00 + reconciliation sentinel to the dollar. Chain 21:18-22:49Z (19min under precedent), both pages served-fresh by 22:53:36Z. GO-to-recovered ~2h17m (~1h31m chain runtime), ~42min ACTIVE recovery. The morning-stamp mystery resolved (07:30 run never wrote a 06-12 partition) — strengthens + is covered by follow-up (d)/BRONZE-FIX #4 (vintage stamping, landed 24753c70e). P0 CLOSED. The entire failure-class is now structurally sealed (TOOL-01/02/03 + BRONZE-FIX #1/#2/#4/#5/#7/#9/#10 + W4-G1/G2/G3); residual #6/#7 in DS queue, #10 Leg B + W4-G1b in tomorrow's instance-up batch. RAVC3-accepted to DS 230308Z (CC CTO/CVO/MSTR).
