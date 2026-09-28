# /self-drive ~O fabric -- ticks 102-103 (1.0.0_SA_CTO~O, 2026-09-28 05:45Z-06:45Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **MX-s-9 COMPLETE** (COO~O @f87d5b8b77): the BD asset dimension pulled by REST, 12,132 rows, super-class = dim 7.
  A disclosed 3-vs-2 read overrun was accepted; there was no vendor write.
- **MX-s-6:**
  - A1 pointed the asset-grain pull at the transaction-grain `silver/bd_assets.parquet` (3.45M rows).
    `0.4.0_DS_ClientPlatform~D` STOPPED before writing (row Z-S34 @b0fdb8fa33).
  - A2 made step 2 DIM-ONLY. The data is done: 12,141 rows, s4.AC3 PASS, 805/805 coverage.
- **Z-S33, the naming gate against the `_bd` column: DISARMED** by this seat, row Z-S36 @22d6e8f182.
  - The union goes inside the existing `build_bd_assets_dim.py`, where the literal is EXISTING at HEAD
    (`naming-gate.py:17-18`), so the gate WARNs.
- **Z-S37, the silver-id gate is fabric-wide but its helper is firm-local: RULED (a)** @86b1b3b5b4.
  - Promote `coerce_silver_ids` to `lib/silver_ids.py`, with an inf re-export.
  - Refused: the cross-firm import (NEVER firm separation), and the exemption (it leaves the gate blind in bd).
  - COO~O's A3 grants the paths (@5b454bd219).

**Cards at Andrew:**
- (1) URGENT: rotate the BD password.
- (2) The history-scrub scope.
- (3) The census as a commit gate.
- (4) The switchover sitting.

**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED
