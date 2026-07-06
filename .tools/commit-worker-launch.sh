#!/usr/bin/env bash
# NFRA_CMTQUE TO-6 -- commit-worker-launch.sh
# Ensure-if-down launcher for the commit-worker daemon (the manual / bash-hook entry point).
#
# The PRIMARY reliability trigger is the Python _ensure_commit_worker() in server.py's
# register_agent path (every agent session ensures the worker up -- mirrors _ensure_broker).
# THIS script is the equivalent for non-Python contexts: a manual `bash commit-worker-launch.sh`,
# a bash hook, or a diagnostic. Both launch the SAME daemon; the worker's own worker.pid
# singleton makes a concurrent double-launch a safe no-op (loser exits).
#
# Detach: nohup + background + disown so the daemon OUTLIVES this launcher AND the calling
# session (the worker is a shared host daemon serving all agents, like the broker). Rule-16:
# nohup is a Git Bash 3.6.7 default; setsid is NOT (so we use nohup+disown, not setsid).
#
# Idempotent: if a live worker already holds worker.pid with a fresh heartbeat, do nothing.

set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=commit_queue_lib.sh
source "$SCRIPT_DIR/commit_queue_lib.sh"

# must be inside a git repo (the queue is per-gitdir)
if ! git rev-parse --absolute-git-dir >/dev/null 2>&1; then
  echo "ERROR: not inside a git repository." >&2
  exit 2
fi
cq_init || { echo "ERROR: cannot init commit-queue." >&2; exit 1; }

if cq_worker_alive; then
  echo "OK: commit-worker already live (pid $(cat "$(cq_worker_pid)" 2>/dev/null)); nothing to do."
  exit 0
fi

LOGF="$(cq_root)/worker.log"
# Detached launch. nohup -> ignore SIGHUP; & -> background; disown -> drop from job table
# so it survives this shell's exit. </dev/null so it never blocks on stdin.
nohup bash "$SCRIPT_DIR/commit-worker.sh" --daemon </dev/null >>"$LOGF" 2>&1 &
_wpid=$!
disown "$_wpid" 2>/dev/null || true
echo "OK: commit-worker launched detached (bg pid $_wpid); log: $LOGF"
exit 0
