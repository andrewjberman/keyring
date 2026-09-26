#!/usr/bin/env bash
# =============================================================================
# gitlink-publication-check.sh -- refuse a staged submodule pointer that is not
# PUBLISHED on that submodule's remote.
#
# ADOPTED 2026-09-26 by 3.0.0_SA_CVO~Z as a governance fork
# (ADJUDICATION_GITLINK_PUBLICATION_CHECK_20260926_Z.md @fd6fe5c6c9), on a
# proposal by 0.0.0_AB_MSTR~Z, with three refinements from 1.0.0_SA_CTO~Z and
# the CVO. Mechanical, not an approval gate.
#
# THE DEFECT IT CATCHES. A trunk commit can name a submodule commit that exists
# only locally. Every parent-side instrument reads green; the seam is invisible
# until someone else clones and cannot fetch the pointer. Measured 2026-09-26:
# origin/CLOUD carried portal gitlink 6712c7429e while that commit was on NO
# remote branch.
#
# THE THREE REFINEMENTS, each closing the same defect one layer down. They are
# the whole design, so they are stated before the code:
#
#   1. RESOLVE BY ls-remote AT CHECK TIME, never from the local remote-tracking
#      ref. A stale local origin/DEV makes --is-ancestor return false for a
#      commit that IS on the remote, and FALSE means "not that direction",
#      never "absent". (1.0.0_SA_CTO~Z)
#
#   2. "THAT SUBMODULE'S ORIGIN BRANCH" IS SINGULAR AND UNDEFINED. The portal
#      remote carried NINE heads when this was adjudicated, with PROD at a
#      different commit from DEV, so one hard-coded branch would FALSE-REFUSE a
#      legitimate gitlink today. Test against the PRINTED SET of heads and
#      print its denominator. (3.0.0_SA_CVO~Z spec 1)
#
#   3. ls-remote CAN RETURN EMPTY ON A NETWORK FAULT, and empty vs genuine
#      absence is THE SAME VALUE. Fail-closed or fail-open is acceptable if
#      PRINTED; a SILENT fail-open is refused. This gate FAILS CLOSED and says
#      so on every such line. (3.0.0_SA_CVO~Z spec 2)
#
# So every refusal PRINTS THE READING IT REFUSED ON: the head set, its
# denominator, and whether the network read succeeded. A refusal that cannot be
# distinguished from a blind instrument is the defect this gate exists to catch.
#
# COST: one ls-remote plus one merge-base per head per gitlink commit.
# NON-APPLICATION: a commit that moves no gitlink -- the gate prints its zero
# denominator and exits 0.
#
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only (Rule 4).
# =============================================================================
set -u

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$ROOT" ] || { echo "ERROR: gitlink-publication-check: not in a git repo." >&2; exit 1; }

# ---------------------------------------------------------------------------
# The staged gitlink set. `git diff --cached --raw` prints the NEW mode in
# field 2; 160000 is a gitlink. A DELETED submodule has a new sha of all zeros
# and is not a publication question, so it is excluded and counted separately.
# ---------------------------------------------------------------------------
RAW="$(git diff --cached --raw 2>/dev/null || true)"
GITLINKS="$(printf '%s\n' "$RAW" | awk '$2 == "160000" { print $4 "\t" substr($0, index($0, $5)) }' 2>/dev/null || true)"

TOTAL=0
SKIPPED_DELETE=0
CHECKED=0
REFUSALS=0

# Field layout of `git diff --cached --raw`:
#   :<oldmode> <newmode> <oldsha> <newsha> <status>\t<path>
while IFS= read -r line; do
    [ -n "$line" ] || continue
    NEWSHA="$(printf '%s' "$line" | cut -f1)"
    REST="$(printf '%s' "$line" | cut -f2-)"
    SMPATH="$(printf '%s' "$REST" | sed 's/^[A-Z][0-9]*[ \t]*//')"
    [ -n "$SMPATH" ] || continue
    TOTAL=$((TOTAL + 1))

    case "$NEWSHA" in
        0000000000000000000000000000000000000000)
            SKIPPED_DELETE=$((SKIPPED_DELETE + 1))
            echo "SKIP: gitlink-publication-check: '$SMPATH' is a submodule REMOVAL (new sha all zeros); publication does not apply."
            continue ;;
    esac

    CHECKED=$((CHECKED + 1))

    # -----------------------------------------------------------------------
    # The remote URL. Prefer the submodule's own origin (what a push there
    # actually targets); fall back to .gitmodules.
    # -----------------------------------------------------------------------
    URL="$(git -C "$ROOT/$SMPATH" config --get remote.origin.url 2>/dev/null || true)"
    if [ -z "$URL" ]; then
        URL="$(git config -f "$ROOT/.gitmodules" --get "submodule.$SMPATH.url" 2>/dev/null || true)"
    fi
    if [ -z "$URL" ]; then
        echo "BLOCKED: gitlink-publication-check: '$SMPATH' -> $NEWSHA"
        echo "  READING: no remote URL resolved (submodule origin ABSENT and .gitmodules entry ABSENT)."
        echo "  This is a FAIL-CLOSED refusal: with no remote to ask, published and unpublished read identically."
        REFUSALS=$((REFUSALS + 1))
        continue
    fi

    # -----------------------------------------------------------------------
    # Refinement 1: ls-remote AT CHECK TIME. Refinement 3: an empty or failed
    # read is NOT an absence, and the branch taken is PRINTED either way.
    # -----------------------------------------------------------------------
    LS_OUT="$(git ls-remote --heads "$URL" 2>/dev/null)"
    LS_RC=$?
    HEADS="$(printf '%s\n' "$LS_OUT" | awk 'NF >= 2 { print $1 "\t" $2 }')"
    NHEADS="$(printf '%s\n' "$HEADS" | awk 'NF > 0' | wc -l | tr -d ' ')"

    if [ "$LS_RC" -ne 0 ] || [ "$NHEADS" -eq 0 ]; then
        echo "BLOCKED: gitlink-publication-check: '$SMPATH' -> $NEWSHA"
        echo "  READING: ls-remote rc=$LS_RC, heads returned=$NHEADS, url=$URL"
        echo "  A network fault and a remote with no branches RETURN THE SAME VALUE here, so this"
        echo "  gate does NOT convert the empty read into an absence. This is a FAIL-CLOSED refusal."
        echo "  If the remote is genuinely reachable, re-run; if it is genuinely empty, push the"
        echo "  submodule branch first."
        REFUSALS=$((REFUSALS + 1))
        continue
    fi

    # Objects for the remote heads may not be present locally. Fetch to supply
    # them; the SHAS still come from the ls-remote read above, never from a
    # remote-tracking ref (refinement 1). A failed fetch is not fatal on its
    # own -- a head may still be testable -- but it is printed.
    FETCH_RC=0
    git -C "$ROOT/$SMPATH" fetch --quiet origin 2>/dev/null || FETCH_RC=$?

    PUBLISHED=0
    UNTESTABLE=0
    MATCHED_REF=""
    while IFS= read -r hline; do
        [ -n "$hline" ] || continue
        HSHA="$(printf '%s' "$hline" | cut -f1)"
        HREF="$(printf '%s' "$hline" | cut -f2)"
        if [ "$HSHA" = "$NEWSHA" ]; then
            PUBLISHED=1; MATCHED_REF="$HREF (exact tip)"; break
        fi
        if ! git -C "$ROOT/$SMPATH" cat-file -e "${HSHA}^{commit}" 2>/dev/null; then
            UNTESTABLE=$((UNTESTABLE + 1))
            continue
        fi
        if git -C "$ROOT/$SMPATH" merge-base --is-ancestor "$NEWSHA" "$HSHA" 2>/dev/null; then
            PUBLISHED=1; MATCHED_REF="$HREF"; break
        fi
    done <<EOF
$HEADS
EOF

    if [ "$PUBLISHED" -eq 1 ]; then
        echo "OK: gitlink-publication-check: '$SMPATH' -> $NEWSHA is published (ancestor of $MATCHED_REF)."
        echo "  READING: ls-remote rc=$LS_RC, heads tested against=$NHEADS, fetch rc=$FETCH_RC, untestable heads=$UNTESTABLE"
        continue
    fi

    echo "BLOCKED: gitlink-publication-check: '$SMPATH' -> $NEWSHA is NOT PUBLISHED."
    echo "  READING: ls-remote rc=$LS_RC, heads tested against=$NHEADS (the denominator), fetch rc=$FETCH_RC, untestable heads=$UNTESTABLE"
    echo "  url=$URL"
    echo "  HEADS READ AT CHECK TIME:"
    printf '%s\n' "$HEADS" | awk 'NF > 0 { printf "    %s  %s\n", substr($1,1,12), $2 }'
    if [ "$UNTESTABLE" -gt 0 ]; then
        echo "  WARNING: $UNTESTABLE of $NHEADS heads could not be tested (objects absent locally after fetch rc=$FETCH_RC)."
        echo "  Those heads are NOT counted as negative evidence; this refusal rests on the heads that WERE testable."
    fi
    echo "  REMEDY: push the submodule branch first, then re-stage the gitlink --"
    echo "    git -C $SMPATH push origin <branch>"
    echo "  A trunk commit naming an unpublished submodule commit cannot be resolved by any other clone."
    REFUSALS=$((REFUSALS + 1))
done <<EOF
$GITLINKS
EOF

echo "gitlink-publication-check: staged gitlinks=$TOTAL (checked=$CHECKED, removals skipped=$SKIPPED_DELETE), refusals=$REFUSALS"
[ "$REFUSALS" -eq 0 ] || exit 1
exit 0
