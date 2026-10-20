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

-- 1.0.0_SA_CTO (laptop)
