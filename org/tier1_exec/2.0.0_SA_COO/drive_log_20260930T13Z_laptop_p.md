# /canonical-drive log -- 2.0.0_SA_COO~P -- 2026-09-30 13:0xZ to 17:0xZ (host laptop; post-crash relaunch)

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE
**Lease:** IRPT_BCKEND FULL; IRPT_DASHBD FULL (no lease row). LIVE_ARMS row: `/canonical-drive 10m` over IRPT_BCKEND ~P (RELAUNCH
2026-09-28, re-authorised by the 2026-09-30 13:0xZ post-crash word); IRPT_DASHBD workstream B added to this seat by Andrew's seating
in the PRD (section 5), CTO 103251.

## Tick 1 (13:0xZ-14:3xZ) -- relaunch: assess, clean, issue round 26

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_BCKEND | L6 issued | 26 | 0/2 open (pr-261 WK~97, pr-263 DS~S) + IB-pr-262 issuer's | 3/3 | n (INF raw chain broken since 09-28) | residue commit 78f68cd2d2; CTO nudged for the round-25 analysis (landed dd4c69b696); issuance f54e17e4c6; worker 97 + seat DS~S spawned |

Surfaced and ruled: the Schwab silver dim_position for 09-29 absent at 13:3xZ (row S235 @410818259a, placement to the CTO; the
49F r3 ledger A1 leg stays OPEN); IRPT_DASHBD v0.2 ADMITTED and workstream B seated here (103251/103257/103260/103263/103264).

## Tick 2 (14:3xZ-16:0xZ) -- the pr-242 served move, the DS finding, IRPT_DASHBD L5

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_BCKEND | L7 in flight + issuer's served move | 26 | pr-263 SUPERSEDED @ed0be5b557 on row S236 (the two twr_daily partitions are non-performance days by the producer's own rule) | 3/3 | n | packet e0a2f524e4 (blob 1bc65b9b16); CTO half @0386ab930c; seat DS~S retained for IRPT_DASHBD |
| IRPT_DASHBD | L5 | 1 | -- | 4 cells cut | none yet | decomposition b6cfb3316e (dep_stage DECOMP) |

## Tick 3 (16:0xZ-17:0xZ) -- apply, issue, drain

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_BCKEND | L7 -> L8 | 26 | pr-261 COMPLETE on wk-IRPT_BCKEND-97 (P26-1-AC1/AC2/AC3 PASS; drain waits on ~T's in-progress drain in the shared index); pr-263 superseded; IB-pr-262 APPLIED 16:19:48Z (CodeSha256 t1QrzaDe..., re-plan No changes; apply ledger CLOSED; observation ledger HELD on tomorrow's first stop event, 5449e4ffcf) | 3/3 | n: the raw writers run again (bronze/positions/2026-09-30 landed 15:18Z) but the mirror + opal-assets-silver-orion stage has not moved fact_positions past 09-27 (read 16:3xZ), and the full chain now stops at INF_C_01 on the NNA coverage guard (row W97-S3) | drain attempted twice (index carried other seats' staged sets); slug to the CTO follows the drain |
| IRPT_DASHBD | L6 issued | 1 | 0/4 (DB-b-1, DB-b-3 on DS~S; DB-b-2, DB-b-4 on WK_IRPT_DASHBD~1, spawned on "gold landed") | 4/4 | n | issuance 51c05d1530 (dep_stage EXECUTING); DB-b-1 carries the SKIPPED-DAY RULE from row S237 (DS~S) |

Rulings received this hour and where they land: CTO 103314 (S219 row fix, mine; edited in the working copy, commit waits on DS~S's
uncommitted S239 in the same file); CTO 103318 (S238: the API half is a precondition -- `_authz/served.py` allowedFirmIds enforcement
for service principals is the TOP cell of ~P's next IRPT_BCKEND issuance; ~Y's exact patch candidate @4a3cabe67d).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-find | silver_ids importers, twr_daily readers, artifact_key census, code prefixes | PASS | denominators printed in the decomposition sections and the packet |
| comp-read | dispatch sync, handler, safe-deploy, trigger, holdings entry | PASS | the flat-by-basename sync was the fact the ship cell turned on |
| comp-freshness | the Schwab silver prefix | PASS at 27.9 h (default 48 h; no cadence entry) | a 4-hour miss on a fixed-hour feed is invisible to the default threshold (noted in S235) |
| comp-which | two questions | no vetted match | read source directly |
| to-pipeline-gate / to-decomp-ref-lint | both issuances | PASS after two preflight rewrites | the seating lint mis-parses `0.9.0_WK_IRPT_DASHBD~1` as class `0.9.0_WK_IRPT` (ANNOUNCE only) |
| deploy_ledger.py | open / close-leg / close / hold x4 | PASS | `hold` refuses an entry with no open verify leg: the observation got its own entry |
| safe-apply | inf-pipeline, targeted | PASS 0/1/0 | readback and re-plan clean |

**What failed:** four commits refused for other seats' state in the shared tree (a merge in progress; the CTO's uncommitted
`lib/opal_naming.py` with a SyntaxError; two staged-only ledger sets; an in-progress drain) -- each routed to its owner in one message
and retried. **Gap:** the ledger tool cannot hold a proven apply on a later observation leg without a second entry.
