# 0.0.3_BG_BBGTerminal -- STARTUP + daily guardrail, 2026-09-14T15:28-16:10Z

**archetype:** VALIDATE

Session `073c8ea7-9596-4b2c-a6b3-cb398a49c921` - broker PID 15404 - site Z, the Bloomberg box.

## 1. Reachability

| | state |
|---|---|
| Broker | NOT REGISTERED at load -> registered; pruned twice more on quiet (known 600 s prune), re-registered each time |
| Inbox Monitor | `bu4lpnnxg` -> expired 30m -> `betr2yfjo`, `TaskOutput -> running`; `ps` shows one watcher for this serial |
| Teams Monitor | `bt6e1oj2q` -> expired 30m -> `b0a247zo5`, pinned `server=opal-gateway-bbg identity=opalbloomberg` |
| Identity gate (2a) | **PASS** -- `whoami` = Opal Bloomberg / `opalbloomberg@opalinvest.com` |
| `bloomberg_health` | `ok: true` (127.0.0.1:8194, //blp/refdata) |
| Crons | zero (`CronList`: no jobs) |
| Inbox | empty (`check_inbox`); `check-inbox` shim is NOT on this session's PATH |

**Monitors cap at 30 min, not 60** -- the tool clamps `timeout_ms`; re-arm on every expiry notice.
Orphan check before each re-arm used BOTH `ps` and `Win32_Process`: they disagree on this box
(`Win32_Process` did not show any seat's inbox-watch bash; `ps` did). A DEAD verdict needs both.

## 2. Teams cursors -- no replay, one silent advance explained

- Arm 1: `cursor=2026-09-11T14:25:41.415Z` = this seat's last served act (Manav). Clean.
- Arm 2: `cursor=2026-09-11T21:15:07.917Z` with zero emits between. Discriminated with
  `poll_addressed_teams_messages(since=14:25:41Z)` (does not touch the cursor file): count 1, from
  Opal Bloomberg (the account's own outgoing). Source read of the chat: three attachment-only posts
  21:13-21:15Z to Manav -- the known human file-drop pattern (09-01 log 2a). Nothing skipped, nothing owed.
- **Corrected a prior record:** 09-11 "FIRST CONTACT" for Manav was wrong -- see
  `threads/2026-09-11-manav-shah/2026-09-14.md`.

## 3. Daily guardrail -- GREEN

```
OPAL_BBGTML_daily_pull       LastRun 09/14 07:00:01 ET  rc=0  Next 09/15 07:00
OPAL_BBGTML_freshness_check  LastRun 09/14 07:30:01 ET  rc=0  Next 09/15 07:30
C:\opal-elev\freshness_check.log 2026-09-14T11:30:02Z:
  PASS: data_as_of=2026-09-11 expected_frontier=2026-09-14 trading_days_behind=1
```
Monday's T-1 is Friday 2026-09-11: served content matches. rc=0 was not taken alone; the log line is
the checker's own read of served data (one instrument, not independently re-read portal-side).

## 3b. Teams token lapse on `b0a247zo5` -- recovered by a gateway call (KNOWN pattern, not new)

Monitor output census (4 lines, whole file): banner, `token selected`, `pinned token expired -- quiet
retry, pin HELD (cycle 1)`, then `re-selected after lapse: identity=opalbloomberg@opalinvest.com`
immediately after this seat's `whoami` on `opal-gateway-bbg`. Same identity; pin held.

Mechanism already on record (`logs/2026-09-06/resume_and_teams_lapse_1657-1705Z.md` S2, source
`teams-watch.py:36-39`): the watcher is a PASSIVE token reader; only an agent MCP call re-mints, and
an idle event-driven seat makes none. Bounded as DELAY, not LOSS -- the cursor cannot advance while
the token is falsy. Owner `0.5.0_AE_OpalETL~Z`; not re-surfaced.

**Seat-side ordering adopted (no cron, no new mechanism):** every 30-min Monitor re-arm now includes
one `whoami` on `opal-gateway-bbg`, which caps an unnoticed lapse at roughly one Monitor lifetime.

## 3c. ~17:2xZ -- msg 22846 (4.0.0_SA_CRO~Z relay, Andrew "Call 4 Yes": add GLD + VXX to etf_daily_pull.py FUNDS) -- RETURNED AS BLOCKER

READ-acked 22846. The ruling is not disputed; the card's lane assignment to this seat is.
- Fence read at source, not exercised (an edit on this box IS a deploy if the gate misfired):
  `.tools/hooks/bg-concierge-gate.sh:23-24` G1 write allowlist = own logs/threads/deliverables + tmp;
  deny text `:152`; G2 `:193/:196` git + commit tooling denied.
- File facts confirmed: `etf_daily_pull.py:45` FUNDS, `:174-176` unconditional append.
- Who can land it, as a CLAIM from commit `ebce987b42`'s message ("integrations/** is ANY_EXEC_OR_AE"),
  not a `.owned-paths.yaml` read.
- "Today" needs a second act: the 07:00 ET chain already ran (rc=0), so an edit now lands at the
  09-15 fire; capturing 09-14 needs a same-day ad-hoc ETF pull (download-class, gate G3 -- also not
  this seat's). The trade is Andrew's.
- Sent to `4.0.0_SA_CRO~Z` + `0.0.0_AB_MSTR~Z` in one send. Nothing edited, committed or pulled here.
- **CLOSED for this seat by msg 22854 (`0.0.0_AB_MSTR~Z`, READ-acked):** lane read at `.owned-paths.yaml`
  (`integrations/**` -> ANY_EXEC_OR_AE), which upgrades this seat's commit-history claim to a lane-file read
  by a different instrument. Act handed to `1.0.0_SA_CTO~Z` (seat edit vs round-5 cell is that seat's call);
  the "today" ambiguity (edit-only, 09-14 lost, vs + ad-hoc pull) surfaced to Andrew. Nothing owed by this seat.

## 3d. ~18:2xZ -- msg 22897 (`1.0.0_SA_CTO~Z`): DAPI DOWN -- did this seat restart it / sign in? ANSWERED NO

READ-acked 22897. Andrew approved ONE ad-hoc ETF pull at `1.0.0_SA_CTO~Z` (@b4c1666eb9); that seat held its
sign-in pending this answer.
- Measured 14:26:42 ET: bbcomm 33200 (14:22:36), blpcrashmon 31952 (14:22:37), NO wintrv, 8194 not listening;
  sign-in-shaped processes 0 (control explorer=1). This seat did nothing Bloomberg-side beyond read-only health.
- Application event log 13:30-14:30 ET: 14 events, 0 Bloomberg / WER / hang -- "no crash RECORDED", not "no crash".
- Ledger `C:\Users\Opal Bloomberg\.bbg_signin_attempts.json` (shared by bbg_signin.ps1:49 + terminal_signin.py:57):
  15 entries, newest 2026-09-13T11:01:59Z UNATTENDED-FALLBACK, ZERO on 09-14.
- Budget carriers DISAGREE, not adjudicated: READ_HERE.md s.2 "2-attempt budget" (no window) vs
  terminal_signin.py:58-59 "1 per 6h". Full under either reading.
- Heartbeat piggyback re-emitted 22846/22854/22897 as EMITTED after all three were individually READ-acked --
  the known replay; NOT re-acked, not batch-acked.

## 3e. Teams watcher `WinError 10054` -- three ISOLATED drops, no loss, not escalated

`[teams-watch] URLError: ... [WinError 10054] An existing connection was forcibly closed by the remote host`
appeared ONCE in each of three Monitors: `blan8p0ef`, `bhg7b242c`, `bilwhlvrz`. Never consecutive. Each time
`whoami` on `opal-gateway-bbg` answered normally right after, and the watcher kept running.
- Loss: none. `teams-watch.py` catches the exception before the cursor write (`:591-598`), so a failed poll HOLDS
  the cursor and the next cycle re-covers the window. Cursor at every arm since: `2026-09-11T21:15:07.917Z`.
- Correlation, stated as an observation NOT a cause: 2 of 3 followed a `re-selected after lapse` line; 1 of 3
  (`bhg7b242c`) had no lapse. Denominator 3, one device, one afternoon -- no rate and no mechanism claimed.
- Would change the call: consecutive drops in one Monitor, or `whoami` failing alongside one.
  Owner of the watcher: `0.5.0_AE_OpalETL~Z`; not surfaced at 3 isolated instances.
- **4th instance (`bygdi3697`) MET the second trigger, and a retry DISCHARGED it.** The watcher's drop coincided
  with this seat's own `whoami` failing (`The socket connection was closed unexpectedly`) -- so the drop is NOT
  watcher-specific; the gateway connection itself reset for both clients at once. Discriminator: ONE immediate
  retry of `whoami` -> answered normally (Opal Bloomberg). Monitor output after it: the single error line, no
  repeat. Read: a shared, momentary gateway-side reset, cleared within seconds -- not an outage.
  Denominator now 4 drops / 4 Monitors, never consecutive. Still not surfaced; the bar is now a SECOND failed
  `whoami` on retry, or consecutive drops, since one coincident failure has proven to be transient.

## 4. Carried forward

- Andrew's 2026-09-11 06:44Z attachment: still UNSERVED, not closed. Do not re-ask.
- Ball with Manav Shah. Nothing owed.
- Owned elsewhere, unchanged: attachment-read allowlist (Andrew ruling), D7 intake credential,
  teams-watch cursor-home defect (`0.5.0_AE_OpalETL~Z`).

**Push state: UNREAD BY THIS SEAT** -- no git lane; `0.0.0_AB_MSTR~Z` sweeps logs/threads.
