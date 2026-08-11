#!/usr/bin/env bash
# to-proof-of-spec-check.sh -- ISSUANCE LINT: a NEW task-order file must carry <proof_of_spec>.
#
# Andrew-direct 2026-08-11 ~0821Z (canonization, verbatim in CVO's record
# ANDREW_DIRECT_20260811_PROOF_OF_SPEC_CANONIZED.md): "I do not want TOs being
# issued that do not have machine-readable data contracts, where the agent
# responsible must fill out the contract based on their efforts."
# GO on this mechanical lint: Andrew-direct at the CTO terminal ~0824Z ("Go").
#
# Scope: staged ADDED files matching */task_orders/*.md|.xml (NEW issuance only --
# pre-existing TOs are not retro-gated; edits to existing TOs pass untouched).
# The check reads STAGED content (git show :path), never the worktree.
# Audited override: TO_POS_OVERRIDE="<reason>" -- appends to org/to-pos-override-audit.log.
#
# Env from the orchestrator: ROOT, STAGED (precomp_v1 contract).

set -u

root="${ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
staged="${STAGED:-$(git diff --cached --name-only 2>/dev/null || true)}"
[ -z "$staged" ] && exit 0

added="$(git diff --cached --name-only --diff-filter=A 2>/dev/null | grep -E '(^|/)task_orders/[^/]+\.(md|xml)$' || true)"
[ -z "$added" ] && exit 0

blocked=0
while IFS= read -r f; do
    [ -z "$f" ] && continue
    if git show ":$f" 2>/dev/null | grep -q '<proof_of_spec'; then
        continue
    fi
    if [ -n "${TO_POS_OVERRIDE:-}" ]; then
        printf '%s | %s | %s | %s\n' "$(date -u +%Y-%m-%dT%H%M%SZ)" \
            "$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')" "$f" "$TO_POS_OVERRIDE" \
            >> "$root/org/to-pos-override-audit.log"
        echo "WARN: TO_POS_OVERRIDE -- $f issued WITHOUT <proof_of_spec> (audited: $TO_POS_OVERRIDE)" >&2
        continue
    fi
    echo "BLOCKED: NEW task order '$f' carries NO <proof_of_spec> element." >&2
    echo "  Andrew-direct 2026-08-11: no TO issues without a machine-readable data contract." >&2
    echo "  Fix: mint the criterion-id set per org/ref/TASK_ORDER_PROTOCOL.md <proof_of_spec>;" >&2
    echo "  contract schema: org/standards/PROOF_OF_SPEC.schema.json; validator: .tools/proof-of-spec-check.py" >&2
    echo "  Audited override (edge cases only): TO_POS_OVERRIDE=\"<reason>\" git commit ..." >&2
    blocked=1
done <<EOF_LIST
$added
EOF_LIST

exit $blocked
