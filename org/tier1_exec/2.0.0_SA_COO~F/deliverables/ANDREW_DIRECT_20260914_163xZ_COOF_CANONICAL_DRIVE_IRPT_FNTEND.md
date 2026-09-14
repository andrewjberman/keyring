# ANDREW-DIRECT 2026-09-14 ~16:3xZ -- 2.0.0_SA_COO~F continues IRPT_FNTEND under /canonical-flow and runs /canonical-drive IRPT_FNTEND

**Seat:** `2.0.0_SA_COO~F` (laptop, branch CLOUD) · **Channel:** Andrew at this lane's terminal, typed mid-turn during the
post-reboot startup · **Recorded:** the same turn it was given (UTC clock read 16:38Z at recording).

## VERBATIM

> "yes you will be continuing where you left off with /canonical-flow on IRPT_FNTEND. Once establishing state, and your
> last log on the subject, you will run /canonical-drive IRPT_FNTEND."

## WHAT IT RULES, NO WIDER

1. `2.0.0_SA_COO~F` continues IRPT_FNTEND where its wind-down handoff left it (log @94f5fa9257), on the canonical workflow.
2. After establishing state and reading that log, `2.0.0_SA_COO~F` runs `/canonical-drive IRPT_FNTEND`. The skill's bare
   form with a scope is one tick plus a cron. Its cadence for a COO on its own active project is **10m, STANDING and
   DIRECTED** (`.claude/skills/canonical-drive/SKILL.md` s.0, Andrew-direct 2026-09-11 ~22:2xZ "need to be"). So this arm
   records as **DIRECTED**, scope **IRPT_FNTEND ONLY**, cadence 10m. **STOP-CONDITION:** IRPT_FNTEND `status: complete` per
   the register, the project leaving DECOMP/EXECUTING/ROUND_CLOSE, or Andrew's stand-down.
3. NOT RULED: any other project, any change to `org/missions/SEQUENCE.yaml`, and the PORTAL FREEZE (local DEV commits only),
   which stands.

## CARRIER

The live cron is session-local; `CronList` at this seat is the artifact. Per `org/XXX.md` Step 1b-F, this seat arms its
own loop and does NOT author its own Step 1b-F row: `1.0.0_SA_CTO` lands the row from this record.

## BROADCAST

MCP to `1.0.0_SA_CTO` and `0.0.0_AB_MSTR` the same turn. The base `2.0.0_SA_COO` is not live, so no message goes to it.
