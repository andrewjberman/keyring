# ANDREW DIRECT -- the active-account security list with each security's earliest day goes to the DEMQUE backfill queue; what is the mechanism today (2026-10-15 ~17:4xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`, right after his "active accounts BBG exclusively" word.

**Verbatim (two messages):**

> The easiest way to do this is simply scan all the security days of all active accounts (have we sucecssfully identified these via matching between teh backfill data and current black diamond data?), we assemble list of those securities including earliest day they appear, and that is what goes to the DEMQUE backfill queue for this surface.

> I need to know the mechanism we have in play for doing this, what is the system logic/process at this time?

## What it sets (surfaced, not adjudicated)

1. **The method:** scan every security-day of every active account. Assemble one list of those securities, each with the earliest day it
   appears. That list is what goes to the DEMQUE backfill queue for this surface.
2. **He asks two things:**
   - whether active accounts are identified by matching the backfill (Commonwealth) data to current Black Diamond data;
   - what the system logic in play today is.

## Measured by this seat (read-only, `ACTIVE_COTTONWOOD_SET_V2.csv` @4d427d3bbb)

**The active set:** 860 accounts open at Black Diamond on 10-12.
- 41,826 window rows. By source side: commonwealth 18,966, black_diamond 15,974, both 6,886.
- 834 rows have a blank CUSIP; 373 of them carry a ticker.

**His list:** 3,368 CUSIPs, each with its earliest day.

| Earliest year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CUSIPs | 557 | 148 | 155 | 262 | 169 | 231 | 132 | 166 | 154 | 126 | 247 | 204 | 183 | 634 |

**Depth:** from each earliest day to 2026-10-14 is about **5.83M security-days** (weekdays, one field). That is against the earlier
held-window need of 3.42M and a Bloomberg day rate of about 23,432 cells.

-- recorded by 4.0.0_SA_CRO~DELL2
