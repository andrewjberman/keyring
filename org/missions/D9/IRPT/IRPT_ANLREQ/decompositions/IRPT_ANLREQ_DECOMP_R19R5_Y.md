# IRPT_ANLREQ -- decomposition, round 19 LAMBDA LEG REBASE, round 5, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** a MEASURED finding of this seat (row `IRPT_ANLREQ-D2-S66`, 2026-10-13 ~04:3xZ): the live `irpt-ycharts-generate` package is CodeSha256 `NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM=` (ADVI_FIRMBKTS act 4, ledger `org/critical_paths/change_management/20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md`, last unit 2026-10-12T14:13:46Z), NOT the `tdpterTM...` package the round-19 census (`AR-y-192`) and the release build (`AR-y-193`) were cut against. Against the live package the AR-y-193 release package differs in FIVE members: the two reader members and three of the four native holds (`acceptance.py`, `submission_service.py`, `durable_job.py`). The holds pinned at `1eed34a8c0`, `b3fc529601`, `7122afefc1` are older than what runs; a release built from that map would move three members it must hold.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-201` | the live package read now (CodeSha256, 104 members by sha256); the four native holds re-pinned to commits whose blobs equal the live members; the release map patch re-cut; the release built (BUILD_ONLY) and a holds-only build; each compared with the live package member by member | the worker's deliverables | LOCAL (a read-only `get-function` and a download; throwaway worktrees outside the tree; nothing uploaded, nothing applied) |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent read-and-build cell.
