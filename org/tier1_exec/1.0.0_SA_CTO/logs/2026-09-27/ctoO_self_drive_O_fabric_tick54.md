# /self-drive ~O fabric -- ticks 52-54 (06:17Z-07:25Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a ruling, a re-route, and the hourly floor.

## What moved

- **MX-r-3 COMPLETE** @694268b5cf (`2.0.0_SA_COO~O`; AC1-AC3 re-run on CLOUD, PASS). `3.0.0_SA_CVO~O`'s post-act read put it
  inside the signed radius (Z-C-S19 @3edf006d10).
- **MX-s-7** (the recorder's UTF-8 fix): proof PASS (@f82c698bec), drained @ce2587a5e5 -- re-pointed to a worker because...
- **`0.7.0_AE_CloudOps~I` is DEAD.** COO~O read 0 of 7 live sessions carrying its serial (@57bb9e25fd). It has made no commit
  since 02:42Z.
- **Open orders in scope** (last `<status>` per order file): MX-s-4, MX-s-6 (MCPINDEX); OA-t-1, OA-t-3 (OPALAI). OA-f-2
  is now terminal. (41 round-1 MCPINDEX orders read an empty status: the known multi-`<` parse artifact, not open orders.)

## Driver acts

1. **Z-S3's Lambda half re-routed.** DS~D's source fix is @8ba0d6645b. The patch for the 4 vendored Lambda copies had been
   handed to AE~I (@5dd42c44e9), which is dead. It is re-routed to COO~O as a worker cell (like MX-s-7), deployed via
   safe-apply under a never-widen sign-off. Not urgent: no bad value is written today.
2. **RULING, Z-S25 (the cause of the pathfinder fact_dailynav gap):** DS~D read it. filepoint delivered an EMPTY
   `Median 30 Day Spread Percentage` on 2026-08-29/30; `csv.reader` gives `''`; `_numeric_or_raise('')` raised, so 2 dates
   x 2 funds = 4 partitions were missing. The denominator was 74 bronze deliveries, of which exactly 2 were empty.
   - **Ruled YES:** in a float64-declared column, an EXACTLY-empty field maps to None. Whitespace and every other
     non-parsing token still raise; string columns are untouched.
   - **Not a Rule-17 edit:** `_numeric_or_raise:291-292` already returns None for None/NaN. In CSV an empty field IS the
     source's null, so the mapping substitutes nothing (it is not fillna).
   - **Order:** source fix + a failing-first test, then vendor it into the SAME Z-S3 Lambda cell (one deploy, one
     sign-off), then backfill the 4 named partitions (a literal-key write).

## Calls, verdicts

No new call. At Andrew, unchanged: call 1 BLOCKING (the OPLGTW re-seat), call 2 CARRIED (D9 device), and the switchover
sitting. 0 self-drive verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE.

state: ARMED

## Compiler Tools

The order-file status census (last `<status>` tag per file); a Grep of Rule 17 in CLAUDE_ANNEX.md; a read of
`_numeric_or_raise`.
