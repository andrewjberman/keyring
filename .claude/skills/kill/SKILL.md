---
name: kill
description: Clear recurring machine cruft in two modes without ever touching a live Claude agent session or the fabric comms infra. `/kill scripts` reaps orphan bash.exe / python.exe / py.exe processes that are NOT descendants of a live claude session and NOT fabric comms infra (server.py / broker.py / agent-poller.py / inbox-watch.sh) -- the leftover gold runs, dead watchers, and abandoned diagnostics that build up as memory pressure. `/kill apps` reaps bloat GUI apps (Microsoft Edge, Chrome, Teams, Tailscale, Copilot, Spotify, Slack, Discord, Zoom, ...) that are not a Claude/Playwright-automation browser and not a session host. `/kill all` does both. DRY-RUN by default -- shows exactly what it would kill and how much memory it reclaims; append `go` (e.g. `/kill apps go`) to actually kill. Engine: `.tools/kill-maint.ps1` (PowerShell, ASCII-only, protect-set = live-claude descendant tree + comms-infra cmdline whitelist + hard-deny system/EDR list). Built for the Windows host that keeps accumulating zombie scripts + bloat under the multi-agent load (the Huntress/Rio memory-pressure class). Any agent may run the dry-run; killing is an operator action.
---

# /kill -- machine-cruft reaper (zombie scripts + bloat apps)

The Windows host running the fabric keeps accumulating two kinds of junk that show
up as memory pressure and CPU trudge (the same class that drove the 2026-07-07
Huntress/Rio reboots): **orphaned bash/python scripts** left behind by dead sessions,
and **bloat GUI apps** nobody asked for (Edge, Chrome, Teams, Tailscale, Copilot).
`/kill` clears them in one shot -- while treating every live Claude agent session and
the fabric comms infra as untouchable.

**DRY-RUN is the default.** Bare `/kill <mode>` shows precisely what it *would* kill
and the memory it reclaims, and kills nothing. You add `go` to pull the trigger.

## Modes

| Invocation | What it does |
|---|---|
| `/kill` or `/kill all` | Dry-run BOTH modes -- show the full plan, kill nothing. |
| `/kill scripts` | Dry-run: orphan `bash.exe` / `python.exe` / `pythonw.exe` / `py.exe` not tied to a live claude session and not comms infra. |
| `/kill apps` | Dry-run: bloat GUI apps (Edge, Chrome, Teams, Tailscale, Copilot, Spotify, Slack, Discord, Zoom, ...). |
| `/kill <mode> go` | Same selection, but **actually kills** (`go` / `force` / `--execute` are synonyms). |
| `... --webview2` | ALSO target `msedgewebview2.exe` (embedded in Windows Search / Outlook / widgets -- respawns; off by default). |
| `... --onedrive` | ALSO target OneDrive. **WARNING: the Schwab pipeline delivers data through OneDrive folders** -- only with an explicit reason. |

## What is PROTECTED (never killed, both modes)

The engine builds the protect-set from live process state on every run:

1. **The live-claude session tree.** Every `claude.exe` and its full descendant
   closure (the Bash-tool shell-snapshot shells, the `@playwright/mcp` node server,
   the per-session `server.py`, spawned PowerShell). Walked via `ParentProcessId`.
2. **Fabric comms infra by command line** (these run DETACHED from the claude tree,
   so ancestry alone misses them): anything whose cmdline matches
   `org/mcp/`, `inbox-watch.sh`, `agent-poller.py`, `broker.py`, or `server.py`.
   This is why every agent's inbox Monitor and poller survive.
3. **A Claude/Playwright automation browser** -- any chrome/edge/chromium whose
   cmdline carries `--remote-debugging`, `ms-playwright`, `--headless`, or
   `--enable-automation`, or that was launched inside the live-claude tree.
4. **A hard-deny list** that wins even if a pattern over-matches: OS/session
   processes (`svchost`, `explorer`, `dwm`, `csrss`, `powershell`, `WindowsTerminal`,
   `conhost`, `SearchHost`, ...) and **security/EDR** (`EPSecurityService`, `Huntress`,
   `Sentinel`, `Defender`, `CrowdStrike`, ...). EDR is IT-managed -- killing it is both
   futile and a security event.

Scripts mode also skips any candidate **younger than 60s** (`-MinAgeSeconds`) so a
process still resolving its parent link during spawn is never mistaken for an orphan.

## What is a KILL TARGET

- **scripts**: a `bash/python/py` process that is (a) not in the live-claude tree,
  (b) not comms infra, (c) not a Bash-tool shell-snapshot shell, (d) older than the
  age floor. These are orphaned gold runs, dead `inbox-watch` remnants from crashed
  sessions, abandoned diagnostic loops -- real reclaimable memory.
- **apps**: a process whose name matches the bloat list (`msedge`, `chrome`,
  `chromium`, `ms-teams`/`Teams`, `tailscale`/`tailscaled`/`tailscale-ipn`,
  `mscopilot`/`copilot`, `Spotify`, `Slack`, `Discord`, `Zoom`, `WhatsApp`, `Skype`,
  ...), minus every protection above. `--webview2` / `--onedrive` extend the list.

## How to run it (agent instructions)

1. **Parse the invocation.** Mode = `scripts` | `apps` | `all` (default `all`).
   Execute = true iff the args contain `go`, `force`, or `--execute`. Opt-ins:
   `--webview2`, `--onedrive`.
2. **Always dry-run first.** Run the engine WITHOUT `-Execute` and show the plan
   (summary-by-process + reclaimable MB + the target list). This is fast and safe.
   ```
   & .tools/kill-maint.ps1 -Mode <mode> [-IncludeWebView2] [-IncludeOneDrive]
   ```
3. **If an execute token was given**, run again WITH `-Execute` and report the
   killed/failed/reclaimed summary:
   ```
   & .tools/kill-maint.ps1 -Mode <mode> -Execute [-IncludeWebView2] [-IncludeOneDrive]
   ```
   If no execute token, present the dry-run plan and tell the operator to append
   `go` (e.g. `/kill apps go`) to apply.
4. **Report** the before/after: what was protected (count), what was killed, MB
   reclaimed. Keep it tight; ASCII only.

## Safety model / notes

- **Recoverable by design.** Killing a bloat app or an orphan script is reversible
  (relaunch). This is NOT in the CLAUDE.md human-confirmation-required set (which is
  recursive delete / destructive git / drop tables / delete S3 / stop EC2). The
  dry-run-first flow is the guardrail: you see the exact PID list before anything dies.
- **Tailscale is a Windows service** (`tailscaled` under `services.exe`). Stopping the
  process may be restarted by the SCM and/or briefly drop tailnet connectivity -- fine
  if you don't route AWS/remote access through it, but know that's what happens.
- **Self-safe.** The engine runs as a PowerShell child of the invoking claude session,
  so it is itself inside the protected tree; it only ever targets bash/py (scripts) or
  named bloat apps (apps), never PowerShell.
- **Snapshot-once semantics.** Each run enumerates processes once and acts on that
  snapshot; a browser that churns renderers between runs may show a slightly different
  count -- expected, not a bug.
- Engine + full protect logic: `.tools/kill-maint.ps1`. Read the `-WhatIf`-style
  dry-run output before ever passing `go`.
