#!/usr/bin/env bash
# =============================================================================
# install-mass-deletion-check.sh -- wire mass-deletion-check.sh as a commit-msg hook.
#
# Idempotent. Safe to re-run every session (org/XXX.md Step 1b-D pattern).
# CHAINS rather than clobbers: if a commit-msg hook already exists and is not
# ours, we back it up and invoke it first, preserving its exit code.
#
# Why commit-msg and not pre-commit: the gate needs BOTH the commit message
# (to read the Authorized-Deletion trailer) and an index view honoring
# $GIT_INDEX_FILE (so `git commit --only` correctly shows zero foreign
# deletions). Only commit-msg has both. See mass-deletion-check.sh header.
#
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only.
# =============================================================================
set -e

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$ROOT" ] || { echo "ERROR: not in a git repo." >&2; exit 1; }

HOOK_DIR="$ROOT/.git/hooks"
HOOK="$HOOK_DIR/commit-msg"
CHECK=".tools/git-hooks/mass-deletion-check.sh"
MARKER="mass-deletion-check (CTO 192324Z)"

[ -f "$ROOT/$CHECK" ] || { echo "ERROR: $CHECK not found." >&2; exit 1; }
mkdir -p "$HOOK_DIR"
chmod +x "$ROOT/$CHECK" 2>/dev/null || true

if [ -f "$HOOK" ] && grep -qF "$MARKER" "$HOOK" 2>/dev/null; then
  echo "OK: commit-msg mass-deletion gate already wired (idempotent no-op)."
  exit 0
fi

# Chain a pre-existing foreign hook rather than destroying it.
CHAIN=""
if [ -f "$HOOK" ]; then
  cp "$HOOK" "$HOOK.pre-massdel-bak"
  CHAIN="$HOOK_DIR/commit-msg.chained"
  mv "$HOOK" "$CHAIN"
  chmod +x "$CHAIN" 2>/dev/null || true
  echo "NOTE: existing commit-msg hook preserved -> commit-msg.chained (backup: commit-msg.pre-massdel-bak)"
fi

{
  echo '#!/usr/bin/env bash'
  echo "# $MARKER -- unattributed mass deletion of tracked files."
  echo '# Installed by .tools/git-hooks/install-mass-deletion-check.sh (idempotent).'
  echo 'set -e'
  echo 'ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"'
  if [ -n "$CHAIN" ]; then
    echo '# Pre-existing hook runs first; its non-zero exit still aborts the commit.'
    echo 'if [ -x "$ROOT/.git/hooks/commit-msg.chained" ]; then'
    echo '  "$ROOT/.git/hooks/commit-msg.chained" "$@" || exit $?'
    echo 'fi'
  fi
  echo 'exec bash "$ROOT/.tools/git-hooks/mass-deletion-check.sh" "$@"'
} > "$HOOK"

chmod +x "$HOOK"
echo "OK: commit-msg mass-deletion gate installed at .git/hooks/commit-msg"
# Ask the CHECK for its state rather than restating it -- a second copy of the
# ramp date here is exactly how the 2026-07-09 wrong-epoch bug printed "WARN"
# while the gate was actually BLOCKING.
bash "$ROOT/$CHECK" --mode 2>/dev/null | sed 's/^/    /'
echo "    attribute: 'Authorized-Deletion: LD-####' trailer | bypass: FORCE_DELETE=1 (audited)"
