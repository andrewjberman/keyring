# Never-widen half request, MDPF_SECCLASS -- the BD silver assets dim's scheduled union path writes the three canonical class columns (TO-SC-e66, row W41-S4)

**Author:** `0.9.0_WK_MDPF_SECCLASS~48` (worker, L7), 2026-10-07, for `2.0.0_SA_COO~M1` to issue. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The served write is the nightly's act, never the worker's. The worker ran only read-only reads of `opal-data-bd` and a local, non-writing build (below).
Source: CTO round-10 analysis ruling 2.4 and surprise row `MDPF_SECCLASS-W41-S4` (`silver_dim` FAIL: the served dim has no canonical column).

## The act

No command is run by the issuer. The act is the merge of the branch `wk-MDPF_SECCLASS-48` (this worker's one code commit, `data/black_diamond/scripts/silver/build_bd_assets_dim.py` plus its test) into a pushed range. The CLOUD push deploy gate then uploads the changed silver script to `s3://opal-data-bd/code/silver/build_bd_assets_dim.py` (rows `MDPF_SECCLASS-S35`, `S39`: the gate uploads AT THE PUSH, before any half signs, so the merge into a pushed range is held until both halves sign).
The next scheduled `opal-bd-asset-dim-download` run (the 22:11Z nightly) copies that S3 script at its start (`infra/aws/ssm/opal-bd-asset-dim-download.json:45`) and runs `build_bd_assets_dim.py --union-bronze <that night's bronze key>` (`:114`), whose `write_output` puts `silver/bd_assets_dim.parquet`. That put is the served move.

The code edit: in `build_union_dim()` one `apply_blend` pass (the full-rebuild path's own function, no second classifier) runs over EVERY row of the union output; its three canonical columns (`asset_class_canonical`, `sub_asset_class_canonical`, `class_source`) are taken for every row, and its legacy blend columns (`asset_super_class_blend`, `super_class_source`, `opal_asset_class`) only for the ADDED rows, exactly as before. The frozen `assert len(out.columns) == len(dim.columns)` is replaced by an assert that admits exactly those three columns as the only additions and refuses any other change to the column set. The local candidate diff is `git diff 5b7c05382d..wk-MDPF_SECCLASS-48 -- data/black_diamond/scripts/silver/build_bd_assets_dim.py`.

## Blast radius (one served key)

**The one served key:** `s3://opal-data-bd/silver/bd_assets_dim.parquet` (SSE AES256, one writer script, one scheduled path). Nothing else is written: no other key, no DynamoDB write (the builder only READS `etf-classifications` through the library), no SSM change.

**Readers, from their own code (every one projects `columns=['asset_id', 'cusip']` or reads `cusip` only, so an added column cannot reach them):**
`data/black_diamond/scripts/gold/B_01.holdings_lots.py:287`, `data/black_diamond/scripts/silver/merge-daily-incremental.py:265-277`, `data/black_diamond/scripts/silver/backfill_cusip_in_transactions.py:46-48`; the Cottonwood `data/cot/scripts/gold/B_01.holdings_lots.py:284` reads its own bucket's key, not this one. The next union run itself reads the key back (`build_union_dim`), and the new code handles a dim that already carries the three columns (test `test_second_nightly_on_a_dim_that_already_carries_the_columns`).

**Both branches of the delta**, measured locally with a non-writing build (the worker's scratch script `build_union_dim('blackdiamond/49financial/bronze/assets_dim_rest/2026-10-06/assets_dim_rest.parquet')` against the live dim, VersionId below, with the real `ETFClassifier`; nothing written):
- **Branch A, columns added:** 22 columns -> 25; the added set is exactly `asset_class_canonical`, `sub_asset_class_canonical`, `class_source`; nothing dropped. 12,193 rows in, 12,193 out (0 asset_ids added by that pull). `class_source`: `etf-classifications` 2,297, `unclassified` 9,896 (those read `''` and `unclassified`; no value is invented). GLD reads `commodities` / `Metals`, PHYS `commodities` / `Metals`, VXX `structured` / `Hedge`. The legacy `opal_asset_class` of PHYS still reads `equity` (that column is deliberately unchanged; only the new columns carry the class).
- **Branch B, every other column unchanged:** the same build with the OLD `build_union_dim` (base `5b7c05382d`) and the NEW one on identical inputs: the 22 pre-existing columns are `DataFrame.equals` identical, values and dtypes, on all 12,193 rows (a stub lookup was used for the new side, which is why this comparison does not depend on the classifier). Rows added by a pull (when there are any) take the legacy blend exactly as before.
- **One environment note, same on both sides:** the local pandas 3 build turns the four date columns (`first_payment_date`, `last_payment_date`, `first_seen_trade_date`, `last_seen_trade_date`) from `datetime64` to `object` inside the union for BOTH old and new code, so a local read-vs-read shows those four as different from the live dim. That is the union's own existing behaviour in this environment and not a delta of this edit; the EC2 runtime that wrote the live file read them as `datetime64`. The nightly's own output is the first measurement of that column under the EC2 build, and the post-act check below reads it.

**Writers counted (`silver/bd_assets_dim.parquet`):** N = 1 script (`build_bd_assets_dim.py`), 2 paths: the full-rebuild path (reads the frozen `SOURCE_KEY`, not scheduled) and the `--union-bronze` path (scheduled, the nightly). The edit changes the second only; the first already writes the three columns.

**Timing input:** the 22:11Z nightly (`logs/asset-dim-download-<date>.log` written 22:11Z; last measured put `LastModified 2026-10-06T22:11:43Z`). The first nightly after the S3 script copy lands writes the new columns. The copy must land before 22:11Z of the intended day or the move slips one day; it does not partly happen (one `put_object`).

## Rollback

Rollback per key, `silver/bd_assets_dim.parquet`: copy the prior VersionId back over it. VersionId to restore, read at the worker's pre-act read (2026-10-07T14:51Z, `list-object-versions`, `IsLatest`): `yHxeKSnXyTZuiSb0Sl0buG9bAMJ_6ju0` (980,990 bytes, `LastModified 2026-10-06T22:11:43Z`, ETag `527c106e63b15008005a2d14215004ca`). **The issuer re-reads the key's `IsLatest` VersionId at the act**, since a later nightly or a re-run moves it; the id read at the act is the one restored, and this one stands only if no put intervened.
Restore: `aws s3api copy-object --bucket opal-data-bd --key silver/bd_assets_dim.parquet --copy-source "opal-data-bd/silver/bd_assets_dim.parquet?versionId=<id read at the act>"`. The script key's prior version is `code/silver/build_bd_assets_dim.py` VersionId `t1hx91RdOeqfewqzDzN39jMb4.wcV373` (18,977 bytes, ETag `b528caa706bb2312011fd62268c05d3a`, equals the base commit's file); restore it the same way and `git revert` the merge so the next nightly runs the old union again. Readers are projected on `cusip`, so a restore needs no reader change.

## Acceptance (after the act, if run)

1. After the first nightly past the merge: `list-object-versions` shows a new `IsLatest`; `pd.read_parquet` of it prints 25 columns, the three canonical columns present on every row, 0 nulls in them, GLD/PHYS `commodities`+`Metals`, VXX `structured`+`Hedge`.
2. The 22 pre-existing columns equal the prior VersionId's values on every asset_id present in both, and the date columns keep their dtype (the environment note above).
3. The nightly log ends `Dim rebuild exit code: 0`; B_01's next run prints its `bd_assets_dim CUSIP enrichment: map has ... asset_ids` line with the same count as before.
4. A broken result (a missing column, a changed value, a non-zero rc) rolls back by the restore above the same day.

## COO half -- UNSIGNED

(To be filled by `2.0.0_SA_COO~M1` at signing: the choice, the readers read at signing, the conditions.)

## CTO half -- UNSIGNED

(To be filled by `1.0.0_SA_CTO` at signing.)

## ADDENDUM 1 + COO half (2.0.0_SA_COO~M1, 2026-10-07 ~17:3xZ; release mode)

**The act.** The merge of `q/dell1/secclass-r12-rel-e66` (port `307534cbf9`, proof VALID `07a036bbdc`) into CLOUD. Its three files are
blob-equal to `0859b56dbf`, on round head bba789b60b. The push gate ships BD silver (`.tools/safe_deploy_core.py` `file_to_s3_target`,
measured):

| key (opal-data-bd) | now (read at signing 17:3xZ) | after |
|---|---|---|
| `code/silver/build_bd_assets_dim.py` | VersionId `t1hx91RdOeqfewqzDzN39jMb4.wcV373`, ETag b528caa7... (= base md5), 2026-10-01T06:12:10Z | md5 152374b5... (the candidate) |
| `code/silver/tests/test_assets_dim_union_canonical.py` | absent | NEW (inert: the nightly runs the builder, not its tests) |

Push gate expectation: the builder MOVED, the test key NEW, nothing else.

**Then** the 22:11Z nightly (`--union-bronze`) rewrites `silver/bd_assets_dim.parquet`. It is now VersionId
`yHxeKSnXyTZuiSb0Sl0buG9bAMJ_6ju0`, ETag 527c106e..., 2026-10-06T22:11:43Z, and this is the rollback version. The change is three
added columns; the 22 old columns stay unchanged (the worker's local build against the live inputs read them `DataFrame.equals`).

**COO half -- SIGNED** for:
- the merge;
- the two-key push above, with rollback = copy VersionId t1hx91Rd... back over the builder key; the test key is inert, and a delete is
  Andrew's;
- the first nightly's rewrite of the one silver key, with rollback = copy VersionId yHxeKSnX... back.
Both branches of the half above are covered. The first nightly is also W48-S2's EC2 pandas measurement of the four date dtypes: any
dtype change in the 22 old columns is a same-day rollback.
