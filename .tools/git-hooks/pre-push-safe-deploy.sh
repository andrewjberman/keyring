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

# --- NFRA_CTLPLN round 20 (PRD FWD-5; row NFRA_CTLPLN-D1-S8, remedy P1) -- PINNED-ENTRY DEPLOY ---
# A deploy-scope file named by an OPEN, pinned change-management entry is deployed by this box's push when its S3 bytes
# differ from the pinned blob, whether or not this box's diff carries it: a file that reached CLOUD by integrate before
# its box push is in no later box diff, so the diff-bounded logic above never sees it. Usage: pinned_entry_deploy <tip>
# [deploy-scope paths the box diff already handled]. Pins are read by deploy-ledger-names.py --rev <tip> (it admits only a
# pin that resolves to this build); scope by crossbox-deploy-check.py --list-deployable. The S3 object is read with ONE
# `aws s3 cp` into a temp file: a missing object is ABSENT (differs, so deployed); an unreadable one HOLDS the file.
# Deploys go through safe-deploy.sh, the same path a ledgered box-diff file takes. Nothing else is deployed.
pinned_entry_deploy() {
    local _tip="$1" _pyf _pl _k _p _slug _blob _bucket _key _tmp _err _rc _s3 _bh _ts _who _audit _pd
    _pd=()
    shift
    _ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"; _who="${OPAL_AGENT_SERIAL:-UNKNOWN}"; _audit="$REPO_ROOT/org/safe-deploy-bypass-audit.log"
    _pyf="$(mktemp)"
    cat > "$_pyf" <<'PINNED_PY'
import os, re, subprocess, sys
root, tip = sys.argv[1], sys.argv[2]
handled = set(a.replace('\\', '/') for a in sys.argv[3:])
hook_dir = os.path.join(root, '.tools')
BUCKETS = {'black_diamond': 'opal-data-bd', 'inf': 'opal-data-inf', 'cot': 'opal-data-cot'}
SCRIPT = re.compile(r'^data/([^/]+)/scripts/(gold|silver|bronze)/([^/]+\.py)$')

def git(*args):
    p = subprocess.run(['git', '-C', root] + list(args), capture_output=True)
    return p.stdout.decode('utf-8', 'replace') if p.returncode == 0 else None

tree = git('ls-tree', '-r', '--name-only', tip, '--', 'data')
if tree is None:
    print('PINNED-UNREADABLE tree')
    sys.exit(0)
cands = [p for p in tree.splitlines() if SCRIPT.match(p) and p not in handled]
named = []
if cands:
    led = subprocess.run([sys.executable, os.path.join(hook_dir, 'deploy-ledger-names.py'), '--repo-root', root,
                          '--rev', tip] + cands, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    for ln in led.stdout.splitlines():
        f = ln.split(' ')
        if f[0] == 'LEDGERED' and len(f) >= 3:
            named.append((f[1], f[2]))
slug_of = dict(named)
scope = []
if named:
    sc = subprocess.run([sys.executable, os.path.join(hook_dir, 'crossbox-deploy-check.py'), '--list-deployable',
                         '--repo-root', root, '--files-from', '-'],
                        input='\n'.join(p for p, _ in named) + '\n', capture_output=True, text=True)
    scope = [ln[len('DEPLOYABLE '):].strip() for ln in sc.stdout.splitlines() if ln.startswith('DEPLOYABLE ')]
for p in scope:
    if p not in slug_of:
        continue
    blob = (git('rev-parse', '--verify', '-q', tip + ':' + p) or '').strip()
    m = SCRIPT.match(p)
    bucket = BUCKETS.get(m.group(1), '-') if m else '-'
    key = ('code/%s/%s' % (m.group(2), m.group(3))) if (m and bucket != '-') else '-'
    print('PIN %s %s %s %s %s' % (p, slug_of[p], blob or '-', bucket, key))
print('PINNED-COUNT n=%d' % len(scope))
PINNED_PY
    _pl="$(python -I "$_pyf" "$REPO_ROOT" "$_tip" "$@" 2>/dev/null </dev/null | tr -d '\r' || true)"
    rm -f "$_pyf"
    case "$_pl" in
      *"PINNED-COUNT n="*) ;;
      *)
        echo "deploy gate: HELD-DEPLOY -- the pinned-entry list for $REMOTE_REF could not be read; no pinned file deployed; the push goes through" >&2
        echo "$_ts HELD-DEPLOY  $_who  ref=$REMOTE_REF  reason=pinned-list-unreadable" >> "$_audit" 2>/dev/null || true
        return 0 ;;
    esac
    while IFS=' ' read -r _k _p _slug _blob _bucket _key; do
        [ "$_k" = "PIN" ] || continue
        if [ "$_bucket" = "-" ] || [ -z "$_blob" ] || [ "$_blob" = "-" ]; then
            echo "deploy gate: HELD-DEPLOY $_p -- pinned by OPEN entry $_slug; no S3 bucket or pin blob resolves for it; not deployed (the push goes through)" >&2
            echo "$_ts HELD-DEPLOY  $_who  ref=$REMOTE_REF  path=$_p  reason=pinned-s3-target-not-derivable" >> "$_audit" 2>/dev/null || true
            continue
        fi
        _tmp="$(mktemp)"; _err="$(mktemp)"
        _rc=0; aws s3 cp "s3://$_bucket/$_key" "$_tmp" >/dev/null 2>"$_err" </dev/null || _rc=$?
        if [ "$_rc" -eq 0 ]; then
            _s3="$(sha256sum "$_tmp" | cut -c1-64)"
        elif grep -q -E 'NoSuchKey|Not Found|404' "$_err"; then
            _s3="ABSENT"
        else
            _s3="UNREADABLE"
        fi
        _bh="$(git -C "$REPO_ROOT" cat-file blob "$_blob" | sha256sum | cut -c1-64)"
        rm -f "$_tmp" "$_err"
        if [ "$_s3" = "UNREADABLE" ]; then
            echo "deploy gate: HELD-DEPLOY $_p -- pinned by OPEN entry $_slug; the S3 object could not be read; not deployed (the push goes through)" >&2
            echo "$_ts HELD-DEPLOY  $_who  ref=$REMOTE_REF  path=$_p  reason=pinned-s3-read-failed" >> "$_audit" 2>/dev/null || true
            continue
        fi
        if [ "$_s3" = "$_bh" ]; then
            echo "deploy gate: $_p -- pinned by OPEN entry $_slug; S3 bytes already equal the pin; nothing to deploy" >&2
            continue
        fi
        echo "deploy gate: $REMOTE_REF -- deploying $_p: pinned by OPEN entry $_slug, S3 ${_s3:0:12} differs from the pin ${_bh:0:12}" >&2
        echo "$_ts PINNED-DEPLOY  $_who  ref=$REMOTE_REF  path=$_p  slug=$_slug  s3=${_s3:0:12}  pin=${_bh:0:12}" >> "$_audit" 2>/dev/null || true
        _pd+=("$_p")
    done <<< "$_pl"
    if [ "${#_pd[@]}" -gt 0 ]; then
        bash "$SAFE_DEPLOY" --no-pipescript "${_pd[@]}" || exit 1
    fi
    return 0
}

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
            echo "deploy gate: $REMOTE_REF -- no deploy-scope file in this box's diff against origin/CLOUD; nothing to deploy from the diff" >&2
            pinned_entry_deploy "$LOCAL_SHA" ${_dpaths[@]+"${_dpaths[@]}"}
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
        pinned_entry_deploy "$LOCAL_SHA" ${_dpaths[@]+"${_dpaths[@]}"}
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
