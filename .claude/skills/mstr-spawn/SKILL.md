---
name: mstr-spawn
description: MSTR-only event-triggered skill — provision a new agent session by serial via spawn-agent.ps1, with concurrency-cap pre-check, optional first-message direction, broker-registration verification, and audited bypass for legitimate overflow. Sibling to /mstr-kill.
---

# /mstr-spawn — provision an agent session

MSTR's structural mechanism for **population creation**. The invocation
`/mstr-spawn {serial}` IS the per-instance authorization within skill body for
spawning a session; `/mstr-spawn {serial} --force "<reason>"` is the
charter-blanket authorization for the audited concurrency-cap overflow path
(parallel to /mstr-kill's blanket force-kill authorization). Only `0.0.0_AB_MSTR`
invokes it.

> **Spawn != dispatch** (Constitution Art. VI). This skill provisions the
> session. Direction still flows through Tier 1. A first-message hint via
> `--say "<text>"` is allowed for fast-orient (see SPAWN-WITH-DIRECTION
> canonical pattern, memory `feedback_spawn_with_direction_fast_orient_pattern`)
> but the substantive TO/charter authoring stays at Tier 1.

## When to invoke

- Andrew direct: `/mstr-spawn {full-agent-serial}` — symmetric to `/mstr-kill`; covers initial provisioning + respawn after kill.
- MSTR autonomous: population action arising from `/mstr-review` scan (unaddressed work surface, wrong-mix swap, FORK-STALLED SPAWN-WITH-DIRECTION fallback per /govern Step 4 table) — LD-charter governs; ledger LD-NNNN before invocation per Stakes Matrix (spawn is S1 per spawn-agent.ps1 line 19).
- Never invoked by any agent other than `0.0.0_AB_MSTR`.

---

## Step 0 — Parse + identity gate

Parse the argument:
- Must be a full agent serial matching `^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$`.
- Tilde-lane suffixes (`~B`/`~C`/`~D`) included as needed — they are distinct sessions from the base serial.
- Optional flags:
  - `--say "<text>"` → first-message hint appended to ajb invocation (SPAWN-WITH-DIRECTION pattern; max ~200 chars to keep CommandLine sane).
  - `--force "<reason>"` → audited concurrency-cap bypass; mandatory reason string.

**Identity gate:** confirm caller is `0.0.0_AB_MSTR` (`$env:OPAL_AGENT_SERIAL` / `.comp-graph/.agent_context`). Non-MSTR invocation halts here with an error.

## Step 1 — Pre-flight checks

Three checks before spawning. Each surfaces as a clean refuse-with-reason rather than an opaque script error:

### 1a — Already-live check

```
mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
```

If `LIVE` AND last seen < 120s → **a session already exists**. Default action: **refuse the spawn** (avoid double-provisioning the same serial; CommandLine marker scan would detect the second window as a v1-marker-collision risk). Surface to Andrew: "{serial} already LIVE at PID {pid}; spawn would create a duplicate. Kill first via `/mstr-kill {serial}` or pass `--force "intentional-duplicate"` if a duplicate is intended."

If `STALE` / `NOT_REGISTERED` / not found → safe to proceed.

### 1b — Marker scan

```powershell
Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object { $_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1: {serial}*" }
```

Catches the gap that 1a misses: a session whose process is alive but broker is `STALE` / unregistered (post-window-exit-pre-deregister, or a registration failure). If a marked window exists for this serial → refuse with the same surface (treat as duplicate).

This double-check is the cheap defense against a class of cap-evasion bug where the broker says STALE but the PowerShell window is still alive holding a concurrency-cap slot.

### 1c — Concurrency-cap headroom (informational; spawn-agent.ps1 enforces)

```powershell
$live = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object { $_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1*" }).Count
```

If `$live >= 16` → spawn-agent.ps1 will reject. Either kill an idle session first (`/mstr-kill {idle-serial}`) OR re-invoke with `--force "<reason>"` (audited bypass).

Surface the count in the Step 6 report regardless — useful context for population-management decisions.

## Step 2 — Spawn

```powershell
.tools\spawn-agent.ps1 {serial} [<say-text>]
```

If `--force "<reason>"` was passed, set the env var first:

```powershell
$env:FORCE_SPAWN = "<reason>"
.tools\spawn-agent.ps1 {serial} [<say-text>]
$env:FORCE_SPAWN = $null
```

The script:
- Loose serial sanity check (regex match).
- Concurrency rate cap (3/spawner/60s, 5/global/60s) — only enforced when `$env:OPAL_AGENT_SERIAL` is set (MSTR-as-spawner case — that IS this skill's case).
- Live-window cap (16 simultaneous).
- Both caps bypassable via `FORCE_SPAWN` env var with reason → writes `FORCE-SPAWN` line to audit log.
- Opens new detached PowerShell window via `Start-Process powershell -NoProfile -NoExit`.
- Dot-sources `.tools\ajb.ps1`; runs `ajb -Headless {serial} [extra]`.
- `-Headless` drops the `--dangerously-load-development-channels` flag (memory `feedback_spawn_drop_dev_channels_flag` — silent-ignore per server.py:299-300).
- Appends `SPAWN` audit line to `org/mcp/agent-spawn-audit.log`.
- Marker `# OPAL_SPAWN_MARKER_v1: {serial}` baked into the spawned window's CommandLine (kill-tracking + cap-counting contract).

**Read the script's output:**
- `[spawn-agent] launched {serial} in a new window` → success. Continue.
- `spawn-agent: ... cap exceeded` → cap rejection. Either re-invoke with `--force` OR kill an idle session first. Surface in report; do not silently retry.
- `spawn-agent: 'X' does not look like an agent serial` → typo. Surface to Andrew; do not retry.

## Step 3 — Wait + registration verify

The spawned window takes ~10-30s to: launch PowerShell, dot-source ajb, start `claude`, run startup protocol per `org/XXX.md`, register with broker. Wait for registration, do not assume immediate.

Polling loop (max 60s, 5s interval):

```
for attempt in 1..12:
  status = mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
  if status.liveness == "LIVE":
    break
  sleep 5s
```

Expected: `LIVE` within ~30-45s. If still not LIVE at 60s, the spawn may have failed silently (claude crashed, ajb path missing, dev-channels flag not dropped, startup loop hung). Surface to Andrew with diagnostic context (marker scan, last few lines of any visible window output if accessible). Do not retry-spawn — investigate root cause first (memory `feedback_spawn_drop_dev_channels_flag` is the most common historical cause and is already addressed by `-Headless`).

## Step 4 — Optional first-message direction

If `--say "<text>"` was passed AND the agent registered LIVE, send the directing message via broker:

```
mcp__opal-agent-comms__send_message(
  to="{serial}",
  from="0.0.0_AB_MSTR",
  subject="[MSTR-DIRECT] startup hint",
  body="<text>"
)
```

This is the SPAWN-WITH-DIRECTION fast-orient pattern (memory `feedback_spawn_with_direction_fast_orient_pattern`) — empirically ~40min from spawn to first substantive RAVC2-Request when the bootstrap message lands at agent startup with the chosen path baked in. The agent's `/watcher` Step 5 inbox-pull picks it up on the first cycle.

Note: the `--say` text already went into the ajb invocation extras (Step 2). The send_message is the **broker-side** counterpart — robust against the agent missing the CommandLine extras during early startup. Belt + suspenders.

## Step 5 — Verify-after

Confirm population state matches intent:

```
mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
mcp__opal-agent-comms__get_live_agents()
```

Expected: `{serial}` appears in `get_live_agents` output, broker `liveness=LIVE`, last_seen < 60s. If `--say` was sent, the message should be in the agent's read or unread inbox depending on whether the watcher fired.

## Step 6 — Report

Print the fixed report:

```
/mstr-spawn {serial}
  PRE-CHECK:    no-duplicate | marker-clean | concurrency {N}/16
  SPAWN:        launched (script said: ...) | FORCE-SPAWN reason="<>" | rejected reason="<>"
  REGISTER:     LIVE after {N}s | NOT-LIVE after 60s (INVESTIGATE)
  DIRECTION:    --say sent via broker | (none)
  AUDIT:        org/mcp/agent-spawn-audit.log
```

Then surface any population-context the spawn affects — concurrency count after, which workstreams the new session is expected to take up, any TOs that should now flow via Tier 1 to the freshly-provisioned session. This is the LD-0074 generalized lesson: a spawn is a population state change with routing implications, not just a process action.

---

## Discipline / risk notes

- **Per-invocation scope.** One `/mstr-spawn` = one spawn of one serial. A second spawn same turn = a second invocation. Skill is not a session-wide spawn license.
- **--force scope.** The `--force "<reason>"` blanket-authorizes ONE FORCE-SPAWN audit line. It does not lower the cap; it bypasses it for one spawn with forensic record. Outside this skill, FORCE_SPAWN still requires explicit Andrew per-instance auth or new LD-charter.
- **Spawn != dispatch.** Constitution Art. VI: MSTR provisions the session; TO authoring and direction flow through Tier 1. `--say "<text>"` is a startup-orient hint (the SPAWN-WITH-DIRECTION pattern when the direction is already worked out — e.g., a CORROBORATE/COUNTER verdict to execute), not a TO body. Substantive direction at agent-startup should be a Tier-1-authored TO/inbox message; `--say` is the bootstrap hint that tells the agent which TO to read first.
- **Already-live default = refuse.** Avoids double-provisioning the same serial which would create a marker-collision and confuse `/mstr-kill` and the concurrency cap. Override via `--force "intentional-duplicate"` if a duplicate is genuinely needed (rare; e.g., a tilde-lane spawn under a different lane suffix is the normal pattern instead).
- **Registration timing.** ~30-45s is normal first-time spawn latency. Do not retry-spawn before 60s — the first attempt may still register. Premature retry is how cap exhaustion happens.
- **Self-spawn.** MSTR spawning MSTR (`/mstr-spawn 0.0.0_AB_MSTR`) is legitimate (e.g., after a self-kill or a crashed prior session); no `--self-ack` flag needed for spawn (the symmetry with `/mstr-kill --self-ack` is intentional — kill ends a session, spawn creates one, only the destructive direction needs the extra confirmation).

## Cross-references

- `.tools\spawn-agent.ps1` — the underlying spawn mechanism + concurrency caps + audit (Step 2).
- `.tools\kill-agent.ps1` + `/mstr-kill` — sibling destruction primitive; spawn/kill are paired population primitives per LD-0069 + Andrew architectural ruling 2026-05-22.
- `org/mcp/agent-spawn-audit.log` — forensic trail for SPAWN / FORCE-SPAWN / REJECT / KILL / FORCE-KILL / KILL-NOOP / WARN.
- LD-0061 (fabric-wide kill empirical; companion population-action context).
- LD-0069 (MSTR thin architecture; `/mstr-spawn` listed as event-triggered skill — this materializes it).
- LD-0070 (telemetry-derived liveness; will tighten Step 3 registration polling once Phase 2 lands).
- LD-0075 (`/mstr-kill` skill scribe; this skill mirrors its structural pattern).
- Memory `feedback_spawn_drop_dev_channels_flag` (the `-Headless` flag rationale — silent-ignore push mechanism per server.py).
- Memory `feedback_spawn_with_direction_fast_orient_pattern` (SPAWN-WITH-DIRECTION canonical anchor; the `--say` flag use case).
- Memory `feedback_mstr_creator_destroyer_coo_coordinator` (supply-side authority: MSTR is the fabric's creator and destroyer; spawn/kill are MSTR's primitives).
- Memory `feedback_concurrency_cap_ceiling_not_target` (cap = ceiling not target; reallocate before overflow-bypass).
- Memory `reference_agent_spawn_kill_methodology` (canonical methodology; this skill is the structural channel for it).
- CLAUDE.md "Agent Autonomy" + concurrency-cap discipline.

## Rollback

A spawn is not destructive at fabric level — the new session can be killed via `/mstr-kill` if it should not have been provisioned. Recovery from a wrongful spawn is one `/mstr-kill {serial}` turn; the audit trail preserves both the spawn and the kill.

If the skill itself produces wrong behavior (e.g., 1a/1b pre-checks false-positive refuse legitimate spawns), revise SKILL.md or temporarily fall back to `.tools\spawn-agent.ps1 {serial}` direct invocation while iterating.
