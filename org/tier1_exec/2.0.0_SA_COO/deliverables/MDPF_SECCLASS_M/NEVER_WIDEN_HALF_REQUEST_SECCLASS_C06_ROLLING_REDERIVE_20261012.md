# Never-widen half request, MDPF_SECCLASS -- C_06 re-derives B_00's correction window on every fire (FWD-1, cell SC-e-97, rows MDPF_SECCLASS-D1-W83-S5 and MDPF_SECCLASS-D1-W80-S4)

**Author:** `0.9.0_WK_MDPF_SECCLASS~86` for `2.0.0_SA_COO~M1`, 2026-10-12. **For:** `2.0.0_SA_COO~M1` (COO half) and `1.0.0_SA_CTO` (CTO half).
**Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed. The build is LOCAL on worktree branch `wk-MDPF_SECCLASS-86` (not pushed). Every figure below is read-only: `head-object`, `get-object`, `list-objects-v2`, `describe-instances`, and one dry-run of the build with every write skipped. Security-level and aggregate figures only; no relationship id, account id or client name appears here.

## The act

1. Open a change-management ledger in `org/critical_paths/change_management/` before the act; close it at completion.
2. A CloudOps lane deploys TWO code keys to `s3://opal-data-bd/code/gold/`, outside a BD gold run and before the next nightly fire: `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` and `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`, by `bash .tools/safe-deploy.sh <file>` for each. The new test file `tests/test_c06_rolling_rederive_r23.py` is not deployed (the deploy core ships named code files only).
3. Precondition, read by head-object on 2026-10-12 (see Rollback): the served C_06 object is VersionId `zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT`, ETag `2e35d043163cc18b135d7698cf11dc56`, and the served D_04 object is VersionId `ap.CyBT8aJijz5kWFsSNjEFU99itbXED`, ETag `9d083669159ee8875b6489dea4fb2e37`. The deploy delta is exactly the diff of the two files against the base they were cut from.
4. The lib (`lib/etf_classifier.py`), D_03, B_00 and the SC-e-91 retained pass body are NOT in this act. The retained pass is called as before; its helpers `_write_mix_summary` and `_read_mix_summary_strict` gained a carried `restated_through` (see Blast radius).
5. Read back after the first post-ship fire: `platinum/firm/mix_summary.json` `mix` Unclassified at `as_of` 2026-10-09, and `restated_through` (expected `2026-09-25`), beside the pre-act values in Rollback.

## Blast radius

**What the act writes:** two code objects. Nothing else.

**What the next fire writes.** The fire is the nightly B_00-then-C_06 run. Its window is B_00's own 15 dates, 2026-09-25 to 2026-10-09 (Window and gap). Read from the dry run and from the SC-e-96 scan, which agree:
- Relationship JSONs `gold/entities/clients/{id}.json` and their legacy copies `gold/client_timeseries/{id}.json`, and the period views `{id}_views.json` and their legacy copies: ONLY where a window date's stored entry differs from the re-derive, or a stored window date has no partition entry. **3,274 relationship JSONs rewritten of 3,793 read; 13,096 keys (four per rewritten relationship); 8,870,708,106 payload bytes** (SC-e-96 scan, the sizes of the bodies the writes carry, legacy copies included). The dry run measured the same 3,274 rewrites and 13,096 keys.
- `gold/views/mix_daily_summary.json`: rewritten on every window fire that changes a day (its whole content, 2,293 firm days and 56 advisors in the dry run's summary).
- D_03's outputs `gold/artifacts/firm_mix_views.json`, `gold/artifacts/firm_mix_views_daily.json`, and the advisor `gold/entities/advisors/{id}/mix.json`, `mix_daily.json`, `mix_timeseries.json` (D_03.composition_artifacts.py, `_publish_mix_views`, its docstring at :470-480).
- D_04's `platinum/firm/mix_summary.json` (D_04.client_portal_summary.py `build_firm_mix_summary`).
- The watermark is re-put with the same value (`2026-10-09`).

**Every served object that embeds a window date's firm or advisor class dollars** (read from the code; magnitudes from the SC-e-96 record where it has them):
- **D_03 firm daily accumulator** `gold/artifacts/firm_mix_views_daily.json`: the whole firm daily map is written, so all 15 window days are reached. Per-date change: the "served minus rebuilt" column below.
- **D_03 quarterly and monthly period bars and annual bar** (`lib/mix_views.py:66-80`): each period's bar takes the LAST date present in the daily map for that period (`period_map[pk]` is overwritten in sorted order). The window reaches four bars: the Q3 2026 and September 2026 bars (end date 2026-09-30) and the Q4 2026 and October 2026 bars plus the 2026 annual bar (end date 2026-10-09). The bar's `unclassified` row is the residual `total_aua` at the end date minus the classified sum (`lib/mix_views.py:99-107`), so the restated class dollars of the end-date day move that residual. Inferred from the code: the bar's unclassified moves by about the end-date day's delta, scaled by `total_aua` over the cube total. The `total_aua` and cube totals for those days are not in the record and are not measured here.
- **D_04 `platinum/firm/mix_summary.json`, `mix`** (the snapshot at the latest date, 2026-10-09): reached. Served Unclassified (D_04's rule) moves by the 10-09 delta in the table below, measured from the record.
- **D_04 `platinum/firm/mix_summary.json`, `mix_periods`** (the last five quarterly bars): reached through the Q3 and Q4 2026 bars above. Inferred from the code.
- **D_04 `platinum/firm/mix_summary.json`, `composition.mix`** (C_06 class market values of the latest date overwrite the donut's classes): reached; the class-level change is not in the record and is not measured here.
- **Advisor summaries** (D_03 `mix.json`, `mix_daily.json`, `mix_timeseries.json`): each advisor's window days are replaced whole. Reached for every advisor with a window-date entry. The per-advisor magnitude is NOT in the record (the record is firm-level) and is not measured here.

**Per-date movement, from the record** (`WINDOW_READ_C06_ROLLING_20261012.json`, read at 2026-10-12 over the 15 window partitions and the served `gold/views/mix_daily_summary.json`). Served = D_04's rule (`D_04.client_portal_summary.py:440-462`, total minus the canonical classes present); rebuilt = the sum over relationships of `mix['unclassified'] * total_mv` from the re-derive; served minus rebuilt is the fall in the served figure (it equals rebuilt minus served with the sign reversed, the record's `delta_unclassified`); the two orphan columns are the relationship counts that the stored JSONs and the partition disagree on:

| date | served (D_04 rule) | rebuilt | served minus rebuilt | stored not in partition | in partition not stored | key present | key minus remainder |
|---|---:|---:|---:|---:|---:|---|---:|
| 2026-09-25 | 42.50 | 10,153.33 | -10,110.83 | 10 | 18 | no |  |
| 2026-09-26 | 24.94 | 10,142.73 | -10,117.79 | 10 | 172 | no |  |
| 2026-09-27 | 21.86 | 10,132.10 | -10,110.25 | 10 | 172 | no |  |
| 2026-09-28 | 73.19 | 10,121.46 | -10,048.26 | 9 | 205 | no |  |
| 2026-09-29 | -42.04 | 10,110.82 | -10,152.86 | 10 | 68 | no |  |
| 2026-09-30 | 76,259,877.65 | 53,010.45 | 76,206,867.21 | 9 | 62 | yes | 96.20 |
| 2026-10-01 | 75,964,048.04 | 43,081.20 | 75,920,966.85 | 14 | 67 | yes | -7.87 |
| 2026-10-02 | 150,433,862.60 | 1,924.34 | 150,431,938.26 | 14 | 25 | yes | -184.61 |
| 2026-10-03 | 152,418,257.84 | 1,927.10 | 152,416,330.74 | 15 | 18 | yes | -6,480,424.81 |
| 2026-10-04 | 152,995,165.84 | 1,929.87 | 152,993,235.97 | 15 | 18 | yes | -6,488,756.24 |
| 2026-10-05 | 148,224,563.78 | 0.00 | 148,224,563.78 | 15 | 18 | yes | -6,502,294.55 |
| 2026-10-06 | 140,161,790.57 | 0.00 | 140,161,790.57 | 11 | 17 | yes | 4.71 |
| 2026-10-07 | 998,762.85 | 32,455.34 | 966,307.51 | 8 | 16 | yes | -128.06 |
| 2026-10-08 | 972,621.40 | 8,030.41 | 964,590.99 | 1 | 0 | yes | 128.57 |
| 2026-10-09 | 1,846,332.73 | 883,483.05 | 962,849.68 | 0 | 0 | yes | 66.73 |

The "key minus remainder" column compares `firm[date].unclassified`, where the day carries the key (ten dates, 2026-09-30 to 2026-10-09), with the D_04 remainder. They agree to the cent on none of the ten dates. On 2026-10-03 to 2026-10-05 the key is about $6.5M below the remainder. The served Unclassified on those three days is therefore the remainder, not the key.

**Memory (measured or inferred, marked per figure).**
- Total bytes of the 15 window partitions: 35,972,189 (head-object ContentLength, 2026-10-12). Measured.
- In-memory size of one partition after `pd.read_parquet` (2026-10-09: 114,554 rows, 10 columns; parquet 2,370,862 bytes): 18.4 MB (`memory_usage(deep=True)`). Measured.
- Preload resident size, estimated as one partition times 15: about 276 MB. Inferred (linear in partitions; the build bulk-loads the window and any new partitions into `cube_cache`, `C_06.client_mix_timeseries.py:845-863` at base 028fab8273; the same block is unchanged in the new build).
- Runner: `i-01003b035d2988dfb`, instance type `r6i.4xlarge`, state `stopped`, no launch template. Measured by read-only `ec2 describe-instances`. Its memory of 128 GiB is inferred from the instance type's published size; the tool did not return it.
- 276 MB against 128 GiB is about 0.2 percent, below the 70 percent threshold. Inferred. No build change is made for memory.
- SC-e-95 measured a process peak of 3.26 to 3.30 GB for N = 1 to 5 including the static load (`RESIDUAL_READ_C06_FREEZE_20261012.json`). Cited, not re-measured.
- The SC-e-96 scan process peaked at 635.6 MB (`peak_mb`, psutil peak working set, scan process only). Measured.
- The dry run of the new build from this seat completed in 752.7 s with every write skipped. Its peak was not measured.

**Relationship JSON reads per fire** (measured in the dry run, which reads the live stored JSONs):
- A fire with new partitions: 3,793 reads (3,267 by the merge for relationships in the window and new partitions, plus 526 by the orphan visit for the rest). The SC-e-91 retained-date pass does not run on such a fire, as before.
- A window-only fire (no new partition, the nightly case after the watermark): 3,793 reads by the merge and orphan visit, plus 3,793 by the SC-e-91 retained-date pass, which still runs on every fire that builds no new date. 7,586 in all.
- The dry run's SC-e-91 pass reports 796 rewrites and 5,907 holdings moved. It reads the STORED pre-window JSONs (a dry run writes nothing), so those counts are a stored-state artifact of the dry run, not a live-fire count. Not measured live.

**Not touched:** `etf-classifications` (read only), the lib, `B_00`, `D_03`, every ticker and relationship outside the window partitions, the watermark value, every in-window entry whose stored value already equals the re-derive (byte-identical; not rewritten).

## Writers

**Writers of the served `platinum/firm/mix_summary.json`: N = 1.**
- `data/black_diamond/scripts/gold/D_04.client_portal_summary.py:578` -- `_write_batch([(summary, 'platinum/firm/mix_summary.json')], ...)` in `build_firm_mix_summary` (:468). The put is `_write_json_to_s3` (:268-279, `s3.put_object` at :273), reached through `_write_batch` (:296). Other hits are docstrings only (:11, :470, :478).

**Writers of `gold/views/mix_daily_summary.json`: N = 1.**
- `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:679` -- `s3.put_object(... MIX_DAILY_SUMMARY ...)` in `_write_mix_summary` (:669). Called at :1024 (the SC-e-91 retained-date pass) and :1365 (the build). Readers: `D_03.composition_artifacts.py:484`, `D_04.client_portal_summary.py:486`.

**Writers of the relationship JSONs `gold/entities/clients/{id}.json` (and the legacy copies): N = 1 function, 4 call sites.**
- `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:597` -- `_write_relationship_json`, puts at :602 and :608. Call sites: :539 (the new window orphan visit, `_window_orphan_pass`), :987 (the SC-e-91 retained-date pass), :1170 (the merge), :1303 (the full build).
- The subdirectory keys `gold/entities/clients/{id}/detail.json` and `.../aua_timeseries.json` are written by `D_02.advisor_client_detail.py` (:2183, :2862). They are different keys and are not counted here.

## Both branches

1. **A window date whose partition differs from the stored entry.** `restate_window` replaces the date's mix and concentration entries with the re-derive. The relationship JSON and its views are rewritten. Counted in the 3,274.
2. **A window date whose partition is unchanged.** The re-derived entry equals the stored one, so `restate_window` changes nothing and the relationship is not rewritten (`_merge_and_write` returns before any write when no entry changed). Inferred from the idempotence test (`test_second_identical_call_changes_nothing`); not measured against live writes.
3. **A relationship absent from the partition on a window date.** `restate_window` removes the stored entry for that date (the orphan case). The SC-e-96 record shows the stored-but-not-in-partition count above zero on 14 of 15 dates (up to 15 relationships a date). The orphan visit reads every stored JSON the merge did not visit (526 in the dry run).
4. **A date outside the window.** Byte-identical: `restate_window` never touches a date not in its window (`test_date_outside_the_window_is_byte_identical`). The SC-e-91 retained pass body is unchanged.
5. **The rule unreadable.** `producer_force_recent_days` returns None, the build prints `C06-ROLLING-RULE-UNREADABLE`, re-derives nothing, runs no orphan visit, carries the stored `restated_through`, and writes every visited relationship as before. Not exercised live.
6. **The security-level list that stays Unclassified because no classifier places it.** SC-e-98's record `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json` was NOT on disk at this read (2026-10-12), so no list is stated here.
7. **The sibling file absent or unreadable.** `producer_force_recent_days` returns None; the build re-derives nothing, runs no orphan visit, and writes every visited relationship as before. The window is not typed as 14 in its place; the build is a no-op for the window. Tested: `test_rule_absent_sibling_is_none_and_never_a_typed_window` and `test_rule_unreadable_sibling_is_none`. Not exercised live.

## Rollback

Read by head-object on 2026-10-12, before the act:

| key | VersionId | ETag | LastModified | size | role |
|---|---|---|---|---:|---|
| `code/gold/C_06.client_mix_timeseries.py` | `zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT` | `2e35d043163cc18b135d7698cf11dc56` | 2026-10-12T09:55:03Z | 55078 | prior served C_06; **the rollback target** (the order's cited ETag and VersionId match) |
| `code/gold/D_04.client_portal_summary.py` | `ap.CyBT8aJijz5kWFsSNjEFU99itbXED` | `9d083669159ee8875b6489dea4fb2e37` | 2026-10-12T06:18:41Z | 166009 | prior served D_04; **the rollback target** |
| `gold/views/mix_daily_summary.json` | `VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD` | `c51968d1d37d3cb078095360d3347d30` | 2026-10-11T05:23:28Z | 9877189 | pre-act; **restore target** if a fire's day dollars are wrong |
| `platinum/firm/mix_summary.json` | `_MTtBmpPHKvL3Hvt58tzeIsshH4c_lxb` | `b8ffd506d117c94249592968011e43a0` | 2026-10-12T05:44:00Z | 25124 | pre-act; **restore target** after a D_04 re-run |

- Code rollback: `s3api get-object --version-id <VersionId>` for each code key, then `safe-deploy.sh` of that file. This restores today's behaviour.
- Data rollback for the relationship JSONs and views: the ship's pre-act read records the VersionIds of every key the first fire rewrites (3,274 relationship JSONs, 13,096 keys, per the SC-e-96 scan). This file does not list them; that read is the ship's, not this request's.
- The 15 window partitions are read-only inputs to this act and are not rewritten by it.

## Expected outcome

Read from the rule, not typed from the input:
- After the first post-ship fire, for every date in the window, the served firm class dollars equal an independent rebuild from the then-current partitions, within the rounding the code carries. The rounding is six places per relationship mix, measured at up to $128.58 per firm snapshot (row MDPF_SECCLASS-D1-W85-S6, served 2026-10-08).
- At 2026-10-09 the served Unclassified by D_04's rule is $1,846,332.73 before the act (the SC-e-96 record); the rebuilt value is $883,483.05 at the 2026-10-12 read. Served minus rebuilt is +$962,849.68: if no canonical byte moves, the served figure falls by that amount to the rebuilt value within rounding. The same magnitude expressed as rebuilt minus served (the record's `delta_unclassified`) is -$962,849.68. Against the stored key (`firm[2026-10-09].unclassified` = $1,846,399.46) served-key minus rebuilt is +$962,916.42 at full precision (+$962,916.41 from the two-decimal figures shown).
- The per-date "served minus rebuilt" column above is the expected fall in the served figure for each window date, if no canonical byte moves.

## Window and gap

- **N = 14**, read from `data/black_diamond/scripts/gold/gold_dispatch.sh:99` (`B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14`). The runtime source is the sibling file `gold_dispatch.sh` in the directory of C_06 (`Path(__file__).resolve().parent / 'gold_dispatch.sh'`, C_06 `_read_dispatch_text`). The runner's `sync_scripts` (`gold_dispatch.sh:672-674`; scripts directory `:78`) materializes it flat beside the gold scripts before C_06 runs. The rule has NO S3 fallback. If the file is absent or unreadable, `producer_force_recent_days` returns None: the build is a no-op for the window (it prints `C06-ROLLING-RULE-UNREADABLE` and behaves as today), never a typed 14.
- **The window is 15 dates, 2026-09-25 to 2026-10-09** (anchor 2026-10-09, cutoff 2026-09-25, inclusive), from 2,474 canonical partitions.
- **Cap: none.** `fits` is true (cold 735.05 s against 1,800 s), and `largest_n_that_fits` is 15 of 15. No `ROLLING_MAX_DATES` constant is added.
- **Gap if truncated** (`gap_if_truncated`, the dollars left wrong on the dates NOT re-derived): newest 1 date = $898,337,131.86; newest 5 dates = $608,019,879.02; all 15 dates = $0.00. Non-increasing; zero at the full window.

COO half: UNSIGNED
CTO half: UNSIGNED
