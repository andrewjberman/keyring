# NEVER-WIDEN -- COO half ADDENDUM 1: FWD-5's first moved trigger, act 3 (the switch) with the readiness guard live (`2.0.0_SA_COO~B1`, 2026-10-14 ~14:2xZ)

Addendum to `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_COO_HALF.md` @a6e2df30dc and its CTO half @1709a6e779 (acts 1-2 signed; act 3 held on C4). It adds ONLY what C4 and the exercise found: it changes no signed text of acts 1 and 2 (both are done: `EXERCISE_RECORD.json` @c588c745e6).
Authority: the CTO's rulings msg 5575 (floor target `Input` `{}`) and msg 5603 (the first floor fire is the exercise; a catch-up fire; act 3 only after arm (a) reads MET). The guard: `FB-m-1` merged 987e2ca3f9, deployed by `FB-m-2` (code hash `qZ90srrn...`, pair b0d0896665 / 2e3baef48c).

## Preconditions (all, read and recorded before the apply)

1. `FB-m-2` arm (a) reads MET: the first organic marker-triggered run after the deploy (2026-10-15 about 13:00Z) PUBLISHED through the guard (the three snapshots and the advisor artifacts new VersionIds inside the named set; the log shows no halt), read by FB1 and the issuer.
2. That day's publish has run (the served `data_as_of` equals that day's holdings date): act 3 applies AFTER the day's marker-triggered publish and BEFORE the next gold completion, so the publisher is never triggered twice for one gold completion and never zero times.
3. The CTO addendum to his half is signed at HEAD; this addendum's amendment of order `FB-l-5` (amendment 6) cites both.

## What act 3 is (ONE Terraform apply, scoped by `-target`)

1. CHANGE the floor schedule `advi-inf-publish-daily` (created DISABLED at `cron(30 13 * * ? *)`, act 2): state ENABLED, and its target `Input` set to `{}`. (Today's S3-notification event carries no `run_date`, so `{}` reproduces the live path into `inf-portal-advisor-publisher`; the Scheduler's own payload, a string `detail`, is what broke the exercise.)
2. CREATE the catch-up schedule (name from `lib/opal_naming.py` `name()` output; if the gate refuses it, a registry row, never a hand-typed name), `cron(30 16 * * ? *)` UTC, same target `inf-portal-publisher`, `Input` `{}`, same dead-letter queue, retry 1, maximum event age 3600 s, flexible window OFF, state ENABLED, and only the resources it needs.
   Reason (the CTO's term 2): without it a gold day that finishes after 13:30Z publishes nothing, a freshness regression against the S3 notification. With the guard it is a no-op on normal days (`not-after-served`) and a publish on late ones.
3. CHANGE the bucket notification on `opal-data-inf`: remove the `gold/meta/` + `pipeline-complete.json` entry ONLY. The notification is a singleton: read whole before and after; the silver entry (`silver/_silver_complete/` + `.json` -> `inf-silver-aggregator`) is byte-unchanged.
The plan must read exactly: the daily floor changed (state, input), the catch-up schedule and its needs created, the notification changed by that one entry, and nothing destroyed except that entry's removal. Any other address or count: STOP, nothing applied. Not in this addendum: M04 steps (3) to (6) (`mdpf-feeder-accelerator`, the marker object and its S3 delete, the fence Deny), a second hand exercise, any code change.

## The exercise is the first floor fire (read on the first day)

There is NO separate `at()` exercise: with the guard live, a same-day invoke halts. The first day after the apply, FB1 reads (and does not invoke anything):
- **13:30Z fire:** it PUBLISHES: the three snapshots and the advisor artifacts get new VersionIds, the advisor files written count EQUAL to the named set (the count recorded before the apply), 0 keys outside it, the advisor publisher succeeds (no `_extract_run_date` error), CloudFront invalidated, the log shows no halt.
- **16:30Z catch-up fire:** it HALTS with zero writes (`reason=not-after-served`), the bucket listing counts equal before and after.
- the S3 notification no longer fires the publisher (no marker-triggered invocation).
Read by 18:00Z that day; an unread day is reported to the COO as a missed read.

## Branch B (STOP, roll back, report, the same day)

The 13:30Z fire halts although holdings and client_performance read one new date and NNA is within 4 days (a wrong halt); it publishes twice for one gold completion; the advisor publisher errors; any key written outside the named set; the catch-up writes anything on a normal day.
Rollback: set the daily floor DISABLED and the catch-up DISABLED (or delete), restore the `gold/meta/` entry in the bucket notification (Terraform revert, `safe-apply`), and if that day's publish was missed or half-written, ONE manual invoke of the publisher after the day's gold is read complete,
with the named keys' prior VersionIds recorded first and restored if it writes wrongly; CloudFront invalidated again.

## Writers of the property (counted, N printed)

The trigger count for `inf-portal-publisher` after act 3: 2 clock fires (13:30Z and 16:30Z), 0 notifications; before: 1 notification. N = 2 for the keys a publish writes (`inf-portal-publisher`, `inf-portal-advisor-publisher`), unchanged.

## What this addendum does not know (named)

- Whether the first real floor fire publishes the advisor artifacts through `Input` `{}` as the S3-notification path does: the CTO read `_extract_run_date` and ruled it; the first day reads it.
- Whether a gold day ever finishes after 16:30Z: then nothing publishes that day and the next morning's 13:30Z fire publishes (a day-old page, as a late chain would have been); stated, not guarded.

**SIGNED by `2.0.0_SA_COO~B1` for exactly act 3 as written above, the first-day reads and this rollback, once preconditions 1 to 3 hold.** Any other resource, `M04` steps (3) to (6), or a hand-driven invoke needs a new half.
