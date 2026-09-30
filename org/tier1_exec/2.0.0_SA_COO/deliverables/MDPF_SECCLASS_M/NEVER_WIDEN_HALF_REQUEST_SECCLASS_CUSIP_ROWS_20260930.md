# Never-widen half, MDPF_SECCLASS SC-e-9 -- the FIRST CUSIP-keyed writes to `etf-classifications`
# (CTO RULING 103137 hold, RULING 103140 key design, option a)

**Author:** 0.9.0_WK_MDPF_SECCLASS~4, 2026-09-30. **For:** the issuer (2.0.0_SA_COO~M) to sign and
send, same "never widen without a named blast radius + rollback per key" discipline as the round-1
and round-2 halves and CLAUDE.md HARD STOPS section 5.

**Status of the act described here: NOT YET RUN.** SC-e-9 is a LOCAL build + record cell: no table
write happened in this cell. This half covers the FIRST write of `ticker = "CUSIP:<9 chars>"` rows
into the live `etf-classifications` table -- a new key SHAPE the table has never carried before
(measured live 2026-09-30: 0 of 2,309 rows start with `CUSIP:`). The evidence file is
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CUSIP_CENSUS_20260930.json`.

## The act

One ordered step, plus the readers this half requires guarded FIRST:

1. **Guard the readers named below** (candidate diffs, not yet applied -- each is a small, additive
   filter on an existing Scan/Query, never a rewrite of the reader's logic):
   - `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (and its two byte-identical
     copies at `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/`
     and `.../yang-generate-positioning/`): `find_by_asset_class`/`find_by_sub_asset_class` must add
     a filter excluding `identifier_namespace == "CUSIP"` from their Query results (both GSIs are
     `projection_type = "ALL"`, so the attribute is already projected -- a client-side filter is
     sufficient, no index change). These two methods are uncalled in-tree today, so this guard has
     zero current behavioral effect; it closes the gap before any future caller appears.
   - `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` and
     `seed-etf-constituents.py`: `read_existing()`'s full Scan should exclude `identifier_namespace
     == "CUSIP"` rows from the printed merge-baseline count (`PRE-READ: N existing row(s)` /
     `EXISTING rows in %s: %d`) -- count-only exposure today (neither script's write loop is driven
     by the existing map, only by its own frozen literal ticker list, so a CUSIP row is never itself
     written or touched), but an accurate count matters for anyone reading these logs as an audit
     trail.
   - `data/black_diamond/scripts/classification/seed_bd_securities.py`: **the one real risk.** Its
     `seed()` does an UNFILTERED full Scan of `etf-classifications` and `put_item`s every row
     verbatim into `bd-securities`. Without a guard, a CUSIP-keyed row is copied into
     `bd-securities` under the identical `CUSIP:<...>` key -- a table with no `identifier_namespace`
     concept, whose own readers (the COT and opal-partners-data `etf_classifier.py` copies, and
     `classify_bd_securities.py`) key everything by ticker or `NAME::` slug. The guard: skip any
     item whose `ticker` starts with `CUSIP:` before the copy loop. This script is a one-time,
     re-runnable seed (not on a schedule); the guard must land before its next run, whenever that is.
   No other reader needs a guard: every per-ticker `get_item`/`classify()` consumer (Positioning's
   two Lambdas, `etf_positioning_publisher.py`, the 49F satellite builders, the BD gold family, BD's
   own `etf_classifier.py`) looks up an EXACT key the caller already knows -- a raw, unprefixed CUSIP
   never collides with the new `CUSIP:`-prefixed key, so these are unaffected, not guarded.
   Full reader-by-reader disposition: `R2_CUSIP_CENSUS_20260930.json` `readers` (18, denominator
   printed) and `not_a_reader_of_etf_classifications_today` (2 `etf_classifier.py` copies that
   default to `bd-securities`, not the target table, today).
2. **Write (candidate rows, not yet applied):** conditional `put_item` (`attribute_not_exists(ticker)`,
   the identical mechanism the ticker path already uses -- no table/schema change) for the 349 rows
   `R2_CUSIP_CENSUS_20260930.json` plans: 113 of 49financial's 173 held no-ticker-valid-CUSIP bonds
   (evidenced only by the security master's own `rate_bearing` flag -- `security_type` is absent
   live from that firm's `dim_security`), 236 of cottonwood's 339 (evidenced by the custody
   `SEC Asset Type` enrichment field), 0 of inflection's 9 valid-format candidates (no security-type
   evidence reaches any of them; 16 more are Orion-masked CUSIPs, rejected as invalid by design, never
   candidates at all). Every row's `classified_by = "scheduled"`; every `asset_class`/`sub_asset_class`
   pair is a DIRECT vocabulary member (measured against the live table at build time), never a fold.
   **overwrites: 0, guessed: 0** (measured, not assumed).

## Evidence (this cell's real local build, 2026-09-30, LOCAL, no table write)

`R2_CUSIP_CENSUS_20260930.json`:
- `table_rows_at_build: 2309` (live DynamoDB scan of the `ticker` key, matches release step 2's
  count; no `CUSIP:`-prefixed key exists yet).
- `reader_denominator: 18`, every reader's `path`/`how`/`surfaces_cusip`/`guard` printed; 3 need the
  guard above, 15 do not (single-key lookups, or already-by-design absorption in this very module's
  own `existing_tickers()`/`TableVocabulary.from_live_table()`, which MUST see CUSIP rows for the
  absence check and the vocabulary to stay correct).
- `would_write: 349`, `rows` (349, each with `ticker`, `identifier_namespace`, `asset_class`,
  optional `sub_asset_class`, `classified_by`, `name`, `input`, `firm`), `unresolved` (241, each with
  `cusip`, `name`, `reason`, `firm`), `overwrites: 0`, `guessed: 0`.
- Per-firm sourcing (`per_firm_summary`): 49financial via
  `opal-data-49financial:gold/advi/canonical/canonical_positions/date=2026-09-28` JOIN
  `gold/advi/dimensions/dim_security/date=2026-09-28` ON `security_key`; cottonwood via
  `opal-data-assets:blackdiamond/cottonwood/silver/fact_holdings/date=2026-09-28` JOIN
  `blackdiamond/cottonwood/silver/fact_transactions/*` (SEC Asset Type, last-seen per AssetID) ON
  `AssetID`; inflection via `opal-data-inf:gold/holdings/2026-09-25.parquet` held tickers with
  `silver/transactions/2026-09-27.parquet` product names, Orion-masked CUSIPs excluded per
  `data/inf/scripts/gold/lib/display_label.py`'s own documented mask format.

## Blast radius

**What this act touches:** ONLY new rows under a key shape (`CUSIP:<9 chars>`) no existing row has
ever occupied -- `attribute_not_exists(ticker)` makes an accidental overwrite of an EXISTING row
structurally impossible, exactly as the ticker-keyed scheduled path already relies on. No existing
row's `asset_class`, `sub_asset_class`, `classified_by`, or any other attribute changes.

**Who reads the new rows, and how each is affected (both branches, per HARD STOPS section 5):**
- **A CUSIP row that gets written:** appears in `get_item(Key={"ticker": "CUSIP:<cusip>"})` results
  for any future caller that knows to ask for it by that exact key (the follow-on below); appears in
  the two guarded Query methods' results ONLY if the guard above is skipped (named, not applied here);
  is copied into `bd-securities` by `seed_bd_securities.py` ONLY if that guard is skipped.
- **A CUSIP row that stays unresolved (241 of them):** no row is written, so no reader is affected at
  all -- the security remains exactly as unclassified as it is today, under its own listed `reason`.
- **A ticker-keyed row (the other 2,309):** entirely untouched -- this act adds rows, it never
  reads-then-rewrites an existing one, and the readers above that already existed before this cell
  keep returning the exact same values for every ticker key they already served.

**Follow-on this half does NOT cover (named, not widened here):** the IRPT Holdings classifier that
would look up a bond node by `CUSIP:<cusip>` is an IRPT_BCKEND cell, not built yet -- measured
2026-09-30: no `etf_classifications_dynamodb`/`ETFClassifier` import exists anywhere under
`infra/aws/lambda/investor-reporting`. Until that cell lands, these 349 rows are written but
UNCONSUMED by Holdings; they are, however, immediately visible to the three per-ticker/per-key
readers above that would look one up by its exact `CUSIP:<cusip>` key if ever asked.

**A `bd-securities` value never writes an existing `etf-classifications` row (Andrew-direct
2026-09-30 ~02:2xZ):** none of the 349 planned rows are seeded from `bd-securities`/legacy-fork
evidence in this build (the resolved sources are the security master's `rate_bearing` flag and the
custody `SEC Asset Type` field only) -- `classify_cusip_asset_class`'s legacy-fork branch exists and
is tested (`test_fold_only_bd_value_leaves_cusip_unresolved`) but did not fire for any of the 349.
Per the standing ruling, were it to fire in a later run, it can only ever SEED a brand-new
`CUSIP:`-keyed row (the same `attribute_not_exists` gate), never touch an existing one; there is no
case in this build where a legacy-fork value would write into an existing row, so no such write is
named here for Andrew's decision.

## Rollback per key

- **No table write yet:** this cell wrote nothing; there is no rollback to perform for THIS commit.
- **Once the write above runs:** each new row is its own DynamoDB item at a key (`CUSIP:<cusip>`) no
  other row shares -- rollback is `delete_item(Key={"ticker": "CUSIP:<cusip>"})` for exactly the
  rows this write created (the 349 `ticker` values listed in `R2_CUSIP_CENSUS_20260930.json`'s
  `rows`), independent of every other row and every ticker-keyed row (deleting a `CUSIP:`-keyed item
  cannot affect a ticker-keyed item's key, since the two key spaces cannot collide by construction --
  RULING 103140's own guarantee). `etf-classifications` carries point-in-time recovery
  (`infra/aws/terraform/yang-pipeline/etf-classifications.tf`), a second, table-wide restore path
  independent of the per-key deletes above.
- **Reader guards (once applied):** each is an additive filter clause on an existing Scan/Query or an
  additive skip in a copy loop -- rollback is reverting that one file to its pre-guard commit; no
  guard changes what any of these scripts write today (only what a CUSIP-shaped key is allowed to
  surface in), so reverting a guard is a pure code rollback with no data-side effect.

## COO half -- [PENDING SIGNATURE]

## CTO half -- [PENDING SIGNATURE]

## Guard (SC-e-11)

Live dry-run against the real `etf-classifications` and `bd-securities` tables (read only; Scan only), 2026-09-30, by
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_cusip_guard_dryrun.py`:

```
CUSIP-GUARD etf_rows=2309 cusip_rows=0 bd_rows=10929 bd_delta_from_cusip=0
CUSIP-GUARD-PLANNED planned=349 would_copy_to_bd=0
```

- **The guard:** `data/black_diamond/scripts/classification/seed_bd_securities.py` -- `is_cusip_row` at lines 43-45
  (prefix constant at line 40) and the skip in the copy loop at lines 75-78, before the `put_item` write path; the skip is
  counted and printed as `skipped_cusip=<n>`. Negative control: with the guard removed, all 349 planned `CUSIP:` rows
  would copy (the dry-run prints this on stderr as `control: unguarded planned copy would be 349`).
- **The test:** `data/black_diamond/scripts/classification/tests/test_seed_bd_securities_cusip_guard.py` (stub DynamoDB,
  no network).
- **Standing condition:** the CUSIP_ROWS act is REFUSED unless a fresh dry-run immediately before it prints both counts
  (`bd_delta_from_cusip` and `would_copy_to_bd`) as 0.
