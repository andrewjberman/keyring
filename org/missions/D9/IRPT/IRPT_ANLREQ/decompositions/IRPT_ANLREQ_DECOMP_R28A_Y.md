# IRPT_ANLREQ -- decomposition, round 28A: THE FWD-1 CONSOLIDATED RELEASE CENSUS, workstream YS round 28 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's msg 7264 (fold the template reader r19.3 into ONE FWD-1 consolidated release) and the cells drained on the trunk since the last releases: `AR-y-245`, `AR-y-280`, `AR-y-281`, `AR-y-284`, `AR-y-285`, `AR-y-291`, `AR-y-292`, `AR-y-293`. The release has not been counted: which served packages carry which changed members (N writers per member), the live start state of each package, and the order of the legs. The issuer writes the never-widen pair, the build cells and the apply orders from this record, not from memory. Row `IRPT_ANLREQ-D2-W109-S2` (ARMED, the issuer's): the packager released before the ticket service's `AR-y-284` leg gets a 400 on every attach.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-295` | READ: the release census record `r28/FWD1_RELEASE_CENSUS.json` (cells, packages with diff command and path count, members with writers, live start states read beside the map, order constraints with evidence, proposed legs with applier lane and rollback) | the worker's record folder and the surprise channel file | LOCAL |

## Edges and chains

- One chain, read-only. It blocks the next issuance (the build cells and the never-widen pair); nothing else waits on it. Not in this round: the KEPT shares pricing (a later cell, with the CTO note 7296 that Yahoo-sourced prices read UNVERIFIED until they pass the porting test), typo suggestions (C-SWAP step F), the staff held-submit sentence (row `W111-S5`), and the checker's wiring into the resident (dell1's, via MSTR).

fanout: 1 of 1 chains, cap 8, reason: one read-only census whose output feeds the next issuance; the packages are counted together because a member carried by several packages must be seen once.
