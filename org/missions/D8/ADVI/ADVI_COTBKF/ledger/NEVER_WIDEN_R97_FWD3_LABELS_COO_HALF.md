# NEVER-WIDEN -- COO half -- ADVI_COTBKF round 97: two label columns on the three served FWD-3 tables

**Signer:** `2.0.0_SA_COO~C1` (dell1) | **State: GIVEN** (2026-10-16 ~07:0xZ). **Counterpart:** `1.0.0_SA_CTO~DELL1` (owed; the half is not in force until his is signed against the same section-1 versions and section-3 hashes). **Applier:** a CloudOps seat, to be named by the CTO (`0.7.0_AE_CloudOps~CB1` seated this project's round 88). Supersedes the unsigned draft `NEVER_WIDEN_R96_FWD3_LABELS_COO_HALF_DRAFT.md`, which stays as the history of the round-96 finding.

**Basis.** Andrew's call `3adb` (a): served Yahoo-priced days stay, labelled interim until Bloomberg replaces them (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md`). CTO msg 6455: delta 0 on every pre-existing value or stop. CTO msg 6530: do not apply the round-96 build (its labels read NOT_YAHOO over Yahoo-sourced prices); relabel and re-measure. Round 97, `CB-cs-1` (worker ~187, drained @7d9663b5ad, order complete @76a608ad60), did that.

## 1. The act and its blast radius (versions re-read at signing, 2026-10-16 ~07:0xZ, `head-object`)

Act: `commonwealth_fwd3_serve.py --apply --overwrite --out <the round-97 build>`, one put per key. No other object is touched. Keys are the builder's `target_addresses()`, read from code. Bucket `opal-data-assets`, versioning `Enabled`.

| table | key (under `commonwealth/cottonwood/silver/`, `date=2026-06-23/part-00000.parquet`) | prior VersionId | prior ETag | prior size | prior LastModified |
|---|---|---|---|---|---|
| daily_returns | `daily_returns/` | `w9j5YeV1LnNIakNlRTBX6jW1.SDHqmJR` | `26ad8293e2ba2e561dbde60b1aa7eb95` | 1,651,055 | 2026-10-09T12:41:01Z |
| account_day_value | `account_day_value/` | `qIWjLLwCIh_Gx6IblSgyaint2tfJ37pr` | `ca1ac0f48971f6cc0d11a147dcda086e-7` | 54,246,028 | 2026-10-09T12:41:02Z |
| month_grades | `month_grades/` | `QI5Ks8vQwGTwnc9ekyh.DOsyN8PKN3PB` | `7269e2607b1e5806058b1136b8c4e36b` | 421,751 | 2026-10-09T12:41:03Z |

The three versions read today equal the draft's of ~03:4xZ and the worker's reads of rounds 96 and 97 (no seat has written these keys since 2026-10-09). The applier re-reads them immediately before the first put and STOPS if any differs.

**Writers of the named property: N = 1.** The builder's `--apply` is the only code that writes these three keys. Re-census at signing: `comp-find --files` over the corpus `all`, 140 file hits (434 matches) across 115,457 files scanned (12,723 ephemeral-floor, 50 unreadable, 27,755 binary not searched). The code files that name the keys or the builder are the builder, its two test files and `commonwealth_account_return_daily.py`, which writes the `account_return_daily` table and not these keys (round 34 and the draft's census read the same). No scheduled producer writes these keys.

**Readers: none today.** The gateway catalog entities for all three tables (`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`) carry `tools: []` and `read_tool: null`. The round-34 half recorded 0 readers and a closed reader gate; this signing re-reads only the catalog and the census above. Not established: a reader that builds the key from parts (the opal_naming.address() form matches no literal token), and a consumer outside the catalog. (Round 91's `READERS_RECORD.json` covers readers of the Yahoo and price tokens, not consumers of these tables, and is not cited as evidence of none.) The change appends columns after the last pre-existing column of each table and moves no value.

## 2. Rollback per key

For each key, copy the prior VersionId above back as the current version: `s3api copy-object --copy-source opal-data-assets/<key>?versionId=<prior VersionId>`; then read the three objects back and compare size and ETag with the table above. No key is deleted.

## 3. The build to apply, and the expected outcome (both branches)

- **The build to apply is the issuer's local build, applied as built and not rebuilt.** Location `.scratch/cotbkf_r97/build/` on dell1 (gitignored, off git; `fwd3_manifest.json` beside the three tables). Built by worker ~187 at `run_commit` `14793ce1882921b8da023c99e9512879d0d451c1` from a regrade re-run with the current code at the served settings (after arm `method_r28`, price basis `as_traded`, list `v1`; split store pinned at `2026-10-09T11:52:52Z`, 32 listed and held; Yahoo cache 3,580 files, sha256 `5b4bb7db3acde4b18f15b22bde58e3d4a27c1e690c5c601f7684bcf62e0cf3cb`; hold list `05613L3H2,95000U2D4,651639AX4`; policy `interim`). The run_commit is part of the table content, so the applier runs `--dry-run` and `--apply` against THIS `--out` and never `--build`.
- Content hashes (from the manifest, `manifest_hash_same` to be read by the applier's `--dry-run`):

| table | rows (before -> after) | content hash (after) |
|---|---|---|
| daily_returns | 1,691,729 -> 1,691,729 | `b558693deb2975198b36c1a23a5905f7eb9b19daf2a387a6924276bf1508427c` |
| account_day_value | 21,102,041 -> 21,102,041 | `7792443dc3e61d6f0766e7eda4af83a78a89b2e849ad888f09b7a48949e4199b` |
| month_grades | 82,593 -> 82,593 | `eca458ac82800c658d9ebcf8c986362cc53652a4924997b3d6e019c547e1aa0a` |

- **Branch A, REALIZED at signing: the control reads equal on all three tables AND the labels mark the Yahoo-sourced prices.** `pre_existing_equal` true in 3 of 3 tables, `rows_differing` 0, `max_abs_diff` 0.0, over 5 / 6 / 18 compared columns (`SERVED_MOVE_RELABEL_RECORD.json`, `deliverables/0.9.0_WK_ADVI_COTBKF~187/`). ONE column differs by design: `run_commit`, from `6f70d5cc01bb2e196266799a657be6d0b2dc8a16` to `14793ce1882921b8da023c99e9512879d0d451c1` on every row (a provenance column, not a value). Two columns are APPENDED, `use_class` then `porting_verdict`. Row counts do not change.
- **Branch B, a difference on any pre-existing column:** NOT SIGNED; a finding for the CTO, nothing written. The applier's pre-write re-read of the three versions and its `--dry-run` hash read are the check that the build and the keys are still the ones measured; a change in either is Branch B.
- **Branch C, equal but the labels do not mark the Yahoo-sourced prices:** NOT SIGNED. It was the round-96 result and is the reason for round 97; it does not hold now (section 4).
- **Either way the act writes labels only.** The `interim` policy moves no value (builder docstring; round 89 record). `--yahoo-active-policy blank` is never applied (call `3adb` (a); the builder refuses it under `--apply`).

## 4. Counts (from the round-97 record; the labels reconcile to the price file)

| table | rows | `use_class` NOT_YAHOO | NOT_FOR_ACTIVE | INACTIVE_USE | `porting_verdict` NOT_YAHOO / UNVERIFIED |
|---|---|---|---|---|---|
| daily_returns | 1,691,729 | 1,022,467 | 667,974 | 1,288 | 1,022,467 / 669,262 |
| account_day_value | 21,102,041 | 17,392,999 | 3,688,916 | 20,126 | 17,392,999 / 3,709,042 |
| month_grades | 82,593 | 49,376 | 33,150 | 67 | 49,376 / 33,217 |

- Accounts with a NOT_FOR_ACTIVE `account_day_value` row: 729.
- The labelled `account_day_value` rows (3,709,042) equal the priced, non-cash rows whose (cusip, date) point names `yahoo_finance` or `linear_interpolation` in the regrade's per-point price file (issuer re-run of `deliverables/2.0.0_SA_COO~C1/cs1_ac2_label_check.py`: 3,709,042 = 3,709,042). The same count was `UNVERIFIED` in round 83's measure under the wide rule.
- The CTO's 1,049,193 is a count of ticker-day POINTS replaced by the as-traded basis (price input: 1,049,193 `yahoo_finance` + 477,980 re-derived `linear_interpolation`). The tables label account-days and holding-days, so their counts cannot equal it. The price file holds 1,325,110 `yahoo_finance` and 705,133 `linear_interpolation` (cusip, date) points; the label marks every Yahoo-sourced point, replaced or original, because the price file carries no substitution flag. Not established: which served days used a replaced point.
- `porting_verdict` reads UNVERIFIED on every Yahoo-labelled row: the Yahoo index carries no verdict column yet (`commonwealth_price_need.py`, the documented state today).

## 5. Conditions

- The applier is named by the CTO; it opens a change-management ledger entry at the start and closes it at completion (NEVER-2), and prints the three content hashes it applies.
- The applier re-reads the three prior versions in section 1 immediately before the first put and STOPS on any difference; it runs `--dry-run` and then `--apply --overwrite` against `.scratch/cotbkf_r97/build/`, never `--build`.
- The reader gate stays as section 1 reads it (no served reader); the CVO grades the labelled served tables after the write. The labelled days stay labelled interim until Bloomberg replaces them.
- Nothing about a client account, name or dollar value is written to a record, a message or a commit.
- The CTO half is signed against the same section-1 versions and section-3 hashes. An unmeasured change to the build directory, the keys or the builder between this signing and the apply voids this half.
