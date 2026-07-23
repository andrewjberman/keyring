#!/bin/sh
# =============================================================================
# deploy-pipescript-check-post-commit.sh -- fire comp-pipescript deployed at the
# DEPLOY-COMPLETION moment (NFRA_MSBEFF.R4-B, 0.8.0_AE_CloudComp~B, 2026-07-23).
# =============================================================================
# THE GAP (measured): the automated deploy path runs safe-deploy with --no-pipescript
# (pre-push-safe-deploy.sh), so the comp-pipescript deployed MATCH check (STALE/MISSING)
# is SKIPPED and deferred to a manual "run it post-push to confirm" that nobody does.
# Consequence (bd-gold-trigger-vs-4-stale-scripts, 2026-07-xx): a PROD gold-trigger fired
# against 4 stale S3 scripts because no tool detected the deploy gap automatically pre-run.
# comp-pipescript deployed was AVAILABLE and never FIRED on that path.
#
# THIS binds it to the deploy-COMPLETION moment: a deploy-completion ledger is committed
# (CLAUDE.md NEVER-rule: opened at deploy-start, CLOSED at completion). When that ledger
# NAMES gold/silver/bronze scripts, run the deployed-check on exactly those scripts. A STALE
# / MISSING lands as an OWNED finding + LOUD -- the deploy that landed without the check now
# surfaces it. A serve-only ledger (no scripts named) is not a script deploy -> silent.
#
# CONSTRAINTS: post-commit surface (reused, no new scheduler); SYNCHRONOUS but rare (a deploy
# ledger closes seldom); NON-BLOCKING (the ledger commit is already made); Rule 16 clean.
# =============================================================================
WS="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -n "$WS" ] || exit 0

changed="$(git -C "$WS" diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null)"
echo "$changed" | grep -qE '^org/critical_paths/change_management/.*_deploy_completion\.md$' || exit 0

# Collect the ledger file(s) closed in this commit, and the SCRIPT paths they name.
scripts=""
for led in $(echo "$changed" | grep -E '^org/critical_paths/change_management/.*_deploy_completion\.md$'); do
    got="$(git -C "$WS" show "HEAD:$led" 2>/dev/null \
        | grep -oE 'data/[a-z_]+/scripts/(gold|silver|bronze)/[A-Za-z0-9_.-]+\.py' | sort -u)"
    scripts="$scripts $got"
done
scripts="$(echo "$scripts" | tr ' ' '\n' | grep -E '.' | sort -u)"
# No scripts named -> a serve-only / infra ledger, not a script deploy. Nothing to verify.
[ -n "$scripts" ] || exit 0

owner="$(git -C "$WS" log -1 --format='%an' HEAD 2>/dev/null)"; [ -n "$owner" ] || owner="unknown"
head_sha="$(git -C "$WS" rev-parse --short HEAD 2>/dev/null)"
FIND_DIR="$WS/org/critical_paths/.open_findings"
mkdir -p "$FIND_DIR"
# ASYNC (CTO~Z ruling 2026-07-23): fast path returns in <100ms with a breadcrumb; the heavy
# comp-pipescript-deployed sweep (+AWS) runs DETACHED (fire-and-forget) and lands its result
# OUT-OF-BAND as the owned finding file -- never a per-commit latency tax. Rule 16 detached `&`.
printf '\n[deploy-check NFRA_MSBEFF.R4-B] deploy-completion ledger closed (%s script(s) named) -- comp-pipescript deployed sweep dispatched (async); finding in .open_findings/ if STALE.\n' "$(echo "$scripts" | grep -c .)" >&2
(
now="$(date -u +%Y%m%dT%H%M%SZ)"
review_by="$(date -u -d '+1 day' +%Y-%m-%d 2>/dev/null || date -u +%Y-%m-%d)"
stale_list=""
for s in $scripts; do
    out="$( cd "$WS" && timeout 90 .tools/comp-pipescript deployed "$s" 2>/dev/null )"
    # Parse the Summary COUNTS, never a bare substring: the summary line literally reads
    # "N MATCH, 0 STALE, 0 MISSING_ON_S3" even for a clean MATCH, so `grep 'STALE|MISSING'`
    # false-flags EVERY script (the documented _pipescript_output_ok trap). STALE>0 OR
    # MISSING_ON_S3>0 in the Summary => the deploy landed against stale/absent S3.
    summary="$(echo "$out" | grep -oE 'Summary:.*' | head -1)"
    stale_n="$(printf '%s' "$summary" | grep -oE '[0-9]+ STALE' | grep -oE '^[0-9]+')"
    miss_n="$(printf '%s' "$summary" | grep -oE '[0-9]+ MISSING_ON_S3' | grep -oE '^[0-9]+')"
    [ -n "$stale_n" ] || stale_n=0
    [ -n "$miss_n" ] || miss_n=0
    if [ -z "$summary" ]; then
        # No summary line (e.g. engine unreachable) -> fall back to a per-line status scan.
        if echo "$out" | grep -qE '\b(STALE|MISSING_ON_S3)\b'; then bad=1; else bad=0; fi
    elif [ "$stale_n" -gt 0 ] || [ "$miss_n" -gt 0 ]; then bad=1; else bad=0; fi
    if [ "$bad" -eq 1 ]; then
        printf '  STALE/MISSING  %s  (STALE=%s MISSING_ON_S3=%s)\n' "$s" "$stale_n" "$miss_n" >&2
        stale_list="$stale_list $s"
    else
        printf '  MATCH          %s\n' "$s" >&2
    fi
done

stale_list="$(echo "$stale_list" | tr ' ' '\n' | grep -E '.' | sort -u)"
if [ -n "$stale_list" ]; then
    nstale="$(echo "$stale_list" | grep -c '.')"
    f="$FIND_DIR/deploy_stale_${now}.json"
    {
        printf '{\n'
        printf '  "finding": "deploy-stale-s3",\n'
        printf '  "owner": "%s",\n' "$owner"
        printf '  "severity": "blocking-class",\n'
        printf '  "review_by": "%s",\n' "$review_by"
        printf '  "closing_commit": "%s",\n' "$head_sha"
        printf '  "detected_utc": "%s",\n' "$now"
        printf '  "stale_script_count": %s,\n' "$nstale"
        printf '  "stale_scripts": "%s",\n' "$(echo "$stale_list" | tr '\n' ' ')"
        printf '  "trigger": "deploy-pipescript-check-post-commit (NFRA_MSBEFF.R4-B)",\n'
        printf '  "note": "A deploy-completion ledger CLOSED but comp-pipescript deployed reports the named script(s) STALE/MISSING on S3 -- the exact bd-gold-trigger-vs-4-stale-scripts class. A scheduled PROD trigger may run STALE code. RE-DEPLOY (.tools/safe-deploy.sh <script>) so S3 matches the repo, then delete this file."\n'
        printf '}\n'
    } > "$f"
fi
) >/dev/null 2>&1 &
exit 0
