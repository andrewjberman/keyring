#!/usr/bin/env bash
# pre-push-safe-deploy.sh -- pre-push hook for safe-deploy gate.
# ADHC_DSFLOW.005 (0.7.0_AE_CloudOps, 2026-05-11)
#
# Reads the push refspec from stdin (git pre-push protocol):
#   <local-ref> <local-sha1> <remote-ref> <remote-sha1>
#
# For each push line, if data/*/scripts/*.py files are in the diff,
# delegates to safe-deploy.sh. Passes if no script files are in scope.
#
# To bypass (emergency only):
#   git push --no-verify
# --no-verify is audit-loggable by the git pre-push protocol; prefer
# running safe-deploy.sh --allow-stale --reason "..." manually instead.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
SAFE_DEPLOY="$REPO_ROOT/.tools/safe-deploy.sh"

if [ ! -f "$SAFE_DEPLOY" ]; then
    echo "WARN: safe-deploy.sh not found at $SAFE_DEPLOY -- skipping deploy gate" >&2
    exit 0
fi

REMOTE="$1"
REMOTE_URL="$2"

while read -r LOCAL_REF LOCAL_SHA REMOTE_REF REMOTE_SHA; do
    # Skip deletes (sha = 0000...)
    if [[ "$LOCAL_SHA" == "0000000000000000000000000000000000000000" ]]; then
        continue
    fi

    # Skip tag pushes — tags are immutable refs, not code changes; no deploy needed
    if [[ "$LOCAL_REF" == refs/tags/* ]]; then
        continue
    fi

    # Build commit range: remote_sha..local_sha
    # On new branch (remote = 0000...), diff against merge-base of main
    RANGE="${REMOTE_SHA}..${LOCAL_SHA}"

    # Run the deploy gate for this push range.
    # --no-pipescript: hook context has limited PATH; MD5 ETag verify is the primary guard.
    # Run safe-deploy.sh directly (with comp-pipescript) post-push to confirm.
    bash "$SAFE_DEPLOY" --no-pipescript --commit-range "$RANGE" || exit 1
done

exit 0
