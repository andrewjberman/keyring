# 0.0.3_BG_BBGTerminal -- second launch today; a stale-cursor REPLAY put a false apology in front of the principal -- 2026-08-25 ~2032-2055Z

**Date:** 2026-08-25
**Task Order:** ad-hoc -- launch sequence + Teams concierge serve
**Status:** COMPLETE -- launch gates green; one self-inflicted error, corrected in-thread same minute; two findings routed
**archetype:** SERVE + VALIDATE

Second session on this box today (prior seat 1445-1455Z discharged the daily guardrail green).
Launched ~20:32Z via ajb. The guardrail was NOT re-run as a full pass -- it was discharged
5h45m earlier and the next scheduled fire is 2026-08-26 07:00 ET; I re-read the OS execution
records only (below), which is the proportionate check for a same-day relaunch.

## VERDICT: every launch gate passed. The one defect found today was in MY OWN reply, not in the
## pipeline: I apologised to Andrew for a 5-day delay on three messages that had been served on
## 08-20, because the Teams monitor replayed them off a cursor home 3 days behind. He said "No
## need thanks"; I corrected it in one block and stopped. Nothing was owed and nothing new served.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | comp-which "how do I grep the repo" | PASS | XXX.md A.3 mandatory EXERCISE half -- scored on OUTPUT (its own banner), not rc. Resolution is not execution. |
| A.3 denominator probe | for-loop over .tools/comp-* | PASS | **98 of 102** resolve bare. Unchanged from 08-24 and 08-25 AM. A denominator, never a boolean. |
| to-check | python .tools/to-check.py --all --assignee 0.0.3_BG_BBGTerminal | 2 TOs | --all carried, never trimmed. Both named-but-held by other seats (Blockers). |

No raw repo grep was needed. Every read was a known path, a comp-tool, or a source file I
opened deliberately to ground a claim (teams-watch.py, audit-archive-invoker.py, bg-concierge-gate.sh).

## Launch gates (prompt.md On-Launch, which supersedes XXX.md for this seat)

| Gate | Result |
|---|---|
| 1. register_agent | Was NOT REGISTERED (expected). Registered, PID 32524. |
| 2. /watcher orphan sweep | ps -ef for inbox-watch.sh -> **zero** matches. Nothing to adjudicate; the clean case, not the ambiguous one. I killed nothing. |
| 2. Inbox Monitor | Armed task bvcnhisup; TaskOutput -> running (the only probe that observes a CONSUMER). Path built from git rev-parse --show-toplevel plus a measured /cygdrive/c -- **not** the AndrewBerman literal the skill doc still carries, which does not exist on this box. |
| Inbox (both probes) | check-inbox top-level empty; get_agent_status no channel messages; newest read/ entry 20260824T234442Z predates the prior session. Nothing unhandled. |
| **2a. Identity acceptance gate** | **PASS** -- whoami on opal-gateway-bbg -> Opal Bloomberg / opalbloomberg@opalinvest.com. Not Andrew. Re-confirmed by from.displayName on both sends. |
| 3. Teams Monitor | Armed task be1kzrz6y, **both pin halves read off the task output file**: pin(server=opal-gateway-bbg, identity=opalbloomberg) AND token selected: identity=opalbloomberg@opalinvest.com, plus channels=1 watched (Opal Client Tickets). A returned task id is not that evidence. |
| 4. bloomberg_health | PASS -- ok:true, //blp/refdata, 127.0.0.1:8194 |
| 4. cma interpreter | **EXERCISED** -- C:\Anaconda\envs\cma\python.exe 3.13.2, blpapi 3.26.4.2, pandas 2.2.3 imported. Green MCP is not a runnable pull, so both were checked. |
| 5. Crons | CronList -> none. Zero is the correct end state for a Tier-0 UA. |
| XXX.md A.1 serial file | Not written BY ME, and correctly so: ajb.ps1 had already written both .serial and .launch-path at 20:32:20Z. bg-concierge-gate:130 states the design in words -- "never write the serial from this seat (G1)". My first attempt tripped G2 before I read that; the fence was right and I stopped. |

**Scheduled tasks (records read, not inferred):** all six OPAL_* tasks LastTaskResult 0.
OPAL_BBGTML_daily_pull last 2026-08-25 07:00:01 ET, next 08-26 07:00. OPAL_BLOOMBERG-FreezeTripwire
had fired ~60s before I looked. No SCHEDULE-GAP.

---

## The serve -- and my error in it

Three [TEAMS] lines landed at arm, framed (1 of 3)/(2 of 3)/(3 of 3), all from Andrew, all
dated 2026-08-20. I ran the ACK-FIRST rule and sent a receipt at 20:43:15Z -- **and put a claim
in it**: that they had "been sitting since the 20th". Then RECALL (step 2) opened the thread file
and showed all three SERVED on 08-20. He replied **"No need thanks"** at 20:43:51Z. I sent one
correction at 20:44:43Z and stopped.

**F2 -- the error is mine and the rule was not at fault.** The skill's ack norms are explicit
that a receipt is content-neutral and carries no outcome. RECALL is step 2 precisely so the ack
does not have to know anything. I used the receipt slot to assert a five-day delay I had not
checked, and the check was one file read away in the very next step. A bare "Got it, let me look
into that" would have cost nothing and been retracted by nothing.
**The durable form: an ACK may state that a message was RECEIVED. It may not state anything
about that message's HISTORY -- that is what the step after it is for.**

## F1 -- teams-watch cursor home is TMPDIR-dependent, and the two homes diverged

teams-watch.py:98 -- CURSOR_FILE = os.path.join(os.environ.get("TMPDIR", "/tmp"), "teams-watch.cursor").
Under native Windows Python 3.11 an UNSET TMPDIR resolves /tmp to C:\tmp; a SET TMPDIR puts it
elsewhere. Both homes exist here and had drifted apart:

| home | value at my arm | mtime |
|---|---|---|
| C:\tmp\teams-watch.cursor (TMPDIR unset) | 2026-08-18T17:54:21.641Z | Aug 18 |
| %LOCALAPPDATA%\Temp\teams-watch.cursor (TMPDIR set) | 2026-08-21T22:01:07.014Z | Aug 24 |

My shell had TMPDIR unset, so the arm used the home **3 days behind** and re-emitted everything
after 08-18. The banner is the proof of which was selected.

**Why the 08-20 session did not catch it:** it verified its cursor before AND after at
2026-08-20T18:06:09.908Z -- a TRUE reading **of the other home**. Two carriers of one piece of
state, no named primary, each session silently selecting by environment. The 08-18 log had
already flagged "two stale decoy copies" and pinned C:\tmp as the LIVE one; C:\tmp is now the
STALE one. **Which file is "live" is not a property of the file.**

Replay remains the safe direction for LOSS (CTO~Z's 08-20 ruling, which I still agree with). It
is not safe when the duplicate arrives wearing an apology. Routed with a note that a cursor able
to move BACKWARD across sessions is a distinct property from picking one path.

**Owner 0.5.0_AE_OpalETL~Z; I attempted nothing** -- G1 fences this seat out of .claude/** by
construction, and that is correct.

## A5 -- NOT satisfied. The interim re-send rule STANDS.

Today's three lines arrived complete, oldest-first, with the per-chat denominator: the fixed
engine's exact contract. **It is still not the A5 live positive.** A5 is Andrew's next real
two-in-a-row exchange; this was a stale-cursor replay of history. A control produced by a defect
is no better than one I manufacture myself, and the thread record explicitly forbids the
manufactured kind. S1 stays ACCEPTED-PENDING-LIVE-POSITIVE.

## Findings routed

| # | Finding | To | Receipt |
|---|---|---|---|
| F1 | teams-watch cursor home TMPDIR-dependent; two homes diverged; replayed served mail at the principal | 0.5.0_AE_OpalETL~Z (owner), 1.0.0_SA_CTO~Z (gate), 0.0.0_AB_MSTR~Z | ids 9093/9094/9095 -- **3 QUEUED / 0 REFUSED** (denominator 3). QUEUED is written-and-waiting, not delivered. |
| F3 | audit-archive-invoker compares site-Z live logs against the LAPTOP baseline -- 18 findings that read as tamper evidence | 3.0.0_SA_CVO~Z (surprise channel), 0.7.0_AE_CloudOps~Z (owner), 1.0.0_SA_CTO~Z (gate) | ids 9096/9097/9098 -- **3 QUEUED / 0 REFUSED** (denominator 3) |

**F3 detail:** chain_root() (audit-archive-invoker.py:99-116) falls back to the legacy flat root
when no archive/<DEVICE>/ exists, and its own docstring says that root **is the laptop chain**.
No device subdirs exist here (migration pending, :405), and detection is deliberately left
running against it (:398). Discriminating evidence: baseline actors are 100% BARE serials
(2.0.0_SA_COO, 1.0.0_SA_CTO, 0.4.0_DS_ClientPlatform_B...), live actors are 100% ~Z-suffixed
across 2,283 lines -- **zero overlap**. Two devices' logs diffed as one file. Not tampering.
No alarm/monitor/gate proposed (standing moratorium).

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Sent a correction after he said "No need thanks" | He declined the RESEARCH; my correction addressed something else -- that his mail had NOT been sitting unread. In the same thread where he found real message loss five days ago, leaving him with my false version was worse than one 3-sentence block. |
| Did NOT re-run the full daily guardrail | Discharged green 5h45m earlier this same day; next fire tomorrow 07:00 ET. I read the OS execution records (all rc=0, current) rather than re-performing a pass whose inputs cannot have moved. Re-running would have re-reported the morning's evidence as if it were new. |
| Did NOT claim A5 | The emit met the contract, but a replay is not his live exchange. |
| Did NOT attempt the memory-file write | .claude/** is fenced from this seat (confirmed 08-21). F2 lives in this log instead; a durable cross-session memory is MSTR~Z's write, not mine. |
| Did NOT chase the cursor fix | teams-watch.py is AE~Z's and sits under .claude/. Surfaced with mechanism plus a design note; implementing it would be routing around the fence. |
| Did NOT act on either open TO | D7 WD-SITEZ BG half still held on the CTO~Z/AE~Z disagreement; D6 TO-CDBFG-SITEZ pending at MSTR~Z-assigned seats. Neither is mine to adjudicate. Unchanged from this morning. |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| threads/2026-08-07-andrew-capability-roster/2026-08-25.md | today's serve + F1/F2 record | **No -- local only** |
| threads/2026-08-07-andrew-capability-roster/THREAD.md | Day index entry | **No -- local only** |
| logs/2026-08-25/startup_and_teams_cursor_replay_2032-2055Z.md | this log | **No -- local only** |

My G1 fence denies git entirely; 0.0.0_AB_MSTR~Z is the named integrator and sweeps this folder
(OPAL_ANALYST.TO5). No repo content, no cloud mutation, no git act.

**Tooling note worth carrying:** a python heredoc had C:\tmp reach python as a real TAB -- the
shell layer unescapes before python's string parser runs, so a QUOTED heredoc and a doubled
backslash BOTH failed to protect it. The plain file-write heredoc preserved backslashes
correctly. Caught by reading the written file back; repaired via chr(92). **The hazard is the
NESTED interpreter, not the heredoc.** Separately, a heredoc body containing a literal
here-doc-operator token broke the outer shell parse outright -- split the write instead.

## Blockers

None of mine. Two TOs name me, both held by other seats' open questions.

## Next Steps

1. **Available.** Teams concierge live (be1kzrz6y, identity-pinned), fabric inbox live
   (bvcnhisup), broker LIVE, zero crons. Next scheduled Bloomberg fire 2026-08-26 07:00 ET.
2. **[0.5.0_AE_OpalETL~Z]** F1 -- one cursor home, and consider a monotonic guard so a cursor
   cannot move backward across sessions.
3. **[0.0.0_AB_MSTR~Z]** sweep + commit this log and the two thread files -- local until then.
4. **[whoever spawns next here]** the cursor divergence is UNFIXED. If you arm the Teams monitor
   with a different TMPDIR than this session, expect another replay. Check the arm banner's
   cursor= value against BOTH homes before believing a backlog is real.
5. **[unchanged, Andrew's call]** the one-time message-grain backfill question stays open and was
   not re-raised today.

**Second tooling note:** a closing heartbeat() after a quiet gap returned "is not registered" --
the call PRUNES the stale liveness entry and then reports the absence it just created. Known
banked hazard; re-registered same PID (32524), no identity conflict. Do not read that string as
evidence the seat was never registered.

**F1 sharpened after the first routing (ids 9099/9100):** off the live process argv, the harness
wrapper exports TEMP and TMP but NOT TMPDIR, while teams-watch.py:98 reads TMPDIR specifically.
The environment does name a temp dir; the code reads a different name for it. That is why the
split is SYSTEMATIC, not occasional -- and it means "export TMPDIR in the arm line" is NOT the
fix: the D7 intake runner imports the same engine from a Windows Scheduled Task, a third
environment again. Routed as: resolve the state dir from something that cannot vary by launcher,
and separately add a monotonic guard so a cursor can never be seeded EARLIER than one on disk.

---

## ANDREW-DIRECT received 2026-08-25T21:10:05.427Z (after the body of this log was written)

**VERBATIM:** "Ok tell MSTR he needs to adjust your startup/operating tenets to account for this
kind of thing."

Teams 1:1, Opal Bloomberg account via opal-gateway-bbg; trailing &nbsp; in the raw body is markup.
Recorded + broadcast the same turn per XXX.md. Addressed to 0.0.0_AB_MSTR~Z; CTO~Z + COO~Z copied
so latest+most-restrictive has something to bind on. ids 9101/9102/9103 -- **3 QUEUED / 0 REFUSED**
(denominator 3); MSTR~Z was dark, and I reported it to him as QUEUED rather than as delivered.

**I did not adjudicate scope.** "This kind of thing" may mean the specific replay defect, the
class, or both; that is his and MSTR's call. What I carried upward, explicitly as recommendation
and not ruling: (a) an ACK states RECEIPT, never a message's HISTORY; (b) a monitor emit is a
delivery event, never evidence a message is unanswered -- thread memory decides what is owed;
(c) both would have to land in prompt.md/refs/, which G1 makes unwritable from this seat, which is
why the instruction went to MSTR rather than to me.

**Why this matters beyond the one incident:** F1 (the cursor mechanism) and F2 (my conduct) are
separable, and **a code fix reaches only F1**. Had the cursor been correct today I would still
have been an ack away from asserting an unverified history. That is the half his instruction is
pointed at, and the half only a tenet closes.

**Added to Next Steps by this event:**
6. **[0.0.0_AB_MSTR~Z -- ADDRESSED, and the only seat that can act]** the Andrew-direct tenet
   adjustment above. QUEUED at id 9101 while MSTR~Z was dark; Andrew was told it is queued, not
   delivered. I adopted the behaviour immediately as standing instruction 4 in the Andrew thread
   (the same behaviourally-adopt-then-route split rule 1 of that file already used for the
   comms-length ruling), but the DURABLE tenet lives in prompt.md/refs/ and only MSTR~Z can write it.
