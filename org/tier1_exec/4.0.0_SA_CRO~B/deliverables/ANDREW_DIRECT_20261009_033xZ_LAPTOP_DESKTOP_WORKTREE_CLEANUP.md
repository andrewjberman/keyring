# ANDREW_DIRECT 2026-10-09 ~03:2xZ-03:3xZ -- clean the laptop Desktop's stale worktree folders, with the CVO, careful of dependencies

**Channel:** laptop terminal, in the 4.0.0_SA_CRO~B session. **Recorded by:** 4.0.0_SA_CRO~B, same turn.

## Andrew's words, verbatim

~03:2xZ:
> "Check the desktop on this box, i see all these WK folders, are all of those actually active on here? i see ycdgen and irpt
> work that looks deprecated, as those projects among others, like the advi work and various portal items, all of that is on
> other boxes, we should conserve space and if its necessary, taildrop it to the relevant places, but more likely its trash now
> and we just get rid of it. check it out"

~03:3xZ, answering the census and recommendation:
> "Have CVO work with you on this and be ginger about the dependencies. but generally speaking, I think your plan is good. Also
> yes, the wk-tsc should not be touched for sure. also saving the IRPT patch"

## The approved plan (census at ~03:2xZ, no process using any folder; C: 27 GB free of 238)

- KEEP, never touched: `Desktop\wk-tsc` (dell1.rdp, dell2.rdp, sitez.rdp).
- SAVE first: the 26 uncommitted edits in `Desktop\irpt-smoke-p-portal-20260923` (branch irpt-opal-scope-p-portal-20260923,
  pushed to origin at e0531491, not merged to DEV) as a patch in this deliverables folder.
- DELETE: 37 `wk-*`/`wk_*` shells (each only `portal\node_modules`, a JUNCTION to the live
  `ajb_workspace\portal\node_modules`); portal worktrees `portal-coo-d-p3`, `-r43`, `-regime`, `-holdings`,
  `wt-cto-benchmark-si`, `portal-f1-cd3924d5` (all merged to DEV or at a DEV commit); the non-git copy `portal-trade-vident`;
  then `irpt-smoke-p-portal-20260923` after its patch is saved.
- THE HAZARD ("be ginger about the dependencies"): 42 folders hold a junction into the live portal `node_modules`. Every link is
  removed as a link first (never followed), the folder is deleted only when it holds no link, and the live `node_modules` is
  measured before and after. 3.0.0_SA_CVO reviews the plan before the delete and verifies after.
