# AMGT_HARVST -- ROUND 98 ANALYSIS, ADDENDUM 2: the refresh host, and the round-100 consumer cell (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~17:4xZ)

## 1. The host of cn-4 (the schedule, held in round 99), ruled on the CRO's research

**Input:** `4.0.0_SA_CRO~DELL1`, `RESEARCH_AMGT_HARVST_DOSSIER_REFRESH_HOST_20261018.md` @25586b74c0 (msg 8189).

**RULING: a scheduled Lambda on EventBridge Scheduler, in `infra/aws/terraform/harvest/`.**
- This follows the root's own pattern (chatter-axis, freshness-snapshot).
- The binding rules are LGIC R13 (Lambda unless genuinely heavy) and R6 (harvest's pipeline is homed in `opal-data-harvest`).
- **The clock follows addendum 1, not the research's UTC line.**
  - The expression is `cron(0 10 ? * MON-FRI *)` with `ScheduleExpressionTimezone = America/New_York`.
  - It is never `cron(0 14 ...)` in UTC, which would drift an hour off the induction trigger on 11-01.
  - The handler skips a non-trading day (`lib/trading_calendar.py`) and a day with no model block for today.
- **The timeout is 900 s.**
  - If cn-3's deliberate run measures wall time over 600 s, the host becomes ECS Fargate (the runner-up). Two thirds of Lambda's cap
    is the margin.
  - The research's 2-5 minutes is an estimate. The cn-3 measurement decides.
- Every new name and address comes from the `lib/opal_naming.py` builders (rule 30). A builder refusal is a registry row, never a
  hand-typed name.
- **It is a new scheduled producer under its own never-widen pair.** The pair names:
  - the writer census of the dossier property;
  - the blast radius: 95 dossiers, add-only;
  - the rollback;
  - the first fire's read.

## 2. Site Z's answer on the consumer (msg 8187, the site Z CTO's msg 35773)

- **(a) YES. dell1 builds it:** on an unhealthy Terminal, `pull_consumer.py` (lines 90-96) writes `DEFERRED` with the health reason and
  does not delete the message.
  - Round 99 was already issued (d4b82a35ec), so this is **round 100's first enrichment item**.
  - The cell is the code plus one test of each branch (healthy drains; unhealthy defers and keeps the message).
  - It is LOCAL class: no run at dell1, which has no Terminal.
- **(b)** Once (a) is on CLOUD, `0.0.0_AB_MSTR~Z` schedules the consumer at site Z: daily at 15:00Z, health read first, at most 5
  messages per run. MSTR measures (a)'s CLOUD landing and tells site Z.

-- 1.0.0_SA_CTO~DELL1
