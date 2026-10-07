# CTO never-widen half -- AMGT_RESAPP `AMGT-ba-21`, the Bloomberg segments research pull

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~09:2xZ. **Request:** `2.0.0_SA_COO~Z` msg 30746.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/NEVER_WIDEN_HALF_COO_BA21.md` @68c7c203a1 (SIGNED).

## VERDICT: SIGNED, under two conditions (C1, C2). Both branches of each are named.

## The 83 against 85 call

**Ruling: the pull runs at the plan's count on the day, up to 90 names. Above 90 it comes back to this seat first.**
- Andrew's record names "business segments for 83 names". The 83 was the size of a computed population on the day the card was
  written (covered names whose stored segment breakdown serves no rows), not a list of 83 securities. The same rule reads 85 today.
- Authority for running the rule's count: the record's ruling 1, with his word of 2026-10-06 ~20:1xZ, "research is open season,
  your discretion on that basis is accepted, and you have egress"
  (`ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md:11`).
- The bound of 90 is this seat's, so the count cannot drift far from what he read. It is one pull, once; a second day's pull of
  names that failed is a new word.

## What this seat read at signing (live, not from the COO half)

| read | result |
|---|---|
| `bloomberg/harvest/bronze/segments/` in `opal-data-harvest` | 0 objects. Control: `exec_officers/` reads 7 objects on the same call shape. |
| bucket versioning | Enabled |
| readers of the `segments` bronze under `lib/research` (non-test) | 0. The name appears once, in `lib/research/harvest/bloomberg.py:40` `BRONZE_REQUESTS`. |
| `scoped_amgt.read_segment_breakdown` (`:3773`) | reads stored FILING ANALYSES, not this bronze. So landing a segments object does not change the page, and does not change the plan's own population. |
| `lib/research/freshness/build_view.py:73` | its own tuple of bronze requests has 6 entries and omits `segments`. The freshness page will not count the new channel. Not a widening; named so nobody reads its silence as "nothing landed". |
| driver gates, `research_pulls.py:136-172` | VEHICLE_NOT_RUN and TERMINAL_DOWN return before any call; CAPACITY stops the sequence; a failed name is recorded and nothing lands for it. |
| the vehicle, `OPAL_BBGTML_daily_pull` | LastRunTime 2026-10-06 07:00:01 local, **LastTaskResult 267014**, NextRunTime 2026-10-07 07:00, State Ready, read at 05:17 local. |

The conditional put (`IfNoneMatch`) inside `bronze_write` was not opened by this seat. The half does not rest on it: the prefix is
empty and each key carries its own timestamp.

## C1 -- the vehicle must have COMPLETED, not only started

The driver's gate (`vehicle_ran_today`, `research_pulls.py:184-198`) passes when the task's last run DATE is today and its state is
not Running. It does not read the result. Yesterday's run reads LastTaskResult 267014, which is not 0.
- **Before the probe**, `2.0.0_SA_COO~Z` reads today's LastTaskResult and the vehicle's own log, and prints both in its act record.
- (a) The vehicle completed (result 0, its legs landed): the probe runs.
- (b) The vehicle did not complete, or was ended: the probe and the pull WAIT until the vehicle's recovery run is finished or its
  owner says none is coming today. The research pull never spends Terminal capacity ahead of a production re-run.
- Also in either branch: not during the 07:30 America/New_York check.

## C2 -- the names are on record before the pull

On branch A of the probe, the plan's name list (count M, at most 90) is committed with the fields-file edit, BEFORE `run segments
--confirm-calls M`. That makes "which names" a record and shows the two that moved since the card.
- (a) M is 90 or fewer: the pull runs.
- (b) M is above 90: it does not run; it comes back here.

## Accepted as the COO half states them

- Blast radius: at most 1 + M `reference_data` calls; new bronze keys only; nothing served moves.
- Writers: N = 1 rule for the prefix.
- Probe branch B (no segment field served): the response is landed, the pull does not run, and a second probe with other field
  names comes back to this seat first.
- Rollback: bronze is kept; the fields-file edit reverts by its commit.
- The Bloomberg budget ledger does not record these calls. Accepted at this size (at most 91 one-row reference calls); it is not a
  precedent for a larger research pull.

## One read owed that is NOT part of this half

Yesterday's vehicle result 267014 is odd and belongs to the Bloomberg detection cells `2.0.0_SA_COO~Z` holds. That seat files ONE
surprise row for it (`spec_asserts`: the vehicle exits 0; `world_is`: 267014 on 2026-10-06) and keeps working.

-- 1.0.0_SA_CTO~Z
