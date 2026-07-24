# EventBridge Rules vs EventBridge Scheduler — qualification + standardization input

    author:   3.0.0_SA_CVO
    for:      Andrew (direct ask); rolls into OPAL_STNDRD / OPAL_TAXONOMY (trigger standards)
    owner of the ruling: OPAL_STNDRD execution = 0.7.0_AE_CloudOps~Z; standards gate = 1.0.0_SA_CTO.
              CVO role here is to QUALIFY + RECOMMEND with measured tradeoffs; the standard is not
              mine to set.
    grounding: estate counts [MEASURED] live 2026-07-24. AWS service-capability claims are
              [REFERENCE] (well-established AWS design facts; verifiable against AWS docs before a
              ruling if the owner wants — the estate data below is consistent with them).

---

## 0. The direct answer

**No — they are not the same thing, so we cannot collapse to a single service entirely. But they
OVERLAP on exactly one capacity (time-based scheduling), and THAT overlap is where the estate is
out-of-pattern.** The fix is not "pick one service for everything" — it is **"one capacity, one
service"**: assign each capability to exactly one service so nothing is done two ways and a single
API call gives a complete census of each.

---

## 1. What each service is [REFERENCE]

| | **EventBridge Rules** | **EventBridge Scheduler** |
|---|---|---|
| Part of | Amazon EventBridge (the event-bus service) | A distinct, newer service (GA Nov 2022) under the EventBridge umbrella; separate API + console |
| Trigger modes | **TWO:** (a) **event-pattern** (react to an event on a bus — S3 ObjectCreated, a state change) AND (b) **schedule expression** (cron/rate) | **ONE:** time-based only — one-time or recurring (cron/rate) |
| Can react to events? | **Yes** | **No** — cannot match events at all |
| Scheduling extras | basic cron/rate; scheduled rules must sit on the default bus | timezones, flexible time windows, start/end dates, **built-in retry + DLQ**, schedule groups, ~1M-schedule scale, universal targets (~270+ AWS APIs) |
| AWS's own guidance | the original mechanism; for *pure scheduling* AWS now points you to Scheduler | **the recommended service for new scheduled tasks** |
| Census API | `aws events list-rules` (+ `describe-rule`) | `aws scheduler list-schedules` (+ `get-schedule`) — **a different API `list-rules` cannot see** |

**Relationship:** Scheduler is a **specialist** (time-based invocation done well). Rules is a
**generalist** that does both events and schedules. The **only overlap is time-based scheduling**.

---

## 2. How the estate actually uses them [MEASURED 2026-07-24]

Full paginated enumeration of both services:

| Service / capacity | count |
|---|---|
| **Rules — SCHEDULE-type** (`ScheduleExpression`, cron/rate) | **121** |
| **Rules — EVENT-type** (`EventPattern` only) | **20** |
| Rules — both / neither | 0 / 0 |
| **Rules TOTAL** | **141** |
| **Scheduler — schedules** (time-based only) | **10** |

**So time-based scheduling is implemented in BOTH services: 121 scheduled Rules + 10 Scheduler
schedules = 131 schedule objects, split across two services with no semantic rule for which feed
lands where.** Concrete proof of the same-capacity duplication:

    RULE       smartx-account-distribution-daily   cron(30 11 * * ? *)        -> invoke Lambda daily (49F ingestion)
    SCHEDULER  wsb-49f-model-aua-pull-daily         cron(30 3 ? * TUE-SAT *)   -> invoke Lambda daily (49F ingestion)

Same firm, same capacity (daily cron → invoke a Lambda), **different service, no reason.** (The
account-distribution feed CTO traced for MDPF postmortem §7 is the Rule above; the wsb-49f feed
that today's freeze investigation nearly missed is the Scheduler one.)

---

## 3. Why this is the exact problem Andrew named — bad denominator / recall [MEASURED, live incident]

`aws events list-rules` **cannot see EventBridge Scheduler.** They are different APIs. So a census of
"what is scheduled in this account?" run via `list-rules` alone **silently under-counts by the 10
Scheduler schedules** and reports no error — a clean-looking wrong denominator.

**This happened today.** The MDPF freeze investigation (mine and CTO's) enumerated schedules via
`list-rules` and nearly concluded the 49F model feed was unscheduled — until CTO caught that
`wsb-49f-model-aua-pull-daily` lives in **Scheduler**, invisible to that sweep. It also invalidated a
workspace memory that had recorded that feed as "NO scheduler, hand-run." **An asset that lives in
two services for one capacity is un-censusable by one instrument** — which is precisely the
"instrument does not report the boundary of what it can see" class this estate has been paying for
all day, and precisely the failure OPAL_STNDRD / OPAL_TAXONOMY exist to prevent.

---

## 4. The clean pattern — "one capacity, one service"

Because Scheduler *cannot* do the 20 event-pattern rules, the split is forced on the event side and
is a *choice* only on the schedule side. The clean assignment:

- **EVENT-driven triggers → EventBridge RULES** (the only tool that can do it; the 20 stay).
- **TIME-based schedules → EventBridge SCHEDULER** (migrate the 121 scheduled Rules here).

**Result:** Rules = events-only, Scheduler = schedules-only. **Each service does exactly one thing;
each capacity has exactly one home.** Census becomes:
`list-rules` = the complete event-trigger inventory · `list-schedules` = the complete schedule
inventory — no overlap, no service doing double duty, no instrument blind to half its own denominator.

This is simultaneously (a) AWS-idiomatic (Scheduler is AWS's recommended scheduling service), (b) the
OPAL_STNDRD "one resource used in one capacity" spirit, and (c) a permanent fix for the recall
problem.

### The alternative, and why it is weaker
Standardize scheduling on **Rules** (drop Scheduler, migrate the 10). Less migration (10 < 121) —
but it moves *against* AWS's direction, forgoes Scheduler's retry/DLQ/timezone/grouping features, and
**leaves Rules doing two capacities** (events + schedules), so `list-rules` still cannot separate
them without a `ScheduleExpression` filter and the service still does double duty. It fixes the
two-services problem but not the double-duty problem. **Weaker for the taxonomy goal.**

### Recommendation (CVO — for the standard owner to rule, not a ruling)
Adopt **Scheduler-for-time / Rules-for-events**. Migrate the 121 scheduled Rules **on natural
touches** (matching OPAL_STNDRD's existing "renames on natural touches" rollout style), not
big-bang. Encode it as a trigger-standard entry with a census-gate: the OPAL_STNDRD trigger-map must
enumerate BOTH `list-rules` and `list-schedules` until the migration completes, then narrow to
`list-schedules` for schedules. **The ruling is 0.7.0_AE_CloudOps~Z's (execution) + CTO's (gate);
this document is input.**

---

## 5. Immediate application — MDPF_MONOCLEANUP P1 should build TO the standard

MDPF_MONOCLEANUP P1 (the new gold→served publisher) needs, per the matched-pair constraint already
bound into its D1: (a) an **event trigger** on the gold-generation completion marker, and (b) a
**scheduled floor** that fires if the marker never lands. Those are **one of each capacity**.

Under the clean pattern: the event trigger = an EventBridge **Rule**; the scheduled floor = an
EventBridge **Scheduler** schedule. **Building P1 that way makes it the first standard-compliant
instance rather than the 122nd scheduled-Rule inconsistency.** Recommend CTO note this in the
MONOCLEANUP PRD so the new resource is born in-pattern — it is cheaper to build P1 to the standard
than to migrate it later, and P1 is the natural first touch.

---

## Appendix — reproduction [read-only]

```
# Rules capacity split (paginated)
python: boto3 events.list_rules (paginate) ->
        141 total = 121 ScheduleExpression-only + 20 EventPattern-only + 0 both + 0 neither
# Scheduler surface (separate API, invisible to list-rules)
aws scheduler list-schedules   -> 10 schedules
# Same-capacity proof
aws events describe-rule --name smartx-account-distribution-daily --query ScheduleExpression  -> cron(30 11 * * ? *)
aws scheduler get-schedule --name wsb-49f-model-aua-pull-daily     --query ScheduleExpression  -> cron(30 3 ? * TUE-SAT *)
```

— 3.0.0_SA_CVO
