# 49F freeze-class ROOT: positions_cube held at 06-26 = BD-delivered-but-silver-filename-skipped (source+data grounded)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE
**serial:** 0.6.0_AE_PartnerETL | **date:** 2026-06-30 | **window:** ~22:25Z (follows 297f251ce) -> ~23:18Z

## Summary

While staged for the 23:00Z co-verify, DS~B corrected that the chain HELD at 06-26 (positions_cube/06-29 ABSENT) and asked my lane to diagnose the A_03 stall + the BD txn feed status. Drove it to the source+data-grounded ROOT: BD ALREADY DELIVERED 06-29 (today's raw txn pull), but the BD silver merge FILENAME-skips the same-name re-land, so silver/transactions held at trade_date 06-26 -> 49F frozen-behind-available-data (self-heals tomorrow on the next new-name pull). CTO accepted + ELEVATED the retry-net to the durable 49F FREEZE-CLASS root-fix. Disposition: correct-hold tonight, flip-tonight = deliberate force + Andrew widen GO.

## The diagnosis (Rule 22 -- mechanism grounded in source THEN confirmed in data)

1. **Served date driver:** A_03.positions_cube sets `global_end_date = unit_events['trade_date'].max()` (A_03:1545); nightly runs `A_03 --upload` = FULL build, no end-date cap (gold_dispatch.sh:82). So positions_cube max date = max TRADE date in silver/transactions -- DECOUPLED from allocations/06-29.
2. **Data confirm:** global max trade_date across silver/transactions/{06-25..06-29} = **06-26** (even the 06-29 partition file has trade_date_max=06-26, as_of_max=06-26). So positions_cube correctly capped at 06-26.
3. **KEY catch (read the RAW):** TODAY's BD txn REST pull `forwardfill_v2/transactions/TRANSACTIONS_DAILY_2026-06-29.xlsx` (LM 06-30 15:23Z, 316,457 rows) has `Trade Date` max = **06-29** (06-24..06-29 all present). => BD DELIVERED 06-29 (Andrew confirmed: "BD always lags last trading day" -- the normal ~1-day lag put 06-29 in today's pull). The silver is just STALE (converted from yesterday's pull, pre-15:23Z).
4. **ROOT (source-confirmed):** `merge-daily-incremental.py:384` processed=set(manifest['processed_files']); `:389` new_files=[f for f in all_files if f not in processed] -- FILENAME tracking, NO etag. The re-landed same-name `TRANSACTIONS_DAILY_2026-06-29.xlsx` is already in processed_files (132 entries in `silver/incremental_manifest.json`, confirmed present) -> SKIPPED -> silver frozen at 06-26.
5. **Disposition:** STUCK-on-same-name-reland (won't flip tonight w/o force) but SELF-HEALS tomorrow (07-01's new-name pull = not-in-processed -> advances). So 49F = correct-for-vintage at clean 06-26 tonight, NOT permanently frozen. A tonight flip = deliberate force-reprocess (clear the manifest entry + re-merge) = a WIDEN -> COO->Andrew GO.

## Freeze-class significance (CTO ELEVATED the retry-net)

The filename-skip-no-etag IS the same bug class as the allocations empty-stub that started tonight's P0. A same-name re-land of fresher content sitting un-processed is a FREEZE-class root across ALL 4 BD silver merges (transactions/allocations/realized/unrealized -- all use processed_files filename tracking). My CTO-blessed RETRY-NET option-(a) (etag/content-skip + completeness floor, all 4 tables) FIXES EXACTLY THIS -> retires the "frozen-behind-data-on-reland" class. CTO noted it on the retry-net item; scope is now freeze-class-root-fix, not just allocations hardening. Still post-serve (self-heal-tomorrow = no urgency).

## Force-reprocess lever (pre-positioned, NOT triggered)

Manifest = `s3://opal-data-bd/silver/incremental_manifest.json`; remove `TRANSACTIONS_DAILY_2026-06-29.xlsx` from processed_files (backup first) -> `python merge-daily-incremental.py` (default=transactions) -> silver/transactions advances to trade_date 06-29 -> A_03 positions_cube/06-29 -> canonical -> served flip $1,831,666,360.06@06-29. (Same move I ran on the allocations manifest earlier tonight.) DS~B has it STAGED, holding for the widen GO.

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-glob A_03* | PASS | located A_03.positions_cube.py (bd lane) + the watermark key |
| comp-grep POSITIONS_CUBE_INCR_WATERMARK / positions_cube / manifest keys | PASS | mapped A_03 watermark + the 4 silver-merge manifest keys (MANIFEST_KEY=transactions) |
| (rail-checked raw) aws cp + python parquet/xlsx read | n/a | NO comp-tool reads a parquet/xlsx `trade_date` content or a silver manifest's file-list (comp-freshness=status only) -> rail-checked the trade-date diagnosis, the raw-pull read, + the manifest read |

What worked: comp-grep SYSTEMS-CONTEXT routed straight to A_03 + the manifest keys. What failed: none. Gap: the freshness/value-of-an-artifact class (parquet/xlsx column max, manifest file-list) has no comp-tool -- a candidate `comp-content`/`comp-trace-date` family (recurring all session).

## Blockers

None. Tonight's 06-26 hold is correct-for-vintage (NOT a freeze); the 06-29 flip is a legitimate Andrew widen-GO decision (in flight) or self-heals on tomorrow's cadence. External/decision gate, not an assumption-block.

## Current State (handoff)

- **ROOT grounded:** BD delivered 06-29 (raw 06-30 15:23Z, trade_date thru 06-29); silver/transactions frozen at 06-26 via filename-skip (merge-daily-incremental.py:389). 49F = clean correct-hold at 06-26 ($1,816,267,427.27, no-$0), self-heals tomorrow.
- **Force lever staged (DS~B):** clear `TRANSACTIONS_DAILY_2026-06-29.xlsx` from `silver/incremental_manifest.json` -> re-merge. Holds for COO->Andrew widen GO. On GO: DS~B converts + pings me -> I run A_03/positions_cube/06-29-exists + gold-freshness(>21:39Z) + gold_aua->cert convergence gate -> RAVC CTO.
- **Penny-test:** scratchpad/penny_verify.py staged (served==cert + CK5/CK6); both exact values grounded (HOLD $1,816,267,427.27@06-26 / FLIP $1,831,666,360.06@06-29). publish-watch Monitor `bws1on2zi` fires on the 23:00Z republish.
- **Retry-net:** design 2202c3355, CTO-blessed option-(a), now scoped FREEZE-CLASS root-fix (etag content-skip, all 4 tables). Implement + extend test_retry_net.py + deploy both code paths POST-serve.
- Monitors live: inbox b3piybf3o, publish-watch bws1on2zi. No commits this window (diagnosis + coordination only).

## Next Steps

- **[0.6.0_AE_PartnerETL]** (me) on 23:00Z publish OR a flip-GO: run the verify gate, RAVC CTO/DS~B/0.7.0; POST-serve implement the freeze-class retry-net (option-a, all 4 tables).
- **[Andrew]** ride (default, my rec) vs force-tonight (widen GO).
- **[2.0.0_SA_COO]** relay Andrew's serve-vs-hold/widen ruling.
- **[0.4.0_DS_ClientPlatform~B]** on GO: clear the txn manifest entry + re-convert + ping me; else confirm the natural self-heal tomorrow.
- **[1.0.0_SA_CTO]** gold/cert + Orion leg at flip; retry-net formal pickup post-serve.
