# 2.0.0_SA_COO~MP drive log -- 2026-10-08 22Z-23Z -- /canonical-drive NFRA_MCPORTAL 30m (:22/:52)

| tick | time | limb | round | TOs t/T | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| 1b | ~22:2xZ | L7 | 4 | 0/2 | 2/2 cut | n | DRIVE FORWARD: MP-x-2's first report; amendment 1 merged into its worktree through safe-merge @a7b399ec99 (union-resolved channel); the worker continued |
| 1c | ~22:4xZ | L7 drain | 4 | 1/2 | 2/2 | n | DRIVE FORWARD: MP-x-2 re-run by the issuer (AC1 5 of 5, AC2, AC3 PASS); drained @6b1b7b18dd |
| 2 | 22:34Z | L7 | 4 | 1/2 | 2/2 | n | NO-OP: MP-x-1's worker live (commit 06bfb80b54, deliverables touched 22:34Z) |
| 3 | ~23:0xZ-23:3xZ | L7 drain -> L8 | 4 | 2/2 | 2/2 | y (pre-release real run) | DRIVE FORWARD: MP-x-1 re-run in a fresh no-cone worktree (AC1 7 passed with 5 of 5 named, AC2 30 passed, AC3 routes=1); drained @1cf3a1dce5; round-close-check MAY-CLOSE; real run; packet to 3.0.0_SA_CVO~O's stand-in 3.0.0_SA_CVO~Z |

## Decisions

- **Round 4's one real run** was the drained handler's `_compute(6)` against the LIVE activity store, from this box:
  - 2150 records, 0 skipped, 21.1 s cold;
  - dell2 409, laptop 268 and dell1 120 commits; sitez "not reporting";
  - `fabric-activity.py boxes --hours 6` agrees, up to the commits that landed between the two reads.

  The live page waits on round 5: the grant, then the release.
- **The orders now carry `<to_id>` and a bare `<status>complete</status>`.** `round-close-check` read the prose status as
  not complete and the missing element as `to_id ''`. The drain pointers moved to each record face.
- **`dep_stage` stays EXECUTING** (@af5141e38c, with the index in the same commit). The close gate grades all 20 orders, and
  round 3 holds two on Andrew's gates. The ROUND_CLOSE stamp at 5061ff3042 was admitted only in WARN mode. While my failed
  stage commit sat uncommitted in the shared tree it blocked peers' commits; `0.0.0_AB_MSTR~Z` regenerated the index
  (msg 32117) and was told the final state.
- **Site Z applies now go to `0.7.0_AE_CloudOps~Z`** (msg 32061). They are carried in the packet's round-5 list.

## Waiting on

- 3.0.0_SA_CVO~Z: L8 compile and the slug. 1.0.0_SA_CTO~O: the round-4 analysis, which the round-5 cut reads.
- Round 3: G-CLOSE (Andrew, after r29) and G-2ND.

## Compiler Tools

- `round-close-check`: REFUSED (0 complete) -> MAY-CLOSE (2 of 2, proof_ok 2).
- `missions-tree-index` `check` and `derive --write`: 1 drift, then 0.
- `comp-surprise --json`: 45 rows, 12 armed. Every armed row predates round 4, and every owner is seated.
- `comp-state --self-test`: 4/4.
- `safe-merge` guarded drains: 2, both with a union-resolved channel.
- IAM and S3 reads: SSE-S3 with no bucket policy on the globgrph bucket.
