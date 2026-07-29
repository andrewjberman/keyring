#!/usr/bin/env bash
# Wire the local missions-refresh post-commit hook (idempotent). Body:
# .tools/git-hooks/missions-refresh-post-commit.sh. Appends to an existing post-commit
# hook rather than clobbering it. Re-run safe. See that body file for the design.
#
# WHY THIS FILE EXISTS AT ALL (LD-0343, 2026-07-29): the missions-refresh hook was
# chained into .git/hooks/post-commit BY HAND on 2026-07-28. Git tracks nothing under
# .git/, so a hand-chained hook exists on exactly one machine and CAN NEVER EXIST on a
# second clone. The mission register (org/missions/) would then silently stop updating
# at site Z with no error and no signal -- the register would simply be wrong there.
#
# The general form of that lesson: A HOOK BODY WITHOUT AN INSTALLER IS A HOOK THAT
# EXISTS ON ONE MACHINE. .tools/install-all-git-hooks.sh now enforces the pairing and
# reports any body that has no installer, so this class cannot recur silently.
#
# PATH PORTABILITY (mirrors install-stitch-refresh.sh, NFRA_TOOLUNIFY REC-1 s10): do NOT
# bake an install-time `pwd`-derived absolute path into the generated hook line -- `pwd`
# returns a path in whatever style the INSTALLING shell uses (MSYS `/c/...` under Git
# Bash, `/cygdrive/c/...` under Cygwin), and the hook is a plain `sh` script that may
# later be EXECUTED under a different shell flavor than the one that installed it.
# Resolve the workspace root at RUN time via `git rev-parse --show-toplevel` -- git
# always returns a path its own invocation understands, portable by construction.
set -e
WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOK="$WS/.git/hooks/post-commit"
MARK="missions-refresh"
BODY="$WS/.tools/git-hooks/missions-refresh-post-commit.sh"

# Fail loudly if the body is missing -- installing a hook line that points at nothing
# would produce a post-commit that silently does nothing on every commit forever.
if [ ! -f "$BODY" ]; then
  echo "FAIL: missions-refresh body not found at $BODY -- refusing to wire a dead hook line." >&2
  exit 1
fi

if [ -f "$HOOK" ] && grep -q "$MARK" "$HOOK" 2>/dev/null; then
  echo "OK: missions-refresh post-commit already wired (idempotent no-op)."
  exit 0
fi

if [ ! -f "$HOOK" ]; then
  printf '#!/bin/sh\n' > "$HOOK"
fi

# Insert BEFORE any trailing `exit 0` -- a prior installer may have left one, and a hook
# line appended after it never runs. This is the silent-no-op failure mode the whole file
# exists to prevent, so it is checked rather than assumed.
if grep -q '^exit 0[[:space:]]*$' "$HOOK" 2>/dev/null; then
  TMP="$HOOK.tmp.$$"
  # Drop the trailing exit 0, append our line, then restore exit 0.
  sed '/^exit 0[[:space:]]*$/d' "$HOOK" > "$TMP"
  printf '\n# %s (installed %s, LD-0341/LD-0343): keeps org/missions/ current. Backgrounded,\n# never stages, never blocks, never runs the FULL rebuild path. See the script header for why.\n_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/missions-refresh-post-commit.sh"\nexit 0\n' "$MARK" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$TMP"
  mv "$TMP" "$HOOK"
else
  printf '\n# %s (installed %s, LD-0341/LD-0343): keeps org/missions/ current. Backgrounded,\n# never stages, never blocks, never runs the FULL rebuild path. See the script header for why.\n_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/missions-refresh-post-commit.sh"\n' "$MARK" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$HOOK"
fi

chmod +x "$HOOK" 2>/dev/null || true
echo "OK: wired missions-refresh post-commit -> $HOOK"
