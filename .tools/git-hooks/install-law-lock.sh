#!/usr/bin/env bash
# install-law-lock.sh -- idempotently wires law-lock-check.sh into .git/hooks/pre-commit as a
# FAIL-CLOSED stage (a locked path staged while the check script is missing = DENY).
# Run once per device: bash .tools/git-hooks/install-law-lock.sh
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
HOOK="$ROOT/.git/hooks/pre-commit"
[ -f "$ROOT/.tools/git-hooks/law-lock-check.sh" ] || { echo "ERROR: law-lock-check.sh missing" >&2; exit 1; }
[ -f "$HOOK" ] || { echo "ERROR: $HOOK missing -- run install-owned-paths.sh first" >&2; exit 1; }
if grep -q "law-lock-check.sh" "$HOOK"; then
    echo "OK: law-lock already wired (idempotent no-op)"; exit 0
fi
cat >> "$HOOK" <<'STAGE'

# ---------- 11. LAW LOCK (Andrew-direct 2026-09-24): CLAUDE.md and org/XXX.md need his express order ----------
# FAIL-CLOSED: a locked path staged while the check script is missing = DENY.
if [ -f "$ROOT/.tools/git-hooks/law-lock-check.sh" ]; then
    bash "$ROOT/.tools/git-hooks/law-lock-check.sh" "$@" || exit 1
elif printf '%s\n' "$STAGED" | grep -qxE 'CLAUDE\.md|org/XXX\.md'; then
    echo "BLOCKED: a locked law file is staged but .tools/git-hooks/law-lock-check.sh is missing." >&2
    exit 1
fi
STAGE
echo "OK: law-lock stage appended to $HOOK"
