#!/usr/bin/env bash
# NFRA_COMPPROOF B FIX-2 -- TRUE-SANDBOX filtered-repo TEMPLATE builder (CTO ruling 154055Z).
#
# WHY: the old model retained FULL substrate file-access + relied on a POST-HOC tool-log audit
# (harness.cheat_check) to VOID a forbidden read. MSTR found that is detection-not-prevention +
# the answer-key (corpus.py) sat in the allowed org/modules/graph tree. CTO ruled TRUE-SANDBOX:
# the solver runs inside a FILTERED REPO COPY where the forbidden narrative/answer set PHYSICALLY
# DOES NOT EXIST -- so a broad `grep -r <symptom> .` finds nothing forbidden because nothing
# forbidden is there. cheat_check stays as belt-and-suspenders for any absolute-path read.
#
# HOW: `git archive` the tracked tree at HEAD (NO .git -> a solver can't git-show/history-recover a
# forbidden file) for BOTH the superproject AND the portal submodule (git archive does not recurse
# submodules), extract, then rm the forbidden set. Git Bash 3.6.7 default utils only (Rule 16: git,
# tar, rm, find, grep -- NO rsync/pgrep/flock). Build ONCE; spawn_solver.sh copies it per solver.
#
# Usage: build_sandbox.sh [TEMPLATE_DIR]   (default: a fresh mktemp -d)  ->  prints TEMPLATE path.
set -eu

WS="/c/Users/AndrewBerman/Desktop/ajb_workspace"
TEMPLATE="${1:-$(mktemp -d -t compproof_sandbox_XXXXXX)}"
mkdir -p "$TEMPLATE"

echo "SANDBOX: building filtered template at $TEMPLATE" >&2

# 1. export the tracked tree at HEAD (no .git). MODE selects the isolation model (CTO ruling pending
# on allowlist-vs-blocklist -- COO~B 174421Z routed it, leans allowlist):
#   blocklist (default, COO~B RE-VERIFY GREEN 99af83086): copy the WHOLE tree, then rm the forbidden
#             set in step 2 (location-agnostic + variant-aware + citation records).
#   allowlist (provably-complete): copy ONLY the allowed SOURCE substrate (AFFORDANCE_SPEC ALLOWED) ->
#             the forbidden narrative/answer set is absent BY CONSTRUCTION (never copied), not by
#             removal. Step 2 still scrubs the sub-forbidden WITHIN the allowed trees (the answer-key +
#             debtscan under org/modules/graph). Both modes share the same fail-closed step-3 verify.
# NOTE: git-bash tar cannot recreate committed venv symlinks (data/*/.venv, tools/analytics_venv,
# infra/.../cookie-env, research/.../venv -> /usr/bin/python3). Those are BUILD JUNK, not incident
# substrate -- extract TOLERANTLY (symlink failures non-fatal) then rm the venv-class dirs in step 2.
# A genuinely-broken extraction is caught fail-closed by the step-3 allowed-substrate-present verify.
# DEFAULT = allowlist (CTO ruling 175214Z: copy-ONLY-allowed is the provably-complete gate; docs
# DROPPED). blocklist stays available as a fallback mode (COMPPROOF_SANDBOX_MODE=blocklist).
MODE="${COMPPROOF_SANDBOX_MODE:-allowlist}"
echo "SANDBOX: mode=$MODE" >&2
set +e
if [ "$MODE" = "allowlist" ]; then
    # ALLOWED SOURCE: data/*/scripts, infra/, org/modules/graph (+ portal below). git pathspec globbing
    # is unreliable for data/*/scripts -> enumerate the data/<firm>/scripts dirs via ls-files+grep.
    DATA_SCRIPT_DIRS="$(cd "$WS" && git ls-files | grep -E '^data/[^/]+/scripts/' | awk -F/ '{print $1"/"$2"/scripts"}' | sort -u | tr '\n' ' ')"
    ( cd "$WS" && git archive --format=tar HEAD -- $DATA_SCRIPT_DIRS infra org/modules/graph ) | tar -x -C "$TEMPLATE" 2>/dev/null
else
    ( cd "$WS" && git archive --format=tar HEAD ) | tar -x -C "$TEMPLATE" 2>/dev/null
fi
# portal is a SUBMODULE (allowed SOURCE in BOTH modes) -- git archive of the superproject leaves it
# empty; archive it separately.
if [ -d "$WS/portal/.git" ] || [ -f "$WS/portal/.git" ]; then
    mkdir -p "$TEMPLATE/portal"
    ( cd "$WS/portal" && git archive --format=tar HEAD ) | tar -x -C "$TEMPLATE/portal" 2>/dev/null
fi
set -e

# 2. PHYSICALLY REMOVE the forbidden set. ABSOLUTE $TEMPLATE paths + `find "$TEMPLATE"` throughout --
# relative ops after a cd into a git-bash /tmp mount are UNRELIABLE (a nested relative `[ -e ]` returns
# false-absent), which silently no-op'd removals + made a leaking build PASS verify (COO~B 171554Z).
rm -rf "$TEMPLATE/memory" "$TEMPLATE/org/critical_paths" "$TEMPLATE/org/daily_log" \
       "$TEMPLATE/org/modules/graph/debtscan" "$TEMPLATE/org/modules/graph/compproof" 2>/dev/null || true
# org/XXX.md = fabric startup guide (a Vector-1 CONTEXT-INJECTION marker); the sandbox IS the solver cwd
# so it must carry NO injection marker (CLAUDE.md + memory/ already gone).
rm -f "$TEMPLATE/org/XXX.md" 2>/dev/null || true
find "$TEMPLATE" -type f -iname 'CLAUDE.md' -delete 2>/dev/null || true
find "$TEMPLATE" -type f -iname '*compiler-tools-log*' -delete 2>/dev/null || true
# EVERY narrative-container DIRECTORY, LOCATION-AGNOSTIC + NAME-VARIANT-aware. COO~B 171554Z: the
# org-scoping AND the single name 'logs' were the completeness bug -- a top-level logs/ (859 session-
# logs + postmortems) AND a session_logs/ variant leaked. None of these are allowed substrate (which is
# comp-tools / graph / live-estate / SOURCE only). Add a variant here if the audit ever surfaces one.
find "$TEMPLATE" -type d \( -name logs -o -name session_logs -o -name 'session-logs' -o -name sessions \
     -o -name threads -o -name handoffs -o -name daily_log -o -name change_management \
     -o -name 'change-management' \) -prune -exec rm -rf {} + 2>/dev/null || true
# EVERY *postmortem* ANYWHERE (documented incident resolutions), not just under docs/.
find "$TEMPLATE" -iname '*postmortem*' -prune -exec rm -rf {} + 2>/dev/null || true
# build junk: committed venv-class dirs (the broken symlinks that failed tar) -- not incident substrate
find "$TEMPLATE" -type d \( -name '.venv' -o -name 'venv' -o -name 'cookie-env' -o -name 'analytics_venv' \) \
     -prune -exec rm -rf {} + 2>/dev/null || true

# CORPUS-CITATION records: the DEFINITE per-incident answer record for each of the 20 corpus incidents
# (harness.resolution_artifacts). Categories above miss answer-records cited under otherwise-allowed
# trees -- e.g. docs/architecture/*_PRD.md, org/projects/*.json. Remove each cited path/file wherever
# it lives. corpus.py + harness live in the REAL ws (absent from the template by design) -- read there.
CITATIONS="$( cd "$WS" && python -c "
import sys; sys.path.insert(0,'org/modules/graph/compproof')
import corpus, harness
seen=set()
for inc in corpus.INCIDENTS:
    for a in harness.resolution_artifacts(inc):
        t=a.strip().split()[0] if a.strip() else ''
        if t and ('/' in t or t.endswith('.json') or t.endswith('.md')) and t not in seen:
            seen.add(t); print(t)
" 2>/tmp/cit_err.log | tr -d '\r' )"
echo "SANDBOX: citation records to remove: $(echo "$CITATIONS" | grep -c .)" >&2
# ABSOLUTE $TEMPLATE-prefixed paths -- relative `[ -e nested/path ]` after a cd into a git-bash /tmp
# mount is UNRELIABLE (returns false-absent for a present nested path), which silently skipped the
# removal AND made the verify falsely PASS a leaking build. `find`/absolute-`[ -e ]` are reliable.
for c in $CITATIONS; do
    if [ -e "$TEMPLATE/$c" ]; then rm -rf "$TEMPLATE/$c" 2>/dev/null || true
    elif [ "${c##*/}" = "$c" ]; then find "$TEMPLATE" -name "$c" -exec rm -rf {} + 2>/dev/null || true; fi
done

# BROAD answer-bearing narrative .md sweep, LOCATION-AGNOSTIC (COO~B 171554Z: remove ANY *.md
# documenting a resolution ANYWHERE -- not just org//docs/; the org-scoping was the bug). Names that
# denote an incident record / session narrative / reconciliation / handoff / retrospective / closeout /
# ledger. Errs toward REMOVAL: the solve reaches root cause via graph + comp-tools + SOURCE + live
# estate, NEVER a narrative doc, so losing these cannot cost the solver a legit path -- but leaving one
# could hand over an answer. (Blocklist cannot be PROVABLY complete for scattered narrative -- the
# allowlist model is the provable fix, flagged to CTO/COO in the RAVC.)
find "$TEMPLATE" -type f -name '*.md' \( \
    -iname '*incident*' -o -iname '*postmortem*' -o -iname '*retrospective*' -o -iname '*_retro*' \
    -o -iname '*reconciliation*' -o -iname '*_recon*' -o -iname '*session_log*' -o -iname '*session_summary*' \
    -o -iname '*_handoff*' -o -iname '*handoff_*' -o -iname '*closeout*' -o -iname '*close_out*' \
    -o -iname '*_ledger*' -o -iname '*ledger_*' \) -delete 2>/dev/null || true

# 3. VERIFY fail-closed: the forbidden NARRATIVE/ANSWER RECORDS are physically ABSENT, there is no
#    .git (history-recover vector), and the allowed substrate is PRESENT. NOTE: source content that
#    happens to mention a root cause is ALLOWED by the CTO clean-room boundary -- only the narrative/
#    answer RECORD FILES are forbidden, so we assert those files are gone (NOT that root-cause phrases
#    are absent from source, which would false-flag the very substrate the solver reasons from).
# ABSOLUTE $TEMPLATE paths + find only (NO cd + relative -- that was unreliable in a git-bash /tmp
# mount and is what let a leaking build PASS verify).
FAIL=0
for f in memory org/critical_paths org/daily_log CLAUDE.md org/XXX.md logs \
         org/modules/graph/debtscan org/modules/graph/compproof; do
    [ -e "$TEMPLATE/$f" ] && { echo "VERIFY-FAIL: forbidden present -> $f" >&2; FAIL=1; }
done
# LOCATION-AGNOSTIC completeness checks -- a future spec-miss FAILS the build. The org/docs-scoped
# verify was itself the bug that PASSED a leaking build (top-level logs/ leaked) -- COO~B 171554Z.
[ -n "$(find "$TEMPLATE" -type d \( -name logs -o -name session_logs -o -name 'session-logs' -o -name sessions -o -name threads -o -name handoffs -o -name daily_log -o -name change_management -o -name 'change-management' \) 2>/dev/null)" ] && { echo "VERIFY-FAIL: a narrative-container dir survives (logs/session_logs/sessions/threads/handoffs/daily_log/change_management)" >&2; FAIL=1; }
[ -n "$(find "$TEMPLATE" -iname '*postmortem*' 2>/dev/null)" ]         && { echo "VERIFY-FAIL: a postmortem survives (ANY location)" >&2; FAIL=1; }
# BACKSTOP: NO .md under ANY narrative path segment -- catches a dir-name variant the removal missed.
[ -n "$(find "$TEMPLATE" -name '*.md' \( -path '*/logs/*' -o -path '*/session_logs/*' -o -path '*/sessions/*' -o -path '*/threads/*' -o -path '*/handoffs/*' -o -path '*/daily_log/*' -o -path '*/change_management/*' -o -path '*/critical_paths/*' -o -path '*/debtscan/*' -o -path '*/memory/*' \) 2>/dev/null)" ] && { echo "VERIFY-FAIL: a narrative-path .md survives" >&2; FAIL=1; }
# every corpus incident's DEFINITE answer-record (citation) must be gone, wherever it lived
for c in $CITATIONS; do
    if [ -e "$TEMPLATE/$c" ]; then echo "VERIFY-FAIL: corpus citation-record present -> $c" >&2; FAIL=1
    elif [ "${c##*/}" = "$c" ] && [ -n "$(find "$TEMPLATE" -name "$c" 2>/dev/null)" ]; then echo "VERIFY-FAIL: corpus citation-file present -> $c" >&2; FAIL=1; fi
done
[ -n "$(find "$TEMPLATE" -iname 'CLAUDE.md' 2>/dev/null)" ]            && { echo "VERIFY-FAIL: a CLAUDE.md survives" >&2; FAIL=1; }
[ -n "$(find "$TEMPLATE" -iname '*compiler-tools-log*' 2>/dev/null)" ] && { echo "VERIFY-FAIL: a compiler-tools-log survives" >&2; FAIL=1; }
[ -e "$TEMPLATE/.git" ] && { echo "VERIFY-FAIL: .git present (would leak the forbidden set via history)" >&2; FAIL=1; }
for f in data/black_diamond/scripts/gold infra/aws/globgrph \
         org/modules/graph/comp_aws_cli.py portal/src; do
    [ -e "$TEMPLATE/$f" ] || { echo "VERIFY-FAIL: allowed substrate MISSING -> $f" >&2; FAIL=1; }
done
# GRAPH-COVERAGE GUARD (CTO 175214Z guard #1 -- LOAD-BEARING for allowlist): the allowlist must include
# EVERY source the GRAPH references, or a solver false-MISSes a reachable source -> B UNDER-scores. Assert
# every graph repo-source path ROOT (excluding M365 SharePoint nodes -- live-MCP, not repo files) is
# present, AND every repo data-firm-with-scripts is present (PipelineScript nodes map firm+name ->
# data/<firm>/scripts). comp-kuzu unreachable -> WARN (unverified); a GAP -> FAIL.
if [ "$MODE" = "allowlist" ]; then
    GROOTS="$(comp-kuzu "MATCH (n:CloudNode) WHERE (n.props CONTAINS 'path') AND NOT n.node_type IN ['MS_FILE','MS_FOLDER'] RETURN n.props" 2>/dev/null \
        | grep -oE '"path": *"[^"]+"' | sed -E 's/"path": *"//; s/"$//' | grep -E '/' | awk -F/ '{print $1}' | sort -u)"
    if [ -z "$GROOTS" ]; then
        echo "SANDBOX WARN: graph-coverage guard could not reach comp-kuzu -- coverage UNVERIFIED this build" >&2
    else
        for r in $GROOTS; do
            [ -d "$TEMPLATE/$r" ] || { echo "VERIFY-FAIL: graph references repo-source root '$r' NOT in allowlist (would false-MISS -> B under-scores)" >&2; FAIL=1; }
        done
    fi
    for d in $(cd "$WS" && git ls-files | grep -oE '^data/[^/]+/scripts' | sort -u); do
        [ -d "$TEMPLATE/$d" ] || { echo "VERIFY-FAIL: data-firm scripts '$d' MISSING from allowlist (graph PipelineScript would false-MISS)" >&2; FAIL=1; }
    done
fi
if [ "$FAIL" -ne 0 ]; then
    echo "SANDBOX VERIFY FAILED -- NOT emitting template path (fail-closed)." >&2
    exit 1
fi
echo "SANDBOX VERIFY PASS: forbidden records absent, no .git, allowed substrate present." >&2
echo "$TEMPLATE"
