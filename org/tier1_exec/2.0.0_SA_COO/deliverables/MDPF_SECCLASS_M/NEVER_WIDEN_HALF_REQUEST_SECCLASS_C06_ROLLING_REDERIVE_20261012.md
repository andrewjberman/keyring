# Never-widen half request, MDPF_SECCLASS -- C_06 re-derives B_00's correction window on every fire (FWD-1, cell SC-e-97, rows MDPF_SECCLASS-D1-W83-S5 and MDPF_SECCLASS-D1-W80-S4)

**Author:** `0.9.0_WK_MDPF_SECCLASS~86` for `2.0.0_SA_COO~M1`, 2026-10-12. **For:** `2.0.0_SA_COO~M1` (COO half) and `1.0.0_SA_CTO` (CTO half).
**Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed. The build is LOCAL on worktree branch `wk-MDPF_SECCLASS-86` (not pushed). Every figure below is read-only: `head-object`, `get-object`, `list-objects-v2`, `describe-instances`, and the build's dry run with every write skipped (run again for Amendment 3, with the two writer functions wrapped to capture their arguments), plus list-object-versions and get-object by VersionId for the last five served versions of `gold/views/mix_daily_summary.json`. Security-level and aggregate figures; opaque relationship ids appear only in the section Added and dropped relationships, where Amendment 3 asks for them. No account id or client name appears here.

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
- **D_03 quarterly and monthly period bars and annual bar** (`lib/mix_views.py:66-80`): each period's bar takes the LAST date present in the daily map for that period (`period_map[pk]` is overwritten in sorted order). The window reaches four bars: the Q3 2026 and September 2026 bars (end date 2026-09-30) and the Q4 2026 and October 2026 bars plus the 2026 annual bar (end date 2026-10-09). The bar's `unclassified` row is the residual `total_aua` at the end date minus the classified sum (`lib/mix_views.py:99-107`), so the restated class dollars of the end-date day move that residual. Measured in the section Period bars: the Q3 2026 and September 2026 bars' Unclassified falls by $82,391,488.82 (from $82,444,446.18 to $52,957.36), and the Q4 2026, October 2026 and 2026 annual bars' Unclassified falls by $962,919.40. Each bar total is the client_performance AUA at its end date and does not move.
- **D_04 `platinum/firm/mix_summary.json`, `mix`** (the snapshot at the latest date, 2026-10-09): reached. Served Unclassified (D_04's rule) moves by the 10-09 delta in the table below, measured from the record.
- **D_04 `platinum/firm/mix_summary.json`, `mix_periods`** (the last five quarterly bars): reached through the Q3 and Q4 2026 bars above. Measured in the section Period bars.
- **D_04 `platinum/firm/mix_summary.json`, `composition.mix`** (C_06 class market values of the latest date overwrite the donut's classes): reached; measured on the 2026-10-09 snapshot: equity +$876,265.04 and fixed income +$86,654.36 in raw firm class dollars, the other classes unchanged (sections Totals and AUA and Period bars).
- **Advisor summaries** (D_03 `mix.json`, `mix_daily.json`, `mix_timeseries.json`): each advisor's window days are replaced whole. Reached for every advisor with a window-date entry. Measured in the section Advisors the map drops: 502 of 840 advisor-days move, with the per-date counts and the ten largest moves; part of the advisor movement is re-attribution under the current lookup (row MDPF_SECCLASS-D1-W86-S8).

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

The "key minus remainder" column compares `firm[date].unclassified`, where the day carries the key (ten dates, 2026-09-30 to 2026-10-09), with the D_04 remainder. They agree to the cent on none of the ten dates. On 2026-10-03 to 2026-10-05 the key is about $6.5M below the remainder. The served Unclassified on those three days is therefore the remainder, not the key. The rebuilt column above is the record's per-relationship sum; the D_04 rule on the would-be firm snapshot gives $883,413.33 on 2026-10-09 (section Totals and AUA), and the stored Unclassified key gives $883,483.05 (row MDPF_SECCLASS-D1-W86-S10).

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
6. **The security-level list that stays Unclassified because no classifier places it.** SC-e-98's record `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNLISTED_UNCLASSIFIED_20261009_BY_SECURITY_20261012.json` is on disk at this read (2026-10-12) and is read here: 32 securities, rebuilt 2026-10-09 Unclassified $883,483.05 (the securities sum to $883,521.92, within the record's $51.91 tolerance). 22 securities (22 positions, $210,486.42) sit outside every stored top-10 list, and 10 are listed in one. Reason codes: name-not-in-feed 26 securities ($871,922.68), cusip-carries-no-ticker 5 ($4,005.24), ticker-has-no-row 1 ($7,594.00). No security name is printed here.
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
- At 2026-10-09 the served Unclassified by D_04's rule is $1,846,332.73 before the act (the SC-e-96 record). Measured on the would-be firm snapshot (section Totals and AUA), the D_04 rule gives $883,413.33 after the act, so the served figure falls by $962,919.40 to that value if no canonical byte moves. The stored firm Unclassified key is $1,846,399.46 served and $883,483.05 rebuilt (the per-relationship sum that the SC-e-98 record also carries), a fall of $962,916.42. The $69.72 between the rule and the key is row MDPF_SECCLASS-D1-W86-S10. The earlier figure of -$962,849.68 used the record's per-relationship sum against the D_04 remainder and is superseded for the served D_04 figure.
- The per-date "served minus rebuilt" column above is the expected fall in the served figure for each window date, if no canonical byte moves.

## Window and gap

- **N = 14**, read from `data/black_diamond/scripts/gold/gold_dispatch.sh:99` (`B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14`). The runtime source is the sibling file `gold_dispatch.sh` in the directory of C_06 (`Path(__file__).resolve().parent / 'gold_dispatch.sh'`, C_06 `_read_dispatch_text`). The runner's `sync_scripts` (`gold_dispatch.sh:672-674`; scripts directory `:78`) materializes it flat beside the gold scripts before C_06 runs. The rule has NO S3 fallback. If the file is absent or unreadable, `producer_force_recent_days` returns None: the build is a no-op for the window (it prints `C06-ROLLING-RULE-UNREADABLE` and behaves as today), never a typed 14.
- **The window is 15 dates, 2026-09-25 to 2026-10-09** (anchor 2026-10-09, cutoff 2026-09-25, inclusive), from 2,474 canonical partitions.
- **Cap: none.** `fits` is true (cold 735.05 s against 1,800 s), and `largest_n_that_fits` is 15 of 15. No `ROLLING_MAX_DATES` constant is added.
- **Gap if truncated** (`gap_if_truncated`, the dollars left wrong on the dates NOT re-derived): newest 1 date = $898,337,131.86; newest 5 dates = $608,019,879.02; all 15 dates = $0.00. Non-increasing; zero at the full window.

## Totals and AUA

Plain reading. On 14 of the 15 window dates the firm total a partner sees would move, and on 2026-10-09 it holds at $2,015,391,646.72. Up on 2026-09-25 by $32.1 million; on 09-26 to 09-28 by $224 million, $224 million and $247 million; on 09-29 by $156.4 million; on 09-30 and 10-01 by $149.5 million and $150.3 million; on 10-02 by $28.2 million; on 10-03 and 10-04 by $5,204 and $48,507. Down on 10-05 to 10-08 by $1.8 million, $1.3 million, $1.5 million and $1.9 million. The AUA does not move on any date: it is client_performance, which the act does not write, and the period bars carry it as their total, so the bar totals at 2026-09-30 ($1,992,588,179.03) and 2026-10-09 ($2,015,391,646.72) are the same before and after. After the act the firm total equals that AUA to the cent on all 15 dates. What moves on the page is the class split of the bars: Unclassified on the Q3 and September 2026 bars falls from $82.44 million to $0.05 million, and Structured rises by $87.55 million (Period bars). The 2026-10-09 served Unclassified (D_04 rule) falls by $962,919.40.

Sources. Served firm total: `gold/views/mix_daily_summary.json` VersionId `VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD` (LastModified 2026-10-11T05:23:28Z, ETag c51968d1, read by get-object and MD5-checked against the ETag; `firm[date].total`). Rebuilt firm total: the would-be summary the build writes, captured from the build's own dry run (`C_06.client_mix_timeseries.py` `_write_mix_summary`, the main call with `restated_through`; the dry run wrote nothing). AUA: `gold/timeseries/client_performance.parquet` VersionId `0Dx5uzxSXleuqe6zrNpwhdLAb4VZnmfK` (LastModified 2026-10-12T05:18:33Z), `total_aua` summed by date, the input D_03 reads at `D_03.composition_artifacts.py:497-503` and passes as `cp_daily_total` at :523. The served AUA is on the page as a period bar's `total_aua` only where the date is a period end (`lib/mix_views.py:82-84`): 2026-09-30 and 2026-10-09 here. On the other 13 dates the figure shown is the value the same function would use if that date were a period end. The served bars were reproduced from the served summary by the lib function (control: `compute_period_views(served, cp)` equals the served `firm_mix_views.json`, every bar).

| date | served firm total | rebuilt firm total | firm total move | AUA (client_performance) | AUA after the act | AUA move | rebuilt minus AUA |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-09-25 | 1,955,227,870.36 | 1,987,307,868.35 | +32,079,997.98 (up) | 1,987,307,868.35 | 1,987,307,868.35 | 0.00 | -0.0000 |
| 2026-09-26 | 1,759,693,087.06 | 1,983,735,060.18 | +224,041,973.12 (up) | 1,983,735,060.18 | 1,983,735,060.18 | 0.00 | -0.0000 |
| 2026-09-27 | 1,756,350,143.06 | 1,980,162,252.01 | +223,812,108.95 (up) | 1,980,162,252.01 | 1,980,162,252.01 | 0.00 | +0.0000 |
| 2026-09-28 | 1,753,979,879.64 | 2,000,630,717.71 | +246,650,838.07 (up) | 2,000,630,717.71 | 2,000,630,717.71 | 0.00 | -0.0000 |
| 2026-09-29 | 1,840,926,601.56 | 1,997,308,171.72 | +156,381,570.16 (up) | 1,997,308,171.72 | 1,997,308,171.72 | 0.00 | -0.0000 |
| 2026-09-30 | 1,843,114,215.49 | 1,992,588,179.03 | +149,473,963.53 (up) | 1,992,588,179.03 | 1,992,588,179.03 | 0.00 | +0.0000 |
| 2026-10-01 | 1,843,207,832.37 | 1,993,538,267.44 | +150,330,435.06 (up) | 1,993,538,267.44 | 1,993,538,267.44 | 0.00 | -0.0000 |
| 2026-10-02 | 1,994,163,246.13 | 2,022,378,266.88 | +28,215,020.75 (up) | 2,022,378,266.88 | 2,022,378,266.88 | 0.00 | -0.0000 |
| 2026-10-03 | 2,026,207,014.97 | 2,026,212,218.57 | +5,203.59 (up) | 2,026,212,218.57 | 2,026,212,218.57 | 0.00 | -0.0000 |
| 2026-10-04 | 2,029,997,663.13 | 2,030,046,170.25 | +48,507.12 (up) | 2,030,046,170.25 | 2,030,046,170.25 | 0.00 | -0.0000 |
| 2026-10-05 | 2,007,761,226.11 | 2,005,935,887.86 | -1,825,338.25 (down) | 2,005,935,887.86 | 2,005,935,887.86 | 0.00 | +0.0000 |
| 2026-10-06 | 2,019,548,567.60 | 2,018,199,717.00 | -1,348,850.60 (down) | 2,018,199,717.00 | 2,018,199,717.00 | 0.00 | +0.0000 |
| 2026-10-07 | 2,013,270,405.35 | 2,011,778,570.56 | -1,491,834.79 (down) | 2,011,778,570.56 | 2,011,778,570.56 | 0.00 | -0.0000 |
| 2026-10-08 | 2,014,814,865.45 | 2,012,881,683.71 | -1,933,181.74 (down) | 2,012,881,683.71 | 2,012,881,683.71 | 0.00 | -0.0000 |
| 2026-10-09 | 2,015,391,646.72 | 2,015,391,646.72 | +0.00 (holds) | 2,015,391,646.72 | 2,015,391,646.72 | 0.00 | -0.0000 |

Firm total moves on 14 of 15 dates (up 10, down 4, holds 1: 2026-10-09). Largest absolute difference between rebuilt firm total and AUA on any date: 0.0000.

Served Unclassified on 2026-10-09, D_04 rule (`D_04.client_portal_summary.py:440-462`: total minus the six canonical classes, the firm snapshot): served $1,846,332.73; from the would-be snapshot $883,413.33; move -$962,919.40. The stored firm Unclassified key in the would-be snapshot is $883,483.05, the same figure as the per-relationship sum the SC-e-96 and SC-e-98 records carry. The D_04 rule and the key differ by $69.72: the six canonical classes and the key together exceed the firm total by that amount (measured on the snapshot; its cause, the six-place rounding of the per-relationship class shares, is inferred and not read per relationship; row MDPF_SECCLASS-D1-W86-S10). The Period bars Unclassified on 2026-10-09 is the D_04 figure, $883,413.33.

The CVO figures for this radius do not reproduce from this measure (row MDPF_SECCLASS-D1-W86-S7). The CVO statement of 14 of 15 dates above the served total, up to $270,086,670.20, is not what the build dry run gives: 10 dates are above (2026-09-25 to 2026-10-04), 4 are below (2026-10-05 to 2026-10-08), and the largest excess is $246,650,838.07 on 2026-09-28. The smallest excess ($5,203.59 on 2026-10-03) and the equality on 2026-10-09 reproduce.

## Added and dropped relationships

Definitions. Added: a relationship the rebuild carries on the date and the stored JSON does not (dollars = rebuilt `total_mv`). Dropped: a relationship the stored JSON carries on the date and the rebuild does not (dollars = stored `total_mv`). Changed: a relationship on both sides whose `total_mv` differs (dollars = rebuilt minus stored). Stored JSONs are the ones the build read (3,793 relationship JSONs; control: the 3,103 relationships with a 2026-10-09 entry equal the SC-e-98 record count). Relationship ids are the opaque keys the stored JSONs carry. Added minus dropped alone does not reconcile to the firm total move; the changed term is the missing one, and with it the residual is zero on every date.

| date | firm total move | added n | added $ | dropped n | dropped $ | changed n | changed $ | added minus dropped | residual |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026-09-25 | +32,079,997.98 | 18 | 14,387,303.32 | 10 | 1,090,347.66 | 954 | +18,783,042.33 | +13,296,955.66 | -0.00 |
| 2026-09-26 | +224,041,973.12 | 172 | 83,175,990.96 | 10 | 1,088,527.25 | 1005 | +141,954,509.40 | +82,087,463.71 | +0.00 |
| 2026-09-27 | +223,812,108.95 | 172 | 83,052,780.13 | 10 | 1,086,706.84 | 1004 | +141,846,035.66 | +81,966,073.29 | +0.00 |
| 2026-09-28 | +246,650,838.07 | 205 | 85,380,814.67 | 9 | 1,097,172.64 | 1012 | +162,367,196.05 | +84,283,642.03 | -0.00 |
| 2026-09-29 | +156,381,570.16 | 68 | 29,762,973.11 | 10 | 4,943,791.06 | 966 | +131,562,388.10 | +24,819,182.06 | +0.00 |
| 2026-09-30 | +149,473,963.53 | 62 | 19,850,416.81 | 9 | 987,626.70 | 2731 | +130,611,173.43 | +18,862,790.11 | +0.00 |
| 2026-10-01 | +150,330,435.06 | 67 | 21,153,764.46 | 14 | 3,569,763.19 | 432 | +132,746,433.80 | +17,584,001.26 | +0.00 |
| 2026-10-02 | +28,215,020.75 | 25 | 7,393,059.25 | 14 | 3,586,805.35 | 347 | +24,408,766.85 | +3,806,253.90 | -0.00 |
| 2026-10-03 | +5,203.59 | 18 | 4,683,821.13 | 15 | 3,743,536.60 | 349 | -935,080.93 | +940,284.53 | -0.00 |
| 2026-10-04 | +48,507.12 | 18 | 4,693,935.81 | 15 | 3,751,634.39 | 349 | -893,794.29 | +942,301.42 | -0.00 |
| 2026-10-05 | -1,825,338.25 | 18 | 4,704,499.38 | 15 | 3,773,029.37 | 361 | -2,756,808.26 | +931,470.01 | -0.00 |
| 2026-10-06 | -1,348,850.60 | 17 | 13,117,245.21 | 11 | 2,499,082.77 | 304 | -11,967,013.05 | +10,618,162.44 | -0.00 |
| 2026-10-07 | -1,491,834.79 | 16 | 3,361,606.93 | 8 | 1,823,952.52 | 281 | -3,029,489.19 | +1,537,654.41 | -0.00 |
| 2026-10-08 | -1,933,181.74 | 0 | 0.00 | 1 | 32,323.74 | 68 | -1,900,858.00 | -32,323.74 | -0.00 |
| 2026-10-09 | +0.00 | 0 | 0.00 | 0 | 0.00 | 0 | +0.00 | +0.00 | +0.00 |

Both branches, read from the rule. Dates whose total moves: 14 (2026-09-25 to 2026-10-08): the added, dropped and changed sums above are non-zero and reconcile to the move. A date whose total holds: 2026-10-09, with 0 added, 0 dropped and 0 changed. Totals over the window: 876 added rows and 151 dropped rows. Added rows with no JSON in the store at all: 0; every added relationship is stored on other dates. Dropped rows whose relationship is stored on other dates: 151; with no other stored date: 0.

The ten largest added and the ten largest dropped per date, by dollars, by relationship id (opaque). Added: stored on other dates (the id exists, the date is missing). Dropped: stored on other dates (the id exists, the date is present in the store but not in the rebuild).

2026-09-25. Added (rebuilt $): z08250781 8,000,316.80; z08401325 1,962,949.65; z08306514 1,452,271.53; z08324492 801,241.04; z08400313 706,115.91; z08400437 649,655.50; z08330561 388,789.62; z08400789 108,953.18; z08268946 106,684.48; z08173275 34,537.77
2026-09-25. Dropped (stored $): z08324596 363,188.24; z08124014 259,703.74; z08171071 141,756.34; z08312385 127,119.55; z0893525 94,900.43; z08299947 53,915.85; z0893343 19,718.31; z08346291 18,972.52; z08305491 11,072.68; z08129847 0.00

2026-09-26. Added (rebuilt $): z08390508 9,397,217.92; z08250781 7,995,663.01; z08390546 3,984,078.34; z08130103 2,515,814.22; z08268857 2,229,602.61; z08249182 2,002,570.27; z08387390 1,986,287.11; z08401325 1,959,597.42; z08320635 1,878,611.35; z08395886 1,812,618.45
2026-09-26. Dropped (stored $): z08324596 362,618.72; z08124014 259,339.51; z08171071 141,500.42; z08312385 126,856.96; z0893525 94,704.60; z08299947 53,850.77; z0893343 19,674.86; z08346291 18,932.15; z08305491 11,049.28; z08129847 0.00

2026-09-27. Added (rebuilt $): z08390508 9,389,783.29; z08250781 7,991,009.22; z08390546 3,976,227.58; z08130103 2,513,084.60; z08268857 2,225,723.10; z08249182 1,998,297.11; z08387390 1,982,308.24; z08401325 1,956,245.19; z08320635 1,874,846.82; z08395886 1,810,992.19
2026-09-27. Dropped (stored $): z08324596 362,049.19; z08124014 258,975.28; z08171071 141,244.49; z08312385 126,594.36; z0893525 94,508.77; z08299947 53,785.69; z0893343 19,631.40; z08346291 18,891.78; z08305491 11,025.87; z08129847 0.00

2026-09-28. Added (rebuilt $): z08390508 9,382,348.65; z08250781 7,986,355.43; z08390546 3,968,376.82; z08130103 2,510,354.99; z08249182 1,994,023.95; z08387390 1,978,329.38; z08401325 1,952,892.96; z08320635 1,871,082.30; z08124280 1,822,541.77; z08395886 1,809,365.93
2026-09-28. Dropped (stored $): z08324596 361,479.66; z08124014 258,611.05; z08171071 140,988.57; z08312385 126,331.77; z0893525 94,312.94; z08299947 53,720.61; z08382298 31,874.16; z08346291 18,851.41; z08305491 11,002.47

2026-09-29. Added (rebuilt $): z08250781 7,976,501.65; z08130103 2,515,722.66; z08249182 1,988,645.18; z08401325 1,948,255.88; z08124280 1,812,849.62; z08391340 1,743,078.24; z08399956 1,059,351.01; z08396968 994,508.81; z08398952 899,357.27; z08324492 794,194.62
2026-09-29. Dropped (stored $): z08129921 3,524,961.87; z08327615 591,167.92; z08305488 450,684.52; z08305527 151,046.27; z0893525 94,064.11; z08299947 53,671.55; z08382298 31,838.76; z08305542 19,220.54; z08125675 16,160.94; z08305491 10,974.59

2026-09-30. Added (rebuilt $): z08393466 6,317,005.08; z08130103 2,512,103.79; z08249182 1,980,072.29; z08401325 1,939,349.34; z08324492 784,468.28; z08400313 700,011.38; z0880298 559,258.75; z08296327 556,841.65; z08117302 506,245.45; z08400990 491,405.08
2026-09-30. Dropped (stored $): z08299937 246,571.24; z08325341 229,840.33; z08124014 190,663.82; z08171071 140,211.60; z0893525 64,061.57; z08299947 53,574.36; z08382298 31,898.94; z08346291 18,720.15; z08124514 12,084.71

2026-10-01. Added (rebuilt $): z08393466 6,372,904.07; z08130103 2,513,937.51; z08249182 1,973,422.18; z08401325 1,932,986.99; z08398952 897,518.61; z08324492 783,953.34; z08400313 699,530.26; z08189502 586,620.42; z0880298 559,258.75; z08296327 554,946.15
2026-10-01. Dropped (stored $): z08387324 861,356.97; z08311387 643,793.07; z08327615 586,620.42; z08305488 448,107.64; z08299937 246,039.44; z08325341 229,093.65; z08124014 190,281.29; z08171071 139,773.15; z0893525 63,847.43; z08299947 53,510.48

2026-10-02. Added (rebuilt $): z08401325 1,943,174.21; z08324492 786,568.13; z08400313 703,746.89; z08189502 597,074.25; z08296327 559,058.15; z08400990 493,238.10; z08296389 484,978.25; z08305511 483,985.83; z08296381 451,579.88; z08124685 275,606.36
2026-10-02. Dropped (stored $): z08387324 866,916.00; z08311387 647,286.28; z08327615 597,074.25; z08305488 451,579.88; z08299937 247,932.64; z08325341 230,326.30; z08124014 191,730.62; z08171071 140,587.71; z0893525 64,318.47; z08299947 53,541.38

2026-10-03. Added (rebuilt $): z08398952 905,038.45; z08324492 788,024.25; z08400313 705,499.23; z08189502 599,244.47; z08296327 560,157.35; z08296381 452,520.99; z08124685 275,998.13; z08268946 106,018.89; z08306538 85,162.34; z08305494 52,881.20
2026-10-03. Dropped (stored $): z08387324 905,546.91; z08327615 599,244.47; z08306475 560,552.75; z08305488 452,520.99; z08124014 450,637.51; z08299937 248,445.76; z08171071 140,801.81; z08392251 115,934.24; z0893525 94,307.04; z08305527 63,686.69

2026-10-04. Added (rebuilt $): z08398952 906,575.86; z08324492 789,480.38; z08400313 707,251.57; z08189502 601,414.69; z08296327 561,256.56; z08296381 453,462.10; z08124685 276,389.90; z08268946 106,229.92; z08306538 85,330.59; z08305494 52,971.98
2026-10-04. Dropped (stored $): z08387324 907,118.22; z08327615 601,414.69; z08306475 561,631.98; z08305488 453,462.10; z08124014 451,523.99; z08299937 248,958.87; z08171071 141,015.91; z08392251 116,160.47; z0893525 94,492.74; z08305527 63,795.53

2026-10-05. Added (rebuilt $): z08398952 908,139.11; z08324492 791,141.91; z08400313 709,003.91; z08189502 603,624.18; z08296327 562,391.37; z08296381 454,403.22; z08124685 276,896.25; z08268946 106,445.21; z08306538 85,498.85; z08305494 53,073.12
2026-10-05. Dropped (stored $): z08387324 908,715.36; z08327615 603,624.18; z08306475 562,738.26; z08305488 454,403.22; z08124014 452,675.74; z08299937 249,471.98; z08171071 141,277.03; z08392251 116,386.69; z0893525 94,684.99; z08305527 63,904.37

2026-10-06. Added (rebuilt $): z08250781 7,978,576.91; z08124280 1,837,001.77; z08189502 616,968.08; z08296327 564,613.78; z08305511 488,678.02; z08296381 456,078.19; z08330561 389,144.21; z08268895 304,675.60; z08305496 112,396.07; z0880221 104,510.69
2026-10-06. Dropped (stored $): z08327615 616,968.08; z08305488 456,078.19; z08324596 361,547.92; z08129921 339,227.36; z08325341 232,253.76; z08124014 195,250.33; z0893525 95,051.54; z08312385 78,491.45; z08299947 53,706.08; z08387324 37,713.50

2026-10-07. Added (rebuilt $): z08189502 619,335.15; z08296327 561,622.17; z08305511 486,134.06; z08296381 453,445.16; z08330561 387,094.73; z08268895 304,069.49; z08305496 111,751.49; z0880221 103,959.83; z0880650 81,563.87; z08299949 70,376.35
2026-10-07. Dropped (stored $): z08327615 619,335.15; z08305488 453,445.16; z08129921 337,254.89; z08124014 194,790.70; z0893525 94,544.22; z08299947 53,674.32; z08387324 38,191.40; z08382298 32,716.68

2026-10-08. Added: none.
2026-10-08. Dropped (stored $): z08382298 32,323.74

2026-10-09. Added: none.
2026-10-09. Dropped: none.

## Advisors the map drops

Advisor keys of the served `gold/views/mix_daily_summary.json` (VersionId VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD): 56. Advisor keys of the would-be summary: 56. Keys in the served map and not in the would-be: 0. Keys in the would-be and not served: 0. Advisor days the act removes outright (a window day present in the served map and absent from the would-be): 0. No advisor is dropped by the act.

Measure first, on the base code (row MDPF_SECCLASS-D1-W80-S3). The last five served versions of the object, newest first (list-object-versions, then get-object by VersionId, each MD5 checked against its ETag): VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD (2026-10-11T05:23:28Z), 6o1FOSbTRgA9hRzl7I5WyHcN3EyFH.RJ (2026-10-10T05:26:14Z), yeOM6gafw_nQ_fJTasMozeD3S3.3x8rW (2026-10-09T05:26:46Z), 2aF_6jdpgdPAekkVc527O4RDO_3lUNvW (2026-10-08T05:26:01Z), wIyPICXUfBiEyJGrjMvqWGZutImWp6Ng (2026-10-07T05:27:03Z). Each carries 56, 56, 56, 56, 56 advisor keys; the union is 56 and the intersection is 56. No advisor key left the served map in those five versions, so the drop the base code could make (its write carries only the advisors with data in the fire, `028fab8273` C_06 :1126-1144, read from the code, not measured) did not happen on those fires.

Advisor totals over the 15 window days. One row per date: advisor-days whose total moves (a day present on either side and differing by more than $0.005), gross absolute move, net move, and the advisors whose window day is removed:

| date | advisors whose total moves | gross absolute move | net move |
|---|---:|---:|---:|
| 2026-09-25 | 43 | 46,830,216.22 | +32,807,857.57 |
| 2026-09-26 | 45 | 241,378,557.78 | +210,381,656.06 |
| 2026-09-27 | 45 | 241,194,713.30 | +210,171,041.99 |
| 2026-09-28 | 45 | 269,937,836.24 | +232,087,736.28 |
| 2026-09-29 | 41 | 250,820,080.70 | +145,521,204.83 |
| 2026-09-30 | 48 | 242,581,328.87 | +137,706,143.83 |
| 2026-10-01 | 32 | 243,310,746.53 | +138,776,752.25 |
| 2026-10-02 | 30 | 42,604,313.75 | +27,808,992.34 |
| 2026-10-03 | 31 | 8,613,290.18 | +394,782.15 |
| 2026-10-04 | 31 | 8,595,118.15 | +438,385.11 |
| 2026-10-05 | 31 | 9,247,348.29 | -1,435,179.20 |
| 2026-10-06 | 31 | 7,645,249.11 | -1,821,291.64 |
| 2026-10-07 | 28 | 7,145,369.10 | -1,966,407.47 |
| 2026-10-08 | 21 | 2,081,752.43 | -1,933,474.68 |
| 2026-10-09 | 0 | 0.00 | +0.00 |

Advisor-days that move in all: 502 of 840 advisor-days present on either side. The full 15-date by advisor table (advisor key, date, served total, rebuilt total, move) is named by path: `.scratch/advisor_window_table.csv` in worktree wk-MDPF_SECCLASS-86 (not committed).

The ten largest advisor moves by absolute dollars (advisor key as the served map carries it, date, served total, rebuilt total, move):

- Tim Rodgers, 2026-09-28: served 60,804,390.93, rebuilt 140,134,528.37, move +79,330,137.44
- Tim Rodgers, 2026-10-01: served 64,857,426.74, rebuilt 143,251,616.57, move +78,394,189.83
- Tim Rodgers, 2026-09-29: served 65,301,323.27, rebuilt 140,118,264.42, move +74,816,941.15
- Tim Rodgers, 2026-09-30: served 65,011,243.34, rebuilt 139,710,170.71, move +74,698,927.37
- Tim Rodgers, 2026-09-26: served 61,357,579.86, rebuilt 134,196,492.62, move +72,838,912.76
- Tim Rodgers, 2026-09-27: served 61,241,122.68, rebuilt 133,988,724.41, move +72,747,601.74
- Luke Heiligenthal, 2026-09-29: served 64,168,048.45, rebuilt 11,521,163.71, move -52,646,884.73
- Luke Heiligenthal, 2026-09-30: served 63,950,582.67, rebuilt 11,515,582.05, move -52,435,000.62
- Luke Heiligenthal, 2026-10-01: served 64,075,320.69, rebuilt 11,809,893.92, move -52,265,426.77
- Patrick Mundlin, 2026-09-28: served 71,241,978.80, rebuilt 103,965,197.30, move +32,723,218.49

Attribution. The advisor totals on the window days are not the stored history under the build's own rel_architect lookup (`C_06._load_rel_architect_lookup`, read at build time: 3,267 relationships, 57 advisors). Of the 825 advisor-days read in a control (served map against the stored JSONs summed under the current lookup), the largest gap is $54,859,391.75. Worked example, 2026-09-29: Tim Rodgers served $65,301,323.27; stored history under the current lookup $120,160,715.02 (attribution +$54,859,391.75); would-be $140,118,264.42 (data +$19,957,549.40). Luke Heiligenthal served $64,168,048.45; stored history under the current lookup $9,325,975.05 (attribution -$54,842,073.40); would-be $11,521,163.71 (data +$2,195,188.66). So the advisor moves on the window days are partly re-attribution under the current lookup, not dollars re-derived, and the dates before 2026-09-25 keep the attribution the served history carries (row MDPF_SECCLASS-D1-W86-S8).

Unresolved relationships. The firm total move less the net move of the advisor totals, per date (relationships with no resolved advisor appear in the firm total and in no advisor total). The residual is what the advisor totals do not carry: the change on relationships with no resolved advisor in either map, and any attribution change that crosses the resolved boundary (not split here): 2026-09-25 -727,859.59; 2026-09-26 +13,660,317.06; 2026-09-27 +13,641,066.96; 2026-09-28 +14,563,101.79; 2026-09-29 +10,860,365.33; 2026-09-30 +11,767,819.72; 2026-10-01 +11,553,682.81; 2026-10-02 +406,028.41; 2026-10-03 -389,578.56; 2026-10-04 -389,877.98; 2026-10-05 -390,159.06; 2026-10-06 +472,441.03; 2026-10-07 +474,572.68; 2026-10-08 +292.94; 2026-10-09 +0.00.

## Period bars

The four period bars the window reaches, plus the 2026 annual bar. Each bar is `compute_period_views` (lib/mix_views.py:66-107) applied by D_03 to the firm daily map with the client_performance AUA as `cp_daily_total` (D_03 :523). The bar total is the AUA at the end date; each class is the end-date class share of the cube total times that AUA; Unclassified is the residual. Served = the served daily map (VrrTn2 summary) through the same function; after = the would-be daily map. Positive control: the served function output equals the served `gold/artifacts/firm_mix_views.json` bars (every row).

| bar | end date | total before | total after | class | before | after | move |
|---|---|---:|---:|---|---:|---:|---:|
| Q3 2026 | 2026-09-30 | 1,992,588,179.03 | 1,992,588,179.03 | equity | 1,469,893,820.26 | 1,477,147,101.25 | +7,253,280.99 |
|  | | |  | fixed_income | 406,457,511.45 | 389,614,044.94 | -16,843,466.51 |
|  | | |  | alternatives | 1,697,108.13 | 3,424,494.97 | +1,727,386.84 |
|  | | |  | commodities | 1,506,424.47 | 1,877,776.72 | +371,352.25 |
|  | | |  | structured | 28,414,846.10 | 115,964,148.49 | +87,549,302.39 |
|  | | |  | cash | 2,174,022.44 | 4,507,655.30 | +2,333,632.86 |
|  | | |  | unclassified | 82,444,446.18 | 52,957.36 | -82,391,488.82 |
| September 2026 | 2026-09-30 | 1,992,588,179.03 | 1,992,588,179.03 | equity | 1,469,893,820.26 | 1,477,147,101.25 | +7,253,280.99 |
|  | | |  | fixed_income | 406,457,511.45 | 389,614,044.94 | -16,843,466.51 |
|  | | |  | alternatives | 1,697,108.13 | 3,424,494.97 | +1,727,386.84 |
|  | | |  | commodities | 1,506,424.47 | 1,877,776.72 | +371,352.25 |
|  | | |  | structured | 28,414,846.10 | 115,964,148.49 | +87,549,302.39 |
|  | | |  | cash | 2,174,022.44 | 4,507,655.30 | +2,333,632.86 |
|  | | |  | unclassified | 82,444,446.18 | 52,957.36 | -82,391,488.82 |
| Q4 2026 | 2026-10-09 | 2,015,391,646.72 | 2,015,391,646.72 | equity | 1,518,033,035.28 | 1,518,909,300.32 | +876,265.04 |
|  | | |  | fixed_income | 397,149,719.30 | 397,236,373.66 | +86,654.36 |
|  | | |  | alternatives | 5,192,672.93 | 5,192,672.93 | +0.00 |
|  | | |  | commodities | 2,059,707.90 | 2,059,707.90 | +0.00 |
|  | | |  | structured | 86,759,811.62 | 86,759,811.62 | +0.00 |
|  | | |  | cash | 4,350,366.96 | 4,350,366.96 | +0.00 |
|  | | |  | unclassified | 1,846,332.73 | 883,413.33 | -962,919.40 |
| October 2026 | 2026-10-09 | 2,015,391,646.72 | 2,015,391,646.72 | equity | 1,518,033,035.28 | 1,518,909,300.32 | +876,265.04 |
|  | | |  | fixed_income | 397,149,719.30 | 397,236,373.66 | +86,654.36 |
|  | | |  | alternatives | 5,192,672.93 | 5,192,672.93 | +0.00 |
|  | | |  | commodities | 2,059,707.90 | 2,059,707.90 | +0.00 |
|  | | |  | structured | 86,759,811.62 | 86,759,811.62 | +0.00 |
|  | | |  | cash | 4,350,366.96 | 4,350,366.96 | +0.00 |
|  | | |  | unclassified | 1,846,332.73 | 883,413.33 | -962,919.40 |
| 2026 annual | 2026-10-09 | 2,015,391,646.72 | 2,015,391,646.72 | equity | 1,518,033,035.28 | 1,518,909,300.32 | +876,265.04 |
|  | | |  | fixed_income | 397,149,719.30 | 397,236,373.66 | +86,654.36 |
|  | | |  | alternatives | 5,192,672.93 | 5,192,672.93 | +0.00 |
|  | | |  | commodities | 2,059,707.90 | 2,059,707.90 | +0.00 |
|  | | |  | structured | 86,759,811.62 | 86,759,811.62 | +0.00 |
|  | | |  | cash | 4,350,366.96 | 4,350,366.96 | +0.00 |
|  | | |  | unclassified | 1,846,332.73 | 883,413.33 | -962,919.40 |

The bar totals do not move: each is the client_performance AUA at the bar's end date. The class dollars move. The after figures are the would-be daily map through the function; they exclude the post-act SC-e-91 retained-only pass on window dates, which the dry run could not measure against the post-act state (row MDPF_SECCLASS-D1-W86-S9).

COO half: UNSIGNED
CTO half: UNSIGNED
