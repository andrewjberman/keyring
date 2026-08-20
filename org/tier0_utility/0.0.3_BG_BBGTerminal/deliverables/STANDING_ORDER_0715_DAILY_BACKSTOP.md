# STANDING ORDER — 07:15 ET DAILY BACKSTOP (0.0.3_BG_BBGTerminal)

**Status:** LIVE. **Authority:** Andrew-direct, record `@eede873a2f`, relayed by `0.0.0_AB_MSTR~Z`
`20260820T023754Z`. **Armed:** cron `8b5d18cb`, `15 7 * * *` local (= 07:15 ET), 2026-08-20.

> **VERBATIM (Andrew):** *"0.0.3_BG should have an ongoing schedule to check 15 min after the cron
> and if it didnt work then it manually logs in and pulls or does whatever is necessary."*

> **VERBATIM (Andrew, on the same finding — why nobody signs in ahead of a failure):** *"the whole
> point is that the device needs to be able to figure this out and get it done on its own accord."*

## ⚠ THIS FILE IS A CARRIER. THE CRON IS SESSION-ONLY.
It is in-memory, dies with the session, and auto-expires after 7 days. **A successor that reads
"Tier-0 UA arms ZERO crons" and does not re-arm SILENTLY DROPS A STANDING SOVEREIGN INSTRUCTION.**
The zero-crons law yields here because Andrew operator-initiated this one by name.
**RE-ARM EVERY SESSION while this ruling stands.** Carriers: `@eede873a2f`, this file, my lane logs.

> **PLACEMENT NOTE — read this before assuming it is misfiled.** Andrew said *"bank it in your refs
> so successors inherit."* `refs/` is **deliberately unwritable from my own seat** (G1 mechanical
> fence — the point is that no message can become a prompt/refs edit, even one that convinces me).
> So this landed in `deliverables/`, which I can write, and the refs/ placement is routed to
> `0.0.0_AB_MSTR~Z` as named integrator. **The fence working is why this file is here; it is not a
> deviation from his instruction, it is the instruction executed through the surface I actually hold.**

## What fires at 07:15 ET

### Step 1 — READ THE 07:00 OUTCOME PER LEG. Never collapse the legs into one verdict.
| Leg | Read | Trap |
|---|---|---|
| Scheduled task | `Get-ScheduledTaskInfo OPAL_BBGTML_daily_pull` -> `LastRunTime` + **`LastTaskResult`** | **`NumberOfMissedRuns` is NOT a health instrument** — it counts runs that never STARTED and reads `0` on a run that started and returned rc=1 (measured 2026-08-19). `LastResult` is the instrument. |
| **FALLBACK (FIRST)** | Did the chain's own self-heal restore the Terminal? `wintrv.exe` running · listener on 8194 · `bloomberg_health` | **Enumerate ALL processes under `C:\blp\` and PRINT THE DENOMINATOR** — an absence only means something if the query returned other blp processes. **A running `bbcomm` is NOT a running Terminal.** A fallback FAILURE is the self-heal exercise's **honest finding, never a confound.** |
| WDAC/kernel | Only **if** DAPI was restored | Otherwise it is **UNEXERCISED — say so.** Do not infer pass or fail from a leg that never ran. |
| Publish/served | Served artifact **BY CONTENT** (`data_as_of` + `generated_at`) | Not the producer's rc, not the object's LastModified alone. |

### Step 2 — IF THE SCHEDULED RUN FAILED: standing authorization, **this recovery context only**
- **Runbook:** `deliverables/BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md`.
- **FIRE-ONCE DISCIPLINE, NON-NEGOTIABLE — ONE fill attempt.** Verify field contents **by screenshot
  BEFORE submitting**. A fill failure **ESCALATES LOUD** (Andrew + MSTR~Z) and **STOPS**. Never a
  blind retry: Bloomberg locks on repeated failures, and a lockout escalates an outage into a
  support call.
- **Never TAB from Login Name to Password** — on this dialog TAB lands in the language selector and
  the password goes into the **unmasked** Login Name field (measured 08-11, cost one failed attempt).
  Direct clicks only. `wintrv`'s own `MainWindowHandle` is **0**; find the `BLOOMBERG: Login` window
  by `EnumWindows` title match.
- **Credential:** Secrets Manager `opal/mcp/opalbloomberg-login`. **The NAME is citable, the VALUE
  never** enters chat, a log, Teams, a commit, or any artifact.
- **Re-pull:** production runner `workflows/bloomberg/tplus1/tools/run_daily_pull.py` under the `cma`
  env — **not** the OneDrive `.bat` an operator would reach for. **NEVER send/publish on a tripwire FAIL.**
- **Resolve the trading calendar BEFORE calling anything stale.** T-1 is the healthy state (NEVER#1).
- **If the Terminal was signed in fresh, run the `.ST` CIX content check** — CIX resolution is
  **login-scoped**, so a pull right after a sign-in is exactly the case that can succeed and still
  carry wrong custom-index data (08-03 incident). Row count must advance by **exactly** the trading
  days elapsed; inception 2023-12-29 @ 100.0; run a **positive control** (SPX) and a **negative
  control** (bogus ticker) so a zero would have meant something.
- **Verify the SERVED object by content** afterward.

### Step 2b — LAG RECORD LINE (CTO~Z R1, ruling @008135604e, 2026-08-20)
**Every backstop log carries one line, verbatim shape:**
`armed 07:15 ET / fired HH:MM / lag N min`
**It is a RECORD LINE, NOT A MONITOR** — no alarm, no threshold, no escalation on it. It exists so the
lag has a denominator instead of an anecdote. **Redesign is considered at n>=5 observations**, not on
any single bad day. Ruling: `ctoZ_RULING_BG_0715_BACKSTOP_TIMING_OSTASK_VS_SESSION_CRON_20260820.md`.

> **WHY THE SESSION CRON STANDS, and the softness that actually matters (CTO~Z R2 — read this, it is
> not the jitter).** The `CronCreate` jitter/idle-REPL lag is the VISIBLE softness and the smaller one.
> **The load-bearing one: this cron exists only on days an operator relaunched the seat before 07:15.
> On a seat-down day there is no cron, no check, and NO SIGNAL THAT THERE WAS NONE** — the absence of
> a check produces no artifact, so nothing reports it. A lag you can measure is strictly safer than a
> check that silently did not exist.
> **Whether the check must survive seat-down is AT ANDREW** — (a) session-cron stands, or (b) an OS
> Scheduled Task performs **Step 1 (the read) ONLY**. **Step 2 recovery stays an AGENT act either way**
> — do not let (b) be read as automating the sign-in. **Default if silent = (a).**

### Step 3 — REPORT per-leg + exactly what was done, to Andrew and MSTR~Z. Session log. Every figure
carries its vintage.

## Scope fence — what this authorization is NOT
It authorizes **sign-in + re-pull in the specific context of a failed scheduled run.** It is not a
general Terminal-login authorization, not a publish authorization outside the runbook's gates, and
not a warrant to build an alarm, monitor or freshness checker for the dead-Terminal gap (standing
moratorium — that remains a route/schedule question for CTO/Andrew).
