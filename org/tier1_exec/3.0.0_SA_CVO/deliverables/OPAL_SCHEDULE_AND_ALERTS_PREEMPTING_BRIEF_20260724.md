# OPAL_SCHEDULE + OPAL_ALERTS — preempting brief

    author:   3.0.0_SA_CVO
    for:      Andrew (direct ask) — preempts two new projects: OPAL_SCHEDULE (triggers) and
              OPAL_ALERTS (alarms), each a cleanup + potential reorganization of the estate's
              scheduling / alerting surface.
    date:     2026-07-24
    grounding: [MEASURED] live AWS 2026-07-24 (EventBridge Rules, EventBridge Scheduler,
              CloudWatch alarms) reconciled against the existing `trigger-map.json` census
              (built 2026-07-18 by trigger-census.py, OPAL_STNDRD). Census membership reconciled
              to live: +2 added since 07-18, 0 phantom — the census is reliable minus those two.
    sibling:  EventBridge Rules-vs-Scheduler standardization input @e0828c47f (the "which service"
              question this brief's reorg axis builds on).

---

## 0. Why this exists

Two capabilities are scattered across the estate with no single semantic view, which is how we
got bad denominators when scanning them (a schedule census via `list-rules` alone silently misses
the 10 EventBridge Scheduler entries; the alarm surface has no semantic census at all). Andrew's
ask: assess **what we have and when it fires**, grouped by the actual product, as the input to two
cleanup/reorg projects.

**The good news up front: for TRIGGERS the semantic census already exists** — `trigger-map.json`
tags every trigger with its `unit` and `tf_file`, so grouping by product is a solved problem that
just needs to be kept fresh and acted on. **For ALARMS it does NOT exist** — that gap is itself the
first OPAL_ALERTS deliverable.

---

# PART A — OPAL_SCHEDULE (triggers)

## A.1 What we have, by product [MEASURED — 151 live triggers: 141 Rules + 10 Scheduler]

Grouped by Terraform module → product. "When" is the enabled-schedule cadence class; `D` = disabled.

| Product (TF module) | triggers | R / S | when (enabled) | disabled |
|---|---:|---|---|---:|
| **News** (`news-pipeline/`) | 26 | 26/0 | daily, twice-daily | **4** |
| **Inflection ETL** (`inf-pipeline/`) | 24 | 24/0 | daily ~13:xx suite, hourly parity | **3** |
| **Black Diamond / 49F** (`bd-pipeline/`) | 20 | 20/0 | 21:xx pipelines, 15-min keepalive, weekday | **3** |
| **Monolith** (`opal-assets` tfstate) | 9 | 8/1 | daily silver sweeps + mirrors | 0 |
| **SmartX / 49F** (`smartx-pipeline/`) | 7 | 3/4 | daily pulls (mixed Rules+Scheduler) | **2** |
| **NFRA / infra-audit** | 7 | 7/0 | 15-min, event | 1 |
| **Cottonwood** (`cot-pipeline/`) | 6 | 6/0 | 06:00 rebalancer, hourly parity, 15-min | 0 |
| **Market Overview** (`market-overview/`) | 6 | 6/0 | daily, twice-daily, weekday | **3** |
| **Macro / FRED** (`fred-pipeline/`) | 6 | 6/0 | daily, weekly, monthly | 0 |
| **Dependency Graph** (`globgrph/`) | 6 | 5/1 | daily/nightly producers | 0 |
| **Schwab custody** (`canonical-schwab-ec2/`) | 5 | 5/0 | 10:15 + 22:15 pulls, 12:15 sweep | 1 |
| **ETF** (`etfs-*/`) | 5 | 4/1 | daily, monthly | 0 |
| **Shared infra / monitoring** (`shared-infra/`) | 4 | 4/0 | 5-min, daily, weekday | 0 |
| **Model Portfolios (MDPF)** (`mdpf-pipeline/`) | 3 | 1/2 | event (INF marker) + wp5 feeders | 0 |
| **M365 gateway** | 2 | 2/0 | 6-hourly | 0 |
| **Seeking Alpha**, **YCharts**, **Portal auth**, **ASTN**, **Exec Summary**, **OPAL_CONSOLIDATION** | 1 each | — | daily / event / disabled | 2 total |
| **ARCHIVE (dead / audit-doc only)** | 5 | 5/0 | — | 0 |

*(Full per-trigger detail with exact crons: `trigger-map.json` + this session's reconciliation.
News, Inflection, and Black Diamond alone are 70 of 151 — nearly half the surface.)*

## A.2 Cleanup candidates [MEASURED]

1. **19 DISABLED triggers (18 Rules + 1 Scheduler)** — the first cleanup denominator. A disabled
   trigger is either dead-and-should-be-deleted or intentionally-parked-and-should-be-documented;
   right now they are neither. Named:
   `bd-49f-fees-runner-daily`, `bd-49f-runner-daily`, `bd-gold-layer-monthly-trigger`,
   `canonical-schwab-si2-download-schedule`, `consolidation-gold-runner-scheduled-start`,
   `dc2-test1-offpeak-harness`, `inf-canonical-prices-daily`, `inf-gold-full-on-bronze-complete`,
   `inf-gold-incremental-daily`, `keyword-drilldown-generator-daily`,
   `keyword-intelligence-generator-daily`, `layer3-gpt-curation-daily`, `news-api-1100am`,
   `smartx-daily-export-trigger`, `trending-topics-portal-publisher-{morning,afternoon,daily}`,
   `ycharts-session-capture-schedule`, `smartx-model-monthly-pull-daily` (Scheduler).
   *(The three `trending-topics-portal-publisher-*` are the name-collision that fooled a substring
   census earlier today — a concrete example of why grouping matters.)*
2. **5 triggers whose only declaration is an ARCHIVE / audit doc** (`infra/aws/archive/*.md`,
   `nfra_terraform_p1/*.json`) — declaration drift: the census can't tie them to live TF. Either
   they are live-but-undeclared (a real TF-parity gap) or stale census rows. Resolve each.
3. **The Rules-vs-Scheduler split** (sibling @e0828c47f): SmartX (3 Rules + 4 Scheduler) and MDPF
   (1 Rule + 2 Scheduler) are the mixed-service products — same capacity, two services, no reason.

## A.3 Reorganization axes [for the project to weigh, not adjudicated here]

- **Service standardization** — event→Rules, time→Scheduler (the @e0828c47f recommendation);
  migrate the 121 scheduled Rules on natural touches so a schedule census is one API call.
- **Cadence clustering / collision** — many daily pulls land 10:xx–16:xx; worth a timeline view to
  spot contention and to sequence dependent chains explicitly rather than by cron-guessing (the
  MDPF freeze was a chain that fired off another pipeline's marker with no floor).
- **Naming grammar** — the census enforces `{unit}-{function}-{cadence}`; `conforms` flags
  non-conformers. Renames-on-natural-touch fold in here.

## A.4 Proposed OPAL_SCHEDULE scope

1. **Refresh + own the census.** `trigger-census.py` exists and drifts (+2 in 6 days). Put it on
   the drift-check it already has a workflow for (`trigger-map-drift.yml`) and make the map the
   canonical answer to "what fires, when, for which product."
2. **Retire the 19 disabled + resolve the 5 archive-declared.** Delete the dead, document the parked.
3. **Standardize the service split** (A.3) on natural touches — MDPF_MONOCLEANUP P1 is already
   building to it as the first compliant instance.
4. **A timeline / collision review** of the daily cadence band.

---

# PART B — OPAL_ALERTS (alarms)

## B.1 What we have [MEASURED — 51 CloudWatch alarms]

By product (best-effort by name; **alarms carry no `unit`/`tf_file` tag** — see B.3):

| Product | alarms | | Product | alarms |
|---|---:|---|---|---:|
| Inflection | 8 | | ETF | 3 |
| FirmSep guard | 5 | | Model Portfolios | 3 |
| Exec Summary | 3 | | Dependency Graph | 2 |
| CloudFront (portal edge) | 3 | | Black Diamond | 2 |
| `cmtque` (comms queue) | 4 | | GLDINC | 2 |
| `opal-*` shared | 7 | | YCharts / ASTN / Orion / Portal / WSB | 1 each |

State: **45 OK, 5 INSUFFICIENT_DATA, 1 ALARM.**

## B.2 Cleanup candidates [MEASURED]

1. **⚠ ONE ALARM IS FIRING RIGHT NOW: `cmtque-worker-down`.** Live, in ALARM state. Flagging it
   explicitly — it is either a real down worker or a stale alarm on a retired resource. Worth a look
   independent of the project.
2. **12 alarms have NO alarm action — they fire into the void.** An alarm with no SNS/action is a
   dashboard light nobody is paged by; it is the alarm-equivalent of a guard nothing invokes. Named:
   `PortfolioExcelGenerator-Errors`, `cloudfront-high-error-rate`, `cloudfront-high-origin-latency`,
   `cloudfront-low-cache-hit-rate`, `etfs-netassets-daily-errors`,
   `exec-summary-advisors-processed-ceiling`, `exec-summary-tokens-in-anomaly`,
   `opal-partners-data-{duration-high,errors,throttles}`, `wsb-49f-model-aua-daily-errors`,
   `wsd-49f-partner-held-etf-daily-errors`. **Either wire an action or delete — an actionless alarm
   is worse than none because it reads as coverage.**
3. **5 INSUFFICIENT_DATA** — alarms that have never had enough data to evaluate; likely on
   resources that never emit the metric. Verify each is watching a live resource.
4. **The failure-vs-liveness gap** (the MDPF incident's root cause, one altitude up): the alarms we
   have are overwhelmingly **failure alarms** (`*-errors`, `*-throttles`). Almost none fire on
   *"the thing did not run at all"* — which is exactly how the MDPF freeze went six days unseen with
   `Errors=0`. OPAL_ALERTS should add **did-not-run / staleness alarms** as a class, not just error
   alarms.

## B.3 The structural finding — alarms need the census triggers already have

`trigger-map.json` gives every trigger a `unit` + `tf_file` semantic tag, so "group by product" is
one query. **Alarms have no equivalent** — I grouped the 51 by name-substring, which is exactly the
brittle, connection-blind approach that produces bad recall. **The first OPAL_ALERTS deliverable
should be an `alarm-map.json` census** (the alarm twin of `trigger-census.py`): every alarm tagged
with its product, its TF source, its target action, and its class (failure vs did-not-run). That
turns "what alerts do we have and are any useless" into a one-call, always-fresh answer — the same
win OPAL_STNDRD already bought for triggers.

## B.4 Proposed OPAL_ALERTS scope

1. **Build the `alarm-map.json` census** (semantic tag + TF source + action + class). Deliverable #1.
2. **Resolve the 12 actionless + the 5 insufficient-data + the 1 live-firing** alarm.
3. **Add a did-not-run / staleness alarm class** to close the failure-vs-liveness gap.
4. **Reorganize by product + standardize naming**, mirroring OPAL_SCHEDULE.

---

## C. What binds the two (and to MDPF_MONOCLEANUP)

These three are the same shape at three altitudes: **a resource type used out-of-pattern across
multiple homes, with no single semantic census, producing bad recall when scanned.** MDPF_MONOCLEANUP
fixes one product's pipeline; OPAL_SCHEDULE and OPAL_ALERTS fix the estate-wide trigger and alarm
surfaces the same way — **census with semantic + TF tags, cleanup of the dead/void, standardize the
service and naming.** All three should share the "one capacity, one home, one census" principle so a
future agent scanning cloud assets gets a complete denominator every time.

**CVO posture:** this brief is assessment + scope input; the projects are CTO's to create/scope and
the standard rulings are the ~Z/OPAL_STNDRD lane's. I will hold each project's census-completeness
and cleanup claims to a verification bar (the census enumerates BOTH services / all alarms; a
"deleted" trigger is gone live; an actionless alarm is wired-or-removed, exercised not asserted).

---

## Appendix — reproduction [read-only]

```
# Triggers (both services, reconciled to census)
python: boto3 events.list_rules (paginate) -> 141 ; scheduler.list_schedules -> 10  (=151 live)
        vs trigger-map.json 149 (07-18): +2 [cot-rebalancer-runner-daily, opal-assets-silver-smartx-sweep-daily], 0 phantom
        group by trigger-map.json .triggers[].tf_file / .unit
# Disabled denominator
        18 rules + 1 schedule State!=ENABLED (named in A.2)
# Alarms
aws cloudwatch describe-alarms (paginate) -> 51 ; states 45 OK / 5 INSUFFICIENT_DATA / 1 ALARM
        12 with empty AlarmActions (named in B.2) ; firing: cmtque-worker-down
```

— 3.0.0_SA_CVO
