#!/bin/sh
# =============================================================================
# _open-findings-status.sh -- echo "N open finding(s) (M PAST review_by)".
# =============================================================================
# NFRA_MSBEFF.R4 RULING-1 (1.0.0_SA_CTO~Z, 2026-07-23). THE SURFACING HOME for the
# R4 owned findings is the breadcrumb the trigger fast-path ALREADY emits -- one
# surface, NO new sweeper, NO new cadence (a new cadence is the fan-out that trains
# skimming; the finding file keeps owner+review_by as the accountability record, the
# breadcrumb is the SURFACING). It closes both TRIGGER_LAYER failure limbs:
#   - the open COUNT kills "an honest flag nobody owns" (nobody sees it),
#   - the PAST-DUE count kills the dangling expiry -- an owned finding whose review_by
#     has passed is the eleven-week note with a klaxon, so it must be loud where people
#     already look (every commit that touches a closeout/deploy surface).
#
# FAST-PATH BUDGET: this runs on the synchronous fast path, so it stays O(open findings)
# with no parsing beyond a grep per file. Rule 16 (Git Bash 3.6.7 defaults only).
# Usage: sh _open-findings-status.sh [<workspace-root>]
# =============================================================================
WS="$1"
[ -n "$WS" ] || WS="$(git rev-parse --show-toplevel 2>/dev/null)"
D="$WS/org/critical_paths/.open_findings"
[ -d "$D" ] || { printf '0 open findings'; exit 0; }

today="$(date -u +%Y-%m-%d)"
n=0
past=0
for f in "$D"/*.json; do
    [ -f "$f" ] || continue
    n=$((n + 1))
    rb="$(grep -o '"review_by"[[:space:]]*:[[:space:]]*"[0-9][0-9-]*"' "$f" \
          | grep -o '[0-9][0-9-]*' | head -1)"
    # ISO-8601 dates compare lexicographically; strictly-before today == PAST DUE.
    if [ -n "$rb" ] && [ "$rb" \< "$today" ]; then
        past=$((past + 1))
    fi
done
printf '%s open finding(s) (%s PAST review_by)' "$n" "$past"
