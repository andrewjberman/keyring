# ANDREW-DIRECT 2026-09-29 ~18:5xZ -- remove the 13 worktrees

**Channel:** Andrew, in the 1.0.0_SA_CTO~Z Claude Code session (site Z), 2026-09-29 ~14:5x ET.
**Recorded by:** 1.0.0_SA_CTO~Z, same turn, before the act.

## Verbatim

> "go ahead and remove the 13 worktrees"

## Scope (verbatim scope, nothing wider)

"The 13" is the list this seat put to him. It is the checkout-removal list from tick 1
(`logs/2026-09-29/ctoZ_self_drive_AMGTOPS_tick1.md` @4b8e817869), plus `wt-cvoz-harvst`, which CVO~Z confirmed in msg
26651:

`C:/tmp/wk-crps10-1`, `C:/tmp/wk-crps12-1`, `C:/tmp/wk-crps13-1`, `C:/tmp/wk-dsgn-amgtv1-9`, `-10`, `-11`, `-12`,
`Desktop/wk-hvst-r16-42`, `Desktop/wk-hvst-r17-43`, `Desktop/wk-hvst-r17-44`, `C:/tmp/ae-a-vv4`,
`Desktop/wk-hvst-z2-r11`, `C:/tmp/wt-cvoz-harvst`.

NOT covered by this word:
- the in-place repair of `wk-crps14-5`, which was asked separately and is still on his list;
- every branch, which stays, including `wk-hvst-z2-r11` and its 3 client-screenshot commits (the purge decision is
  0.0.0_AB_MSTR~Z's);
- every other worktree.

## Pre-act measurement (this seat, just before the act)

- Tracked edits: 0 in all 13 except `wt-cvoz-harvst`. There, the one modified file (`etf-classifications.tf`) differs
  only in line endings: `git diff --ignore-cr-at-eol` is empty.
- Unique commits: 0 on 11 branches. `wk-hvst-z2-r11` and `cvo-z-harvst-l4r` have 3 each, and both branches are kept.
  CVO~Z restored the branch-only records @651d64ed51.
- Untracked files:
  - `wk-crps10-1`'s round-10 check scripts: COO~X measured them byte-identical to CLOUD.
  - `wk-hvst-z2-r11`'s `0.9.0_WK_AMGT_HARVST~33/scripts/*.py`: `cmp` identical to CLOUD.
  - `ae-a-vv4`'s two files: copies of the vv-4 reissue entry, CLOSED 10 of 10 on CLOUD @1c410c5936.
  - `.scratch/`: copied to `.runtime/crash-investigation-20260929/wt-scratch-archive/<name>/` with file counts equal.
    COO~X copied crps10/12/13 earlier; this seat copied dsgn 9-12 and hvst 42/43/44.

## Result

**DONE, 13 of 13 (~19:0xZ).**

- **Junction trap, found and handled before any removal.** Five trees (`ae-a-vv4`, `wk-dsgn-amgtv1-9..12`) held
  `portal/node_modules` as a JUNCTION into the MAIN `ajb_workspace/portal/node_modules`.
  - The first removal (`ae-a-vv4`) left that junction behind and did not follow it.
  - The other four were unlinked first with `cmd /c rmdir <link>`, which removes the link and never the target.
  - Afterwards the main tree still has `vite/` and `react/`, and localhost:5174 still returns 200.
  - Any future worktree removal on this box must enumerate reparse points first
    (`Get-ChildItem -Recurse -Depth 2 -Attributes ReparsePoint`).
- **Removal.** `git worktree remove --force` on each of the 13: rc=0 every time and every directory is gone.
  `ae-a-vv4`'s leftover empty `portal/` was removed with `rmdir`.
- **Branches.** All 13 still resolve under `refs/heads/`.
- **Portal metadata.** `git -C portal worktree prune -v` pruned metadata only, for portal worktrees whose directories
  no longer exist. That includes stale entries from MSTR~Z's earlier reclamation. No portal branch was touched.
- **Worktree count.** 49 including main (48 linked). The inventory read 57 linked; the difference beyond the 13 is round-4
  checkouts the COOs cut after the inventory.
- **Still on his list:** the in-place repair of `wk-crps14-5`.
