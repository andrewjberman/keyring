# Never-widen half request, MDPF_SECCLASS -- C_06 revisits a retained date's unclassified holdings on every fire (FWD-1, cell SC-e-91, row MDPF_SECCLASS-D1-S30)

**Author:** `0.9.0_WK_MDPF_SECCLASS~80` for `2.0.0_SA_COO~M1`, 2026-10-12. **For:** `2.0.0_SA_COO~M1` (COO half) and `1.0.0_SA_CTO` (CTO half).
**Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed or written to any bucket or table. Order `MDPF_SECCLASS.TO-SC-e91` (worktree branch `wk-MDPF_SECCLASS-80`, commit pending the COO's sign-off on the cell). Reads were read-only: `head-object`, `list-objects-v2` (paginated count), and DynamoDB `get_item` through the shared client.

## What is wrong

Round 20's SC-e-87 taught the three served classify sites to place a ticker-no-row position by its `NAME::` row, and it shipped. The served effect did not follow at D_04: `platinum/firm/mix_summary.json` reads Unclassified $1,846,332.73 at as_of 2026-10-09 before the ship and after it, equal to the cent. Four facts at base `2f215ca75a` explain it in `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`:

1. `SERVED_HOLDING_CLASSES` contains `unclassified` (base :274-275), so the retained pass (base :278-311) only revisited a retained holding whose class was OUTSIDE the set. A retained `unclassified` holding was never sent back through `classify_series`.
2. `build()` returned early on a fire with no new partition (base :694-696), so the retained pass did not run at all on a fire that built no new date.
3. `existing['firm'].update(firm_daily_new)` (base :975) replaced only the new dates; a retained date's class dollars were never adjusted.
4. D_04 reads `gold/views/mix_daily_summary.json` for its firm mix (`D_04.client_portal_summary.py:486`), so D_04's Unclassified is the firm total minus the six classes.

## The fix (staged in the worktree, LOCAL, not deployed)

All changes are in `C_06.client_mix_timeseries.py` (working tree; lines cited are post-edit). Nothing else is edited.

| change | file:line | what it does |
|---|---|---|
| revisit candidates | `:278-281` `_is_revisit_candidate` | a holding whose class is outside the six, or `unclassified` |
| `reclassify_retained(..., moved=None)` | `:284-339` | `unclassified` holdings are reclassified through `classify_series`; a holding that stays `unclassified` is skipped (`:316-317`, byte-identical, not counted); a moved holding's pct moves inside its date's mix; `moved` gets `(date, old, new, pct * total_mv)` (`:324`) |
| snapshot helpers | `:341-374` | `_moves_since`, `_adjust_day`, `_apply_retained_moves` |
| retained-only pass | `:772-836` (nested in `build()`), called `:842` (no new partition) and `:927` (no usable data) | reads every relationship JSON, rewrites only those where a holding moved (with their views), adjusts the firm and advisor day dollars, writes the summary only if a day changed |
| merge path | `:947`, `:1137-1139` | the same moves are derived from a before/after diff and applied to the firm and advisor snapshots of a fire WITH new partitions |
| strict summary read | `:489-493` | the retained pass reads the summary first; a failed read stops it before any JSON is rewritten |
| import | `:74` | `list_target` from `lib/platinum_dest` (READ ONLY) |

Tests: `data/black_diamond/scripts/gold/tests/test_c06_retained_unclassified_r21.py` (10 new, pass) and the sibling `test_c06_retained_dates_six_class.py` (6, pass, unchanged).

## The act (by a CloudOps lane, after both halves sign)

1. Open a change-management ledger in `org/critical_paths/change_management/` before the act, close it at completion.
2. Deploy ONLY this file to `s3://opal-data-bd/code/gold/`, outside a BD gold run: `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` (the deploy core ships only named files), before the next BD gold fire.
3. Precondition, measured read-only: the served `code/gold/C_06.client_mix_timeseries.py` has ETag `8e1b350fc55607bddd1ac84329cb1a98`, and that equals the md5 of the base bytes (`git show 2f215ca75a:data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`). The deploy delta is therefore exactly this cell's file diff. The lib (`lib/etf_classifier.py`) and D_03, D_04 are not in this act.
4. Read back: `platinum/firm/mix_summary.json` Unclassified beside the pre-act values in the Rollback table, after the first fire that builds or revisits a date.

## Blast radius

**Objects the act writes:** one code object, `code/gold/C_06.client_mix_timeseries.py`. No table, no data key, no watermark.

**Objects the next fire writes** (the nightly fire, with or without a new partition):
- Relationship JSONs `gold/entities/clients/{id}.json` and their legacy copies `gold/client_timeseries/{id}.json` (C_06 dual-write, `:442-446`), and the period views `{id}_views.json` (`:450`): ONLY the relationships where a holding moved. The retained-only pass READS every relationship JSON: **3,793** top-level `.json` objects under `gold/entities/clients/` (read-only list 2026-10-12, paginated, delimiter `/`; the `_views.json` and `_composition.json` siblings, 3,793 and 3,343, are excluded from the read set). The number rewritten per fire is the count of holdings the pass moves, not measured here.
- `gold/views/mix_daily_summary.json` (`:502`): written only if a day's dollars changed. A second fire over unchanged data writes nothing (measured in a scratch harness with in-memory stubs: fire 2 wrote 0 relationship JSONs, 0 views, 0 summaries).
- Downstream of that: D_03 (reads it at `D_03.composition_artifacts.py:484`) and D_04 (reads it at `D_04.client_portal_summary.py:486`; writes `platinum/firm/mix_summary.json` at `:574`).

**Not touched:** `etf-classifications` (read only), the lib, any ticker that has a row, any ticker-no-row position without a `NAME::` row (it stays `unclassified`), the watermark, and every in-six entry (byte-identical).

## Writers

**Writers of the served `platinum/firm/mix_summary.json`: N = 1.** Native Grep over `data/black_diamond/scripts/` (working tree):
- `data/black_diamond/scripts/gold/D_04.client_portal_summary.py:574` -- `_write_batch([(summary, 'platinum/firm/mix_summary.json')], ...)`, the only writer. (Other hits: docstring lines `:11`, `:470`, `:478`; test `tests/test_d04_unclassified_line.py:2`, `:43-44`, read only.)

**Writers of `gold/views/mix_daily_summary.json`: N = 1.**
- `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:502` -- `s3.put_object(... MIX_DAILY_SUMMARY ...)` inside `_write_mix_summary` (`:495`), called at `:835` (retained-only pass) and `:1144` (merge path). Readers: `D_03.composition_artifacts.py:484`, `D_04.client_portal_summary.py:486`, `E_25.aua_decomposition_audit.py:133`.

**Writers of the relationship JSONs `gold/entities/clients/{id}.json`: N = 1 file, 3 call sites.**
- `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:434` -- `_write_relationship_json`, called at `:798` (retained-only pass, new), `:970` (merge path), `:1084` (full build). Reader: `D_04.client_portal_summary.py:1237` and `:1241` (`client_timeseries_key`).

## Both branches of the expected outcome

Read from the code written (`reclassify_retained`, working tree `:284-339`):
- **A ticker-no-row holding WITH a `NAME::` row moves.** `classify_series` (`:202-270`) calls `classify_with_identity(ticker, name)` (`:239`), which returns `(class, sub, 'etf-classifications', 'ticker-no-row-name-key')` from the `NAME::` row (lib: `classify_with_identity`, the `_name_row` branch). The holding's class and its pct move from `unclassified` to that class inside the date's mix (`:318-323`), and `moved` receives `(date, unclassified, class, pct * total_mv)` (`:324`).
- **A ticker-no-row holding WITHOUT a `NAME::` row stays `unclassified` and is listed.** `classify_with_identity` returns `('', '', 'unclassified', 'ticker-no-row')`, the new class is `unclassified`, and the `continue` at `:316-317` leaves the holding byte-identical and uncounted. The cash-keyword rule still decides `cash` where the name carries CASH, SWEEP, MONEY MARKET or MMKT.

**Live read (2026-10-12, denominator 23).** `D1W66S3_TICKER_NO_ROW_LIST_20261009.json` `entries`, read against `etf-classifications` through the shared client (`get_classification`, which calls `table.get_item(Key={"ticker": ...})` only; no write, no query, no scan). Security-level fields only; the dollars are the list's 2026-10-06 partition.

| ticker | security name | dollars | NAME:: row class (live) | returned class | ticker row |
|---|---|---:|---|---|---|
| LBSAX | COLUMBIA DIVIDEND INCOME A | 365,335.72 | equity | equity | none |
| SCGE1 | LARGE CAP EQUITY MANAGED POOL | 151,435.14 | equity | equity | none |
| SCGN1 | INTERNATIONAL EQUITY INDEX POOL | 149,833.97 | equity | equity | none |
| TWCUX | AMERICAN CENTURY ULTRA INV | 88,936.60 | equity | equity | none |
| SCSI1 | SHORT TERM INCOME POOL | 59,242.28 | fixed_income | fixed_income | none |
| ASMIY | ASM INTL NV NY REGISTER SH | 27,730.24 | equity | equity | none |
| BALCX | AMERICAN FUNDS AMERICAN BALANCED C | 23,420.00 | equity | equity | none |
| SCGS1 | SMALL CAP EQUITY POOL | 22,958.00 | equity | equity | none |
| SCGG1 | GROWTH POOL | 22,773.13 | equity | equity | none |
| SCGT1 | TREASURY INFLATION PROTECTED SECS | 15,574.65 | fixed_income | fixed_income | none |
| PFF | ISHARES PREFERRED & INCOME SECURITIES ETF | 11,808.00 | fixed_income | fixed_income | none |
| SCGL1 | INTL EQUITY MANAGED POOL | 5,585.81 | equity | equity | none |
| FBCVX | FIDELITY BLUE CHIP VALUE | 4,812.51 | equity | equity | none |
| CEMVX | CAUSEWAY EMERGING MARKETS INVESTOR | 4,109.08 | equity | equity | none |
| AEMGX | ACADIAN EMERGING MARKETS INVESTOR | 3,973.06 | equity | equity | none |
| VWIGX | VANGUARD INTERNATIONAL GROWTH INV | 3,832.43 | equity | equity | none |
| FIADX | FIDELITY ADVISOR INTERNATIONAL DISCV I | 2,882.52 | equity | equity | none |
| FG | F&G ANNUITIES & LIFE INC COMMON STOCK | 1,533.60 | equity | equity | none |
| DJT | TRUMP MEDIA & TECHNOLOGY GROUP COM | 390.26 | equity | equity | none |
| GLPI | GAMING & LEISURE P COM | 67.24 | equity | equity | none |
| SKYQ | SKY QUARRY INC COM NEW | 33.00 | equity | equity | none |
| TDSC | ETC CABANA TARGET DRAWDOWN 10 ETF | 17.18 | equity | equity | none |
| BLIAQ | BB LIQUIDATING INC CL A | 1.04 | equity | equity | none |

Totals: **MOVED 23 of 23** (equity 20, $879,660.53; fixed_income 3, $86,624.93; total $966,285.46). **STAYING 0 of 23.** These are the classifier's answers for the 23 securities. They are NOT the dollars the act moves on a retained date: the revisit reaches only the holdings in each stored top-10 list. The reach, and the expected move as a range, are in the Reach section. The returned class equals the NAME:: row class for every row (mismatch 0). The branch that stays `unclassified` is exercised by the unit test (`test_unclassified_without_a_name_row_stays_unclassified_byte_identical_and_uncounted`), not by live data.

## Rollback

The prior C_06 object is the object served now, read by `head-object` on 2026-10-12. (The order cites ETag `1aa6e3b555815417bb90c65db3f2152f` / VersionId `AREnJgLoyQnZ1zKwPan793py8CCkNHHA`; that is the SC-e-87 post-act object, superseded by the 2026-10-12T06:18Z ADVI FB-f-9 mode move. Recorded in the channel as `MDPF_SECCLASS-D1-W80-S1`.)

| key | VersionId | ETag | LastModified | size | role |
|---|---|---|---|---|---|
| `code/gold/C_06.client_mix_timeseries.py` | `5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP` | `8e1b350fc55607bddd1ac84329cb1a98` | 2026-10-12T06:18:21Z | 46212 | CURRENT served = base bytes @2f215ca75a; **the rollback target** |
| `gold/views/mix_daily_summary.json` | `VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD` | `c51968d1d37d3cb078095360d3347d30` | 2026-10-11T05:23:28Z | 9877189 | pre-act; **restore target** if a fire's day dollars are wrong |
| `platinum/firm/mix_summary.json` | `_MTtBmpPHKvL3Hvt58tzeIsshH4c_lxb` | `b8ffd506d117c94249592968011e43a0` | 2026-10-12T05:44:00Z | 25124 | pre-act; **restore target** after a D_04 re-run |

Code rollback: `s3api get-object --version-id 5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP` for the code key, then `safe-deploy.sh` of that file; this restores today's behaviour. Data rollback for the relationship JSONs and views: the ship's pre-act read records the VersionIds of every `gold/entities/clients/{id}.json` and `{id}_views.json` the first fire rewrites (3,793 relationship JSONs are listed; this worker did not enumerate their VersionIds). Restoring a relationship JSON does not restore a snapshot day; the summary restore above is the only path for that.

## Reach

Measured read-only on 2026-10-12 over every relationship JSON the retained-only pass reads: `gold/entities/clients/`, top-level `.json`, `_views` and `_composition` skipped. **Relationships read: 3,793** (the denominator; 4.77 GB). The watermark `data_as_of` is 2026-10-09. Dollars are sums over all relationships; the mix-level figure is `mix.unclassified * total_mv`; the listed figure is the `unclassified` holdings inside the stored per-date concentration list (top 10 by market value per relationship per date).

| date | relationships with a mix entry (of 3,793) | mix-level unclassified $ | listed unclassified $ | listed / mix-level | relationships where mix > listed | listed $ that resolve now | canonical 23-security $ (raw, before the AP gate) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-10-09 | 3,103 | 1,846,399.46 | 1,326,892.62 | 71.86% | 29 | 653,857.12 (8 relationships) | 962,826.84 (85 rows) |
| 2026-10-08 | 3,262 | 972,749.97 | 630,060.89 | 64.77% | 27 | 629,530.89 (8 relationships) | 963,206.57 (86 rows) |

Cross-check: the 2026-10-09 mix-level sum, 1,846,399.46, is within $66.73 of the served firm Unclassified at that as-of, $1,846,332.73. "Resolve now" is each distinct listed (ticker, name) read through the shared classifier (get_item only; 21 distinct pairs on the two dates, 11 resolve). The canonical figure is read from `gold/canonical/holdings/<date>.parquet` by ticker, from the 23-security list; it is an upper figure because it is taken before the account-performance gate.

**The limit, in plain words.** Unclassified dollars that sit outside a relationship's stored holding list are NOT revisited by this act. Only a rebuild of that date from its canonical partition can move them. The act therefore moves AT MOST the listed share: 71.86% of the 2026-10-09 mix-level unclassified dollars and 64.77% of 2026-10-08, and of those only the holdings that now resolve. The remaining $519,506.84 (2026-10-09, 28.14%) and $342,689.08 (2026-10-08, 35.23%) stay in the served Unclassified until a rebuild.

**Expected move, as a range.** The served retained-date `platinum/firm/mix_summary.json` Unclassified (D_04 firm mix) should be expected to fall by between **$0 and $653,857.12** on 2026-10-09, and by between **$0 and $629,530.89** on 2026-10-08. The upper bound is the listed dollars that resolve; the 23-security canonical dollars on those dates ($962,826.84 and $963,206.57) are above it, so the cap does not bind. The 23-security total of $966,285.46 is the classifier's answer for those 23 securities on the 2026-10-06 list. It is not the point figure for the move. The act is material (about 35% of the 2026-10-09 mix-level unclassified dollars can move), so no gap row is needed for the act itself; the gap is the stored-list limit above.

## COO half: UNSIGNED

Left for `2.0.0_SA_COO~M1`. Read: the writer counts above (N = 1 for `platinum/firm/mix_summary.json`, N = 1 for `gold/views/mix_daily_summary.json`, N = 1 file for the relationship JSONs), the live 23-row table, both branches, the precondition (served bytes = base HEAD).

## CTO half: UNSIGNED

Left for `1.0.0_SA_CTO`. Read: the named file only, the blast radius (23 of 23 securities, $966,285.46, moved on retained dates; 0 staying), the rollback per key above.
