---
name: kill
description: Clear machine cruft without touching a live Claude session, fabric comms infra or a repo file: `/kill scripts` (orphan bash/python not under a live session), `/kill apps` (bloat GUI apps that are not a session host or automation browser), `/kill storage` (allowlist-only junk roots; opt-in package caches, __pycache__, recycle bin, docker prune), `/kill all` (scripts+apps, never storage). Dry-run by default; append `go` to apply. Engines `.tools/kill-maint.ps1`, `.tools/kill-storage.ps1`. Any agent may dry-run; killing is an operator act.
---

# /kill -- machine-cruft reaper (zombie scripts + bloat apps)

The Windows host running the fabric keeps accumulating two kinds of junk that show
up as memory pressure and CPU trudge (the same class that drove the 2026-07-07
Huntress/Rio reboots): **orphaned bash/python scripts** left behind by dead sessions,
and **bloat GUI apps** nobody asked for (Edge, Chrome, Teams, Copilot).
`/kill` clears them in one shot -- while treating every live Claude agent session and
the fabric comms infra as untouchable.

**DRY-RUN is the default.** Bare `/kill <mode>` shows precisely what it *would* kill
and the memory it reclaims, and kills nothing. You add `go` to pull the trigger.

## Modes

| Invocation | What it does |
|---|---|
| `/kill` or `/kill all` | Dry-run the PROCESS modes (scripts + apps) -- show the plan, kill nothing. **Does NOT include storage** (recursive deletion is always invoked explicitly). |
| `/kill scripts` | Dry-run: orphan `bash.exe` / `python.exe` / `pythonw.exe` / `py.exe` not tied to a live claude session and not comms infra. |
| `/kill apps` | Dry-run: bloat GUI apps (Edge, Chrome, Teams, Copilot, Spotify, Slack, Discord, Zoom, ...). |
| `/kill storage` | Dry-run: allowlist-only disk reclaim (dead Claude scratchpad, user/Windows temp, crash dumps). See the storage section below. |
| `/kill <mode> go` | Same selection, but **actually kills/deletes** (`go` / `force` / `--execute` are synonyms). |
| `... --webview2` | (apps) ALSO target `msedgewebview2.exe` (embedded in Windows Search / Outlook / widgets -- respawns; off by default). |
| `... --onedrive` | (apps) ALSO target OneDrive. **WARNING: the Schwab pipeline delivers data through OneDrive folders** -- only with an explicit reason. |
| `... --caches` `--pycache` `--recyclebin` `--docker` `--docker-volumes` | (storage) opt-in extra categories -- see the storage section. |

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
  `chromium`, `ms-teams`/`Teams`,
  `mscopilot`/`copilot`, `Spotify`, `Slack`, `Discord`, `Zoom`, `WhatsApp`, `Skype`,
  ...), minus every protection above. `--webview2` / `--onedrive` extend the list.

## `/kill storage` -- allowlist-only disk reclaim (recursive delete)

Storage is a different, more dangerous animal than the process modes: it does
`rm -rf`, which is **unrecoverable** and on the CLAUDE.md human-confirmation list. So
it inverts the safety model -- instead of "delete everything except the protected set"
(a denylist), it **only ever deletes paths that live strictly UNDER a vetted junk root**
(an allowlist). Engine: `.tools/kill-storage.ps1`.

**Default categories** (bare `/kill storage`, no flags):

| Category | What | Guard |
|---|---|---|
| `claude-scratch` | Dead Claude scratchpad session dirs under `%LOCALAPPDATA%\Temp\claude\` | Skips the CURRENT session id AND any dir written within `-StaleHours` (default 2h) -- protects every live session. |
| `user-temp` | Items under `%TEMP%` older than `-TempAgeDays` (default 1d) | Excludes the `claude` subdir (handled above); in-use files fail-skip. |
| `win-temp` | Items under `C:\Windows\Temp` older than the age floor | May need admin; locked items skip. |
| `crash-dumps` | `%LOCALAPPDATA%\CrashDumps` contents | -- |

**Opt-in categories** (data-loss or slow-to-rebuild -- off by default):

| Flag | Adds | Why opt-in |
|---|---|---|
| `--caches` | pip / bun / npm package caches | Regenerable, but re-download costs time. |
| `--pycache` | workspace `__pycache__` dirs | **Some `.pyc` are git-tracked in this repo** -- deleting shows as working-tree deletions. |
| `--recyclebin` | empties the Recycle Bin | Final deletion of whatever you binned. |
| `--docker` | `docker container/image/builder prune -f` | Only STOPPED containers / DANGLING images / build cache -- a running ka_testing container is untouched. Skipped with a notice if the daemon is down. |
| `--docker-volumes` | ALSO `docker volume prune -f` | **Deletes unused volume DATA.** Never without intent. |

**The hard safety gate** (`Assert-Deletable`, checked at plan time AND re-checked at
delete time): every target must resolve to a path that is a *strict descendant* of one
of the 7 allowlisted junk roots (never a root itself), and must not be a reparse
point / junction / symlink (which could redirect the delete elsewhere). The workspace
repo is NOT a junk root -- the only repo deletion ever permitted is a dir literally
named `__pycache__` under `--pycache`. Anything failing the gate is skipped, never
deleted. This is what makes a path-construction bug unable to nuke source or served data.

Validated on this host: default dry-run = ~7.3 GB reclaimable (user-temp ~4.0 GB,
win-temp ~2.0 GB, 244-of-251 dead scratchpad dirs ~1.5 GB) with the current session +
6 other live sessions correctly protected.

## How to run it (agent instructions)

1. **Parse the invocation.** Mode = `scripts` | `apps` | `all` | `storage`
   (default `all`, which = scripts+apps, NEVER storage). Execute = true iff the args
   contain `go`, `force`, or `--execute`. Opt-ins: apps -> `--webview2`, `--onedrive`;
   storage -> `--caches`, `--pycache`, `--recyclebin`, `--docker`, `--docker-volumes`.
2. **Dispatch on whether an execute token was given** (`go` / `force` / `--execute`):

   - **Process modes (`scripts` / `apps` / `all`) WITH an execute token** -> run the engine
     directly WITH `-Execute` and report. **No dry-run first** -- process kills are
     recoverable (relaunch) and NOT on the CLAUDE.md human-confirmation set, and the operator
     already said `go`, so do not make them look at a plan they've already authorized.
     ```
     & .tools/kill-maint.ps1 -Mode <scripts|apps|all> -Execute [-IncludeWebView2] [-IncludeOneDrive]
     ```
   - **Process modes WITHOUT an execute token** (bare `/kill apps`) -> run WITHOUT `-Execute`
     to show the plan, kill nothing, and tell the operator to append `go` to apply.
     ```
     & .tools/kill-maint.ps1 -Mode <scripts|apps|all> [-IncludeWebView2] [-IncludeOneDrive]
     ```
   - **Storage mode -- ALWAYS dry-run first, even with `go`** -> because `rm -rf` IS on the
     CLAUDE.md human-confirmation list, run WITHOUT `-Execute` first, present the plan, and
     confirm the operator's `go` maps to THIS plan before running with `-Execute`. Never chain
     dry-run -> execute silently; never auto-run storage.
     ```
     & .tools/kill-storage.ps1 [-Caches] [-Pycache] [-RecycleBin] [-Docker] [-DockerVolumes]   # plan first, always
     & .tools/kill-storage.ps1 -Execute [...]                                                   # only after the operator confirms the plan
     ```
3. **Report** the before/after: what was protected (count), what was killed/deleted, MB
   reclaimed, anything skipped (locked/in-use). Keep it tight; ASCII only.

## Safety model / notes

- **Process modes are recoverable by design.** Killing a bloat app or an orphan script
  is reversible (relaunch), and is NOT in the CLAUDE.md human-confirmation set. So `go`
  executes directly -- no dry-run first. The guardrail is the invocation itself: bare
  `/kill apps` (no `go`) shows the exact PID plan and kills nothing; add `go` only when
  you want it applied.
- **Storage mode is NOT recoverable** -- `rm -rf` is exactly the recursive-deletion case
  that IS on the CLAUDE.md human-confirmation list. Its guardrails are stronger to match:
  allowlist-only (never deletes outside the 7 vetted junk roots), never a root itself,
  reparse-point/junction guard, current-session + live-session scratchpad protection, and
  a re-validation at delete time. Present the dry-run and get an explicit `go` -- never
  auto-run storage, never chain dry-run into execute without the operator seeing the plan.
- **Tailscale is a Windows service** (`tailscaled` under `services.exe`). Stopping the
  process may be restarted by the SCM and/or briefly drop tailnet connectivity -- fine
  if you don't route AWS/remote access through it, but know that's what happens.
- **Self-safe.** The engine runs as a PowerShell child of the invoking claude session,
  so it is itself inside the protected tree; it only ever targets bash/py (scripts) or
  named bloat apps (apps), never PowerShell.
- **Snapshot-once semantics.** Each run enumerates processes once and acts on that
  snapshot; a browser that churns renderers between runs may show a slightly different
  count -- expected, not a bug.
- Engine + full protect logic: `.tools/kill-maint.ps1`. For process modes, `go` executes
  directly; run the bare (no-`go`) plan first only when you want to preview. For `storage`,
  the dry-run plan + explicit confirm is mandatory every time (recursive deletion).
