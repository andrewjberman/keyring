# bd49f dim-convert: out of memory on every trading day since 2026-09-29, so 49F dim_account_xref stopped at 2026-09-28

**By:** `1.0.0_SA_CTO` (laptop), 2026-10-20 ~18:2xZ. **Asked by:** site Z (CRO~Y brief @1ce8848c4b), carried by dell1's CTO (msg 8742) and
`0.0.0_AB_MSTR` (msg 109977): "restore the cadence, or name it retired". **Ruling:** RESTORE. The producer is not retired; it crashes.

## Measured (read only)

- **Newest xref partition:** `s3://opal-data-assets/blackdiamond/49f/silver/dim_account_xref/date=2026-09-28/`. Today is 2026-10-20, so
  2026-09-29 through 2026-10-19 is 15 trading days, the same as site Z's count.
- **Lambda `opal-assets-bd49f-dim-convert`:** `memory_size = 1024`, `timeout = 900`
  (`infra/aws/terraform/opal-assets/bd49f_convert.tf:112-113`). The code was last changed 2026-07-17, and the schedule was retimed to
  07:05Z on 2026-08-19.
- **Log group `/aws/lambda/opal-assets-bd49f-dim-convert`, last 30 days:**
  - Every trading-day run reads `Max Memory Used: 1024 MB` and ends `Status: error` (`Runtime.OutOfMemory`) or `Status: timeout`.
    The days are 10-14, 10-15, 10-16, 10-17 and 10-20, three attempts each.
  - The 10-18 and 10-19 weekend runs use about 222 MB and do not fail (no new feed).
  - Today's 07:1xZ run logged `dim rows total 288194 (current 5339) | xref rows 6200`, then `Runtime.OutOfMemory`, before landing outputs.
- **Cause:** the converter reads the SCD2 dim's full history, about 288k rows and growing every day, into memory. It crossed 1 GB around
  2026-09-29. The producer chain is alive, and the bronze pull still feeds it.

## The fix

- **The change:** one line, `memory_size = 1024` to `memory_size = 3008` in `bd49f_convert.tf`, applied by `safe-apply` in the
  `opal-assets` root.
- **Proof:** one invoke for today's date, which lands `date=2026-10-20` for the xref and the dims.
- **Blast radius:** this one function's configuration. The next run writes new date partitions, which is the producer's own rule, and touches
  no existing partition. Rollback is `memory_size = 1024`.
- **What it does not do:** the 15 missed days stay missing as partitions. The dims are SCD2 and the newest xref is a full snapshot, so the
  current resolution is whole once one run lands.
- **Growth:** this is headroom, not a cure. The full-history read keeps growing, so a later cut should read only the latest partition (owner
  to be named).

## ROOT CAUSE (measured ~18:3xZ): a false SCD2 change on `flat_fee`, every account, every day

- **The stored dim at `date=2026-09-28`:**
  - 282,857 rows, of which 5,338 are current;
  - 53 periods per account (median), one new period per account every trading day;
  - between the 09-25 and 09-28 periods, **3 of 5,338 accounts** actually differ in the change tuple.
- **The 09-28 fold, reproduced locally** (the converter's own `run()` up to `scd2_fold`):
  - the fold sees **5,338 of 5,338** accounts as changed;
  - the one column that differs for all of them is `flat_fee`.
- **Why:** `_tuple_frame` compares `astype(str)`.
  - The prior partition reads `flat_fee` as float64, so `"0.0"`.
  - Today's frame builds it with `pd.to_numeric(...)` (line 343), which yields an integer, so `"0"`.
  - Every account therefore closes and reopens daily, and the history grows about 5,300 rows a day until the 1 GB Lambda dies.

## The fix (three parts)

1. **Code** (stops the growth): in the fold's comparison, cast every tuple column to its `DIM_SCHEMA` type before stringifying, or cast
   `flat_fee` to float64 at line 343. Add a test in which a prior float `0.0` and today's int `0` are unchanged. Both copies change:
   `infra/aws/lambda/...` and `data/assets/scripts/silver/`.
2. **Memory** (restores today): `memory_size = 3008` until part 3 lands. With part 1 alone, the next run still loads the 288k rows.
3. **Compaction** (one time, under a never-widen pair): merge consecutive periods whose tuple is identical, which takes about 288k rows to
   about 5.4k plus the real changes. It rewrites served history, so the sign-off names the blast radius, and the old partitions stay
   until Andrew confirms any delete.

-- 1.0.0_SA_CTO (laptop)
