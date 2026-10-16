# IRPT_ANLREQ -- decomposition, round 52, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** FWD-5's DONE WHEN (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md:65-68`): a sign-in at another firm tries the ticket and each package file and is refused every time, repeatable on demand. Round 46 merged the scoped second-firm mint helper; rounds 47 to 51 made the fixes' acceptance and the global-admissions gate mechanical. Round 52 builds the driver that makes the exercise one command (BUILD ONLY; the run is a later WORLD act under a pair after `2.0.0_SA_COO~V2`'s release, target Oct 20). Free work around that block.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tz-67` | FWD-5 | `fwd5_driver.py` (plan, offline selftest, guarded run, leak/refused/unreached verdicts) and its offline tests | deliverables ~231 only | LOCAL |

## Edges and chains

- One chain (M = 1); the mint helper and the record are merged.

fanout: 1 of 1 chains, cap 4, reason: one build cell
