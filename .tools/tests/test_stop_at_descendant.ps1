# test_stop_at_descendant.ps1 -- fake-process battery for CT-ac-2: kill-agent stops AT a descendant seat.
#
# Kills nothing and starts nothing: every process list is a FAKE passed with -Processes; kill-agent.ps1 is only
# PARSED and inspected through the PowerShell AST (it is never run against a real process).
# Run:  powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_stop_at_descendant.ps1
# Final line: STOP-AT-DESCENDANT cases=<k>/<n> ok=<True|False>

$ErrorActionPreference = 'Stop'
$tools = Split-Path -Parent $PSScriptRoot
. (Join-Path $tools 'seat-boundary.ps1')

$script:n = 0
$script:k = 0
function Check {
    param([string]$Name, [bool]$Ok)
    $script:n++
    if ($Ok) { $script:k++ }
    $tag = if ($Ok) { 'PASS' } else { 'FAIL' }
    Write-Output ("{0}  {1}" -f $tag, $Name)
}
function New-FakeProc {
    param([int]$Id, [int]$Parent, [string]$Name, [string]$Cl)
    [PSCustomObject]@{ ProcessId = $Id; ParentProcessId = $Parent; Name = $Name; CommandLine = $Cl }
}
function Get-PidList {
    param([object[]]$Objs)
    return @($Objs | ForEach-Object { [int]$_.ProcessId } | Sort-Object)
}

# ---- fake command lines -------------------------------------------------------
$sA      = '1.0.0_SA_CTO~DELL2'
$sB      = '2.0.0_SA_COO~D2'
$sC      = '2.0.0_SA_COO~C'
$clA     = 'claude.exe --dangerously-skip-permissions -- 1.0.0_SA_CTO~DELL2 begin the round'
$clB     = 'claude.exe --dangerously-skip-permissions -- 2.0.0_SA_COO~D2 begin the round'
$clC     = 'claude.exe --dangerously-skip-permissions -- 2.0.0_SA_COO~C begin the round'
$clHelp  = 'claude.exe --native-helper --no-serial'
$clCxB   = 'codex.exe --dangerously-bypass-approvals-and-sandbox -- 2.0.0_SA_COO~D2 begin the round'
$clShell = 'powershell.exe -NoProfile -NoExit -Command "ajb -Headless" # OPAL_SPAWN_MARKER_v1'
$clLane  = 'claude.exe -- 1.0.0_SA_CTO~DELL2 begin'
$clBase  = 'claude.exe -- 1.0.0_SA_CTO begin'

# ---- (a) shell -> seat A -> seat B: the plan for target A ----------------------
$tA = @(
    (New-FakeProc 100 1   'powershell.exe' $clShell),
    (New-FakeProc 101 100 'claude.exe'     $clA),
    (New-FakeProc 103 101 'bash.exe'       'bash inbox-watch.sh 1.0.0_SA_CTO~DELL2'),
    (New-FakeProc 102 101 'claude.exe'     $clB),
    (New-FakeProc 104 102 'node.exe'       'node.exe mcp-server.js')
)
$pA = Get-SeatSubtreePids -RootPid 101 -TargetSerial $sA -Processes $tA
$skipA = @($pA.Skip)
$seatRootsA = @($skipA | Where-Object { $_.IsSeat })
Check ("(a) Kill = {A, A's non-seat child} (got " + (@(Get-PidList -Objs @($pA.Kill | ForEach-Object { [pscustomobject]@{ProcessId=$_} })) -join ',') + ')') ((@($pA.Kill | Sort-Object) -join ',') -eq '101,103')
Check '(a) Skip names the foreign seat B as a seat root with its serial (count 1, pid 102)' ($seatRootsA.Count -eq 1 -and $seatRootsA[0].ProcessId -eq 102 -and $seatRootsA[0].Serial -eq $sB)
Check "(a) Skip includes B's subtree (node.exe pid 104)" (@($skipA | ForEach-Object { [int]$_.ProcessId }) -contains 104)
Check '(a) neither B (102) nor its subtree (104) is in Kill' ((-not (@($pA.Kill) -contains 102)) -and (-not (@($pA.Kill) -contains 104)))
Check '(a) Unclassified is empty' (@($pA.Unclassified).Count -eq 0)
Check '(a) the target pid is the last Kill entry (children before parents)' ($pA.Kill[-1] -eq 101)

# ---- (b) a tree with only the target's own children: same as the old behaviour ---
$tB = @(
    (New-FakeProc 200 1   'claude.exe'     $clA),
    (New-FakeProc 201 200 'bash.exe'       'bash inbox-watch.sh 1.0.0_SA_CTO~DELL2'),
    (New-FakeProc 202 201 'node.exe'       'node.exe mcp-server.js')
)
$pB = Get-SeatSubtreePids -RootPid 200 -TargetSerial $sA -Processes $tB
Check ("(b) Kill = the target and every descendant (got " + ((@($pB.Kill | Sort-Object)) -join ',') + ')') ((@($pB.Kill | Sort-Object) -join ',') -eq '200,201,202')
Check '(b) Skip is empty' (@($pB.Skip).Count -eq 0)
Check '(b) Unclassified is empty and the old whole-tree judge also finds no foreign seat (count 0)' ((@($pB.Unclassified).Count -eq 0) -and (@(Test-SeatBoundary -RootPid 200 -TargetSerial $sA -Processes $tB).Count -eq 0))

# ---- (b2) a target with no children: Kill is the target alone -------------------
$tB2 = @((New-FakeProc 210 1 'claude.exe' $clA))
$pB2 = Get-SeatSubtreePids -RootPid 210 -TargetSerial $sA -Processes $tB2
Check '(b2) a lone target: Kill = {target}, Skip and Unclassified empty' ((@($pB2.Kill) -join ',') -eq '210' -and @($pB2.Skip).Count -eq 0 -and @($pB2.Unclassified).Count -eq 0)

# ---- (c) a foreign seat whose command line cannot be read: the floor -------------
$tC = @(
    (New-FakeProc 300 1   'claude.exe' $clA),
    (New-FakeProc 301 300 'claude.exe' $null),
    (New-FakeProc 302 301 'node.exe'   'node.exe mcp-server.js')
)
$pC = Get-SeatSubtreePids -RootPid 300 -TargetSerial $sA -Processes $tC
$uC = @($pC.Unclassified)
Check '(c) Unclassified is non-empty and names the unreadable seat pid 301' ($uC.Count -eq 1 -and $uC[0].ProcessId -eq 301)
Check '(c) the unreadable seat (301) and its subtree (302) are not in Kill' ((-not (@($pC.Kill) -contains 301)) -and (-not (@($pC.Kill) -contains 302)))
$tC2 = @(
    (New-FakeProc 310 1   'claude.exe' $clA),
    (New-FakeProc 311 310 'codex.exe'  '')
)
$pC2 = Get-SeatSubtreePids -RootPid 310 -TargetSerial $sA -Processes $tC2
Check '(c) an empty command line is unreadable too (Unclassified count 1, pid 311)' (@($pC2.Unclassified).Count -eq 1 -and @($pC2.Unclassified)[0].ProcessId -eq 311)

# ---- (c3) kill-agent takes the refusal path when Unclassified is non-empty (AST, not run) ----
function Get-ParsedAst {
    param([string]$Path)
    $tokens = $null; $errs = $null
    $ast = [System.Management.Automation.Language.Parser]::ParseFile($Path, [ref]$tokens, [ref]$errs)
    [PSCustomObject]@{ Ast = $ast; Errors = @($errs).Count }
}
$kaPath = Join-Path $tools 'kill-agent.ps1'
$kaParsed = Get-ParsedAst -Path $kaPath
$kaAst = $kaParsed.Ast
$floorIfs = @($kaAst.FindAll({ param($node) $node -is [System.Management.Automation.Language.IfStatementAst] -and
    $node.Clauses[0].Item1.Extent.Text -match 'Unclassified' -and
    $node.Clauses[0].Item2.Extent.Text -match 'Write-SeatRefusal' -and
    $node.Clauses[0].Item2.Extent.Text -match 'Stopped\s*=\s*\$false' }, $true))
Check '(c3) kill-agent.ps1 has the floor branch: if Unclassified then Write-SeatRefusal and not stopped (count 1)' ($kaParsed.Errors -eq 0 -and $floorIfs.Count -eq 1)

# ---- (d) a codex.exe foreign seat is skipped like a claude.exe one ----------------
$tD = @(
    (New-FakeProc 400 1   'claude.exe' $clA),
    (New-FakeProc 401 400 'codex.exe'  $clCxB),
    (New-FakeProc 402 401 'node.exe'   'node.exe mcp-server.js')
)
$pD = Get-SeatSubtreePids -RootPid 400 -TargetSerial $sA -Processes $tD
$rootsD = @($pD.Skip | Where-Object { $_.IsSeat })
Check '(d) a codex.exe seat B is a skipped seat root: pid 401, name codex.exe, serial 2.0.0_SA_COO~D2' ($rootsD.Count -eq 1 -and $rootsD[0].ProcessId -eq 401 -and $rootsD[0].Name -eq 'codex.exe' -and $rootsD[0].Serial -eq $sB)
Check "(d) the codex seat's subtree (402) is left running and Kill = {400}" ((@($pD.Kill) -join ',') -eq '400' -and (@($pD.Skip | ForEach-Object { [int]$_.ProcessId }) -contains 402))
Check '(d) the boundary judge agrees: Test-SeatBoundary names the codex seat (count 1)' (@(Test-SeatBoundary -RootPid 400 -TargetSerial $sA -Processes $tD).Count -eq 1)

# ---- (e) the skipped line and the log line name each skipped seat ----------------
$linesA = @(Format-SkipLines -Skip $skipA)
Check ("(e) SKIPPED line names seat B: '" + ($linesA -join '|') + "'") ($linesA.Count -eq 1 -and $linesA[0] -eq 'SKIPPED foreign seat pid=102 serial=2.0.0_SA_COO~D2')
$suffixA = Format-SkipLogSuffix -Skip $skipA
Check ("(e) KILL log suffix names seat B: '" + $suffixA + "'") ($suffixA -eq '  skipped=2.0.0_SA_COO~D2@102')
Check "(e) KILL log suffix reads skipped=none with no skipped seat" ((Format-SkipLogSuffix -Skip @()) -eq '  skipped=none')
$kaCalls = @($kaAst.FindAll({ param($node) $node -is [System.Management.Automation.Language.CommandAst] }, $true) | ForEach-Object { $_.GetCommandName() })
Check '(e) kill-agent.ps1 prints the SKIPPED lines and writes the KILL suffix through the same helpers' (($kaCalls -contains 'Format-SkipLines') -and ($kaCalls -contains 'Format-SkipLogSuffix'))
Check '(e) kill-agent.ps1 plans the tree with Get-SeatSubtreePids' ($kaCalls -contains 'Get-SeatSubtreePids')

# ---- (f) a seat selected by the same run is not skipped (fabric-wide sweep) -------
$tF = @(
    (New-FakeProc 500 1   'claude.exe' $clA),
    (New-FakeProc 501 500 'claude.exe' $clB)
)
$pF = Get-SeatSubtreePids -RootPid 500 -TargetSerial $sA -Selected @(501) -Processes $tF
Check '(f) a selected seat under the target is in Kill, not Skip (Kill has 501; Skip empty)' ((@($pF.Kill) -contains 501) -and @($pF.Skip).Count -eq 0)

# ---- (g) a foreign seat nested under a skipped seat is named too -----------------
$tG = @(
    (New-FakeProc 600 1   'claude.exe' $clA),
    (New-FakeProc 601 600 'claude.exe' $clB),
    (New-FakeProc 602 601 'claude.exe' $clC)
)
$pG = Get-SeatSubtreePids -RootPid 600 -TargetSerial $sA -Processes $tG
$linesG = @(Format-SkipLines -Skip $pG.Skip)
Check ("(g) both nested seats are named (lines=" + $linesG.Count + ')') ($linesG.Count -eq 2 -and ($linesG -contains 'SKIPPED foreign seat pid=601 serial=2.0.0_SA_COO~D2') -and ($linesG -contains 'SKIPPED foreign seat pid=602 serial=2.0.0_SA_COO~C'))

# ---- (h) a serial-less claude.exe is a native helper: killable, not Unclassified --
$tH = @(
    (New-FakeProc 700 1   'claude.exe' $clA),
    (New-FakeProc 701 700 'claude.exe' $clHelp)
)
$pH = Get-SeatSubtreePids -RootPid 700 -TargetSerial $sA -Processes $tH
Check '(h) a serial-less claude.exe is killed with the target (Kill has 701; Unclassified and Skip empty)' ((@($pH.Kill) -contains 701) -and @($pH.Unclassified).Count -eq 0 -and @($pH.Skip).Count -eq 0)

# ---- (i) -Family: a ~lane child of the target base is killable; a bare child is not ---
$tI = @(
    (New-FakeProc 800 1   'claude.exe' $clBase),
    (New-FakeProc 801 800 'claude.exe' $clLane)
)
$pIf = Get-SeatSubtreePids -RootPid 800 -TargetSerial '1.0.0_SA_CTO' -Family -Processes $tI
$pIn = Get-SeatSubtreePids -RootPid 800 -TargetSerial '1.0.0_SA_CTO' -Processes $tI
Check '(i) -Family admits the ~lane child (Kill has 801; Skip empty)' ((@($pIf.Kill) -contains 801) -and @($pIf.Skip).Count -eq 0)
Check '(i) without -Family the ~lane child is a skipped foreign seat (Skip has seat root 801)' (@($pIn.Skip | Where-Object { $_.IsSeat -and $_.ProcessId -eq 801 }).Count -eq 1)

# ---- denominator ------------------------------------------------------------------
$ok = ($script:k -eq $script:n)
Write-Output ("STOP-AT-DESCENDANT cases={0}/{1} ok={2}" -f $script:k, $script:n, $ok)
if ($ok) { exit 0 } else { exit 1 }
