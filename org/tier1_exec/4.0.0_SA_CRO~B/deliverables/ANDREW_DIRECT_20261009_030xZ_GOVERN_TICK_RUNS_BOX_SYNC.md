# ANDREW_DIRECT 2026-10-09 ~03:0xZ -- every MSTR's /govern tick runs box-sync, pulling in what the rest of the cluster did

**Channel:** laptop terminal, in the 4.0.0_SA_CRO~B session. **Recorded by:** 4.0.0_SA_CRO~B, same turn.

## Andrew's words, verbatim

> "I think their govern ticks should include a box-sync action where they pull in all the stuff the rest of the cluster has
> been working on"

(Asked after the slot table: every MSTR runs `/govern` every 30 minutes, laptop :00/:30, sitez :06/:36, dell1 :12/:42, dell2
:18/:48, per `org/ref/LIVE_ARMS.md`.)

## What it changes

`.claude/skills/govern/SKILL.md` step 7(a) read: box-sync "runs from the box's Windows scheduled task ... never from this loop"
(Andrew ~20:1xZ 2026-10-08, "I think B is the stable long-term solution"). The scheduled task stays (option B is kept); the
govern tick now also runs the pass itself whenever there is something to take: on the integrator box, `box-sync.sh integrate`
when any `origin/box/*` is ahead of `origin/CLOUD`, then on every box `box-sync.sh box` when `origin/CLOUD` is ahead of this
box's branch. box-sync's own pass lock makes a tick that meets the task mid-pass skip (exit 3), never double-merge.
