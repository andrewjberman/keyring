# Andrew-direct 2026-10-14 ~19:0xZ (laptop, 1.0.0_SA_CTO terminal) -- every pull behind Investor Reporting's performance and holdings tabs runs daily at 6:00 AM ET

## VERBATIM

> "Also another thing, we need to make sure that whatever pulls are happening to get all the IRPT performance tab and holdings tab
> data (on the Investor Reporting portal page), that those are scheduled with daily 6a ET pulls. I noticed that some data for the
> various clients would be from October 9th or earlier, so there must not be clean scheduling for that stuff. Need that message
> issued to DELL2 box so they can have their CRO look into it and scope it out for the CTO on that box to fold into the relevant
> workstream."

## What he observed

Some clients' data on the Investor Reporting page reads **October 9 or earlier** on Oct 14. Resolved with
`lib/trading_calendar.py` at ~19:0xZ: `trading_days_behind(2026-10-09, 2026-10-14)` is **3**, and
`expected_last_trading_day(2026-10-14)` is 2026-10-14. On a T-1 basis, October 9 is at least two trading days late. This is
his observation, not a measured census; each client is called stale only after its own trading-day read (CLAUDE.md hard stop).

## The directive (issued by `0.0.0_AB_MSTR` to dell2)

1. **`4.0.0_SA_CRO~DELL2` scopes it.** It inventories every pull and producer feeding the performance tab and the holdings tab,
   per client and firm. Each row gives:
   - the source;
   - the producer;
   - its trigger, as DESIRED (scheduled) against APPLIED (the live rule, read from AWS);
   - its last success;
   - the as-of date it serves today.

   The denominator is every client at every firm the page shows. Then the CRO names each one that is unscheduled, runs only on
   an upstream's success, is ad hoc, or runs off-cadence. Success-of-upstream as the only trigger is a defect under CLAUDE.md
   hard stops.
2. **The target:** every such pull is scheduled daily at **6:00 AM ET** (the cron must express 6 AM in New York across the
   daylight-saving change). Each downstream producer runs after its input lands, under its own schedule, with a stated
   freshness basis on the trading-day frontier. The CRO explains each client it finds at Oct 9 or earlier: a missed run, no
   schedule, a source that publishes late, or a correct trading-day read.
3. **The CRO issues the scope to `1.0.0_SA_CTO~DELL2`**, who folds it into the relevant workstream. That is IRPT_BCKEND or
   IRPT_DASHBD, which are P1 Investor Reporting, due Nov 15
   (`ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md`).
4. **No alarm or monitor is built**: the moratorium stands. Freshness is enforced by the schedule plus a gate or an owned
   blocking item.
