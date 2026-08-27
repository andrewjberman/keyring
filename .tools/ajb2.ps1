# ajb2.ps1 -- launch a CODEX seat, the peer of `ajb` for Claude seats.
#
# USAGE (dot-source, then call -- identical shape to ajb):
#     . .tools\ajb2.ps1
#     ajb2 4.0.0_SA_CRO~A
#     ajb2 4.0.0_SA_CRO~A -ThreadId <thread>     # resume an existing thread
#     ajb2 4.0.0_SA_CRO~A -Port 8123             # pin the app-server port
#     ajb2 4.0.0_SA_CRO~A -ShowLaunchInfo        # inspect; do not launch
#
# WHAT IT DOES: resolves the workspace root, validates the serial, exports
# OPAL_AGENT_SERIAL, and hands off to org/mcp/start-codex-seat.ps1 -- which
# starts the codex app-server, the heartbeat and the inbox-turn bridge as
# background children, then runs `codex` INLINE in this window and reaps those
# children when it exits.
#
# ajb  -> claude seat   (.tools/ajb.ps1)
# ajb2 -> codex seat    (this file -> org/mcp/start-codex-seat.ps1)
#
# THIS IS A THIN WRAPPER BY DESIGN. All Codex host behaviour -- the app-server
# handshake, the idle/active/unloaded turn routing, the conflict scan -- lives
# in start-codex-seat.ps1 and is NOT duplicated here. If seat behaviour is
# wrong, fix it there; this file only resolves and delegates.

# --- Workspace root -----------------------------------------------------------
# Same resolution ajb uses, and deliberately the SAME ORDER. OPAL_WS_ROOT is the
# device-level escape hatch (an env var lives outside the repo, so it can never
# be pushed); otherwise derive from THIS FILE'S location so a second clone under
# a different profile follows its own checkout.
#
# NOTE: ajb.ps1 documents that this is deliberately NOT `git rev-parse` -- it has
# to work before/without git. Mirrored rather than "improved".
if ($env:OPAL_WS_ROOT -and (Test-Path -LiteralPath $env:OPAL_WS_ROOT)) {
    $Global:Ajb2RepoRoot = (Resolve-Path -LiteralPath $env:OPAL_WS_ROOT).Path
} elseif ($env:OPAL_WS_ROOT) {
    Write-Host "[ajb2] WARN: OPAL_WS_ROOT is set but does not exist: $env:OPAL_WS_ROOT -- ignoring it and deriving instead." -ForegroundColor Yellow
    $Global:Ajb2RepoRoot = Split-Path -Parent $PSScriptRoot
} else {
    $Global:Ajb2RepoRoot = Split-Path -Parent $PSScriptRoot
}

<#
.SYNOPSIS
Launch or inspect one canonical Codex agent seat.

.DESCRIPTION
ajb2 is the required Codex entry point for this workspace. It delegates to
org/mcp/start-codex-seat.ps1, which owns one loopback app-server shared by the
foreground TUI and the inbox turn bridge, one broker/liveness heartbeat, and
one non-consuming inbox detector started by that bridge.

Use the complete serial, including any ~lane suffix. Do not run the Claude
consuming watcher, check-inbox.sh, the generic agent poller, a second heartbeat
or detector, or the retired model-side notify bridge for the same serial.

For an already-open embedded session, record its thread ID and top-level
codex.exe PID, then migrate from a separate PowerShell with
org/mcp/handoff-codex-seat.ps1. The old TUI must exit before the shared-host
launcher can resume the thread because the TUI owns the active-writer lock.

This startup path is repository-closed. Do not browse the web, consult
external/OpenAI documentation, or infer replacement steps. If a checked-in
dependency is missing or contradictory, report a repository defect instead of
improvising another launch or monitor mechanism.

.PARAMETER Serial
The exact full agent serial. Base and suffixed lanes are distinct seats.

.PARAMETER ThreadId
Resume this saved Codex thread after the previous TUI has fully exited.

.PARAMETER Port
Pin the loopback app-server port. Zero lets the launcher choose a free port.

.PARAMETER Workspace
Override the workspace root for this invocation.

.PARAMETER ShowLaunchInfo
Print the resolved canonical scripts, inbox, runtime log directory, launch
mode, and prohibited duplicate mechanisms, then return without launching.

.EXAMPLE
ajb2 '4.0.0_SA_CRO~B'

Launch a fresh suffixed CRO Codex seat under the canonical shared host.

.EXAMPLE
ajb2 '4.0.0_SA_CRO~B' -ThreadId '01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

Resume a known thread after completing the canonical handoff sequence.

.EXAMPLE
ajb2 '4.0.0_SA_CRO~B' -ShowLaunchInfo

Inspect the exact-serial launch topology without starting any process.

.NOTES
Binding workspace contracts: AGENTS.md, org/XXX.md Step 1b, and
org/mcp/CODEX_INBOX_MONITOR.md.
#>
function ajb2 {
    [CmdletBinding()]
    param(
        # Full agent serial INCLUDING any ~lane suffix. A lane is a distinct
        # seat: 4.0.0_SA_CRO and 4.0.0_SA_CRO~A are different sessions.
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Serial,

        # Resume an existing Codex thread instead of starting a fresh one.
        [string]$ThreadId,

        # Pin the app-server port. 0 (default) lets the host choose.
        [ValidateRange(0, 65535)]
        [int]$Port = 0,

        # Override the workspace root for this call only. Unset = derived above.
        [string]$Workspace,

        # Resolve and print the canonical topology without starting a process.
        [switch]$ShowLaunchInfo
    )

    $root = if ($Workspace) { $Workspace } else { $Global:Ajb2RepoRoot }

    if (-not (Test-Path -LiteralPath $root)) {
        Write-Error "[ajb2] workspace root does not exist: $root"
        return
    }

    # Serial shape -- same grammar the spawn/kill primitives use. Catching a typo
    # here is cheaper than a half-provisioned seat registered under a bad name.
    if ($Serial -notmatch '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$') {
        Write-Error "[ajb2] '$Serial' does not look like an agent serial (expected N.N.N_ROLE_Name[~Lane])."
        return
    }

    $starter = Join-Path $root 'org\mcp\start-codex-seat.ps1'
    if (-not (Test-Path -LiteralPath $starter)) {
        Write-Error "[ajb2] start-codex-seat.ps1 not found at $starter"
        return
    }

    $baseSerial = ($Serial -split '~', 2)[0]
    $lane = if ($Serial.Contains('~')) { ($Serial -split '~', 2)[1] } else { $null }
    $inboxRelative = if ($lane) {
        "org\mcp\inbox\$baseSerial\~$lane"
    }
    else {
        "org\mcp\inbox\$baseSerial"
    }
    $runtimeSerial = $Serial -replace '[^A-Za-z0-9_.~-]', '_'
    $runtimeRelative = ".runtime\codex-seats\$runtimeSerial"
    $launchMode = if ($ThreadId) { "resume thread $ThreadId" } else { 'new thread' }

    $launchInfo = @(
        "[ajb2] identity:       $Serial",
        "[ajb2] mode:           $launchMode",
        "[ajb2] seat launcher:  org\mcp\start-codex-seat.ps1",
        "[ajb2] heartbeat:      org\mcp\codex-agent-heartbeat.py (launcher-owned, exactly one)",
        "[ajb2] turn bridge:    org\mcp\codex-inbox-turn-bridge.py (launcher-owned, exactly one)",
        "[ajb2] detector:       org\mcp\codex-inbox-monitor.py (bridge-owned, non-consuming, exactly one)",
        "[ajb2] inbox:          $inboxRelative",
        "[ajb2] runtime logs:   $runtimeRelative",
        "[ajb2] load skill:     org\mcp\codex-skills\load (canonical source; installed before app-server)",
        "[ajb2] seat context:   org\mcp\codex-seat-load.py (exact serial/path derivation)",
        "[ajb2] startup input:  automatic `$load $Serial prompt; no manual load command required",
        "[ajb2] handoff:        org\mcp\handoff-codex-seat.ps1 (already-open embedded sessions)",
        "[ajb2] contract:       AGENTS.md -> org\XXX.md Step 1b -> org\mcp\CODEX_INBOX_MONITOR.md",
        "[ajb2] authority:      repository-local only; zero web research and zero inferred setup",
        "[ajb2] prohibited:     inbox-watch/check-inbox, generic agent-poller, duplicate detector/heartbeat, notify bridge"
    )

    if ($ShowLaunchInfo) {
        $launchInfo | ForEach-Object { Write-Host $_ -ForegroundColor Cyan }
        return
    }

    # Mirror ajb's established Windows Terminal path: create the tab with the
    # serial as its title, then run this same alias inside it once. The existing
    # profiles.defaults.suppressApplicationTitle setting pins that creation
    # title even when Codex updates its own application title.
    if ($env:WT_SESSION -and $env:AJB2_NO_WT_RELAUNCH -ne '1') {
        $wtCmd = Get-Command wt.exe -ErrorAction SilentlyContinue
        if ($wtCmd) {
            $ajb2Path = Join-Path $root '.tools\ajb2.ps1'
            $ajb2Lit = "'" + $ajb2Path.Replace("'", "''") + "'"
            $rootLit = "'" + $root.Replace("'", "''") + "'"
            $serialLit = "'" + $Serial.Replace("'", "''") + "'"
            $threadArg = if ($ThreadId) {
                " -ThreadId '" + $ThreadId.Replace("'", "''") + "'"
            } else { '' }
            $portArg = if ($Port -gt 0) { " -Port $Port" } else { '' }
            $inner = "`$env:AJB2_NO_WT_RELAUNCH='1'; `$env:OPAL_WS_ROOT=$rootLit; . $ajb2Lit; ajb2 $serialLit -Workspace $rootLit$threadArg$portArg"
            # wt parses semicolons as action separators unless escaped.
            $innerForWt = $inner -replace ';', '\;'
            & wt.exe -w 0 new-tab --title $Serial powershell.exe -NoProfile -NoExit -Command $innerForWt
            Write-Host "[ajb2] opened $Serial in a new titled Windows Terminal tab (current window)" -ForegroundColor Cyan
            return
        }
    }

    # The seat's own identity, read by the inbox bridge and the heartbeat.
    $env:OPAL_AGENT_SERIAL = $Serial

    # Window title, so a wall of terminals is readable. OSC 0 + WindowTitle,
    # belt-and-suspenders, same as the claude spawn path.
    [Console]::Write(([char]27).ToString() + "]0;$Serial" + ([char]7).ToString())
    try { $Host.UI.RawUI.WindowTitle = $Serial } catch { }

    $splat = @{ Serial = $Serial; Workspace = $root }
    if ($ThreadId) { $splat['ThreadId'] = $ThreadId }
    if ($Port -gt 0) { $splat['Port'] = $Port }

    Write-Host "[ajb2] codex seat $Serial  (root: $root)" -ForegroundColor Cyan
    $launchInfo | Select-Object -Skip 1 | ForEach-Object {
        $color = if ($_ -match 'authority:|prohibited:') { 'Yellow' } else { 'DarkCyan' }
        Write-Host $_ -ForegroundColor $color
    }

    # Same truecolor signal used by ajb for raw-commandline WT tabs.
    $env:FORCE_COLOR = '3'

    # BLOCKING BY DESIGN: start-codex-seat.ps1 runs `codex` inline and reaps its
    # background children in a finally block. Backgrounding this call would
    # orphan the app-server, the heartbeat and the bridge.
    & $starter @splat
}
