# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: re-seated for one round (direction Z4); round 10 decomposed, battery built, issued, worker ~33 spawned -- 2026-10-13 19:1xZ-20:1xZ (host opal_bloomberg)

**archetype:** DRIVE FORWARD (L5 + L6 + L7 spawn)

## Ticks and events

| time | act |
|---|---|
| 19:1xZ | Seated by `0.0.0_AB_MSTR~Z` (msg 33698). /watcher: registered, one watcher; delivery ledger 20 of 20 READ. Read direction `DIRECTION_SITEZ_20261013.md` Z4 |
| 19:2xZ | Round-10 cut ruling arrives (msg 33704, `ledger/CTO_RULING_ROUND10_Z4_ONE_SHORT_ROUND_20261013.md`). L4-R reads WITHHELD (ratified-text half STALE). Decomposition started on the ruling |
| 19:4xZ | PRD v0.9 cured to a three-member FWD-20 partition (@e581c26ab4); ADMITTED (msgs 33710, 33712). The census instrument was re-cut to the partition, and to the CVO's note (member classified from its definition) |
| 19:5xZ | Battery built in `round10/checks/` (6 checks, 4 instruments). Base 08b77fd98d: all 6 FAIL as a build check must. Planted PASS and FAIL arms exercised for every instrument (standing clause 1) |
| 20:0xZ | ONE issuance @0fa3174d89: MX-c-8 + MX-r-11, fan-out 1 of 1 chains, cap 8. project.json ROUND_CLOSE -> EXECUTING. Pipeline gate OK; L4-R OK at v0.9 |
| 20:1xZ | Worker `0.9.0_WK_NFRA_MCPINDEX~33` spawned on MX-c-8 in `wk-mcpindex-r10-33` (base edc544ba75, carries the issuance) |

Tick row: `NFRA_MCPINDEX | L7 | 10 | TOs 0/2 | cells 2/2 (FWD-20, FWD-21) | thread none (one-round enrichment) | issued + spawned`.

## Measured facts the cut rests on

- Served tools at the deployed commit 185dc04888: **N = 67** (43 native + 24 from 7 enabled integrations). The live host
  read the same 67 (ssm 6f80490b).
- The base catalog links 10 of the 67 tools to an index. No tool carries depth or freshness.
- No gateway tool reads `opal-data-harvest`: comp-find found 0 hits across 261 files, and `gateway_query_catalog` reads only
  the catalog's one bucket. So the harvest rows ship with `gap_owner: NFRA_OPLGTW` (direction Z5).
- The servable-prefix list v3 @0b2778751a: 11 SERVE-NOW rows, 16 prefixes (row 8 = six gold tables; row 22's sub-folders
  belong to `derived/`).
- The Schwab control ("Schwab account positions") reproduces offline exactly as live: 8 matches, 3 of 3 silver.

## Next

- On worker ~33's report, drain MX-c-8 (merge, AC1-AC3 re-run at the merged index), then continue it with MX-r-11 PHASE A.
- MX-r-11 PHASE B waits on the gateway slot: NFRA_MCPORTAL.TO-MP-z-5 reads `staged`, so its ledger must close first
  (direction Z1 is first on site Z).
- No /canonical-drive cron armed: no live scoped authorization for this lane in `org/ref/LIVE_ARMS.md`.

## Compiler Tools

- `comp-find` refuses a census piped through `tail` (R6). Pass `--limit` and keep the DENOMINATOR line.
- A row-22-style table cell can name sub-folders after the prefix. A token-set parse over-counted 18 against the grant
  section's 16. The cross-check against the list's own grant section caught it before the cut.
