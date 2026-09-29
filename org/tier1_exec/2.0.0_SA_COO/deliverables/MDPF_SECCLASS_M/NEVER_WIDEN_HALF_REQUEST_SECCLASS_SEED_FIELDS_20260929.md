# Never-widen half, MDPF_SECCLASS.TO-SC-k2 (cell SC-k-2) -- the etf-classifications seed run that writes instrument_kind and industry (and the held-back PHYS row)

**Author:** 0.9.0_WK_MDPF_SECCLASS~2, 2026-09-29. **For:** the issuer (2.0.0_SA_COO~M) to sign and send, per
`.tools/prd-signoff.py`-style precedent -- this is a table-write sign-off, not a served-bytes move, but the same
"never widen without a named blast radius + rollback per key" discipline applies (CLAUDE.md HARD STOPS section 5).
**Status of the act described here: NOT YET RUN.** This task order is a LOCAL build + record: the census below was
produced with `--dry-run` against the LIVE table (read-only scan + S3 GetObject); nothing was written. This half
covers the FIRST real run of `seed-etf-classifications.py` (no flags needed -- `class_changes` is 0, so no
`--accept-module-truth` is required) followed by `seed-etf-constituents.py` (its own conditional per-row puts).

## The act

Two writes, in order, against the live DynamoDB table `etf-classifications` (344 rows today):

1. `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py --region us-east-1` -- merges the
   module (`etf_classification.py`, now carrying `instrument_kind`, `industry`, and IB-mr-251's PHYS row) into every
   one of 137 module tickers. Sets `classified_by = "seed"` on every row it writes (unconditional provenance, like
   `last_updated`/`updated_by`). No `--accept-module-truth` needed: the live census shows zero `asset_class`
   conflicts (`class_changes: []` in the census JSON below).
2. `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py --region us-east-1` -- writes
   `instrument_kind` (`single_security` for a stock, `fund` for the two money-market funds SALXX/FXFXX, absent for
   the CASH residual line) to its own 167-ticker universe, via a PER-ROW conditional put
   (`ConditionExpression="attribute_not_exists(classified_by)"`, RULING 103050): it never sets `classified_by` itself
   and refuses (does not write) any row the seed path already owns. `--force-names` is NOT part of this act (name
   stays preserved on the 157 already-existing constituent rows; only the 10 net-new tickers get a full row).

Evidence -- the exact seed-vs-live diff this act would produce, computed by running both seeders' own merge logic
(`merge_item`/`build_row`) against a live read of the table (candidate write set, not yet applied):
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_SEED_FIELDS_CENSUS_20260929.json`
-- `seed_rows: 302`, `live_rows: 344`, `class_changes: 0`, `other_diffs: 88`.

## Blast radius

**Readers of `etf-classifications`, both branches, each field this act touches:**

1. **`yang-generate-positioning` (Positioning surface 1).** `registry_field(ticker, field, default)` reads ONE named
   key at a time (`classification.get(field)`); it never enumerates the item's keys. Adding `instrument_kind`,
   `industry` and `classified_by` is INERT to it -- nothing here reads those names.
   - **A ticker it already classifies, value unchanged:** identical output.
   - **A ticker it already classifies, value changed (BNDX only, see below):** `sub_asset_class` for BNDX changes
     from `Intermediate` to `International` in Positioning's attribution hierarchy. This is a PRE-EXISTING drift
     this cell's census surfaces, not something instrument_kind/industry caused; the module has carried
     `'BNDX': 'International'` unchanged by this cell (`git blame` shows this line predates TO-SC-k2).
   - **A ticker not yet classified:** unaffected (falls back to its own default, unchanged either way).
2. **`yang-generate-holdings-attribution` (Positioning surface 2).** Same pattern: `classification.get('asset_class',
   ...)` / `.get('sub_asset_class', ...)` by explicit key. Same BNDX exposure as above; no other live ticker's
   `asset_class` changes (`class_changes: []`).
3. **The IR Holdings producer, AFTER IB-mr-251 lands (currently HELD, not on CLOUD).** Once 251 drains, `Holdings`
   reads `etf-classifications` through the same `ETFClassifier`/`resolve()` client. The PHYS row this cell adds is
   BYTE-IDENTICAL to 251's own seed-source addition (`git show 40b86ffab3` vs this cell's diff) -- when 251 merges,
   the two copies of the same five dict entries collide harmlessly (identical text, no conflict). 251's own
   never-widen half (not this one) covers its classifier-swap and refusal-on-unknown behavior; this half covers only
   the field-write act above.

**Every listed class change:** `class_changes: []` (empty) -- zero rows change `asset_class`. The one real live
VALUE change in `other_diffs` that is not `instrument_kind`/`industry` is:
  - `BNDX.sub_asset_class`: live `Intermediate` -> seed `International` (pre-existing drift, unrelated to this
    cell's two new fields, first surfaced by this census).
  - `CASH.name`: live `Cash & Cash Equivalents` -> derived `Cash & Other Assets` -- NOT written by the constituents
    seeder's default run (name is only rewritten under `--force-names`, which is not part of this act).
The other 86 `other_diffs` entries are net-new tickers (live value `None` for every field) that do not yet have a
row at all (e.g. `DFAC`, `EVNT`, `ACSG`, `IXJ`, ... -- module additions that predate this cell); creating their rows
is additive, not an overwrite of anything served.

**What every OTHER live row gets, additively:** 302 of 344 rows gain `instrument_kind` (and WMT alone gains
`industry`); 42 rows (344-302) are either cash/cash-equivalent lines excluded from this field's own MECE domain
(`CASH_USD`, `CASH`) or rows neither seeder's ticket universe currently names.

## Rollback per key

DynamoDB `etf-classifications` is NOT S3-versioned; rollback is per-attribute, per-ticker, using the PRE-READ scan
this same run performs (`read_existing(table)`, printed as `PRE-READ: N existing row(s)` before any write) as the
"before" snapshot, plus the census file above as the durable record of every value this act would change:

- **To undo the two new fields on every touched row:** `UpdateItem` with
  `REMOVE instrument_kind, industry, classified_by` (constituents-seeder-written rows never carry `classified_by`,
  so that clause is a no-op there) for every ticker in the census's `kinds` map (302 keys) -- returns every row to
  its exact PRE-READ state, since these three attributes did not exist before this act.
- **The one real value candidate, BNDX:** `UpdateItem SET sub_asset_class = :v` with `:v = "Intermediate"` (the
  PRE-READ value) restores it; the census's `other_diffs` entry is the durable record of both the before and after
  values.
- **A net-new row (e.g. `DFAC`):** `DeleteItem {"ticker": "DFAC"}` removes it entirely -- it did not exist before
  this act (PRE-READ confirms absence).
- **`CASH.name`:** not written by this act (guarded by `--force-names`, not part of the act above); no rollback
  needed unless a LATER, separately-signed `--force-names` run lands it, at which point the same PRE-READ value
  (`Cash & Cash Equivalents`) is the rollback candidate.
