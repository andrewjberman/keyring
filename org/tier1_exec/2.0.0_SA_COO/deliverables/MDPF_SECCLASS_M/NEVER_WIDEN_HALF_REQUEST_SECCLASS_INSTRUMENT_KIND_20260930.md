# NEVER-WIDEN HALF REQUEST -- MDPF_SECCLASS FWD-8 instrument_kind population (SC-e-2)

**Requesting seat:** `0.9.0_WK_MDPF_SECCLASS~5` (worker of `2.0.0_SA_COO~M`), task order `MDPF_SECCLASS.TO-SC-e2`.
**For:** the CTO+COO never-widen sign-off on the ONE additive conditional `instrument_kind` update this cell names
but does NOT execute (LOCAL build + record bound -- no table write). The numbers below are measured LIVE at build
time (`infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py --dry-run --source constituents`, real
DynamoDB reads, 2026-09-30 ~04:xxZ), and recorded in
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_KIND_CENSUS_20260930.json`.

## The act

For every row of `etf-classifications` that (a) carries NO `instrument_kind` attribute AND (b) is a ticker the
served ETF constituents feed (`s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`, read via
`seed-etf-constituents.py`'s `load_constituents()`) can determine a kind for, run ONE additive conditional update
per ticker:

```
UpdateExpression:     SET instrument_kind = :v      (:v = "fund" | "single_security")
ConditionExpression:  attribute_not_exists(instrument_kind)
```

No other attribute is named in the `UpdateExpression`, so no other attribute can ever be touched by this call --
`set_kind_if_absent()` / `set_kind_only_if_absent()` hard-code the expression, they are not built from a
caller-supplied field list. The value is never a default: a row whose kind cannot be determined from the named
source is excluded from `rows`, not guessed.

Measured scope of this act (`R2_KIND_CENSUS_20260930.json`, live scan, `set-instrument-kind.py --dry-run --source
constituents`):

| table_rows_at_build | rows_absent_kind | would_set (this act) | defaulted | from_bd_securities (excluded) |
|---|---|---|---|---|
| 2,309 | 2,163 | 156 | 0 | 1,970 |

Of the 156: 154 `single_security`, 2 `fund` (the constituents feed's two money-market mutual-fund tickers). One
more constituent ticker, `CASH`, is a derived NAV-residual line the feed itself resolves to no kind
(`instrument_kind_for("CASH") -> None`) -- excluded from `rows`, not defaulted, same rule the constituents seeder
already applies to its own new-row writes. The remaining 36 absent-kind tickers have no candidate source named in
this build at all (mostly foreign-listed ADR/local-exchange tickers on `scheduled` rows -- not in the constituents
feed, not in the per-firm securities classifier table either) and are simply left absent; a future source, if one
is found, is a separate act.

**Why 1,970 rows are named but NOT written here (`from_bd_securities`):** those 2,163-156-1-36=1,970 absent-kind
tickers ARE resolvable to a kind today, but only from the estate's per-firm securities classifier table (an
LLM-derived `asset_class`/`sub_asset_class`/name field, not `instrument_kind` itself, but sufficient to infer one).
Every one of them is an EXISTING `etf-classifications` row (1,934 `scheduled` + a handful `legacy`/no-label). Per
Andrew-direct 2026-09-30 ~02:2xZ ("yes, bd-securities values can seed new rows. THey just don't overwrite existing
rows"), a value from that table may seed a brand-new row and must never write into a row that already exists. This
act never reads or writes that table (see `set-instrument-kind.py`'s own docstring and
`test_no_bd_securities_reference`, which this build's grant does not touch or loosen). The 1,970 are counted here
so the gap is visible and decided, not silently narrowed to "156 done, rest unknown."

## Blast radius

- **The rows.** Exactly the 156 tickers `R2_KIND_CENSUS_20260930.json` `rows[]` names, each gaining exactly one
  new attribute: `instrument_kind`. Zero existing attributes on any row are touched (`defaulted: 0`; the
  `UpdateExpression` itself names no other attribute, proved by unit test
  `test_only_instrument_kind_changes` / `test_kind_only_mode_touches_no_other_attribute_on_the_constituents_seeder`,
  `infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py`). `classified_by` is never read or
  written by this act, regardless of whether the row is `scheduled`, `legacy`, `seed` or `constituents` --
  the write is orthogonal to that column by construction.
- **Readers of `instrument_kind`.** Per the contract's own token census (`org/standards/MDPF_SECCLASS_CONTRACT.json`
  v0.2.0, `rule24_record.token_census`), no reader in `infra/aws/lambda/v2_portal`, `data/**/*.py` or `portal/src`
  branches on `instrument_kind` today (0 hits at that census). This act therefore changes no downstream behavior
  yet; it only makes the attribute present on 156 more rows for a future reader (the holdings-table ordering use
  named in the contract) to find.
- **`find_by_asset_class` / `find_by_sub_asset_class` callers** (the one client,
  `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`): unaffected -- neither method reads or
  returns `instrument_kind`, and this act changes no `asset_class`/`sub_asset_class`/`classified_by`/`name` value
  on any row.
- **Not in scope of this act.** The 1,970 `from_bd_securities` rows (no write, no read of that table). The 36
  `unresolved_no_source` rows (no candidate named). The `CASH` row (feed-determined absence, not a candidate).
  The 146 rows that already carry `instrument_kind` (135 `fund` + 11 `single_security`, untouched -- the
  condition refuses them by construction).

## Rollback per key

`REMOVE instrument_kind` per written key -- the key list is exactly the 156 tickers named in
`R2_KIND_CENSUS_20260930.json` `rows[].ticker`, one `UpdateExpression: REMOVE instrument_kind` per ticker, never a
table-wide scan-and-filter. No pre-existing attribute is touched by the write (proved by the additive-only
`UpdateExpression` and the live `defaulted: 0` census), so rollback restores each row to byte-identical its
pre-write state (the removed attribute did not exist before this act on any of the 156 keys).

## Live control proving the rule this write would obey

Unit tests (`infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py`, 7 passed) exercise the exact
conditional-update call against a stub table that refuses precisely as DynamoDB would:
- `test_only_instrument_kind_changes`: the `UpdateExpression`/`ConditionExpression`/`ExpressionAttributeValues`
  sent are asserted verbatim (`SET instrument_kind = :v`, `attribute_not_exists(instrument_kind)`,
  `{":v": "single_security"}`) -- no other attribute name appears in the call.
- `test_row_with_existing_kind_is_refused` / `test_constituents_kind_only_mode_refuses_existing_kind`: a row
  already carrying `instrument_kind` raises `KindAlreadySet` and is never overwritten.
- `test_unknown_kind_is_refused_before_any_write`: a kind outside the contract's two values raises `UnknownKind`
  before `update_item` is ever called (`table.calls == []`) -- no default, no guess.
- `test_rows_from_constituents_feed_excludes_undetermined_kind`: a feed ticker whose kind cannot be determined
  (e.g. a cash-residual line) is excluded from the plan, not defaulted.

No live write of any kind was performed against `etf-classifications` in this build; the numbers above come from a
real, read-only `--dry-run` scan against the live table (2,309 rows, matching `describe-table` `ItemCount`).

## Known gaps, not widened here

- The 1,970 `from_bd_securities` rows and the 36 `unresolved_no_source` rows stay absent after this act. Andrew's
  own word decides whether the per-firm classifier table's data may ever be used to CORRECT an existing row (a
  different question from seeding a new one, and explicitly not answered by the 2026-09-30 ~02:2xZ ruling) --
  that decision, not a script change, is what would close the 1,970 gap.
- Whether any of the 156 `single_security`/`fund` determinations is itself wrong is not decided here; the value
  is taken as-is from the same `instrument_kind_for()` logic the constituents seeder already uses for its own new
  rows (SC-e-1), not re-derived by this act.
- The `identifier_namespace` field (round-3, E9, CUSIP-keyed rows) is untouched by this act.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-09-30 ~07:1xZ)

Signed on the blast radius above, against TO-SC-e2 drained @d8b716a044. The issuer re-ran the criteria on CLOUD at
@bc13447e97: 7 passed, KIND-CENSUS would_set=156 of 2163 absent, HALF-READY, proof VALID.

**The act, exactly (the issuer runs it):**
- **Write set.** The 156 tickers of `R2_KIND_CENSUS_20260930.json` `rows[]`, one conditional update each:
  `SET instrument_kind = :v` on `attribute_not_exists(instrument_kind)`, with :v from the census row (154
  single_security, 2 fund). No other attribute is named. The 1,970 rows a bd-securities value could fill are NOT
  written: Andrew-direct 2026-09-30 ~02:2xZ, "bd-securities values can seed new rows. THey just don't overwrite
  existing rows."
- **Writers of the property: 2** exist (the seed path writes `instrument_kind` on seed rows; this update script).
  Only the update script runs in this act. Two rules were read: this update's condition, and the seed path's
  replacement of a whole seed row. None of the 156 is a seed row: a live batch read at signing (156 of 156 read)
  shows every one carrying no `classified_by` (the LEGACY_LABEL act's candidates) and 0 already carrying a kind. The
  two acts touch disjoint attributes on the same rows, in either order.
- **Both branches.** An absent-kind row gains its kind. A row that gained a kind since the census refuses and is
  counted, never overwritten. No reader branches on `instrument_kind` today, so no served value moves.
- **Ledger.** Opened before the first write with a PRE-READ of the 156 rows; closed at the read-back (set, refused,
  denominator).
- **Rollback.** `REMOVE instrument_kind` per written key, from the read-back's written list, never a scan.
