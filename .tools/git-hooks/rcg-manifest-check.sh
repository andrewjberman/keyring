#!/usr/bin/env bash
# =============================================================================
# rcg-manifest-check.sh -- pre-commit wiring for the rcg/ folder contract.
#
# NFRA_REPOCOHERENCEGRAPH D-0001 item 3 (ferried to 1.0.0_SA_CTO~B via D-0004 /
# R-0021). The checker itself -- rcg/bin/manifest_check.py -- was built standalone
# under the CRO solo posture (R-0001) and has been correct since it landed. This
# script is the missing half: putting it in the chain so it runs whether or not
# the author remembers.
#
# WHY IT IS NOT MERELY HYGIENE (the evidence, 2026-08-03): a CRLF-dead pattern in
# rcg/.gitignore let 17 scan-vintage artifacts commit into tracking. The standalone
# gate provably WOULD have denied them; it simply was not invoked. Fixed at
# 3d13bed37d by untracking them, but "the author ran the checker" is discipline,
# not a control. Andrew-direct on this folder: "it is IMPERATIVE that folder is
# kept immaculately clean; should be strict rules on writes and edits so that it
# does not become victim to the same sprawl."
#
# ---------------------------------------------------------------------------
# TWO DESIGN DECISIONS, both deliberate:
#
# 1. SCOPED, NOT FABRIC-WIDE. This fires ONLY when the staged set touches rcg/.
#    The checker spawns python + several git subprocesses; rcg/ is a single-writer
#    lane, so running it on every commit by every agent would tax the whole fabric
#    for one folder. The parent hook's own precomp_v1 header (RV0017-F002) exists
#    because that subprocess fan-out was already measured as a real cost.
#    Correctness is unaffected: an out-of-manifest file can only ENTER the tree by
#    being staged under rcg/, so gating at introduction catches every path in.
#
# 2. FAIL-CLOSED, unlike its siblings. Stages 2-4 of the parent hook guard with
#    `if [ -f <script> ]` -- a MISSING script silently disables them. That is the
#    gate-fails-open-and-silent class this repo has been bitten by (the ~/bin
#    forwarder collapse, 2026-07-29: safe-commit's hooks printed "No such file or
#    directory" and let commits through). Here, if rcg/ is being written and the
#    checker cannot be evaluated, that is a DENY. A gate that cannot fail is not a
#    control; a gate that vanishes silently is worse than none, because its absence
#    reads exactly like its approval.
#
# rc: 0 = clean or not-applicable | 1 = DENY (out-of-manifest, append-only edit, or
# the gate could not evaluate itself). The checker's own rc=2 (deny) and rc=3
# (cannot-evaluate) BOTH become 1 here -- never a silent pass.
#
# Rule 16: Git Bash 3.6.7 default utilities only (git, grep, printf, command).
# CLAUDE.md Code Quality: ASCII only.
#
# Author: 1.0.0_SA_CTO~B, 2026-08-04.
# =============================================================================
set -e

ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
[ -n "$ROOT" ] || exit 0

# Reuse the parent hook's hoisted staged list when present (precomp_v1 seam);
# otherwise compute it. --diff-filter=d: a staged DELETION leaves the population,
# matching the checker's own denominator so removing a leaked file does not
# re-flag the removal itself.
STAGED="${OWNED_PATHS_STAGED_FILES:-}"
if [ -z "$STAGED" ]; then
    STAGED="$(git -C "$ROOT" diff --cached --name-only --diff-filter=d 2>/dev/null || true)"
fi
[ -n "$STAGED" ] || exit 0

# Applicability: does this commit touch rcg/ at all?
if ! printf '%s\n' "$STAGED" | grep -q '^rcg/'; then
    exit 0
fi

CHECKER="$ROOT/rcg/bin/manifest_check.py"

if [ ! -f "$CHECKER" ]; then
    echo "" >&2
    echo "BLOCKED: rcg/ paths are staged but the folder gate is MISSING." >&2
    echo "  expected: $CHECKER" >&2
    echo "  The rcg/ folder contract (PRD s.12) is enforced by that checker. With it" >&2
    echo "  absent the contract is unenforceable, so this is a DENY, not a skip." >&2
    echo "  If you deleted it deliberately, restore it or amend the contract first." >&2
    echo "" >&2
    exit 1
fi

if ! command -v python >/dev/null 2>&1; then
    echo "" >&2
    echo "BLOCKED: rcg/ paths staged but 'python' is not on PATH -- gate cannot evaluate." >&2
    echo "" >&2
    exit 1
fi

# The checker prints its own DENOMINATOR line and every DENY with a remedy.
# Pass its output through untouched; it is the operator-facing surface.
if ! python "$CHECKER"; then
    echo "" >&2
    echo "BLOCKED: rcg/ folder-contract violation (see rcg-manifest-check output above)." >&2
    echo "  Remedy is always one of: add the file to rcg/MANIFEST.yaml allowed_paths in" >&2
    echo "  THIS SAME commit, or unstage/remove it. Append-only ledgers are never edited." >&2
    echo "" >&2
    exit 1
fi

exit 0
