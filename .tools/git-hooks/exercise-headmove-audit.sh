#!/usr/bin/env bash
# Exercise of headmove-guard.sh's audit-log resolution when its functions are defined from a file that is NOT in the
# workspace (the agent harness's shell-snapshot shape), row NFRA_OPLGTW-Z-W28-S16.
# usage: bash hm_exercise.sh <abs path to headmove-guard.sh> <abs workspace root> <abs linked worktree>
set -u
SRC="$1"; WS="$2"; WT="$3"
T="$(mktemp -d)"; cp "$SRC" "$T/snapshot-like.sh"
unset HEADMOVE_WS HEADMOVE_AUDIT_LOG
# shellcheck disable=SC1090
. "$T/snapshot-like.sh"
pass=0; n=0
ok() { n=$((n+1)); if [ "$2" = "$3" ]; then pass=$((pass+1)); echo "  PASS  $1"; else echo "  FAIL  $1 (got '$2', want '$3')"; fi; }

echo "A. shared tree, functions defined from outside the workspace"
cd "$WS" || exit 2
HEADMOVE_AUDIT_LOG="$T/a.log" __headmove_audit "TEST-PROBE" "a" 2> "$T/a.err"; ok "rc 0" "$?" "0"
ok "one line written" "$(wc -l < "$T/a.log" 2>/dev/null | tr -d ' ')" "1"
ok "no NOT RECORDED warning" "$(grep -c 'NOT RECORDED' "$T/a.err")" "0"

echo "B. linked worktree, functions defined from outside the workspace"
cd "$WT" || exit 2
HEADMOVE_AUDIT_LOG="$T/b.log" __headmove_audit "TEST-PROBE" "b" 2> "$T/b.err"; ok "rc 0" "$?" "0"
ok "one line written" "$(wc -l < "$T/b.log" 2>/dev/null | tr -d ' ')" "1"
ok "the line names the worktree as the repo" "$(grep -c '\[repo: ' "$T/b.log")" "1"

echo "C. a foreign repo: the record cannot be written, so a forced destructive reset is REFUSED"
F="$T/foreign"; mkdir "$F"; cd "$F" || exit 2
command git init -q -b main .; command git config user.name t; command git config user.email t@t
echo 1 > f; command git add f; command git commit -q -m one; echo 2 > f; command git commit -q -a -m two
H="$(command git rev-parse HEAD)"
__headmove_audit "TEST-PROBE" "c" 2> "$T/c.err"; ok "audit rc 3 when unresolvable" "$?" "3"
FORCE_HEADMOVE=1 __headmove_guard reset --hard HEAD~1 2> "$T/c2.err"; ok "forced reset refused (rc 1)" "$?" "1"
ok "says the record could not be written" "$(grep -c 'audit record could not be written' "$T/c2.err")" "1"
ok "does not claim it was logged" "$(grep -c 'ALLOWED via FORCE_HEADMOVE' "$T/c2.err")" "0"
ok "HEAD unmoved by the guard call" "$(command git rev-parse HEAD)" "$H"
__headmove_guard reset --hard HEAD~1 2> "$T/c3.err"; ok "unforced reset still blocked (rc 1)" "$?" "1"
__headmove_guard reset --soft HEAD 2> /dev/null; ok "a non-destructive reset is allowed (rc 0)" "$?" "0"

echo "D. the same foreign repo WITH HEADMOVE_WS set: recorded, and the forced move is allowed"
HEADMOVE_WS="$WS" HEADMOVE_AUDIT_LOG="$T/d.log" FORCE_HEADMOVE=1 __headmove_guard reset --hard HEAD~1 2> "$T/d.err"; ok "rc 0" "$?" "0"
ok "FORCE-HEADMOVE line written" "$(grep -c 'FORCE-HEADMOVE' "$T/d.log" 2>/dev/null)" "1"

echo "DENOMINATOR: $pass of $n arm(s) passed"
cd / ; [ "$pass" -eq "$n" ] && echo PASS || { echo "outputs kept at $T"; exit 1; }
