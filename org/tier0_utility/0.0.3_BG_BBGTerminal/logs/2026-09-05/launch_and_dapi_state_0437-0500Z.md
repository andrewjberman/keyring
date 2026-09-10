# 0.0.3_BG_BBGTerminal — session log 2026-09-05T04:37–05:00Z

**archetype:** DIAGNOSE

**Serial:** `0.0.3_BG_BBGTerminal` (base, no lane). Session `18e706ac-824b-4a54-abb7-5358248e2ae7`,
PID 6184. Launched via `ajb` — both F8 markers present and written by the launcher at 04:37:19Z
(`.launch-path` = `bg-concierge … launcher=ajb.ps1 host=OPAL_BLOOMBERG`, `.serial` =
`0.0.3_BG_BBGTerminal`). **XXX.md A.1 was NOT this seat's act** — G1 forbids the seat both writes and
the gate says so in its own denial text (`bg-concierge-gate.sh:130`); the launcher does them.

**Continuity:** previous session 2026-09-04, log `freshness_summons_step1_1139-1203Z.md` (the 07:30
STALE summons, discharged in that session). Nothing was owed into this one — see §1.

---

## 1. LOAD — reachability, and the one thing that could have been silently missed

`/watcher`: registration was NOT REGISTERED (a reboot drops it), re-registered LIVE PID 6184. Inbox
Monitor armed as task `bj0ydyxqs`; arm banner reads `parent-tied: pid 65`, so it is NOT orphan-capable.
Confirmed by `TaskOutput(bj0ydyxqs, block=false)` → `running` — the one probe that observes a CONSUMER.
`CronList` → no scheduled jobs, which is the correct state for this serial (XXX.md 1b-F: zero crons).

**Both inbox probes run, not one.** `check-inbox` empty; `get_agent_status` clean. Then the ledger,
which is the probe that can see what the other two structurally cannot:
`get_delivery_state(since=2026-09-04T00:00:00Z)` → **12 of 12 READ, 0 unread, ACKABLE denominator
12 of 12**. No `OFFER-EXHAUSTED` row, so nothing arrived into the dead window between sessions.
**Nothing was owed at load.** That is a measured statement, not the absence of a notification.

---

## 2. IDENTITY GATE AND THE TEAMS ARM

**2a IDENTITY ACCEPTANCE GATE: PASS.** `whoami` on `opal-gateway-bbg` → `displayName: Opal Bloomberg`,
`opalbloomberg@opalinvest.com`. `opal-gateway` (Andrew's proxy) was not called and is fence-denied anyway.

**3 TEAMS MONITOR: armed WITH the mandatory pin**, task `bjifdpaea`, `TaskOutput` → running. Banner,
read before anything was served off it:

```
[teams-watch] armed interval=15s cursor=2026-08-28T20:07:10.323Z (incoming-only) pin(server=opal-gateway-bbg, identity=opalbloomberg)
[teams-watch] token selected: identity=opalbloomberg@opalinvest.com
```

**CURSOR ADJUDICATED, NOT ASSUMED.** TEAMS_DUTY's replay test is *cursor vs the newest thread daily
file*. Newest daily file is `2026-08-25.md` (threads/2026-08-07-andrew-capability-roster/); the armed
cursor is `2026-08-28`, i.e. **NEWER**. So the backward-cursor replay condition does **not** hold and
nothing this arm emits is being carried as SUSPECT-REPLAY.
⚠ **The residual runs the other way and I am recording it rather than smoothing it:** a 08-25→08-28
gap means anything served in those three days left no thread record. That is the *un*-recorded
direction, which the TEAMS_DUTY test does not cover. RECALL still decides per message; the emit never does.

---

## 3. FINDING 1 — DAPI DOWN. The P0 gate run in full, and the sign-in deliberately NOT fired

`bloomberg_health` → `ok: false`. Launch step 4 therefore FAILS, which is RELAUNCH.md P4.

**Cause, measured not inferred:** Event 1074 at 00:30:10 local — `winagent.exe` (Advanced Monitoring
Agent / RMM) initiated the restart; `LastBootUpTime` 00:35:52. `wintrv` absent, `bbcomm` +
`blpcrashmon` up.

⛔ **The absent `wintrv` is NOT the evidence, and P0 exists precisely to stop that reading.** The
recovery record's three-row table shows `wintrv` absent across a working DAPI *and* a dead one on the
same day — a variable constant across both outcomes explains neither. So the P0 discriminator was run,
under **the pull's own interpreter** (`C:\Anaconda\envs\cma\python.exe integrations/bloomberg/auth/dapi_check.py`):

```
DAPI: DOWN (session.start() failed -- no listener/transport on 8194)   rc=1
```

**Layer 1 fails ⇒ the "If layer 1 FAILS" limb, all four cheap remedies, each recorded as eliminated:**

| # | Remedy | Result |
|---|---|---|
| 1 | re-probe 8194, sustained | **6/6 probes NO listener** (3 before, 3 after remedy 2) — a finding, not an unlucky read |
| 2 | restart `bbcomm` | pid 15600 → 10352, **still no listener** → ELIMINATED |
| 3 | network + unrelated control | BBG `69.187.48.83:8194` True, control `8.8.8.8:53` True → ELIMINATED |
| 4 | `bbcomm` outbound sockets | **loopback only** (127.0.0.1 pairs) — up but not connecting, path provably open |

That is the 2026-08-12 signature exactly. Sign-in is now the candidate remedy.

**⛔ AND I DID NOT FIRE IT. The reason is a mechanism with a filename, not caution.**
`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:99` runs
`bbg_credentials.py -- powershell -File bbg_fallback.ps1` as the **DAPI-liveness PRECONDITION** ahead of
the pull (Andrew RULED YES 2026-08-19, `@f45e5db124`). That fallback is agent-independent and carries
**C1 FIRE-ONCE — exactly one sign-in attempt per 6h window**, ledger
`%USERPROFILE%\.bbg_signin_attempts.json`, `$recent -ge 1 → Escalate; exit 2`.

Ledger read: last entry **2026-09-03T11:02:06Z**, 42h before this reading — **CLEAR**, so today's
07:00 ET (11:00Z) fire is UNBLOCKED. A sign-in fired now at ~01:00 ET lands within *minutes* of that
6h cutoff and would convert the scheduled fallback's one fire into an escalation.

**This is CLAUDE.md's named exception to the anti-coast rule** — "the ad-hoc would destroy the
discriminator the scheduled run exists to produce" — and the evidence is named, so the wait is not
the defect. It would be the defect without this paragraph.

**Why I hold that the automated path will work, stated as a rate rather than a hope:** the ledger
records `SUBMITTED-UNATTENDED-FALLBACK` at 11:00–11:02Z on **08-23, 08-26, 08-30, 09-01, 09-03** —
5 for 5 since the 08-18 end-to-end validation, and `bbg_fallback_ESCALATION.txt` has **no entry after
2026-08-18T17:47Z**. A Terminal token expiring roughly every other day is this box's ROUTINE state.
⚠ **Bounded honestly:** 5 for 5 is the unattended record *since* the 08-18 fix; it is not a claim that
tonight's post-reboot shape is identical to those five. It is closer to the 08-12 post-RMM-reboot case,
which also recovered. The fallback's attempt 1 uses `-Fresh` (kill a stale tree, relaunch a clean
dialog), which is the branch a post-reboot absence needs.

Precondition the GUI path needs and I checked rather than assumed: `query session` → `console … Opal
Bloomberg … Active`. Autologon carried the box through the reboot.

**Nothing is asked of any seat on this finding.** It is a NO-ACTION report by design.

---

## 4. FINDING 2 — D7 client-ticket intake has served nothing for 44.5 hours

Off this seat's lane; surfaced, not chased. It reaches this log only because that runner is what puts
client dashboard form submissions into the **Opal Client Tickets** channel this seat watches.

`OPAL_D7_ticket_intake`, every 5 minutes, `LastTaskResult=5`. Exit 5 is **runner.py's own contract**,
not `ERROR_ACCESS_DENIED` — `run_intake.cmd` says so in its header, so the code had to be read against
the log rather than against a Windows error table.

**Census over the WHOLE log** — `%USERPROFILE%\opal_ticket_intake\runner.log`, 13534 lines, no `head`
and no `tail` on the count:

```
4429 passes total:   613 exit 0   |   3702 exit 2   |   114 exit 5
LAST exit 0:         2026-09-03 04:29:48 local
first 403 line:      immediately after it  ->  outage began ~2026-09-03 04:34 local
403 lines:           113
```

Read at 2026-09-05 00:57 local ⇒ **44.5 hours with no healthy pass.**

Two interleaved modes: `REFUSED (exit 2): pinned gateway token expired -- no live credential this
pass`, and `FETCH_FAILED HTTPError: HTTP Error 403: Forbidden`. Tonight: exit 2 through 00:34, exit 5
from 00:39 on.

⚠ **NOT CAUSED BY THIS SESSION, and I checked because the timing invited the opposite reading.** The
mode flipped from exit 2 to exit 5 at 00:39, two minutes after this session registered at 00:37, which
looks exactly like a token-selection collision. It is not: **the 403 first appears at 09-03 04:34,
~44h before this session existed.** The onset date is the discriminator; the 00:39 flip is only which
of two pre-existing failure modes the pass landed in.

**NOTHING IS LOST, ONLY DELAYED** — every failing pass logs `no row examined, cursor unchanged` and
`SWEEP_SKIPPED no rows this pass (the fetch did not answer) -- NOT a zero`. The cursor has not moved,
so a credential repair should let the backlog flow.

Not fixed here: this seat is read-only, holds no lane on `integrations/ticketing`, and the surprise-
channel paths are outside its four writable paths. Routed to `0.0.0_AB_MSTR~Z` in the same turn.

---

## 5. COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | PATH exercise per XXX.md A.3 | **EXERCISE: a forwarder RAN** | scored on OUTPUT, not rc — a real and a no-match question both exit 0 |
| PATH census | `for t in .tools/comp-*` | **104 of 104 resolve bare** | denominator printed, not a boolean |
| `comp-read` | `BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md --for "who is authorized … attempt budget … preconditions"` | 327 lines / 59 sections; SALIENT surfaced the P0 gate and the "cannot complete one alone" qualifier | the QUALIFIER block is what stopped a premature sign-in |
| `comp-read` | `logs/2026-09-04/freshness_summons_step1_1139-1203Z.md --for "what is still open or owed"` | 522 lines / 73 sections | UNREAD LEDGER made §14 an explicit read rather than an assumed one |
| `comp-read` | `--enumerate` on `runner.py` | **BLOCKED by the HUD** (piped into `head`) | the block was CORRECT — a census into a receiver erases its denominator |
| `comp-find` | `"teams-watch" --files` | **BLOCKED by the HUD** (piped into `head`) | correct for the same reason; used native `Glob` instead |

**Rail fired three times against me and all three were right** — twice for piping a census into `head`,
once (G2) for a shell redirect into repo content that is genuinely outside this seat's writable set.
No `# rail-checked:` marker was used and `/freeform` was not invoked.

**Gap found, no tool at fault:** `.tools/to-check.py --all --assignee 0.0.3_BG_BBGTerminal` returned
the whole-fabric TO listing rather than an assignee-scoped one. XXX.md B.1 already says to treat a
zero or an absence from that read as telling nothing, and the authority is the dispatch message —
of which there were none. So it changed no conclusion and is recorded, not chased.

---

## 6. STATE AT CLOSE

Registered LIVE PID 6184. Inbox Monitor `bj0ydyxqs` and Teams Monitor `bjifdpaea` both `running`,
Teams arm carries the pin and the `identity=opalbloomberg@opalinvest.com` token line. **Zero crons** —
the backstop duty is EVENT-BASED (RELAUNCH §0b) and no summons has arrived. No Teams traffic this
session; nothing served, so no thread record was owed.

Sent: one message to `0.0.0_AB_MSTR~Z` carrying both findings and the housekeeping item
(`20260905T050027Z_0.0.3_BG_BBGTerminal_BG_launch_complete___TWO_measured_findin.md`).

**Open, owned elsewhere:**
1. D7 ticket intake credential — 44.5h, client-facing, owner not this seat.
2. `run_daily_pull.py`'s closing hint still points at the retired m365 gateway (carried from 09-04).

**Waiting on nobody. The next event on this box is the 07:00 ET fallback + pull**, which needs no seat.

⚠ **UNCOMMITTED, and stated here rather than left to be discovered:** this file, plus
`logs/2026-09-04/freshness_summons_step1_1139-1203Z.md` which is still ` M` against its last sweep
`c89605f379`. This seat holds no git lane by design; `0.0.0_AB_MSTR~Z` is the named integrator.
`deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md` IS swept (`@39c9040161`) and needs nothing.

**Push state of every hash cited above: UNREAD** — no `git ls-remote` was run in this session.
