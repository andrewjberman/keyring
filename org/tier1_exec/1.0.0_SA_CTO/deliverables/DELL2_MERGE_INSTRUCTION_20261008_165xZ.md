# Instruction to dell2's fabric manager: merging the GitOps / GC / graph fast-fix work (1.0.0_SA_CTO, 2026-10-08 ~16:5xZ)

**Order:** Andrew-direct ~16:5xZ, laptop terminal, verbatim: "Ok also, I am leading a reboot of the DELL1 Box, the Dell2
box just rebooted, and i want you to have MSTR send an instruction to the DELL2 box on how they should handle merging
with the new work that has been done on these subjects."
**Carrier:** 0.0.0_AB_MSTR sends the FRAME TEXT below to dell2 over the agentbus, verbatim. Dell2 cannot read this file
until it has merged, so the frame carries the whole instruction.

## FRAME TEXT (send verbatim)

```
For dell2's fabric manager, from laptop 1.0.0_SA_CTO via 0.0.0_AB_MSTR (Andrew-direct ~16:5xZ). Merging today's fast fixes:
1. WAIT for the laptop's push frame naming the origin CLOUD hash that carries the fast-fix set (govern GC step, kill-maint
   tree-kill, safe-commit lock fix, watcher Monitor bound). Until then commit locally as usual; do not drain.
2. DRAIN IN A LINKED WORKTREE, not the shared tree (the new /integrate text arrives inside this merge, so do it by hand):
   git worktree add <scratch>/drain-<ts> -b drain/dell2/<ts> CLOUD; in it: git fetch origin; bash .tools/safe-merge.sh
   origin/CLOUD; run the TREE-drop check (--diff-filter=D) there; then bash .tools/safe-merge.sh CLOUD for local commits
   made meanwhile. In the shared tree: git merge --ff-only drain/dell2/<ts> (repeat the catch-up if it refuses). Push, then
   git worktree remove the drain tree and delete its branch.
3. Surprise-channel conflicts: resolve by hand as a union of rows INSIDE the JSON list. There is no union merge driver
   (rolled back: it broke the JSON list).
4. After the merge: git update-index --test-untracked-cache; if OK, git config core.untrackedCache true.
5. Then one GC sweep: powershell -NoProfile -File .tools/kill-maint.ps1 -Mode scripts (dry), read the targets, then
   -Execute. From then on every /govern cycle runs Step 3a.6 (garbage collection).
6. Reply over the bus: the merge hash, push state (ls-remote read), and the GC count.
```
