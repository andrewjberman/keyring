# Teams ack latency is an OAuth TTL defect: 500 s measured, cause isolated, Andrew takes the fix to the app registration

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE (the live-arm control), SCRIBE (the Andrew-direct record)

Written on Andrew's direct instruction, 2026-10-13T20:12:50.23Z: *"write a /log on the subject and
issue to MSTR~Z."* Verbatim record + scope:
`deliverables/ANDREW_DIRECT_20261013_2012Z_CONTROL_THE_GRAPH_TOKEN_TTL_LOG_IT_AND_ISSUE_TO_MSTR_Z.md`.

## The ask behind it

20:00:32Z, Teams 1:1: *"We need to figure out a mechanism for faster turnaround on chat ... a 'sure,
let me look into that' ... that shoots out the second the agent is made aware of a new user query,
then it sends it's followup message that is actually researched."*

**The mechanism he describes already exists and fired on his own message.** `/bbg-teams-assist` step 1
is an immediate in-thread receipt before any research; that is what went out at 20:08:52Z, sent
before I had read his body. **So the ack policy is not the defect. The defect is AWARENESS, which is
upstream of it, and it is worth separating because the two have different owners and different
fixes.**

## The 500 seconds

His message 20:00:32.89Z; my ack 20:08:52.549Z. **500 s.**

**The explanation I was about to give was wrong, and the arithmetic killed it before I sent it.**
I had the arm's designed death at 20:08:27Z and reached for "the monitor was down" -- but his message
landed **475 s BEFORE** that death, and the engine polls every **10 s** (`INTERVAL`,
`teams-watch.py:157`). A live watcher on a 10-second loop had his message in its window for nearly
eight minutes and emitted nothing. "It was down" is not just unproven, it is false.

**The watch's own output file says what happened** -- `tasks/bodbap82m.output`, 802 bytes, read whole:

```
[teams-watch] armed interval=10s cursor=2026-10-09T20:14:55.504Z (incoming-only) pin(...) channels=1 watched
[teams-watch] pinned token expired -- quiet retry, pin HELD (cycle 1, identity=517aa5ee-...)
[teams-watch] re-selected after lapse: identity=6810043e-.../517aa5ee-...
[TEAMS] oneOnOne from Andrew Berman: Are you online? ... ts=2026-10-13T19:44:04.558Z
[teams-watch] pinned token expired -- quiet retry, pin HELD (cycle 1, identity=517aa5ee-...)
[exited with code 124]
```

The last lapse line never gets a matching `re-selected`. Decomposed against my own call history:

| clock | event | instrument |
|---|---|---|
| 19:45:08.709Z | my PFDE send -- **my last gateway call** | send receipt `1791920708709` |
| ~19:59Z | pinned token hits its ~14 min TTL; `if tok:` skips the whole poll block, so the cursor cannot advance | the 2nd lapse line |
| **20:00:32.89Z** | **his message lands inside the lapse** -- nothing polls, nothing emits | msg `1791921632890` |
| 20:08:52Z | my gateway calls re-mint the token; the re-arm emits his message | ack `1791922132549` |

**Loss is impossible here and that is structural, not luck:** while `tok` is falsy the `res`/`cursor`/
`CURSOR_FILE` writes are all inside the guard, so a lapse cannot advance the cursor past an unseen
message. **It is a pure latency defect** -- and its bound is not a constant. It is "how long until the
agent next calls the gateway," which for an idle event-driven seat is unbounded.

## Why this was predicted and still surprised me

**This exact failure mode is banked** in memory `bg-relaunch-teams-watch-identity-defect-held.md`,
written 2026-08-12 with a negative control: *"RECOVERY IS AGENT-TRIGGERED, NOT SPONTANEOUS ... an idle
event-driven seat makes no gateway calls by definition, so the condition the monitor exists to cover
is exactly the condition in which nothing triggers its recovery,"* and *"unbounded in principle for an
idle seat."*

**It had no measured instance until today. Now it has one: 500 s.** The entry also records that I
declined a timed keepalive then, on the grounds that it would make every liveness instrument read
healthy while leaving the mismatch intact. **That reasoning was about LIVENESS REPORTING and it does
not reach a LATENCY ask** -- which is why the same proposal is right today and was right to decline
then. The narrow form of the objection survives and I volunteered it to Andrew unprompted: a
keepalive must not become the liveness oracle.

## The fix moved layers, and his is better than mine

I proposed a ~10-minute keepalive call inside the TTL -- worst case ~14 min -> ~10 s. **Andrew
redirected it:** *"we should be able to control TTL for this process, considering that we are admins
on the graphapi application."*

**That is a better fix and the difference is worth stating:** a keepalive is a workaround that keeps
a short-lived token artificially warm, adds a standing call, and leaves the lapse path live for every
window the keepalive misses. Lengthening the TTL at the app registration **removes the lapse state
instead of outrunning it.** My proposal treated the TTL as a constant; it is a setting.

**Two premises of his I did not verify and am not asserting:** that the app registration's token
lifetime is administrator-configurable for this flow, and that Opal's admin rights extend to that
setting. Both plausible (Entra token-lifetime policy is a real surface); **both HELD, not measured**
-- I have no read on that app registration from this seat and did not attempt one. He is implementing
at the terminal himself, so the verification is his.

## ⛔ A correction to my own earlier log, same session

`logs/2026-10-13/relaunch_1900-1920Z_*.md` section 2 says the arm banner **"cannot reach me."** The
premise is right -- `teams-watch.py:523` writes it with `file=sys.stderr`, and only stdout triggers a
Monitor notification -- **but the conclusion was too strong.** The Monitor's output file carries
stderr, its path is `tasks/<task-id>.output`, and **the task id is returned by the Monitor call
itself**, so the banner is readable **at arm time**, not only after an expiry notice hands the path
over.

**Exercised on the live arm, which is the control:** `tasks/bx0sfv9x4.output` while still running
reads `armed interval=10s cursor=2026-10-13T19:45:08.709Z (incoming-only) pin(server=opal-gateway-bbg,
identity=517aa5ee-...) channels=1 watched (Opal Client Tickets)`.

**Accurate statement: the banner cannot NOTIFY, but it can be READ.** `prompt.md` step 3 is therefore
performable, and the habit it wants is "read that file right after arming" -- which also surfaces the
lapse lines above, the very evidence this log rests on. I reached the right verdict this morning by a
different route (reading both cursor homes directly), so nothing downstream was wrong; the overstated
sentence would have taught the next session to stop looking.

## Compiler Tools

| tool | result | read |
|---|---|---|
| `read_chat_messages` (1:1, `top=2` then `top=6`) | denominators 2 and 6 | The `top=6` read is what reframed the whole session: it showed his 10-09 PFDE question had sat unanswered in-thread for four days behind an ack that promised a return. The OWED list recorded the item but not that fact. |
| `poll_addressed_teams_messages` | 1 new at 20:00:32Z; earlier sweeps 0 | Chats-only by contract -- it cannot speak for the channel leg, which is a separate bounded read. Scope stated every time rather than reported as a bare zero. |
| Monitor output files (`tasks/<id>.output`) | 802 B and 1 live arm, both read whole | **The instrument this log rests on, and the one I had written off.** Also the correction above. |
| `Win32_Process` census on `teams-watch.py` / `inbox-watch.sh` | 1 row each at every re-arm, pids 8136 -> 17484 -> current; 9452 -> 20940 -> 12756 | Still the liveness instrument, and deliberately kept separate from the TTL question: a minted token says nothing about a running process, and vice versa. |
| `bloomberg_reference_data` (PFDE, 1 security) | `28.37 / 28.5044 / 2026-10-12` | Under the 2-security cap. The held figure had aged exactly as the 10-12 daily predicted. |

**Gap:** no `TaskOutput` tool in this session, which `org/XXX.md` C names for confirming an arm. Reading
`tasks/<task-id>.output` directly substitutes for it and carries strictly more (the stderr
diagnostics), which is how the lapse was found at all.

## Blockers

- **The TTL change is Andrew's**, at the terminal, later today by his word. Not mine, not MSTR's,
  not `0.5.0_AE_OpalETL~Z`'s unless he routes it there.
- **Three Teams items remain on his word** (the 10-09 forward ack, the Alyssa Tax SMA reply, the ack
  on his 10-08 dictated note) plus the "more details" owed to Alyssa from 09-30. PFDE discharged
  19:45Z.
- Not blocked on me: nothing else. Served data healthy at T-1, no task orders held.
