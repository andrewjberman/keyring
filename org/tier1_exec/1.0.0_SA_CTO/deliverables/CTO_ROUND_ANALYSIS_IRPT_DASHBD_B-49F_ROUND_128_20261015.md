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

## ADDENDUM 2 (~17:3xZ): one table name, two contracts (`4.0.0_SA_CRO~DELL2` msg 8488, research @03d1a87a9c section B)

`irpt/cottonwood/gold/account_return_daily` holds two eras under one name:
- **Commonwealth:** 3,325 dates to 2026-06-22, `method_version` 3, an `asof`/`firm_scope` manifest.
- **Black Diamond:** 65 dates from 2026-07-10, `method_version` 2, a `business_date`/`contract_version 0.3.0` manifest.
- **A gap:** 12 trading days, 06-23 to 07-09.

**RULED (owner `2.0.0_SA_COO~D2`, row D2-S92):**
1. **The consumer never chains across a contract.** The report-build handler (DB-b-263/265, in flight) reads each partition's manifest
   contract and `method_version`, and chains only within one contract.
   - A window that reaches before 2026-07-10 serves from the Black Diamond era only and states "returns from July 10, 2026", or reads
     "not enough history" in words.
   - It never splices eras and never fills the gap. This is a build criterion of that handler, with a test that spans 06-22 and 07-10.
2. **No history is rewritten now.** Restating the Commonwealth era under contract 0.3.0, or moving it to its own name, moves served
   bytes. It is not cut until a page needs pre-07-10 returns, and then under its own pair. The 07-10 floor (round-124 ruling 1b) stands.
3. **`method_version` going backwards (3, then 2) is a label defect, recorded in the row.** The guard in item 1 keys on the manifest
   contract as well, so the label cannot mislead it. A producer re-stamp is a later cell, never a rewrite of landed keys.
4. **The schedule word (ADDENDUM 1) stands.** It writes Black Diamond-era days only and does not widen the mix.
5. **ADVI_COTBKF's un-park is not this fabric's.** Its placement is dell1 on Andrew's 10-14 word. The note that `~D2`'s report-build handler
   may meet its un-park condition goes MSTR to MSTR (`0.0.0_AB_MSTR~DELL2` relays it to dell1's manager). Nothing is driven across.
