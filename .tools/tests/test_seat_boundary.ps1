# test_seat_boundary.ps1 -- fake-process battery for .tools/seat-boundary.ps1 and its callers.
#
# Kills nothing and starts nothing: every process list is a FAKE passed with -Processes; the two kill
# tools and spawn-agent.ps1 are only PARSED and inspected through the PowerShell AST.
# Run:  powershell -NoProfile -ExecutionPolicy Bypass -File .tools/tests/test_seat_boundary.ps1
# Final line: SEAT-BOUNDARY-TEST cases=<k>/<n> wired=<both|kill-agent|kill-maint|none> ok=<True|False>

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

# ---- fake command lines -------------------------------------------------------
$sA      = '1.0.0_SA_CTO~DELL2'
$sB      = '2.0.0_SA_COO~D2'
$sCOO    = '2.0.0_SA_COO~ZI'
$sMSTR   = '0.0.0_AB_MSTR'
$clA     = '"C:\Users\x\.local\bin\claude.exe" --dangerously-skip-permissions -- 1.0.0_SA_CTO~DELL2 begin the round'
$clB     = 'claude.exe --dangerously-skip-permissions -- 2.0.0_SA_COO~D2 begin the round'
$clHint  = 'claude.exe --dangerously-skip-permissions -- 0.7.0_AE_CloudOps~IR ready; launched by a hint that names 2.0.0_SA_COO~ZI'
$clOwn   = 'claude.exe --dangerously-skip-permissions -- 2.0.0_SA_COO~ZI begin'
$clLane  = 'claude.exe --dangerously-skip-permissions -- 2.0.0_SA_COO~C begin'
$clBase  = 'claude.exe --dangerously-skip-permissions -- 2.0.0_SA_COO begin'
$clBare  = 'claude.exe --dangerously-skip-permissions -p hello'
$clPunct = 'claude.exe -- 0.9.0_WK_CTLPLN~78. go'
$clShell = 'powershell.exe -NoProfile -NoExit -Command "ajb -Headless" # OPAL_SPAWN_MARKER_v1'

# ---- 1-4: launch serial identity -----------------------------------------------
$ls1 = Get-LaunchSerial -CommandLine $clHint
Check 'launch serial of a seat is its own first serial token, not a serial named in a hint' ($ls1 -eq '0.7.0_AE_CloudOps~IR')
Check 'a hint naming the target in ANOTHER seat command line is not a target' (-not (Test-LaunchSerialMatch -CommandLine $clHint -Serial $sCOO))
Check 'the target own launch serial is a target' (Test-LaunchSerialMatch -CommandLine $clOwn -Serial $sCOO)
Check 'a trailing full stop on the serial token is trimmed' ((Get-LaunchSerial -CommandLine $clPunct) -eq '0.9.0_WK_CTLPLN~78')

# ---- 5-8: no serial, single vs family, no bleed ---------------------------------
Check 'a command line with no serial token has no launch serial' ($null -eq (Get-LaunchSerial -CommandLine $clBare))
Check 'single mode: a base serial does not match its own ~lane' (-not (Test-LaunchSerialMatch -CommandLine $clLane -Serial '2.0.0_SA_COO'))
Check '-Family admits serial~lane (the -All family rule)' (Test-LaunchSerialMatch -CommandLine $clLane -Serial '2.0.0_SA_COO' -Family)
Check '-Family does not bleed into a longer serial (2.0.0_SA_COOX)' (-not (Test-LaunchSerialMatch -CommandLine 'claude.exe -- 2.0.0_SA_COOX~C go' -Serial '2.0.0_SA_COO' -Family))

# ---- 9-10: two-serial tree refuses A's tree and names B -------------------------
$tree2 = @(
    (New-FakeProc 100 1    'powershell.exe' $clShell),
    (New-FakeProc 101 100  'claude.exe'     $clA),
    (New-FakeProc 102 101  'claude.exe'     $clB)
)
$f9  = @(Test-SeatBoundary -RootPid 101 -TargetSerial $sA -Processes $tree2)
Check 'two-serial tree: killing A tree is refused, foreign seat B named (count 1)' ($f9.Count -eq 1 -and $f9[0].Serial -eq $sB -and $f9[0].ProcessId -eq 102)
$f10 = @(Test-SeatBoundary -RootPid 100 -TargetSerial $sA -Processes $tree2)
Check 'two-serial tree: killing the host shell names foreign seat B (count 1)' ($f10.Count -eq 1 -and $f10[0].Serial -eq $sB)

# ---- 11: one-serial tree passes -------------------------------------------------
$tree1 = @(
    (New-FakeProc 200 1    'powershell.exe' $clShell),
    (New-FakeProc 201 200  'claude.exe'     $clA),
    (New-FakeProc 202 201  'bash.exe'       'bash inbox-watch.sh 1.0.0_SA_CTO~DELL2'),
    (New-FakeProc 203 201  'node.exe'       'node.exe mcp-server.js')
)
$f11a = @(Test-SeatBoundary -RootPid 201 -TargetSerial $sA -Processes $tree1)
$f11b = @(Test-SeatBoundary -RootPid 200 -TargetSerial $sA -Processes $tree1)
Check 'one-serial tree: the seat tree passes with no foreign seat (count 0)' ($f11a.Count -eq 0)
Check 'one-serial tree: the host shell passes with no foreign seat (count 0)' ($f11b.Count -eq 0)

# ---- 12-13: -All family admits serial~lane --------------------------------------
$treeFam = @(
    (New-FakeProc 300 1    'powershell.exe' $clShell),
    (New-FakeProc 301 300  'claude.exe'     $clBase),
    (New-FakeProc 302 301  'claude.exe'     $clLane)
)
$f12 = @(Test-SeatBoundary -RootPid 301 -TargetSerial '2.0.0_SA_COO' -Family -Processes $treeFam)
Check '-All family: base seat with its ~lane child passes (count 0)' ($f12.Count -eq 0)
$f13 = @(Test-SeatBoundary -RootPid 301 -TargetSerial '2.0.0_SA_COO' -Processes $treeFam)
Check 'without -Family the ~lane child is foreign (count 1, serial 2.0.0_SA_COO~C)' ($f13.Count -eq 1 -and $f13[0].Serial -eq '2.0.0_SA_COO~C')

# ---- 14-15: Selected pids (fabric-wide sweep) -----------------------------------
$tree14 = @(
    (New-FakeProc 400 1    'powershell.exe' $clShell),
    (New-FakeProc 401 400  'claude.exe'     $clA),
    (New-FakeProc 402 401  'claude.exe'     $clB)
)
$f14 = @(Test-SeatBoundary -RootPid 401 -TargetSerial $sA -Selected @(402) -Processes $tree14)
Check 'selected foreign seat is not foreign under a fabric-wide sweep (count 0)' ($f14.Count -eq 0)
$tree15 = @(
    (New-FakeProc 500 1    'powershell.exe' $clShell),
    (New-FakeProc 501 500  'claude.exe'     $clA),
    (New-FakeProc 502 501  'claude.exe'     $clB),
    (New-FakeProc 503 501  'claude.exe'     ('claude.exe -- ' + $sMSTR + ' begin'))
)
$f15 = @(Test-SeatBoundary -RootPid 501 -TargetSerial $sA -Selected @(502) -Processes $tree15)
Check 'an unselected seat (MSTR) under a fabric-wide sweep is refused (count 1, serial 0.0.0_AB_MSTR)' ($f15.Count -eq 1 -and $f15[0].Serial -eq $sMSTR)

# ---- 16: null target makes every serial-bearing seat foreign --------------------
$tree16 = @(
    (New-FakeProc 600 1    'powershell.exe' $clShell),
    (New-FakeProc 601 600  'claude.exe'     $clB)
)
$f16 = @(Test-SeatBoundary -RootPid 600 -TargetSerial $null -Processes $tree16)
Check 'null target serial: a serial-bearing seat below is foreign (count 1)' ($f16.Count -eq 1)

# ---- 17: a serial-less claude.exe is a native helper, not a seat -----------------
$tree17 = @(
    (New-FakeProc 700 1    'powershell.exe' $clShell),
    (New-FakeProc 701 700  'claude.exe'     $clA),
    (New-FakeProc 702 701  'claude.exe'     $clBare)
)
$f17 = @(Test-SeatBoundary -RootPid 701 -TargetSerial $sA -Processes $tree17)
Check 'a serial-less claude.exe under the target is not a seat (count 0)' ($f17.Count -eq 0)

# ---- 18: a seat two levels down is found ----------------------------------------
$tree18 = @(
    (New-FakeProc 800 1    'claude.exe'     $clA),
    (New-FakeProc 801 800  'powershell.exe' $clShell),
    (New-FakeProc 802 801  'claude.exe'     $clB)
)
$f18 = @(Test-SeatBoundary -RootPid 800 -TargetSerial $sA -Processes $tree18)
Check 'a foreign seat two levels down is found (count 1)' ($f18.Count -eq 1 -and $f18[0].ProcessId -eq 802)

# ---- 19: a cyclic parent map terminates -----------------------------------------
$tree19 = @(
    (New-FakeProc 900 901  'powershell.exe' $clShell),
    (New-FakeProc 901 900  'claude.exe'     $clA)
)
$f19 = @(Test-SeatBoundary -RootPid 901 -TargetSerial $sA -Processes $tree19)
Check 'a cyclic parent map terminates with no foreign seat (count 0)' ($f19.Count -eq 0)

# ---- 20-23: the four files parse with no errors ---------------------------------
function Get-ParseErrorCount {
    param([string]$Path)
    $tokens = $null; $errs = $null
    [void][System.Management.Automation.Language.Parser]::ParseFile($Path, [ref]$tokens, [ref]$errs)
    return @($errs).Count
}
$files = @('seat-boundary.ps1', 'kill-agent.ps1', 'kill-maint.ps1', 'spawn-agent.ps1')
foreach ($fn in $files) {
    $ec = Get-ParseErrorCount -Path (Join-Path $tools $fn)
    Check ("parses with no errors: {0} (errors={1})" -f $fn, $ec) ($ec -eq 0)
}

# ---- 24-25: each kill tool calls Test-SeatBoundary (AST, not text) --------------
function Test-CallsSeatBoundary {
    param([string]$Path)
    $tokens = $null; $errs = $null
    $ast = [System.Management.Automation.Language.Parser]::ParseFile($Path, [ref]$tokens, [ref]$errs)
    $hits = $ast.FindAll({ param($node) $node -is [System.Management.Automation.Language.CommandAst] -and $node.GetCommandName() -eq 'Test-SeatBoundary' }, $true)
    return (@($hits).Count -gt 0)
}
$kaCalls = Test-CallsSeatBoundary -Path (Join-Path $tools 'kill-agent.ps1')
$kmCalls = Test-CallsSeatBoundary -Path (Join-Path $tools 'kill-maint.ps1')
Check 'kill-agent.ps1 calls Test-SeatBoundary' $kaCalls
Check 'kill-maint.ps1 calls Test-SeatBoundary' $kmCalls

# ---- 26: spawn-agent no longer starts a bare powershell as a child of the caller --
$spTokens = $null; $spErrs = $null
$spAst = [System.Management.Automation.Language.Parser]::ParseFile((Join-Path $tools 'spawn-agent.ps1'), [ref]$spTokens, [ref]$spErrs)
$bareLaunch = $spAst.FindAll({ param($node) $node -is [System.Management.Automation.Language.CommandAst] -and $node.GetCommandName() -eq 'Start-Process' -and $node.CommandElements.Count -gt 1 -and $node.CommandElements[1].Value -match '^powershell(\.exe)?$' }, $true)
Check 'spawn-agent.ps1 has no bare Start-Process powershell (the caller-child launch)' (@($bareLaunch).Count -eq 0)

$wired = if ($kaCalls -and $kmCalls) { 'both' } elseif ($kaCalls) { 'kill-agent' } elseif ($kmCalls) { 'kill-maint' } else { 'none' }
$ok = ($script:k -eq $script:n)
Write-Output ("SEAT-BOUNDARY-TEST cases={0}/{1} wired={2} ok={3}" -f $script:k, $script:n, $wired, $ok)
if ($ok) { exit 0 } else { exit 1 }
