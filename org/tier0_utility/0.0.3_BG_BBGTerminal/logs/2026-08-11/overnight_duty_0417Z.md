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
