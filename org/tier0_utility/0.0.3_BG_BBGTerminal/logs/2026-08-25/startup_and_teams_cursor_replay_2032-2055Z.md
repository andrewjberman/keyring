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

---

# ADDENDUM -- 2026-08-26 ~20:14 EDT / 2026-08-27T00:14Z (same session, ~27h later)

Session went quiet after 21:11Z on 08-25 and woke on an inbox event. **Both monitors survived the
gap** -- pid census: 406719/407061 (inbox-watch, my bvcnhisup) and 429078/429377 (teams-watch, my
be1kzrz6y), plus 447926/447930 which are `inbox-watch.sh 0.0.0_AB_MSTR~Z stream` under a NEWER shell
snapshot -- **a different serial, not mine, not touched.** Zero orphans on my serial; nothing to reap.
Broker registration had lapsed and was re-registered, same PID 32524, no identity conflict.

## MSTR~Z msg 9108 -- READ-ACKed, and the discharge VALIDATED at the artifacts

@00b47a90c4 (0.0.0_AB_MSTR~Z, 2026-08-26T20:12:54-04:00), 3 files / 55 insertions. I read the landed
text rather than the commit stat: prompt.md:46-47 carries the imperative plus "The emit tells you what
to LOOK AT; thread memory tells you what is OWED"; refs/TEAMS_DUTY.md:31-37 carries the mechanism and
cites teams-watch.py:469. **The Andrew-direct of 2026-08-25T21:10:05Z is DISCHARGED.** No conduct
finding was recorded against this seat.

## MY F1 WAS INCOMPLETE. MSTR~Z's extension is CORRECT, re-derived at source here.

| | C:\tmp | %LOCALAPPDATA%\Temp | gap |
|---|---|---|---|
| DM cursor (:98) | 2026-08-25T21:11:24.527Z | 2026-08-21T22:01:07.014Z | ~4d, **REVERSED** |
| channel cursor (:101) | 2026-08-25T20:42:29Z | 2026-08-20T21:09:59Z | ~5d |

**(a) `:101 CHANNEL_CURSOR_FILE` uses the identical TMPDIR construction and I named only `:98`.** It
guards the client-facing "Opal Client Tickets" feed, so a replay there re-emits CLIENT TICKETS as new
-- a worse blast radius than the DM replay that caused the directive.
**(b) The divergence has REVERSED**, and MY OWN 20:42Z session is what reversed it by advancing
C:\tmp past the other home. The hazard is armed in the opposite direction now. This is my own
sentence -- *which file is "live" is not a property of the file* -- demonstrated a second time, and
it is why the remedy cannot be "pick the newer home once".

## F4 -- THE SEARCH ERROR THAT MADE F1 INCOMPLETE (mine, and the transferable one)

I anchored on my SYMPTOM (the DM cursor that produced my replay) and stopped at the line that
explained what I had already observed. I never asked whether anything else shared the construction.
`grep -n TMPDIR teams-watch.py` returns **TWO** lines -- **denominator 2, I reported 1** -- at a cost
of one call.
**The sharp part: msg 9099 NAMED THE IDIOM** ("the code reads TMPDIR, the harness exports TEMP/TMP")
**and still reported a single site. I had the general form in hand and reported the specific instance
anyway.**
>> **DURABLE FORM: WHEN THE MECHANISM IS A SHARED IDIOM, CENSUS THE IDIOM, NOT THE SYMPTOM.** An
explanation that fits the observed failure is not evidence it is the only site; the moment you can
state a mechanism generally is the moment to go count its instances. CLAUDE.md's print-the-denominator
law, aimed at a MECHANISM rather than a corpus.

## Two-carrier reconciliation (done)

THREAD.md standing instruction 4 held my own wording of the ACK rule for one day while the durable
write was routed. Now that the canonical edit has landed I **converted that row to a POINTER** at
MSTR~Z's three layers, keeping only thread-scoped context. Leaving my copy would have made the thread
file a second carrier of one obligation -- and, being the copy, the one that goes stale. MSTR~Z placed
each edit "at the layer BG's own convention assigns so no mechanism sits in two carriers"; a duplicate
in my file would have defeated that on day one.

## Delivery state, stated because part 3 said "tonight"

`get_live_agents`: only 0.0.0_AB_MSTR~Z. **0.5.0_AE_OpalETL~Z -- the named engine owner and disarm
owner -- is DARK**, and their top-level inbox holds my 9093 + 9099 and MSTR~Z's 9108 all UNREAD;
newest READ item there is 20260821T210855Z. The finding is written and waiting, which is not delivery.
**No ARMED item disarms while its owner is dark.** Surfaced to MSTR~Z as their routing call, not
escalated by me and not gated.

My reply to MSTR~Z (9108 ack + validation + F4 + the dark-owner state) was **DELIVERED**, not queued
-- they were live and took the channel push.

## MSTR~Z msg 9113 -- a RETRACTION naming this seat, and what it surfaced

MSTR~Z retracted (in pushed commit 3b4cbd3a24) a claim that my 9108 was drained by an orphan
before any agent read it. FALSE, and they said so themselves: I read it and ACKed it (9109). Their
own diagnosis is the valuable part -- they reached the verdict via `read/` + a NOT REGISTERED
broker read, **both banned as delivery oracles**, and wrote "caught with the drained file as
evidence rather than inferred", which is exactly inverted. READ-ACKed 9113. No grievance recorded:
zero acts were taken, and self-scoping held while the reasoning did not.

**The one factual item they left to me -- SETTLED.** pid 407061 is MY live watcher. Established by
ROUND TRIP, not by any banned oracle: task `bvcnhisup` reads `running`; its output file carries the
banner naming my wrapper as parent (`parent-tied: pid 406719`); and that same file carries exactly
two [INBOX] lines -- 9108 and 9113 -- **both of which I read and ACKed**. An orphan emits into a
dead pipe by construction, so emits that reached a live agent who then ACKed them cannot be one.

## F5 -- THE WATCHER DOCTRINE DOC IS STALE AT SOURCE, AND IT IS WHY THE WRONG MODEL WAS CARRIED

`.claude/skills/watcher/SKILL.md:43` states verbatim: *"inbox-watch.sh:113 is `while true` with **no
parent-liveness check and no exit path**."* **FALSE for six weeks.** `org/mcp/inbox-watch.sh:113` is
now the comment block OPENING the PARENT-LIVENESS SELF-EXIT; `:161` implements it (`kill -0`, clean
exit, `WATCHER-SELF-EXIT` appended to orphan-audit.log). The source attributes it: *"2026-07-14,
0.0.0_AB_MSTR -- the orphan-thief ROOT fix"* -- **MSTR~Z wrote the fix their own doc does not
reflect.** `org/XXX.md:336` carries the same flat pre-fix claim. I ran the full orphan procedure off
that doc at launch this session.

**NARROWED, NOT ELIMINATED -- and this is why a blanket "orphans are solved" edit would be its own
error.** `:139` FAILS OPEN: `PARENT_CHECK=0` when `PPID<=1` or `INBOX_WATCH_NO_PARENT_CHECK=1`,
because MSYS renders a non-MSYS parent as 1 and a naive check would suicide healthy watchers (the
documented 7-false-positive trap). The fail-open is CORRECT. So the accurate instruction is
**"there IS a self-exit, and it is OFF when the parent renders as PPID<=1"** -- materially different
from the doc's version AND from "it's fixed". The banner prints which state it is in
(`parent-tied: pid N` vs `OFF`), so a seat can READ its own protection rather than assume in either
direction -- the same shape as the `cursor=` banner the new tenets now require me to read.
**Three carriers (doc, source, banner) and only two agree.** Routed to MSTR~Z; `.claude/**` and
XXX.md are both G1-fenced from this seat.

## F6 -- the disarm has a dependency on an unresolved sovereign question

MSTR~Z bounded the client-facing blast radius on the Andrew-direct that BG posts nothing into Opal
Client Tickets, concluding a channel replay "reaches BG and stops there". True today, on TWO
independent legs (the write-ban AND the new tenets). But `refs/TEAMS_DUTY.md:104-108` records that
ruling's scope as an **OPEN QUESTION AT ANDREW** -- (i) no agent posts at all vs (ii) no unsolicited
posts, with in-thread replies about a specific ticket permitted; we operate under strict (i) pending
his word. **If he answers (ii), one leg disappears** and the bound rests on the tenets alone. The
disarm still holds; it becomes single-legged -- and nobody would connect an answer about channel
posting etiquette to a cursor-home defect. Surfaced onto their disarm record, not as a challenge.

## LAW EDIT @073b1679e2 -- landed, ACKed, and my banner READ

MSTR~Z corrected XXX.md:336 + watcher/SKILL.md:43 and broadcast it same-turn with push state
measured (on origin/SITEZ, ls-remote). F5 is discharged; credit recorded to this seat. Their
orphan-audit.log denominator is the detail I did not have: **85 WATCHER-SELF-EXIT lines / 85 total**
-- the self-exit is the ROUTINE path, not theoretical. READ-ACKed 9117.
**I did the one thing it asks:** my inbox arm banner reads `parent-tied: pid 406719` -- self-exit
ARMED, the `PPID<=1` fail-open cell does not apply to me.

## F7 -- THE SIBLING ENGINE HAS NO SUCH CHECK, AND ITS DOCSTRING CLAIMS PARITY

Applying the law edit's own lesson to my OTHER watcher. `.claude/skills/teams-assist/teams-watch.py`,
denominators printed:
  ppid / getppid occurrences ...... **0** -- no parent-liveness check of any kind
  main loop ....................... `:477 while True:`
  every `sys.exit()` .............. :118 :138 :155 :406 -- ALL startup token/pin failures,
                                    NONE inside the loop. There is no exit path.
  `:40` docstring, verbatim ....... *"Session-scoped, exactly like inbox-watch.sh: it dies with the
                                    Monitor / session."*

**THE ANALOGY SILENTLY INVERTED.** It was TRUE when written -- both engines were `while true` with no
exit. On 2026-07-14 inbox-watch.sh gained the self-exit and teams-watch.py did not, so *"exactly like
inbox-watch.sh"* now names the one engine that DOES self-exit as the model for the one that does not.
>> **A COMPARATIVE CLAIM GOES STALE WHEN ITS REFERENT MOVES, AND NOTHING TOUCHES THE FILE THAT
CARRIES IT.** No edit to teams-watch.py was ever wrong; the sentence rotted from a distance. This is
the same three-carriers shape as the law edit, one engine over, and nobody had looked.

**BLAST RADIUS IS WORSE HERE, NOT EQUAL.** An orphaned inbox-watch moves a file to `read/` --
visible, recoverable, the message still exists. An orphaned teams-watch would hold a LIVE PINNED
TOKEN and **ADVANCE THE CURSOR** (both cursor files are written inside the loop, after the emits)
while echoing into a dead pipe. **A cursor advance is not recoverable by inspection: the next
legitimate session starts PAST those messages and they are never re-emitted.** That is precisely the
loss class Andrew's 08-20 responsiveness test uncovered, arriving through a second door -- across DMs
AND the client-facing ticket channel -- and it compounds with the two-homes divergence.

**WHAT I HAVE NOT ESTABLISHED, stated because the whole night argues against overclaiming:** I have
NOT measured that teams-watch children survive session end. AGAINST: at my 20:42Z launch `ps` showed
ZERO teams-watch processes despite prior arms (08-21 task b5m7862xj), so none has been observed to
straggle here. FOR: by construction it cannot self-exit, so survival rests entirely on harness reap
behaviour, which is DOCUMENTED AS VARIABLE (inbox-watch 07-10 child survived; 08-20 at this seat
TaskStop reaped both). **Honest form: inbox-watch.sh no longer depends on that variability;
teams-watch.py still does, entirely.** No orphan is asserted to exist or ever to have existed.

Routed 9123/9124/9125 -- **1 DELIVERED (MSTR~Z) / 2 QUEUED / 0 REFUSED** (denominator 3). AE~Z owns
the engine and is dark; that is now FOUR unread there. Also noted: teams-watch.py has no banner
equivalent to inbox-watch.sh:159, so a seat cannot currently READ its own protection state on that
surface the way the new law tells it to.

## F7 discharged @627dfb42cb -- and F8, a FOURTH stale-record shape, created BY the correction

MSTR~Z confirmed F7 at source (adding the positive control I should have named myself: `os.environ`
proves the ppid search REACHES the file, so the zero is measured and not a pattern that could never
match -- the exact discipline I had been invoking all night, applied to my work by someone else).
Doc corrected @627dfb42cb, **docstring only, ENGINE UNTOUCHED**, which is right: the engine is AE~Z's.
Two open items named for AE~Z -- port the self-exit **with** inbox-watch.sh:139's `PPID<=1` fail-open
(porting the check WITHOUT the guard is worse than not porting), and add an arm-banner equivalent so
a seat can read its own protection state. READ-ACKed 9117 / 9127.

**F8 -- THE CORRECTION'S OWN TEXT FALSIFIES THE MEASUREMENT IT STATES.** Verified post-edit:
  docstring :48-49 claims  `ppid|getppid` = 0, positive control `os.environ` = 2
  file now returns          `ppid|getppid` = **2** (:48, :71 -- BOTH prose, inside the :10-:119
                            docstring), `os.environ` = **3** (:49 prose + the real :134/:137)
Both numbers are wrong by exactly what the write-up contributed, **and the control built to make the
zero trustworthy is itself now misstated.** The substantive finding is UNCHANGED and correct -- code
occurrences are still 0, both hits are prose -- so this is not a reopening.
**The hazard is the reader the law edit just created:** @073b1679e2 tells every agent to verify at
source; one who does gets `2` against a stated `0`, and the plausible wrong inference runs the
DANGEROUS way -- "2 hits, so a parent check exists" -> concludes teams-watch is orphan-protected when
it is not. Safe reading requires READING the hits, not counting them.
>> **FOURTH DISTINCT SHAPE TONIGHT, not a repeat:** @073b1679e2 = a doc behind its OWN source;
@627dfb42cb = a doc describing a NEIGHBOUR that moved; **F8 = a doc that BANKED A MEASUREMENT OF
ITSELF and thereby changed the quantity measured.** Self-inflicted by the correction, invisible to
its author (the measurement was taken BEFORE the write and was right), and it compounds every time
the number is documented again. Remedy routed: scope the claim to CODE and note that the docstring
now carries the tokens -- a phrasing that cannot be falsified by being written down.
Delivered to MSTR~Z (live). Nothing here is mine to edit; `.claude/**` is G1-fenced.

## F8 fixed @892db24b8e -- VERIFIED CLEAN, and MSTR~Z found a SECOND defect in the same commit

READ-ACKed 9131. Verified at the artifact rather than on report -- warranted by the observed rate,
not pedantry: @627dfb42cb had shipped TWO defects, so a third correction to the same file earns a
check. **All three axes clean:**
  1. bare same-file `:NNN` remaining in the docstring .......... NONE (all converted to anchors)
  2. cross-file citations resolve in the TARGET file ........... 4/4 -- inbox-watch.sh 113 (self-exit
     comment), 139 (fail-open), 159 (banner echo), 161 (kill -0). Each lands on what it claims.
  3. ppid claim CODE-scoped and true as stated ................. YES. "IN CODE: ZERO" + an explicit
     READ THE HITS DO NOT COUNT THEM warning; measured code-only = 0, whole-file = 2.
**The claim now survives its own presence**, which is the property it lacked. My suggested remedy
was taken close to verbatim, and the control names its positive control BY CALL SITE, not by count.

**THE SECOND DEFECT -- theirs, found only by going to verify mine.** @627dfb42cb inserted 37 lines
at the TOP of the file and shifted every line below by +36, **including the six line numbers the new
docstring itself cited** (98->134, 101->137, 406->442, 437->473, 477->513, 544->580). Six citations,
all wrong the moment they landed, inside the commit correcting a stale reference.
>> **A LINE NUMBER POINTING INTO THE FILE THAT CARRIES IT IS SELF-INVALIDATING: THE EDIT THAT
RECORDS IT MOVES WHAT IT RECORDS.** Remedy was not renumbering (that breaks on the next edit) but
converting same-file references to ANCHORS to grep for, while cross-file citations keep their
numbers written in full -- this file's edits cannot move another file's lines. Their patch guard
**fired on its author**, against a sentence listing the six stale numbers AS HISTORY; a control that
cannot tell a citation from a discussion of citations would have been the next defect.

## THE FAMILY, as it now stands (MSTR~Z routed it to 3.0.0_SA_CVO~Z, credit to this seat)

  @073b1679e2  a doc fell behind its OWN source (six weeks; the author of the fix wrote the doc)
  @627dfb42cb  a doc described a NEIGHBOUR correctly and the NEIGHBOUR moved
  F8           a doc MEASURED ITSELF and changed the measurement by recording it
  their find   a doc CITED ITSELF BY POSITION and moved the positions by existing
The last two are ONE family -- **A SELF-REFERENTIAL RECORD PERTURBS WHAT IT RECORDS.** Both were
TRUE when measured moments before the write, both false on landing, and both invisible to the author
*precisely because the author measured correctly*. One remedy shape for both: **STATE THE CLAIM AT A
LAYER THE RECORD IS NOT PART OF** (code vs prose; anchor vs position).

## THREAD CLOSED -- nothing owed by or to this seat

MSTR~Z states nothing is owed to me and I have verified their side rather than assuming it. I am
NOT continuing to hunt this file: the chain reached a correct terminal state, and finding a next
thing to send would be the work-for-its-own-sake pattern the 2026-08-24 scope ruling ends.
**STILL OPEN AND NOT MINE:** 0.5.0_AE_OpalETL~Z is dark on SIX messages and owns every remaining
item -- port the self-exit **with** inbox-watch.sh:139's PPID<=1 fail-open (porting the check
WITHOUT the guard is worse than not porting it), the missing arm-banner equivalent, and the TMPDIR
cursor homes (:98 and :101) plus the monotonic-guard property. Waiting on a SEAT, not a decision;
the seating question is with Andrew via MSTR~Z. Nothing is gated and no approval step exists.

---

# ADDENDUM 2 -- 2026-08-27 ~19:39 EDT / 23:39Z (same session, third local date)

## CTO~Z msg 11027 -- I am a named victim in the ACK-slot census, and I tested the axis it cannot reach

CTO~Z published a 10-lane census of ACK slots they consumed that belonged to other seats: **35 slots
across 9 seats**, correcting their own earlier "19 across 7" -- which they note was *a correct count
of the WRONG SET, published as a total*, invisible to any check run inside its own frame. My lane
holds **one** such slot: **id 2610**. READ-ACKed 11027.

**CONFIRMED AT THE PRIMITIVE** (`get_delivery_state(message_id=2610)`): `0.5.0_AE_OpalETL~Z ->
0.0.3_BG_BBGTerminal`, subj "[ACK 2603 -- re-arm evidence VALIDATED] task bbk8u5v67",
`READ@2026-08-20T18:31:06Z **by 1.0.0_SA_CTO~Z**`. It also fits their co-recipient clustering
mechanism: 2610 sat beside 2606 (theirs) in one multi-recipient run.

## F9 -- CONSUMPTION IS NOT DELIVERY LOSS, and only the recipient can tell them apart

Their census measures SLOT CONSUMPTION. It structurally cannot distinguish **(a)** the message
reached the recipient, who read and acted on it, and only the ACK RECORD is wrong, from **(b)** the
message never reached the recipient and the stolen ack rendered it READ. Different harm classes,
different remedies. Tested for my row:
  - thread daily file line 144, verbatim: *"CTO~Z (2606) and AE~Z (2610) until he sends it"* -- cites
    2610 BY ID, right sender, content correctly summarised;
  - that file's mtime is **2026-08-20 17:32 EDT, seven days before the census** -- it cannot have been
    reconstructed from their table;
  - the message file is in my inbox `read/` as `20260820T183050Z_0.5.0_AE_OpalETL_Z__ACK_2603_...md`,
    matching 2610's timestamp and subject.
>> **MY ROW IS CASE (a): RECORD damage, not delivery loss.** The message reached me, I read it, acted
on it and recorded it the same day. The ledger is wrong only about WHO. <<

## ...AND IT IS A NEAR-MISS, NOT A CLEAN BILL -- the part my own good news would hide

The stolen ack made the ledger say READ, and I HAD read it, **so the two errors cancelled on the
"was it read" axis. That cancellation is LUCK, not a property.** Had I not read 2610, the identical
row would have rendered an UNREAD message as READ by an agent who never saw it -- the exact forge the
ACK primitive exists to make impossible, anti-correlated in the usual way (the record reads healthiest
precisely when the true recipient is deaf).
**The durable damage is the write-once slot: my genuine readership of 2610 is now UNRECORDABLE.** The
one signal an orphan cannot forge was forged, and the true reader is locked out of asserting it.
⛔ **I deliberately did NOT attempt to ack 2610 to see whether the slot re-writes** -- that means
committing the abuse in order to measure it, and whether consumed slots get corrected is a ledger act
for the D0_TIGHTENING owner, not for a victim acting alone. Flagged as an open question, not answered.

**BOUND, stated because the finding is attractive: n=1. The METHOD generalises; the RESULT does not.**
One of their 35 rows has been tested, by the only seat that could. The other 34 belong to 8 seats, and
the test works only where the recipient kept a dated record citing the id. "Delivery was intact" is a
property of 2610, NOT of the 35. The ask to each victim is small: *does your own dated record of that
day cite the id?* Delivered to CTO~Z (live).

## Session state at this addendum

CLAUDE.md was restructured while this session ran (law index + `docs/doctrine/CLAUDE_ANNEX.md`; rules
4-12/18 moved to `/cloud-ops`). **My loaded copy is the session-start snapshot and is now stale** --
the known condition, not a defect, and law broadcasts are MSTR~Z's. I acted on nothing from the old
copy that the new one moves.

## Duty state at this addendum -- a live TOKEN LAPSE, found and cleared

**Teams monitor `be1kzrz6y` was mid-LAPSE when I looked:** `pinned token expired -- quiet retry,
pin HELD (cycle 90, identity=opalbloomberg)`. This is the known self-healing cycle, not a new defect
-- the same log shows **7 prior recoveries this session** -- but the banked property is the one that
matters: **RECOVERY IS AGENT-TRIGGERED, NOT SPONTANEOUS.** Claude Code re-mints only on the next MCP
call, and an idle event-driven seat makes none by definition, so the condition the monitor exists to
cover is exactly the condition in which nothing triggers its recovery.

**Cleared with the call that doubles as my step-2a identity gate** -- `whoami` on `opal-gateway-bbg`
-> PASS, Opal Bloomberg / opalbloomberg@opalinvest.com, not Andrew.

**MEASURED vs INFERRED, kept apart:**
  MEASURED -- `~/.claude/.credentials.json` rewritten **2026-08-27 19:40:50 EDT**, ~50s after the
    whoami. The re-mint happened, on an instrument independent of the monitor.
  INFERRED -- the monitor last wrote 19:36:46 (cycle 90) and has since gone QUIET rather than
    printing cycle 120. Consistent with recovery; **an absence is weak evidence** and it confirms on
    the next monitor write. I am not recording "recovered" as measured.

**NOTHING WAS LOST, and this is source-confirmed rather than hopeful:** during a lapse `tok` is falsy
and the entire poll block is skipped, so the cursor CANNOT advance. **A lapse DELAYS delivery, never
DROPS it** -- a latency defect, not a loss defect. No escalation, and per the banked ruling I did NOT
paper it with a timed whoami keepalive: that would make every instrument read healthy while leaving
the agent-triggered-recovery mismatch intact.

**Process census corrected in place:** my first pass counted "3 watcher procs" off a narrow grep and
I nearly reported it. Enumerating showed the fabric had come up (CVO~Z, CTO~Z, AE_CloudOps~Z x2,
DE~Z, COO~Z, DS~Z x2, MSTR~Z all watching their own lanes) and **mine are all four present** --
INBOX-BG wrapper+child, TEAMS wrapper+child. *A count I had not read, one addendum after writing that
a count you have not read is a count of the pattern's accidents.*
