# CTO~Z RULING — BG 07:15 daily backstop: OS Scheduled Task vs session cron (route/schedule design)

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~1225Z · **Class:** design ruling in the CTO~Z lane (MSTR~Z routed 2091: *"Rule if/when you and he settle it"*). Interim pending ONE word from Andrew (R4). **Builds nothing. Gates nothing. Proposes no alarm/monitor.**

## Inputs (all read at this desk)
- BG Msg-ID 2089 (1148Z) — first fire of the 07:15 standing order: all four legs GREEN, no Step-2 recovery invoked; **the cron fired ~07:45, not 07:15** (~30 min lag); cause stated by BG as CronCreate REPL-idle gating + jitter — INFERRED, unmeasured.
- MSTR~Z routing 2091 (1150Z); COO~Z 2100 item 5 (D7's TAC-3 law: *"a schedule, never an alert"*).
- `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md` @8a92531dd2 (Andrew verbatim: *"0.0.3_BG should have an ongoing schedule to check 15 min after the cron and if it didnt work then it manually logs in and pulls or does whatever is necessary"* · *"the whole point is that the device needs to be able to figure this out and get it done on its own accord"*).
- `refs/RELAUNCH.md` §0b (cron re-arm pointer) + *Steady state*: **the seat is RULED OPERATOR-STARTED** (Andrew-direct 2026-08-10 ~1653Z @bc7eb60de: no cron, no auto-start; a dead session stays down until an operator relaunches it).
- BG `README.md:55`: the box already runs TWO OS-level Scheduled Tasks (`OPAL_BBGTML_daily_pull` 07:00 ET, `OPAL_vendor_watch` hourly) — schedule-class precedent on this exact box.
- Live primitive at 12:20Z: `get_live_agents` = 5 seats; **0.0.3_BG_BBGTerminal NOT REGISTERED** (COO~Z census counts it "by process" only).

## The measurement, framed before it is reasoned from
1. **n = 1.** One fire, one lag figure. The lag's cause is inferred. Rate and distribution are unmeasured. (The /watcher doc's own lesson: *measure the rate before sizing the remedy.*)
2. **Today's fire was CONDITIONAL.** It happened because MSTR~Z relaunched the seat at 0210Z. On a day nobody relaunches BG before 07:15 ET there is no cron, no check, no recovery — and no signal that there was none. The seat is not registered now.
3. **Cost today: zero.** Recovery, had it been needed, would have begun ~08:00-08:15 ET — still before 09:30 ET open, but outside the figure Andrew designed around.

## Ruling
- **R1 — The session cron STANDS as today's carrier of the standing order.** No redesign off n=1. BG adds ONE line to each backstop log — `armed 07:15 ET / fired HH:MM / lag N min` — a record line, not a monitor. Any lag-driven redesign is considered at n >= 5.
- **R2 — The load-bearing soft-ness is not the 30-min jitter; it is the seat's existence.** A session-cron backstop exists only on days an operator relaunched BG before 07:15 ET. That is precisely the half of *"on its own accord"* a session cron structurally cannot deliver, and it is the question worth Andrew's word — not the 15 minutes.
- **R3 — The only mechanism that survives seat-down is schedule-class** (TAC-3 law; the 07:00 leg and `OPAL_vendor_watch` are the precedent on this box): an OS Scheduled Task at 07:15 ET running **Step 1 ONLY** — the four deterministic leg reads (`LastTaskResult` · blp process census WITH denominator · 8194 listener · served object BY CONTENT with the trading calendar resolved first) — writing the per-leg verdict as a file in the BG seat's `logs/` dir plus ONE fabric inbox message (BG's inbox; MSTR~Z's when BG is not registered). **Step 2 (sign-in, fire-once, screenshot-verify, re-pull, `.ST` CIX check) STAYS AN AGENT ACT** — BG if live, else the verdict reaches MSTR~Z who relaunches BG per RELAUNCH.md. Not an alarm, SNS, SES, or freshness monitor: the CHECK is Andrew-asked verbatim, and its output is a record + an inbox message — the fabric's normal report channel.
- **R4 — DECISION AT ANDREW (one word, via MSTR~Z's console):**
  - **(a) ACCEPT** the session cron + lag record; seat-down days are operator days (R1 becomes permanent).
  - **(b) OS-TASK the Step-1 check** per R3; Step 2 stays agent.
  - **My recommendation:** (b) IFF he wants the check to survive the seat being down, OR he confirms the 15 minutes is load-bearing; otherwise (a). **Ask him the seat-down question; it is the one that decides.** Default if silent: (a) stands.
- **R5 — Not ruled / not authorized here:** no build. On (b), COO~Z cuts the TO; builder = the seat's tooling owner (0.5.0_AE_OpalETL~Z authored RELAUNCH.md under OPAL_ANALYST TO2); dependencies to name at cut: AWS read credentials on the Bloomberg box for the served-object leg; a `bloomberg_health` equivalent outside the MCP (direct blpapi session, or the 8194 listener as the proxy leg). The `.ST` CIX content check stays in Step 2 (it needs the `cma` interpreter + judgment).

## Moratorium / gate self-check
No alarm, SNS, SES, freshness checker or monitor is proposed; the scheduled CHECK is Andrew-asked (verbatim above). No gate, hold, or approval step is created on any seat. BG re-arms per §0b either way until Andrew's word lands.
