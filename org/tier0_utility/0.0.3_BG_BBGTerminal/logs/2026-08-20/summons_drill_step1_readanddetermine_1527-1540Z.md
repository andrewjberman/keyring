# 0.0.3_BG_BBGTerminal -- SUMMONS DRILL, Step-1 read-and-determine -- 2026-08-20 1527-1540Z
**archetype:** VALIDATE

Entered at **Step 1** per the summons (`20260820T152701Z_freshness_checker_stale.md`, kind STALE,
`[TEST-EXERCISE]`). **Step 2 NOT entered** -- Step 1 found no failure to recover from.

## VERDICT: the 07:00 scheduled run SUCCEEDED end-to-end. NO STALENESS. NO RECOVERY ACT.
## The `behind=99` in the summons is a DECLARED INJECTION, not a measurement -- and I re-derived
## the real number independently (=1, healthy T-1) rather than repeating the instrument.

`summons emitted 11:27 ET / entered Step 1 11:34 ET / lag 7 min` (Step-2b record-line shape, borrowed;
this was a cron+30 summons, not the 07:15 backstop fire -- no threshold, no escalation on the number).

## Step 1 -- per leg, never collapsed

| Leg | Read | Result |
|---|---|---|
| **a. Scheduled task** | `Get-ScheduledTaskInfo OPAL_BBGTML_daily_pull` | `LastRunTime 2026-08-20 07:00:01`, **`LastTaskResult 0`** = end-to-end OK. `NextRunTime 08/21 07:00`. (`NumberOfMissedRuns 0` noted and NOT used as health -- it is not the instrument.) |
| **b. FALLBACK / DAPI** | processes + listener + `bloomberg_health` | **`wintrv` pid 15016 RUNNING** (started 07:00:25). Listener on `127.0.0.1:8194` = 1, owned by `bbcomm` pid 30400. `bloomberg_health -> ok:true, //blp/refdata`. **DENOMINATOR: 54 processes under `C:\blp\`** (name-matched control 19) -- the query returned plenty of other blp processes, so an absence would have meant something. |
| **c. WDAC/kernel** | -- | **UNEXERCISED** -- that leg runs only if DAPI had to be restored. It did not. Not a pass, not a fail. |
| **d. Publish / SERVED, BY CONTENT** | `tools/portal_lookup.py get pipeline-status manifest.json` (my own read, not the producer's log line) | `data_pkl` / `model_pkl` **`data_as_of 2026-08-19`**, `updated_at 2026-08-20T11:06:58Z`; manifest `generated_at 2026-08-20T11:10:38Z`; object 1551 B, **read COMPLETE**. |

**Trading calendar resolved FIRST, from `lib/trading_calendar.py`, not from the message:**
`expected_last_trading_day(2026-08-20 Thu) = 2026-08-20`; served `2026-08-19` -> **`trading_days_behind = 1`**.
**Discriminating control:** the same call on `2026-08-10` returns **8** -- so the instrument is not returning a
constant. This pipeline is **T-1 by fixed rule**, so `behind=1` IS the healthy steady state (NEVER#1).

**The injection is source-grounded, not inferred:** `integrations/bloomberg/pipeline/freshness_check.py:204-207`
sets `behind = 99` only under the declared test path and logs the real computed values beside it; the
`[TEST-EXERCISE] ` banner comes from `:107`. The summons body carried the real numbers itself, and mine agree.

## The missing `PRECONDITION:` line is EXPLAINED, not an anomaly
The standing order says a healthy log must now carry `PRECONDITION: PASS -- DAPI UP` and that its ABSENCE is
the anomaly. **Today's 07:00 log has `DAPI FALLBACK EXIT: 0` and NO `PRECONDITION:` line.** Cause, measured:
`git log -S "PRECONDITION: PASS -- DAPI UP" -- .../scheduled_daily_pull.cmd` -> **`7284baa5c7`, 2026-08-20
08:36:33 ET** -- the echoes landed **96 minutes AFTER the 07:00:01 fire**. The Task runs the working tree, so
the file now on disk is evidence of what runs **NEXT**, never of what ran. **First fire that must carry the
line is 2026-08-21 07:00** -- if it is absent THEN, it is a finding.

## >> FINDING (drill-value, would have bitten a real Step 2 TODAY): the fire-once window is NOT clear
Read-only precheck of `%USERPROFILE%\.bbg_signin_attempts.json` -- 3 rows total, and
**`2026-08-20T11:00:41Z` is 4.55 h old: 1 attempt INSIDE the 6 h window.**
Had Step 1 found a real failure, **Step 2a would have REFUSED the fill and escalated** -- mine would have been
attempt #2 in the window, exactly what `bbg_fallback.ps1:71` refuses. Discriminated on **timestamp + 6 h count**,
never on the `outcome` label (every row still reads `SUBMITTED-SUPERVISED-MSTRZ`, including today's unattended one).
The standing order predicted this as "real, just not live tomorrow" -- **today it was live.**

## >> OPEN CALL ROUTED, NOT DECIDED: the 07:15 backstop cron is NOT armed
Two records point opposite ways and I do not adjudicate scope:
- `deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md` (Andrew-direct @`eede873a2f`): **re-arm every session.**
- My launch prompt this session: *"ZERO crons at launch, every serial ... Any live scoped loop authorization is
  recorded in org/XXX.md Step 1b-F -- that row is the only source of truth."* **XXX.md 1b-F has NO BG row**
  (rows exist for MSTR / CTO / COO / CVO / CVO~Z / tier-2-3 only).

**I armed nothing** (`CronList` -> none) and I am surfacing it LOUDLY rather than dropping it silently -- the
harm the standing order names is the *silent* drop. Materially: 07:15 ET has already passed today and the cron
is session-only, so the decision binds on **tomorrow**, not on any missed check today. **Ask: Andrew's word, or
a BG row in XXX.md 1b-F.** (CTO~Z R2's (a)/(b) fork on seat-down survivability is the same question one layer up.)

### >> OPEN CALL CLOSED 1540Z -- BY THE CUTOVER, NOT BY AN ANSWER
`0.0.0_AB_MSTR~Z` `20260820T154029Z` relayed **THE WORD**: the drill PASSED end-to-end (dead seat confirmed with
controls; spawn fired 15:27:04Z, my registration 15:28:07Z = **63 s**; Step-1 entry per the payload's own routing;
correct healthy verdict; recovery hold never fired). Andrew's ~1329Z word -- *"no 07:15 time poll... event-based off
that gate"* -- **retires the cron**, so the re-arm clause is superseded by the event contract: **no cron to arm, no
XXX.md 1b-F row needed, and my zero-crons launch state is the CORRECT end state, not a gap.**

**Executed same turn:** `STANDING_ORDER_0715_DAILY_BACKSTOP.md` rewritten **event-shaped** -- trigger contract
(Kind ∈ {STALE, CHECK-ERROR, SCHEDULE-GAP}, unknown ⇒ ENGAGE; silence only on an affirmative PASS); ran-at-all
closed at two layers with layer 2 named as MINE (records read on BOTH tasks whenever I am up, no clock); **Step 2a
UNCHANGED** and now carrying today's live 4.55 h measurement instead of the old prediction; **Step 2c UNCHANGED**;
**Step 2b RETIRED with the clock** -- it measured armed-wake-vs-firing and has no denominator without an armed
clock, and **nothing replaces it** (an invented event-latency metric would be the instrument the moratorium
forbids). The retired re-arm section keeps its provenance in-file, because a successor half-remembering this file
must land on the retirement, not the re-arm. **Filename retained deliberately** -- `RELAUNCH sec0b` resolves it by
path; renaming is MSTR~Z's act in the same commit as the sec0b re-point, or not at all.

**Catalog home move VERIFIED on disk, not relayed:** my `refs/DATA_CATALOG.yaml` is **gone**;
`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` **exists, 126,724 B, 11:16 ET**; negative control in the
same directory absent, so the check discriminates. My loaded prompt predates the move (CTO~Z `@88a00a3f81`) --
reading the new home for any catalog question this session.

## Startup (this session)
| Step | State | Evidence |
|---|---|---|
| `register_agent` | LIVE | pid 5636, broker port 7800; serial read **NOT REGISTERED** beforehand => genuine fresh session |
| `/watcher` | ARMED | task `bs8uoz30e`; **no pre-existing `inbox-watch.sh` under my serial** (`ps` showed 5 others -- COO~Z, AE~Z, CTO~Z, DE~Z, MSTR~Z -- all left alone), so no orphan, no kill. First event delivered the summons |
| 2a identity gate | **PASS** | `whoami` on `opal-gateway-bbg` = **Opal Bloomberg / opalbloomberg@opalinvest.com** |
| Teams Monitor | ARMED + PINNED | task `biv9ah27j`; **both banner lines confirmed, not assumed**: `pin(server=opal-gateway-bbg, identity=opalbloomberg)` and `token selected: identity=opalbloomberg@opalinvest.com` |
| `bloomberg_health` | ok:true | `127.0.0.1:8194`, `//blp/refdata` |
| Teams backlog | 0 | `poll_addressed_teams_messages` since `2026-08-19T18:30:00Z` -> count 0 |
| TOs | 0 | `to-check.py --all --assignee 0.0.3_BG_BBGTerminal` -> total=0 (`--all` carried) |
| Crons | 0 | `CronList` -> none (see the open call above) |

## Compiler Tools
| Tool | Result | Read |
|---|---|---|
| `comp-which "is the served model portfolio exposure dashboard data fresh for the expected trading day"` | 3-way TIE, all off-domain | `comp-freshness chain <bd/inf/cot>` is scoped to the pipeline trees, `comp-parity` to the BD-served surface, `comp-xray frozen` to value-motion on AUA fields. **None covers "is the opal-data-portal-v2 Bloomberg-dashboard served vintage at the trading frontier."** |
| `tools/portal_lookup.py channels` + `get pipeline-status manifest.json` | 13 channels; object read **COMPLETE** | The seat's own sanctioned rail for this bucket -- used instead of raw `aws`, which would also have mishandled the gzip channel class. |
| `lib/trading_calendar.py` | frontier `2026-08-20`, behind `1` (control `8`) | The ONE frontier definition (NEVER#1). |

**Coverage note (mild, not a defect claim):** the freshness question for THIS surface is answered by the seat's
own `portal_lookup.py` + `integrations/bloomberg/pipeline/freshness_check.py`, not by a comp-tool. Recording it
because a `comp-which` tie with three off-domain hits is what a coverage gap looks like from the inside.

## What I did NOT do
No Step 2. No sign-in, no fill, no re-pull, no publish, no upload. No git, no cloud mutation. No alarm/monitor/
checker built (moratorium). No cron armed. Read-only throughout, except this log.
