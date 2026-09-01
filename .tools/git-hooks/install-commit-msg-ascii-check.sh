#!/usr/bin/env bash
# =============================================================================
# install-commit-msg-ascii-check.sh -- wire commit-msg-ascii-check.sh as a
# commit-msg hook.
#
# AUTHORITY: Andrew-direct 2026-09-01 "yes enforce it at commit time", after
# "i never want emojis, made it very specific in many docs not to use them".
#
# Idempotent. Safe to re-run every session (org/XXX.md Step 1b-D pattern).
# CHAINS rather than clobbers: a commit-msg hook ALREADY EXISTS on this device
# (mass-deletion-check, CTO 192324Z). Replacing it would silently disable an
# unattributed-mass-deletion guard -- so the pre-existing hook runs FIRST and
# its non-zero exit still aborts the commit.
#
# ORDER MATTERS AND IS DELIBERATE: mass-deletion runs first because it is the
# higher-consequence gate (data loss vs a character). A message rejected for
# non-ASCII should not mask a mass-deletion refusal the author also needs to see.
#
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only.
# =============================================================================
set -e

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$ROOT" ] || { echo "ERROR: not in a git repo." >&2; exit 1; }

HOOK_DIR="$ROOT/.git/hooks"
HOOK="$HOOK_DIR/commit-msg"
CHECK=".tools/git-hooks/commit-msg-ascii-check.sh"
MARKER="commit-msg-ascii-check (Andrew-direct 2026-09-01)"

[ -f "$ROOT/$CHECK" ] || { echo "ERROR: $CHECK not found." >&2; exit 1; }
chmod +x "$ROOT/$CHECK" 2>/dev/null || true

# Refuse to install a gate that cannot prove it works.
if ! bash "$ROOT/$CHECK" --self-test >/dev/null 2>&1; then
  echo "ERROR: $CHECK self-test FAILED. Not installing a gate that cannot refuse." >&2
  bash "$ROOT/$CHECK" --self-test >&2 || true
  exit 1
fi

if [ -f "$HOOK" ] && grep -qF "$MARKER" "$HOOK" 2>/dev/null; then
  echo "OK: commit-msg ASCII gate already wired (idempotent no-op)."
  exit 0
fi

CHAIN=""
if [ -f "$HOOK" ]; then
  cp "$HOOK" "$HOOK.pre-ascii-bak"
  CHAIN="$HOOK_DIR/commit-msg.chained-ascii"
  cp "$HOOK" "$CHAIN"
  chmod +x "$CHAIN" 2>/dev/null || true
  echo "NOTE: existing commit-msg hook preserved -> commit-msg.chained-ascii"
  echo "      (backup: commit-msg.pre-ascii-bak). It runs FIRST and still aborts on failure."
fi

{
  echo '#!/usr/bin/env bash'
  echo "# $MARKER -- non-ASCII in a commit message is REFUSED."
  echo '# Installed by .tools/git-hooks/install-commit-msg-ascii-check.sh (idempotent).'
  echo 'set -e'
  echo 'ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"'
  if [ -n "$CHAIN" ]; then
    echo '# Pre-existing hook (mass-deletion) runs FIRST; its non-zero exit aborts the commit.'
    echo 'if [ -f "$ROOT/.git/hooks/commit-msg.chained-ascii" ]; then'
    echo '  bash "$ROOT/.git/hooks/commit-msg.chained-ascii" "$@" || exit $?'
    echo 'fi'
  fi
  echo 'exec bash "$ROOT/.tools/git-hooks/commit-msg-ascii-check.sh" "$@"'
} > "$HOOK"

chmod +x "$HOOK" 2>/dev/null || true
echo "OK: commit-msg ASCII gate installed at .git/hooks/commit-msg"
echo "    scope:  the COMMIT MESSAGE only -- file contents are NOT inspected."
echo "    bypass: ASCII_OVERRIDE=\"<reason>\" git commit ... (audited; empty value refused)"
bash "$ROOT/$CHECK" --self-test | sed 's/^/    /'
