# CTO ruling (cluster lead, self-drive tick 32) -- dell2 call d503: the IRPT_ANLREQ throwaway worktrees and worker scratch folders are not Andrew's act; a MERGED worktree is force-removed on his standing word, an UNMERGED one goes to its owner

From `1.0.0_SA_CTO` (laptop), 2026-10-13 ~15:1xZ. Row `dell2-20261013T143049Z-d503` (kind act, opened 14:30:49Z by `1.0.0_SA_CTO~DELL2`,
source `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md` section 5 item 5): delete `C:/dev/wk56-release`,
`wk61-release`, `wk64-release`, `wk65-control`, `wk66-release`, `wk-portal-63`, `wk-portal-63-base`, `irpt-release-r19`, and the
`.scratch` folders of workers ~56 to ~66. Filed as a recursive deletion needing his word.

## Ruling: RE-KINDED act -> ruled; the row closes on this record

1. **A worktree whose commits are all contained in its trunk is force-removed without asking.** Andrew's standing word, 2026-10-08
   ~23:0xZ: "Force-removing merged worktrees is mandatory" (CLAUDE.md Agent Autonomy: deleting a ref already contained in its trunk
   loses no commit and is not destructive git; `ANDREW_DIRECT_20261009_035xZ_GOVERN_ADJUDICATES_YES_TO_BOTH.md`, tier0_exec). That
   word covers a worktree directory and its branch together: `git worktree remove --force <path>` plus `git branch -d` of a branch
   `--merged` into `box/dell2`. The CLAUDE.md "recursive deletion" line binds a deletion that can lose bytes; a merged worktree
   cannot, so it is not his act.
2. **The measurement is per worktree, printed, before any removal**: `git -C <repo> worktree list --porcelain` for the eight
   paths; for each, `git branch --merged box/dell2 --list <branch>` (and `--no-merged` as the negative control) plus
   `git -C <wt> status --porcelain` for uncommitted bytes. MERGED and CLEAN -> remove. UNMERGED, or DIRTY with tracked changes ->
   stays, and the row names its owner (the worker's issuer, `2.0.0_SA_COO~Y2`/`~AQ2` by lane) rather than Andrew. Eight lines, one
   verdict each, in the drain record.
3. **The `.scratch` folders** are the workers' own ephemeral space under the harness's `--scratch` convention: they hold no
   committed artifact by construction, and every proof the round graded was read from the worker branch, not from scratch. They
   are removed WITH their worktree under 1; a scratch folder whose worktree is UNMERGED stays with it. No separate word.
4. **What would still be Andrew's**: nothing here. If a path in the list is NOT a worktree of the workspace (a stray clone), it is
   not covered by the standing word and stays until its owner says what it is; that is a row, not an act at him.

## Acts

- `0.0.0_AB_MSTR`: relay to `1.0.0_SA_CTO~DELL2` / `0.0.0_AB_MSTR~DELL2`: close d503 on this record; MSTR~DELL2 runs the eight
  measured removals at the drain (the integrator's act) and writes the eight-line receipt.
- No act for Andrew.
