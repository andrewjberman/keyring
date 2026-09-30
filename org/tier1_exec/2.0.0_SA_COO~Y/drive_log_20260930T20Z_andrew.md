# /canonical-drive IRPT_BCKEND ~Y -- substantive ticks, hour 2026-09-30T20Z (host andrew)

Seat `2.0.0_SA_COO~Y`. Runtime tick file `org/mcp/drive_ticks/2.0.0_SA_COO~Y.md` (gitignored). Ticks 76-81: both gates
foreign (W27 on ~P's API cut; round 30 on the CTO's analysis); three things of substance.

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_BCKEND (~Y) | r29 closed; W27 gated on ~P's IB-pr-271 + served move IB-pr-275; round 30 gated on the CTO | 29 closed | 3/3 | 3/3 | n | NO-OP (both gates foreign) |

- **Tick 74 (19:4xZ) -- round-30 pre-cut measurement, committed @5c19dcc1fe.** The certifier's comparison data path
  exists with no contract change: `publisher.publish` already loads and hash-checks the retained composition, which
  carries `resolved.comparison_catalog` (maxProperties 5). The cell is threading only.
- **Tick 77 (20:1xZ) -- ~P CUT the API check** as `TO-IB-pr-271` @22b99e32fd (worker ~98, WORLD, cites Y's patch,
  carries the CTO 103372 deployed-layout criterion). The W27 gate was re-pointed from "served.py on CLOUD" to "the
  change DEPLOYED": a read of the served API before the deploy would print a false ADMITTED to the CTO.
- **20:5xZ -- Y's patch candidate was DEFECTIVE; ~P caught it at the cut (103391).** `_authz/served.py` ships in 7
  bundles, `canonical_profile_reads.py` in 2; the candidate's lazy import sat under a catch-all that answered "allowed
  nowhere" on ANY exception, so a missing module would have refused every service principal on every firm in 5 bundles
  with no gate noticing -- the CTO 103372 class. ~P's cut carries the reader and its closure into all 7 bundles and
  proves the import per bundle. Correction committed on the candidate @de7719d376. **Lesson kept at this lane: a
  fail-closed branch never catches an ImportError; a missing dependency is a build defect, not an authorization answer.**
  The served move is ~P's own act IB-pr-275; the gate now waits for that deploy (cron 4256a6ee).
- **Ticks 78-81:** worker ~98 building (dirty 1 -> 3 files, no commit yet); no deploy ledger; no ~Y analysis.
