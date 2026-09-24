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
| **B2** current-day generation exists and is SERVED | **MET at the store AND at the source reader** -- but see The Reader: it resolves via `dated: true`, so the clause *"rather than the dated fallback"* is structurally unreachable | Pointers read back live; `read_rankings` exercised. |
| **B3** the schedule is the production trigger | **EXERCISED** | The 2026-09-24 07:00 ET fire ran the leg end to end: `PRICE LEG EXIT CODE: 0`, task `LastTaskResult 0`. See The Fire. |
| **B4** the 09-29 fallback expiry no longer load-bearing | **MET, and now held by a PROVEN trigger** -- the fallback is still the serving mechanism, but at a 1-day walk and re-fed daily by an exercised schedule | See The Reader and The Fire. It was correct not to close this on the QA fire; B3's exercise is what closes it. |

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

## THE FIRE -- B3's acceptance, 2026-09-24 07:00 ET

The scheduled task fired at **07:00:01**, ran to completion and returned to `Ready` with
`LastTaskResult 0` (it read `267009` = still-running at 07:03, so the 0 is a completed run, not a stale
value). Verified **before** the fire that the task's action points at the edited file --
`cmd.exe /c "...\integrationsloomberg\pipeline\scheduled_daily_pull.cmd"`, principal
`Opal Bloomberg` / Interactive -- so this is not a wrong-object read of another copy.

**The isolation held and the new leg perturbed nothing:**

```
:9    PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request
:59   PULL EXIT CODE: 0
:94   RESULT: PUBLISHED 2026-09-23 -- verified by content, not by self-report
:97   RESULT: END-TO-END OK
:124  ETF LEG EXIT CODE: 0
:143  CONSTITUENTS LEG EXIT CODE: 0
:145  PRICE LEG (AMGT Lead Panel price axis)
:154  PRICE LEG EXIT CODE: 0 -- generation committed
```

**L4's discriminator is satisfied, which is the whole point of having written it that way:** the served
pointers now carry `run_id` **`R20260924T110713Z`**, **distinct from the 09:52Z ad-hoc QA fire's
`R20260924T095217Z`**. A scheduled result therefore cannot be a re-read of the ad-hoc one. Both axes
`state=COMPLETE`, `row_count=32`, `written_at 2026-09-24T11:07Z`; denominators identical to the QA fire
(34 names, 32 usable, 31 identity-resolved, 64 of 64 rows, 2 of 2 pointers, failed axes `[]`).

**NEVER-1 re-checked across this SECOND write rather than assumed from the first:**
`TRENDING_PRICE#2026-09-15/_CURRENT` re-read **byte-identical for the third time** -- `generation_id
20260917T222503Z-c35c454d1e4f`, `run_id R20260917T222502Z`, `written_at 2026-09-17T22:25Z`. DELTA=0 holds
for the scheduled fire as well as the ad-hoc.

⚠ **THE GATE THIS CLEARED WAS REAL, NOT HYPOTHETICAL:** on 2026-09-23 the same 07:00 fire died at
`PRECONDITION: FAILED` (rc 50, DAPI down) with every landing leg correctly skipped. B3 could never have
been graded on the schedule merely existing.


## DEPENDENCIES, WITH OWNERS

| What | Owner | State |
|---|---|---|
| **Commit of the three record paths** | `0.0.0_AB_MSTR~Z` -- this seat's **named integrator** | **DONE** @`8d235eadb1`, on `origin/CLOUD` @`64df5daa18`. `safe-commit` refused this seat CORRECTLY (`not in permitted_agents`, lane `ANY_EXEC_OR_AE`) -- no OWNPATHS lane exists for it by README design. **`GIT_COMMIT_AUTHOR_OVERRIDE` was NOT used**; the designed route was available. |
| **Commit of THIS file's later revisions** | same | **OWED.** `deliverables/` is refused to this seat under lane `TIER0_UTILITY` (only `logs/` + `task_orders/` are self-owned), so every STATUS.md revision after `8d235eadb1` needs an integrator pass. |
| **DAPI up at 07:00 ET** | this seat (sign-in runbook) | Up now (`bloomberg_health ok:true`). **This is a real gate on B3:** on 2026-09-23 the precondition FAILED (rc 50, DAPI down, pull not attempted) and every landing leg was correctly skipped. 09-19..09-22 all ran end-to-end. |
| **The Lead Panel READER actually serving 09-23** | AMGT reader owners (`lib/research/api/scoped_amgt.py`) | **VERIFIED AT SOURCE** -- `read_rankings` resolves to this seat's generation. Deployed bytes and the rendered screen remain unverified (401). See The Reader and Limits. |

## THE READER -- EXERCISED, and it changes what B2 and B4 can honestly claim

`lib/research/api/scoped_amgt.py:read_rankings` was run in-process against the live store (read-only):

```
trending/price   as_of_date 2026-09-23   requested_as_of 2026-09-24   dated TRUE
                 SERVED   rows_read 32   generation_id 20260924T095217Z-7bfec22eec6f
breakout/price   as_of_date 2026-09-23   requested_as_of 2026-09-24   dated TRUE
                 SERVED   rows_read 32   generation_id 20260924T095218Z-4c1424d093c3
```

**The reader lands on THIS seat's generation, not the 2026-09-15 one.** That is the reader half of B2,
verified rather than assumed.

⛔ **BUT IT ARRIVES VIA THE DATED-FALLBACK BRANCH (`dated: true`), AND THAT IS STRUCTURAL, NOT A MISS.**
`read_rankings` sets `requested_as_of = as_of_date or _today()` -- it asks for **2026-09-24** -- while the
producer's as-of is `prev_trading_day` = **2026-09-23**. So the pointer at the requested date is ABSENT on
every ordinary day, `_find_latest_served_pointer` walks back, and the list is served with `dated: true`.

**So the mandate's B2 phrasing -- *"the Lead Panel reads it rather than the 14-day dated fallback"* -- is
NOT REACHABLE while the reader requests today and the producer writes T-1.** What this work actually
changed is the **fallback DISTANCE: 9 days (09-24 -> 09-15) down to 1 day (09-24 -> 09-23)**.

⚠ **THEREFORE B4 IS DEFUSED BY THE SCHEDULE, NOT BY A ONE-OFF.** The 14-day window is still the mechanism
carrying the panel; it is simply no longer near its edge. If the producer misses more than 14 consecutive
days the list returns ABSENT again -- which is precisely why **B3, the daily trigger, is the acceptance and
the ad-hoc fire is not.** Closing the 09-29 clock on the QA fire alone would have been a false close.

**Not this seat's to change:** either the reader requesting the trading frontier, or the producer also
writing a pointer at today's date, would remove the fallback from the path. Both sit in `lib/research/`,
which the mandate's write surface explicitly excludes (`2.0.0_SA_COO~Z`'s). Reported, not patched.

## LIMITS -- what this file does NOT claim

⛔ **THE READER EXERCISE IS THE REPO'S SOURCE, NOT THE DEPLOYED BYTES.** It imports
`lib/research/api/scoped_amgt.py` from this working tree. It does **not** establish that the deployed
Lambda behind the Lead Panel runs those bytes -- the code-instrument trap (diff deployed against the build
input, never assume by filename).

⛔ **AND THE SCREEN WAS NEVER READ.** A direct GET of
`https://d2n2nzpeqf34ge.cloudfront.net/api/scoped/amgt/lead-panel/rankings/{trending,breakout}/price`
returned **HTTP 401 `Missing or invalid Authorization header`** on both. The authenticated browser-session
endpoint is R-21 call 1's subject and belongs to another seat, so this seat cannot close the last hop. The
deliverable's wording is *"a person opening the Lead Panel sees ..."*; what is proven here is the store and
the source reader, and stating either as the panel would be the grain error the evidence law names.

⭐ **THE RECORD IS NOW IN GIT AND THAT EXPOSURE IS CLOSED.** It is kept here because it is a STANDING
PROPERTY OF THIS DEVICE, not an incident: site-Z scheduled tasks run the **working tree**, so an
uncommitted edit to a task's target is not *"not yet deployed"* -- it IS the deployment, and a
`checkout`/`reset` would have silently reverted a landed deploy while the ledger read OPEN. That window ran
from ~09:5xZ to the integrator commit at ~10:21Z. It generalises to every file a Scheduled Task on this box
executes.

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

**The mandate's own proofs are spent: B1-B4 met, ledger L1-L4 closed, entry CLOSED.** What remains is not
this seat's to close:

1. **The rendered panel** -- blocked on the authenticated browser-session endpoint (R-21 call 1), another
   seat's. A direct GET returns 401.
2. **The deployed reader's bytes** -- diff the Lambda against its build input; not measured here.
3. **`AMGT_RESAPP-Z-S248`** -- `disarm_owner` is `1.0.0_SA_CTO~Z`; the leg is another owner's write surface.
4. **The dated-fallback mismatch** (reader asks `_today()`, producer writes T-1) -- `lib/research/`, excluded
   from this mandate's write surface.

**The one standing duty this seat keeps:** the 07:00 ET fire is now the production trigger, and its
precondition is DAPI liveness -- which failed on 2026-09-23. A sign-out at 07:00 skips the leg by correct
design, so the recovery runbook remains this seat's.
