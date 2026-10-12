# Possible loss in `opal-data-bd/silver/transactions/` (dell2 row IRPT_DASHBD-D2-W124-S1): MEASURED -- no transaction id is lost (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~22:0xZ)

**Asked:** `1.0.0_SA_CTO~DELL2` dell2 msg 5923 (MSTR relay msg 4132). Two of three sampled days (2026-08-22, 2026-08-23) now hold 0 rows in the
original, after rewrites on 2026-08-26..2026-09-02; the copy in `opal-data-assets/blackdiamond/49financial/silver_legacy/` was faithful on
2026-08-25.

**Instrument (read only; boto3, this seat, ~21:5xZ):**
- read each day's OLDEST version with `GetObject` by VersionId;
- take the union of `transaction_id` over the CURRENT `silver/transactions/<day>.parquet` objects dated 2026-07-20..2026-10-10: 83 of 1,925 objects
  in the prefix, 360,103 distinct ids.

| day | first version | rows | distinct ids | present now in a current file | missing |
|---|---|---|---|---|---|
| 2026-08-22 (Sat) | 2026-08-22T00:10:21Z | 23,229 | 4,545 | 4,545 | **0** |
| 2026-08-23 (Sun) | 2026-08-23T00:14:13Z | 4,990 | 1,035 | 1,035 | **0** |
| 2026-08-24 (Mon) | 2026-08-24T21:54:40Z | 0 | 0 | 0 | 0 |

**Reading:** the later runs re-attributed those transactions to other days' files (the loader's 30-day id window). The weekend files emptied, and
the ids live elsewhere. That is not a loss of any transaction id.

**What this does not show:**
- that the re-attributed rows are byte-equal in their other fields (ids only were compared);
- whether a gold reader keyed by FILE day (rather than by `trade_date`) reads a different day's figures after the move.
The second is IRPT_DASHBD's tie-out question on its own surface. ADVI_FIRMBKTS's moving classes do not include `silver/`.
