# CTO~Z post-crash edict -- AMGT_CORPUS, AMGT_RESAPP, AMGT_HARVST, DSGN_AMGTV1 -- 2026-09-29 ~14:10 ET

**Author:** 1.0.0_SA_CTO~Z. **Order relayed:** `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`
(Andrew's sequence: 1. residue, 2. worktree need/dispose by `/canonical-flow` position with the CVO, 3. restart).
**Inventory (measured, 57 of 57 linked worktrees):** `POSTCRASH_WORKTREE_INVENTORY_20260929_1400ET.json` beside this file;
re-run `python org/tier1_exec/1.0.0_SA_CTO/deliverables/postcrash_worktree_inventory.py` (about 55 s). Columns:
`ahead_of_trunk` = `rev-list CLOUD..HEAD`; `patch_unique` = `git cherry CLOUD HEAD` `+` rows; dirty counts exclude the
`portal` gitlink. This edict adds no gate; it names each owner's residue. No loop is re-armed before step 3.

## Measured state at the crash (11:34 ET)

| project | round | cells | measured |
|---|---|---|---|
| AMGT_CORPUS | r14, issued 10:19 @a592fb2bf0 | p-1..p-5 all `pending` | 0 worker commits. 14-1/2/3 clean (no edits). **p-4 has no checkout and no branch.** 14-5 is a disk-full PARTIAL CHECKOUT (180 tracked files dirty, all unrelated DS task orders, 0 unique commits), not worker work. |
| DSGN_AMGTV1 | r4, issued 10:20 @2177e483a2 | w-1..w-6 `pending` | **w-1 (`wk-dsgn-amgtv1-13`) holds UNCOMMITTED worker edits**: `.claude/skills/ui-walk/{SKILL.md,walk.mjs}` M, `signin_detect.mjs` new, surprise channel M. w-3/w-4 (15/16) clean. **w-2/w-6 (~14) and w-5 (~17) never got a checkout**; branch `wk-DSGN_AMGTV1-14` exists at 2ab3d567c8 with no worktree. |
| AMGT_HARVST | r18, issued 10:08 @4d86812a13 | g-1, g-2 `pending` (~45) | **`wk-hvst-r18-45` holds UNCOMMITTED worker edits**: `lib/research/harvest/{publication_gold,universe_securities}.py`, the test, the surprise channel (M), plus 4 untracked. |
| AMGT_RESAPP | r48 | ww-2/3/4 `complete`; ww-1 `pending` | **NEVER-2 entry `amgt-resapp-ww1-redeploy-research-dossier-20260929` OPEN, 0 of 4 legs** (opened 10:38 ET by 0.7.0_AE_CloudOps~A, not live; window ends 16:38 ET). WORLD MEASURED UNTOUCHED: `opal-amgt-scoped-api` LastModified 2026-09-29T09:56:25Z (05:56 ET, the vv-4 rollback), before the entry opened. Not half-landed. |

## Residue, one owner each (step 1)

1. **2.0.0_SA_COO~X (CORPUS r14).** `wk-crps14-5` is crash damage with nothing to salvage: remove it and re-add it from
   its branch at restart. Decide per cell whether to resume in the 14-1/2/3 checkouts or re-cut; p-4 needs a checkout
   either way. The two untracked round-10 check scripts in `wk-crps10-1` are yours to keep or drop.
2. **2.0.0_SA_COO~D (DSGN r4).** SALVAGE w-1's uncommitted edits in `wk-dsgn-amgtv1-13` before anything touches that
   tree. w-2, w-5 and w-6 were never started.
3. **2.0.0_SA_COO~H (HARVST r18).** SALVAGE g-1's uncommitted edits in `wk-hvst-r18-45` first. Then decide on
   `wk-hvst-z2-r11` (0.7.0_AE_CloudOps~I, 09-28): it has 3 patch-unique commits that are not on trunk.
4. **2.0.0_SA_COO~Z (RESAPP r48).** For the OPEN ww-1 entry, name an executor for restart inside the window, or close
   the entry as NOT-STARTED and cite the LastModified read above. Never close it as done.
5. **3.0.0_SA_CVO~Z.** `wt-cvoz-harvst` is yours: 3 patch-unique commits since 09-23 plus an edit to
   `etf-classifications.tf`. Also grade each project's `/canonical-flow` position against the need list below.

## Worktree need list, AMGT/DSGN scope (step 2) -- 22 of 57 worktrees

- **NEED (in-flight round, salvage or resume), 9:** `wk-hvst-r18-45`, `wk-dsgn-amgtv1-13`, `-15`, `-16`,
  `wk-crps14-1`, `-2`, `-3`, `wk-crps14-5` (recreate), `wt-cvoz-harvst` (the CVO rules on it).
- **OWNER RULING (unique commits or parked), 2:** `wk-hvst-z2-r11` (COO~H); `coo-y-leadpanel-20260924`, which has 3
  modified harvest `.tf` files. Its owner, 2.0.0_SA_COO~Y, is a laptop seat that is not live here. PARKED: owner COO~Y;
  it un-parks when COO~Y is live on site Z or Andrew rules.
- **DISPOSABLE on the owner's confirmation, 11:** each branch has 0 patch-unique commits, and each tree holds only
  `.scratch/` or stale untracked copies. The trees are `wk-crps10-1`, `-12-1`, `-13-1` (COO~X); `wk-dsgn-amgtv1-9`,
  `-10`, `-11`, `-12` (COO~D); `wk-hvst-r16-42`, `r17-43`, `r17-44` (COO~H); and `ae-a-vv4`, whose two untracked files
  are copies of the vv-4 reissue entry, CLOSED 10 of 10 on trunk @1c410c5936 (COO~Z). Removing a checkout is a
  recursive deletion, which CLAUDE.md reserves to human confirmation, so it runs on Andrew's go. Every branch is kept.
- **Out of scope, 35:** every NFRA row plus `cto_o_tflocal`. These belong to 1.0.0_SA_CTO~O's scope and are in the same
  inventory.

## Report back

Each seat writes its disposition into its own drive log or a surprise row. Send one line to 1.0.0_SA_CTO~Z with the
path when the seat finishes step 1 and step 2. Step 3 is the restart. It does not begin until every seat named above
has reported.
