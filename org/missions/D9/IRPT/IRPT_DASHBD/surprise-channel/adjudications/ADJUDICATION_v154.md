# IRPT_DASHBD: CVO adjudication, workstream B-IN (~I2), round 132: the first real run of the wrapper on the Scope feed's first silver (DB-i-19)

<sweep_watermark>2026-10-19T13:54Z</sweep_watermark>

**Basis.** L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-19T13:54Z, on msg 10694. The packet is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND132_BIN_DRAIN_END_20261019.md` @bddaac50dd. One order, TO-DB-i-19, complete; no judgment criterion. Read-only on AWS; counts only, no client value.

**Criterion, re-run on the merged tree (HEAD bddaac50dd):** DBI132-1-AC1 PASS.

**This seat's own reads.**
- **Independent of the wrapper:** the feed's bronze and silver prefixes each hold exactly ONE partition, `date=2026-10-16`. The silver day holds 863 rows, 863 distinct account ids and 16 columns. The bronze envelope's `universe_rows` is 863, its 294 calls' row counts sum to 863, and 0 households failed. **The silver row count equals the feed's own manifest.**
- **Through the wrapper:** `live_read.py` re-run into a private scratch folder, not the repo. It gives RAN, MANIFEST_AGREES, 863 in the feed, 863 mapped, 0 unmapped, **795 PRESENT + 68 ABSENT = 863** and 0 trading days unaccounted. The ABSENT reasons are NO_START_DATE_AT_SOURCE 39, GROUP_NO_SERIES 17 and NO_GROUP 12. All 795 PRESENT rows read `market_value_eod_claim` measured. **0 unaccounted holds.**
- **Against v81's denominator (863 roster accounts):** the total matches. One difference is noted, not graded: v81 counted 40 of the 863 with a null `accountStartDate` on the round-~171 dimension read, where this run classes 39 as NO_START_DATE_AT_SOURCE. One account has either gained a start date at source or falls in another ABSENT class. The membership read by hash is ~I2's next act (S60).
- **ONE snapshot (the v144 trap):** `live_read.py:101-102` reads `latest_partition` of `fact_positions` and of `fact_assets` (one partition each), and the feed silver holds one day. No union of cumulative snapshots.
- **Nothing written or deployed:**
  - the record's counters show 0 S3 writes, 0 vendor calls and 0 secret reads;
  - independently, the Inflection gold `account_return_daily` and platinum `reporting` addresses (`address()`) hold 0 objects, so 0 were written today;
  - no Lambda named for the Scope feed or Inflection account return exists.

**Stated limits, not passes.**
- **The boundary measure (0 pairs):** `run_scope_feed_real.py:66-67` pairs a day with the CALENDAR next day, `_next_day` = d + 1. The second landed day, 2026-10-19 (Monday), will NOT pair with Friday 2026-10-16.
  - **Earliest testable:** once silver holds `date=2026-10-19` and `date=2026-10-20`, the first two calendar-consecutive trading days, i.e. after the 2026-10-20 day lands.
  - **A finding:** every Friday-to-Monday and pre-holiday boundary is skipped by the same rule, so the measure never sees about one boundary in five.
- **The chain check (WINDOW_TOO_SHORT):** `MIN_WINDOW_DAYS = 238` (`:45`) calendar days.
  - **Earliest testable:** on the daily chain alone, when the silver spans 2026-10-16 to **2027-06-10**. Sooner only if the history backfill (waiting on the bronze-writer fix, IB-pn-5) lands 238 days of history.
  - **The issuer's plan does not fit it:** "cut the same read again once 3 landed days exist, so the boundary measure and the chain check have pairs" does not fit the chain check, which stays WINDOW_TOO_SHORT until a 238-day window.
- **Calendar arithmetic:** exercised only at one trading day, from the hardcoded NYSE table (W319-S2).

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S97",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-19T13:54:00Z",
  "one_line": "B-IN round 132 (~I2, DB-i-19): DBI132-1-AC1 PASS on the merged tree. Own reads: silver date=2026-10-16 holds 863 rows = the bronze manifest's universe_rows 863 (294 calls, 0 failed); wrapper 795 PRESENT + 68 ABSENT (39/17/12) = 863, 0 unaccounted, matching v81's 863. One snapshot read; nothing written or deployed. Limits, not passes: the boundary pairs only calendar-consecutive days (testable after 2026-10-20 lands; Fri-Mon never measured), and the chain needs a 238-day window (2027-06-10 on the daily chain).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-W319-S3"],
  "spec_asserts": "DB-i-19: the wrapper's output on the landed silver matches the feed's own manifest counts; PRESENT + ABSENT equals the accounts the feed carries; boundary and chain reported as untestable on one day.",
  "world_is": "Silver/bronze each 1 partition (2026-10-16); silver 863 rows, 863 distinct ids; manifest universe 863, calls 294 summing 863, 0 failed. Wrapper: 795/68, 0 unmapped, 0 unaccounted, claims 795 measured. run_scope_feed_real.py: _next_day = calendar d+1 (:66-67); MIN_WINDOW_DAYS = 238 (:45). Inflection gold account_return_daily and platinum reporting: 0 objects.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r132/p132_live.py . DBI132-1-AC1 -> PASS at bddaac50dd",
    "read-only list_objects_v2 + get_object of the feed's bronze and silver (pull_inflection_scope_account_returns.feed_addresses('2026-10-16')); pyarrow row and distinct-id counts",
    "python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~319/live_read.py --private <scratch> --record <scratch>: RAN, MANIFEST_AGREES, 795/68, 0 unaccounted",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py:45,66-67,70-99",
    "read-only list of address('irpt','inflection','gold','account_return_daily',...) and ('platinum','reporting'): 0 objects"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owed by 2.0.0_SA_COO~I2: (a) the boundary measure pairs on calendar d+1, so Friday-to-Monday and pre-holiday boundaries are never measured: rule whether the pair should be the next TRADING day (lib/trading_calendar); (b) the plan 'three landed days' does not reach the chain check (238-day window); state the chain's real earliest date or the backfill route; (c) the 40-vs-39 null-start difference against v81, settled by the S60 membership read."
 }
]
```
