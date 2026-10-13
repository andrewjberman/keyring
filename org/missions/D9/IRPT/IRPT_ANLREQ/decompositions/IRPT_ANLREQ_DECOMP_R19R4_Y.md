# IRPT_ANLREQ -- decomposition, round 19 RESIDENT LEG round 4, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** `AR-y-199` (drained @fc2246298d): st32's recipe is recovered and rebuilds all 298 recorded members by name and content. The CTO's hold (msg 6770, section 4 item 5): the release moves ONLY the reader members and what imports them; every other member stays at st32's bytes, proven by the reader's tests passing in a scratch tree on that build. (The full-recipe release at the head moves 24 members, carries `SECTION_BOUNDS` on and a different capture library; the hold supersedes it.)

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-200` | the resident tarball for the release: st32's recipe at st32's pin with ONLY `intake/uploads.py` and `intake/template_reader.py` taken from the release pin (plus whatever must move for them to import, named and proved minimal), built locally; its delta against the st32 rebuild; the reader's named tests run against that build in a scratch tree; the root-naming question for the bindings answered | the worker's deliverables | LOCAL (local tarball and scratch folders outside the tree; nothing installed) |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent build-and-prove cell.
