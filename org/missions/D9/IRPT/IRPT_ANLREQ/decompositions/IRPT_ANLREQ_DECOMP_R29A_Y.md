# IRPT_ANLREQ -- decomposition, round 29A: THE ARMED-ROWS CENSUS, workstream YT round 29 (issuer 2.0.0_SA_COO~Y2)

**Input:** CLAUDE.md rule 27 (L10): the one slug to the CTO is sent only after every task order of the round is terminal and every BLOCKING or ARMED row is dispositioned. The surprise channel holds 320 rows; 32 are ARMED with `disarm_owner` `2.0.0_SA_COO~Y2`, 10 of those are named by a later row that says `DISARMS`, which leaves 22 (the issuer's parse, re-run by the checker `y296-armed`). Several were raised mid-round and answered by a later cell. The issuer cannot disarm a row on memory: each needs a verdict with a commit, a record or a read behind it, and a hazard that sits in the live world is resolved only by a live read or a record of one.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-296` | READ: `r29/ARMED_ROWS_CENSUS.json`, one verdict (RESOLVED, STILL_ARMED, UNCLEAR) with evidence for every ARMED-OWNED row not yet disarmed, grouped by what resolved it; the worker files no disarm row | the worker's record folder and the surprise channel file | LOCAL |

## Edges and chains

- One chain, read-only, independent of the release census `AR-y-295` (round 28) except that both write rows to the same channel file (append-only). The issuer adjudicates the verdicts and files one disarm row per resolved group; the STILL_ARMED and UNCLEAR rows go into the slug as the remainder or are cut as cells.

fanout: 1 of 1 chains, cap 8, reason: one read-only census over one channel file; splitting by row would repeat the parse and the grouping.
