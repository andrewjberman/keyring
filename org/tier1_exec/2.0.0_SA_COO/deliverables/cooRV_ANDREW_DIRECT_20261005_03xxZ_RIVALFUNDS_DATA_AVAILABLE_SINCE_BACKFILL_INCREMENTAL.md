# ANDREW-DIRECT 2026-10-05 ~03:0xZ (23:0x ET 10-04) -- /rivalfunds design ideas approved; "Data available since X"; IDVZ/PFOE backfill to 01-01 via BBG ad hoc; daily pulls must be one-day incremental

**Channel:** Andrew at the `2.0.0_SA_COO~RV` terminal (site Z), in session, answering this seat's five-idea pitch (two-tier
switch with dates under each pill; every component header states its window with the switch in it, all in tandem; never "YTD"
over a short window; a short QTD says so and greys under 5 days; optional "Match IDVZ's window" comparison).

**Verbatim:**
> I agree with all of this but I'd go even further and qualify on 3. Instead of just saying "Since X", I'd say "Data
> available since X", so it is extra clear. We definitely can get the data on IDVZ and PFOE back to January 1 via BBG through
> the original backfill, so that should be easy enough to go pick up ad hoc. Beyond that, i want to make sure that we are
> pulling the new days data (and only new day, make sure the daily scripts are incremental one day adds, not just running the
> backfill script every day).

**Read by this seat (scope not widened):**
1. Ideas 1-5 are agreed; idea 3's label is "Data available since <date>".
2. The IDVZ/PFOE Bloomberg backfill to 2026-01-01 is directed, ad hoc, via the original backfill path (the D12 act).
3. The daily jobs must fetch only the new day (one-day incremental adds), never a backfill each day: to be measured and,
   where not true, fixed.

Recorded by `2.0.0_SA_COO~RV`.
