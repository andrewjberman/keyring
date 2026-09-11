[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[^\\/]+$')]
    [string]$Serial,

    [string]$ThreadId,

    [string]$Workspace = '',

    [ValidateRange(1, 65535)]
    [int]$Port = 0
)

$ErrorActionPreference = 'Stop'

function Set-CodexSeatTitle {
    param([Parameter(Mandatory = $true)][string]$SeatSerial)

    $title = $SeatSerial
    try {
        $Host.UI.RawUI.WindowTitle = $title
    }
    catch {
        Write-Warning "Could not set the PowerShell window title: $($_.Exception.Message)"
    }
    try {
        [Console]::Title = $title
    }
    catch {
        # RawUI is the primary path. Some redirected/non-console hosts reject
        # Console.Title even though the active Windows Terminal accepts OSC.
    }

    if ($env:WT_SESSION -and -not [Console]::IsOutputRedirected) {
        $escape = [char]27
        $bell = [char]7
        [Console]::Write("${escape}]0;${title}${bell}")
    }
}

function Enable-CodexSeatColor {
    # The parent automation environment may deliberately export TERM=dumb and
    # NO_COLOR=1. Those values are correct for captured command output but must
    # not leak into the foreground interactive TUI.
    if ([string]::IsNullOrWhiteSpace($env:TERM) -or $env:TERM -eq 'dumb') {
        $env:TERM = 'xterm-256color'
    }
    if ([string]::IsNullOrWhiteSpace($env:COLORTERM)) {
        $env:COLORTERM = 'truecolor'
    }
    Remove-Item -LiteralPath 'Env:NO_COLOR' -ErrorAction SilentlyContinue
    $env:CLICOLOR = '1'
    $env:CLICOLOR_FORCE = '1'
    $env:FORCE_COLOR = '3'
}

$colorEnvironmentNames = @(
    'TERM',
    'COLORTERM',
    'NO_COLOR',
    'CLICOLOR',
    'CLICOLOR_FORCE',
    'FORCE_COLOR'
)
$originalColorEnvironment = @{}
foreach ($name in $colorEnvironmentNames) {
    $item = Get-Item -LiteralPath "Env:$name" -ErrorAction SilentlyContinue
    $originalColorEnvironment[$name] = [pscustomobject]@{
        Exists = $null -ne $item
        Value = if ($null -ne $item) { $item.Value } else { $null }
    }
}

# Windows PowerShell evaluates parameter default expressions before
# $PSScriptRoot is reliably populated. Resolve the default only after binding.
$seatScriptRoot = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($seatScriptRoot)) {
    $seatScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
}
if ([string]::IsNullOrWhiteSpace($seatScriptRoot)) {
    throw 'Cannot resolve the directory containing start-codex-seat.ps1.'
}
if ([string]::IsNullOrWhiteSpace($Workspace)) {
    $Workspace = (Resolve-Path -LiteralPath (
        Join-Path -Path $seatScriptRoot -ChildPath '..\..'
    )).Path
}
else {
    $Workspace = (Resolve-Path -LiteralPath $Workspace).Path
}

# Codex tool calls run through PowerShell, where the extensionless Python and
# Bash entrypoints under .tools are not executable by bare command name. The
# canonical repository provisioner writes the full derived comp-* forwarding
# set as both Bash scripts and PowerShell/cmd .cmd shims in the persistent
# user bin. Run it idempotently for each Codex seat and put that directory
# first on this launcher's child PATH, so every Codex app-server/TUI/tool call
# resolves `comp-which`, `comp-read`, and the rest exactly as a Claude seat
# does. Do not hand-maintain a second subset here.
$compShimProvisioner = Join-Path $Workspace '.tools\provision-path-shims.sh'
$gitBash = 'C:\Program Files\Git\bin\bash.exe'
foreach ($requiredCompShimDependency in @($compShimProvisioner, $gitBash)) {
    if (-not (Test-Path -LiteralPath $requiredCompShimDependency)) {
        throw "Codex comp-tool shim dependency not found: $requiredCompShimDependency"
    }
}
$compShimOutput = @(
    & $gitBash $compShimProvisioner 2>&1
)
$compShimExitCode = $LASTEXITCODE
if ($compShimExitCode -ne 0) {
    $detail = ($compShimOutput | ForEach-Object { [string]$_ }) -join "`n"
    throw "Codex comp-tool shim provisioning failed (exit $compShimExitCode): $detail"
}
$compShimDir = Join-Path $env:USERPROFILE 'bin'
if (-not (Test-Path -LiteralPath $compShimDir)) {
    throw "Codex comp-tool shim directory was not created: $compShimDir"
}
if (-not (($env:PATH -split ';') -contains $compShimDir)) {
    $env:PATH = "$compShimDir;$env:PATH"
}
if (-not (($env:PATHEXT -split ';') -contains '.CMD')) {
    $env:PATHEXT = (($env:PATHEXT -split ';') + '.CMD' | Where-Object { $_ }) -join ';'
}

# The full launcher serial is the process identity for ajb2, direct starts,
# and handoffs alike. Downstream startup checks must never infer it elsewhere.
$env:OPAL_AGENT_SERIAL = $Serial

# Install the checked-in skill projections before the app-server starts so the
# TUI's first model context can discover $load and $log. Then render the startup prompt
# from the exact launcher serial. Neither step consults the network.
$loadSkillInstaller = Join-Path $Workspace 'org\mcp\install-codex-load-skill.py'
$seatLoadRenderer = Join-Path $Workspace 'org\mcp\codex-seat-load.py'
foreach ($requiredLoadHelper in @($loadSkillInstaller, $seatLoadRenderer)) {
    if (-not (Test-Path -LiteralPath $requiredLoadHelper)) {
        throw "Codex seat load helper not found: $requiredLoadHelper"
    }
}

$skillInstallOutput = @(
    & python -u $loadSkillInstaller --workspace $Workspace --format quiet 2>&1
)
$skillInstallExitCode = $LASTEXITCODE
if ($skillInstallExitCode -ne 0) {
    $detail = ($skillInstallOutput | ForEach-Object { [string]$_ }) -join "`n"
    throw "Codex skill installation failed (exit $skillInstallExitCode): $detail"
}

$startupPromptOutput = @(
    & python -u $seatLoadRenderer --workspace $Workspace --serial $Serial `
      --format prompt 2>&1
)
$startupPromptExitCode = $LASTEXITCODE
if ($startupPromptExitCode -ne 0) {
    $detail = ($startupPromptOutput | ForEach-Object { [string]$_ }) -join "`n"
    throw "Codex seat startup context failed (exit $startupPromptExitCode): $detail"
}
$startupPrompt = (($startupPromptOutput | ForEach-Object { [string]$_ }) -join "`n").Trim()
if ([string]::IsNullOrWhiteSpace($startupPrompt)) {
    throw 'Codex seat startup context produced an empty prompt.'
}

# Windows PowerShell 5.1 serializes native-process arguments through a single
# command-line string. Literal double quotes inside an otherwise single prompt
# argument would reopen that command line and split the prompt at the quoted
# text (for example, comp-which "your question"). Escape only for the native
# invocation; keep $startupPrompt unchanged for the persisted diagnostic file.
$startupPromptArgument = $startupPrompt.Replace('"', '\"')

Set-CodexSeatTitle -SeatSerial $Serial

# Reuse the estate's serial-scoped registration cleanup before asserting that
# no predecessor helpers remain. Codex calls server.register_agent directly,
# so Claude's PostToolUse hook runner is absent; feeding the same hook payload
# here preserves the one established cleanup implementation. This runs before
# any new heartbeat/bridge/monitor exists, so it cannot reap the incoming seat.
$orphanCleanupHook = Join-Path $Workspace 'org\mcp\hook_register_orphan_cleanup.py'
if (-not (Test-Path -LiteralPath $orphanCleanupHook)) {
    throw "Serial-scoped orphan cleanup hook not found: $orphanCleanupHook"
}
$cleanupPayload = @{
    tool_input = @{ agent_serial = $Serial }
} | ConvertTo-Json -Compress
$savedClaudeSession = Get-Item -LiteralPath 'Env:CLAUDE_CODE_SESSION_ID' `
  -ErrorAction SilentlyContinue
try {
    # A launcher cleanup is one attempt per new seat, not a Claude-hook session;
    # do not let an unrelated inherited marker suppress it.
    Remove-Item -LiteralPath 'Env:CLAUDE_CODE_SESSION_ID' `
      -ErrorAction SilentlyContinue
    $cleanupPayload | & python $orphanCleanupHook
    $cleanupExitCode = $LASTEXITCODE
}
finally {
    if ($null -ne $savedClaudeSession) {
        Set-Item -LiteralPath 'Env:CLAUDE_CODE_SESSION_ID' `
          -Value $savedClaudeSession.Value
    }
}
# FRESH SESSION ID PER CODEX CHILD (2026-09-03, 1.0.0_SA_CTO on 2.0.0_SA_COO's /drive tick-4 finding, row
# NFRA_COMPEFFICACY-S28 by 0.8.0_AE_CloudComp~H): this launcher inherits the PARENT Claude session's
# CLAUDE_CODE_SESSION_ID through the environment, so ten Codex lanes launched from one COO seat shared one
# session id and every per-session file keyed on it (comp-to's .to_id, comp-which's .route) became
# last-writer-wins across the lanes -- the COO's own .to_id read a task order it never set. The seat's
# children (app-server, bridge, heartbeat) get a session id that is THEIRS; the serial file for that id is
# written here so the session-keyed identity tier (comp_log_auto, the L6 gate's committer read) resolves for
# a Codex seat exactly as it does for a Claude one. The parent's variable is untouched (this is a child
# process of Start-Process).
$env:CLAUDE_CODE_SESSION_ID = [guid]::NewGuid().ToString()
$sessionsDir = Join-Path $Workspace 'org\mcp\sessions'
New-Item -ItemType Directory -Force -Path $sessionsDir | Out-Null
Set-Content -LiteralPath (Join-Path $sessionsDir ($env:CLAUDE_CODE_SESSION_ID + '.serial')) -Value $Serial -Encoding ascii -NoNewline
if ($cleanupExitCode -ne 0) {
    throw "Serial-scoped orphan cleanup hook failed for $Serial (exit $cleanupExitCode)."
}

$conflictNames = @(
    'codex-inbox-turn-bridge.py',
    'codex-inbox-monitor.py',
    'codex-agent-heartbeat.py',
    'inbox-watch.sh',
    '[HARD-NUDGE]',
    '[INBOX]'
)
$serialPattern = '(?<![\w~])' + [regex]::Escape($Serial) + '(?![~\w])'
$conflicts = Get-CimInstance Win32_Process | Where-Object {
    $candidate = $_
    $matchingName = $conflictNames | Where-Object {
        $candidate.CommandLine -and $candidate.CommandLine.Contains($_)
    }
    $serialMatch = $candidate.CommandLine -and
      $candidate.CommandLine -match $serialPattern
    $candidate.ProcessId -ne $PID -and
    $candidate.CommandLine -and
    $serialMatch -and
    $matchingName.Count -gt 0
}
if ($conflicts) {
    $description = ($conflicts | ForEach-Object {
        "PID $($_.ProcessId): $($_.CommandLine)"
    }) -join [Environment]::NewLine
    throw "Refusing duplicate watcher/heartbeat processes for ${Serial}:`n$description"
}

function ConvertTo-ProcessArgument {
    param([Parameter(Mandatory = $true)][string]$Value)
    return '"' + $Value.Replace('"', '\"') + '"'
}

if ($Port -eq 0) {
    $listener = [System.Net.Sockets.TcpListener]::new(
        [System.Net.IPAddress]::Loopback,
        0
    )
    $listener.Start()
    $Port = ([System.Net.IPEndPoint]$listener.LocalEndpoint).Port
    $listener.Stop()
}

$endpoint = "ws://127.0.0.1:$Port"
$runtimeDir = Join-Path $Workspace ('.runtime\codex-seats\' + ($Serial -replace '[^A-Za-z0-9_.~-]', '_'))
# THE LANE'S INBOX AND ITS read/ EXIST BEFORE THE FIRST TURN (2026-09-03, 2.0.0_SA_COO 93817): a Claude seat's watcher
# creates <lane>/read/ when it arms; this runtime has no watcher, and a fresh lane (~N, ~U) met its first mail with an
# inbox root and no read/ folder. The broker now creates read/ on every delivery too; this is the launch-time half so a
# seat's very first sweep has the folder whether or not anything has been delivered yet. Same path grammar as
# server.py's _deliver_to_one: base serial folder, then ~suffix for a lane.
$inboxBase = ($Serial -split '~', 2)[0]
$inboxLane = Join-Path $Workspace ('org\mcp\inbox\' + $inboxBase)
if ($Serial -match '~') { $inboxLane = Join-Path $inboxLane ('~' + ($Serial -split '~', 2)[1]) }
New-Item -ItemType Directory -Force -Path (Join-Path $inboxLane 'read') | Out-Null
New-Item -ItemType Directory -Path $runtimeDir -Force | Out-Null
$startupPromptPath = Join-Path $runtimeDir 'startup-prompt.txt'
[System.IO.File]::WriteAllText(
    $startupPromptPath,
    $startupPrompt + [Environment]::NewLine,
    [System.Text.UTF8Encoding]::new($false)
)

# A stale binding record from a prior session would be read by the NEW
# heartbeat as current state -- delete it BEFORE anything registers, so the
# summary is DEGRADED-truthful until THIS session's bridge actually binds.
Remove-Item -LiteralPath (Join-Path $runtimeDir 'bridge-state.json') `
  -ErrorAction SilentlyContinue

$appServerOut = Join-Path $runtimeDir 'app-server.stdout.log'
$appServerErr = Join-Path $runtimeDir 'app-server.stderr.log'
$bridgeOut = Join-Path $runtimeDir 'turn-bridge.stdout.log'
$bridgeErr = Join-Path $runtimeDir 'turn-bridge.stderr.log'
$heartbeatOut = Join-Path $runtimeDir 'heartbeat.stdout.log'
$heartbeatErr = Join-Path $runtimeDir 'heartbeat.stderr.log'
$preflightOut = Join-Path $runtimeDir 'thread-preflight.stdout.log'
$preflightErr = Join-Path $runtimeDir 'thread-preflight.stderr.log'

function Stop-OwnedProcessTree {
    param([Parameter(Mandatory = $true)][System.Diagnostics.Process]$RootProcess)

    # CLI shims can exit after spawning node.exe and the native Codex binary.
    # Preserve the original root PID and walk its exact descendant tree even
    # when that wrapper has already exited.
    $snapshot = @(Get-CimInstance Win32_Process)
    $nodes = [System.Collections.Generic.List[object]]::new()
    $frontier = @([pscustomobject]@{ Id = [int]$RootProcess.Id; Depth = 0 })
    $seen = [System.Collections.Generic.HashSet[int]]::new()
    while ($frontier.Count -gt 0) {
        $next = @()
        foreach ($item in $frontier) {
            if (-not $seen.Add([int]$item.Id)) {
                continue
            }
            $nodes.Add($item)
            foreach ($child in $snapshot | Where-Object {
                [int]$_.ParentProcessId -eq [int]$item.Id
            }) {
                $next += [pscustomobject]@{
                    Id = [int]$child.ProcessId
                    Depth = [int]$item.Depth + 1
                }
            }
        }
        $frontier = $next
    }

    foreach ($node in $nodes | Sort-Object Depth -Descending) {
        if (Get-Process -Id $node.Id -ErrorAction SilentlyContinue) {
            Stop-Process -Id $node.Id -Force -ErrorAction SilentlyContinue
        }
    }
}

$owned = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()
$codexPermissionArgs = @(
    '-c', 'default_permissions=":danger-full-access"',
    '-c', 'approval_policy="never"'
)
try {
    $appServerArgs = ($codexPermissionArgs + @('app-server', '--listen', $endpoint)) |
      ForEach-Object { ConvertTo-ProcessArgument $_ }
    # Start-Process WITH -Redirect* goes through raw CreateProcess and takes the EXACT-NAME file first, so 'codex' must be a REAL .exe on PATH
    # (bun's codex.exe). An npm global install ships an extensionless POSIX 'codex' beside codex.cmd/.ps1: Get-Command, --version and `which`
    # all PASS on it while this line dies with '%1 is not a valid Win32 application' (site Z, 2026-09-11). The check that passes is not the call that runs.
    $appServer = Start-Process -FilePath 'codex' -ArgumentList $appServerArgs `
      -WorkingDirectory $Workspace -WindowStyle Hidden -PassThru `
      -RedirectStandardOutput $appServerOut -RedirectStandardError $appServerErr
    $owned.Add($appServer)

    $ready = $false
    for ($attempt = 0; $attempt -lt 100; $attempt++) {
        if ($appServer.HasExited) {
            throw "Codex app-server exited early; see $appServerErr"
        }
        $client = [System.Net.Sockets.TcpClient]::new()
        try {
            $client.Connect('127.0.0.1', $Port)
            $ready = $true
            break
        }
        catch {
            Start-Sleep -Milliseconds 100
        }
        finally {
            $client.Dispose()
        }
    }
    if (-not $ready) {
        throw "Codex app-server did not listen on $endpoint"
    }

    if ($ThreadId) {
        $preflightArgs = @(
            '-u', (Join-Path $Workspace 'org\mcp\codex-inbox-turn-bridge.py'),
            '--serial', $Serial,
            '--endpoint', $endpoint,
            '--cwd', $Workspace,
            '--thread-id', $ThreadId,
            '--preflight-only'
        ) | ForEach-Object { ConvertTo-ProcessArgument $_ }
        $preflight = Start-Process -FilePath 'python' -ArgumentList $preflightArgs `
          -WorkingDirectory $Workspace -WindowStyle Hidden -PassThru -Wait `
          -RedirectStandardOutput $preflightOut -RedirectStandardError $preflightErr
        $preflightExitCode = $preflight.ExitCode
        $preflight.Dispose()
        if ($preflightExitCode -ne 0) {
            $detail = [string](Get-Content -LiteralPath $preflightErr -Raw `
              -ErrorAction SilentlyContinue)
            $detail = $detail.Trim()
            if ($detail -match 'active writer') {
                throw @"
Cannot migrate thread $ThreadId because its old Codex TUI still owns the active-writer lock.
Exit the old TUI completely, wait for its codex process to close, then rerun this launcher.
Stopping watcher/heartbeat helpers alone does not release the thread writer.
Preflight detail: $detail
"@
            }
            throw "Codex thread preflight failed for $ThreadId. See ${preflightErr}: $detail"
        }
    }

    $heartbeatArgs = @(
        '-u', (Join-Path $Workspace 'org\mcp\codex-agent-heartbeat.py'),
        '--serial', $Serial,
        '--runtime-dir', $runtimeDir
    ) | ForEach-Object { ConvertTo-ProcessArgument $_ }
    $heartbeat = Start-Process -FilePath 'python' -ArgumentList $heartbeatArgs `
      -WorkingDirectory $Workspace -WindowStyle Hidden -PassThru `
      -RedirectStandardOutput $heartbeatOut -RedirectStandardError $heartbeatErr
    $owned.Add($heartbeat)

    $bridgeArgs = @(
        '-u', (Join-Path $Workspace 'org\mcp\codex-inbox-turn-bridge.py'),
        '--serial', $Serial,
        '--endpoint', $endpoint,
        '--cwd', $Workspace,
        '--runtime-dir', $runtimeDir
    )
    if ($ThreadId) {
        $bridgeArgs += @('--thread-id', $ThreadId)
    }
    $bridgeProcessArgs = $bridgeArgs | ForEach-Object { ConvertTo-ProcessArgument $_ }
    $bridge = Start-Process -FilePath 'python' -ArgumentList $bridgeProcessArgs `
      -WorkingDirectory $Workspace -WindowStyle Hidden -PassThru `
      -RedirectStandardOutput $bridgeOut -RedirectStandardError $bridgeErr
    $owned.Add($bridge)

    # FAIL CLOSED ON EARLY BRIDGE DEATH. The bridge now supervises thread
    # discovery indefinitely, so ANY exit this early is a real defect (bad
    # python, bad endpoint, import error) -- not a slow operator. Before this
    # gate the launcher reported the seat normally while the bridge lay dead
    # and its detector child had never existed (measured 2026-08-26 on CRO
    # base + ~B; the heartbeat's summary reported the seat green regardless).
    Start-Sleep -Seconds 3
    if ($bridge.HasExited) {
        $bridgeDetail = [string](Get-Content -LiteralPath $bridgeErr -Raw `
          -ErrorAction SilentlyContinue)
        throw ("FAILED COMPONENT: codex-inbox-turn-bridge exited " +
          "(code $($bridge.ExitCode)) within 3s of launch. Seat is NOT " +
          "provisioned; owned processes will be reaped. Bridge stderr: " +
          $bridgeDetail.Trim())
    }
    if ($heartbeat.HasExited) {
        $hbDetail = [string](Get-Content -LiteralPath $heartbeatErr -Raw `
          -ErrorAction SilentlyContinue)
        throw ("FAILED COMPONENT: codex-agent-heartbeat exited " +
          "(code $($heartbeat.ExitCode)) within 3s of launch. Seat is NOT " +
          "provisioned; owned processes will be reaped. Heartbeat stderr: " +
          $hbDetail.Trim())
    }

    Write-Host "Codex seat host: $Serial"
    Write-Host "Shared app-server: $endpoint"
    Write-Host "Runtime logs: $runtimeDir"
    Write-Host "Startup load prompt: $startupPromptPath"
    Write-Host ("Bridge: supervising thread discovery (binds when the TUI " +
      "thread persists; waits indefinitely -- this is normal on a fresh seat)")
    Write-Host ("READINESS IS MEASURED, NOT ANNOUNCED: run " +
      "org\mcp\codex-seat-status.ps1 -Serial $Serial " +
      "-- exit 0 is the only green. Liveness/broker alone are NOT readiness.")

    Enable-CodexSeatColor
    Set-CodexSeatTitle -SeatSerial $Serial

    if ($ThreadId) {
        & codex @codexPermissionArgs resume --remote $endpoint -C $Workspace `
          $ThreadId $startupPromptArgument
    }
    else {
        & codex @codexPermissionArgs --remote $endpoint -C $Workspace $startupPromptArgument
    }
}
finally {
    foreach ($name in $colorEnvironmentNames) {
        $original = $originalColorEnvironment[$name]
        if ($original.Exists) {
            Set-Item -LiteralPath "Env:$name" -Value $original.Value
        }
        else {
            Remove-Item -LiteralPath "Env:$name" -ErrorAction SilentlyContinue
        }
    }
    foreach ($process in $owned) {
        Stop-OwnedProcessTree -RootProcess $process
        $process.Dispose()
    }
}
