# ADVI_COTBKF round 24 -- L9 grade of CB24x1-AC4

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~00:1xZ. **Order:** `ADVI_COTBKF.TO-CB-x-1` (drained @d9484f20fa).
**Criterion (verbatim; AMENDMENT 1 moved AC2 only):** "the rule follows the CRO's table row by row; round 22's 25 are each MATCH or named
with a traced cause; every cross-month dividend month is graded both ways with the swing printed and neither date adopted by assumption."

## Verdict: NOT MET (one clause, unmeasurable without an ex-date source)

| clause | result | evidence |
|---|---|---|
| the rule follows the CRO's table row by row | MET | every leg of the CRO's table matches the method section (org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md lines 1239-1306): `man`, `ManAltT`, `ManCheck` drags; `ManAltF` a flow; `fch`, `genmain`, `fee`, `misc`, `csltfee`, `pcf` flows; `12b1` and dividends/interest income; sweeps + CFNCASH one cash position at par; `li`/`lo`/`ci`/`trf*`/`trc*`/`TRFIR` flows (`ci` moved from the default to the table, as the table says) |
| round 22's 25 each MATCH or named | MET | line 1204: 25 of 25 MATCH |
| every cross-month dividend month graded both ways, swing printed | **NOT MET** | no dividend row carries an ex-date (row D2-W46-S2); the pay/ex option is built and tested, with no ex-date input |
| neither date adopted by assumption | MET | the default dates by pay date as delivered and the report states neither date is adopted |

Types the table does not name keep the documented default (row D2-W46-S3); that is outside "row by row", not against it.

## What the round achieved

MATCH 2,058 -> 3,059 and DIFF 1,525 -> 925. The year-chain control is 103 of 103, and the cash ledger equals the broker snapshot to the
cent on 40 of 40 accounts. All 98 regressions are named with one traced cause each: unlisted types 35, pay-dated dividends 22, carried
levels 39, `man` 2. The NOT MET is data the fabric does not hold yet. The fastest close is the ex-date feed, then grading the 22
pay-dated months both ways.
