# HANDOFF TO 4.0.0_SA_CRO -- the strategy brief for four devices (laptop, sitez, dell1, dell2)

From `1.0.0_SA_CTO`, clock read 00:51Z 2026-10-06 (evening of 2026-10-05, Eastern). Andrew will task the brief himself; this is the
context he asked this seat to hand over. It orders nothing.

## Andrew's words

"We are going to be adding two new dells, i will call these boxes dell1 and dell2, akin to this box being laptop, and bbg terminal
being sitez. We need to figure out our strategy for when there are two additional boxes working in parallel, i will task CRO with
the brief." Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0051Z_NEW_DEVICE_ZIP_DELL1_DELL2_AND_CRO_HANDOFF.md`.

## What exists today

- **A new-device kit:** `C:\Users\AndrewBerman\Desktop\Opal_New_Device_Kit_20261005.zip` (34 files; its `README_NEW_DEVICE.md`
  is the bring-up order, and `TOOL_VERSIONS_LAPTOP.txt` is this laptop's tool versions). It covers standing a box up. It does
  not cover how four boxes work together; that is the brief.
- **Two devices run the fabric now:** `laptop` and `sitez` (the Bloomberg terminal box).

## How the two-device fabric works now (each line names where to read it)

| Mechanism | Today | Read at |
|---|---|---|
| Trunk | both devices commit to branch `CLOUD`; `SITEZ` is retired | `org/XXX.md` Step 1b; `CLAUDE.md` section Git |
| Pushes | only `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z` push a shared branch, on Andrew's word while he is at the terminal | `org/XXX.md` Step 1b (LD-0367, LD-0368, LD-0522, LD-0613) |
| Parity between devices | the `/integrate` skill, "the two devices on ONE TRUNK" | `.claude/skills/integrate/SKILL.md` |
| Messaging inside a device | one broker per device on `localhost`, port 7800; tradeops is a second fabric on 7801 | `org/mcp/server.py`; the laptop's PowerShell profile |
| Messaging across devices | the agent bus (one inbound queue per device), relayed by each device's fabric manager | `.claude/skills/agentbus/SKILL.md` |
| Device identity in a serial | a lane suffix: site-Z seats are `~Z`, `~RV`, `~X`, `~H` and so on; the laptop's are `~P`, `~M`, `~Y`, `~D` | `org/ref/LIVE_ARMS.md` |
| Which device a directive lives on | each directive carries a placement | `org/missions/DIRECTIVES.yaml` |
| Per-device records | audit archive folders by device name; open-deploy ledgers read per worktree | `org/audit/archive/<device>/`; `CLAUDE.md` section 5 |
| No device-specific code | paths are derived, never hardcoded; `OPAL_WS_ROOT` is the one device-level override | `CLAUDE.md` section 5 (LD-0405); `.tools/ajb.ps1` header |

## Measured on the laptop today (this seat, 2026-10-05)

- 31.7 GB RAM, 8 cores. With six sessions live (fabric manager, CTO, CVO, CRO and two COO lanes) 15.5 GB was free and CPU
  sat near 26 percent. Andrew's standing limit is three COO lanes on the laptop; he allowed a fourth today by name.
- Disk: 37.6 GB free on C:. A full worker checkout costs about 2.35 GB, and worker worktrees are the recurring disk pressure.
- The laptop was 5 commits ahead of origin `CLOUD` at restart (the fabric manager's reading) and is 149 ahead now (`git rev-list` against the local origin ref); origin has not moved since (ls-remote 01a47ac2e7).

## What the brief has to settle (questions, not answers)

1. **What the Dells are for.** More lanes of the same projects, whole directives moved onto them, or dedicated jobs (worker
   pools, builds, the resident host's kind of work).
2. **Naming.** How `dell1` and `dell2` appear in serials, in the audit archive, in directive placement and on the agent bus.
3. **The trunk.** Two devices already need a deliberate push-pull to stay in parity. With four, who pushes, how often, and what
   stops four local `CLOUD` branches drifting hundreds of commits apart.
4. **One issuer per round.** A project's round has one issuing COO. Can a round's workers sit on a different box from its issuer,
   given a worker cannot be messaged and shares files, not messages?
5. **Messaging.** Four brokers and four fabric managers relaying over the bus, or one shared broker. The broker is
   localhost-only today.
6. **Deploys and served output.** Open-deploy ledgers sit on the deploying device's branch until drained; with four boxes a seat
   can no longer see every open deploy by reading its own tree.
7. **Scarce vendor seats.** Bloomberg has one Terminal seat (site Z) and a daily quota that ran out today. YCharts has evicted
   sessions on a shared account. Yahoo pulls are unofficial. Four boxes must not multiply calls on any of them.
8. **Credentials and identity.** Each box signs in separately. Whether each has its own AWS identity matters to every audit
   trail that records who acted.
9. **Andrew's attention.** Sovereign words are given at a terminal and relayed. With four terminals, where he speaks and how a
   word reaches the right box.
10. **Limits and failure.** Seat limits per box; what happens to a round when the box running it reboots.

## Not known to this seat

The Dells' hardware, their network location, whether they sit behind the same accounts, and when they arrive.

-- 1.0.0_SA_CTO
