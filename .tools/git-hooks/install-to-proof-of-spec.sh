#!/usr/bin/env bash
# install-to-proof-of-spec.sh -- Idempotent: appends the TO proof-of-spec issuance
# lint stage to .git/hooks/pre-commit (precomp_v1 orchestrator pattern).
# Marker-guarded: re-running is a no-op. FAIL-CLOSED sentinel: a NEW task_orders
# file staged while the check script is missing = DENY (the gate-whose-binary-
# cannot-be-found-must-not-silently-skip law).
set -eu

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK="$REPO_ROOT/.git/hooks/pre-commit"
MARKER="to-proof-of-spec-check.sh"

if [ ! -f "$HOOK" ]; then
    echo "ERROR: $HOOK missing -- run install-owned-paths.sh first (the orchestrator)." >&2
    exit 1
fi
if grep -q "$MARKER" "$HOOK"; then
    echo "OK: TO proof-of-spec stage already wired (idempotent no-op)."
    exit 0
fi

cat >> "$HOOK" <<'EOF_STAGE'

# ---------- 8. TO proof-of-spec issuance lint (Andrew-direct 2026-08-11 canonization + GO) ----------
# A NEW task-order file must carry <proof_of_spec>. FAIL-CLOSED on the sentinel:
# a new task_orders file staged while the check script is missing = DENY.
# Wired by .tools/git-hooks/install-to-proof-of-spec.sh.
if [ -f "$ROOT/.tools/git-hooks/to-proof-of-spec-check.sh" ]; then
    ROOT="$ROOT" STAGED="$STAGED" bash "$ROOT/.tools/git-hooks/to-proof-of-spec-check.sh" "$@" || exit 1
elif git diff --cached --name-only --diff-filter=A 2>/dev/null | grep -qE '(^|/)task[_-]orders/[^/]+\.(md|xml)$'; then
    echo "BLOCKED: a NEW task_orders file is staged but .tools/git-hooks/to-proof-of-spec-check.sh is missing." >&2
    exit 1
fi
EOF_STAGE

echo "OK: TO proof-of-spec issuance lint wired as stage 8 of $HOOK"
