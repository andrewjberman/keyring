---
name: schedule-check
description: The SCHEDULED JOBS timetable, view-time compiled from the live AWS APIs: every timed job across both EventBridge planes (Rules, always UTC; Scheduler, explicit timezone) ordered by fire time in UTC and ET. `/schedule-check`; `--drift` (live ENABLED/DISABLED vs org/missions/SCHEDULE.yaml, exceptions only); `--plane rules|scheduler`; `--events`; `--json`. Each plane prints its own denominator; an unreadable plane renders UNREADABLE, never zero rows. Read-only; never alerts. Engine `.tools/schedule-check.py`.
---

# /schedule-check — the scheduled-jobs timetable

The human-reading lens on everything that fires on a timer. Andrew-commissioned 2026-08-28 as the
answer to *"we should never be writing ephemeral shit in XXX.md"* — a jobs view that cannot rot
because it is compiled at the moment you look at it.

## Invocation

| form | behavior |
|---|---|
| `/schedule-check` | The timetable: every timed job, both planes, ordered by real fire time. |
| `/schedule-check --drift` | Only jobs whose live state differs from declared intent. |
| `/schedule-check --plane rules` | One plane (`rules` or `scheduler`). |
| `/schedule-check --events` | Also include event-driven rules (no fire time — they show `-`). |
| `/schedule-check --json` | Machine-readable rows. |

Exit: `0` rendered · `1` hard error, nothing rendered · `2` rendered but ≥1 plane UNREADABLE.

## ⛔ There is no generated artifact, and that is the design

Every value is read live, every run. Do **not** add an emit step, a fingerprint, a `--check`, or a
regen owner. That machinery exists only to manage a cache, and the cache is the bug.

The live counter-example was in hand the day this was written: `infra/system/06_current_state.json`
read `STALE rc=2` for an entire day because its regen belonged to a device nobody was sitting at.
The emit-and-check pattern does not prevent staleness — **it converts staleness into a chore, and
the chore is what fails.**

## ⛔ What it costs, stated: the failure mode inverts

A stale file fails by confidently showing OLD data. This fails by **not answering** — a throttle,
expired creds, an API error. That is strictly better because it is loud, **but only if an unread
plane renders as UNREADABLE rather than as zero rows.** A partial table presented as complete is
the one way this tool can lie, so every plane always prints its own status and denominator.

**When you read the output: `-` in the ROWS column is not "nothing scheduled there." It is
"this plane was not read."** Never quote a total from a run that had an UNREADABLE plane without
saying so.

## ⛔ The timezone trap it exists to close

Measured at both APIs 2026-08-28:

```
EventBridge RULES      NO timezone field. Cron is ALWAYS UTC.
EventBridge SCHEDULER  carries an explicit ScheduleExpressionTimezone.
```

So `cron(15 9 * * ? *)` is **09:15 UTC** in one plane and **09:15 America/New_York** in the other —
4–5 hours apart, and the gap shifts with DST. Reading a merged timetable off raw expressions puts
jobs in the **wrong order**, and nothing in the Rules API hints that a timezone is missing.

Every row is therefore normalised to **both** UTC and ET. Anything that is not a single fixed daily
time (a `rate()`, an hour list like `14,21`, a `*/6` step) renders `-` beside its raw expression
rather than a guessed clock time — `-` means "fires more than once a day", not "unknown", and the
raw expression is always shown so nothing is hidden.

## `org/missions/SCHEDULE.yaml` — exceptions only

Holds **only what no API can answer**: why a job is deliberately off, who owns it, which directive
it serves. No cron, no state, no target — those are read live. *A queryable value written down is a
second carrier, and two carriers of one fact diverge from minute one.*

`expect` **defaults to ENABLED**, so the file records only departures. Measured at build time: 157
jobs, 18 not ENABLED — so ~18 rows rather than 157, and it shrinks as the estate is cleaned up
rather than growing as the estate grows.

⛔ **Do not bulk-annotate the drift list to make it go quiet.** `UNDECLARED` does not mean broken;
it means nobody has recorded whether this is deliberate — a true statement about our records. An
`expect: DISABLED` written without knowing why converts an honest open question into a false
answer, and nothing will ever re-open it.

## Adding a plane

Append one reader to `PLANES` in the engine. A reader takes no arguments and returns a
`PlaneResult(name, status, rows, error)`. The render, the join, and the denominators are generic —
nothing else changes. Candidate planes not yet built: GitHub Actions `schedule:` blocks, systemd
timers declared in repo setup scripts (**DESIRED only** — a stopped host cannot be queried, so
never label those APPLIED), Windows Scheduled Tasks per device.

## It is not a checker

Drift **never** changes the exit code. Nothing is written, nothing is sent, nothing is gated —
CLAUDE.md's monitor moratorium stands. This is a viewer. If a scheduled job needs an owner or a
remedy, that lands as a gate or an owned blocking item through the normal route, not from here.
