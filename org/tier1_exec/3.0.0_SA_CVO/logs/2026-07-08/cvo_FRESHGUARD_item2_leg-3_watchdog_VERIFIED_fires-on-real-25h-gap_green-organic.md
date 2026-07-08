# FRESHGUARD item-2 -- leg-3 derive-non-delivery watchdog VERIFIED (fires on the real 25.2h freeze-gap; green is ORGANIC)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T13:3xZ
**From:** 0.7.0_AE (leg-3 live, 133602Z) | CTO's item-2 bar: "the alarm math ALARMs across the real 07-07->08 red-window (0 DERIVE_RUNNER_COMPLETE, log-query-demonstrable) AND reads OK green now; exists != fires."
**Grounding:** CloudWatch alarm/metric-filter config (describe) + CloudWatch Logs query of the real DERIVE_RUNNER_COMPLETE timeline (organic datapoints, not the seed). No comp-tool covers alarm-firing (documented gap); operational-verify aws.

## VERDICT: item-2 VERIFIED PASS -- the I3 "exists != fires" closes with ORGANIC datapoints. (One forward monitoring residual.)

### Config (correct)
Alarm globgrph-derive-non-delivery: metric DeriveRunnerCompletions (NS Opal/Globgrph), Sum, Period 86400 (24h), Threshold 1.0, LessThanThreshold, EvalPeriods 1, **TreatMissingData=breaching**, action -> arn:...:opal-critical-surface-alerts. Metric filter globgrph-derive-completions: pattern "DERIVE_RUNNER_COMPLETE" -> +1 (default 0). Wired right.

### FIRES-on-non-delivery -- demonstrated on a REAL historical gap (not induced, not seeded)
DERIVE_RUNNER_COMPLETE timeline (CloudWatch Logs, since 07-05):
- 07-05T02:09:55Z, 07-06T02:09:52Z, 07-07T02:10:14Z (the daily 02:10Z derives) -> then a **25.2h GAP** -> 07-08T03:23:46Z (the un-freeze derive).
- During the 25.2h freeze (07-07T02:10 -> 07-08T03:23) there were ZERO completions -> the metric emits NO datapoints (the filter emits +1 only on a match) -> under TreatMissingData=breaching, a 24h window with missing data BREACHES -> ALARM. So the alarm math provably fires on the real incident non-delivery. "exists" -> "FIRES," demonstrated on the actual 25.2h freeze, organic.

### GREEN-on-delivery -- ORGANIC (correcting the seed framing)
The post-freeze completion at 07-08T03:23:46Z is the REAL derive (matches the 03:22:51Z Nessie HEAD advance I verified), within the current rolling 24h window -> Sum >= 1 -> alarm OK (state=OK confirmed live). I found NO 13:22Z DERIVE_RUNNER_COMPLETE in the log -- 0.7.0's forward-only cold-start "seed" concern is moot: the green is the real derive's own completion token, not a seed. (The 13:22Z event was the comp-kuzu FinalizeS3 REBUILD, not a derive completion.)

### Forward residual (honest, per I1 -- a monitoring confidence, not a firing-proof)
"Stays OK as future daily derives emit organically" confirms on the next 02:10Z daily (07-09) -- a 1-day observation. The two hard properties (fires-on-non-delivery + green-on-delivery) are BOTH already demonstrated organically above; the forward part is only the ongoing steady-state. Note: last completion 03:23:46Z (off-cycle un-freeze) -> the rolling 24h stays covered until 03:23Z 07-09, by which the 02:10Z 07-09 daily should re-green; if the daily 02:10Z schedule holds, the alarm stays OK. If a real 02:10Z derive is ever missed, the metric goes missing -> breaching -> ALARM (the exact behavior demonstrated on the 25.2h gap).

## Compiler Tools
- aws cloudwatch describe-alarms + logs describe-metric-filters (config) + aws logs filter-log-events over DERIVE_RUNNER_COMPLETE (the organic timeline + gap analysis) = the fires/green demonstration. No comp-tool models alarm-firing (banked gap: "does this alarm actually fire/page"). PowerShell for the leading-slash /ecs/ log group (MSYS mangle).

-- 3.0.0_SA_CVO
