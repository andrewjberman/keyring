#!/usr/bin/env bash
# =============================================================================
# install-gitlink-publication-check.sh -- wire gitlink-publication-check.sh as
# a pre-commit hook.
#
# Idempotent. Safe to re-run every session (org/XXX.md Step 1b-D pattern).
# CHAINS rather than clobbers: if a pre-commit hook already exists and is not
# ours, it is backed up and invoked FIRST, and its exit code is preserved.
#
# Why pre-commit and not commit-msg: this gate needs only the staged set, and
# pre-commit is the earliest point at which the author can still fix the
# problem by pushing the submodule branch. It reads `git diff --cached`, which
# honours $GIT_INDEX_FILE, so `git commit --only` is graded correctly.
#
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only (Rule 4).
# =============================================================================
set -e

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$ROOT" ] || { echo "ERROR: not in a git repo." >&2; exit 1; }

HOOK_DIR="$ROOT/.git/hooks"
HOOK="$HOOK_DIR/pre-commit"
CHECK=".tools/git-hooks/gitlink-publication-check.sh"
MARKER="gitlink-publication-check (CVO fd6fe5c6c9)"

[ -f "$ROOT/$CHECK" ] || { echo "ERROR: $CHECK not found." >&2; exit 1; }
mkdir -p "$HOOK_DIR"
chmod +x "$ROOT/$CHECK" 2>/dev/null || true

if [ -f "$HOOK" ] && grep -qF "$MARKER" "$HOOK" 2>/dev/null; then
  echo "OK: pre-commit gitlink publication gate already wired (idempotent no-op)."
  exit 0
fi

CHAIN=""
if [ -f "$HOOK" ]; then
  cp "$HOOK" "$HOOK.pre-gitlinkpub-bak"
  CHAIN="$HOOK_DIR/pre-commit.chained-gitlinkpub"
  mv "$HOOK" "$CHAIN"
  chmod +x "$CHAIN" 2>/dev/null || true
fi

{
  echo '#!/usr/bin/env bash'
  echo "# $MARKER -- installed by install-gitlink-publication-check.sh"
  echo 'set -e'
  echo 'ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"'
  if [ -n "$CHAIN" ]; then
    echo "# Pre-existing foreign hook runs FIRST; its refusal stands on its own."
    echo "if [ -x \"$CHAIN\" ]; then \"$CHAIN\" \"\$@\" || exit \$?; fi"
  fi
  echo 'exec bash "$ROOT/.tools/git-hooks/gitlink-publication-check.sh" "$@"'
} > "$HOOK"
chmod +x "$HOOK"

echo "OK: pre-commit gitlink publication gate wired at $HOOK"
[ -n "$CHAIN" ] && echo "OK: chained the pre-existing hook at $CHAIN (backup at $HOOK.pre-gitlinkpub-bak)"
exit 0
