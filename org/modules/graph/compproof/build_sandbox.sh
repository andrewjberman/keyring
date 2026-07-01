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

# 1. export the tracked tree at HEAD (no .git). Superproject first.
# NOTE: git-bash tar cannot recreate committed venv symlinks (data/*/.venv, tools/analytics_venv,
# infra/.../cookie-env, research/.../venv -> /usr/bin/python3). Those are BUILD JUNK, not incident
# substrate -- extract TOLERANTLY (symlink failures non-fatal) then rm the venv-class dirs in step 2.
# A genuinely-broken extraction is caught fail-closed by the step-3 allowed-substrate-present verify.
set +e
( cd "$WS" && git archive --format=tar HEAD ) | tar -x -C "$TEMPLATE" 2>/dev/null
# portal is a SUBMODULE -- git archive of the superproject leaves it empty; archive it separately.
if [ -d "$WS/portal/.git" ] || [ -f "$WS/portal/.git" ]; then
    mkdir -p "$TEMPLATE/portal"
    ( cd "$WS/portal" && git archive --format=tar HEAD ) | tar -x -C "$TEMPLATE/portal" 2>/dev/null
fi
set -e

# 2. PHYSICALLY REMOVE the forbidden set (must match harness._is_forbidden_path / AFFORDANCE_SPEC).
cd "$TEMPLATE"
rm -rf memory org/critical_paths org/daily_log \
       org/modules/graph/debtscan org/modules/graph/compproof 2>/dev/null || true
# org/XXX.md is the fabric startup guide -- a Vector-1 CONTEXT-INJECTION marker (harness
# _FABRIC_INJECTION_MARKERS). Since the sandbox IS the solver's cwd, it must carry NO injection marker
# (CLAUDE.md + memory/ are already gone) so assert_clean_context passes. Not an answer, but fabric-orienting.
rm -f org/XXX.md 2>/dev/null || true
# session logs: org/**/logs/**  (org/tier*/*/logs, etc.)
find org -type d -name logs -prune -exec rm -rf {} + 2>/dev/null || true
# CLAUDE.md anywhere (incident-prose / NEVER-history) + any running compiler-tools-log
find . -type f -iname 'CLAUDE.md' -delete 2>/dev/null || true
find . -type f -iname '*compiler-tools-log*' -delete 2>/dev/null || true
# postmortem docs under docs/ (files or dirs; arch/PRD docs stay)
find docs -iname '*postmortem*' -prune -exec rm -rf {} + 2>/dev/null || true
# build junk: committed venv-class dirs (the broken symlinks that failed tar) -- not incident substrate
find . -type d \( -name '.venv' -o -name 'venv' -o -name 'cookie-env' -o -name 'analytics_venv' \) \
     -prune -exec rm -rf {} + 2>/dev/null || true

# 3. VERIFY fail-closed: the forbidden NARRATIVE/ANSWER RECORDS are physically ABSENT, there is no
#    .git (history-recover vector), and the allowed substrate is PRESENT. NOTE: source content that
#    happens to mention a root cause is ALLOWED by the CTO clean-room boundary -- only the narrative/
#    answer RECORD FILES are forbidden, so we assert those files are gone (NOT that root-cause phrases
#    are absent from source, which would false-flag the very substrate the solver reasons from).
cd "$TEMPLATE"
FAIL=0
for f in memory org/critical_paths org/daily_log CLAUDE.md org/XXX.md \
         org/modules/graph/debtscan org/modules/graph/compproof; do
    [ -e "$f" ] && { echo "VERIFY-FAIL: forbidden present -> $f" >&2; FAIL=1; }
done
[ -n "$(find org -type d -name logs 2>/dev/null)" ]         && { echo "VERIFY-FAIL: org/**/logs survive" >&2; FAIL=1; }
[ -n "$(find . -iname 'CLAUDE.md' 2>/dev/null)" ]            && { echo "VERIFY-FAIL: a CLAUDE.md survives" >&2; FAIL=1; }
[ -n "$(find docs -iname '*postmortem*' 2>/dev/null)" ]      && { echo "VERIFY-FAIL: a postmortem survives" >&2; FAIL=1; }
[ -n "$(find . -iname '*compiler-tools-log*' 2>/dev/null)" ] && { echo "VERIFY-FAIL: a compiler-tools-log survives" >&2; FAIL=1; }
[ -e ".git" ] && { echo "VERIFY-FAIL: .git present (would leak the forbidden set via history)" >&2; FAIL=1; }
for f in data/black_diamond/scripts/gold infra/aws/globgrph \
         org/modules/graph/comp_aws_cli.py portal/src; do
    [ -e "$f" ] || { echo "VERIFY-FAIL: allowed substrate MISSING -> $f" >&2; FAIL=1; }
done
if [ "$FAIL" -ne 0 ]; then
    echo "SANDBOX VERIFY FAILED -- NOT emitting template path (fail-closed)." >&2
    exit 1
fi
echo "SANDBOX VERIFY PASS: forbidden records absent, no .git, allowed substrate present." >&2
echo "$TEMPLATE"
