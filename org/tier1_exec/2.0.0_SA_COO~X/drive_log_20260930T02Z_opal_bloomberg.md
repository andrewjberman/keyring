# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 02Z (host opal_bloomberg)

Respawn at ~02:0xZ (the prior session exited ~01:44Z). `/watcher` armed; msg 26846 (the round-18 analysis) READ-acked. The loop
was armed per `org/ref/LIVE_ARMS.md` (the `1.0.0_SA_CTO~Z` AMGT fabric-ops row: `/canonical-drive <own project> 30m`,
+15m), cron `17,47 * * * *`.

| time | limb | round | TOs | act |
|---|---|---|---|---|
| 02:26Z | L6 | 19 | 0/2 | DRIVE FORWARD: the analysis `62ccfcb8d2` became ONE issuance, `49d41f0c2b` (merged `65f1025c46`). u-1 went to `~1` and u-2 to `~2`; u-3 is dependent. |
| 02:27Z | L7 | 19 | 0/2 | NO-OP: both workers in flight |
| 02:3xZ | L8 | 19 | 2/2 | DRIVE FORWARD: re-graded and merged u-1 (`186d1cc8da`) and u-2 (`db3344a99c`); the hookup `ff1a0f531d`; the one real run and the packet `2679493720` to `3.0.0_SA_CVO~Z` (READ 02:40:44Z) |
| 02:5xZ | -- | -- | -- | Andrew-direct: removed the 9 drained CRPS worktrees and kept their branches (record `8c4f79e531`) |

## Rulings at L5 this hour

- u-1: the readers also honour a per-security status that is not `MEASURED`. The committed map's 6501 entry predates the
  `exception` shape.
- Round-18 ruling 1's branch was settled at the cut: the served block already read UNRESOLVED, so no re-derive was owed.

## Compiler Tools

- `to-pipeline-gate.py` (via safe-commit) on the issuance: 2 orders; cells resolve 3 of 3; L4-R sign-offs OK; no refusal.
- `safe-merge.sh` on 3 merges: each graded its MERGED index (11, 4 and 4 staged paths); 0 collisions.
- `proof-of-spec-check.py`: both instances VALID when re-run by this seat.
- `comp-pulse diff` (risk reflex): 11 of 11 files checked, 0 danger hits.
- Gap: the `/watcher` census regex misses a quoted script path (a known memory entry); the loose form found the row.
