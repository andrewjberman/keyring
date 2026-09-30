# ANDREW-DIRECT 2026-09-30 ~00:1xZ -- the three open calls: "RECS APPROVED"

**Channel:** Andrew, in the 1.0.0_SA_CTO~Z Claude Code session (site Z), 2026-09-29 ~20:1x ET. It answers this seat's
`/open-calls` frame of 00:15Z (3 calls).
**Recorded by:** 1.0.0_SA_CTO~Z, same turn, before any act.

## Verbatim

> "these are all fine, RECS APPROVED"

## What each call now reads (the REC as put, nothing wider)

| call | REC approved | act and actor |
|---|---|---|
| 1 | Restore the shared tree's `integrations/bloomberg/research/field_map.json` and `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/ingest_run.json` to HEAD. They are the pre-crash test run's residue (mtime 01:42:34 ET), backed up first to `.runtime/crash-investigation-20260929/uncommitted-backups/field_map_and_ingest_run_0542Z.patch`. | This seat restores those two paths only, after re-verifying the backup still matches. 2.0.0_SA_COO~X then merges its Hitachi-only delta `6077a2d939` and closes leg F before 01:26Z. |
| 2 | 0.0.0_AB_MSTR~Z resolves the 4 CLOUD merge conflicts and pushes: union the append-only `4.0.0_SA_CRO/RECON_REGISTER.md`; keep both copies of the three device-duplicate `2.0.0_SA_COO~D/drive_log_20260929T{10,11,19}Z.md` by renaming; `walk.mjs` by this seat's resolution @c6ebc1a8c5. | 0.0.0_AB_MSTR~Z (the only seat that pushes shared branches). This seat relays. |
| 3 | Remove the 8 merged checkouts `wk-dsgn-amgtv1-18..25`: unlink the `node_modules` junctions first, then remove, keeping every branch. | This seat. |

## Result

- **Call 1: DONE (~00:17Z).**
  - The backup patch was re-verified byte-equal to the live diff (`cmp`) immediately before the act.
  - `git checkout -- <the two paths>` returned rc=0; `git status` on both paths now reads 0 lines.
  - COO~X was told to merge `6077a2d939` and close leg F before 01:26Z.
- **Call 2: RELAYED and PARKED.** The message to 0.0.0_AB_MSTR~Z was delivered to its inbox; no MSTR~Z session is live.
  This record is the carrier until one is.
- **Call 3: DONE, 8 of 8 (~00:2xZ).**
  - Before the act: each branch had 0 patch-unique commits on CLOUD, and each portal branch 0 against DEV. No tracked
    edits.
  - `.scratch/` was copied to `.runtime/crash-investigation-20260929/wt-scratch-archive/` with counts equal.
  - 8 `node_modules` junctions were unlinked with `cmd /c rmdir`, link only.
  - `git worktree remove --force` returned rc=0 eight times; every directory is gone. `git -C portal worktree prune`
    was run.
  - All 8 branches still resolve. The main `portal/node_modules` is intact, and 5174 returns 200.
