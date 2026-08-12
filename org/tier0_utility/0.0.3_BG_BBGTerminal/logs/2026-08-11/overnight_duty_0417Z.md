# 0.0.3_BG_BBGTerminal — Session Log — 2026-08-11 (day rollover, ~0417Z onward)
**archetype:** VALIDATE

Continues the session opened 2026-08-10 ~2345Z (`logs/2026-08-10/relaunch_opus5_high_2345Z.md`
— relaunch evidence + the token-expiry finding live there). New file on the DATE boundary; the
session itself is unbroken.

## Summary
Overnight duty on the same relaunched seat. Teams concierge live and identity-pinned through
five token-expiry re-arm cycles; zero inbound across all of them; cursor unmoved. Bloomberg
DAPI still down (unchanged, at Andrew). New session-day opened the daily upload guardrail duty
again — today's scheduled run has NOT YET occurred and is recorded as PENDING, not as a pass.

## Timeline
- **Death #10 / re-arm:** b9bl0kn00 armed 0316:49Z, died **0416:44Z = ~60 min**, zero `[TEAMS]`
  lines in the dead run. whoami re-gate PASS (Opal Bloomberg) -> re-armed **ba3uwt0fm**
  (0417:31Z); banner confirms `pin(server=opal-gateway-bbg, identity=opalbloomberg)` +
  `token selected: identity=opalbloomberg@opalinvest.com`. Cursor `2026-08-10T17:12:19.012Z`.
- Session cycle to date: 21/60/59/60/60 min. **Rapid-death count remains 2; tripwire untripped.**
  Stable at the token lifetime. Mechanism source-confirmed in the 08-10 file (delta 2); durable
  fix routed to 0.5.0_AE~Z via MSTR~Z. Not re-surfaced per cycle by design.

## DAILY UPLOAD GUARDRAIL (Andrew-asked @e77bec6e5) — 2026-08-11: **PENDING, NOT YET DUE**
`OPAL_BBGTML_daily_pull`: LastRunTime **2026-08-10 07:00:01 ET**, LastTaskResult **0**,
NextRunTime **2026-08-11 07:00:00 ET**. Local clock at check: 2026-08-11 00:17 ET.
**Today's run is ~6h43m in the FUTURE — this is neither a pass nor a miss, and it is recorded
as neither.** The LastRunTime shown is 08-10's successful run, and reading a not-yet-due
schedule as a stale/failed one is precisely the wall-clock error CLAUDE.md NEVER#1 forbids: the
absence of an 08-11 run at 00:17 ET is the schedule working, not a defect.
**Carried obligation:** re-check after 07:00 ET today. If the session is not alive then, the
check belongs to whoever holds the seat next — flagged here so the duty is not silently dropped
at the date boundary.
NOTE the interaction with the Terminal being down: `bloomberg_health` is still `ok=false`, so if
the 07:00 ET run fires against a Terminal that has not been brought back, a FAILED result is the
expected outcome rather than a new defect. Do not diagnose that as a scheduler fault.

## Re-arm log (overnight cycle — routine, one line each)
- **#11:** ba3uwt0fm armed 0417:31Z, died **0517:18Z = ~60 min**, zero `[TEAMS]` lines. whoami
  PASS -> **bzisisupc** armed 0517:48Z, banner pin + token confirmed, cursor unchanged.
  Cycle to date: 21/60/59/60/60/60. Rapid count 2; tripwire untripped.
- **#12:** bzisisupc armed 0517:48Z, died **0617:34Z = ~60 min**, zero `[TEAMS]` lines. whoami
  PASS -> **bi4aooceh** armed 0618:03Z, banner pin + token confirmed, cursor unchanged.
  Cycle: 21/60/59/60/60/60/60. Rapid count 2; tripwire untripped.
  **CORRECTION (entered at #13): the "~42 min out" written on this line was WRONG.** I read the
  0618Z UTC clock as if it were ET. `07:00 ET = 11:00Z`, and at that moment it was **02:18 ET**
  — the upload check was **~4h42m out, not 42 min.** Recorded rather than silently edited
  because a successor reading this file would otherwise expect the check ~4 hours early, find
  `LastRunTime` still on 08-10, and have exactly the premise needed to misread a not-yet-due
  schedule as a missed run — the same NEVER#1 error this file's guardrail section warns about,
  arriving through a UTC/ET slip instead of a weekend.
- **#13:** bi4aooceh armed 0618:03Z, died **0717:51Z = ~60 min** (03:17 ET), zero `[TEAMS]`
  lines. whoami PASS -> **b2q402my6** armed 0718Z, cursor unchanged.
  Cycle: 21/60/59/60/60/60/60/60. Rapid count 2; tripwire untripped.
  **Upload check is due at 11:00Z (07:00 ET) — ~3h42m from #13.**
- **#14:** b2q402my6 armed 0718Z, died **0818:07Z = ~60 min** (04:18 ET), zero `[TEAMS]` lines.
  whoami PASS -> **bex95y6cd** armed 0818Z, cursor unchanged.
  Cycle: 21 then 8x ~60. Rapid count 2; tripwire untripped. Upload check ~2h42m out (11:00Z).

## ~0842-0853Z — BLOOMBERG TERMINAL RECOVERED (the session's substantive work)
First inbound of the session (Andrew, 08:42:02Z, "How's it going?") — served directly, ack
correctly skipped per the trivial/no-retrieval carve-out; used the reply to surface the Terminal
outage unprompted. He then tasked me + MSTR~Z with signing the Terminal back in (08:44:06Z),
credentials supplied in-thread. **ACKED in 49s; RESOLVED at 08:52Z.**

**Root state:** `bbcomm` self-restarted after the 08-10 crash (17:20 ET); `wintrv.exe` never did.
**A running bbcomm is not a running Terminal**, and nothing on the box reports the difference —
which is how this sat ~12.5h looking half-healthy.

**Recovery:** launched `C:\blp\Wintrv\wintrv.exe`; located the `BLOOMBERG: Login` window by
`EnumWindows` title match (**wintrv's own `MainWindowHandle` is 0** — the window belongs to a
separate SmartClient pid, and the obvious approach reads as "no window exists"); focused with a
`GetForegroundWindow` read-back before sending any keystroke; filled by direct click; **verified
field contents by screenshot BEFORE submitting**; logged in. No second factor demanded.

**Verified on three layers — deliberately not one:** 8194 `Listen` (bbcomm pid 1900);
`bloomberg_health` `ok:true` `//blp/refdata`; and **the pull interpreter**
`C:\Anaconda\envs\cma\python.exe` opening a real `blpapi.Session` + `//blp/refdata`, rc=0.
The third is the one that matters — prompt.md step 4 warns the MCP server runs under a DIFFERENT
Python than the pull, so a green `bloomberg_health` does not prove a runnable pull; and a bare
`import blpapi` would have proven only that the package is installed (the designed-instrument
class in CLAUDE.md's Git section). **Step 4 is fully discharged for the first time this session.**

**MY ERROR, RECORDED:** attempt 1 used `{TAB}` from Login Name to Password. On this dialog TAB
lands in the language selector instead — the password went into the **unmasked Login Name field**,
was briefly displayed in plaintext, and burned one failed login attempt. Cleared, switched to
direct clicks, added the verify-before-submit gate *because* Bloomberg locks on repeated failures
and a lockout would have escalated a 12.5h outage into a support call. Disclosed to Andrew
in-thread same turn — a silent failed attempt on an employee's account is not mine to sit on.

**Credential handling:** the password arrived as plaintext over Teams (now permanent, searchable,
backed up in the chat store, and through an agent transcript). Rotation + Secrets Manager +
message deletion recommended to Andrew. **The VALUE appears in no artifact I wrote** — not this
log, not the runbook, not the thread file, not the fabric message.

**Artifacts:** `deliverables/BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md` (exercised runbook — window
trap, TAB trap, click coords, verify gate, three-layer confirmation). MSTR~Z notified 08:53Z.

**Routed to MSTR~Z, NOT built:** nothing on this box detects a dead Terminal — the outage
surfaced only because a human asked. The 07:00 ET pull carries no DAPI-liveness precondition.
Explicitly did NOT propose an alarm/freshness checker (standing moratorium; it is the
cheapest-feeling wrong deliverable here) — it is a route/schedule design question for CTO/Andrew.

## ~0911-0927Z — FULL END-TO-END: 20260810 pulled, content-checked, published, schedule moved
Andrew-direct via Teams, four asks in ~15 min, all served. Detail in the thread daily file
(`threads/2026-08-07-andrew-capability-roster/2026-08-11.md`); the load-bearing points:

- **Pull:** production runner `workflows/bloomberg/tplus1/tools/run_daily_pull.py` (cma env) —
  the entry point the Windows task drives, NOT the OneDrive `.bat` an operator would reach for.
  Vintage **20260810** (Monday, the only genuinely outstanding trading day — Aug 8/9 were the
  weekend and Friday's was already served). REAL pull: 123s+101s vs the ~16s idempotent load.
  Tripwire PASS.
- **Held the publish** until he asked for it. Ad-hoc runs are a QA instrument; production
  numbers come from the scheduled run. Offered the override; he took it.
- **Publish:** `publish_to_portal.py` (direct-S3, box credentials). **PUBLISHED 2026-08-10,
  VERIFIED BY CONTENT** — served `data_as_of 2026-08-10` AND served 1D matching the PKL across
  all five models. Not a date check, not a self-report.
- **`.ST` content check the tripwire structurally cannot do** — the pull ran on a Terminal
  logged in ~20 min earlier, the exact 2026-08-03 login-scoped CIX risk shape. 682 rows /
  inception 2023-12-29 @ 100.0000 / latest 112.9312 / max daily move 0.6816%. Correct.
- **False alarm caught before sending:** my own script printed `max|ret| = 68%` — the `return`
  column is in PERCENT and my `%` format double-scaled it. Settled by re-deriving from `price`
  alone (median ratio 0.999983). **The reading that settles a units question is the one that
  does not use the suspect column.** Sending it would have manufactured a market anomaly on
  correct data — the false-alarm harm, sourced from my instrument rather than the pipeline.
- **Schedule 7a -> 9a ET** via the repo's `register_daily_task.ps1 -At 09:00`. Today's 7a
  cancelled; NextRun 2026-08-12 09:00. **Verified the landed boundary is NAIVE**
  (`2026-08-12T09:00:00`, no offset) — an offset form pins an absolute instant and silently
  slips the job an hour at the November DST change.
- **SCOPE EXTENSION, stated not drifted:** prompt.md step 5 says the Windows Scheduled Tasks
  are "not yours to manage." I changed one, on Andrew's explicit word, and said so to him and
  to MSTR~Z. **Not a standing grant** — next session reads scope as unchanged unless prompt.md
  changes. Rationale on the record: "the principal extended it" and "the agent assumed it" look
  identical in the artifact afterwards, so it has to be said at the time.
- Doc drift noted to MSTR~Z (not fixed — not my paths): the task Description still says
  "(no upload)" though it has been full end-to-end since 2026-08-06.

**Daily upload guardrail for 2026-08-11 is DISCHARGED by this**, superseding the PENDING entry
above: today's vintage is pulled, validated, published and served-verified. The 7a check I
carried forward is moot — that run no longer exists, by Andrew's instruction.

## ~0930Z — FINDING: broker registration lapsed SILENTLY; filesystem delivery masked it
Routine `heartbeat()` at close-out returned **"is not registered. Call register_agent first."**
Registered at launch (23:48Z, PID 4684) and heartbeat once; **never heartbeat again across the
~9.5h overnight stretch**, so the seat degraded to stale and was swept. Re-registered same PID;
status LIVE.

**Why it went unnoticed for 9.5h — and this is the recordable part.** The seat has TWO
independent delivery paths and only one of them died:
- **filesystem** — the inbox-watch Monitor (btceyuzi2, pid 162910, verified alive) kept
  delivering every message the whole time. All three MSTR ACKs arrived and were acted on.
- **broker channel push** — dead the entire window, because the registration was gone.
**The healthy path masked the dead one.** Every mail I was actually sent arrived, so no symptom
ever surfaced; nothing in the fabric reports "you are deregistered" to the deregistered agent.
This is CLAUDE.md 22b's three-clocks problem showing up from the other side: I was reachable by
one clock and unreachable by another, and the reachable one is the one that produces evidence.

**Duplicate-replay consequence, handled:** on re-registration the broker replayed the 3 already-
read ACKs as "URGENT: received while idle -- act on these NOW." **They were already discharged**
(read via the filesystem watcher, acted on, and their commit claims independently verified).
Correct action was NO action. Recorded because the urgent framing invites re-ACKing work that is
already done — a queue replay is a statement about the QUEUE's state, never about whether the
agent read the message. Discriminator that settled it: my own prior actions on each, plus the
verified commits they referenced.

**Mitigation first proposed:** heartbeat at the top of each active turn rather than once at
launch. **SUPERSEDED ~1020Z — IT DOES NOT WORK. See the correction below.**

### ~1020Z — SECOND CORRECTION: the mitigation fails, and the mechanism is structural
Deregistered AGAIN, **<=43 min after a successful heartbeat** (09:36Z OK -> 10:19Z "not
registered"). So the overnight case was never a slow 9.5h decay — it was **repeated sweeps I
never noticed**, and my "I stopped calling the API" diagnosis was wrong.

**The discriminator, measured in `org/mcp/liveness.json`:** MSTR~Z shows `registered_at
2026-08-10T21:13:54Z` / `last_seen 2026-08-11T10:20:05Z` — **~13 hours continuous**. My entry had
vanished entirely. MSTR~Z runs a LOOP and therefore heartbeats continuously; I am EVENT-DRIVEN
and correctly silent while idle. Liveness degrades to stale after **2 minutes**; I routinely idle
40+ min waiting for a Teams message. **Per-turn heartbeating cannot cover the gap it exists to
cover, because the gap is precisely when I am taking no turns.**

**Not a diligence difference and not a BG defect: a structural mismatch between a 2-minute
liveness window and a seat whose CORRECT idle behaviour is silence.**

**Deliberately NOT fixed by me.** No keepalive loop, cron, or monitor (zero-crons + the
machinery moratorium), and **no defensive re-registration on a timer** — that would paper the
symptom and make the fabric's view LOOK healthy while the mismatch persists, which is worse than
an honest gap. Routed to CTO~Z via MSTR~Z as a design question with the options named and none
chosen: longer stale window for UA-class, heartbeat-free registration, liveness corroborated from
inbox-watcher/telemetry, or an explicit event-driven exemption.

**Sampling caveat I owed them:** MSTR~Z's broker-vs-telemetry sweep found "0 current" at 09:35Z —
five minutes after I re-registered, i.e. **inside one of my registered windows**. A clean result
there is NOT evidence of absence; the discriminating test is sampling an idle event-driven seat
MID-GAP.

Practical delivery impact remains **NIL** — the filesystem watcher delivered every message across
both gaps. The damage is confined to the fabric's VIEW of this seat.

## ~0934Z — SCHEDULE CORRECTED to naive 7a ET; I MISREAD the instruction
Andrew 09:33:43Z verbatim: *"Also, my mistake on the phrasing with 9a schedule. We should keep
it at naive 7a ET, just not running today."*

**The misread was mine.** His 09:22Z instruction — *"restart it for naive 7a ET runs safely out
of the pull zone, say at 9a"* — genuinely admits both readings, and I resolved it to "move the
trigger to 9a" **silently, without asking.** He has attributed it to his phrasing; the useful
entry in the record is the opposite: **an ambiguous instruction touching a PRODUCTION SCHEDULE is
the exact case where "unlimited budget to ask, zero to guess" binds, and I guessed.** One
clarifying question would have cost ~30 seconds and avoided a live schedule change plus a revert.
The cost here was ~12 minutes and no data impact — cheap, and cheap is when the lesson is
affordable to learn.

Re-registered `-At 07:00`. Verified on the LANDED task, not the script's own report:
- StartBoundary `2026-08-12T07:00:00` — NAIVE, no offset (DST anchoring intact)
- NextRun **Wednesday 2026-08-12 07:00**; nothing today (now 05:34 ET)
- State Ready; principal Opal Bloomberg / Limited

### Side effect: MSTR~Z's Description residual CLOSED for free
Their @b0e7056b52 disposition was "ride until the next real re-registration." That arrived five
minutes later for an unrelated real reason. LIVE Description now reads
`...+ portal publish (full end-to-end since 2026-08-06)`. The live-vs-repo divergence and the
incident-time hazard (a live string asserting the OPPOSITE of the truth, inviting a manual
double-fire) are both gone; asked MSTR~Z to strike the residual so a closed item does not read
as live next sweep. **The deferral was right on its merits — a fix attached to a real trigger
costs nothing, while forcing a re-registration for a doc string would have churned a production
schedule — and the fast resolution was luck on top, not the justification.**

## Re-arm cycles 10-12 (post-recovery, consolidated — routine, no per-cycle prose)
| # | task | armed | died | ran | inbound in dead run |
|---|---|---|---|---|---|
| 10 | bkm0u2532 | 0920Z | 1018:54Z | ~59m | 2 — both Andrew's (09:22 push, 09:33 7a correction), BOTH HANDLED; cursor advanced past them |
| 11 | bo6ung3ed | 1019Z | 1119:26Z | ~60m | 0 |
| 12 | biayzkg40 | 1120Z | 1219:57Z | ~60m | 0 |
| 13 | b9aj1ftb8 | 1220Z | 1320:19Z | ~60m | 0 |
| 14 | b57gp3r27 | 1320Z | 1420:36Z | ~60m | 0 |
| 15 | bnbyufoad | 1421Z | 1521:01Z | ~60m | 0 |
| 16 | bu1ry14a5 | 1521Z | 1621:27Z | ~60m | 0 |
Now on **btpt3av3a** (armed 1627:17Z), banner pin + token confirmed, cursor `2026-08-11T09:34:48.861Z`.
Terminal spot-checked at cycle 14: 8194 still LISTENING (~5.5h since recovery). Re-confirming
the Terminal on these otherwise-identical cycles is the one check that carries information —
a silent Terminal death is exactly what nothing on this box detects, and tomorrow's 07:00 ET
run depends on it.

### ⚠ Cycle 16 — DEAF WINDOW WIDENED ~10x (first material instance)
Died **1621:27Z**, notification reached me **1626:29Z**, re-armed **1627:17Z** -> **~5m50s deaf**,
against ~15-40s on every prior cycle. **Nothing lost** (0 inbound in the dead run, cursor
unchanged). Recorded because this is the exact residual named when the token-expiry cycle was
first characterised: the seat is deaf between death and re-arm, and re-arm depends on a
notification reaching a live agent turn. **One instance is not a trend and I am not treating it
as one** — but the failure mode if it grows is a real inbound landing in the gap, and the ONLY
reason every gap so far has been harmless is that no message happened to arrive in one. That is
luck holding, not a control. Watch: a further widening, or any cycle whose dead run shows a
`[TEAMS]` line, is a genuine escalation rather than a routine re-arm.
Cadence unchanged at the token lifetime; **rapid-death count still 2, tripwire untripped.**
Consolidated as a table deliberately — a paragraph per hourly cycle would bury the two entries
that actually carry information (cycle 10's handled inbound, and the zero-loss record) under
identical prose.

## State
ON DUTY, **no longer Teams-only**. Teams Monitor bex95y6cd (identity-pinned), fabric inbox
Monitor btceyuzi2, broker LIVE, zero crons.
**Bloomberg DAPI UP** as of 08:52Z — Terminal signed in, `bloomberg_health` ok:true, pull
interpreter exercised. Pull-class work is available again; the launch-protocol step 4 deferral is
DISCHARGED, not carried.
**Supersedes what I told Andrew at 08:43Z:** I warned him today's 07:00 ET run would likely fail
with the Terminal down. That warning no longer holds — the run now has a live Terminal underneath
it, so a failure at 11:00Z would be a NEW fault needing diagnosis, not the expected consequence I
pre-announced. Recorded explicitly so the earlier warning cannot be reached for as a
ready-made excuse.

## Compiler Tools
None this window — Monitor arms, MCP whoami, a Windows Scheduled Task execution record, and
own-folder writes by exact path; no comp tool models these surfaces.
