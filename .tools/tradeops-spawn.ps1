# tradeops-spawn.ps1 -- spawn ONE seat on the TRADEOPS fabric with Remote Control on,
# then drive it past the development-channels approval prompt and PROVE it registered.
#
# WHY THIS EXISTS. `ajb3` is the tradeops fabric's customary launcher and it is the
# right thing for a human at a keyboard. It has NO -RemoteControl switch, and its
# non-headless path adds --dangerously-load-development-channels, which raises a
# blocking Y/N prompt at startup -- ajb3's own source says so ("so autonomous spawns
# never stall on its Y/N startup prompt"). An agent spawning a seat therefore lands a
# tab that looks launched, returns exit 0, and sits frozen forever. Measured
# 2026-09-11T21:44Z: claude.exe alive, CPU flat at 2.7s across 8s, no MCP child, no
# broker registration after 5 minutes. This script closes that gap end to end.
#
# ⛔ THE LAUNCH IS NOT THE ORACLE. A returned exit code, a created tab and a running
# claude.exe are all consistent with a seat frozen at a prompt. The ONLY success signal
# this script accepts is the serial appearing in the TRADEOPS broker's liveness store,
# which only the agent itself can cause.
#
# Usage:
#   powershell -NoProfile -ExecutionPolicy Bypass -File .tools\tradeops-spawn.ps1 -Serial 4.0.0_SA_CRO
#   ... -DryRun            resolve + validate + print the exact command, launch NOTHING
#   ... -NoRemoteControl   omit --remote-control
#   ... -TimeoutSec 240    how long to wait for registration (default 180)
#   ... -Force             spawn even if that serial already reads live (audited in the output)
#
# Exit codes: 0 registered · 2 launch failed / preconditions unmet · 3 launched but never
# registered (the tab is up; a human should look) · 4 refused, serial already live.

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)] [string]$Serial,
    [switch]$NoRemoteControl,
    [switch]$DryRun,
    [switch]$Force,
    [int]$TimeoutSec = 180
)

$ErrorActionPreference = 'Stop'
function Say($m, $c = 'Gray') { Write-Host "[tradeops-spawn] $m" -ForegroundColor $c }

# --- 1. ROOT -------------------------------------------------------------------
# OPAL_TRADEOPS_ROOT first (the device-level escape hatch ajb3 itself honours), then
# the standard clone location. Never a guess: if neither exists we stop.
$Root = $null
if ($env:OPAL_TRADEOPS_ROOT -and (Test-Path -LiteralPath $env:OPAL_TRADEOPS_ROOT)) {
    $Root = (Resolve-Path -LiteralPath $env:OPAL_TRADEOPS_ROOT).Path
    Say "root from OPAL_TRADEOPS_ROOT: $Root"
} else {
    $std = 'C:\Users\AndrewBerman\Downloads\docs_abcdeg'
    if (Test-Path -LiteralPath $std) { $Root = (Resolve-Path -LiteralPath $std).Path; Say "root derived: $Root" }
}
if (-not $Root) { Say "TRADEOPS ROOT NOT FOUND. Set OPAL_TRADEOPS_ROOT and retry." 'Red'; exit 2 }

$ajb3     = Join-Path $Root 'entry\windows\ajb3.ps1'
$launchPy = Join-Path $Root '.tools\launch-directive.py'
$liveness = Join-Path $Root 'org\mcp\liveness.json'
foreach ($f in @($ajb3, $launchPy)) {
    if (-not (Test-Path -LiteralPath $f)) { Say "MISSING: $f" 'Red'; exit 2 }
}

# --- 2. DRIFT CHECK against the real ajb3 --------------------------------------
# This script MIRRORS ajb3's flag set. A mirror with only a comment holding it true
# goes stale silently, so assert the strings are still there and WARN loudly if not.
# This is a warning, never a block: ajb3 changing is not a reason to refuse a spawn.
$ajb3src = Get-Content -LiteralPath $ajb3 -Raw
$mirrored = @(
    '--dangerously-skip-permissions',
    '--dangerously-load-development-channels',
    'server:tradeops-agent-comms',
    "OPAL_BROKER_PORT = '7801'"
)
$missing = @($mirrored | Where-Object { $ajb3src -notlike "*$_*" })
if ($missing.Count -gt 0) {
    Say "DRIFT: ajb3.ps1 no longer contains: $($missing -join ', ')" 'Yellow'
    Say "       This script's mirrored flag set may be stale -- re-read entry\windows\ajb3.ps1." 'Yellow'
} else {
    Say "drift check: ajb3.ps1 still carries all $($mirrored.Count) mirrored strings"
}

# --- 3. SERIAL VALIDITY (fail closed) ------------------------------------------
Push-Location $Root
try {
    $loop = & python $launchPy --role $Serial 2>&1
    if ($LASTEXITCODE -ne 0) { Say "launch-directive.py rejected serial '$Serial': $loop" 'Red'; exit 2 }
    $loop = ($loop -join "`n")
    # ⛔ THE EXIT CODE IS NOT A VALIDITY ORACLE. launch-directive.py returns 0 for a serial it
    # does not recognise and reports it only in its TEXT:
    #   "UNRECOGNIZED ('<serial>' matched no role pattern)"
    # Measured 2026-09-11 -- the first version of this script checked $LASTEXITCODE alone and
    # called it fail-closed; '9.9.9_XX_NotAThing' passed and would have opened a tab for a seat
    # with no role. Keying on the marker means this check PARSES THE TOOL'S PROSE and inherits
    # every future edit to that string; that is a worse instrument than an exit code and is used
    # only because the tool emits nothing better. If the marker is ever renamed, this silently
    # stops catching -- which is why the WARN below names the string it looked for.
    if ($loop -match 'UNRECOGNIZED') {
        if ($Force) {
            Say "-Force: '$Serial' is UNRECOGNIZED by launch-directive.py (no role pattern) -- spawning anyway" 'Yellow'
        } else {
            Say "REFUSED: launch-directive.py does not recognise '$Serial' -- it matched no role pattern." 'Red'
            Say "         The seat would launch with no role directive. Check the serial, or -Force if you mean it." 'Red'
            exit 2
        }
    }
    $modelArgs = @(& python $launchPy --claude-args $Serial 2>&1)
    if ($LASTEXITCODE -ne 0) { Say "launch-directive.py --claude-args failed for '$Serial'" 'Red'; exit 2 }
    $modelArgs = @($modelArgs | Where-Object { $_ -ne '' })
} finally { Pop-Location }
Say "serial OK; role directive resolved ($($loop.Length) chars); model args: [$($modelArgs -join ' ')]"

# --- 4. DUPLICATE GUARD ---------------------------------------------------------
# A second live session under one serial is an identity conflict, and the loser is
# silent. Refuse unless -Force.
if (Test-Path -LiteralPath $liveness) {
    try {
        $lv = Get-Content -LiteralPath $liveness -Raw | ConvertFrom-Json
        $row = $lv.PSObject.Properties | Where-Object { $_.Name -eq $Serial } | Select-Object -First 1
        if ($row) {
            $pid0 = $row.Value.pid
            $alive = $false
            if ($pid0) { $alive = [bool](Get-Process -Id $pid0 -ErrorAction SilentlyContinue) }
            if ($alive -and $DryRun) {
                # A dry run DESCRIBES; it must not exit before showing the command, or the
                # one thing the operator asked to see is the one thing withheld.
                Say "NOTE (dry run): $Serial is already registered and pid $pid0 is ALIVE -- a real run would REFUSE with rc=4 unless -Force." 'Yellow'
            } elseif ($alive -and -not $Force) {
                Say "REFUSED: $Serial already registered and pid $pid0 is ALIVE. Use -Force only if you mean two sessions." 'Red'
                exit 4
            } elseif ($alive) {
                Say "-Force: spawning a SECOND $Serial while pid $pid0 is alive (identity conflict accepted by the operator)" 'Yellow'
            } else {
                Say "stale liveness row for $Serial (pid $pid0 gone) -- proceeding"
            }
        }
    } catch { Say "liveness.json unreadable ($($_.Exception.Message)) -- proceeding without the duplicate guard" 'Yellow' }
}

# --- 5. BUILD THE LAUNCH --------------------------------------------------------
$watcher = "FIRST: run /watcher to self-heal inbox-watcher + broker registration. THEN: start_here.md startup protocol."
$firstMessage = "$Serial`n`n$watcher`n`n$loop"

$claudeArgs = @('--dangerously-skip-permissions')
if ($modelArgs.Count -gt 0) { $claudeArgs += $modelArgs }
$claudeArgs += @('--dangerously-load-development-channels', 'server:tradeops-agent-comms')
if (-not $NoRemoteControl) {
    # Named EXPLICITLY: --remote-control takes an OPTIONAL value, so a bare flag can
    # swallow the next token as the session name.
    $claudeArgs += @('--remote-control', $Serial)
}
$claudeArgs += @('--', $firstMessage)

if ($DryRun) {
    Say "DRY RUN -- nothing launched." 'Cyan'
    Say "cwd:    $Root"
    Say "env:    OPAL_AGENT_SERIAL=$Serial OPAL_BROKER_PORT=7801 OPAL_TRADEOPS_ROOT=$Root AJB3_NO_WT_RELAUNCH=1"
    Say "claude $(($claudeArgs | Select-Object -SkipLast 2) -join ' ') -- <first message, $($firstMessage.Length) chars>"
    exit 0
}

# The child runs this generated script so nothing has to survive wt's quoting layers.
$stamp   = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ')
$runner  = Join-Path $env:TEMP "tradeops-spawn_${Serial}_$stamp.ps1"
$argLits = ($claudeArgs | ForEach-Object { "'" + ($_ -replace "'", "''") + "'" }) -join ",`n    "
$body = @"
`$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath '$($Root -replace "'","''")'
`$env:OPAL_AGENT_SERIAL   = '$($Serial -replace "'","''")'
`$env:OPAL_BROKER_PORT    = '7801'
`$env:OPAL_TRADEOPS_ROOT  = '$($Root -replace "'","''")'
`$env:AJB3_NO_WT_RELAUNCH = '1'
`$env:FORCE_COLOR         = '3'
`$a = @(
    $argLits
)
& claude @a
"@
Set-Content -LiteralPath $runner -Value $body -Encoding UTF8
Say "runner: $runner"

$wt = Get-Command wt.exe -ErrorAction SilentlyContinue
if (-not $wt) { Say "wt.exe not found -- cannot create a TITLED tab, and /unstick needs the title to find it." 'Red'; exit 2 }
& wt.exe -w 0 new-tab --title $Serial powershell.exe -NoProfile -NoExit -ExecutionPolicy Bypass -File $runner
Say "tab requested for $Serial (remote-control: $(if ($NoRemoteControl) {'OFF'} else {'ON'}))" 'Cyan'

# --- 6. WAIT FOR REGISTRATION, UNSTICK ONCE IF IT STALLS ------------------------
function Test-Registered {
    if (-not (Test-Path -LiteralPath $liveness)) { return $false }
    try {
        $lv = Get-Content -LiteralPath $liveness -Raw | ConvertFrom-Json
        $r = $lv.PSObject.Properties | Where-Object { $_.Name -eq $Serial } | Select-Object -First 1
        if (-not $r) { return $false }
        $p = $r.Value.pid
        if ($p -and -not (Get-Process -Id $p -ErrorAction SilentlyContinue)) { return $false }
        return $true
    } catch { return $false }
}

$half = [Math]::Max(30, [int]($TimeoutSec / 3))
$sw = [Diagnostics.Stopwatch]::StartNew()
$unstuck = $false
$peek = $null
while ($sw.Elapsed.TotalSeconds -lt $TimeoutSec) {
    if (Test-Registered) {
        Say "REGISTERED on the tradeops broker after $([int]$sw.Elapsed.TotalSeconds)s" 'Green'
        Say "SUCCESS $Serial -- remote-control $(if ($NoRemoteControl) {'OFF'} else {'ON'}), broker 7801, cwd $Root" 'Green'
        exit 0
    }
    if (-not $unstuck -and $sw.Elapsed.TotalSeconds -ge $half) {
        # Only ever keyed at a seat that has NOT registered -- never a healthy one.
        $unstickPs1 = Join-Path $PSScriptRoot 'unstick.ps1'
        if (Test-Path -LiteralPath $unstickPs1) {
            Say "no registration after $([int]$sw.Elapsed.TotalSeconds)s -- peeking, then answering the dev-channels prompt" 'Yellow'
            $peek = Join-Path $env:TEMP "tradeops-spawn_peek_${Serial}_$stamp.png"
            & powershell -NoProfile -ExecutionPolicy Bypass -File $unstickPs1 -Serial $Serial -Peek -OutFile $peek 2>&1 | ForEach-Object { Say "  peek: $_" }
            & powershell -NoProfile -ExecutionPolicy Bypass -File $unstickPs1 -Serial $Serial -Keys '1{ENTER}' 2>&1 | ForEach-Object { Say "  unstick: $_" }
        } else {
            Say "unstick.ps1 not found beside this script -- cannot auto-answer the prompt" 'Yellow'
        }
        $unstuck = $true
    }
    Start-Sleep -Seconds 5
}

Say "LAUNCHED BUT NEVER REGISTERED within ${TimeoutSec}s. The tab exists; the seat did not come up." 'Red'
if ($peek) { Say "READ THIS IMAGE -- it shows what the tab is actually sitting on: $peek" 'Red' }
Say "Next: re-peek with .tools\unstick.ps1 -Serial $Serial -Peek and read the PNG; the prompt may have a different shape." 'Red'
exit 3
