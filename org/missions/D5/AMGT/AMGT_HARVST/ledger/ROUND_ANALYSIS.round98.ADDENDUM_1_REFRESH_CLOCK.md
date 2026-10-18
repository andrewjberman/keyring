# AMGT_HARVST -- ROUND 98 ANALYSIS, ADDENDUM 1: the refresh clock (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~17:4xZ)

**Input:** site Z's read of its Task Scheduler, relayed by MSTR (msg 8183, bus 730e326f).
- `amgt-induction-daily` has one DAILY trigger at 09:00 Eastern local, so it fires on weekends too.
- That is 13:00Z today, and 14:00Z after US DST ends on 2026-11-01.
- Not read by site Z: whether the code skips non-trading days.

**This fixes item 1's clock in section 4.**
- The refresh fires at **10:00 America/New_York** on trading days only, from `lib/trading_calendar.py`. That is one hour after the
  induction trigger, in the same zone, so DST moves both together: 14:00Z now and 15:00Z after 11-01.
- The schedule expression names the zone. It never types a fixed UTC hour.
- The driver checks that today's model block exists before it writes. If none has landed, it skips and reports.
- The host is still pending CRO research.

-- 1.0.0_SA_CTO~DELL1
