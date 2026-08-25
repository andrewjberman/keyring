# ajb2.ps1 -- launch a CODEX seat, the peer of `ajb` for Claude seats.
#
# USAGE (dot-source, then call -- identical shape to ajb):
#     . .tools\ajb2.ps1
#     ajb2 4.0.0_SA_CRO~A
#     ajb2 4.0.0_SA_CRO~A -ThreadId <thread>     # resume an existing thread
#     ajb2 4.0.0_SA_CRO~A -Port 8123             # pin the app-server port
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
        [string]$Workspace
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

    # BLOCKING BY DESIGN: start-codex-seat.ps1 runs `codex` inline and reaps its
    # background children in a finally block. Backgrounding this call would
    # orphan the app-server, the heartbeat and the bridge.
    & $starter @splat
}
