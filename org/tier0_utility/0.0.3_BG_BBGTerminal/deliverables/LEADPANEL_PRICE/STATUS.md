# LEADPANEL_PRICE -- `0.0.3_BG_BBGTerminal` -- CURRENT STATE

**This file is overwritten in place. It is a current-state file, not a journal; git history is the journal.**
Mandate: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/BG_BBGTERMINAL_PRICE_PRODUCER.md`.
Authority: Andrew-direct R-21 @`b390c36444` call 3 (this seat owns the terminal-box schedules) + R-15
@`884475c5a1` ("(i) the price pull" by name). Last written 2026-09-24 ~10:15Z.

## THE ONE-LINE ANSWER THE MANDATE ASKED FOR

⭐ **THE PRODUCER ALREADY WORKED. ONLY THE TRIGGER WAS ABSENT.** No producer code was written. The mandate's
own closing line made this the first question and the build ladder's second rung -- *the estate already has
it* -- is the whole finding.

## ACCEPTANCE

| ID | State | Evidence |
|---|---|---|
| **B1** producer runs deterministically | **MET** | `integrations/bloomberg/research/price_axis_pull.py`, a scripted re-runnable producer invoked by a Windows Scheduled Task. No number below came from an agent-typed Bloomberg lookup. |
| **B2** current-day generation exists and is SERVED | **MET for the STORE; the READER half is UNVERIFIED** -- see Limits | Pointers read back live (below). |
| **B3** the schedule is the production trigger | **APPLIED, NOT YET EXERCISED** | The leg is on disk; the 07:00 ET fire has not yet run with it. |
| **B4** the 09-29 fallback expiry no longer load-bearing | **MET for the store** once B3 exercises | A generation now exists at the frontier, inside the 14-day window. |

## WHAT IS MEASURED

**Frontier.** `lib.trading_calendar.prev_trading_day(2026-09-24)` = **2026-09-23**. Resolved before calling
anything stale, per the NEVER rule.

**Before the write** (this is the guard, not a formality): `TRENDING_PRICE#2026-09-23/_CURRENT` and
`BREAKOUT_PRICE#2026-09-23/_CURRENT` both **ABSENT**, with a **positive control on the identical command
shape** -- `TRENDING_PRICE#2026-09-15/_CURRENT` **PRESENT** -- so ABSENT could not be an instrument failure.

**The QA fire** (ad-hoc, permitted for QA; the SCHEDULED fire remains the acceptance), 2026-09-24T09:52Z,
run `R20260924T095217Z`:

```
as-of 2026-09-23   window 2026-08-24 .. 2026-09-23 (30 days)
universe            34 covered names with a MEASURED Bloomberg ticker
usable PX_LAST      32 of 34   (2 insufficient: 'Enel IM', 'ROG SW')
identity resolved   31 of 32   (source=pool:universe/v1/2026-09-16.json)
TRENDING_PRICE      32 rows COMPLETE   gen 20260924T095217Z-7bfec22eec6f
BREAKOUT_PRICE      32 rows COMPLETE   gen 20260924T095218Z-4c1424d093c3
written             64 of 64 rows; pointers 2 of 2; failed axes []
```

**After the write, read back from the STORE (never the producer's self-report):** both 09-23 pointers
`state=COMPLETE`, `row_count=32`, `written_at=2026-09-24T09:52Z`.

**NEVER-1, and it is MEASURED rather than argued.** Writer census of the PRICE pointer keyspace: **N=2**
(`price_axis_pull.py`, `lib/research/price/backfill_legacy_generation.py`) -- both scripted, neither
scheduled; the other `default_write_generation` callers write CHATTER. The writer's own contract is
two-phase (immutable generation partition, then ONE pointer put) and *"prior generations are never
deleted here"*. After the fire, `TRENDING_PRICE#2026-09-15/_CURRENT` re-read **byte-identical** -- same
`generation_id` `20260917T222503Z-c35c454d1e4f`, same `written_at` `2026-09-17T22:25Z`. **DELTA=0 on the
prior served key is measured, so no never-widen hold is required.**

## THE TRIGGER -- a fourth ISOLATED leg, not a new schedule

R-21 constrains mechanism: *"deterministic/scripted in nature **like the existing pull**"*. So this **is**
the existing pull. A second Scheduled Task would be a second path to the same loopback DAPI; a fourth leg
is the shape `etf_daily_pull` and `etf_constituents_pull` already established in
`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`.

`RC_PRICE` never touches `%RC%`, `%RC_ETF%` or `%RC_CONS%`. Codes **80-83** are disjoint from models
(0/1/9/20/30/40/50), ETF (60-63) and constituents (70-73):
`0` committed - `80` producer script absent - `81` an axis FAILED (marker written, prior pointer untouched)
- `82` producer crashed / Bloomberg unreachable - `83` interpreter absent.

**Exercised, 6 of 6 arms**, in an isolated harness with a stub producer (no Bloomberg, no S3, no DynamoDB):
`rc0->0`, `rc3->81`, `rc1->82`, `rc62->82`, script-missing->`80`, interpreter-missing->`83`; the
models-chain `%RC%` sentinel survived all six.

## DEPENDENCIES, WITH OWNERS

| What | Owner | State |
|---|---|---|
| **Commit of the three record paths** (`scheduled_daily_pull.cmd`, the `.open_deploys` json, the `change_management` md) | `0.0.0_AB_MSTR` / `~Z` -- this seat's **named integrator** | **ASKED.** `safe-commit` refused: `agent=0.0.3_BG_BBGTerminal not in permitted_agents` for lane `ANY_EXEC_OR_AE`. That refusal is CORRECT and by design -- this seat's README says no OWNPATHS lane exists for it and none should be added. Not escalated to `GIT_COMMIT_AUTHOR_OVERRIDE`: the named integrator is live and is the designed route. |
| **DAPI up at 07:00 ET** | this seat (sign-in runbook) | Up now (`bloomberg_health ok:true`). **This is a real gate on B3:** on 2026-09-23 the precondition FAILED (rc 50, DAPI down, pull not attempted) and every landing leg was correctly skipped. 09-19..09-22 all ran end-to-end. |
| **The Lead Panel READER actually serving 09-23** | AMGT reader owners (`lib/research/api/scoped_amgt.py`) | **UNVERIFIED by this seat** -- see Limits. |

## LIMITS -- what this file does NOT claim

⛔ **B2's reader half is UNVERIFIED.** This seat measured the **STORE** (the `_CURRENT` pointers), not the
**SCREEN**. The mandate's deliverable is *"a person opening the Lead Panel sees ... a price generation dated
the current trading day"*, and a served pointer is a necessary, not sufficient, condition for that. No
Lead Panel render was read. Stating the store result as though it were the panel result would be exactly the
grain error the evidence law names.

⛔ **B3 is APPLIED, NOT EXERCISED.** The leg is on disk and the arms are proven in a harness; the scheduled
fire at 07:00 ET has not yet run it. Ledger legs **L3** and **L4** are open against precisely that, and L4
requires a `run_id` **distinct from** the QA fire's `R20260924T095217Z` so a scheduled result can never be
read off the ad-hoc one.

⛔ **The record is on disk but NOT in git.** Site-Z scheduled tasks run the **working tree**, so the edit is
already the deployed state; a `git checkout`/reset of this tree would silently revert the deploy while the
ledger still read OPEN. That is the live exposure in the dependency row above.

## SURPRISED, NOT FIXED

**`AMGT_RESAPP-Z-S248`** (EXPOSURE, ARMED) -- `%PY_AWS%` is assigned inside the SEND leg at `:166`, but the
pull-failed/DAPI-up branch at `:145` does `goto :etf_leg` from **above** it, so on that one path the ETF and
constituents legs invoke an **empty interpreter**. That branch *is* the 2026-09-04 leg-isolation fix's own
protected path. **EXPOSURE, not INCIDENT, and the discriminator was run rather than assumed:** the defect's
signature returns **0 across the 30 retained run logs (2026-08-25..2026-09-23)**; `RESULT: PULL FAILED`
appears exactly once (2026-09-04) and that run shows no `ETF LEG` line, i.e. it predates the fix.
⚠ That denominator is **bounded by the .cmd's own 30-log prune** and says nothing about earlier runs.
Not fixed here -- another owner's leg, outside this mandate's write surface. **The price leg cannot inherit
it:** it resolves `PRICE_PY` itself and refuses with `rc=83`.

## NEXT PROOF

The 07:00 ET fire. Close **L3** on the run log's `PRICE LEG EXIT CODE` line plus
`Get-ScheduledTaskInfo` `LastRunTime`/`LastTaskResult`; close **L4** on a `_CURRENT` pointer whose
`run_id` is distinct from `R20260924T095217Z`.
