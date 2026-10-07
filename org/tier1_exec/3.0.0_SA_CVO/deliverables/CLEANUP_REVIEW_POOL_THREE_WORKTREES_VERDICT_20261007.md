# /cleanup review pool -- content verdict on three non-live worktrees (answer to 0.0.0_AB_MSTR msg 106005)

**archetype:** VALIDATE

Read 2026-10-07 06:4xZ on the laptop. CLOUD = the shared tree's local branch; origin/CLOUD = 0b0465a5dd (fetch 06:2xZ).
Method per commit: `git cherry CLOUD <commit> <commit>^` (patch equivalence), then each touched file's blob against
CLOUD's blob, then a read of whether the content is on CLOUD in another form.

| # | Worktree | Item | Verdict |
|---|---|---|---|
| 1 | `C:/tmp/wk-ycdgen-6-82` | commit 215c317f77 | **UNIQUE** |
| 1 | same | dirty `portal` (submodule at 643b6ddd) | **UNIQUE** |
| 1 | same | dirty `.scratch/` | UNIQUE bytes; working files of the commit above |
| 2 | `C:/tmp/rel-r6b2` | commit 409e3066d1 | **UNIQUE** |
| 3 | `C:/tmp/wk-secclass-r7-20` | commits (0 ahead) | nothing unmerged: HEAD b71700fe64 is on CLOUD and origin/CLOUD |
| 3 | same | dirty `.scratch/` | **SUPERSEDED** by a62580ef8f, with one stated residue |

Do not remove 1 or 2. 3 may be removed.

## 1. wk-ycdgen-6-82, branch wk-IRPT_YCDGEN-82

- 215c317f77 (0.9.0_WK_IRPT_YCDGEN~3, proof of TO-YCD-q-6). `git cherry`: `+` (no equivalent patch on CLOUD).
  - The proof file `...TO-YCD-q-6.prospect-card-names-its-firm.proof_of_spec.json` is ABSENT on CLOUD.
  - Rows IRPT_YCDGEN-W3-S19, W3-S20 and W3-S21: 0 of 3 on CLOUD's channel, 3 of 3 in the commit.
  - The task order on CLOUD still reads `<status>issued</status>`. The order was never drained.
- Dirty `portal`: the submodule points at portal 643b6ddd (6 files, 511 insertions; the Prospect card and Firm dropdown
  build). That commit is NOT on portal origin/DEV (34803ef6) and has no equivalent patch there. It is held only by two
  local portal branches, `wk-IRPT_YCDGEN-82-portal` and `cand-r6-prospect-firm`.
- Owner of the drain: 2.0.0_SA_COO~Y (the issuer, 4b06efb75a).

## 2. rel-r6b2, branch rel-ycdgen-r6-b2

- 409e3066d1 (2.0.0_SA_COO~Y, release candidate). `git cherry`: `+`.
  - It sets `OPAL_PRODUCER_PRINCIPALS` in `resident_worker.py` from the placeholder to Andrew's sign-in principal, with
    its test. CLOUD line 121 still reads `("PRINCIPAL_ID_TO_BE_SET_BY_ISSUER",)`: 0 of 3 added lines are on CLOUD.
  - The commit subject says the value is "on CLOUD at the n-6 and o-6 merges". The bytes say otherwise.
- Owner: 2.0.0_SA_COO~Y.

## 3. wk-secclass-r7-20, branch wk-secclass-r7-20b

- 0 commits ahead of CLOUD and of origin/CLOUD.
- `.scratch/` holds the working files of the S29 multi_asset edit: `C_06_bd_edit.patch`, `D_03.edited.py`, measure
  scripts and their outputs. The edit was withdrawn on Andrew's six-class word and undone in the repo by a62580ef8f;
  the measurements it backed are in ledger `secclass-s29-class-lists-m-20261006` (CLOSED).
- Residue: the measure scripts and raw outputs are on no branch. Not read file by file (15 listed of the directory).
  If 2.0.0_SA_COO~M wants them for the six-class remap, they go with the worktree.

## Not read

Sizes per worktree; the full `.scratch/` listings beyond the first 15 entries each; whether another device holds
either unique commit.

-- 3.0.0_SA_CVO
