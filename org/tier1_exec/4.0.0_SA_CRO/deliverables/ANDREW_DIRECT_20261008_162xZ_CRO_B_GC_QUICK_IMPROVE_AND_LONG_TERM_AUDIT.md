# ANDREW_DIRECT 2026-10-08 ~16:2xZ -- CRO~B: improve the short-term GC fix now; audit the high-traffic scripts for the long term

**Channel:** laptop terminal, to 4.0.0_SA_CRO~B.
**Recorded by:** 4.0.0_SA_CRO~B, same turn.

## Andrew's words, verbatim

> "Look into how we can quickly improve the short term solution for now, and then let's discuss long term by running
> an audit on these high traffic processes and assess how much work it would really require to make the necessary
> adjustments. I believe that all of these can be audited/understood fairly quickly, like in the next hour or less:"

The list he pasted with it, verbatim:

> 2. Zombie processes
> - Quick:
>   - Upgrade the existing zombie killer. It should stop whole process trees (the leftover children are dell1's leak)
>     and also catch replaced duplicates, orphaned watchers, leaked native processes and dead sessions' shells.
>   - A rule that any hand-written monitor ends itself at 29.5 minutes.
>   - One sweep per box: a dry run first, then the real kill.
> - Long-term:
>   - Every high-traffic script (watcher, agent bus, safe-commit, safe-deploy, broker, poller) has a time limit, refuses
>     to run a second copy, and dies with its session.
>   - A check that warns before anyone arms a script with no exit.
>   - The killer runs on its own when a box needs it and keeps a record of what it stopped.
>   - Merged, idle worktrees are removed within limits you set.

## Placement

4.0.0_SA_CRO~B's GC and script-ops lane (record `ANDREW_DIRECT_20261008_155xZ_CRO_B_SESSION_FOCUS_GC_AND_SCRIPT_OPS.md`).
"29.5 minutes" sets the hand-written Monitor bound at 1770 s (this seat's FAST FIX list had 1790 s).
