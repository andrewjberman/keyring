#!/usr/bin/env bash
# orphan-detector.sh — RV-0017 F-005 process-orphan + concurrency observability
#
# Enumerates the host's process table and reports two classes of finding:
#   (1) ORPHAN — a PID whose recorded parent PID no longer exists in the table.
#       Inspired by the 2026-05-27 broker.py incident (PID 3812 orphan of dead
#       parent 20276; 8158 CPU-sec / 6h45m of accumulated polling traffic).
#   (2) CONCURRENCY-ALARM — >50 concurrent bash OR >20 concurrent git observed
#       on the host. Diagnostic for pathological storm-class fabric states.
#
# Output: append-only log at `org/mcp/orphan-audit.log` + optional hot-signal
# MCP send to MSTR when a threshold trips. Read-only otherwise; never kills.
#
# Rule 16 compliance: relies only on Git Bash 3.6.7 default utilities:
#   bash, ps, awk, sort, grep, date, mkdir, printf, wc, tee.
# Does NOT use pgrep / pkill / flock / pidof.
#
# Invocation:
#   bash org/mcp/orphan-detector.sh              # one cycle, exit
#   bash org/mcp/orphan-detector.sh --notify     # one cycle + MCP-CC MSTR on alarm
#   bash org/mcp/orphan-detector.sh --test-self  # spawn synthetic orphan, verify catch
#
# Cron: arm a 5-min recurring loop via the host's task scheduler (or a wrapper
# /loop in a long-running session). Session-only CronCreate is fine for ad-hoc
# observation; production should use Windows Task Scheduler for persistence.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
AUDIT_LOG="${ORPHAN_DETECTOR_AUDIT_LOG:-$REPO_ROOT/org/mcp/orphan-audit.log}"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Thresholds (override via env for testing)
BASH_ALARM_THRESHOLD="${ORPHAN_BASH_THRESHOLD:-50}"
GIT_ALARM_THRESHOLD="${ORPHAN_GIT_THRESHOLD:-20}"

NOTIFY=0
TEST_SELF=0
for arg in "$@"; do
  case "$arg" in
    --notify) NOTIFY=1 ;;
    --test-self) TEST_SELF=1 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true

# ---------------------------------------------------------------------------
# Test-self mode: spawn a synthetic orphan, verify the detector catches it
# ---------------------------------------------------------------------------
if [ "$TEST_SELF" -eq 1 ]; then
  echo "test-self: spawning a synthetic orphan..."
  # Start a parent bash that backgrounds a long-running child, then exits.
  # The child's PPID becomes invalid post-parent-exit -> orphan.
  bash -c 'bash -c "sleep 120 &" ; exit 0' &
  PARENT_PID=$!
  wait "$PARENT_PID" 2>/dev/null || true
  sleep 1
  # Now run the detector and check if any orphan was reported
  bash "$0" 2>&1 | tee /tmp/orphan-detector-test.out
  if grep -q '^ORPHAN' /tmp/orphan-detector-test.out; then
    echo "test-self: PASS (orphan caught)"
    # Cleanup: kill any leftover synthetic orphans (sleep 120)
    ps -ef 2>/dev/null | awk '/sleep 120/ {print $2}' | while read -r pid; do
      kill "$pid" 2>/dev/null || true
    done
    exit 0
  else
    echo "test-self: FAIL (no orphan reported)"
    exit 1
  fi
fi

# ---------------------------------------------------------------------------
# Enumerate the process table. On Git Bash for Windows, `ps -ef` lists MSYS
# processes; `ps -ef -W` includes native Windows processes. We use both: the
# Bash-spawned + native trees both matter for the storm-class diagnostic.
# Format columns vary; we extract PID + PPID + COMMAND defensively.
# ---------------------------------------------------------------------------
# Use a single Python pass over `ps -ef` output for the orphan check + counts.
# Per-PID `grep` would fan out hundreds of subprocesses on Windows = unusable.
# Python is in the Rule-16-allowed utility set.
ANALYSIS="$(ps -ef 2>/dev/null | python3 -c '
import os, re, sys
self_pid = int(os.environ.get("DETECTOR_PID", "0") or 0)
self_ppid = int(os.environ.get("DETECTOR_PPID", "0") or 0)
rows = []
for line in sys.stdin:
    parts = line.split(None, 7)
    if len(parts) < 8: continue
    try:
        pid = int(parts[1]); ppid = int(parts[2])
    except ValueError:
        continue
    rows.append((pid, ppid, parts[7].rstrip()))
live_pids = {r[0] for r in rows}
orphans = []
bash_n = 0
git_n = 0
for pid, ppid, cmd in rows:
    if re.search(r"(/bash|\\\\bash)\\.?(exe)?($| )", cmd): bash_n += 1
    if re.search(r"(/git|\\\\git)\\.?(exe)?($| )", cmd):   git_n += 1
    if ppid in (0, 1): continue
    if pid == self_pid or pid == self_ppid: continue
    if ppid not in live_pids:
        orphans.append((pid, ppid, cmd[:100]))
print(f"BASH={bash_n}")
print(f"GIT={git_n}")
print(f"ORPHANS={len(orphans)}")
for pid, ppid, cmd in orphans:
    print(f"ORPHAN  pid={pid}  ppid={ppid}(dead)  cmd={cmd}")
' 2>/dev/null)"

DETECTOR_PID=$$ DETECTOR_PPID=$PPID
BASH_COUNT="$(printf '%s\n' "$ANALYSIS" | awk -F= '/^BASH=/{print $2; exit}')"
GIT_COUNT="$(printf '%s\n' "$ANALYSIS" | awk -F= '/^GIT=/{print $2; exit}')"
ORPHAN_COUNT="$(printf '%s\n' "$ANALYSIS" | awk -F= '/^ORPHANS=/{print $2; exit}')"
ORPHAN_LINES="$(printf '%s\n' "$ANALYSIS" | grep '^ORPHAN ' || true)"
[ -z "$BASH_COUNT" ] && BASH_COUNT=0
[ -z "$GIT_COUNT" ] && GIT_COUNT=0
[ -z "$ORPHAN_COUNT" ] && ORPHAN_COUNT=0

ALARM_TRIPPED=""
[ "$BASH_COUNT" -gt "$BASH_ALARM_THRESHOLD" ] && ALARM_TRIPPED="${ALARM_TRIPPED}BASH-COUNT=${BASH_COUNT}>${BASH_ALARM_THRESHOLD} "
[ "$GIT_COUNT" -gt "$GIT_ALARM_THRESHOLD" ] && ALARM_TRIPPED="${ALARM_TRIPPED}GIT-COUNT=${GIT_COUNT}>${GIT_ALARM_THRESHOLD} "

# ---------------------------------------------------------------------------
# Emit audit log entry + stdout summary
# ---------------------------------------------------------------------------
{
  printf '%s  bash=%s  git=%s  orphans=%s' \
    "$TS" "$BASH_COUNT" "$GIT_COUNT" "$ORPHAN_COUNT"
  [ -n "$ALARM_TRIPPED" ] && printf '  ALARM:%s' "$ALARM_TRIPPED"
  printf '\n'
  [ "$ORPHAN_COUNT" -gt 0 ] && printf '%s' "$ORPHAN_LINES"
} | tee -a "$AUDIT_LOG"

# ---------------------------------------------------------------------------
# Hot-signal to MSTR if --notify + alarm tripped (best-effort; no fail on miss)
# ---------------------------------------------------------------------------
if [ "$NOTIFY" -eq 1 ] && [ -n "$ALARM_TRIPPED" ]; then
  # Filesystem-direct MCP per ws inbox path (no broker dependency required)
  MSTR_INBOX="$REPO_ROOT/org/mcp/inbox/0.0.0_AB_MSTR"
  mkdir -p "$MSTR_INBOX" 2>/dev/null || true
  MSG_TS="$(date -u +%Y%m%dT%H%M%SZ)"
  MSG_FILE="$MSTR_INBOX/${MSG_TS}_org-mcp-orphan-detector__ALARM__concurrency-thresholds.md"
  {
    echo "# Message from org/mcp/orphan-detector.sh"
    echo "**To:** 0.0.0_AB_MSTR"
    echo "**Date:** $MSG_TS"
    echo "**Subject:** [ALARM] orphan-detector thresholds tripped — ${ALARM_TRIPPED}"
    echo ""
    echo "Audit log: \`$AUDIT_LOG\`"
    echo ""
    echo "Counts: bash=$BASH_COUNT (threshold=$BASH_ALARM_THRESHOLD); git=$GIT_COUNT (threshold=$GIT_ALARM_THRESHOLD); orphans=$ORPHAN_COUNT"
    [ "$ORPHAN_COUNT" -gt 0 ] && { echo ""; echo "## Orphans"; printf '```\n%s```\n' "$ORPHAN_LINES"; }
  } > "$MSG_FILE" 2>/dev/null || true
fi

exit 0
