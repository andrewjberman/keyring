# NEVER-WIDEN -- CTO HALF: `chatter_event` gold rebuild under PRD v0.3

**Signer:** `1.0.0_SA_CTO~Z`. **Date:** 2026-09-28 ~11:1xZ. **Pairs with:** the COO half,
`NEVER_WIDEN_COO_HALF_chatter_event_rebuild_20260928.md` @`7f9df49098` (`2.0.0_SA_COO~Y`).

## VERDICT: SIGNED -- blast radius ONE new object; rollback forward-only, accepted

## What I measured myself rather than adopted

1. **One writer, no overwrite.** `write_gold` is reached for this table only from `build_event`
   (`lib/research/harvest/publication_gold.py:899-914`); the put is conditional, `IfNoneMatch="*"` (`:306-312`), into
   a new `part-<run_stamp>.parquet`. Every prior snapshot, including the 12-row one, is untouched.
2. **The reader takes exactly ONE part: the newest.** `_latest_gold_snapshot_rows` (`:646-663`) sorts every key by
   `(date partition, key)` and reads the single last one -- it does NOT union a partition's parts. So the forward-only
   rollback is sound even on the same day: a third snapshot with a later `run_stamp` sorts last and wins. **This is the
   property the COO half's rollback depends on, and it holds.**
3. **`C-HV-GOLD-REBUILDABLE` is proved** (`HVST-y-1` AC2: two builds byte-identical over the same input), so the
   rollback build reproduces the 12-row set by construction.
4. **NO SERVED READER EXISTS TODAY -- which narrows the blast radius further than either half assumed.**
   `timeline_api.get_timeline` takes its `event_loader` as an argument, and every caller in the repo is a test or a
   proof script (15 hits across 76,968 files); the served backend for `/api/scoped/amgt`
   (`lib/research/api/scoped_amgt.py`, 4,206 lines) carries **0** occurrences of `timeline`. **So this rebuild moves
   no output any user can reach.** The pair is signed anyway, because the next round wires the route and the rebuilt
   snapshot is what it will serve.

## Both branches, from the producer's own rule

- SUCCESS: a new newest part; readers see 8 events (12 -> 8; BA and HD `event_id`s move).
- KEY COLLISION: `PreconditionFailed`, nothing written, 12 stays newest.
- READ-BACK MISMATCH: `HarvestStoreError`; the object exists and is distrusted. **Recovery is forward-only too: a
  further rebuild, never a delete.**

## What this half does NOT cover

No S3 delete, version removal or delete-marker removal, on any branch. Not `chatter_daily` (a new pair). Not the
portal DEV push. Not the backend route that will serve this table -- that is its own cell and, once it serves, the
next rebuild of this table owes a fresh pair.
