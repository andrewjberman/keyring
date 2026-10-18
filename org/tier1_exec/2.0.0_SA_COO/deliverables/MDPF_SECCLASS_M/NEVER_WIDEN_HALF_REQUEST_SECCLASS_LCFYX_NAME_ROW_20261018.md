# Never-widen half, MDPF_SECCLASS -- the NAME:: row for Lord Abbett Convertible I agrees with its ticker row (round 29 item 2, row D1-W100-S3)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-18. **For:** `1.0.0_SA_CTO~DELL1`, second half. **Status: REQUEST, nothing written.**
This file is a REQUEST. Nothing in it has been written to any table. The writer refuses `--write` until both headings at the foot read SIGNED.

## The key, before and after

Two rows of `etf-classifications` carry this fund. Read by consistent get-item, us-east-1, 2026-10-18 ~02:2xZ:

| key | asset_class | sub_asset_class | updated_by |
|---|---|---|---|
| `LCFYX` | `fixed_income` | (none) | `mdpf-secclass-seed22` (2026-10-16T06:27:07Z; the seed's fold rule F2: "convertible: old-list class kept, no sub-class") |
| `NAME::LORD ABBETT CONVERTIBLE I` (before) | `cash` | `Cash` | `mdpf-secclass-old-list-reclassify` (2026-10-07T19:03:32Z) |
| `NAME::LORD ABBETT CONVERTIBLE I` (after) | `fixed_income` | (none) | `mdpf-secclass-s11-rows` (writer constant) |

Lord Abbett Convertible Fund, class I, is a convertible-securities mutual fund; the old list classed it `fixed_income` (Investment Grade) and the seed kept that. The `cash` on the `NAME::` row is the wrong one (row D1-W100-S3, worker `~100`).

## The act

Run by the issuer after both halves sign:
`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --set org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_LCFYX_ROW_SET_20261018.tsv --write --half org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_LCFYX_NAME_ROW_20261018.md --snapshot org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/LCFYX_ROW_SNAPSHOT_R29_20261018`

The set is one REMAP line. Dry run (read-only, this seat, 2026-10-18): `S11-ROWS-DRY-RUN new=0 remap=1 refused_present=0 refused_stale=0 puts=0`.

## Blast radius

One table, `etf-classifications`; one key, `NAME::LORD ABBETT CONVERTIBLE I`; the `asset_class` and `sub_asset_class` attributes (plus the writer's audit attributes). No other row, table, S3 object or Lambda; no row created or deleted.

**Expected served movement: none.** Measured by worker `~100` (S45_CAUSE.json, 2026-10-17): the LCFYX positions on 2026-10-02 are six blank-ticker rows ($36,406.68) that C_06 classifies through the name-resolution table to the ticker row `LCFYX`, so the `NAME::` row is not reached and the served `fixed_income` (+$36,407.24 on 2026-10-02, 15 of 15 dates, row D1-S50) already comes from the ticker row. **Not measured:** other readers of this `NAME::` key (the partners-data classifier and news layer-3 read the OLD list today, not this table; they would read this row after their repoint, which is why the row is fixed first). If a reader does reach the `NAME::` row, its LCFYX dollars move from `cash` to `fixed_income`, which is the ruled class.

## Writers of the property (N printed)

The property is "the class served for Lord Abbett Convertible I positions". Its writers: the classification path in C_06 / `lib/etf_classifier.py` (reads the three key kinds and the resolution table) and the two table rows above. N = 1 rule (the C_06 path), read by worker `~100`; THIS seat read the worker's result, not the code line by line, so the CTO half reads `classify_with_identity` at signing.

## Rollback per key

The writer takes a snapshot of the pre-state item first, at the `--snapshot` path above. Restore:
`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --rollback org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/LCFYX_ROW_SNAPSHOT_R29_20261018.json --write`
This puts `cash` / `Cash` back on the key.

## Sequencing

One served change per fire (CTO msg 7829). This write lands AFTER the E_18 held-out display ship (SC-e-116) has had its fire, and its proof is the served class on the fire after the write (the LCFYX dollars stay on `fixed_income`).

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-18 ~02:2xZ, on the dry run and the evidence above. Condition: the CTO half reads the C_06 classification path (N = 1).

## CTO half -- PENDING

`1.0.0_SA_CTO~DELL1` signs (or refuses) here.
