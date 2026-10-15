# CTO ROUND-128 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): Cottonwood account_return_daily landing, Acts 1-2 (2026-10-15 ~16:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8461, ADJUDICATION_v94 @16bddc09a1, MAY-CLOSE.
**No PRD addendum.** Issuer: `2.0.0_SA_COO~D2`.

- **Acts 1-2 landed inside revision 3's blast radius.**
  - Live equals the pinned .tf, and the schedule is DISABLED.
  - The write set is exactly 2026-07-10's `data.parquet` and `manifest.json`, and history is unmodified.
  - The artifact matches the pin, under the r3 clarification and row S88.
  - The lost invoke response is proven benign: 1 invocation, 0 errors, 118 s.
- **New, and it binds Act 3's grading: the layer ships pyarrow 14.0.2, but the reference measurement ran on 25.0.1.**
  - The served bytes come from 14.0.2, so byte or sha equality against a 25.0.1 reference proves nothing either way.
  - Act 3's grade therefore reads ONE landed day (07-10) at the VALUE level, against the reference: row count, key set, and every
    return value equal within 1e-12. Any difference is a STOP and a row.
  - The read also proves that the downstream reader (the holdings_performance function) loads the 14.0.2 file. That is the consumer's
    pyarrow, not the worker's.
  - This is a read and needs no new pair.
- **Timing is n=1.** Act 3's day count times 118 s must stay inside the order's window at concurrency 1. A day over the function's
  timeout is a STOP, never a raised limit as a rider.
- **No next fire while the schedule is DISABLED.** Enabling it is its own act, after Act 3 grades, under revision 3's terms.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~17:2xZ): Act 3 landed; the schedule is enabled on this word (`2.0.0_SA_COO~D2` msg 8481, packet @27847c126a)

- **Act 3 grades as the analysis asked.**
  - It landed 64 days, with the longest event at 436 s and the largest at 627 MB, and left history unmodified.
  - 2026-07-10 read at the value level: 867 rows, the key set equal, and a maximum difference of 0. The ledger is closed.
- **Erratum, mine:** this analysis named holdings_performance as the consumer, but that function does not read this table. The consumer is
  the **report-build function**. Its load of a 14.0.2 file is proved by its first build after the first scheduled fire, read in the fire
  check below. Until then, "loads under 14.0.2" is the worker's read, not the consumer's.
- **RULED: enable `irpt-cot-account-return-daily-daily` (DISABLED to ENABLED), on these terms:**
  1. One line in the pinned .tf, applied by `safe-apply`, under its own ledger entry. The plan reads 1 change and nothing else.
  2. The schedule's day is the trading calendar's T-1, as revision 3 states it. A fire on a non-trading day that writes a partition is a
     STOP and a row.
  3. **The first scheduled fire is read:**
     - exactly one new dated partition;
     - history unmodified;
     - one value-level spot read of the new day against the source;
     - the report-build function's next build loads the table without error.
     The ledger closes on that read.
  4. Rollback is the one line back to DISABLED. The partitions written stay; they are inert to a disabled schedule, and removing any is
     Andrew's act.
