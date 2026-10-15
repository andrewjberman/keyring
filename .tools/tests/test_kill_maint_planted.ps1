# test_kill_maint_planted.ps1 -- CT-ae-1 (row NFRA_CTLPLN-S9118): a planted tree holding a foreign seat survives a REAL
# kill-maint.ps1 -Execute run, and a plain planted tree dies under the same run.
#
# Starts ONLY its own planted processes: two python.exe roots created through WMI (Win32_Process.Create), each with a
# working directory in a temporary folder outside every checkout, their native children, and a copy of cmd.exe named
# claude.exe (its child is ping.exe). Each root is stopped ONLY by kill-maint.ps1 -OnlyPid (never without it). Every planted PID is killed
# in a finally block, by PID (the creation time recorded at start must still match) and by image path (the temporary
# folder). The real claude.exe seats are READ for a count before and after; nothing about them is changed.
# Run:  powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_kill_maint_planted.ps1
# Final line: KILL-MAINT-PLANTED cases=<k>/<n> ok=<True|False>

$ErrorActionPreference = 'Stop'
$tools      = Split-Path -Parent $PSScriptRoot
$killMaint  = Join-Path $tools 'kill-maint.ps1'
$fakeSerial = '9.9.0_SA_TEST~PLANT'

$script:n = 0
$script:k = 0
function Check {
    param([string]$Name, [bool]$Ok)
    $script:n++
    if ($Ok) { $script:k++ }
    $tag = if ($Ok) { 'PASS' } else { 'FAIL' }
    Write-Output ("{0}  {1}" -f $tag, $Name)
}

# The helper below is the planted root's program. It starts only harmless children (ping.exe, or the claude.exe copy).
$helperText = @'
import os
import subprocess
import sys

PING = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'System32', 'PING.EXE')

def main():
    mode = sys.argv[1]
    if mode == 'seat':
        claude_copy = sys.argv[2]
        cmd = [claude_copy, '/d', '/c', 'ping -n 900 127.0.0.1 >nul & rem 9.9.0_SA_TEST~PLANT begin']
    else:
        cmd = [PING, '-n', '900', '127.0.0.1']
    subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

main()
'@

function Get-ProcRows {
    @(Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine, CreationDate)
}

# The root row (when present) followed by every descendant, breadth first.
function Get-PlantTree {
    param([int]$Root, $Rows)
    $out  = New-Object System.Collections.ArrayList
    $seen = @{}
    foreach ($r in $Rows) { if ([int]$r.ProcessId -eq $Root) { [void]$out.Add($r); $seen[$Root] = $true } }
    $queue = New-Object System.Collections.Queue
    $queue.Enqueue($Root)
    while ($queue.Count -gt 0) {
        $cur = [int]$queue.Dequeue()
        foreach ($r in $Rows) {
            $me = [int]$r.ProcessId
            if ([int]$r.ParentProcessId -eq $cur -and -not $seen.ContainsKey($me)) {
                $seen[$me] = $true
                [void]$out.Add($r)
                $queue.Enqueue($me)
            }
        }
    }
    return @($out)
}

# WMI creates the root: its parent is the WMI provider host (not a shell), and its working directory is the temp folder.
function Start-PlantRoot {
    param([string]$CommandLine, [string]$WorkDir)
    $r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{ CommandLine = $CommandLine; CurrentDirectory = $WorkDir }
    if ($r.ReturnValue -ne 0) { throw ("Win32_Process.Create returned {0}" -f $r.ReturnValue) }
    return [int]$r.ProcessId
}

function Wait-PlantTree {
    param([int]$Root, [string[]]$NeedNames, [int]$Seconds = 30)
    $end = (Get-Date).AddSeconds($Seconds)
    do {
        $tree  = @(Get-PlantTree -Root $Root -Rows (Get-ProcRows))
        $names = @($tree | ForEach-Object { $_.Name })
        $missing = @($NeedNames | Where-Object { $names -notcontains $_ })
        if ($missing.Count -eq 0) { return $tree }
        Start-Sleep -Milliseconds 500
    } while ((Get-Date) -lt $end)
    Write-Host ("  WAIT: tree under {0} missing {1}; names seen: {2}" -f $Root, ($missing -join ','), ($names -join ','))
    return @()
}

function Test-Alive {
    param([int]$ProcId, $Created)
    $now = Get-CimInstance Win32_Process -Filter ("ProcessId={0}" -f $ProcId) -ErrorAction SilentlyContinue
    if (-not $now) { return $false }
    if ($Created -and $now.CreationDate -ne $Created) { return $false }
    return $true
}

function Wait-Gone {
    param($Recorded, [int]$Seconds = 15)
    $end = (Get-Date).AddSeconds($Seconds)
    do {
        $alive = @($Recorded | Where-Object { Test-Alive -ProcId $_.Pid -Created $_.Created })
        if ($alive.Count -eq 0) { return $true }
        Start-Sleep -Milliseconds 500
    } while ((Get-Date) -lt $end)
    return $false
}

# The kill-maint run under test: real script, real -Execute, narrowed by -OnlyPid to one planted root.
function Invoke-KillMaint {
    param([int]$OnlyPid, [string]$Audit)
    $kmArgs = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $killMaint, '-Mode', 'scripts', '-Execute',
                '-OnlyPid', [string]$OnlyPid, '-MinAgeSeconds', '0', '-MonitorCapSeconds', '0', '-AuditLog', $Audit)
    $prev = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $out = @(& powershell.exe @kmArgs 2>&1 | ForEach-Object { "$_" })
    $ErrorActionPreference = $prev
    return $out
}

function Get-RealSeatPids {
    param([hashtable]$Planted)
    @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'" |
        Where-Object { -not $Planted.ContainsKey([int]$_.ProcessId) } |
        ForEach-Object { [int]$_.ProcessId } | Sort-Object)
}

$tmp = Join-Path $env:TEMP ('kmp-planted-' + [guid]::NewGuid().ToString('N').Substring(0, 12))
New-Item -ItemType Directory -Path $tmp | Out-Null
$audit      = Join-Path $tmp 'audit.log'
$helper     = Join-Path $tmp 'kmp_helper.py'
$claudeCopy = Join-Path $tmp 'claude.exe'
$py = Join-Path $env:LOCALAPPDATA 'Programs\Python\Python312\python.exe'
if (-not (Test-Path $py)) { $py = (Get-Command python.exe -ErrorAction Stop).Source }
Write-Output ("python: {0}" -f $py)
Copy-Item (Join-Path $env:SystemRoot 'System32\cmd.exe') $claudeCopy
Set-Content -Path $helper -Value $helperText -Encoding ASCII

$recorded = New-Object System.Collections.ArrayList   # every planted PID with its creation time, root first
$planted  = @{}
$realBefore = @()
$realAfter  = @()

try {
    $realBefore = @(Get-RealSeatPids -Planted @{})
    Write-Output ("REAL-SEATS claude.exe before={0}" -f $realBefore.Count)

    # ---- TREE A: control, no seat. python root -> ping.exe ----
    $rootA = Start-PlantRoot -CommandLine ('"{0}" "{1}" control' -f $py, $helper) -WorkDir $tmp
    $treeA = @(Wait-PlantTree -Root $rootA -NeedNames @('python.exe', 'PING.EXE'))
    Check 'tree A planted: root python.exe with a native child PING.EXE' ($treeA.Count -ge 2)
    foreach ($r in $treeA) { [void]$recorded.Add([PSCustomObject]@{ Pid = [int]$r.ProcessId; Name = $r.Name; Created = $r.CreationDate }); $planted[[int]$r.ProcessId] = $true }

    $outA = Invoke-KillMaint -OnlyPid $rootA -Audit $audit
    foreach ($ln in $outA) { Write-Output ("  kill-maint(A)| {0}" -f $ln) }
    Check ('tree A: kill-maint names the root as stopped (PID {0})' -f $rootA) (@($outA | Where-Object { $_ -match ("stopped tree PID\s+{0}\s" -f $rootA) }).Count -ge 1)
    $goneA = Wait-Gone -Recorded @($recorded | Where-Object { $_.Pid -in @($treeA | ForEach-Object { [int]$_.ProcessId }) })
    Check 'tree A dies: root and every child gone' $goneA
    Check 'tree A: audit file holds a KILL-MAINT line for the root' (@(Get-Content -Path $audit -ErrorAction SilentlyContinue | Where-Object { $_ -match ("KILL-MAINT\s.*pid={0}\s" -f $rootA) }).Count -ge 1)

    # ---- TREE B: foreign seat. python root -> claude.exe (copy of cmd.exe, serial token) -> ping.exe ----
    $rootB = Start-PlantRoot -CommandLine ('"{0}" "{1}" seat "{2}"' -f $py, $helper, $claudeCopy) -WorkDir $tmp
    $treeB = @(Wait-PlantTree -Root $rootB -NeedNames @('python.exe', 'claude.exe', 'PING.EXE'))
    Check 'tree B planted: root python.exe, a claude.exe seat child, and its PING.EXE child' ($treeB.Count -ge 3)
    foreach ($r in $treeB) { [void]$recorded.Add([PSCustomObject]@{ Pid = [int]$r.ProcessId; Name = $r.Name; Created = $r.CreationDate }); $planted[[int]$r.ProcessId] = $true }
    $seatB = @($treeB | Where-Object { $_.Name -eq 'claude.exe' })
    $seatPid = if ($seatB.Count -gt 0) { [int]$seatB[0].ProcessId } else { 0 }

    $outB = Invoke-KillMaint -OnlyPid $rootB -Audit $audit
    foreach ($ln in $outB) { Write-Output ("  kill-maint(B)| {0}" -f $ln) }
    $refusedLine = @($outB | Where-Object { $_ -match 'REFUSED: seat boundary' -and $_ -match [regex]::Escape($fakeSerial) })
    Check ('tree B: kill-maint REFUSED: seat boundary and names {0}' -f $fakeSerial) ($refusedLine.Count -ge 1)
    $auditB = @(Get-Content -Path $audit -ErrorAction SilentlyContinue | Where-Object { $_ -match ("KILL-MAINT-REFUSED.*pid={0}\s.*reason=seat-boundary" -f $rootB) })
    $auditSeat = @($auditB | Where-Object { $_ -match [regex]::Escape("foreign=$fakeSerial@$seatPid") })
    Check 'tree B: audit holds KILL-MAINT-REFUSED reason=seat-boundary for the root, foreign serial and PID named' ($auditSeat.Count -ge 1)
    Start-Sleep -Seconds 3
    $survivors = @($treeB | Where-Object { Test-Alive -ProcId ([int]$_.ProcessId) -Created $_.CreationDate })
    Check ('tree B survives: root, claude.exe seat and child all still running ({0} of {1})' -f $survivors.Count, $treeB.Count) ($survivors.Count -eq $treeB.Count -and $treeB.Count -ge 3)
}
finally {
    # Kill ONLY what this test started: by PID (children first, creation time must match), then by image path.
    $ordered = @($recorded.ToArray())
    [array]::Reverse($ordered)
    foreach ($x in $ordered) {
        $now = Get-CimInstance Win32_Process -Filter ("ProcessId={0}" -f $x.Pid) -ErrorAction SilentlyContinue
        if ($now -and $now.CreationDate -eq $x.Created) { Stop-Process -Id $x.Pid -Force -ErrorAction SilentlyContinue }
    }
    foreach ($p in @(Get-CimInstance Win32_Process | Where-Object { $_.ExecutablePath -and $_.ExecutablePath.StartsWith($tmp, [System.StringComparison]::OrdinalIgnoreCase) })) {
        Stop-Process -Id ([int]$p.ProcessId) -Force -ErrorAction SilentlyContinue
    }
    Start-Sleep -Seconds 1
    $leftover = @($recorded | Where-Object { Test-Alive -ProcId $_.Pid -Created $_.Created })
    $pathLeft = @(Get-CimInstance Win32_Process | Where-Object { $_.ExecutablePath -and $_.ExecutablePath.StartsWith($tmp, [System.StringComparison]::OrdinalIgnoreCase) })
    Check ('no planted PID remains, by PID and by image path ({0} by PID, {1} by path)' -f $leftover.Count, $pathLeft.Count) ($leftover.Count -eq 0 -and $pathLeft.Count -eq 0)
    foreach ($f in @($helper, $claudeCopy, $audit)) { Remove-Item -Path $f -Force -ErrorAction SilentlyContinue }
    Remove-Item -Path $tmp -Force -ErrorAction SilentlyContinue
    $realAfter = @(Get-RealSeatPids -Planted $planted)
    Write-Output ("REAL-SEATS claude.exe before={0} after={1}" -f $realBefore.Count, $realAfter.Count)
    Check 'the real claude.exe seats are unchanged (same PIDs before and after)' (($realBefore -join ',') -eq ($realAfter -join ','))
}

Write-Output ("KILL-MAINT-PLANTED cases={0}/{1} ok={2}" -f $script:k, $script:n, ($script:k -eq $script:n))
