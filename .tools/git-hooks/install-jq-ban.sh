#!/usr/bin/env bash
# install-jq-ban.sh -- Idempotent: appends the jq-invocation ban stage to
# .git/hooks/pre-commit (precomp_v1 orchestrator pattern). Marker-guarded.
# FAIL-CLOSED sentinel: a skills/tools shell file staged while the check script
# is missing = DENY (the gate-whose-binary-cannot-be-found-must-not-silently-skip law).
set -eu

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK="$REPO_ROOT/.git/hooks/pre-commit"
MARKER="jq-ban-check.sh"

if [ ! -f "$HOOK" ]; then
    echo "ERROR: $HOOK missing -- run install-owned-paths.sh first (the orchestrator)." >&2
    exit 1
fi
if grep -q "$MARKER" "$HOOK"; then
    echo "OK: jq-ban stage already wired (idempotent no-op)."
    exit 0
fi

cat >> "$HOOK" <<'EOF_STAGE'

# ---------- 9. jq-invocation ban (Andrew gate GO 2026-08-11 "2a yes") ----------
# jq is NOT installed (Rule 16); an invocation in skills/tools shell contexts is denied.
# FAIL-CLOSED on the sentinel. Wired by .tools/git-hooks/install-jq-ban.sh.
if [ -f "$ROOT/.tools/git-hooks/jq-ban-check.sh" ]; then
    ROOT="$ROOT" STAGED="$STAGED" bash "$ROOT/.tools/git-hooks/jq-ban-check.sh" "$@" || exit 1
elif git diff --cached --name-only --diff-filter=ACM 2>/dev/null | grep -qE '^(\.claude/skills/|\.tools/).*\.(sh|bash|md)$'; then
    echo "BLOCKED: skills/tools shell files staged but .tools/git-hooks/jq-ban-check.sh is missing." >&2
    exit 1
fi
EOF_STAGE

echo "OK: jq-invocation ban wired as stage 9 of $HOOK"
