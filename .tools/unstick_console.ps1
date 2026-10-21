# unstick_console.ps1 -- read or key a seat's console BY PROCESS, not by tab title.
#
# Why (CTO ruling 8873 item 2, 2026-10-21): unstick.ps1 finds a tab only when its title is the exact
# serial. Seats spawned with `spawn-agent.ps1 -Tab <PROJECT>` are titled by project, so the title
# lookup exits 2 for them and a deaf seat could only be respawned (its unwritten memory lost). Every
# spawned seat is hosted by a powershell.exe whose command line ENDS with
# `# OPAL_SPAWN_MARKER_v1: <serial>`. This helper attaches to THAT process's console (AttachConsole),
# so the target is identified by the serial in the command line and the keys go to that console
# alone: no window focus, no tab cycling, no way to key a sibling tab that shares a title.
#
# It runs as its OWN process (unstick.ps1 starts it hidden), because FreeConsole/AttachConsole
# replaces the caller's console. It prints nothing to a console; it writes its result to -OutFile.
#
#   -Mode peek : write the visible screen text of the target console to -OutFile. Sends nothing.
#   -Mode keys : type -Text into the target console; with -Enter, press Enter as a SEPARATE act after
#                a pause (an Enter inside the typing burst is a paste-newline and never submits).
# Exit codes: 0 done | 5 could not attach | 6 could not open the console handle | 7 read/write failed

param(
    [Parameter(Mandatory = $true)][int]$TargetPid,
    [Parameter(Mandatory = $true)][ValidateSet('peek', 'keys')][string]$Mode,
    [string]$Text = '',
    [string]$TextFile = '',      # the body from a file: spaces and quotes survive (Start-Process does not quote)
    [switch]$Enter,
    [Parameter(Mandatory = $true)][string]$OutFile
)

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
using System.Text;
public static class UCon {
  [DllImport("kernel32.dll", SetLastError=true)] public static extern bool FreeConsole();
  [DllImport("kernel32.dll", SetLastError=true)] public static extern bool AttachConsole(uint pid);
  [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Unicode)]
  public static extern IntPtr CreateFileW(string name, uint access, uint share, IntPtr sec, uint disp, uint flags, IntPtr tmpl);
  [DllImport("kernel32.dll", SetLastError=true)] public static extern bool CloseHandle(IntPtr h);
  [StructLayout(LayoutKind.Sequential)] public struct COORD { public short X; public short Y; }
  [StructLayout(LayoutKind.Sequential)] public struct SMALL_RECT { public short Left; public short Top; public short Right; public short Bottom; }
  [StructLayout(LayoutKind.Sequential)] public struct CSBI { public COORD dwSize; public COORD dwCursorPosition; public ushort wAttributes; public SMALL_RECT srWindow; public COORD dwMaximumWindowSize; }
  [DllImport("kernel32.dll", SetLastError=true)] public static extern bool GetConsoleScreenBufferInfo(IntPtr h, out CSBI info);
  [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Unicode)]
  public static extern bool ReadConsoleOutputCharacterW(IntPtr h, StringBuilder sb, uint len, COORD origin, out uint read);
  [StructLayout(LayoutKind.Explicit, CharSet=CharSet.Unicode)]
  public struct INPUT_RECORD {
    [FieldOffset(0)] public ushort EventType;
    [FieldOffset(4)] public int bKeyDown;
    [FieldOffset(8)] public ushort wRepeatCount;
    [FieldOffset(10)] public ushort wVirtualKeyCode;
    [FieldOffset(12)] public ushort wVirtualScanCode;
    [FieldOffset(14)] public char UnicodeChar;
    [FieldOffset(16)] public uint dwControlKeyState;
  }
  [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Unicode)]
  public static extern bool WriteConsoleInputW(IntPtr h, INPUT_RECORD[] buf, uint len, out uint written);
}
"@

if ($TextFile) { $Text = [IO.File]::ReadAllText($TextFile) }

[UCon]::FreeConsole() | Out-Null
if (-not [UCon]::AttachConsole([uint32]$TargetPid)) {
    Set-Content -Path $OutFile -Value ("ATTACH-FAILED pid=$TargetPid win32=" + [Runtime.InteropServices.Marshal]::GetLastWin32Error()) -Encoding ASCII
    exit 5
}

$GENERIC_RW = [uint32]3221225472      # GENERIC_READ | GENERIC_WRITE
$SHARE_RW = [uint32]3
$OPEN_EXISTING = [uint32]3

if ($Mode -eq 'peek') {
    $h = [UCon]::CreateFileW('CONOUT$', $GENERIC_RW, $SHARE_RW, [IntPtr]::Zero, $OPEN_EXISTING, 0, [IntPtr]::Zero)
    if ($h -eq [IntPtr]::new(-1)) { Set-Content -Path $OutFile -Value 'OPEN-CONOUT-FAILED' -Encoding ASCII; exit 6 }
    $info = New-Object UCon+CSBI
    if (-not [UCon]::GetConsoleScreenBufferInfo($h, [ref]$info)) { Set-Content -Path $OutFile -Value 'CSBI-FAILED' -Encoding ASCII; exit 7 }
    $w = $info.srWindow.Right - $info.srWindow.Left + 1
    $lines = New-Object System.Collections.Generic.List[string]
    for ($row = $info.srWindow.Top; $row -le $info.srWindow.Bottom; $row++) {
        $sb = New-Object System.Text.StringBuilder ($w + 2)
        $org = New-Object UCon+COORD; $org.X = $info.srWindow.Left; $org.Y = [int16]$row
        $n = [uint32]0
        if ([UCon]::ReadConsoleOutputCharacterW($h, $sb, [uint32]$w, $org, [ref]$n)) { $lines.Add($sb.ToString().Replace([string][char]0, " ").TrimEnd()) } else { $lines.Add('') }
    }
    [UCon]::CloseHandle($h) | Out-Null
    # ASCII-safe record: drop anything above 0x7E so the file never carries a stray code page byte.
    $clean = ($lines | ForEach-Object { (($_ -replace '[^\x20-\x7E]+\s*$', '') -replace '[^\x20-\x7E]', '?').TrimEnd() }) -join "`n"
    Set-Content -Path $OutFile -Value $clean -Encoding ASCII
    exit 0
}

# keys mode
$h = [UCon]::CreateFileW('CONIN$', $GENERIC_RW, $SHARE_RW, [IntPtr]::Zero, $OPEN_EXISTING, 0, [IntPtr]::Zero)
if ($h -eq [IntPtr]::new(-1)) { Set-Content -Path $OutFile -Value 'OPEN-CONIN-FAILED' -Encoding ASCII; exit 6 }

function New-KeyRecord([char]$c, [int]$down, [uint16]$vk) {
    $r = New-Object UCon+INPUT_RECORD
    $r.EventType = 1; $r.bKeyDown = $down; $r.wRepeatCount = 1
    $r.wVirtualKeyCode = $vk; $r.wVirtualScanCode = 0; $r.UnicodeChar = $c; $r.dwControlKeyState = 0
    return $r
}

function Write-Records($recs) {
    $arr = [UCon+INPUT_RECORD[]]$recs
    $wr = [uint32]0
    return [UCon]::WriteConsoleInputW($h, $arr, [uint32]$arr.Length, [ref]$wr)
}

$ok = $true
if ($Text.Length -gt 0) {
    $recs = New-Object System.Collections.Generic.List[object]
    foreach ($ch in $Text.ToCharArray()) {
        $recs.Add((New-KeyRecord $ch 1 0)); $recs.Add((New-KeyRecord $ch 0 0))
    }
    $ok = Write-Records $recs.ToArray()
}
if ($ok -and $Enter) {
    Start-Sleep -Milliseconds 900                       # separate act: never inside the typing burst
    $ok = Write-Records @((New-KeyRecord ([char]13) 1 13), (New-KeyRecord ([char]13) 0 13))
}
[UCon]::CloseHandle($h) | Out-Null
if ($ok) { Set-Content -Path $OutFile -Value ("KEYS-SENT chars=" + $Text.Length + " enter=" + [int]$Enter.IsPresent) -Encoding ASCII; exit 0 }
Set-Content -Path $OutFile -Value ("WRITE-FAILED win32=" + [Runtime.InteropServices.Marshal]::GetLastWin32Error()) -Encoding ASCII
exit 7
