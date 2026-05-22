#!/usr/bin/env bash
# install-mstr-ledger-check.sh -- wire the Tier-0 ledger hook into pre-commit.
#
# Idempotent. Produces the canonical 3-stage pre-commit:
#   1. COMP branch isolation
#   2. owned-paths-check
#   3. mstr-ledger-check  (Tier-0 Decision Ledger enforcement, Constitution Art. V)
#
# ACTIVATION TIMING: run this in Phase 3, when 0.0.0_AB_MSTR is stood up. The
# hook is inert before then -- Check 1 needs LD/CY/RT files to exist, Check 2
# needs an MSTR committer -- so early wiring is harmless, but Phase 3 alongside
# the rest of the tier-0 wiring is the natural point.
#
# Safe to re-run: idempotent (no-op if mstr-ledger-check is already wired).

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK_DEST="$REPO_ROOT/.git/hooks/pre-commit"
MSTR_HOOK="$REPO_ROOT/.tools/git-hooks/mstr-ledger-check.sh"

if [ ! -f "$MSTR_HOOK" ]; then
    echo "ERROR: $MSTR_HOOK not found -- mstr-ledger-check.sh must ship first." >&2
    exit 1
fi

if [ -f "$HOOK_DEST" ] && grep -q "mstr-ledger-check.sh" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: mstr-ledger-check already wired at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

cat > "$HOOK_DEST" <<'PRECOMMIT'
#!/usr/bin/env bash
# Pre-commit hook: composes three structural checks.
#   1. COMP branch isolation
#   2. owned-paths-check
#   3. mstr-ledger-check (Tier-0 Decision Ledger enforcement, Constitution Art. V)
set -e

# ---------- 1. COMP branch isolation ----------
branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "")
author=$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')
comp_re='(^|[^0-9])(1\.1\.0_SA_CTO|2\.1\.0_SA_COO|3\.1\.0_SA_CVO|2\.1\.0_SC_CompLearns|1\.[1-4]\.0_DS_CompLearns)([^0-9]|$)'
if [[ "$author" =~ $comp_re ]]; then
    if [[ "$branch" != "COMP" ]]; then
        echo "BLOCKED: COMP-serial author '$author' must commit to COMP branch (currently on '$branch')." >&2
        echo "Switch: git checkout COMP    (or use the feature_clb worktree which is pinned to COMP)" >&2
        exit 1
    fi
elif [[ "$branch" == "COMP" ]]; then
    echo "BLOCKED: Non-COMP author '$author' must not commit to COMP branch." >&2
    echo "Switch: git checkout CLOUD" >&2
    exit 1
fi

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

# ---------- 2. owned-paths check ----------
if [ -f "$ROOT/.tools/git-hooks/owned-paths-check.sh" ]; then
    bash "$ROOT/.tools/git-hooks/owned-paths-check.sh" "$@"
fi

# ---------- 3. mstr-ledger check (Tier-0 Decision Ledger enforcement) ----------
if [ -f "$ROOT/.tools/git-hooks/mstr-ledger-check.sh" ]; then
    bash "$ROOT/.tools/git-hooks/mstr-ledger-check.sh" "$@"
fi
PRECOMMIT

chmod +x "$HOOK_DEST" 2>/dev/null || true
echo "OK: pre-commit rewired -- 3 stages (COMP isolation -> owned-paths -> mstr-ledger) at $HOOK_DEST"
