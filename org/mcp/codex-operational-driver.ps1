[CmdletBinding()]
param(
    [string]$Workspace = '',
    [string]$DriverSerial = '1.0.0_SA_CTO~Y',
    [int]$IntervalSeconds = 300,
    [int]$NudgeAfterMinutes = 5,
    [switch]$Once
)

$ErrorActionPreference = 'Stop'

function Resolve-Workspace {
    param([string]$Candidate)
    if (-not [string]::IsNullOrWhiteSpace($Candidate)) {
        return (Resolve-Path -LiteralPath $Candidate).Path
    }
    $scriptRoot = $PSScriptRoot
    if ([string]::IsNullOrWhiteSpace($scriptRoot)) {
        $scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
    }
    return (Resolve-Path -LiteralPath (Join-Path $scriptRoot '..\..')).Path
}

function Get-InboxPath {
    param(
        [string]$Root,
        [string]$Serial
    )
    $parts = $Serial -split '~', 2
    $base = $parts[0]
    if ($parts.Count -eq 2) {
        return Join-Path $Root ("org\mcp\inbox\$base\~" + $parts[1])
    }
    return Join-Path $Root "org\mcp\inbox\$base"
}

function Write-DriverLog {
    param(
        [string]$Path,
        [string]$Message
    )
    $stamp = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    Add-Content -LiteralPath $Path -Encoding utf8 -Value "[$stamp] $Message"
}

function Read-DriverState {
    param([string]$Path)
    $lastNudge = @{}
    if (Test-Path -LiteralPath $Path) {
        foreach ($line in @(Get-Content -LiteralPath $Path)) {
            if ($line -notmatch '^(?<key>[^|]+)\|(?<epoch>[0-9]+)$') {
                continue
            }
            $lastNudge[$Matches['key']] = [int64]$Matches['epoch']
        }
    }
    return @{
        last_nudge = $lastNudge
    }
}

function Write-DriverState {
    param(
        [string]$Path,
        [hashtable]$State
    )
    $last = @{}
    $lastNudge = $State['last_nudge']
    if ($null -eq $lastNudge) {
        $lastNudge = @{}
    }
    $lines = @()
    foreach ($key in @($lastNudge.Keys | Sort-Object)) {
        $lines += "$key|$($lastNudge[$key])"
    }
    Set-Content -LiteralPath $Path -Encoding ascii -Value $lines
}

function Get-SeatStatus {
    param(
        [string]$Root,
        [string]$Serial
    )
    $statusScript = Join-Path $Root 'org\mcp\codex-seat-status.ps1'
    $output = @(& $statusScript -Serial $Serial 2>&1)
    $exit = $LASTEXITCODE
    $first = ($output | Select-Object -First 1)
    $state = if ($first -match ': GREEN') { 'GREEN' } elseif ($first -match ': RED') { 'RED' } else { 'UNKNOWN' }
    return [pscustomobject]@{
        Serial = $Serial
        State = $state
        Exit = $exit
        FirstLine = [string]$first
    }
}

function Get-InboxUnreadState {
    param(
        [string]$Root,
        [string]$Serial
    )
    $inbox = Get-InboxPath -Root $Root -Serial $Serial
    if (-not (Test-Path -LiteralPath $inbox)) {
        return [pscustomobject]@{
            Serial = $Serial
            Count = -1
            OldestAgeSeconds = -1
            Names = @()
        }
    }
    $files = @(Get-ChildItem -LiteralPath $inbox -File -Filter '*.md' | Sort-Object LastWriteTimeUtc)
    $oldestAge = -1
    if ($files.Count -gt 0) {
        $oldestAge = [int]([DateTimeOffset]::UtcNow - $files[0].LastWriteTimeUtc).TotalSeconds
    }
    return [pscustomobject]@{
        Serial = $Serial
        Count = $files.Count
        OldestAgeSeconds = $oldestAge
        Names = @($files | Select-Object -ExpandProperty Name)
    }
}

function Get-GitShortStatus {
    param([string]$Repo)
    if (-not (Test-Path -LiteralPath $Repo)) {
        return [pscustomobject]@{
            Exists = $false
            Head = ''
            Branch = ''
            Dirty = -1
        }
    }
    $status = @(git -C $Repo status --short)
    return [pscustomobject]@{
        Exists = $true
        Head = [string](git -C $Repo rev-parse HEAD)
        Branch = [string](git -C $Repo branch --show-current)
        Dirty = $status.Count
    }
}

function Test-P2To05CroRuling {
    param([string]$DocsRoot)
    $verdictRoot = Join-Path $DocsRoot 'fabric\seats\4.0.0_SA_CRO~Y\verdicts'
    if (-not (Test-Path -LiteralPath $verdictRoot)) {
        return $false
    }
    $hits = @(Get-ChildItem -LiteralPath $verdictRoot -File -Recurse -Filter '*.md' |
        Where-Object { $_.Name -match 'P2[-_]TO[-_]05|P2_TO_05' } |
        Select-Object -First 1)
    return $hits.Count -gt 0
}

function Test-P2To05ObservedFailure {
    param([string]$Root)
    $ctoInbox = Get-InboxPath -Root $Root -Serial '1.0.0_SA_CTO~Y'
    $roots = @($ctoInbox, (Join-Path $ctoInbox 'read'))
    foreach ($candidateRoot in $roots) {
        if (-not (Test-Path -LiteralPath $candidateRoot)) {
            continue
        }
        $hits = @(Get-ChildItem -LiteralPath $candidateRoot -File -Filter '*.md' |
            Where-Object {
                $_.Name -match 'P2-TO-05_FI_handback_dispatch_s' -or
                $_.Name -match 'P2[-_]TO[-_]05.*dispatch.*schema'
            } |
            Select-Object -First 1)
        if ($hits.Count -gt 0) {
            return $true
        }
    }
    return $false
}

function Test-P2To05FailRepairRuling {
    param([string]$Root)
    $ctoInbox = Get-InboxPath -Root $Root -Serial '1.0.0_SA_CTO~Y'
    foreach ($candidateRoot in @($ctoInbox, (Join-Path $ctoInbox 'read'))) {
        if (-not (Test-Path -LiteralPath $candidateRoot)) {
            continue
        }
        $hits = @(Get-ChildItem -LiteralPath $candidateRoot -File -Filter '*.md' |
            Where-Object {
                $_.Name -match 'CRO_RULING_P2-TO-05_FI_handback_FAIL_REP'
            } |
            Select-Object -First 1)
        if ($hits.Count -gt 0) {
            return $true
        }
    }
    return $false
}

function Test-P2To05RepairRoutedToCro {
    param([string]$Root)
    $croInbox = Get-InboxPath -Root $Root -Serial '4.0.0_SA_CRO~Y'
    foreach ($candidateRoot in @($croInbox, (Join-Path $croInbox 'read'))) {
        if (-not (Test-Path -LiteralPath $candidateRoot)) {
            continue
        }
        $hits = @(Get-ChildItem -LiteralPath $candidateRoot -File -Filter '*.md' |
            Where-Object {
                $_.Name -match 'P2-TO-05_FI_dispatch_repair_handback_for' -or
                $_.Name -match 'P2[-_]TO[-_]05.*dispatch_repair.*handback'
            } |
            Select-Object -First 1)
        if ($hits.Count -gt 0) {
            return $true
        }
    }
    return $false
}

function Test-P2To05RepairPassRuling {
    param([string]$Root)
    $ctoInbox = Get-InboxPath -Root $Root -Serial '1.0.0_SA_CTO~Y'
    foreach ($candidateRoot in @($ctoInbox, (Join-Path $ctoInbox 'read'))) {
        if (-not (Test-Path -LiteralPath $candidateRoot)) {
            continue
        }
        $hits = @(Get-ChildItem -LiteralPath $candidateRoot -File -Filter '*.md' |
            Where-Object {
                $_.Name -match 'CRO_RULING_P2-TO-05_FI_dispatch_repair_P'
            } |
            Select-Object -First 1)
        if ($hits.Count -gt 0) {
            return $true
        }
    }
    return $false
}

function Test-P2To05PostLandingRoutedToCro {
    param([string]$Root)
    $croInbox = Get-InboxPath -Root $Root -Serial '4.0.0_SA_CRO~Y'
    foreach ($candidateRoot in @($croInbox, (Join-Path $croInbox 'read'))) {
        if (-not (Test-Path -LiteralPath $candidateRoot)) {
            continue
        }
        $hits = @(Get-ChildItem -LiteralPath $candidateRoot -File -Filter '*.md' |
            Where-Object {
                $_.Name -match 'P2-TO-05_landed_on_main_for_CRO_post-lan'
            } |
            Select-Object -First 1)
        if ($hits.Count -gt 0) {
            return $true
        }
    }
    return $false
}

function Send-DriverMessage {
    param(
        [string]$Root,
        [string]$From,
        [string]$To,
        [string]$Subject,
        [string]$Body,
        [string]$LogPath
    )
    $send = Join-Path $Root 'org\mcp\codex-send.ps1'
    $output = @(& $send -FromSerial $From -To $To -Subject $Subject -Body $Body 2>&1)
    $exit = $LASTEXITCODE
    Write-DriverLog -Path $LogPath -Message "send to=$To exit=$exit subject=$Subject output=$($output -join ' ')"
}

function Invoke-DriverPass {
    param(
        [string]$Root,
        [string]$Driver,
        [int]$NudgeMinutes,
        [string]$LogPath,
        [string]$StatePath
    )

    $state = Read-DriverState -Path $StatePath
    $docsRoot = 'C:\Users\AndrewBerman\Downloads\docs_abcdeg'
    $fiRepo = 'C:\Users\AndrewBerman\Downloads\scratchpad_fi'
    $mainRepo = 'C:\Users\AndrewBerman\Downloads\scratchpad_tmp'
    $note = Join-Path $docsRoot 'fabric\seats\1.5.0_SA_FI~Y\deliverables\P2-TO-05\P2_TO_05_IMPLEMENTATION_HANDBACK_161B9131_20260902.md'
    $deliverablesRoot = Join-Path $docsRoot 'fabric\seats\1.5.0_SA_FI~Y\deliverables\P2-TO-05'

    $ctoInbox = Get-InboxPath -Root $Root -Serial $Driver
    $ctoUnread = @()
    if (Test-Path -LiteralPath $ctoInbox) {
        $ctoUnread = @(Get-ChildItem -LiteralPath $ctoInbox -File -Filter '*.md')
    }

    $seats = @(
        '1.0.0_SA_CTO~Y',
        '4.0.0_SA_CRO~Y',
        '1.3.0_SA_ADP~Y',
        '1.4.0_SA_GATE~Y',
        '1.5.0_SA_FI~Y',
        '1.6.0_SA_TRN~Y'
    )
    $seatStates = @($seats | ForEach-Object { Get-SeatStatus -Root $Root -Serial $_ })
    $seatSummary = ($seatStates | ForEach-Object { "$($_.Serial)=$($_.State)/$($_.Exit)" }) -join ', '
    $seatUnreadStates = @($seats | ForEach-Object { Get-InboxUnreadState -Root $Root -Serial $_ })
    $inboxSummary = ($seatUnreadStates | ForEach-Object { "$($_.Serial)=$($_.Count)/oldest=$($_.OldestAgeSeconds)s" }) -join ', '

    $fiGit = Get-GitShortStatus -Repo $fiRepo
    $mainGit = Get-GitShortStatus -Repo $mainRepo
    $handbackPresent = Test-Path -LiteralPath $note
    $handbackHash = if ($handbackPresent) { (Get-FileHash -Algorithm SHA256 -LiteralPath $note).Hash } else { '' }
    $croRulingPresent = Test-P2To05CroRuling -DocsRoot $docsRoot
    $observedFailure = Test-P2To05ObservedFailure -Root $Root
    $failRepairRuling = Test-P2To05FailRepairRuling -Root $Root
    $repairRoutedToCro = Test-P2To05RepairRoutedToCro -Root $Root
    $repairPassRuling = Test-P2To05RepairPassRuling -Root $Root
    $postLandingRoutedToCro = Test-P2To05PostLandingRoutedToCro -Root $Root
    $failedFiCommit = '161b9131d996e6e77c77ebd440eb46786e45ac3e'
    $p2To05BaseMain = 'e6b7266f702ea35e118cc343c4b8750bacd60c0c'
    $fiRepairMoved = $fiGit.Exists -and $fiGit.Head -ne $failedFiCommit
    $p2To05Landed = $mainGit.Exists -and $mainGit.Head -ne $p2To05BaseMain -and (Test-Path -LiteralPath (Join-Path $mainRepo 'platform\os\runtime\fi_oracle.py'))
    $repairHandbackPresent = $false
    if (Test-Path -LiteralPath $deliverablesRoot) {
        $repairHandbacks = @(Get-ChildItem -LiteralPath $deliverablesRoot -File |
            Where-Object { $_.Name -notmatch '161B9131' })
        $repairHandbackPresent = $repairHandbacks.Count -gt 0
    }

    Write-DriverLog -Path $LogPath -Message "pass cto_unread_md=$($ctoUnread.Count) seats=[$seatSummary] inboxes=[$inboxSummary] main_head=$($mainGit.Head) main_dirty=$($mainGit.Dirty) fi_head=$($fiGit.Head) fi_dirty=$($fiGit.Dirty) p2_to_05_handback=$handbackPresent cro_ruling=$croRulingPresent observed_failure=$observedFailure fail_repair=$failRepairRuling fi_repair_moved=$fiRepairMoved repair_handback=$repairHandbackPresent repair_routed_to_cro=$repairRoutedToCro repair_pass=$repairPassRuling p2_to_05_landed=$p2To05Landed post_landing_routed_to_cro=$postLandingRoutedToCro"
    if ($ctoUnread.Count -gt 0) {
        Write-DriverLog -Path $LogPath -Message "cto_unread_names=$((($ctoUnread | Sort-Object Name | Select-Object -ExpandProperty Name) -join ', '))"
    }

    $nowEpoch = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
    $lastNudgeState = $state['last_nudge']
    if ($null -eq $lastNudgeState) {
        $lastNudgeState = @{}
        $state['last_nudge'] = $lastNudgeState
    }
    if ($repairPassRuling -and $p2To05Landed -and -not $postLandingRoutedToCro) {
        $key = 'P2-TO-05-CTO-POST-LANDING-ROUTE'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $body = @"
DRIVER NUDGE: P2-TO-05 is landed on main and needs CRO post-landing validation routing.

Measured state:
- main HEAD: $($mainGit.Head)
- main dirty count: $($mainGit.Dirty)
- repair PASS ruling seen: $repairPassRuling
- post-landing route to CRO seen: $postLandingRoutedToCro
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 1.0.0_SA_CTO~Y routes landed main evidence to CRO for bounded post-landing validation.
"@
            Send-DriverMessage -Root $Root -From $Driver -To $Driver -Subject 'DRIVER NUDGE P2-TO-05 landed evidence needs CRO route' -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }
    elseif ($repairPassRuling -and $p2To05Landed -and $postLandingRoutedToCro) {
        $key = 'P2-TO-05-CRO-POST-LANDING'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $body = @"
DRIVER NUDGE: P2-TO-05 is landed on main and under CRO post-landing validation.

Measured state:
- main HEAD: $($mainGit.Head)
- main dirty count: $($mainGit.Dirty)
- post-landing route to CRO seen: $postLandingRoutedToCro
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 4.0.0_SA_CRO~Y issues the bounded post-landing validation ruling for P2-TO-05. Downstream issuance remains held until that ruling.
"@
            Send-DriverMessage -Root $Root -From $Driver -To '4.0.0_SA_CRO~Y' -Subject 'DRIVER NUDGE P2-TO-05 post-landing validation pending' -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }
    elseif ($failRepairRuling -and -not $fiRepairMoved) {
        $key = 'P2-TO-05-FI-REPAIR'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $body = @"
DRIVER NUDGE: P2-TO-05 requires next motion.

Current driver read: CRO issued FAIL/REPAIR for the FI handback; FI repair is pending.

Measured state:
- failed FI commit still current: $($fiGit.Head)
- FI repo HEAD: $($fiGit.Head)
- FI branch: $($fiGit.Branch)
- FI dirty count: $($fiGit.Dirty)
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 1.5.0_SA_FI~Y returns repaired P2-TO-05 handback for the dispatch schema failure. CTO holds landing/downstream issuance.
"@
            Send-DriverMessage -Root $Root -From $Driver -To '1.5.0_SA_FI~Y' -Subject 'DRIVER NUDGE P2-TO-05 repair handback pending' -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }
    elseif ($failRepairRuling -and $fiRepairMoved -and -not $repairHandbackPresent) {
        $key = 'P2-TO-05-FI-REPAIR-HANDBACK'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $body = @"
DRIVER NUDGE: P2-TO-05 FI repair commit is present, but repaired handback artifact is not yet present.

Measured state:
- failed FI commit: $failedFiCommit
- current FI HEAD: $($fiGit.Head)
- FI branch: $($fiGit.Branch)
- FI dirty count: $($fiGit.Dirty)
- repaired handback present: $repairHandbackPresent
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 1.5.0_SA_FI~Y emits repaired P2-TO-05 handback note with validation evidence, negative coverage, and non-claims.
"@
            Send-DriverMessage -Root $Root -From $Driver -To '1.5.0_SA_FI~Y' -Subject 'DRIVER NUDGE P2-TO-05 repair commit present, handback missing' -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }
    elseif ($failRepairRuling -and $fiRepairMoved -and $repairHandbackPresent -and -not $repairRoutedToCro) {
        $key = 'P2-TO-05-CTO-REPAIR-VERIFY'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $body = @"
DRIVER NUDGE: P2-TO-05 FI repair appears to have moved and needs CTO verification.

Measured state:
- failed FI commit: $failedFiCommit
- current FI HEAD: $($fiGit.Head)
- FI branch: $($fiGit.Branch)
- FI dirty count: $($fiGit.Dirty)
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 1.0.0_SA_CTO~Y reads the FI repair handback, verifies it, and routes it to CRO if complete.
"@
            Send-DriverMessage -Root $Root -From $Driver -To $Driver -Subject 'DRIVER NUDGE P2-TO-05 FI repair ready for CTO verification' -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }
    elseif ($failRepairRuling -and $fiRepairMoved -and $repairHandbackPresent -and $repairRoutedToCro) {
        $key = 'P2-TO-05-CRO-REPAIR-CERTIFICATION'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $body = @"
DRIVER NUDGE: P2-TO-05 FI dispatch repair is under CRO certification review.

Measured state:
- failed FI commit: $failedFiCommit
- current FI HEAD: $($fiGit.Head)
- FI branch: $($fiGit.Branch)
- FI dirty count: $($fiGit.Dirty)
- repaired handback present: $repairHandbackPresent
- CTO routed repair to CRO: $repairRoutedToCro
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 4.0.0_SA_CRO~Y issues the bounded PASS/FAIL/REPAIR ruling for FI repair commit $($fiGit.Head). CTO holds landing/downstream issuance until that ruling.
"@
            Send-DriverMessage -Root $Root -From $Driver -To '4.0.0_SA_CRO~Y' -Subject 'DRIVER NUDGE P2-TO-05 FI repair certification pending' -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }
    elseif ($handbackPresent -and -not $croRulingPresent) {
        $key = 'P2-TO-05-CRO-HANDBACK-REVIEW'
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $stateLine = if ($observedFailure) {
                'CRO observed a dispatch schema failure; formal PASS/FAIL/REPAIR ruling is still pending.'
            }
            else {
                'FI handback review is still pending CRO PASS/FAIL ruling.'
            }
            $subject = if ($observedFailure) {
                'DRIVER NUDGE P2-TO-05 observed FI schema failure pending CRO ruling'
            }
            else {
                'DRIVER NUDGE P2-TO-05 handback review pending CRO ruling'
            }
            $body = @"
DRIVER NUDGE: P2-TO-05 requires next motion.

Current driver read: $stateLine

Measured state:
- handback note present: $handbackPresent
- handback note SHA256: $handbackHash
- FI repo HEAD: $($fiGit.Head)
- FI branch: $($fiGit.Branch)
- FI dirty count: $($fiGit.Dirty)
- CTO root unread .md count: $($ctoUnread.Count)
- seat readiness summary: $seatSummary

Expected next motion: 4.0.0_SA_CRO~Y issues the bounded P2-TO-05 handback ruling. CTO holds landing/downstream issuance until that ruling.
"@
            Send-DriverMessage -Root $Root -From $Driver -To '4.0.0_SA_CRO~Y' -Subject $subject -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }

    foreach ($seatState in $seatStates) {
        if ($seatState.State -ne 'GREEN') {
            $key = "SEAT-RED-$($seatState.Serial)"
            $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
            if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
                $body = "DRIVER ALERT: codex-seat-status for $($seatState.Serial) is $($seatState.State) exit $($seatState.Exit). First line: $($seatState.FirstLine)"
                Send-DriverMessage -Root $Root -From $Driver -To '4.0.0_SA_CRO~Y' -Subject "DRIVER ALERT seat not GREEN $($seatState.Serial)" -Body $body -LogPath $LogPath
                $lastNudgeState[$key] = $nowEpoch
            }
        }
    }

    foreach ($unreadState in $seatUnreadStates) {
        if ($unreadState.Serial -eq $Driver -or $unreadState.Count -le 0) {
            continue
        }
        if ($unreadState.OldestAgeSeconds -lt ($NudgeMinutes * 60)) {
            continue
        }
        $key = "UNREAD-INBOX-$($unreadState.Serial)"
        $lastEpoch = if ($lastNudgeState.ContainsKey($key)) { [int64]$lastNudgeState[$key] } else { 0 }
        if (($nowEpoch - $lastEpoch) -ge ($NudgeMinutes * 60)) {
            $names = ($unreadState.Names | Select-Object -First 10) -join ', '
            $body = @"
DRIVER NUDGE: root inbox has unread mail older than the driver threshold.

Measured state:
- seat: $($unreadState.Serial)
- unread root .md count: $($unreadState.Count)
- oldest unread age seconds: $($unreadState.OldestAgeSeconds)
- first unread names: $names

Expected next motion: the addressed seat reads exact root-level files, acts on live orders, and moves only handled files to read/.
"@
            Send-DriverMessage -Root $Root -From $Driver -To $unreadState.Serial -Subject "DRIVER NUDGE unread root inbox $($unreadState.Serial)" -Body $body -LogPath $LogPath
            $lastNudgeState[$key] = $nowEpoch
        }
    }

    Write-DriverState -Path $StatePath -State $state
}

$root = Resolve-Workspace -Candidate $Workspace
$runtimeRoot = Join-Path $root ('.runtime\codex-operational-driver\' + ($DriverSerial -replace '[^A-Za-z0-9_.~-]', '_'))
New-Item -ItemType Directory -Force -Path $runtimeRoot | Out-Null
$logPath = Join-Path $runtimeRoot 'driver.log'
$statePath = Join-Path $runtimeRoot 'state.txt'
$pidPath = Join-Path $runtimeRoot 'driver.pid'
Set-Content -LiteralPath $pidPath -Encoding ascii -Value ([string]$PID)
Write-DriverLog -Path $logPath -Message "start pid=$PID interval_seconds=$IntervalSeconds nudge_after_minutes=$NudgeAfterMinutes once=$Once"

do {
    try {
        Invoke-DriverPass -Root $root -Driver $DriverSerial -NudgeMinutes $NudgeAfterMinutes -LogPath $logPath -StatePath $statePath
    }
    catch {
        Write-DriverLog -Path $logPath -Message "ERROR $($_.Exception.Message)"
    }
    if ($Once) {
        break
    }
    Start-Sleep -Seconds $IntervalSeconds
} while ($true)
