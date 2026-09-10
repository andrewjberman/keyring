# 0.0.3_BG_BBGTerminal — session log 2026-09-06T16:57–17:05Z

**archetype:** DIAGNOSE

**Serial:** `0.0.3_BG_BBGTerminal`, session `18e706ac-…`, PID 6184 — **same session as the 09-05 log**,
resumed after ~36h idle on an operator question ("still online?").
**Continuity:** `logs/2026-09-05/launch_and_dapi_state_0437-0500Z.md`. That log left two findings and a
no-action call. This entry closes one, worsens one, and adds the one that should have been caught earlier.

---

## 1. THE 09-05 NO-ACTION CALL WAS RIGHT, AND THE ARTIFACT SAYS SO

09-05 predicted the 07:00 ET scheduled fallback would self-heal on its one fire-once attempt, and
declined to fire a sign-in at 01:00 because that would have consumed it. `bbg_tplus1_20260905_070002.log`:

```
[fallback]   password dots: 9 (expect 9)
[fallback] VERIFY: PASS  ->  verify PASS -- submitting ONCE
DAPI FALLBACK EXIT: 0
PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request.
TRIPWIRE: vintage 20260904 ... RESULT: PASS
OK:   served data_as_of 2026-09-04 (generated_at 2026-09-05T11:08:14Z)
RESULT: PUBLISHED 2026-09-04 -- verified by content, not by self-report.
ETF LEG EXIT 0 (7 objects) | CONSTITUENTS LEG EXIT 0 (9 objects)
```

Ledger gained `2026-09-05T11:01:41Z SUBMITTED-UNATTENDED-FALLBACK` — **6 for 6** since the 08-18
validation; `bbg_fallback_ESCALATION.txt` has **zero** 2026-09 lines.

09-06 07:00: DAPI already up, no sign-in; tripwire PASS; publish leg correctly **SKIPPED** —
*"portal already serves data_as_of 2026-09-04 … NOT re-firing the pipeline."* Both scheduled tasks
Result=0. DAPI re-verified just now under the pull's own `cma` interpreter: `DAPI: UP … entitled
session live` rc=0.

⚠ **Sunday's correct answer IS Friday.** Served vintage `2026-09-04` on 2026-09-06 is T-1 by the
trading calendar, not staleness. Saying so before anyone can misread it is the point of NEVER#1.

---

## 2. THE FINDING I DID NOT HAVE AND SHOULD HAVE — THE TEAMS MONITOR WAS DEAF FOR ITS ENTIRE LIFE

Census of task `bjifdpaea`'s complete output (51 lines, no `head`, no `tail`):

```
 1  arm banner (cursor=2026-08-28T20:07:10.323Z, pin present)
 1  token selected: identity=opalbloomberg@opalinvest.com
48  "pinned token expired -- quiet retry, pin HELD"   cycles 1 -> 1410
 0  successful polls        0  [TEAMS] emit lines
```

**IT LAPSED AT CYCLE 1** — the cycle immediately after the banner I had just confirmed as evidence of a
good arm. So the documented arm check passed and the surface went deaf about fifteen seconds later.

⛔ **AND NOTHING DOWNSTREAM COULD HAVE TOLD ME.** `TaskOutput` read `running`; the process was in `ps`;
the task id never changed; the fabric inbox Monitor beside it was genuinely healthy the whole time.
That is the anti-correlated shape — every liveness instrument reads healthy *precisely because* the
seat is deaf. My 09-05 log closed with "now event-driven and idle", which was true of the fabric
surface and false of the Teams one, and I had no instrument that separated them.

**Recovered, and the recovery is itself the proof of mechanism:** one `whoami` on `opal-gateway-bbg`
at 12:57 ET produced `[teams-watch] re-selected after lapse: identity=opalbloomberg@opalinvest.com`.
**Recovery is AGENT-TRIGGERED, never spontaneous** — Claude Code re-mints only on the next MCP call,
**and an idle event-driven seat makes none by definition.** The condition the monitor exists to cover
is exactly the condition in which nothing triggers its recovery.

**Bounded, so this is a DELAY and not a LOSS:** the cursor cannot advance during a lapse (the poll
block is skipped when the token is falsy), and it still reads `2026-08-28T20:07:10.323Z`.

**Post-recovery emit count: 0**, with no further lapse note after the re-select — so the monitor is
polling successfully from an unmoved 08-28 cursor and finding nothing. Read: **no Teams traffic since
2026-08-28T20:07Z**, consistent with the newest thread record being `2026-08-25.md`. Nothing owed on
the Teams surface. ⚠ That is a poll-window read, not a mailbox audit — it is what the instrument saw
in ~24 poll opportunities, and I am not upgrading it to a guarantee.

**Not mine to fix and not a new defect** — `teams-watch.py` is `0.5.0_AE_OpalETL~Z`'s and the
lapse-reshape is on record. What is NEW is that this lapse covered a seat's **whole session** starting
at cycle 1, rather than an interval inside one. Offered to that owner as evidence, not as a fix ask.

---

## 3. D7 CLIENT-TICKET INTAKE — 44.5h HAS BECOME 80.5h

Recount over the whole log (14851 lines, no `head`/`tail`): **4862 passes — 613 exit 0, 4126 exit 2,
123 exit 5.** `LAST exit 0` is **unchanged** at 2026-09-03 04:29:48 local ⇒ **80.5h** at this reading.

**A lead worth handing over, now two-for-two:** the mode flips from exit 2 (`pinned gateway token
expired`) to exit 5 (`HTTP 403: Forbidden`) within ~2 minutes of this seat making a gateway call —
00:37→00:39 on 09-05, 12:57→12:59 today. Reading: the intake shares the token store with this seat,
and the token this seat mints **authenticates but is not authorized** for the intake's fetch. Exit 2 =
no token at all; exit 5 = a token that is the wrong one. **Two faces of one credential problem.**

⛔ **The correlation is not causation, and that half is what keeps it useful:** the 403 first appears
2026-09-03 04:34, ~44h before this session existed. This seat's calls select which failure mode is
*visible*; they did not create the outage.

Still nothing lost — every failing pass logs `no row examined, cursor unchanged` / `SWEEP_SKIPPED …
NOT a zero`. Read-only seat, no lane on `integrations/ticketing`, no surprise row possible from here.

---

## 4. COMPILER TOOLS

| Tool | Invocation | Result |
|---|---|---|
| line-class census | `sed`-normalised `sort \| uniq -c` over the Monitor output | 48 lapse notes / 0 emits — **the finding**; a tail would have shown a healthy-looking last line |
| exit-code census | `grep -oE 'intake pass exit [0-9]+' \| sort \| uniq -c` over 14851 lines | 613/4126/123 with the denominator printed |
| `dapi_check.py` | under `C:\Anaconda\envs\cma\python.exe` | `DAPI: UP … entitled session live` rc=0 |

**Instrument trap paid for once:** `ls` is `-F` aliased in this shell, so `$(ls …)` returned names
carrying the executable `*` and two `cat`s failed on a path that existed. Fixed by naming the files
directly. The tell was a *file-not-found on a file the listing had just shown* — a wrong-object error,
which is the class no content tool can catch for you.

---

## 5. STATE AT CLOSE

Registered LIVE PID 6184 (**pruned twice** by the liveness reaper during idle; re-registered both
times, same PID, so neither was an identity conflict). Inbox Monitor `bj0ydyxqs` and Teams Monitor
`bjifdpaea` both `running`; Teams pin held and token re-selected. Zero crons. Fabric inbox empty;
`get_delivery_state` since 2026-09-05T04:30Z returned **0 rows matched — which is not zero delivered**,
and the empty `read/` agrees.

Update sent to `0.0.0_AB_MSTR~Z`
(`20260906T170307Z_0.0.3_BG_BBGTerminal_UPDATE_on_both_09-05_findings…`).

**Open, owned elsewhere:** (1) D7 intake credential, 80.5h, client-facing. (2) `teams-watch.py` lapse
recovery being agent-triggered — `0.5.0_AE_OpalETL~Z`. (3) `run_daily_pull.py`'s closing hint still
points at the retired m365 gateway.

⚠ **UNCOMMITTED:** this file, and `logs/2026-09-05/launch_and_dapi_state_0437-0500Z.md`. No git lane
here by design; `0.0.0_AB_MSTR~Z` is the named integrator.
**Push state of every hash cited: UNREAD** — no `ls-remote` run this session.
