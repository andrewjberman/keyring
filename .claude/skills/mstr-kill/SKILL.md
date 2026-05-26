---
name: mstr-kill
description: MSTR-only event-triggered skill — terminate a live agent by serial, covering both MSTR-spawned (marker-tracked) and Andrew-launched (no marker) cases via a tiered fallback chain.
---

# /mstr-kill — terminate a live agent

MSTR's structural mechanism for **population destruction**. The invocation
`/mstr-kill {serial}` IS the per-instance authorization for force-kill of
unmarked sessions — this skill charter blanket-authorizes the destructive-without-marker
path within its body. Only `0.0.0_AB_MSTR` invokes it.

> **Force-kill outside this skill still requires explicit Andrew per-instance
> authorization** (CLAUDE.md / LD-0027). The skill is the structural channel —
> outside the channel, the default discipline holds.

## When to invoke

- Andrew direct: `/mstr-kill {full-agent-serial}` (covers both his manual launches and MSTR's own spawns).
- MSTR autonomous: population action arising from `/mstr-review` scan (STANDING_BY + no queued work, BLOCKED unrecoverable, wrong-mix swap) — LD-charter governs; ledger LD-NNNN before invocation per Stakes-Matrix class.
- Never invoked by any agent other than `0.0.0_AB_MSTR`.

---

## Step 0 — Parse + identity gate

Parse the argument:
- Must be a full agent serial matching `^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$`.
- Tilde-lane suffixes (`~B`/`~C`/`~D`) MUST be included — `1.0.0_SA_CTO~B` is a different session than `1.0.0_SA_CTO`.
- Refuse self-kill (`0.0.0_AB_MSTR`) without `--self-ack` flag — a self-kill ends MSTR's own session.

**Identity gate:** confirm caller is `0.0.0_AB_MSTR` (read `$env:OPAL_AGENT_SERIAL` / `.comp-graph/.agent_context`). Non-MSTR invocation halts here with an error.

## Step 1 — Marker-tracked kill attempt (covers MSTR spawns)

```powershell
.tools\kill-agent.ps1 {serial} -Reason "<short reason>"
```

The script walks `Win32_Process` for `powershell.exe` carrying the
`# OPAL_SPAWN_MARKER_v1: {serial}` CommandLine tag, then `Stop-ProcessTree`
each match (children first), and writes a `KILL` line to
`org/mcp/agent-spawn-audit.log`.

**Read the script's verdict:**
- `[kill-agent] terminated {serial} (pid {pid})` → success. **Skip to Step 4.**
- `[kill-agent] No live spawned windows for serial '{serial}' found -- nothing to kill.` → marker-tracking gap. **Continue to Step 2.**

The "nothing to kill" outcome means one of:
- The agent was launched manually (no marker — Andrew direct launch is the most common case).
- The agent already died (broker still lying about LIVE per ~120s heartbeat lag — see LD-0070).
- The serial is wrong (typo / lane suffix missing).

Step 2 disambiguates these.

## Step 2 — Broker lookup (find the PID if unmarked)

Call the broker:

```
mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
```

Read the response:

| Liveness | PID present | Interpretation | Next |
|---|---|---|---|
| `LIVE`, last seen < 120s | yes | Unmarked live process — Andrew-launched or pre-marker-era spawn | **Step 3 force-kill** |
| `LIVE`, last seen 120s-600s | yes | Possibly heartbeat-lag-after-death (LD-0074 banked); verify before force-killing | **Step 2a verify** |
| `STALE` / `NOT_REGISTERED` | no | Already dead OR never registered under this serial | **Step 4 deregister-only** |
| Not found at all | n/a | Wrong serial OR broker dropped the entry | Surface to Andrew; do not proceed |

### Step 2a — Verify-before-force-kill (heartbeat-lag mitigation)

Per LD-0074 empirical lesson: heartbeat-authoritative liveness lies by omission
~120s post-process-death. Before force-killing a PID returned by the broker:

```powershell
Get-Process -Id {pid} -ErrorAction SilentlyContinue
```

- Process exists → genuine live unmarked session; proceed to Step 3.
- Process does not exist → broker is lagging; the session already died. Skip Step 3, proceed to Step 4 deregister-only.

This single check is the difference between LD-0074's "no-op force-kill on a
ghost PID" and a correct kill decision. Do not skip it.

## Step 3 — Force-kill by PID (audited)

```powershell
Stop-Process -Id {pid} -Force -ErrorAction Stop
```

Then walk the parent process tree if the broker PID was a `claude.exe` under a
`powershell.exe` window (common case — the PowerShell window stays alive after
its child Claude session ends, leaking a host slot):

```powershell
$parent = (Get-CimInstance Win32_Process -Filter "ProcessId={pid}").ParentProcessId
if ($parent) {
    $parentProc = Get-CimInstance Win32_Process -Filter "ProcessId=$parent" -ErrorAction SilentlyContinue
    if ($parentProc -and $parentProc.Name -eq 'powershell.exe') {
        Stop-Process -Id $parent -Force -ErrorAction SilentlyContinue
    }
}
```

**Audit append (mandatory):**

```powershell
$ts = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
Add-Content -Path "org/mcp/agent-spawn-audit.log" -Value "$ts  FORCE-KILL  {serial}  by 0.0.0_AB_MSTR  pid={pid}  reason=<reason>  authorized-via=/mstr-kill"
```

The `FORCE-KILL` verb (distinct from the script's `KILL` verb) marks this as
the destructive-without-marker path so audit walks can distinguish the two
mechanisms. The `authorized-via=/mstr-kill` token marks it as
skill-charter-authorized rather than ad-hoc.

## Step 4 — Deregister broker (always)

Regardless of which path landed the kill:

```
mcp__opal-agent-comms__deregister_agent(agent_serial="{serial}")
```

This stops the broker from continuing to report the agent LIVE for the next
~120s heartbeat-lag window. Skipping this step is what produced the LD-0074
misjudgment — the broker shows a dead serial as LIVE until the deregister or
the heartbeat-timeout fires.

If `deregister_agent` returns an error (broker doesn't have the serial), that
is fine — the agent was already deregistered or never registered. Note in the
report; do not retry.

## Step 4b — Remove from `live_agents_by_marker.json` ground-truth artifact (LD-0105 Fix 2)

Post-deregister, remove the entry for `{serial}` from `org/mcp/live_agents_by_marker.json` `live_agents[]` array. Bump `last_updated` to current ISO timestamp.

This keeps the MSTR-published ground-truth artifact accurate for downstream consumers (ws COO `/allocation`, /govern reconciliation, /mstr-review surface). If `{serial}` was not present in the artifact (e.g., killed agent was spawned pre-LD-0105 or by an Andrew direct path that didn't go through `/mstr-spawn`), no-op silently — `/govern` Step 1 reconciliation will catch any out-of-band drift.

Tilde-suffix-sensitive: remove the entry matching the FULL tilde-suffixed serial verbatim. Do not strip-and-match the base serial — that would remove the wrong entry.

## Step 5 — Verify-after

Re-run:

```
mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
```

Expected: `STALE` / `NOT_REGISTERED` / not-found. If the broker still shows
LIVE after Step 4, surface to Andrew — that is a broker-state corruption
finding, not a kill failure.

Also re-run the marker scan if Step 1 path was taken:

```powershell
.tools\kill-agent.ps1 {serial} -Reason "verify-after"
```

Expected: `nothing to kill`.

## Step 6 — Report

Print the fixed report:

```
/mstr-kill {serial}
  PATH:    marker-tracked | force-kill-pid | deregister-only | already-dead
  KILLED:  pid {pid} (and parent {ppid}) | none — already dead
  BROKER:  deregistered | was-not-registered | STILL-LIVE (CORRUPTION)
  AUDIT:   org/mcp/agent-spawn-audit.log
  REASON:  <reason>
```

Then surface any context the kill displaced — in-flight work, open RAVC2s,
STUCK asks the killed agent was holding — so the next routing call has the
context. Cite specific commits / TO IDs where applicable. This is the
LD-0074 empirical lesson generalized: a kill is not just a process action,
it's a population state change with routing implications.

---

## Discipline / risk notes

- **Per-instance authorization scope.** The `/mstr-kill {serial}` invocation
  authorizes ONE kill of ONE serial. A second kill in the same MSTR turn
  requires a second invocation. The skill is not a session-wide kill license.
- **No silent escalation.** If Step 1 succeeds, do not also force-kill any
  PID returned by Step 2 "just to be sure" — that is the LD-0074 failure mode
  (assumed broker LIVE = alive; escalated to no-op force-kill of a ghost).
  Trust the Step-1 success unless Step 5 verify-after fails.
- **Heartbeat-lag is real.** Step 2a is non-negotiable; skipping it
  reproduces LD-0074. Once LD-0070 telemetry-derived liveness lands and
  Phase 2 makes the broker report NOT_LIVE within seconds of process death,
  Step 2a becomes vestigial — but until then, every force-kill goes through
  the `Get-Process` check first.
- **MSTR self-kill ends the loop.** `--self-ack` flag is required to kill
  `0.0.0_AB_MSTR`. After self-kill the `/govern` / `/mstr-review` cron is
  orphaned but harmless (next fire will hit a dead session and surface as
  a watcher exit). Andrew respawns via `.tools\spawn-agent.ps1 0.0.0_AB_MSTR`.
- **Audit log is append-only.** Never edit `org/mcp/agent-spawn-audit.log`
  to remove a `FORCE-KILL` line. Constitution Art. V on ledger integrity
  applies by analogy — the forensic trail is the structural defense.

## Cross-references

- `.tools\kill-agent.ps1` — marker-tracked kill mechanism (Step 1).
- `.tools\spawn-agent.ps1` — corresponding creation primitive (the
  marker-write side of the marker-track contract).
- `org/mcp/agent-spawn-audit.log` — forensic trail for all kill paths.
- LD-0027 — marker-tracking-gap empirical anchor + tilde-lane fallback.
- LD-0061 — fabric-wide kill empirical anchor + force-kill audit pattern.
- LD-0069 — MSTR thin architecture; `/mstr-kill` as an event-triggered skill.
- LD-0070 — telemetry-derived liveness; eventually obsoletes Step 2a.
- LD-0074 — broker-lag misjudgment; the empirical reason Step 2a exists.
- CLAUDE.md "Agent Autonomy" — force-kill default discipline (this skill is
  the structural channel that blanket-authorizes within its body).

## Rollback

A kill is irreversible at the process level — the PowerShell window and its
Claude session are gone. Recovery is **respawn**:

```powershell
.tools\spawn-agent.ps1 {serial}
```

The new session inherits no state from the killed one beyond what is in git
+ broker + MCP inbox. In-flight uncommitted work is lost — surface this in
the Step 6 report if the killed agent had recent activity without a
corresponding commit.
