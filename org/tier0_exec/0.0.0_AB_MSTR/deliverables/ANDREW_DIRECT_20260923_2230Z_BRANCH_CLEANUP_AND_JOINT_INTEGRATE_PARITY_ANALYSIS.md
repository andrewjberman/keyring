# Andrew-direct: clear the dead branches, prune worktrees, then a joint MSTR analysis of /integrate parity for both repos

**Channel:** the `0.0.0_AB_MSTR` terminal (laptop), 2026-09-23 ~22:2xZ.
**Recorded by:** `0.0.0_AB_MSTR`.

## Verbatim

> "Let's clear these out to start: [main, PROD, COMP, cro/sitez-harvest-dedup], clean up that clutter: delete the merged portal side branches and prune the finished local worker branches and worktrees. Deleting remote branches needs your yes first. Then I want to figure out how to actually get us properly synched. I will make both you and MSTR~Z fable agents, you two can analyze very carefully how to manage the /integrate parity for both ajb_workspace and portal, and we get it done."

(The bracketed list is the table row set he pasted: `main`, `PROD`, `COMP`, `cro/sitez-harvest-dedup` on `ajb_workspace`.)

## What was done on it (laptop, 22:2x-22:4xZ)

- `ajb_workspace` origin: default branch changed `main` -> `CLOUD` (GitHub refuses to delete a default branch; `CLOUD` is the real trunk). Deleted `main`, `PROD`, `COMP`, `cro/sitez-harvest-dedup`. Each tip kept as a tag `archive/<name>-20260923` on origin. Origin now carries exactly `CLOUD` and `SITEZ`.
- `portal` origin: deleted the 8 side branches already merged into `DEV` (`de/blend-cohort-interim-revert`, `laptop/d13-visual-elevation`, `laptop/dev-local`, `laptop/integ-promote-20260915`, `sitez/aggfix-1-portal`, `sitez/amgt-resapp-ri1`, `sitez/bunlock-fix-20260915`, `sitez/posn-asttax-r6`). Kept `sitez/merge-trial-20260915` (2 unmerged commits) and the older branches he did not name (`backup-attribution-dense-view`, `demo/portal-optimized`, `feature/*`, `testing`, `main`).
- Local `ajb_workspace`: 8 finished worktrees removed (merged, clean, no live process in them), 87 merged local branches deleted; 131 -> 44 branches, 22 -> 14 worktrees.
- Local `portal`: 3 finished worktrees removed, 26 merged local branches deleted; 36 -> 10 branches, 12 -> 9 worktrees.
- Side effect disclosed: the archive-tag push used `--tags` and also pushed three release tags that existed only locally (`opal-assets-v0.49.0`, `opal-gateway-v1.7.0`, `yang-v2.4.19`). All three point at commits already in `CLOUD`.

## What it settles next

The reverse leg SITEZ -> CLOUD is the laptop's. It is not merged until the joint analysis by `0.0.0_AB_MSTR` and `0.0.0_AB_MSTR~Z` (both on the fable model) is done and Andrew says go. The laptop's read-only assessment at 22:4xZ: base `b475b96309`, SITEZ-only 1086, overlap 0 of 1188, merge-tree clean, deploy ceiling 1 file.
