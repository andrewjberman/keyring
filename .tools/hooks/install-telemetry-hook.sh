#!/usr/bin/env bash
# install-telemetry-hook.sh -- bootstrap telemetry hook scripts from canonical sources.
#
# Idempotent. Copies version-controlled canonical hook sources from org/mcp/hooks/
# into the gitignored runtime install target at .tools/hooks/. Per-checkout local
# install pattern matching .tools/git-hooks/install-mstr-ledger-check.sh precedent.
#
# Bootstraps:
#   org/mcp/hooks/post-tool-telemetry.sh -> .tools/hooks/post-tool-telemetry.sh
#   org/mcp/hooks/classify-tool-kind.sh  -> .tools/hooks/classify-tool-kind.sh
#
# Marker: TELEMETRY_HOOK_INSTALL_V1 (idempotency check on installed copy).
#
# WB-1.1 + 0e8fffe1e empirical fix carried in canonical content; install replaces
# any stale local copy with the canonical version on each run.
#
# Per-checkout activation: run after `git pull` brings new canonical content.
# Safe to re-run anytime. Drift mitigation: WARNs if installed hash differs
# from canonical hash (would indicate a stale install or out-of-band local edit).
#
# Authority: LD-0070 + LD-0084 batched ratification + Andrew-direct substrate-cleanup
# dispatch 2026-05-26T~04:32Z (MSTR §1 TARGET A option (a) move+bootstrap pattern;
# ws CVO CORROBORATE on (a) per 3-ground rationale 20260526T043820Z).

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

# Canonical sources
CANONICAL_HOOK="$REPO_ROOT/org/mcp/hooks/post-tool-telemetry.sh"
CANONICAL_CLASSIFIER="$REPO_ROOT/org/mcp/hooks/classify-tool-kind.sh"

# Install targets (gitignored per .gitignore:175)
INSTALL_DIR="$REPO_ROOT/.tools/hooks"
INSTALL_HOOK="$INSTALL_DIR/post-tool-telemetry.sh"
INSTALL_CLASSIFIER="$INSTALL_DIR/classify-tool-kind.sh"

# Gate: canonical sources must exist
if [ ! -f "$CANONICAL_HOOK" ]; then
    echo "ERROR: $CANONICAL_HOOK not found -- canonical source missing." >&2
    exit 1
fi
if [ ! -f "$CANONICAL_CLASSIFIER" ]; then
    echo "ERROR: $CANONICAL_CLASSIFIER not found -- canonical source missing." >&2
    exit 1
fi

mkdir -p "$INSTALL_DIR"

# Drift detection: compare installed vs canonical hash; WARN if differs
install_with_drift_check() {
    local canonical="$1"
    local target="$2"
    local name="$3"

    if [ -f "$target" ]; then
        local canonical_hash target_hash
        canonical_hash="$(sha256sum "$canonical" | awk '{print $1}')"
        target_hash="$(sha256sum "$target" | awk '{print $1}')"
        if [ "$canonical_hash" != "$target_hash" ]; then
            echo "WARN: $name installed copy differs from canonical -- overwriting." >&2
            echo "$(date -u +%FT%TZ) TELEMETRY_HOOK_INSTALL_DRIFT $name installed=$target_hash canonical=$canonical_hash" >> "$REPO_ROOT/org/mcp/hook_errors.log" 2>/dev/null || true
        fi
    fi

    cp "$canonical" "$target"
    chmod +x "$target" 2>/dev/null || true
}

install_with_drift_check "$CANONICAL_HOOK" "$INSTALL_HOOK" "post-tool-telemetry.sh"
install_with_drift_check "$CANONICAL_CLASSIFIER" "$INSTALL_CLASSIFIER" "classify-tool-kind.sh"

echo "OK: telemetry hook installed -- $INSTALL_HOOK + $INSTALL_CLASSIFIER (canonical sources at $REPO_ROOT/org/mcp/hooks/; marker TELEMETRY_HOOK_INSTALL_V1)"
