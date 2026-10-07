#!/usr/bin/env bash
# halt-gate-lane-test.sh -- falsifier for halt_gate_validate_serial's lane rule (.tools/halt-gate-check.sh).
# CTO ruling org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_HALT_GATE_MULTI_LETTER_LANE_20261007.md, row
# NFRA_CTLPLN-Z-S1: check (2) is an EXISTENCE check (uppercase letters only AND the lane's nested inbox exists), and
# the refusal banner names the failed check and never prescribes rewriting the session serial file.
# Runs in a throwaway fixture; touches no real inbox and no session file. HALT_GATE_LIB overrides the library under
# test (the negative control: point it at a pre-fix copy and cases 1 and 3 or the banner cases must FAIL).
# Prints one line per case and the count; exit 0 only when every case passes.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIB="${HALT_GATE_LIB:-$HERE/halt-gate-check.sh}"
T="$(mktemp -d -t halt-gate-lane-XXXXXX)"
trap 'rm -rf "$T"' EXIT
mkdir -p "$T/org/tier2_senior/0.7.0_AE_CloudOps" "$T/org/tier0_exec/0.0.0_AB_MSTR" \
         "$T/org/mcp/inbox/0.7.0_AE_CloudOps/~RV" "$T/org/mcp/inbox/0.7.0_AE_CloudOps/~A" \
         "$T/org/mcp/inbox/0.0.0_AB_MSTR/~Z" "$T/org/mcp/inbox/0.0.0_AB_MSTR/~DELL2"          "$T/org/mcp/inbox/0.7.0_AE_CloudOps/~K2" "$T/org/mcp/sessions"

pass=0; n=0
# validate <serial> -> prints "<rc> <reason>"
validate() {
  ( unset CLAUDE_CODE_SESSION_ID HALT_OVERRIDE HALT_ACK
    export HALT_GATE_REPO_ROOT="$T" HALT_GATE_SHARED_ROOT="$T" HALT_GATE_INBOX_ROOT="$T/org/mcp/inbox"
    # shellcheck disable=SC1090
    . "$LIB"
    halt_gate_validate_serial "$1"; rc=$?
    printf '%s %s\n' "$rc" "${HALT_GATE_VALIDATE_REASON:-}" )
}
case_v() { # <name> <serial> <want_rc> <want_reason>
  n=$((n+1)); local got; got="$(validate "$2" 2>/dev/null)"
  if [ "$got" = "$3 $4" ]; then pass=$((pass+1)); echo "PASS: case $n $1 ($2 -> rc $3 ${4:-admitted})"
  else echo "FAIL: case $n $1 ($2): got '$got', wanted '$3 $4'"; fi
}
case_v "a multi-letter lane with an inbox resolves"          "0.7.0_AE_CloudOps~RV" 0 ""
case_v "the corruption shape is refused as malformed"        "0.0.0_AB_MSTR~Zn"     1 "malformed-lane"
case_v "an uppercase lane nobody seated is refused"          "0.7.0_AE_CloudOps~QQ" 1 "lane-no-inbox"
case_v "a Dell lane with a box digit resolves"             "0.7.0_AE_CloudOps~K2" 0 ""
case_v "a Dell fabric-manager lane resolves"               "0.0.0_AB_MSTR~DELL2"  0 ""
case_v "a digit-led lane is refused as malformed"          "0.7.0_AE_CloudOps~2K" 1 "malformed-lane"
case_v "a digit lane nobody seated is refused"             "0.7.0_AE_CloudOps~Q9" 1 "lane-no-inbox"
case_v "a single-letter lane behaves as before"              "0.7.0_AE_CloudOps~A"  0 ""
case_v "a base serial behaves as before"                     "0.7.0_AE_CloudOps"    0 ""
case_v "an unknown base is refused and named"                "9.9.9_XX_Nobody~A"    1 "unknown-base"
case_v "a worker with no order is refused as before"         "0.9.0_WK_NOPROJECT~7" 1 "worker-no-order"

# Banner: the full check on the corruption shape exits 3, names the failed check, and prints no line that writes a
# serial file.
banner="$( ( unset CLAUDE_CODE_SESSION_ID HALT_OVERRIDE HALT_ACK
             export HALT_GATE_REPO_ROOT="$T" HALT_GATE_SHARED_ROOT="$T" HALT_GATE_INBOX_ROOT="$T/org/mcp/inbox"
             export OPAL_AGENT_SERIAL="0.0.0_AB_MSTR~Zn" HALT_GATE_AUDIT_LOG="$T/audit.log"
             . "$LIB"; halt_gate_check; echo "RC=$?" ) 2>&1 )"
n=$((n+1)); if printf '%s\n' "$banner" | grep -q '^RC=3$' && printf '%s\n' "$banner" | grep -q 'Check that failed: malformed-lane'; then
  pass=$((pass+1)); echo "PASS: case $n the banner exits 3 and names the failed check"
else echo "FAIL: case $n the banner did not exit 3 naming malformed-lane"; printf '%s\n' "$banner" | sed 's/^/      /' | head -12; fi
n=$((n+1)); if printf '%s\n' "$banner" | grep -q 'sessions/.*\.serial"$'; then
  echo "FAIL: case $n the banner still prints a line that overwrites the session serial file"
else pass=$((pass+1)); echo "PASS: case $n the banner prints no line that overwrites the session serial file"; fi
n=$((n+1)); if printf '%s\n' "$banner" | grep -q 'NEVER write a different serial'; then
  pass=$((pass+1)); echo "PASS: case $n the banner forbids writing a different serial"
else echo "FAIL: case $n the banner lacks the never-rewrite remedy"; fi

echo "DENOMINATOR: $pass of $n case(s) passed"
[ "$pass" -eq "$n" ]
