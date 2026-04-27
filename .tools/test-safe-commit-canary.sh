#!/usr/bin/env bash
# Canary tests for .tools/safe-commit.sh (ADHC_OWNPTH.007).
#
# Uses a temporary throwaway repo so the live workspace's shared index
# is never touched. Verifies AC2 / AC3 / AC4 from the TO.
#
# Run: bash .tools/test-safe-commit-canary.sh

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SAFE="$REPO_ROOT/.tools/safe-commit.sh"
TMPDIR="$(mktemp -d -t safe-commit-canary-XXXXXX)"

cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT

cd "$TMPDIR"
git init -q
git config user.email "canary@test"
git config user.name "canary"
git config commit.gpgsign false
git config core.autocrlf false

# Seed a base commit
echo "v0" > a.txt
echo "v0" > b.txt
git add a.txt b.txt
git commit -q -m "seed"

PASS=0
FAIL=0
note_pass() { PASS=$((PASS + 1)); echo "  PASS: $1"; }
note_fail() { FAIL=$((FAIL + 1)); echo "  FAIL: $1"; }

echo "=== Canary A: match case (staged == pathspec, exit 0, commit created) ==="
echo "vA" > a.txt
git add a.txt
BEFORE_HEAD="$(git rev-parse HEAD)"
if SAFE_COMMIT_AUDIT_LOG="$TMPDIR/audit.log" bash "$SAFE" \
    --author "canary <c@c>" -m "canary A" -- a.txt > /tmp/canary_a.out 2>&1; then
  note_pass "exit 0 as expected"
else
  note_fail "expected exit 0, got $?"
  cat /tmp/canary_a.out
fi
AFTER_HEAD="$(git rev-parse HEAD)"
if [ "$BEFORE_HEAD" != "$AFTER_HEAD" ]; then
  note_pass "HEAD advanced ($BEFORE_HEAD -> $AFTER_HEAD)"
else
  note_fail "HEAD did NOT advance"
fi
SUBJECT="$(git log -1 --pretty=%s)"
if [ "$SUBJECT" = "canary A" ]; then
  note_pass "commit subject matches"
else
  note_fail "expected 'canary A', got '$SUBJECT'"
fi
if [ ! -f "$TMPDIR/audit.log" ] || [ ! -s "$TMPDIR/audit.log" ]; then
  note_pass "no audit log entry on clean commit"
else
  note_fail "audit log unexpectedly written: $(cat $TMPDIR/audit.log)"
fi
echo ""

echo "=== Canary B: mismatch case (extra staged, exit 1, commit aborted) ==="
echo "vB1" > a.txt
echo "vB2" > b.txt
git add a.txt b.txt
BEFORE_HEAD="$(git rev-parse HEAD)"
set +e
SAFE_COMMIT_AUDIT_LOG="$TMPDIR/audit.log" bash "$SAFE" \
    --author "canary <c@c>" -m "canary B" -- a.txt > /tmp/canary_b.out 2>&1
RC=$?
set -e
if [ "$RC" -eq 1 ]; then
  note_pass "exit 1 as expected"
else
  note_fail "expected exit 1, got $RC"
fi
AFTER_HEAD="$(git rev-parse HEAD)"
if [ "$BEFORE_HEAD" = "$AFTER_HEAD" ]; then
  note_pass "HEAD unchanged (commit aborted)"
else
  note_fail "HEAD advanced unexpectedly"
fi
if grep -q "Contaminating staged files" /tmp/canary_b.out && grep -q "  b.txt" /tmp/canary_b.out; then
  note_pass "ERROR message lists contaminating file (b.txt)"
else
  note_fail "ERROR message missing or did not list b.txt"
  cat /tmp/canary_b.out
fi
# Audit log should still NOT have a FORCE-BYPASS entry from this run
if [ ! -f "$TMPDIR/audit.log" ] || ! grep -q "FORCE-BYPASS" "$TMPDIR/audit.log"; then
  note_pass "no FORCE-BYPASS entry written on plain abort"
else
  note_fail "audit log unexpectedly contains FORCE-BYPASS"
fi
echo ""

echo "=== Canary C: --force bypass (extra staged, exit 0, audit logged) ==="
# Index still has a.txt + b.txt staged from B
BEFORE_HEAD="$(git rev-parse HEAD)"
if SAFE_COMMIT_AUDIT_LOG="$TMPDIR/audit.log" bash "$SAFE" --force \
    --author "canary <c@c>" -m "canary C" -- a.txt > /tmp/canary_c.out 2>&1; then
  note_pass "exit 0 with --force as expected"
else
  note_fail "expected exit 0, got $?"
  cat /tmp/canary_c.out
fi
AFTER_HEAD="$(git rev-parse HEAD)"
if [ "$BEFORE_HEAD" != "$AFTER_HEAD" ]; then
  note_pass "HEAD advanced under --force"
else
  note_fail "HEAD did NOT advance under --force"
fi
# Verify only a.txt was committed (NOT b.txt) -- --only scoping
LAST_FILES="$(git log -1 --name-only --pretty=format: | grep -v '^$' | sort | tr '\n' ',' || true)"
if [ "$LAST_FILES" = "a.txt," ]; then
  note_pass "commit scoped to a.txt only (b.txt remains staged for next run)"
else
  note_fail "expected only a.txt, got: $LAST_FILES"
fi
if grep -q "FORCE-BYPASS  canary  1" "$TMPDIR/audit.log"; then
  note_pass "FORCE-BYPASS audit entry written with agent + count"
  echo "    audit line: $(grep FORCE-BYPASS $TMPDIR/audit.log)"
else
  note_fail "audit log missing FORCE-BYPASS entry"
  cat "$TMPDIR/audit.log" 2>/dev/null || echo "(no audit log)"
fi
echo ""

echo "=== Canary D: missing pathspec (exit 2) ==="
set +e
bash "$SAFE" --author "canary <c@c>" -m "no paths" > /tmp/canary_d.out 2>&1
RC=$?
set -e
if [ "$RC" -eq 2 ]; then
  note_pass "exit 2 as expected (pathspec required)"
else
  note_fail "expected exit 2, got $RC"
fi
if grep -q "pathspec required" /tmp/canary_d.out; then
  note_pass "ERROR message present"
else
  note_fail "missing 'pathspec required' message"
fi
echo ""

echo "=== Summary ==="
echo "PASS: $PASS"
echo "FAIL: $FAIL"
if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
exit 0
