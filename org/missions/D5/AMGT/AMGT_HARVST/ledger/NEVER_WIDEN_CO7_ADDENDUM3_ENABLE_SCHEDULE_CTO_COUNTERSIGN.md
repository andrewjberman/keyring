# NEVER-WIDEN -- CTO COUNTERSIGN of COO ADDENDUM 3 to the `HVST-co-7` pair: enable the daily gold-refresh schedule

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-21 ~03:3xZ.

**Binds the COO addendum**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round100/NEVER_WIDEN_HALF_COO_CO7_ADDENDUM_3_ENABLE_SCHEDULE.md`
as committed at 20d5a3e83c, sha256 `12670fb2e8f3213425cb89f11cbce32d96f86482e7df44bbd40aaec8d43bb87f` (re-hashed by me on disk and
at the pin; equal). It sits under my CTO half @d9bedbcbff ("the enable is a later act under an addendum"), after addendum 1
(@191e42726b), addendum 2 (@368c6df8c6, the write run landed 03:15Z and read by me: 25 / 27 / 11 objects, three `date=2026-10-19`
parts of 10,800,894 / 480,913 / 151,653 B) and my ruling on the S69 triage (msg 8964/8963 reply: parts 1-3 suffice; the rebuild
is a round-101 cell).

## What I read at countersigning, by my own instrument

- The schedule's bytes: `gold-refresh.tf:508` `state = var.gold_refresh_schedule_state`, `:510` `cron(0 6 ? * MON-FRI *)`, `:511`
  `America/New_York`. Equal to the addendum. 06:00 New York is 10:00Z until 2026-11-01, then 11:00Z; the addendum's first accepted
  fire, Friday 2026-10-23 10:00Z, is inside daylight time.
- The producer's own rule, both branches: `gold_refresh.py:140-142` sets `as_of` to the previous trading day of the New York date, so
  the Friday fire writes `date=2026-10-22`, each later weekday fire the prior trading day's partition, and a non-trading-day fire
  prints `GOLD-SKIPPED` under `--require-trading-day` and writes nothing. `publication_gold.py:552` `IfNoneMatch="*"`: add-only.
- The apply span (2026-10-22 10:30Z to 2026-10-23 08:30Z) sits after Thursday's would-be fire and before Friday's, so the enable
  itself fires nothing inside site Z's named windows; condition (b) re-asks site Z within two hours of the apply.

## Blast radius and rollback, as signed

One full-root `safe-apply`, plan exactly `0 to add, 1 to change, 0 to destroy`, the one change the schedule's `state` DISABLED to
ENABLED; any other proposed change is a STOP. Rollback is the same apply with `DISABLED`, never a deletion. The three objects any fire
adds are removable only by an S3 delete on Andrew's word, carded by the CTO with the keys; the previous snapshots stay, so nothing
is lost by waiting. The task role, the digest, the single manual write and S69 are unchanged.

**VERDICT: COUNTERSIGNED.** Stage 7 starts on the COO's message inside the apply span with every start condition printed true;
`HVST-co-7` stays open until the Friday fire's read (stage 8).

-- 1.0.0_SA_CTO~DELL1
