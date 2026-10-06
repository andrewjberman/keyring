#!/usr/bin/env bash
# install-one-writer-check.sh -- Idempotent: appends the one-writer stage (NFRA_CTLPLN FWD-8, C-ONE-WRITER) to the
# repository's pre-commit orchestrator (precomp_v1 pattern). Marker-guarded. Resolves the hooks directory through
# --git-common-dir, so it installs the same hook from the main checkout or any linked worktree.
# FAIL-CLOSED sentinel: an append-only file staged while the check script is missing = DENY.
set -eu

COMMON="$(git rev-parse --path-format=absolute --git-common-dir)"
HOOK="$COMMON/hooks/pre-commit"
MARKER="one-writer-check.py"

if [ ! -f "$HOOK" ]; then
    echo "ERROR: $HOOK missing -- run install-owned-paths.sh first (the orchestrator)." >&2
    exit 1
fi
if grep -q "$MARKER" "$HOOK"; then
    echo "OK: one-writer stage already wired (idempotent no-op)."
    exit 0
fi

cat >> "$HOOK" <<'EOF_STAGE'

# ---------- 12. ONE WRITER PER APPEND FILE (NFRA_CTLPLN FWD-8, C-ONE-WRITER; 1.0.0_SA_CTO 105634) ----------
# A box appends only to its own surprise-channel / audit-log file (<stem>.<device>.<ext>; the laptop keeps the
# unsuffixed one). A staged file whose suffix names ANOTHER box is refused; a merge commit is exempt.
# FAIL-CLOSED on the sentinel. Wired by .tools/git-hooks/install-one-writer-check.sh.
if [ -f "$ROOT/.tools/git-hooks/one-writer-check.py" ]; then
    ROOT="$ROOT" STAGED="$STAGED" python "$ROOT/.tools/git-hooks/one-writer-check.py" || exit 1
elif printf '%s\n' "$STAGED" | grep -qE '(surprise-channel/|surprise_channel/|-audit(\.[^/.]+)?\.(log|jsonl)$)'; then
    echo "BLOCKED: an append-only file is staged but .tools/git-hooks/one-writer-check.py is missing." >&2
    exit 1
fi
EOF_STAGE

echo "OK: one-writer stage wired as stage 12 of $HOOK"
