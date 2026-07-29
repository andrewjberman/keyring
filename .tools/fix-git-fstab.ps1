# fix-git-fstab.ps1 -- write Git for Windows' /etc/fstab durably. RUN AS ADMINISTRATOR.
#
# WHAT THIS FIXES (LD-0340): the harness's exit-code capture is corrupted when the `/c`
# mount is absent. `mount -f C: /c` repairs it LIVE, but MSYS keeps the mount table in
# shared memory with no backing file, so the repair DIES AT REBOOT. An /etc/fstab entry
# is the only durable form -- and /etc/fstab lives under C:\Program Files, so writing it
# needs an elevated shell. That is the whole reason this is an operator action.
#
# THE TRAP THIS SCRIPT EXISTS TO AVOID -- `/c` IS NOT `/cygdrive/c`:
#   C: on /cygdrive/c   <- compiled-in default, ALREADY correct, needs no fstab line
#   C: on /c            <- the mount the rc fix depends on; THIS is what must persist
# An fstab that remaps /cygdrive/c looks plausible, changes nothing that was broken, and
# leaves /c to disappear on the next boot. Verify the MOUNT POINT, not just the drive.
#
# ENCODING IS LOAD-BEARING: MSYS will not parse an fstab with a UTF-8 BOM -- it silently
# ignores the first line. PowerShell 5.1's `Set-Content -Encoding utf8` WRITES A BOM, so
# this uses [IO.File]::WriteAllText with explicit ASCII + LF line endings instead. A
# BOM'd fstab fails in the worst way: the file exists, looks right in an editor, and the
# mount is silently missing.
#
# Idempotent. Backs up any existing fstab. Verifies by reading back AND by launching a
# FRESH bash to print the resulting mount table -- a config read is not a behavior check.
#
# USAGE (elevated PowerShell):
#   powershell -ExecutionPolicy Bypass -File .tools\fix-git-fstab.ps1
#   powershell -ExecutionPolicy Bypass -File .tools\fix-git-fstab.ps1 -WhatIf

[CmdletBinding()]
param(
    [switch]$WhatIf,
    # Add noacl to the /c mount (ignore Windows ACLs, everything reads as 0777). Matches
    # the /cygdrive/c default. Off by default so this reproduces the mount flags that were
    # ACTUALLY exercised and proven to fix the rc corruption on 2026-07-28.
    [switch]$NoAcl
)

$ErrorActionPreference = 'Stop'

function Say($m, $c = 'Gray') { Write-Host $m -ForegroundColor $c }

Say ""
Say "fix-git-fstab -- durable Git for Windows mount table" 'Cyan'
Say "=========================================================================" 'Cyan'

# --- 1. Elevation check -------------------------------------------------------
$id = [Security.Principal.WindowsIdentity]::GetCurrent()
$pr = New-Object Security.Principal.WindowsPrincipal($id)
if (-not $pr.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Say "FAIL: not elevated." 'Red'
    Say "      /etc/fstab lives under C:\Program Files -- a non-admin write fails, and on"
    Say "      some systems it fails SILENTLY into a VirtualStore shadow copy that Git"
    Say "      never reads. Re-run from an Administrator PowerShell:" 'Yellow'
    Say ""
    Say "        powershell -ExecutionPolicy Bypass -File `"$PSCommandPath`"" 'White'
    Say ""
    exit 1
}
Say "  [ok] running elevated"

# --- 2. Locate the Git installation -------------------------------------------
$gitRoot = $null
$cmd = Get-Command git.exe -ErrorAction SilentlyContinue
if ($cmd) {
    # <root>\cmd\git.exe or <root>\bin\git.exe -> <root>
    $gitRoot = Split-Path -Parent (Split-Path -Parent $cmd.Source)
}
foreach ($cand in @($gitRoot, 'C:\Program Files\Git', 'C:\Program Files (x86)\Git')) {
    if ($cand -and (Test-Path (Join-Path $cand 'etc'))) { $gitRoot = $cand; break }
}
if (-not $gitRoot -or -not (Test-Path (Join-Path $gitRoot 'etc'))) {
    Say "FAIL: could not locate a Git installation with an etc\ directory." 'Red'
    exit 1
}
$fstab = Join-Path $gitRoot 'etc\fstab'
Say "  [ok] git root: $gitRoot"
Say "       fstab:    $fstab"

# --- 3. Compose the desired content -------------------------------------------
# Format: <device> <mount point> <type> <options> <dump> <pass>
$cOpts = if ($NoAcl) { 'binary,noacl,posix=0,user,noumount,auto' }
         else        { 'binary,posix=0,user,noumount,auto' }

$lines = @(
    '# Git for Windows /etc/fstab -- managed by .tools/fix-git-fstab.ps1',
    '#',
    '# /tmp -> the calling user''s TEMP. Keeps per-user temp isolation and stops MSYS',
    '# from inventing a /tmp inside the Git install directory.',
    'none /tmp usertemp binary,posix=0 0 0',
    '#',
    '# C: at /c -- REQUIRED. Without it the harness''s exit-code capture is corrupted',
    '# (LD-0340). `mount -f C: /c` fixes it live but dies at reboot: MSYS holds the',
    '# mount table in shared memory with no backing file. NOTE: this is /c, NOT',
    '# /cygdrive/c -- /cygdrive/c is a compiled-in default that is already correct and',
    '# remapping it fixes nothing. The two are different mount points.',
    "C: /c ntfs $cOpts 0 0",
    ''
) -join "`n"

Say ""
Say "  content to write:" 'Cyan'
foreach ($l in ($lines -split "`n")) { if ($l) { Say "    $l" } }

# --- 4. Idempotency -----------------------------------------------------------
if (Test-Path $fstab) {
    $existing = [IO.File]::ReadAllText($fstab)
    if ($existing -eq $lines) {
        Say ""
        Say "  RESULT: already correct (byte-identical) -- no change made." 'Green'
        Say "          If /c is still missing, the mount table is stale: see step 6."
        exit 0
    }
    Say ""
    Say "  existing fstab found; current content:" 'Yellow'
    foreach ($l in ($existing -split "`r?`n")) { if ($l) { Say "    | $l" } }
} else {
    Say ""
    Say "  no existing fstab (this is why the mount is not durable)" 'Yellow'
}

if ($WhatIf) {
    Say ""
    Say "  -WhatIf: nothing written." 'Yellow'
    exit 0
}

# --- 5. Back up, then write ASCII + LF, no BOM --------------------------------
if (Test-Path $fstab) {
    $bak = "$fstab.bak-$(Get-Date -Format 'yyyyMMddHHmmss')"
    Copy-Item $fstab $bak -Force
    Say "  [ok] backed up -> $bak"
}

# WriteAllText with ASCIIEncoding: no BOM, and the "`n" above keeps LF endings.
[IO.File]::WriteAllText($fstab, $lines, (New-Object Text.ASCIIEncoding))
Say "  [ok] wrote $fstab"

# --- 6. VERIFY -- read back, and exercise a FRESH bash ------------------------
Say ""
Say "  VERIFY (read-back):" 'Cyan'
$after = [IO.File]::ReadAllBytes($fstab)
if ($after.Length -ge 3 -and $after[0] -eq 0xEF -and $after[1] -eq 0xBB -and $after[2] -eq 0xBF) {
    Say "    FAIL: file has a UTF-8 BOM -- MSYS will ignore the first line." 'Red'
    exit 1
}
Say "    [ok] no BOM"
if ([IO.File]::ReadAllText($fstab) -ne $lines) {
    Say "    FAIL: read-back does not match what was written." 'Red'
    exit 1
}
Say "    [ok] content matches"

$bash = Join-Path $gitRoot 'bin\bash.exe'
if (Test-Path $bash) {
    Say ""
    Say "  VERIFY (behavior -- fresh bash, new mount table):" 'Cyan'
    $mountOut = & $bash -lc 'mount' 2>&1
    foreach ($l in $mountOut) { Say "    $l" }

    # A BARE "/c IS MOUNTED" CHECK CANNOT FAIL HERE, so it is worthless as evidence.
    # LD-0340's live repair (`mount -f C: /c`) may ALREADY have /c mounted from shared
    # memory; an existing mount wins over fstab, so the line appears either way. The
    # check has to key on something only the fstab could have produced: THE FLAGS.
    #   fstab-applied -> binary,posix=0,user,noumount,auto
    #   volatile      -> binary,user      (what `mount -f` with no options gives)
    $cLine = ($mountOut | Where-Object { $_ -match ' on /c ' }) -join ''
    Say ""
    if (-not $cLine) {
        Say "    /c: ABSENT from this table. fstab is written but not yet applied." 'Yellow'
    } elseif ($cLine -match 'noumount' -and $cLine -match 'posix=0') {
        Say "    /c: FSTAB IS LIVE (flags carry posix=0 + noumount) -- durably fixed." 'Green'
    } else {
        Say "    /c: MOUNTED, BUT NOT FROM THIS FSTAB." 'Yellow'
        Say "        Flags are '$($cLine -replace '.*type ntfs ','')' -- that is the VOLATILE" 'Yellow'
        Say "        mount from LD-0340's `mount -f C: /c`, which already held the mount"
        Say "        point, so fstab could not take effect. THE DURABLE FIX IS UNPROVEN"
        Say "        until the MSYS shared-memory mount table clears."
        Say "        Re-test after a reboot:" 'Yellow'
        Say "          & `"$bash`" -lc `"mount | grep ' /c '`"" 'White'
    }
    if ($mountOut -match ' on /tmp ') { Say "    /tmp: present (same caveat -- may predate this fstab)" }
}

Say ""
Say "=========================================================================" 'Cyan'
Say "  fstab WRITTEN and content-verified (no BOM, LF, byte-identical read-back)." 'Green'
Say ""
Say "  WHAT IS NOT YET PROVEN: that MSYS APPLIES it. An already-mounted /c wins over" 'Yellow'
Say "  fstab, and MSYS holds the mount table in shared memory that outlives individual"
Say "  processes -- so a fresh bash can inherit the stale table. Read the /c verdict"
Say "  above: only 'FSTAB IS LIVE' is evidence. Anything else means WRITTEN-BUT-UNTESTED."
Say ""
Say "  TO CLOSE IT: reboot (always clears the cache), then run" 'Yellow'
Say "    & `"C:\Program Files\Git\bin\bash.exe`" -lc `"mount | grep ' /c '`"" 'White'
Say "  Expect flags binary,posix=0,user,noumount,auto. If you instead see binary,user"
Say "  or nothing, the fstab is NOT being read and LD-0340 is still open."
Say ""
