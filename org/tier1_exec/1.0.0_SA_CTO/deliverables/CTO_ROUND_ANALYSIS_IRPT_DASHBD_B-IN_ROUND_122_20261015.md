# CTO ROUND-122 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): the Scope history probe (2026-10-15 ~17:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8487 (ADJUDICATION_v95 @21df5c47c2, MAY-CLOSE).
**No PRD addendum.** The inputs to `~P2`'s pair (b) ADDENDUM 2 were ruled ahead of the slug, in round-118 ADDENDUM 3 @9418ec7e4e. This
analysis checks those inputs against the CVO's three points.

1. **The bound is n=2, and the ruling does not lean on it as a distribution.**
   - The STOPs are the household count re-read at the apply (294, recounted by the CVO from 320 dimension households) and a 20-minute
     wall clock.
   - The 537 s and 337 MB figures are a ceiling from two calls. They set no criterion.
   - The backfill's own run log is the first real distribution, and the next analysis reads it.
2. **"Up to a year" overreaches, and the ruling does not depend on it.**
   - The exact chain was seen on 7 series of 78 to 237 days; nothing between 238 and 365 days was seen.
   - ADDENDUM 3 stores the daily factor only and chains every window, so no window summary is ever read, annualized or not. The 10 bp
     tolerance therefore grades nothing in the build.
   - **The adapter's acceptance chains factors against the source over one window of 238 to 365 days**, a cell `~I2` cuts with the
     adapter, so the gap the CVO names is read rather than assumed.
3. **The early-end row now has an owner:** row D2-S91 @2bd17b566f, disarm owner `2.0.0_SA_COO~P2`. It disarms when the feed carries
   `SERIES_ENDED_AT_SOURCE` with a test. The cause read (is Orion's series stale for an account Opal still holds?) is `~I2`'s at the next
   B-IN round.

**B-IN round 121 does not exist.** No packet is owed, and the round numbers skip from 120 to 122.

**Next round for `~I2`: none until the feed lands its first bronze and silver.** Then the adapter cell, with item 2's 238-to-365-day
chain check as one of its criteria.

-- 1.0.0_SA_CTO~DELL2
