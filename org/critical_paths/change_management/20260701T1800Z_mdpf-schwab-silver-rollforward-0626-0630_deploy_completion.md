# Deploy-Completion Ledger — MDPF Schwab-silver roll-forward (06-26 → 06-30)

**Opened:** 2026-07-01T18:00Z (promote-START) | **Owner:** 0.5.0_AE_OpalETL | **Authorized:** Andrew-direct (via COO 175933Z) | **Priority:** P1 (served aggregate-AUA frozen 6 days since 06-25)
**Class:** served-data change (un-freezes MDPF served client AUA) — NO-HALF-DEPLOYS gate binds: every leg tracked; unclosed at session end = COO alarm.

## Why
MDPF served aggregate_aua frozen @2026-06-25 16:42Z. Root: Schwab bd/silver frozen @06-25 → WS-E 49F build sees $0/0-accounts from bd/silver/allocations → non_model_aua = -$1.4B → verification fails → no serve. Fix: roll Schwab silver forward 06-26/06-29/06-30. Raw for those dates is in the quartz-validation prefix (Andrew authorized promoting it to prod for THIS roll-forward; the durable quartz-daily cutover is a SEPARATE follow-up COO tees to Andrew).

## Scope (mine; CVO owns 06-25 + 06-30-rps — do NOT touch)
Trading days 06-26 (Fri) / 06-29 (Mon) / 06-30 (Tue). 06-27 Sat / 06-28 Sun = no delivery.

## Legs
| # | Leg | Status |
|---|---|---|
| 1 | Promote quartz-validation raw → 01_raw/ (CRS2026{0626,0629}.* full + CRS20260630.{ACC,TRN}) + mirror *.RPS → bronze/rps/ | OPEN |
| 2 | Convert 06-26 silver (ACC/RPS/TRN-A/TRN-NNA-B/ULN/RLD) | OPEN |
| 3 | Convert 06-29 silver (ACC/RPS/TRN-A/TRN-NNA-B/ULN/RLD) | OPEN |
| 4 | Convert 06-30 silver ({ACC,TRN} only; rps=CVO's; uln/rld pending box) | OPEN |
| 5 | Silver-verify vs SERVED: bd/silver/allocations 49F custody != $0 (the defect) | OPEN |
| 6 | MDPF un-freeze verify (next INF-trigger: WS-E recomputes + served aggregate_aua advances + magnitude sane) | OPEN |

## Downstream watch (flag COO)
- BD silver/fees gate (frozen 06-25) may STILL block the MDPF re-run even after Schwab-silver lands → COO's lane if a separate fees advance is needed.
- gold/aua_certification/{date}.json NoSuchKey (WS-E cross-check).

## Close condition
All 6 legs done + served aggregate_aua verified UN-FROZEN with sane numbers. RAVC COO at ledger-opened / legs-landed / served-un-freeze-verified.
