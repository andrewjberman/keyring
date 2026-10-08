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

# ---------- 1. COMP branch isolation: REMOVED 2026-10-08 ----------
# Andrew-direct ~19:3xZ: "There are no CL-Fabric authors, any cl-fabric is long gone and should be deleted if
# there are any vestiges of it" (record: org/tier1_exec/4.0.0_SA_CRO~A/deliverables/
# ANDREW_DIRECT_20261008_193xZ_CL_FABRIC_GONE_DELETE_VESTIGES.md). No COMP branch, no COMP-serial author.

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
