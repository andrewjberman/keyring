#!/usr/bin/env bash
# MX-x-4 (b), row Z-W21-S21: halt_gate_resolve_serial() in a worktree that SHARES its issuer's CLAUDE_CODE_SESSION_ID.
# Offline, temp dirs, fake session files. Exits 0 only when all three arms hold:
#   ARM 1  a worktree declaring its own serial (OPAL_AGENT_SERIAL in env, or its own sessions/<sid>.serial) -> its own
#   ARM 2  the issuer's tree (no env declaration)                                                           -> the issuer
#   ARM 3  a tree declaring nothing                                                -> the shared root's serial, as before
# CONTROL  the pre-change halt-gate-check.sh (git HEAD of this file's parent commit) resolves ARM 1's env declaration to
#          the ISSUER -- the defect; reported, and graded only when git can print that version.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GATE="$HERE/../halt-gate-check.sh"
[ -f "$GATE" ] || { echo "FAIL: $GATE absent"; exit 1; }

T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
SID="sess-mx-x-4-shared"
ISSUER="0.0.0_TEST_ISSUER"; WORKER="0.9.0_WK_TEST~7"
SHARED="$T/shared"; WT="$T/wt"; WT_BARE="$T/wt_bare"
for d in "$SHARED" "$WT" "$WT_BARE"; do mkdir -p "$d/org/mcp/sessions"; done
printf '%s\n' "$ISSUER" > "$SHARED/org/mcp/sessions/$SID.serial"     # the shared session id resolves to the issuer
printf '%s\r\n' "$WORKER" > "$WT/org/mcp/sessions/$SID.serial"       # worktree declaring its own (CRLF on purpose)

fails=0
# resolve <gate-file> <repo_root> <shared_root> <env-serial-or-empty>
resolve() {
  local gate="$1" rr="$2" sr="$3" es="$4"
  if [ -n "$es" ]; then
    ( export CLAUDE_CODE_SESSION_ID="$SID" HALT_GATE_REPO_ROOT="$rr" HALT_GATE_SHARED_ROOT="$sr" OPAL_AGENT_SERIAL="$es"
      . "$gate" >/dev/null 2>&1; halt_gate_resolve_serial 2>/dev/null | tr -d '\r' )
  else
    ( unset OPAL_AGENT_SERIAL; export CLAUDE_CODE_SESSION_ID="$SID" HALT_GATE_REPO_ROOT="$rr" HALT_GATE_SHARED_ROOT="$sr"
      . "$gate" >/dev/null 2>&1; halt_gate_resolve_serial 2>/dev/null | tr -d '\r' )
  fi
}
check() {  # check <label> <got> <want>
  if [ "$2" = "$3" ]; then echo "PASS: $1 -> '$2'"; else echo "FAIL: $1 -> got '$2' want '$3'"; fails=$((fails+1)); fi
}

echo "--- ARM 1: a worktree declaring its own serial resolves to its own"
check "1a worktree's own sessions/<sid>.serial, no env" "$(resolve "$GATE" "$WT" "$SHARED" "")" "$WORKER"
check "1b OPAL_AGENT_SERIAL in env, worktree has no file" "$(resolve "$GATE" "$WT_BARE" "$SHARED" "$WORKER")" "$WORKER"
check "1c both declared: the worktree's own file precedes env (and both precede the shared root)" "$(resolve "$GATE" "$WT" "$SHARED" "0.9.0_WK_TEST~8")" "$WORKER"

echo "--- ARM 2: the issuer's tree resolves to the issuer"
check "2a issuer tree (repo root == shared root), no env" "$(resolve "$GATE" "$SHARED" "$SHARED" "")" "$ISSUER"
check "2b issuer tree with the issuer's own env" "$(resolve "$GATE" "$SHARED" "$SHARED" "$ISSUER")" "$ISSUER"

echo "--- ARM 3: a tree declaring nothing resolves through the shared root, as before"
check "3a no env, no own file -> shared root" "$(resolve "$GATE" "$WT_BARE" "$SHARED" "")" "$ISSUER"

echo "--- CONTROL: the pre-change gate resolves ARM 1b to the ISSUER (the defect this repairs)"
OLD="$T/old-halt-gate-check.sh"
if git -C "$HERE" show "HEAD:.tools/halt-gate-check.sh" > "$OLD" 2>/dev/null && [ -s "$OLD" ] \
   && ! grep -q 'MX-x-4' "$OLD"; then
  check "control: pre-change gate, env declared, no own file" "$(resolve "$OLD" "$WT_BARE" "$SHARED" "$WORKER")" "$ISSUER"
else
  echo "SKIP: control -- HEAD's halt-gate-check.sh is already the changed one or git cannot print it (reason printed; not graded)"
fi

if [ "$fails" -eq 0 ]; then echo "RESULT: three arms pass (own serial / issuer serial / shared-root fallback)"; exit 0; fi
echo "RESULT: $fails check(s) FAILED"; exit 1
