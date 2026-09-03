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
# LAYER-2 DECOMP LINT (2026-08-27, 1.0.0_SA_CTO; authority = the 08-21 ratification,
# org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md item 2 "build routed"; sequenced as a D2
# launch precondition per CVO's ANDREW_DIRECT_20260827_D2_TIGHTENING_LOCKIN_BEFORE_FLOOD.md):
# a NEW TO whose project is PIPELINE-REGISTERED must carry <decomp_ref> -- refused otherwise.
# Pipeline-registered predicate: org/projects/{CODE}.json exists AND carries "dep_stage"
# (the ratification's own forward-only stage field -- pre-pipeline projects structurally
# out of scope, no retro-gating; CODE = filename segment before the first dot, per the
# TASK_ORDER_PROTOCOL filename convention; ad-hoc no-project TOs resolve to no JSON and pass).
# Audited override: TO_DECOMP_OVERRIDE="<reason>" -- same audit log, DECOMP tag.
#
# Env from the orchestrator: ROOT, STAGED (precomp_v1 contract).

set -u

root="${ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
staged="${STAGED:-$(git diff --cached --name-only 2>/dev/null || true)}"
[ -z "$staged" ] && exit 0

added="$(git diff --cached --name-only --diff-filter=A 2>/dev/null | grep -E '(^|/)task_orders/[^/]+\.(md|xml)$|^org/missions/D(0|[1-9][0-9]?)/[^/]+/[^/]+/task-orders/[^/]+\.(md|xml)$' || true)"
[ -z "$added" ] && exit 0

blocked=0
while IFS= read -r f; do
    [ -z "$f" ] && continue
    content="$(git show ":$f" 2>/dev/null || true)"

    if ! printf '%s\n' "$content" | grep -q '<proof_of_spec'; then
        if [ -n "${TO_POS_OVERRIDE:-}" ]; then
            printf '%s | %s | %s | %s\n' "$(date -u +%Y-%m-%dT%H%M%SZ)" \
                "$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')" "$f" "$TO_POS_OVERRIDE" \
                >> "$root/org/to-pos-override-audit.log"
            echo "WARN: TO_POS_OVERRIDE -- $f issued WITHOUT <proof_of_spec> (audited: $TO_POS_OVERRIDE)" >&2
        else
            echo "BLOCKED: NEW task order '$f' carries NO <proof_of_spec> element." >&2
            echo "  Andrew-direct 2026-08-11: no TO issues without a machine-readable data contract." >&2
            echo "  Fix: mint the criterion-id set per org/ref/TASK_ORDER_PROTOCOL.md <proof_of_spec>;" >&2
            echo "  contract schema: org/standards/PROOF_OF_SPEC.schema.json; validator: .tools/proof-of-spec-check.py" >&2
            echo "  Audited override (edge cases only): TO_POS_OVERRIDE=\"<reason>\" git commit ..." >&2
            blocked=1
        fi
    fi

    base="${f##*/}"
    code="${base%%.*}"
    pj="$root/org/projects/${code}.json"
    if [ -f "$pj" ] && grep -q '"dep_stage"' "$pj" 2>/dev/null; then
        if ! printf '%s\n' "$content" | grep -q '<decomp_ref'; then
            if [ -n "${TO_DECOMP_OVERRIDE:-}" ]; then
                printf '%s | %s | %s | DECOMP: %s\n' "$(date -u +%Y-%m-%dT%H%M%SZ)" \
                    "$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//')" "$f" "$TO_DECOMP_OVERRIDE" \
                    >> "$root/org/to-pos-override-audit.log"
                echo "WARN: TO_DECOMP_OVERRIDE -- $f issued WITHOUT <decomp_ref> on pipeline project $code (audited: $TO_DECOMP_OVERRIDE)" >&2
            else
                echo "BLOCKED: NEW task order '$f' -- project $code is PIPELINE-REGISTERED (dep_stage in its JSON) and the TO carries NO <decomp_ref>." >&2
                echo "  Rule 27 layer 2 (ratified 2026-08-21, org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md item 2):" >&2
                echo "  a pipeline project's TO cites the decomp run it executes -- decomp before TOs." >&2
                echo "  Fix: add <decomp_ref> naming the decomp run (workflows/atom_decomposition/runs/...)." >&2
                echo "  Audited override (edge cases only): TO_DECOMP_OVERRIDE=\"<reason>\" git commit ..." >&2
                blocked=1
            fi
        fi
    fi
done <<EOF_LIST
$added
EOF_LIST

exit $blocked
