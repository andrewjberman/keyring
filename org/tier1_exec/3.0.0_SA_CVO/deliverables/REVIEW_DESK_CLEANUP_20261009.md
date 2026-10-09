# REVIEW: laptop Desktop cleanup (4.0.0_SA_CRO~B msg 107690; Andrew-direct ~03:3xZ "be ginger about the dependencies")

**archetype:** VALIDATE

Reviewed: `org/tier1_exec/4.0.0_SA_CRO~B/deliverables/desk_cleanup_20261009.py`, its dry run and the record, @d3918e91e4.
All checks were read-only, run by this seat on the laptop at ~03:4xZ.

## Verdict: GO, with one condition

**Condition (before `--execute`):** copy two untracked files out of `C:\Users\AndrewBerman\Desktop\irpt-smoke-p-portal-20260923`
to a local folder OUTSIDE git, for example `C:\Users\AndrewBerman\desk_cleanup_archive_20261009\irpt-smoke\`:
- `reviewer-parser.test.ts` (45 lines);
- `reviewer-wire.json` (1,753 lines).

They are an independent reviewer's test and the API response it captured ("independently captured actual Global response passes
real client"), not runtime scratch, so `IRPT_SMOKE_P_PORTAL_20260923_UNCOMMITTED.status.txt` misclassifies them. The patch does
not carry them, and `git worktree remove --force` would delete them. The wire capture may hold client directory data, so it does
not go into git.

## The dependency hazard: the script handles it

- **Links found without being followed.** `links_in()` detects a junction with `os.path.isjunction`, which needs Python 3.12.
  `python` on this box is 3.12.10. The function drops each junction from `dirs` before `os.walk` would descend into it.
- **Links removed as links.** `os.rmdir` / `os.unlink` act on the link itself. The target's existence is checked after each
  removal, a vanished target stops the run, and a target folder that still holds a link is skipped.
- **The live `node_modules` is measured before and after.** Any change fails the run. The dry run reads UNCHANGED at
  312 entries, 41,855 files and 448,768,516 bytes.
- **`wk-tsc` stays.** It is refused by name and asserted off the list.

## Each target class, measured

1. **37 `wk-*` / `wk_*` shells:** each holds 0 files other than the junction (a walk that skips links). 20 of them are still
   registered in portal's worktree list as `<shell>\portal`. The script's end-of-run `git worktree prune` clears those
   registrations once the folders are gone; their branches stay.
2. **Portal worktrees:**
   - `portal-coo-d-p3`, `-r43`, `-regime`, `wt-cto-benchmark-si` and `portal-f1-cd3924d5` are clean, and each HEAD is an
     ancestor of `origin/DEV`.
   - `portal-coo-d-holdings` (HEAD in DEV) has one untracked folder, `tmp/`: 124 UI-review screenshots from 2026-10-04 and -05.
     They are scratch, and losing them is acceptable on Andrew's "more likely its trash".
3. **`irpt-smoke-p-portal-20260923`** (HEAD e0531491 on origin, not in DEV):
   - The 19 `M` entries are line-ending only (`git diff HEAD --ignore-cr-at-eol --stat` is empty).
   - The 2 `AD` entries are in the saved patch.
   - 5 entries are untracked; see the condition above.
   - The status file's "24 M entries" should read 19.
4. **`portal-trade-vident`** (non-git): it holds 1,155 files outside `node_modules`.
   - 839 are identical to the live portal tree.
   - The 316 that differ all exist as blobs in portal's git history (`git cat-file --batch-check` on LF-normalized and raw
     hashes: 316 of 316 found).
   - None is unique, so nothing is lost.
5. **Workspace repo:** no target is registered as a worktree of `ajb_workspace`. Its live worktrees (3) are elsewhere.

## After the run, this seat verifies

- The script's last line reads `node_modules=UNCHANGED`.
- `wk-tsc` exists with its three `.rdp` files.
- None of the 45 targets exists.
- `git -C portal worktree list` shows no Desktop target.
- The archive folder holds the two reviewer files.
- The free space on C: (27 GB before) is stated.

-- 3.0.0_SA_CVO

## After-state, measured by this seat at ~04:0xZ (the run stopped partway)

`desk_cleanup_20261009.execute.txt` ends in a traceback. `shutil.rmtree` on `wt-cto-benchmark-si` raised
`FileNotFoundError [WinError 3]` on a `node_modules` path longer than MAX_PATH. That came after `git worktree remove --force`
had dropped the worktree's registration but failed to delete its folder. The final `git worktree prune` did not run.

- **Safe:** the live `portal\node_modules` reads 312 entries, 41,855 files and 448,768,516 bytes, identical to before. `wk-tsc`
  holds dell1.rdp, dell2.rdp and sitez.rdp. The archive holds `reviewer-parser.test.ts` and `reviewer-wire.json`.
- **Removed:** 41 of 45 targets.
- **Left:**
  - `wt-cto-benchmark-si` (partly deleted; real `node_modules`, no junction);
  - `portal-f1-cd3924d5`, `irpt-smoke-p-portal-20260923` and `portal-trade-vident` (not reached).
  - 30 portal worktree registrations read `prunable`.
- **To finish (the CRO's run):**
  1. Delete the long-path trees through the `\?\C:\Users\AndrewBerman\Desktop\<name>` prefix, so rmtree is not bound by
     MAX_PATH. `portal-trade-vident` has its own deep `node_modules` and needs the same prefix.
  2. Re-run the script, which skips absent targets and still unlinks `irpt-smoke`'s junction first.
  3. Run `git -C portal worktree prune`.

  This seat re-verifies after.
- **C: free:** 27 GB (238 total), before the remaining deletes.
