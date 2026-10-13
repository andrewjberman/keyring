# seat-boundary.ps1 -- the seat boundary shared by kill-agent.ps1, kill-maint.ps1 and spawn-agent.ps1.
#
# Dot-source this file. It defines functions only and starts no process.
#
# A SEAT is a claude.exe or codex.exe whose command line carries its LAUNCH SERIAL as the first full serial token
# (ajb.ps1 opens claude with the serial as its first message). Another seat's launch hint may NAME
# a serial further along a command line, so "the command line contains the serial" is not identity.
# A kill must match the launch serial exactly, and a kill must not stop a process tree that holds a
# seat with a different launch serial (that seat would die with the tree it was never part of).
#
#   Get-LaunchSerial -CommandLine <text>                     -> first full serial token, or $null
#   Test-LaunchSerialMatch -CommandLine <text> -Serial <s> [-Family]
#                                                            -> $true when the launch serial is <s>
#                                                               (with -Family: or a ~lane of <s>)
#   Test-SeatBoundary -RootPid <n> -TargetSerial <s> [-Family] [-Selected <int[]>] [-Processes <list>]
#                                                            -> @() when the tree is clear; otherwise one
#                                                               object per FOREIGN seat: ProcessId, Serial, Name
#
# -Processes takes fake process objects (ProcessId, ParentProcessId, Name, CommandLine) for tests;
# without it the live Win32_Process table is read. A claude.exe or codex.exe with no serial token is not
# a seat (a native helper; S9118 notes) and is never reported. -Selected names pids the caller is killing in
# the same run; a selected seat is not foreign. A null -TargetSerial makes every serial-bearing seat foreign.

$script:SeatSerialRe = '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9_]+(~[A-Za-z0-9]+)?$'

# The process names that carry a seat. One name set: Test-SeatBoundary judges every name in it the same way.
$script:SeatAgentNames = @('claude.exe', 'codex.exe')

function Get-LaunchSerial {
    param([string]$CommandLine)
    if (-not $CommandLine) { return $null }
    foreach ($tok in ($CommandLine -split '\s+')) {
        $t = $tok.Trim('"', "'", '`', ',', ';', ':', '(', ')', '[', ']', '{', '}', '<', '>', '.')
        if ($t -and $t -match $script:SeatSerialRe) { return $t }
    }
    return $null
}

function Test-LaunchSerialMatch {
    param(
        [string]$CommandLine,
        [string]$Serial,
        [switch]$Family
    )
    if (-not $Serial) { return $false }
    $ls = Get-LaunchSerial -CommandLine $CommandLine
    if (-not $ls) { return $false }
    if ($ls -eq $Serial) { return $true }
    if ($Family -and $ls.StartsWith($Serial + '~', [System.StringComparison]::OrdinalIgnoreCase)) { return $true }
    return $false
}

function Test-SeatBoundary {
    param(
        [Parameter(Mandatory = $true)][int]$RootPid,
        [string]$TargetSerial,
        [switch]$Family,
        [int[]]$Selected = @(),
        [object[]]$Processes
    )
    if (-not $PSBoundParameters.ContainsKey('Processes')) {
        $Processes = @(Get-CimInstance Win32_Process -ErrorAction Stop |
            Select-Object ProcessId, ParentProcessId, Name, CommandLine)
    }
    $kids = @{}
    foreach ($p in $Processes) {
        $pp = [int]$p.ParentProcessId
        if (-not $kids.ContainsKey($pp)) { $kids[$pp] = New-Object System.Collections.ArrayList }
        [void]$kids[$pp].Add($p)
    }
    $seen  = New-Object 'System.Collections.Generic.HashSet[int]'
    $queue = New-Object 'System.Collections.Generic.Queue[int]'
    $queue.Enqueue([int]$RootPid)
    $foreign = New-Object System.Collections.ArrayList
    while ($queue.Count -gt 0) {
        $cur = $queue.Dequeue()
        if (-not $kids.ContainsKey($cur)) { continue }
        foreach ($k in $kids[$cur]) {
            $kp = [int]$k.ProcessId
            if ($kp -eq [int]$RootPid -or -not $seen.Add($kp)) { continue }
            $queue.Enqueue($kp)
            if ($k.Name -notin $script:SeatAgentNames) { continue }
            $ls = Get-LaunchSerial -CommandLine $k.CommandLine
            if (-not $ls) { continue }
            if ($Selected -contains $kp) { continue }
            if (Test-LaunchSerialMatch -CommandLine $k.CommandLine -Serial $TargetSerial -Family:$Family) { continue }
            [void]$foreign.Add([PSCustomObject]@{ ProcessId = $kp; Serial = $ls; Name = $k.Name })
        }
    }
    # Emit the objects plainly: callers wrap in @(), so an empty result is count 0 (a ,@() wrapper counts 1).
    return $foreign.ToArray()
}
