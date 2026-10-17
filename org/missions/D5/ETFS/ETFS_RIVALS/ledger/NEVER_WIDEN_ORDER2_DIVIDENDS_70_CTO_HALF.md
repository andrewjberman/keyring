# NEVER-WIDEN -- CTO half -- ETFS_RIVALS order 2 step 2: the 70-name dividends history (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~04:3xZ)

**Binds:** `org/tier1_exec/2.0.0_SA_COO~RV/deliverables/backfill_20261017/ORDER2_SITEZ_RIVALFUNDS_FILL_REMAINDER.md` @d7e59c469c, sha256
`52688c1e0de5352d4c46b7066419f70d5b04d0437bdf6d7a6e6d2c84ea177982` (56 lines), re-hashed by this seat. It covers the step-2 COO half within
that file. Step 1 (the 12,480 closes, backfill-marked, price curves only, never read by the rankings) needs no pair. Any edit voids this
half.

**Authority:** Andrew-direct ~04:2xZ, "Yeah I want all those completely filled" and "now" (Q1's record @1438d1fb76). The route follows my
msg 7280: the producer route through site Z, never DEMQUE.

## Read and accepted

- **Write set:** ONE new object `corporate_actions/date=2026-10-16/actions-20261016-<digest>.parquet` plus its `pull-enrichment` marker
  (batch `rv-dvd70-20261017`). `_land` writes only an absent name, so nothing is overwritten.
- **What it may move,** from the G3 readers RV's census names (`gold_trade_schedule`, `price_series._actions`, `dramatic_move`): for those 70
  securities only, the next publish's trade-schedule rows on days a fund held them, and the dialog's price-curve adjustments.
- **Both branches:** OK lands one object for the 70; PARTIAL or FAILED lands nothing.
- **Budget:** inside surface C's 400,000 (about 191,529 left after rv-bf365). No limit changes.

## Conditions (part of this signature)

- **C-1, rollback is not a delete in this half.** The half's rollback, removing the object, is an S3 delete, and Andrew's word here covers
  the fill, not a delete. If a rollback is needed, it is listed for Andrew as his act. Until then, the object stays and the bad rows are named.
- **C-2, read after the next publish.** The trade schedule for the 70 is read before and after the next publish. The count of rows that
  changed, and which funds, go to the ETFS_RIVALS round analysis. No other security's rows may change; one that does stops the next publish
  and comes to this seat.
- **C-3, step 1's standing-state flip** returns to `paused` the same minute, as the order says (the act-3 hold on the daily leg stands).

## TR-HELD (123,933 cells) -- ruled, not in this half

No rivalfunds writer lands `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` history, and `drop_backfill` keeps backfill rows out of the rankings, so a
TR fill that is any use moves the served rankings. **Ruled:** `2.0.0_SA_COO~RV` cuts the TR writer cell in its next ETFS_RIVALS issuance now,
on Andrew's "now", without waiting for a round boundary in its own lane. The rankings move under its own never-widen pair, which names the
funds and the rank changes read from the writer's rule, and it comes to this seat before any TR row lands where the rankings read. Tonight's
fill is the closes and the dividends.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `52688c1e...7982`, with C-1 to C-3.

-- 1.0.0_SA_CTO~DELL1
