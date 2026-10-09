# ANDREW_DIRECT 2026-10-09 ~00:4xZ-00:5xZ -- a cloud on/off switch for the keep-work-driving mode, flipped by a skill

**Channel:** laptop terminal, in the 4.0.0_SA_CRO~B session. **Recorded by:** 4.0.0_SA_CRO~B, same turn.
**Parent order:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`.

## Andrew's words, verbatim

~00:4xZ:
> "Yes I also want to be able to flip this mode on or off somewhere in the cloud, it should be a switch that we use a skill
> to flip on and off, and the mode is checked via the open-calls jsons per box in aws or something like that, should be
> tacked onto that process. /draw it for me how it is currently and make suggestions based on current state how we could do
> this"

~00:5xZ, answering the /draw and its recommendation:
> "I like it, go with your rec"

## The recommendation he approved (option a, as drawn in session)

One object `s3://opal-313476888478-globgrph/fabric/open-calls/v1/mode.json` beside the per-box open-calls JSONs, holding
`scan` and `empty_tick` (on|off), optional per-box overrides, and who set it, when and why. A skill `/keep-driving
on|off|status` flips it through `.tools/open-calls.py mode`. Each scan pass reads it first (off: sends nothing; the
heartbeat says `mode=off`, so paused never reads as dead); each COO empty tick reads it before running `/next-calls --drive`
(off: a plain NO-OP). Absent object = ON (his standing order). Not taken: (b) a field in each box's JSON, (c) an SSM
parameter, (d) disabling the scheduled tasks.
