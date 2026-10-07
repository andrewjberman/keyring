# IRPT_BCKEND row S338, measured from the laptop -- a FILE for dell2 to file as its own row

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~08:1xZ, read-only, on `1.0.0_SA_CTO` msg 106060.

This content was filed in the laptop's copy of the channel as IRPT_BCKEND-S348 (@8dc6d1f929), renumbered S351
(@ffd56930e6), and taken out of the channel on `1.0.0_SA_CTO` msg 106091: only dell2 mints row ids for its project.
dell2's seat files it as a row under dell2's next id and cites it for leg A1 of ledger
irpt-inf-performance-serving-20261002. The `id` field below is the laptop's withdrawn id, kept so the history reads;
it is not a row id any more.

## The measurement (row content, as filed) -- S338 measured from the laptop: Inflection held positions on all three days; each day has no partition because the producer's declared close rule finds no source partition holding that day's close

```json
{
  "id": "IRPT_BCKEND-S351",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T08:10Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Row S338's NOT MEASURED half, read from the laptop: Inflection held positions on 2026-05-11, 2026-06-30 and 2026-08-10 (888, 922 and 948 accounts in the source partitions of those dates). None of the three is a no-data day. Each lacks a gold partition because, under the producer's declared partition_close, no source partition holds that trading day's CLOSE: two by declaration (NO_SINGLE_CLOSE), one because the 2026-07-01 source partition does not exist.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "producer source: data/assets/scripts/gold/irpt_holdings_performance/sources.json entry orion -> bucket opal-data-assets, positions_prefix {monolith}/{scope}/silver/fact_positions/, link_across_gaps true, gap_link_max_trading_days 10, balance_prefix null",
      "s3api list-objects-v2 on that prefix, every page (this seat, 2026-10-07 08:0xZ): 2352 date= partitions, 2020-04-24 to 2026-10-06. Present: date=2026-05-11, 2026-06-30, 2026-08-10. ABSENT: date=2026-07-01 (2026-06-30 and 2026-07-02 are present on either side)",
      "the producer's own close_partitions(), imported and run read-only on the three days: 2026-05-11 day-t close -> [] (its close would sit in the partition dated 2026-05-12, which the declaration marks NO_SINGLE_CLOSE); 2026-06-30 day-t close -> [2026-07-01, PRIOR_TRADING_DAY, NOT PRESENT]; 2026-08-10 day-t close -> [] (partition 2026-08-11 is declared NO_SINGLE_CLOSE). For all three the t-1 close IS present (2026-05-08 in 05-11/05-10/05-09; 2026-06-29 in 06-30; 2026-08-07 in 08-10/08-09/08-08). Control: 2026-08-07 resolves to three present partitions",
      "rows and distinct accountId read from the source parquet: date=2026-05-11 24293 rows, 888 accounts; date=2026-05-12 24372, 893; date=2026-06-30 33588, 922; date=2026-07-02 33618, 922; date=2026-08-10 35262, 948; date=2026-08-11 35262, 948",
      "holdings_performance.py _frame_for lines 1044-1048: with no partition holding the day-t close it returns ABSENT ('no day-t price exists') and writes no row; lines 1018-1034: the NEXT trading day links back over the missing close, so the return of the missing day is carried in the following day's linked row"
    ]
  },
  "spec_asserts": "Ledger irpt-inf-performance-serving-20261002 leg A1 (CTO batch 202 @8da55ee13b): every trading day of 2026 through the fire's day has a date= partition under Inflection's holdings gold; a trading day without one FAILS A1. Row S338 left NOT MEASURED whether Inflection had positions on the three days.",
  "world_is": "The three gaps are the producer behaving as declared, not a failed run and not a no-data day. A backfill cannot fill them: the closes of 2026-05-11 and 2026-08-10 are in no partition by the declaration's own measurement, and the close of 2026-06-30 would need the 2026-07-01 pull, which is not in the source. As written, leg A1 can never pass for 2026. Whether A1's wording changes (a trading day with no close in any source partition is a disclosed gap) is 1.0.0_SA_CTO's.",
  "notes": "RENUMBERED 2026-10-07 from S348 to S351 by its author on 1.0.0_SA_CTO msg 106081: dell2 minted S348, S349 and S350 in the same hour (branch q/dell2/custdy-r1-drains-cotbkf-l8-cro/r1), and S351 is the first id free on the laptop trunk and on that branch. dell2 row S350 cites this row as S348. Read-only: no backfill, no landing, no policy change (CTO msg 106060). NOT read: the gold rows of 2026-05-12, 2026-07-01 and 2026-08-11 (whether each carries the linked span the code implies); whether the adapter's missing-trading-day disclosure names the three days (S338's second NOT MEASURED item); why partitions 2026-05-12 and 2026-08-11 were declared NO_SINGLE_CLOSE (2026-08-10 and 2026-08-11 have equal row and account counts, which is consistent with a repeated snapshot, INFERRED). The gold bucket opal-data-inflection was not read by this seat."
}
```
