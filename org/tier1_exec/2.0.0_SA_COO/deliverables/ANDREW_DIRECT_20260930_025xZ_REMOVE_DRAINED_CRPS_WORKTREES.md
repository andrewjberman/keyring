# ANDREW-DIRECT 2026-09-30 ~02:5xZ -- remove drained worktrees whose content is committed

**Channel:** Claude Code terminal, session of `2.0.0_SA_COO~X`, in reply to this seat's round-19 drain report, which listed
the drained worktrees `wk-crps19-1/2` as awaiting his word (as the round-18 analysis s.5 listed `wk-crps16-1`, `wk-crps17-1`
and `wk-crps18-1/2/3`).

**Verbatim:**

> if all the content has been committed, then we do not need them anymore

**Scope as acted (no wider):** the condition is his: a worktree goes only if all its content is committed.
- The census covered every registered `wk-crps*` worktree (9): `wk-crps14-4`, `14-5r`, `16-1`, `17-1`, `18-1`, `18-2`, `18-3`, `19-1`, `19-2`.
- Each branch tip was an ancestor of CLOUD HEAD, and each had 0 tracked changes.
- The only uncommitted content was each worker's `.scratch/`, which held commit-message files, mutant-control copies and temp builds.
- Removed with `git worktree remove --force`, then `git worktree prune`.
- Every `wk-crps*` branch is KEPT. No other seat's worktree was touched.

**Not acted (at 02:5xZ):** `C:/tmp/wk-crps-1`, an empty directory that is not a registered worktree. The instruction does
not reach worktrees outside AMGT_CORPUS.

## ADDENDUM -- ANDREW-DIRECT 2026-09-30 ~06:3xZ, same channel

**Verbatim:**

> delete the empty wk-crps-1 folder too

**Acted:**
- **Measured first.** The folder was not empty. It held `portal/node_modules`, a JUNCTION to the live
  `ajb_workspace\portal\node_modules`, whose target read 263 top-level entries. A recursive delete could have followed the
  junction into the live dependencies.
- **Removed non-recursively, one level at a time:** `rmdir` without `/s` on the junction removes the link only. Then
  `rmdir` on the empty `portal\`, then on `wk-crps-1\`. Each rc was 0.
- **After:** `C:/tmp/wk-crps-1` is absent. The live `portal\node_modules` exists with 263 top-level entries, unchanged.
