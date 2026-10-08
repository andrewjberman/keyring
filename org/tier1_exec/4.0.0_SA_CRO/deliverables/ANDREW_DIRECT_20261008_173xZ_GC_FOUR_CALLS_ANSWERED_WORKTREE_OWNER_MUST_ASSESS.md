# ANDREW_DIRECT 2026-10-08 ~17:3xZ -- GC open calls 1-4 answered; a held worktree needs its owner online to assess

**Channel:** laptop terminal, to 4.0.0_SA_CRO~B, answering its four open-call cards (session of record
`ANDREW_DIRECT_20261008_164xZ_REAPER_UNATTENDED_OK_IF_SESSION_SHELLS_ASSIGNED.md`).
**Recorded by:** 4.0.0_SA_CRO~B, same turn.

## Andrew's words, verbatim

> "1.) Yes approved. 2.) Agreeed. 3.) Yes approved. 4.) I agree with 24 hours but we dont want to lose uncommitted
> work, therefore there has to be exceptions made if for example an agent is brought online, the session ends before
> worktrees are all committed, and days go by. The agent has to be online to assess in essence if the situation
> develops where we spot a worktree thats hanging around for multiple days, do you understand what I mean? lets think
> of a clean simple mechanism for how to handle that"

## What each answer rules

1. **Install the unattended reaper on the laptop as soon as it lands, every 15 minutes:** approved.
2. **Rollout to dell1, dell2 and site Z after one clean hour on the laptop:** agreed.
3. **Long-term script fixes:** approved in the recommended order: agentbus/watcher fixes and the Monitor warning in
   parallel first, then the broker, then the safe-* residue (handed to 4.0.0_SA_CRO~A for safe-commit/safe-merge per
   CTO msg 107031).
4. **Worktree removal:** 24 hours of idleness, BUT no uncommitted work may be lost. A worktree left with uncommitted or
   unmerged work (for example, a session ended before committing and days went by) is never removed blind: its
   owning agent has to be online to assess it. The mechanism is to be designed "clean" and "simple" and brought back.

## Addendum ~17:4xZ -- the held-worktree threshold, verbatim

4.0.0_SA_CRO~B proposed: CLEAN (merged into CLOUD, nothing uncommitted or untracked, idle 24 h, not drain-*/fenced)
is removed automatically; HELD (any unlanded work) is never touched and is owned by the serial on its newest unlanded
commit (else the serial in its branch/path name, else the box's MSTR); the owner is told at its next registration;
and if the owner has not come back after 72 hours, the box's MSTR brings that seat online to assess it. Andrew:

> "48 Hours is better"

Ruled: the held-worktree threshold is **48 hours**, not 72. The rest of the mechanism stands as proposed.

## Reconciliation ~17:4xZ -- two answers on the scheduled task (surfaced, not adjudicated)

- To 4.0.0_SA_CRO~B (~17:3xZ), card 1 "install the unattended reaper on the laptop ... every 15 minutes": "1.) Yes
  approved." The task was installed at 17:32Z and ran twice, cleanly (KILL-MAINT-RUN 17:32:16Z and 17:33:14Z, 0
  targets).
- To 1.0.0_SA_CTO (~17:4xZ, the later word), card 1 "(a) /govern only or (b) also a scheduled task": "1.) A is better
  for now." (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
  @9932790e65).

Act: the later word was followed. The laptop task was uninstalled at ~17:4xZ (`.tools\kill-maint-task.ps1 -Uninstall`;
`-Install` restores it in one command). `/govern` Step 3a.6 is the one unattended reaper for now. The question went
back to Andrew to confirm.
