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

### 1b — Marker scan (AUTHORITATIVE live-state check — LD-0105)

```powershell
$selfPid = $PID
Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object {
    $_.ProcessId -ne $selfPid -and
    $_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1: {serial}*"
  }
```

**This is the AUTHORITATIVE pre-spawn live-state check** per LD-0105 Andrew sovereign 2026-05-26T~22:00Z. Step 1a (broker `get_agent_status`) is supplementary; the broker `opal-agent-comms` has a **suffix-strip semantic** that returns base-serial state for tilde-lane queries — meaning `get_agent_status("0.1.0_DS_MarketIntelligence~D")` returns the base serial registration, NOT the tilde-lane registration. The marker scan above uses the FULL tilde-suffixed serial in its match pattern, so it disambiguates accurately.

Empirical anchor for the elevation: 2026-05-26T~21:38Z /allocation #12 BATCHED-2 spawn of DS 0.1.0~C + ~D — both ws COO `get_live_agents()` read AND MSTR Step 1a `get_agent_status` returned NOT REGISTERED for the tilde-lanes, but the lanes WERE alive from prior /allocation #10 batch (16:30Z) that Andrew countermanded "let it go." Visual collision surfaced 2026-05-26T~21:50Z.

**Mandatory refusal:** If marker scan returns count > 0 (post-`$PID` exclusion + tilde-suffix-sensitive match) → **refuse the spawn**. Surface to spawn-requester: "{full-tilde-suffixed-serial} already LIVE at PID {pid}; spawn refused per LD-0105 authoritative-marker-scan gate. Either redirect the proposed work to the existing LIVE agent OR pass `--force "intentional-duplicate <reason>"` if a genuine duplicate is needed (audited bypass per existing discipline)."

The audited `--force "intentional-duplicate <reason>"` bypass remains for rare cases (e.g., reverse-engineering a prior session crashed mid-init that left a zombie marker). Scanner-self false-positive protection per LD-0100 retained via `$PID` exclusion.

**Tilde-suffix-sensitivity discipline:** the `*# OPAL_SPAWN_MARKER_v1: {serial}*` pattern requires the FULL serial including any tilde-suffix verbatim. Passing the BASE serial when a tilde-lane is the proposed target will miss the disambiguation — always interpolate the full target serial into the pattern.

**Scanner-self false-positive (empirical 2026-05-26).** The `$_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1: {serial}*"` pattern matches the scanner's OWN PowerShell process because the search-pattern literal is embedded in the scanner's CommandLine. Without the `$_.ProcessId -ne $selfPid` exclusion above, every fresh-spawn pre-check returns count=1 (the scanner itself) → false-positive refuse. The `$PID` exclusion eliminates the self-hit. **Diagnostic fallback if a count still surfaces:** inspect each hit's `ProcessId` + `CreationDate` + `CommandLine` — a legitimate spawn-marker window is a long-lived `powershell.exe -NoProfile -NoExit -Command "$Host.UI.RawUI.WindowTitle = '{serial}'; ..."` whose command line ENDS with the marker; a one-shot scanner is short-lived + has the marker EMBEDDED IN ITS Where-Object filter argument. Sister-pattern to memory `feedback_b_lane_orders_only_from_b_agents` family of "structural-self vs other distinction" empirics.

### 1c — Concurrency-cap headroom (informational; spawn-agent.ps1 enforces)

```powershell
$selfPid = $PID
$live = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object {
    $_.ProcessId -ne $selfPid -and
    $_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1*"
  }).Count
```

If `$live >= 16` → spawn-agent.ps1 will reject. Either kill an idle session first (`/mstr-kill {idle-serial}`) OR re-invoke with `--force "<reason>"` (audited bypass).

(Same `$PID` exclusion as Step 1b applies; the scanner's CommandLine contains the marker literal verbatim. Pre-fix 2026-05-26 empirical: `CONCURRENCY_LIVE=7/16` was actually 6 spawned agents + 1 scanner-self. The exclusion ensures the cap-headroom signal reflects only true spawned-agent windows.)

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

(Caveat: broker `get_live_agents()` is suffix-strip; tilde-lane LIVE state is not reliably surfaced. The marker scan in Step 1b is the authoritative tilde-disambiguating check. Step 5 broker verify is for base-serial confirmation + freshness ack only.)

## Step 5b — Update `live_agents_by_marker.json` ground-truth artifact (LD-0105 Fix 2)

Post-spawn confirm-LIVE, append entry to `org/mcp/live_agents_by_marker.json`:

```json
{
  "serial": "{full-tilde-suffixed-serial}",
  "pid": {register-returned-PID},
  "spawn_timestamp": "{ISO-8601-UTC}",
  "spawn_authority": "{spawn-request-source — e.g., 'ws COO /allocation #N' or 'Andrew direct'}",
  "marker": "# OPAL_SPAWN_MARKER_v1: {full-tilde-suffixed-serial}"
}
```

Bump `last_updated` to current ISO timestamp. This artifact is the marker-based LIVE-set source-of-truth consumed by ws COO `/allocation` (per LD-0105 Fix 3) + read-only by other Tier-1 + MSTR own scans. Bypasses the broker suffix-strip semantic that caused the empirical anchor failure.

Reconciliation (out-of-band): `/govern` Step 1 sub-check + `/mstr-review` Step 2 sweep should reconcile artifact against current marker scan to catch crashed/exited PIDs that didn't trigger Step 5b removal.

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
