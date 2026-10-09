# Relaunch 07:00-07:45Z: post-reboot startup, the Teams arm is dead by construction, and 10-08's pull was never recovered

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (the four acceptance reads), DIAGNOSE (the arm failure, the
missed pull), SCRIBE (thread daily, one memory sharpened)

Window: 07:00Z (register, pid 16136) to 07:45Z. Prior log:
`winddown_0620-0640Z_site_z_reboot_state_and_time_windowed_obligations.md`. Site Z booted
2026-10-09 02:58:55 EDT = **06:58:55Z**, measured from `Win32_OperatingSystem.LastBootUpTime`.

## Current State

Startup complete under `org/XXX.md` A-F plus this seat's own `prompt.md` On-Launch list.
Registered LIVE, both inbox watchers armed and re-armed once on expiry. **The Teams Monitor is
the one thing that did NOT come up, and it cannot be made to from this seat.** Four Teams items
are held at draft-and-ask awaiting Andrew's word; he is live at this terminal and the held set
was put to him in session, the same discharge route the 10-08 and 03:14Z items took.

### The four acceptance reads (msg 32201's set), re-measured for THIS session

| read | instrument | result |
|---|---|---|
| exactly 3 MCP servers | `org/mcp/sessions/7ae0b7ba-...mcp.json`, 3 keys | PASS: bloomberg, opal-agent-comms, opal-gateway-bbg; all three answered live this session |
| registered LIVE | `register_agent` | PASS, pid 16136 |
| `bloomberg_health` | the tool | PASS `ok:true`, `//blp/refdata` |
| token subject oid `517aa5ee` | read-only decode of `~/.claude/.credentials.json` | PASS on identity; see the arm section -- the record was EXPIRED at first read and the file read is NOT the liveness instrument |

Identity acceptance gate (`prompt.md` step 2a): `whoami` on `opal-gateway-bbg` returned
**Opal Bloomberg** (`opalbloomberg@opalinvest.com`), not Andrew. PASS, re-exercised twice.

## 1. THE TEAMS MONITOR CANNOT ARM -- and the cause is not the one I carried in

Two arms (`b5u7p63x0`, `bs9zv8i8k`) died **`exit 2 [TEAMS-IDENTITY-FAIL] no-token-for-identity`**.

My successor note from the prior session said to expect lapsed-token blindness and prescribed a
gateway call to re-mint. **I ran that control and it did not save the arm**, which is what made
the real cause findable: the gateway call re-minted the record (file mtime 07:29:35Z, record
`LIVE (+883s)` -- the ~14-min TTL confirmed to the second), and **the very next arm still died**.
Expiry is therefore ruled out by positive control, not by argument.

Filter census on `_read_pinned_token` (`teams-watch.py:234-241`), by subtraction over my own
credential store, denominator 4 `mcpOAuth` records:

| filter | predicate | survivors |
|---|---|---|
| 0 | all `mcpOAuth` records | 4 |
| 1 | `"opalinvest.dev" in serverUrl` | 3 |
| 2 | `"opal-gateway-bbg" in serverName` | 1 |
| 3 | `"opalbloomberg" in self_id(accessToken)` | **0** |

`self_id()` (`:283`) reads `sub` or `preferred_username` or `upn`. This token carries **only**
`sub`, and `sub` is `6810043e-d171-4adc-9975-068b35e179da/517aa5ee-b4d0-425a-b493-5a22ff77ac4f`
-- two GUIDs. `opalbloomberg` is not a substring of it and never will be. **The pin
`--identity opalbloomberg` is unsatisfiable BY CONSTRUCTION, not by lapse.**

**This corrects the prior session's attribution.** "3 of 3 arms came up blind ... the pinned
token's TTL is ~14 min" named a real mechanism (the TTL is real, measured twice today) that is
**not the one that empties the set** -- filter 3 empties it before the expiry filter at `:240` is
ever consulted. The TTL explanation is the dangerous kind: true, adjacent, and it predicts a
QUIET return-None retry, whereas the measured behaviour is a LOUD exit 2. A real mechanism will
explain the symptom it is offered for; this one explained a different one.

Routed to `1.0.0_SA_CTO~Z` (msg @20261009T073513Z) with a one-token fix: pin by oid,
`--identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f`, a substring of that `sub`, identity guarantee
intact. **Not taken here** -- `.claude/` is deliberately unwritable from this seat, and arming
bare is the OPAL_ANALYST P0 defect.

**Service continuity: the seat is UNWOKEN, not DEAF.** `poll_addressed_teams_messages` +
`read_chat_messages` are both reachable; I polled and served the backlog by hand this turn.

## 2. THE POLL COUNT IS A CHAT COUNT, NOT A MESSAGE COUNT

`poll_addressed_teams_messages(since_iso=2026-10-07T00:00:00Z)` returned **`count: 1`** -- the
06:40Z message. `read_chat_messages` on that same chat returned **two** unserved Andrew messages:
the 06:40Z forward **and the 03:14Z PFDE ask**. The tool's own contract is per-CHAT ("chats whose
LATEST message arrived after `since_iso`"), one row carrying that chat's latest preview.

**Had RECALL not run, the 03:14Z ask would have read as already-handled because the poll did not
name it** -- an absence produced by the instrument, indistinguishable from a true absence. The
`/bbg-teams-assist` doctrine ("THREAD MEMORY DECIDES WHAT IS OWED, never the emit") is written
against the replay direction; this is the **under-count** direction and it bites the same way.
Banked to the thread daily. Cost of the control: one `read_chat_messages` per woken chat.

## 3. THE 2026-10-08 SCHEDULED PULL FAILED AND WAS NEVER RECOVERED

Daily guardrail (Andrew-asked 2026-08-10, @e77bec6e5). `OPAL_BBGTML_daily_pull`
**LastResult = 50** = DAPI-liveness PRECONDITION FAILED, pull NOT attempted.

Census over the 30 retained `bbg_tplus1_*.log` files (2026-09-10 to 2026-10-08), denominator
printed: **6 are rc=50.** 10-06's 07:00 failure was recovered by an 08:24 run that passed;
**10-08's has no recovery log at all**, and there is no 10-05 07:00 log (that day's user-context
task appears not to have fired).

Consequences, separated by whether they self-heal:
- **Models: self-heals.** The PKL is a full series, so today's 11:00Z publish of as-of 10-08
  carries the 10-07 bar. The served layer has been a day behind since Wednesday.
- **ETF + constituents: PERMANENT.** Both legs sit after the publish leg and are **not reached on
  the rc-50 path**; the derived/constituents layer is current-day-only with no backfill, so
  2026-10-08's capture is gone. The wrapper's own `:cons_leg` comment names this exact harm.

⚠ **A census trap I walked into and caught.** My first pass over these logs returned
`<no verdict line>` on **all 30 rows** -- an unquoted `$f` in a `for` loop word-split on the space
in `C:\Users\Opal Bloomberg\`. Every row read as a clean absence. The banked lesson
(`sitez-path-space-splits-unquoted-word-splitting`) is exactly this and I still wrote it; what
caught it was that **30 of 30 reading identically is not a finding shape**. A per-row predicate
true on every row is a broken predicate, not a discovery.

## 4. THE `etf_daily_pull.py` REBOOT HAZARD RESOLVED FAVOURABLY

Surfaced at wind-down as unowned. Re-measured at 07:13Z: the **15-line deletion SURVIVED the
reboot** (`git diff --stat`: 1 file, 15 deletions, unchanged). A reboot is not a tree wipe. So the
11:00Z ETF leg runs the bytes whoever staged them intended, and
`OPAL_restore_etf_daily_pull_20261009` (08:00 local = 12:00Z, action read:
`git -C <repo> checkout HEAD -- integrations/bloomberg/pipeline/etf_daily_pull.py`) restores the
committed block afterwards. **The pathological branch I named did not materialise.**

I also verified the premise I had inherited rather than carrying it: `scheduled_daily_pull.cmd:242`
does set `ETF_PULL` to that file and run it from the working tree, so the hazard chain was
correctly described. Still not mine on either count (`integrations/bloomberg/` no-modify order; I
did not stage it); neither committed nor reverted.

## 5. A LIVENESS CLAIM I GOT WRONG, AND THE CORRECTION

I told `0.0.0_AB_MSTR~Z` that `0.7.0_AE_CloudOps~ZV` -- owner of the 10:45Z terminal sign-in
pre-flight -- was "not among the 15 live", read off `get_live_agents`. **Wrong, corrected in four
minutes (msg 32517):** ~ZV relaunched 07:19Z, turn bridge READY 07:21Z, READ and ACKed both its
orders at 07:26Z. **Codex lanes do not register on the broker at all** -- a different runtime, no
`register_agent` path, sends read `sender-unverified`. Broker absence for a Codex serial is not
weak evidence; it is `0 of 0`.

Worse, the remedy in my own banked memory for this class (`an-unregistered-session-is-not-a-dead-one`:
"measure the PROCESS plane, `claude.exe` with the serial in argv") is **also blind to a Codex lane**
-- I would have checked twice, got two zeroes, and been more confident while just as wrong. That
memory is updated with the new class and the corrected remedy: name the seat's RUNTIME before
converting any roster zero into absence, and route the question to the box MSTR.

What kept the cost at four minutes: the claim went out **as a message with an ASK attached**, not
as an act. ~ZV is still blocked on carrier placement (its orders sit in
`org/missions/D5/ETFS/ETFS_RIVALS/task-orders/`, not its seat home); the fix is dell1's and the
MSTR holds a **10:15Z checkpoint** to name a fallback seat. Nothing owed by me.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-find --files` | locate `teams-watch.py` | PASS -- denominator 2822 hits / 171922 files, bands printed |
| `comp-which` forwarder exercise | XXX.md A.3 | PASS -- 102 of 102 resolve bare, a forwarder RAN |
| `python .tools/to-check.py --all --assignee` | work held | PASS -- 0 active TOs, scanned 5085, third-population 91 named |
| `.tools/audit-archive-invoker.py` | XXX.md A.2 | rc=1, 15 findings, all standing owned class -- not re-filed |
| `git diff --stat` + `Get-ScheduledTask(-Info)` | the reboot hazard | PASS -- deletion intact, both task actions read verbatim |
| per-filter subtraction over `mcpOAuth` | the arm failure | PASS -- isolated filter 3 as the emptier; the whole finding |
| `get_live_agents` | ~ZV liveness | **FAILED, and silently** -- out-of-corpus for a Codex lane; see section 5 |

**What worked:** running the prior session's prescribed control (the re-mint) *and not stopping
when it did not fix the symptom*. The control passing while the failure persisted is what turned
"known flaky arm" into a located defect with a one-token fix.

**What failed:** the unquoted-path census in section 3, and the ~ZV liveness claim in section 5 --
both cases of an instrument reporting a clean zero outside its corpus, which is the same defect
twice in one session on two different planes.

**Gap found, unchanged from the prior session and still routed not taken:** lane `TIER0_UTILITY`
does not list this seat in `permitted_agents`, so `threads/` and `deliverables/` -- the serve
loop's continuity record -- cannot be committed from this seat without the audited lane escape.
`logs/` and `task_orders/` auto-enrol and commit cleanly.

## Blockers

- **Teams Monitor: BLOCKED on `1.0.0_SA_CTO~Z`** for the `.claude/skills/bbg-teams-assist/SKILL.md:35`
  arm-line amendment. Serving by direct poll meanwhile.
- **Four Teams sends held at draft-and-ask**, awaiting Andrew's word in session: the PFDE answer
  (in hand, calendar-resolved), the 06:40Z forward ack, the Alyssa Tax SMA reply (drafted 10-08),
  and the ACK on his 10-08T21:57Z dictated Tax SMA ask. Plus the "more details" promised to Alyssa
  on 09-30, carried from 10-07.
- **Gateway allowlist: 6 of 6 reads denied on this identity**, unchanged. Measured service cost
  stands: the Bloomberg guardrails' PREFERRED path is the already-paid-for served artifact, and
  this seat cannot reach it, so every data question burns a live terminal read.
- Not blocked on me: the 10:45Z pre-flight (MSTR, 10:15Z checkpoint) and the 11:00Z fire.

---

# ADDENDUM 08:3x-08:4xZ -- SECTION 3 IS WRONG, AND THE DEFECT IS THE ONE THIS LOG ALREADY NAMES TWICE

**Section 3 above claims 2026-10-08 "has no recovery log at all" and that its ETF + constituents
captures are "PERMANENT[ly]" lost. Both claims are FALSE.** Corrected to `0.0.0_AB_MSTR~Z`
@20261009T083925Z. The log body above is left standing unedited so the error and its correction
are both readable; this addendum governs.

## What is actually true, measured

The pull chain for 2026-10-08 **fully recovered and published**. Seven `bbg_recovery_*` logs,
11:43Z to 12:23Z, sat in `C:\Users\Opal Bloomberg\opal_bbg_logs\` -- **the same directory I
censused.**

| leg | verdict read in its own log |
|---|---|
| pull | `RESULT: PASS -- both PKLs safe to send`; model as-of 2026-10-07 |
| publish | `RESULT: PUBLISHED 2026-10-07 -- verified by content, not by self-report`; served `data_as_of 2026-10-07`, `generated_at 2026-10-08T12:04:14Z`; 1D matches the PKL for all five models |
| constituents | `[etf_constituents] EXIT 0` -- landed under `bbg/2026-10-07/constituents/` |
| ETF | `[etf_daily] EXIT 0` -- landed under `bbg/2026-10-07/` |
| price | as-of 2026-10-07, 30-day window |
| rivalfunds + collector | `status: OK`, corporate actions + security_market written for date=2026-10-07 |

**And the backstop limb worked exactly as designed.** `OPAL_BBGTML_freshness_check` (07:30 ET =
11:30Z, `freshness_check.cmd` contract `0 fresh / 2 stale-summoned / 3 check-error-summoned`)
returned **2** on 10-08 -- STALE DETECTED, SUMMONED. Recovery began 11:43Z, 13 minutes after the
summons; served and content-verified at 12:04Z. **1h04m from missed fire to verified serve.**
Andrew's 2026-08-20 design ("only then are you summoned") fired, and the summons was answered.

## THE DEFECT, and it is the third instance in one session

My census filter was `bbg_tplus1_*.log`. The recovery family is `bbg_recovery_*`. **The filter
excluded the answer by construction, and the zero it returned was indistinguishable from "no
recovery happened."** I printed a denominator -- "30 retained logs" -- and that denominator was
TRUE and bounded the WRONG POPULATION: 30 of 30 scheduled-wrapper logs, when the question was
about delivery, which has a second producer. A real denominator over the whole directory reads
**37 files in 8 families**, 7 of them the ones I needed.

⛔ **This is the same defect as the unquoted-path census (section 3) and the ~ZV liveness read
(section 5): an instrument scoped narrower than the claim, returning a clean zero.** Three times
in one session, on three planes, and I had **already written the lesson up twice in this very log
and once into memory** before committing it the third time. Knowing the class does not catch it;
only asking "what else writes this?" at the moment of the filter does.

⭐ **The specific question that would have caught it, and it is cheap:** before reading absence
from a filtered census, **count the writers of the thing you are asking about.** Delivery here has
TWO producers -- the scheduled wrapper and the recovery path -- and I filtered to one. CLAUDE.md
NEVER#1's sibling rule already says this for sign-offs ("first count the writers of the named
property: N writers = N rules read, and N is printed"). It applies to censuses, not just
sign-offs.

⚠ **Also corrected: the framing, not just the fact.** "6 of 30 rc=50" grades the SCHEDULED limb
and is not a delivery failure rate. A system that misses a fire and self-heals to a
content-verified serve in 1h04m is a system with a working backstop, not a 20%-failure pipeline.
I handed the MSTR the alarming reading of a healthy mechanism while it was weighing a
time-windowed ownership call.

## What stands from section 3

- `OPAL_BBGTML_daily_pull` LastResult=50 on 10-08 is real: the 07:00 ET fire did not run, DAPI
  down, pull not attempted. That is why the 10:45Z sign-in pre-flight exists and is worth owning.
- The rc=50 count (6 of 30) is a real read OF THE SCHEDULED LIMB and is a fair input to the
  pre-flight question.
- No 10-05 07:00 wrapper log exists.
- The `:precond_down` -> `:prune` path does skip the ETF/constituents/price legs **within that
  run**; what is false is the inference that the day's captures were therefore lost, because the
  recovery path reaches them all.

## Compiler Tools (addendum)

| Tool | Use | Result |
|------|-----|--------|
| `Get-ScheduledTask` over the whole box | find the backstop the wrapper's prose cites | PASS -- 13 Opal/BBG tasks, denominator 213; found `OPAL_BBGTML_freshness_check`, which the wrapper's prose calls "the 07:15 backstop" while its trigger reads **07:30** |
| `ls | sed | sort | uniq -c` over the log dir | the denominator I should have taken first | PASS -- 37 files, 8 families; the whole correction |
| per-leg verdict read of 7 recovery logs | verify before correcting | PASS -- did not replace one unverified claim with another |
