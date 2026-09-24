#!/usr/bin/env bash
# law-lock-check.sh -- pre-commit gate: CLAUDE.md and org/XXX.md are LOCKED.
#
# Andrew-direct 2026-09-24: "make it so no agent can edit claude.md or XXX.md without my express order."
#
# A commit that stages either file is REFUSED unless ANDREW_LAW_EDIT_ORDER names an ANDREW_DIRECT_*.md
# record (under org/, on disk or staged) that carries his order for THIS edit. Every pass and every
# refusal is appended to org/law-edit-audit.log (the instrument for "who edited the law and on what word").
#
# Env (hoisted by the pre-commit orchestrator): PRECOMP_REPO_ROOT, OWNED_PATHS_STAGED_FILES.
# Exit 0 = no locked path staged, or an order named and present. Exit 1 = REFUSED.

ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
STAGED="${OWNED_PATHS_STAGED_FILES:-$(git diff --cached --name-only 2>/dev/null)}"

LOCKED=""
while IFS= read -r p; do
    case "$p" in
        CLAUDE.md|org/XXX.md) LOCKED="$LOCKED $p" ;;
    esac
done <<< "$STAGED"

[ -z "$LOCKED" ] && exit 0

AUDIT="$ROOT/org/law-edit-audit.log"
AUTHOR="$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')"
STAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
ORDER="${ANDREW_LAW_EDIT_ORDER:-}"

refuse() {
    printf '%s REFUSED author=%s paths=%s order=%s reason=%s\n' "$STAMP" "$AUTHOR" "$LOCKED" "${ORDER:-<none>}" "$1" >> "$AUDIT" 2>/dev/null
    echo "BLOCKED: $LOCKED is LOCKED -- no agent edits CLAUDE.md or org/XXX.md without Andrew's express order." >&2
    echo "  $1" >&2
    echo "  Pass ANDREW_LAW_EDIT_ORDER=org/<path>/ANDREW_DIRECT_<stamp>_<slug>.md naming the record of his order for THIS edit." >&2
    exit 1
}

[ -z "$ORDER" ] && refuse "ANDREW_LAW_EDIT_ORDER is not set."
case "$ORDER" in
    org/*ANDREW_DIRECT_*.md) ;;
    *) refuse "ANDREW_LAW_EDIT_ORDER must be an org/**/ANDREW_DIRECT_*.md record path (got: $ORDER)." ;;
esac
if [ ! -f "$ROOT/$ORDER" ] && ! printf '%s\n' "$STAGED" | grep -qx -- "$ORDER"; then
    refuse "the named record does not exist on disk and is not staged: $ORDER"
fi

printf '%s PASS author=%s paths=%s order=%s\n' "$STAMP" "$AUTHOR" "$LOCKED" "$ORDER" >> "$AUDIT" 2>/dev/null
echo "OK: law-lock -- $LOCKED edited under Andrew's order $ORDER (audited)."
exit 0
