# ANDREW_DIRECT 2026-10-08 ~20:1xZ -- each box's fabric manager keeps its box synced and its open calls published

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn.

**Context:** reported to Andrew: site Z's box branch is fully in `CLOUD` but site Z is 691 commits behind `origin/CLOUD` (it has
not taken the trunk since the morning), and site Z has not published its open calls; proposed that 0.0.0_AB_MSTR press site Z
to take the trunk, push its local work and publish.

**Andrew, verbatim:**

> "Ok I think we need the fabric managers at each box to manage that, maybe its in their launch script or in claude.md or
> something"

**Same minute, at 4.0.0_SA_CRO~A:** "I think B is the stable long-term solution" -- box-sync runs from a Windows scheduled task
per box, no agent (record `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_201xZ_BOX_SYNC_SCHEDULED_TASK_B.md`).
So the manager's loop does not run box-sync; it verifies the task, resolves a held box, and publishes open calls.

**Placement:** the mechanism is the `/govern` loop every fabric manager arms at instantiation on its own minutes (Andrew
~17:4xZ and ~18:0xZ). Added as `.claude/skills/govern/SKILL.md` Step 3a.7 with a SYNC report line: every cycle, (a)
verify the box's box-sync scheduled task (install if absent), (b) resolve a held box, (c) `open-calls.py publish` and a
cluster read. Not CLAUDE.md (rules index; a loop step is a skill's) and not the launch script
(launch already arms `/govern 30m`, `org/XXX.md` Step 1b-F).
