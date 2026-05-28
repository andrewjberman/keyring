#!/usr/bin/env bash
# =============================================================================
# halt-gate-ld0131-test.sh -- LD-0131 Layer-1 recipient-scoping integration test
# =============================================================================
# Three end-to-end scenarios (CVO-spec'd) exercising halt_gate_main exit codes:
#   Scenario 1: only foreign ferry (To: RD~B) in inbox  -> exit 0 (gate passes)
#   Scenario 2: foreign ferry + same-serial [STOP]       -> exit 2 (hard block)
#   Scenario 3: foreign ferry + routine same-serial msg  -> exit 1 (surfaced, unacked)
#
# Uses HALT_GATE_INBOX_ROOT + HALT_GATE_CONTEXT_FILE overrides to test against
# a controlled temp inbox rather than the live agent inbox.
#
# Usage:  bash .tools/halt-gate-ld0131-test.sh
# Exit 0: all 3 scenarios passed
# Exit 1: at least one scenario failed
# =============================================================================
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HALT_GATE="$REPO_ROOT/.tools/halt-gate-check.sh"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

TEST_SERIAL="0.7.0_AE_CloudOps"
CTX_FILE="$TMP/agent_context"
INBOX_ROOT="$TMP/inbox"
mkdir -p "$INBOX_ROOT/$TEST_SERIAL"

printf "SERIAL=%s\nTO_ID=\n" "$TEST_SERIAL" > "$CTX_FILE"

PASS=0
FAIL=0

assert_exit() {
  local label="$1" got="$2" want="$3"
  if [ "$got" = "$want" ]; then
    echo "  PASS: $label (exit $got)"
    PASS=$((PASS + 1))
  else
    echo "  FAIL: $label -- got exit $got, want exit $want"
    FAIL=$((FAIL + 1))
  fi
}

# Helper: write a message file to the test inbox
write_msg() {
  local fname="$1" to="$2" subject="$3" body="$4"
  cat > "$INBOX_ROOT/$TEST_SERIAL/$fname" << EOF
# Message from 2.0.0_SA_COO
**To:** $to
**Date:** 20260528T220000Z
**Subject:** $subject

$body
EOF
}

run_gate() {
  CLAUDE_CODE_SESSION_ID="" \
  HALT_GATE_INBOX_ROOT="$INBOX_ROOT" \
  HALT_GATE_CONTEXT_FILE="$CTX_FILE" \
  bash "$HALT_GATE" 2>/dev/null
  echo $?
}

# ===========================================================================
# Scenario 1: only a foreign ferry in inbox (To: RD~B)
# Expected: ferry is skipped -> inbox effectively empty -> exit 0 (gate passes)
# ===========================================================================
rm -f "$INBOX_ROOT/$TEST_SERIAL"/*.md
write_msg "ferry_rdb.md" "0.4.2_RD_AdvisorIntelligence~B" \
  "[STOP] MDPF S1 GO for RD~B" \
  "Ferry copy. Intended for RD~B; AE gate must not trip on this."

echo ""
echo "=== Scenario 1: only foreign ferry (To: RD~B) in inbox -> exit 0 ==="
got1=$(run_gate)
assert_exit "foreign ferry alone is skipped, gate passes" "$got1" "0"

# ===========================================================================
# Scenario 2: foreign ferry + genuine same-serial [STOP]
# Expected: ferry skipped, STOP found -> exit 2 (hard block)
# ===========================================================================
write_msg "same_serial_stop.md" "$TEST_SERIAL" \
  "[STOP] deploy blocked" \
  "Real STOP message addressed to this agent. Must trip the gate."

echo ""
echo "=== Scenario 2: foreign ferry + same-serial [STOP] -> exit 2 ==="
got2=$(run_gate)
assert_exit "ferry skipped, real STOP hard-blocks" "$got2" "2"

# ===========================================================================
# Scenario 3: foreign ferry + routine same-serial message (no [STOP])
# Expected: ferry skipped, routine message surfaces -> exit 1
# ===========================================================================
rm -f "$INBOX_ROOT/$TEST_SERIAL/same_serial_stop.md"
write_msg "same_serial_routine.md" "$TEST_SERIAL" \
  "DRIVE: F3 Phase-1 in progress" \
  "Routine status message addressed to this agent. Not STOP-class."

echo ""
echo "=== Scenario 3: foreign ferry + routine same-serial msg -> exit 1 ==="
got3=$(run_gate)
assert_exit "ferry skipped, routine message surfaced as unacked" "$got3" "1"

# ===========================================================================
# Summary
# ===========================================================================
echo ""
echo "=== RESULTS: $PASS PASS, $FAIL FAIL ==="
[ "$FAIL" -eq 0 ] && { echo "ALL PASS"; exit 0; } || { echo "FAILURES DETECTED"; exit 1; }
