# Never-widen half request, MDPF_SECCLASS -- the canonical CASH row to cash/Cash (FWD-2, FWD-16, cell SC-e-68)

**Author:** `0.9.0_WK_MDPF_SECCLASS~58` for `2.0.0_SA_COO~M1`, 2026-10-08 ~03:0xZ. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been written to any table. The writer refuses `--write` until both headings at the foot read SIGNED.
Source: CTO round-12 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md` @82c4790d6c) section 3 item 2; the CTO e42 half (`CTO_HALF_MDPF_SECCLASS_SC_e42_A07_CANONICAL_FIRST_20261007.md`) condition 5 ("the table row is the defect, not a07"); PRD v0.14 ruling 2.4 (SC-e-64): Cash is a sub-class of cash only.

## The act (by the issuer, after both halves sign)

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_row_write.py --write --half <this file> --snapshot <snapshot.json>`

ONE conditional `UpdateItem` on table `etf-classifications`, key `ticker = CASH`:

    SET asset_class = 'cash', sub_asset_class = 'Cash', updated_by = 'mdpf-secclass-cash-row-r12'
    CONDITION classified_by = 'legacy' AND asset_class = 'fixed_income' AND sub_asset_class = 'Ultra Short Duration'

- **The one row, before and after** (the before read live, `get-item --consistent-read`, 2026-10-08T03:02Z, `measured`):

| attribute | before | after |
|---|---|---|
| ticker (key) | CASH | CASH |
| name | Cash & Cash Equivalents | unchanged |
| asset_class | fixed_income | cash |
| sub_asset_class | Ultra Short Duration | Cash |
| classified_by | legacy | legacy (not written) |
| management_style | unknown | unchanged |
| last_updated | 2026-08-25T17:48:57Z | unchanged (not written) |
| updated_by | seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25) | mdpf-secclass-cash-row-r12 |

- **No other attribute is touched; no row is created or deleted; no other table, no S3 object.** The values are the ones the constituents seeder's `build_row("CASH", ...)` now derives (SC-e-64: `cash` / `Cash`, proved by `R12_CHECKS/sc_e64_cash_row.py`); the contract lists `Cash` under `cash` only.
- **Dry run** (read this session, `R12_CHECKS/cash_row_write.py` with no flag, rc 0): `CASH-ROW-DRY-RUN write=1 current=fixed_income/Ultra Short Duration classified_by=legacy puts=0`. The client is wrapped with a counter of every mutating call, a mutating call in dry-run mode raises, and the run asserts puts=0.
- **The money-market funds are not in the act.** SALXX and FXFXX are separate keys and stay as they are; only the NAV-residual line `CASH` moves (the control in `sc_e64_cash_row.py`).

## Blast radius

One table, one key, three attributes (`asset_class`, `sub_asset_class`, `updated_by`) of the one row `CASH`.

### The local candidate diff (what the row reads before and after)

`CASH`: `fixed_income` / `Ultra Short Duration` -> `cash` / `Cash`; `updated_by` -> `mdpf-secclass-cash-row-r12`. Every other attribute of `CASH` and every other row reads as it does now. This is a one-row table candidate; there is no code candidate and no deploy.

### Served mix delta, per firm (e42 condition 5: stated here, not hidden)

The held amounts are the e42 compare's (`A07_SWITCH_BEFORE_AFTER_20261007.json`, row `CASH`, `held_claim` **inferred**: a local build of a07's own population legs, NOT the served bytes). The figure is the held position's value as that compare prints it; the sign is the compare's own.

| firm | the CASH key held | amount in the compare | served file(s) that read the `CASH` key | read of the served bytes |
|---|---|---|---|---|
| 49financial | yes | USD 14,678.18 | `dim_asset_classification` (a07, `runners_49f/a07_dim_asset_classification.py`), then the d06 mix | **UNREAD** by this device (the firm bucket denies dell1, rows W25-S1 and W32-S4). Seat that can read: a laptop cloud-operations seat |
| cottonwood | yes | USD -5,480,054.44 | the Black Diamond-family gold: `D_04.client_portal_summary.py` (`_classify_with_canonical`, `classifier.classify(ticker, name)`), `C_06.client_mix_timeseries.py`, `D_03.composition_artifacts.py`, all through `lib/etf_classifier.py` `ETFClassifier` reading the canonical row by ticker; and a07's Cottonwood leg, then the d08 mix | **UNREAD** by this device (firm bucket denies dell1). Seat that can read: a laptop cloud-operations seat |
| inflection | not in the compare's CASH row | 0 (`inferred`; the 164-key compare lists no Inflection amount for `CASH`; its cash-like keys such as `CUSTODIAL_CASH` and `FID:CASH` are other keys this act does not touch) | `INF_D_07a.firm_concentrations.py` reads the classifier (its header says no ETFClassifier fallback is needed; the `CASH` key was not traced there) | **UNREAD** (bucket denied to dell1). Seat that can read: a laptop cloud-operations seat |

- **What moves, by reader state.** The canonical-table readers (the Black Diamond-family gold through `ETFClassifier`, and a07 once canonical-first has run) read the row on their next run: `CASH` moves from the `fixed_income` bucket to the `cash` bucket by the row's amount. A reader still on the old list (a07 before its first canonical-first run reads `bd-securities` where `CASH` is "Pathward Financial Inc", `equity`; the e42 compare shows this as equity -> fixed_income) moves `CASH` from `equity` to `cash` at its first canonical run instead. The endpoint is `cash` in both cases and the amount is the same; which of the two bucket moves a given served file shows depends on whether that file's reader has run canonical-first yet, which this device cannot read.
- **Totals.** Each firm's mix total is unchanged: the amount moves between buckets (the same check as e42 condition 4: the d06/d08 mix totals still sum to each firm's value). A negative Cottonwood amount lowers its `cash` bucket and raises the bucket it leaves by the same amount.
- **Not a reader of the key:** `holdings_snapshot.py` (line 961) keys Black Diamond's own cash line by its description, never the ticker `CASH`, so the Holdings producers do not read this key for that line (read from the repo, `measured`; the served Holdings files are `UNREAD`).
- **Named, class not traced:** `data/etfs/scripts/gold/etf_positioning_publisher.py` reads the table through `ETFClassifier` for the ETF constituent universe, in which `CASH` is a labelled residual line (`seed-etf-constituents.py` `_CASH_RESIDUAL_TICKERS`). The act does not change `name`, so a name display does not move; whether the publisher groups by `asset_class` was not traced here. The issuer reads this limit at signing.
- **Next-run timing.** No served byte changes at the write. Each reader moves at its own next run (the chain run for a07/d06/d08; the scheduled gold runs for the Black Diamond family).

### The writers that can touch the key `CASH` (counted, each rule read from the repo)

N = 10 write paths to `etf-classifications` were counted by `git grep` over `data/` and `infra/aws/lambda/v2_portal/` for `put_item` / `update_item` against the table, plus the round-12 record's own writers. Their treatment of key `CASH` (live: `classified_by = legacy`):
1. `yang_pipeline/seed-etf-classifications.py` (the seed path, `seed`): its ticker set is the ETF registries' keys; none of them carries `CASH` (no `"CASH"` literal in `etf_classification.py`). Cannot reach the key.
2. `yang_pipeline/seed-etf-constituents.py` `put_row_if_unclassified`: `attribute_not_exists(classified_by)`. The row has `legacy`, so it refuses (`RowProtected`). Its kind-only mode sets `instrument_kind` only, and `instrument_kind_for("CASH")` is None.
3. `yang_pipeline/label-legacy-classified-by.py`: `attribute_not_exists(classified_by)`. Refuses.
4. `yang_pipeline/set-instrument-kind.py`: `instrument_kind` only. Cannot move a class.
5. `_shared/etf_classification_scheduled.py` (E_18, the `scheduled` writer): `put_item` with `attribute_not_exists(ticker)`. Refuses an existing key.
6. `data/black_diamond/scripts/classification/seed_canonical_securities.py --sync-yang` (preserve-don't-clobber `update_item`): its list carries `CASH_USD`, not `CASH`. Cannot reach the key.
7. The old-list reclassify set V3 (e32): row `CASH` is route `PRESENT` (already in the table), so no write line. Read from `OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv`.
8. The clean-names v2 set (e48): row `CASH` is `UNCHANGED`. Read from `CLEAN_NAME_ROW_SET_V2_20261007.tsv`.
9. The e49 DIRECT and AI writers: they land new rows and delete only where `updated_by` is their own value; `CASH` is not a new row. Not a writer of this key.
10. This writer, `cash_row_write.py`.
Of the ten, only number 10 moves the class of this key, and only if the condition holds. A concurrent writer that changed `classified_by`, `asset_class` or `sub_asset_class` between the read and the write makes the condition fail; the writer reports it and writes nothing. `claim: measured` for the code reads above (the dry run proves only the live row, not that no other seat is about to write). A write path outside `data/` and `infra/aws/lambda/v2_portal/` (an ad-hoc script by a seat) is not enumerable from the repo and is not claimed absent.

## Both branches (read from the producer's own rule: the condition in the writer)

- **Branch A, the row moves.** The row still reads `legacy`, `fixed_income`, `Ultra Short Duration` at the write. The update lands; the row reads `cash` / `Cash`, `updated_by = mdpf-secclass-cash-row-r12`, `classified_by = legacy`. Readers move at their next runs as above. Writer output: `WROTE 1 of 1; condition failures 0`.
- **Branch B, the condition refuses.** The row moved first (another writer changed `classified_by`, the class or the sub-class). The conditional update fails, the writer prints `CONDITION FAILED at write` and `WROTE 0 of 1; condition failures 1`, exits 1, and nothing is overwritten. At the read, a moved row prints `CASH-ROW-DRY-RUN write=0 ...` and `REFUSED_STALE`, so the issuer re-reads before re-trying; the pair is re-requested if the new state is not the one named above.

## Readers that print the name

Not touched: the act does not write `name`. Every reader that prints "Cash & Cash Equivalents" keeps printing it.

## Rollback per key

One key, `CASH`. The snapshot (`--snapshot`, written before the update) holds the full pre-state item. `cash_row_write.py --rollback <snapshot.json> --write` puts `asset_class` and `sub_asset_class` back to the snapshot's values (`fixed_income`, `Ultra Short Duration`) and `updated_by` to the snapshot's value (or REMOVE it if the row had none), only where the row still reads `asset_class = cash AND sub_asset_class = Cash AND updated_by = mdpf-secclass-cash-row-r12`. A row changed by another writer since is skipped and reported (`ROLLED BACK 0, skipped 1`). The dry-run form (`--rollback <snapshot.json>`, no `--write`) lists what it would restore and writes nothing; it was run this session against a scratch snapshot and printed `SKIP CASH (not at this run's value)`, the correct answer while the row has not moved. Served bytes rebuilt from the changed row return at the readers' next runs after a rollback, the same way.

## COO half -- UNSIGNED (2.0.0_SA_COO~M1)

## CTO half -- UNSIGNED (1.0.0_SA_CTO)
