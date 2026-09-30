# NEVER-WIDEN HALF REQUEST -- MDPF_SECCLASS FWD-4/FWD-7 legacy classified_by label (SC-e-1)

**Requesting seat:** `0.9.0_WK_MDPF_SECCLASS~5` (worker of `2.0.0_SA_COO~M`), task order `MDPF_SECCLASS.TO-SC-e1`.
**For:** the CTO+COO never-widen sign-off on the ONE additive conditional label update this cell names but does NOT
execute (LOCAL build + record bound -- no table write). The numbers below are measured LIVE at build time
(`infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py --dry-run`, real DynamoDB reads, 2026-09-30
~03:1xZ), and recorded in
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_LABEL_CENSUS_20260930.json`.

## The act

For every row of `etf-classifications` that carries NO `classified_by` attribute, run ONE additive conditional
update per ticker:

```
UpdateExpression:     SET classified_by = :v         (:v = "legacy")
ConditionExpression:  attribute_not_exists(classified_by)
```

No other attribute is named in the `UpdateExpression`, so no other attribute can ever be touched by this call --
`label_row_if_unlabelled()` hard-codes the expression (`_WRITTEN_ATTRIBUTE = "classified_by"`), it is not built from
a caller-supplied field list. `legacy` is the contract's own text: "written before this contract; provenance not
recorded" (`org/standards/MDPF_SECCLASS_CONTRACT.json` v0.2.0, `classified_by.definitions.legacy`) -- it is not a
claim about which seeder actually wrote any of these 238 rows.

Measured scope of this act (`R2_LABEL_CENSUS_20260930.json`, live scan):

| table_rows_at_build | unlabelled_rows (candidate) | would_label | other_attributes_touched | overwrites |
|---|---|---|---|---|
| 2,309 | 238 | 238 | 0 | 0 |

`classified_by` distribution across all 2,309 live rows at build time: `scheduled` 1,934, `<absent>` 238 (the
candidate set), `seed` 137. `constituents` reads 0 today -- no constituents-seeded row has landed live yet under the
new label (the seeder change is this same cell's build item 2; its own write is a separate, future act under
`seed-etf-constituents.py`'s own conditional put, unaffected by this half).

## Blast radius

- **The rows.** Exactly the 238 tickers this build's census names (`R2_LABEL_CENSUS_20260930.json` `tickers[]`),
  each gaining exactly one new attribute: `classified_by = "legacy"`. Zero existing attributes on any row are
  touched -- `other_attributes_touched: 0`, `overwrites: 0` in the census, and the `UpdateExpression` itself names
  no other attribute (proved by unit test, `test_label_update_writes_only_classified_by`,
  `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`).
- **Readers of `classified_by`.** A repo-wide census (`comp-find "classified_by"`, `--band SURFACED/DEF`, this
  build) finds: (1) the three sanctioned writers themselves (`seed-etf-classifications.py`, the FWD-7 scheduled
  module, `seed-etf-constituents.py`), each writing its OWN value, never reading another row's; (2) the round-1/
  round-2 census/check scripts under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/` (`r1_backfill_census.py`
  branches on `classified_by == "scheduled"`; `r2_evidence.py check_label` requires the four-value set) -- none of
  these branch on `legacy` today, so none change behavior when a previously-absent attribute appears; (3) NO reader
  in `portal/src` (measured zero, 1,215 files scanned) and no other reader in `infra/aws/lambda/v2_portal` or `data/`
  branches on `etf-classifications.classified_by` at all today. FWD-4's future census (E2/E5/E8, not yet built) is
  the first reader this label is FOR -- it is designed to stop reporting these 238 rows as "no provenance" once
  labelled.
- **`find_by_asset_class` / `find_by_sub_asset_class` callers** (the one client,
  `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`): unaffected -- neither method reads or
  returns `classified_by`, and this act changes no `asset_class`/`sub_asset_class` value on any row.
- **Precedence.** Per the contract's own precedence rule, `legacy` is the read-time default for an absent
  attribute and never competes for a row against `seed`/`scheduled`/`constituents` writers -- once written, it
  behaves exactly like any other value under `attribute_not_exists(classified_by)`: a future seed run over a
  `legacy` row still replaces it (seed always wins); a future scheduled/constituents write against a NOW-labelled
  row is refused, same as against a `seed`/`scheduled`/`constituents` row today.
- **Not in scope of this act.** No row that already carries any `classified_by` value (1,934 `scheduled` + 137
  `seed` = 2,071 rows) is touched, read for its own sake, or an input to this write. No `asset_class`,
  `sub_asset_class`, `name`, `instrument_kind`, `industry`, `last_updated` or `updated_by` value moves on any row.

## Rollback per key

`REMOVE classified_by` per written key -- the key list is exactly the 238 tickers named in
`R2_LABEL_CENSUS_20260930.json` `tickers[]` (the candidate set this half names), one `UpdateExpression: REMOVE
classified_by` per ticker, never a table-wide scan-and-filter. No pre-existing attribute is touched by the write
(proved by the additive-only `UpdateExpression` and the live `other_attributes_touched: 0` / `overwrites: 0`
census), so rollback restores each row to byte-identical its pre-write state (the removed attribute did not exist
before this act on any of the 238 keys).

## Live control proving the rule this write would obey

Unit tests (`infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`, 13 passed) exercise the exact
conditional-update call against a stub table that refuses precisely as DynamoDB would:
- `test_label_update_writes_only_classified_by`: the `UpdateExpression`/`ConditionExpression`/
  `ExpressionAttributeValues` sent are asserted verbatim (`SET classified_by = :v`,
  `attribute_not_exists(classified_by)`, `{":v": "legacy"}`) -- no other attribute name appears in the expression.
- `test_label_update_refuses_an_already_labelled_row`: a row already carrying `classified_by` raises
  `RowAlreadyLabelled` and is never overwritten.
- `test_label_update_cli_blocks_a_live_run`: the CLI's own `main([])` (no `--dry-run`) raises `SystemExit` naming
  the LOCAL-build bound -- this build's CLI has no live-write path at all.

No live write of any kind was performed against `etf-classifications` in this build; the numbers above come from a
real, read-only `--dry-run` scan.

## Known gaps, not widened here

- `instrument_kind` and `industry` remain whatever they already are on every one of the 238 rows (this act adds
  only `classified_by`) -- FWD-8's gap (cell SC-e-2, this worker's next order), unaffected either way.
- Whether any of the 238 rows is itself WRONG (a bad `asset_class`/`sub_asset_class`) is explicitly NOT decided
  here, per the CTO's own ruling (analysis @151c890591 section 1, "Not decided here: whether any of the 238 is
  wrong. That is FWD-2's job once they carry a label.").
- The constituents seeder's own `classified_by = "constituents"` write (build item 2 of this same cell) is a
  SEPARATE future act under its own existing conditional-put discipline (`attribute_not_exists(classified_by)`,
  unit-tested here too); it is not part of this half's write set and needs no additional sign-off beyond what its
  own pre-existing act already carries, since its condition and write-set shape are unchanged by this cell (only
  the labelled VALUE it sets is new).
