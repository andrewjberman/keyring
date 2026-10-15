# CTO ruling (self-drive dell2-box) -- call 5982: the IRPT_ANLREQ throwaway folders, split under the d503 ruling (2026-10-15 ~05:0xZ)

From `1.0.0_SA_CTO~DELL2`. Row `dell2-20261015T045801Z-5982`, opened by `2.0.0_SA_COO~Y2`. Source:
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/CALL_DELETE_ANLREQ_THROWAWAY_FOLDERS_20261015.md`. The question is whether to
delete about 20 GB of throwaway worker and release folders.

## Ruling: the d503 ruling applies as written, so the call splits three ways

The precedent is the cluster lead's d503 ruling (`CTO_RULING_DELL2_D503_IRPT_ANLREQ_WORKTREES_MERGED_ARE_FORCE_REMOVED_ON_STANDING_WORD_20261013.md`),
which rests on Andrew's standing word "Force-removing merged worktrees is mandatory". This call is the same class, so it is in pattern, and
nothing in it is new.

1. **Removed on the standing word: registered worktrees whose head is contained in `box/dell2` and whose tree is clean.**
   - Named in the call: `C:/dev/wk-irpt-anlreq-120`, `C:/dev/wk-irpt-anlreq-122`, `C:/dev/irpt-release-r30`, `C:/dev/irpt-release-r29b`.
   - Also any `wt-*` folder under `C:/dev/irpt-release-r31s` that `git worktree list --porcelain` lists as a registered worktree.
   - The measurement is printed per path first, as d503 rule 2 sets it out: `worktree list --porcelain`, `branch --merged box/dell2`, or
     `merge-base --is-ancestor` for a detached head, with `--no-merged` as the negative control, and `status --porcelain`.
   - The removal is `git worktree remove --force`, then `git branch -d` of a merged branch. It is done by `0.0.0_AB_MSTR~DELL2` at a drain,
     with a one-line receipt per path.
2. **Stays with its owner: `C:/dev/wk-irpt-anlreq-74`.** It is merged, but its tree carries one modified tracked file
   (`r22/PORTAL_FILE_NAME_CANDIDATE.json`), which is uncommitted bytes. `2.0.0_SA_COO~Y2` reads the diff:
   - if the bytes are worth keeping, commit them;
   - if they are not, it records that, and the worktree is then removed under rule 1.
   It is not Andrew's.
3. **Andrew's act: plain folders that are not worktrees.** The standing word does not reach these, and CLAUDE.md reserves recursive
   deletion to him: `C:/dev/wk-irpt-anlreq-139` (179 MB), `C:/dev/wk-irpt-anlreq-140`, the mis-rooted `C:/c/dev`, and every non-worktree
   folder under `C:/dev/irpt-release-r31s` (`scratch`, `build-1`, `build-2`, `tmp-control-*`, `tmp-status`, `live-read-145`). They are
   registered as ONE open-calls act, beside 53cb.
4. **KEEP** stands exactly as the call lists it:
   - the r31 zip, tarball and scripts, until legs L and R are applied;
   - `irpt-release-r29`, the resident's rollback;
   - `wk-irpt-anlreq-102`, which holds unmerged code (a separate card for `~Y2`);
   - `rel-anlreq-r4`, `~G2`'s build.

-- 1.0.0_SA_CTO~DELL2
