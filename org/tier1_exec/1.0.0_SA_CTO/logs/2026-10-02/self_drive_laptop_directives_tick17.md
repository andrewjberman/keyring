# /self-drive laptop directives -- ticks 16-17 (2026-10-02 19:1xZ-20:3xZ)

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_050xZ_SELF_DRIVE_60M_LAPTOP_DIRECTIVES_ADJUDICATE_ALL_KEEP_COOS_FLOWING.md`
@d4050ac185. Cron `57facd67`. **state: ARMED**. Previous log: tick 15 @ff0acc0bc5. Tick 16 (19:28Z) was quiet: a tick-file line only.

```
SELF-DRIVE laptop directives -- tick 17 (20:28Z)   state: ARMED   cadence: 60m   job: 57facd67
SCOPE: 10 directives -> 48 projects   device: laptop   inbox: 0 unread at the tick
OPEN CALLS IN SCOPE: 5 ruled since tick 15 (batches 183-187) - 0 design forks - 0 governance forks; 0 open
ACTS ONLY ANDREW CAN DO: 2 (below)
SEQUENCE: no DRIFT, no OUT-OF-SEQUENCE; CAPACITY 4 COO lanes against cap 3 (Andrew's IRPT seating word)
COMPLETION TEST: NOT DONE -- 15 of 48 complete or closed; D10 UNMEASURABLE (no member projects)
```

## Since tick 15

| batch | item | ruling |
|---|---|---|
| 183 | `~M` 104382: the `multi_asset` producer deploy | no re-mint now; the producer ships WITH its rows after a PROD promote carries the readers (named trigger, full member census) |
| 184 | `~M` 104385 | corrects 183 item 3: the -0.0 fix is already live and the route does not validate enums while serving, so the contract pin rides the rows packet |
| -- | `3.0.0_SA_CVO` 104384 | IRPT_DASHBD rounds 2-4 compiled (18 rows) and held by the row gate while round 5 runs; no override; one analysis when it lands |
| 185 | `~P` 104389: IB-pr-221 | SIGNED: Inflection Performance served from its holdings gold; 49F label GROSS with values unchanged. `Absence("fees_and_income")` read in the answer |
| 186 | `~Y` 104386: row S279 | a fund ticker fails the whole upload (measured); the st14 fix is proven offline first; vendor traffic stays paused (five WAF challenges) until its cause is named; `~D` holds the Case A walk |
| 187 | `~M` @8859c2003c: the TARGET fold | (a), OPT-IN (`include=target`) and labelled `basis: TARGET`, never summed with actual. PROD v2.1.195 carries the IR `multi_asset` readers; the Advisor Intelligence half does not yet |

## The COO lanes (20:28Z)

| lane | state |
|---|---|
| `2.0.0_SA_COO~M` | BD r3 re-land and Cottonwood re-point RAN, green through leg R; leg S at 23:00Z (BD) and on 10-03 (Cottonwood); the TARGET fold (batch 187) |
| `2.0.0_SA_COO~Y` | M2 + hop 11 served and graded PASS (@8c2d1378a6); st14 fund-row fix; vendor paused; `backend_join.py` (Y-H) built |
| `2.0.0_SA_COO~P` | IB-pr-298 drained (GROSS); IB-pr-221 ledger OPEN @53c86ea96f; DB-b-11 (P-2 scale) running; DB-b-12 and DB-b-13 (S22) queued |
| `2.0.0_SA_COO~D` | item 85 (H-1..H-3) on DEV and proven (17=17 at 49F, 467=467 at Cottonwood); next the Y-H submit harness, then 2.1 |

## Acts only Andrew can do (each with its citation)

1. A population pull of Black Diamond's performance endpoint for P-5, after P-2 publishes. CLAUDE.md: "NEVER call an external
   vendor API without Andrew's explicit per-use word"; card 4 covered five accounts.
2. The portal PROD promote that carries the Advisor Intelligence `multi_asset` readers (batch 180's candidate). CLAUDE.md Portal:
   "DEV only, PROD gated". The `multi_asset` rows and the producer wait on it (batch 183).

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| git | `git show 394c246fb6:performance/holdings_gold.py` (the label's companions) | PASS | `Absence("fees_and_income")`, `basis`, TIME_WEIGHTED, GROSS |
| git | the lanes' commits since 19:30Z | PASS | grades read at their commits |
| python | `.tools/sequence-check.py` | PASS | 10 projects; NEEDS-SLOT 2 held at cap |

-- 1.0.0_SA_CTO
