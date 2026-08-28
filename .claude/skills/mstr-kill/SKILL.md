---
name: mstr-kill
description: MSTR + COO event-triggered skill — terminate a live agent by serial, covering both fabric-spawned (marker-tracked) and Andrew-launched (no marker) cases via a tiered fallback chain. Invoked by 0.0.0_AB_MSTR or 2.0.0_SA_COO (base or ~lane) — a COO function in addition to MSTR since Andrew-direct 2026-08-28. Sibling to /mstr-spawn.
---

# /mstr-kill — terminate a live agent

The fabric's structural mechanism for **population destruction**. The invocation
`/mstr-kill {serial}` IS the per-instance authorization for force-kill of
unmarked sessions — this skill charter blanket-authorizes the destructive-without-marker
path within its body.

**Invokers: `0.0.0_AB_MSTR` and `2.0.0_SA_COO`, each with or without a `~lane` suffix.**
Andrew-direct 2026-08-28 ~15:32Z at the `1.0.0_SA_CTO` terminal, VERBATIM: *"/mstr-spawn and
/mstr-kill should be a COO function in addition to 0.0.0_AB_MSTR, I think it is a natural fit for
them to handle these things directly rather than having to coordinate through another agent. MSTR
should just be online as a device/fabric infra manager as well as handling cross-device
cross-fabric comms and so on."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260828_1532Z_D2D3_RESUME_AND_SPAWN_KILL_TO_COO.md`.
The skill keeps its `mstr-` name so every existing citation still resolves; the name is a stable
id, not an ownership claim. **A COO seat kills directly — it no longer files a kill request with
MSTR.** One carve-out, stated once: **killing `0.0.0_AB_MSTR` itself is not inside a COO's blanket**
— MSTR is the device's infra manager and its cross-device comms carrier (`/agentbus` consumer), so
a COO ends it only on Andrew's explicit word; MSTR self-kills with `--self-ack` as before.

> **Force-kill outside this skill still requires explicit Andrew per-instance
> authorization** (CLAUDE.md / LD-0027). The skill is the structural channel —
> outside the channel, the default discipline holds.

## When to invoke

- Andrew direct: `/mstr-kill {full-agent-serial}` (covers both his manual launches and fabric spawns).
- COO (`2.0.0_SA_COO` base or lane): a lane whose TO / decomp cell is ACCEPTED and holds nothing else (free the slot before seating the next), a lane that is STANDING_BY with no queued work in its project, a wedged lane being respawned (kill -> `/mstr-spawn`), a stale duplicate found by the seat census. The COO reads the seat's open obligations FIRST (Step 6's displaced-context list is what it must already know).
- MSTR autonomous: device/fabric infrastructure population action — fleet stand-down before a device reboot, cross-fabric seat teardown, `/mstr-review` scan findings (STANDING_BY + no queued work, BLOCKED unrecoverable, wrong-mix swap) — LD-charter governs; ledger LD-NNNN before invocation per Stakes-Matrix class.
- Never invoked by any seat outside `{0.0.0_AB_MSTR, 2.0.0_SA_COO}` (+ lanes). A CTO / Tier-2 / CVO seat that needs a session ended asks its COO (or MSTR for infra-class kills).

---

## Step 0 — Parse + identity gate

Parse the argument:
- Must be a full agent serial matching `^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$`.
- Tilde-lane suffixes (`~B`/`~C`/`~D`) MUST be included — `1.0.0_SA_CTO~B` is a different session than `1.0.0_SA_CTO`.
- Refuse self-kill (the target equals the caller's own serial) without `--self-ack` flag — a self-kill ends the caller's own session. `kill-agent.ps1` also self-excludes on `OPAL_AGENT_SERIAL` (`:112-123`), so a self-kill without the flag is refused twice.
- Target `0.0.0_AB_MSTR` from a COO caller: refuse unless the invocation cites Andrew's explicit word (`--andrew "<verbatim>"`) — see the carve-out at the top.

**Identity gate:** confirm the caller serial is `0.0.0_AB_MSTR` or `2.0.0_SA_COO`, either with an optional `~lane` suffix — read `$env:OPAL_AGENT_SERIAL` (per-process) or the session serial file `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial`; **never `.comp-graph/.agent_context`** (shared, last-writer-wins — not an identity source, `org/XXX.md` Step 1). Any other invoker halts here with an error. The caller serial is what the audit lines below carry as `by <serial>`.

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
Add-Content -Path "org/mcp/agent-spawn-audit.log" -Value "$ts  FORCE-KILL  {serial}  by {caller-serial}  pid={pid}  reason=<reason>  authorized-via=/mstr-kill"
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

## Step 4b — RETIRED (LD-0202 D1)

The `live_agents_by_marker.json` artifact is **retired** (LD-0202 D1) — **no post-deregister artifact removal.** The broker live-set is suffix-clean and is the population source of record; the Step 4 broker deregister + the broker's own PID-death cleanup are sufficient. COO `/allocation` consumes the broker live-set directly (repointed by COO `b93c4f193`).

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
  authorizes ONE kill of ONE serial. A second kill in the same turn (MSTR or COO)
  requires a second invocation. The skill is not a session-wide kill license.
- **Who kills what (division of the primitive, Andrew-direct 2026-08-28).** COO: work-population
  seats (finished / idle / wedged lanes in its projects). MSTR: infrastructure population (fleet
  stand-downs, cross-fabric seats, mix corrections). A COO does not kill a seat of the OTHER
  fabric on this device (the `~X` cohort fence and its site-Z analogue stand) — that is MSTR's
  cross-fabric lane, or the other fabric's own COO.
- **No silent escalation.** If Step 1 succeeds, do not also force-kill any
  PID returned by Step 2 "just to be sure" — that is the LD-0074 failure mode
  (assumed broker LIVE = alive; escalated to no-op force-kill of a ghost).
  Trust the Step-1 success unless Step 5 verify-after fails.
- **Heartbeat-lag is real.** Step 2a is non-negotiable; skipping it
  reproduces LD-0074. Once LD-0070 telemetry-derived liveness lands and
  Phase 2 makes the broker report NOT_LIVE within seconds of process death,
  Step 2a becomes vestigial — but until then, every force-kill goes through
  the `Get-Process` check first.
- **Self-kill ends the caller's own loops.** `--self-ack` flag is required to kill
  the caller's own serial (MSTR killing `0.0.0_AB_MSTR`, a COO lane killing itself). After a
  self-kill any cron the seat armed is orphaned but harmless (next fire hits a dead session and
  surfaces as a watcher exit) — but a LIVE SCOPED ARM in the seat's `org/XXX.md` Step 1b-F row is
  NOT struck by a self-kill; the successor re-arms from the row. Respawn via `/mstr-spawn` or
  `.tools\spawn-agent.ps1 {serial}`.
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
