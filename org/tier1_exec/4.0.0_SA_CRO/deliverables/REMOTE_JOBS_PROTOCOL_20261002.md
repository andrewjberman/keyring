# Remote jobs -- ad hoc work from Teams, dispatched to the least-loaded MSTR (the protocol)

Andrew-direct 2026-10-02 ~16:4xZ-17:0xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md` (newest addendum):
a Teams request for small work (a bug fix, a Lambda redeploy) becomes a job when Andrew says so; the job goes to the
agent bus; the MSTR agents online bid with availability, then CPU/memory; the winner sends a `2.0.0_SA_COO~{N}` with
`/remote-drive`; the requester hears "I'm on it"; the job closes when the requester confirms it works.

Two halves build against this file and nothing else: LDO-001 (`data/transcripts/scripts/teams_chat/tenant.py`, the
cloud side) and the device side (`.tools/remote-job.py`, `.claude/skills/remote-drive/SKILL.md`).

## Names

| Thing | Value |
|---|---|
| Job id / SMS tag | `J` + three digits (`J042`), stable for the job's life |
| Job object (LDO-001) | `job:J042` |
| Devices | `laptop`, `sitez` (the agent bus's two; `.tools/agentbus-sqs.sh device` resolves which one you are) |
| Bus queues (device inbound) | laptop `agentbus-ajbdev-sitez-to-laptop.fifo`, sitez `agentbus-ajbdev-laptop-to-sitez.fifo` |
| Bus message shape | as `agentbus-sqs.sh send`: group `opal-sqschat`, attributes `from`, `sent_at`, body `[<ts>] [from LDO-001] <text>` |
| LDO-001 mailbox (devices -> cloud) | `teams-global-chat-assist-queue.fifo`, via `ldo.Runtime(...).send("job:J042", <kind>, <payload>)` |
| Bid window | 120 seconds from the offer, or sooner once both devices have bid |

## Bus messages, cloud -> device

Every one is a single body: one human line, then one line `REMOTE-JOB-JSON <json>`. The listener shows both.

| Type | Sent to | Human line | JSON adds |
|---|---|---|---|
| `offer` | every device | `REMOTE-JOB OFFER J042 -- <one-line ask>. Bid within 120 s: python .tools/remote-job.py bid J042` | `brief`, `requester`, `chat_title`, `deadline` |
| `award` | the winner | `REMOTE-JOB AWARD J042 -- yours. Spawn a 2.0.0_SA_COO~<N> with /remote-drive J042, then: python .tools/remote-job.py accept J042 --coo <serial>` | `brief`, `requester`, `chat_title` |
| `lost` | every other bidder | `REMOTE-JOB LOST J042 -- awarded to <device>. Nothing to do.` | `winner` |
| `close` | the winner | `REMOTE-JOB CLOSE J042 -- the requester confirmed it works. The COO writes /log tagged adhoc-remote-job; MSTR reaps it.` | `confirmed_by` |

JSON always carries `{"type", "job", "ldo": "LDO-001", "sent_at"}`.

## LDO events, device -> cloud (to object `job:J042`)

| Kind | Sent by | Payload |
|---|---|---|
| `job.bid` | MSTR, `remote-job.py bid` | `{"device", "serial", "available": bool, "cpu_pct", "mem_pct", "at"}` |
| `job.accepted` | MSTR, `remote-job.py accept` | `{"device", "serial", "coo"}` |
| `job.complete` | MSTR, `remote-job.py complete` | `{"device", "serial", "summary", "deployed": bool, "evidence"}` |
| `job.failed` | MSTR, `remote-job.py fail` | `{"device", "serial", "reason"}` |

`available` is false when this device already runs a remote job (its lock file `.tools/.remote-job.json` names an
open job), and true otherwise. CPU and memory are psutil's `cpu_percent(interval=1)` and `virtual_memory().percent`.

## The award rule

Only `available` bids count. None means the job is PARKED and Andrew is texted. One means that device wins. Two or
more means the lowest `(cpu_pct + mem_pct) / 2` wins; a tie goes to the earlier bid. Bids after the award are
ignored, and the bidder gets `lost`.

## Andrew's texts on a job (the J tag)

| Text | Meaning |
|---|---|
| `C042 #dev <notes>` (or `#dev <notes>` for the newest draft) | open a job from that chat; the chat's pending draft is dropped |
| `J042 1` / `J042 0` / `J042 <notes>` | send / hold / redraft the completion message to the requester (the standing rule: nothing goes to Teams without his 1) |
| `J042 #close` | close the job now (as if the requester confirmed) |

"I'm on it" goes to the requester without a further 1: Andrew's `#dev` is that message's approval (his words).

## The sequence

1. `#dev` on a chat -> `job.open` on `job:J042`: Kimi writes the brief (what is asked, who asked, which function or
   page, how the requester will check), Andrew is texted the brief's first line, `offer` goes to every device, an
   alarm fires the award at 120 s.
2. Each MSTR with its bus listener armed runs `remote-job.py bid J042`.
3. Award -> `award` to the winner, `lost` to the rest, Andrew texted where it went.
4. The winning MSTR spawns `2.0.0_SA_COO~<N>` with `/remote-drive J042` (the brief is in the award JSON;
   `remote-job.py show J042` writes it to a file) and runs `remote-job.py accept`. -> "I'm on it" to the requester.
5. The COO runs `/remote-drive`: identify the function the requester means, `/closer trace` it, `/atom-decomp` the
   relevant surfaces, do the work, validate it on the real artifact, deploy through the normal gates if the fix needs
   it, and report to its MSTR (MCP) with the evidence.
6. MSTR runs `remote-job.py complete` -> Kimi drafts the message to the requester -> texted to Andrew under J042.
7. The requester's next message that confirms the fix (Kimi reads it), or Andrew's `J042 #close` -> `close` to the
   winner -> the COO writes `/log` tagged `adhoc-remote-job`; MSTR reaps it.

A job is small by definition: not registered, no PRD, no task orders. Deploys still run through `safe-deploy` /
`safe-apply` and a change-management ledger (CLAUDE.md NEVER-2).
