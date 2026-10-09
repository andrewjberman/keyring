# Never-widen half, MDPF_SECCLASS -- the NAME:: row for American Century Ultra Inv agrees with its CUSIP: row (cell SC-e-83, row D1-W66-S1)

**Author:** `0.9.0_WK_MDPF_SECCLASS~73` for `2.0.0_SA_COO~M1`, 2026-10-09. **For:** `1.0.0_SA_CTO`, second half. **Status: REQUEST, nothing written.**
This file is a REQUEST. Nothing in it has been written to any table. The writer refuses `--write` until both headings at the foot read SIGNED.

## The key, before and after

Two canonical rows of `etf-classifications` carry the name "American Century Ultra Inv". Read by consistent get-item, us-east-1, 2026-10-09:

| key | asset_class | sub_asset_class | updated_by |
|---|---|---|---|
| `CUSIP:025083882` | `equity` | `US Large Cap` | `mdpf-secclass-s62-ascii-names` |
| `NAME::AMERICAN CENTURY ULTRA INV` (before) | `fixed_income` | `Ultra Short Duration` | `mdpf-secclass-old-list-reclassify` |
| `NAME::AMERICAN CENTURY ULTRA INV` (after) | `equity` | `US Large Cap` | `mdpf-secclass-s11-rows` (writer constant) |

American Century Ultra Fund, Investor class (TWCUX), is a US large-cap growth equity fund; "Ultra" is the fund name, not a duration. The `NAME::` row is the wrong one.

## The act

Run by the issuer after both halves sign:
`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --set org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_ULTRA_ROW_SET_20261009.tsv --write --half org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ULTRA_NAME_ROW_20261009.md --snapshot org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ULTRA_ROW_SNAPSHOT_R16_20261009.json`

The set is one REMAP line. Dry run (read-only, this worker): `S11-ROWS-DRY-RUN new=0 remap=1 refused_present=0 refused_stale=0 puts=0`.

## Blast radius

One table, `etf-classifications`; one key, `NAME::AMERICAN CENTURY ULTRA INV`; the `asset_class` and `sub_asset_class` attributes (plus the writer's audit attributes). No other row, table or S3 object; no row created or deleted.

The candidate diff is the one-line set `R16_ULTRA_ROW_SET_20261009.tsv` (REMAP, `fixed_income`/`Ultra Short Duration` to `equity`/`US Large Cap`), as in the table above.

Served positions carrying this name, read-only from the newest `gold/canonical/holdings/` partition (`2026-10-07.parquet`) in each firm bucket, rows whose `asset_name` contains "AMERICAN CENTURY ULTRA":
- **BD** (`opal-data-bd`, 116,919 rows): 2 positions, 2 accounts, market value 88,936.60 USD. `asset_name` is `AMERICAN CENTURY ULTRA® INV` (with the registered mark), `ticker` `TWCUX`.
- **COT** (`opal-data-cot`, 21,024 rows): 0 positions, 0 USD.

Limit stated: the 2 BD positions' name carries the registered mark and a ticker, and the exact name `AMERICAN CENTURY ULTRA INV` matches 0 rows in either partition. `TWCUX` has no row in the table (consistent get-item: absent). Whether those 2 positions resolve through the `NAME::` row (after ASCII-fold of the mark) or through the `CUSIP:` row, this worker did not trace; if through the `NAME::` row, their class moves from fixed_income to equity at the next gold run (88,936.60 USD), and if not, no served position moves. The signing seats read this limit.

## Rollback per key

The writer takes a snapshot of the pre-state item first, at the `--snapshot` path above. Restore:
`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --rollback org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ULTRA_ROW_SNAPSHOT_R16_20261009.json --write`
This puts `fixed_income` / `Ultra Short Duration` back on the key.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-09 ~09:3xZ, after the round-16 drain (@6087246b44).
- **The limit above is answered by SC-e-79's trace run** (`R16_CHECKS/sc_r16_ticker_no_row.py`, issuer re-run at the drain: `resolved=23`): TWCUX
  carries a ticker with no row, so under the SERVED lib (SC-e-76) its 2 BD positions stop at hop `ticker-no-row` and serve `unclassified`.
  This write alone moves NO served position. Under the SC-e-79 lib they resolve through this `NAME::` key (the e79 candidate diff lists
  TWCUX $88,937 as fixed_income, which is this row's current, wrong class).
- **Both branches of the writer's own rule** were read: no `--write` writes nothing (dry run `puts=0`); `--write` refuses a stale or
  present row (`refused_stale=0 refused_present=0` at the dry run), else puts the one REMAP after the snapshot.
- **Blast radius: one key, two class attributes plus the writer's audit attributes.** No S3 object, no Lambda.
- **Condition (sequencing): this write lands BEFORE the SC-e-79 lib deploy**, so no fire ever serves TWCUX as fixed_income.

## CTO half -- SIGNED

`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~09:3xZ, unconditionally, in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALVES_SECCLASS_R16_E83_E79_20261009.md` @279fa3391e (section "SC-e-83 -- SIGNED").
Transcribed here by the issuer `2.0.0_SA_COO~M1` with that citation; the signing text is the CTO's file.
