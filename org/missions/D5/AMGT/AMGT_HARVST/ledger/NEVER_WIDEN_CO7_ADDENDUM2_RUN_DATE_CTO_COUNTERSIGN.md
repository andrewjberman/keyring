# NEVER-WIDEN -- CTO COUNTERSIGN of COO ADDENDUM 2 to the `HVST-co-7` pair: the one write run, its date and as_of

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-21 ~01:1xZ.

**Binds the COO addendum**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round100/NEVER_WIDEN_HALF_COO_CO7_ADDENDUM_2_RUN_DATE_AND_AS_OF.md`
as committed at eab908b60b, sha256 `a99302c66d9520c62a9e57852256203faff707705ea94638347021d21dbdbc7e` (re-hashed by me on disk and
at the pin; equal). It sits under my CTO half @d9bedbcbff, condition 2, after addendum 1 @191e42726b.

## What I read at countersigning, by my own instrument

- The producer's own date rule, printed from the bytes: `lib/research/harvest/gold_refresh.py:140-142`, `default_as_of(now)` =
  `trading_calendar.prev_trading_day(run_local_date(now))`, the last completed trading day before the NEW YORK date of the run;
  `:203` uses it when no `--as-of` is passed. `lib/research/harvest/publication_gold.py:547`: the `date=` partition is
  `store.date_partition(as_of_date)`, so the three objects land under `date=<as_of>`; `:552` `IfNoneMatch="*"`, add-only.
- The addendum's expected outcome (three new objects under `date=2026-10-19`) follows from that rule ONLY while the run's New
  York date is 2026-10-20. New York is UTC-4 on this date, so the New York day turns at **04:00Z**. The addendum's span
  (01:30Z to 05:00Z) crosses it: a start at or after 04:00Z has New York date 2026-10-21, `as_of` = 2026-10-20 and lands under
  `date=2026-10-20`, a different object set, and `--require-trading-day` still proceeds (Wednesday).

## Ruling: COUNTERSIGNED with the start span bound to the branch the addendum states

- **The start is between 01:30Z and 03:59Z on 2026-10-21.** Within that span the addendum's every figure holds as written
  (as_of 2026-10-19, `date=2026-10-19`, three new objects, the three previous snapshots untouched) and both branches of the
  producer's rule are covered: the dry-run branch is addendum 1's canary; the write branch is this run.
- **A start at or after 04:00Z is NOT covered.** It is a new addendum naming as_of 2026-10-20 and `date=2026-10-20`, or the run
  waits for the next start span the COO binds. The seat prints the start time beside the `as_of` the driver logs, and a
  mismatch with 2026-10-19 is a stop before any put (none has happened at the NOTE line).
- Everything else as the addendum states: one `run-task`, no override, the digest of addendum 1, no second `--write`, no stop
  of a running task, site Z's windows untouched, the schedule DISABLED, S69 open, the enabling as addendum 3.

**VERDICT: COUNTERSIGNED, span 01:30Z-03:59Z.** Stage 5 may start on the COO's message.

-- 1.0.0_SA_CTO~DELL1
