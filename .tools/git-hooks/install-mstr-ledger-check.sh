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

if [ -f "$HOOK_DEST" ] && grep -q "claude_skills_carve_out_v1" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: pre-commit already wired with Path B .claude/skills/** carve-out at $HOOK_DEST (idempotent no-op)"
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
# Path B narrow carve-out (claude_skills_carve_out_v1): COMP-serial authors may
# commit to non-COMP branches IFF ALL staged paths match .claude/skills/** (workspace-
# shared skill-discovery substrate authored by CL CVO per LD-0066). Substantive
# CL-fabric content (cases_queue, session logs, responses) remains branch-isolated.
# Ratified: MSTR LD-PENDING 2026-05-26T~04:02Z + Andrew direct 2026-05-26T~04:23Z
# "do it now". Retires the Co-Authored-By bridge pattern for .claude/skills/** path-class.
branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "")
author=$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')
comp_re='(^|[^0-9])(1\.1\.0_SA_CTO|2\.1\.0_SA_COO|3\.1\.0_SA_CVO|2\.1\.0_SC_CompLearns|1\.[1-4]\.0_DS_CompLearns)([^0-9]|$)'
if [[ "$author" =~ $comp_re ]]; then
    if [[ "$branch" != "COMP" ]]; then
        # Carve-out check: are ALL staged paths under .claude/skills/?
        staged_paths=$(git diff --cached --name-only --diff-filter=ACMR 2>/dev/null)
        carve_out_ok=1
        if [ -z "$staged_paths" ]; then
            carve_out_ok=0
        else
            while IFS= read -r p; do
                case "$p" in
                    .claude/skills/*) ;;
                    *) carve_out_ok=0; break ;;
                esac
            done <<< "$staged_paths"
        fi
        if [[ "$carve_out_ok" != "1" ]]; then
            echo "BLOCKED: COMP-serial author '$author' must commit to COMP branch (currently on '$branch')." >&2
            echo "Switch: git checkout COMP    (or use the feature_clb worktree which is pinned to COMP)" >&2
            echo "(Path B carve-out: .claude/skills/** workspace-shared substrate is permitted on CLOUD; substantive CL-fabric content stays on COMP)" >&2
            exit 1
        fi
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
