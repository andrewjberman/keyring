#!/usr/bin/env bash
# =============================================================================
# halt-gate-ld0131-test.sh -- halt-gate battery: LD-0131 recipient scoping + the list/stat race
# =============================================================================
# Six arms + one mutant control, all HERMETIC (a temp repo root, inbox root and session
# serial file; the live inbox and the live session are never read).
#
#   Scenario 1: only foreign ferry (To: RD~B) in inbox            -> exit 0 (gate passes)
#   Scenario 2: foreign ferry + same-serial [STOP]                 -> exit 2 (hard block)
#   Scenario 3: foreign ferry + routine same-serial msg            -> exit 1 (surfaced, unacked)
#   Arm 4 (RACE): the listing names a file that no longer exists  -> exit 0 (not a pending message)
#   Arm 5 (RACE guardrail): vanished file + real same-serial STOP -> exit 2 (the STOP still blocks)
#   Arm 6 (RACE guardrail): vanished file + routine same-serial   -> exit 1 (the routine still surfaces)
#   MUTANT: a copy of the gate with the RACE-GUARD line deleted must FAIL arm 4 (exit 1),
#           proving arm 4 discriminates the fix rather than passing vacuously.
#
# HISTORY OF THIS FILE'S OWN VALIDITY (1.0.0_SA_CTO~Z, 2026-09-03): the 2026-05-28 version set
# CLAUDE_CODE_SESSION_ID="" and identified the gate through HALT_GATE_CONTEXT_FILE -- the
# .comp-graph/.agent_context fallback the gate REMOVED on 2026-07-13 (fail-closed identity).
# From that day every scenario returned exit 3 (NO-SERIAL) and the battery read 0/3, while three
# further gate edits landed (07-13, 07-25, 07-30) with no battery that could see them. Identity is
# now the gate's real primary: a session-keyed serial file under the (overridden) repo root, plus
# an agent home folder for the serial's base so halt_gate_validate_serial accepts it.
#
# Arms 4-6 run the gate SOURCED (its documented library mode) and redefine halt_gate_unread_for so
# the listing can name a path that does not exist -- the shape 0.0.0_AB_MSTR~Z observed at
# 08:12:32Z 2026-09-03 when the inbox watcher's mv raced the gate's stat and a push was refused
# with "(age unknown)" on a message that had already been delivered to read/.
#
# Usage:  bash .tools/halt-gate-ld0131-test.sh
# Exit 0: every arm and the mutant control passed
# Exit 1: at least one failed
# =============================================================================
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HALT_GATE="$REPO_ROOT/.tools/halt-gate-check.sh"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

TEST_SERIAL="0.7.0_AE_CloudOps"
TEST_SID="halt-gate-battery-session"
FAKE_ROOT="$TMP/repo"
INBOX_ROOT="$FAKE_ROOT/org/mcp/inbox"
mkdir -p "$INBOX_ROOT/$TEST_SERIAL" "$FAKE_ROOT/org/mcp/sessions" "$FAKE_ROOT/org/tier2_senior/$TEST_SERIAL"
printf '%s\n' "$TEST_SERIAL" > "$FAKE_ROOT/org/mcp/sessions/$TEST_SID.serial"

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

# Executed mode (scenarios 1-3): the gate run as a program under the hermetic identity.
run_gate() {
  CLAUDE_CODE_SESSION_ID="$TEST_SID" \
  HALT_GATE_REPO_ROOT="$FAKE_ROOT" \
  HALT_GATE_INBOX_ROOT="$INBOX_ROOT" \
  HALT_GATE_AUDIT_LOG="$TMP/audit.log" \
  bash "$HALT_GATE" 2>/dev/null
  echo $?
}

# Sourced mode (arms 4-6 + mutant): source a gate file, replace the lister with one that returns
# the given paths (one per argument), run halt_gate_check, print its exit code. Runs in a subshell
# so the redefinition never leaks. $1 = gate file; $2.. = paths the listing should name.
run_gate_sourced() {
  local gate_file="$1"; shift
  local -a listed=("$@")
  (
    export CLAUDE_CODE_SESSION_ID="$TEST_SID" HALT_GATE_REPO_ROOT="$FAKE_ROOT" \
           HALT_GATE_INBOX_ROOT="$INBOX_ROOT" HALT_GATE_AUDIT_LOG="$TMP/audit.log"
    # shellcheck disable=SC1090
    . "$gate_file"
    halt_gate_unread_for() { printf '%s\n' "${listed[@]}"; }
    halt_gate_check "battery" 2>/dev/null
    echo $?
  )
}

# ===========================================================================
# Scenario 1: only a foreign ferry in inbox (To: RD~B)
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
# Arms 4-6: the list/stat race -- a listed file that no longer exists
# ===========================================================================
VANISHED="$INBOX_ROOT/$TEST_SERIAL/20260903T081226Z_already_moved_to_read.md"
rm -f "$VANISHED"
STOP_FILE="$INBOX_ROOT/$TEST_SERIAL/same_serial_stop.md"
ROUTINE_FILE="$INBOX_ROOT/$TEST_SERIAL/same_serial_routine.md"
write_msg "same_serial_stop.md" "$TEST_SERIAL" "[STOP] deploy blocked" "Real STOP."

echo ""
echo "=== Arm 4: the listing names ONLY a vanished file -> exit 0 (not a pending message) ==="
got4=$(run_gate_sourced "$HALT_GATE" "$VANISHED")
assert_exit "a vanished file is skipped, gate passes" "$got4" "0"

echo ""
echo "=== Arm 5: vanished file + real same-serial [STOP] -> exit 2 (guardrail: the STOP still blocks) ==="
got5=$(run_gate_sourced "$HALT_GATE" "$VANISHED" "$STOP_FILE")
assert_exit "the STOP beside a vanished file still hard-blocks" "$got5" "2"

echo ""
echo "=== Arm 6: vanished file + routine same-serial msg -> exit 1 (guardrail: the routine still surfaces) ==="
got6=$(run_gate_sourced "$HALT_GATE" "$VANISHED" "$ROUTINE_FILE")
assert_exit "the routine message beside a vanished file still surfaces" "$got6" "1"

# ===========================================================================
# MUTANT CONTROL: the gate with its RACE-GUARD line deleted must FAIL arm 4
# ===========================================================================
MUTANT="$TMP/halt-gate-mutant.sh"
sed '/HALT-GATE-RACE-GUARD/d' "$HALT_GATE" > "$MUTANT"
if cmp -s "$HALT_GATE" "$MUTANT"; then
  echo "  FAIL: mutant control -- the RACE-GUARD marker is absent from the gate, nothing was deleted"
  FAIL=$((FAIL + 1))
else
  echo ""
  echo "=== Mutant control: the gate WITHOUT the race guard on arm 4 -> exit 1 (the arm discriminates) ==="
  gotm=$(run_gate_sourced "$MUTANT" "$VANISHED")
  assert_exit "mutant (guard deleted) counts the vanished file as pending" "$gotm" "1"
fi

# ===========================================================================
# Summary
# ===========================================================================
echo ""
echo "=== RESULTS: $PASS PASS, $FAIL FAIL (denominator $((PASS + FAIL))) ==="
[ "$FAIL" -eq 0 ] && { echo "ALL PASS"; exit 0; } || { echo "FAILURES DETECTED"; exit 1; }
