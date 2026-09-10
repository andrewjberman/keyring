# 0.0.3_BG_BBGTerminal — session log 2026-09-10T06:19–06:48Z

**archetype:** STARTUP + DAILY GUARDRAIL

**Serial:** `0.0.3_BG_BBGTerminal`, session `fd87eb7b-…`, PID 6104 — **fresh session after a reboot**,
not a resume. **Continuity:** `logs/2026-09-06/resume_and_teams_lapse_1657-1705Z.md`.
This entry closes that log's Teams-deafness question with a stronger instrument, resolves a pull-log
gap that log could not have seen, and **retracts one causal lead that log routed upward**.

---

## 1. STARTUP — every On-Launch step, with its evidence

| Step (prompt.md On launch) | Result |
|---|---|
| 1. `register_agent` | LIVE, PID 6104 (liveness.json holds the serial at MY pid — no identity conflict) |
| 2. `/watcher` | inbox Monitor `bh55lbr03`, `TaskOutput -> running`, banner `parent-tied: pid 2102` (armed, not orphan-capable) |
| **2a. IDENTITY ACCEPTANCE GATE** | **PASS** — `whoami` on `opal-gateway-bbg` = `Opal Bloomberg / opalbloomberg@opalinvest.com` |
| 3. Teams Monitor | `by8vel475`, stock engine + identity pin, `TaskOutput -> running` |
| 4. `bloomberg_health` | `ok: true`, `//blp/refdata` @ 127.0.0.1:8194 |
| 4. `cma` interpreter | `dapi_check.py` under `C:\Anaconda\envs\cma\python.exe`: `DAPI: UP … entitled session live` rc=0; blpapi 3.26.4.2 / py3.13.2 |
| 5. latest log read, **zero crons** | `CronList` -> no scheduled jobs |

Fabric mail: `check-inbox` empty, `get_agent_status` empty, `get_delivery_state` since 2026-09-06
**0 rows matched — which is not zero delivered**; `read/` agrees.

⚠ **`XXX.md` Step A.1 is mechanically REFUSED for this seat and that is by design.** Writing
`org/mcp/sessions/<session>.serial` is blocked by `bg-concierge-gate` (G2 on the shell redirect, G1 on
the Write tool) — the BG seat is read-only outside its own `logs/threads/deliverables` + tmp.
**Identity is sound anyway** by the higher-precedence source: `$OPAL_AGENT_SERIAL=0.0.3_BG_BBGTerminal`
(per-process) plus my own armed Monitor. **Surfaced, not chased** — the gate is pre-existing and
correct for this seat; only the generic startup text assumes every seat can write there.

**Box rebooted 02:17:18 ET today** — three restarts 02:06:30 / 02:15:00 / 02:16:29 (Advanced Monitoring
Agent, then TrustedInstaller x2: the RMM patch cycle). Nothing respawns across a restart; this session
is the respawn.

---

## 2. THE MISSING 2026-09-08 PULL LOG — RESOLVED, AND IT COST NOTHING

`~/opal_bbg_logs` census: **30 files**, and `bbg_tplus1_20260908_*` does not exist while
`20260907_070002` and `20260909_083629` do. A missing scheduled fire is exactly the shape this
seat's guardrail exists to catch, so I measured rather than assumed.

**System event log settles it:** `6008 — "The previous system shutdown at 4:19:28 PM on 9/7/2026 was
unexpected"`, and the next `6005` (Event log service started) is **9/9/2026 8:28:57 AM**.
**The box was powered off from 2026-09-07 16:19 to 2026-09-09 08:28.** So:

- 09-08 07:00 ET never fired because there was no machine to fire it. Correct absence, not a defect.
- `OPAL_BBGTML_daily_pull` then ran its missed-schedule catch-up at **09-09 08:36:29**, ~8 min after
  boot. `Get-ScheduledTaskInfo`: `Last=9/9/2026 8:36:29 AM, Result=0, Next=9/10/2026 7:00:00 AM,
  State=Ready`. Log: `TRIPWIRE: vintage 20260908` PASS -> `PUBLISH vintage 20260908` ->
  `OK: served data_as_of 2026-09-08 (generated_at 2026-09-09T12:44:39Z)` ->
  `RESULT: END-TO-END OK — pulled, validated, published, served-content verified.`

⚠ **AND THE OUTAGE LOST NO CORRECT ANSWER, because of the trading calendar — state this before anyone
reads a two-day gap as two days of stale data.** 2026-09-07 was Labor Day, so **T-1 for Tuesday 09-08
is Friday 09-04**, and the portal was *already* serving `data_as_of 2026-09-04` (published 09-05;
both the 09-06 and 09-07 runs correctly logged `SKIP: portal already serves … NOT re-firing`).
**The portal served the right vintage through the entire outage.** The gap is a scheduling fact, not
a data fact. (CLAUDE.md NEVER#1.)

---

## 3. DAILY GUARDRAIL — GREEN, PENDING TODAY'S 07:00 ET FIRE

Measured through the sanctioned mechanism (`tools/portal_lookup.py`, not self-report):

```
s3://opal-data-portal-v2/json/latest/manifest.json  (1551 bytes, read COMPLETE)
generated_at            = 2026-09-09T12:46:05.365584+00:00
sources.data_pkl.data_as_of  = "2026-09-08"
sources.model_pkl.data_as_of = "2026-09-08"
```

At 02:40 ET on 09-10 the served vintage **should** be 2026-09-08 — yesterday's publish. T-1 for today
is 2026-09-09, and the run that moves it is today's 07:00 ET fire, which has not happened yet
(`Next=9/10/2026 7:00:00 AM`, task `Ready`). **Not stale; pending.** It becomes a finding only if the
07:00 run fails to advance the served `data_as_of` to 2026-09-09.

No `bbg_fallback_ESCALATION.txt` exists anywhere under the user profile (maxdepth-4 sweep) — read as
no fallback escalation outstanding, and stated as the sweep it is.

---

## 4. D7 CLIENT-TICKET INTAKE — 166.1 HOURS, AND I AM WITHDRAWING MY OWN 09-06 CAUSAL LEAD

**The substantive fact, worse than the last reading (80.5h -> 166.1h):**

Census over the whole log (16660 lines, no `head`, no `tail`): **5407 passes — 613 exit 0,
4584 exit 2, 210 exit 5.** `LAST exit 0` is **unchanged** at `[Thu 09/03/2026 4:29:48.69]` =>
**166.1 h / 6.9 days** with no successful client-ticket fetch. Every failing pass logs
`no row examined, cursor unchanged` / `SWEEP_SKIPPED … NOT a zero`, so nothing is lost — but nothing
is being examined either, and this is the client-facing surface.

### ⛔ TWO RETRACTIONS ON MY OWN 09-06 ENTRY

**(a) "exit 5 = HTTP 403 = a token that is the wrong one" is WRONG.** The first exit 5 in the file is
`[Mon 08/31/2026 17:35:07.89]`, and the pass above it reads
`FETCH_FAILED URLError: <urlopen error _ssl.c:989: The handshake operation timed out>`.
**exit 5 is the generic FETCH_FAILED code**; 403 is one cause of it, not its meaning. The 09-06 entry
read the code off the two 403 instances in front of it and named the code after the instance.

**(b) "the mode flips from exit 2 to exit 5 within ~2 minutes of this seat making a gateway call,
two-for-two" is FALSIFIED.** Today's complete ordered sequence — **30 passes, denominator printed,
no filter** — flips mode **four times**:

```
00:04 - 00:14  exit 5  (3)
00:19 - 00:44  exit 2  (6)
00:49 - 01:44  exit 5  (12)
01:49 - 02:09  exit 2  (5)
02:19 - 02:34  exit 5  (4)
```

**This session did not exist until 02:19:51 ET and made no gateway call until ~02:26.** Three of those
four flips happened with no agent anywhere. The mode oscillates on its own at roughly 25-60 minute
cadence; the 09-05 and 09-06 observations sampled only the minutes around their own calls and found
the transition that was going to happen regardless. **A filtered census confirmed the hypothesis that
chose the filter.** The correlation is withdrawn; the outage is not.

**Still not mine and no surprise row is possible from here** — read-only seat, no lane on
`integrations/ticketing`. Routed to `0.0.0_AB_MSTR~Z` as evidence, with the retraction attached.

---

## 5. TEAMS — NOTHING OWED, AND THIS TIME BY A MAILBOX AUDIT, NOT A POLL WINDOW

**Arm banner, read before serving anything:**
`[teams-watch] armed interval=10s cursor=2026-08-28T20:07:10.323Z (incoming-only) pin(server=opal-gateway-bbg, identity=opalbloomberg)`
then `token selected: identity=opalbloomberg@opalinvest.com`.

- **Cursor 2026-08-28 is NEWER than my newest thread daily file (`2026-08-25.md`) -> no SUSPECT-REPLAY
  condition.** (TEAMS_DUTY "Reading the arm banner".)
- **No lapse.** Line-class census of the Monitor's complete output: 2 lines, **0 lapse notes,
  0 emits**, across ~90 cycles at 10s. Compare 09-06: **48 lapse notes from cycle 1**. The engine
  defect (`0.5.0_AE_OpalETL~Z`) has not recurred this session.

⚠ **09-06 could only offer a poll-window read. This one is a mailbox audit with a DIFFERENT
instrument** — `list_chats` (direct Graph) rather than `poll_addressed_teams_messages`:
**7 chats, `@odata.count: 7` against `top=10`, so complete, not a page.** Newest INCOMING message in
any of them:

| Chat | newest incoming | state |
|---|---|---|
| Andrew Berman (DM) | 2026-08-25T21:10:05Z | **answered** 79 s later, same thread |
| Yang Liu | 2026-08-18T17:54Z "thank you" | closed |
| Alyssa Keith (DM) | 2026-08-13T21:41Z | closed |
| Alyssa Keith (group) | 2026-08-03T17:42Z | closed |
| Manav Shah (meeting) | 2026-07-16T18:34Z | closed |
| Menachem Goldstein | 2026-06-22T20:14Z | closed |
| Manav Shah (DM) | — (cursor sits on my own 08-28 outgoing) | closed |

**Nothing is unanswered on the Teams surface.** That is now a claim about the mailbox, not about what
~24 polls happened to see.

⚠ **One unexplained artifact, noted not chased:** a message body `Test` was sent **FROM** the Opal
Bloomberg account into Andrew's DM at `2026-09-09T22:16:58.631Z` (18:16 ET) — **no agent session
existed then** (the box booted 09-09 08:28, last session ended 09-06). Outgoing, so no reply is owed
and the incoming-only monitor correctly ignored it; most likely a human at this box. Recorded because
an unattributed send from this identity is the kind of thing that should never be discovered later.

---

## 6. COMPILER TOOLS

| Tool | Invocation | Result |
|---|---|---|
| exit-code census | `grep -oE "intake pass exit [0-9]+" \| sort \| uniq -c` over 16660 lines | 613 / 4584 / 210, denominator printed — the **retraction** came from widening this to the whole file |
| ordered-mode census | `grep -E "^\[... 09/10/2026.*exit"` — all 30 of today's passes, unfiltered | four flips, three with no session live — the falsifier |
| line-class census | `sed -E 's/[0-9]+/N/g' \| sort \| uniq -c` over the Teams Monitor output | 0 lapse notes / 0 emits; a `tail` would have shown a healthy last line either way |
| `portal_lookup.py get … --find` | pipeline-status manifest.json | served vintage read WHOLE with its own denominator |
| `Get-WinEvent` 6005/6008/1074 | System log | the 09-07 -> 09-09 outage — the one instrument that could explain a missing log |
| `dapi_check.py` | under `C:\Anaconda\envs\cma\python.exe` | `DAPI: UP` rc=0 (green MCP is not a runnable pull) |
| `list_chats` | `opal-gateway-bbg` | mailbox audit — deliberately a DIFFERENT instrument from the monitor |

**Rule 22 note:** items 2, 4 and 5 each cost the world or another seat if wrong, so each was taken to
DISCRIMINATION with a second, differently-shaped instrument — event log for the pull gap, an unfiltered
whole-file census for the intake lead, direct Graph for the mailbox. The 09-06 entry's error was
precisely a second look through the FIRST instrument's window.

---

## 7. STATE AT CLOSE

Registered LIVE PID 6104. Inbox Monitor `bh55lbr03` and Teams Monitor `by8vel475` both `running`,
Teams pin held, cursor unmoved at 2026-08-28T20:07:10.323Z. Zero crons. Fabric inbox empty.
Portal serving `data_as_of 2026-09-08`; next scheduled fire 2026-09-10 07:00 ET, task `Ready`.

**Open, owned elsewhere:** (1) **D7 client-ticket intake, 166.1 h, client-facing** — the escalation.
(2) `teams-watch.py` lapse recovery being agent-triggered — `0.5.0_AE_OpalETL~Z`; did not recur today.
(3) `run_daily_pull.py`'s closing hint still points at the retired m365 gateway.
(4) `XXX.md` A.1 is unreachable from this seat by design (section 1) — a doc-vs-gate mismatch, not a
    defect in either.

⚠ **UNCOMMITTED:** this file, and every log under `logs/2026-09-05/` and `logs/2026-09-06/`. No git
lane here by design; `0.0.0_AB_MSTR~Z` is the named integrator.
**Push state of every hash cited: UNREAD** — no `ls-remote` run this session.
