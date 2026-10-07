#!/usr/bin/env bash
# halt-gate-worker-order-test.sh -- fixture for OG-hg-1 (CTO R35 cell 1).
# Proves halt_gate_worker_issuer (.tools/halt-gate-check.sh) (a) finds a worker's order in the SHARED root when the
# release tree it runs from predates that order, and (b) reads the LAST line-leading <status> tag of the order.
# Self-contained: two throwaway git repos in a temp directory (a shared root and a linked release worktree cut on an
# older commit), a fake issuer inbox, no network, no real inbox. One line per case: "PASS: case <n> ..." or
# "FAIL: case <n> ..."; exit 0 only when all four pass. HALT_GATE_LIB overrides the library under test (the negative
# control points it at the pre-change function). Git Bash default utilities only; ASCII only.

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIB="${HALT_GATE_LIB:-$HERE/halt-gate-check.sh}"
[ -f "$LIB" ] || { echo "FAIL: case 0 library not found: $LIB"; exit 1; }

T="$(mktemp -d)" || { echo "FAIL: case 0 mktemp failed"; exit 1; }
trap 'rm -rf "$T"' EXIT
SHARED="$T/shared"; REL="$T/release"
CODE="HGTEST"; WORKER="0.9.0_WK_${CODE}~7"; ISSUER="2.0.0_SA_COO~O"; IBASE="${ISSUER%%~*}"
ORDER="org/missions/D9/NFRA/${CODE}/task-orders/${CODE}.TO-x.md"
G=(git -c core.autocrlf=false -c user.name=fixture -c user.email=fixture@example.invalid)

mkdir -p "$SHARED" && "${G[@]}" -C "$SHARED" init -q || { echo "FAIL: case 0 git init"; exit 1; }
printf 'seed\n' > "$SHARED/seed.txt"
"${G[@]}" -C "$SHARED" add seed.txt && "${G[@]}" -C "$SHARED" commit -q -m seed || { echo "FAIL: case 0 seed commit"; exit 1; }
# The release tree: a linked worktree cut NOW, i.e. before any order exists in the shared root.
"${G[@]}" -C "$SHARED" worktree add -q -b rel "$REL" HEAD || { echo "FAIL: case 0 worktree add"; exit 1; }
mkdir -p "$SHARED/org/mcp/inbox/$IBASE/~O"   # untracked, as in the real shared checkout

# set_order <body-after-header>: commit a new version of the order in the SHARED root (never in the release tree).
set_order() {
  mkdir -p "$(dirname "$SHARED/$ORDER")"
  { printf '# fixture order\n<issued_to>%s</issued_to>\n<issued_by>%s</issued_by>\n' "$WORKER" "$ISSUER"; printf '%s\n' "$1"; } > "$SHARED/$ORDER"
  "${G[@]}" -C "$SHARED" add "$ORDER" && "${G[@]}" -C "$SHARED" commit -q -m "order" || return 1
}

# run_gate: run the gate from the release tree as the worker; prints rc, leaves stderr in $T/err.
run_gate() {
  ( unset CLAUDE_CODE_SESSION_ID HALT_OVERRIDE HALT_ACK HALT_GATE_SHARED_ROOT HALT_GATE_INBOX_ROOT
    export HALT_GATE_REPO_ROOT="$REL" OPAL_AGENT_SERIAL="$WORKER" HALT_GATE_AUDIT_LOG="$T/audit.log"
    . "$LIB"
    halt_gate_check "worker-order-test" ) 2> "$T/err" > "$T/out"
  echo $?
}

fails=0
verdict() { # <n> <ok 0/1> <pass text> <fail text>
  if [ "$2" = 0 ]; then echo "PASS: case $1 $3"; else echo "FAIL: case $1 $4"; fails=$((fails + 1)); fi
}

# case 1: release tree predates the order; order non-terminal in the shared root -> admit, issuer named.
set_order '<status>pending</status>' || { echo "FAIL: case 1 fixture commit"; exit 1; }
rc="$(run_gate)"
if [ "$rc" = 0 ] && grep -q "scanning its issuer $ISSUER" "$T/err"; then
  verdict 1 0 "release tree predates the order; shared-root order admitted, issuer $ISSUER named" ""
else
  verdict 1 1 "" "gate rc=$rc, expected 0 with the issuer named (release tree predates the order)"
fi

# case 2: first tag staged, LAST tag complete -> not admitted.
# The release tree carries the SAME order (cut after its first flip), so a first-tag reader sees 'staged' and admits.
body2="$(printf '<status>staged</status>\nbody\n<status>complete</status>')"
set_order "$body2" || { echo "FAIL: case 2 fixture commit"; exit 1; }
mkdir -p "$(dirname "$REL/$ORDER")"
{ printf '# fixture order\n<issued_to>%s</issued_to>\n<issued_by>%s</issued_by>\n' "$WORKER" "$ISSUER"; printf '%s\n' "$body2"; } > "$REL/$ORDER"
"${G[@]}" -C "$REL" add "$ORDER" && "${G[@]}" -C "$REL" commit -q -m "release order copy" || { echo "FAIL: case 2 release commit"; exit 1; }
rc="$(run_gate)"
if [ "$rc" != 0 ] && ! grep -q 'scanning its issuer' "$T/err"; then
  verdict 2 0 "LAST tag complete (earlier tag staged) is not admitted (rc=$rc)" ""
else
  verdict 2 1 "" "gate rc=$rc, expected a refusal for an order whose last tag is complete"
fi

# case 3: first tag complete, LAST tag pending (plus a mid-line quoted tag in prose) -> admitted.
set_order "$(printf '<status>complete</status>\nbody\n<status>pending</status>\nprose: flip the <status>complete</status> tag later')" || { echo "FAIL: case 3 fixture commit"; exit 1; }
rc="$(run_gate)"
if [ "$rc" = 0 ] && grep -q "scanning its issuer $ISSUER" "$T/err"; then
  verdict 3 0 "first tag complete, LAST tag pending is admitted" ""
else
  verdict 3 1 "" "gate rc=$rc, expected 0 with the issuer named (last tag pending)"
fi

# case 4 (case 1's order restored): a [STOP] to the issuer still halts, no override.
set_order '<status>pending</status>' || { echo "FAIL: case 4 fixture commit"; exit 1; }
printf '# Message from 1.0.0_SA_CTO\n**To:** %s\n**Subject:** [STOP] fixture stop\n\nbody\n' "$ISSUER" > "$SHARED/org/mcp/inbox/$IBASE/~O/stop.md"
rc4="$(run_gate)"
if [ "$rc4" = 2 ] && grep -q 'STOP-CLASS MESSAGE -- HARD BLOCK' "$T/err"; then
  verdict 4 0 "a [STOP] to the issuer halts the worker (rc=2, no override)" ""
else
  verdict 4 1 "" "gate rc=$rc4, expected 2 with a STOP hard block"
fi
rm -f "$SHARED/org/mcp/inbox/$IBASE/~O/stop.md"

[ "$fails" = 0 ]
