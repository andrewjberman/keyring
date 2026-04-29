#!/usr/bin/env bash
# ADHC_COMPIL.004 — PRD Compiler Evidence linter
# Scans PRD files for:
#   - §5 Compiler Evidence header
#   - >= 1 comp-* tool citation in the body
# Warn-only: always exits 0. Never blocks commits.
# Usage:
#   prd-evidence-check.sh <file> [file ...]   -- check named PRD(s)
#   prd-evidence-check.sh --baseline          -- scan all docs/architecture/*.md, log to compiler-tools-log.md

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
COMPIL_LOG="$WORKSPACE_ROOT/org/compiler-tools-log.md"
PRD_DIR="$WORKSPACE_ROOT/docs/architecture"

COMP_TOOLS="comp-pipescript comp-blast comp-iam comp-routes comp-platinum comp-transform comp-validate comp-cache comp-pii comp-trace comp-build comp-diff comp-xref"

check_file() {
    local file="$1"
    local has_s5=0
    local has_comp=0
    local warns=()

    # Check for §5 Compiler Evidence header
    if grep -qiE "^##+ (§?5[. ]|Compiler Evidence)" "$file" 2>/dev/null; then
        has_s5=1
    fi

    # Check for >= 1 comp-* citation
    for tool in $COMP_TOOLS; do
        if grep -q "$tool" "$file" 2>/dev/null; then
            has_comp=1
            break
        fi
    done

    [ "$has_s5" -eq 0 ] && warns+=("missing-s5-header")
    [ "$has_comp" -eq 0 ] && warns+=("no-comp-tool-citation")

    if [ "${#warns[@]}" -eq 0 ]; then
        echo "PASS  $file"
        return 0
    else
        local warn_str
        warn_str=$(IFS=','; echo "${warns[*]}")
        echo "WARN  $file  [$warn_str]"
        return 1
    fi
}

run_baseline() {
    local ts
    ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local pass=0 warn=0 total=0
    local results=()

    while IFS= read -r -d '' f; do
        total=$((total + 1))
        local line
        line=$(check_file "$f") || true
        results+=("$line")
        if [[ "$line" == PASS* ]]; then
            pass=$((pass + 1))
        else
            warn=$((warn + 1))
        fi
    done < <(find "$PRD_DIR" -maxdepth 1 -name "*.md" -print0 | sort -z)

    echo ""
    echo "Baseline complete: $pass PASS / $warn WARN / $total total"

    # Append to compiler-tools-log.md
    {
        echo ""
        echo "## prd-evidence-check --baseline | $ts"
        echo ""
        echo "| Status | File | Notes |"
        echo "|--------|------|-------|"
        for r in "${results[@]}"; do
            local status="${r%% *}"
            local rest="${r#* }"
            local fname="${rest%%  *}"
            local note=""
            if [[ "$rest" == *"["* ]]; then
                note="${rest#*[}"
                note="${note%]}"
            fi
            echo "| $status | $(basename "$fname") | $note |"
        done
        echo ""
        echo "Total: $pass PASS, $warn WARN, $total PRDs scanned."
    } >> "$COMPIL_LOG"

    echo "Coverage report appended to $COMPIL_LOG"
}

# --- Main ---

if [ $# -eq 0 ]; then
    echo "Usage: prd-evidence-check.sh <file> [file ...]"
    echo "       prd-evidence-check.sh --baseline"
    exit 0
fi

if [ "$1" = "--baseline" ]; then
    run_baseline
    exit 0
fi

# Single/multi file mode
any_warn=0
for f in "$@"; do
    check_file "$f" || any_warn=1
done

# Always exit 0 per TO spec (warn-only)
exit 0
