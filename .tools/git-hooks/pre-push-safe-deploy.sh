#!/usr/bin/env bash
# pre-push-safe-deploy.sh -- pre-push hook for safe-deploy gate.
# ADHC_DSFLOW.005 (0.7.0_AE_CloudOps, 2026-05-11)
#
# Reads the push refspec from stdin (git pre-push protocol):
#   <local-ref> <local-sha1> <remote-ref> <remote-sha1>
#
# For each push line whose REMOTE ref is refs/heads/CLOUD (a box that has not switched to a per-box branch), or
# refs/heads/box/<this box>, delegates the range to safe-deploy.sh (which passes if no data/*/scripts/*.py is in it).
# An integration push of CLOUD, another box's branch, or any other ref prints one SKIP line and deploys nothing.
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

# --- ADHC_HALTGT.002 -- HALTGT deploy-time checkpoint ---
# Source the .001 checkpoint library and gate on its exit code before the push:
# a STOP-class inbox message hard-blocks; a routine message surfaces + needs
# HALT_ACK=1; an empty inbox passes silently. Non-zero = abort the push.
# The library never reads stdin, so the git pre-push refspec on stdin is intact.
HALT_GATE="$REPO_ROOT/.tools/halt-gate-check.sh"
if [ -f "$HALT_GATE" ]; then
    # shellcheck source=/dev/null
    . "$HALT_GATE"
    halt_gate_check "pre-push" || exit $?
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

    # WHICH PUSHES DEPLOY (NFRA_CTLPLN FWD-5, contract C-TRUNK-DEPLOY, extended for per-box branches -- build item B2,
    # 1.0.0_SA_CTO PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md; Andrew ~16:4xZ "We should no longer need to be running
    # deploys for the whole fabric on this box"). A deploy fires on the AUTHORING box, for that box's own work only:
    #   refs/heads/box/<this box>  -> deploy the box's diff against origin/CLOUD (merge-base..tip). Other boxes' work the
    #                                 box took from the trunk is already in origin/CLOUD, so it is not in that diff.
    #   refs/heads/box/<other box> -> SKIP: only the authoring box deploys its branch.
    #   refs/heads/CLOUD           -> if the push brings in any origin/box/* tip (an INTEGRATION push), deploy nothing:
    #                                 each box deployed its own work on its box push. If that integration push ALSO
    #                                 carries commits of this box that came through no box branch, REFUSE: push those
    #                                 first, on their own, so they deploy. A CLOUD push that brings in no box branch is
    #                                 a box that has not switched yet: today's behaviour, unchanged.
    #   anything else              -> SKIP, as before.
    # Keyed on the REMOTE ref, so `git push origin work:CLOUD` still deploys and `git push origin CLOUD:work` does not.
    BOX_REFS="$(git for-each-ref --format='%(refname)' refs/remotes/origin/box/ 2>/dev/null || true)"
    case "$REMOTE_REF" in
      refs/heads/box/*)
        _target="${REMOTE_REF#refs/heads/box/}"
        _me="${AGENTBUS_DEVICE:-}"
        if [ -z "$_me" ] && [ -f "$REPO_ROOT/.tools/agentbus-sqs.sh" ]; then
            _me="$(bash "$REPO_ROOT/.tools/agentbus-sqs.sh" device 2>/dev/null | sed -n 's/^device: *//p' | head -1)"
        fi
        if [ -z "$_me" ] || [ "$_me" = "UNKNOWN" ]; then
            echo "BLOCKED: push of $REMOTE_REF -- this box's name is unknown (AGENTBUS_DEVICE unset), so the deploy gate cannot tell whether this is the authoring box. Set AGENTBUS_DEVICE and push again." >&2
            exit 1
        fi
        if [ "$_target" != "$_me" ]; then
            echo "SKIP: no deploy ran for $REMOTE_REF -- box/$_target is not this box ($_me); only the authoring box deploys its branch" >&2
            continue
        fi
        _mb="$(git merge-base refs/remotes/origin/CLOUD "$LOCAL_SHA" 2>/dev/null || true)"
        if [ -z "$_mb" ]; then
            echo "BLOCKED: push of $REMOTE_REF -- no merge-base with origin/CLOUD, so this box's own diff cannot be bounded. Fetch origin and push again." >&2
            exit 1
        fi
        # LEDGER-GATED (1.0.0_SA_CTO ruling msg 107341 on dell1's finding 107334: a scheduled box push must not put a
        # script live whose never-widen pair is unsigned). Of this box's deploy-scope files, ONLY those an OPEN
        # change-management ledger entry names are deployed (.tools/deploy-ledger-names.py); every other one is HELD:
        # not deployed, one HELD-DEPLOY row in org/safe-deploy-bypass-audit.log, and the push still goes through.
        # A list that cannot be read deploys nothing (held, logged). PREPUSH_DEPLOY_LISTER is a test seam only.
        _audit="$REPO_ROOT/org/safe-deploy-bypass-audit.log"
        _ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"; _who="${OPAL_AGENT_SERIAL:-UNKNOWN}"
        _lister="${PREPUSH_DEPLOY_LISTER:-$REPO_ROOT/.tools/crossbox-deploy-check.py}"
        # `|| true` inside: under set -e + pipefail a failed lister would otherwise KILL the hook and block the push.
        _dl="$(python "$_lister" --list-deployable --repo-root "$REPO_ROOT" --commit-range "${_mb}..${LOCAL_SHA}" </dev/null 2>/dev/null | tr -d '\r' || true)"
        _dn="$(printf '%s\n' "$_dl" | sed -n 's/^DEPLOYABLE-COUNT n=\([0-9]*\)$/\1/p' | tail -n 1)"
        if [ -z "$_dn" ]; then
            echo "deploy gate: HELD-DEPLOY -- the deploy-scope list for $REMOTE_REF could not be read; NOTHING deployed; the push goes through" >&2
            echo "$_ts HELD-DEPLOY  $_who  ref=$REMOTE_REF  range=${_mb:0:10}..${LOCAL_SHA:0:10}  reason=deploy-list-unreadable" >> "$_audit" 2>/dev/null || true
            continue
        fi
        if [ "$_dn" -eq 0 ]; then
            echo "deploy gate: $REMOTE_REF -- no deploy-scope file in this box's diff against origin/CLOUD; nothing to deploy" >&2
            continue
        fi
        _dpaths=(); while IFS= read -r _p; do [ -n "$_p" ] && _dpaths+=("$_p"); done < <(printf '%s\n' "$_dl" | sed -n 's/^DEPLOYABLE //p')
        _ln="$(python "$REPO_ROOT/.tools/deploy-ledger-names.py" --repo-root "$REPO_ROOT" --rev "$LOCAL_SHA" "${_dpaths[@]}" 2>/dev/null | tr -d '\r' || true)"
        _led=()
        if printf '%s\n' "$_ln" | grep -q '^LEDGER-OPEN-ENTRIES n='; then
            while read -r _k _p _s; do [ "$_k" = "LEDGERED" ] && _led+=("$_p"); done <<< "$_ln"
        else
            _ln="$(printf 'HELD %s\n' "${_dpaths[@]}")"   # the ledger could not be read: hold everything
        fi
        while read -r _k _p _s; do
            [ "$_k" = "HELD" ] || continue
            # $_s is "ledger-names-path-not-this-build:<slug>" when an OPEN ledger names the path but pins another build (row IRPT_BCKEND-D2-S28)
            echo "deploy gate: HELD-DEPLOY $_p -- ${_s:-no OPEN change-management ledger names it}; not deployed (the push goes through)" >&2
            echo "$_ts HELD-DEPLOY  $_who  ref=$REMOTE_REF  path=$_p  reason=${_s:-no-open-ledger-names-it}" >> "$_audit" 2>/dev/null || true
        done <<< "$_ln"
        if [ "${#_led[@]}" -gt 0 ]; then
            echo "deploy gate: $REMOTE_REF -- deploying ${#_led[@]} ledgered file(s) of ${_dn} deploy-scope file(s)" >&2
            bash "$SAFE_DEPLOY" --no-pipescript "${_led[@]}" || exit 1
        fi
        continue
        ;;
      refs/heads/CLOUD)
        _integ=""
        if [ -n "$BOX_REFS" ] && [[ "$REMOTE_SHA" != "0000000000000000000000000000000000000000" ]]; then
            for _r in $BOX_REFS; do
                if git merge-base --is-ancestor "$_r" "$LOCAL_SHA" 2>/dev/null && ! git merge-base --is-ancestor "$_r" "$REMOTE_SHA" 2>/dev/null; then
                    _integ="${_integ}${_integ:+ }${_r#refs/remotes/origin/}"
                fi
            done
        fi
        if [ -n "$_integ" ]; then
            # shellcheck disable=SC2086
            _own="$(git rev-list --no-merges "${REMOTE_SHA}..${LOCAL_SHA}" --not $BOX_REFS 2>/dev/null | head -5)"
            if [ -n "$_own" ]; then
                echo "BLOCKED: this CLOUD push integrates ($_integ) AND carries commits that came through no box branch:" >&2
                printf '  %s
' $_own >&2
                echo "  Those would never deploy. Push them first on their own (they deploy on that push), then push the integration." >&2
                exit 1
            fi
            echo "SKIP: no deploy ran for $REMOTE_REF -- an integration push ($_integ); each box deployed its own work on its box push" >&2
            continue
        fi
        ;;
      *)
        echo "SKIP: no deploy ran for $REMOTE_REF -- the deploy gate runs only on a push to refs/heads/CLOUD or to this box's refs/heads/box/<box>" >&2
        continue
        ;;
    esac

    # Build commit range: remote_sha..local_sha
    # On new branch (remote = 0000...), diff against merge-base with the shared trunk --
    # the zero-sha range this comment always promised to avoid was actually being passed
    # through, and safe-deploy scans unbounded history on it (hang, measured 2026-08-06
    # on the first SITEZ branch push: >5min vs 2s with the merge-base range).
    if [[ "$REMOTE_SHA" == "0000000000000000000000000000000000000000" ]]; then
        BASE="$(git merge-base origin/CLOUD "$LOCAL_SHA" 2>/dev/null \
             || git merge-base origin/main  "$LOCAL_SHA" 2>/dev/null \
             || echo "$LOCAL_SHA")"
        RANGE="${BASE}..${LOCAL_SHA}"
    else
        RANGE="${REMOTE_SHA}..${LOCAL_SHA}"
    fi

    # Run the deploy gate for this push range.
    # --no-pipescript: hook context has limited PATH; MD5 ETag verify is the primary guard.
    # Run safe-deploy.sh directly (with comp-pipescript) post-push to confirm.
    bash "$SAFE_DEPLOY" --no-pipescript --commit-range "$RANGE" || exit 1
done

exit 0
