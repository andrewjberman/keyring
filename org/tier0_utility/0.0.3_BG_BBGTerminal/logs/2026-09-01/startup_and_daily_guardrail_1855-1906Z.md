# 0.0.3_BG_BBGTerminal — session log 2026-09-01T18:55–19:06Z

**Archetype:** STARTUP + DAILY GUARDRAIL
**Serial:** 0.0.3_BG_BBGTerminal (base; no lane suffix) · broker PID 16328 · device: site Z
**Launch instruction:** `/watcher` first, then `org/XXX.md`. prompt.md's "On launch" says *no
XXX.md — you are not a fabric work seat*. **I ran prompt.md's sequence**, and ran the two XXX.md
limbs that are cheap and self-scoped (A.1, A.3). A.1 was REFUSED by my own fence — see §1b.

---

## 1. Launch sequence — every step with the evidence that scored it

| # | Step | Result |
|---|---|---|
| 1 | `register_agent` | LIVE, PID 16328. **Receipt also said `Broker: unavailable`** — recorded, see §1c |
| 2 | `/watcher` | Monitor `b38eciz71`; banner `parent-tied: pid 1078` = ARMED, not orphan-capable; child 1082 ppid 1078 |
| 2a | **IDENTITY ACCEPTANCE GATE** | **PASS** — `opalbloomberg@opalinvest.com`, not Andrew |
| 3 | Teams Monitor | `bi6lvvse4`; pin confirmed AT THE BANNER (§3) |
| 4 | `bloomberg_health` + `cma` | `ok:true` (127.0.0.1:8194, //blp/refdata); cma py3.13.2 blpapi 3.26.4.2, `session.start()=True`, `openService(//blp/refdata)=True` |
| 5 | Latest log read (2026-08-28); **ZERO crons** | `CronList` → "No scheduled jobs". The two Monitors are not crons |

**Watcher pre-state, measured not assumed:** `ps -ef | grep inbox-watch.sh` returned NOTHING for any
serial, and `get_agent_status` read **NOT REGISTERED**. Both limbs of the orphan discriminator agreed
on "genuine fresh session" — no kill was needed and none was made.

### 1b. A.1 (session serial file) was REFUSED BY MY OWN FENCE — and that is the fence working
`bg-concierge-gate G2` blocked the write: *"shell redirect into repo content ... The BG seat's writable
set is its own logs/threads/deliverables + tmp."* `org/mcp/sessions/` is outside it. **I did not route
around it** (prompt.md: a BLOCKED from this gate is the system working). Consequence stated rather than
implied: **no `org/mcp/sessions/<session-id>.serial` row exists for this session**, so XXX.md Step 1
identity-precedence source #2 is unavailable for me; sources #3 (my armed Monitor watches this serial's
inbox) and #4 (my registration) both resolve. Session id `43f2d0b3-ff55-4894-b6b3-fb72a21ae590`.
**This is structural for this seat, not an incident** — it will recur every session. Not surfaced as a
finding; noted so a reader does not read the absent row as a missed step.

### 1c. `Broker: unavailable` at first register — RESOLVED at close, same session, same PID
The first `register_agent` receipt read `Broker: unavailable` while `Channel push: enabled`. I did not
investigate at the time (Rule 2: the next check would not change what I do — my mail path is the
Monitor, which was armed and parent-tied). **It resolved itself and I did not have to ask:** the
close-of-session re-register (§5a) returned `Broker: connected (port 7800)`, same PID 16328. **The
daemon was still coming up at 18:55Z**, which `register_agent` auto-launches. Not a defect; the string
is a startup-race artifact. Recorded with BOTH readings so a peer who sees the first one knows to
re-read rather than chase.

### 1d. A.3 PATH — **`105 of 106` comp-tools resolve bare**, and one was EXERCISED
`comp-which "how do I grep the repo"` produced its own banner → scored on OUTPUT, not rc. The
07-29 anti-correlated failure (93 of 93 resolving while zero ran) is excluded by the exercise limb.
1 of 106 not resolving is not a defect I am asserting — I did not identify which, because it would
not change what I do.

---

## 2. Teams — arm banner read BEFORE serving; cursor CLEAN this session

```
[teams-watch] armed interval=15s cursor=2026-08-25T21:11:24.527Z (incoming-only)
              pin(server=opal-gateway-bbg, identity=opalbloomberg)
[teams-watch] token selected: identity=opalbloomberg@opalinvest.com
```
Pin confirmed at the BANNER, not from the returned task id.

**F1 cursor divergence did NOT bite this session — the two homes AGREE.** Measured before arming:
```
/c/tmp/teams-watch.cursor                                  2026-08-25T21:11:24.527Z
%LOCALAPPDATA%\Temp\teams-watch.cursor                     2026-08-25T21:11:24.527Z
```
`TMPDIR` unset (harness exports `TEMP`/`TMP` only), so native Windows Python resolved `/tmp` → `C:\tmp`.
**I set no `TMPDIR` and hand-edited no cursor file.** The armed cursor (08-25T21:11:24Z) is NEWER than
my newest thread daily entry (`threads/2026-08-07-andrew-capability-roster/2026-08-25.md`, last recorded
message 21:10:05Z) → **the SUSPECT-REPLAY condition does not hold this arm.** F1 remains live and
remains `0.5.0_AE_OpalETL~Z`'s; today it simply did not fire.

### 2a. ZERO emits with a cursor ADVANCE — resolved, and the resolution is worth carrying
The cursor moved `2026-08-25T21:11:24.527Z` → `2026-08-28T20:07:10.323Z` while the Monitor printed
**no `[TEAMS]` line at all.** A silent advance is the shape a dropped message would also make, so I
did not accept it. **Instrument used: `poll_addressed_teams_messages(since_iso=2026-08-25T21:11:00Z)`
— the MCP tool, which reads the API and does NOT touch the engine's cursor file**, so re-reading the
window cost nothing and moved nothing.

**Both rows in the window are `from_name: "Opal Bloomberg"` — the account's OWN outgoing.**
`incoming-only` filtered them correctly. Denominator: 2 of 2 accounted for.

| ts | chat | verdict |
|---|---|---|
| 2026-08-25T21:11:24.527Z | Andrew DM | my own reply, already in the 08-25 daily file |
| 2026-08-28T20:07:10.323Z | 1:1 with `7aa72700…` | 3 attachments, posted by the ACCOUNT, not by an agent |

⭐ **THE DATUM WORTH BANKING: THIS ACCOUNT'S CURSOR IS NOT AGENT-CONTROLLED.** A human posting from
the Opal Bloomberg Teams account advances the monitor's cursor, because the engine takes the API's
cursor for the whole window and only FILTERS at emit. That is benign as built (it can only skip the
account's own outgoing, never a third party's inbound) — but it means **"the cursor moved" is not
evidence an agent did anything**, and a reader reconciling cursor position against session history
will find gaps that no session explains. Read the second chat at source: **all 15 messages back to
2026-07-02 are from Opal Bloomberg, zero from the other party** — it is a human file-drop thread.

**NOTHING WAS OWED. I sent no ack and no reply.** The emit told me what to look at; thread memory and
the source read told me what was owed.

---

## 3. DAILY UPLOAD GUARDRAIL (record @e77bec6e5) — **PASS**, end-to-end, for 2026-09-01

**Trading calendar resolved via the ONE frontier, not by hand** (`lib/trading_calendar.py`):
`calendar_source = NYSE/hardcoded-fallback-2024-2027`; `is_trading_day(2026-09-01) = True` (Tuesday);
`prev_trading_day(2026-09-01) = 2026-08-31`. **T-1 is 20260831.**

| surface | reading |
|---|---|
| `OPAL_BBGTML_daily_pull` | Last **9/1 07:00:01 ET**, Result **0**, Next 9/2 07:00 |
| `OPAL_BBGTML_freshness_check` | Last **9/1 07:30:01 ET**, Result **0**, Next 9/2 07:30 |
| artifacts | `data 20260831 v1.pkl` (8,611,786 B) + `model 20260831 v1.pkl` (17,584,849 B), written 9/1 07:04–07:05 |

**The run's as-of 20260831 IS exactly T-1. Correct, not stale.**

**This guardrail is STRONGER than a records check today, and the reason is in the task, not in me.**
`scheduled_daily_pull.cmd` has been FULL END-TO-END since 2026-08-06 (Andrew-direct): DAPI-liveness
precondition → pull → tripwire → as-of-scoped gate → publish to S3 → **verify SERVED by CONTENT**.
So `LastTaskResult=0` is not only a producer self-report here. Read at source in
`~/opal_bbg_logs/bbg_tplus1_20260901_070001.log`:
```
PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request.
TRIPWIRE: vintage 20260831 ... RESULT: PASS -- both PKLs safe to send
WAIT: polling served artifact for data_as_of 2026-08-31 (timeout 900s)
OK:   served data_as_of 2026-08-31 (generated_at 2026-09-01T11:07:56Z)
OK:   served 1D matches the PKL for all five models
RESULT: PUBLISHED 2026-08-31 -- verified by content, not by self-report.
RESULT: END-TO-END OK -- pulled, validated, published, served-content verified.
```
ETF leg EXIT 0 (7 objects under `bbg/2026-08-31/`), constituents leg EXIT 0 (9 objects).
**No fallback `/terminal-upload` was needed and none was run.** The gateway overlay allow row stays
what it is: fallback capability, not the routine path.

### 3a. A gap I raised against myself and then RETIRED with the right instrument
No PKL carries an 8/30 or 8/31 mtime, which reads as two missed fires. **It is not.** Scheduled-task
`LastRunTime` is single-valued (banked: it cannot speak about any fire but the most recent), so I used
the run-log directory instead: `bbg_tplus1_20260830_070001.log` and `bbg_tplus1_20260831_070001.log`
both exist. **Both days fired.** 8/29–8/30 are the weekend and 8/31's answer was Friday's vintage
already on disk — *Friday IS Monday's answer* — so neither produced a new artifact mtime. **The
artifact-mtime instrument cannot distinguish "did not run" from "ran and correctly wrote nothing";
the run-log directory can.**

### 3b. The DAPI fallback FIRED today — designed path, recorded because it is not free
`[fallback] VERIFY: PASS ... submitting ONCE (bbg_signin.ps1 -Phase submit)` → `DAPI FALLBACK EXIT: 0`.
The Terminal was not signed in at 07:00 and the two-phase budgeted sign-in self-healed it, exactly as
`integrations/bloomberg/READ_HERE.md` specifies. **Not a failure and not mine to chase** — logged
because a fallback that fires silently every day is a fallback that has become the primary path, and
that transition is only visible if each firing is written down.

---

## 4. Compiler Tools

| tool | use | outcome |
|---|---|---|
| `comp-find` (content) | locate `teams-watch.py` across the estate | HEAD band put `.claude/skills/teams-assist/teams-watch.py` first; denominator printed (1134 hits / 50305 files) |
| `comp-find` (scoped) | prior arm invocation in my own logs | 18 of 18 on one page — no truncation, no `head` |
| `comp-which` | A.3 exercise | produced its own banner (scored on output, not rc) |

**Rail compliance, self-scored against last session's finding.** The 08-28 log's sharpest self-audit
was *"I proved the instrument worked and then did not pick it up"* — 12 raw greps, zero comp-which
reflexes. **This session the rail FIRED once and I complied rather than routing around it:** a
`grep -rn` over my own logs was DENIED by the HUD and I re-ran it as `comp-find`. One raw grep survives,
marked: `# rail-checked:` on `~/opal_bbg_logs/bbg_tplus1_20260901_070001.log` — a transient run log
**outside the repo corpus**, which is Rule 21's non-application limb (iii) verbatim. That is the
adopted behaviour actually exercised, not restated.

---

## 5. State at close of startup

- **Both Monitors armed and confirmed:** inbox `b38eciz71` (parent-tied pid 1078), Teams `bi6lvvse4`
  (pin confirmed at banner). **ZERO crons.**
- **Fabric inbox:** empty — `check_inbox` and `get_agent_status` both clean, no ferry entry needed.
- **Zero pending task orders** (`get_agent_status`).
- **Nothing owed on Teams.**
- **Daily guardrail PASS** for 2026-09-01; served vintage 2026-08-31 = T-1, content-verified.
- **Available.** Next scheduled Bloomberg fire 2026-09-02 07:00 ET.

### 5a. A close-of-session `heartbeat` PRUNED my own registration — banked behaviour, exercised live
`heartbeat("0.0.3_BG_BBGTerminal", ...)` returned **`is not registered. Call register_agent first.`**
~11 minutes after a successful `register_agent` at the same PID. This is the banked
`heartbeat-after-10min-quiet-prunes-you-then-blames-you` shape: **my own liveness call deleted my
liveness entry and then reported it as my error.** Remedy is the one the receipt names —
`register_agent` again (PID unchanged at 16328, so no identity conflict and no peer to adjudicate).
**Consequence a reader should not have to infer: between the prune and the re-register I read as
NOT REGISTERED to the fabric**, while both Monitors stayed armed and my inbox stayed watched. That is
the anti-correlation this estate keeps meeting from a new door — *the registration plane and the
delivery plane fail independently, and only one of them was ever down.*

**No ARMED surprise items opened this session.** The 08-28 READ-clock item (§2/§2c of that log) was
closed at my end by my predecessor and its disposition rests with `3.0.0_SA_CVO~Z`; I am not
re-opening an item I do not own and did not re-measure.

---

## 6. POST-STARTUP — 21:32Z inbound: merge window on the shared tree (msg 19274)

**The inbox Monitor delivered its first live event of the session** — `0.0.0_AB_MSTR~Z` opened a
MERGE WINDOW on the site-Z shared tree (`/integrate parity` leg 1, CLOUD→SITEZ, 86 commits / 94
files, overlap 3 of 166 = 1.81%), asking every seat sharing the worktree to hold safe-commits until
a CLOSE frame. **The Monitor arming in §1 is therefore not just declared-armed, it is EXERCISED** —
delivered, read at source, acked.

**Acked on BOTH clocks, in the right order:** `ack_messages("19274")` → *"READ ack recorded by
0.0.3_BG_BBGTerminal for 1 message(s)"* — accepted, not the write-once refusal my predecessor hit on
08-28. Then the RAVC reply (silent receipt is a violation), delivered not queued.

**My compliance is STRUCTURAL and I said so rather than letting it read as restraint.** This seat
runs zero safe-commits during the window because it runs zero safe-commits at all — no OWNPATHS lane
exists for this serial and prompt.md says none should ever be added. **A "held" ACK from a seat that
never commits would inflate the denominator of seats actually restrained**, so I asked to be counted
as a NON-SOURCE of the staging hazard, not as a complier. That distinction is the whole content of
the reply.

⭐ **THE ONE JUDGEMENT CALL: I named my untracked log to the integrator AND told them not to take
it yet.** `logs/2026-09-01/startup_and_daily_guardrail_1855-1906Z.md` is the only file this seat
touched, it is untracked, and `0.0.0_AB_MSTR` is my named integrator for logs (OPAL_ANALYST.TO5) —
so it IS in sweep scope. But msg 19274's stated hazard is a lane's files being silently staged into
the integrator's merge index. **Volunteering an untracked file mid-merge is a way to walk straight
into the hazard the message was sent to prevent**, so I framed it AFTER-CLOSE explicitly rather than
either staying silent (the sweep misses it) or offering it plainly (it lands in the merge index).

**49F deploy note: not mine, and I said so instead of absorbing it.** `49-schwab-conv` is AE-owned;
prompt.md names this seat as aware-of-but-not-owner. That note needs a different addressee.

**Surfaced, not requested:** if any parity or census instrument resolves seats through
`org/mcp/sessions/`, this seat is structurally absent from it (§1b) — absent by fence, not by
failure, and on every future run. I asserted no instrument does this and asked for no change.

---

## 7. 21:39Z — CLOSE frame (msg 19282): the merge DELIVERED LAW, and the tree moved under my running processes

**Window CLOSED @`a4c3c519cf`, on origin.** Acked (`ack_messages("19282")` accepted). The thread I
opened in §6 — the log held back for after the CLOSE — I closed myself rather than leaving it for
the integrator to remember: the file is now free for any ordinary sweep.

### 7a. I re-read CLAUDE.md with a DIFF, not with the harness notification — and the distinction is the point
My harness surfaced the Rule 21 change on its own, before msg 19282 arrived. **I did not treat that
as the re-read.** A harness notification is explicitly headed *"relevant changes"* — a SCOPED view,
which structurally cannot answer *"was that the only change?"*. So:
```
git diff a4c3c519cf^1 a4c3c519cf -- CLAUDE.md   ->  EXACTLY ONE HUNK, Rule 21 limb (i). Nothing else.
```
The notification turned out to be complete. **That is a result, not a reason to have skipped the
check** — msg 19282's own thesis is that a stale snapshot carries no signal, and *reading a scoped
notification as a complete diff is that same defect one layer up.* Cost: one `git diff`.

### 7b. LAW CHANGE THAT BINDS MY INSTRUMENT CHOICE — Rule 21 limb (i) DISCHARGED
`comp-read --enumerate` has landed and is certified. **A count is no longer a reason to reach for
`grep`.** Limb (iii) — files outside the repo corpus — is UNCHANGED, so this session's one marked
raw grep (`~/opal_bbg_logs/…`, §4) **stands correct as filed** and needs no retraction. Going
forward the count case routes to `--enumerate`. `grep -q` as a pure predicate and any pipe-receiver
remain non-application. **[[adoption-is-not-implementation]] — banking this changes nothing; the
trigger is the next act.**

### 7c. THE MERGE DID NOT DISTURB THIS SEAT — measured, with the denominator, not assumed
94 files landed on the tree my two Monitors are running from. **"Nothing changed for me" is worth
exactly as much as the set it was checked against**, so:
```
git diff --name-status a4c3c519cf^1 a4c3c519cf   ->  denominator 94 files
filtered for: tier0_utility/0.0.3_BG_BBGTerminal | skills {watcher, teams-assist,
  bbg-teams-assist, terminal-upload, bbg-daily} | integrations/bloomberg |
  lib/trading_calendar.py | hooks/bg-concierge-gate | inbox-watch
RESULT: ZERO OF 94.
```
**Consequence that actually mattered and could have been missed:** `inbox-watch.sh` and
`teams-watch.py` were both untouched, so **both Monitors are still executing bytes that match the
tree** — no re-arm needed, none done. Had either moved, the armed process would have been running
pre-merge bytes with every liveness instrument still reading healthy, which is this estate's
recurring anti-correlated shape through yet another door.

### 7d. Two items checked rather than waved past
- **`LD-0499` → `LD-0500` renumber:** I hold **no** citation to either number, drafted or committed.
  Checked, not assumed. Nothing to correct.
- **49F deploy note** (`chain_49f_entrypoint.py`, LastModified moved with an UNCHANGED ETag): not my
  chain, and I hold no drift detector — timestamp- or hash-based — on that object or anything under
  `opal-data-49financial`. It needs its owner.

**Reach disclosure in 19282 names this seat accurately** (came up mid-merge, acked 19274). I asked
that it not be counted as one of seven seats restrained: this seat was never a source of the staging
hazard, because it does no git work at all.
