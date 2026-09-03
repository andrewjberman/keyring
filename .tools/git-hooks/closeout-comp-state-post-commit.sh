#!/bin/sh
# =============================================================================
# closeout-comp-state-post-commit.sh -- fire comp-state at the PROJECT-CLOSEOUT moment.
# =============================================================================
# NFRA_MSBEFF.R4-A (0.8.0_AE_CloudComp~B, 2026-07-23). TRIGGER_LAYER doctrine:
# comp-state (the BM25 registry-drift linter) ran ZERO times in the entire telemetry
# era while a live registry drift sat undetected -- it was AVAILABLE but never FIRED.
# This binds it to the one moment its answer matters: when a project flips status or a
# REGISTRY row moves, the drift sweep for THAT project fires automatically and its
# output lands as an OWNED item (org/critical_paths/.open_findings/), never a log line.
#
# CONSTRAINTS honored:
#   - post-commit surface (reused, not a new scheduler) -> NON-BLOCKING by construction:
#     the commit is already made; closure is never blocked or altered (TO cross-domain
#     coordination: additive observation only).
#   - fires ONLY on a closeout-shaped commit (a project JSON status->closure OR a
#     REGISTRY.md change) -> never taxes an unrelated commit.
#   - scoped to the CLOSING project (comp-state --project CODE) -> not the 720-BEHIND
#     estate-wide noise; a precise "you just closed X, and X still reads BEHIND -- look."
#   - output lands as an OWNED tracked item {owner, severity, review_by}; its presence is
#     the visible-until-resolved carrier a log line structurally lacks.
#   - backgrounded detached subshell (Rule 16: no setsid/nohup in Git Bash 3.6.7): the
#     ~10s comp-state run is off the commit's critical path.
# =============================================================================
WS="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -n "$WS" ] || exit 0

changed="$(git -C "$WS" diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null)"

# closeout-shaped? a project JSON OR the REGISTRY moved this commit.
echo "$changed" | grep -qE '^org/projects/([A-Za-z0-9_]+\.json|REGISTRY\.md)$' || exit 0

# Derive the closing project CODE(s):
#  (1) any org/projects/<CODE>.json whose staged content declares a CLOSURE status, and
#  (2) if only REGISTRY.md moved, the CODE(s) whose row text changed this commit.
CLOSURE_RE='"status"[[:space:]]*:[[:space:]]*"(complete|complete-as-superseded|cancelled|superseded)"'
codes=""
for f in $(echo "$changed" | grep -E '^org/projects/[A-Za-z0-9_]+\.json$'); do
    if git -C "$WS" show "HEAD:$f" 2>/dev/null | grep -qiE "$CLOSURE_RE"; then
        base="${f##*/}"; codes="$codes ${base%.json}"
    fi
done
# REGISTRY-only closeout: pull CODE tokens from the added/removed rows of this commit.
if echo "$changed" | grep -qE '^org/projects/REGISTRY\.md$'; then
    reg_codes="$(git -C "$WS" show HEAD -- org/projects/REGISTRY.md 2>/dev/null \
        | grep -E '^[+-]' | grep -vE '^[+-]{3}' \
        | grep -oE '\b[A-Z][A-Z0-9]+_[A-Z0-9_]+\b' | sort -u)"
    codes="$codes $reg_codes"
fi
codes="$(echo "$codes" | tr ' ' '\n' | grep -E '.' | sort -u)"
[ -n "$codes" ] || exit 0

# Author of the closing commit = the OWNER of any drift finding.
owner="$(git -C "$WS" log -1 --format='%an' HEAD 2>/dev/null)"
[ -n "$owner" ] || owner="unknown"
head_sha="$(git -C "$WS" rev-parse --short HEAD 2>/dev/null)"

# ASYNC (CTO~Z ruling 2026-07-23, post shared-worktree incident). A SYNCHRONOUS post-commit
# doing comp-state (~10s) on every closeout commit is a LATENCY TAX on all future closeouts,
# and a hook that taxes every commit trains agents to bypass it -- the same skim-death one
# layer over. So: the FAST PATH returns in <100ms (detection + a one-line breadcrumb); the
# heavy comp-state scan runs in a DETACHED background subshell (fire-and-forget) whose result
# lands OUT-OF-BAND as the OWNED FINDING FILE. Per TRIGGER_LAYER the OWNED ITEM is the durable
# carrier (b) -- NOT the terminal print (a detached bg print is unreliable anyway), so the
# finding-file is authoritative and the breadcrumb is only a courtesy pointer.
# Rule 16: detached subshell `( ... ) &` (no setsid/nohup in Git Bash 3.6.7).
# helper ships BESIDE this trigger -- resolve via $0, not $WS (robust in worktrees/fixtures)
_hkdir="$(dirname "$0")"
_of_status="$(sh "$_hkdir/_open-findings-status.sh" "$WS" 2>/dev/null)"
[ -n "$_of_status" ] || _of_status="$(sh "$WS/.tools/git-hooks/_open-findings-status.sh" "$WS" 2>/dev/null)"
printf '\n[closeout-trigger NFRA_MSBEFF.R4-A] closeout detected (%s) -- comp-state drift sweep dispatched (async); finding lands in org/critical_paths/.open_findings/ if drift.\n' "$codes" >&2
printf '  open findings: %s  <- resolve + delete, or the PAST-DUE count is an expiry nobody honoured\n' "${_of_status:-unavailable}" >&2
# CLASS DECISION 2026-09-03 (1.0.0_SA_CTO, mechanism owner, on 0.0.0_AB_MSTR's /govern owner-sweep 93407 -- LD-0528):
# THE OWNED FINDING FILE IS RETIRED FOR R4-A. Measured: 255 of 256 open findings estate-wide were closeout-drift, 250 of
# 250 past review_by, and every one MSTR re-ran cited an UNRELATED later commit sharing tokens. comp-state's BEHIND is a
# LEXICAL (BM25) drift over the corpus; a closed project's row is never touched again while the corpus keeps mentioning
# its tokens, so a closeout-drift finding on a closed row is UNRESOLVABLE BY ANY ACT -- the trigger was measuring itself
# and filing the measurement as an obligation on the closing seat. A finding no act can clear is a control that fires on
# the class name, not on a defect event (CLAUDE.md s.2). The comp-state run and the breadcrumb stay -- "you just closed X,
# here is what comp-state read" is still worth a line -- but the line lands in an APPEND-ONLY RUN LOG, not as an owned
# item with an expiry: one line per closeout, code / closing commit / owner / BEHIND count / POST-CLOSE count. R4-B
# (deploy_stale, blocking-class, a different instrument with a real negative) is untouched.
(
    FIND_DIR="$WS/org/critical_paths/.open_findings"
    mkdir -p "$FIND_DIR"
    now="$(date -u +%Y%m%dT%H%M%SZ)"
    for CODE in $codes; do
        out="$( cd "$WS" && timeout 120 .tools/comp-state --project "$CODE" 2>/dev/null )"
        n_behind="$(echo "$out" | grep -c '^\[BEHIND\]')"
        n_post="$(echo "$out" | grep -c '^\[POST-CLOSE\]')"
        printf '%s | %s | closing=%s | owner=%s | BEHIND=%s | POST-CLOSE=%s | R4-A run log (owned finding retired 2026-09-03, see README)\n' \
            "$now" "$CODE" "$head_sha" "$owner" "$n_behind" "$n_post" >> "$FIND_DIR/closeout-runs.log"
    done
) >/dev/null 2>&1 &
exit 0
