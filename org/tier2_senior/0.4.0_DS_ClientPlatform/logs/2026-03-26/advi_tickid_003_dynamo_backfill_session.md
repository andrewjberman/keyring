# ADVI_TICKID.003 -- DynamoDB Name Alias Backfill Session Log

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-03-26
**Project:** ADVI_TICKID
**Task Order:** ADVI_TICKID.003.ds-dynamo-name-alias-backfill.md

---

## Deliverable

Created `data/black_diamond/scripts/classification/backfill_name_aliases.py`.

## Design

For each resolved (asset_name, ticker) in ticker_resolution.parquet:
1. Look up bd-securities item with PK = resolved_ticker (ticker-keyed only)
2. Skip NAME::-keyed stub items (not updated)
3. Skip items where all aliases already present (idempotent)
4. `UpdateItem` with `ADD name_aliases :names` (DynamoDB StringSet atomic add)
5. Both raw and normalized forms of the BD asset name are added

### Edge Cases Handled
- Ticker-keyed item doesn't exist: skipped with count
- NAME::-keyed stubs: excluded from scan results entirely
- name_aliases already contains the name: DynamoDB ADD is idempotent, but we skip the call if no new names to save WCU
- Re-run safe: identical aliases are a no-op

### DynamoDB Cost Note
Uses individual UpdateItem calls (not BatchWriteItem) because BatchWriteItem only supports PutItem/DeleteItem, not UpdateItem. DynamoDB ADD on StringSet is the native way to append to sets. Each call is 1 WCU (item < 1KB). ~500-2000 calls total, well within free tier burst capacity.

## Metrics

Must be measured on actual run with --upload. Expected:
- Items with name_aliases before: ~6
- Items with name_aliases after: ~500-2000
- Total aliases added: ~2000-8000

## Verification

Script includes a post-update verification scan that counts items with non-empty name_aliases before and after, printing the delta.
