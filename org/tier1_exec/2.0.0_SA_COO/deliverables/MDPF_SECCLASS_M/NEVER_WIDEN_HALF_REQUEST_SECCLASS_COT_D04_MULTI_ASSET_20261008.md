# Never-widen half request, MDPF_SECCLASS -- Cottonwood's served client concentration stops carrying `multi_asset` (TO-SC-e67, round 12 row S60)

**Author:** `0.9.0_WK_MDPF_SECCLASS~57` (worker, L7), 2026-10-08, for `2.0.0_SA_COO~M1` to issue. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The deploy and the gold run are the issuer's acts, never the worker's. The worker edited one shipped gold file on its branch, ran a fixture test, and wrote nothing to S3.
Records: round-12 analysis section 3 item 1 (S60); Andrew-direct 2026-10-07 (no `multi_asset` class, six classes only); the 33-row remap `CTO_HALF_MDPF_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md`.

## Where `multi_asset` entered (traced, read-only)

D_04 (`data/cot/scripts/gold/D_04.client_portal_summary.py`, `build_client_timeseries` around line 1237-1285) does not classify: it copies the `concentration` list of C_06's per-relationship file `gold/entities/clients/{rid}.json` into `platinum/clients/{rid}/concentration.json` (line 1282). The class producer is **`data/cot/scripts/gold/C_06.client_mix_timeseries.py`**. Its incremental merge (`_merge_and_write`, `existing_conc = {e['date']: e for e in existing['concentration']}`) keeps every STORED date's holdings exactly as written. A date written while the canonical table (`etf-classifications`, read through `lib/etf_classifier.py`, which returns the table's `asset_class` verbatim) still read `multi_asset` for SGIIX kept that word after the 33-row remap fixed the table. No COT script holds a `multi_asset` literal (`comp-find`: 0 hits across 120 files of `data/cot/scripts`); the class input is STORED HISTORY. Measured entry: `platinum/clients/z09305621/concentration.json`, date 2026-10-05, SGIIX `asset_class: multi_asset`, market_value 25862.98.

## The act

Merge branch `wk-MDPF_SECCLASS-57` (`data/cot/scripts/gold/C_06.client_mix_timeseries.py` and the fixture test `data/cot/scripts/gold/tests/test_d04_no_multi_asset.py`) into a pushed range after both halves sign, then ship the COT gold code prefix (`.tools/safe_deploy_core.py` CODE_TREES `"gold": ("data/cot/scripts/gold", "code/gold/")`), so `s3://opal-data-cot/code/gold/C_06.client_mix_timeseries.py` moves; then ONE scheduled COT gold run publishes the corrected keys.

**The shipped code key(s) the fix moves:** `s3://opal-data-cot/code/gold/C_06.client_mix_timeseries.py` (38198 bytes at the live read 2026-10-07T04:16:43Z, ETag 75135f33950396de58f9f439b8ac66c3, VersionId `M.bUto2CRQ9XPSkdUiF_3wd3nlXsQdEM`, equal in size to the repo file at the base). The test file is a new key `code/gold/tests/test_d04_no_multi_asset.py`, inert (nothing in the gold chain imports it).

**The local candidate diff:** `git diff e6f1fdfc1f..wk-MDPF_SECCLASS-57 -- data/cot/scripts/gold/C_06.client_mix_timeseries.py` (27 lines added, none removed): (1) `RETIRED_CLASS = 'multi_asset'` and `reclass_retired_holdings(holdings, classifier=None)`: a holding carrying it takes the canonical class by ticker (`ETFClassifier.classify_position`), else `unclassified`, never a new word; every other holding is returned as the same object; (2) in `_merge_and_write`, the stored `existing_conc` entries pass through that function before the new dates merge in; (3) in `process_date`, a freshly classified row the table still reads `multi_asset` is published as `unclassified`. D_04 is not edited: its copy is clean once its input is.

## Blast radius

Keys the act may touch, measured by a read-only GET scan on 2026-10-08 (`opal-data-cot`, versioning Enabled): every `platinum/clients/*/concentration.json` (227 keys read, 0 errors) and every `gold/entities/clients/{rid}.json` (453 keys read, 0 errors).
- `multi_asset` appears in **exactly two relationships, one holding each, ticker SGIIX**: `z09305621` and `z09305679`.
- Served keys the act changes: `platinum/clients/z09305621/concentration.json` (VersionId `HvI4KbR9dmlcN27zMJxrUxKNGl_CtZFh`, LastModified 2026-10-07T11:40:06Z) and `platinum/clients/z09305679/concentration.json` (VersionId `SB3cb7Pd1MO6NWHXoGgTenwztoIgCtx7`, 2026-10-07T11:40:05Z).
- Their upstream copies, also changed: `gold/entities/clients/z09305621.json` (VersionId `gEa6W9aEBVT7.H2fXgQ_WgvrK4wAFAux`), `gold/entities/clients/z09305679.json` (VersionId `MVKFjFO9rI66_eYoaRRG7WyqvV7nzMdT`), and the C_06 legacy dual-write `gold/client_timeseries/z09305621.json` (VersionId `BYxgreaMAHPYmrN9JsK5tdM6mG5w0f6n`) and `gold/client_timeseries/z09305679.json` (VersionId `GOdbZnDXz32Tk62llrMDFNMZm7gnqDtz`), each of which holds the word once.
- The delta per key: the one holding's `asset_class` moves from `multi_asset` to the canonical class (`equity` for SGIIX; `_shared/etf_classification.ETF_CLASSIFICATIONS['SGIIX']` reads `equity` in the repo and the canonical table holds 0 `multi_asset`). Every other holding, every `market_value`, `pct`, `mix` and `date` is untouched (fixture-proven: the unrelated ticker's class and object are unchanged). C_06 also rewrites every other relationship's file on a run that carries new dates, with the same bytes apart from `generated_at`, as it does every night.
- **Not touched:** the `mix` series. A `multi_asset` holding was never a `MIX_ASSET_CLASSES` key, so those dates' stored `mix` omit its share (their pct sum is below 1.0); this act does not recompute them. Flagged for the signers, not changed.

**Writers counted (N printed):** the served concentration keys have N = 1 writer (D_04 `build_client_timeseries`, a copy of C_06's list); the gold and legacy keys have N = 1 (C_06 `_merge_and_write` / the full-build writer). Two C_06 write paths exist (incremental merge, full build); the full build recomputes every date from the table, the incremental merge is the path that carried stored history, and the fix covers the incremental path plus the new-row path both paths share. The rule of each writer was read at signing-prep.

## Branches (both covered)

**Branch A -- the two relationships are present in the run (SGIIX held, the table reads `equity`):** the next scheduled run rewrites the six keys above with SGIIX at `equity`; a GET of the two `concentration.json` files reads 0 `multi_asset`.
**Branch B -- SGIIX is absent from a relationship's new dates, or the relationship has no new date in the run:** its stored file is not rewritten by the incremental path and the old word stays in that key until a run carries a new date for it, or until one full build (`C_06 --upload` without `--incremental`, which recomputes every date from the table). The post-run scan reads which of the six keys still carry it, and the signers decide whether the one full build is run. A stored holding whose ticker the table does not hold (or is null) reads `unclassified`, the named residue; the fixture proves it.
**Branch C -- the table is changed back to `multi_asset` for a ticker (not reachable by this act):** the new-row guard publishes `unclassified`, never the word.

## Timing input

The COT gold chain fires on its schedule, `cron(30 10 * * ? *)` UTC, and its last run wrote these keys at 2026-10-07T11:38Z-11:40Z (the CloudOps session log of 2026-10-08 reads the gold run log at 11:40:13Z). The code ship must land before the fire it is meant to serve; a ship landing after 10:30Z serves from the NEXT day's run. The deploy is a code-prefix upload, not a data write; the data write is the scheduled run.

## The hold

**The deploy waits on Andrew's limit item 5 (routes-host), which today denies dell1 any `opal-data-cot` code write.** Until item 5 clears, no seat on dell1 can upload `code/gold/C_06.client_mix_timeseries.py`; this half is signed for the act and the release is held behind that item. The worker wrote nothing to S3.

## Rollback per key

Rollback per key, by prior VersionId (bucket versioning Enabled, read 2026-10-08):
- code key `code/gold/C_06.client_mix_timeseries.py`: copy VersionId `M.bUto2CRQ9XPSkdUiF_3wd3nlXsQdEM` back over the key (or revert the merge commit, which also removes the test);
- served and upstream data keys: each restores its recorded pre-act VersionId listed under Blast radius (`HvI4KbR9d...`, `SB3cb7Pd1...`, `gEa6W9aEB...`, `MVKFjFO9r...`, `BYxgreaMA...`, `GOdbZnDXz...`). The issuer re-reads each VersionId at the act's start and records it in the deploy ledger entry.
No other key is touched, so no other key needs a rollback.

## Acceptance (after the act, if run)

1. A GET of `platinum/clients/z09305621/concentration.json` and `.../z09305679/concentration.json` reads 0 `multi_asset`, and the SGIIX entries read `equity`.
2. A scan of all `platinum/clients/*/concentration.json` and `gold/entities/clients/*.json` reads 0 `multi_asset` (denominator printed; Branch B names any key still carrying it).
3. Every other holding in the two files reads byte-equal to the pre-act snapshot except `generated_at`.
4. `python data/cot/scripts/gold/tests/test_d04_no_multi_asset.py` via pytest: 4 passed.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
