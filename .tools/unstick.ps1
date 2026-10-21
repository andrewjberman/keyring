# unstick.ps1 -- send an approval keystroke to a serial-titled terminal tab.
#
# The /unstick engine (first exercised 2026-08-20, ATOM_LAYER0 Codex lanes; runbook:
# org/ref/RUNBOOK_CODEX_TAB_UNSTICK.md). Mechanism: agent terminals are top-level
# windows of one WindowsTerminal process, and a WINDOW'S TITLE FOLLOWS ITS ACTIVE
# TAB -- so a background tab is located by focusing each candidate window and
# cycling Ctrl+Tab, reading the title after every switch. Keystrokes are sent ONLY
# to a tab whose title EXACTLY matches the target serial (positive identification),
# with the foreground re-verified before every send (abort-on-steal).
#
# Usage:
#   .tools\unstick.ps1 -Serial <full-serial>            # locate + send (default '1'+Enter)
#   .tools\unstick.ps1 -Serial <full-serial> -DryRun    # locate + report only, no keystrokes
#   .tools\unstick.ps1 -Serial <s> -Keys '2{ENTER}'     # a different prompt answer
#   .tools\unstick.ps1 -Serial <s> -Keys '<prompt text>{ENTER}'   # NUDGE an idle-at-input lane:
#                                     # body is typed, PAUSE, then Enter as a separate act (see
#                                     # Send-ToActiveTab -- an Enter inside the burst never submits)
#
# Exit codes: 0 = keys sent (or dry-run located) | 2 = serial's tab NOT FOUND
#             3 = focus lost/steal-aborted        | 4 = bad serial argument
#
# PRECONDITION (load-bearing): the target tab is TITLED with the lane serial at
# creation (WT suppressApplicationTitle pins creation titles). An untitled tab
# cannot be positively identified and this tool will correctly NOT find it.
# SUCCESS ORACLE IS CONSUMER-SIDE: this tool proves keys were DELIVERED to the
# identified tab, never that the lane RESUMED -- resumption is the lane consuming
# its queued inbox / messaging its base. A lane not at a prompt receives the keys
# into its input buffer (submits as chat input) -- for an IDLE-AT-INPUT lane that IS
# the remedy (the nudge: a short prompt naming the work waiting in its inbox); for a
# prompt-stuck lane the answer key is. PEEK FIRST to tell the two apart. And verify
# the submit on a SECOND peek: two identical peeks a minute apart after a send = the
# text is sitting in the composer, not running (no 'Working' line, no transcript
# movement beyond the composer growing) -- a lone '{ENTER}' submits it.

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Serial,
    [string]$Keys = '1{ENTER}',
    [switch]$DryRun,
    # -Peek: locate + focus the tab, capture the WINDOW to a PNG, send NOTHING.
    # The image is the "what is it stuck on" answer -- a multimodal seat reads it.
    [switch]$Peek,
    [string]$OutFile = ''
)

if ($Serial -notmatch '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$') {
    Write-Host "[unstick] '$Serial' does not look like an agent serial" -ForegroundColor Red
    exit 4
}

Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text; using System.Collections.Generic;
public class UnstickWin {
  [DllImport("user32.dll")] static extern bool EnumWindows(EnumWindowsProc cb, IntPtr lp);
  [DllImport("user32.dll")] static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] static extern int GetWindowText(IntPtr h, StringBuilder sb, int max);
  [DllImport("user32.dll")] static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int cmd);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  delegate bool EnumWindowsProc(IntPtr h, IntPtr lp);
  public static string Title(IntPtr h) { var sb = new StringBuilder(512); GetWindowText(h, sb, 512); return sb.ToString(); }
  public static List<long[]> Windows() {                     // [hwnd, pid]
    var o = new List<long[]>();
    EnumWindows((h, lp) => {
      if (!IsWindowVisible(h)) return true;
      var sb = new StringBuilder(512); GetWindowText(h, sb, 512);
      if (sb.Length == 0) return true;
      uint pid; GetWindowThreadProcessId(h, out pid);
      o.Add(new long[] { h.ToInt64(), pid });
      return true;
    }, IntPtr.Zero);
    return o;
  }
}
"@

$wsh = New-Object -ComObject WScript.Shell

function Focus-Verified([IntPtr]$h) {
    [UnstickWin]::ShowWindow($h, 9) | Out-Null          # SW_RESTORE if minimized
    [UnstickWin]::SetForegroundWindow($h) | Out-Null
    Start-Sleep -Milliseconds 400
    return ([UnstickWin]::GetForegroundWindow() -eq $h)
}

function Send-ToActiveTab([IntPtr]$h, [string]$k) {
    if ([UnstickWin]::GetForegroundWindow() -ne $h) { return $false }   # abort-on-steal
    # PASTE-BURST SPLIT (measured 2026-08-20 2202Z on 4.0.0_SA_CRO~A/~B): the Codex TUI treats
    # a fast keystroke stream as a PASTE, and an Enter INSIDE that burst becomes a NEWLINE --
    # a nudge prompt sat UNSUBMITTED in the composer through three peeks while the operator
    # reported it submitted. So a trailing {ENTER} on a body longer than ONE character is sent
    # as a SEPARATE act after a pause, foreground re-verified in between. '1{ENTER}' / 'y{ENTER}'
    # (approval answers) are unaffected: two keys sit under the burst threshold.
    if ($k -match '^(.+)\{ENTER\}$' -and $Matches[1].Length -gt 1) {
        $body = $Matches[1]
        $wsh.SendKeys($body); Start-Sleep -Milliseconds 900
        if ([UnstickWin]::GetForegroundWindow() -ne $h) { return $false }   # re-verify before the submit
        $wsh.SendKeys('{ENTER}'); Start-Sleep -Milliseconds 400
        return $true
    }
    $wsh.SendKeys($k); Start-Sleep -Milliseconds 400
    return $true
}

Add-Type -AssemblyName System.Drawing
function Capture-Window([IntPtr]$h, [string]$path) {
    # Screen-scrape the focused window's rect. Requires the window foreground+visible
    # (the caller just focus-verified it); WT is GPU-rendered, so CopyFromScreen of the
    # live pixels is the reliable capture (PrintWindow can render black for it).
    Start-Sleep -Milliseconds 300                       # let the tab finish painting
    $r = New-Object UnstickWin+RECT
    if (-not [UnstickWin]::GetWindowRect($h, [ref]$r)) { return $null }
    $w = $r.R - $r.L; $ht = $r.B - $r.T
    if ($w -le 0 -or $ht -le 0) { return $null }
    $bmp = New-Object System.Drawing.Bitmap($w, $ht)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.CopyFromScreen($r.L, $r.T, 0, 0, (New-Object System.Drawing.Size($w, $ht)))
    $g.Dispose()
    $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    return $path
}

if ($Peek -and -not $OutFile) {
    $ts = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ')
    $safe = $Serial -replace '[^A-Za-z0-9._~-]', '_'
    $OutFile = Join-Path $env:TEMP "unstick_peek_${safe}_${ts}.png"
}

# CASE 0 -- FIRST, by process (a seat spawned with -Tab <PROJECT> is titled by project, so its tab never matches the serial).
# Find the seat's host process by the serial in its COMMAND LINE (every spawned seat is a powershell.exe whose
# command line ends with `# OPAL_SPAWN_MARKER_v1: <serial>`) and read or key THAT console through
# .tools\unstick_console.ps1. No window is focused and no tab is cycled, so a sibling tab that shares the
# project title cannot be keyed by mistake. (CTO ruling 8873, 2026-10-21.)
$rxSerial = [regex]::Escape($Serial)
$hosts3 = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where-Object {
    $_.ProcessId -ne $PID -and $_.CommandLine -notlike '*Where-Object*' -and
    $_.CommandLine -match "OPAL_SPAWN_MARKER_v1: $rxSerial(?![A-Za-z0-9~])" })
if ($hosts3.Count -eq 1) {
    $hp = [int]$hosts3[0].ProcessId
    $helper = Join-Path $PSScriptRoot 'unstick_console.ps1'
    $liveClaude = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe' and ParentProcessId=$hp").Count
    if ($DryRun -and -not $Peek) { Write-Host "[unstick] DRY-RUN: no tab is titled '$Serial', but its host process is pid $hp (found by the serial in its command line). Would use its console for '$Keys'."; exit 0 }
    $ts3 = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ')
    $res = Join-Path $env:TEMP "unstick_console_${ts3}_$hp.txt"
    if ($Peek) {
        $txt = if ($OutFile -match '\.png$') { $OutFile -replace '\.png$', '.txt' } else { $OutFile }
        $pr = Start-Process powershell -ArgumentList @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $helper, '-TargetPid', $hp, '-Mode', 'peek', '-OutFile', $txt) -WindowStyle Hidden -Wait -PassThru
        if ($pr.ExitCode -eq 0) { Write-Host "[unstick] PEEKED '$Serial' by process (host pid $hp, console text) -> $txt  [no keystrokes sent]" -ForegroundColor Cyan; exit 0 }
        Write-Host "[unstick] console peek failed (helper exit $($pr.ExitCode)): $(Get-Content $txt -ErrorAction SilentlyContinue) -- nothing sent" -ForegroundColor Red; exit 3
    }
    if ($liveClaude -lt 1) { Write-Host "[unstick] host pid $hp for '$Serial' has NO live claude.exe child (the seat is gone, the window left at a shell prompt). Not keying it." -ForegroundColor Yellow; exit 2 }
    # Keys: '<body>{ENTER}', '{ENTER}' or plain characters. Other SendKeys syntax (^ % + {TAB} ...) needs a real window.
    $body = $Keys; $press = $false
    if ($Keys -match '^(.*)\{ENTER\}$') { $body = $Matches[1]; $press = $true }
    if ($body -match '[\^%+~{}()\[\]]') { Write-Host "[unstick] the process path types plain text and Enter only; '$Keys' uses SendKeys syntax it cannot send. Nothing sent." -ForegroundColor Yellow; exit 2 }
    $args3 = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $helper, '-TargetPid', $hp, '-Mode', 'keys', '-Text', $body, '-OutFile', $res)
    if ($press) { $args3 += '-Enter' }
    $pr = Start-Process powershell -ArgumentList $args3 -WindowStyle Hidden -Wait -PassThru
    if ($pr.ExitCode -eq 0) { Write-Host "[unstick] SENT '$Keys' to '$Serial' by process (host pid $hp, its console only)" -ForegroundColor Green; exit 0 }
    Write-Host "[unstick] console send failed (helper exit $($pr.ExitCode)): $(Get-Content $res -ErrorAction SilentlyContinue) -- treat as NOT sent" -ForegroundColor Red; exit 3
}
if ($hosts3.Count -gt 1) { Write-Host "[unstick] '$Serial' matches $($hosts3.Count) host processes (pids $(($hosts3 | ForEach-Object { $_.ProcessId }) -join ',')); refusing to guess. Nothing sent." -ForegroundColor Yellow; exit 2 }

# Candidate windows: any process that hosts terminal tabs.
$termNames = @('WindowsTerminal', 'OpenConsole', 'conhost', 'cmd', 'powershell', 'pwsh')
$wins = [UnstickWin]::Windows() | ForEach-Object {
    $h = [IntPtr]$_[0]; $procId = $_[1]
    $pname = try { (Get-Process -Id $procId -ErrorAction Stop).ProcessName } catch { '' }
    [pscustomobject]@{ Hwnd = $h; ProcId = $procId; PName = $pname; Title = [UnstickWin]::Title($h) }
}

# CASE 1 -- a window's ACTIVE tab already is the target (title == serial).
$direct = @($wins | Where-Object { $_.Title -eq $Serial })
if ($direct.Count -ge 1) {
    $w = $direct[0]
    if ($DryRun -and -not $Peek) { Write-Host "[unstick] DRY-RUN: '$Serial' is the ACTIVE tab of window $($w.Hwnd) ($($w.PName)). Would focus + send '$Keys'."; exit 0 }
    if (-not (Focus-Verified $w.Hwnd)) { Write-Host "[unstick] FOCUS FAILED on window $($w.Hwnd) -- nothing sent" -ForegroundColor Red; exit 3 }
    if ($Peek) {
        $p = Capture-Window $w.Hwnd $OutFile
        if ($p) { Write-Host "[unstick] PEEKED '$Serial' (active tab, window $($w.Hwnd)) -> $p  [no keystrokes sent]" -ForegroundColor Cyan; exit 0 }
        Write-Host "[unstick] capture failed on window $($w.Hwnd) -- nothing saved, nothing sent" -ForegroundColor Red; exit 3
    }
    if (-not (Send-ToActiveTab $w.Hwnd $Keys)) { Write-Host "[unstick] focus stolen pre-send -- nothing sent" -ForegroundColor Red; exit 3 }
    Write-Host "[unstick] SENT '$Keys' to '$Serial' (active tab, window $($w.Hwnd))" -ForegroundColor Green
    exit 0
}

# CASE 2 -- the target is a BACKGROUND tab: cycle each terminal-host window's tabs,
# identifying by title after every switch. Keys go ONLY to an exact-title match.
$hosts = @($wins | Where-Object { $termNames -contains $_.PName })
foreach ($w in $hosts) {
    if (-not (Focus-Verified $w.Hwnd)) { Write-Host "[unstick] skip window $($w.Hwnd) ('$($w.Title)') -- could not focus"; continue }
    $start = [UnstickWin]::Title($w.Hwnd)
    $sent = $false
    for ($i = 0; $i -lt 12; $i++) {
        if ([UnstickWin]::GetForegroundWindow() -ne $w.Hwnd) { Write-Host "[unstick] focus stolen mid-cycle in window $($w.Hwnd) -- aborting this window" -ForegroundColor Yellow; break }
        $wsh.SendKeys('^({TAB})'); Start-Sleep -Milliseconds 600
        $t = [UnstickWin]::Title($w.Hwnd)
        if ($t -eq $Serial -and -not $sent) {
            if ($Peek) {
                $p = Capture-Window $w.Hwnd $OutFile
                if ($p) { Write-Host "[unstick] PEEKED '$Serial' (tab $($i+1) of window $($w.Hwnd)) -> $p  [no keystrokes sent]" -ForegroundColor Cyan; $sent = $true }
                else { Write-Host "[unstick] capture failed -- nothing saved, nothing sent" -ForegroundColor Red; exit 3 }
            }
            elseif ($DryRun) { Write-Host "[unstick] DRY-RUN: located '$Serial' as tab $($i+1) of window $($w.Hwnd) ('$start'). Would send '$Keys'."; $sent = $true }
            elseif (Send-ToActiveTab $w.Hwnd $Keys) { Write-Host "[unstick] SENT '$Keys' to '$Serial' (tab $($i+1) of window $($w.Hwnd))" -ForegroundColor Green; $sent = $true }
            else { Write-Host "[unstick] focus stolen pre-send -- nothing sent" -ForegroundColor Red; exit 3 }
        }
        if ($t -eq $start -and $i -gt 0) { break }          # full circle -- original tab restored
    }
    if ($sent) { exit 0 }
}

Write-Host "[unstick] NOT FOUND: no tab titled '$Serial' in any terminal window, and no host process carries its spawn marker. Nothing sent." -ForegroundColor Yellow
exit 2
