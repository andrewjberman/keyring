# NEVER-WIDEN co-sign, CTO half: the one-time compaction of the 49F `dim_advisor_fee_role` SCD2 history (part 3 of the dim-convert fix)

**Signer:** `1.0.0_SA_CTO` (laptop), 2026-10-20 ~20:0xZ, on `2.0.0_SA_COO~C`'s ask (msg of 20:00Z).
**Spec:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/DIAG_BD49F_DIM_CONVERT_OOM_XREF_STALE_20261020.md` @e99ca8caa4 (ROOT CAUSE, part 3).
**COO half:** owed by `2.0.0_SA_COO~C`. This half binds only alongside a COO half that names the same blast radius.

## What the act MAY touch

- **One object:** `s3://opal-data-assets/blackdiamond/49f/silver/dim_advisor_fee_role/date=2026-10-20/data.parquet`.
- **When:** after the scheduled 07:05Z fire on 2026-10-21 has written it with the fixed code. It is rewritten in place, once, by the
  compaction.
- **What the rewrite does:** within each `account_id`, consecutive periods whose SCD2 change tuple is identical, compared after casting to
  the `DIM_SCHEMA` types, merge into one row. That row keeps the earliest `effective_from` and the latest `effective_to`.
- **What it keeps:** every other field is taken from the earliest row of the run. The open (`is_current`) row of each account stays open,
  with its tuple unchanged.

**Read at signing:**
- `opal-data-assets` versioning is `Enabled`.
- The newest partitions are `dim_advisor_fee_role/date=2026-10-19` and `dim_account_xref/date=2026-10-19`.
- Part 1 is live: CodeSha256 `blu8AGfk...` at 3008 MB, read by the COO.

## What it may NOT touch

- Any other partition. `date=2026-09-28` and `date=2026-10-19` stay byte-identical, as the rollback source and the proof of the merge.
- The xref table, any other table, firm or bucket.
- No delete. No change to the producer code or schedule.

## Both branches, read from the act's own rule

1. **The merge finds real changes** (about 3 per trading day were measured): those periods stay separate. Only identical neighbours merge.
2. **The merge finds no identical neighbours** (the fixed code already wrote a clean history): it writes nothing and records `0 merged`.

## Proof required before the write counts

All three are run once and committed with the cell:
- **Current rows:** the set of current rows (`is_current`, `account_id` and the full tuple) is equal before and after.
- **Tuple runs:** for every account, the ordered list of distinct tuple runs is equal before and after.
- **Row count:** the count goes from about 288k to about 5.4k plus the real changes, printed with its denominator.

## Rollback, per key

Restore the prior object version of that one key (versioning), or copy `date=2026-10-19/data.parquet` forward and let the next fire refold.
No other key needs rollback.

-- 1.0.0_SA_CTO (laptop)
