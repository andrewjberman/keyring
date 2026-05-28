#!/usr/bin/env bash
# =============================================================================
# halt-gate-ld0131-test.sh -- LD-0131 Layer-1 recipient-scoping unit test
# =============================================================================
# Two cases per CTO/COO spec:
#   Case A: message addressed to the running serial --> included --> TRIPS gate
#   Case B: ferry copy addressed to a foreign tilde-lane --> SKIPPED --> PASSES
#
# Sources halt-gate-check.sh as a library (the file has a BASH_SOURCE guard so
# sourcing does not execute halt_gate_main). Exercises halt_gate_recipient() and
# the base-strip scoping logic directly on controlled message fixtures.
#
# Usage:  bash org/tier0/audit/halt-gate-ld0131-test.sh
# Exit 0: all assertions PASS
# Exit 1: at least one assertion FAIL
# =============================================================================
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

# Source the library (main guard prevents execution)
# shellcheck source=../../../.tools/halt-gate-check.sh
. "$REPO_ROOT/.tools/halt-gate-check.sh"

RUNNING_SERIAL="0.7.0_AE_CloudOps"
RUNNING_BASE="${RUNNING_SERIAL%%~*}"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

PASS=0
FAIL=0

assert_eq() {
  local label="$1" got="$2" want="$3"
  if [ "$got" = "$want" ]; then
    echo "  PASS: $label"
    PASS=$((PASS + 1))
  else
    echo "  FAIL: $label -- got='$got' want='$want'"
    FAIL=$((FAIL + 1))
  fi
}

assert_included() {
  local label="$1" f="$2"
  local to_field to_base included=1
  to_field="$(halt_gate_recipient "$f" || true)"
  if [ -n "$to_field" ]; then
    to_base="${to_field%%~*}"
    [ "$to_base" != "$RUNNING_BASE" ] && included=0
  fi
  assert_eq "$label (included=1)" "$included" "1"
}

assert_skipped() {
  local label="$1" f="$2"
  local to_field to_base skipped=0
  to_field="$(halt_gate_recipient "$f" || true)"
  if [ -n "$to_field" ]; then
    to_base="${to_field%%~*}"
    [ "$to_base" != "$RUNNING_BASE" ] && skipped=1
  fi
  assert_eq "$label (skipped=1)" "$skipped" "1"
}

# ---------------------------------------------------------------------------
# Case A -- message TO this agent (same serial, no tilde suffix)
# Expected: halt_gate_recipient returns matching serial -> INCLUDED -> gate TRIPS
# ---------------------------------------------------------------------------
CASE_A="$TMP/msg_case_a.md"
cat > "$CASE_A" << 'EOF'
# Message from 2.0.0_SA_COO
**To:** 0.7.0_AE_CloudOps
**Date:** 20260528T220000Z
**Subject:** [STOP] deploy blocked -- please hold

Hold the current apply. Escalation in progress.
EOF

echo ""
echo "=== Case A: message TO 0.7.0_AE_CloudOps (same serial) ==="
to_a="$(halt_gate_recipient "$CASE_A")"
echo "  halt_gate_recipient -> '$to_a'"
assert_eq "To: field parsed correctly" "$to_a" "0.7.0_AE_CloudOps"
assert_included "message is INCLUDED (gate TRIPS)" "$CASE_A"

# ---------------------------------------------------------------------------
# Case B -- ferry copy of a message TO a foreign tilde-lane serial
# Simulates LD-0099 ferry: broker strips ~B, deposits copy in AE base inbox.
# Expected: halt_gate_recipient returns foreign base -> SKIPPED -> gate PASSES
# ---------------------------------------------------------------------------
CASE_B="$TMP/msg_case_b.md"
cat > "$CASE_B" << 'EOF'
# Message from 2.0.0_SA_COO
**To:** 0.4.2_RD_AdvisorIntelligence~B
**Date:** 20260528T202516Z
**Subject:** [STOP] MDPF_SCOPED.S1 GO -- RD~B deploy

Ferry copy. Intended for RD~B. Should not trip AE 0.7 gate.
EOF

echo ""
echo "=== Case B: ferry copy TO 0.4.2_RD_AdvisorIntelligence~B (foreign tilde-lane) ==="
to_b="$(halt_gate_recipient "$CASE_B")"
echo "  halt_gate_recipient -> '$to_b'"
assert_eq "To: field parsed correctly" "$to_b" "0.4.2_RD_AdvisorIntelligence~B"
to_b_base="${to_b%%~*}"
assert_eq "base-strip correct" "$to_b_base" "0.4.2_RD_AdvisorIntelligence"
assert_skipped "message is SKIPPED (gate PASSES)" "$CASE_B"

# ---------------------------------------------------------------------------
# Case C (fail-safe) -- message with NO **To:** header
# Expected: empty To: -> fail-safe -> INCLUDED (never drop unclassifiable message)
# ---------------------------------------------------------------------------
CASE_C="$TMP/msg_case_c.md"
cat > "$CASE_C" << 'EOF'
# Message from 0.0.0_AB_MSTR
**Date:** 20260528T193000Z
**Subject:** [STOP] urgent fabric pause

Older-format message without explicit To: header.
EOF

echo ""
echo "=== Case C: message with no To: header (fail-safe) ==="
to_c="$(halt_gate_recipient "$CASE_C" || true)"
echo "  halt_gate_recipient -> '$to_c'"
assert_eq "empty To: returned (fail-safe)" "$to_c" ""
assert_included "message INCLUDED when To: absent (fail-safe)" "$CASE_C"

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "=== RESULTS: $PASS PASS, $FAIL FAIL ==="
[ "$FAIL" -eq 0 ] && { echo "ALL PASS"; exit 0; } || { echo "FAILURES DETECTED"; exit 1; }
