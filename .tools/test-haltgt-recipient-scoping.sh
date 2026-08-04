#!/usr/bin/env bash
# =============================================================================
# test-haltgt-recipient-scoping.sh -- LD-0131 Layer 1 acceptance fixture
# =============================================================================
# CVO-mandated discrimination proof for the halt-gate-check.sh recipient-scoping
# filter (MSTR LD-0131 guardrail (c)): the gate must STILL hard-block a genuine
# same-serial [STOP], and must IGNORE a foreign-lane ferry copy that scattered
# into the running agent's inbox. Anti-over-scope: never suppress a same-base
# pending. Fail-safe: a message with no parseable To: is still surfaced.
#
# Sandboxed: all inbox/context/audit paths point at a temp dir; the real
# org/mcp/inbox + .comp-graph are never touched. Every run uses </dev/null.
# Git Bash 3.6.7-safe: bash/grep/sed/printf/mktemp only.
# =============================================================================
set -u
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GATE="$REPO/.tools/halt-gate-check.sh"
SBX="$(mktemp -d)"
trap 'rm -rf "$SBX"' EXIT

# Running agent for this fixture: a base serial (the scatter victim class).
SERIAL="0.1.0_DS_MarketIntelligence"
INBOX="$SBX/inbox"
CTX="$SBX/.agent_context"
AUDIT="$SBX/halt-gate-override-audit.log"
mkdir -p "$INBOX/$SERIAL/read"
printf 'SERIAL=%s\nTO_ID=TEST\n' "$SERIAL" > "$CTX"

# mkmsg <file> <sender> <to> <subject>
mkmsg() {
  printf '# Message from %s\n**To:** %s\n**Date:** 20260528T000000Z\n**Subject:** %s\n\nbody\n' \
    "$2" "$3" "$4" > "$INBOX/$SERIAL/$1"
}
mkmsg_noto() { # <file> <sender> <subject>  -- no To: line (fail-safe case)
  printf '# Message from %s\n**Date:** 20260528T000000Z\n**Subject:** %s\n\nbody\n' \
    "$2" "$3" > "$INBOX/$SERIAL/$1"
}
clear_inbox() { rm -f "$INBOX/$SERIAL"/*.md 2>/dev/null; }
run() { HALT_GATE_INBOX_ROOT="$INBOX" HALT_GATE_CONTEXT_FILE="$CTX" HALT_GATE_AUDIT_LOG="$AUDIT" \
        bash "$GATE" "recipient-scoping-test" </dev/null >"$SBX/out" 2>&1; echo $?; }

PASS=0; FAIL=0
check() { if [ "$2" = "$3" ]; then echo "  PASS: $1 (exit $3)"; PASS=$((PASS+1));
  else echo "  FAIL: $1 (expected $2, got $3)"; cat "$SBX/out"; FAIL=$((FAIL+1)); fi; }

echo "== MSTR Case 1 (guardrail i): genuine same-serial [STOP] -> MUST hard-block (exit 2) =="
clear_inbox
mkmsg "001_stop_mine.md" "2.0.0_SA_COO" "$SERIAL" "[STOP] hold all DS-MI deploys -- mid-apply"
rc=$(run); check "same-serial STOP hard-blocks" 2 "$rc"
grep -q "STOP-CLASS" "$SBX/out" && echo "  PASS: surfaced the STOP" || { echo "  FAIL: STOP not surfaced"; FAIL=$((FAIL+1)); }

echo "== MSTR Case 2 (the bug fix): foreign ~lane ferry copy -> MUST be ignored (exit 0 silent) =="
clear_inbox
mkmsg "002_ferry_foreign.md" "2.0.0_SA_COO" "0.4.2_RD_AdvisorIntelligence~B" "[GO] MDPF_SCOPED.S1 (FERRY -- scattered to wrong base inbox)"
rc=$(run); check "foreign ferry ignored" 0 "$rc"
[ -s "$SBX/out" ] && { echo "  FAIL: expected silent, got:"; cat "$SBX/out"; FAIL=$((FAIL+1)); } || echo "  PASS: silent (ignored)"

echo "== Case 3 (critical): foreign-lane [STOP] copy -> MUST NOT block this agent (exit 0) =="
clear_inbox
mkmsg "003_foreign_stop.md" "0.0.0_AB_MSTR" "1.2.0_SA_CL_CTO" "[STOP] CL-CTO hold -- not addressed to DS-MI"
rc=$(run); check "foreign-lane STOP does not block us" 0 "$rc"

echo "== Case 4 (anti-over-scope): same-base sibling ~lane message -> MUST surface (exit 1) =="
clear_inbox
mkmsg "004_sibling_lane.md" "2.0.0_SA_COO" "${SERIAL}~B" "routine -- addressed to my ~B lane"
rc=$(run); check "same-base sibling kept" 1 "$rc"

echo "== Case 5 (fail-safe): message with NO To: line -> MUST surface (exit 1), never silently dropped =="
clear_inbox
mkmsg_noto "005_no_to.md" "2.0.0_SA_COO" "legacy message, no To: field"
rc=$(run); check "no-To: fail-safe surfaces" 1 "$rc"

echo "== Case 6 (mixed): foreign ferry + genuine same-serial routine -> only mine counts (exit 1) =="
clear_inbox
mkmsg "006a_ferry.md" "2.0.0_SA_COO" "0.7.0_AE_CloudOps~B" "[GO] foreign -- must be ignored"
mkmsg "006b_mine.md" "2.0.0_SA_COO" "$SERIAL" "routine -- addressed to me"
rc=$(run); check "mixed: mine surfaces, foreign ignored" 1 "$rc"
grep -q "1 pending message" "$SBX/out" && echo "  PASS: exactly 1 pending (foreign filtered)" || { echo "  FAIL: pending count wrong"; cat "$SBX/out"; FAIL=$((FAIL+1)); }

echo
echo "RESULT: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
