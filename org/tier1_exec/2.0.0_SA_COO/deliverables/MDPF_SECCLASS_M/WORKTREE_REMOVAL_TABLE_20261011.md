# MDPF_SECCLASS stale worker worktrees -- the per-worktree removal table (2.0.0_SA_COO~M1, dell1, 2026-10-11 ~04:2xZ)

**For:** `0.0.0_AB_MSTR~DELL1`. **Ruling it serves:** laptop `1.0.0_SA_CTO` msg 108195, addendum in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_CLUSTER_TICK2_20261011_0357Z.md` @2b337cf804: no blanket `--force`; this table, written by
the owner, is the precondition. **Tips already tagged** `archive/MDPF_SECCLASS/<branch>` by MSTR (msg 3464). Assessment of what each branch
holds: `WORKTREE_GC_ASSESSMENT_20261011.md` (same folder).

**Columns (read 2026-10-11 ~04:2xZ, each by its own command):**
1. `git -C <wt>/portal merge-base --is-ancestor HEAD origin/DEV` (or `origin/PROD`): the nested portal commit is already on a portal remote.
   Controls: `merge-base --is-ancestor origin/DEV origin/DEV` reads yes (positive); `merge-base --is-ancestor origin/DEV <portal root
   commit ddb7271ae9>` reads no (negative). Portal `origin/DEV` = 26f621d51c, `origin/PROD` = 37aa1247ee.
2. `git -C <wt> status --porcelain`, after removing the two admitted lines (`?? .scratch/` and ` M portal`, the gitlink): any other line fails.

| worktree | branch | portal HEAD | ancestor of origin/DEV | of origin/PROD | other status lines | removal |
|---|---|---|---|---|---|---|
| `C:/dev/wk-secclass-44` | `wk-MDPF_SECCLASS-44` | 8ddfe40994 | yes | yes | **1**: `?? org/pipescript-suite-gate-audit.log` | **STAYS** (owner `2.0.0_SA_COO~M1`, see below) |
| `C:/dev/wk-secclass-47` | `wk-MDPF_SECCLASS-47` | 8ddfe40994 | yes | yes | 0 | pass |
| `C:/dev/wk-secclass-48` | `wk-MDPF_SECCLASS-48` | 8ddfe40994 | yes | yes | 0 | pass |
| `C:/dev/wk-secclass-54` | `wk-MDPF_SECCLASS-54` | 35002195b3 | yes | yes | 0 | pass |
| `C:/dev/wk-secclass-r8-27` | `wk-MDPF_SECCLASS-27` | 8ddfe40994 | yes | yes | 0 | pass |
| `C:/dev/wk-secclass-r9-34` | `wk-MDPF_SECCLASS-34` | 8ddfe40994 | yes | yes | 0 | pass |
| `C:/dev/wk-secclass-r9-38` | `wk-MDPF_SECCLASS-38` | 8ddfe40994 | yes | yes | 0 | pass |
| `C:/dev/wk-secclass-42` | `secclass-r10-held-38` | 8ddfe40994 | yes | yes | 0 | pass |

**The one that stays.** `wk-secclass-44` holds one untracked 157-byte file, `org/pipescript-suite-gate-audit.log`: the pre-push
suite gate's own audit line for worker `~44` (`2026-10-07T13:38Z PERMITTED ... 141 passed`). It is gate output, not work, and the same file
is not present in the trunk tree. The audit file is explicitly un-ignored in `.gitignore:531`, so its one line is preserved verbatim here before
anything is deleted:

```
2026-10-07T13:38:00Z  PERMITTED        author=0.9.0_WK_MDPF_SECCLASS~44  files=15 result='141 passed in 65.41s (0:01:05)' trigger=.tools/safe_deploy_core.py
```

It still fails column 2 as the ruling wrote it, so the owner does not pass it: on MSTR's word (or the CTO's) the owner deletes that one
file, re-reads column 2, and the row becomes `pass`.

**Seven of eight pass.** The seven passing trees hold only `.scratch/` and the portal gitlink beside tracked content that every tag
preserves; their nested portal commits are on `origin/DEV` and `origin/PROD`.
