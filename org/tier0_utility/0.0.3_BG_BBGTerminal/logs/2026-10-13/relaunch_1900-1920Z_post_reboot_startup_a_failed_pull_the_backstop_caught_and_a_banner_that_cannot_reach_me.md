# Relaunch 19:00-19:20Z: post-reboot startup, a scheduled pull the backstop caught, and an arm banner that cannot reach me

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (the readiness exercises, the guardrail's second instrument),
DIAGNOSE (the stderr banner, the file-date replay test), SCRIBE (thread daily, one memory corrected)

Window: 19:00Z (register, pid 8384) to 19:20Z. Prior log:
`logs/2026-10-09/relaunch_0700-0745Z_post_reboot_startup_teams_arm_dead_and_a_missed_pull.md` (with
four addenda). Site Z rebooted ~17:51Z today on Andrew's word, relayed to me as msg 33686.

## Current State

Startup complete under `org/XXX.md` A-F plus this seat's own `prompt.md` On-Launch list. Registered
LIVE, inbox watcher armed (1 row, pid 9452), Teams Monitor armed (1 row, pid 8136), both at 1 row
with no stacking. Fabric mail 2/2 READ and acked. **Teams inbound this session is ZERO on both legs**
and the six items owed to Andrew are unchanged, all held on a draft-and-ask fork only he closes.
**The one number that moved is PFDE**, re-read because yesterday's entry predicted it would age at
Monday's close and it did.

### Readiness, exercised rather than read off a map

| check | instrument | result |
|---|---|---|
| identity acceptance gate (`prompt.md` 2a) | `whoami` on `opal-gateway-bbg` | **PASS -- Opal Bloomberg**, not Andrew |
| DAPI via MCP | `bloomberg_health` | `ok:true`, `//blp/refdata` |
| **a RUNNABLE pull** | the pull's OWN interpreter `C:\Anaconda\envs\cma\python.exe` -> `Session.start()` / `openService('//blp/refdata')` | **True / True** |

The third row is the one that matters and is the one `prompt.md` step 4 asks for: the MCP server runs
under a different Python than the pull, so a green `bloomberg_health` is not evidence a pull can run.
Two interpreters, deliberate (`integrations/bloomberg/READ_HERE.md:95`).

## 1. DAILY GUARDRAIL: the 11:00Z pull FAILED, the 11:30Z backstop caught it, and the served artifact is HEALTHY

Two pull logs today, and the pair is the finding:

| | 11:00:01Z (scheduled) | 14:32:45Z (summoned recovery) |
|---|---|---|
| precondition | **FAILED -- DAPI DOWN, PULL NOT ATTEMPTED**; fallback `rc=4` submit aborted pre-click, **no Bloomberg attempt spent, ledger untouched** | **PASS -- DAPI UP** |
| pull / publish / ETF / constituents / price | not reached | `0` / `0` (vintage **20261012**) / `0` / `0` / `0` |
| rivalfunds collector / enrichment | `93` / `97` (blpapi unreachable, 3 session attempts) | **`90` landed, marker written** / **`94` landed** |

`OPAL_BBGTML_freshness_check` at 11:30:02Z returned **2 -- STALE, SUMMONED**, and the summons
re-fired the pull task (`LastRunTime 14:32:43Z`, `LastTaskResult 0`).

**Second instrument, by content, because the wrapper's rc is not the artifact** (CLAUDE.md: never
trust a producer's self-report): `freshness_check.py` re-run read-only at **19:14:10Z -> PASS,
`data_as_of=2026-10-12 expected_frontier=2026-10-13 trading_days_behind=1`, series graded 10, every
graded series ends ON `data_as_of`.** Trading calendar resolved on the one frontier
(`lib/trading_calendar.py`, `NYSE/hardcoded-fallback-2010-2027`): 10-10 Sat / 10-11 Sun not trading
days, 10-12 Mon is -> **T-1 today IS 2026-10-12, so the vintage is correct and nothing is late.**

⚠ **THE TASK RECORD AND THE ARTIFACT NOW DISAGREE, AND THE TASK RECORD IS THE WRONG ONE TO READ.**
`Get-ScheduledTaskInfo` still reports `LastTaskResult 2` for the freshness check -- the 11:30Z
verdict, three hours stale and superseded by the recovery it summoned. A session checking the
guardrail from the task record alone would report a healthy artifact as stale. **The task result is a
log line; the artifact is the state.** This is the same shape as the stale-`<status>` class, reached
through the scheduler instead of a file.

## 2. THE ARM BANNER CANNOT REACH ME, SO A SUCCESSFUL ARM IS SILENT -- and silence is the dangerous half

> ⛔ **SUPERSEDED IN PART, SAME SESSION 20:1xZ -- the heading overstates it.** The stderr premise
> holds (`:523` writes `file=sys.stderr`, and only stdout notifies), but the banner IS READABLE: the
> Monitor's output file carries stderr at `tasks/<task-id>.output`, and the task id comes back from the
> Monitor call, so it can be read AT ARM TIME. Exercised on the live arm `bx0sfv9x4`. **Accurate form:
> the banner cannot NOTIFY, but it can be READ** -- and reading it is how the token-lapse evidence in
> `teams_token_ttl_500s_ack_latency_andrew_direct.md` was found at all. `prompt.md` step 3 is
> performable. The process census remains the liveness instrument; these are different questions.

`prompt.md` step 3 is emphatic: **"READ THE ARM BANNER'S `cursor=` VALUE BEFORE SERVING ANYTHING IT
EMITS."** I armed the Teams Monitor and no banner arrived. The instruction is not performable through
the channel it assumes.

**Source-confirmed, not inferred.** `teams-watch.py:523` writes the banner with
`file=sys.stderr`. The Monitor tool's own contract: only stdout is the event stream; stderr reaches
the output file and triggers no notification. The identity-FAIL lines print to **stdout as well**
(`:170`, `:207`, `:458`), which is exactly why the prior session's three dead arms notified loudly as
`exit 2 [TEAMS-IDENTITY-FAIL]`.

**So the notification channel carries FAILURE and not SUCCESS**, and "no notification after arming"
means either a healthy watch or a dead one. The instrument that separates them is a process census,
which I ran: `Win32_Process` where `CommandLine -match 'teams-watch\.py'` -> **1 row, pid 8136**,
command line carrying both the `--identity` oid pin and `--channels`. This is the
silence-is-not-success trap arriving through a new door: the prior incidents in this class were
watchers that read REACHABLE while deaf, and the remedy was the same -- a positive control on the
silence rather than an inference from it.

**Not routed as a defect, and that is deliberate.** Writing a status line to stderr is correct
engine behaviour; the gap is that `prompt.md` prescribes reading it through a channel that drops it.
`prompt.md` and `refs/` are unwritable from this seat by design, so the correction lands in the
record and in the memory entry, and the next session reads it there.

## 3. THE REPLAY TEST FIRES ON THE FILE DATE AND NOT ON THE FRONTIER -- I nearly declared a replay against a current cursor

`refs/TEAMS_DUTY.md` says: if the cursor is **"older than the newest entry in your thread daily
files"**, treat everything the arm emits as SUSPECT-REPLAY. Read literally, that fires today -- the
newest daily is `2026-10-12.md` and **both** cursor homes read 10-09, so I had written the
SUSPECT-REPLAY verdict before testing it.

**It is wrong, and the denominator is what shows it.** The newest *inbound message* recorded anywhere
across the 10-09..10-12 dailies (4 files, read) is `2026-10-09T20:14:55.504Z`; the live cursor
`/c/tmp/teams-watch.cursor` holds `2026-10-09T20:14:55.504Z` -- matching to the millisecond. The
intervening dailies record pipeline work, not messages. **The file date tracks when I last wrote,
which is not when I last served**, and a replay re-emits messages, so only the message frontier can
answer it.

Both homes read, denominator 2: `/c/tmp` 10-09T20:14:55.504Z (live -- `TMPDIR` unset in the harness,
so native Windows Python resolves `/tmp` to `C:\tmp`), `/tmp` 10-09T03:14:32.592Z (would replay
~17h). **The no-replay verdict holds on either home**, so it does not rest on the which-home
inference -- which is just as well, because that inference is the one part of this section I did not
exercise.

## 4. Teams inbound: ZERO on both legs, each scope named

| leg | instrument | result |
|---|---|---|
| DM + group | `poll_addressed_teams_messages since_iso=2026-10-09T20:14:56Z` | **0 new** |
| Opal Client Tickets channel | `read_channel_messages top=10` | **2 of 2 total**, both 2026-08-20, both authored by this seat |

The poll is chats-only by its own contract and cannot speak for the channel; the channel is the
separate bounded read. Its denominator is 2 because the intake schedule has never gone live, so
**there is no ticket to have missed** -- a zero with its cause named rather than a bare zero.

## 5. PFDE re-read: the prediction was right and the carried number was wrong

Yesterday's daily held `PX_LAST 28.645 / NAV 28.648 / PX_CLOSE_DT 2026-10-09` and said it ages at
Monday's close. Monday closed. Re-read at 19:1xZ: **`PX_LAST 28.37 / NAV 28.5044 / PX_CLOSE_DT
2026-10-12`** -- off by 0.275 on price, and the close date it named had been superseded. Had the word
to send arrived today, the held draft would have carried a stale figure under a current timestamp.
**The item is held, so the figure has now been re-read three times to keep it serveable; the holding
has a running cost and this is where it shows.**

## 6. The mechanical fence is STILL wired nowhere -- re-measured, unchanged, not re-filed

| registry | exists | `bg-concierge-gate` refs |
|---|---|---|
| `.claude/settings.json` | yes | **0** |
| `.claude/settings.local.json` | yes | **0** |
| `~/.claude/settings.json` | yes | **0** |
| `~/.claude/settings.local.json` | yes | **0** |

**0 refs across a denominator of 4.** Positive control, because a 0 from my own search is worth
nothing alone: `.claude/settings.json` carries 22 `"command"` entries and its hooks **fired on me
this session** -- the comp-rail denied my `grep -rn` at 19:14:29Z (`deny_id
20261013T191429Z-db271d19`). The registry is live; the gate (16161 bytes, Oct 1) is absent from it.

Unchanged in 4 days. It sits with `1.0.0_SA_CTO~Z` because wiring G3 as written would deny the very
booked Bloomberg draws this seat serves -- gate versus queue, which is not mine to rule. **Not
re-sent to anyone:** rule 31 puts corroborations in the record, not an inbox, and re-filing an owned
finding is noise.

## Compiler Tools

| tool | result | read |
|---|---|---|
| `comp-which "how do I grep the repo"` | forwarder RAN (A.3 exercise) | PATH healthy: **102 of 102** comp-tools resolve bare |
| comp-rail (`comp-tool-hud` PreToolUse) | **DENIED** one call -- `grep -rn 'cma' <file>` tripped F1 (blind recursive search) | My fault, not the rail's: I wanted ONE named file and typed `-r`. The REMAINDER line handed back the rest of the call intact and the re-run without `-r` was free. **This denial is also the positive control in section 6** -- it proves `.claude/settings.json` is the live hook registry the fence is missing from. |
| `python .tools/to-check.py --all --assignee 0.0.3_BG_BBGTerminal` | **0 active TOs**, scanned 6275, 0 parse errors | I hold no task orders. The THIRD-POPULATION line (91 of 6275 faces with a `<status>` and no recognised assignment field) is a fabric-wide artifact, not mine. |
| `python .tools/audit-archive-invoker.py` | `rc=1`, **16 findings**, snapshot not-due (baseline 9.9h < 12.0h) | 3 classes: 5 MANIFEST-ENTRY-MISSING-LIVE, 2 UNCOVERED-AUDIT-LOG, 4 NON-APPEND-EDIT + 5 ERROR-FAILCLOSED. **The NON-APPEND-EDITs all read live-head SMALLER than baseline** (e.g. `git-author-override-audit.log` 2670305B vs 2705416B) -- the signature of a box-sync merge taking another box's version of an append-only log, not of a truncating writer here. Surfaced, not re-filed: the class has an owner and `org/XXX.md` A.2 says surface only an unowned class. |
| `freshness_check.py` (read-only re-run) | **PASS** `data_as_of=2026-10-12 behind=1`, 10 series graded | The guardrail's second instrument. Chose it over trusting `LastTaskResult 2`, which was the finding in section 1. |
| `lib/trading_calendar.py` | `is_trading_day` / `trading_days_behind`, source `NYSE/hardcoded-fallback-2010-2027` | WARN: `pandas_market_calendars` absent, answering from the hardcoded fallback (covers 2010-2027, regenerate before 2028). Good enough for a 10-12/10-13 question; it would not be for a 2028 one. |

**Gap:** no `TaskOutput` tool in this session's toolkit, which is what `org/XXX.md` C names for
confirming an arm and what section 2's banner would need. The process census substituted for it and
is the better instrument anyway, since it measures the python rather than the wrapper.

## Blockers

- **The six Teams items remain held at Andrew**, on the draft-and-ask fork between this thread's
  standing line and `prompt.md`'s "beyond a Teams reply" carve-out. Five sessions now. He is at this
  terminal; the held set goes to him in session, the established discharge route.
- **Mechanical fence unwired** -- with `1.0.0_SA_CTO~Z`, unchanged, re-measured above. Not blocked on
  me and not re-filed.
- **Gateway allowlist: 6 of 6 reads denied on this identity**, carried from 10-09 and not re-exercised
  this session. Stated as held, not as measured today.
- Not blocked on me: nothing. No task orders, no pipeline act owed -- today's data is served and
  healthy at T-1.
