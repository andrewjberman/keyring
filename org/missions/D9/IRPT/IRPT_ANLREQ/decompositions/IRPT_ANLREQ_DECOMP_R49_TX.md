# IRPT_ANLREQ -- decomposition, round 49, workstream ~TX (issuer 2.0.0_SA_COO~T2)

**Input:** round 48's open row IRPT_ANLREQ-D2-W225-S1 (disposition S139): the draft store's `fail` op (AR-tf-71, merged) has a stub live writer because the hop_failure writer needed a hash the commentary hop lacks. `2.0.0_SA_COO~G2` merged the sha-free `mark_hop_failure_keyed` (msg 9024, bc0e7e96c4, TO-AR-g-109 amendment 1). One cell wires it.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tf-74` | FWD-4 | the draft store's live jobs factory calls `mark_hop_failure_keyed`; tests drive the real writer against a fake client | `commentary_draft_store.py`, `test_hop_failure_live_writer.py` | WORLD (path floor; source and tests, no deploy) |

## Edges and chains

- One chain (M = 1). Depends on AR-tf-71 (merged) and G2's AR-g-109 (merged).
- The release pair is still later and WORLD: the draft-store zip members, the surgical commentary zip (row S127), the grant apply with an iam simulate battery.

fanout: 1 of 1 chains, cap 4, reason: one wiring cell on one file
