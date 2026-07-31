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

if [ -f "$HOOK_DEST" ] && grep -q "precomp_v1" "$HOOK_DEST" 2>/dev/null; then
    echo "OK: pre-commit already wired with precomp_v1 hoisting at $HOOK_DEST (idempotent no-op)"
    exit 0
fi

cat > "$HOOK_DEST" <<'PRECOMMIT'
#!/usr/bin/env bash
# Pre-commit hook: composes three structural checks.
#   1. COMP branch isolation
#   2. owned-paths-check
#   3. mstr-ledger-check (Tier-0 Decision Ledger enforcement, Constitution Art. V)
#
# precomp_v1 (RV0017-F002, 2026-05-27): orchestrator hoists ROOT + STAGED once
# and passes via env to children. Eliminates 2-3x git subprocess fan-out + bash
# subshell spawn cost on no-op stages. Preserves claude_skills_carve_out_v1
# semantics.
set -e

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
STAGED="$(git diff --cached --name-only 2>/dev/null || true)"

# Fast-path: empty staged set is a no-op for ALL three stages.
# COMP block also short-circuits to no-op (its inner check is gated on
# non-empty staged_paths after diff-filter=ACMR; the unfiltered list being
# empty implies the ACMR list is also empty).
if [ -z "$STAGED" ]; then
    exit 0
fi

# ---------- 1. COMP branch isolation ----------
# Path B narrow carve-out (claude_skills_carve_out_v1): COMP-serial authors may
# commit to non-COMP branches IFF ALL staged paths match .claude/skills/** (workspace-
# shared skill-discovery substrate authored by CL CVO per LD-0066). Substantive
# CL-fabric content (cases_queue, session logs, responses) remains branch-isolated.
# Ratified: MSTR LD-PENDING 2026-05-26T~04:02Z + Andrew direct 2026-05-26T~04:23Z
# "do it now". Retires the Co-Authored-By bridge pattern for .claude/skills/** path-class.
branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "")
author=$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')
# 2.1.0_SA_COO REMOVED 2026-07-31. Grantor: 0.0.0_AB_MSTR~Z (SoD -- the grantee does not
# grant itself). Andrew-direct re-pointed the serial at CORE: "just run it as 2.1.0_SA_COO
# as youre already running... you are exclusively on the CORE side of NFRA_VELOCITY,
# 2.0.0_SA_COO is handling the other fabric on the ESTATE side."
#
# The rule was CORRECT against a premise Andrew overturned. It fires on BRANCH, so it
# refused EVERY commit by this serial on CLOUD regardless of path -- and that composed
# with the shared-tree sweep into a loop with no exit: cannot commit -> work stays
# uncommitted -> uncommitted is the only class a sweep can reach -> destroyed -> rebuild
# -> still cannot commit. It fired TWICE in one session. Every other seat escapes by
# committing; this one structurally could not.
#
# WHY THIS EDIT EXISTS SEPARATELY FROM THE LIVE FIX: the running gate is
# .git/hooks/pre-commit, which is UNTRACKED and device-local, and it was corrected first
# so the seat could work. This installer is the TRACKED source. It is idempotent-skip
# (see the precomp_v1 guard above), so it would not have re-broken this device -- but a
# fresh clone, a hook reinstall, or the other device would have inherited the stale
# premise and re-created the loop. Deployed-and-repo disagreeing is not resolved by
# asking which is RUNNING; it is resolved by making the tracked source RIGHT.
#
# The other four serials are unchanged and remain branch-isolated to COMP.
comp_re='(^|[^0-9])(1\.1\.0_SA_CTO|3\.1\.0_SA_CVO|2\.1\.0_SC_CompLearns|1\.[1-4]\.0_DS_CompLearns)([^0-9]|$)'
if [[ "$author" =~ $comp_re ]]; then
    if [[ "$branch" != "COMP" ]]; then
        # Carve-out check: are ALL staged paths (ACMR-filtered) under .claude/skills/?
        # ACMR semantic preserved for parity with v1; if all-empty after filter,
        # treat as carve-out-fail (matches prior behavior).
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
            echo "Switch: git checkout COMP    (feature_clb worktree RETIRED, LD-0222 -- CL paused; re-home TBD)" >&2
            echo "(Path B carve-out: .claude/skills/** workspace-shared substrate is permitted on CLOUD; substantive CL-fabric content stays on COMP)" >&2
            exit 1
        fi
    fi
elif [[ "$branch" == "COMP" ]]; then
    echo "BLOCKED: Non-COMP author '$author' must not commit to COMP branch." >&2
    echo "Switch: git checkout CLOUD" >&2
    exit 1
fi

# Hoist ROOT + STAGED into children via env. PRECOMP_REPO_ROOT skips
# the children's own git rev-parse; OWNED_PATHS_STAGED_FILES /
# MSTR_LEDGER_STAGED_FILES are the existing test seams that the
# children already honor, reused here as production fast-paths.
export PRECOMP_REPO_ROOT="$ROOT"
export OWNED_PATHS_STAGED_FILES="$STAGED"
export MSTR_LEDGER_STAGED_FILES="$STAGED"

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
