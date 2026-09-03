"""PostToolUse hook: SERIAL-SCOPED orphan-watcher cleanup on register_agent.

Invoked after mcp__opal-agent-comms__register_agent. The Codex seat launcher also
feeds it the same stdin payload immediately before its duplicate-process assertion,
because Codex registration does not pass through Claude's PostToolUse runner. It
reads tool_input.agent_serial and reaps ONLY that EXACT serial's orphan watchers
via `kill-orphans --serial <S> --force` -- tilde-specific, so an agent's
registration never touches another serial's (or another lane's) watcher.

REPLACES the prior fabric-wide `kill-orphans --stale --force` hook, which reaped
live-but-stale-reading watchers across the WHOLE fabric on every registration --
the root cause of the exit-143 LIVE-watcher reaps (MSTR analysis + Andrew-direct
2026-06-15: "it should only kill-orphans associated with the agent serial being
spawned, tilde-specific").

V4 self-kill guard (per-session marker): the scoped cleanup runs ONCE per
(session, serial), keyed on CLAUDE_CODE_SESSION_ID. At the first register the new
Monitor watcher is not yet armed (register precedes /watcher), so the only
same-serial watcher present is a prior-session orphan -- safe to reap. A
subsequent re-register in the SAME session finds the marker and SKIPS, so it can
never reap the agent's own now-live watcher. If CLAUDE_CODE_SESSION_ID is unset,
it degrades to run-every-register (V3 startup-safe + the rare V4 case is lossless).

Silent on success. Fast on the happy path (one marker stat).

>> 2026-07-13 (MSTR) -- THIS HOOK HAD NEVER ONCE REAPED ANYTHING, AND IT
   REPORTED SUCCESS EVERY TIME. It shelled out via a BARE ["bash", ...]; on
   Windows CreateProcess searches System32 before PATH, so that resolved to the
   WSL launcher (no distro installed) and exited rc=1. The hook then piped
   stdout/stderr to DEVNULL, NEVER CHECKED rc (the `except` never fired -- the
   process RAN, it just FAILED), and wrote the "orphan-cleaned" marker anyway,
   which then SUPPRESSED any retry for the rest of the session.
   A control that cannot fail is not a control; this one could only ever pass.
   Cost: MSTR (the fabric's only spawner) died 09:06Z, its orphaned watcher
   survived its own re-registration, and per inbox-watch.sh:120 that orphan
   `mv`d two COO respawn requests into read/ before echoing into a dead pipe --
   so the fabric ran 70 minutes with ZERO builders while every reachability
   probe read REACHABLE. The corpse of the only agent who can respawn a lane
   ate the messages asking it to do so.
   Grounded by exercise, not inference: a live orphan surrogate that
   kill-orphans DOES match survives this hook and dies to a direct invocation.
   Fixed here: absolute bash (never the System32 shim), rc IS checked, failures
   are AUDITED as ORPHAN-CLEANUP-FAILED, and the marker is written ONLY on
   rc==0 so a failed reap RETRIES instead of stamping itself clean. <<
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def _resolve_bash() -> str | None:
    """Absolute path to a REAL bash, never the System32 WSL shim.

    Windows CreateProcess searches System32 BEFORE PATH, so a bare
    subprocess.run(["bash", ...]) from a Windows-spawned python resolves to
    C:\\Windows\\System32\\bash.exe -- the WSL launcher. On a host with no WSL
    distro that exits rc=1 with
        WSL ERROR: CreateProcessCommon:800: execvpe(/bin/bash) failed
    and NOT with an exception. shutil.which("bash") does NOT reveal this: it
    walks PATH only, so it happily reports Git bash while subprocess executes
    the WSL shim. That divergence is why this went unnoticed -- the obvious
    diagnostic exonerates the culprit.
    """
    for cand in (
        os.environ.get("OPAL_BASH", ""),
        r"C:\Program Files\Git\bin\bash.exe",
        r"C:\Program Files (x86)\Git\bin\bash.exe",
    ):
        if cand and Path(cand).exists():
            return cand
    found = shutil.which("bash")
    if found and "system32" not in found.lower():  # never the WSL shim
        return found
    return None


def _log_failure(workspace: Path, serial: str, why: str) -> None:
    """A reap that failed must SAY SO. Silence is what made this hook a lie."""
    try:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        line = f"{ts}  ORPHAN-CLEANUP-FAILED  serial={serial}  {why}\n"
        with (workspace / "org" / "mcp" / "agent-spawn-audit.log").open(
            "a", encoding="utf-8"
        ) as fh:
            fh.write(line)
    except Exception:
        pass


def _log_codex_reap(workspace: Path, serial: str, pid: int, endpoint: str) -> None:
    try:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        by = os.environ.get("OPAL_AGENT_SERIAL", "unknown")
        line = (
            f"{ts}  KILL-CODEX-RUNTIME  by {by}  serial={serial}  "
            f"pid={pid}  endpoint={endpoint or '?'}\n"
        )
        with (workspace / "org" / "mcp" / "agent-spawn-audit.log").open(
            "a", encoding="utf-8"
        ) as fh:
            fh.write(line)
    except Exception:
        pass


def _codex_runtime_dir(workspace: Path, serial: str) -> Path:
    safe_serial = "".join(
        ch if ch.isalnum() or ch in "_.~-" else "_" for ch in serial
    )
    return workspace / ".runtime" / "codex-seats" / safe_serial


def _read_codex_endpoint(workspace: Path, serial: str) -> str:
    state_path = _codex_runtime_dir(workspace, serial) / "bridge-state.json"
    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        return ""
    endpoint = data.get("endpoint")
    return endpoint if isinstance(endpoint, str) else ""


def _reap_codex_runtime(workspace: Path, serial: str) -> int:
    """Reap Windows-native Codex launcher leftovers for this exact serial.

    .tools/kill-orphans is intentionally Bash/MSYS-shaped and does not see the
    native Python/Codex app-server tree that ajb2 launches on Windows. The
    duplicate-process assertion uses Win32_Process, so this cleanup uses the
    same process surface and the same exact serial boundary.
    """
    if os.name != "nt":
        return 0

    powershell = shutil.which("powershell.exe") or shutil.which("powershell")
    if powershell is None:
        _log_failure(workspace, serial, "no powershell found for Codex runtime reap")
        return 1

    endpoint = _read_codex_endpoint(workspace, serial)
    command = r"""
$payload = [Console]::In.ReadToEnd() | ConvertFrom-Json
$serial = [string]$payload.serial
$workspace = [string]$payload.workspace
$endpoint = [string]$payload.endpoint
$serialPattern = '(?<![\w~])' + [regex]::Escape($serial) + '(?![~\w])'
$scriptNames = @(
  'codex-inbox-turn-bridge.py',
  'codex-inbox-monitor.py',
  'codex-agent-heartbeat.py'
)
$all = @(Get-CimInstance Win32_Process)
$ids = New-Object 'System.Collections.Generic.HashSet[int]'
foreach ($proc in $all) {
  $cmd = [string]$proc.CommandLine
  if ([string]::IsNullOrWhiteSpace($cmd)) { continue }
  $isHelper = $false
  foreach ($name in $scriptNames) {
    if ($cmd.Contains($name)) { $isHelper = $true; break }
  }
  if ($isHelper -and $cmd.Contains($workspace) -and ($cmd -match $serialPattern)) {
    [void]$ids.Add([int]$proc.ProcessId)
  }
  if (-not [string]::IsNullOrWhiteSpace($endpoint) -and
      $cmd.Contains($endpoint) -and $cmd.Contains('app-server')) {
    [void]$ids.Add([int]$proc.ProcessId)
  }
}
if (-not [string]::IsNullOrWhiteSpace($endpoint) -and
    $endpoint -match ':(\d+)$') {
  $port = [int]$Matches[1]
  foreach ($conn in @(Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue)) {
    if ($conn.OwningProcess) { [void]$ids.Add([int]$conn.OwningProcess) }
  }
}

$changed = $true
while ($changed) {
  $changed = $false
  foreach ($proc in $all) {
    if ($ids.Contains([int]$proc.ParentProcessId) -and
        -not $ids.Contains([int]$proc.ProcessId)) {
      [void]$ids.Add([int]$proc.ProcessId)
      $changed = $true
    }
  }
}

$killed = @()
$failed = @()
foreach ($pidToKill in @($ids | Sort-Object -Descending)) {
  if ($pidToKill -eq $PID) { continue }
  $target = Get-Process -Id $pidToKill -ErrorAction SilentlyContinue
  if (-not $target) { continue }
  try {
    Stop-Process -Id $pidToKill -Force -ErrorAction Stop
    $killed += $pidToKill
  }
  catch {
    if ($_.Exception.Message -like 'Cannot find a process with the process identifier*') {
      continue
    }
    $failed += [pscustomobject]@{
      pid = $pidToKill
      error = $_.Exception.Message
    }
  }
}
[pscustomobject]@{ killed = $killed; failed = $failed } | ConvertTo-Json -Compress
"""
    payload = json.dumps(
        {
            "serial": serial,
            "workspace": str(workspace),
            "endpoint": endpoint,
        }
    )
    try:
        proc = subprocess.run(
            [
                powershell,
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                command,
            ],
            input=payload,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except Exception as exc:
        _log_failure(workspace, serial, f"Codex runtime reap {type(exc).__name__}: {exc}")
        return 1

    detail = (proc.stdout or proc.stderr or "").strip()
    if proc.returncode != 0:
        _log_failure(
            workspace,
            serial,
            f"Codex runtime reap rc={proc.returncode} out={detail[:300]}",
        )
        return 1
    if detail:
        try:
            data = json.loads(detail)
        except Exception:
            data = {}
        killed = data.get("killed") or []
        if isinstance(killed, int):
            killed = [killed]
        for pid in killed:
            if isinstance(pid, int):
                _log_codex_reap(workspace, serial, pid, endpoint)
        failed = data.get("failed") or []
        if failed:
            _log_failure(
                workspace,
                serial,
                f"Codex runtime reap partial failure out={detail[:300]}",
            )
            return 1
    return 0


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = payload.get("tool_input") or {}
    serial = tool_input.get("agent_serial")
    if not isinstance(serial, str) or not serial.strip():
        return 0
    serial = serial.strip()

    # org/mcp/<this>.py -> workspace
    workspace = Path(__file__).resolve().parent.parent.parent
    kill_orphans = workspace / ".tools" / "kill-orphans"
    if not kill_orphans.exists():
        return 0

    bash = _resolve_bash()
    if bash is None:
        _log_failure(workspace, serial, "no usable bash found (System32 WSL shim is NOT usable)")
        return 0

    # V4 per-session marker: scoped cleanup runs once per (session, serial).
    marker = None
    session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
    if session_id:
        marker_dir = workspace / "org" / "mcp" / "sessions"
        try:
            marker_dir.mkdir(parents=True, exist_ok=True)
        except Exception:
            return 0
        safe_serial = serial.replace("/", "_").replace("\\", "_")
        # =====================================================================
        # *** MARKER VERSION -- RV-0049 F-003b (CVO). THE FIX WAS INERT ON THE
        #     RUNNER, SUPPRESSED BY THE RESIDUE OF THE BUG IT FIXES. ***
        #
        # The PRE-FIX hook wrote this marker UNCONDITIONALLY -- including after
        # a reap that had FAILED (rc was never checked). So every session that
        # ever registered carries a marker asserting "orphans already cleaned"
        # when nothing was ever cleaned. 368 of them existed; EVERY live session
        # had one, all stamped BEFORE the fix landed.
        #
        # The FIXED hook then read that lie, took the `already cleaned` branch,
        # and RETURNED WITHOUT REAPING -- so the correct code never executed.
        # It landed, it was sound, it was EXERCISED GREEN in isolation, and it
        # was INERT ON THE RUNNER. (CTO's own criterion, ruled this morning off
        # CVO's finding: *** LANDED IS NOT REACHABLE-FROM-THE-RUNNER. ***)
        #
        # >> A FIX GATED ON A MARKER THAT THE BUG ITSELF WROTE IS INERT UNTIL
        #    THE MARKER IS INVALIDATED. VERSION THE MARKER WHEN YOU FIX THE
        #    WRITER -- do NOT mass-delete the old ones (a destructive sweep to
        #    repair a safety hook is how you get a second incident). <<
        # Bumping the suffix retires all 368 stale markers at zero risk: the new
        # hook simply cannot see them, and the old hook no longer exists.
        # =====================================================================
        marker = marker_dir / f"{session_id}.{safe_serial}.orphan-cleaned-v2"
        if marker.exists():
            return 0  # already cleaned this session BY THE FIXED HOOK -> never reap the live watcher

    # Scoped, tilde-specific reap of THIS serial's orphan watchers only.
    #
    # rc IS CHECKED and the marker is written ONLY on rc==0. A reap that failed
    # must retry on the next register -- never stamp "cleaned" over a failure.
    #
    # TIMEOUT: kill-orphans MEASURES ~25s on this host (ps -ef + per-line awk on
    # MSYS is slow). The prior 12s bound was BELOW the tool's own runtime, so
    # even a correctly-resolved bash would have timed out and reaped nothing --
    # the second, independent defect. Fixing only the bash resolution leaves the
    # hook broken. Budget generously; the marker keeps it to once per session.
    #
    # NEVER stdout=PIPE: on TimeoutExpired, communicate() blocks waiting for EOF
    # on a pipe that kill-orphans' surviving grandchildren still hold -> the hook
    # HANGS FOREVER, and it runs on EVERY register_agent, so that would freeze
    # every agent's registration fabric-wide. Route output to a file instead.
    out_path = workspace / "org" / "mcp" / "sessions" / f".orphan-reap.{os.getpid()}.out"
    try:
        with out_path.open("wb") as out_fh:
            proc = subprocess.run(
                [bash, str(kill_orphans), "--serial", serial, "--force"],
                stdin=subprocess.DEVNULL,
                stdout=out_fh,
                stderr=subprocess.STDOUT,
                timeout=90,
            )
        rc = proc.returncode
        detail = out_path.read_text(encoding="utf-8", errors="replace").strip()
    except Exception as exc:  # exec failure, timeout
        _log_failure(workspace, serial, f"{type(exc).__name__}: {exc} bash={bash}")
        return 0
    finally:
        try:
            out_path.unlink()
        except Exception:
            pass

    if rc != 0:
        # bash= and out_bytes= added 2026-07-14 (MSTR): the one failure row on record
        # read `rc=1 out=` -- an empty capture that could not say whether kill-orphans
        # died before its first echo or the capture itself failed. kill-orphans now
        # also prints a start-banner as its first fallible-work-free line, so this
        # detail field distinguishes died-at-birth from died-mid-scan.
        _log_failure(workspace, serial,
                     f"rc={rc} bash={bash} out_bytes={len(detail)} "
                     f"out={detail[:300].replace(chr(10), ' | ')}")
        return 0  # NO marker -> the next register retries.

    codex_rc = _reap_codex_runtime(workspace, serial)
    if codex_rc != 0:
        return 0  # NO marker -> the next register retries.

    if marker is not None:
        try:
            marker.write_text("1", encoding="utf-8")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
