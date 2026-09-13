# 0.0.3_BG_BBGTerminal — PRE-REBOOT STATE 2026-09-11T13:40Z

**Andrew-direct 13:3xZ, VERBATIM:** *"have everyone take /log of current state and ill reboot this
device"* (relayed `0.0.0_AB_MSTR~Z` msg 21385). Written for a successor with **no context**.

**Serial:** `0.0.3_BG_BBGTerminal` · session `fd87eb7b-…` · PID 6104 · site Z, the Bloomberg box.
**Today's fuller records:** `logs/2026-09-11/teams_serve_roster_and_guardrail_1150-1245Z.md` and
`threads/2026-08-07-andrew-capability-roster/2026-09-11.md`. Read those second; read §1 first.

---

## 1. ⛔ SUCCESSOR: THE TEAMS CURSOR HAS TWO HOMES AND THEY ARE 14 DAYS APART. READ THIS BEFORE ARMING.

Measured 13:39Z, both homes, byte values and mtimes:

```
C:\tmp\teams-watch.cursor                      2026-09-11T12:37:32.566Z   mtime 09-11 08:37 ET  <- LIVE
%LOCALAPPDATA%\Temp\teams-watch.cursor         2026-08-28T20:07:10.323Z   mtime 09-04 08:08 ET  <- STALE
```

**The live value is `2026-09-11T12:37:32.566Z`** — this session's own last outgoing message. The
cursor ADVANCED today; the arm banner's `2026-08-28T20:07:10.323Z` is NOT the closing value and
must not be carried forward as one.

⛔ **IF YOUR ARM LANDS ON THE `%LOCALAPPDATA%` HOME YOU WILL REPLAY FOURTEEN DAYS AS NEW BACKLOG**,
including **the entire Andrew exchange of 2026-09-11** — his 06:44Z attachment and all seven of this
seat's replies. It will arrive complete, oldest-first, correctly framed `(1 of N)` with per-chat
denominators, and **it is indistinguishable from a real backlog by shape alone.** That is the
measured 2026-08-25 failure (an ack apologised to Andrew for a five-day delay on messages already
served; he has seen it ONCE — do not spend it a second time).
**`teams-watch.py:98` builds the path from `os.environ.get("TMPDIR", "/tmp")`.** The harness exports
`TEMP`/`TMP` but **not** `TMPDIR`, so native Windows Python resolves `/tmp` to `C:\tmp` — which is
why `C:\tmp` is the live home under the harness. A launcher that sets `TMPDIR` lands elsewhere.
**READ THE ARM BANNER'S `cursor=` VALUE AND COMPARE IT TO THE TWO VALUES ABOVE BEFORE SERVING
ANYTHING THAT ARM EMITS.** Engine defect owned by `0.5.0_AE_OpalETL~Z`; do not hand-edit a cursor
file to compensate.

---

## 2. WHAT SURVIVES THE REBOOT AND WHAT DOES NOT

| | state |
|---|---|
| **SURVIVES** — `OPAL_BBGTML_daily_pull` | 07:00 ET, `StartWhenAvailable=True`, next 09-12 07:00 |
| **SURVIVES** — `OPAL_BBGTML_freshness_check` | 07:30 ET, **`StartWhenAvailable=False`** — it does NOT backfill a missed fire; a reboot spanning 07:30 drops that day silently (`NumberOfMissedRuns` reads 0 either way) |
| **SURVIVES** — the Bloomberg Terminal sign-in | DAPI was UP at 12:39Z; a reboot signs it OUT. The 07:00 fallback will sign in unattended (6 for 6 since 08-18) |
| **DIES** — inbox Monitor `bh55lbr03` | re-arm via `/watcher` |
| **DIES** — Teams Monitor `by8vel475` | re-arm per §1, cursor check FIRST |
| **DIES** — broker registration | re-`register_agent` under the FULL serial |

**Sign-in budget at close:** ledger `~/.bbg_signin_attempts.json` holds **13** entries, last
`{"at": "2026-09-10T19:47:28.6435476Z", "outcome": "SUBMITTED-SUPERVISED"}`. **One attempt of two
unspent.** Playbook is `integrations/bloomberg/READ_HERE.md` §2 — fill (free, repeatable), **verify
the screenshot against `pw_len` before submitting**, then submit.

---

## 3. OWED, AND TO WHOM

1. **Andrew — his 06:44:18.59Z Teams attachment is UNSERVED.** Body is exactly
   `<attachment id="fa5079da-3c82-4dc4-8754-b2f91a595ef7"></attachment>`, **no text**. This identity
   **cannot open it** (`search_files` / `list_onedrive` / `get_item` / `list_recent_email` /
   `find_sharepoint_site` all return `identity_scope_denied`). He was told, and given two unblocks.
   **Waiting on HIS content or question — do not re-ask, and do not treat it as closed.**
2. **A5 live positive — STILL UNSATISFIED.** His next real two-in-a-row exchange must arrive
   complete and in order with the `(1 of 2)` frame; confirm in-thread and retire the interim
   re-send rule in the same message. **DO NOT MANUFACTURE IT.** (`THREAD.md` OPEN.)
3. **Nothing owed to any fabric seat.** `0.0.0_AB_MSTR~Z` closed every thread today and said
   "nothing owed back" four times. No task orders: `to-check --all --assignee` = 0.
4. **No worker subagents, no worktrees.** This seat spawns none and holds no git lane.

**Open, owned ELSEWHERE — carry forward, do not chase:** D7 client-ticket intake (171.2 h at the
09-10 reading, client-facing) · `teams-watch.py` agent-triggered lapse recovery, `0.5.0_AE_OpalETL~Z`
(**recurred overnight and cost five hours on a real Andrew message**) · mid-session terminal
sign-out has no automatic recovery (route is Andrew) · `freshness_check`'s `StartWhenAvailable=False`
with this seat's transient-alarm qualifier (`0.0.0_AB_MSTR~Z` holds the call) ·
`run_daily_pull.py`'s closing hint still points at the retired m365 gateway.

---

## 4. ONE CORRECTION TO THE RELAY'S PREMISE — RIGHT CONSTRAINT, WRONG PLANE

Msg 21385 says the box is at **"0.2 GB free"** and warns of "no headroom for a large checkout".
Measured here 13:39Z:

```
RAM free : 0.53 GB of 63.46 GB      <- THIS is the 0.2-GB-class figure. Rio.exe WS = 43.62 GB
C: free  : 179.1 GB                 <- disk is FINE
CPU load : 73%
```

**The scarcity is MEMORY, not DISK.** The instruction's substance is right — keep the log small,
skip long gate runs — but "no headroom for a large checkout" is a DISK claim and disk is not the
constrained resource; a checkout would succeed and a memory-hungry gate is what would fail. Stated
because a true number on the wrong plane sends the next seat to the wrong remedy. **The reboot is
correct either way: Rio.exe at 43.62 GB working set is the reason.** Not a dispute — Andrew chose it.

---

## 5. DAILY GUARDRAIL AT CLOSE — GREEN

`bbg_tplus1_20260911_070002.log`: `PRECONDITION: PASS -- DAPI UP` · `PULL EXIT CODE: 0` ·
`RESULT: PUBLISHED 2026-09-10 -- verified by content, not by self-report` · ETF 0 · constituents 0.
Checker `2026-09-11T11:30:03Z PASS: data_as_of=2026-09-10 expected_frontier=2026-09-11
trading_days_behind=1`. **Portal serving `2026-09-10` = healthy T-1.** Next fires 09-12.
⚠ **Successor: T-1 for Monday 09-14 is Friday 09-11. Friday's data on Monday is CORRECT.**

**Push state: UNREAD BY THIS SEAT.** This seat holds no git lane; `0.0.0_AB_MSTR~Z` is the named
integrator and pushes. Every hash in today's records is quoted from that seat's `ls-remote` reads.
