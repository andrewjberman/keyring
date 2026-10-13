# IRPT_ANLREQ -- decomposition, round 20 STATUS.PY, workstream YR round 11 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-20 analysis (msg 6841, row D2-W55-S25): the deployed `irpt-status` carries 4 of the 28 correction words (its `ops/status.py` is the pinned `361c44fa9d` bytes); the status rule's all-eight pair carries the current `status.py` to `irpt-status`. `AR-y-212` moved `served.py` only. The trunk's `ops/status.py` differs from the pinned one by +68 lines (the finding words), last touched at `e93258c650`.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-217` | the `irpt-status` release re-cut with `served.py` AND `ops/status.py` moved, on the live package, the `status.py` difference shown to be words only, the ops tests and the correction-words parity test run against it | the worker's deliverables | LOCAL (read-only live read) |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent read-and-build cell.
