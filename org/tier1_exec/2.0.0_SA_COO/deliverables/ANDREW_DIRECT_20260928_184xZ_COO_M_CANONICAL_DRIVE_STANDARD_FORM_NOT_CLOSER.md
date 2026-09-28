# ANDREW-DIRECT 2026-09-28 ~18:4xZ -- ~M runs its workstream on /canonical-drive standard form, not /closer-drive

**Channel:** Andrew at the `2.0.0_SA_COO~M` terminal (laptop), 2026-09-28 ~18:4xZ.

## Verbatim

> make sure you run your workstream on /canonical-drive standard form, NOT /closer-drive

## State at receipt (measured 18:42Z)

- Loop: session cron 8af98d92, `3,13,23,33,43,53 * * * *`, prompt `/canonical-drive IRPT_BCKEND ~M workstream ...`
  (CronList). Authority: `org/ref/LIVE_ARMS.md` RELAUNCH 2026-09-28 row (landed by 1.0.0_SA_CTO @1d443e50db).
- Leases: `drive-mode.py read IRPT_BCKEND~M` -> FULL; `read IRPT_BCKEND` -> FULL. On FULL, /canonical-drive runs its own
  body (obligations 1-8) and never routes to /closer-drive; that route opens only on a FAST lease.
- Workstream: IRPT_BCKEND ~M, round 19 (`decompositions/IRPT_BCKEND_DECOMP_R19_M.md`, orders TO-IB-m19-1 / -2 cut
  under /dispatch; issuance refused by GATE (x), row IRPT_BCKEND-S179, decision with 1.0.0_SA_CTO).

## Binding on this seat

- Every tick of this workstream runs the /canonical-drive body. /closer-drive is not run for IRPT_BCKEND ~M.
- A FAST lease on `IRPT_BCKEND~M` or `IRPT_BCKEND` does not change that for this seat; if one appears, this seat
  still runs the canonical body and surfaces the lease to 1.0.0_SA_CTO.
- Scope is as spoken: this seat's workstream. Nothing here reads onto another seat.
