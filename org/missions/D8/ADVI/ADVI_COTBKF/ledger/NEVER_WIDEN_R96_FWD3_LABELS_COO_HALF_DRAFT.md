# NEVER-WIDEN -- COO half -- DRAFT, UNSIGNED -- ADVI_COTBKF round 96: two label columns on the three served FWD-3 tables

**Signer (to sign):** `2.0.0_SA_COO~C1` (dell1). **Counterpart:** `1.0.0_SA_CTO~DELL1` (owed). **Applier:** a CloudOps seat, to be named at signing (`0.7.0_AE_CloudOps~CB1` seated this project's round 88).
**State: DRAFT. Nothing is applied, minted or served by this draft.** The fixed sections 1, 2 and 5 are measured now; sections 3 and 4 wait on round 96's control record (the served-move rebuild needs dell2's run data, CTO msg 6467).

## 1. The act and its blast radius (measured 2026-10-16 ~03:4xZ, read-only)

Act: `commonwealth_fwd3_serve.py --build --yahoo-active-policy interim` (local, at the served settings) then `--apply --overwrite`, one put per key. No other object is touched.
Keys are the builder's `target_addresses()`, read from code. Bucket `opal-data-assets`, versioning `Enabled`.

| table | key (under `commonwealth/cottonwood/silver/`, `date=2026-06-23/part-00000.parquet`) | prior VersionId | prior ETag | prior size | prior LastModified |
|---|---|---|---|---|---|
| daily_returns | `daily_returns/` | `w9j5YeV1LnNIakNlRTBX6jW1.SDHqmJR` | `26ad8293e2ba2e561dbde60b1aa7eb95` | 1,651,055 | 2026-10-09T12:41:01Z |
| account_day_value | `account_day_value/` | `qIWjLLwCIh_Gx6IblSgyaint2tfJ37pr` | `ca1ac0f48971f6cc0d11a147dcda086e-7` | 54,246,028 | 2026-10-09T12:41:02Z |
| month_grades | `month_grades/` | `QI5Ks8vQwGTwnc9ekyh.DOsyN8PKN3PB` | `7269e2607b1e5806058b1136b8c4e36b` | 421,751 | 2026-10-09T12:41:03Z |

The applier re-reads these three versions immediately before the first put and STOPS if any differs: something else moved the key.
Served rows (read now): `daily_returns` 1,691,729; `month_grades` 82,593; `account_day_value` 21,102,041 (round 83's figure; the control re-reads it). Served `run_commit` on both tables read: `6f70d5cc01bb2e196266799a657be6d0b2dc8a16`, the CB-ah-3 held build (row `ADVI_COTBKF-D1-S9`).

**Writers of the named property: N = 1.** The builder's `apply` is the only code that writes these three keys; no scheduled producer writes them (R34 half, section 1). Re-census at this draft: `comp-find` over `data/assets/scripts`, `lib`, `infra` for the builder module or the three key paths, 27 hits across 9,221 files scanned (5,525 ephemeral and 1,738 binary not searched); the one producer file that appears writes the `account_return_daily` table, not these keys. **Readers:** to be re-read at signing (R34 recorded 0 and a closed reader gate; this draft does not assume it still holds).

## 2. Rollback per key

For each key, copy the prior VersionId above back as the current version: `s3api copy-object --copy-source opal-data-assets/<key>?versionId=<prior VersionId>`; then read the three objects back and compare size and ETag with the table above. No key is deleted.

## 3. Expected outcome, BOTH branches (to be completed from the control record)

- **Branch A, the control reads equal on all three tables.** The built tables equal the served ones on every pre-existing column, row for row, with ONE exception stated here so it is not read as a moved value: `run_commit` changes from `6f70d5cc01bb...` to the build's commit on every row. It is a provenance column, not a value. Two columns are APPENDED: `use_class` (immediately before `porting_verdict`) and `porting_verdict` (last). `porting_verdict` was built in round 83 and never applied, so it is new to the served tables too. Row counts do not change. Label counts: from the record.
- **Branch B, the control reads a difference on any table.** NOT SIGNED. The difference is a finding for the CTO and nothing is written.
- **Either way the act writes labels only.** The `interim` policy moves no value (builder docstring; round 89 record). `--yahoo-active-policy blank` is never applied (call `3adb` (a); the builder refuses it under `--apply`).

## 4. Counts (empty: filled from the round-96 control record)

## 5. Conditions

- The round-96 control record reads `pre_existing_equal` true on all three tables, measured on run data copied from dell2 whose file count and total bytes equal dell2's own listing (CTO msg 6467).
- The applier runs `--dry-run` and `--apply` against the issuer's local build and never `--build`; the run_commit is part of the table content.
- The reader gate and any consumer of the served tables are read at signing; the CVO grades the labelled served tables after the write.
- The CTO half is signed against the same section-1 versions and section-3 branches.
