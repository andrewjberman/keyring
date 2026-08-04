#!/usr/bin/env bash
# =============================================================================
# test-rcg-manifest-check.sh -- exercise matrix for the rcg/ folder-contract gate.
#
# Usage: bash .tools/git-hooks/test-rcg-manifest-check.sh
#
# Every case runs against a THROWAWAY index (GIT_INDEX_FILE) or the documented
# env seam -- the real index is never written, no commit is made, no audit log is
# touched, and rcg/ (a live single-writer lane) is never modified. Safe to run at
# any time, including while another agent is working in rcg/.
#
# WHY THIS FILE EXISTS: the gate's whole job is to DENY. A gate is only known to
# deny if you have watched it deny -- "it did not fire" and "it cannot fire" are
# the same observation from outside. T1 and T4 are the mutants; T2 and T3 are the
# controls that stop a gate from passing by being uniformly broken or uniformly
# loud.
#
# NOTE ON T5: the append-only tamper path is NOT exercised here. The checker
# compares the WORKING COPY of rcg/ledger/*.jsonl, so exercising it requires
# mutating a live append-only ledger. Deliberately out of scope -- recorded rather
# than silently omitted. Prior evidence the path fires: 7390a1a33d.
#
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only.
# Author: 1.0.0_SA_CTO~B, 2026-08-04 (NFRA_REPOCOHERENCEGRAPH D-0001 item 3).
# =============================================================================
set -u
WS="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$WS" ] || { echo "ERROR: not in a git repo" >&2; exit 1; }
GATE="$WS/.tools/git-hooks/rcg-manifest-check.sh"
[ -f "$GATE" ] || { echo "ERROR: gate not found at $GATE" >&2; exit 1; }
TMP="$(mktemp -d)"
PASS=0; FAIL=0

report() { # $1=name $2=expected_rc $3=actual_rc $4=expected_substring $5=output
  local ok=1
  [ "$2" = "$3" ] || ok=0
  # -F (fixed string) is LOAD-BEARING: the expected substrings contain
  # [brackets], which grep otherwise parses as a character class. Without it,
  # 'DENY [not-in-manifest]' errors "Invalid range end" and reports FAIL against
  # a CORRECT gate -- the harness's pattern failing, misread as the subject
  # failing. (Measured on this file's first run.) Same class as CLAUDE.md's
  # "put the control on the RETRIEVAL, not the pattern".
  if [ -n "$4" ]; then printf '%s' "$5" | grep -qF -- "$4" || ok=0; fi
  if [ "$ok" = 1 ]; then PASS=$((PASS+1)); echo "  PASS  $1  (rc=$3)"
  else FAIL=$((FAIL+1)); echo "  FAIL  $1  (expected rc=$2 got rc=$3; wanted: '$4')"
       printf '%s\n' "$5" | sed 's/^/          | /'; fi
}

echo "T1 NEGATIVE CONTROL -- out-of-manifest file staged under rcg/ MUST DENY"
cp "$WS/.git/index" "$TMP/idx1"
printf 'gate probe -- transient, removed by this test\n' > "$WS/rcg/__gate_probe_test.txt"
GIT_INDEX_FILE="$TMP/idx1" git -C "$WS" add -f rcg/__gate_probe_test.txt 2>/dev/null
OUT="$(cd "$WS" && env -u OWNED_PATHS_STAGED_FILES GIT_INDEX_FILE="$TMP/idx1" bash "$GATE" 2>&1)"; RC=$?
rm -f "$WS/rcg/__gate_probe_test.txt"
report "out-of-manifest file denied" 1 "$RC" "DENY [not-in-manifest]" "$OUT"

echo "T2 POSITIVE CONTROL -- legitimate in-manifest rcg/ path MUST PASS"
OUT="$(cd "$WS" && OWNED_PATHS_STAGED_FILES="rcg/MANIFEST.yaml" bash "$GATE" 2>&1)"; RC=$?
report "in-manifest path passes" 0 "$RC" "CLEAN" "$OUT"

echo "T3 NOT-APPLICABLE -- a commit not touching rcg/ MUST no-op silently"
OUT="$(cd "$WS" && OWNED_PATHS_STAGED_FILES="docs/architecture/SOMETHING.md" bash "$GATE" 2>&1)"; RC=$?
report "non-rcg commit is a silent no-op" 0 "$RC" "" "$OUT"
[ -n "$OUT" ] && { echo "  FAIL  expected NO output on the not-applicable path"; FAIL=$((FAIL+1)); }

echo "T4 FAIL-CLOSED -- rcg/ staged but checker ABSENT MUST DENY, not skip"
mkdir -p "$TMP/fakeroot"
OUT="$(PRECOMP_REPO_ROOT="$TMP/fakeroot" OWNED_PATHS_STAGED_FILES="rcg/ledger/LABELS.jsonl" bash "$GATE" 2>&1)"; RC=$?
report "missing checker denies" 1 "$RC" "BLOCKED" "$OUT"

rm -rf "$TMP"
echo ""
echo "RESULT: $PASS passed, $FAIL failed  (T5 append-only tamper: NOT RUN, see header)"
[ "$FAIL" -eq 0 ] || exit 1
