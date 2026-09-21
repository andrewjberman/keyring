# ARM RECORD 2026-09-21 ~13:26Z -- 2.0.0_SA_COO~F arms /canonical-drive IRPT_FNTEND, 10m, STANDING, DIRECTED

**Authority:** Andrew-direct 2026-09-21 ~12:37Z (`ANDREW_DIRECT_20260921_1237Z_COOF_SOLE_FOCUS_IRPT_FNTEND_CANONICAL_FLOW_THEN_DRIVE.md` @ae67a8bf46) --
"Use /canonical-flow IRPT_FNTEND to assess state, and then /canonical-drive IRPT_FNTEND to loop its drive."
Corroborated by `1.0.0_SA_CTO` the same minute (IRPT is today's device-wide sole priority).

**Precedent for cadence:** the 2026-09-14 ~16:3xZ record at this same path
(`ANDREW_DIRECT_20260914_163xZ_COOF_CANONICAL_DRIVE_IRPT_FNTEND.md`) established 10m, STANDING, DIRECTED for
this lane's own active project, per `.claude/skills/canonical-drive/SKILL.md` s.0 and Andrew-direct 2026-09-11
~22:2xZ ("Both COOs need to be on 10m /drive loops for their projects"). Today's word re-seats this lane on the
SAME project after the 2026-09-15 free-after-round-8 plan, so the same cadence rule applies without needing a
fresh derivation.

**CLASS:** DIRECTED. **SCOPE:** IRPT_FNTEND only. **CADENCE:** 10 minutes, off-minute
(`4,14,24,34,44,54 * * * *`), session-local cron `b1f8684b`. **STOP-CONDITION:** IRPT_FNTEND `status: complete`
per the register, the project leaving DECOMP/EXECUTING/ROUND_CLOSE, or Andrew's stand-down.

**Tick 1** (this record's own trigger) already ran: L5 recut to v0.9 (`6f56917cef`), L6 wave-A issuance
(`a21bf57e05`), 7 of 8 wave-A workers spawned, drive log `e2207972b5`.

## CARRIER

The live cron (`b1f8684b`) is session-local; `CronList` at this seat is the artifact. Per `org/XXX.md` Step
1b-F, this seat arms its own loop and does NOT author its own Step 1b-F row: `1.0.0_SA_CTO` lands the row from
this record.

## BROADCAST

MCP to `1.0.0_SA_CTO` and `0.0.0_AB_MSTR` the same turn.
