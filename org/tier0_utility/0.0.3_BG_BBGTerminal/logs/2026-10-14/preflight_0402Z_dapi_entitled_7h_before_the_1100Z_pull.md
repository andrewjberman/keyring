# Pre-flight 04:02Z: DAPI is entitled ~7h before today's 11:00Z pull -- the precondition that killed yesterday's run currently passes

**archetype:** VALIDATE

A measurement taken deliberately early, not a status report. **Yesterday (2026-10-13) the 11:00Z
scheduled pull died at its DAPI precondition** -- sign-in fallback `rc=4`, *"submit aborted pre-click
(login window gone or focus lost)"*, pull NOT attempted -- and only the 11:30Z freshness backstop
caught it, with a summoned recovery landing at 14:32Z. The same failure recurring today is a live
possibility, so the cheap thing is to measure the precondition now rather than learn about it from
the backstop.

## Measured 2026-10-14T04:02Z (local 00:02 EDT)

| check | instrument | result |
|---|---|---|
| DAPI reachable | `bloomberg_health` (MCP) | `ok: true`, `127.0.0.1:8194`, `//blp/refdata` |
| session starts | `C:\Anaconda\envs\cma\python.exe` -> `blpapi.Session.start()` | **True** |
| service opens | `openService('//blp/refdata')` | **True** |
| **a real request is answered** | `ReferenceDataRequest` SPX Index / PX_LAST | **`ReferenceDataResponse` with `securityData`** |

The fourth row is the one that matters and is why I did not stop at the first. `bloomberg_health`
answers "is the port listening"; `start()`/`openService()` answer "can this interpreter attach". **Only
a served request proves the session is ENTITLED**, which is exactly what yesterday's precondition was
testing when it failed -- the scheduled wrapper's own check is *"an entitled session answered a real
refdata request."* The pull runs under the `cma` interpreter, not the MCP server's Python, so the MCP
green light alone would not have been evidence.

## What this does and does not predict

**Does:** the Terminal is logged in and entitled at 04:02Z. Yesterday's thread record measured a
session staying entitled **~19 hours** after a 11:3xZ sign-in and carrying the whole chain, so a
~7-hour hold to 11:00Z is well inside observed behaviour.

**Does NOT:** entitlement can still lapse, and the Terminal can still be logged out by a person, an
update or a reboot between now and 11:00Z. **This is not a prediction that the run will pass.** Its
value is diagnostic: **if the 11:00Z run fails anyway, the cause lies between 04:02Z and 11:00Z** and
is not "the session was already dead overnight" -- which is one of the two shapes yesterday's failure
could have had, and the one this read eliminates in advance.

## Not acted on, deliberately

No pull fired, no sign-in attempted, nothing pre-warmed. The 07:00 ET cron remains the PRIMARY path
(`prompt.md`: the gateway overlay allow row is *"FALLBACK CAPABILITY ONLY, never the routine path"*),
and firing a pull at 04:0xZ would be an ad-hoc run standing in for a scheduled one -- barred, and it
would also consume the entitled session this read just confirmed. **The guardrail act for 2026-10-14
is still owed after 11:00Z:** read the run's exit codes and `freshness_check` by content, exactly as
yesterday.

Carried forward from 2026-10-13 and unchanged: served data healthy at T-1 (`data_as_of=2026-10-12`,
`trading_days_behind=1`, 10 series graded, re-read 19:14:10Z).
