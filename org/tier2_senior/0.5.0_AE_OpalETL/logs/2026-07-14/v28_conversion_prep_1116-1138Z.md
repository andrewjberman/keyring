# 0.5.0_AE_OpalETL — V2-8 conversion prep, window 1116-1138Z

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE

## Window summary

Prep window so tonight's first conversion is execute-only. No commits (driver is a scratchpad
one-time runner, per the sweep/enrichment precedent -- the record artifacts are the S3
manifests + the D2 findings, both already committed).

1. **_probe/-vs-real-key discipline GROUNDED on the live tree** (rail-checked listings, on the
   record): the standing convention is `_probe/{source}/{scope}/{layer}/{feed}/{date}/
   grammar.probe` -- 35B markers, content `grammar probe <ISO-timestamp>`, all stamped
   02:43:45Z (the grammar-ratification pass). Schwab has BOTH bronze and silver probes; the
   smartx silver draft objects exist (`smartx/platform/silver/allocation_positions/
   date=2026-07-14/data.parquet` 3.05MB + `allocation_valuation` 1.13MB) -- the "2 draft
   objects" that rode the V2-8 landing. No repo tooling writes probes (0 comp-grep hits);
   the discipline is the key-shape mirror itself.
2. **First-conversion driver AUTHORED** (scratchpad `v28_first_conversion.py`), keyed off
   `silver.MAP_TABLE_NAME` (= `fact_allocation_account_map`, cell-6 settled CTO 111700Z).
   Honors every signoff condition (CTO 094726Z): grammar probe written + listing-verified
   BEFORE the real write; write_parquet's ListObjectsV2 key+Size+ETag acceptance; per-model
   denominators + set-identity with NAMED holes; (b)-join miss count recomputed at run time
   from live artifacts (feed-5 closed x sweep x living map x detail enrichment), never quoted
   from today's session. Scope held to the signed family: feed-9 living-map rows only;
   closed-identity rows joining the table is a separate design fold.
3. **13:30Z fire-verify watcher ARMED** (background task b9blawvul): sleeps to 13:36Z, then
   reads the daily fire's rewritten platform manifest -- guard_ok + missing/surplus + a check
   that nonzerosleeve is correctly EXCLUDED from the reconciled landed set (first live
   exercise of the v1.5.1 platform-scope two-writers exclusion).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-grep | 3 calls (_probe/grammar-probe implementation hunt) | PASS -- 0 hits is the real result (no repo tooling; ad-hoc convention confirmed) |
| raw aws s3 listings (rail-checked x2) | _probe/ + smartx silver prefix discovery | convention + draft objects grounded on live keys |

What worked: comp-grep's honest-zero (gitignore-aware denominator printed) let "no probe
tooling exists" be a grounded claim, not an absence-for-mechanism guess. Gap found: none.

## MCP traffic

0 new (3 broker re-surfaces of already-handled messages, not counted per the speed contract).

## Current State (zero-prior-context)

Branch CLOUD pushed through `075f30e14`. Monitors: bm85gqzkg (inbox), buxydij3b (22:00Z
etfs/ landing watch, 22:50Z deadline), b9blawvul (13:36Z fire verify). Driver ready:
scratchpad `v28_first_conversion.py` (session d33639ae scratchpad dir). Table name settled
`fact_allocation_account_map` (silver.py MAP_TABLE_NAME @ `075f30e14`). Pending time-gated:
13:36Z fire verify -> 22:00Z three verdicts (gate `python .tools/etfs-parity-check.py`
UNPIPED; report to [2.0.0_SA_COO], V2-1 GO rides it) -> first V2-8 conversion.

## Next Steps

1. [self, 13:36Z] read b9blawvul verdict; escalate only on a guard surprise.
2. [self, 22:00Z] three verdicts + COO report; then run the conversion driver.
3. [1.0.0_SA_CTO] holds: Andrew veto window on cell-6; grant-boundary consolidation.
