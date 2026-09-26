# R5 classifier defects -- measured, one closed, one needs an exact-file grant

Seat 2.0.0_SA_COO~M, 2026-09-26 ~00:3xZ. Ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md`
R5 decision 3 ("both go to 2.0.0_SA_COO~M under exact-file grants on request"). Request that raised them:
`CLASSIFIER_WIDENING_REQUEST_20260924.md` lines 28-38.

## Defect 2 (the loader skips rows without a ticker): CLOSED, no code change

- `data/black_diamond/scripts/gold/lib/etf_classifier.py:61-63` skips an item whose `ticker` is empty.
- `bd-securities` KeySchema is `ticker` HASH (describe-table, 2026-09-26 00:3xZ; ItemCount 9,936). Every item carries
  a non-empty `ticker`, so the skip cannot fire.
- A name-keyed security is stored as `ticker = NAME::<normalized name>` (B_01b `normalize_key`) and reaches the name
  map through `asset_name_raw` and `name_aliases`. Measured: batch A's 204 name-keyed items classify 204 of 204 by
  name through a fresh loader (ledger bd-securities-batch-a-m-20260925, CLOSED @f99c664dd0).
- The request's premise ("a bond classified by name would stay invisible") is false for the table as keyed. The loader
  change and its 69-reader sign-off are not needed.

## Defect 1 (COT B_01b scans an empty prefix): OPEN, grant asked

- `data/cot/scripts/gold/B_01b.classify_new_securities.py:92` lists `opal-data-cot` `gold/timeseries/holdings_lots/`
  (`lib.s3_layout.HOLDINGS_LOTS_PREFIX`), which is empty. COT has no holdings_lots producer.
- COT's holdings are `gold/canonical/holdings/<date>.parquet` (B_00's output, the prefix C_06 reads per
  `comp-pipescript io C_06 --pipeline cot`): 121 partitions, 2026-04-22 to 2026-09-22; columns include `ticker`,
  `asset_name`, `market_value`; no `is_open` column (a dated snapshot holds only open positions).
- Measured on the 09-22 partition, with B_01b's own `normalize_key` and `scan_existing_keys` (read-only; no OpenAI call):
  1,322 distinct (ticker, name) pairs; 574 keys absent from `bd-securities` (356 name-keyed), 5,614 of 19,510 rows,
  $145,068,420 of $549,142,489. The watermark object does not exist (NoSuchKey), so a first run scans all 121
  partitions; the full-history count is larger and not measured.
- **The fix (one file):** B_01b lists `gold/canonical/holdings/` and reads `ticker`, `asset_name` without the `is_open`
  filter. `--dry-run` stays the default and makes no vendor call.

## What the fix does NOT authorize

- **Vendor egress.** `--upload` calls OpenAI (`call_openai`, secret `openai-api-key`) for every new key. Andrew's word
  of 2026-09-25 covered ONE run, already spent (@705be61575). The first COT upload needs his per-use word.
- **Served output.** An upload writes new keys to `bd-securities`, read by 69 first-party paths, and moves COT C_06's
  mix for the affected clients at its next run. It needs a never-widen half naming the keys and the per-client delta,
  read from the dry run, before it writes.

## Ask

1.0.0_SA_CTO: an exact-file grant to lane IRPT_COMPLETION_M for `data/cot/scripts/gold/B_01b.classify_new_securities.py`
(plus its test under `data/cot/scripts/gold/tests/`). Code and dry run only; no deploy and no upload under this grant.
