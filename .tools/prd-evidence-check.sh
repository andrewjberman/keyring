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
    # Delegate to python3 for baseline scan — avoids per-grep process overhead on Windows
    # (165 files × grep calls via bash subshells is prohibitively slow on Windows Git Bash)
    if command -v python3 >/dev/null 2>&1; then
        python3 - "$PRD_DIR" "$COMPIL_LOG" << 'PYEOF'
import os, re, sys
from datetime import datetime, timezone

arch_dir, log_file = sys.argv[1], sys.argv[2]
s5_re = re.compile(r'^#{1,3}\s*(§5|5[. )—]|Compiler Evidence)', re.IGNORECASE | re.MULTILINE)
comp_re = re.compile(r'\bcomp-(pipescript|blast|iam|routes|platinum|transform|validate|cache|pii|trace|build|diff|xref|freshness|constants|shell)\b')

results = []
pass_n = warn_n = 0
for fname in sorted(os.listdir(arch_dir)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(arch_dir, fname)
    try:
        text = open(fpath, encoding='utf-8', errors='replace').read()
    except Exception:
        continue
    warns = []
    if not s5_re.search(text):
        warns.append('missing-s5-header')
    if not comp_re.search(text):
        warns.append('no-comp-tool-citation')
    status = 'PASS' if not warns else 'WARN'
    results.append((status, fname, ','.join(warns)))
    if status == 'PASS': pass_n += 1
    else: warn_n += 1

ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
total = len(results)
print(f'\nBaseline complete: {pass_n} PASS / {warn_n} WARN / {total} total')
with open(log_file, 'a', encoding='utf-8') as f:
    f.write(f'\n## prd-evidence-check --baseline | {ts}\n\n')
    f.write('| Status | File | Notes |\n|--------|------|-------|\n')
    for s, fn, note in results:
        f.write(f'| {s} | {fn} | {note} |\n')
    f.write(f'\nTotal: {pass_n} PASS, {warn_n} WARN, {total} PRDs scanned.\n')
print(f'Coverage report appended to {log_file}')
PYEOF
        return
    fi

    # Fallback: pure bash (slow on Windows; fast on Linux/Mac EC2)
    local ts pass=0 warn=0 total=0
    ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local tmp_rows
    tmp_rows=$(mktemp)
    while IFS= read -r f; do
        total=$((total + 1))
        local has_s5=0 has_comp=0 warns="" status="PASS"
        grep -qiE "^#{1,3} *(§?5[. )—]|Compiler Evidence)" "$f" 2>/dev/null && has_s5=1
        for tool in $COMP_TOOLS; do
            if grep -q "$tool" "$f" 2>/dev/null; then has_comp=1; break; fi
        done
        [ "$has_s5" -eq 0 ] && warns="missing-s5-header"
        if [ "$has_comp" -eq 0 ]; then
            [ -n "$warns" ] && warns="$warns,no-comp-tool-citation" || warns="no-comp-tool-citation"
        fi
        [ -n "$warns" ] && status="WARN"
        echo "| $status | $(basename "$f") | $warns |" >> "$tmp_rows"
        if [ "$status" = "PASS" ]; then pass=$((pass + 1)); else warn=$((warn + 1)); fi
    done < <(find "$PRD_DIR" -maxdepth 1 -name "*.md" | sort)
    echo ""
    echo "Baseline complete: $pass PASS / $warn WARN / $total total"
    { echo ""; echo "## prd-evidence-check --baseline | $ts"; echo ""; echo "| Status | File | Notes |"; echo "|--------|------|-------|"; cat "$tmp_rows"; echo ""; echo "Total: $pass PASS, $warn WARN, $total PRDs scanned."; } >> "$COMPIL_LOG"
    rm -f "$tmp_rows"
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
