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
  echo '#'
  echo '# .git/hooks is SHARED by every linked worktree; the check SCRIPT is not. Resolving'
  echo '# it from $ROOT alone broke 55 of 56 live worktrees on 2026-09-26: every worktree'
  echo '# based before the script landed exec.d a file it does not have and refused EVERY'
  echo '# commit. So resolve from the MAIN worktree too, and FAIL OPEN with a printed WARN'
  echo '# when neither has it. A gate that hard-fails on a file only newer bases carry'
  echo '# cannot be installed shared.'
  echo 'set -e'
  echo 'ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"'
  echo 'CDIR="$(git rev-parse --git-common-dir 2>/dev/null || true)"'
  echo 'case "$CDIR" in'
  echo '  /*|?:*|?:\\*) ;;'
  echo '  "") CDIR="$ROOT/.git" ;;'
  echo '  *) CDIR="$ROOT/$CDIR" ;;'
  echo 'esac'
  echo 'MAIN="$(cd "$(dirname "$CDIR")" 2>/dev/null && pwd || true)"'
  if [ -n "$CHAIN" ]; then
    echo "# Pre-existing foreign hook runs FIRST; its refusal stands on its own."
    echo "if [ -x \"$CHAIN\" ]; then \"$CHAIN\" \"\$@\" || exit \$?; fi"
  fi
  echo 'CHECK=""'
  echo 'for c in "$ROOT/.tools/git-hooks/gitlink-publication-check.sh" "$MAIN/.tools/git-hooks/gitlink-publication-check.sh"; do'
  echo '  if [ -n "$c" ] && [ -f "$c" ]; then CHECK="$c"; break; fi'
  echo 'done'
  echo 'if [ -z "$CHECK" ]; then'
  echo '  echo "WARN: gitlink-publication-check.sh not found in this worktree ($ROOT) or the main tree ($MAIN)." >&2'
  echo '  echo "WARN: gitlink publication gate SKIPPED for this commit -- FAIL-OPEN, and this line is the disclosure." >&2'
  echo '  CHECK=""'
  echo 'fi'
  echo '# NEITHER `exec` NOR a bare `exit 0` here. Another installer (owned-paths) INLINES this'
  echo '# hook into a wrapper and APPENDS its own check after it. `exec` replaces the shell and'
  echo '# `exit 0` ends it, and either one silently kills every appended check -- measured'
  echo '# 2026-09-26: the owned-paths LANE check sat dead after the inline, with no error.'
  echo 'if [ -n "$CHECK" ]; then bash "$CHECK" "$@" || exit $?; fi'
} > "$HOOK"
chmod +x "$HOOK"

echo "OK: pre-commit gitlink publication gate wired at $HOOK"
[ -n "$CHAIN" ] && echo "OK: chained the pre-existing hook at $CHAIN (backup at $HOOK.pre-gitlinkpub-bak)"
exit 0
