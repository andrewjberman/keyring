#!/usr/bin/env bash
# block-bare-inbox-watch.sh — PreToolUse hook
#
# Blocks Bash/PowerShell tool calls that launch inbox-watch.sh with a
# relative path. Auto-respawn propagates $0; relative launches therefore
# create bare-path PPID=1 zombies that survive session death and
# short-circuit future tracked launches via the single-watcher guard
# (Claude Code surfaces the guard-exit-0 as a misleading exit 143).
#
# Allowed forms:
#   - inbox-watch <serial>                              (PATH wrapper, preferred)
#   - bash /absolute/path/to/inbox-watch.sh <serial>    (absolute fallback)
#
# Blocked form:
#   - bash org/mcp/inbox-watch.sh <serial>              (relative path)
#
# Hook input: tool-call JSON on stdin.
# Block mechanism: emit JSON to stdout with permissionDecision="deny" and exit 0.
# Bare exit-2 + stderr is treated as a hook error (not a block) on current Claude Code.
# Full mechanism: org/mcp/INBOX_WATCH_DESIGN.md § "Failure mode: 143 / zombie short-circuit"

set -uo pipefail

INPUT=$(cat 2>/dev/null || true)
[ -z "$INPUT" ] && exit 0

# Locate jq deterministically. Claude Code's hook shell does NOT load .bashrc,
# so workspace .tools/ is not in PATH. Resolve relative to this script's location
# (always .tools/hooks/), then fall back to PATH for Linux/Mac dev.
SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)" || SCRIPT_DIR="."
if [ -x "$SCRIPT_DIR/../jq.exe" ]; then
    JQ="$SCRIPT_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then
    JQ="jq"
else
    # jq unavailable — fail-safe pass-through (hook can only be advisory here)
    exit 0
fi

# Extract the command field. Failure to parse = pass-through.
CMD=$(printf '%s' "$INPUT" | "$JQ" -r '.tool_input.command // empty' 2>/dev/null) || exit 0
[ -z "$CMD" ] && exit 0

# Match: 'bash' or 'sh' (as a word boundary), whitespace, then 'org/mcp/inbox-watch.sh'.
# The leading boundary check ensures we don't match against '/.../bash' (absolute path
# to bash binary). The path must not start with '/' (absolute) or '.tools/' (wrapper).
if printf '%s' "$CMD" | grep -qE '(^|[[:space:];|&(])([a-z0-9_./-]*/)?(bash|sh)[[:space:]]+org/mcp/inbox-watch\.sh'; then
    REASON='BLOCKED: relative-path inbox-watch.sh invocation. Use the canonical PATH wrapper "inbox-watch <serial>" or absolute path "bash /c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh <serial>". Relative-path launches propagate bare-path $0 into auto-respawn children, creating PPID=1 zombies that survive session death and short-circuit future tracked launches via the single-watcher guard (Claude Code surfaces guard-exit-0 as misleading exit 143). See org/XXX.md Step 1b / org/mcp/INBOX_WATCH_DESIGN.md.'
    "$JQ" -nc --arg r "$REASON" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
    exit 0
fi

exit 0
