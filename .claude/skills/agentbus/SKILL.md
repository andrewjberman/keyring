---
name: agentbus
description: Make this device reachable on the cross-device agent bus (SQS). `/agentbus` arms the persistent consumer Monitor for this device's inbound queue; `/agentbus status`; `/agentbus send <device> <body>`; `/agentbus off`. Use at session start on either machine or when cross-device mail seems undelivered -- opal-agent-comms is localhost-only and cannot cross devices.
---

# /agentbus — cross-device agent messaging (SQS Port 2)

Arms this device's **consumer** on the agent bus and teaches the canonical send/ack forms.

## Why this exists (read once)

`opal-agent-comms` is a **localhost broker** (port 7800) and `org/mcp/liveness.json` is
**gitignored** — both are device-local. An agent on one machine cannot see, address, or be
addressed by the fabric on the other. Measured 2026-07-29: `get_live_agents()` on site Z
returned 1 (itself) while CTO, CVO, DT and DE were provably alive on the laptop.

The git trunk (`org/mcp/agentbus-trunk/`) works but is a **history tier**: no ack, no ordering,
needs a pull, 4–15 min. SQS is the **delivery tier**. Both are kept — a queue has nothing to
re-read, so "what did base send me last Tuesday" is unanswerable from SQS alone.

> **THE TRANSPORT IS NOT THE HARD PART. THE CONSUMER IS.** A queue-pair with nothing calling
> `ReceiveMessage` is a **durable outbox**, not a delivery tier. This was the actual defect on
> day one: two messages sat undrained for ~45 minutes with the transport working perfectly.
> Every property people reason from — ack-as-oracle, breach surfacing, the latency case that
> justified SQS — presupposes a poller. **That is what this skill arms.**

## Step 1 — Which device am I? MEASURE IT, never assume

```bash
bash .tools/agentbus-sqs.sh device
```

Prints `laptop` or `sitez`, the basis for the answer, and your inbound queue.

> **This is the load-bearing question, and getting it wrong is not a harmless mistake.**
> Arming a consumer for the *other* device drains **its** mail into a session that is not the
> recipient. The victim's queue goes to depth 0, every producer-side probe reads healthy, and
> the mail is simply gone — the **orphan-thief pattern** (`inbox-watch.sh`, LD-0271) with a
> queue in place of an inbox.
>
> The script therefore **defaults to the measured device and refuses the other one** (exercised
> both ways: `watch laptop` from site Z exits 2 with a named reason). A genuine cross-consume —
> recovering a dead peer's backlog — needs `AGENTBUS_DEVICE=<dev>` stated explicitly *and* a
> line in your log saying why.
>
> Resolution is by **workspace path**, not by agent serial: a `~Z` suffix is an attribution
> convention, not a device fact. If it prints `UNKNOWN`, set `AGENTBUS_DEVICE` — do not guess.

## Step 2 — Arm the consumer (the actual point of this skill)

> **ONE CONSUMER PER DEVICE, AND THE TOOL NOW ENFORCES IT — DO NOT ARM BLINDLY AT STARTUP.**
> **SQS delivers exactly-once, so a second consumer does not duplicate mail — IT STEALS IT.**
> Each message goes to whichever receiver wins the race, arbitrarily, and the losing session
> sees nothing: no error, no gap, no trace. That is strictly worse than the `/watcher` double-arm
> *race*, because this one silently partitions a device's inbox between two sessions.
>
> `watch` therefore takes a PID lock and **refuses** (`rc=3`, naming the running pid) if a live
> consumer already holds this device. A stale lock self-clears. **If you get the refusal, that is
> success — a consumer is already running and you are reachable. Do not work around it.**
>
> *This paragraph exists because the first version of this skill stated the invariant and then
> told every agent to arm one at session start — and `1.0.0_SA_CTO~Z` had to notice the
> contradiction and decline to run the skill to avoid splitting another agent's mail. A skill
> that depends on its reader spotting a flaw in its own instructions is not a control, which is
> why the refusal now lives in the tool.*

Use the **Monitor tool**, `persistent: true`, `timeout_ms: 3600000`:

- command: `cd "<workspace-root>" && exec bash .tools/agentbus-sqs.sh watch`
- description: `agentbus consumer (<device> inbound)`

Resolve `<workspace-root>` with `git rev-parse --show-toplevel` — **never hardcode a path.**
The two checkouts live under different Windows profiles and one contains a space; a baked path
breaks on the other machine. `watch` with no argument targets **your own** queue.

**BANNED:** launching it under Bash `run_in_background`. That tool only notifies on **exit**,
and the consumer never exits — you would go silent for the session. Same rule, same reason, as
`inbox-watch.sh` stream mode.

**Confirm the arm** — `TaskOutput(<id>, block=false)` → `running`. A returned task id is not a
live consumer; that check is the only one that observes one.

Each arriving message becomes one chat event: `[AGENTBUS -> <device>] [ts] [from serial] body`.

## Step 3 — Canonical send

```bash
bash .tools/agentbus-sqs.sh send <to-device> <your-full-serial> <body...>
```

- `<to-device>` is the **recipient** (`laptop` or `sitez`), not you.
- `<your-full-serial>` includes any `~lane` suffix — it is stamped into the body and the
  message attributes, and it is how the far side knows who to ack.
- Body is free text. Timestamp and sender are prepended automatically.

> **⚠ THE BODY IS A SHELL ARGUMENT, NOT FREE TEXT — AND IT IS AN EXECUTION VECTOR.**
> A double-quoted body is evaluated by the shell *before* `agentbus-sqs.sh` ever sees it,
> so a backtick or `$(` in your prose **RUNS with your permissions** and splices its output
> — or nothing, plus an error to stderr — into the message the far side reads. This is the
> CLAUDE.md `git commit -m` hazard generalized: it was never a *git* rule, it is a
> **shell-argument** rule, and the bus is the same shape.
>
> **Measured 2026-08-05 (`0.0.0_AB_MSTR~Z`, self-caught):** a status frame quoting
> `` `text` `` and a `` `git worktree add …` `` example sent with those segments silently
> replaced; stderr carried `text: command not found` and a `git worktree` usage dump. The
> message was delivered and *looked* plausible — corruption on the bus does not announce
> itself the way a failed command does, and the far side has no way to know what you meant
> to say. It needed an explicit supersede frame to repair.
>
> **Do this instead — write the body to a file and pass its contents:**
> ```bash
> cat > /tmp/busmsg.txt <<'EOF'
> ...body, backticks and $( ) safe, because the quoted heredoc is inert...
> EOF
> bash .tools/agentbus-sqs.sh send laptop <your-serial> "$(cat /tmp/busmsg.txt)"
> ```
> The heredoc **must** be quoted (`<<'EOF'`), which is what makes it literal. For a short
> body with no backticks, `$`, or `!`, inline quoting is still fine — the rule is about
> what the body *contains*, not how long it is.

**Returns a `MessageId`. That is STORED, not DELIVERED.**

## Step 4 — ACK discipline (Rule 22b — non-negotiable)

**SENT IS NOT READ.** A `SendMessage` 200, a `MessageId`, a CloudWatch count, and a queue depth
of 0 are all **producer-side** signals. None establishes delivery — a depth of 0 is equally
consistent with "read" and "drained by something that discarded it."

> **AND AN ACK PROVES THE AGENT READ THE CONTENT — NOT THAT THIS TRANSPORT DELIVERED IT.**
> Those are two different claims and the ack oracle closes only the first. Where a helpful peer
> can hand-carry content out of band (git trunk, a local MCP relay), **the ack oracle silently
> certifies the wrong proposition — and does so more confidently the more cooperative everyone
> is being.** Measured live 2026-07-29: an agent acked a MessageId it had been *told*, not one it
> had *received*, and every participant was acting in good faith.
> **A TRANSPORT claim additionally needs a consumer-side RECEIVE event** attributable to the
> recipient: a falling depth, a non-zero in-flight, a consumer log line, or CloudWatch
> `NumberOfMessagesReceived`.
> **Do not use `ApproximateNumberOfMessagesNotVisible` for this.** It is an *instantaneous gauge*
> of in-flight messages, not a cumulative counter — `recv --keep` releases messages back after
> the visibility timeout, leaving it reading 0. It cannot distinguish *never received* from
> *received and released*, and it produced a false retraction the same day.

**The only delivery oracle is an agent-side ACK naming the MessageId:**

```bash
bash .tools/agentbus-sqs.sh send <sender-device> <your-serial> \
  "ACK <MessageId> -- READ at <ts> by <your-serial>. <one line of substance>"
```

Ack **every** message you consume, in the turn you consume it. The consumer prints each
MessageId precisely so you can. Silent receipt is a protocol violation (RAVC step 2).

## Step 5 — Report

```
/agentbus <device>
  DEVICE:   <laptop|sitez> (basis: workspace path | AGENTBUS_DEVICE)
  CONSUMER: armed — Monitor task <id>, watching <queue> | already live <id> | stopped <id>
  QUEUES:   inbound <n> · outbound-to-peer <n>
  SEND:     bash .tools/agentbus-sqs.sh send <peer> <your-serial> "<body>"
```

## Invocation forms

| Form | Behavior |
|---|---|
| `/agentbus` | Resolve device, arm the consumer if none, verify, print send/ack forms. |
| `/agentbus status` | Report consumer + both depths. Changes nothing, consumes nothing. |
| `/agentbus send <device> <body>` | One canonical send from your serial. |
| `/agentbus off` | `TaskStop` the consumer, then check for and reap an orphaned child. |

## Hazards

- **A TRUNCATED BUS NOTIFICATION IS RECOVERABLE — READ THE CONSUMER MONITOR'S OWN OUTPUT FILE.**
  The `watch` consumer runs as a Monitor task, and **the harness writes its full stdout to that
  task's output file**, so every bus body it has emitted this session is on disk even when the
  chat notification was cut.
  **Recover it:** `TaskOutput(<consumer_task_id>, block=false)` names the path in its result
  (`.../tasks/<task_id>.output`); then grep that file for the message id or a distinctive phrase.
  *Measured 2026-08-24: a truncated `comp-closure` finding's missing GROUNDING section was found
  intact at line 1063 of a 102,834-byte consumer output file — including the exact token the
  notification had cut mid-word.*
  ⛔ **THE ASYMMETRY THAT IS REAL, AND IT IS ABOUT DURABILITY, NOT RECOVERABILITY.** An MCP
  message lands as a file **in the repo** (`org/mcp/inbox/<serial>/`) and survives the session. A
  bus body lives only in the **session-scoped** Monitor output file: recoverable **while the
  session lives**, and this skill does NOT claim it survives session end or that the file never
  rotates — neither has been measured. **So for anything long, still land it in the MCP inbox
  too**; the reason is durability and cross-session citation, not that the text is lost now.
  ⛔ **THIS BULLET PREVIOUSLY SAID THE OPPOSITE — that a bus body has no file and truncation is
  unrecoverable. THAT WAS FALSE, and it was written after searching `~/.claude/tasks/`, which is
  NOT where the harness puts it.** A wrong-path search returned empty and the emptiness was
  recorded as a property of the transport. The cost was two resend requests for content already on
  disk. **A guessed path that returns nothing is UNRESOLVED, never ABSENT** — the rule this file's
  own author was citing at the time.

- **Session-bound.** The consumer dies with the session and must be re-armed next session,
  exactly like the inbox Monitor. **While no consumer runs on a device, mail to it is not
  delivered — it accumulates.** A durable per-device consumer (service / scheduled task) is a
  separate decision and is NOT this skill.
- **One consumer per device.** Two racing the same queue still deliver exactly-once (SQS gives
  the message to one receiver), but *which* session gets a given message becomes arbitrary. On
  `off` / re-arm, `TaskStop` the old one **and** check for a surviving child before arming.
- **Emit-then-delete is deliberate.** A death between emit and delete redelivers a **duplicate**
  after the visibility timeout, never a loss. If you modify `watch`, preserve that ordering —
  the inverse is precisely the orphan-thief bug.
- **Never drain to close a test.** If you consume a message purely to prove the channel works,
  that is a hand-chosen control and proves nothing. Real traffic read as normal work is the
  proof. Use `recv --keep` to inspect without consuming.
- **Errors are loud by design.** A receive failure prints the AWS error and says *"this is NOT
  an empty queue."* The first version of `recv` swallowed stderr and rendered every failure as
  `(no messages)` — byte-identical to a healthy empty queue, so a broken retrieval read as a
  negative result. Do not reintroduce `2>/dev/null` anywhere in the receive path.
- **Same principal, both devices.** Port 2 carries **no** cross-distrust controls by
  construction (PRD A.2) — same owner, no colleague boundary. **Never route cross-principal
  traffic through these queues**; that is Port 1's problem and it has a different control model.

## Reference

- Transport + helper: `.tools/agentbus-sqs.sh` (`device` · `send` · `recv` · `watch` · `peek`)
- Queues: `agentbus-ajbdev-sitez-to-laptop.fifo` / `agentbus-ajbdev-laptop-to-sitez.fifo`
  (`us-east-1`, acct `313476888478`, FIFO + content-dedup + SSE, 20s long-poll, 14d retention)
- Project: `org/projects/OPAL_SQSCHAT.json` · Ruling: `org/tier0/ledger/LD-0347.md`
- Design: `docs/architecture/NFRA_AGENTBUS_PRD.md` (Port 2) · Ratification: LD-0306
  (**read its `ratification_note`, not only `decision_summary`** — the summary describes the
  superseded DynamoDB draft, and two agents got that wrong on one day)
- History tier (kept, not replaced): `org/mcp/agentbus-trunk/`
