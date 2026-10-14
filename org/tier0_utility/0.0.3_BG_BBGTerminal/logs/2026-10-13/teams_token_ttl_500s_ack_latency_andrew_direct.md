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

---

## ADDENDUM 20:3xZ -- SECOND INSTANCE, SAME SESSION, AND THE RECOVERY EXERCISED DELIBERATELY

The defect reproduced ~15 minutes after the log above was written, which is worth recording because
**a single instance cannot distinguish a one-off from a cadence, and this one is a cadence.**

Read from the live arm `bx0sfv9x4` while it was still running: its last line was
`pinned token expired -- quiet retry, pin HELD` with **no matching `re-selected`** -- i.e. **the seat
was deaf on Teams at the moment I read it.** Last gateway call before that read: my 20:16:44.498Z
send. The interval matches the ~14 min TTL again. **Two instances, one session, both following the
same trigger: the seat goes quiet, the token lapses, hearing stops.**

**Recovery exercised on purpose rather than waited out:** one `whoami` on `opal-gateway-bbg` -- the
cheapest gateway call available, and it doubles as this seat's `prompt.md` 2a identity re-gate (it
returned **Opal Bloomberg**, not Andrew, so the pin still holds). This is the mechanism's own stated
recovery path, performed by hand. **It is NOT a keepalive and nothing standing was built:** Andrew
reserved the TTL fix to himself, and CLAUDE.md bars implementing an unasked-for mechanism. One manual
call is an act; a timer would be a mechanism.

**Service check, run independently of whether the watcher recovered**, because the watcher's state is
not the service question: `poll_addressed_teams_messages since_iso=2026-10-13T20:12:51Z` returns
**1 message, and it is my own 20:16:44.498Z send.** Nothing inbound landed during the lapse, so
**nothing was missed** -- the latency-not-loss property holding in practice, not just in the source
reading.

**What this adds to the case Andrew will act on:** the ~14 min lapse is not an edge case reachable
only after a long idle. It fires between ordinary turns of a working session -- twice in forty
minutes here, and the only reason the second one cost nothing is that nobody happened to write during
it. **The exposure is "whatever arrives in the gap," and the gap recurs every ~14 minutes of quiet.**

### CONFIRMED: the manual recovery WORKED, and my own caution about it was a bad read

When the prior arm expired I read its full tail and found the ordering I had missed:

```
[teams-watch] re-selected after lapse: identity=6810043e-.../517aa5ee-...
[teams-watch] URLError: <urlopen error [WinError 10054] ... forcibly closed by the remote host>
[exited with code 124]
```

**The `re-selected after lapse` fired -- the `whoami` re-mint restored the watch exactly as the
mechanism predicts.** I had reported the recovery as UNCONFIRMED, and that was wrong: I read `tail -1`,
got the transient `URLError` that landed AFTER the confirmation, and treated a one-line window as the
verdict. **The confirmation was already in the file, one line up.** This is the banked
"never read a gate's verdict from a positional slice" lesson biting in the CONSERVATIVE direction --
safer than over-claiming, still a misread, and it cost a true recovery its credit. The rule is the
same either way: widen the read to the lines that carry the verdict, then decide.

**Why the correction matters to Andrew's decision rather than being bookkeeping:** it establishes that
the lapse is *recoverable on demand* and that the recovery is *reliable*, not hopeful. So the choice
in front of him is clean -- raise the TTL and the lapse state stops existing, or leave it and the
seat depends on an agent-side call that only happens when the agent is already doing something. The
manual path is proven to work and proven to require exactly the condition (agent activity) that the
deaf window is defined by the absence of.

Next arm `b911j0y5z` came up clean on the first cycle: `cursor=2026-10-13T20:16:44.498Z`,
**`token selected`** rather than a lapse, `channels=1 watched (Opal Client Tickets)`. Inbound since
20:16:45Z: **0**.

---

## ADDENDUM 21:0x-21:1xZ -- THE SILENT-ARM FINDING WAS FIXED BY SOMEONE ELSE IN ~50 MINUTES, AND I NEARLY CONFESSED TO AN ERROR I DID NOT MAKE

My 21:07Z arm emitted a line no previous arm had: **`[TEAMS-ARMED] pid=6036
identity=517aa5ee-... channels=1 cursor=2026-10-13T20:16:44.498Z`, on STDOUT**, which the Monitor
delivered as a notification. Reading the source, `:528` prints it under a comment that states my own
finding as its rationale:

> `# ARM RECEIPT (Z6 R5): the banner above is stderr, which a Monitor does not deliver, so from`
> `# inside an armed session a healthy watcher and a dead one read identically.`

**My first instinct was that I had been wrong** -- that the receipt had been there all along and my
"a successful arm is silent by construction" was an overreach from an incomplete read. I was about to
write that correction. **It would have been false, and three instruments say so:**

| instrument | reading |
|---|---|
| `git show HEAD:.claude/skills/teams-assist/teams-watch.py \| grep -c 'TEAMS-ARMED'` | **0** |
| positive control, same ref, `grep -c 'armed interval'` | **1** -- so the ref read and the grep both work |
| `git status --porcelain` on the path | **` M`** -- working-tree only, uncommitted |
| working-tree mtime | **2026-10-13 17:06:36 EDT = 21:06:36Z** |

**The receipt did not exist when I made the claim.** It was written ~50 minutes after I logged the
finding and ~20 minutes after `0.0.0_AB_MSTR~Z` swept the log to origin. The claim was TRUE when
made and the fix is a RESPONSE to it, which is the opposite of an error.

⛔ **THE REAL LESSON IS THE CONFESSION I ALMOST FILED.** I read the CURRENT bytes to adjudicate a
PAST claim. That is the deployed-bytes-vs-build-input trap pointed at my own record, and the banked
rule covers it exactly: *a confession is a claim and carries the same evidence burden.* A false
confession is not harmless modesty -- it would have retracted a correct finding, told the next
session the gap was imaginary, and stripped the fix of its reason for existing. **The instrument that
settles "was this true when I said it" is never the working tree; it is the ref at that time, plus
an mtime, plus a positive control.**

### Side finding: a census is a SAMPLE, not a STATE

The census that followed read **2 teams-watch rows** (6036 and 10044, born 21:07:44Z and 21:09:41Z) --
stacking, and two watchers on one cursor is the banked 2-watchers-1-cursor hazard. **One minute later
it read 1 row.** 10044 was transient, almost certainly the D7 intake runner the engine's own header
says imports this module every 5 minutes. **Both readings are true; neither is "the state."**

**What stopped a bad act:** `/watcher`'s N>1 rule says reap every row but the one you recorded, and my
recorded pid was 6036 -- so the rule pointed at killing 10044. **Reading its command line FIRST (which
showed it already gone) is what prevented killing a peer's or a scheduled runner's process.** The
reap rule is written for MY stacked watchers; it does not license killing a row before identifying it.

**No cursor damage:** `/c/tmp/teams-watch.cursor` reads `2026-10-13T20:16:44.498Z`, mtime 20:16:47Z --
unchanged since my own 20:16:44Z send and matching the receipt exactly. Inbound since: **0**.

### What this changes for my own earlier sections

Section 2 of `relaunch_1900-1920Z_*.md` and its in-session correction both stand as written **for the
bytes they described**. The receipt now closes that gap properly -- better than my
read-the-output-file workaround, because it NOTIFIES rather than needing to be fetched. **Live
uncommitted, so it is a deploy only on this box:** surfaced to `0.0.0_AB_MSTR~Z` (msg at 21:13:12Z)
as a loss risk, deliberately WITHOUT prescribing a commit, since an uncommitted edit may be a peer's
in-flight work and `.claude/` is not mine to write.

### CLOSED: owned in-flight work, and my own loop is now bound by its output

`0.0.0_AB_MSTR~Z` msg 33781 (acked): the receipt is **`0.7.0_AE_CloudOps~ZT`'s in-flight Z6 R5**,
order `org/tier2_senior/0.7.0_AE_CloudOps~ZT/task_orders/OPAL_BBGTML.TO-Z6-R5.teams-armed-stdout-receipt.md`,
issued by `2.0.0_SA_COO~ZB` @6338955a02 on CTO~Z ruling @61e3067f5c disposition 5, WORLD risk. The
order names exactly the two files I measured, and **its deploy-ledger leg L1 IS the commit of them**
-- so the working-tree-only state is a mid-act step the order closes, not an orphan. COO~ZB drains it.

**My loss-risk framing was wider than the mechanism warranted.** I wrote "a tree reset would lose
them"; MSTR~Z's answer is that no pass of its own resets a tree and **box-sync refuses rather than
overwrite a seat's uncommitted edit.** True for a deliberate reset, but I named a risk without first
asking what already protects against it -- the cautious direction again, and it still costs a peer a
read. **Surfacing the unknown ownership was right; attaching a risk I had not checked was not.**

**THE NEW RULE BINDS ME, and it supersedes my own workaround.** The pending `SKILL.md` edit adds:
*"THE ARM PROOF IS THE STDOUT RECEIPT, NOT THE BANNER ... Read it as the ARM RECEIPT, never as a
message: no ACK, no reply, no cursor effect, no serve loop ... No `[TEAMS-ARMED]` event within 60
seconds of an arm means the watcher did NOT arm -- census the process rows, then re-arm. A silent arm
is a deaf seat, not a quiet one."* Required fields: `identity=517aa5ee-...` (never `BARE`) and
`channels=1` (0 = unwatched tickets channel).

**Compliance checked rather than assumed, on the live arm `b7my8ava9`:** receipt read
`identity=517aa5ee-b4d0-425a-b493-5a22ff77ac4f channels=1` -- **PASSES both limbs**. And I handled it
correctly before the rule existed: I ran no serve loop, sent no ack and touched no cursor on it,
treating it as an anomaly to investigate. **Going forward every re-arm owes the 60-second receipt
check.**

⚠ **DO NOT apply the 60-second rule backwards to this session.** The three earlier arms
(`bodbap82m`, `bx0sfv9x4`, `b911j0y5z`) emitted no receipt and WERE armed -- they delivered real
messages. They predate the code. A rule read against bytes that did not contain it manufactures
three false failures, which is the same mistake as the near-confession above pointed the other way.

**My re-arm command does not change:** `SKILL.md:35` is byte-identical between HEAD and the working
tree (both read, diffed). The edit is documentation around it.

### First re-arm under the new contract: PASSES, and the receipt's `cursor=` field does extra work

Arm `bi9nlopia` 21:37:20Z. Receipt arrived within seconds:
`[TEAMS-ARMED] pid=36776 identity=517aa5ee-b4d0-425a-b493-5a22ff77ac4f channels=1 cursor=2026-10-13T20:16:44.498Z`.
**Both limbs pass** (identity pinned not `BARE`; `channels=1` not 0), and the census agrees exactly:
one row, pid **36776**, parent the `timeout` wrapper. Handled as a receipt -- no ack, no reply, no
serve loop. **This is the first arm in the session whose health is provable from INSIDE the session;**
the four before it were armed and unprovable, which was the whole finding.

⭐ **A use of the receipt the SKILL.md edit does not name: its `cursor=` field proves the re-arm gap
lost nothing.** The Teams watch was down from its 21:37:0xZ `exit 124` to the 21:37:20Z re-arm. The
receipt reports `cursor=2026-10-13T20:16:44.498Z` -- unchanged from before the gap and still my own
20:16:44Z send -- so **the cursor did not advance while the watch was dead, and the new arm re-polls
everything after it.** That converts "was anything missed during the re-arm hole" from a question
needing a separate poll into a field I am already being handed. Same latency-not-loss property as the
token lapse, read off a different instrument. **Caveat on scope: this holds for the DM/group cursor
only** -- the channel leg keeps its own cursor file and the receipt's single `cursor=` does not speak
for it.
